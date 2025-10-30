KNOWAGE Community  Installation using Docker
########################################################################################################################

In this guide, you will find instructions on how to install KNOWAGE Community Edition using Docker.
You can install Knowage by connecting it to an existing external database, or by loading the Docker image of the MySQL database as well.

Repository cloning
------------------------------------------------------------------------------------------------------------------------
First f all, to install Knowage CE via Docker, you need to clone the GitHub repository:

.. code-block:: bash
   :caption: git command

        git clone https://github.com/KnowageLabs/Knowage-Server-Docker.git

Preparation of the Environment
------------------------------------------------------------------------------------------------------------------------
Access the project directory:

.. code-block:: bash
   :caption: shell command

      cd Knowage-Server-Docker

Configuration of Environment Variables
------------------------------------------------------------------------------------------------------------------------

Knowage requires several variables to be configured to launch correctly. 

These can be defined in the ``.env`` file present in the project directory.
KNOWAGE need to use 2 DB schema, one for the metadata and una for the temporary cache.

For an initial demo installation using the included database, you can keep the database configuration settings as default.
You must change them if you are using an existing external database — see **Using External Databases** section.

Data base parameters:

• **DB_HOST**: database host

• **DB_PORT**: database port

• **DB_DB**: database name

• **DB_USER**: database user

• **DB_PASS**: user password

• **CACHE_DB_HOST**: cache database host

• **CACHE_DB_PORT**: cache database port

• **CACHE_DB_DB**: name of the cache database

• **CACHE_DB_USER**: cache database user

• **CACHE_DB_PASS**: cache user password

• **HMAC_KEY**: HMAC key to configure in Tomcat, it is important to configure it carefully, avoiding the use of trivial or predictable strings, as this setup is used to generate the token.

• **PASSWORD_ENCRYPTION_SECRET**: key for password encryption. Key used to securely store user passwords

• **SENSIBLE_DATA_ENCRYPTION_SECRET**: key for encrypting sensitive data. It is used for data decryption functionalities.



Parameters in the docker-compose.yml file
------------------------------------------------------------------------------------------------------------------------

• **DB_DO_INITIALIZATION**: Defaults to true; Set to false to avoid initializing the database. This is useful when using an already initialized external database, see **Using External Databases** section.

• **HAZELCAST_HOSTS**: Comma-separated Hazelcast hosts (e.g., "host1,host2,host3")

• **HAZELCAST_PORT**: Hazelcast port (e.g., "5701")

• **PUBLIC_ADDRESS**: IP or hostname visible from the outside (e.g. http://$PUBLIC_ADDRESS:8080/knowage)  

• **DB_TYPE**: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• **CACHE_DB_TYPE**: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

Complete Installation
------------------------------------------------------------------------------------------------------------------------
To install all Knowage components without demo content, run:

.. code-block:: bash
   :caption: docker command

      podman compose up -d

Instead, if you want to  install the demo version with preconfigured reports, run:

.. code-block:: bash
   :caption: docker command

      podman compose -f docker-compose-demo.yml up -d


Components Installed
------------------------------------------------------------------------------------------------------------------------
• Knowage Tomcat with all packages

• Hazelcast

• KnowagePython for Python integration

• KnowageDB (metadata)

• KnowageCache (cache)

Access the web interface: http://localhost:18080/knowage


Changing the Access Port
------------------------------------------------------------------------------------------------------------------------

To change the port on which Knowage is exposed, edit the **docker-compose.yml file in the knowage service section.

.. code-block:: bash
   :caption: docker command

      version: "3.8"
         services:
         knowage:
            image: knowagelabs/knowage-server-docker:9.0
            hostname: knowage
         depends_on:
            - knowagedb
            - knowagecache
            - hazelcast
         ports:
            - "18080:8080"
         networks:
            - main


Using External Databases
------------------------------------------------------------------------------------------------------------------------
It may be useful to use an existing external database instead of the one included in the standard distribution. In that case, you should:

- Remove the knowagedb service from `docker-compose.yml`.

.. code-block:: bash
   :caption: docker compose fragment

        knowagedb:
         image: mariadb:10.3
            environment:
               - MYSQL_USER=$DB_USER
               - MYSQL_PASSWORD=$DB_PASS
               - MYSQL_DATABASE=$DB_DB
               - MYSQL_RANDOM_ROOT_PASSWORD=yes
            networks:
               - main
         volumes:
            - "db:/var/lib/mysql"

- Install the Knowage schema on your database via DDL, you can find here the DDL `<https://github.com/KnowageLabs/Knowage-Server/tree/knowage-server-9.0/knowagedatabasescripts>`_.

- Update the parameters in the `.env` file.

- Set **DB_DO_INITIALIZATION** : false.

The same applies to using an external database for the cache (knowagecache).

Adding JNDI Resources
------------------------------------------------------------------------------------------------------------------------
To add new JNDI resources, edit the following files:

• conf/context.xml.d/extContext

• conf/server.xml.d/extGlobalResources

Example of ResourceLink in extContext:

.. code-block:: xml
   :linenos:

      <ResourceLink global="jdbc/foodmart" name="jdbc/foodmart" type="javax.sql.DataSource" />

Example of Resource in extGlobalResources:

.. code-block:: xml
   :linenos:

      <Resource
    auth="Container"
    driverClassName="<DRIVER JDBC>"
    logAbandoned="true"
    maxTotal="20"
    maxIdle="4"
    maxWait="300"
    minEvictableIdleTimeMillis="60000"
    name="jdbc/<JNDI NAME>"
    password="<PASSWORD>"
    removeAbandoned="true"
    removeAbandonedTimeout="3600"
    testOnReturn="true"
    testWhileIdle="true"
    timeBetweenEvictionRunsMillis="10000"
    type="javax.sql.DataSource"
    url="jdbc:mysql://<IP ADRESS>:<PORT>/<DB NAME>"
    username="<USERNAME>"/>

Mounting volumes in ``docker-compose.yml`` in the volumes section of the knowage service:

- ./conf/confServerFoodmart:/home/knowage/apache-tomcat/conf/server.xml.d

- ./conf/context.xml.d:/home/knowage/apache-tomcat/conf/context.xml.d



How upgrade KNOWAGE version
------------------------------------------------------------------------------------------------------------------------

If you want to upgrade the KNOWAGE packages to the last patch version released ( eg. from 9.0.0  to 9.0.1) you have to:

.. code-block:: bash
   :caption: docker command

    podman compose down
    podman rmi <IMAGE ID>
    podman compose up -d

