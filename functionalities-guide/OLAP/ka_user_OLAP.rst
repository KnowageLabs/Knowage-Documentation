
MULTIDIMENSIONAL ANALYSIS
=========================

OLAP tools enable users to analyse multidimensional data interactively from multiple perspectives. OLAP consists of basic analytical operations: slice and dice, roll up, drill down and pivot.

 OLAP user manual step by step
-------------------------------

We start our lecture on the OLAP engine by analysing an existing OLAP document. Open the document browser folder of the Knowage suite as in Figure 7.1 and launch an OLAP document. Figure 7.2 exhibits an example.

   |image134|

   Figure 7.1: Browse the documents and select an OLAP document.

We will describe the main parts of the OLAP page in the following.

   |image135|

   Figure 7.2: Exploring an existing OLAP document.

The filter panel
~~~~~~~~~~~~~~~~

Once the document is executed, the central area of the window contains the table whose measures are aggregated on dimensions. At the top of this area, panels are available to configure filters on attributes. We see in Figure 7.3 that the filter panel is made up of **Filter cards**. Here you can find the cube dimensions and their hierarchies as defined in the OLAP schema by the developer.

   |image136|

   Figure 7.3: The filter panel.

The filter cards
~~~~~~~~~~~~~~~~

Filter cards can be placed on the filter panel (Figure 7.4) or on column axis. You can switch their position dragging and dropping them from one place to the other.

   |image137|

   Figure 7.4: The filter card inside the filter panel.

Filter cards are used to:

-  inform the user about available dimensions defined in OLAP schema,

-  inform the user about dimension’s name,

-  perfom slices,

-  Add the dimensions to the cube visualization,

-  place hierarchies in different axes,

-  filter visible members.

Considering Figure 7.5, we can see that a filter card is made up of:

-  (a) an icon for opening dimension chooser dialog,

-  (b) a dimension name,

-  (c)+(e) icon slicer,

-  (d) choosed filter name,


   |image138|

   Figure 7.5: Features of a filter card.

Axes panel
~~~~~~~~~~

In the panel axes you can:

-  drag and drop one or more dimensions,

-  organise the dimensions visualization,

-  swap axes.

Referring to Figure 7.6, the axes panel consists of the following items:

-  (a) columns axis,

-  (b) row axis,

-  (c) filter cards,

-  (d) icon for swap axes,

-  (e) icon for hierarchy order.

   |image139|

   Figure 7.6: Axes panel features.

Pivot table
~~~~~~~~~~~

The Pivot table is the central part of the OLAP page. In Figure 7.7 is shown an example. 

   |image140|

   Figure 7.7: Pivot table.

Pivot table is used to:

-  show data based on MDX query sent from the interface,

-  drill down/up hierarchies’ dimensions,

-  drill through,

-  show properties of a particular member,

-  sort data,

-  show calculated fields,

-  perform cross navigation to other documents.


Referring to Figure 7.8, Pivot table consists of:

-  (a) dimensions involved in the analysis,

-  (b) cells with data,

-  (c) icons for drill down and drill up,

-  (d) icons for sorting (only if enabled by the developer),

-  (e) icons for showing properties (only if enabled and configured by the developer),

-  links for cross navigation (only if enabled and configured by the developer)


   |image141|

   Figure 7.8: Pivot table features.

Side bar
~~~~~~~~

You can open the side bar by clicking on the icon positioned on the top right side of the page (Figure 7.9). Side bar will be shown on the right side (Figure 7.10).

   |image142|

   Figure 7.9: Open the side bar.

Side bar is used to:

-  choose between different data representations,

-  choose between different drill types,

-  call dialogs and functionalities that effect the pivot table,

-  get additional data based on loaded model.


   |image143|

   Figure 7.10: Side bar.

The side bar shows the **Menu**. This area let you customize the Olap layout. As highlighted in Figure 7.11, the Menu is divided in three subsections:

-  (a) drill options,

-  (b) OLAP functions,

-  (c) table functions, 

-  what if.


   |image144|

   Figure 7.11: Side bar Menu.

We start introducing the interface and leave the description to the next Section 7.2. In particular, referring to Figure 7.12, drill types consists of:

-  (a) position,

-  (b) member,

-  (c) replace,

-  (d) drill through.

   |image145|

   Figure 7.12: Drill types.

Meanwhile, referring to Figure 7.13, the OLAP functions consist of:

-  (a) reload model,

-  (b) show MDX,

-  (c) send MDX.


Referring to Figure 7.14, table functions consist of:

-  (a) show parent members,

-  (b) hide spans,

-  (c) show properties,

-  (d) suppress empty rows/columns,

-  (e) enable compact properties,

-  (f) enable sorting,

-  (g) sorting settings,

-  (h) calculated field wizard.


   |image146|

   Figure 7.13: OLAP functions.

   |image147|

   Figure 7.14: Table functions.


Referring to Figure 7.15, what if consists of:

-  (a) lock/unlock model,

-  (b) save,

-  (c) save as new version,

-  (d) undo, 

- (e) delete versions, 

- (f) output wizard.


   |image148|

   Figure 7.15: Table functions.


 Functionalities
-----------------

Placing hierarchies on axes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we already told, the user can easily move a dimension from the filter bar to the axis or viceversa dragging and dropping it to the desired place.

Let us suppose we want to move a dimension from the filter panel to the columns axis. The steps are summarized in Figure 7.16

Vice versa, to move back the dimension from the columns axis to the filter panel the user must simply drag and drop the dimension from one place to the other as in Figure 7.17.

   |image149|

   Figure 7.16: Move a hierarchy to the columns axis.

   |image150|

   Figure 7.17: Move a dimension from the columns axis to the filter panel.


Similarly, a dimension can be moved from the filter panel to the rows axis simply dragging and dropping it from one place to the other.

Swaping axes
~~~~~~~~~~~~

To swap axes the user should click on the icon |image151|. The user will get the outcome showed in Figure 7.18.

   |image152|

   Figure 7.18: Swap axes.

Selecting different hierarchies on dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an OLAP schema is defined, the user can choose different hierarchies of the same dimension. The icon for opening the dialog is positioned on the top left corner of the filter card (if the dimension has more than one hierarchy). Select the hierarchies icon underlined in Figure 7.19.

   |image153|

   Figure 7.19: Hierarchies icon.

A pop up will be displayed. Figure 7.20 shows its characteristics. The window will present:

-  (a) the dimension name,

-  (b) name of selected hierarchies,

-  (c) drop down list of available hierarchies,

-  (d) save button,

- (e) cancel button.

   |image154|

   Figure 7.20: Hierarchies dialog pop up.

After selecting the hierarchy and saving user’s choice, that hierarchy will be used by the pivot table.

If the user re-opens the dialog window, he/she sees the selected hieararchies and has the chance to change it if needed to, as shown in Figure 7.21.

We give an example of the output when the hierarchy “Time” is selected in Figure 7.22 and hierarchy “Time Weekly” in Figure 7.23.

Slicing
~~~~~~~

The slicing operation consists in the analysis of a subset of a multi-dimensional array corresponding to a single value for one or more members of the dimensions. In order to perform this operation you need to drag and drop the dimesion of interest in the axis panel.  Then clicking on the filter icon choose the new single focus and apply it. Once concluded these steps the cube will show only the selected level of the dimension, while the others have been sliced out.

Figure 7.24 shows the slicer option panel which consists of:

-  (a) a dimension name,

-  (b) a search input field,

-  (c) a search button,

-  (d) a show/hide siblings checkbox,

-  (e) a member tree,

-  (f) a selected member icon,


   |image155|

   Figure 7.21: Changing the hierarchies.

   |image156|

   Figure 7.22: Time hierachy: the table shows days in the month.

   |image157|

   Figure 7.23: Time Weekly hierachy: table shows weeks in the month.


-  (g) a highlighted member (result of searching), 

- (h) a save and a cancel buttons.

   |image158|

   Figure 7.24: Dialog for slicer choosing.

In particular, it is possible to search for a member in three ways:

1. by browsing the member tree (Figure 7.25);

2. by typing member’s name or it’s part in the input field and clicking on the search button. The research will be possible if the user    enters at least four letters. If the user wishes to include member’s siblings to the research, the checkbox (Figure 7.24, (d))          needs to be checked (Figure 7.26);

3. after the first research, if the user types some other member’s name before clicking on the search button, visible members whose        names contains a entered text will be highlighted (Figure 7.27).

Once the selection has been saved, the users choice will affect the pivot table and the filter cards slicer name will rearrange.

Filtering
~~~~~~~~~

To filter dimension members in a pivot table, the user should click on a button (see Figure 7.5) located on the right side of dimension’s filter card placed in the filter area.

   |image159|

   Figure 7.25: Browsing the member tree.

   |image160|

   Figure 7.26: Using the research box.

   |image161|

   Figure 7.27: Using the research box after a first investigation.

The procedure to search for a member using the filter dialog has no meaningful differences with the one described for the slicer chooser dialog. The pop up interface is the one showed in Figure 7.28. After selecting a member, the user should click on the save button. The pivot table will display the changements. Otherwise click on the cancel button to discard changes.

   |image162|

   Figure 7.28: Filter dialog.


Drill down and drill up
~~~~~~~~~~~~~~~~~~~~~~~

User can choose between drill types by clicking on one of the three buttons in the drill types section of the side bar (Figure 7.10). There are three drill types. In the following we give some details on them.

1. **Position**: this is the default drill type. Clicking on a drill down/drill up command will expand/collapse a pivot table with          child members of a member with that particular command. See Figure 7.30.

2. **Member**: if the user wants to perform drill operation not only on one member per time but on all members of the same name and        level at the same time it is needed to select member drill type. See Figure 7.31.

   |image163|

   Figure 7.29: Filter effects on pivot table.

   |image164|

   Figure 7.30: “Position” drill down.

   |image165|

   Figure 7.31: “Member” drill down.

3. **Replace**: This option lets the user replace the parent member with his child member during drill down operation. To drill up the      user should click on the arrow icon next to the dimension name on which to perform operation. See Figure 7.32.

   |image166|

   Figure 7.32: “Replace” drill down.

Drill through
~~~~~~~~~~~~~

To perform drill through operation the user needs first to select a cell, as in Figure 7.33, on which to perform operations. Then clicking on the button for a drill through in the side bar, a dialog will open with results (this pop up could take some time to    open).

   |image167|

   Figure 7.33: Drill thorugh option.

In particular, referring to Figure 7.34, drill though dialog consists of:

-  (a) a hierarchy menu,

-  (b) a table of values,

-  (c) a maximum rows drop down list,

-  (d) a pagination,

-  (e) a apply button,

-  (f) a export button,

-  (g) a cancel button.


   |image168|

   Figure 7.34: Drill thorugh window.

The user must therefore select a cell, open the side bar and select the drill through item from the panel. A pop up will show up: here the user can choose the level of detail with which data will be displayed. The steps to follow are:

1. to click on hierarchy in hierarchy menu,

2. to check the checkbox of the level,

3. to click on the “Apply” button (after checking the checkbox, remember to click outside of the level list and then select apply).

The user can also select the maximum rows to load by choosing one of the options in the drop down list (see Figure 7.34, (c)). Finally, loaded data can be exported in csv format by clicking on the “Export” button.

Refreshing model
~~~~~~~~~~~~~~~~

To refresh a loaded model the user needs to click on the “Refresh” button available in the side bar panel. This action will clear the cash, load pivot table and the rest of data again.


Showing MDX
~~~~~~~~~~~

To show current mdx query user should click on show mdx button in the side bar. Figure 7.35 shows an example.

   |image169|

   Figure 7.35: Showing MDX query example.


Sending MDX
~~~~~~~~~~~

If you want to execute an MDX query you need to:

-  click on send MDX button in the sidebar,

-  type a query in a text area of send MDX dialogs (Figure 7.36), 

-  click on the save button (Figure 7.36).


   |image170|

   Figure 7.36: Sending MDX query example.

Result of the MDX query “should” appear in pivot table as in Figure 7.37. In fact, the user is responsable for entering *valid* MDX query.

   |image171|

   Figure 7.37: Sending MDX query example.


Showing parent members
~~~~~~~~~~~~~~~~~~~~~~

If a user wants to see additional information about members shown in the pivot table (for example: member’s hierarchy, level or parent member) he should click on a show parent members button in the side bar panel. The result will be visible in the pivot table. An example is shown in Figure 7.38 and Figure 7.39.

   |image172|

   Figure 7.38: Pivot table without the parent members mode.

   |image173|

   Figure 7.39: Pivot table after the parent members selection.

Hiding/showing spans
~~~~~~~~~~~~~~~~~~~~

To hide or show spans the user should click on show/hide spans button in the side bar. The result will be visible in pivot table as in Figure 7.40.

   |image174|

   Figure 7.40: Hide/show spans.

Showing properties
~~~~~~~~~~~~~~~~~~

In OLAP schema the XML member properties, if configured, could be represented in two possible ways:

1. as part of pivot table where a property values are placed in rows and columns. To get these values, the user needs to click on show      properties button in the side bar. Results will be shown in the pivot table;


   |image175|

   Figure 7.41: Show properties.

2. in a pop up as compact properties. To enable compact properties user should click on enable compact properties button in the side bar. In this way in all the cells of members Suppressing empty colunms/rows which has property set, a table icon appears. This icon lets the property pop up opens. Figure 7.42 shows an example.

   |image176|

   Figure 7.42: Show properties summarized in a pop up.

Suppressing empty colunms/rows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To hide the empty rows and/or colums, if any, from pivot table the user can click on the “Suppress empty rows/colums” button in the side bar panel. An example is given in Figure 7.43.


   |image177|

   Figure 7.43: Suppressing empty colunms/rows.

   |image178|

   Figure 7.44: Member sorting.

Sorting
~~~~~~~

To enable member ordering the user must click on the “Enable sorting” button in the side bar panel. The command for sorting will appear next to the member’s name in the pivot table. In addition, the sorting command will show the members of “Measures” hieararchy or members that are crossjoined with them, as shown in Figure 7.44. 

To sort members the user needs to click on the sorting command |image179|, available next to each member of the pivot table. Note that the sorting criteria is ascending at first execution. If the user clicks on the sorting icon, criteria will change to descending and the result will be shown in pivot table.

To remove the sorting, the user just have to click on the icon again. To change sorting mode user should click on sorting settings button in the side bar. Referring to Figure 7.45, dialog sorting settings consists of:
   
   |image180|

   Figure 7.45: Sorting settings window.

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

   |image181|

   Figure 7.46: Calculated member.

1. select a member of the pivot table, as in Figure 7.46, which will be the parent of the calculated member,

2. click on the “calculated field” button in the side bar panel: a “Select function” dialog will appear. The latter consists of            (refer to Figure 7.47):

   -  (a) a name input field,

   -  (b) an aggregation functions tab,

   -  (c) an arithmetic functions tab,

   -  (d) a temporal functions tab,

   -  (e) a custom functions tab,

   -  (f) a recent functions tab,

   -  (g) an available functions list,

   -  (h) ok and cancel buttons.


   |image182|

   Figure 7.47: Select function dialog.

The function definition used to create calculated members are read from the formula.xml file, located at: ROOT/resources/yourTennant/Olap folder. Functions are divided by few different tabs. In particular,\ **Tab Recent** contains calculated members and calculated sets created by user and saved in cookies. If there are no sets/members stored in the cookies, that tab will be empty. **Tab Custom** is where to define custom functions. These functions can be used to make really complex operations that are not part of predefined MDX functions. There you can use combination of few functions together or use operators for complex mathematical  calculations. They are also defined in formulas xml. If a specific tab doesn’t contain any formula, it will not be displayed. The “Name” field is mandatory, indeed the creation of a function without a name is forbidden. In **Recent tab**, the “Name” field is hidden for  Figure 7.48 provides an example of edited formula in the formulas.xml file.

3. Select a function and enter a calculated member/set name and click on “Ok”. A dialog for arguments defintion will show up, as shown in Figure 7.49. This is made up of the following elements:

-  (a) selected function name,

-  (b) function description,

   |image183|

   Figure 7.48: Example of one formula inside of formulas xml.

-  (c) text input fields for argument expression,

-  (d) expected MDX expression return type,

-  (e) argument’s MDX expression description,

-  (f) open saved button, 

-  (g) select from table button,

-  (h) ok and cancel buttons.


   |image184|

   Figure 7.49: Argument defintion dialog.

   |image185|

   Figure 7.50: Selecting members.

   |image186|

   Figure 7.51: Expression of the selected members.

In particular, to input MDX expression argument, the user has three options, listed in the following.

1. Type it manually (for advance users).

2. Select members from the pivot table: to select a members that are going to be included in a set, the user should (see Figure 7.50):

   -  click on select from table button,

   -  click on members in a pivot table,

   -  click ok in dialog to finish selection.


The expression of selected members will be imported in text input fields for argument expression as Figure 7.51 shows.

   |image187|
   
   Figure 7.52: Saved sets dialog.

   |image188|

   Figure 7.53: Expression of the saved/calculated member/set.

3. Import expression from saved calculated members or sets. To import calculated member/set, the user should:


   • Click on open saved button. Then the dialog of saved calculated members/sets will appear (Figure 7.52) and it consists of:

     -  a list of saved calculated members and sets,

     -  a calculated member/set name,

     -  calculated member/set return type is shown by round icon.

   •  Click on calculated member/set. The expression of saved calculated member/set will be imported in text input fields for argument         expression, as highlighted in Figure 7.53.

   •  After filling all the arguments of function, clicking on OK button will:

      -  add calculated member in a pivot table,

      -  save calculated set and it will be available for creation of other calculated member and sets.


In tab “Recent”, opening the “Select function” dialog the user can find a list of saved calculated member and sets which can be edited or deleted. Editing is done by clicking on one of them. 

   |image189|

   Figure 7.54: Edit a calculated member.

Deleting is done by Delete button as shown in Figure 7.54.

  .. include:: olapThumbinals.rst
