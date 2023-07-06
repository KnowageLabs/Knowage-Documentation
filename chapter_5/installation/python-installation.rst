Python Engine
================

These functionalities use a Python standalone webservice, which allows to submit widgets and datasets scripts and get result from a Python environment already installed on the machine where the webservice runs. For this reason, Python environments need to be installed and configured on the same machine of Knowage server or even on a remote one, and the Python webservice has to be running **inside that same environment**. 
This implies that, in order to use this functionalities, you have to install Python properly (depending on the OS) on the same machine where the service will be running. You can find all information about Python installation at https://www.python.org. The official supported version is Python >=3.8.

Install knowage-python webservice
---------------------------------

The knowage-python package contains the source code of the webservice that has to be installed and run on the server. You can download it via ``pip`` with the command:

.. code-block:: bash

    pip install knowage-python=={knowage_version_number}
	
or simply you can find it in the Knowage-Server GitHub repository under the Knowage-Python folder.

If you downloaded knowage-python via pip, use "pip show knowage-python" to find the pip package installation location. Then copy the source file from this folder to your own custom folder such as ``/opt/knowagepython``.

You will now have to create a file called ``hmackey`` that contains the value of the HMACkey in plaintext, and place it inside the ``<KNOWAGE_PYTHON_HOME>/src/app`` folder. It must be the same value specified in ``TOMCAT_HOME/conf/server.xml`` file.

Run knowage-python webservice
-----------------------------

Once you have installed all the requirements, you need to get the python-webservice running. The Python service for KNOWAGE is a Flask application: please take a look at `the official documentation <https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment>`_. In order to do so, you should rely on a WSGI Server.

On Linux with Gunicorn
~~~~~~~~~~~~~~~~~~~~~~

If you are working on a Linux environment, take a look at `Gunicorn <https://gunicorn.org/>`_.

**The entry point for the application is <KNOWAGE_PYTHON_HOME>/src/knowage-python.py and the default port is 5000.**

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

Then to start the service run the following command inside the ``<KNOWAGE_PYTHON_HOME>/src/app`` folder.

.. code-block:: bash

    /usr/local/bin/gunicorn -c file:gunicorn.conf.py knowage-python

	/usr/local/bin/gunicorn --certfile cert.pem -c file:gunicorn.conf.py knowage-python

You can now create a service to start/stop Gunicorn: see your operating system documentation for that.

On Windows with Waitress
~~~~~~~~~~~~~~~~~~~~~~~~

If you are working on a Windows environment, take a look at `Waitress <https://docs.pylonsproject.org/projects/waitress>`_.

Create a ``waitress_server.py`` in ``<KNOWAGE_PYTHON_HOME>/src`` folder with the following content:

.. code-block:: python

    import multiprocessing

	from waitress import serve
	import importlib

	knowage = importlib.import_module("knowage-python")

	serve(knowage.application,
		channel_timeout=30,
		host='0.0.0.0',
		port=5000,
		threads=multiprocessing.cpu_count() * 2 + 1
	)

Then run:

.. code-block:: shell

    python waitress_server.py


Configure Knowage to enable Python/R functionalities
-----------------------------------------------------

From the Knowage interface you can now enable the Python/R functionalities. 

Go to the ``Roles management`` section, in the *Authorizations* tab under *Widgets* check the ``Edit Python Scripts`` option.
Now you will be able to see the Python and R Dataset and Widget among the list of available ones.

Go to the ``Configuration management`` section, and create new variables of category ``PYTHON_CONFIGURATION`` and ``R_CONFIGURATION``. 
For the label you can use ``python.default.environment.url``. 
The value of this variables will specify the addresses of the Python and R webservices (es. ``python.webservice.address.com/domain``).
Now you will be able to see the addresses of the so configured environments when creating a Dataset or a Widget.
