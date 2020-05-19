Python Widget and DataSet
================

These functionalities use a Python standalone webservice, which allows to submit widgets and datasets scripts and get result from a Python environment already installed on the machine where the webservice runs. For this reason, Python environments need to be installed and configured on the same machine of Knowage server or even on a remote one, and the Python webservice has to be running **inside that same environment**. 
This implies that, in order to use this functionalities, you have to install Python properly (depending on the OS) on the same machine where the service will be running. You can find all information about Python installation at https://www.python.org. The official supported version is Python 3.7, but other 3.x releases might work as well.

Install knowage-python webservice
-------------------

The knowage-python package contains the source code of the webservice that has to be installed and run on the server. You can download it via ``pip`` with the command:

.. code-block:: python
    
	pip install knowage-python
	
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
-------------------

Once you have installed all the requirements, you need to get the python-webservice running. In order to do so, you can rely on a WSGI Server.
If you are working on a UNIX environment, take a look at gunicorn (https://gunicorn.org/).
The service leverages on Flask, for deployment in any other environment take a look at the official documentation (https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).
**The entry point for the application is ``Knowage-Python/pythonwebservice/knowage-python.py`` and the default port is ``5000``.**

Configure Knowage to enable Python functionalities
-------------------

From the Knowage interface you can now enable the Python functionalities. 

Go to the ``Roles management`` section, in the *Authorizations* tab under *Widgets* check the ``Edit Python Scripts`` option.
Now you will be able to see the Python Dataset and Widget among the list of available ones.

Go to the ``Configuration management`` section, and create a new variable of category ``PYTHON_CONFIGURATION``. The value of this variable will specify the address of the python webservice (es. ``python.webservice.address.com/domain``)
Now you will be able to see the address of the so configured environment when creating a Dataset or a Widget.

**Be aware that depending on the architecture of your solution, you might have to define two different addresses for reaching the same instance of Python.**

*  One address is for reaching Python from the client (browser) and will be used when creating a widget,
*  One address is for reaching Python from the server (Knowage) and will be used when creating a Dataset.

DataMining Engine
================
 
The engine uses a Java/Python interface, which allows to submit scripts and get result from a Python environment already installed on the machine where the Datamining Engine runs. For this reason, Python environment need to be installed on the same machine of KnowAge server. This implies that, in order to run this engine, you have to install Python properly (depending on the OS) on the same machine where Knowage is installed. You can find all information about Python installation at https://www.python.org. Datamining engine only support Python 3 (the product has been tested with Python 3.4.0, but other 3.x releases are supported).
 
JPY installation
-------------------

JPY is a connector that make possible a bidirectional communication between Python and Java and its components must be installed on both sides (dataminingengine Java project and Python environment). Dataminingengine project is provided with ``jpy.jar`` that allows the communication, but this is not sufficient, because JPY must be installed on your Python environment. To do this you have to download the JPY source files and build them by yourself on your machine (unfortunately pre-built packages are not made available yet by JPY creators). All the detailed instructions to build and install JPY on your Python environment are described on the page http://jpy.readthedocs.org/en/stable/install.html. During the testing phase Python 3.4 and JPY 0.8 (stable version) have been used; here the version-specific installation steps are described. You will need:

*  Python 3.3 or higher (3.2 may work as well but is not tested),
*  Oracle JDK 7 or higher (JDK 6 may work as well),
*  Maven 3 or higher,
*  Microsoft Windows SDK 7.1 or higher If you build for a 32-bit Python, make sure to also install a 32-bit JDK. Accordingly, for a 64-bit Python, you will need a 64-bit JDK.

The Python setup tools ``distutils`` can make use of the command-line C/C++ compilers of the free Microsoft Windows SDK. These will by used by ``distutils`` if the ``DISTUTILS_USE_SDK`` environment variable is set. The compilers are made accessible via the command-line by using the setenv tool of the Windows SDK. In order to install the Windows SDK execute the following steps.

* If you already use Microsoft Visual C++ 2010, make sure to uninstall the x86 and amd64 compiler redistributables first. Otherwise the installation of the Windows SDK will definitely fail. This may also be applied to higher versions of Visual C++.
* Download and install Windows SDK 7.1.
* Download and install Windows SDK 7.1 SP1. Open the command-line and execute:
	* ``"C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\bin\\setenv" /x64 /release`` to prepare a build of the 64-bit version of jpy.
	* ``"C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\bin\\setenv" /x86 /release`` to prepare a build of the 32-bit version of jpy. 
   
Now set other environment variables:

.. code-block:: bash
    :linenos:

    SET DISTUTILS_USE_SDK=1
	SET JAVA_HOME=%JDK_HOME%
	SET PATH=%JDK_HOME%\jre\bin\server;%PATH%

Then, to actually build and test the jpy Python module use the following command: python setup.py install.
To use JPY you need to replace the jpyconfig.properties file on your project, with the one generated by the build process that is present in your JPY built folder ``jpy-master\build\lib.<SO-CPU-PYTHON_versions>``. Properties file to replace is located under ``knowagedataminingengine\src\``.

Datamining engine supports the use of all Python libraries: before import a library in your script install it on your native Python environment (for example using ``pip``). To use Python YOU NEED TO INSTALL the following libraries: ``matplotlib``, ``pandas``, ``numpy``, ``scipy``. You can install them using pip typing the following commands on your native Python console:

.. code-block:: python
    :linenos:
    
	pip install pandas
	pip install numpy 
	pip install scipy 
	pip install matplotlib.

.. code-block:: xml
        :linenos:
        :caption: Example of a Knowage Data Mining engine template which uses a Python script
    
	<?xml version="1.0" encoding="ISO-8859-15"?> 
    	<DATA_MINING>            
           <LANGUAGE name="Python"/>                                          
           <DATASETS>                                                         
               <DATASET name="df" readType="csv" type="file" label="HairEyeColor" canUpload="true"><![CDATA[sep=',']]>
               </DATASET>                                                         
           </DATASETS>                                                        
           <SCRIPTS>                                                          
               <SCRIPT name="test01" mode="auto" datasets="df" label="HairEyeColor" libraries="csv,os,pandas,numpy">              
                <![CDATA[ print(df.ix[0,0]) y=df.ix[0,0] ]]>                                                                
               </SCRIPT>                                                          
           </SCRIPTS>                                                         
           <COMMANDS>                                                         
			<COMMAND name="testcommand" scriptName="test01" label="test01"  mode=" auto">
                <OUTPUTS>                                                          
			<OUTPUT type="text" name="first_element" value="y" function=""  mode="manual" label="first_element"/>
                </OUTPUTS>                                                         
            </COMMAND>                                                         
           </COMMANDS>                                                        
    	</DATA_MINING>

Note that the ``LANGUAGE`` tag is used to specify the language to use: name=Python and name=R are supported. If the ``LANGUAGE`` tag is not present or name is not specified correctly, the default language is set to R.
