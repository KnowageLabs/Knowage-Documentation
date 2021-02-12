Requirements
====================

Before going into details on Knowage installation, it is necessary to check if certain requirements are satisfied. We start to distinguish between the certified environments and the compatible ones. The first are those where check tests take place. The latter are those environments technically compatibles but where integration tests are not executed.

Operating systems
------------------

The following Operating Systems (OS) are those ones which suit with Knowage platform.

.. table:: Certified environments
   :widths: auto

   +---------------------------+-------------+
   |    Certified Environments               |
   +===========================+=============+
   |    **Operating System**   | **Version** |
   +---------------------------+-------------+
   |    CentOS                 | 7 64-bit    |
   +---------------------------+-------------+
   |    Windows                | 7 , 10      |
   +---------------------------+-------------+

.. table:: Compatible environments
    :widths: auto

    +-----------------------------+-------------+
    |    Compatible Environments                |
    +=============================+=============+
    |    **Operating System**     | **Version** |
    +-----------------------------+-------------+
    |    RHEL Red Hat Enterprise  | 7           |
    +-----------------------------+-------------+
    |    Ubuntu                   | 18 LST      |
    +-----------------------------+-------------+
    |    Windows server           | 2012, 2008  |
    +-----------------------------+-------------+

Disk usage
--------------------

The Knowage installation requires 2 GB of available space on file system. This space does not include the space relative to the data and the metadata storage.

Java environment
--------------------

The enviroment in which Knowage will be installed must include a JDK 1.8 installation. Be sure that the JDK component is successfully installed and that the environment variable ``JAVA_HOME`` is properly configured. The steps to configure it depend on the OS.
Knowage 7 is compatible with Open JDK 1.8.

Linux
~~~~~~~~~~~~

Define the ``JAVA_HOME`` variable inside the users’ file ``.bash_profile`` used in the installation process

.. code-block:: shell
	:caption: Instructions to set the JAVA_HOME variable for Linux environment.

	export JAVA_HOME=<root path of the Java installation>
	export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_60/
	export PATH=$JAVA_HOME/bin:$PATH

Windows
~~~~~~~~~~~~

Define the ``JAVA_HOME`` variable and ``PATH`` in the section "Environment variables" which can be reached from the "System".

   .. figure:: media/image7.png

      Setting the path for the JAVA_HOME variable for Windows

Application server
---------------------

The following lists the supported application servers:

.. table:: Supported application servers
    :widths: auto

    +---------------------+------------------------+-------------+
    |    **Support type** | **Application Server** | **Version** |
    +=====================+========================+=============+
    |    Certified        | Apache Tomcat          | 8.5.57      |
    +---------------------+------------------------+-------------+

For each application server installation please refer to its official documentation.

Tomcat 8.5
~~~~~~~~~~~~

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

Tomcat on Linux
^^^^^^^^^^^^^^^

It is recommended to create a proper user for the execution of Tomcat. We state the main steps to follow for this purpose.

- Create the Tomcat user.

.. code-block:: shell

	useradd -m tomcat
	passwd <password for the tomcat user>

- Install the Tomcat using the Tomcat user. Remeber to define the ``TOMCAT_HOME`` variable.

.. code-block:: shell

	export TOMCAT_HOME=<path of the installation Tomcat root folder >

- Be sure that the Tomcat uses the JDK 1.8: usually the Tomcat settings are defined in the ``TOMCAT_HOME/bin/setenv.sh`` file, therefore if the ``TOMCAT_HOME/bin/setenv.sh`` file does not exit, the user must create it and insert it in the content as shown below. Note that ``CATALINA_PID`` contains the ID of the Tomcat process and it kills the process if needed.

.. code-block:: sh

	export CATALINA_PID=<root folder of the Tomcat installation>/logs/tomcat-knowage.pid
	export JAVA_HOME=<root folder of the JDK 1.8 installation>

- Modify the ``TOMCAT_HOME/bin/shutdown.sh`` file to force the shut down of the application in case of hanging:

.. code-block:: sh

	exec "$PRGDIR"/"$EXECUTABLE" stop -f "$@"

Tomcat on Windows
^^^^^^^^^^^^^^^^^

It is recommended to install Tomcat as a service. Documentation is available at https://tomcat.apache.org/tomcat-8.5-doc/windows-service-howto.html.

Database schema for metadata
----------------------------

Knowage uses a schema to manage metadata, that is all those information required for its operation. These concern the configuration, the users and the analytical documents. It is possible to use the following DBMSs for the creation of this schema.

.. table:: Exploitable DBMSs for the metadata schema creation
    :widths: auto

    +---------------------+---------------+------------------+
    | **Support Type**    | **DBMS**      | **Version**      |
    +=====================+===============+==================+
    |    Certified        | Oracle        | 8, 9, 10, 11, 12 |
    +---------------------+---------------+------------------+
    |    Certified        | MySql         | 5.7, 8           |
    +---------------------+---------------+------------------+
    |    Certified        | PostgreSQL    | 8.2, 9.1, 12.3   |
    +---------------------+---------------+------------------+
    |    Certified        | MariaDB       | 10.1, 10.2, 10.3 |
    +---------------------+---------------+------------------+

Therefore, a schema must be available. It can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *metadata DB* in the following. Observe that Knowage includes all the DDL for table creation.

Database schema for data
-------------------------

A schema for data must be also available. It can be queried through Knowage and can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *data DB* in the following.

NodeJS requirements
-------------------------

.. important::
	**Enterprise Edition only**

	NodeJS is required only for Enterprise Edition.

Knowage includes some NodeJS scripts that need to be executed with NodeJS 8 or greater: see `NodeJS official documentation <https://nodejs.org/en/download/package-manager>`_ for the installation process.

CentOS
~~~~~~~~~~~~

In CentOS you need to erase older versions of NodeJS, if present:

.. code-block:: sh
	:caption: Command to erase older versions of NodeJS

	yum erase -y nodejs

Then you need to clear YUM cache and update all local packages:

.. code-block:: sh
	:caption: Cache clearing and system updating

	yum clean all
	yum update -y

Next you can install the official repository of NodeJS:

.. code-block:: sh
	:caption: Installation of the repository of NodeJS

	curl -sL https://rpm.nodesource.com/setup_8.x | bash -

.. important::
 	If you are behind a corporate proxy, you would need to set ``http_proxy`` and/or ``https_proxy``.

Finally you can install NodeJS:

.. code-block:: sh
	:caption: Installation of NodeJS

	yum install -y nodejs

Ubuntu
~~~~~~~~~~~~

In Ubuntu you need to erase older versions of NodeJS, if present:

.. code-block:: sh
	:caption: Command to erase older versions of NodeJS

	apt-get remove nodejs

Then you need to clear APT cache and update all local packages:

.. code-block:: sh
	:caption: Cache clearing and system updating

	apt-get update
	apt-get upgrade -y

Next you can install the official repository of NodeJS:

.. code-block:: sh
	:caption: Installation of the repository of NodeJS

	curl -sL https://deb.nodesource.com/setup_8.x | bash -

.. important::
         If you are behind a corporate proxy, you would need to set ``http_proxy`` and/or ``https_proxy``.

Finally you can install NodeJS:

.. code-block:: sh
	:caption: Installation of NodeJS

	apt-get install -y nodejs

Chromium requirements
-------------------------
.. important::

	**Enterprise Edition only**

	Chromium is required only for Enterprise Edition.

Knowage provides a distribution of Chromium for its functionalities but some other dependencies are needed. In Linux distribution you need to install following Chromium dependencies:

.. code-block:: sh
	:caption: Installation of Chromium dependencies

	# For CentOS
	yum install -y at-spi2-atk cups-libs expat glib2 glibc.i686 glibc libcanberra-gtk3 libgcc libstdc++ libX11 libXScrnSaver minizip nspr nss-mdns nss-util nss policycoreutils-python policycoreutils zlib

	# For Ubuntu
	apt-get install -y libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libgcc1 libgdk-pixbuf2.0-0 libglib2.0-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libuuid1 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxtst6 bash


Support to non-latin languages
------------------------------

Knowage does some of its job at server side and it could need support for non-latin languages. Some operating systems don't provides support to non-latin language by default: see the official documentation to enable the support to those languages.

For example, to install non-latin languages fonts you could use:

.. code-block:: sh
	:caption: Installation of non-latin language fonts

	# For CentOS 7
	yum groupinstall fonts

	# For Ubuntu
	sudo apt-get install language-pack-ja
	sudo apt-get install japan*

	sudo apt-get install language-pack-zh*
	sudo apt-get install chinese*

	sudo apt-get install language-pack-ko
	sudo apt-get install korean*

	etc...
