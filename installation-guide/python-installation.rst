Python Engine
================

These functionalities use a Python standalone webservice, which allows to submit widgets and datasets scripts and get result from a Python environment already installed on the machine where the webservice runs. For this reason, Python environments need to be installed and configured on the same machine of Knowage server or even on a remote one, and the Python webservice has to be running **inside that same environment**. 
This implies that, in order to use this functionalities, you have to install Python properly (depending on the OS) on the same machine where the service will be running. You can find all information about Python installation at https://www.python.org. The official supported version is Python >=3.6.8, but we recommend to use 3.7.x whenever it's possible.

Install knowage-python webservice
---------------------------------

The knowage-python package contains the source code of the webservice that has to be installed and run on the server. You can download it via ``pip`` with the command:

.. code-block::
    
	pip install knowage-python==<knowage_version (ex: 7.2.2)>
	
or simply you can find it in the Knowage-Server github repository under the Knowage-Python folder.

You will now have to create the configuration for the webservice. This configuration will be contained inside a file called ``config.xml`` and placed inside the ``Knowage-Python/pythonwebservice/app`` folder.

The structure of the file will be as follows:

.. code-block:: xml
   :linenos:
   :caption: Example of a knowage-python webservice configuration file
    
	<data>
		<environment name="knowage-python">
			<hmackey>foobar123</hmackey>
			<knowageaddress>knowage.server.address.com</knowageaddress>
			<pythonaddress>python.webservice.address.com</pythonaddress>
			<bokehportsrange>57000-58000</bokehportsrange>
		</environment>
	</data>

*  ``hmackey`` : the Knowage HMAC key contained in the server.xml file,
*  ``knowageaddress`` : the address at which the python webservice can contact the Knowage server (the two entities can either be on the same machine or on different machines),
*  ``pythonaddress`` : the address of the current instance of Python (it is needed by the Knowage server to contact back the engine if needed),
*  ``bokehportsrange`` : the range of open ports upon which the service can dinamically instantiate Bokeh Servers.

Run knowage-python webservice
-----------------------------

Once you have installed all the requirements, you need to get the python-webservice running. In order to do so, you can rely on a WSGI Server.
If you are working on a UNIX environment, take a look at gunicorn (https://gunicorn.org/).
The service leverages on Flask, for deployment in any other environment take a look at the official documentation (https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).
**The entry point for the application is ``Knowage-Python/pythonwebservice/knowage-python.py`` and the default port is ``5000``.**

.. important::
     **Webservice permissions**

     The knowage-python webservice must have the rights to read/write in its own folders (pythonwebservice/*). 


Configure Knowage to enable Python/R functionalities
====================================================

From the Knowage interface you can now enable the Python/R functionalities. 

Go to the ``Roles management`` section, in the *Authorizations* tab under *Widgets* check the ``Edit Python Scripts`` option.
Now you will be able to see the Python and R Dataset and Widget among the list of available ones.

Go to the ``Configuration management`` section, and create new variables of category ``PYTHON_CONFIGURATION`` and ``R_CONFIGURATION``. The value of this variables will specify the addresses of the Python and R webservices (es. ``python.webservice.address.com/domain``).
Now you will be able to see the addresses of the so configured environments when creating a Dataset or a Widget.

**Be aware that depending on the architecture of your solution, you might have to define two different addresses for reaching the same instance of Python.**

*  One address is for reaching Python from the client (browser) and will be used when creating a widget,
*  One address is for reaching Python from the server (Knowage) and will be used when creating a Dataset.

