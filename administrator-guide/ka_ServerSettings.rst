
KPIs
----

In this section we describe how to manage the import/export of KPIs
between two tenants.

The user must enter Knowage as administrator of source tenant and click
on **Import/Export KPIs** from Server Manager menu panel, as shown in
Figure 9.13.

   |image73|

   Figure 9.13: KPIs Import/Export from menu

The window in Figure 9.14 opens. The page contains the **Export** and
the **Import** tab, where the user can select the KPIs for the
export/import respectively.

KPIs

   |image74|

   Figure 9.14: KPIs Import window

Let’s start from the export feature. The user must check the KPIs for
the export using the tab interface. He/she can add some more
functionalities to the export action, namely:

-  to include targets,

-  to include those scorecards related to the selected KPIs,

-  to include schedulations.

Finally click on the red download button (see Figure 9.15) to get a
zipped folder that will be used to conclude the export.

   |image75|

   Figure 9.15: Start export button

Once the .zip file is downloaded, the user has to switch tenant (the one
on which he/she wants to do the import). As admin of the destination
tenant, enter the Import/Export KPIs functionality and move to the
Import tab.

The user must therefore browse the personal folder to catch the zipped
folder and click on the red upload button just aside, as shown in Figure
9.16.

Referring to Figure 9.17, the user has to specify if:

-  to overwrite the existing KPIs and their related formulas,

..

   |image76|

   Figure 9.16: Import tab

-  to import targets,

-  to import scorecards,

-  to import schedulations.

..

   |image77|

   Figure 9.17: Import KPIs settings

Once the import is started, the GUI leads the user to finalise the
import procedure. In particular, the user is asked to map data sources
correctly (Figure 9.18).

   |image78|

   Figure 9.18: Mapping data sources

The process ends successfully when the wizard in Figure 9.19 shows up.

Analytical Drivers
------------------

This option allows to import/export the analytical drivers and their
related LOV.

   |image79|

   Figure 9.19: Import KPIs ended successfully

   |image80|

   Figure 9.20: Import/Export of analytical drivers As shown in Figure
   9.20, the window contains the Export and the Import tab. Use the
   Export tab to download the .zip file to be used in the import
   process.

To produce suce a file, the user has to log in as administrator of the
source tentant. Then he has to assign a name to the export, check the
analytical drivers of interest and click on the red download button
available at the top right corner of the page. Note that it is possible
to slim down the research of the analytical drivers by filtering on
their data of creation.

Switch tenant and log in as administrator. Use the Import tab to upload
the zipped folder and finalise the import.

   |image81|

   Figure 9.21: Import of analytical drivers

Use the GUI exhibited in Figure 9.21 to upload the zipped folder, to
specify if to overwrite on the existind analytical drivers or add
missing. Then click on next and continue by mapping roles among tenants
and data sources.

   |image82|

   Figure 9.22: Import of analytical drivers

   |image83|

   Figure 9.23: Import of analytical drivers

The process ends with a message containing the information about the
import.

Glossay

Glossay
-------

The export/import of glossary allows the user to allign glossaries among
tenants.

   |image84|

   Figure 9.24: Export/Import of glossaries window

There are the two tabs of Export and Import in this instance too (Figure
9.24). The user is asked to select the glossaries to export and to type
a name that will be assigned to the zipped folder. The user can help
himself/herself by using the filter on data (of creation of the
glossary).

Once the user has got the zipped folder he/she must switch tenant and
enter as its admin. Then select the import tab from the Export/Import
main window.

   |image85|

   Figure 9.25: Import of glossaries

The user must use the arrows (Figure 9.25) to indicate the glossaries
he/she wants to import in the target tenant. No further information are
needed to end the process. Then the user has to enter the target tenant
as administrator and use the import tab to finalise the import.

Catalog
-------

This functionality allows to Export/Import the following elements

-  Data sets,

-  Business models,

-  Mondrian catalogs,

Catalog

-  Layers,

-  SVG files.

The steps to perform the Export/Import are equal to those seen in the
previous sections. Namely, the user has to enter the **Import/Export
catalog** menu item from Server Manager menu panel. The window will
contain the Import and Export tabs. The export tab is used to produce
the zip folder to be imported in the tenant of interest. Note that the
user can apply a temporal filter to help him/her to look up elements in
the list.

   |image86|

   Figure 9.26: Import of catalog

The import requires the zipped folder to be uploaded, to check the
elements to import, to map roles among tenants and to map datasources.

In this chapter we describe all functionalities available in Server
Settings panel of the Administrator Menu shown in Figure 10.1.

   |image87|

   Figure 10.1: Server Settings Panel.

Similar editors give you access to configurations and domains. We are
going to provide an example of both cases to let you understand how
thier management works. A complete overview of metadata creation,
editing and management conclude this chapter.

10.1 Configuration Management
=============================

By clicking on the **Server Settings** > **Configuration Management**,
you can manage many configuration elements. For example here you can set
default language as well as mail settings. Start typing DEFAULT in the
search form, as shown in Figure 10.2, to filter among available items
and find what you are interested it.

We provide an example to let you understand the usage of the interface.
Suppose you want to set italian as default language. Select the row with
SPAGOBI.LANGUAGE_SUPPORTED.LANGUAGE.

10.2. Domain Management

   |image88|

   Figure 10.2: Configuration categories list.

default as label and click the pencil icon at the end of the row to edit
the element. Insert it,IT as **Value Check** as click **Save**.

You can view available languages and their code (**Value Check column)**
in the row SPAGOBI.

LANGUAGE_SUPPORTED.LANGUAGES.

10.2 Domain Management
======================

By clicking on **Domains Management** item menu, you can manage
categories. In Figure 10.3 we show Domain Management editor. You can add
for example new categories for a business model, for a dataset and for
all domain you can see in the **Domain name column**.

   |image89|

   Figure 10.3: Domain management editor.

We provide an example to describe how it works. Suppose you want to add
a new category among the datasets, named “Costs”. In Figure 10.4 you can
see the categories already existing.

   |image90|

   Figure 10.4: Business Model Categories already existing.

Click on the plus red button in the top right corner and by default a
new page opens with the

10.3. Metadata

form you need to fill in. An example is shown in Figure 10.5. Fill the
columns as follow:

   |image91|

   Figure 10.5: Form to be filled to create a new category.

-  **Value code**: Costs

-  **Value name_image**: Costs

-  **Domain code**: CATEGORY_TYPE

-  **Domain name_image**: Costs Datasets

-  **Value description**: Costs Datasets

All the values except the **Domain code** to you. the last are mandatory
for correct configuration. Now Click on Save. You have successfully
create your new dataset category.

You can also modify an existing domain by selecting its dedicated row
and clicking the edit button.

10.3 Metadata
=============

Knowage offers the possibility to define metadata categories and then
give them a value for each analytical document and for each subobject.

In the metadata page, shown in Figure 10.6, you can see the list of
existing metadata. Here you can also define a new metadata using the
dedicated button.

   |image92|

   Figure 10.6: List of existing metadata.

You define a new metadata by giving it a **Label**, a **Name**, a
**Description** and a **Type**. The **Label** is a unique identifier,
the **Name** is what will be shown to the end user and the **Type** can
be either SHORT TEXT or LONG TEXT.

Metadata

We recall that metadata visibility is one of the authorization you can
set while creating roles. Only the users associated to roles which have
this authorization will view metadata. In addition, in order to edit
metadata the user roles need to have another authorization called **Save
Metadata**.

|image93|
