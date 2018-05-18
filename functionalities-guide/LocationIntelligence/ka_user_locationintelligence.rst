 Analytical document execution
----------------------------------

Let’s have a look on the user interface of Knowage Location Intelligence
features.

In Figure 15.1 we provide an example of a BI analysis carried out thanks
to map. In our example, the colour intensity of each state shown
proportionally increases according to the value of the indicator
selected. States who have no record connected are not coloured at all.

   |image364|

   Figure 15.1: Example of GIS document. USA sales per store

Click on the arrow on the top right to open the Location Inteligence
options panel. Here you can choose the **Map Type**, the indicators to
be displayed on the map and you can enter filters.

   |image365|

   Figure 15.2: Arrow button (left) Location Inteligence options panel
   (right) .

Analytical document execution

The **Map Type** available are:

-  **Map Zone**: the different map zone are filled with different colour
      range according to the indicator values

-  **Map Point**: the indicator values are displayed by points with
      differs on the radius. A bigger radius means a higher indicator’s
      value.

-  **Map Chart**: thanks to this visualization type you can compare more
      than one indicators simultaneously. Choose which indicators
      compare among the available ones. You have to mark them in the
      **indicator** panel area to visualize them. The charts appears on
      the map displaying the selected indicators’ values.

These three typologies of data visualization on map are compared in
Figure 15.3.

   |image366|

   Figure 15.3: Map Zone (left) Map Point (center) and Map Chart
   (right).

Now you can add extra layers on the default one. Switch to the **layer**
tab of the Location Inteligence options panel.

Here click on **select form catalog**, choose the layers you want to
add. Mark them in the bottom part of the Location Intelligence area in
the Layer box and the selected layer are displayed. These steps are
shown in Figure 15.4. In our example we upload some waypoints, you can
see the results obtained in Figure 15.5.

   |image367|

   Figure 15.4: Steps for layer adding

Now let’s focus on **Configuration** tab of Location Inteligence panel
option. Here you can set some extra configurations. Let’s have a look
them for each data visualization typology.

For the **Map Zone** you can set:

Analytical document execution

   |image368|

   Figure 15.5: Map with two layers

-  **Method**: the available ones are quantiles or equal intervals. If
      you choose quantiles data are classified into a certain number of
      classes with an equal number of units in each classe. If you
      choose equal Intervals the value are divided in ranges for each
      classe, the classes are equal in size and their number can be set.
      The entire range of data values (max - min) is divided equally
      into however many classes have been chosen.

-  **N°of classes**: the number of intervals in which data are
      subdivided.

-  **Range colours**: You can choose the first and the last colour of
      the range. For both of them you can use a colour pixer by clicking
      on the coloured square. An example is provided in Figure 15.6.

   |image369|

   Figure 15.6: Map Zone extra configurations

For the **Map Point** you can set:

-  **Colour**: the colour of the circle.

-  **Min/Max value**: the minimum and the maximum circles radius.

For the **Map Chart** you can set the colour of each chart’s bar.

The last tab of the panel is dedicate to the template preview, it is
provided for advanced user who want to have an approach on generated
code.

Extra functionalities

We can conclude our overview on GIS document describing the buttons
located at the bottom right corner, you can see them underlined in
Figure 15.7. From the left to the right this bottons can be used for:
have a look at the legend, compute a measure of an area of the map and
do the .pdf export of the map.

   |image370|

   Figure 15.7: From the left to the right: Legend, Measure and Export
   bottom.

Extra functionalities
~~~~~~~~~~~~~~~~~~~~~

Let’s come back to Location Layer main tab ad focus on the **Select
Mode** area. If cross navigation has been set you find two options:
**identify** and **Cross navigation**.

Select **Cross Navigation**, the **Spatial Item** tab appears. In this
tab you can configure your selection. To make your selection hide CTRL
key and choose the area on the map with the mouse. If you choose
**near**, the features in the Km set are selected. If you choose
**intersect**, the features which borders intersect your designed area
If you choose **inside**, only the features completely inside your area
of selection are considered for the cross navigation.

When selection is made, a box appears. In this box you find cross
navigation information. The number of features selected and a botton to
perform the cross navigation with the active selection.


 Template building with GIS designer
----------------------------------------

GIS engine document templates can now be built using GIS designer.
Designer is available from administrator document detail page (for this
part refer to Section 15.8) and also for end users workspace. The
creation process and designer sections are described in the text below.

A GIS document can be created by a final user from workspace area of
Knowage Server. Follow My Workspace » Analysis and click on the “Plus”
icon available at the top right corner of the page and launch a new
**Geo-referenced analysis**.

   |image371|

   Figure 15.8: Start a new Geo-referenced analysis.

When the designer is opened there is option to choose dataset for
joining spatial data and business data. When the dataset is selected the
Dataset join columns and indicators sections will appear. By default
dataset is not chosen and there is interface to create map without
business data

   |image372|

   Figure 15.9: GIS document designer window.


Designer sections
----------------------

Layer section
~~~~~~~~~~~~~

Definition of the target layer is configurable in layer section. If the
dataset is selected one of the available layers is chosen from list of
layers catalogs. Button change layer (Figure 15.10) opens a pop up with
a list of all available layer catalogs (Figure 15.11). Selecting one
item from the list and clicking save the selected item will be chosen
for template.

   |image373|

   Figure 15.10: Target layer definition.

   |image374|

   Figure 15.11: List of available layer catalogs.

In case when there is no dataset multiple layers can be selected as in
Figure 15.12.

   |image375|

   Figure 15.12: Multiple selection of available layers.

Dataset join columns
~~~~~~~~~~~~~~~~~~~~

Dataset join columns section is for configuring joining spatial data and
business data. This section is only present when the dataset is selected
for the document. Designer data structure Indicators

for joining is represented by the pairs of dataset columns and
corresponding layer columns. Clicking on add join column that you can
see in Figure15.13 new empty pair appears. Dataset join column can be
selected from columns on selected dataset by choosing an option from
combo box. Layer join column should be added as a free text by editing
corresponding table column.

   |image376|

   Figure 15.13: Dataset join columns interface.

Indicators
~~~~~~~~~~

Measures definition is configurable by adding indicators. The interface
is shown in Figure 15.14 This section is only present when dataset is
chosen for the document. Indicators are represented by pairs of measure
field from selected dataset and corresponding label that will be used on
map. Clicking on add indicators creates empty pair. Measure filed should
be selected by picking one option from combo box that contains measure
fields from selected dataset. Label should be inserted as free text by
editing corresponding table column.

   |image377|

   Figure 15.14: Indicators interface.


Filters
~~~~~~~

Using the filtering dedicated area of Figure 15.16 you define which
dataset attributes can be used to filter the geometry. Each filter
element is defined by an array (e.g. name : "store_country", label
:"COUNTRY"). The first value (name : "store_country") is the name of the
attribute as it is displayed among the properties. The second one label:
"COUNTRY" is the label which will be displayed to the user. This section
is only present when dataset is chosen for the document. Clicking on add
filter creates empty pair. Label field should be selected by picking one
option from combobox that contains attribute fields from selected
dataset. Label should be inserted as free text by editing corresponding
table column.

Map menu configuration

   |image378|

   Figure 15.15: Filters interface.

Map menu configuration
~~~~~~~~~~~~~~~~~~~~~~

Through the **Map menu configuration** panel the user can desides to
enable or disable some available functions and features, like the
legend, the distance calculator and so on. See Figure 15.16 to have a
glimpse at the available items.

   |image379|

   Figure 15.16: map menu configuration.

Layer filters
~~~~~~~~~~~~~

Here, as you can see from Figure 15.17, you define which target layer
attributes can be used to filter the geometry. This section is only
present when a dataset has been selected. Add filters button opens pop
up where you can choose all available filters of the selected layers.
Figure 15.18 gives an example.

   |image380|

   Figure 15.17: Layer filters interface interface.

Edit map
~~~~~~~~

When all required fields are filled basic template can be saved. From
workspace user is first asked to enter name and description of new
created document as in Figure 15.19. When the template is saved
successfuly EDIT MAP button is enabled in the right part of the main
toolbar.

Edit map

   |image381|

   Figure 15.18: List of available filters.

Clicking the edit map button will open created map. An example is given
in Figure 15.20. In edit mode you are able to save all custom setting
made on map.

   |image382|

   Figure 15.19: interface for name and description of new geo document
   for end user.

   
   .. include:: locationIntelligenceThumbinals.rst