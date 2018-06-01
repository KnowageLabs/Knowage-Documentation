
Registry development
--------------------

To create a Registry document there must be available a datamart schema on Knowage Server. Please, refer to Chapter ?? to get more details on how to build it. Then you must edit an XML template. The latter is very similar to the one produced under the Qbe development but in this case you must add an appropriate tag. Indeed, if the template file has the **<REGISTRY>** tag the engine shows data in registry modality; namely it shows a table whose rows are manageable by end users by adding, editing or deleting them.

Here we exhibit a possible syntax for a Registry document.

.. code-block:: xml
    :linenos:
    
    <?xml version="1.0" encoding="windows-1250"?> 
    <QBE>  
      <DATAMART name="RegFoodmartModel" /> 
         <REGISTRY>                  
         <ENTITY name="it.eng.spagobi.meta.Product"> 
             <FILTERS>   
               <FILTER title="Class" field="product_subcategory" presentation="COMBO" /> 
               <FILTER title= "Product name" field="product_name" presentation="COMBO" />  
             </FILTERS>                                                         

             <COLUMNS>  
                <COLUMN field="product_id" unsigned="true" visible="false" editable="false" format="####" />
                <COLUMN field="product_name" title="Product name" size="200"       
                        editor= "MANUAL" sorter="ASC"/> 
                <COLUMN field="product_subcategory" title="Class" size="200"       
                        subEntity="rel_product_class_id_in_product_class" foreignKey="rel_product_class_id_in_product_class" />  
                <COLUMN field="SKU" title="SKU" size="200" editor="MANUAL" /> 
                <COLUMN field="gross_weight" title="Gross weight" size="200" editor="MANUAL" />     
                <COLUMN field="net_weight" title="Net weight" size="200" editor="MANUAL" />    
             </COLUMNS>                                                         

             <CONFIGURATIONS> 
               <CONFIGURATION name="enableButtons" value="true"/>                 
               <CONFIGURATION name="isPkAutoLoad" value="true"/> 
            </CONFIGURATIONS>                                                                  
         </ENTITY>                                                                       
      </REGISTRY>                                                                       
   </QBE>                                                                 

 Code 10.1: Example (a) of template for Registry

In particular, we give some details for each tag and main attributes.

-  **ENTITY**: the entity name as in the model;

-  **FILTERS**: possibility to define filters by specifing the title, the field (among shown columns) and the type among COMBO, MANUAL      or DRIVER: in this last case user has also to specify the analytical driver that take this filter’s value;

-  **COLUMNS**: columns list specifing:

   -  **field name**: the reference to the field identifier into the model,

   -  **title**: the title of the column shown (optional),

   -  **visible**: the visibility of the column (Optional, default true),

   -  **editable**: the editability of the column (Optional, default true),

   -  **color and format for numbers**: optional,

   -  **editor**: : the editor. Default type is free-text for simple column (not fk values), but for date is possible show the picker         through the type PICKER. The format option specify the format date,

   -  **subEntity**: If the column is a reference key user can specify the subentity referred and the foreign key name; in this case the       field shown will be of the entity referred and will be shown as combo if editable,

   -  **dependsFrom**: if the column content is logically correlatd to other registry’s column is possible specifiy this logic through         this parameter. DependsFrom identifies the field name on which it depends (Optional),

   -  **dependsFromEntity**: usable only with dependsFrom parameter. It defines a different entity to resolve the correlation                 (Optional),

   -  **orderBy**: is used in case of foreign key, the combo box is ordered by the column here indicated, by default is the column             extracted (Optional).

   -  **infoColumn**: if true ignore the column when inserting or updating the record (Optional).

We stress that it is mandatory to point at one datamart table using a column with a numeric key. The code line is highlighted in Figure 12.7 While, if not elsewhere specified, a descriptive column will be displayed by default.

   |image344|

   Figure 12.7: Pointing at a numerical column.

Still referring to Code 12.1, we underline that the “product_subcategory” field is used as a subcategory. It belongs in fact to another table. In this case it is enough to add the attributes: subEntity="rel_product_class_id_in_product_class"  foreignKey="rel_product_class_id_in_product_class".

JPivot Registry instance
~~~~~~~~~~~~~~~~~~~~~~~~

The Registry instance allows to develop also a Jpivot table. See Figure 12.6 to have an idea while the syntax example is given:

.. code-block:: xml
    :linenos:
    
    <QBE> 
       <DATAMART name="foodmart" /> 
       <REGISTRY pagination = "false" summaryColor="#00AAAA">    
          <ENTITY name="it.eng.spagobi.meta.Store"> 

              <FILTERS> 
                 <FILTER title="Store Type" field="store_type" presentation="COMBO" /> 
              </FILTERS>                                                         

              <COLUMNS>   
                   <COLUMN field="store_id" visible="false" editable ="false" />   
                   <COLUMN field="store_country" title="store country" visible="true" 
                           type="merge" editable ="false" sorter ="ASC" summaryFunction="sum" />  
                   <COLUMN field="store_state" title="store state" visible="true"     
                           type=" merge" editable ="false" sorter ="ASC" />  
                   <COLUMN field="store_city" title="store city" visible="true"       
                           type="merge" editable ="false" sorter ="ASC" />   
                   <COLUMN field="store_type" title="store type" type="merge" sorter="ASC" />  
                   <COLUMN field="store_number" title="Number" size="150"             
                           editable="true" format="########" color="#f9f9f8" type="measure"/>
              </COLUMNS>                                                         

              <CONFIGURATIONS>     
                 <CONFIGURATION name="enableButtons" value="false"/>   
              </CONFIGURATIONS>  
          </ENTITY> 
       </REGISTRY> 
    </QBE>         
   
  Code 10.1: Example (b) of template code for Registry

Note that to activate the JPivot modality it is important to add the attribute type="merge" and have at least one numeric field. Furthermore the selected column fields must be hierarchically structured.
   
     .. include:: registryThumbinals.rst
