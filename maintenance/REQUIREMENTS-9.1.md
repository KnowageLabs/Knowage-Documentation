# Requirements verification — 26 October 2026

The original chapter structure is retained. These checks concern public source
and recipes; they are not installation tests or a new certification matrix.

| Component | Evidence | Documentation handling |
| --- | --- | --- |
| Java | Tagged parent POM targets Java 17. | Retain JDK 17; fix JAVA_HOME examples and service-account scope. |
| Tomcat | Public Dockerfile pins 9.0.109; application uses javax.servlet. | Retain Tomcat 9; distinguish recipe patch from a production support requirement. |
| OS | Original published manual lists certified/compatible families. | Preserve the matrix with attribution; exact releases and architectures need distribution confirmation. |
| Database | Tagged scripts for MySQL/MariaDB, PostgreSQL and Oracle. | Remove unsupported claims that the historical version matrix certifies 9.1. Verify target DB and JDBC versions. |
| SQL migrations | PostgreSQL uses WITHOUT OIDS; Oracle migration declares SQL BOOLEAN. | Keep database-version checks in the upgrade procedure. |
| Compose | 9.1-SNAPSHOT images, MariaDB 10.3 example, host port 18080. | Require approved release artifacts; the example is not a modern DB recommendation. |
| Hazelcast | Java dependency 5.3.6; example server line 5.3. | Distinguish Java integration and deployment topology. |
| HSQLDB | Public Docker recipe includes 1.8.0.10. | Replace the unconditional 1.8.0.2 requirement with the version supplied by the relevant distribution. |
| Python | setup.py version 1.1, lower bound >=3.7; Flask 1.1.4 and pandas 1.3.5 pinned. | Do not equate Python package and platform version or claim every newer interpreter is compatible. Use the qualified service package. |
| Python startup | Application exported as application; HMACKEY_FILE is relative hmackey. | Correct Gunicorn target and use src as the working directory for the tagged source layout. |
| Node.js / Chromium | EE export package is not public. | Exact supported pair is not established. Use its manifest; remove stale universal OS install commands. |
| CPU/RAM/disk | No universal CPU/RAM minimum in the checked recipe; old disk figure excludes data/metadata. | Retain 2 GB as installation footprint with explicit scope; size the complete deployment by workload. |
| Browser policy | Original manual: latest and preceding Chrome, Firefox and Edge. | Retain the published policy without inventing numeric browser versions. |

Sources are pinned in REVIEW-9.1.md. For the build requirements, see root
requirements.txt: Sphinx 8.2.3 and sphinx-rtd-theme 3.0.2. They are independent
of the Knowage runtime requirements above.
