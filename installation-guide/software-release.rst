Software release
=========================

You can download Knowage through the following links:

- Community Edition: http://www.knowage-suite.com/site/ce-download/
- Enterprise Edition: http://www.knowage-suite.com/portal (registration required)

A typical release contains three elements:

- Installer, which gives you a step-by-step Knowage installation
- Web Application Archives (WARs) and DDL scripts (to populate the schema used by Knowage for its metadata)

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
---------------------------------------
If you're using a VM on AWS cloud and you want to use Knowage EE with license, you should be sure that hardware id doesn't change every start and stop.
To avoid this behaviour you can choose for using MAC address instead of default hardware id calculation.
You just have to add this optional row in "setenv.sh" file:

.. code-block:: bash

 export JAVA_OPTS="$JAVA_OPTS -Dmac.address.licensing=true"
