Knowage CE Installer usage
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

- JDK version 1.8
- ``JAVA_HOME`` environment variable

Different installer packages are provided for JDK 32/64 bit on Windows.

Memory
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE requires **2GB** of available RAM. This configuration is enough for most evaluation purposes.

Disk usage
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE requires **2GB** of free space on file system.
Optional embedded MariaDB Server 10.2 requires **4GB** of free space on file system.

Database
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer requires one of the following **external databases**:

- MySQL Server 5.5 or above already installed
- MariaDB Server 10.2 already installed

A user with sufficient **permissions to create schemas** must be provided.

If you are using MySQL Server 5.7 we suggest to set following configuration in file ``my.ini``:

- ``innodb_buffer_pool_size = 2G`` (adjust value here, 50%-70% of total RAM)
- ``innodb_log_file_size = 500M``

Knowage CE Installer includes also the option to use one of the following **embedded databases**:

- MariaDB Server 10.2 for Windows 32/64 bit
- MariaDB Server 10.2 for Linux 64 bit with GLIBC 2.14 or higher

Please note that embedded database option is not available for macOS.

Application server
~~~~~~~~~~~~~~~~~~~~~~~~
Knowage CE Installer provides Apache Tomcat 7 out of the box. Don't worry about pre-installing any application server.

Client-side requirements
------------------------

Browser
~~~~~~~~~~~~~~~~~~~~~~~~
Enable your browser to execute JavaScript.

Managing Knowage CE
------------------------
After installation, you can start/stop Knowage CE using desktop links, start menu entries or following line commands.

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

Linux (embedded MariaDB option)
~~~~~~~~~~~~~~~~~~~~~~~~
- Start Knowage CE using ``<installation directory>/Knowage-Server-CE/bin/knowage_startup.sh``
- Stop Knowage CE using ``<installation directory>/Knowage-Server-CE/bin/knowage_shutdown.sh``
