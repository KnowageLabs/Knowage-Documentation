 
Creation of an OLAP document\*
------------------------------

Multidimensional analysis allows the hierarchical inquiry of numerical measures over predefined dimensions. In Cockpit we explained how the user can monitor data on different detail levels and from different perspectives. Here we want to go into details of how a technical user can create an OLAP document. We recall that the main characteristics of OLAP documents are:

-  the need for a specific data structure (logical or physical);

-  analysis based on dimensions, hierarchies and measures;

-  interactive analysis;

-  freedom to re-orient analysis;

-  different levels of data analysis, through synthetic and detailed views;

-  drill-down, slice and dice, drill-through operations.


Considering these items, we will describe the steps to develop an OLAP document.

About the engine
-----------------

Knowage performs OLAP documents by relying on the **OLAP engine**. This engine integrates Mondrian OLAP server and two different cube navigation clients to provide multi-dimensional analysis. In general, Mondrian is a Relational Online Analytical Processing (ROLAP) tool that provides the back-end support for the engine. OLAP structures, such as cubes, dimensions and attributes, are mapped directly onto tables and columns of the data warehouse. This way, Mondrian builds an OLAP cube in cache that can be accessed by client applications. The Knowage OLAP engine provides the front-end tool to interact with Mondrian servers and shows the results via the typical OLAP functionalities, like drill down, slicing and dicing on a multi-dimensional table. Furthermore, it can also interact with XMLA servers. This frontend translates user’s navigation actions into MDX queries on the multi-dimensional cube, and show query results on the table he is navigating.


Development of an OLAP document
-------------------------------

The creation of an OLAP analytical document requires the following steps:

1. schema modelling;

2. catalogue configuration; 

3. OLAP cube template building;

4. analytical document creation.

Schema modelling
~~~~~~~~~~~~~~~~

The very first step for a multi-dimensional analysis is to identify essential information describing the process/event under analysis and to consider how it is stored and organized in the database. On the basis of these two elements, a mapping process should be performed to create the multi-dimensional model.

     .. hint::
     
        **From the relational to the multi-dimensional model**

        The logical structure of the database has an impact on the mapping approach to be adopted when creating the multidimensional             model, as well as on query performances.

If the structure of the relational schema complies with multi-dimensional logics, it will be easier to map the entities of the physical model onto the metadata used in Mondrian schemas. Otherwise, if the structure is highly normalized and scarcely dimensional, the mapping process will probably require to force and approximate the model to obtain a multi-dimensional model. As said above, Mondrian is a ROLAP tool. As such, it maps OLAP structures, such as cubes, dimensions and attributes directly on tables and columns of a relational data base via XMLbased files, called Mondrian schemas. Mondrian schemas are treated by Knowage as resources and organized into catalogues. Hereafter, an example of Mondrian schema in Mondrian schema example:

.. code-block:: xml
    :linenos:
    
    <?xml version="1.0"?>                                   
         <Schema name="FoodMart">     
               <!-- Shared dimensions -->   
               <Dimension name="Customers"> 
                  <Hierarchy hasAll="true" allMemberName="All Customers"             
                             primaryKey=" customer_id">                                         
                      <Table name="customer"/>                                           
                      <Level name="Country" column="country" uniqueMembers="true"/>      
                      <Level name="State Province" column="state_province"               
                             uniqueMembers="true"/>                                             

                      <Level name="City" column="city" uniqueMembers="false"/>           

                  </Hierarchy> ...                                                   

               </Dimension> ...                                                      

               <!-- Cubes -->                                                        
               <Cube name="Sales">                                                   

                  <Table name="sales_fact_1998"/>                                    

                  <DimensionUsage name="Customers" source="Customers"                
                                  foreignKey="customer_id" /> ...                                                             

                  <!-- Private dimensions -->                                        

                  <Dimension name="Promotion Media" foreignKey="promotion_id">       

                      <Hierarchy hasAll="true" allMemberName="All Media"                 
                                 primaryKey="promotion_id"> 
                          <Table name="promotion"/>          
                          <Level name="Media Type" column="media_type" uniqueMembers="true"/>   
                      </Hierarchy>                                                       

                  </Dimension> ...                                                   

                  <!-- basic measures-->                                             

                  <Measure name="Unit Sales" column="unit_sales" aggregator="sum"    
                           formatString="#,###.00"/>                                                       

                  <Measure name="Store Cost" column="store_cost" aggregator="sum"    
                           formatString= "#,###.00"/>                                         

                  <Measure name="Store Sales" column="store_sales" aggregator="sum"  
                           formatString="#,###.00"/>                                          
                  ...                                                                

                  <!-- derived measures-->                                           

                  <CalculatedMember name="Profit" dimension="Measures">              
                      <Formula>        
                           [Measures].[Store Sales] - [Measures].[Store Cost]  
                      </Formula>                                                         

                      <CalculatedMemberProperty name="format_string" value="$#,##0.00"/> 
                  </CalculatedMember>                                                

               </Cube> 
          ...      
 </Schema> 

 Code 8.1: Mondrian schema example

Each mapping file contains one schema only, as well as multiple dimensions and cubes. Cubes include multiple dimensions and measures. Dimensions include multiple hierarchies and levels. Measures can be either primitive, i.e., bound to single columns of the fact table, or calculated, i.e., derived from calculation formulas that are defined in the schema. The schema also contains links between the elements of the OLAP model and the entities of the physical model: for example, <table> sets a link between a cube and its dimensions, while the attributes primaryKey and foreignKey reference integrity constraints of the star schema.

   |image191|

Engine catalogue configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To reference an OLAP cube, first insert the corresponding Mondrian schema into the catalogue of schemas managed by the engine. In order to do this, go to **Catalogs> Mondrian schemas catalog**. Here you can define the new schema uploading you XML schema file and choosing **Name** and **Description**. When creating a new OLAP template, you will choose among the available cubes defined in the registered schemas.

Note that the Lock option forbids other technical users to modify settings.

OLAP template building
~~~~~~~~~~~~~~~~~~~~~~

Once the cube has been created, you need to build a template which maps the cube to the analytical document. To accomplish this goal the user must manually edit the template. The template is an XML file telling Knowage OLAP engine how to navigate the OLAP cube and has a structure like the one represented in Code 8.2:

.. code-block:: xml
    :linenos:
    
     <?xml version="1.0" encoding="UTF-8"?> 
     <olap>                                 
        <!-- schema configuration -->       
        <cube reference="FoodMart"/>        

        <!-- query configuration -->        
        <MDXquery>  
            SELECT {[Measures].[Unit Sales]} ON COLUMNS           
            , {[Region].[All Regions]} ON ROWS                    
            FROM [Sales]                                          
            WHERE [Product].[All Products].[${family}]            
            <parameter name="family" as="family"/>                
        </MDXquery>                                           

        <MDXMondrianQuery>                                    
            SELECT {[Measures].[Unit Sales]} ON COLUMNS           
            , {[Region].[All Regions]} ON ROWS                    
            FROM [Sales]                                          
            WHERE [Product].[All Products].[Drink]                
        </MDXMondrianQuery>                                   

        <!-- toolbar configuration -->                        
        <TOOLBAR>                                             
            <BUTTON_MDX visible="true" menu="false" />            
            <BUTTON_FATHER_MEMBERS visible="true" menu="false"/>  
            <BUTTON_HIDE_SPANS visible="true" menu="false"/>      
            <BUTTON_SHOW_PROPERTIES visible="true" menu="false"/> 
            <BUTTON_HIDE_EMPTY visible="true" menu="false" />     
            <BUTTON_FLUSH_CACHE visible="true" menu="false" />    
            <BUTTON_SAVE visible="true" menu="false" />           
            <BUTTON_SAVE_NEW visible="true" menu="false" />       
            <BUTTON_EXPORT_OUTPUT visible="true" menu="false" />  
        </TOOLBAR>                                            

        <!-- data profiling -->                               
        <DATA-ACCESS>                                         
           <ATTRIBUTE name="family"/>                            
        </DATA-ACCESS>                                        
     </olap>                                                  

   Code 8.2: Mapping template example

An explanation of different sections of Mapping template example follows.

-  The CUBE section sets the Mondrian schema. It should reference the exact name of the schema, as registered in the catalogue on the      Server.

-  The MDXMondrianQuery section contains the original MDX query defining the starting view (columns and rows) of the OLAP document.

-  The MDX section contains a variation of the original MDX query, as used by the Knowage Engine. This version includes parameters (if      any). The name of the parameter will allow Knowage to link the analytical driver associated to the document via the parameter (on        the Server).

-  The TOOLBAR section is used to configure visibility options for the toolbar in the OLAP document. The exact meaning and                  functionalities of each toolbar button are explained in next sections. A more complete list of the available options is shown in Menu    configurable options:

.. code-block:: xml
    :linenos:
    
   <BUTTON_DRILL_THROUGH visible="true"/>    
   <BUTTON_MDX visible="true"/>              
   <BUTTON_EDIT_MDX visible="true"/>         
   <BUTTON_FATHER_MEMBERS visible="true"/>   
   <BUTTON_CC visible="true"/>               
   <BUTTON_HIDE_SPANS visible="true"/>       
   <BUTTON_SORTING_SETTINGS visible="true"/> 
   <BUTTON_SORTING visible="true" />         
   <BUTTON_SHOW_PROPERTIES visible="true"/>  
   <BUTTON_HIDE_EMPTY visible="true"/>       
   <BUTTON_FLUSH_CACHE visible="true"/>      
   <BUTTON_SAVE visible="true"/>             
   <BUTTON_SAVE_NEW visible="true"/>        
   <BUTTON_UNDO visible="true"/>             
   <BUTTON_VERSION_MANAGER visible="true"/>  
   <BUTTON_EXPORT_OUTPUT visible="false"/>   

  Code 8.3: Menu configurable options

- The DATA-ACCESS section is used to configure visibility options for data, in particular when the dimensions or cubes defining them are   profiled also in the underlying schema. Details on how to profile OLAP cubes are explained in next sections.

Profiled access
~~~~~~~~~~~~~~~

As for any other analytical document, Knowage provides filtered access to data via its behavioural model. The behavioural model is a very important concept in Knowage. For a full understanding of its meaning and functionalities, please refer to Behavioural Model.

Knowage offers the possibility to regulate data visibility based on user profiles. Data visibility can be profiled at the level of the OLAP cube, namely the cube itself is filtered and all queries over that cube share the same data visibility criteria.

To set the filter, which is based on the attribute (or attributes) in the user’s profile, the tecnical user has to type the Mondrian schema. We report Cube level profilation example as a reference guide. Note that data profiling is performed on the cube directly since the filter acts on the data retrieval logics of the Mondrian Server. So the user can only see the data that have been got back by the server according to the filter.


.. code-block:: xml
    :linenos:
    
   <?xml version="1.0"?>                                                 
   <Schema name="FoodMartProfiled"> 
   ....                                 
     <Cube name="Sales_profiled"> <Table name="sales_fact_1998"/> 
     ...      
        <!-- profiled dimension -->                                        
        <Dimension name="Product" foreignKey="product_id">                 
            <Hierarchy hasAll="true" allMemberName="All Products" primaryKey="product_id">                                   
                <View alias="Product">                                             
                  <SQL dialect="generic">                                            
                    SELECT pc.product_family as product_family, p.product_id as        
                    product_id,                                                        
                    p.product_name as product_name,                                    
                    p.brand_name as brand_name, pc.product_subcategory as              
                    product_subcategory, pc.product_category as product_category,      
                    pc.product_department as product_department                        
                    FROM product as p                                                  
                    JOIN product_class as pc ON p.product_class_id = pc.               
                    product_class_id                                                   
                    WHERE and pc.product_family = '${family}' 
                  </SQL>                   
                </View>                                                            

                <Level name="Product Family" column="product_family"               
                       uniqueMembers="false" />                                                                 
                <Level name="Product Department" column="product_department"       
                       uniqueMembers="false"/>                                                          
                <Level name="Product Category" column="product_category"           
                      uniqueMembers=" false"/>                                           
                <Level name="Product Subcategory" column="product_subcategory"     
                       uniqueMembers="false"/>                                            
                <Level name="Brand Name" column="brand_name"                       
                       uniqueMembers="false"/>                                            
                <Level name="Product Name" column="product_name"                   
                       uniqueMembers="true"/>                                             
            </Hierarchy>                                                       
        </Dimension>                                                       
     </Cube> 
     ...                                       
   </Schema> 

   Code 8.4: Cube level profilation example.

In the above example, the filter is implemented within the SQL query that defines the dimension using the usual syntax and pr.product_family = '${family}'.

To properly set visibility it is required to edit also the OLAP template, adding the <DATA-ACCESS> ... </DATA-ACCESS> tab. OLAP template profilation gives an example.

.. code-block:: xml
    :linenos:
    
   <olap> 
    ...                        
      <DATA-ACCESS>                   
        <ATTRIBUTE name="family" />     
        <ATTRIBUTE name="department" /> 
      </DATA-ACCESS>                  
   </olap>                            

  Code 8.5:OLAP template profilation example.

The value of the “family” user profile attribute will replace the ${family} placeholder in the dimension definition.

You can filter more than one dimensions/cubes and use more profile attributes, remembering to define them in the template. The engine substitutes into the query the exact value of the attribute; in case of a multi value attribute to insert in an SQL-IN clause you will have to give the attribute a value like ’value1’, ’value2’, and insert into the query a condition like “ and pc.product_family IN (${family})”.

Creating the analytical document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the template ready you can create the OLAP document on Knowage Server.

To create a new OLAP document, click on the “create a new document” button in the **Document Development** area and select **Online analytical processing** as Type. Then you can choose the available engines. In this case we have only the **OLAP engine**. 

Type a name, a functionality, load the XML template and save. You will see the document in the functionality (folder) you selected, displayed with the typical cube icon as shown in Figure 8.1.



   |image192|

   Figure 8.1: OLAP document on server.

OLAP Designer\*
---------------

Knowage Server is also endowed of an efficient OLAP designer which avoid the user to edit manually the XML-based template that we discussed on in Development of an OLAP document. We will therefore describe here all features of this functionality. 

The user needs to have a functioning Modrian schema to start the work with. Select **Mondrian Schemas Catalog** to check the available Mondrian schemas on server. It is mandatory that the chosen Mondrian schema has no parameters applied.

   |image193|

The page as the one in Figure 8.2 will open.

   |image194|

   Figure 8.2: Schema Mondrian from catalog.

Then we start entering the **Document Browser** and clicking on the “Plus” icon at the top right corner of the page. Fill in the mandatory boxes as Label and Name of the document, select the On-line Analytica Process Type of document and the What-if Engine (we stress that the What-if engine is available only for who have purchased the Knowage SI package). Remember to save to move to the next step: open the Template Build. The latter can be opend clicking on the editor icon |image195| and it is available at the bottom of the document detail page.

The action opens a first page asking for the kind of template. Here we choose the Mondrian one. Consequently you will be asked to choose the Mondrian Schema and after that to select a cube. Figure 8.3 sums up these three steps. Following the example just given in Figure 8.3 you will enter a page like that of Figure 8.4. 

   |image196|

   Figure 8.3: OLAP core configuration.

   |image197|

   Figure 8.4: Defining OLAP template.

Once entered the page the user can freely set the fields as filter panels or as filter cards, according to requirements. Refer to Chapter 7.1 to review the terminology. Make your selection and you can already save the template as shown in Figure 8.5. You can notice that the side panel contains some features (Figure 8.6): 

   |image198|

   Figure 8.5: Defining OLAP template.

   |image199|

   Figure 8.6: Side panel features for the OLAP Designer.


-  |image200| to set the drill on Position, Member or Replace;

-  |image201| to configure the scenario; 

- |image202| to define the cross navigation;

-  |image203| to configure buttons visibility.


Refer to Section 7.2 to recall the action of the different drills. To select between them will affect the navigation of the OLAP outputs by users. Instead the scenario is used to allow the end-user to edit or not the records contained in the OLAP table. The user is first asked to select the cube in order to get the measures that the admin lets the end-user the permission to edit and modify. Referring to Figure 8.8, an admin user must simply check the measures using the wizard. At the bottom of the page there is also the possibility to add a parameter that can be used by the end-user when editing the measure, for example if one has a frequent multiplication factor that changes accordingly to the user’s needs, the end-user can use that factor to edit measures and ask the admin to update it periodically.

   |image204|

   Figure 8.7: Wizard to configure the scenario.

Once one cross navigation has been set you keep on adding as many as required. Just open the wizard and click on the “Add” button at the top right corner.

Note that the parameter name will be used to configure the (external) cross navigation. In fact, to properly set the cross navigation the the user must access the “Cross Navigation Definition” functionalities available in Knowage Server. Here, referring to Section 5.5, you will use the parameter just set as output parameter.

As shown in Figure 8.9, the buttons visibility serves to decide which permissions are granted to the end-user. Some features can only be let visible while the admin can also grant the selection for others. 

Once the configuration is done click on the **Save template** button and on the **Close designer** button to exit template. As Figure 8.6 highlights, these two buttons are available at the bottom of the side panel.

The admin can develop the OLAP document using also the OLAP engine. In this case the OLAP designer will lack of the scenario configuration since in this case the end-user must not have the grants for editing the records. So in this instance the “Configure scenario” button is not available at all. For the other two options the instructions are right the same as the What-if engine.

   |image205|

   Figure 8.8: Cross navigation definition.

   |image206|

   Figure 8.9: Wizard to configure the scenario.


Profiled access
~~~~~~~~~~~~~~~

Once the OLAP document has been created using the template designer the user can insert parameters to profile the document. To set parameters the user can follow two paths, already seen in Development of an OLAP document:

-  to download the template of the document and edit it, adding the parameter(s),

-  to download the Mondrian schema and edit it; modify the dimension(s) (that will update according to the value parameter(s)) inserting    an SQL query which presents the parametric filtering clause. Then it is necessary to add tbe DATA-ACCESS tab to the template.

 .. hint::
    **Filter through the interface**

    Note that for the OLAP instance, it has not proper sense to talk about “general” parameters. In this case we only deal with             profile attributes while all the filtering issue is performed through the interface, using the filter panel.



Cross Navigation
-----------------

The cross navigation must be implemented at template level but also at analytical document level. The latter has been already wildly described in Cross Navigation . In the following we will see the first case. Observe that both procedures are mandatory.

For OLAP documents it is possible to enable the cross navigation on members or on cells and we will give more details on these two cases in the following.

Generally speaking, the user must modify the template file to configure the cross navigation in order to declaire the output parameters of the document. We remember that the output parameters definition is discussed in Section 5.5 of this manual. 

Cross navigation on members
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To activate the cross navigation on a member means that the user can click on a member of a dimension to be sent and visualize a target document. The first type of navigation can be set by editing the OLAP query template. In the first case you need to add a section called “clickable” inside the MDX query tag. In fact,

-  the attribute value is equal to the hierarchy level containing the member(s) that shall be clickable;

-  the element represents the parameter that will be passed to the destination document. The name attribute is the URI of the              parameter that will be passed to the target document. The value 0 represents the currently selected member, as a convention: this        value will be assigned to the parameter whose URI is null.

Figure 8.10 gives an example. Note that you can recognize that the cross navigation is activated when elements are shown blue highlighted and underlined.

   |image208|

   Figure 8.10: Cross navigation on member.

If you open the template file you will read instructions similar to the ones reported in Syntax used to set cross navigation.

.. code-block:: xml
    :linenos:
    
     <MDXquery> 
       select {[Measures].[Unit Sales]} ON COLUMNS,               
       {([Region].[All Regions], [Product].[All Products])} ON ROWS from     
       [Sales_V]                                                             
       <clickable uniqueName="[Product].[Product Family]" >                  
          <clickParameter name="family" value="{0}"/>                           
       </clickable>                                                          
     </MDXquery>                                                           

 Code 8.6: Syntax used to set cross navigation.


Cross navigation from a cell of the pivot table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This case is similar to the one-dimension drill except that in this case values of all dimensions can be passed to the target document. In other words, the whole dimensional context of a cell can be passed. Now let us suppose the user wishes to click on a cell and pass to the target document the value of the level family of product dimension and year of time dimension. It should creates two parameters one for family where dimension is product, hierarchy is product, level is product family and one for year parameter where dimension in type, hierarchy is time and level is year. Let see what happens when user clicks on a cell. Depending on the selected cell, the analytical driver family of the target document will have a different value: it will be the name of the context member (of the selected cell) of the “Product” dimension, i.e. the [Product] hierarchy, at [Product].[ProductFamily] level. Look at the following Table 8.1 for some examples:

+-----------------------------------------------------------------+-----------------------------------------------------+
|    Context member on Product dimension                          | "Family" analytical driver value                    |
+=================================================================+=====================================================+
|    [Product].[All Products]                                     | [no value: it will be prompted to  the user]        |
+-----------------------------------------------------------------+-----------------------------------------------------+
|    [Product].[All Products].[Food]                              | Food                                                |
+-----------------------------------------------------------------+-----------------------------------------------------+
|    [Product].[All Products].[Drink]                             | Drink                                               |
+-----------------------------------------------------------------+-----------------------------------------------------+
|    [Product].[All Products].[Non-Consumable]                    | Non-Consumable                                      |
+-----------------------------------------------------------------+-----------------------------------------------------+
|    [Product].[All Products].[Food].[Snacks]                     | Food                                                |
+-----------------------------------------------------------------+-----------------------------------------------------+
|    [Product].[All Products].[Food].[Snacks].[Candy]             | Food                                                |
+-----------------------------------------------------------------+-----------------------------------------------------+
 
   Table 8.1

Let us have a look at the template. Syntax used to set cross navigation shows how to use the cross navigation tag:

.. code-block:: xml
    :linenos:
    
   <CROSS_NAVIGATION>                                                    
      <PARAMETERS>                                                       
          <PARAMETER name="family" dimension="Product" hierarchy="[Product]" 
                     level="[Product].[Product Family]" />                             
          <PARAMETER name="year" dimension="Time" hierarchy="[Time]"        
                     level="[Time].[Year]" />                                                          
      </PARAMETERS>                                                      
   </CROSS_NAVIGATION>                                                   

 Code 8.7: Syntax used to set cross navigation


A green arrow will be visible in the toolbar to show that cross navigation is enabled. When user clicks on that icon in each cell a green arrow will displayed in each cell. User can click on that icon to start cross navigation from a cell.

   
     .. include:: olapThumbinals.rst
