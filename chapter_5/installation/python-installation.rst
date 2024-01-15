Python Engine
================

These functionalities use a Python standalone webservice, which allows to submit widgets and datasets scripts and get result from a Python environment already installed on the machine where the webservice runs. For this reason, Python environments need to be installed and configured on the same machine of Knowage server or even on a remote one, and the Python webservice has to be running **inside that same environment**. 
This implies that, in order to use this functionalities, you have to install Python properly (depending on the OS) on the same machine where the service will be running. You can find all information about Python installation at https://www.python.org. The official supported version is Python >=3.6.8, but we recommend to use 3.7.x whenever it's possible.

Install knowage-python webservice
---------------------------------

The knowage-python package contains the source code of the webservice that has to be installed and run on the server. You can download it via ``pip`` with the command:

.. code-block:: bash
    
	pip install knowage-python=={knowage_version_number}
	
or simply you can find it in the Knowage-Server github repository under the Knowage-Python folder.

If you downloaded knowage-python via pip, use "pip show knowage-python" to find the pip package installation location. Then copy the source file from this folder to your own custom folder such as ``/opt/knowagepython``.

You will now have to create a file called ``hmackey`` that contains the value of the HMACkey in plaintext, and place it inside the ``<KNOWAGE_PYTHON_HOME>/`` folder. It must be the same value specified in the server.xml file.


Run knowage-python webservice
-----------------------------

Once you have installed all the requirements, you need to get the python-webservice running. In order to do so, you can rely on a WSGI Server.
If you are working on a UNIX environment, take a look at gunicorn (https://gunicorn.org/).
The service leverages on Flask, for deployment in any other environment take a look at the official documentation (https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).
**The entry point for the application is <KNOWAGE_PYTHON_HOME>/knowage-python.py and the default port is 5000.**

To install GUNICORN you can use:

.. code-block:: bash

	pip3 install gunicorn greenlet eventlet gevent wheel
	pip3 install gunicorn eventlet gevent gthread setproctitle
	pip3 install flask flask_cors bokeh pandas
	pip3 install matplotlib
	pip3 install PyJWT
	pip3 install pandas


.. important::
     **Webservice permissions**

     The knowage-python webservice must have the OS rights to read/write in its own folders.

Following you can find an example that shows you how to run knowage-python with gunicorn.
First you need to create a configuration file called ``gunicorn.conf.py`` and place it under ``<KNOWAGE_PYTHON_HOME>/src`` folder.

.. code-block:: python

	import multiprocessing

	bind = "0.0.0.0:5000"
	workers = multiprocessing.cpu_count() * 2 + 1
	timeout = 30
	keepalive = 2
	user = <user>
	group = <group>
	loglevel = 'info'
	accesslog = '/var/log/gunicorn-access.log' 
	errorlog = '/var/log/gunicorn-error.log' 
	access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

Then to start the service run the following command inside the ``<KNOWAGE_PYTHON_HOME>/`` folder.

.. code-block:: bash
    /usr/local/bin/gunicorn -c file:gunicorn.conf.py knowage-python
	/usr/local/bin/gunicorn --certfile cert.pem -c file:gunicorn.conf.py knowage-python

You can create service to start/stop Gunicorn.

Configure Knowage to enable Python/R functionalities
-----------------------------------------------------

From the Knowage interface you can now enable the Python/R functionalities. 

Go to the ``Roles management`` section, in the *Authorizations* tab under *Widgets* check the ``Edit Python Scripts`` option.
Now you will be able to see the Python and R Dataset and Widget among the list of available ones.

Go to the ``Configuration management`` section, and create new variables of category ``PYTHON_CONFIGURATION`` and ``R_CONFIGURATION``. 
For the label you can use ``python.default.environment.url``. 
The value of this variables will specify the addresses of the Python and R webservices (es. ``python.webservice.address.com/domain``).
Now you will be able to see the addresses of the so configured environments when creating a Dataset or a Widget.
