
 Smart Filter creation\*
----------------------------

The steps to create a smart filter document follow:

-  create the analytical document on the server;

-  create the QbE base query; • add filters and grouping variables;

-  save the document.

The second and the third step. To start, select **Document Developer**
from the left sidebar and click on **Create Document**> **Generic
Document**. In the document detail page, insert label, name and
description. Then, select **Free Inqury - Smart Filter** document as
Type and **Smart Filter Engine** as Engine. Insert all other mandatory
fields and save. A wizard icon shows up at the bottom of the page,
together with the **Template build** label. Open the wizard clicking on
the small icon as shown in Figure 11.3. The template build wizard will
guide you along all necessary steps.

   |image321|

   Figure 11.3: Smart filter - Document detail.

 Query creation
---------------------

The first step is the definition of a QbE query. Therefore, the first
information required by the template wizard is the QbE document over
which the query will be built, as shown in 11.4.

Query creation\*

Alternatively, you can choose to built your query over a *flat* dataset.

   |image322|

   Figure 11.4: Choose the QbE document or flat dataset for the QbE
   query.

Select **Edit**, and then click on **Start** the Designer to create your
template.

The query editor is the same as the one available in the **QbE Engine**,
where the power user can easily create queries without dealing with SQL
code.

   Building QbE queries

   |image323|\ The **QbE Engine** allows the creation of complex queries
   via an intuitive interface for end users. The same interface is used
   to create a smart filter document. Please refer to section My first
   Query By Example in this chapter for more details on query building.

Once you have defined the query, it is a good practice to execute it to
check that the results are correctly displayed. If everything is
correct, move to the **Form designer** tab.

As shown in Figure 11.5, the form editor consists of two parts. On the
right, the base structure of a form is shown.

   |image324|

   Figure 11.5: Smart Filter form editor.

As the user defines new filters (open, closed, dynamic filters) and
grouping variables, they are added to the corresponding section of the
form. The left panel is used to visualize query fields that are used in
filters. This section is initially empty: click on **Refresh** query
fields to view

 Filters

all the fields of the query that you have just defined. If you modify
the query, remember to refresh the fields in this panel.

   |image325|

To have a preview of the form, click on the **Preview** tab located at
the right corner of the editor. When you are happy with the result,
click on **Save template** to save the form as a new template for the
smart filter document.


 Filters
--------------

Designing the form basically involves the definition of filters. There
are three types of filters in a smart filter document. They are grouped
in the following categories (from top to bottom in the graphical
interface):

Static closed filters: filtering criteria based on complex conditions.
They can be single or multivalue.

Static open filters: filtering criteria based on the selection of one or
more values within a pre-defined list. They can be single or multivalue.

Dynamic filters: filtering criteria allowing the user to build his own
filtering conditions (as: operator, expression, value).

Furthermore, you can also define optional Grouping variables,
corrisponding to grouping criteria of data obtained from the initial
result set. If you define them, the **Show Data** window will be divided
in two sections (master/detail) as shown in Figure 11.2, otherwise only
the detail section will be displayed.

In the following we discuss each type of filter in detail showing how to
define them in a smart filter template.

Static closed filters
~~~~~~~~~~~~~~~~~~~~~

Static closed filters are defined as a group. Therefore, the first step
to create a static closed filter is the configuration of the properties
related to the management of the filter group. To add a static closed
filter, click on the plus button located at the right top corner of the
corresponding section. Here the properties described in Table 11.1 must
be set.

Once these options are configured, click on **Add** and a configuration
window, as the one in Figure 11.7,will open, enabling to add filters to
the group that you have just created. Give a Static closed filters

   |image326|

   Figure 11.6: Static closed filters configuration editor.

+-----------------------------------+-----------------------------------+
|    Name                           | Name of the filter group          |
+===================================+===================================+
|    **Single selection**           | If **YES**, the user is enabled   |
|                                   | to select only one filter within  |
|                                   | the filter group. Otherwise,      |
|                                   | multiple selections are allowed.  |
+-----------------------------------+-----------------------------------+
|    **Allow “No selection”**       | If **YES**, an option to select   |
|                                   | all values is added.              |
+-----------------------------------+-----------------------------------+
|    **No selection option’s        | Can be assigned a value only if   |
|    label**                        | the **Allow No selection** is set |
|                                   | to **YES**.                       |
+-----------------------------------+-----------------------------------+
|    **Boolean connector**          | Defines the logical connector     |
|                                   | between filters in the group. Can |
|                                   | be set only if **Single           |
|                                   | selection** is set to **NO**.     |
+-----------------------------------+-----------------------------------+


   Table 11.1: Static closed filters configuration options.

Static open filters

   |image327|

   Figure 11.7: Static closed filters definition.

name, select a field, the operand and a value (see Figure 11.8. The
**Name** attribute defines the name that is shown to the user beside the
filter. The attributes Field,Operator and Value define the filter as a
condition of the form: [field] [operator] [value], where **Field** is a
column of the underlying query and can be selected using the lookup.
Multiple conditions can be combined using the **Boolean Connector**
field. This selection is reflected in the bottom box: this will be
automatically filled in at each selection. Once you have set all
properties, you can actually create the filter group clicking on
**Apply**. To edit the group again, click on **Edit**: this reopens the
editor window.

   |image328|

   Figure 11.8: Static closed filters editor.

Static open filters
~~~~~~~~~~~~~~~~~~~

Static open filters allow the user to select values that are not
pre-determined but retrieved at runtime via a query on the database. For
this reason they are called open. They are still static because the
column that is filtered is determined at filter definition time.
Differently from closed filters, static open filters are not grouped.

Dynamic filters

To create a new static open filter, drag the field that you wish to
filter from the left panel onto the editor area that corresponds to
static open filters. As shown in 11.9, an editor window opens as soon as
the field is dropped onto the editor area.

   |image329|

   Figure 11.9: Static open filters editor.

The open filter is similar to the closed one, except that the **Field**
cannot be modified (because it was dragged before). Furthermore, the
**Value** is not editable since values are retrieved from a query on the
database at runtime. There are two options for the query:

Standard query: in this case all distinct values for the given field are
retrieved. It is possible to choose how to order results, and if values
should be retrieved from the entity to which the field belongs, or its
associated first level entity.

Custom query: with this option it is possible to choose a query defined
via QbE to retrieve admissible values. This means that the level of
control on admissible values is enforced, including the use of the
behavioural model to show different values to different users.

Dynamic filters
~~~~~~~~~~~~~~~

Dynamic filters, like closed ones, require the static definition of the
fields that shall be filtered. Nevertheless the user can freely choose
the value attribute to which the field shall be compared. They generally
replace static closed filters whenever the field domain is a continuum,
which makes the definition of discrete values scarcely meaningful. The
comparison operator is statically defined for a group of filters.

Different groups have in general different operators. Hence, dynamic
filters, like static closed ones, are defined in groups. Therefore,
before creating a filter, you should create a group clicking on the plus
button at the top right corner of the dynamic filter area, as
highlighted in Figure 11.10.

Grouping variables

   |image330|

   Figure 11.10: Add dynamic filter group.

When creating the group, select both the name and the characterizing
operator. Then you can simply drag fields from the left panel onto the
filter group area: this creates a new dynamic filter in that group.

   |image331|

   Figure 11.11: Create a group of dynamic filters.

Grouping variables
~~~~~~~~~~~~~~~~~~

Beside filtering the results of the base query, as seen before, the
smart filter allows grouping on two levels. For each level, you can add
fields from the base query. When executing the document you will be
shown the different options for first and second level grouping.

To add a field on a level, drag it from the left panel onto the
corresponding editor area. Now save it by clicking on **Save Template**.
For a preview, just click on the **Preview** tab.

Grouping variables

   |image332|

   Figure 11.12: Grouping variables definition.
   
      .. include:: smartFilterThumbinals.rst