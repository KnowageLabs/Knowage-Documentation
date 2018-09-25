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
   |    CentOS                 | 6 64-bit    |
   +---------------------------+-------------+
   |    Windows                | 7           |
   +---------------------------+-------------+

.. table:: Compatible environments
    :widths: auto
   
    +-----------------------------+-------------+
    |    Compatible Environments                |
    +=============================+=============+
    |    **Operating System**     | **Version** |
    +-----------------------------+-------------+
    |    RHEL Red Hat Enterprise  | 6.4         |
    +-----------------------------+-------------+
    |    Ubuntu                   |16 LST,18 LST|
    +-----------------------------+-------------+    
    |    Windows server           | 2012, 2008  |
    +-----------------------------+-------------+
   
Disk usage
--------------------

The Knowage installation requires 2 GB of free space on file system. This space does not include the space relative to the data and the metadata storage.

Java environment
--------------------

The enviroment in which Knowage will be installed must include a JDK 1.8 installation. Be sure that the JDK component is successfully installed and that the environment variable ``JAVA_HOME`` is properly configured. The steps to configure it depend on the OS.

Linux
~~~~~~~~~~~~

Define the ``JAVA_HOME`` variable inside the users’ file ``.bash_profile`` used in the installation process

   .. code-block:: bash
           :linenos:
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

.. table:: Supported application server
    :widths: auto
    
    +---------------------+------------------------+-------------+
    |    **Support type** | **Application Server** | **Version** |
    +=====================+========================+=============+
    |    Certified        | Apache Tomcat          | 7.0.65      |
    +---------------------+------------------------+-------------+

.. important::
         **Roadmap**
         
         JBoss support will be available on Q4 2018

For each application server installation please refer to the official documnetation.

Tomcat 7
~~~~~~~~~~~~

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

Linux
^^^^^^^^^^

It is recommended to create a proper user for the execution of Tomcat. We state the main steps to follow for this purpose.

- Create the Tomcat user.

   .. code-block:: bash
           :linenos:

           useradd -m tomcat                     
           passwd <password for the tomcat user> 

- Install the Tomcat using the Tomcat user. Remeber to define the ``TOMCAT_HOME`` variable.

   .. code-block:: bash
           :linenos:

           export TOMCAT_HOME=<path of the installation Tomcat root folder >

- Be sure that the Tomcat uses the JDK 1.8: usually the Tomcat settings are defined in the ``TOMCAT_HOME/bin/setenv.sh`` file, therefore if the ``TOMCAT_HOME/bin/setenv.sh`` file does not exit, the user must create it and insert it in the content as shown below. Note that ``CATALINA_PID`` contains the ID of the Tomcat process and it kills the process if needed.

   .. code-block:: bash
           :linenos:

           export CATALINA_PID=<root folder of the Tomcat installation>/logs/tomcat7.
           pid export JAVA_HOME=<root folder of the JDK 1.8 installation>                  

- Modify the ``TOMCAT_HOME/bin/shutdown.sh`` file to force the shut down of the application in case of hanging:

   .. code-block:: bash
           :linenos:

           exec "$PRGDIR"/"$EXECUTABLE" stop -f "$@" 

Windows
^^^^^^^^^^

It is recommended to install Tomcat as a service. Documentation is available at https://tomcat.apache.org/tomcat-7.0-doc/windows-service-howto.html.

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
    |    Certified        | MySql         | 5.2, 5.5, 5.6    |
    +---------------------+---------------+------------------+
    |    Certified        | PostgreSQL    | 8.2, 9.1         |
    +---------------------+---------------+------------------+
    |    Certified        | MariaDB       | 10.1, 10.2, 10.3 |
    +---------------------+---------------+------------------+

Therefore, a schema must be available. It can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *metadata DB* in the following. Observe that Knowage includes all the DDL for table creation.

Database schema for data
-------------------------

A schema for data must be also available. It can be queried through Knowage and can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *data DB* in the following.

SlimerJS requirements
-------------------------

Knowage includes a standalone edition of SlimerJS 0.9 to export some contents to PDF and image files. Usually SlimerJS runs out-of-the-box on Windows, but requires OS-dependent libraries on Unix-like operating systems.

- In order to fulfill all **SlimerJS requirements** please refer to its official documentation at https://docs.slimerjs.org/0.9/installation.html#requirements.

- **Xvfb** may be required on Unix-like operating systems if no suitable X display server is available; install it with package manager.

Troubleshooting missing requirements may be difficult on Unix-like operating systems. Executing SlimerJS manually with **debug option** may help to investigate further:

.. code-block:: bash
        :caption: Executing SlimerJS with debug option via Xvfb
 
        xvfb-run ./slimerjs --debug=yes
