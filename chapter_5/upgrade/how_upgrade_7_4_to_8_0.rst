How to upgrade KNOWAGE 7.4 to 8.0
#############

This section describes the main steps to manually update an existing Knowage installation, on top of the certified Apache Tomcat server, to the latest available version. In case you are moving between 2 KNOWAGE versions with different certified Apache Tomcat servers, we recommend to follow all the instructions described on the manual installation section.

Pay attention to the fact that Knowage versions' names adhere to the Semantic Versioning 2.0.0.

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

The upgrade of the following Knowage components is generally needed:

-  the applications that reside within ``TOMCAT_HOME/webapps`` folder: all ``knowage*.war`` files (knowage.war, knowagebirtreportengine.war, knowagecockpitengine.war, ...)

-  the Knowage metadata database, where information about analyses, datasets, etc ... is stored.

The latter component must be upgraded in case you are moving from a different major or minor version (for example: from 6.4.x to 7.2.y, or from 7.1.x to 7.2.y), but there is no need in case you are upgrading to a new patch release of the same major/minor family (for example: from 7.2.0 to 7.2.6, or from 7.2.6 to 7.2.13).

Preliminary operations
-----------------------

Before starting upgrade procedure, you have to:

-  download latest packages from the OW2 repository: base location is https://release.ow2.org/knowage/, you'll find a folder for each version, each folder contains: ``Applications`` with the relevant war files, and ``Database scripts`` with the SQL scripts (distributed as zip files) to upgrade Knowage metadata database for supported RDBMS;

-  make a backup copy of the old web applications that reside within: ``TOMCAT_HOME/webapps``;

-  make a backup copy of Knowage metadata database.


Upgrade operations
------------------

To upgrade Knowage installation follow these steps:

-  stop Apache Tomcat service;

-  upgrade the Knowage metadata database by executing the following SQL scripts:

   .. code-block:: bash
    :linenos:

    ORA_upgradescript_7.4_to_8.0.sql

   .. note::
    **Moving into a newest patch version within the same <major.minor> family**
	In case you are moving into a newest patch version that belongs to the same <major.minor> family (for example from Knowage 7.2.0 to 7.2.6, or from 7.2.6 to 7.2.13) there is no need to execute any SQL script.

-  move all ``knowage*.war`` files and all the ``knowage*`` directories from ``TOMCAT_HOME/webapps`` into a backup directory;

-  delete the following directories: ``TOMCAT_HOME/temp`` and ``TOMCAT_HOME/work``;

-  copy and paste all the new ``knowage*.war`` packages within ``TOMCAT_HOME/webapps`` directory;

- In case you defined contexts with relevant files inside ``TOMCAT_HOME/conf/Catalina/localhost`` 

- Quartz configuration file for cluster configuration ( in case of any cluster only ):  by default it is not enabled on released packages therefore you need to restore it in case you have a clustered installation: add these lines in ``TOMCAT_HOME/webapps/knowage/WEB-INF/classes/quartz.properties`` (or restore them from the backup copy):

   .. code-block:: jproperties

    org.quartz.jobStore.isClustered = true
    org.quartz.jobStore.clusterCheckinInterval = 20000
    org.quartz.scheduler.instanceId = AUTO
    org.quartz.scheduler.instanceName = RHECMClusteredSchedule


