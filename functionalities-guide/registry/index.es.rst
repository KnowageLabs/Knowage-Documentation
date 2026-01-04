# Registro

Un documento del Registro permite a los usuarios escribir, cancelar y modificar elementos de un datamart. Knowage permite a los usuarios implementar un documento del Registro a través del **Motor Qbe**. Por cierto, tiene una interfaz gráfica diferente en comparación con la de Qbe. En la siguiente figura se da un ejemplo. En los próximos capítulos veremos cómo navegar por un documento del Registro (*Características del Registro* párrafo) y cómo crear uno nuevo (*Desarrollo de registros* párrafo).

.. figura:: media/image339.png

    Example of Registry document.

## Características del Registro

La ejecución de un documento del Registro abre una tabla simple: los registros se muestran en filas y se pueden navegar utilizando la paginación disponible en la parte inferior de la ventana. Subrayamos que es posible editar cada elemento de la tabla si dentro de la plantilla esa columna está configurada para ser editable. Simplemente haga clic en una celda que desee reorganizar y escriba una cadena o un valor numérico en consecuencia. A continuación se destacan algunos ejemplos.

.. figura:: media/image340.png

    Editing table cells.

Además, puede agregar nuevas filas desde cero seleccionando el botón "Agregar fila" |image335| en el encabezado de la última columna. Inserte en cada celda el valor correspondiente: cadena, número o fecha. El botón "Agregar fila" estará disponible si dentro de la plantilla hay una configuración: <CONFIGURATION name="enableAddRecords" value="true"/>

.. |image335| imagen:: media/image341.png
:ancho: 30

.. figura:: media/image343.png

    Adding a new row.

Viceversa, puede eliminar una o más filas usando el icono "Papelera" |image338| en la última columna. El botón "Papelera" estará disponible si dentro de la plantilla hay una configuración: <CONFIGURATION name="enableDeleteRecords" value="true"/>

.. |image338| imagen:: media/image344.png
:ancho: 30

Es importante hacer clic en el botón "Guardar" |image339| para almacenar los ajustes realizados en el datamart. El botón "Guardar" está disponible en la barra de funcionalidad, encima de la tabla.

.. |image339| imagen:: media/image345.png
:ancho: 30

.. \_functionalitybar:
.. figura:: media/image342.png

    Functionality bar.

Además, puede utilizar filtros, si se implementan, disponibles en la barra de funcionalidad. Haga clic en el icono "Filtro" |image340| para ejecutar la funcionalidad. De lo contrario, haga clic en el icono "Cancelar" para desactivar las casillas.

.. |image340| imagen:: media/image346.png
:ancho: 30

Tenga en cuenta que, dado que los registros se muestran en una tabla simple, está disponible un cuadro combinado (consulte la figura a continuación) que permite al usuario visualizar todos los campos relacionados con el registro de la celda anterior y luego cambiar de uno a otro para obtener todos los datos.

.. figura:: media/image348.png

    Select one field from a combobox.

Características de JPivot Registry

```

It is possible to implement also a JPivot Registry document. The graphical features are very similar to the ones exposed in *Registry development* paragraph. An example is given below.

.. _examplejpivotregdoc:
.. figure:: media/image349.png

    Example of Jpivot Registry document.

In this case the table shows columns organized in a hierarchical way and a grouping function is implemented. From the left to the right the columns contain fields at different detail levels. The last column in our example in the figure above contains numeric data. Such a field is grouped at the “country” level. The grouping level depends on the configurations made on template building.

In the JPivot instance it is not allowed to add, modify or cancel rows. Furthermore, it is not permitted to edit cells which contain string items while the numeric ones are still changeable. If implemented, filters are still available.


Registry development
--------------------

To create a Registry document there must be available a datamart schema on Knowage Server. Then you must edit an XML template. The latter is very similar to the one produced under the Qbe development but in this case you must add an appropriate tag. Indeed, if the template file has the **<REGISTRY>** tag the engine shows data in registry modality; namely it shows a table whose rows are manageable by end users by adding, editing or deleting them.

Here we exhibit a possible syntax for a Registry document.

.. _exampletemplatebuild:
.. code-block:: xml
    :linenos:
    :caption: Example (a) of template for Registry.

    <?xml version="1.0" encoding="windows-1250"?>
    <QBE>
		<DATAMART name="RegFoodmartModel" />
		<REGISTRY>
			<ENTITY name="it.eng.knowage.meta.regfoodmartmodel.Product">
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
					<CONFIGURATION name="enableDeleteRecords" value="true"/>
					<CONFIGURATION name="enableAddRecords" value="true"/>
					<CONFIGURATION name="isPkAutoLoad" value="true"/>
				</CONFIGURATIONS>
			</ENTITY>
		</REGISTRY>
	</QBE>

In particular, we give some details for each tag and main attributes.

-  **ENTITY**: the entity name as in the model. It must be the fully-qualified name of the class representing your registry in the model;
-  **FILTERS**: possibility to define filters by specifying the title, the field (among shown columns) and the type among COMBO, MANUAL or DRIVER: in this last case user has also to specify the analytical driver that take this filter’s value;
-  **COLUMNS**: columns list specifying:

   -  **field name**: the reference to the field identifier into the model;
   -  **title**: the title of the column shown (optional);
   -  **visible**: the visibility of the column (optional, default true);
   -  **editable**: the editability of the column (optional, default true);
   -  **color and format for numbers**: optional;
   -  **size**: the width of the column (optional);
   -  **editor**: the editor. Default type is free-text for simple column (not FK values), but for date is possible to show the picker through the type PICKER. The format option specifies the format date;
   -  **subEntity**: if the column is a reference key, the user can specify the subentity referred and the foreign key name. This value must be equals to the name of the relationship object created in the model. The field shown will be of the entity referred and will be shown as COMBO if editable;
   -  **foreignKey**: if the subEntity property is set, foreignKey property must be set with the name of the foreign key (to lower case);
   -  **dependsFrom**: if the column content is logically correlated to other registry’s column, it is possible to specify this logic through this parameter. DependsFrom identifies the field name on which it depends (Optional);
   -  **dependsFromEntity**: usable only with dependsFrom parameter. It defines a different entity to resolve the correlation (optional);
   -  **orderBy**: is used in case of foreign key. The combo box is ordered by the column here indicated, by default is the column extracted (optional);
   -  **infoColumn**: if true ignore the column when inserting or updating the record (optional);
   -  **defaultValue**: defines the default value for the field; if the user does not set any value for this field during insertion, this value will be set automatically (optional, not allowed if subEntity or foreignKey property is set). For date fields, the correct pattern is "yyyy-MM-dd'T'HH:mm:ss.xxx'Z'".

We stress that it is mandatory to point at one datamart table using a column with a numeric key. The code line is highlighted in figure below. While, if not elsewhere specified, a descriptive column will be displayed by default.

.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.

    <COLUMNS>
      <COLUMN field="store_id" visible="false" editable="false" />
      ...
    </COLUMNS>


Still referring to the code above, we underline that the “product_subcategory” field is used as a subcategory. It belongs in fact to another table. In this case it is enough to add the attributes: subEntity="rel_product_class_id_in_product_class"  foreignKey="rel_product_class_id_in_product_class".

Filters
```

.. code-block:: xml
:linenos:
:caption: Ejemplo de definición de filtro.

    <FILTERS>
    	<FILTER title="Store type" field="store_type" presentation="MANUAL" />
    	<FILTER title="Sales city" field="sales_city" presentation="COMBO" />
    	<FILTER title="Sales first_opened_date" field="first_opened_date" static="true" visible="true" filterValue="29/05/2020 02:00:00.0" />
    </FILTERS>

La definición del filtro permite establecer diferentes propiedades:

*   **título**: el título del filtro;
*   **campo**: la referencia al identificador de campo en el modelo;
*   **presentación**: COMBO/DRIVER/MANUAL (opcional si static="true");
*   **visible**: la visibilidad del filtro (opcional, por defecto falso);
*   **estático**: verdadero/falso. Establezca esta propiedad si desea limitar el valor del filtro a un valor específico (opcional);
*   **filterValor**: el valor específico que desea establecer para el filtro (obligatorio si static="true"). Para los campos de fecha, el patrón correcto es "%d/%m/%Y %h:%i:%s".

Controlador analítico

    Registry filtering by analytical driver is possible using DRIVER value for presentation property in filter TAG. Registry template must contains FILTERS tag. Below an example of configuration for a driver named "UNIT_SALES_AD" insisting on the column "UNIT_SALES".

    .. code-block:: xml
       :linenos:
       :caption: Pointing at a numerical column.

       <FILTERS>
          <FILTER title="UNIT_SALES_AD_title" field="UNIT_SALES" presentation="DRIVER" driverName="UNIT_SALES_AD" />
       </FILTERS>


    Profile attributes

Otra forma de filtrar el contenido del Registro es mediante atributos de perfil. Si desea utilizar atributos de perfil para filtrar valores, debe seguir estos pasos:

*   Crear un atributo de perfil (si es necesario) desde el menú Administrar atributos de perfil
*   Asociar el atributo de perfil a la columna durante la creación del modelo

De esta manera, sus datos serán filtrados por este atributo (si no están vacíos) tanto al ver datos como al insertar o actualizar registros.

Multivalor

***

Si su atributo de perfil es multivalor, debe:

*   poner *EN* cláusula como *"Tipo de filtro de atributo de perfil"* durante la creación del modelo
*   Establecer valores de atributo de perfil que respeten este formato *'value1','value2',...,'valueN'* o *{,{value1,value2,...,valueN}}*.

De esta manera, el valor del atributo de perfil se tratará como una lista de valores y se aplicará un filtro con este criterio.

Instancia de JPivot Registry

```

The Registry instance allows to develop also a Jpivot table. See the last figure (above) to have an idea while the syntax example is given in the next code:

.. code-block:: xml
    :linenos:
    :caption: Example (b) of template code for Registry.

	<QBE>
		<DATAMART name="foodmart" />
		<REGISTRY pagination = "false" summaryColor="#00AAAA">
			<ENTITY name="it.eng.knowage.meta.foodmart.Store">
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
					<CONFIGURATION name="enableDeleteRecords" value="true"/>
					<CONFIGURATION name="enableAddRecords" value="true"/>
				</CONFIGURATIONS>
			</ENTITY>
		</REGISTRY>
	</QBE>

Note that to activate the JPivot modality it is important to add the attribute type="merge" and have at least one numeric field. Furthermore the selected column fields must be hierarchically structured.

Logging & auditing
-------------------

The Registry engine is logging changes performed by users when interacting with Registry documents (insertions/updates/deletions of entries).

By default, the engine is logging messages such as

.. code-block:: bash
   :linenos:

   01 feb 2021 11:40:49,750: User <name of the user> is performing operation <INSERTION/UPDATE/DELETION> on entity <name of the entity> from model <model name> for record: old one is ..., new one is ..., number of changes is ...

into the ``TOMCAT_HOME/logs/knowageQbeEngineAudit.log`` file.

In case you want those information to be stored into a database table (for analytical and visualization purposes), you have to create it and then to configure the engine logging system accordingly, following the below example based on MySQL.

Let's create a table:

.. code-block:: sql
   :linenos:

   CREATE TABLE `LOG_REGISTRY` (
      `AUDIT_ID` INT NOT NULL AUTO_INCREMENT,
      `AUDIT_DATETIME` DATETIME NULL,
      `AUDIT_OPERATION` VARCHAR(45) NULL,
      `AUDIT_USER` VARCHAR(100) NULL,
      `AUDIT_CHANGES_NO` INT NULL,
      `ENTITY_NAME` VARCHAR(100) NULL,
      `MODEL_NAME` VARCHAR(100) NULL,
      `ATTRIBUTES_OLD` TEXT NULL,
      `ATTRIBUTES_NEW` TEXT NULL,
      PRIMARY KEY (`AUDIT_ID`));

then edit ``TOMCAT_HOME/webapps/knowageqbeengine/WEB-INF/classes/log4j.properties`` and add:

.. code-block:: jproperties
   :linenos:
   
   # Define the SQL appender
   log4j.appender.sql=it.eng.spagobi.utilities.logging.Log4jJNDIAppender
   # JNDI connection to be used
   log4j.appender.sql.jndi=java:comp/env/jdbc/knowage
   # Set the SQL statement to be executed.
   log4j.appender.sql.sql=INSERT INTO LOG_REGISTRY (AUDIT_DATETIME,AUDIT_OPERATION,AUDIT_USER,AUDIT_CHANGES_NO,ENTITY_NAME,MODEL_NAME,ATTRIBUTES_OLD,ATTRIBUTES_NEW) VALUES (now(),'%X{operation}','%X{userId}',%X{variations},'%X{entityName}','%X{modelName}','%X{oldRecord}','%X{newRecord}')
   # Define the xml layout for file appender
   log4j.appender.sql.layout=org.apache.log4j.PatternLayout

   log4j.logger.it.eng.qbe.datasource.jpa.audit.JPAPersistenceManagerAuditLogger=INFO, FILE_AUDIT
   log4j.additivity.it.eng.qbe.datasource.jpa.audit.JPAPersistenceManagerAuditLogger=false

pay attention to the JNDI name (in case you created the table within Knowage metadata database, then ``java:comp/env/jdbc/knowage`` is fine) then restart Knowage server: this way, when user is interacting with a registry document, the ``LOG_REGISTRY`` (as per the SQL script above) table will contain:

- ``AUDIT_DATETIME``: the date and time when the operation was performed
- ``AUDIT_OPERATION``: one of the following values: INSERTION/UPDATE/DELETION
- ``AUDIT_USER``: the user who performed the operation
- ``AUDIT_CHANGES_NO``: number of attributes that were actually changed in case of an UPDATE, null otherwise
- ``ENTITY_NAME``: name of the modified entity type
- ``MODEL_NAME``: name of the business model
- ``ATTRIBUTES_OLD``: previous attributes state in case of an UPDATE or DELETION
- ``ATTRIBUTES_NEW``: new attributes state in case of an INSERTION or UPDATE
```
