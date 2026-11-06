.. _birt-static-resources:

BIRT static resources configuration guide
########################################################################################################################

This guide explains how administrators publish static resources in Knowage and how report authors reference them from
BIRT reports. A typical use case is a company logo shared by several reports without embedding it in every template.

Resources are stored in the tenant's ``external-libraries`` folder and retrieved through the authenticated Knowage API.
In the report template, use a placeholder instead of a server address or an access token:

.. code-block:: text

   ${KNOWAGE_EXTERNAL_LIBRARY:logo.png}

When the report runs in Knowage, the placeholder becomes a resource URL authenticated as the executing user.
The stored report template keeps the placeholder, so the same template can be deployed to different environments.

.. important::

   Despite the folder name, this mechanism is intended for static resources consumed through a URL, such as images.
   It does not configure BIRT ``.rptlibrary`` dependencies, script libraries or local resource lookup.
   Use an image format supported by the BIRT output formats you need; PNG is a suitable starting point.

Administrator configuration
------------------------------------------------------------------------------------------------------------------------

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The installation must provide the BIRT engine with external-resource placeholder support and the Knowage external
libraries download service. The executing user must have a valid, expiring Knowage JWT available to the BIRT engine.
Keep the existing SSO and token-signing configuration consistent between Knowage, the BIRT engine and the API.
Do not configure a shared technical token or a password in the report.

The API must be reachable over HTTPS from the BIRT server. Its hostname must resolve there, and its certificate and
certificate chain must be trusted by the BIRT server runtime. A URL that works only in the administrator's browser is
not sufficient.

Publish the files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the resource root configured for the Knowage API through ``resource_path``. With the standard Tomcat configuration,
this is ``TOMCAT_HOME\resources``. Under that root, create the following folder for the organization of the users who
will execute the report:

.. code-block:: text

   TOMCAT_HOME\resources\<tenant>\external-libraries

For example, if the organization is ``DEFAULT_TENANT``:

.. code-block:: text

   TOMCAT_HOME\resources\DEFAULT_TENANT\external-libraries\logo.png
   TOMCAT_HOME\resources\DEFAULT_TENANT\external-libraries\banner.png

Copy the files directly into ``external-libraries`` and grant the account running the Knowage API read access to the
files and access to their parent directories. Use the actual organization identifier, not a user name or a role name.
If ``resource_path`` points to another location, use that location instead of the default Tomcat directory.

Resource selection follows the executing user's tenant. For a report shared by several tenants, publish the required
files separately in each tenant's folder. In a clustered installation, make the files available to every API node that
can receive the download request.

.. warning::

   The download service is available to authenticated users of the corresponding tenant. Do not place secrets or
   files requiring document-specific access restrictions in this folder. Subdirectories and links pointing outside
   the permitted resource folder cannot be used to reference resources.

Configure the BIRT API base URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``engine-config.xml`` in the deployed ``knowagebirtreportengine`` application. In a standard exploded Tomcat
deployment, the file is located at:

.. code-block:: text

   TOMCAT_HOME\webapps\knowagebirtreportengine\WEB-INF\classes\engine-config.xml

Inside the existing ``ENGINE-CONFIGURATION`` element, set ``EXTERNAL_LIBRARIES_API_BASE_URL`` to the HTTPS API base URL.
For the standard API deployment:

.. code-block:: xml

   <EXTERNAL_LIBRARIES_API_BASE_URL>https://bi.example.org/knowage-api/api</EXTERNAL_LIBRARIES_API_BASE_URL>

The resource service path ``/2.0/resources/external-libraries`` is appended to this value. In this example, the download
endpoint is therefore ``https://bi.example.org/knowage-api/api/2.0/resources/external-libraries``.

.. important::

   Include the complete API base path, including ``/api`` in the standard deployment. Do not set only the Knowage
   portal URL or only ``https://bi.example.org/knowage-api``. Do not include the resource service path, ``libraryName``
   or authentication parameters in the configured base URL.

If a reverse proxy publishes the API under a different path, configure the corresponding HTTPS base URL and ensure
that the proxy forwards resource downloads to the API, rather than returning a login page.
The value must be an absolute HTTPS URL without embedded credentials, query parameters or a fragment.

Apply this setting on every BIRT node, restart the BIRT application after changing it, and preserve the configuration
in your deployment procedure so that a redeployment does not overwrite it.
Reports without external-resource placeholders do not require this setting.

Authentication parameter and logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, resource URLs use the authentication parameter name ``X-Kn-Authorization``. If the installation uses a
custom name, set the environment variable ``KNOWAGE_AUTHORIZATION_HEADER_NAME`` to the same non-empty value for both
the BIRT engine and the Knowage API processes. Restart the affected applications after changing the environment.
This variable specifies the parameter name, not an access token.

BIRT obtains the executing user's token automatically. The token must remain valid until the resource is downloaded.
Do not add a token manually to the template or reuse a URL generated by a previous execution.

.. warning::

   The generated resource URL contains a user token in its query string. Configure reverse proxies, web access logs
   and monitoring tools to omit or redact the authentication parameter. Treat generated URLs and execution artifacts
   containing them as credentials: do not publish them, paste them into tickets or store them in shared templates.
   Do not configure shared proxy caching for authenticated resource downloads.

Report author configuration
------------------------------------------------------------------------------------------------------------------------

Add a shared logo in BIRT Designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ask the administrator to publish ``logo.png`` in the appropriate tenant's ``external-libraries`` folder and configure
   the BIRT API base URL.
2. Open the report in BIRT Designer and insert an **Image** in the layout or master page.
3. Select the image source type **URI**, rather than an embedded image or a local resource file.
4. Set the URI to ``${KNOWAGE_EXTERNAL_LIBRARY:logo.png}``. If the URI field opens the expression editor, enter the
   placeholder as a quoted string expression:

   .. code-block:: javascript

      "${KNOWAGE_EXTERNAL_LIBRARY:logo.png}"

5. Save the ``.rptdesign`` file, upload it as the template of the BIRT document in Knowage, and execute the document
   while signed in as a user of the intended tenant.

For reference, the image configuration in the report's **XML Source** can look like this:

.. code-block:: xml

   <image id="100">
       <property name="source">url</property>
       <expression name="uri" type="javascript">"${KNOWAGE_EXTERNAL_LIBRARY:logo.png}"</expression>
   </image>

This is an example of an image element inside a report, not a complete report template. When editing an existing
element, retain its identifier and the other layout properties.

Placeholder rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the exact, case-sensitive prefix ``KNOWAGE_EXTERNAL_LIBRARY`` and include the file extension.
The value after the colon must be a file name only, for example ``logo.png`` or ``company-banner.png``.
Do not supply a filesystem path, a URL, ``.`` or ``..``. Examples such as
``${KNOWAGE_EXTERNAL_LIBRARY:images/logo.png}`` and ``${KNOWAGE_EXTERNAL_LIBRARY:images\logo.png}`` are invalid.
File names cannot contain braces; use simple names and preserve their spelling and case.

Knowage encodes the file name for the download URL automatically. Do not URL-encode the name in the placeholder,
append an authentication parameter or construct a download URL yourself.
You can use different placeholders for different images and reuse the same placeholder in several report elements.
Each placeholder must be complete and appear in the actual resource property or expression, not just in an XML comment.

.. note::

   Standalone BIRT Designer preview does not resolve Knowage placeholders or obtain Knowage authentication.
   Verify this configuration by executing the uploaded report in Knowage. If you temporarily use a local image while
   designing the layout, restore the placeholder before uploading the final template.

Verification and troubleshooting
------------------------------------------------------------------------------------------------------------------------

After deployment, execute the report with a fresh authenticated session and check that the image is displayed.
Export the report to the formats required by your users, especially PDF and HTML, and verify the image in each output.
If the report is used by several tenants, repeat the check with a user from each tenant.
Before enabling scheduled or other unattended executions, verify that their execution context also provides a valid,
expiring user token; an interactive test alone does not establish this.

.. list-table:: Common configuration issues
   :header-rows: 1
   :widths: 30 70

   * - Symptom
     - Checks and action
   * - Report fails when an external resource is referenced
     - Check that ``EXTERNAL_LIBRARIES_API_BASE_URL`` is set to an absolute HTTPS API base URL and that the user has
       a valid, expiring token. Check that placeholders have a closing brace and a valid file name.
   * - Resource request reaches the wrong page or returns a routing error
     - Check the API context path, including ``/api`` in a standard deployment, and the reverse proxy mapping.
       The resource service suffix must not already be included in the base URL.
   * - Authentication failure
     - Sign in again and rerun the report. Check SSO and token-signing configuration, token expiry, and that
       ``KNOWAGE_AUTHORIZATION_HEADER_NAME`` matches on BIRT and the API. Ensure the proxy preserves the parameter.
   * - File or folder is not found
     - Check ``resource_path``, the executing user's tenant, the exact file name and the presence of the file directly
       under ``external-libraries``. Check every API node in a cluster.
   * - Image is missing despite a successful file download
     - Check that the resource is a valid image supported by BIRT and the selected export format, and that the image
       source is configured as URI rather than as an embedded or local file.
   * - HTTPS connection or certificate error
     - Check connectivity and hostname resolution from the BIRT server, the certificate hostname and the trusted
       certificate chain. Do not switch to HTTP as a workaround.
   * - Image is missing only in standalone Designer preview
     - Execute the report in Knowage; standalone preview does not resolve the placeholder.

When collecting diagnostics, remove authentication values from URLs and logs before sharing them.
