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

• DB_PASS_ENCRYPTED: encrypted database password (see chapter 6)

• DB_TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• CACHE_DB_HOST: cache database host

• CACHE_DB_PORT: cache database port

• CACHE_DB_DB: name of the cache database

• CACHE_DB_USER: cache database user

• CACHE_DB_PASS_ENCRYPTED: encrypted database password (see chapter 5)

• CACHE _TYPE: database type (default: MYSQL; options: MYSQL, MARIADB, ORACLE, POSTGRES)

• HMAC_KEY: HMAC key to configure in Tomcat

• PASSWORD_ENCRYPTION_SECRET: key for password encryption

• SENSIBLE_DATA_ENCRYPTION_SECRET: key for encrypting sensitive data

• PUBLIC_ADDRESS: IP or hostname visible from the outside (e.g. http://$PUBLIC_ADDRESS:8080/knowage)

Parameters in the docker-compose.yml file
------------------------------------------------------------------------------------------------------------------------

• HAZELCAST_HOSTS: comma-separated Hazelcast hosts (e.g. "host1,host2,host3")

• HAZELCAST_PORT: Hazelcast port (e.g. "5701")


