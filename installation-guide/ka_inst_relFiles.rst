Released file description
=========================

It is possible to download the software in the web site `www.knowage-suite.com/portal <http://www.knowage-suite.com/portal>`__ where we can find all resources for the installation, the single packages and the DDL.

Here the essential elements for the installation:

-Installer,

-DDL (see Table 2.5),

-the single software packages.

.. table:: Available Data Definition Languages
    :widths: auto
    
    +------------------------------------+
    |   **Component for table creation** |
    +====================================+
    |   Ingres-dbscript                  |
    +------------------------------------+
    |   MySql                            |
    +------------------------------------+
    |   Oracle                           |
    +------------------------------------+
    |   Postgres                         |
    +------------------------------------+
    
Installation procedure
----------------

Knowage can be installed in two ways: manually or using the installer. In this section we will describe both procedures.

Installer usage
------------------
Knowage installer is an application which steers the user to the installation and the first configuration of the product. It works in both Linux and Windows operating systems.

 **[LINUX]** To launch the installer, it is necessary to enable the flag execution on the installation file, typing the command in the bash:

+----------------------------------+
| chmod +x <Knowage_unix_1_0_0.sh> |
+----------------------------------+

Now the installer is executable. Knowage can be installed using a GUI or a command line. In the first case the user must type the the command:

+-------------------------+
| ./Knowage_unix_1_0_0.sh |
+-------------------------+

while in the second case he must type the command:

+----------------------------+
| ./Knowage_unix_1_0_0.sh -c |
+----------------------------+


 **[WIN]** On Windows systems the installer requires some administrator permissions.

Let’s describe the main steps of the execution:

-**Step 1.**\ ( Figure 2.2) Click on “Next” to go on with the installation or “Cancel” to call off.

-**Step 2.**\ (Figure 2.3) Accept the license terms and conditions and click on “Next”.

-**Step 3.**\ (Figure 2.4) The installer requires internet access to connect with Knowage server in order to activate the licences and download the installation packages. It is possible to configure the proxy with for Internet connectivity inside the wizard. In case the settings are wrong, cancel the current installation and start a new one. If the connection succeeds, then the installer proceeds with the online licences, otherwise the user is asked to continue with the offline activation or to cancel the installation.

-**Step 4.**\ (Figure 2.5) It is possible to activate the product on-line thanks to an online activation procedure. It is necessary though to purchase one (or more) product key(s). There are as many product keys as the available components in Knowage. If the installer recognises the product key, then it starts the procedure, otherwise the activation fails.

The user can insert a new product key until there are components to activate.

.. image:: media/image8.png 

Figure 2.2: Installer GUI.

.. image:: media/image9.png 

Figure 2.3: Licence acceptance.

.. image:: media/image10.png 

Figure 2.4: Internet connection.

.. image:: media/image11.png 

Figure 2.5: Insert the product key.

-**Step 5.**\ (Figure 2.6) If the user has chosen the online activation, the products corresponding to the purchased product keys are selected automatically and are not changeable by the user. If the user has chosen the offline procedure he/she must manually select at least one component to be installed.
      
.. image:: media/image12.png 

Figure 2.6: Select components.

-**Step 6.**\ (Figure 2.7) Select the desired application server and set up its installation folder. The installer checks the installation path of the application server before moving to the next step.

-**Step 7.**\ (Figure 2.8) The metadata database is used by Knowage as repository for the configuration information.

**Remark.** Set up a priori a DBMS to store Knowage metadata. Select then the desired DBMS for metadata storage and modify the fields accordingly. The installer will verify the connection before moving to the next step. In addition the installer asks the user if the JDBC connector should be installed the JDBC connector.

To configure a data DB the user must check the relative feature of the wizard, as shown in Figure 2.9, otherwise the installer will not configure such connection. Select then the desired DBMS as data database and modify the fields properly. Once again the installer verifies the connection before moving to the next step. The user is asked to install on the application server the JDBC connector for the specified DBMS.


.. image:: media/image13.png 

Figure 2.7: Application server configuration.

.. image:: media/image14.png 

Figure 2.8: Configuration of the metadata database.

.. image:: media/image15.png 

Figure 2.9: Configuration of the metadata database.

-**Step 8.**\ (Figure 2.10) The setting for clustering is deselected by default, that is Knowage executes on a single node if not otherwise specified. To enable the clustering, select the number of nodes and set up the related IP address for each of them. The installer controls the correctness of each and that they are not repeated. The installation process is therefore activated. The installer attempts to download the installation files from the Knowage web site, for which credentials are required. If the connection fails and the installer cannot verify the user’s credentials, the installer asks the user if he wants to go on using the local WAR files. In this case the installer will check if all essential WAR files are located in the specified path, according to the components selected in the previous steps. It will also copy the WAR files (in the case of the offline installation) and add additional files if needed. All the additional tasks are hidden behind the progress bar showed in the installation wizard (refer to Figure 2.11).

**Remark: offline manual activation.** Note that in this case the wizard, Figure 2.12, provides the instructions to ask for technical support and get the licence files that the user must manually install.

-**Step 9.**\ (Figure 2.13) The installation succeded. The user can now choose if to visit the Knowage website and click "Finish" to exit setup.

.. image:: media/image16.png 

Figure 2.10: Clustering.

.. image:: media/image17.png 

Figure 2.11: Additional tasks.

.. image:: media/image18.png 

Figure 2.12: Offline manual activation.

.. image:: media/image19.png 

Figure 2.13: End of the installation.



Uninstaller
--------------

At the end of the installation, the user can find the **uninstaller** file inside the installation folder. This can be executed to unistall Knowage.
**[LINUX]** The uninstaller is executable from the Knowage installation folder:

-  using the GUI if a desktop environment is available;

-  using the bash if it is executed typing the parameter “-c”.
**[WIN]** On Windows Systems the uninstaller requires administrator permissions. It can be executed from Windows menu or from the Windows control panel.

.. image:: media/image20.png 

Figure 4.13: Knowage uninstaller.

Select also which optional features to run (in Figure 4.14 the available ones) and click on “Next”. The uninstaller controls if the application server is running in that moment. If that is the case, the uninstaller cannot succeed in removing the Knowage packages.

The uninstaller removes also the previous installed files, restores the databases and the application server configuration.

Uninstaller

.. image:: media/image21.png 

Figure 4.14: Knowage uninstaller.

.. image:: media/image22.png 

Figure 4.15: Knowage uninstaller.

Uninstaller

.. image:: media/image23.png 

Figure 4.16: Knowage uninstaller.
