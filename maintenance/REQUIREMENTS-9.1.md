# Verification of Knowage 9.1 runtime requirements

Checked on 19 October 2026. This review checks public source and distribution
recipes; it does not constitute installation testing or a new certification.

| Component | Evidence at the reviewed version | Documentation conclusion |
| --- | --- | --- |
| Java | Backend POM `maven.compiler.source/target=17`; Docker uses `eclipse-temurin:17-jdk`. | JDK 17 baseline. Tagged CI still sets Java 8, inconsistent with the compiler target; it is not runtime guidance. |
| Tomcat | Dockerfile pins 9.0.109; backend uses `javax.servlet-api`. | Tomcat 9.0.x. Recipe version is not the latest patch or a certified minimum; Tomcat 10/11 are not direct replacements. |
| Metadata/cache DB | Tagged scripts for MySQL/MariaDB, PostgreSQL and Oracle; Docker accepts MYSQL/MARIADB/POSTGRES/ORACLE. | Vendor integrations are established; exact server/driver versions are not. Qualify creation, migration, runtime and scheduler operations. |
| Compose DB example | Metadata and cache use `mariadb:10.3`. Upstream maintenance ended 25 May 2023. | Outdated example, not a new-production recommendation. Do not invent a replacement certified version. |
| DB scripts | PostgreSQL retains `WITHOUT OIDS`; Oracle 9.0-to-9.1 migration contains SQL `BOOLEAN`. | Retain version-specific script checks and upgrade warning. A JDBC driver does not certify server-side DDL compatibility. |
| Hazelcast | `knowageutils/pom.xml` pins 5.3.6; Compose uses server line 5.3. | Document the Java dependency and example topology separately. |
| Python | Tagged setup.py: version 1.1, `python_requires >=3.7`; dependencies include Flask 1.1.4 and pandas 1.3.5. Public base source uses Python 3.8. | No open-ended “Python >=3.8 supported” claim. Package/platform versions differ. Built base-image interpreter is unverified. Python 3.8 ended support on 7 October 2024; new deployments need a maintained qualified service build. |
| Node.js/Chromium | Tagged CI sets Node 18 for source builds; private Enterprise export package is not public. | No exact supported export pair established. Use its 9.1 package manifest. Remove obsolete universal OS package commands. |
| OS | Original manual declares Oracle Linux 9/10 and Windows Server 2022/2025 certified; RHEL 10 and Ubuntu 22/24/25 compatible. Ubuntu point releases unspecified. | Preserve declarations with attribution; no new certification is claimed. Confirm exact releases/architectures with package support matrix. |
| Browsers | Original manual: latest and preceding Chrome/Firefox/Edge. | Retain published policy; no new numeric version certification. |
| CPU/RAM/disk | No verified CPU/RAM minimum or fixed JVM heap in reviewed public recipes. Old manual's 2 GB excludes data/metadata. | Describe workload sizing and full storage categories; do not invent hardware minima or claim 2 GB is production capacity. |

## Related edits

- Reworked `chapter_5/requirements.rst` with mandatory/optional services,
  evidence scope, lifecycle findings and versioned references.
- Corrected Python installation interpreter/version assumptions, unpinned
  dependency commands, service working directory and Gunicorn settings.
- Preserved the Windows Java screenshot placeholder and IDs of retained captures.
- Root `requirements.txt` remains Sphinx 8.2.3/theme 3.0.2; documentation
  build dependencies are distinct from product runtime requirements.

## Reproducible sources

- [Backend release](https://github.com/KnowageLabs/Knowage-Server/tree/47d06115a965f8440527b77a9e41d990e77aa078).
- [Parent POM](https://github.com/KnowageLabs/Knowage-Server/blob/47d06115a965f8440527b77a9e41d990e77aa078/knowage-ce-parent/pom.xml).
- [Core POM](https://github.com/KnowageLabs/Knowage-Server/blob/47d06115a965f8440527b77a9e41d990e77aa078/knowage-core/pom.xml).
- [Utilities POM](https://github.com/KnowageLabs/Knowage-Server/blob/47d06115a965f8440527b77a9e41d990e77aa078/knowageutils/pom.xml).
- [Python package](https://github.com/KnowageLabs/Knowage-Server/tree/47d06115a965f8440527b77a9e41d990e77aa078/Knowage-Python).
- [Tagged CI](https://github.com/KnowageLabs/Knowage-Server/blob/47d06115a965f8440527b77a9e41d990e77aa078/.github/workflows/build.yml).
- [Docker recipe](https://github.com/KnowageLabs/Knowage-Server-Docker/tree/26f22a44bc50e4a7bd19a71438227d7fb329acd7).
- [Python base source](https://github.com/KnowageLabs/Knowage-Python-Docker-Base/blob/221d2001804d1f6c105a3452cf6b1221bcb6c02c/Dockerfile).
- [Original requirements](https://github.com/KnowageLabs/Knowage-Documentation/blob/7a5096c8eb03360d31b2ac277f90fe93fd712119/chapter_5/requirements.rst).
- [Tomcat versions](https://tomcat.apache.org/whichversion.html).
- [MariaDB lifecycle](https://mariadb.org/about/#maintenance-policy).
- [Python lifecycle](https://devguide.python.org/versions/).

## Remaining qualification work

Obtain the exact DB/driver and OS matrix from the release owner, Enterprise
export package manifest and a maintained Python service build. Measure CPU/RAM/disk under representative load. No database,
built image or private Enterprise package was installed or changed.
