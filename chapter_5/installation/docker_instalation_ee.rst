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


