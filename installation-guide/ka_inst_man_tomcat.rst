

Tomcat AS Manual Installation
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
You must add some libraries inside the TOMCAT_HOME/lib folder:

-  the JDBC module of the metadata database with its dependencies (if any);
-  the JDBC module of the data database with its dependencies (if any);
-  the module which includes the commonj library with its dependencies (if any):

   -  geronimo-commonj_1.1_spec-1.0.jar,
   -  concurrent.jar,
   -  foo-commonj.jar.
   
You can download here `Libraries <media/lib.zip>`_




File system resources
---------------------

Create the folder TOMCAT_HOME/resources. Such a folder will contain some useful static resources and the indexes for the research engine used by Knowage.



Metadata database connection
----------------------------
To create a new connection, edit the TOMCAT_HOME/conf/server.xml and add the information related to the metadata database inside the GlobalNamingResources tag. Specify: username, password, driver class name and URL. 
We need to create 2 connection:
   - knowage metadata 
   - Knowage cache, this must be an emty schema

The following xml fragment shows an example:

.. code-block:: xml

 <Resource auth="Container" 
		driverClassName="<JDBC driver>" 
		name="jdbc/knowage"
		password="<password>" 
		type="javax.sql.DataSource" 
		url="<JDBC URL>" 
		username="<user name>"
		maxWait="-1" 
		maxActive="10" 
		maxIdle="1" 
		validationQuery="<validation query>" 
		removeAbandoned="true" 
		removeAbandonedTimeout="3600" 
		logAbandoned="true" 
		testOnReturn="true" 
		testWhileIdle="true" 
		timeBetweenEvictionRunsMillis="10000" 
		minEvictableIdleTimeMillis="60000" 
	factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" />   

 <Resource auth="Container" 
		driverClassName="<JDBC driver>" 
		name="jdbc/cache_ds"
		password="<password>" 
		type="javax.sql.DataSource" 
		url="<JDBC URL>" 
		username="<user name>"
		maxWait="-1" 
		maxActive="10" 
		maxIdle="1" 
		validationQuery="<validation query>" 
		removeAbandoned="true" 
		removeAbandonedTimeout="3600" 
		logAbandoned="true" 
		testOnReturn="true" 
		testWhileIdle="true" 
		timeBetweenEvictionRunsMillis="10000" 
		minEvictableIdleTimeMillis="60000" 
		factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" />

Data database connection
------------------------
In the Tomcat case, edit the TOMCAT_HOME/conf/server.xml and add the information related to the metadata database inside the GlobalNamingResources tag. Specify: username, password, driver class name and URL. 
The following xml fragment shows an example:

.. code-block:: xml

 <Resource auth="Container" 
		driverClassName="<JDBC driver>" 
		name="jdbc/dwh"
		password="<password>" 
		type="javax.sql.DataSource" 
		url="<JDBC URL>" 
		username="<user name>"
		maxWait="-1" 
		maxActive="10" 
		maxIdle="1" 
		validationQuery="<validation query>" 
		removeAbandoned="true" 
		removeAbandonedTimeout="3600" 
		logAbandoned="true" 
		testOnReturn="true" 
		testWhileIdle="true" 
		timeBetweenEvictionRunsMillis="10000" 
		minEvictableIdleTimeMillis="60000" 
		factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" />


Environment variables definition
--------------------------------
Edit the file TOMCAT_HOME/conf/server.xml in Tomcat and add the following constants in the GlobalNamingResources tag, by setting the domain within the host_url value. That domain will be used by the browser to call Knowage server, as we can see in :numref:`tomcatoenvironmentvariab`:

.. _tomcatoenvironmentvariab:
.. code-block:: xml
        :linenos:
        :caption: Tomcat environment variables configuration.

        <Environment name="resource_path" type="java.lang.String" value="${catalina.home}/resources"/>                 
                                                                                                                
        <Environment name="sso_class" type="java.lang.String" value="it.eng.spagobi.services.common.FakeSsoService"/> 
                                                                                                                
        <Environment name="service_url" type="java.lang.String" value="http://localhost:8080/knowage"/>               
                                                                                                                
        <Environment name="host_url" type="java.lang.String" value="<server URL which is hosting knowage>"/>            

In both case cases, constants have the following meaning:

- **resource\ \_\ path**: resources folder path,
- **sso_class**:SSO connector class name,
- **service\ \_\ url**:backend services address, typically set to `http://localhost:8080/knowage, <http://localhost:8080/knowage>`__
- **host\_\ url**: frontend services address, the one the user types in his browser.

Applications deploy
-------------------
To deploy knowage you have to copy all the WAR files inside the TOMCAT_HOME/webapps folder. 
Once the first start is ended each WAR file will be unzipped. It is also possible to unzip the WAR files manually using the unzip utility.


Datasource link within the applications
---------------------------------------
Control in the TOMCAT_HOME/webapps/knowage*/META-INF/context.xml and set the ResourceLink for each data source created. 
Inside the released packages there are already two links: one for the jdbc/knowage resource, which the user must keep, and the other for the jdbc/foodmart, which should be renamed with jdbc/dwh, as above.
Here adn example:

.. code-block:: xml

 <Context docBase="knowage-ee" path="/knowage" reloadable="true">
        
	<ResourceLink global="jdbc/dwh" name="jdbc/dwh" type="javax.sql.DataSource"/>
        
	<ResourceLink global="jdbc/knowage" name="jdbc/knowage" type="javax.sql.DataSource"/>
        <ResourceLink global="jdbc/ds_cache" name="jdbc/ds_cache" type="javax.sql.DataSource"/>
	
        <ResourceLink global="resource_path" name="resource_path" type="java.lang.String" />
        <ResourceLink global="sso_class" name="sso_class" type="java.lang.String" />
        <ResourceLink name="hmacKey" global="hmacKey" type="java.lang.String"/>
        <ResourceLink global="host_url" name="host_url" type="java.lang.String" />
        <ResourceLink global="service_url" name="service_url" type="java.lang.String"/>
        <ResourceLink global="wm/SpagoWorkManager" name="wm/SpagoWorkManager" type="commonj.work.WorkManager" />
   </Context>
 
**Remark.** The modification of these files will be effective as soon as the web application is reloaded or the application server is restarted.

Configuration of the metadata db dialect
----------------------------------------
Verify that the right dialect has been set inside **hibernate.cfg.xml** files. We list all the possible dialects that can be used:

.. code-block:: xml

 <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>,
 <property name="hibernate.dialect">org.hibernate.dialect.SQLServerDialect</property>
 <property name="hibernate.dialect">org.hibernate.dialect.PostgreSQLDialect</property>
 <property name="hibernate.dialect">org.hibernate.dialect.Oracle9Dialect</property>

You have to change these files:

- <TOMCAT_HOME>/webapps/knowagekpiengine/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowagegeoreportengine/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowage/WEB-INF/classes/hsql/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowage/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowagesvgviewerengine/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowagemeta/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowagecockpitengine/WEB-INF/classes/hibernate.cfg.xml
- <TOMCAT_HOME>/webapps/knowagedataminingengine/WEB-INF/classes/hibernate.cfg.xml


**Remark.** The modification of these files will be effective as soon as the web application is reloaded or the application server is restarted.

Modification of the Quartz configuration
----------------------------------------
The scheduler is configured by the following file: knowage.war/WEB-INF/classes/quartz.properties. It is essential to enhance in this file the property ”org.quartz.jobStore.driverDelegateClass“ with the right value, according to the metadata database in use. Following the possible values:

.. code-block:: bash

 # Hsqldb delegate class                                                                                
 #org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.HSQLDBDelegate          
 # Mysql delegate class org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.StdJDBCDelegate          
 # Postgres delegate class                                                                     
 #org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.PostgreSQLDelegate      
 # Oracle delegate class                                                                       
 #org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.oracle.OracleDelegate
	


Pool of thread definition
-------------------------
When Knowage is installed in cluster with several nodes, it is necessary to activate the Cluster modality, adding these parameters to the quartz.properties file of every involved machines:

.. code-block:: bash

 org.quartz.jobStore.isClustered = true
 org.quartz.jobStore.clusterCheckinInterval = 20000
 
 org.quartz.scheduler.instanceId = AUTO
 org.quartz.scheduler.instanceName = RHECMClusteredSchedule

Pool of thread definition
-------------------------
For the execution of the batch processing ,Knowage uses a thread pool, it is possible to enable it by editing the configuration of the TOMCAT_HOME/conf/server.xml file and add the settings related to the pool of thread editing the **GlobalNamingResources** tag, as shown follow.

.. code-block:: xml

 <Resource auth="Container" factory="de.myfoo.commonj.work.FooWorkManagerFactory" maxThreads="5" name="wm/SpagoWorkManager" type="commonj.work.WorkManager"/> 


Check of the memory settings
----------------------------

It is recommended to increase the memory dimension used by the application server; this can be done by adjusting some properties. The memory space required by each application server depends on several different factors: number of users, analysis type, amount of handled data, etc. The smallest memory requirements are:

-  Xms1024m;
-  Xmx2048m;

**[LINUX]** Insert at the beginning of the TOMCAT_HOME/bin/setenv.sh file this command:

.. code-block:: bash

 export JAVA_OPTS="$JAVA_OPTS -Xms1024m -Xmx2048m -XX:MaxPermSize=512m" 


**[WIN]** Insert at the beginning of the TOMCAT_HOME/bin/setenv.bat file this command:

.. code-block:: bash

 set JAVA_OPTS= %JAVA_OPTS% -Xms1024m Xmx2048m -XX:MaxPermSize=512m


If one uses Tomcat as a service it is important to modify those settings through the GUI. For that we refer to the documents available on the web page  http://www.apache.org/ 

LOG files
---------

It is necessary to arrange a folder where Knowage and its analytical engines can store their respective log files. From now on, we will call LOG_DIR such folder and LOG_DIR_PATH the path that leads to it. This path is configured in file log4j.properties located inside the *\\*\ WEB-INF\ *\\*\ classes\ *\\* available in each web application.
In short, to configure the Knowage log folder the user must execute the following steps:

- create the LOG_DIR folder on all cluster nodes on which it is intended to deploy Knowage Server and/or one of its analytical engines. The LOG_DIR_PATH string must be the same for every node;

- **[LINUX]** verify that Knowage has write permissions on this folder; set the property :`log4j.appender.knowage.File` inside the WEB-INF/classes/log4j.properties Knowage file to LOG_DIR_PATH/knowage.log;

- set the property :`log4j.appender.knowageXXXXXEngine.File` inside the :`WEB-INF/classes/log4j.properties` file of each engine to LOG_DIR_PATH/knwoageXXXXXEngine.log;
- only for the Birt Engine, to set the property logDirectory inside the WEB-INF/classes/BirtLogConfig.properties file of the knowagebirtreportengine application toLOG\ :`\_`\ DIR\ :`\_`\ PATH.


server-config.wsdd tests
------------------------
In Knowage server the core and its analytical engines exchange information through some SOAP services. Those services can send/receive attached files: those files are temporarely stored in a folder that is configured in the knowage/WEB-INF/server-config.wsdd file. Here the syntax.

.. code-block:: bash
 <parameter name="attachments.Directory" value="../attachments"/>

Obviously it is possible to modify the folder path, but the user who starts the application server is required to have indeed write permissions in the configured folder.
