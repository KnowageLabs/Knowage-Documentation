Upgrade Knowage 9.0 to 9.1
==========================

Upgrade application packages and the metadata database together. This procedure
targets **9.1.0** and an installation already on the 9.0 metadata schema. For an
older installation, complete the preceding migrations first.

Prepare the upgrade
-------------------

1. Download the application archives from the
   `9.1.0 release <https://github.com/KnowageLabs/Knowage-Server/releases/tag/v9.1.0>`_.
   Match the artifacts to your edition and deployed engines.
2. Obtain the metadata migration scripts from the
   `same tag <https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowagedatabasescripts>`_.
3. Back up the metadata database, resources directory, application archives,
   Tomcat configuration, external services configuration and encryption keys.
   Verify that the backups can be restored together.
4. Rehearse the upgrade with a restored copy of the installation. Review
   database-specific syntax before applying its migration script.
5. Arrange a maintenance window and stop every node using the same metadata
   database, including scheduled activities.

Use JDK 17 and the Tomcat 9 deployment configuration described in
:doc:`/chapter_5/requirements`. Retain your current encryption keys so stored
credentials remain readable.

Migrate the metadata database
-----------------------------

Run **one** of the following scripts, according to your database. Paths are
relative to ``knowagedatabasescripts`` in the v9.1.0 source tree.

.. list-table:: 9.0 to 9.1 migration scripts
   :header-rows: 1
   :widths: 20 80

   * - Database
     - Script
   * - MySQL / MariaDB
     - ``mysql/mysql-dbupgradescript-9.0_to_9.1/MySQL_upgradescript_9.0_to_9.1.sql``
   * - PostgreSQL
     - ``postgres/postgres-dbupgradescript-9.0_to_9.1/PG_upgradescript_9.0_to_9.1.sql``
   * - Oracle
     - ``oracle/oracle-dbupgradescript-9.0_to_9.1/ORA_upgradescript_9.0_to_9.1.sql``

These scripts introduce home-page configuration tables, the business-model
``IS_FOR_AI`` flag and the analytical-driver ``MIN_LOV_ID`` reference.

.. important::

   Validate the script against the exact database version in staging. The
   tagged PostgreSQL script contains ``WITHOUT OIDS`` table clauses and the
   Oracle script declares a SQL ``BOOLEAN`` column. Database versions that
   reject these clauses require a compatible, reviewed migration script.
   Resolve this before the production maintenance window.

Keep the script output and check every statement. These scripts are schema
migrations rather than repeatable initialization scripts. For an interrupted
migration, have the database administrator inspect the applied changes before
continuing or restoring the backup.

Update the applications
-----------------------

1. With Tomcat stopped, move the previous ``knowage*.war`` archives and their
   corresponding expanded application directories to the backup location.
2. Clear the deployment working files in Tomcat's ``temp`` and ``work``
   directories, preserving configuration, resources and logs.
3. Deploy matching 9.1.0 archives. Include ``knowage.war``, ``knowage-api.war``
   and ``knowage-vue.war`` along with each engine used by your installation.
4. Reapply the required environment-specific JNDI links, service URLs, external
   authentication, resource paths and cluster settings. Compare configuration
   with the new defaults instead of replacing whole new files with old copies.
5. Update reverse-proxy routes for the application contexts in use. Keep public
   addresses consistent with the configured service URLs.
6. Start a node, inspect the logs and verify the installation before reopening
   traffic and starting the remaining nodes.

Validate the result
-------------------

* Sign in with an administrator and a representative end-user role; check SSO,
  MFA, tenant visibility and role selection where configured.
* Run a dataset and a document with mandatory and correlated parameters. Test a
  date driver with minimum and maximum LOV values.
* Open an existing Cockpit and a Dashboard. Check charts, tables, maps,
  associations, variables, saved views and cross-navigation.
* Test the required exports and execute a representative schedule immediately.
* Review menus, home pages, resources and user administration.

Cockpit migration is separate from upgrading the platform. Follow
:doc:`/chapter_3/create_new_dashboard/index` when converting a copy to a
Dashboard. Rebuild the map and crosstab widgets as described there.

Rollback
--------

Stop all nodes and restore the metadata database, application archives,
configuration and resources from the same pre-upgrade backup. Restart and
validate the restored installation before accepting traffic. Restoring only
the application archives leaves them paired with an incompatible schema.
