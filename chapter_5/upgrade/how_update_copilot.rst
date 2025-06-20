
# How to Upgrade KNOWAGE from Version 8.0 to 8.1

This guide outlines the steps required to manually upgrade an existing KNOWAGE installation from version 8.0 to 8.1.

> ⚠️ **Important:** KNOWAGE versioning follows Semantic Versioning 2.0.0. This means:
> - **Patch versions** (e.g., 8.0.0 → 8.0.1) are backward-compatible and do not require manual intervention.
> - **Minor versions** (e.g., 8.0 → 8.1) may introduce changes that require manual updates.

---

## Prerequisites

Before proceeding, ensure the following:

- You have a **backup** of your current KNOWAGE installation and database.
- You have access to the **KNOWAGE 8.1 distribution**.
- You have reviewed the **release notes** for version 8.1.

---

## Upgrade Steps

### 1. Stop the Application Server

Stop the application server (e.g., Tomcat) where KNOWAGE is currently deployed.

```bash
sudo systemctl stop tomcat
```

---

### 2. Backup the Existing Installation

Make a full backup of:

- The KNOWAGE web application directory (e.g., `webapps/knowage`)
- The KNOWAGE database

---

### 3. Deploy the New Version

Replace the old `knowage.war` file with the new one from version 8.1.

```bash
cp knowage-8.1.war /path/to/tomcat/webapps/knowage.war
```

---

### 4. Update Configuration Files

Manually review and update the following configuration files:

- `knowage-config.xml`
- `hibernate.cfg.xml`
- `datasources.xml`
- Any custom configurations (e.g., LDAP, SSO, scheduler)

> 💡 **Tip:** Compare your old configuration files with the new ones provided in the 8.1 distribution to identify changes.

---

### 5. Apply Database Updates

Run the SQL scripts provided in the `update/sql` folder of the 8.1 distribution.

> ⚠️ **Warning:** Always test SQL scripts in a staging environment before applying them to production.

---

### 6. Restart the Application Server

Once all updates are complete, restart the application server.

```bash
sudo systemctl start tomcat
```

---

### 7. Verify the Upgrade

- Log in to KNOWAGE and verify the version number.
- Check that all functionalities are working as expected.
- Monitor logs for any errors or warnings.

---

## Troubleshooting

If you encounter issues:

- Check the application logs (`catalina.out`, `knowage.log`)
- Ensure all configuration files are correctly updated
- Verify that the database scripts were executed successfully

---