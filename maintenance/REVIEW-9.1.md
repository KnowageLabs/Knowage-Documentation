# Knowage 9.1 documentation review

Target: **9.1.0**, released 2 October 2026. Review prepared 19 October 2026.

## Source baseline

- Documentation repository base: `7a5096c8eb03360d31b2ac277f90fe93fd712119`.
- Backend release: `47d06115a965f8440527b77a9e41d990e77aa078` (`v9.1.0`).
- Frontend: `cbd1086dd2fee140fc96b26b207434d9eefb954a`, the exact submodule
  referenced by that backend tag. The development branch was not used as the
  release definition.
- Docker recipe: `26f22a44bc50e4a7bd19a71438227d7fb329acd7`.
- Primary release reference: [official release](https://github.com/KnowageLabs/Knowage-Server/releases/tag/v9.1.0).

## Scope delivered

The current manual contains **78 navigable source pages** plus the included
Tomcat configuration source. Page coverage is listed in `coverage-9.1.csv`.
Existing detailed technical examples were retained where the update did not
require replacement; this is not a wholesale rewrite of every paragraph.

The revision updates navigation, restores an accessible end-user guide and
adds release notes, AI assistant/management, home-page management and the
9.0 → 9.1 migration. It updates Dashboard/Cockpit separation, authoring,
dynamic titles/columns, map configuration, parameters/LOVs, QBE, users,
exports and scheduling. Installation packages and scripts point to the
release tag. Obsolete Angular localization and Log4j 1 instructions in active
pages were replaced with the current Vue and Log4j 2 configuration.

There are **695 named PNG screenshot placeholders** with an inventory and
replacement instructions. Small action glyphs and two conceptual diagrams
were retained. The PNGs are intentional placeholders, not captured 9.1 screens.

Historical manuals, duplicate copies and unused skeletons remain in the Git
repository and are excluded from the 9.1 build and its search index. Earlier
upgrade steps remain navigable for sequential migrations.

## Source details requiring release-owner attention

| Finding | Evidence | Documentation handling |
| --- | --- | --- |
| PostgreSQL migration contains `WITHOUT OIDS`; Oracle migration declares SQL `BOOLEAN`. | [Tagged database scripts](https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowagedatabasescripts/) | Added an explicit database-version compatibility check before production execution. The scripts themselves were not changed. |
| Public Compose uses `9.1-SNAPSHOT`, not an immutable release identifier; the project is in a nested directory and maps port 18080. | [Docker recipe](https://github.com/KnowageLabs/Knowage-Server-Docker/tree/26f22a44bc50e4a7bd19a71438227d7fb329acd7/Knowage-Server-Docker) | Corrected the working directory and port. Require the approved release image/digest or use released WAR packages. |
| Scheduler backend supports comma-separated output formats, while the tagged standard dialog has a single PDF/XLS selector. | [Output dialog descriptor](https://github.com/KnowageLabs/Knowage-Server-Frontend/tree/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/managers/scheduler/SchedulerTimingOutputTable/SchedulerTimingOutputDetailDialog/tabs/SchedulerTimingOutputOutputTab/SchedulerTimingOutputOutputTabDescriptor.json), [scheduler job](https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowage-core/src/main/java/it/eng/spagobi/tools/scheduler/jobs/XExecuteBIDocumentJob.java) | Describe multiple Timing & Output entries for the standard GUI and combined output through the supported integration. Do not invent a multi-format GUI selector. |
| Upload chooser offers XLS, but the Excel import parser instantiates `XSSFWorkbook`. | [UserDataParsing](https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowage-core/src/main/java/it/eng/spagobi/commons/utilities/UserDataParsing.java) | Recommend UTF-8 CSV or XLSX. |
| CSV import reads the third cell and maintains an attribute map across rows. | Same parser | Require the first three columns and explicit relevant attribute values on each row; ask maintainers to check missing-cell and attribute carry-over behavior. |
| Previous documentation promised migration by changing only the Cockpit engine. | Previous manual; separate document types/editors in 9.1 | Provide a reproducible Dashboard replacement workflow and validation of any converted template, rather than promising automatic conversion. |

## Requirements verification follow-up

The runtime requirements and Python installation pages were checked against the
release POMs and versioned Docker recipes. JDK 17, Tomcat 9.0.x and the Hazelcast
5.3.6 Java dependency are confirmed. MariaDB 10.3 and the Python 3.8 base source
are identified as legacy examples, not maintained production recommendations.
Exact database/driver certification, Enterprise export runtimes and hardware
sizing remain to be qualified. Published OS/browser
declarations are retained with attribution. Detailed evidence and the conflicting
Java 8 CI setting are recorded in [REQUIREMENTS-9.1.md](REQUIREMENTS-9.1.md).

## Chapter removal and edition labels

At the documentation owner's request, the current manual excludes the glossary,
Data Preparation and Performance Indicator chapters, including the KPI,
scorecard and alert subpages. Navigation, object import/export, role guidance,
installation and requirement references were cleaned accordingly. This is a
documentation scope change, not a claim that release binaries were removed.

The current manual has 78 navigable pages. The 82 captures belonging to removed
content were deleted, leaving 695 capture placeholders with unchanged IDs.
AI Management and the AI assistant are explicitly marked as Enterprise Edition
features on their pages, in navigation, at the manual entry point and in the
release overview. Existing edition-specific notices in other pages remain.

## Validation

- Sphinx **8.2.3**, Read the Docs theme **3.0.2**, Python **3.12**.
- Full HTML build with `-E -n -W --keep-going`: zero warnings/errors.
- Local HTML checks: **80 HTML files**, **5,576 references**, including files,
  images and fragment anchors. Screenshot inventory and PNG signatures checked.
- A GitHub Actions workflow and `make check` reproduce these checks.
- The incremental handoff is checked by applying only the changed files,
  complete replacement static folder and stated deletions to the preceding
  9.1 source bundle, then comparing the resulting source files.

No running Knowage installation or authenticated Enterprise distribution was
available for an end-to-end walkthrough. Browser visual QA could not run
because the environment lacked a browser executable and its download failed;
HTML structure and assets were checked directly. External links were not all
subjected to a live availability check. These limits are separate from the
successful Sphinx and local-reference checks.

## Publication handoff

Apply the changed source files over the preceding 9.1 revision and replace
the complete static directory. Delete the two chapter directories and glossary
source listed in the incremental handoff instructions. Build into a clean HTML
directory so removed pages cannot remain as stale output. Complete the actual
GUI captures and review workflows with representative roles and tenants.
Resolve the release-owner items above, then merge to the intended documentation
branch and activate that branch/version in Read the Docs. No remote branch,
pull request, release or Read the Docs publication was created by this update.
