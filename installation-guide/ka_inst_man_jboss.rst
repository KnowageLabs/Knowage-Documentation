
JBoss AS Manual Installation
==========================

Metadata database
-------------------

The metadata database must contains a schema which will collect all Knowage metadata. For configuring such a schema, the user must execute the creation scripts provided for the DBMS in use. The package which includes the DDL will contain the following scripts in :numref:`scriptsformetadat`:

.. _scriptsformetadat:
.. code-block:: bash
        :linenos:
        :caption: Scripts for metadata schema.
 
        XXX_create.sql                                            
        XXX_create_quartz_schema.sql

where XXX represents the DBMS type, for instance ORA stands for Oracle. Inside the packages there are the corresponding files for deleting tables.

Dependencies
-------------------
You must add some modules inside the folder JBOSS_HOME/modules/system/layers/base:

- the JDBC module of the metadata database with its dependencies (if any);
- the JDBC module of the data database with its dependencies (if any);
- the module which includes the commonj library with its dependencies (if any):

   - geronimo-commonj_1.1_spec-1.0.jar,
   - concurrent.jar,
   - foo-commonj.jar;

- the Resteasy Jackson2 Provider module;
- the fasterxml Classmate, Jackson Core e Jackson JAXRS modules.

File system resources
---------------------

In the JBoss instance, create the folder JBOSS_HOME/standalone/data/resources. Equally in the Tomcat instance, create the folder TOMCAT_HOME/resources. Such a folder will contain some useful static resources and the indexes for the research engine used by Knowage.

Metadata database connection
----------------------------
In the JBoss case, edit the file JBOSS_HOME/standalone/configuration/standalone.xml and add the information related to the metadata database inside the “datasources” tag: specify the username, the password and driver class name, URL, connection checker class and exception sorter class. The following :numref:`settingthemetadatadata` is an example:

.. _settingthemetadatadata:
.. code-block:: xml
        :linenos:
        :caption: Setting the metadata datasource.
        
	<datasource jndi-name="java:/jdbc/knowage" pool-name="knowage">       
	<connection-url> <JDBC URL> </connection-url>                         
	<driver> <JDBC driver> </driver>                                      
	<security>                                                            
	<user-name> user name> </user-name>                                   
	<password> <password> </password>                                     
	</security>                                                           
	<validation>                                                          
	<validate-on-match>true</validate-on-match>                           
	<background-validation>false</background-validation>                  
		<valid-connection-checker class-name="<connection checkerclass>"/> 
		<exception-sorter class-name="<exception sorter class>"/>          
		</validation>                                                      
	</datasource>  

In addition, remember to type the information related to the JDBC driver inside the drivers tag before defining the connection. Below an example:

.. code-block:: xml
        :linenos:

         <driver name="<driver class>" module="<module name>" /> 

Data database connection
------------------------

Edit the JBOSS_HOME/standalone/configuration/standalone.xml and add the information related to the data database inside the datasources tag. Specify: username, password, driver class name, URL, connection checker class and exception sorter class. The following :numref:`settingthemetadatadataso` shows an example:

.. _settingthemetadatadataso:
.. code-block:: xml
        :linenos:
        :caption: Setting the metadata datasource.

        <datasource jndi-name="java:/jdbc/dwh" pool-name="knowage">           
            <connection-url> <JDBC URL> </connection-url>                      
            <driver> <JDBC driver> </driver>                                   
            <security>                                                         
            <user-name> <user name> </user-name>                               
            <password> <password> </password>                                  
            </security>                                                        
            <validation>                                                       
            <validate-on-match>true</validate-on-match>                        
            <background-validation>false</background-validation>               
            <valid-connection-checker class-name="<connection checker class>"/>
            <exception-sorter class-name="<exception sorter class>"/>          
            </validation>                                                      
        </datasource>                                                         

In addition, remember to type the information related to the JDBC driver inside the drivers tag before defining the connection. Code is an example:

.. code-block:: xml
        :linenos:

        <driver name="<driver class>" module="<module name>" /> 

Environment variables definition
--------------------------------
Edit the JBOSS_HOME/standalone/configuration/standalone.xml and add the following constants inside the subsystem domain naming tab, by setting the domain within the host_url value. That domain will be used by the browser to call Knowage server, as we can see in :numref:`jbossenvironmentvariables`:

.. _jbossenvironmentvariables:
.. code-block:: xml
        :linenos:
        :caption: JBoss environment variables configuration.

         <bindings>                                                            
              <simple name="java:/urls/resource_path" type="java.lang.String"    
              value="${jboss.server.data.dir}/resources" />                      
              <simple name="java:/urls/sso_class" type="java.lang.String"        
              value="it.eng.spagobi.services.common.JWTSsoService" /> <simple   
              name="java:/urls/service_url" type="java.lang.String"              
              value="http:// localhost:8080/knowage" />                          
              <simple name="java:/urls/host_url" type="java.lang.String"         
              value="<server url which is hosting knowage>"/>                    
        </bindings>                                                           

      

Constants have the following meaning:

- **resource\ \_\ path**: resources folder path,
- **sso_class**:SSO connector class name,
- **service\ \_\ url**:backend services address, typically set to `http://localhost:8080/knowage, <http://localhost:8080/knowage>`__
- **host\_\ url**: frontend services address, the one the user types in his browser.

Applications deploy
-------------------

Execute the following steps:

- copy all the WAR files inside the JBOSS_HOME/standalone/deployments;
- extract the content of each WAR file into (using for instance the unzip utility) one directory with the same name, including the “.war” suffix (for istance, “knowage.war”;
- delete the WAR files;
- create an empty file for each WAR file with the same name plus the suffix “.dodeploy” (for example, “knowage.war.dodeploy“).

Please refer to the instructions that are written in the JBOSS_HOME/standalone/deployments/README.txt. 

Datasource link within the applications
---------------------------------------

Control that in all the JBOSS_HOME/standalone/deployments/knowage*.war/META-INF/context.xml files there are the links reported in :numref:`datasourcelink`:

.. _datasourcelink:
.. code-block:: xml
        :linenos:
        :caption: DataSource link syntax.

 	<ResourceLink global="jdbc/knowage" name="jdbc/knowage" type="javax.sql. DataSource"/>
	<ResourceLink global="jdbc/dwh" name="jdbc/dwh" type="javax.sql.DataSource"/>                                         


Configuration of the metadata db dialect
----------------------------------------
Verify that the right dialect has been set in all JBOSS_HOME/standalone/deployments/knowage*.war/WEB-INF/classes/hibernate.cfg.xml files.

-  <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>,
-  <property name="hibernate.dialect">org.hibernate.dialect.SQLServerDialect</property>
-  <property name="hibernate.dialect">org.hibernate.dialect.PostgreSQLDialect</property>
-  <property name="hibernate.dialect">org.hibernate.dialect.Oracle9Dialect</property>


**Remark.** The modification of these files will be effective as soon as the web application is reloaded or the application server is restarted.

Modification of the Quartz configuration
----------------------------------------
The scheduler is configured by the following file: knowage.war/WEB-INF/classes/quartz.properties. It is essential to enhance in this file the property ”org.quartz.jobStore.driverDelegateClass“ with the right value, according to the metadata database in use. These in :numref:`valuesfortheqz` the possible values:

.. _valuesfortheqz:
.. code-block:: bash
        :linenos:
        :caption: Values for the Quartz file.

 	# Hsqldb delegate class                                                                                
 	#org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.HSQLDBDelegate          
 	# Mysql delegate class org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.StdJDBCDelegate          
 	# Postgres delegate class                                                                     
 	#org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.PostgreSQLDelegate      
 	# Oracle delegate class                                                                       
 	#org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.oracle.OracleDelegate
	


Pool of thread definition
-------------------------

When Knowage is installed in cluster with several nodes, it is necessary to activate the Cluster modality, adding these parameters, in :numref:`clustermodalityman`, to the quartz.properties file of every involved machines:

.. _clustermodalityman:
.. code-block:: bash
        :linenos:
        :caption: Cluster modality manual activation.

 	org.quartz.jobStore.isClustered = true
 	org.quartz.jobStore.clusterCheckinInterval = 20000
 
	org.quartz.scheduler.instanceId = AUTO
 	org.quartz.scheduler.instanceName = RHECMClusteredSchedule

Pool of thread definition
-------------------------

For the execution of the batch processing ,Knowage uses a thread pool. In the JBoss case it is possible to modify the configuration by editing the JBOSS_HOME/standalone/configuration/standalone.xml and adding the configuration related to thread pool inside the **subsystem domain naming** tag, as showed in :numref:`threadpoolconf`:

.. _threadpoolconf:
.. code-block:: xml
        :linenos:
        :caption: Thread pool configuration for JBoss.

 	<bindings>                                                            
	<object-factory name="java:/global/SpagoWorkManager" module="de.myfoo.commonj" class="de.myfoo.commonj.work.MyFooWorkManagerFactory">
	<environment>                                                         
        <property name="maxThreads" value="5"/>                               
        <property name="minThreads" value="1"/>                               
        <property name="queueLength" value="10"/>                             
        <property name="maxDaemons" value="10"/>                              
        </environment>                                                        
        </object-factory>                                                     
        </bindings>                                                           


Check of the memory settings
----------------------------

It is recommended to increase the memory dimension used by the application server; this can be done by adjusting some properties. The memory space required by each application server depends on several different factors: number of users, analysis type, amount of handled data, etc. The smallest memory requirements are:

-  Xms1024m;
-  Xmx2048m;


**JBoss**

**[LINUX]** Insert at the beginning of the JBOSS_HOME/bin/run.conf.bat file the row in :numref:`memorysettingslin`:

.. _memorysettingslin:
.. code-block:: bash
        :linenos:
        :caption: Memory settings for JBoss in Linux environment.

	export JAVA_OPTS="$JAVA_OPTS -Xms1024m -Xmx2048m -XX:MaxPermSize=512m" 

**[WIN]** Insert at the beginning of the JBOSS_HOME/bin/run.conf.sh file the row in :numref:`memorysettingswind`:

.. _memorysettingswind:
.. code-block:: bash
        :linenos:
        :caption: Memory settings for JBoss in Windows environment.

	set JAVA_OPTS= %JAVA_OPTS% -Xms1024m Xmx2048m -XX:MaxPermSize=512m

LOG files
---------

It is necessary to arrange a folder where Knowage and its analytical engines can store their respective log files. From now on, we will call LOG_DIR such folder and LOG_DIR_PATH the path that leads to it. This path is configured in file log4j.properties located inside the *\\*\ WEB-INF\ *\\*\ classes\ *\\* available in each web application.
In short, to configure the Knowage log folder the user must execute the following steps:

- create the LOG_DIR folder on all cluster nodes on which it is intended to deploy Knowage Server and/or one of its analytical engines. The LOG_DIR_PATH string must be the same for every node;

- **[LINUX]** verify that Knowage has write permissions on this folder; set the property :`log4j.appender.knowage.File` inside the WEB-INF/classes/log4j.properties Knowage file to LOG_DIR_PATH/knowage.log;

- set the property :`log4j.appender.knowageXXXXXEngine.File` inside the :`WEB-INF/classes/log4j.properties` file of each engine to LOG_DIR_PATH/knwoageXXXXXEngine.log;
- only for the Birt Engine, to set the property logDirectory inside the WEB-INF/classes/BirtLogConfig.properties file of the knowagebirtreportengine application toLOG\ :`\_`\ DIR\ :`\_`\ PATH.

In case you are using JBoss , in all configuration log4j.properties files substitute the string ”catalina.base/logs“ with "jboss.server.log.dir”.

Configuration file
------------------
It is necessary to modify some configuration files reported in :numref:`stringreplacc`. Apply the string replacements for each web application.
Moreover, apply the string substitutions to the configs.xml file included in the JBOSS_HOME/standalone/deploymen file, as reported in :numref:`stringreplacctothe`:

.. _stringreplacc:
.. table:: String replacements according to the web application.
    :widths: auto

    +----------------------+------------------------------+--------------------------+
    |    **File name**     | **Original string**          | **New string**           |
    +======================+==============================+==========================+
    | hibernate.cfg.xml    | java:/comp/env/jdbc/knowage  | java:/jdbc/knowage       |
    +----------------------+------------------------------+--------------------------+
    | quartz.properties    | java:/comp/env/jdbc/knowage  | java:/jdbc/knowage       |
    +----------------------+------------------------------+--------------------------+
    | engine config.xml    | java:/comp/env/resource_path | java:/urls/resource_path |
    +                      +------------------------------+--------------------------+
    |                      | java:/comp/env/service_url   | java:/urls/service_url   |
    +                      +------------------------------+--------------------------+
    |                      | java:/comp/env/sso_class     | java:/urls/sso_class     |
    +                      +------------------------------+--------------------------+
    |                      | java:/comp/env/hmacKey       | java:/urls/hmacKey       |
    +----------------------+------------------------------+--------------------------+

.. _stringreplacctothe:
.. table:: String replacements according to the web application.
    :widths: auto

    +------------------+------------------------------+--------------------------+
    |    **File name** | **Original string**          | **New string**           |
    +==================+==============================+==========================+
    |    configs.xml   | java:/comp/env/resource_path | java:/urls/resource_path |
    +                  +------------------------------+--------------------------+
    |                  | java:/comp/env/service_url   | java:/urls/service_url   |
    +                  +------------------------------+--------------------------+
    |                  | java:/comp/env/sso_class     | java:/urls/sso_class     |
    +                  +------------------------------+--------------------------+
    |                  | java:/comp/env/hmacKey       | java:/urls/hmacKey       |
    +------------------+------------------------------+--------------------------+

**Remark.** The configs.xml file is used to initialize some configuration tables on the database, therefore the user must set these adjustments before the server is launched. Furthermore, the user must apply the modifications listed below in all configuration web.xml files of each web application:

-  uncomment all blocks bounded by the comments “START JBOSS RES” and “END JBOSS RES”;
-  comment all blocks bounded by the comments “START TOMCAT RES” and “END TOMCAT RES”;
-  comment all blocks bounded by the comments “START ProxyTicketReceptor” and “END ProxyTicketReceptor”.

JAR library file
----------------

Considering the JBoss instance, delete all of the following files from each web application:

-  WEB-INF/lib/jaxrs-api-2.3.5.Final.jar;
-  WEB-INF/lib/resteasy-jaxb-provider-2.3.5.Final.jar;
-  WEB-INF/lib/resteasy-jaxrs-2.3.5.Final.jar;
-  WEB-INF/lib/resteasy-multipart-provider-2.3.5.final.jar.

Moreover, still for JBoss delete only from the Knowage web application the following files:

-  WEB-INF/tlds/liferay-portlet.tld;
-  WEB-INF/tlds/portlet.tld;
-  WEB-INF/lib/resteasy-jackson2-provider-3.0.9.Final.jar.

server-config.wsdd tests
------------------------
In Knowage server the core and its analytical engines exchange information through some SOAP services. Those services can send/receive attached files: those files are temporarely stored in a folder that is configured in the knowage/WEB-INF/server-config.wsdd file. The :numref:`confofthefl` shows the syntax.

.. _confofthefl:
.. code-block:: bash
        :linenos:
        :caption: Configuration of the files.

	<parameter name="attachments.Directory" value="../attachments"/>

Obviously it is possible to modify the folder path, but the user who starts the application server is required to have indeed write permissions in the configured folder.
