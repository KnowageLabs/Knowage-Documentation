In this chapter we will deal with some technical fetaures of the What-If analysis that can be handled only by expert users.

Workflow description\*
----------------------

When you perform a what-if analysis the schema is shared in order to be used as a data source. Therefore each time a document linked to a schema can be edited only by one user per time. This behaviour is managed by the Workflow of the schema. The administrator can configure a workflow opening the details of the model in OLAP schema catalogue, selecting the schema and going on the workflow tab available on the top of the right sided area. The tab is red circled in Figure 10.1.

   |image214|

       Figure 10.1: Workflow tab.

Referring to Figure 10.2, the interface for the definition of the workflow is composed of a double list where

-  the **available users** area contains all the users,

-  the **workflow** area contains the sequence of users for the workflow.

   |image215|

       Figure 10.2: Workflow tab interface.

When an administrator clicks on the user in the list “available users” the user will be added in the workflow as shown in Figure 10.3.

Administrator can move the users in the sequence or remove them clicking on the “action buttons”. When the workflow is defined, the administrator can start it clicking on the button start. To start a workflow means to enable the first user of the sequence to apply the what-if on that schema. When a workflow is started it can not be edited by anyone else and an icon appears in the row of actual active user so that the administrators can monitor the state of the schema. An example is provided by Figure 10.4

Schema definition\*
------------------------

As we foresaid, the What-If analysis requires some modification on the database. The first step is to create a new table in the database to store the named version of the modified data. The user will then change the values of the cube; it is then mandatory to create a new table with a structure similar to the analysed cube and a new table (wbversion) that will contain the versioning of the definitions set in the analysis. 

Therefore the structure of the new fact table should contain:

-  all the foreign keys to the dimensions (all the ones visible in the cube),

   |image216|

        Figure 10.3: Selecting users for workflows.

   |image217|

        Figure 10.4: Selecting users for workflows. 

-  all the editable measures,

-  a new numeric column that is a foreign key referencing the version table.


In Figure 10.5 there is an example where the cube is sales_fact_1998 and the new table is sales_fact_1998_virtual.

|image218|

    Figure 10.5: Cube and new virtual table example.

The sales_fact_1998_virtual table should be initialized with the same data contained in sales_fact_1998 plus 0 as version; the wbversion table should be initialized with one record with wbversion = 0 and a name plus a description for the “original values”.

Changes in the mondrian schema\*
-------------------------------------

Now you should map the new tables in the mondrian schema. In order to merge the fact table and the table with the editable measure we create a virtual cube. A virtual cube is a special cube where the values are the result of the join of other cubes. In our case the join keys are the dimensions. The actions to be performed in the mondrian schema are listed right below.

-  To create a new "Version" dimension as inChanging the Mondrian Schema.

+-----------------------------------------------------------------------+
| <Dimension name="Version">                                            |
|                                                                       |
|    <Hierarchy hasAll="false" primaryKey="wbversion"                   |
|    defaultMember="[Version ].[0]" >                                   |
|                                                                       |
|    <Table name="wbversion"/>                                          |
|                                                                       |
|    <Level name="Version" column="wbversion" uniqueMembers="true"      |
|    captionColumn="version_name"/>                                     |
|                                                                       |
|    </Hierarchy>                                                       |
|                                                                       |
| </Dimension>                                                          |
+-----------------------------------------------------------------------+

   Code 10.1: Changing the Mondrian Schema.

-  To create the mapping of the editable cube (in our example the table sales_fact_1998_virtual) as shown in Code Creating the mapping of the editable cube.

+--------------------------------------------------------------------------+
| <Cube name="Sales_Edit">                                                 |
|                                                                          |
|    <Table name="sales_fact_1998_virtual"/>                               |
|                                                                          |
|    <DimensionUsage name="Product" source="Product"                       |
|    foreignKey="product_id" />                                            |
|                                                                          |
|    <DimensionUsage name="Region" source="Region"                         |
|    foreignKey="store_id"/>                                               |
|                                                                          |
|    <DimensionUsage name="Customers" source="Customers" foreignKey="      |
|    customer_id"/>                                                        |
|                                                                          |
|    <DimensionUsage name="Version" source="Version"                       |
|    foreignKey="wbversion"/>                                              |
|                                                                          |
|    <Measure name="Store Sales" column="store_sales" aggregator="sum"     |
|    formatString="#,###.00"/>                                             |
|                                                                          |
| </Cube>                                                                  |
+--------------------------------------------------------------------------+

   Code 10.2: Creating the mapping of the editable cube.

The name of the cube ("Sales_Edit") is the value of the edit Cube attribute of the tag scenario in the template. Note that the name of the dimension Version must be exactly "Version"!!

• To create the virtual cube that will contain the mapping of the columns as in Code 10.3.

+-----------------------------------------------------------------------+
| <VirtualCube name="Sales_V">                                          |
|                                                                       |
|    <CubeUsages>                                                       |
|                                                                       |
|    <CubeUsage cubeName="Sales_Edit"                                   |
|    ignoreUnrelatedDimensions="true"/>                                 |
|                                                                       |
|    <CubeUsage cubeName="Sales" ignoreUnrelatedDimensions="true"/>     |
|                                                                       |
|    </CubeUsages>                                                      |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales" name="Customers"/>          |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales" name="Product"/>            |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales" name="Region"/>             |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales_Edit" name="Customers"/>     |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales_Edit" name="Product"/>       |
|    <VirtualCubeDimension cubeName="Sales_Edit" name="Region"/>        |
|                                                                       |
|    <VirtualCubeDimension cubeName="Sales_Edit" name="Version"/>       |
|                                                                       |
|    <VirtualCubeMeasure cubeName="Sales" name="[Measures].[Unit Sales  |
|    Original]" visible="false"/>                                       |
|                                                                       |
|    <VirtualCubeMeasure cubeName="Sales" name="[Measures].[Sales Count |
|    Original]" visible="false"/>                                       |
|                                                                       |
|    <VirtualCubeMeasure cubeName="Sales_Edit" name="[Measures].[Store  |
|    Sales]" visible="true"/>                                           |
|                                                                       |
|    <VirtualCubeMeasure cubeName="Sales_Edit" name="[Measures].[Store  |
|    Cost]" visible="true"/>                                            |
|                                                                       |
|    <CalculatedMember name="Sales Count" dimension="Measures">         |
|                                                                       |
| <Formula>VALIDMEASURE([Measures].[Sales Count Original])</Formula>    |
|                                                                       |
|    </CalculatedMember>                                                |
|                                                                       |
|    <CalculatedMember name="Unit Sales" dimension="Measures">          |
|                                                                       |
| <Formula>VALIDMEASURE([Measures].[Unit Sales Original])</Formula>     |
|                                                                       |
|    </CalculatedMember>                                                |
|                                                                       |
| </VirtualCube>                                                        |
+-----------------------------------------------------------------------+


    Code 10.3: Creating the virtual cube

Specifically, in the virtual cube you should specify:

1. the list of cubes to be joined (CubeUsages);

2. the list of the dimensions of the cube (as you can see it contains all the common dimensions, plus the Version that belongs only to the editable cube);

3. The list of the measures. You can perceive that there is a calculated member for the measure Sales Count Original (Sales Count Original is the name of a measure in the Sales cube). This is a trick for the not editable measures. This type of measure lives only in the DWH cube and not in the editable cube. This is due to the fact that the engine doesnt know how to give a value for these measures for the different values of the Version dimension (remember that only the editable cube has the Version dimension). The calculated field solve this problem propagating the same version of the not editable (and versionable) measure for all the version.

Now all the MDX queries can be performed in the virtual cube.
   
    .. include:: whatIfThumbinals.rst
