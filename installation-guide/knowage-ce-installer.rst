Knowage CE Installer
============================

Knowage CE installer is an application which steers the user to the installation and the first configuration of the product.

Knowage CE is a web application, meaning it runs centrally on a server, and users interact with it through web browsers from any computer on the same network. Knowage CE Installer lets you easily configure your server.

Server-side requirements
------------------------

Operating system
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer runs on **Windows**, **Linux** and **macOS** operating systems.

Java platform
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer requires:

- JDK 1.8
- ``JAVA_HOME`` environment variable

Memory
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE requires **3GB** of available RAM. This configuration is enough for most evaluation purposes.

Disk usage
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE requires **2GB** of free space on file system.
Optional embedded MariaDB Server 10.2 requires **4GB** of free space on file system.

Database
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer requires one of the following **external databases**:

- MySQL Server 5.5 or 5.6 or 5.7 already installed
- MariaDB Server 10.2 already installed

A user with sufficient **permissions to create schemas** must be provided. Knowage CE Installer connects to database using a JDBC driver via TCP/IP connection.

If you are using MySQL Server 5.7 we suggest to set following configuration in file ``my.ini``:

- ``innodb_buffer_pool_size = 2G`` (adjust value here, 50%-70% of total RAM)
- ``innodb_log_file_size = 500M``

Knowage CE Installer includes also the option to use one of the following **embedded databases**:

- MariaDB Server 10.2 for Windows 64 bit

Please note that embedded database option is not available for macOS.

Application server
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer provides Apache Tomcat 7 out of the box. Don't worry about pre-installing any application server.

Proxy settings
~~~~~~~~~~~~~~~~~~~~~~~~
If proxy is enabled please add property ``http.nonProxyHosts`` to JVM properties after completing installation, modifying file ``<installation directory>\Knowage-Server-CE\bin\setenv.bat`` on Windows or ``<installation directory>/Knowage-Server-CE/bin/setenv.sh`` on Linux/macOS.

.. code-block:: bash
  :linenos:
  
  -Dhttp.nonProxyHosts=localhost

Client-side requirements
------------------------

Browser
~~~~~~~~~~~~~~~~~~~~~~~~
Enable your browser to execute JavaScript.

Proxy settings
~~~~~~~~~~~~~~~~~~~~~~~~
If proxy is enabled please add hostname to proxy's ignore list.

Launching
------------------------
Windows
~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

  The installer has to be run as administrator.


Linux/macOS
~~~~~~~~~~~~~~~~~~~~~~~~
Extract the installer SH file typing the command in shell:

.. code-block:: bash
  :linenos:

  unzip Knowage-6_2_0-CE-Installer-Unix-20180719.zip

.. warning::
   On **macOS** the default app used to open ZIP files may fail to extract the installer ZIP file.

Enable the execute permission on the file, typing the command in shell:

.. code-block:: bash
  :linenos:

  chmod +x Knowage-6_2_0-CE-Installer-Unix-20180719.sh

Knowage CE installer can run in GUI or console mode.

- **GUI mode** is available only if a desktop environment is available. Run installer in GUI mode typing the command in shell:

  .. code-block:: bash
    :linenos:

    ./Knowage-6_2_0-CE-Installer-Unix-20180719.sh

- **Console mode** is always available and let complete installation using shell. Run installer in Console mode typing the command in shell:

  .. code-block:: bash
    :linenos:

    ./Knowage-6_2_0-CE-Installer-Unix-20180719.sh -c

Managing Knowage CE
------------------------
After completing installation, you can start/stop Knowage CE using desktop links, start menu entries or following shell commands.

Windows
~~~~~~~~~~~~~~~~~~~~~~~~
- Start Knowage CE using ``<installation directory>\Knowage-Server-CE\bin\startup.bat``
- Stop Knowage CE using ``<installation directory>\Knowage-Server-CE\bin\shutdown.bat``

Windows (embedded MariaDB option)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Start Knowage CE using ``<installation directory>\Knowage-Server-CE\bin\knowage_startup.bat``
- Stop Knowage CE using ``<installation directory>\Knowage-Server-CE\bin\knowage_shutdown.bat``

Linux/macOS
~~~~~~~~~~~~~~~~~~~~~~~~
- Start Knowage CE using ``<installation directory>/Knowage-Server-CE/bin/startup.sh``
- Stop Knowage CE using ``<installation directory>/Knowage-Server-CE/bin/shutdown.sh``
