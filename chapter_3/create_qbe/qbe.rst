How to build a QBE
##########

This detailed user guide is dedicated to the Qbe (Query By Example), a Free Inquiry instrument which empowers users with easy and free access to information via graphical interfaces.

Free Inquiry indicates the modus operandi of analysts and operational users that are usually seeking for business analysis that are not limited to pre-arranged lists of results. This method requires a medium level of complexity as an adequate knowledge of data management and a structured organization of work are required.

QbE is a tool that allows you to develop your free inquiry through an entirely graphical modality. Moreover, you can execute the query, check the results, export them and save the query for further use.

The material will be divided in two main sections. The first is dedicated to build queries in the Knowage Server environment, supposing the availability of a business model to analyse. In the second part, we will provide the user with the principal steps to build a proper business model through the Qbe designer, available in Knowage Meta.

My first Query By Example
--------------------------

**QbE** allows you to query (a subset of) a database through a high-level representation of the entities and relations. 
Qbe main features are:

-  rich end user GUI;
-  selection of attributes and setting of filters;
-  no knowledge of data structures;
-  semantic knowledge of data;
-  management of results free;
-  support of export capabilities;
-  repeatable execution of inquiries.

Building a QbE query does not require any technical knowledge, but data domain knowledge: technical aspects, such as creating filters, aggregation and ordering criteria, are managed by a user-friendly graphical interface.

Let’s suppose that an administrator has built a business model and, consequently, released it on Knowage Server. This allows the user to access the model, query the available entities and save the results as a dataset, for further usage in different Knowage documents, such as cockpits.

In the following we will discuss each step in detail, showing the basic and advanced functionalities of the **QbE Editor**.


Query design and execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To open the QbE editor, access the **Models** section, available in the end user **Workspace**. Then, simply click on the model icon to reach the QbE graphical interface.

In this paragraph we show how to build a simple query with the QbE editor.

.. figure:: media/qbeDesigner.png

    QbE editor.

The above figure shows the **Query designer**. In next sections we will explain in detail all the components related to the **Query Designer**, the **Datamart Schema** tab, the query editor and the hidden tab dedicated to the management of queries, subqueries and parameters catalogue.

Datamart Schema
^^^^^^^^^^^^^^^^

Starting from the left side:
	The upper Panel shows the searchable logical schema and the list of entities that can be queried to generate the query. Entities are represented in a tree structure, with user-defined names. Fields can be added to the query (right side) by clicking on them.
	The lower Panel shows the list of created subqueries in a tree structure where the children are the fields of a subquery

Types of entities are: *facts*, represented by a cube symbol.(i.e., the Sales entity), *dimensions*, represented by a four-arrows symbol (i.e., the Product entity), *geographical dimension*, represented by *earth* icon.

Each single entity contains a title, a list of attributes or measures and relationships with other entities. Relations are available clicking on the *i* icon of a single entity. In particular, by exploding the content of an entity (i.e. Sales), you may encounter the following elements:

- **measure**: refers to fields related to numeric data (e.g. UNIT SALES);
- **attribute**: refers to fields that can be associated to a category (e.g. PRODUCT ID);
- **relation**: refers to relationships or connections between two entities (e.g. relationship between the sales and the product dimension).

.. figure:: media/image300_bis.png

	Relations of an entity.

There are two available views: Smart and Advanced. When the QbE is opened, by default the user will see the Smart view. To add a field of a specific entity to the query,just click on it and no other user interaction will be necessary to display the results.

.. figure:: media/smart_8.1.png

	Smart view.

The user can display the Advanced view by switching off the Smart view option displayed on the top right corner. The user can continue adding fields to the query but without seeing result. A specific icon has to be clicked to run the query.

.. figure:: media/advanceView_8.1.png

	Advanced view

The structure of the panel containing the fields of the query as well as the functionalities, changes depending which view is displayed.
For example, to remove a field from the query editor, just click on the *X* icon available for each column in the Smart view or click on the  **delete** item of the three dots menu available inthe Advanced view.
In any case, the Smart view, shows a table structure where each column of the table corresponds to a field of the query and contains:

- a **gear** icon providing functionalities like *Show field, Rename Alias,Group*
- a **deleting** icon
- a **filter** icon

.. figure:: media/image212_8.1.png

    Smart view functionalities.

The Advanced view shows a set of rows where any row contains the **Entity name**, the **Field name**, the **Alias** plus some other functionalities:


- **Alias**: define aliases for fields
- **Aggregation**: define the aggregation function (e.g., **SUM**, **AVERAGE**, …) on non-grouped items;
- **Order**: define a sorting criteria: click on the arrow to select an ascending or descending criteria;
- **Group**: in case of aggregations, define the attribute that you want to group on (due to the SQL syntax, these attributes appear in the GROUP BY clause);
- **Show**: indicate whether a column shall be visible in the result or not (hidden attributes are used and returned by the generated query, but are not shown in the result table);
- **In use**: indicate whether a column shall be used in the select clause of the query or not
- **Filter**: to add a filter criteria;

.. figure:: media/image213_8.1.png

Advanced view functionalities.

It is possible to edit alias, clicking on gear icon (smart view) and on **Alias item**. In advanced view, alias can be changed clicking on cell of alias column.

.. figure:: media/aliasChange.png

	Change alias.

Pay attention to grouping options: if you want to define an aggregation function on a field (like, for instance, the **COUNT** of the sold items), you shall tick the Group checkbox for all the other fields added in the query editor, without an aggregation function defined, otherwise you will get an SQL exception. The possible grouping functions are shown in the following figure.

.. figure:: media/image214.png

    Aggregation functions.

When you drag attributes belonging to entities that are linked through a relationship path, the QbE automatically resolves relationships between attributes (implicit join).

Moreover, multiple relationships may occur among entities. A typical example concerns dates. Suppose you have two relationships between the **Order** fact table and the **Time** dimension table: the first links the order_date column of the first table to the *time_id* column of the latter, while the second relationship joins the *shipping_date* column to the *time_id column*.

In this case, when dragging fields from both the **Order** entity and the **Time** entity you may want to specify which relationship will join the two tables: for instance, you may want to know the total number of orders according to the ordering month, the shipping month or for both. In all these situations, you can set the relationship to be used by clicking the **Relationships wizard** button at the top right corner of the panel. A pop up window opens where you can define the path to be used. Please refer to Multiple relationships section for all details regarding the disambiguation of relationships.

The toolbar about query editor sub-section has a toolbar contains additional functionalities summarized in Table below.

.. table::  Select fields toolbar options
      :widths: auto

      +-----------------------------------+-----------------------------------+
      |    Button                         | Description                       |
      +===================================+===================================+
      |    **Join definitions**           | Displays relations between        |
      |                                   | query entities                    |
      +-----------------------------------+-----------------------------------+
      |    **SQL**                        | Shows SQL generated by the        |
      |                                   | graphical interface               |
      +-----------------------------------+-----------------------------------+
      |    **Discard Repetitions**        | Remove duplicated rows from       |
      |                                   | results, if any                   |
      +-----------------------------------+-----------------------------------+
      |    **P**                          | Add parameters                    |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+
      |    **Calculator**                 | Add calculated fields             |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+
      |    **Three gears**                | Open advanced filters panel       |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+
      |    **Eye**                        | Show/hide hidden fields           |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+
      |    **Smart View**                 | Switch between smart and          |
      |                                   | advanced view                     |
      +-----------------------------------+-----------------------------------+
      |    **Play**                       | Preview query                     |
      +-----------------------------------+-----------------------------------+
      |    **Three dots**                 | Option to choose between Deleting |
      |                                   | all fields from query and Export  |
      |                                   | query into csv/xls/xlsx           |
      +-----------------------------------+-----------------------------------+

Calculated fields management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also add calculated fields to a query. This functionality is only available in the Advanced view through the  item  **Calculated field** ot the three dots menu.

To build a calculated field, you shall define a:

- **Column Name**;
- **Type**: string, number or date;
- **Column Type**: measure or attribute;
- **Formula**: drag and drop the fields included on the left and build the formula using the available functions.

The image below shows the wizard.

.. figure:: media/calculatedField_8.1.png

    Calculated field wizard.


Filters
^^^^^^^^

The **Filters** panel allows you to define filter criteria (WHERE clause). Filters are structured as a table: here rows contain filters, while columns represent the elements of the filter. Filters panel can be opened in three ways:
- In smart view clicking on **Filter icon** on the field in entity
- In smart view clicking on **filter icon** on the already added field in the query
- In advanced view clicking on three dots and **Filters item**

Adding new filter is possible clicking on **+** icon.

Removing the filter is possible clicking on **eraser** icon.

.. figure:: media/addDeleteFilter.png

Filters are expressions of type:

                                      **Left operand + Operator + Right operand.**

Structure of Filters panel is:

-  the **Field, Condition, Target** columns allow you to define filters according to the syntax defined above.
-  the **Target type** column define the types of right operand: manual, value of the field, another entity, parameter, subquery;

With target type **manual** you should fill input **target** with value that you want to be right operand.

.. figure:: media/manualTarget.png

	Manual target type

With target type **value of the field** lookup function is activated to facilitate selection of values. You are able to choose values for right operand. If you are choosing two values, you should set condition to be **between**, **not between**, **in** or **not in**. If you are choosing more then two values, you should set condition to be **in** or **not in**.

.. figure:: media/lookupFunction.png

    Filter lookup for right operand selection.

With target type **another entity** you will get option to choose field from another entity for your right operand.

.. figure:: media/anotherEntity.png

About target type **subquery** and **parameter** there will be more words later.


.. important::
         **Enterprise Edition only**

         Filtering data with fields type of date/time/timestamp using calendar/time/calendar is available only for Enterprise Edition.

If you have SI license file, you will get the chance to filter your data with fields type of date/time/timestamp using calendar/time/calendar + time option. This depends of what is data type of you field, and this is coming form metamodel creation phase.
When creating your metamodel, you can set data type of to your field.

.. figure:: media/timeDataType.png

	Metamodel creation.

.. figure:: media/date.png

	Filters creation on date data type of the field.

.. figure:: media/time.png

	Filters creation on time data type of the field.

.. figure:: media/timestamp.png

	Metamodel creation, timestamp data type of the field.

Note that more complex combinations of filters can be defined using the advanced filter wizard, which you ca find selecting the **Three gears** icon.

In the following table the possible types of filters in the QbE are summarized. The use of subqueries in filters is explained later in *Advanced QbE functionalities* paragraph.

.. table:: Possible combinations of filters in the QbE.
      :widths: auto

      +-------------+-------------+-------------+-------------+-------------+
      | Filter type | Left        | Operator    | Right       | Example     |
      |             | operand     |             | operand     |             |
      +=============+=============+=============+=============+=============+
      |    Basic    | Entity.attr | Any         | value       | Prod.family |
      |             | ibute       |             |             | =           |
      |             |             |             |             |             |
      |             |             |             |             | 'Food'      |
      +-------------+-------------+-------------+-------------+-------------+
      |    Basic    | Entity.attr | Any         | Entity.attr | Sales.sales |
      |             | ibute       |             | ibute       | >           |
      |             |             |             |             | Sales.cost  |
      +-------------+-------------+-------------+-------------+-------------+
      |  Parametric | Entity.attr | Any         | [parameter] | Prod.family |
      |             | ibute       |             |             | =           |
      |             |             |             |             |             |
      |             |             |             |             | [p_family]  |
      +-------------+-------------+-------------+-------------+-------------+
      |    Dynamic  | Entity.attr | Any         | prompt      | Prod.family |
      |             | ibute       |             |             | = ?         |
      +-------------+-------------+-------------+-------------+-------------+
      |    Value    | Entity.attr | In          | subquery    | Sales.custo |
      |    list     | ibute       |             |             | mer         |
      |    from     |             | /not in     |             | in subquery |
      |    subquery |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      |    Single   | subquery    | < = >       | value       | Subquery >  |
      |    value    |             |             |             | 0           |
      |    from     |             |             |             |             |
      |    subquery |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+

When filtering a date attribute or a time attribute it is possible to apply a timespan to ease the insertion of values. Following the images below, we can see that the Timespan button appears when filterting, for instance, a date attribute. We recall that is it possible to configure a new timespan using the dedicated Knowage functionality we described in the administrator guide.

.. figure:: media/imageTS005.png

	Filtering date attribute: use a timespan.

After selecting one timespan, the user must clcik on apply to ask the server to insert the start and end values.

.. figure:: media/imageTS006.png

	Filtering date attribute: apply a timespan.

Finally click on the save button and data is filtered accordingly.


Query Preview
^^^^^^^^^^^^^^^

While you are in smart view you can see preview of you query.
While you are in advanced view, and you are satisfied with your query or if you want to check the results, you can see the returned data by clicking the **Play** button located in the top right corner of the panel. From there, you can go back to the **Designer** to modify the definition of the query.

.. figure:: media/preview.png

	Preview wizard.

In case you have started the QbE editor directly from a model (that is, you have clicked on a model icon in the **My Data** > **Models** section) from here you can also click the **Save** button located in the top right corner of the page to save your query as a new dataset, reachable later from the **My Data**> **Dataset** section. Please note that this operation saves the *definition* of your query and not the snapshot of the resulting data. This means that every time you re-execute the saved dataset, a query on the database is performed to recover the updated data.

We highlight that when the save button is selected, a pop up shows asking you to fill in the details, split in three tabs:

-  **Generic**, in this tab you set basic information for your dataset like its **Label**, **Name**, **Description** and **Scope**.
-  **Persistence**, you have the chance to persist your dataset, i.e., to write it on the default database. Making a dataset persistent may be useful in case dataset calculation takes a considerable amount of time. Instead of recalculating the dataset each time the    documents using it are executed, the dataset is calculated once and then retrieved from a table to improve performance. You can also decide to schedule the persistence operation: this means that the data stored will be update according to the frequency defined in the **scheduling** options.

Choose your scheduling option and save the dataset. Now the table where your data are stored will be persisted according to the settings provided.

-  **Metadata** It recaps the metadata associated to the fields involved in your query.

.. figure:: media/saveQbeDS.png

	Save qbe dataset.


Advanced QbE functionalities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section we focus on advanced features, which can be comfortably managed by more expert users.

Spatial fields usage
^^^^^^^^^^^^^^^^^^^^^^^

.. important::
         **Enterprise Edition only**

         Spatial dimension is available only for Enterprise Edition with LI licence.

The Qbe engine supports spatial queries through a set of operators (that return true or false) or a set of functions (these usually return a measure). This feature is although available only when the Location Intelligence (LI) license is possessed and when data are stored in Oracle 12c database. It also fundamental that the Business Model has to be tagged as geographical model. You can refer to Meta Web Section to have details on how to set the geographical option using Knowage Meta.

We suppose that we have a BM with geographical dimensions enabled (by a technical user). In this case the dimensions which has spatial fields are marked with the compass icon |earthIcon|. Once the spatial dimension is expanded the fields are listed. Here there is no tracking symbol to distinguish between geographical attributes and the “normal” one. Therefore it is very important that the user is previously informed of which fields has geometrical properties.

.. |earthIcon| image:: media/earthIcon.png
   :width: 30

.. figure:: media/image218.png

    QbE spatial dimensions.

After a first selection of fields, it is possible to add calculated fields. Click on the **Calculator** option available on the query editor area as shown by the blue arrow in figure below. Note that a wizard opens: you can use this editor to insert a new field obtained through a finite sequence of operation on the selected fields.The circles of the next figure underline that the fields on which you can operate are the one previously selected by a simple click on the field.

.. _calculfldwizardspt:
.. figure:: media/image219.png

    Calculated field wizard with spatial filters.

In addition note that the **Items** panel provides all the applicable functions sorted by categories:

-  aggregation functions,
-  string functions
-  time functions,
-  spatial functions,
-  sql functions,
-  custom function (if they are registered).

.. warning::
     **Take into account the Oracle function definition**

         It is important to refer to Oracle Documentation to know the arguments, in terms of type and number, of each function to                assure the right functioning and do not occur in errors while running the Qbe document.

The latter are available only in the presence of a geographical Business Model and *must* be properly applied to spatial attributes or measures. Figure below shows the list of the available spatial functions while next table helps you to use them properly, supplying the corresponding Oracle function name and a link to grab more specific information about usage, number of arguments, type and output.

.. figure:: media/image220.png

    Spatial function list.

.. _linkoraclesptfnct:
.. table:: Link to Oracle spatial functions.
         :widths: auto

         +-----------------------+-----------------------+
         |    Function Name      | Oracle Function       |
         +=======================+=======================+
         |    **distance**       | SDO_GEOM.SDO_DISTANCE |
         +-----------------------+-----------------------+
         |    **dimension**      | GET_DIMS              |
         +-----------------------+-----------------------+
         |    **centroid**       | SDO_GEOM.SDO_CENTROID |
         +-----------------------+-----------------------+
         |    **geometrytype**   | GET_GTYPE             |
         +-----------------------+-----------------------+
         |    **length_spa**     | SDO_GEOM.SDO_LENGTH   |
         +-----------------------+-----------------------+
         |    **relate**         | SDO_GEOM.RELATE       |
         +-----------------------+-----------------------+
         |    **intersection**   | SDO_GEOM.INTERSECTION |
         +-----------------------+-----------------------+



To apply one function click on the function name and the “Operands selection window” wizard opens. Figure below shows an example for the funtion “Distance”. Fill in all boxes since all fields are mandatory.

.. figure:: media/image221.png

    Operands selection window.

Finally you can use spatial function to add a calculated field, as shown below.

.. figure:: media/image222.png

    Example of added calculated field using a spatial function.

As well as calculated fields it is possible to filter on spatial fields using specific geometric operators. Once again we report in Figure below the available geometric operator (you can find them scrolling the panel to the bottom) and report the link to the Oracle web pages in the next table.

.. figure:: media/image223.png

    Spatial filters.

See the table below:

.. _linkoraclefltrfnct:
.. table:: Link to Oracle filter functions.
         :widths: auto

         +-----------------------+-----------------------+
         |    Function Name      | Oracle Function       |
         +=======================+=======================+
         |    **touches**        | SDO_TOUCH             |
         +-----------------------+-----------------------+
         |    **filter**         | SDO_FILTER            |
         +-----------------------+-----------------------+
         |    **contains**       | SDO_CONTAINS          |
         +-----------------------+-----------------------+
         |    **covered by**     | SDO_COVEREDBY         |
         +-----------------------+-----------------------+
         |    **inside**         | SDO_INSIDE            |
         +-----------------------+-----------------------+
         |    **covers**         | SDO_COVERS            |
         +-----------------------+-----------------------+
         |    **overlaps**       | SDO_OVERLAPS          |
         +-----------------------+-----------------------+
         |    **equals to**      | SDO_EQUAL             |
         +-----------------------+-----------------------+
         |    **intersects**     | SDO_ANYINTERACT       |
         +-----------------------+-----------------------+
         |    **nn**             | SDO_NN                |
         +-----------------------+-----------------------+



Time functions for creating calculated fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
         **Enterprise Edition only**

         Time functions are available only for Enterprise Edition with SI licence.

If you have SI licence, in the qbe calculated field wizard there are available time functions.

.. figure:: media/timeFunctions.png

    Time functions.

See the table below:

.. _timefunctions:
.. table:: Time functions.
    :widths: auto

    +-----------------------------------+-----------------------------------+
    |    Function                       | Description                       |
    +===================================+===================================+
    |    **CURRENT_DATE()**             | Returns current date              |
    +-----------------------------------+-----------------------------------+
    |    **CURRENT_TIME()**             | Returns current time              |
    +-----------------------------------+-----------------------------------+
    |    **Hour(date)**                 | Returns hour from date            |
    +-----------------------------------+-----------------------------------+
    |    **Second(date)**               | Returns hour from date            |
    +-----------------------------------+-----------------------------------+
    |    **Year(date)**                 | Returns year from date            |
    +-----------------------------------+-----------------------------------+
    |    **Month(date)**                | Returns month from date           |
    +-----------------------------------+-----------------------------------+
    |    **Day(date)**                  | Returns day from date             |
    +-----------------------------------+-----------------------------------+
    |    **get_quarter(date)**          | Returns quarter of year for date  |
    +-----------------------------------+-----------------------------------+
    |    **get_week(date)**             | Returns week of year for date     |
    +-----------------------------------+-----------------------------------+
    |    **get_day_of_the_week(date)**  | Returns day of week for date      |
    +-----------------------------------+-----------------------------------+
    |    **add_days(date, num)**        | Add some days to date             |
    +-----------------------------------+-----------------------------------+
    |    **add_hours(date,num)**        | Add some hours to date            |
    +-----------------------------------+-----------------------------------+
    |    **add_months(date,num)**       | Add some months to date           |
    +-----------------------------------+-----------------------------------+
    |    **add_years(date,num)**        | Add some years to date            |
    +-----------------------------------+-----------------------------------+
    |    **subtract_years(date,num)**   | Remove some years from date       |
    +-----------------------------------+-----------------------------------+
    |    **subtract_days(date,num)**    | Remove some days from date        |
    +-----------------------------------+-----------------------------------+
    |    **subtract_months(date,num)**  | Remove some months from date      |
    +-----------------------------------+-----------------------------------+
    |    **subtract_hours(date,num)**   | Remove some hours from date       |
    +-----------------------------------+-----------------------------------+
    |    **datediff_in_days(date)**     | Difference in days between dates  |
    +-----------------------------------+-----------------------------------+
    |    **datediff_in_hours(date)**    | Difference in hours between dates |
    +-----------------------------------+-----------------------------------+
    |    **datediff_in_minutes(date)**  | Difference in mins between dates  |
    +-----------------------------------+-----------------------------------+


.. figure:: media/currentDate.png

    Creating calculated field with function current_date().

.. figure:: media/currentTime.png

    Creating calculated field with function current_Time().

.. figure:: media/hour.png

    Creating calculated field with function hour(date).

.. figure:: media/second.png

    Creating calculated field with function second(date).

.. figure:: media/year.png

    Creating calculated field with function year(date).

.. figure:: media/month.png

    Creating calculated field with function month(date).

.. figure:: media/day.png

    Creating calculated field with function day(date).

In the picture below, you can see list of all created calculated fields:

.. figure:: media/advanceViewTime.png

    List of created calculated fields.

In the next picture you can see result of you query:

.. figure:: media/previewTime.png

    Result of the query.


Subqueries
++++++++++


The **QbE Engine** also supports the definition and usage of subqueries similarly to the SQL language. As a result, you can define a subquery and use it within a filter in association to the in/not in operator, as shown in Figure below. To create a new subquery, which can be used as a filter inside the main query, click on |addSubqueries| button, on the left part, in **Derived entities**  toolbar. In the main view you will see that you are able to add fields in subquery.

.. |addSubqueries| image:: media/addSubquery.png
   :width: 30

.. figure:: media/subqueries.png

	QbE subquery view.

You can easily return to main qiery clicking on **MAIN** button in the query editor toolbar.

To use the sub-query inside the main query, simply choose from target type **Subquery option**, from **Target** choose subquery that you want and set the type of condition (**IN** or **NOT IN**). Now the subquery is used to provide values within the filter, in a similar way to SQL subqueries.

.. figure:: media/image281.png

    QbE query: use of a subquery in a filter.


Parameters
++++++++++


The **QbE Engine** also supports the definition and usage of parameters that can be used to filter the data using qbe filter. To create a new parameter, which can be used as a filter inside the main query, click on |parameter| button, in the main query toolbar.

.. |parameter| image:: media/parameter.png
   :width: 30

.. figure:: media/paramWizard.png

	QBE parameter view.

To use the parameter inside the main query, simply choose from target type **Parameter option** and from **Target** choose parameter that you want. Now the parameter is used to provide values within the filter.

.. figure:: media/filterParam.png

	QbE query: use of a parameter in a filter.