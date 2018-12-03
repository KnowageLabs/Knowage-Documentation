CAS installation
==============

CAS is an application that implements a Single-Sign-On (SSO) mechanism. It is a good practise in production environments to install it and configure it so to have secure access to the Knowage server applications. CAS expects the use of the HTTPS protocol.

Deploy of the CAS application
-----------------------------

Carry out the following steps:

* shut down the server if running,
* deploy CAS application,
* for Tomcat: unzip the ``cas.war`` file inside the ``TOMCAT_HOME/webapps/cas``
* for JBoss: copy the ``cas.war`` file inside the ``JBOSS_HOME/standalone/deployments``
* edit ``/cas/WEB-INF/classes/cas_spagobi.properties`` inserting the connection parameters for the metadata database of Knowage,as following

	.. _conneparamknow:
	.. code-block:: bash
		:linenos:
		:caption: Connection parameters for Knowage metadata db.

			spagobi.datasource.driver=<driver JDBC> 
			spagobi.datasource.url=<URL JDBC> 
			spagobi.datasource.user=<user_name>                             
			spagobi.datasource.pwd=<password> encript.password=true               

For further details please refer to the official documents available on CAS website `https://www.apereo.org/projects/cas. <https://www.apereo.org/projects/cas>`__

HTTPS certificate
-----------------

Since CAS application requires the use of the HTTPS protocol, the user must own an SSL certificate: it can be released a Certification Authority (CA) or it can be self-signed (it is recommended the use of the ``keytool`` utility -http://docs.oracle.com/javase/7/docs/technotes/tools/solaris/keytool.html- available in the JDK).

In case the certificate self-signed, it must be inserted in the CA repository of the JDK (usually such a repository is located in the ``JDK_HOME/jre/lib/security``) or in an ad-hoc repository, called ``truststore``, and conveniently configured in the application server in use. It is sufficient to set the two Java properties ``Djavax.net.ssl.trustStore=<truststore path>`` and ``Djavax.net.ssl.trustStorePassword=<truststore password>``

We suggest to refer to the Java documents for more details. In the following we will restrict on give some useful commands of the ``keytool`` utility if the user intends to install a self-signed certificate:

* generate a copy of the public/private key-pair into a repository (keystore) called ``keystore.jks``, as below:

	.. code-block:: bash
       	 	:linenos:
        	:caption: keystore.jks creation.

   			$JAVA_HOME/bin/keytool -genkeypair -keystore keystore.jks -storepass <keystore password> -alias <certificate alias> -keyalg RSA -keysize 2048 -validity 5000 -dname CN=<server name that hosts Knowage >, OU=<organization unit>, O=<organization name>,L=<locality name>, ST=<state name>, C=<country>                    

* export a certificate in a ``cert.crt`` file, as suggested below:

		.. code-block:: bash
        		:linenos:
				:caption: Certificate export.

   				$JAVA_HOME/bin/keytool -export -alias <alias of the certificate> -file cert.crt -keystore keystore.jks 

* set the certificate inside the CA certificates of the JDK to make it accessible (the user will be asked the CA certificates password, the default one is *changeit*)

		.. code-block:: bash
        		:linenos:
        		:caption: Importing the certificate into JDK CA repository.

   				$JAVA_HOME/bin/keytool -import -trustcacerts -alias <alias del certificato> -file cert.crt -keystore  
   				$JAVA_HOME/jre/lib/security/cacerts

Configuration of the HTTPS protocol for Tomcat
----------------------------------------------

To enable the HTTPS protocol it is necessary to operate according to these steps:

* copy the keystore which contains the pair public/private keys (``keystore.jks``) inside the ``TOMCAT_HOME/conf``;
* edit the ``TOMCAT_HOME/conf/server.xml`` file, comment the HTTP connector on 8080 port and uncomment the HTTPS connector on 8443 port and configure it as below:

.. code-block:: xml
        :linenos:
        :caption: Export of the certificate.

		<Connector acceptCount="100"
					maxHttpHeaderSize="8192"
					clientAuth="false"
					debug="0"
					disableUploadTimeout="true"
					enableLookups="false"
					SSLEnabled="true"
					keystoreFile="conf/keystore.jks"
					keystorePass="<keystore password>"
					maxSpareThreads="75"
					maxThreads="150"
					minSpareThreads="25"
					port="8443"
					scheme="https"
					secure="true"
					sslProtocol="TLS"
		/>

Knowage configuration
---------------------

Once the CAS has been installed, it is necessary to modify the Knowage configuration. The user must edit some values of the ``SBI_CONFIG`` table using the administrator interface

.. code-block:: bash
        :linenos:
        :caption: Values of the SBI_CONFIG table to change.

		SPAGOBI_SSO.ACTIVE:
		set valueCheck to true

		CAS_SSO.VALIDATE-USER.URL:
		set valueCheck to https://<URL of the CAS application>/cas

		CAS_SSO.VALIDATE-USER.SERVICE:
		set valueCheck to https://<URL of the Knowage server >:8443/knowage/proxyCallback

		SPAGOBI_SSO.SECURITY_LOGOUT_URL:
		set valueCheck to https://<URL of the CAS application>/cas/logout

Then set the ``sso_class`` environment variable as below:

.. code-block:: xml
        :linenos:

   		<Environment name="sso_class" type="java.lang.String" value="it.eng.spagobi.services.cas.CasSsoService3NoProxy"/>  
   
This variable is located:

* Tomcat: in the ``TOMCAT_HOME/conf/server.xml``
* JBoss: in the ``JBOSS_HOME/ standalone/configuration/standalone.xml``
 
Edit all ``knowage\WEB-INF\web.xml`` to activate CAS filters.

.. code-block:: xml
        :linenos:
        :caption: Setting the CAS filters for sso_class variable.
	
      	<filter>                                                              
          <filter-name>CAS Authentication Filter</filter-name>               
          <filter-class>org.jasig.cas.client.authentication.AuthenticationFilter</filter-class>                                         
          <init-param>                                                       
           <param-name>casServerLoginUrl</param-name>                         
            <param-value>https://<nome del server CAS>/cas/login</param-value> 
          </init-param>                                                      
          <init-param>                                                       
           <param-name>serverName</param-name>                                
            <param-value><dominio di knowage, incluso il protocollo e la porta, se non standard></param-value>                             
          </init-param>                                                      
       	</filter> 
       
       	<filter>                                                              
          <filter-name>CAS Validation Filter</filter-name>                   
          <filter-class>org.jasig.cas.client.validation.Cas20ProxyReceivingTicketValidationFilter</filter-class>           
          <init-param>                                                       
          	<param-name>casServerUrlPrefix</param-name>                        
          	<param-value>https://<nome del server CAS>/cas/</param-value>      
         	</init-param>                                                      
          <init-param>                                                       
          	<param-name>serverName</param-name>                                
          	<param-value><dominio di Knowage Server, incluso il protocollo e la porta, se non standard></param-value>
		
          </init-param>                                                      
          <init-param>                                                       
          	<param-name>proxyReceptorUrl</param-name>                          
          	<param-value>/proxyCallback</param-value>                          
          </init-param>                                                      
      
      	[Nelle web application knowageXXXengine presente anche questo parametro:
	
        <init-param> <param-name>proxyCallbackUrl</param-name>             
      	<param-value>                                                      
           <dominio di knowage Server, incluso il protocollo e la porta, se  non standard>/< knowageXXXengine>/proxyCallback </param-value>     
        </init-param>]
        
       	</filter>   
      
       	<filter>                                                              
          <filter-name>CAS HttpServletRequest Wrapper Filter</filter-name>   
          <filter-class>org.jasig.cas.client.util.HttpServletRequestWrapperFtilter</filter-class>
	  
      	</filter>...
      
      	<filter-mapping>                                                    
       	 <filter-name>CAS Authentication Filter</filter-name>                
         <url-pattern>/servlet/*</url-pattern>                               
      	</filter-mapping>                                                   
      
        <filter-mapping>                                                    
         <filter-name>CAS Validation Filter</filter-name>                    
         <url-pattern>/servlet/*</url-pattern>                               
      	</filter-mapping>                                                   
         <filter-mapping>                                                    
         <filter-name>CAS HttpServletRequest Wrapper Filter</filter-name>    
         <url-pattern>/servlet/*</url-pattern>                               
       	</filter-mapping>
        
      	[Nelle web application knowageXXXengine presente anche questo mapping: 
      	 <filter-mapping>                                                    
          <filter-name>CAS Validation Filter</filter-name>                    
          <url-pattern>/proxyCallback</url-pattern>                           
          </filter-mapping>]                                     

All ``web.xml`` files have CAS filters already configured, but they are commented. The user must uncomment them, looking for the strings ``START-CAS``, ``END-CAS`` and adjust the URL as the code abow reports.
