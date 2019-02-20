How to upgrade to the latest version
==========================

This section describes the main steps to manually update an existing Knowage installation, on top of the certified Apache Tomcat server, to the latest available version. 

Pay attention to the fact that Knowage versions' names adhere to the Semantic Versioning 2.0.0.

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

The upgrade of both Knowage components is generally needed:

-  the applications that reside within ``TOMCAT_HOME/webapps`` folder: all ``knowage*.war`` files (knowage.war, knowagebirtreportengine.war, knowagecockpitengine.war, ...)

-  the Knowage metadata database, where configuration information is stored, in case you are upgrading to a different major or minor version.


Preliminary operations
------------------

Before starting upgrade procedure, you have to:

-  download latest packages from the OW2 repository: base location is https://release.ow2.org/knowage/, you'll find a folder for each version, each folder contains: ``Applications`` with the relevant war files, and ``Database scripts`` with the SQL scripts (distributed as zip files) to upgrade Knowage metadata database for supported RDBMS;

-  make a backup copy of the old web applications that reside within: ``TOMCAT_HOME/webapps``;

-  make a backup copy of Knowage metadata database.


Upgrade operations
------------------

To upgrade Knowage installation follow these steps:

-  stop Apache Tomcat service;

-  upgrade the Knowage metadata database by executing the SQL scripts. Each SQL script is conceived for upgrading a Knowage <major.minor> version into the next one, therefore you need to execute all scripts between your current <major.minor> version to the latest one. As an example, suppose RDBMS is Oracle, your current Knowage version is 6.0.x and you want to upgrade into Knowage 6.3.x, then you need to execute the following scripts:

   .. code-block:: bash
    :linenos:

    ORA_upgradescript_6.0_to_6.1.sql	
    ORA_upgradescript_6.1_to_6.2.sql
    ORA_upgradescript_6.2_to_6.3.sql
	
   .. note::
    **Moving into a newest patch version within the same <major.minor> family**
	In case you are moving into a newest patch version that belongs to the same <major.minor> family (for example from Knowage 6.2.0 to 6.2.4) there is no need to execute any SQL script.
		   
-  delete all ``knowage*.war`` files and all the ``knowage*`` directories from ``TOMCAT_HOME/webapps``;

-  delete the following directories: ``TOMCAT_HOME/temp`` and ``TOMCAT_HOME/work``;

-  copy and paste all the ``knowage*.war`` files within ``TOMCAT_HOME/webapps`` directory;

-  start Apache Tomcat service, wait until Apache Tomcat is started and then stop it again in order to change some configuration files;

-  for Knowage metadata database dialect, check that the right dialect has been set inside hibernate.cfg.xml files: the ``hibernate.dialect`` property should match your RDBMS for Knowage metadata database. Admissible dialects are:

   .. code-block:: bash
	 
    org.hibernate.dialect.MySQLDialect
    org.hibernate.dialect.PostgreSQLDialect
    org.hibernate.dialect.Oracle9Dialect
	
-  list of hibernate.cfg.xml files to check follows:

   .. code-block:: bash

    TOMCAT_HOME/webapps/knowage/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagecockpitengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagedataminingengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagegeoreportengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagekpiengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagemeta/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagesvgviewerengine/WEB-INF/classes/hibernate.cfg.xml

-  check Quartz scheduler engine configuration within file ``TOMCAT_HOME/webapps/knowage/WEB-INF/classes/quartz.properties``: it is essential to set the property ``org.quartz.jobStore.driverDelegateClass`` with the right value, according to the metadata database in use. Admissible values are:
   
   .. code-block:: jproperties
	          
	 # Mysql delegate class 
	 org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.StdJDBCDelegate          
	 # Postgres delegate class                                                                     
	 #org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.PostgreSQLDelegate      
	 # Oracle delegate class                                                                       
	 #org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.oracle.OracleDelegate
	 
-  restore the Quartz cluster modality, in case Knowage is installed within a cluster: add these lines:
   
   .. code-block:: jproperties
	
    org.quartz.jobStore.isClustered = true
    org.quartz.jobStore.clusterCheckinInterval = 20000
    org.quartz.scheduler.instanceId = AUTO
    org.quartz.scheduler.instanceName = RHECMClusteredSchedule

-  restore all ``TOMCAT_HOME/webapps/knowage*/META-INF/context.xml`` files from backup copy of previous applications;

-  start Apache Tomcat again.