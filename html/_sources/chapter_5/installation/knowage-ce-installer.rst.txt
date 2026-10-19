Community Edition with Docker or Podman
========================================

Use the public Docker recipe as a starting configuration and select application
images corresponding to the release you intend to install.

.. important::

   The Docker recipe accompanying the 9.1 source update references
   ``9.1-SNAPSHOT`` images. A snapshot tag alone does not identify the
   released 9.1.0 binaries. Confirm the release image or immutable digest from
   your distribution channel before deployment. For the published 9.1.0 WARs,
   follow :doc:`manual_installation`.

Prepare the Compose project
---------------------------

.. code-block:: bash

   git clone https://github.com/KnowageLabs/Knowage-Server-Docker.git
   cd Knowage-Server-Docker/Knowage-Server-Docker

Inspect ``docker-compose.yml`` and the supplied ``.env``. The recipe provides
services for Knowage, Python, Hazelcast, metadata storage and cache storage.
Set your own database passwords and encryption secrets before starting it.

.. list-table:: Main environment settings
   :header-rows: 1
   :widths: 35 65

   * - Variable group
     - Purpose
   * - ``DB_HOST``, ``DB_PORT``, ``DB_DB``, ``DB_USER``, ``DB_PASS``
     - Metadata database connection.
   * - ``CACHE_DB_HOST``, ``CACHE_DB_PORT``, ``CACHE_DB_DB``, ``CACHE_DB_USER``, ``CACHE_DB_PASS``
     - Cache database connection.
   * - ``HMAC_KEY``
     - Shared token authentication key for the participating services.
   * - ``PASSWORD_ENCRYPTION_SECRET``, ``SENSIBLE_DATA_ENCRYPTION_SECRET``
     - Persistent secrets for the configured encryption mechanisms.
   * - ``PUBLIC_ADDRESS``
     - Host name through which clients reach the deployment.
   * - ``HAZELCAST_HOSTS``, ``HAZELCAST_PORT``
     - Hazelcast service connection.
   * - ``DB_TYPE``, ``CACHE_DB_TYPE``
     - Database types selected in the Compose environment.
   * - ``DB_DO_INITIALIZATION``
     - Metadata initialization control. Use ``false`` for an existing schema.

Some values are set directly in ``docker-compose.yml`` rather than passed
through ``.env``. Review both files. Preserve encryption secrets across
container replacement and upgrades.

Start and verify
----------------

After choosing the approved release images and configuring the environment:

.. code-block:: bash

   docker compose pull
   docker compose up -d
   docker compose ps
   docker compose logs --tail=100 knowage

The sample Compose file maps host port **18080** to container port **8080**.
With its local defaults, open ``http://localhost:18080/knowage``. Adapt the
address to your public host, port mapping and reverse proxy. An existing proxy
must route the deployed Knowage application contexts consistently.

Podman users can use the corresponding ``podman compose`` commands with a
configured Compose provider.

The recipe mounts ``./resources`` and uses named database volumes. Retain these
when replacing containers. Check sign-in, a dataset, a document and the optional
Python service before making the environment available to users.

External databases and upgrades
-------------------------------

For external databases, configure both metadata and cache connections, adjust
the service dependencies and select the correct DBMS types. Initialize a new
metadata schema using the 9.1.0 creation scripts, or upgrade an existing schema
with :doc:`/chapter_5/upgrade/how_upgrade_9_0_to_9_1`. Set
``DB_DO_INITIALIZATION=false`` when reusing that schema.

Updating a container image does not execute the required release migration.
Back up the metadata database, resources and configuration together before
changing a deployed release.
