.. _saml-sso:

SAML 2.0 SSO
############

Knowage can delegate authentication to a SAML 2.0 Identity Provider (IdP).
Knowage acts as the Service Provider (SP): users authenticate at the IdP,
then receive a native Knowage session and JWT. SAML assertions are not passed
to analytical engines.

This page describes the standard SAML provider, enabled with
``provider=standard``. It covers the Knowage application side and the information
to exchange with the IdP administrator, not the administration of IdP software.

.. important::

   Authentication and application authorization are separate. Select
   ``profiling.mode=local`` to use existing Knowage users and their local roles,
   without an external profiling service. Alternatively, ``profiling.mode=pm``
   uses an external Profile Manager implementing the PM-API contract.
   The protocol setting ``provider=standard`` does not select the profiling mode.
   If ``profiling.mode`` is omitted, ``pm`` remains the default for compatibility;
   unsupported or empty values deny login. There is no fallback between modes.

Requirements
------------

* A Knowage distribution containing ``knowagesamlsecurityprovider`` and the
  corresponding frontend, common libraries, API and engine updates.
  The current implementation uses Java 17 and Tomcat 9.
* A public HTTPS origin shared by frontend and backend, valid TLS certificates
  and synchronized clocks on application nodes and the IdP.
* An IdP supporting signed HTTP-Redirect authentication requests, signed
  Response and Assertion messages delivered through HTTP-POST, and signed
  HTTP-POST Single Logout messages.
* A persistent, writable shared database accessible from all token consumers.
* For local profiling: existing Knowage users and assigned roles in their own
  tenants. The agreed SAML identifier must match the Knowage user ID.
* For PM profiling only: HTTPS connectivity to the profiling service and
  existing Knowage tenants, roles and functionalities matching its grants.

The standard provider signs requests with RSA-SHA256, uses SHA-256 digests and
rejects deprecated algorithms. Login must start from Knowage: unsolicited,
IdP-initiated responses are not supported. SOAP and Artifact bindings are not
implemented.

Prepare the IdP integration
----------------------------------------

Agree on one public origin for each environment. The following example uses
``https://bi.example.org`` and the standard application contexts.

Provide the IdP administrator with:

* The SP Entity ID, for example
  ``https://bi.example.org/knowage/restful-services/saml/metadata``.
  This identifier must match ``sp.entity-id`` exactly.
* The SP metadata XML and its publication URL:
  ``https://bi.example.org/knowage/restful-services/saml/metadata``.
* The Assertion Consumer Service (ACS), binding HTTP-POST:
  ``https://bi.example.org/knowage/restful-services/saml/acs``.
* The Single Logout service (SLO), binding HTTP-POST:
  ``https://bi.example.org/knowage/restful-services/saml/slo``.
* The public RSA signing certificate included in the SP metadata, the requested
  authentication contexts and the agreed NameID format (transient by default).
* The exact SAML attribute name containing a single, stable, unique identifier,
  together with its value format and any agreed prefix normalization.

Obtain the trusted IdP metadata XML, Entity ID, signing certificates, the
HTTP-Redirect SSO endpoint and the HTTP-POST logout request and response URLs.
Both logout URLs must be configured; they may be identical if the IdP specifies
this. Agree on certificate renewal and test identities enabled in both systems.

The SSO endpoint is read from the IdP metadata. The attribute identifier must
match a local Knowage user ID or be usable by PM, depending on the profiling
mode. Confirm its availability and ensure that users cannot freely edit the
value identifying their application account.
NameID identifies the protocol session, not the Knowage account.
The authentication context returned by the IdP must match one of the configured
``authn.contexts`` values exactly.

.. warning::

   Exchange public certificates and metadata only. Never send the SP private
   key, keystore password, Knowage JWT signing key or profiling credentials to
   the IdP administrator. SAML signing certificates and HTTPS trust are separate.

If Knowage is not deployed yet, first agree on the endpoint URLs and exchange
the public certificate and IdP metadata. Export the SP metadata after preparing
the application, then complete registration before enabling user access.

Configure Knowage
-----------------

Deploy the coordinated distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Back up the installation and database, stop the affected services and deploy
the matching backend, frontend, API and engine artifacts. Installing only the
provider JAR or only the main WAR is insufficient.

Preserve the ``FederatedSessionFilter`` declared in the utils JAR's
``META-INF\web-fragment.xml`` in every WAR; container scanning or application
overlays must not exclude it. Keep the existing JWT/HMAC configuration
consistent across Knowage consumers. Do not apply CAS-specific filters or
replace the global security supplier as part of this setup.

Prepare the shared state
~~~~~~~~~~~~~~~~~~~~~~~~

Run the database-specific script supplied in the provider's
``src\main\resources\saml`` directory:
``schema-mysql.sql``, ``schema-postgresql.sql``, ``schema-oracle.sql`` or
``schema-hsqldb.sql``. Apply it once; do not recreate an existing
``SBI_SAML_STATE`` table without checking its structure.

Expose a DataSource such as ``java:comp/env/jdbc/SamlState`` to every application
node, WAR, engine and API process that verifies federated tokens. Each binding
must point to the same writable database/schema, not a read replica or a
node-local database. Use persistent storage, default auto-commit ``true``,
READ_COMMITTED isolation and support for ``SELECT FOR UPDATE``.
The runtime account needs SELECT, INSERT, UPDATE and DELETE permissions.

For example, add this resource inside the existing Tomcat context descriptor,
adapting the connection parameters and making the JDBC driver available:

.. code-block:: xml

   <Resource name="jdbc/SamlState" auth="Container" type="javax.sql.DataSource"
       factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
       driverClassName="com.mysql.cj.jdbc.Driver"
       url="jdbc:mysql://DB_HOST:3306/KNOWAGE_DB"
       username="DB_USER" password="DB_PASSWORD"
       defaultAutoCommit="true" defaultTransactionIsolation="2" />

Repeat the binding in the other consumer contexts. For another database, use
its driver and connection URL. Protect the database credentials.

Install certificates and configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Store trusted IdP metadata and the SP PKCS12 keystore outside the WAR, for
example in ``C:\knowage\conf``. The keystore must contain the SP RSA private
key and its public certificate. Restrict file access to authorized accounts
and use separate material for test and production.

Create an external properties file, starting from the provider's
``standard.properties.example``. The following example uses local Knowage
accounts without PM. Replace the illustrative attribute name with the agreed
contract. The tenant is read from the local account.
Replace every ``REPLACE_`` value and mapping key before activation.

.. code-block:: properties

   provider=standard
   profiling.mode=local
   frontend.url=https://bi.example.org/knowage-vue/saml-login
   sp.entity-id=https://bi.example.org/knowage/restful-services/saml/metadata
   sp.acs-url=https://bi.example.org/knowage/restful-services/saml/acs
   sp.slo-url=https://bi.example.org/knowage/restful-services/saml/slo
   idp.entity-id=env:KNOWAGE_SAML_IDP_ENTITY_ID
   idp.metadata-file=env:KNOWAGE_SAML_IDP_METADATA_FILE
   idp.slo-url=env:KNOWAGE_SAML_IDP_SLO_URL
   idp.slo-response-url=env:KNOWAGE_SAML_IDP_SLO_RESPONSE_URL
   authn.contexts=env:KNOWAGE_SAML_AUTHN_CONTEXTS
   sp.name-id-format=urn:oasis:names:tc:SAML:2.0:nameid-format:transient
   sp.keystore-type=PKCS12
   sp.keystore-file=env:KNOWAGE_SAML_KEYSTORE_FILE
   sp.keystore-password=env:KNOWAGE_SAML_KEYSTORE_PASSWORD
   sp.key-alias=env:KNOWAGE_SAML_KEY_ALIAS
   sp.key-password=env:KNOWAGE_SAML_KEY_PASSWORD
   session.seconds=36000
   identity.attribute=username
   identity.prefix=

Every ``env:VARIABLE`` value is resolved from the application process environment;
it must be available to the actual Tomcat service, not just an interactive shell.
All service URLs must use HTTPS. Configure the runtime's TLS trust if an
internal CA is used; do not disable certificate verification.

Set ``authn.contexts`` to the agreed authentication context URI, or to a
comma-separated list without spaces. ``session.seconds`` accepts 1 to 36000
seconds; this is an upper bound, since IdP expiry and profiling validity
constraints may shorten the session. ``frontend.url`` must not contain a fragment.

Map the application identity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``identity.attribute``
   Exact SAML attribute name from which Knowage reads the stable identifier.
   A missing, empty or multivalued attribute denies login.

``identity.prefix``
   Optional literal prefix to remove from the start of the identifier.
   An empty value removes nothing. An empty identifier after normalization
   denies login.

Use existing Knowage accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With ``profiling.mode=local``, the normalized identifier must match the
``user_id`` of an existing Knowage account exactly, including case.
For example, ``username=reader`` selects the local user ``reader``.
Knowage derives the tenant from that account, allowing users from different
tenants to log in through the same SAML configuration. Each user keeps the
roles belonging to their own tenant. Do not set ``local.tenant``; neither the
IdP nor the browser selects the tenant. No lookup by email or
NameID, automatic provisioning, or fallback to another identifier is performed.

Knowage loads the account's name, profile attributes, assigned roles and
superadmin flag from its own catalogue. Assertion roles do not grant permissions.
Unknown or blocked accounts (``flgPwdBlocked=true``), accounts without a
tenant, accounts without assigned roles and cross-tenant role
assignments deny login. The local default role is respected and must be an
assigned role.

Normal Knowage role, functionality and license checks apply. No PM endpoint,
credential or permission mapping is required, and no ``pm_functions``
restriction is applied. Local attributes named ``kn_*`` or reserved JWT claims
(``user_id``, ``iss``, ``sub``, ``aud``, ``exp``, ``nbf``, ``iat``, ``jti``)
are not exported into the token.

Authentication, passwords and MFA belong to the IdP; the local Knowage password
and its expiry are not checked. The configured session lifetime and IdP expiry
still apply, as do the shared registry, revocation and SAML logout.

Use an external Profile Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For PM-API profiling, replace the local profiling settings with the following
and obtain the actual API contract and credentials from its administrator.
These settings are not needed in local mode.

.. code-block:: properties

   profiling.mode=pm
   identity.attribute=subjectId
   identity.prefix=
   pm.identity-parameter=subjectId
   pm.identity-field=externalId
   pm.token-url=env:KNOWAGE_PM_TOKEN_URL
   pm.client-id=env:KNOWAGE_PM_CLIENT_ID
   pm.client-secret=env:KNOWAGE_PM_CLIENT_SECRET
   pm.service-user=env:KNOWAGE_PM_SERVICE_USER
   pm.service-password=env:KNOWAGE_PM_SERVICE_PASSWORD
   pm.profile-url=env:KNOWAGE_PM_PROFILE_URL
   pm.user-url=env:KNOWAGE_PM_USER_URL
   pm.authorization-url=env:KNOWAGE_PM_AUTHORIZATION_URL
   pm.procedure=REPLACE_PROCEDURE
   pm.user-type=REPLACE_USER_TYPE
   pm.role-map.REPLACE_EXTERNAL_ROLE=REPLACE_EXISTING_KNOWAGE_ROLE
   pm.tenant-map.REPLACE_EXTERNAL_ORGANIZATION=REPLACE_EXISTING_KNOWAGE_TENANT
   pm.function-map.REPLACE_EXTERNAL_FUNCTION=REPLACE_KNOWAGE_FUNCTION
   pm.access-type-map.REPLACE_EXTERNAL_ACCESS_TYPE=REPLACE_KNOWAGE_FUNCTION

``pm.identity-parameter``
   Query parameter used for the profile and authorization lookups.
   The external API must actually support this parameter.

``pm.identity-field``
   Field in the returned PM user object that must contain the same normalized
   identifier. A missing or different value denies login.

For the example above, a SAML value ``subjectId=ABC123`` is sent to the profiling
service as ``subjectId=ABC123`` and must match its user field
``externalId=ABC123``. These names are independent; configuring them does not
add lookup capabilities to the external API. No alternative identity is guessed
when the configured one is missing.

In PM mode, the application account comes from the external profile, not from
NameID or an automatically assumed IdP username. The current adapter does not
provision accounts. Roles and tenants must already exist in Knowage.
Distinct external organizations require distinct tenant mappings. Function
and access-type mappings accept comma-separated Knowage functionality names
without spaces.

In PM mode, Knowage's normal permission checks remain active, with an additional
intersection against external functionality grants. Local account roles are
not automatically substituted for those grants, and the federated profile does
not enable the global superadmin flag. Verify that tenant/dataset configuration
enforces the required data isolation; importing an organization attribute alone
does not rewrite dataset queries.

Enable the integration
~~~~~~~~~~~~~~~~~~~~~~

Set these JVM options on the main application:

.. code-block:: text

   -Dknowage.saml.enabled=true
   -Dknowage.saml.config=C:\knowage\conf\saml.properties
   -Dknowage.saml.datasource=java:comp/env/jdbc/SamlState

The corresponding environment variables are ``KNOWAGE_SAML_ENABLED``,
``KNOWAGE_SAML_CONFIG`` and ``KNOWAGE_SAML_DATASOURCE``. Set the DataSource
configuration on separate API/engine JVMs too, and restart all updated services.
If the legacy OIDC flow is unused, keep ``oauth2_flow_type=NONE``.

Publish the configured public URLs through the proxy without changing their
host, scheme or path. Preserve SAML POST bodies and parameters, do not add an
authentication gateway in front of the SAML endpoints, and do not cache their
responses. Preserve Secure/HttpOnly cookies and the existing CSRF protection.

Before opening access to users, retrieve the SP metadata and check its Entity
ID, signing certificate, ACS and SLO URLs. Send the XML to the IdP administrator
and obtain registration confirmation. Metadata retrieval requires the enabled
application, valid SAML configuration and the configured DataSource binding.

Login and logout behavior
-------------------------

The frontend reads ``/knowage/restful-services/loginconfig``. When
``items[0].samlActive`` is true, opening ``/knowage-vue/saml-login`` automatically
starts authentication without displaying a local login form or a separate
federated Sign in button.

Knowage validates the returned signatures, issuer, destination, authentication
context, timestamps, request correlation and replay protection, then resolves
the selected local or external application profile. The browser receives a
short-lived, single-use code instead of a JWT in the redirect URL. It exchanges
that code and its browser verifier at ``/knowage/restful-services/saml/exchange``.
The code expires after 60 seconds; the completed HTTP session receives a new ID.

Logout revokes the shared federated session before performing the IdP SLO
exchange. The standard provider sends signed logout messages through HTTP-POST
and accepts signed logout requests and responses at the SP SLO endpoint.
Login/error/logout callbacks do not automatically start another login.

Previously issued tokens are rejected by all updated consumers on their next
request, including engines already open in the browser. Operations already
running are not cancelled retroactively. Account role assignments, attributes
and account status are captured at login in either profiling mode.
Changes require a fresh login or session revocation; they are not polled on
every request.

Verify and operate
------------------

Before enabling production access:

1. Check that the metadata endpoint returns HTTP 200 and the registered values,
   and that login configuration reports ``samlActive=true`` and
   ``authenticationMethod=SAML``.
2. Log in with two different accounts in the selected profiling mode.
   Verify account identity, tenant, roles, permitted actions and the intended
   data scope, not just successful authentication. Check that the authenticated
   ``currentuser`` request succeeds.
3. Confirm denial for a missing/mismatched identifier, blocked or unauthorized
   account, invalid signature and replayed callback. In local mode, also test
   unknown users, users without tenant/roles and cross-tenant role assignments.
   Log in with users in two different tenants and verify their respective
   permissions without PM. In PM mode, test service unavailability.
4. Test application-initiated and IdP-initiated logout notifications. Verify
   rejection of the old session on every deployed API/engine and no automatic
   re-login loop.
5. Test across application nodes to verify that correlation, code consumption
   and revocation use the same registry.

Monitor the shared database, PM endpoints when used, clock synchronization and
certificate expiry. Synchronize trusted metadata updates across nodes.
Schedule deletion of expired registry rows only, comparing ``EXPIRES_AT`` with
the current epoch time in milliseconds; do not remove active state.

.. warning::

   The registry contains identity/session context and temporary exchange tokens.
   Protect database access, backups and retention. Keep the
   ``com.onelogin.saml2`` logger disabled and do not log assertions, JWTs,
   exchange codes, verifiers or credentials in applications or proxies.

Troubleshooting
---------------

Metadata endpoint returns 404
   Check deployment of the SAML module and ``knowage.saml.enabled``.

Metadata or login configuration fails
   Check the external configuration path, process environment, keystore
   alias/password, trusted metadata and JNDI binding. Check the existing OIDC
   configuration if that legacy flow is enabled.

The IdP login succeeds but Knowage rejects the callback
   Check Entity IDs, public ACS URL, trusted signing keys, both required
   signatures, exact authentication context, clock synchronization and the
   agreed identifier. For local mode, check the exact local user ID, block
   flag, assigned roles and the account's tenant. For PM, check service availability
   and mappings.

The wrong application account or permissions appear
   Verify ``profiling.mode`` and the identifier-to-account mapping.
   In local mode, check the account's roles, default role and tenant in Knowage;
   in PM mode, check role, tenant, function and access-type mappings.
   Log out and start a fresh login after
   correcting the profile; do not reuse an old session or a consumed code.

Federated requests fail after a successful login
   Check shared registry connectivity and session expiry/revocation on every
   consumer. Signature validity alone does not make a revoked token usable.
