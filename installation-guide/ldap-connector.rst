LDAP security connectors
=========================

Authentication
---------------

Knowage provides integration with a LDAP server for authentication purposes.

**Remark.** Be sure that the Knowage users have been taken under LDAP census. The LDAP security connectors check the user that is accessing Knowage, but the user must be already defined as a Knowage user. Therefore, the users must coexist in both authentication systems (LDAP and Knowage).

Knowage ships with three LDAP security connectors:

* **LdapSecurityServiceSupplier**: a pure LDAP connector that authenticates every user using an LDAP server,
* **ProfiledLdapSecurityServiceSupplier**: a mixed LDAP/internal connector that authenticates users using an LDAP server or the internal Knowage authentication system according to their profile information. More precisely, the choice of the system to be exploited is based on the **auth_mode** profile attribute: if the user profile attribute **auth_mode** is defined and its value equals to ``internal`` for the user, then Knowage will use its internal authentication mechanism, otherwise it will try an LDAP authentication,
* **FullLdapSecurityServiceSupplier**: this connector performs both authentication and authorization against LDAP, and is the only connector that does not require users to be present both on LDAP and Knowage. There is an apposite section dedicated to this connector at the bottom of the page.

.. warning::
    The only way to maintain access to Knowage for **users not mapped onto LDAP** is to:

    * define the user profile attribute **auth_mode**,
    * set **auth_mode** = ``internal`` for every user not mapped onto LDAP,
    * use the connector **ProfiledLdapSecurityServiceSupplier** (see below).

In order to setup any LDAP security connector, you need to define a .properties file that includes the LDAP configuration:

* **INITIAL_CONTEXT_FACTORY**: initial context factory Java class,
* **PROVIDER_URL**: LDAP server IP,
* **SECURITY_AUTHENTICATION**: authentication type,
* **DN_PREFIX**: prefix that will be prepended to the user name to create the DN (distinguished name) of logging user,
* **DN_POSTFIX**: postfix that will be appended to the user name to create the DN (distinguished name) of logging user;

.. important::
         The final concatenation **DN_PREFIX + <Knowage user ID> + DN_POSTFIX** must be equal to the **DN (distinguished name)** of the user as defined in LDAP server. Please check DN examples at https://ldapwiki.com/wiki/DN%20Syntax .

Then define a custom JVM property ``ldap.config``, setting its value to the path of LDAP properties file.

In a Unix-like environment using Apache Tomcat you can add a custom JVM property to variable ``JAVA_OPTS`` in a ``setenv.sh`` file under ``bin`` folder:

.. code-block:: bash
        :linenos:

        export JAVA_OPTS="${JAVA_OPTS} -Dldap.config=/opt/tomcat/conf/ldap.properties"

In a Windows environment using Apache Tomcat you can add a custom JVM property to variable ``JAVA_OPTS`` in a ``setenv.bat`` file under ``bin`` folder:

.. code-block:: bash
    :linenos:

    set JAVA_OPTS="%JAVA_OPTS% -Dldap.config=C:/Tomcat/conf/ldap.properties"

Below there is an example of the ldap.properties file configuration for both LDAP connectors:

.. code-block:: properties

  INITIAL_CONTEXT_FACTORY   = com.sun.jndi.ldap.LdapCtxFactory
  PROVIDER_URL              = ldaps://<LDAP server address>:389
  SECURITY_AUTHENTICATION   = simple
  DN_PREFIX                 = CN=
  DN_POSTFIX                = ,ou=IT staff,o="Example, Inc",c=US
  SEARCH_USER_BEFORE        = false
  SEARCH_USER_BEFORE_USER   =
  SEARCH_USER_BEFORE_PSW    =
  SEARCH_USER_BEFORE_FILTER = (&((objectclass=person))(uid=%s))

  ldap2.INITIAL_CONTEXT_FACTORY   = com.sun.jndi.ldap.LdapCtxFactory
  ldap2.PROVIDER_URL              = ldaps://<LDAP 2 server address>:389
  ldap2.SECURITY_AUTHENTICATION   = simple
  ldap2.DN_PREFIX                 = CN=
  ldap2.DN_POSTFIX                = ,ou=IT staff,o="Example, Inc",c=US
  ldap2.SEARCH_USER_BEFORE        = true
  ldap2.SEARCH_USER_BEFORE_USER   = user_before_username
  ldap2.SEARCH_USER_BEFORE_PSW    = user_before_password
  ldap2.SEARCH_USER_BEFORE_FILTER = (&((objectclass=account))(uid=%s))


Using the example above, you can configure:
   * *auth_mode = internal*: if you want to log in using the Knowage metadata database instead of contacting an LDAP server
   * *empty auth_mode value*: if you want to login using the first configuration of the properties file (the one without any prefix)
   * *auth_mode = ldap2*: if you want to log in by contacting the LDAP server using the configuration with "ldap2." prefix

In case you want the users to authenticate using their complete distinguish name, set ``SEARCH_USER_BEFORE`` key to be *false*.
In case you want instead the users to authenticate using an LDAP property such as ``uid``, then set ``SEARCH_USER_BEFORE`` key to be *true*; you need also to specify the ``SEARCH_USER_BEFORE_FILTER`` filter that Knowage will exploit in order to retrieve the user's information on the LDAP server. **Pay attention that %s placeholder must be present**: it will be replaced by Knowage with the actual username provided by the user when logging in.

The ``SEARCH_USER_BEFORE_USER`` and ``SEARCH_USER_BEFORE_PSW`` keys are credentials to authenticate to LDAP server; if the first one is set, the second one will be considered also. *These parameters are used only if anonymous bind is not allowed for LDAP server. For this reason they are optional and can be empty.*

.. important::
    Restart your application server in order to load the custom JVM property.
	
.. warning::
        After enabling the search functionality you may encounter the following exception: javax.naming.PartialResultException: Unprocessed Continuation Reference(s). To solve this just change LDAP port from 389 to 3268 (credits: https://stackoverflow.com/questions/16412236/how-to-resolve-javax-naming-partialresultexception )


The final step is to set the LDAP security connector as follow:

* access Knowage as administrator,
* browse to **Configuration Management** via the main menu,
* set the value of config **SPAGOBI.SECURITY.USER-PROFILE-FACTORY-CLASS.className** to ``it.eng.spagobi.security.LdapSecurityServiceSupplier`` **or** ``it.eng.spagobi.security.ProfiledLdapSecurityServiceSupplier``,
* save,
* log out of Knowage.

.. warning::
        To recover the default authentication mechanism please revert manually the config **SPAGOBI.SECURITY.USER-PROFILE-FACTORY-CLASS.className** to its default value ``it.eng.spagobi.security.InternalSecurityServiceSupplierImpl`` using a database client.

Knowage is now ready to authenticate the users via LDAP credentials.


Authentication + authorization
-------------------------------

A third LDAP connector is available, which does not need users to be present in Knowage metadata (but only on LDAP system). This connector allows you to build the UserProfile object based on the information contained in the LDAP system. Only if the user is not found in the LDAP system, the Knowage metadata will be used (this scenario is useful for technical users that are not registered inside the LDAP).

.. important::
         Whenever a user logs into Knowage, the connector will always first query the LDAP system in order to authenticate the user and build the profile object. Only if this operation fails (it means that the user is not present in the LDAP system) Knowage will use its internal metadata to authenticate the user.
		 
As for the above connectors, you must follow some steps in order to setup this connector. First you need to define a ``.properties`` file that includes the following configurations:

* **INITIAL_CONTEXT_FACTORY**: initial context factory Java class,
* **PROVIDER_URL**: LDAP server IP,
* **SECURITY_AUTHENTICATION**: authentication type,
* **DN_PREFIX**: prefix that will be prepended to the user name to create the DN (distinguished name) of logging user,
* **DN_POSTFIX**: postfix that will be appended to the user name to create the DN (distinguished name) of logging user,
* **AUTHENTICATION_FILTER**: LDAP filter that will be checked before allowing permission to users,
* **USER_ROLES_ATTRIBUTE_NAME**: LDAP attribute that contains the full string with user roles,
* **USER_ROLES_ATTRIBUTE_FIELD**: prefix that anticipates each Knowage role inside the full string,
* **SUPERADMIN_ATTRIBUTE**: role that grants superadmin permissions;

Suppose that the structure of a user, inside LDAP, is as follows:

.. code-block:: properties

  cn         : John
  sn         : Doe
  mail       : john.doe@yourorganization.com
  enabled    : true
  deprecated : false
  isMemberOf : cn=ADMIN,ou=unit1,dc=yourorganization,dc=com
  isMemberOf : cn=DEVELOPER,ou=unit1,dc=yourorganization,dc=com
  isMemberOf : cn=USER,ou=unit1,dc=yourorganization,dc=com
  
We want the authentication to succeed only if ``enabled=true`` and ``deprecated=false``. Furthermore, we want to build profile object by using all the ``isMemberOf`` attributes, and using the Knowage roles specified under the ``cn`` properties.


Below there is an example of the ldap.properties file configuration that satisfies the above requirements:

.. code-block:: properties

  INITIAL_CONTEXT_FACTORY    = com.sun.jndi.ldap.LdapCtxFactory
  PROVIDER_URL               = ldaps://<LDAP server address>:389
  SECURITY_AUTHENTICATION    = simple
  DN_PREFIX                  = CN=
  DN_POSTFIX                 = ,ou=IT staff,o="Example, Inc",c=US
  AUTHENTICATION_FILTER      = (&(enabled=true)(!(deprecated=true)))
  USER_ROLES_ATTRIBUTE_NAME  = isMemberOf
  USER_ROLES_ATTRIBUTE_FIELD = cn
  SUPERADMIN_ATTRIBUTE       = ADMIN


Then you need to define a custom JVM property ``ldap.config``, setting its value to the path of LDAP properties file.

In a Unix-like environment using Apache Tomcat you can add a custom JVM property to variable ``JAVA_OPTS`` in a ``setenv.sh`` file under ``bin`` folder:

.. code-block:: bash
        :linenos:

        export JAVA_OPTS="${JAVA_OPTS} -Dldap.config=/opt/tomcat/conf/ldap.properties"

In a Windows environment using Apache Tomcat you can add a custom JVM property to variable ``JAVA_OPTS`` in a ``setenv.bat`` file under ``bin`` folder:

.. code-block:: bash
    :linenos:

    set JAVA_OPTS="%JAVA_OPTS% -Dldap.config=C:/Tomcat/conf/ldap.properties"

The final step is to set the LDAP security connector as follow:

* access Knowage as administrator,
* browse to **Configuration Management** via the main menu,
* set the value of config **SPAGOBI.SECURITY.USER-PROFILE-FACTORY-CLASS.className** to ``it.eng.spagobi.security.FullLdapSecurityServiceSupplier``,
* save,
* log out of Knowage.

.. warning::
        To recover the default authentication mechanism please revert manually the config **SPAGOBI.SECURITY.USER-PROFILE-FACTORY-CLASS.className** to its default value ``it.eng.spagobi.security.InternalSecurityServiceSupplierImpl`` using a database client.

