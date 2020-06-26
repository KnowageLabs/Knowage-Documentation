Using Tomcat
----------------

Dependencies
~~~~~~~~~~~~
You must add required libraries into ``TOMCAT_HOME/lib`` folder:

-  the JDBC connector for the metadata database with its dependencies (if any);
-  the JDBC connector for the business data database with its dependencies (if any);
-  the commonj library with its dependencies:

   -  `Apache Geronimo <https://search.maven.org/remotecontent?filepath=org/apache/geronimo/specs/geronimo-commonj_1.1_spec/1.0/geronimo-commonj_1.1_spec-1.0.jar>`_,
   -  `Concurrency JSR-166 <https://search.maven.org/remotecontent?filepath=org/lucee/oswego-concurrent/1.3.4/oswego-concurrent-1.3.4.jar>`_,
   -  `CommonJ <https://github.com/SpagoBILabs/SpagoBI/raw/mvn-repo/releases/de/myfoo/commonj/1.0/commonj-1.0.jar>`_.

.. important::
         **Enterprise Edition only**

         To enable the Import/Export capability, please also add the JDBC connector for `HyperSQLDB <https://repository.jboss.org/nexus/content/repositories/thirdparty-releases/hsqldb/hsqldb/1.8.0.2/hsqldb-1.8.0.2.jar>`_ , taking care of using version 1.8.0.2 .


File system resources
~~~~~~~~~~~~~~~~~~~~~~~~

Create the folder ``TOMCAT_HOME/resources``. Such a folder will contain some useful static resources and the indexes for the search engine used by Knowage.

Connection to metadata database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To define connection towards metadata database, edit the ``TOMCAT_HOME/conf/server.xml`` and add the information related to the metadata database inside the ``GlobalNamingResources`` tag. Specify: username, password, driver class name, JDBC URL and validation query (any valid query to be executed to validate connections). Connection's name must the ``jdbc/knowage``:

.. code-block:: xml
 :linenos:

    <Resource auth="Container"
    	driverClassName="<JDBC driver>"
    	name="jdbc/knowage"
    	password="<password>"
    	type="javax.sql.DataSource"
    	url="<JDBC URL>"
    	username="<user name>"
    	validationQuery="<validation query>"
    	maxTotal="50"
    	maxIdle="50"
    	minIdle="10"
    	validationInterval="34000"
    	removeAbandoned="true"
    	removeAbandonedTimeout="3600"
    	logAbandoned="true"
    	testOnBorrow="true"
    	testWhileIdle="true"
    	timeBetweenEvictionRunsMillis="10000"
    	minEvictableIdleTimeMillis="60000" />


Cache database connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some scenarios (for example when defining a cockpit document on top of a file dataset), Knowage requires a database to be used as cache. It is highly recommended to create an empty database schema for this purpose. Then, you need to configure it inside ``TOMCAT_HOME/conf/server.xml`` as you did for metadata database. Feel free to type a name of your choice, in this example we used ``jdbc/ds_cache``:

.. code-block:: xml
 :linenos:

    <Resource auth="Container"
    	driverClassName="<JDBC driver>"
    	name="jdbc/ds_cache"
    	password="<password>"
    	type="javax.sql.DataSource"
    	url="<JDBC URL>"
    	username="<user name>"
    	validationQuery="<validation query>"
    	maxTotal="50"
    	maxIdle="50"
    	minIdle="10"
    	validationInterval="34000"
    	removeAbandoned="true"
    	removeAbandonedTimeout="3600"
    	logAbandoned="true"
    	testOnBorrow="true"
    	testWhileIdle="true"
    	timeBetweenEvictionRunsMillis="10000"
    	minEvictableIdleTimeMillis="60000" />


Connection to business data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the ``TOMCAT_HOME/conf/server.xml`` and add the information related to the database containing business data to be analysed by Knowage inside the ``GlobalNamingResources`` tag, specifying username, password, driver class name, URL and validation query. Feel free to type a name of your choice, in this example we used ``jdbc/dwh``:

.. code-block:: xml
 :linenos:

  <Resource auth="Container"
  	driverClassName="<JDBC driver>"
  	name="jdbc/dwh"
  	password="<password>"
  	type="javax.sql.DataSource"
  	url="<JDBC URL>"
  	username="<user name>"
  	validationQuery="<validation query>"
  	maxTotal="50"
  	maxIdle="50"
  	minIdle="10"
  	validationInterval="34000"
  	removeAbandoned="true"
  	removeAbandonedTimeout="3600"
  	logAbandoned="true"
  	testOnBorrow="true"
  	testWhileIdle="true"
  	timeBetweenEvictionRunsMillis="10000"
  	minEvictableIdleTimeMillis="60000"
  	factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" />


Environment variables definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the file ``TOMCAT_HOME/conf/server.xml`` in Tomcat and add the following constants in the ``GlobalNamingResources`` tag, by setting the domain within the ``host_url`` value. That domain will be used by the browser to call Knowage server.

.. code-block:: xml
        :linenos:
        :caption: Tomcat environment variables configuration.

  <Environment name="resource_path" type="java.lang.String" value="${catalina.home}/resources"/>
  <Environment name="sso_class" type="java.lang.String" value="it.eng.spagobi.services.common.JWTSsoService"/>
  <Environment name="service_url" type="java.lang.String" value="http://localhost:8080/knowage"/>
  <Environment name="host_url" type="java.lang.String" value="<server URL which is hosting knowage>"/>
  <Environment name="hmacKey" description="HMAC key" type="java.lang.String" value="<hmac_secret_key_to_substitute>"/>
  <Environment name="password_encryption_secret" description="File for security encryption location" type="java.lang.String" value="<complete_file_path_with_file_name>"/>

Such environment variables have the following meaning:

- ``resource_path``: resources folder path,
- ``sso_class``:SSO connector class name,
- ``service_url``:backend services address, typically set to ``http://localhost:8080/knowage``,
- ``host_url``: frontend services address, the one the user types in his browser.
- ``hmacKey``: secret key to generate JWT tokens used by the default security mechanism. You **must change** it, and **do not distribute** it.
- ``password_encryption_secret``: File used for password encryption. The file must contain random text of any length. This is a security configuration, so don't use short strings. For example, you can create a file and write text into it. **Do not distribute** it for any reason.

Below you can see an example of configuration of the above variables in the server.xml file

.. code-block:: xml
 :linenos:

  <Environment name="resource_path" type="java.lang.String" value="${catalina.home}/resources"/>
  <Environment name="sso_class" type="java.lang.String" value="it.eng.spagobi.services.common.JWTSsoService"/>
  <Environment name="host_url" type="java.lang.String" value="http://localhost:8080"/>
  <Environment name="service_url" type="java.lang.String" value="http://localhost:8080/knowage"/>
  <Environment name="hmacKey" description="HMAC key" type="java.lang.String" value="<value_to_replace>"/>
  <Environment name="password_encryption_secret" description="File for security encryption location"
    type="java.lang.String" value="${catalina.home}/conf/knowage.secret"/>


Applications deploy
~~~~~~~~~~~~~~~~~~~~~~
To deploy Knowage you have to copy all the WAR files inside the ``TOMCAT_HOME/webapps`` folder.
Once the first start is ended each WAR file will be unzipped. It is also possible to unzip the WAR files manually using the unzip utility.


Thread pool defintion
~~~~~~~~~~~~~~~~~~~~~~
You must configure ``TOMCAT_HOME/conf/server.xml`` file and add the settings related to the pool of thread editing the ``GlobalNamingResources`` tag, as shown follow.

.. code-block:: xml
	:linenos:

	<Resource auth="Container" factory="de.myfoo.commonj.work.FooWorkManagerFactory" maxThreads="5" name="wm/SpagoWorkManager" type="commonj.work.WorkManager"/>


Advanced memory settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is recommended to increase the memory dimension used by the application server. This can be done by adjusting some properties. The memory required by each application server depends on many factors: number of users, type of analyses, amount of handled data, etc. The minimum requirements are ``Xms1024m`` and ``Xmx2048m``.

**[LINUX]** Insert at the beginning of the ``TOMCAT_HOME/bin/setenv.sh`` file this command:

.. code-block:: bash
	:linenos:

	export JAVA_OPTS="$JAVA_OPTS -Xms1024m -Xmx2048m -XX:MaxPermSize=512m"


**[WIN]** Insert at the beginning of the ``TOMCAT_HOME/bin/setenv.bat`` file this command:

.. code-block:: bash
	:linenos:

	set JAVA_OPTS= %JAVA_OPTS% -Xms1024m Xmx2048m -XX:MaxPermSize=512m
