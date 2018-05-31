

KEY PERFORMANCE INDICATORS AND ALERTS
=====================================

KPI stands for Key Performance Indicator. It denotes a set of metrics,
usually derived from simple measures, which allow managers to take a
snapshot on key aspects of their business. The main characteristics of
KPIs follow:

-  summary indicators,

-  complex calculations,

-  thresholds supporting results evaluation,

-  reference target goals,

-  easy to use but requiring more specific skills to design it,

-  association with alarms,

-  not necessarily used for real-time analysis,

-  may refer to a specific time frame.

For these reasons, KPIs are always defined by expert analysts and then
used to analyze performances through synthetic views that select and
outline only meaningful information.

Knowage allows the configuration of a KPI document thanks to a specific
**KPI engine**. The critical value (or values) can be computed and
visualized through the functionalities available in the ’KPI model’
section of Knowage menu area (see Figure 7.1).

7.1 KPI development
-------------------

We introduce the KPI tool by splitting the topic in steps. We briefly
sum up here the arguments that we will cover in the following sections
in order to have a general overview of the KPI implemetation.

-  **Measure definition**: it is necessary to define first the measures
      and attributes, eventually with parameters, to compute the
      critical value of interest.

-  **KPI definition**: here you compute the requested value through a
      formula using the measures and attributes set in previuos step and
      configure thresholds.

-  **Target**: it is possible to monitor the value of one or more KPIs
      comparing it to an additional fixed value.

-  **Schedulation**: you can schedule the execution of one or more KPIs,
      eventually filtered by conditions.

-  **Document creation**: finally, you develop the KPI document.

Therefore, we go into further details.

**Measure definition.** The first step is to create a new measure or
rule. Select **Measure/Rule Definition** from the contextual menu of the
main page, as shown in Figure 7.1.

   |image122|

   Figure 7.1: Measure/Rule Definition menu item.

Click on the “Plus” icon to set a new measure/rule. A query editor page
is opened. Note that once the data source is selected, pressing
simultaneously the CRTL key and the space bar opens a contextual menu
containing the available datasource columns and the database keywords.
Refer to Figure 7.2 to have an example.

Each rule is based on a query to which you can add placeholders. A
placeholder represents a filter that you can add to your rule and that
can be useful for profiling tasks. It is possible to assign value to a
placeholder while configuring the schedulation of the KPI (this
procedure will be further examined in “Document creation” paragraph).
The syntax to use in queries for setting a placeholder is
columnName=@placeholderName, as the example in Figure 7.3 shows.

Generally the rule such a query can return one or more measures and
possibly an attribute. An example is given in Figure 7.4.

A typology (measure, attribute and temporal attribute) and a category
can be assigned to each fields returned by the query using the
**Metadata** tab as highlighted in Figure 7.5. The typology

   |image123|

   Figure 7.2: Editing the query when defining a KPI.

   |image124|

   Figure 7.3: Setting placeholder in query definition.

   |image125|

   Figure 7.4: Query definition.

is required to associate a type to each field returned by the query. In
particular, if the field is a temporal one, it is mandatory to specify
to which level you want it to be considered, that is if it corresponds
to a day, a month, a year, a century or a millennium. For measures and
attribute it is possible to assign also a category to easily look them
up in a second moment.

   |image126|

   Figure 7.5: Metadata settings.

We say in advance that, it is important to distinguish these metedata
categories from the required field “Category” that occurs while saving
the KPI definition (see Figure 7.18). In fact, the category assigned
when saving the KPI definition will be added (if it doesn’t exist) in
the “KPI categories“ list, used to profile KPIs on roles (see Figure
7.6).

   |image127|

   Figure 7.6: KPI category.

As we told, a proper categorization exists for the aggregations of type
temporal. In fact, when associating “temporal attribute” as metadata
typology, the technical user must indicate the hierarchy level of the
data: day, month or year. You can see an example in Figure 7.7. Note
that the field set as temporal type must contains numbers (therefore
string types are not allowed). For example, if one wants to set a field
as “month”, such a field must contain {01,02,03,...,12} that will be
considered as {January, February, March,...,December}.

   |image128|

   Figure 7.7: Hierarchy level for temporal attributes.

The **Preview** tab allows you to check the query execution and have a
look on a part of the result set.

Let’s now examine extra features available on the right top corner.
There you can find the following tab:

-  **Alias**: as in Figure 7.8, you can see the aliases defined in other
      rules; note that only the aliases of those colums saved as
      attribute are stored and showed. This is useful in order to avoid
      aliases already in use when defining a new rule. Indeed an alias
      can not be saved twice even if contained in different rules.


   |image129|

   Figure 7.8: Checking aliases.

-  **Placeholder**: here you can check the existing placeholders. These
      are set in the query you’re editing or in other ones. Figure 7.9
      gives an example.


   |image130|

   Figure 7.9: Setting placeholders in a query.

-  **Save**: to save the query and other settings just configured.

-  **Close**: to exit the rule configuration window.

**KPI definition.** Select the **KPI definition** item from the
contextual menu of the main page of Knowage, as shown in Figure 7.10.
Click on the “Plus” icon to configure a new KPI.

   |image131|

   Figure 7.10: Configure a new KPI.

The window opens a first tag, entitled **Formula** (see Figure 7.11),
where you must type the formula to enable calculations.

Press CTRL key and space bar simultaneously to access all measures
defined in the rules, as shown in Figure 7.12. Once a measure is
selected, you need to choose which function must act on it. This can be
done by clicking on the *f*\ () that surrounds the chosen measure. See
Figure 7.13.

Clicking on the *f*\ () the interface opens a pop up where you can
select which function apply to the measure, see Figure 7.14. Once the
selection is made the formula will be autofilled with the proper sintax
and you can go on editing it.

   |image132|

   Figure 7.11: Formula definition tab.

   |image133|

   Figure 7.12: Press crtl and space to get measures.

   |image134|

   Figure 7.13: Formula syntax.

   |image135|

   Figure 7.14: Available functions.

Once a complete formula (an example is given in Figure 7.15) has been
inserted you can move to the next tab.

   |image136|

   Figure 7.15: Complete formula example.

The **Cardinality** tab allows you to define the granularity level
(namely the grouping level) for the attributes of the defined measures.

Referring to the example in Figure 7.16, selecting (with a check) both
measures for the attribute product_name, the KPI measures are computed,
grouped on each product_name; otherwise no grouping will be done.

Limit values can be set using the Threshold tab (Figure 7.17). It is
mandatory to set at least one threshold otherwise the KPI cannot be
saved. You can choose a threshold already defined clicking on
“Threshold” list or create a new one.

To insert a new threshold it is mandatory to insert a name and assign a
type, while the description is optional. Clicking on **Add new
threshold** item a new item appears. It is necessary to define the
**Position**, **Label**, **Minimum** and **Maximum** values. It is
possible to choose if to include the minimum and maximum values in the
value slot. The **Severity** is used to link colors to their meaning and
make the thresholds readable by other technical users. Note that the
color can be defined through the RGB code, the hexadecimal code or
choosing it from the panel.

Remember to save once all thresholds have been set.

   |image137|

   Figure 7.16: Cardinality settings example.

   |image138|

   Figure 7.17: Setting thresholds.

   |image139|

Finally the user must save the KPI definition clicking on the “Save”
button, available at the right top corner of the page. Once the user
clicks on the “Save” button, the “Add KPI associations” wizard opens, as
you can see from Figure 7.18. Here, it is mandatory to assign a name to
the KPI. In addition, the user can set the KPI category so that only
users whose roles have the permmissions to this specific category can
access the KPI. Remember that it is possible to assign permissions over
KPI when defining roles using the “Roles management” functionality
available on Knowage main page. Furthermore, the user can check or
uncheck the “\ **Enable Versioning**\ ” button if he/she wishes to keep
track of the rules/measures/targets that generate the KPI response at
each KPI execution.

   |image140|

   Figure 7.18: Save the KPI definition and set category.

**Target.** This step is not mandatory. Enter the **Target Definition**
menu item as shown in

Figure 7.19.

   |image141|

   Figure 7.19: Target Definition menu item.

Clicking on the “Plus” icon you can add a new target (Figure 7.20).

   |image142|

   Figure 7.20: Add a new target.

The definition of a new target requires to type a name, a validity start
date/end date and the association to at least one target. It is
possibile to associate a target clicking on the item **Add KPI** and
selecting the KPI of interest. Once the association is set, the “Value”
box gets editable and you can insert the value you wish to send to the
selected KPI. An example is given in Figure 7.21. In the KPI
visualization phase, a red bold thick will be displayed on the indicated
value (see Figure 7.22).

   |image143|

   Figure 7.21: KPI target association.

   |image144|

   Figure 7.22: Target mark in KPI scale of values.

Note that once targets are set, the window in Figure 7.20 gets populated
with a list. Note that here the category serves as description and only
to order the records.

**Schedulation.** Once the KPI has been defined, it is necessary to
schedule them to proceed with the creation of an analytical document.
For this purpose, click on the **KPI Scheduler** from the contextual
menu that you can see in Figure 7.23.

   |image145|

   Figure 7.23: KPI Scheduler menu item.

As for the other interfaces it is enough to click on the “Plus” icon to
create a new schedulation. The new schedulation window presents several
tabs.

-  **KPI**: it is possible to associate one or more KPI to the
      schedulation clicking on “Add KPI Association”.

-  **Filters**: here you assign values to the filters (if configured)
      associated to the schedu-

   |image146|

   Figure 7.24: KPI tab window.

   lation. Note that it is possibile to assign values to the filters by
   means of a LOV, a fixed list of values or a temporal function. In
   case the LOV option is chosen, remember that the LOV must return one
   unique value. This choice can be useful for profiling tasks.

   |image147|

   Figure 7.25: Filters options.

-  **Frequency**: referring to Figure 7.26, here is the place where the
      schedulation time interval (start and end date) can be set
      together with its frequency.


   |image148|

   Figure 7.26: Frequency tab window.

-  **Execute**: here you can select the execution type. The available
      options distinguish between the storing and the removal of old
      logged data. In fact, selecting **Insert and update** the
      scheduler compute the current (accordingly to the frequency
      choice) KPI values and store them in proper tables without
      deleting the old measurements and all error log text files are
      available right beneath. While selecting **Delete and insert** the

 Creation of a KPI document

   previous data are deleted.

   |image149|

   Figure 7.27: Execute tab window.

In Figure 7.28 we sum up the example case we have referred to since now.

   |image150|

   Figure 7.28: Overview of the KPI case.

Once the schedulation is completed click on the “Save” button. Remember
to give a name to the schedulation as in Figure 7.29.

 Creation of a KPI document
------------------------------

**Document creation.** Now the schedulation has been set and it is
possible to visualize the results. We need at this point to create a new
analytical document of type KPI and that uses the KPI engine (Figure
7.30). Then we save.

   |image151|

   Figure 7.29: Overview of the KPI case.

   |image152|

   Figure 7.30: Overview of the KPI case.

Click on the **Template build** icon to develop the template. Here you
can choose between KPI and Scorecard (refer to Chapter 8.2 for details
on the Scorecard option). In the KPI case it is possible to choose
between the two following type of document, as you can see in Figure

7.35.

-  **List**: with this option it is possible to add several KPI that
      will be shown in the same page with a default visualization shown
      in Figure 7.39.

-  **Widget**: with this option it is always possible to add several KPI
      that will be shown in the same page but in this case you will also
      be asked to select its visualization: Speedometer (Figure 7.37) or
      KPI Card (Figure 7.36); then the minimum value and the maximum
      value that the KPI can assume and if you want to add a prefix or a
      suffix (for example the unit of measure of the value) to the
      showed value.

Then practically you must add the KPI association using the KPI List
area of the interface. As you can see from Figure 7.31 here you select
the KPI after clicking on the “ADD KPI ASSOCIATION” link. The latter
opens a wizard that allows to pick up a multiple choice of the KPIs.
Once chosen, you need to specify all empty fields of the form, like
“Category”, “View as” and so on (refer to Figure 7.31). Note that the
“View as” field is were you can decide if the widget will be a
Speedometer or a KPI Card.

Moreover, you can set the other properties of the KPI document using the
**Options** and the **Style** areas (Figure 7.32).

   |image153|

   Figure 7.31: Setting the KPI associations using the dedicated area.

   |image154|

   Figure 7.32: Areas of the Template Build for KPI.

In particular, it is possible to steer the time granularity used by the
KPI engine to improve the performances. For this purpose, in the
“Options” area (Figure 7.33) the user is invited to indicate the level
of aggregation choosing among “day”, “week”, “month”, “quarter”, “year”.

   |image155|

   Figure 7.33: Choose the time granularity.

Finally in the “Style” area the user can customize the size of the
widget, the font, the color and size of texts.

   |image156|

   Figure 7.34: Style settings.

   |image157|

   Figure 7.35: KPI association.

Then save and run the document. Examples are shown in Figure 7.37,
Figure 7.38 and Figure

7.39.

In case the document contains grouping functions upon them, it is necessary to add the proper analytical drivers. Refer to Section 5.4 to get more information about how to associate an analytical driver to a document (and therefore to a KPI document). We stress that the URL of the analytical driver *must* coincide with the *attribute aliases* on which you have defined the grouping.

.. include:: kpiThumbinals.rst
