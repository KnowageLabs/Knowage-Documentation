Multidimensional Analysis
=========================

OLAP tools enable users to analyse multidimensional data interactively from multiple perspectives. OLAP consists of basic analytical operations: slice and dice, roll up, drill down and pivot.

OLAP user manual step by step
-------------------------------

We start our lecture on the OLAP engine by analysing an existing OLAP document. Open the document browser folder of the Knowage suite as in figure below and launch an OLAP document.

.. figure:: media/image134.png

    Browse the documents and select an OLAP document.

Here an example.

.. figure:: media/image135.png

      Exploring an existing OLAP document.

We will describe the main parts of the OLAP page in the following.

The filter panel
~~~~~~~~~~~~~~~~

Once the document is executed, the central area of the window contains the table whose measures are aggregated on dimensions. At the top of this area, panels are available to configure filters on attributes. We see in the following figure that the filter panel is made up of **Filter cards**. Here you can find the cube dimensions and their hierarchies as defined in the OLAP schema by the developer.

.. figure:: media/image136.png

    The filter panel.

The filter cards
~~~~~~~~~~~~~~~~

Filter cards can be placed on the filter panel or on column axis. You can switch their position dragging and dropping them from one place to the other.

.. figure:: media/image137.png

    The filter card inside the filter panel.

Filter cards are used to:

-  inform the user about available dimensions defined in OLAP schema,
-  inform the user about dimension’s name,
-  perfom slices,
-  Add the dimensions to the cube visualization,
-  place hierarchies in different axes,
-  filter visible members.

Considering :numref:`featuresoffiltcard`, we can see that a filter card is made up of:

- (a) an icon for opening dimension chooser dialog,
- (b) a dimension name,
- (c)+(e) icon slicer,
- (d) choosed filter name,

.. _featuresoffiltcard:
.. figure:: media/image138.png

    Features of a filter card.

Axes panel
~~~~~~~~~~

In the panel axes you can:

-  drag and drop one or more dimensions,
-  organise the dimensions visualization,
-  swap axes.

Referring to :numref:`axespanelfeat`, the axes panel consists of the following items:

-  (a) columns axis,
-  (b) row axis,
-  (c) filter cards,
-  (d) icon for swap axes,
-  (e) icon for hierarchy order.

.. _axespanelfeat:
.. figure:: media/image140.png

    Axes panel features.

Pivot table
~~~~~~~~~~~

The Pivot table is the central part of the OLAP page. In figure below is shown an example. 

.. figure:: media/image141.png

    Pivot table.

Pivot table is used to:

-  show data based on MDX query sent from the interface,
-  drill down/up hierarchies’ dimensions,
-  drill through,
-  show properties of a particular member,
-  sort data,
-  show calculated fields,
-  perform cross navigation to other documents.


Referring to :numref:`pivottablefeat`, Pivot table consists of:

-  (a) dimensions involved in the analysis,
-  (b) cells with data,
-  (c) icons for drill down and drill up,
-  (d) icons for sorting (only if enabled by the developer),
-  (e) icons for showing properties (only if enabled and configured by the developer),
-  links for cross navigation (only if enabled and configured by the developer)

.. _pivottablefeat:
.. figure:: media/image142.png

    Pivot table features.

Side bar
~~~~~~~~

You can open the side bar by clicking on the icon positioned on the top right side of the page (:numref:`openthesidebar`). Side bar will be shown on the right side (:numref:`sidebar`).

.. _openthesidebar:
.. figure:: media/image143.png

    Open the side bar.

Side bar is used to:

-  choose between different data representations,
-  choose between different drill types,
-  call dialogs and functionalities that effect the pivot table,
-  get additional data based on loaded model.

.. _sidebar:
.. figure:: media/image144.png

    Side bar.

The side bar shows the **Menu**. This area let you customize the Olap layout. As highlighted in :numref:`sidebarmenu`, the Menu is divided in three subsections:

-  (a) drill options,
-  (b) OLAP functions,
-  (c) table functions, 
-  what if.

.. _sidebarmenu:
.. figure:: media/image145.png

    Side bar Menu.

We start introducing the interface and leave the description to the next Section 7.2. In particular, referring to :numref:`drilltypes`, drill types consists of:

-  (a) position,
-  (b) member,
-  (c) replace,
-  (d) drill through.

.. _drilltypes:
.. figure:: media/image146.png

    Drill types.

Meanwhile, referring to :numref:`olapfunctions`, the OLAP functions consist of:

-  (a) reload model,
-  (b) show MDX,
-  (c) send MDX.

.. _olapfunctions:
.. figure:: media/image147.png

    OLAP functions.

Referring to :numref:`tablefunctions1`, table functions consist of:

-  (a) show parent members,
-  (b) hide spans,
-  (c) show properties,
-  (d) suppress empty rows/columns,
-  (e) enable compact properties,
-  (f) enable sorting,
-  (g) sorting settings,
-  (h) calculated field wizard.

.. _tablefunctions1:
.. figure:: media/image148.png

    Table functions.


Referring to :numref:`tablefunctions2`, what if consists of:

-  (a) lock/unlock model,
-  (b) save,
-  (c) save as new version,
-  (d) undo, 
- (e) delete versions, 
- (f) output wizard.

.. _tablefunctions2:
.. figure:: media/image149.png

    Table functions.


Functionalities
----------------

Placing hierarchies on axes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we already told, the user can easily move a dimension from the filter bar to the axis or viceversa dragging and dropping it to the desired place.

Let us suppose we want to move a dimension from the filter panel to the columns axis. The steps are summarized in figure below

.. figure:: media/image150.png

    Move a hierarchy to the columns axis.

Vice versa, to move back the dimension from the columns axis to the filter panel the user must simply drag and drop the dimension from one place to the other as in the following figure.

.. figure:: media/image151.png

    Move a dimension from the columns axis to the filter panel.

Similarly, a dimension can be moved from the filter panel to the rows axis simply dragging and dropping it from one place to the other.

Swaping axes
~~~~~~~~~~~~

To swap axes the user should click on the icon |image151|. The user will get the outcome showed in figure below.

.. figure:: media/image153.png

    Swap axes.

Selecting different hierarchies on dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an OLAP schema is defined, the user can choose different hierarchies of the same dimension. The icon for opening the dialog is positioned on the top left corner of the filter card (if the dimension has more than one hierarchy). Select the hierarchies icon underlined below.

.. figure:: media/image154.png

    Hierarchies icon.

A pop up will be displayed. :numref:`hierarchiesdialogpopup` shows its characteristics. The window will present:

- (a) the dimension name,
- (b) name of selected hierarchies,
- (c) drop down list of available hierarchies,
- (d) save button,
- (e) cancel button.

.. _hierarchiesdialogpopup:
.. figure:: media/image155.png

    Hierarchies dialog pop up.

After selecting the hierarchy and saving user’s choice, that hierarchy will be used by the pivot table.

If the user re-opens the dialog window, he/she sees the selected hieararchies and has the chance to change it if needed to, as shown below.

.. figure:: media/image156.png

    Changing the hierarchies.

We give an example of the output when the hierarchy “Time” is selected in :numref:`timehierarchieshowsdays` and hierarchy “Time Weekly” in :numref:`timeweeklyhierarchyshowsweek`.

.. _timehierarchieshowsdays:
.. figure:: media/image159.png

     Time hierachy: the table shows days in the month.

.. _timeweeklyhierarchyshowsweek:
.. figure:: media/image160.png

    Time Weekly hierachy: table shows weeks in the month.

Slicing
~~~~~~~

The slicing operation consists in the analysis of a subset of a multi-dimensional array corresponding to a single value for one or more members of the dimensions. In order to perform this operation you need to drag and drop the dimesion of interest in the axis panel.  Then clicking on the filter icon choose the new single focus and apply it. Once concluded these steps the cube will show only the selected level of the dimension, while the others have been sliced out.

:numref:`dialogforslicerchoosing` shows the slicer option panel which consists of:

- (a) a dimension name,
- (b) a search input field,
- (c) a search button,
- (d) a show/hide siblings checkbox,
- (e) a member tree,
- (f) a selected member icon,
- (g) a highlighted member (result of searching), 
- (h) a save and a cancel buttons.

.. _dialogforslicerchoosing:
.. figure:: media/image161.png

    Dialog for slicer choosing.

In particular, it is possible to search for a member in three ways:

1. by browsing the member tree;

.. figure:: media/image162.png

   Browsing the member tree.

2. by typing member’s name or it’s part in the input field and clicking on the search button. The research will be possible if the user enters at least four letters. If the user wishes to include member’s siblings to the research, the checkbox (:numref:`dialogforslicerchoosing`, (d))needs to be checked;

.. figure:: media/image163.png

   Using the research box.

3. after the first research, if the user types some other member’s name before clicking on the search button, visible members whose        names contains a entered text will be highlighted.

.. figure:: media/image165.png

    Using the research box after a first investigation.

Once the selection has been saved, the users choice will affect the pivot table and the filter cards slicer name will rearrange.

Filtering
~~~~~~~~~

To filter dimension members in a pivot table, the user should click on a button (see :numref:`featuresoffiltcard`) located on the right side of dimension’s filter card placed in the filter area.

The procedure to search for a member using the filter dialog has no meaningful differences with the one described for the slicer chooser dialog. The pop up interface is the one showed below. After selecting a member, the user should click on the save button. The pivot table will display the changements. Otherwise click on the cancel button to discard changes.

.. figure:: media/image166.png

    Filter dialog.
    
.. figure:: media/image167.png

    Filter effects on pivot table.

Drill down and drill up
~~~~~~~~~~~~~~~~~~~~~~~

User can choose between drill types by clicking on one of the three buttons in the drill types section of the side bar (Figure 7.10). There are three drill types. In the following we give some details on them.

1. **Position**: this is the default drill type. Clicking on a drill down/drill up command will expand/collapse a pivot table with          child members of a member with that particular command. See below.

.. figure:: media/image168.png

     “Position” drill down.

2. **Member**: if the user wants to perform drill operation not only on one member per time but on all members of the same name and        level at the same time it is needed to select member drill type. See below.

.. figure:: media/image169.png

   Figure 7.31: “Member” drill down.

3. **Replace**: This option lets the user replace the parent member with his child member during drill down operation. To drill up the      user should click on the arrow icon next to the dimension name on which to perform operation. See figure below.

.. figure:: media/image170.png

    “Replace” drill down.

Drill through
~~~~~~~~~~~~~

To perform drill through operation the user needs first to select a cell, as in the following figure, on which to perform operations. Then clicking on the button for a drill through in the side bar, a dialog will open with results (this pop up could take some time to    open).

.. figure:: media/image171.png

    Drill thorugh option.

In particular, referring to :numref:`drillthoroughwindow`, drill though dialog consists of:

-  (a) a hierarchy menu,
-  (b) a table of values,
-  (c) a maximum rows drop down list,
-  (d) a pagination,
-  (e) a apply button,
-  (f) a export button,
-  (g) a cancel button.

.. _drillthoroughwindow:
.. figure:: media/image172.png

    Drill thorugh window.

The user must therefore select a cell, open the side bar and select the drill through item from the panel. A pop up will show up: here the user can choose the level of detail with which data will be displayed. The steps to follow are:

1. to click on hierarchy in hierarchy menu,

2. to check the checkbox of the level,

3. to click on the “Apply” button (after checking the checkbox, remember to click outside of the level list and then select apply).

The user can also select the maximum rows to load by choosing one of the options in the drop down list (see :numref:`drillthoroughwindow`, (c)). Finally, loaded data can be exported in csv format by clicking on the “Export” button.

Refreshing model
~~~~~~~~~~~~~~~~

To refresh a loaded model the user needs to click on the “Refresh” button available in the side bar panel. This action will clear the cash, load pivot table and the rest of data again.


Showing MDX
~~~~~~~~~~~

To show current mdx query user should click on show mdx button in the side bar. Figure below shows an example.

.. figure:: media/image173.png

     Showing MDX query example.


Sending MDX
~~~~~~~~~~~

If you want to execute an MDX query you need to:

-  click on send MDX button in the sidebar,
-  type a query in a text area of send MDX dialogs, 
-  click on the save button.

.. figure:: media/image174.png

    Sending MDX query example.

Result of the MDX query “should” appear in pivot table as in figure below. In fact, the user is responsable for entering *valid* MDX query.

.. figure:: media/image175.png

    Sending MDX query example.


Showing parent members
~~~~~~~~~~~~~~~~~~~~~~

If a user wants to see additional information about members shown in the pivot table (for example: member’s hierarchy, level or parent member) he should click on a show parent members button in the side bar panel. The result will be visible in the pivot table. An example is shown in the following two figures.

.. figure:: media/image176.png

    Pivot table without the parent members mode.

.. figure:: media/image177.png

    Pivot table after the parent members selection.

Hiding/showing spans
~~~~~~~~~~~~~~~~~~~~

To hide or show spans the user should click on show/hide spans button in the side bar. The result will be visible in pivot table as in figure below.

.. figure:: media/image178.png

    Hide/show spans.

Showing properties
~~~~~~~~~~~~~~~~~~

In OLAP schema the XML member properties, if configured, could be represented in two possible ways:

1. as part of pivot table where a property values are placed in rows and columns. To get these values, the user needs to click on show      properties button in the side bar. Results will be shown in the pivot table;

.. figure:: media/image179.png

    Show properties.

2. in a pop up as compact properties. To enable compact properties user should click on enable compact properties button in the side bar. In this way in all the cells of members Suppressing empty colunms/rows which has property set, a table icon appears. This icon lets the property pop up opens. Figure below shows an example.

.. figure:: media/image180.png

    Show properties summarized in a pop up.

Suppressing empty colunms/rows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To hide the empty rows and/or colums, if any, from pivot table the user can click on the “Suppress empty rows/colums” button in the side bar panel. An example is given in Figure below.

.. figure:: media/image181.png

    Suppressing empty colunms/rows.

Sorting
~~~~~~~

To enable member ordering the user must click on the “Enable sorting” button in the side bar panel. The command for sorting will appear next to the member’s name in the pivot table. In addition, the sorting command will show the members of “Measures” hieararchy or members that are crossjoined with them, as shown below. 

.. figure:: media/image182.png

    Member sorting.

To sort members the user needs to click on the sorting command |image179|, available next to each member of the pivot table. Note that the sorting criteria is ascending at first execution. If the user clicks on the sorting icon, criteria will change to descending and the result will be shown in pivot table.

To remove the sorting, the user just have to click on the icon again. To change sorting mode user should click on sorting settings button in the side bar. Referring to the following figure, dialog sorting settings consists of:
   
.. figure:: media/image185.png

    Sorting settings window.

-  (a) sorting modes:
-  (b) basic (by default),
-  (c) breaking,
-  (d) count,
-  (e) a number input field for count mode definition,
-  (f) a save button.

Note that “breaking mode” means that the hierarchy will be broken.

If the user selects “Count sorting” mode the top or last 10 members will be shown by default in the pivot table. Furthermore, the user can also define a custom number of members that should be shown. 

Calculated members and sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Firstly we stress that to enable **Calculated fields** in your Olap document a proper button tag is needed in your Olap template. Such a tag is <BUTTON_CC visible="true"/>.

Once enabled, to create a calculated member/set the user should:

.. figure:: media/image186.png

   Calculated member.

1. select a member of the pivot table, as in figure above, which will be the parent of the calculated member,

2. click on the “calculated field” button in the side bar panel: a “Select function” dialog will appear. The latter consists of            (refer to :numref:`selectfunctiondialog`):

   -  (a) a name input field,
   -  (b) an aggregation functions tab,
   -  (c) an arithmetic functions tab,
   -  (d) a temporal functions tab,
   -  (e) a custom functions tab,
   -  (f) a recent functions tab,
   -  (g) an available functions list,
   -  (h) ok and cancel buttons.

.. _selectfunctiondialog:
.. figure:: media/image187.png

    Select function dialog.

The function definition used to create calculated members are read from the formula.xml file, located at: ROOT/resources/yourTennant/Olap folder. Functions are divided by few different tabs. In particular,\ **Tab Recent** contains calculated members and calculated sets created by user and saved in cookies. If there are no sets/members stored in the cookies, that tab will be empty. **Tab Custom** is where to define custom functions. These functions can be used to make really complex operations that are not part of predefined MDX functions. There you can use combination of few functions together or use operators for complex mathematical  calculations. They are also defined in formulas xml. If a specific tab doesn’t contain any formula, it will not be displayed. The “Name” field is mandatory, indeed the creation of a function without a name is forbidden. In **Recent tab**, the “Name” field is hidden for  Figure 7.48 provides an example of edited formula in the formulas.xml file.

.. figure:: media/image188.png

    Example of one formula inside of formulas xml.

3. Select a function and enter a calculated member/set name and click on “Ok”. A dialog for arguments defintion will show up, as shown in :numref:`argumentdefdialog`. This is made up of the following elements:

- (a) selected function name,
- (b) function description,
- (c) text input fields for argument expression,
- (d) expected MDX expression return type,
- (e) argument’s MDX expression description,
- (f) open saved button, 
- (g) select from table button,
- (h) ok and cancel buttons.

.. _argumentdefdialog:
.. figure:: media/image189.png

    Argument defintion dialog.

In particular, to input MDX expression argument, the user has three options, listed in the following.

1. Type it manually (for advance users).

2. Select members from the pivot table: to select a members that are going to be included in a set, the user should (see :numref:`selectingmembers`):

   -  click on select from table button,
   -  click on members in a pivot table,
   -  click ok in dialog to finish selection.

.. _selectingmembers:
.. figure:: media/image190.png

    Selecting members.

The expression of selected members will be imported in text input fields for argument expression as figure below shows.

.. figure:: media/image191.png

    Expression of the selected members.

3. Import expression from saved calculated members or sets. To import calculated member/set, the user should:

   • Click on open saved button. Then the dialog of saved calculated members/sets will appear (:numref:`savedsetsdialog`) and it consists of:

     -  a list of saved calculated members and sets,
     -  a calculated member/set name,
     -  calculated member/set return type is shown by round icon.

.. _savedsetsdialog:
.. figure:: media/image192.png
   
    Saved sets dialog.

   •  Click on calculated member/set. The expression of saved calculated member/set will be imported in text input fields for argument         expression, as highlighted below.
   
.. figure:: media/image193.png

    Expression of the saved/calculated member/set.

   •  After filling all the arguments of function, clicking on OK button will:

      -  add calculated member in a pivot table,
      -  save calculated set and it will be available for creation of other calculated member and sets.


In tab “Recent”, opening the “Select function” dialog the user can find a list of saved calculated member and sets which can be edited or deleted. Editing is done by clicking on one of them. 

.. figure:: media/image194.png

   Edit a calculated member.

Deleting is done by Delete button as shown in figure above.

.. include:: olapThumbinals.rst
