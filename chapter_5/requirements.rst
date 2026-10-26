Requirements
########################################################################################################################

Before going into details on Knowage installation, it is necessary to check if certain requirements are satisfied. We start to distinguish between the certified environments and the compatible ones. The first are those where check tests take place. The latter are those environments technically compatibles but where integration tests are not executed.

Operating systems
------------------------------------------------------------------------------------------------------------------------

The following Operating Systems (OS) are those ones which suit with Knowage platform.
The matrix below is retained from the published manual. Confirm the exact OS
release and architecture covered by your Knowage 9.1 distribution; the table
is not a new certification of every available version.

.. table:: Certified environments
   :widths: auto

   +---------------------------+-------------+
   |    Certified Environments               |
   +===========================+=============+
   |    **Operating System**   | **Version** |
   +---------------------------+-------------+
   |    Oracle Linux           |   9, 10     |
   +---------------------------+-------------+   
   |    Windows Server         | 2022,2025   |
   +---------------------------+-------------+

.. table:: Compatible environments
    :widths: auto

    +-----------------------------+-------------------+
    |    Compatible Environments                      |
    +=============================+===================+
    |    **Operating System**     | **Version**       |
    +-----------------------------+-------------------+
    |    RHEL Red Hat Enterprise  | 10                |
    +-----------------------------+-------------------+
    |    Ubuntu                   | 22, 24, 25        |
    +-----------------------------+-------------------+

Disk usage
------------------------------------------------------------------------------------------------------------------------

The Knowage installation requires 2 GB of available space on file system. This space does not include the space relative to the data and the metadata storage.
This installation footprint is not the complete production storage requirement:
allow for logs, resources, temporary exports, cache, database growth and backups.
Size CPU and RAM for the workload and enabled services; the 9.1 release does
not supply a universal minimum for concurrent production use.

Java environment
------------------------------------------------------------------------------------------------------------------------

The enviroment in which Knowage will be installed must include a JDK 17 installation. Be sure that the JDK component is successfully installed and that the environment variable ``JAVA_HOME`` is properly configured. The steps to configure it depend on the OS.
Knowage is compatible with Open JDK 17.

Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define the ``JAVA_HOME`` variable for the account that runs Tomcat, using the
actual JDK installation path. An OS service may not read the interactive
user’s ``.bash_profile``; also check its service environment or ``setenv.sh``.

.. code-block:: shell
        :caption: Instructions to set the JAVA_HOME variable for Linux environment.

        export JAVA_HOME="/path/to/jdk-17"
        export PATH="$JAVA_HOME/bin:$PATH"

Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define the ``JAVA_HOME`` variable and ``PATH`` in the section "Environment variables" which can be reached from the "System".

   .. figure:: media/image7.png

      Setting the path for the JAVA_HOME variable for Windows

Application server
------------------------------------------------------------------------------------------------------------------------

The following lists the supported application servers:

.. table:: Supported application servers
    :widths: auto

    +---------------------+------------------------+-------------+
    |    **Support type** | **Application Server** | **Version** |
    +=====================+========================+=============+
    |    Certified        | Apache Tomcat          | 9           |
    +---------------------+------------------------+-------------+

For each application server installation please refer to its official documentation.
The public Knowage Docker recipe uses Tomcat **9.0.109**. This identifies the
recipe baseline, not a requirement to use that patch indefinitely. Use a
maintained Tomcat 9.0.x patch qualified for your deployment. Tomcat 10 and 11
use the Jakarta namespace and are not direct replacements for this deployment.

Tomcat 9.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following we will refer to Tomcat installation folder as ``TOMCAT_HOME``.

Tomcat on Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to create a proper user for the execution of Tomcat. We state the main steps to follow for this purpose.

- Create the Tomcat user.

.. code-block:: shell

        useradd -m tomcat
        passwd tomcat

- Install the Tomcat using the Tomcat user. Remeber to define the ``TOMCAT_HOME`` variable.

.. code-block:: shell

        export TOMCAT_HOME="/path/to/apache-tomcat-9"

- Be sure that the Tomcat uses the JDK 17: usually the Tomcat settings are defined in the ``TOMCAT_HOME/bin/setenv.sh`` file, therefore if the ``TOMCAT_HOME/bin/setenv.sh`` file does not exit, the user must create it and insert it in the content as shown below. ``CATALINA_PID`` identifies the file used to record the Tomcat process ID.

.. code-block:: sh

        export CATALINA_PID="$TOMCAT_HOME/logs/tomcat-knowage.pid"
        export JAVA_HOME="/path/to/jdk-17"

- Modify the ``TOMCAT_HOME/bin/shutdown.sh`` file to force the shut down of the application in case of hanging:

.. code-block:: sh

        exec "$PRGDIR"/"$EXECUTABLE" stop -f "$@"

Tomcat on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to install Tomcat as a service. Documentation is available at https://tomcat.apache.org/tomcat-9.0-doc/windows-service-howto.html.

Database schema for metadata
------------------------------------------------------------------------------------------------------------------------

Knowage uses a schema to manage metadata, that is all those information required for its operation. These concern the configuration, the users and the analytical documents. It is possible to use the following DBMSs for the creation of this schema.

The 9.1.0 source provides metadata creation and upgrade scripts for:

- MySQL / MariaDB;
- PostgreSQL;
- Oracle.

Use the exact DBMS version and JDBC driver qualified for the distribution.
The old matrix listed historical database releases and does not establish
their certification for 9.1. A JDBC driver version or support as a business
data source is not a metadata-database compatibility guarantee.

The public Compose recipe uses MariaDB 10.3 as an example. Do not take that
legacy example as the version recommendation for a new production database.
Review the database-specific scripts before provisioning or upgrading; see
:doc:`upgrade/how_upgrade_9_0_to_9_1`.

Therefore, a schema must be available. It can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *metadata DB* in the following. Observe that Knowage includes all the DDL for table creation.

Database schema for data
------------------------------------------------------------------------------------------------------------------------

A schema for data must be also available. It can be queried through Knowage and can be reached through the JDBC protocol by the Knowage installation server; such a schema will be called *data DB* in the following.

Cache service
--------------------------------------------------------------------------------

The public deployment uses a separate Hazelcast 5.3 service; the Java
integration dependency in 9.1.0 is 5.3.6. Keep the topology and configuration
supplied with the deployment. Configure the SQL cache resource ``jdbc/ds_cache``
as described in :doc:`installation/manual_installation`.

NodeJS requirements
------------------------------------------------------------------------------------------------------------------------

.. important::
         **Enterprise Edition only**

         NodeJS is required only for Enterprise Edition.

Knowage includes NodeJS scripts for Enterprise export services. Install the
Node.js version and dependencies supplied with the **9.1 EE export package**.
The public Community source does not establish the exact supported
Node.js/Chromium pair for that package. A frontend build workflow is not an
export-service requirement.

Verify the installation as the service account:

.. code-block:: console

   node --version
   npm --version

Chromium requirements
------------------------------------------------------------------------------------------------------------------------

.. important:: Enterprise Edition only

   Chromium export services require the corresponding EE package.

Use the Chromium build and native OS dependencies supplied for the export
package. The earlier CentOS 8 and Red Hat 7 commands do not describe the
dependency packages for every supported OS. Follow the package instructions
for the actual host and test the required PDF and image exports.

Support to non-latin languages
------------------------------------------------------------------------------------------------------------------------

Knowage does some of its job at server side and it could need support for non-latin languages. Some operating systems don't provides support to non-latin language by default: see the official documentation to enable the support to those languages.

Install explicit font packages from the host OS repositories. Make them
available to Java and Chromium, and check the required scripts in an exported
document. Package names depend on the OS release.

Python service
------------------------------------------------------------------------------------------------------------------------

Python datasets, functions and widgets require a separate web service with
the interpreter and libraries qualified for that service package. The 9.1.0
source still declares a Python lower bound of 3.7 and pins older libraries;
this does not establish compatibility with every later Python version.
Use the package associated with your 9.1 deployment and follow
:doc:`installation/python-installation`.

Supported browsers
------------------------------------------------------------------------------------------------------------------------

Knowage supports the newest and the second to last version of these browsers:

- `Google Chrome <https://www.google.com/intl/en_en/chrome/>`_
- `Firefox <https://www.mozilla.org/en-US/firefox/new/>`_
- `Microsoft Edge <https://www.microsoft.com/en-us/edge?icid=SSM_AS_Promo_Other_Edge>`_

.. important::
         **Internet Explorer**

         Internet Explorer is no longer supported by Microsoft and it is also vulnerable. Please, use one of the supported browser listed above.

Containers
------------------------------------------------------------------------------------------------------------------------

For Docker installations, Java and Tomcat are included in the application
image. Select the approved 9.1.0 application and service images: the public
Compose example uses **9.1-SNAPSHOT** tags, which do not identify the released
9.1.0 artifacts. See :doc:`installation/knowage-ce-installer`.
