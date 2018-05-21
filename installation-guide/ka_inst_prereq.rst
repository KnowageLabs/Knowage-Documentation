 
Prerequisite
====================
 
Before going into details on Knowage installation, it is necessary to check if certain prerequisites are satisfied. We start to distinguish between the certified environments and the compatible ones. The first are those where check tests take place. The latter are those environments technically compatibles but where integration tests are not executed.

Operation systems
------------------

The Operation Systems (OS) showed in Table 3.1 and 3.2 are those ones which suit with Knowage platform.

+---------------------------+-------------+
|    Certified Environments               |
+===========================+=============+
|    **Operative System**   | **Version** |
+---------------------------+-------------+
|    CentOS                 | 6 64-bit    |
+---------------------------+-------------+
|    Windows                | 7           |
+---------------------------+-------------+
   Table 3.1: Certified Environments.

+-----------------------------+-------------+
|    Compatible Environments                |
+=============================+=============+
|    **Operative System**     | **Version** |
+-----------------------------+-------------+
|    RHEL Read Hat Enterprise | 6.4         |
+-----------------------------+-------------+
|    Windows server           | 2012, 2008  |
+-----------------------------+-------------+
   Table 3.2: Compatible Environments.
   
Disk usage
--------------------

The Knowage installation requires 2 GB of free space on file system. This memory does not include the space relative to the data and the metadata storage.

JDK version
--------------------

The enviroment in which Knowage will be installed must include a 1.7 or 1.8 JDK installation. Be sure that the JDK component is successfully installed and that the environment variable JAVA_HOME is properly configured.

|image1| Define the JAVA_HOME variable inside the users’ file .bash_profile used in the installation process (root and tomcat, as shown in the following Code 3.1):

+-----------------------------------------------------------------------+
| export JAVA_HOME=<root path of the Java installation>                 |
| export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_60/                            |
| export PATH=$JAVA_HOME/bin:$PATH                                      |
+-----------------------------------------------------------------------+

Code 3.1: Instructions to set the JAVA_HOME variable for Linux environment.

   |image2| Define the JAVA_HOME variable and PATH in the section "Environment variables“ which can be reached from the ”System“. You can refer to Figure 3.1.

   |image3| 

Figure 3.1: Setting the path for the JAVA_HOME variable for Windows.
   

Application server
---------------------
The following Table 3.3 displays the compatibility with the supported application servers:

+---------------------+------------------------+-------------+
|    **Support type** | **Application Server** | **Version** |
+=====================+========================+=============+
|    Certified        | Apache Tomcat          | 7           |
+---------------------+------------------------+-------------+
|    Certified        | JBoss EAP              | 6           |
+---------------------+------------------------+-------------+
|    Compatible       | Jboss Wildfly          |             |
+---------------------+------------------------+-------------+
   Table 3.3: Supported application server.

For each application server installation please refer to each official user guide.

JBoss Enterprise Application Platform (EAP) 6
-----------------------

In the following we will refer to the JBoss installation folder as JBOSS_HOME.

|image4|It is recommended to create a proper user for the execution of JBoss. We state the main steps to reach this purpose.
   

-Create the JBoss user.

+--------------------------------------+
| useradd -m jboss                     |
|                                      |
| passwd <password for the jboss user> |
+--------------------------------------+



-Install the JBoss using the JBoss user, remeber to define the JBOSS_HOME variable.

+-----------------------------------------------------------------+
| export JBOSS_HOME=<path of the installation JBoss root folder > |
+-----------------------------------------------------------------+


- Be sure that the JBoss uses the JDK 1.7 o 1.8: usually the JBoss settings are defined in the JBOSS_HOME/bin/run.conf.sh file, therefore if the JBOSS_HOME/bin/run.conf.sh file does not exit, the user must create it and insert it in the content as shown in Code 3.6:

+-----------------------------------------------------+
| export JAVA_HOME=<JDK 1.8 installation root folder> |
+-----------------------------------------------------+

   |image5| It is recommended to install JBoss as a service, using the
   dedicated user guide available on the Red Hat web site
   `www.redhat.com/en. <http://www.redhat.com/en>`__


Tomcat 7
------------------

In the following we will refer to Tomcat installation folder as TOMCAT_HOME.

|image6|It is recommended to create a proper user for the execution of Tomcat. We state the main steps to follow for this purpose.

-Create the Tomcat user.

+---------------------------------------+
| useradd -m tomcat                     |
|                                       |
| passwd <password for the tomcat user> |
+---------------------------------------+


-Install the Tomcat using the Tomcat user. Remeber to define the TOMCAT_HOME variable.

+-------------------------------------------------------------------+
| export TOMCAT_HOME=<path of the installation Tomcat root folder > |
+-------------------------------------------------------------------+

-Be sure that the Tomcat uses the JDK 1.7 o 1.8: usually the Tomcat settings are defined in the TOMCAT_HOME/bin/setenv.sh file, therefore if the TOMCAT_HOME/bin/setenv.sh file does not exit, the user must create it and insert it in the content as shown in Code 3.6. Note that CATALINA_PID contains the ID of the Tomcat process and it kills the process if needed.

+-----------------------------------------------------------------------------+
| export CATALINA_PID=<root folder of the Tomcat installation>/logs/tomcat7.  |
| pid                                                                         |
| export JAVA_HOME=<root folder of the JDK 1.8 installation>                  |
+-----------------------------------------------------------------------------+

   **Remark.** Modify the TOMCAT_HOME/bin/shutdown.sh file to force the
   shut down of the application in case of hanging:

+-------------------------------------------+
| exec "$PRGDIR"/"$EXECUTABLE" stop -f "$@" |
+-------------------------------------------+

|image7|It is recommended to install Tomcat as a service using the installer available on the Apache web site httpd.apache.org/.

 
 Database schema for metadata
---------------------

Knowage uses a schema to manage metadata, that is all those information required for its operation. These concern the configuration, the users and the analytical documents. It is possible to use the DBMSs listed in Table 3.4 for the creation of this schema.

+---------------------+---------------+--------------+
|    **Support Type** | **DBMS**      | **Version**  |
+=====================+===============+==============+
|    Certified        | Oracle        | 8,9,10,11,12 |
+---------------------+---------------+--------------+
|    Certified        | MySql         | 5.1          |
+---------------------+---------------+--------------+
|    Certified        | PostgreSQL    | 8.2          |
+---------------------+---------------+--------------+
|    Certified        | MS Sql Server | 2012         |
+---------------------+---------------+--------------+
|    Certified        | Ingres        | II           |
+---------------------+---------------+--------------+
|    Certified        | MySql         | 5.5          |
+---------------------+---------------+--------------+
|    Certified        | MariaDB       |              |
+---------------------+---------------+--------------+
|    Certified        | PostgreSQL    | 9.1          |
+---------------------+---------------+--------------+

Table 3.4: Exploitable DBMSs for the metadata schema creation.

Therefore, a schema must be available. It can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called "metadata DB” in the following. Observe that Knowage includes all the DDL for table creation.


Database schema for data.
---------------------

A schema for data must be also available. It can be queried through Knowage and can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called "data DB” in the following .
To correctly use the Knowage data mining engine it is necessary to install R, R Studio and rJava on the target server. Please refer to  `http://cranr-project.org/. <http://cranr-project.org/>`__


R
-----------

Be sure to use the following versions:

-version 3.2.2 for R,

-version 0.99 for R Studio,

-version 0.98 for rJava (library to connect Knowage to the R server)


