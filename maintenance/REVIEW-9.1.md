# Conservative review of the Knowage 9.1 documentation

Review date: 26 October 2026. Target: **9.1.0**.

## Baselines and scope

- Original documentation: `d73d7265a051e7ded9a8dc0721008ca0fdc86edd`.
  Compared with the previous base (`7a5096c8eb03360d31b2ac277f90fe93fd712119`),
  the only upstream change is the copyright year. The current 2026 value is retained.
- Backend: `47d06115a965f8440527b77a9e41d990e77aa078`, tag `v9.1.0`.
- Frontend: `cbd1086dd2fee140fc96b26b207434d9eefb954a`, the submodule revision
  referenced by that backend tag.
- Docker recipe: `26f22a44bc50e4a7bd19a71438227d7fb329acd7`.

The review compares the prior delivery with the original manual and the tagged
implementation. It restores original prose and illustrations where no
functional change justifies a rewrite. Existing version numbers in historical
upgrade instructions are retained. The documentation itself remains version 9.1.

The previous delivery had shortened useful explanations and replaced almost
every screenshot. That approach has been reversed. The page-by-page actions
are recorded in `coverage-9.1.csv`. An unchanged page is retained documentation,
not a claim that the entire feature has been retested in a running 9.1 system.

## Corrections to the previous delivery

1. **Cockpit conversion:** the prior rewrite incorrectly required creating a
   replacement Dashboard and rebuilding all widgets. The tagged controller
   invokes `formatModel` for legacy templates. The compatibility helper has
   conversion paths for Map and Crosstab/Pivot as well. The original engine-change
   procedure is restored, with backup and validation of a copy. It does not
   promise that every custom setting survives conversion.
2. **Scheduling:** removed the undocumented instructions for configuring a
   combined-output integration or several entries as a verified workaround.
   The standard dialog exposes one output format per selection. The backend
   parses comma-separated formats, but that does not establish a public GUI
   procedure. The release capability and the dialog are described separately.
3. **User guide:** restored the behavioural-model explanation, role types,
   workspace descriptions, metadata, notes and document rating. Changes are
   limited to navigation, account fields, toolbar groups, parameter search/date
   bounds and saved views. The 9.1 account dialog edits passwords; it no longer
   has the old name/surname/email fields.
4. **Requirements and installation:** retained the old structure and useful
   JNDI, database dialect, Quartz and deployment instructions. Corrected Java
   environment examples, the nested Docker working directory, release/schema
   references, invalid Compose fragments, Log4j 2 configuration and Python
   package/working-directory assumptions. The Java 17 Security Manager section
   is retained with an explicit description of the permissive policy.
5. **Screenshots:** restored original image files at their original paths.
   Placeholders remain for targeted changes and one image absent from the
   original repository. Existing QBE and OLAP filename errors were corrected.
6. **Scope and editions:** Glossary, Data Preparation and Performance Indicator
   chapters and their active navigation/references remain removed. AI Management
   and the AI assistant are explicitly labelled Enterprise Edition only.

## Targeted 9.1 additions retained

- Dashboard dynamic titles and columns, position locks, column visibility,
  pivot options, map wizard, dataset-specific selections and export naming.
- LOV cloning, date-driver limits, parameter search and formatted QBE tooltips.
- Bulk-user actions and corrected CSV/XLSX import requirements.
- AI Management, AI assistant, home-page management and 9.0-to-9.1 upgrade pages.
- Current language-resource paths for the Vue frontend.

## Verification and limits

The Sphinx build runs with nitpicky mode and warnings treated as errors.
`tools/check_docs.py` checks generated local links, anchors, screenshot
inventory and unused placeholder PNGs. The final counts are in `VALIDATION.txt`.
The original content is preserved except for the changes listed in the coverage
file and the minimal markup repairs needed for the strict build.

No live Knowage installation, database upgrade, private EE package or export
service was exercised. Confirm the exact OS/database/JDBC certification and
EE service versions with the distribution owner. Migration fidelity, GUI
captures and end-to-end procedures still require testing on the target instance.

## Reproducible source references

- [Release](https://github.com/KnowageLabs/Knowage-Server/releases/tag/v9.1.0).
- [Original manual](https://github.com/KnowageLabs/Knowage-Documentation/tree/d73d7265a051e7ded9a8dc0721008ca0fdc86edd).
- [Dashboard controller](https://github.com/KnowageLabs/Knowage-Server-Frontend/blob/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/documentExecution/dashboard/DashboardController.vue).
- [Legacy template conversion](https://github.com/KnowageLabs/Knowage-Server-Frontend/blob/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/documentExecution/dashboard/helpers/DashboardBackwardCompatibilityHelper.ts).
- [Widget editor](https://github.com/KnowageLabs/Knowage-Server-Frontend/tree/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/documentExecution/dashboard/widget/WidgetEditor).
- [Document toolbar](https://github.com/KnowageLabs/Knowage-Server-Frontend/blob/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/documentExecution/main/DocumentExecutionHelpers.ts).
- [Account dialog](https://github.com/KnowageLabs/Knowage-Server-Frontend/blob/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/mainMenu/dialogs/AccountDialog.vue).
- [User import parser](https://github.com/KnowageLabs/Knowage-Server/blob/v9.1.0/knowage-core/src/main/java/it/eng/spagobi/commons/utilities/UserDataParsing.java).
- [Management modules](https://github.com/KnowageLabs/Knowage-Server-Frontend/tree/cbd1086dd2fee140fc96b26b207434d9eefb954a/src/modules/managers).
- [Scheduler job](https://github.com/KnowageLabs/Knowage-Server/blob/v9.1.0/knowage-core/src/main/java/it/eng/spagobi/tools/scheduler/jobs/XExecuteBIDocumentJob.java).
- [Database scripts](https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowagedatabasescripts).
- [Core configuration](https://github.com/KnowageLabs/Knowage-Server/tree/v9.1.0/knowage/src/main/resources).
- [Docker recipe](https://github.com/KnowageLabs/Knowage-Server-Docker/tree/26f22a44bc50e4a7bd19a71438227d7fb329acd7/Knowage-Server-Docker).
