KNOWAGE Community  Installation using Docker
########################################################################################################################

Repository cloning
------------------------------------------------------------------------------------------------------------------------
To install Knowage CE via Docker, you need to clone the GitHub repository:

git clone https://github.com/KnowageLabs/Knowage-Server-Docker.git

Preparation of the Environment
------------------------------------------------------------------------------------------------------------------------
Access the project directory:

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
