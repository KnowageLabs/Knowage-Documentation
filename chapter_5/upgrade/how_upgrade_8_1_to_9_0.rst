How to upgrade KNOWAGE 8.1 to 9.0
########################################################################################################################

This section describes the main steps to manually update an existing Knowage installation.

Pay attention to the fact that Knowage versions' names adhere to the Semantic Versioning 2.0.0.

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

The upgrade of the following Knowage components is generally needed:

-  the applications that reside within ``TOMCAT_HOME/webapps`` folder: all ``knowage*.war`` files (knowage.war, knowagebirtreportengine.war, knowagecockpitengine.war, ...)

-  the Knowage metadata database, where information about analyses, datasets, etc ... is stored.

- JDK version to 17

The latter component must be upgraded in case you are moving from a different major or minor version (for example: from 8.0.1 to 8.1.2), but there is no need in case you are upgrading to a new patch release of the same major/minor family (for example: from 8.0.2 to 8.0.4).

Preliminary operations
------------------------------------------------------------------------------------------------------------------------

Before starting upgrade procedure, you have to:

-  download latest packages from the OW2 repository: base location is https://release.ow2.org/knowage/, you'll find a folder for each version, each folder contains: ``Applications`` with the relevant war files, and ``Database scripts`` with the SQL scripts (distributed as zip files) to upgrade Knowage metadata database for supported RDBMS;

-  make a backup copy of the old web applications that reside within: ``TOMCAT_HOME/webapps``;

-  make a backup copy of Knowage metadata database.


Upgrade operations
------------------------------------------------------------------------------------------------------------------------

To upgrade Knowage installation follow these steps:

-  stop Apache Tomcat service;

-  upgrade the Knowage metadata database by executing the following SQL scripts:

   .. code-block:: bash
    :linenos:

    ORA_upgradescript_8.1_to_8.2.sql
    ORA_upgradescript_8.2_to_9.0.sql



-  move all ``knowage*.war`` files and all the ``knowage*`` directories from ``TOMCAT_HOME/webapps`` into a backup directory;

-  delete the following directories: ``TOMCAT_HOME/temp`` and ``TOMCAT_HOME/work``;

-  copy and paste all the new ``knowage*.war`` packages within ``TOMCAT_HOME/webapps`` directory;

-  Make sure you have set the ``symmetric_encryption_key`` system property in file ``TOMCAT_HOME/bin/setenv.sh`` or ``TOMCAT_HOME/bin/setenv.bat``; that property is required to encrypt/decrypt the JDBC data source passwords:

.. code-block:: bash

  export JAVA_OPTS="$JAVA_OPTS -Dsymmetric_encryption_key=<any random string>"
  
.. code-block:: bash

   set JAVA_OPTS=%JAVA_OPTS% -Dsymmetric_encryption_key=<any random string>

-  Make sure you have set the ``hazelcast.ignoreXxeProtectionFailures`` system property in file ``TOMCAT_HOME/bin/setenv.sh`` or ``TOMCAT_HOME/bin/setenv.bat``;

.. code-block:: bash

  export JAVA_OPTS="$JAVA_OPTS  -Dhazelcast.ignoreXxeProtectionFailures=true"
  
.. code-block:: bash

   set JAVA_OPTS=%JAVA_OPTS%  -Dhazelcast.ignoreXxeProtectionFailures=true

- In case you defined contexts with relevant files inside ``TOMCAT_HOME/conf/Catalina/localhost`` 

- Quartz configuration file for cluster configuration ( in case of any cluster only ):  by default it is not enabled on released packages therefore you need to restore it in case you have a clustered installation: add these lines in ``TOMCAT_HOME/webapps/knowage/WEB-INF/classes/quartz.properties`` (or restore them from the backup copy):

- upgrade JDV version to 17