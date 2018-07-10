 
Prerequisite
====================
 
Before going into details on Knowage installation, it is necessary to check if certain prerequisites are satisfied. We start to distinguish between the certified environments and the compatible ones. The first are those where check tests take place. The latter are those environments technically compatibles but where integration tests are not executed.

Operating systems
------------------

The Operating Systems (OS) showed in :numref:'certenvironments' and :numref:'compenvironments' are those ones which suit with Knowage platform.

.. _certenvironments:
.. table:: Certified environments
   :widths: auto
   
   +---------------------------+-------------+
   |    Certified Environments               |
   +===========================+=============+
   |    **Operating System**   | **Version** |
   +---------------------------+-------------+
   |    CentOS                 | 6 64-bit    |
   +---------------------------+-------------+
   | Red Hat Enterprise RHEL   | 6.4 64-bit  |
   +---------------------------+-------------+ 
   |    Windows                | 7,10        |
   +---------------------------+-------------+   
   |    Windows Server         | 2008, 2012  |
   +---------------------------+-------------+


Disk usage
--------------------

The Knowage installation requires 2 GB of free space on file system. This memory does not include the space relative to the data and the metadata storage.

JDK version
--------------------

The enviroment in which Knowage will be installed must include a 1.8 JDK installation. Be sure that the JDK component is successfully installed and that the environment variable JAVA_HOME is properly configured.

**[LINUX]** Define the JAVA_HOME variable inside the users’ file .bash_profile used in the installation process (root and tomcat, as shown in the following :numref:`instructionstosetthejava`):

.. _instructionstosetthejava:
.. code-block:: bash
        :linenos:
        :caption: Instructions to set the JAVA_HOME variable for Linux environment.
        
        export JAVA_HOME=<root path of the Java installation>                 
        export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_60/                            
        export PATH=$JAVA_HOME/bin:$PATH                                      

**[WIN]** Define the JAVA_HOME variable and PATH in the section "Environment variables“ which can be reached from the ”System“. You can refer to :numref:`settingthepathfor`.
 
.. _settingthepathfor:
.. figure:: media/image7.png
  
   Setting the path for the JAVA_HOME variable for Windows.
   
Application server
---------------------
The following :numref:`supportedapp` displays the compatibility with the supported application servers:

.. _supportedapp:
.. table:: Supported application server
    :widths: auto
    
    +---------------------+------------------------+-------------+
    |    **Support type** | **Application Server** | **Version** |
    +=====================+========================+=============+
    |    Certified        | Apache Tomcat          | 7.0.65      |
    +---------------------+------------------------+-------------+
    |                     | JBoss EAP              | 6           |
    +---------------------+------------------------+-------------+

    
**N.B. JBoss support will be available on Q4 2018**

For each application server installation please refer to each official user guide.

JBoss Enterprise Application Platform (EAP) 6
---------------------------------------------

In the following we will refer to the JBoss installation folder as JBOSS_HOME.

**[LINUX]** It is recommended to create a proper user for the execution of JBoss. We state the main steps to reach this purpose.
   
- Create the JBoss user.

.. code-block:: bash
        :linenos:

        useradd -m jboss                                                         
        passwd <password for the jboss user> 

- Install the JBoss using the JBoss user, remeber to define the JBOSS_HOME variable.

.. code-block:: bash
        :linenos:

        export JBOSS_HOME=<path of the installation JBoss root folder > 

- Be sure that the JBoss uses the JDK 1.8: usually the JBoss settings are defined in the JBOSS_HOME/bin/run.conf.sh file, therefore if the JBOSS_HOME/bin/run.conf.sh file does not exit, the user must create it and insert it in the content as shown below:

.. code-block:: bash
        :linenos:

        export JAVA_HOME=<JDK 1.8 installation root folder> 

**[WIN]** It is recommended to install JBoss as a service, using the dedicated user guide available on the Red Hat web site http://www.redhat.com


Tomcat 7
---------

In the following we will refer to Tomcat installation folder as TOMCAT_HOME.

**[LINUX]** It is recommended to create a proper user for the execution of Tomcat. We state the main steps to follow for this purpose.

- Create the Tomcat user.

.. code-block:: bash
        :linenos:

        useradd -m tomcat                     
        passwd <password for the tomcat user> 

- Install the Tomcat using the Tomcat user. Remeber to define the TOMCAT_HOME variable.

.. code-block:: bash
        :linenos:

        export TOMCAT_HOME=<path of the installation Tomcat root folder >

- Be sure that the Tomcat uses the JDK 1.7 o 1.8: usually the Tomcat settings are defined in the TOMCAT_HOME/bin/setenv.sh file, therefore if the TOMCAT_HOME/bin/setenv.sh file does not exit, the user must create it and insert it in the content as shown below. Note that CATALINA_PID contains the ID of the Tomcat process and it kills the process if needed.

.. code-block:: bash
        :linenos:

        export CATALINA_PID=<root folder of the Tomcat installation>/logs/tomcat7.
        pid export JAVA_HOME=<root folder of the JDK 1.8 installation>                  


**Remark.** Modify the TOMCAT_HOME/bin/shutdown.sh file to force the shut down of the application in case of hanging:

.. code-block:: bash
        :linenos:

        exec "$PRGDIR"/"$EXECUTABLE" stop -f "$@" 

**[WIN]** It is recommended to install Tomcat as a service using the installer available on the Apache web site http://www.apache.org.

 
Database schema for metadata
----------------------------

Knowage uses a schema to manage metadata, that is all those information required for its operation. These concern the configuration, the users and the analytical documents. It is possible to use the DBMSs listed in :numref:`exploitabledbms` for the creation of this schema.

.. _exploitabledbms:
.. table:: Exploitable DBMSs for the metadata schema creation
    :widths: auto

    +---------------------+---------------+--------------+
    |    **Support Type** | **DBMS**      | **Version**  |
    +=====================+===============+==============+
    |    Certified        | Oracle        | 8,9,10,11,12 |
    +---------------------+---------------+--------------+
    |    Certified        | MySql         | 5.2,5.5,5.6  |
    +---------------------+---------------+--------------+
    |    Certified        | PostgreSQL    | 8.2, 9.1     |
    +---------------------+---------------+--------------+
    |    Certified        | MariaDB       |10.1,10.2,10.3|
    +---------------------+---------------+--------------+


Therefore, a schema must be available. It can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called "metadata DB” in the following. Observe that Knowage includes all the DDL for table creation.


Database schema for data.
-------------------------

A schema for data must be also available. It can be queried through Knowage and can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called "data DB” in the following .
To correctly use the Knowage data mining engine it is necessary to install R, R Studio and rJava on the target server. Please refer to  `http://cranr-project.org/. <http://cranr-project.org/>`__


R
-----------

Be sure to use the following versions:

- version 3.2.2 for R,
- version 0.99 for R Studio,
- version 0.98 for rJava (library to connect Knowage to the R server)
