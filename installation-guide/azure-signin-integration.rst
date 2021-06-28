Azure Sign-In integration
==========================

Knowage provides integration with Azure Sign-In for authentication purposes, i.e. users can login into Knowage using their Azure accounts.

**Remark.** Azure Sign-In is exploited only for authentication, not for authorization. The authorization part (that consists of defining roles and profile attributes for users) is still in charge of Knowage: this means that, before an user can enter into Knowage with his Azure account, the admin user has to define that user inside the regular Knowage users catalogue, keeping in mind that the user id must match the email of his Azure account (the provided password will not be considered when user will log in). In case the user is not defined inside Knowage users list, the authentication will fail.

In order to enable Azure Sign-In authentication, please follow these steps:

* start Knowage with default configuration;
* enter Knowage as admin and define users who will be allowed to enter Knowage (use their email address as user id);
* browse to **Configuration management** via the main menu;
* set the value of configuration parameter **SPAGOBI.SECURITY.USER-PROFILE-FACTORY-CLASS.className** to ``it.eng.spagobi.security.azure.AzureSecurityServiceSupplier``, then save;
* stop Knowage application;
* follow Azure Sign-In documentation in order to configure your Knowage application and to get information about tenant ID and client ID;
* create a text file wherever you want and paste the tenant ID and the client ID inside it, for example: create file TOMCAT_HOME/conf/azure.signin.config.properties with this content:

.. code-block:: properties
    :linenos:

    enabled=true
    client_id=<your client ID>
    tenant_id=<your tenant ID>

* add the ``azure.signin.config`` Java System property that specifies the location of this properties file: in a Unix-like environment, edit TOMCAT_HOME/bin/setenv.sh and add

.. code-block:: bash
    :linenos:

    export JAVA_OPTS="${JAVA_OPTS} -Dazure.signin.config=<your Tomcat home folder>/conf/azure.signin.config.properties"

instead, in a Windows environment using Apache Tomcat, edit TOMCAT_HOME/bin/setenv.bat:

.. code-block:: bash
    :linenos:

    set JAVA_OPTS="%JAVA_OPTS% -Dazure.signin.config=<your Tomcat home folder>/conf/azure.signin.config.properties"

* start Knowage application.

When users will connect into Knowage, the login page will display the Azure Sing-In button:

.. figure:: media/azure_signin.jpg

   Advanced configuration - Azure Sing-In button.

When clicking on that button, Azure Sing-In authentication applies; if successful, users will be redirected into their home page inside Knowage.
In case the account is not recognized by Knowage (i.e. the provided email address does not match any existing Knowage user id), he will get an error message.
   
Inside the Azure portal, after you have successfully registered our app, you will have to configure a new Single-page application, and enter "https://<your-host-name>/knowage/servlet/AdapterHTTP" as Redirect URI.

.. figure:: media/azure_redirect_uri.jpg

   Azure portal configuration - Redirect URI.
   
The authorization endpoint must be able to issue ID tokens, so make sure that the corresponding checkbox is flagged.

.. figure:: media/azure_idtoken_checkbox.jpg

   Azure portal configuration - ID token checkbox.
   
Directly from the application manifest.json file, you need to set "accessTokenAcceptedVersion": 2 in order to use the v2.0 endpoints.

.. figure:: media/manifest.jpg

   Azure portal configuration - manifest.json file.