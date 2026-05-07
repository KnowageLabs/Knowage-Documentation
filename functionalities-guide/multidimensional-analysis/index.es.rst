# Análisis multidimensional

Las herramientas OLAP permiten a los usuarios analizar datos multidimensionales de forma interactiva desde múltiples perspectivas. OLAP consiste en operaciones analíticas básicas: cortar y dar, enrollar, profundizar y pivotar.

## Manual de usuario de OLAP paso a paso

Comenzamos nuestra conferencia sobre el motor OLAP analizando un documento OLAP existente. Abra la carpeta del explorador de documentos de la suite Knowage como se muestra a continuación e inicie un documento OLAP.

.. figura:: media/image134.png

    Browse the documents and select an OLAP document.

Aquí un ejemplo.

.. figura:: media/image135.png

      Exploring an existing OLAP document.

Describiremos las partes principales de la página OLAP a continuación.

El panel de filtros

```

Once the document is executed, the central area of the window contains the table whose measures are aggregated on dimensions. At the top of this area, panels are available to configure filters on attributes. We see in the following figure that the filter panel is made up of **Filter cards**. Here you can find the cube dimensions and their hierarchies as defined in the OLAP schema by the developer.

.. figure:: media/image136.png

    The filter panel.

The filter cards
```

Las tarjetas de filtro se pueden colocar en el panel de filtro o en el eje de columna. Puede cambiar su posición arrastrándolos y soltándolos de un lugar a otro.

.. figura:: media/image137.png

    The filter card inside the filter panel.

Las tarjetas de filtro se utilizan para:

*   informar al usuario acerca de las dimensiones disponibles definidas en el esquema OLAP,
*   informar al usuario sobre el nombre de la dimensión,
*   rebanadas de rendimiento,
*   Agregue las dimensiones a la visualización del cubo,
*   colocar jerarquías en diferentes ejes,
*   filtrar miembros visibles.

Teniendo en cuenta la siguiente figura, podemos ver que una tarjeta de filtro se compone de:

*   un icono para abrir el cuadro de diálogo selector de cotas (a),
*   un nombre de dimensión (b),
*   segmentación de datos de iconos (c)+(e),
*   nombre de filtro elegido (d),

.. \_featuresoffiltcard:
.. figura:: media/image13839.png

    Features of a filter card.

Panel Ejes

```

In the panel axes you can:

-  drag and drop one or more dimensions,
-  organise the dimensions visualization,
-  swap axes.

Referring to the following figure, the axes panel consists of the following items:

-  columns axis (a),
-  row axis (b),
-  filter cards (c),
-  icon for swap axes (d),
-  icon for hierarchy order (e).

.. _axespanelfeat:
.. figure:: media/image140.png

    Axes panel features.

Pivot table
```

La tabla dinámica es la parte central de la página OLAP. En la siguiente figura se muestra un ejemplo.

.. figura:: media/image141.png

    Pivot table.

La tabla dinámica se utiliza para:

*   mostrar datos basados en consultas MDX enviadas desde la interfaz,
*   desglose/aumento de las dimensiones de las jerarquías,
*   perforar a través de,
*   mostrar las propiedades de un miembro en particular,
*   ordenar datos,
*   mostrar campos calculados,
*   realizar la navegación cruzada a otros documentos.

Refiriéndose a la siguiente figura, la tabla dinámica consta de:

*   dimensiones implicadas en el análisis (a),
*   celdas con datos (b),
*   iconos para profundizar y profundizar (c),
*   iconos para ordenar (solo si el desarrollador lo habilita) (d),
*   iconos para mostrar propiedades (solo si el desarrollador habilita y configura) (e),
*   enlaces para la navegación cruzada (solo si el desarrollador lo habilita y configura) (f).

.. \_pivottablefeat:
.. figura:: media/image142a.png

    Pivot table features.

Barra lateral

```

You can open the side bar by clicking on the icon positioned on the top right side of the page (see next figure). Side bar will be shown on the right side (see *Side bar* figure).

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

The side bar shows the **Menu**. This area let you customize the Olap layout. As highlighted in the figure below, the Menu is divided in three subsections:

-  drill options (a),
-  OLAP functions (b),
-  table functions (c), 
-  what if.

.. _sidebarmenu:
.. figure:: media/image145a.png

    Side bar Menu.

We start introducing the interface and leave the description to the next *Functionalities* paragraph. In particular, referring to next figure, drill types consists of:

-  position (a),
-  member (b),
-  replace (c),
-  drill through (d).

.. _drilltypes:
.. figure:: media/image146.png

    Drill types.

Meanwhile, referring to the following figure, the OLAP functions consist of:

-  show MDX (a),
-  reload model (b).

.. _olapfunctions:
.. figure:: media/image147a.png

    OLAP functions.

Referring to figure below, table functions consist of:

-  show parent members (a),
-  sorting settings (b),
-  save customized view (c),
-  show properties (d),
-  suppress empty rows/columns (e),
-  hide spans (f),
-  calculated field wizard (g).

.. _tablefunctions1:
.. figure:: media/image148a.png

    Table functions.

Referring to next figure, what if consists of:

-  lock/unlock model (a),
-  delete versions (b),
-  select an algotithm (c),
-  output wizard (d), 
-  save as new version (e), 
-  undo (f),
-  export excel for edit (g).

.. _tablefunctions2:
.. figure:: media/image149a.png

    Table functions.

Functionalities
----------------

Placing hierarchies on axes
```

Como ya dijimos, el usuario puede mover fácilmente una dimensión de la barra de filtro al eje o viceversa arrastrándola y soltándola al lugar deseado.

Supongamos que queremos mover una cota del panel de filtro al eje de columnas. Los pasos se resumen en la siguiente figura

.. figura:: media/image150.png

    Move a hierarchy to the columns axis.

Viceversa, para mover hacia atrás la cota desde el eje de columnas hasta el panel de filtro, el usuario simplemente debe arrastrar y soltar la cota de un lugar a otro como en la siguiente figura.

.. figura:: media/image151.png

    Move a dimension from the columns axis to the filter panel.

Del mismo modo, una cota se puede mover desde el panel de filtro al eje de filas simplemente arrastrándola y soltándola de un lugar a otro.

Intercambio de ejes

```

To swap axes the user should click on the icon |image151|. The user will get the outcome showed in figure below.

.. |image151| image:: media/image152.png
   :width: 30

.. figure:: media/image153.png

    Swap axes.

Selecting different hierarchies on dimension
```

Si se define un esquema OLAP, el usuario puede elegir diferentes jerarquías de la misma dimensión. El icono para abrir el cuadro de diálogo se coloca en la esquina superior izquierda de la tarjeta de filtro (si la dimensión tiene más de una jerarquía). Seleccione el icono de jerarquías subrayado a continuación.

.. figura:: media/image154.png

    Hierarchies icon.

Se mostrará una ventana emergente. La siguiente figura muestra sus características. La ventana presentará:

*   el nombre de la dimensión (a),
*   nombre de las jerarquías seleccionadas (b),
*   lista desplegable de jerarquías disponibles (c),
*   botón Guardar (d),
*   botón cancelar (e).

.. \_hierarchiesdialogpopup:
.. figura:: media/image155.png

    Hierarchies dialog pop up.

Después de seleccionar la jerarquía y guardar la elección del usuario, la tabla dinámica utilizará esa jerarquía.

Si el usuario vuelve a abrir la ventana de diálogo, ve las hieararquías seleccionadas y tiene la oportunidad de cambiarlas si es necesario, como se muestra a continuación.

.. figura:: media/image1565758.png

    Changing the hierarchies.

Damos un ejemplo de la salida cuando la jerarquía "Tiempo" se selecciona en la primera figura siguiente y la jerarquía "Tiempo semanal" en la segunda figura siguiente.

.. \_timehierarchieshowsdays:
.. figura:: media/image159.png

     Time hierachy: the table shows days in the month.

.. \_timeweeklyhierarchyshowsweek:
.. figura:: media/image160.png

    Time Weekly hierachy: table shows weeks in the month.

Rebanar

```

The slicing operation consists in the analysis of a subset of a multi-dimensional array corresponding to a single value for one or more members of the dimensions. In order to perform this operation you need to drag and drop the dimesion of interest in the axis panel.  Then clicking on the filter icon choose the new single focus and apply it. Once concluded these steps the cube will show only the selected level of the dimension, while the others have been sliced out.

The following figure shows the slicer option panel which consists of:

-  a dimension name (a),
-  a search input field (b),
-  a search button (c),
-  a show/hide siblings checkbox (d),
-  a member tree (e),
-  a selected member icon (f),
-  a highlighted member (result of searching) (g), 
-  a save and a cancel buttons (h).

.. _dialogforslicerchoosing:
.. figure:: media/image161.png

    Dialog for slicer choosing.

In particular, it is possible to search for a member in three ways:

1. by browsing the member tree;

.. figure:: media/image162.png

   Browsing the member tree.

2. by typing member’s name or it’s part in the input field and clicking on the search button. The research will be possible if the user enters at least four letters. If the user wishes to include member’s siblings to the research, the checkbox (:numref:`dialogforslicerchoosing` (d))needs to be checked;

.. figure:: media/image16364.png

   Using the research box.

3. after the first research, if the user types some other member’s name before clicking on the search button, visible members whose        names contains a entered text will be highlighted.

.. figure:: media/image165.png

    Using the research box after a first investigation.

Once the selection has been saved, the users choice will affect the pivot table and the filter cards slicer name will rearrange.

Filtering
```

Para filtrar los miembros de dimensión en una tabla dinámica, el usuario debe hacer clic en un botón (consulte :numref:`featuresoffiltcard`) situado en el lado derecho de la tarjeta de filtro de dimensiones colocada en el área del filtro.

El procedimiento para buscar un miembro mediante el cuadro de diálogo de filtro no tiene diferencias significativas con el descrito para el cuadro de diálogo de selección de segmentación de datos. La interfaz emergente es la que se muestra a continuación. Después de seleccionar un miembro, el usuario debe hacer clic en el botón Guardar. La tabla dinámica mostrará los cambios. De lo contrario, haga clic en el botón Cancelar para descartar los cambios.

.. figura:: media/image166.png

    Filter dialog.

.. figura:: media/image167.png

    Filter effects on pivot table.

Profundizar y profundizar

```

User can choose between drill types by clicking on one of the three buttons in the drill types section of the side bar. There are three drill types. In the following we give some details on them.

1. **Position**: this is the default drill type. Clicking on a drill down/drill up command will expand/collapse a pivot table with          child members of a member with that particular command. See below.

.. figure:: media/image168.png

     “Position” drill down.

2. **Member**: if the user wants to perform drill operation not only on one member per time but on all members of the same name and        level at the same time it is needed to select member drill type. See below.

.. figure:: media/image169.png

    “Member” drill down.

3. **Replace**: This option lets the user replace the parent member with his child member during drill down operation. To drill up the      user should click on the arrow icon next to the dimension name on which to perform operation. See figure below.

.. figure:: media/image170.png

    “Replace” drill down.

Drill through
~~~~~~~~~~~~~

To perform drill through operation the user needs first to select a cell, as in the following figure, on which to perform operations. Then clicking on the button for a drill through in the side bar, a dialog will open with results (this pop up could take some time to    open).

.. figure:: media/image171.png

    Drill thorugh option.

In particular, referring to the next figure, drill though dialog consists of:

-   a hierarchy menu (a),
-   a table of values (b),
-   a maximum rows drop down list (c),
-   a pagination (d),
-   a apply button (e),
-   a export button (f),
-   a cancel button (g),
-   a clear all button (h).

.. _drillthoroughwindow:
.. figure:: media/image172a.png

    Drill thorugh window.

The user must therefore select a cell, open the side bar and select the drill through item from the panel. A pop up will show up: here the user can choose the level of detail with which data will be displayed. The steps to follow are:

1. to click on hierarchy in hierarchy menu,

2. to check the checkbox of the level,

3. to click on the “Apply” button (after checking the checkbox, remember to click outside of the level list and then select apply).

The user can also select the maximum rows to load by choosing one of the options in the drop down list (see figure above, (c)). Finally, loaded data can be exported in csv format by clicking on the “Export” button.

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

.. figure:: media/image180a.png

    Show properties summarized in a pop up.

Suppressing empty colunms/rows
```

Para ocultar las filas vacías y/o colums, si las hubiera, de la tabla dinámica, el usuario puede hacer clic en el botón "Suprimir filas/colums vacías" en el panel de la barra lateral. Un ejemplo se da en la Figura a continuación.

.. figura:: media/image181.png

    Suppressing empty colunms/rows.

Ordenación

```

To enable member ordering the user must click on the “Enable sorting” button in the side bar panel. The command for sorting will appear next to the member’s name in the pivot table. In addition, the sorting command will show the members of “Measures” hieararchy or members that are crossjoined with them, as shown below. 

.. figure:: media/image18283.png

    Member sorting.

To sort members the user needs to click on the sorting command |image179|, available next to each member of the pivot table. Note that the sorting criteria is ascending at first execution. If the user clicks on the sorting icon, criteria will change to descending and the result will be shown in pivot table.

.. |image179| image:: media/image184.png
   :width: 65

To remove the sorting, the user just have to click on the icon again. To change sorting mode user should click on sorting settings button in the side bar. Referring to the following figure, dialog sorting settings consists of:
   
.. figure:: media/image185a.png

    Sorting settings window.

-  sorting modes (a),
-  no sorting (by default) (b), 
-  basic (c),
-  breaking (d),
-  count (e),
-  a number input field for count mode definition (f),
-  a save button (g).

Note that “breaking mode” means that the hierarchy will be broken.

If the user selects “Count sorting” mode the top or last 10 members will be shown by default in the pivot table. Furthermore, the user can also define a custom number of members that should be shown. 

Calculated members and sets
```

En primer lugar, hacemos hincapié en que para permitir **Campos calculados** en su documento Olap se necesita una etiqueta de botón adecuada en su plantilla Olap. Tal etiqueta es \<BUTTON_CC visible="true"/>.

Una vez habilitado, para crear un miembro/conjunto calculado, el usuario debe:

.. figura:: media/image186.png

Miembro calculado.

1.  seleccionar un miembro de la tabla dinámica, como en la figura anterior, que será el elemento primario del miembro calculado,

2.  haga clic en el botón "campo calculado" en el panel de la barra lateral: aparecerá un cuadro de diálogo "Seleccionar función". Este último consiste en (consulte la siguiente figura):

    *   un campo de entrada de nombre (a),
    *   una ficha de funciones de agregación (b),
    *   una ficha de funciones aritméticas (c),
    *   una ficha de funciones temporales (d),
    *   una ficha de funciones personalizadas (e),
    *   una ficha de funciones recientes (f),
    *   una lista de funciones disponibles (g),
    *   ok y botones de cancelación (h).

.. \_selectfunctiondialog:
.. figura:: media/image187.png

    Select function dialog.

La definición de función utilizada para crear miembros calculados se lee desde la carpeta formula.xml archivo, ubicado en: ROOT/resources/yourTennant/Olap. Las funciones están divididas por pocas pestañas diferentes. En particular,\ **Pestaña Reciente** contiene miembros calculados y conjuntos calculados creados por el usuario y guardados en cookies. Si no hay conjuntos /miembros almacenados en las cookies, esa pestaña estará vacía. **Pestaña Personalizada** es donde definir funciones personalizadas. Estas funciones se pueden utilizar para realizar operaciones realmente complejas que no forman parte de funciones MDX predefinidas. Allí puede usar la combinación de pocas funciones juntas o usar operadores para cálculos matemáticos complejos. También se definen en fórmulas xml. Si una pestaña específica no contiene ninguna fórmula, no se mostrará. El campo "Nombre" es obligatorio, de hecho, la creación de una función sin nombre está prohibida. En **Pestaña reciente**, el campo "Nombre" está oculto. la siguiente figura proporciona un ejemplo de fórmula editada en el archivo formulas.xml.

.. figura:: media/image188.png

    Example of one formula inside of formulas xml.

3.  Seleccione una función e ingrese un nombre de miembro / conjunto calculado y haga clic en "Aceptar". Aparecerá un cuadro de diálogo para la definición de argumentos, como se muestra en la siguiente figura. Este se compone de los siguientes elementos:

*   nombre de función seleccionado (a),
*   descripción de la función (b),
*   campos de entrada de texto para la expresión del argumento (c),
*   tipo de retorno de expresión MDX esperado (d),
*   descripción de la expresión MDX del argumento (e),
*   abrir botón guardado (f),
*   seleccionar del botón de tabla (g),
*   ok y botones de cancelación (h).

.. \_argumentdefdialog:
.. figura:: media/image189.png

    Argument defintion dialog.

En particular, para introducir el argumento de expresión MDX, el usuario tiene tres opciones, enumeradas a continuación.

1.  Escríbalo manualmente (para usuarios avanzados).

2.  Seleccionar miembros de la tabla dinámica: para seleccionar un miembro que se va a incluir en un conjunto, el usuario debe (ver siguiente figura):

    *   haga clic en el botón Seleccionar de la tabla,
    *   haga clic en los miembros de una tabla dinámica,
    *   haga clic en Aceptar en el cuadro de diálogo para finalizar la selección.

.. \_selectingmembers:
.. figura:: media/image190.png

    Selecting members.

La expresión de los miembros seleccionados se importará en campos de entrada de texto para la expresión del argumento, como se muestra en la figura siguiente.

.. figura:: media/image191.png

    Expression of the selected members.

3.  Importar expresión de miembros o conjuntos calculados guardados. Para importar un miembro/conjunto calculado, el usuario debe:

    • Haga clic en el botón Abrir guardado. A continuación, aparecerá el cuadro de diálogo de miembros/conjuntos calculados guardados (siguiente figura) y consta de:

    *   una lista de los miembros y conjuntos calculados guardados,
    *   un nombre de miembro/conjunto calculado,
    *   el tipo de retorno de miembro/conjunto calculado se muestra mediante un icono redondo.

.. \_savedsetsdialog:
.. figura:: media/image192.png

    Saved sets dialog.

• Haga clic en miembro/conjunto calculado. La expresión de miembro/conjunto calculado guardado se importará en campos de entrada de texto para la expresión del argumento, como se resalta a continuación.

.. figura:: media/image193.png

    Expression of the saved/calculated member/set.

• Después de completar todos los argumentos de función, al hacer clic en el botón Aceptar:

      -  add calculated member in a pivot table,
      -  save calculated set and it will be available for creation of other calculated member and sets.

En la pestaña "Reciente", abriendo el cuadro de diálogo "Seleccionar función", el usuario puede encontrar una lista de miembros y conjuntos calculados guardados que se pueden editar o eliminar. La edición se realiza haciendo clic en uno de ellos.

.. figura:: media/image194.png

Edite un miembro calculado.

La eliminación se realiza mediante el botón Eliminar como se muestra en la figura anterior.

## Creación de un documento OLAP\*

El análisis multidimensional permite la indagación jerárquica de medidas numéricas sobre dimensiones predefinidas. En Cockpit explicamos cómo el usuario puede monitorizar los datos en diferentes niveles de detalle y desde diferentes perspectivas. Aquí queremos entrar en detalles de cómo un usuario técnico puede crear un documento OLAP. Recordamos que las principales características de los documentos OLAP son:

*   la necesidad de una estructura de datos específica (lógica o física);
*   análisis basado en dimensiones, jerarquías y medidas;
*   análisis interactivo;
*   libertad para reorientar el análisis;
*   diferentes niveles de análisis de datos, a través de vistas sintéticas y detalladas;
*   drill-down, slice and dice, drill-through operations.

Teniendo en cuenta estos elementos, describiremos los pasos para desarrollar un documento OLAP.

Acerca del motor

```

Knowage performs OLAP documents by relying on the **OLAP engine**. This engine integrates Mondrian OLAP server and two different cube navigation clients to provide multi-dimensional analysis. In general, Mondrian is a Relational Online Analytical Processing (ROLAP) tool that provides the back-end support for the engine. OLAP structures, such as cubes, dimensions and attributes, are mapped directly onto tables and columns of the data warehouse. This way, Mondrian builds an OLAP cube in cache that can be accessed by client applications. The Knowage OLAP engine provides the front-end tool to interact with Mondrian servers and shows the results via the typical OLAP functionalities, like drill down, slicing and dicing on a multi-dimensional table. Furthermore, it can also interact with XMLA servers. This frontend translates user’s navigation actions into MDX queries on the multi-dimensional cube, and show query results on the table he is navigating.


Development of an OLAP document
```

La creación de un documento analítico OLAP requiere los siguientes pasos:

*   modelado de esquemas;
*   configuración del catálogo;
*   Construcción de plantillas de cubos OLAP;
*   creación de documentos analíticos.

Modelado de esquemas
^^^^^^^^^^^^^^^^^

El primer paso para un análisis multidimensional es identificar la información esencial que describe el proceso / evento bajo análisis y considerar cómo se almacena y organiza en la base de datos. Sobre la base de estos dos elementos, se debe realizar un proceso de mapeo para crear el modelo multidimensional.

.. indirecta::

     **From the relational to the multi-dimensional model**

        The logical structure of the database has an impact on the mapping approach to be adopted when creating the multidimensional             model, as well as on query performances.

Si la estructura del esquema relacional cumple con lógicas multidimensionales, será más fácil asignar las entidades del modelo físico a los metadatos utilizados en los esquemas de Mondrian. De lo contrario, si la estructura es altamente normalizada y escasamente dimensional, el proceso de mapeo probablemente requerirá forzar y aproximar el modelo para obtener un modelo multidimensional. Como se dijo anteriormente, Mondrian es una herramienta ROLAP. Como tal, mapea estructuras OLAP, como cubos, dimensiones y atributos directamente en tablas y columnas de una base de datos relacional a través de archivos basados en XML, llamados esquemas Mondrian. Los esquemas de Mondrian son tratados por Knowage como recursos y organizados en catálogos. A continuación, un ejemplo de esquema de Mondrian en ejemplo de esquema de Mondrian:

.. code-block:: xml
:linenos:
:caption: Ejemplo de esquema de Mondrian

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

Cada archivo de asignación contiene un solo esquema, así como varias dimensiones y cubos. Los cubos incluyen múltiples dimensiones y medidas. Las dimensiones incluyen múltiples jerarquías y niveles. Las medidas pueden ser primitivas, es decir, enlazadas a columnas individuales de la tabla de hechos, o calculadas, es decir, derivadas de fórmulas de cálculo que se definen en el esquema. El esquema también contiene vínculos entre los elementos del modelo OLAP y las entidades del modelo físico: por ejemplo, <table> establece un vínculo entre un cubo y sus dimensiones, mientras que los atributos primaryKey y foreignKey hacen referencia a las restricciones de integridad del esquema en estrella.

.. nota::
**Mondrian**

```
     For a detailed explanation of Mondrian schemas, please refer to the documentation available at the official project webpage: http://mondrian.pentaho.com/.
     
     
```

Configuración del catálogo de motores
\+++++++++++++++++++++++++++++++

Para hacer referencia a un cubo OLAP, primero inserte el esquema Mondrian correspondiente en el catálogo de esquemas administrados por el motor. Para hacer esto, vaya a **Catálogos> catálogo de esquemas de Mondrian**. Aquí puede definir el nuevo esquema cargando su archivo de esquema XML y eligiendo **Nombre** y **Descripción**. Al crear una nueva plantilla OLAP, elegirá entre los cubos disponibles definidos en los esquemas registrados.

Tenga en cuenta que la opción Bloquear prohíbe a otros usuarios técnicos modificar la configuración.

Creación de plantillas OLAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez que se ha creado el cubo, debe crear una plantilla que asigne el cubo al documento analítico. Para lograr este objetivo, el usuario debe editar manualmente la plantilla. La plantilla es un archivo XML que le dice al motor OLAP de Knowage cómo navegar por el cubo OLAP y tiene una estructura como la representada en el siguiente código:

.. \_mappingtemplateexample:
.. code-block:: xml
:linenos:
:caption: Ejemplo de plantilla de asignación

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
                                      
     </olap>                                                  

A continuación se explican las diferentes secciones del ejemplo de plantilla de asignación.

*   La sección CUBE establece el esquema de Mondrian. Debe hacer referencia al nombre exacto del esquema, tal como se registra en el catálogo en el servidor.
*   La sección MDXMondrianQuery contiene la consulta MDX original que define la vista inicial (columnas y filas) del documento OLAP.
*   La sección MDX contiene una variación de la consulta MDX original, tal como la utiliza el motor de Knowage. Esta versión incluye parámetros (si los hay). El nombre del parámetro permitirá a Knowage vincular el controlador analítico asociado al documento a través del parámetro (en el servidor).
*   La sección TOOLBAR se utiliza para configurar las opciones de visibilidad de la barra de herramientas en el documento OLAP. El significado exacto y las funcionalidades de cada botón de la barra de herramientas se explican en las siguientes secciones. Una lista más completa de las opciones disponibles se muestra en Opciones configurables del menú:

.. code-block:: xml
:linenos:
:caption: Opciones configurables del menú

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

Creación del documento analítico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez que tenga la plantilla lista, puede crear el documento OLAP en Knowage Server.

Para crear un nuevo documento OLAP, haga clic en el botón "crear un nuevo documento" en el **Desarrollo de documentos** y seleccione **Procesamiento analítico en línea** como Tipo. Luego puede elegir los motores disponibles. En este caso solo tenemos el **Motor OLAP**.

Escriba un nombre, una funcionalidad, cargue la plantilla XML y guárdela. Verá el documento en la funcionalidad (carpeta) que seleccionó, que se muestra con el típico icono de cubo como se muestra a continuación.

.. \_olapdocserver:
.. figura:: media/image195.png

    OLAP document on server.

Diseñador OLAP\*

```

Knowage Server is also endowed of an efficient OLAP designer which avoid the user to edit manually the XML-based template that we discussed on in Development of an OLAP document. We will therefore describe here all features of this functionality. 

The user needs to have a functioning Modrian schema to start the work with. Select **Mondrian Schemas Catalog** to check the available Mondrian schemas on server. It is mandatory that the chosen Mondrian schema has no parameters applied.

.. warning::
      **Mondrian schema for OLAP designer**
         
         The Mondrian schema must not be filtered thorough any parameter or profile attribute.

The page as the one in figure below will open.

.. figure:: media/image196.png

    Schema Mondrian from catalog.

Then we start entering the **Document Browser** and clicking on the “Plus” icon at the top right corner of the page. Fill in the mandatory boxes as Label and Name of the document, select the On-line Analytica Process Type of document and the What-if Engine (we stress that the What-if engine is available only for who have purchased the Knowage SI package). Remember to save to move to the next step: open the Template Build. The latter can be opend clicking on the editor icon |image195| and it is available at the bottom of the document detail page.

.. |image195| image:: media/image197.png
   :width: 30

The action opens a first page asking for the kind of template. Here we choose the Mondrian one. Consequently you will be asked to choose the Mondrian Schema and after that to select a cube. Next figure sums up these three steps. Following the example just given below you will enter a page like that of the second figure below. 

.. _olapcoreconfig:
.. figure:: media/image198.png

    OLAP core configuration.

.. _definingolaptempl:
.. figure:: media/image199.png

    Defining OLAP template.

Once entered the page the user can freely set the fields as filter panels or as filter cards, according to requirements. Refer to *Functionalities* Chapter to review the terminology. Make your selection and you can already save the template as shown below.  

.. _definingolaptempl2:
.. figure:: media/image200.png

    Defining OLAP template.

You can notice that the side panel contains some features (see next figure):

.. _sidepanelfeatolapdes:
.. figure:: media/image201.png

    Side panel features for the OLAP Designer.

- |image200| to set the drill on Position, Member or Replace;

.. |image200| image:: media/image202.png
   :width: 30

- |image201| to configure the scenario; 

.. |image201| image:: media/image203.png
   :width: 30

- |image202| to define the cross navigation;

.. |image202| image:: media/image204.png
   :width: 30

- |image203| to configure buttons visibility.

.. |image203| image:: media/image205.png
   :width: 30

Refer to Section *Functionalities* to recall the action of the different drills. To select between them will affect the navigation of the OLAP outputs by users. Instead the scenario is used to allow the end-user to edit or not the records contained in the OLAP table. The user is first asked to select the cube in order to get the measures that the admin lets the end-user the permission to edit and modify. Referring to to the following figure, an admin user must simply check the measures using the wizard. At the bottom of the page there is also the possibility to add a parameter that can be used by the end-user when editing the measure, for example if one has a frequent multiplication factor that changes accordingly to the user’s needs, the end-user can use that factor to edit measures and ask the admin to update it periodically.

.. _wizconfigscena:
.. figure:: media/image20607.png

    Wizard to configure the scenario.

Once one cross navigation has been set you keep on adding as many as required. Just open the wizard and click on the “Add” button at the top right corner.

Note that the parameter name will be used to configure the (external) cross navigation. In fact, to properly set the cross navigation the the user must access the “Cross Navigation Definition” functionalities available in Knowage Server. Here, referring to *Cross Navigation* section of *Analytical document* chapter, you will use the parameter just set as output parameter.

.. figure:: media/image2080910.png

    Cross navigation definition.

As shown in figure below, the buttons visibility serves to decide which permissions are granted to the end-user. Some features can only be let visible while the admin can also grant the selection for others. 

.. figure:: media/image211.png

    Wizard to configure the scenario.

Once the configuration is done click on the **Save template** button and on the **Close designer** button to exit template. As :numref:`sidepanelfeatolapdes` highlights, these two buttons are available at the bottom of the side panel.

The admin can develop the OLAP document using also the OLAP engine. In this case the OLAP designer will lack of the scenario configuration since in this case the end-user must not have the grants for editing the records. So in this instance the “Configure scenario” button is not available at all. For the other two options the instructions are right the same as the What-if engine.


Profiled access
^^^^^^^^^^^^^^^^^^^^^^

As for any other analytical document, Knowage provides filtered access to data via its behavioural model. The behavioural model is a very important concept in Knowage. For a full understanding of its meaning and functionalities, please refer to Behavioural Model.

Knowage offers the possibility to regulate data visibility based on user profiles. Data visibility can be profiled at the level of the OLAP cube, namely the cube itself is filtered and all queries over that cube share the same data visibility criteria.

To set the filter, which is based on the attribute (or attributes) in the user’s profile, the tecnical user has to type the Mondrian schema. We report Cube level profilation example as a reference guide. Note that data profiling is performed on the cube directly since the filter acts on the data retrieval logics of the Mondrian Server. So the user can only see the data that have been got back by the server according to the filter.


.. code-block:: xml
   :linenos:
   :caption: Cube level profilation example.
    
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

In the above example, the filter is implemented within the SQL query that defines the dimension using the usual syntax “pr.product_family = '${family}'”.                         

The value of the “family” user profile attribute will replace the ${family} placeholder in the dimension definition.

You can filter more than one dimensions/cubes and use more profile attributes. The engine substitutes into the query the exact value of the attribute; in case of a multi value attribute to insert in an SQL-IN clause you will have to give the attribute a value like ’value1’, ’value2’, and insert into the query a condition like “and pc.product_family IN (${family})”.

Once the OLAP document has been created using the template designer the user can insert parameters to profile the document. To set parameters the user has to download the Mondrian schema and edit it; modify the dimension(s) (that will update according to the value parameter(s)) inserting an SQL query which presents the parametric filtering clause.

.. hint::
    **Filter through the interface**

       Note that for the OLAP instance, it has not proper sense to talk about “general” parameters. In this case we only deal with             profile attributes while all the filtering issue is performed through the interface, using the filter panel.

Cross Navigation
```

La navegación cruzada debe implementarse a nivel de plantilla, pero también a nivel de documento analítico. Este último ya ha sido descrito salvajemente en Cross Navigation. A continuación veremos el primer caso. Observe que ambos procedimientos son obligatorios.

Para los documentos OLAP es posible habilitar la navegación cruzada en miembros o en celdas y daremos más detalles sobre estos dos casos a continuación.

En términos generales, el usuario debe modificar el archivo de plantilla para configurar la navegación cruzada con el fin de eliminar los parámetros de salida del documento. Recordamos que la definición de los parámetros de salida se discute en *Navegación cruzada* sección de *Documento analítico* capítulo de este manual.

Navegación cruzada en miembros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activar la navegación cruzada en un miembro significa que el usuario puede hacer clic en un miembro de una dimensión que se va a enviar y visualizar un documento de destino. El primer tipo de navegación se puede establecer editando la plantilla de consulta OLAP. En el primer caso, debe agregar una sección llamada "clicable" dentro de la etiqueta de consulta MDX. En realidad

*   el valor del atributo es igual al nivel jerárquico que contiene los miembros en los que se podrá hacer clic;
*   el elemento representa el parámetro que se pasará al documento de destino. El atributo name es el URI del parámetro que se pasará al documento de destino. El valor 0 representa el miembro seleccionado actualmente, como una convención: este valor se asignará al parámetro cuyo URI es null.

La siguiente figura da un ejemplo. Tenga en cuenta que puede reconocer que la navegación cruzada se activa cuando los elementos se muestran resaltados y subrayados en azul.

.. figura:: media/image212.png

    Cross navigation on member.

Si abre el archivo de plantilla, leerá instrucciones similares a las que se informan en Sintaxis utilizada para establecer la navegación cruzada.

.. code-block:: xml
:linenos:
:caption: Sintaxis utilizada para establecer la navegación cruzada.

     <MDXquery> 
       select {[Measures].[Unit Sales]} ON COLUMNS,               
       {([Region].[All Regions], [Product].[All Products])} ON ROWS from     
       [Sales_V]                                                             
       <clickable uniqueName="[Product].[Product Family]" >                  
          <clickParameter name="family" value="{0}"/>                           
       </clickable>                                                          
     </MDXquery>                                                           

Navegación cruzada desde una celda de la tabla dinámica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este caso es similar al taladro de una dimensión, excepto que en este caso los valores de todas las dimensiones se pueden pasar al documento de destino. En otras palabras, se puede pasar todo el contexto dimensional de una célula. Ahora supongamos que el usuario desea hacer clic en una celda y pasar al documento de destino el valor de la familia de niveles de dimensión del producto y dimensión del año de tiempo. Debe crear dos parámetros, uno para la familia donde la dimensión es el producto, la jerarquía es el producto, el nivel es la familia del producto y otro para el parámetro del año donde la dimensión en el tipo, la jerarquía es el tiempo y el nivel es el año. Veamos lo que sucede cuando el usuario hace clic en una celda. Dependiendo de la celda seleccionada, la familia de controladores analíticos del documento de destino tendrá un valor diferente: será el nombre del miembro de contexto (de la celda seleccionada) de la dimensión "Producto", es decir, la jerarquía \[Producto], en \[Producto]. Nivel \[ProductFamily]. Consulte la siguiente tabla para ver algunos ejemplos:

.. tabla:: Miembro de contexto en la dimensión del producto
:widths: automático

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

Echemos un vistazo a la plantilla. La sintaxis utilizada para establecer la navegación cruzada muestra cómo usar la etiqueta de navegación cruzada:

.. code-block:: xml
:linenos:
:caption: Sintaxis utilizada para establecer la navegación cruzada.

        <CROSS_NAVIGATION>                                                    
            <PARAMETERS>                                                       
                <PARAMETER name="family" dimension="Product" hierarchy="[Product]" level="[Product].[Product Family]" /> 
                <PARAMETER name="year" dimension="Time" hierarchy="[Time]" level="[Time].[Year]" />
            </PARAMETERS>                                                      
        </CROSS_NAVIGATION>                                                   

Una flecha verde será visible en la barra de herramientas para mostrar que la navegación cruzada está habilitada. Cuando el usuario hace clic en ese icono en cada celda, se mostrará una flecha verde en cada celda. El usuario puede hacer clic en ese icono para iniciar la navegación cruzada desde una celda.
