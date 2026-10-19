Manual installation
===================

Prepare JDK 17, Tomcat 9, a metadata database and a cache database as described
in :doc:`/chapter_5/requirements`. Obtain all application packages from the
same 9.1.0 distribution; see :doc:`software_release`.

Metadata initialization
-----------------------

Create an empty schema and run the creation and Quartz scripts matching its
DBMS from the v9.1.0 source tree. Inspect the supplied scripts and their
execution order before running them. Assign the application database account
the privileges required by those scripts and the application's runtime work.

For an existing schema, use :doc:`/chapter_5/how_upgrade` instead of initialization.

Tomcat and JNDI resources
-------------------------

.. include:: ka_inst_man_tomcat.rst

Deploy the applications
-----------------------

With Tomcat stopped, place ``knowage.war``, ``knowage-api.war``,
``knowage-vue.war`` and the required engine WARs in ``TOMCAT_HOME/webapps``.
Configure the JNDI resources and links required by each deployed application.
Use its packaged ``META-INF/context.xml`` as the reference.

For example, the metadata and cache links use the following names:

.. code-block:: xml

   <ResourceLink global="jdbc/knowage" name="jdbc/knowage"
                 type="javax.sql.DataSource" />
   <ResourceLink global="jdbc/ds_cache" name="jdbc/ds_cache"
                 type="javax.sql.DataSource" />
   <ResourceLink global="resource_path" name="resource_path"
                 type="java.lang.String" />
   <ResourceLink global="hmacKey" name="hmacKey"
                 type="java.lang.String" />
   <ResourceLink global="service_url" name="service_url"
                 type="java.lang.String" />

Link your business data sources separately. Configure a persistent resources
directory, accessible to the Tomcat user, and keep authentication and service
URL settings consistent across the applications. Preserve the password
secrets and encryption keys across restarts and upgrades.

Where JDBC password encryption uses ``symmetric_encryption_key``, set the JVM
property in Tomcat's environment file:

.. code-block:: bash

   export JAVA_OPTS="$JAVA_OPTS -Dsymmetric_encryption_key=<deployment-specific-key>"

Use the Windows equivalent in ``setenv.bat`` for a Windows deployment.

Hibernate and Quartz
--------------------

Keep the defaults shipped with 9.1 unless the deployment requires an override.
Review the Hibernate and Quartz configuration for the DBMS in use. Quartz
settings are in ``knowage/WEB-INF/classes/quartz.properties`` after deployment.

For a cluster, configure the nodes consistently and assign unique automatic
instance identifiers, for example:

.. code-block:: properties

   org.quartz.jobStore.isClustered = true
   org.quartz.jobStore.clusterCheckinInterval = 20000
   org.quartz.scheduler.instanceId = AUTO
   org.quartz.scheduler.instanceName = KnowageClusteredSchedule

Coordinate cluster settings with the shared metadata database and cache.

Logging
-------

The 9.1 applications use Log4j 2 configuration in
``WEB-INF/classes/log4j2.xml``. Configure its appenders and log paths for the
deployment. The main application's supplied configuration writes tenant-specific
logs under ``${sys:catalina.base}/logs``. Ensure the Tomcat account can write to
the configured locations and configure retention for operational logs.

See :doc:`/chapter_5/server_settings` and :doc:`/chapter_4/log_manager`.

Optional export and Python services
-----------------------------------

Install the export service distributed for your edition and configure its
Node.js/Chromium runtime and script paths. Test the formats required by your
users. For Python datasets, functions and widgets, follow
:doc:`python-installation` and use the matching 9.1 package.

Optional Data Preparation
-------------------------

Data Preparation requires a configured Livy/Spark service and the corresponding
Knowage integration libraries. Keep their versions aligned with the supplied
integration package. Configure ``KNOWAGE.DATAPREP.LIVY_URL`` and the resources
path, then select a data source with **Use for data preparation** to store the
prepared data. Test a transformation and save a prepared dataset before exposing
the feature to authors.

.. figure:: /_static/screenshots/9.1/chapter-5-installation-manual-installation-9-1-data-preparation-source.png

   Selecting the data source used for prepared dataset output.

Start and verify
----------------

Start Tomcat, inspect the logs, sign in and test a dataset and a document with
an end-user role. Verify external authentication, parameter entry, exports and
a scheduled execution for the components enabled in your installation.
