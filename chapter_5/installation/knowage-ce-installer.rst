KNOWAGE Community  Installation using Docker
########################################################################################################################

Repository cloning
------------------------------------------------------------------------------------------------------------------------
To install Knowage CE via Docker, you need to clone the GitHub repository:

.. code-block:: bash

    git clone https://github.com/KnowageLabs/Knowage-Server-Docker.git

Preparation of the Environment
------------------------------------------------------------------------------------------------------------------------
Access the project directory:

.. code-block:: bash
    cd Knowage-Server-Docker

Configuration of Environment Variables
------------------------------------------------------------------------------------------------------------------------
Knowage requires several variables to be configured to launch correctly. 

These can be defined in the .env file present in the project directory.

Mandatory parameters:

• DB_HOST: database host

• DB_PORT: database port

• DB_DB: database name

• DB_USER: database user

• DB_PASS: user password

• DB_TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• CACHE_DB_HOST: cache database host

• CACHE_DB_PORT: cache database port

• CACHE_DB_DB: name of the cache database

• CACHE_DB_USER: cache database user

• CACHE_DB_PASS: cache user password

• CACHE_DB_TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• HMAC_KEY: HMAC key to configure in Tomcat

• PASSWORD_ENCRYPTION_SECRET: key for password encryption

• SENSIBLE_DATA_ENCRYPTION_SECRET: key for encrypting sensitive data

• DB_TYPE and CACHE_DB_TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• PUBLIC_ADDRESS: IP or hostname visible from the outside (e.g. http://$PUBLIC_ADDRESS:8080/knowage)

Parameters in the docker-compose.yml file
------------------------------------------------------------------------------------------------------------------------

• DB_DO_INITIALIZATION: Defaults to true; set to false to skip DB initialization.

• HAZELCAST_HOSTS: Comma-separated Hazelcast hosts (e.g., "host1,host2,host3")

• HAZELCAST_PORT: Hazelcast port (e.g., "5701")

Complete Installation
------------------------------------------------------------------------------------------------------------------------
To install all Knowage components, run:

.. code-block:: bash
    podman compose up -d

Components Installed
------------------------------------------------------------------------------------------------------------------------
• Knowage Tomcat with all packages

• Hazelcast for clustering

• KnowagePython for Python integration

• KnowageDB (metadata)

• KnowageCache (cache)

Access the web interface: http://localhost:18080/knowage-vue/

Changing the Access Port
------------------------------------------------------------------------------------------------------------------------

To change the port on which Knowage is exposed, edit the docker-compose.yml file in the knowage service section.

Using External Databases
------------------------------------------------------------------------------------------------------------------------
If you have an external database:

- Remove the knowagedb service from `docker-compose.yml`.

- Install the Knowage schema on your database via DDL.

- Update the parameters in the `.env` file.

- Set DB_DO_INITIALIZATION=false.

The same applies to using an external database for the cache (knowagecache).

Adding JNDI Resources
------------------------------------------------------------------------------------------------------------------------
To add new JNDI resources, edit the following files:

• conf/context.xml.d/extContext

• conf/server.xml.d/extGlobalResources

Example of ResourceLink in extContext:

<ResourceLink global="jdbc/foodmart" name="jdbc/foodmart" type="javax.sql.DataSource" />

Example of Resource in extGlobalResources:

<Resource
    auth="Container"
    driverClassName="com.mysql.jdbc.Driver"
    logAbandoned="true"
    maxTotal="20"
    maxIdle="4"
    maxWait="300"
    minEvictableIdleTimeMillis="60000"
    name="jdbc/foodmart"
    password="foodmart"
    removeAbandoned="true"
    removeAbandonedTimeout="3600"
    testOnReturn="true"
    testWhileIdle="true"
    timeBetweenEvictionRunsMillis="10000"
    type="javax.sql.DataSource"
    url="jdbc:mysql://foodmart:3306/foodmart"
    username="foodmart"/>

Mounting volumes in docker-compose.yml in the volumes section of the knowage service:

- ./conf/confServerFoodmart:/home/knowage/apache-tomcat/conf/server.xml.d

- ./conf/context.xml.d:/home/knowage/apache-tomcat/conf/context.xml.d

Installing the Demo Version
------------------------------------------------------------------------------------------------------------------------
To install the demo version with preconfigured reports:
.. code-block:: bash
    podman compose -f docker-compose-demo.yml up -d


