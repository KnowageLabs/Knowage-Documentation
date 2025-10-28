KNOWAGE Enterprise Installation using Docker
########################################################################################################################

Installation on the host machine of Docker/Podman.

Internet access from the host machine is required at the time of installation (for OS updates and Knowage image updates).

If internet access is not available, it will be necessary to manually transfer to the host machine both the “knowage-ee-server-docker” folder mentioned in paragraph 'Repository cloning' and manually copy the Knowage images.

Repository cloning
------------------------------------------------------------------------------------------------------------------------
To install Knowage EE via Docker, you need to clone the GitLab repository:

git clone https://production.eng.it/gitlab/KNOWAGE-LABS/knowage-ee-server-docker.git

access the project directory:

cd knowage-ee-server-docker

N.B. in the absence of an internet connection, the following files and folders must be copied to the host machine in the knowage-ee-server-docker folder

1. docker-compose.yaml

2. .env

3. hazelcast-server.xml

4. the “resources” folder

5. the “conf” folder

Configuration of Environment Variables
------------------------------------------------------------------------------------------------------------------------
Knowage requires several variables to be configured to launch correctly. 

These can be defined in the .env file present in the project directory.

Mandatory parameters:

• DB_HOST: database host

• DB_PORT: database port

• DB_DB: database name

• DB_USER: database user

• DB_PASS_ENCRYPTED: encrypted database password (see paragraph 'DB password encryption')

• DB_TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• CACHE_DB_HOST: cache database host

• CACHE_DB_PORT: cache database port

• CACHE_DB_DB: name of the cache database

• CACHE_DB_USER: cache database user

• CACHE_DB_PASS_ENCRYPTED: encrypted database password (see paragraph 'DB password encryption')

• CACHE _TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• HMAC_KEY: HMAC key to configure in Tomcat

• PASSWORD_ENCRYPTION_SECRET: key for password encryption

• SENSIBLE_DATA_ENCRYPTION_SECRET: key for encrypting sensitive data

• PUBLIC_ADDRESS: IP or hostname visible from the outside (e.g. http://$PUBLIC_ADDRESS:8080/knowage)

Parameters in the docker-compose.yml file
------------------------------------------------------------------------------------------------------------------------

• HAZELCAST_HOSTS: comma-separated Hazelcast hosts (e.g. "host1,host2,host3")

• HAZELCAST_PORT: Hazelcast port (e.g. "5701")

DB password encryption
------------------------------------------------------------------------------------------------------------------------
To encrypt the database password you need:

1. download the “tomcat-password-encryption.jar” jar in the “knowage-enterprise” directory from https://knowage-devops.knowage-suite.eu/webdav

2. run the following command (with java 17 or later): 

java -cp tomcat-password-encryption.jar -Dsymmetric_encryption_key=KEY_SECRET
en.eng.knowage.enterprise.tomcatpasswordencryption.helper.EncryptOnce DB_CLEAR_PASSWORD

where KEY_SECRET corresponds to the value indicated in the SENSIBLE_DATA_ENCRYPTION_SECRET environment variable

where DB_CLEAR_PASSWORD is the plaintext password of the database

3. replace the values ​​obtained in correspondence with the DB_PASS_ENCRYPTED and CACHE_DB_PASS_ENCRYPTED environment variables respectively

Installation of Database Schemas
------------------------------------------------------------------------------------------------------------------------
It is necessary to manually install the knowage and knowage_cache schemes on the customer database, executing the related DDLs. 

Make sure to update the parameters in the .env file with the correct data for DB access.

Check the connectivity between the host machine where Knowage will be installed and the DB.

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

Note on paths and mounted volumes
------------------------------------------------------------------------------------------------------------------------
The paths and directories specified in the docker-compose.yml file volumes (e.g. ./resources, ./conf/server.xml.d, etc.) must be adapted according to the structure and needs of the host machine on which Knowage is running.

Make sure the directories exist and contain the necessary files before starting the containers. Otherwise, the service may not start correctly or work as expected.

On the directories change the permissions with the following commands: 

Example:

chown -R knowage:knowage /portal_data/knowage_*

chmod -R 750 /portal_data/knowage_*

Create the following file with the command: 

vim ~/.config/containers/containers.conf and write 

[containers]

userns="keep-id"

Configuring additional hosts
------------------------------------------------------------------------------------------------------------------------
You can add the extra_hosts parameter within the service definition in the docker-compose.yml file to map custom hostnames to specific IP addresses.

This can be useful, for example, to resolve internal DNS names or to facilitate communication with external services not managed by Docker.

Example:

extra_hosts:

  - "hostname:192.168.1.100"

Container network setup
------------------------------------------------------------------------------------------------------------------------
In the docker-compose.yml file, the network_mode: "host" parameter is used to make containers share the host's network.

However, this configuration is not always the most suitable, especially in multi-container or production environments, where it is preferable to isolate services.

Alternatively, you can define a dedicated Docker network and assign it to containers, improving the security and flexibility of communication between services.

Caution with network_mode parameter: "host" cannot install the Hazelcast container for clustering

Dedicated network example:

networks:
  knowage_net

services:
  know-how:
    networks:
      - knowage_net
  hazelcast:
    networks:
      - knowage_net

Launching Knowage Services
------------------------------------------------------------------------------------------------------------------------
Go to the knowage-ee-server-docker directory and authenticate in the private repository:

podman login knowage.azurecr.io

After login, start the services:

podman composed up –d

Components Installed
------------------------------------------------------------------------------------------------------------------------
• Knowage Tomcat with all packages

• Hazelcast for clustering

• KnowagePython for integration with Python


Access the web interface: http://localhost:8080/knowage-vue/



