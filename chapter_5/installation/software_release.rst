Software release
########################################################################################################################

You can download Knowage through the following links:

- Community Edition: https://github.com/KnowageLabs/Knowage-Server/releases

A typical release contains 2 elements:

- Web Application Archives (WARs) 
- DDL scripts (to populate the schema used by Knowage for its metadata) you canfine it in https://github.com/KnowageLabs/Knowage-Server/tree/knowage-server-9.0/knowagedatabasescripts

      .. table:: Supported databases for DDL scripts
          :widths: auto

          +------------------------------------+
          |   **Supported databases**          |
          +====================================+
          |   MySQL / MariaDB                  |
          +------------------------------------+
          |   Oracle                           |
          +------------------------------------+
          |   Postgres                         |
          +------------------------------------+

Optional: using MAC address for license
------------------------------------------------------------------------------------------------------------------------

If you're using a VM on AWS cloud and you want to use Knowage EE with license, you should be sure that hardware id doesn't change every start and stop.
To avoid this behaviour you can choose for using MAC address instead of default hardware id calculation.
You just have to add this optional row in "setenv.sh" file:

   .. code-block:: bash

   	export JAVA_OPTS="$JAVA_OPTS -Dmac.address.licensing=true"
