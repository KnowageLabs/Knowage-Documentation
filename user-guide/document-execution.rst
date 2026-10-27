Document Execution
========================================================================================================================

In this chapter we describe all the features related to Knowage analytical documents, such as parameters management, printing, exporting and so on.

First of all, notice that once you execute a document from the document browser or from the menu, it is visualized full screen. In the first case, you can return to the document browser by clicking on the folder icon located at the top left.

.. figure:: media/image25.png

    Back to Document Browser

Parameters management
------------------------------------------------------------------------------------------------------------------------

Knowage documents may have associated parameters. If any, you will be asked to select the chosen parameter’s values in a collapsible panel located at the top or on the right side of the page. If this is the case, choose the parameters values and then click the **Execute** button to run the document. In case there are only optional parameters or default values are already defined, the document is directly executed after the first click on its relative icon.

.. figure:: media/parameters.png

   Parameters panel

Mandatory parameters are marked with an asterisk. Date controls respect the
minimum and maximum limits configured by the author. List and tree parameters
support search, including successive searches while selecting multiple values.

It is possible to show or hide the parameter panel by clicking on the filter button located in the document toolbar. With the **Reset** button at the top of the panel you can clear the form.

Furthermore, the parameter configuration can be saved for future use. This is particularly useful when the document includes several customized parameters. This feature is accessible from the toolbar located at the top right corner of the parameters panel.

- **Reset** inserted values for parameters;
- **Open saved** a window listing the **saved parameters**, so that you can select or modify them;
- **Save** the parameters. Here you can choose between two options: **Public** means visible to all the other users that share your role while **Private** means visible only to you.

Document Toolbar
------------------------------------------------------------------------------------------------------------------------

The toolbar menu shows the actions available for the current document and role.
Use the labelled commands to refresh the analysis, open its parameters, manage
views, export, open full screen or return to the browsing area.

Where enabled, **Info** contains metadata, notes and rating. **Shortcuts** can
provide scheduled executions and commands to add the document to Workspace,
copy a link or obtain HTML embedding code.

.. _documenttoolbar:
.. _toolbarcontexmenu:
.. figure:: media/toolbar.png

   Document toolbar in Knowage 9.1.


Exporters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each Knowage document can be exported into several formats, depending on the options offered by the engine.

Clicking the **Export** functionality in the document toolbar you will see the available formats for the current document. Select one and check the exported document.

.. figure:: media/export.png

   View document metadata

Business and structural metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Knowage allows the definition of business metadata to describe an object, in our case a document. Business metadata, unlike technical metadata used in Knowage Meta to build the metamodel, are business information associated to the document intended to help users to understand, access and classify it. As such, they have been mainly conceived for the end user understanding.

There are three types of business metadata, some of them are editable while others can only be read. In particular, general metadata are read-only, while short and long text metadata are editable. General metadata contain basic information about the document, which cannot be altered because they are related to the structure of the document (e.g., type, engine, label). They provide useful and synthetic information on the document. Short and long text metadata should be used to add relevant business information: all the allowed users will see this information, which will help them understand the purpose and context of that document.

In general, metadata should be edited by users with adequate expertise and authority to do so. Therefore, it is possible for the administrator to assign the right to edit and save metadata only to some users. The right is not specific to a profile, but it is part of the authorizations that can be granted to any role. This applies to bookmarks as well.

Metadata can be accessed from **Info** in the document toolbar menu, where enabled for your role.

.. figure:: media/image33.png

   View document metadata

As stated before, in order to see and/or edit metadata the user roles need some grants. Knowage administrator manages this authorizations. If you have editing metadata authorization, you will be able to see to change them. If you want to edit short metadata just click in the value area and write what you prefer. If you want to edit long metadata just click in the value area and an HTML editor will appear.

When you are satisfied with what you wrote just click on the **SAVE** button. We provide the following example.

.. figure:: media/image3435.png

   Editing metadata

Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Knowage offers a simple collaborative tool to share notes and comments on documents, allowing users to share information and receive feedback. This may be useful, for example, to limit the number of exchanged e-mails: notes can be stored online and are accessible to all users sharing the same access rights. Each user can add a single note to a single document.

Click on **Info** > **Notes** in the document toolbar menu. In this way a text editor opens where you can type your comment. Make it private or public (i.e., accessible to users with the same rights as you) by selecting the preference in the appropriate box. Click **Save** to confirm. All public comments from all users, as well as your private notes, will be shown the next time you open this window. If you want to edit or delete a note, click on the Rate document corresponding symbols in the **Note list** tab. You can also export the note in PDF or RTF format.

Rate document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The aim of this functionality is to acquire explicit quality data that can be further used. Specifically, it allows the administrator to identify anomalies about the use of an analytical document by end users. Rating a document means assigning it a value from the end user perspective. This brings additional information with respect to traditional audit and monitoring data, which can track the number of executions but cannot interpret users motivations and feelings.

.. figure:: media/image36.png

   Rating a document

To rate documents, open **Info** and the document rating action in the toolbar menu. Choose the document ranking in the pop-up window and click **Save**. The administrator can exploit the result of votes, in order to evaluate and improve the quality of the document.

.. figure:: media/image38.png

   Share notes and comments

Scheduled Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The administrator has the possibility to set schedulation for documents. These schedulations can be accessed by **Shortcuts** > **Show scheduled executions**, where enabled.

Saved views
-----------

Use **Views** in the document toolbar menu to open the **Saved views list**.
For a Dashboard, the list is accessible before the first execution, allowing
you to start from an existing saved view.

After loading the document and setting the desired values, choose
**Save current view**, enter a meaningful name and select the sharing options
available to your role. Reopen the view to restore its saved configuration.
Views retain the access rules of the underlying document and data.

.. figure:: main/saved-views.png
   :alt: Views menu and saved views list before dashboard execution.

   Opening a saved view.

Dashboard selections and navigation
-----------------------------------

Select a chart item, table value or selector value to filter the widgets
connected to that data. The document author determines which interactions are
enabled. An **Active selections** widget can show selections for all datasets
or for a specified dataset.

* Remove a selection through the active selections controls when it is
  editable. A locked selection remains in force until an authorized editor
  unlocks it.
* Use drill-down to move through the categories configured in a chart; use
  its back control to return to a higher level.
* A configured cross-navigation opens another document and passes mapped
  parameter values to it.

For details, see :doc:`/chapter_3/create_new_dashboard/index`.

