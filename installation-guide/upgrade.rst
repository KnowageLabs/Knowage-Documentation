How to upgrade to the latest version
==========================

This section describes the main steps to manually update an existing Knowage installation, on top of the certified Apache Tomcat server, to the latest available version.

Pay attention to the fact that Knowage versions' names adhere to the Semantic Versioning 2.0.0.

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

The upgrade of the following Knowage components is generally needed:

-  the applications that reside within ``TOMCAT_HOME/webapps`` folder: all ``knowage*.war`` files (knowage.war, knowagebirtreportengine.war, knowagecockpitengine.war, ...)

-  the Knowage metadata database, where information about analyses, datasets, etc ... is stored.

The latter component must be upgraded in case you are moving from a different major or minor version (for example: from 6.4.x to 7.2.y, or from 7.1.x to 7.2.y), but there is no need in case you are upgrading to a new patch release of the same major/minor family (for example: from 7.2.0 to 7.2.6, or from 7.2.6 to 7.2.13).

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
	In case you are moving into a newest patch version that belongs to the same <major.minor> family (for example from Knowage 7.2.0 to 7.2.6, or from 7.2.6 to 7.2.13) there is no need to execute any SQL script.

-  move all ``knowage*.war`` files and all the ``knowage*`` directories from ``TOMCAT_HOME/webapps`` into a backup directory;

-  delete the following directories: ``TOMCAT_HOME/temp`` and ``TOMCAT_HOME/work``;

-  copy and paste all the new ``knowage*.war`` packages within ``TOMCAT_HOME/webapps`` directory;

-  in case you are upgrading from a version prior to 7.2.0, create a file containing the password encryption secret (just a random text of any length). This is a security configuration, so don’t use short strings. **Do not distribute** it for any reason. Then update ``TOMCAT_HOME/conf/server.xml`` file by creating a new environment variable as shown below and set the value property as the complete path of the file with password encryption secret:

.. code-block:: xml

   <Environment name="password_encryption_secret" description="File for security encryption location"
      type="java.lang.String" value="${catalina.home}/conf/knowage.secret"/>


At this point, in some cases you need to deal with some configuration files, in particular when you modified the following files within the previous Knowage installation, then you need to restore those changes (after having unzipped the war files):

- context files ``TOMCAT_HOME/webapps/knowage*/META-INF/context.xml``: they contain links to resources such as datasource connections and environment variables; in case you modified them in order to add a new datasource, you need to restore the changes and check if links to environment variables defined in ``TOMCAT_HOME/conf/server.xml`` are all there. In case you defined contexts with relevant files inside ``TOMCAT_HOME/conf/Catalina/localhost`` and you are upgrading from a version prior to 7.2.0, then you need to add the link to the ``password_encryption_secret`` variable, since that was introduced by 7.2.0 version;

- Hibernate files: they contain the metadata database Hibernate dialect (the ``hibernate.dialect`` property): since versione 7.2.0, Knowage is able to autodetect the dialect by itself but, in case you customized it to a value other than ``org.hibernate.dialect.MySQLDialect`` or ``org.hibernate.dialect.PostgreSQLDialect`` or ``org.hibernate.dialect.Oracle9Dialect``, you have to restore your change: this is the list of Hibernate files to be checked:

   .. code-block:: bash

    TOMCAT_HOME/webapps/knowage/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagecockpitengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagedataminingengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagegeoreportengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagekpiengine/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagemeta/WEB-INF/classes/hibernate.cfg.xml
    TOMCAT_HOME/webapps/knowagesvgviewerengine/WEB-INF/classes/hibernate.cfg.xml

- Quartz configuration file for metadata database dialect and for cluster configuration (in case of any cluster): again, since versione 7.2.0, Knowage is able to autodetect the dialect by itself but, in case you customized the ``org.quartz.jobStore.driverDelegateClass`` property inside ``TOMCAT_HOME/webapps/knowage/WEB-INF/classes/quartz.properties`` to a value other than ``org.quartz.impl.jdbcjobstore.StdJDBCDelegate`` or  ``org.quartz.impl.jdbcjobstore.PostgreSQLDelegate`` or ``org.quartz.impl.jdbcjobstore.oracle.OracleDelegate``, you have to restore your change. Regarding cluster configuration, by default it is not enabled on released packages therefore you need to restore it in case you have a clustered installation: add these lines in ``TOMCAT_HOME/webapps/knowage/WEB-INF/classes/quartz.properties`` (or restore them from the backup copy):

   .. code-block:: jproperties

    org.quartz.jobStore.isClustered = true
    org.quartz.jobStore.clusterCheckinInterval = 20000
    org.quartz.scheduler.instanceId = AUTO
    org.quartz.scheduler.instanceName = RHECMClusteredSchedule


.. important::

	Since Knowage 7.2.0, the security level was highly increased. For this reason, users are requested to log in and change their password as a first step after upgrading.

To admin users: it is recommended to check which users didn't change the password and tell them to do it as soon as possible. Run the following query on the Knowage metadata database to extract the list of users who are still using the previous password encryption mechanism:

.. code-block:: SQL

  select * from SBI_USER where password like '#SHA#%' order by user_id;
