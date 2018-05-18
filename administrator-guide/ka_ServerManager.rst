9.1.

   |image61|

   Figure 9.1: Server Manager Panel

Those about **Import/Export** let you export some configurations or
elements from one istallation to another. This can be helpful for
example in managing a test and a production areas. We are going to give
the full description of these funtionalities in the following.

9.1 Tenants Management
======================

We start this Section undeling that only those users who have the
superadmin role can use this functionality. In addition, although
implemented, this menu item is not visible in Figure 9.1. In fact, the
**Tenants Management** is available only for users who possess the
Knowage Enterprise Reporting (ER) license. A **tenant** is generally a
user who can or cannot employ specific product Tenants Management

types or access some (or all) datasources inside the same environment.
Then, this functionality allows you to create new tenants or manage old
ones. The Tenants Management window is shown in Figure 9.2. On the left
you have the list of existing tenants. On the top of such list it is
available the **Search** box to help users to browse the tenants. When
clicking on the “Plus” icon you can create a new tenant. A form opens on
the right area. Insert a **Name** and a **Theme**. Then change tabs to
set product types access and select which datasources are achievable. An
example is given in Figure 9.3.

   |image62|

   Figure 9.2: Tenants Management window.

   |image63|

   Figure 9.3: Product types tab (Left) Datasources tab (Right).

Note that, in a single-tentant environment admin and superadmin
coincides. In a multitenants environment (developed then through the
Server Manager functionality), only *one* user has the superadmin role
for each tenant, while there can be one or more users with admin role.
In particular compared to the admin case, the superadmin has the
possibility to manage the multi-tenancy. Moreover, he is the only one
who can configure the JNDI datasources and access the cache
configuration (through the cache manager menu item).

9.2. Template Management

9.2 Template Management
=======================

Each Knowage document is associated to a *template*. The template
defines the standard layout of a document, including specific
information on its appearance and the way contents should be displayed.
Templates can be encoded by hand or using Knowage Studio designers, when
available. For each analytical document the history of templates is
maintained. Old templates can be restored if needed. A new version is
saved at each deployment, either manual or from Knowage Studio.

The **Template Management** let you choose a starting date before which
delete the templates versions. This could be very useful because it
allows the administrator to clean the environment and save space in
Knowage metadata database once a document life cycle is completed.

First of all you are asked to insert a date by clicking on the calendar
icon. Then click the magnifier icon and select the documents you are
interested in. The list displayed contains only documents created before
the selected date. Clicking the trash icon you delete the template of
the selected documents which were uploaded before the chosen date. If
all the templates of a document precede the chosen date, the last
template uploaded will be kept, so that no document is deleted
accidentally. We sum up the steps described in Figure 9.4.

9.3 Import\Export
=================

These options are about Import\Export of Documents, Menu, Users, KPIs
and Catalogs. Let’s focus on each of these features.

Documents
---------

This feature let you create and download a .zip of whole or a part of
the documents existing in your Knowage installation. In this way you can
upload it in another istallation or keep it as backup.

When you import, all the “objects” associated to those documents (such
as datasets, lovs, drivers, roles and folders) are created. Instead
users, menu configurations, hot link and remember me are not exported
with this tool.

Let’s have a look on the steps to create the .zip.

In Figure 9.5, we show the export editor.

First of all choose the name to give to your exportation (i.e. if you
choose MyFirstExport, you will create the MyFirstExport.zip.

Documents

   |image64|

   Figure 9.4: Deleting templates

   |image65|

   Figure 9.5: Document Export

Menu

Then select which documents do you want to export. You can browse the
folder by clicking the folder icon. Choose the elements or folders you
want to include by marking the related checkbox. A check in a parent
folder will automatically select/deselect all its childer
folders/leaves.

When you have chose a name and select some documents the export icon
change colour from gray to pink. This means all elements are set to
start exporting. Before going on decide if you want to export
**Subviews** and **Snapshot** as well one or both of them. Now you are
ready to click on the export icon to generate and download the .zip.

Suppose you want to upload MyFirstExport.zip in another installation.
Log in it and move to **Server Manager** >\ **Import\Export Documents**
area Switch to the **Import** tab and click on **Browse** to accede your
personal folders. In Figure 9.6 we show the document import interface.

   |image66|

   Figure 9.6: Document Import

Choose the .zip obtained from the **Export** phase and click on the
import icon. Few steps guide you trought importation. You are asked to
map from source to target: the Roles, the Engines and the Metadata. If a
role doesn’t map any of the existing among the target one, it will be
created. Please keep attention during the metadata step beacause you can
choose to overwrite or don’t the target metadata. By default this option
is set to false. If you change to yes documents, lov, driver, etc. which
has the same label of the exported ones will have metadata overwritten
at the end of import procedure.

Menu
----

This feature let you export the menu structure.

   |image67|

   Figure 9.7: Menu Export

To start the export you need only to insert the Export name. Once
inserted the name, the export icon changes colour from grey to pink to
let you understand all mandatory fields to Users

start the export were filled. Click on this icon and the related .zip is
downloaded.

To upload it in another istallation, accede to the **Import\Export**
Menu area and switch to the tab **import**. Here click on **Browse** to
search in your folders the .zip previously created, see Figure 9.8.

   |image68|

   Figure 9.8: Menu Import

Then choose between the two import modes: **Override** and **Add
Missing**. If you choose **Override**, the menu items which match with
existing ones will be override by the imported. If you choose **Add
missing** only the menu items which don’t match with the existing one
will be added. You are ready to start importation by clicking on **Start
Import**.

Users
-----

In this area you can export the users from an installation to another,
see Figure 9.9.

   |image69|

   Figure 9.9: User Export

To generate the .zip you have to mark the user to include in the export
and insert an export name. Save the export in the folders of your pc and
move to the other installation. You have the chance to include the
personal folder of the chosen users in the Export. Put a mark in the
**Export Personal folder** checkbox and choose if you want to include
snapshots and subviews too.

To import the .zip in another installation, log in and open the **Server
Manager** > **Import\\**

**Export Users**, switching to **Import** area. Here click on **Browse**
to choose the .zip created by exportation. Then click on the import
icon. The users contained in your file are uploaded and Catalogs

   |image70|

   Figure 9.10: User Import

displayed in the left side of the screen. Choose among the users
displayed the one you want to import, mark them and click on the arrow
to move them in the other side. Now click on **Start import** button and
your users are successfully created in this installation too. Keep
attention in marking personal folder checkbox if you want that personal
folders are imported. In Figure 9.10 you can see **User Import**
interface.

Catalogs
--------

In this area you can export the different catalogs (such as datasets
catalogs, business models catalogs and so on) from one installation to
another, see Figure 9.11.

   |image71|

   Figure 9.11: Catalogs Export

To generate the .zip you have to mark the elements to include in the
export and insert an export name. Save the export somewhere in your
local system and move to the other installation. You have the chance to
include the personal folder of the chosen users in the Export. Put a
mark in the **Export Personal folder** checkbox and choose if you want
to include snapshots and subviews too.

To import the .zip in another instance, log in and open the **Server
Manager** > **Import\\ Export Catalogs**, switching to **Import** area.
Here click **Browse** to choose the .zip created through exportation.
Uploading the file, the available exported catalogs are displayed in the
bottom area. Selecting a catalogs (for instance, the **Dataset** one),
all the catalogs exported elements are displayed in the left side of the
screen. Choose the ones that you want to import, decide if you want to
override or to just add the missing ones and then click **Start
import**. Your catalogs are successfully created in this environment. In
Figure 9.12 you can see **User Import** interface.

KPIs

   |image72|

   Figure 9.12: Catalogs Import
