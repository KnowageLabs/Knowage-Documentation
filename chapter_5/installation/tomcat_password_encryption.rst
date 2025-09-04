Encrypted Passwords for Tomcat DataSources
========================================================================================================================

This feature allows you to store encrypted JNDI DataSource passwords in server.xml (prefixed with “#encr#…”) while keeping the decryption key protected outside server.xml.

Goals:

- Only “#encr#BASE64…” is stored in server.xml
- The decryption key is read from a system property 'symmetric_encryption_key'

Includes:

- A custom Tomcat DataSourceFactory
- A small CLI to encrypt a password once
- Build, install, and configuration steps
- Examples

How it works
------------------------------------------------------------------------------------------------------------------------

- In server.xml, your JNDI Resource uses a custom DataSourceFactory.
- If the password starts with “#encr#…”, the factory decrypts it at runtime before the pool is initialized.
- System property -Dsymmetric_encryption_key=your_secret

.. important::
    **CLEAR PASSWORDS**

    Note: If the password does not start with “#encr#…”, it’s used as-is.

Build
------------------------------------------------------------------------------------------------------------------------

Clean and package

.. code-block:: bash
  	    :linenos:

        mvn clean package

Install on Tomcat
------------------------------------------------------------------------------------------------------------------------

Place the jar on Tomcat’s common classpath:
- Location: ${CATALINA_BASE}/lib

Options:
- Shaded jar: copy only target/tomcat-password-encryption-<version>-shaded.jar
- Lean jar: copy target/tomcat-password-encryption-<version>.jar and also jasypt-1.9.3.jar into ${CATALINA_BASE}/lib

Restart Tomcat.

Configure the key
------------------------------------------------------------------------------------------------------------------------

Set the JVM property:

- -Dsymmetric_encryption_key=your_secret

## Generate an encrypted password (“#encr#…”)
------------------------------------------------------------------------------------------------------------------------

Use the included CLI to produce the encrypted string you will paste into server.xml. Use the same key source as Tomcat (JVM property symmetric_encryption_key).

If the jar already includes Jasypt (single jar on classpath):

.. code-block:: bash
        :linenos:

        java -cp target/tomcat-password-encryption-<version>.jar
        -Dsymmetric_encryption_key='YOUR_SECRET'
        it.eng.knowage.tomcatpasswordencryption.helper.EncryptOnce 'CLEAR_PASSWORD'


Output:
- A string starting with:

  #encr#BASE64_CIPHERTEXT

Paste this into the password attribute of your Resource in server.xml.

Configure the DataSource (server.xml)
------------------------------------------------------------------------------------------------------------------------

Example (MySQL):

.. code-block:: xml
   :linenos:

    <Resource
      name="jdbc/yourDS"
      auth="Container"
      type="javax.sql.DataSource"
      factory="it.eng.knowage.tomcatpasswordencryption.KnowageTomcatEncryptedPasswordDatasource"
      driverClassName="com.mysql.cj.jdbc.Driver"
      url="jdbc:mysql://db-host:3306/yourdb?useSSL=false&serverTimezone=UTC"
      username="dbuser"
      password="#encr#BASE64_CIPHERTEXT"
      maxActive="20"
      maxIdle="4"
      validationQuery="SELECT 1"
      />

Quick checklist
------------------------------------------------------------------------------------------------------------------------

- Build a clean (or shaded) jar.
- Copy the jar to ${CATALINA_BASE}/lib.
- Set the JVM option symmetric_encryption_key
- Generate a “#encr#…” value with the CLI and paste it into server.xml.
- Restart Tomcat and verify DB connectivity.