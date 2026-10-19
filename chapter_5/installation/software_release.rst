Get the Knowage 9.1 packages
============================

Download Community Edition archives from the
`v9.1.0 release <https://github.com/KnowageLabs/Knowage-Server/releases/tag/v9.1.0>`_.
Enterprise Edition customers obtain the corresponding packages and licensed
components through their distribution channel.

Use one release consistently across the applications and engines. The 9.1.0
assets include the main applications ``knowage.war``, ``knowage-api.war`` and
``knowage-vue.war`` and additional engine archives. Deploy the engines required
by the documents covered in this manual. AI services and other components marked
**Enterprise Edition (EE)** require the corresponding licensed distribution.

Database scripts are in the
`tagged source tree <https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowagedatabasescripts>`_.
Choose the MySQL/MariaDB, PostgreSQL or Oracle directory matching your metadata
database. Use creation scripts for a new schema and upgrade scripts for an
existing schema. Check database-version compatibility before execution.

For an existing installation, follow
:doc:`/chapter_5/upgrade/how_upgrade_9_0_to_9_1`.

License hardware identification
-------------------------------

For an Enterprise deployment requiring a stable MAC-based license identifier,
the deployment may use this JVM property in ``setenv.sh``:

.. code-block:: bash

   export JAVA_OPTS="$JAVA_OPTS -Dmac.address.licensing=true"

Agree the license identifier with your distribution channel before changing
an existing licensed installation.
