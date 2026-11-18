# Análisis hipotético

El **¿Qué pasaría si** El análisis es la capacidad de hacer hipótesis y ver cómo estos impactan en el negocio. En la práctica, el usuario puede realizar un análisis hipotético utilizando una extensión de la herramienta OLAP. El proceso de What-if se compone en tres fases:

*   preparación de datos,
*   definición de flujo de trabajo,
*   definición de hipótesis.

Comenzamos entonces a centrarnos en esta última fase.

## Detalles de la interfaz

El flujo de trabajo tiene un impacto en la visualización de datos. Un usuario puede comprender el estado del flujo de trabajo mirando la sección Qué pasaría si de la barra lateral. Hay tres posibilidades descritas a continuación.

*   El usuario puede realizar el análisis What-if: en este caso la sección What-If contiene los botones para editar valores; vea la figura a continuación para
    marque esos botones.

.. figura:: media/image213.png

      What-If buttons inside the sidebar.

*   El esquema está bloqueado por otro usuario. En este caso, aparece un mensaje con el nombre del usuario activo en el flujo de trabajo como se muestra a continuación.

.. figura:: media/image214.png

     The What-If is used by another user.

*   El flujo de trabajo ha finalizado.

.. figura:: media/image215.png

      The What-If is finished.

Recordamos brevemente la funcionalidad de los botones principales:

*   Modelo de desbloqueo: cambia el estado del flujo de trabajo para mover el control al siguiente usuario.
*   Guardar: persiste la modificación en la base de datos.
*   Guardar como nueva versión: persiste la modificación en la base de datos en una nueva versión.
*   Deshacer: deshace la última modificación.
*   Eliminar versiones: abre un asistente que el usuario puede usar para eliminar versiones.
*   Asistente de salida: permite al usuario exportar el cubo de edición en dos formatos diferentes, tabla y csv en el específico.

## Descripción del metalenguaje

Vimos que el motor What-If permite al usuario final cambiar los valores de los datos. Aquí vemos cómo es posible modificar un valor de celda a través de una fórmula, incondicionalmente a partir del nivel de agregación de la celda. La fórmula debe escribirse utilizando un lenguaje particular llamado **meta-lenguaje** que se describe a continuación. En primer lugar, los símbolos aritméticos disponibles son: + - :sub:`\*` / ( ) %.

El cálculo 100 + 10% es un ejemplo simple de uso de la operación %. Tenga en cuenta que la fórmula puede comenzar con "=", pero esto no es obligatorio.

Para activar la edición de una celda de medida que no se muestra en el OLAP primero debe hacer clic en el icono de filtro de la tarjeta de filtro de medida y verificar la medida de destino. A continuación, seleccione la versión que desea utilizar y cambie los valores de la figura a continuación muestra dónde están disponibles estos objetos en la interfaz.

.. figura:: media/image21616.png

    Checking measures and selecting version.

Luego haga doble clic en la celda de medida de destino y aparecerá un cuadro que le permitirá insertar una fórmula. Escriba la sintaxis de cálculo y haga clic en el botón *f*\ (*x*) para convalidarlo o cancelarlo, como se muestra a continuación.

.. figura:: media/image21819.png

    Inserting formula and its convalidation.

Destacamos que también se puede hacer referencia a miembros que no están incluidos en la tupla representada por la celda que se va a modificar. Veamos algunos ejemplos. Por ejemplo, supongamos que la celda se refiere a la siguiente tupla informada en el código siguiente:

.. code-block:: xml
:linenos:
:caption: Producto.Deli

         [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],
         [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]

Puede referirse a la tupla en el siguiente código con solo Product.Eggs y al mismo tiempo a la tupla en el segundo código a continuación con solo Product.Eggs; Medidas.Ventas de unidades

.. \_producteggs:
.. code-block:: xml
:linenos:
:caption: Producto.Huevos

            [Measures].[Store Sales], [Product].[Food].[Eggs], [Version].[0],
            [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]

.. code-block:: xml
:linenos:
:caption: Producto.Huevos; Medidas.Ventas de unidades

            [Measures].[Unit Sales], [Product].[Food].[Eggs], [Version].[0],
            [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]

Tenga en cuenta que si crea una fórmula en una celda y desea moverla a lo largo de una dimensión (por ejemplo, la celda hace referencia al miembro Time.2016 y desea obtener un valor para Time.2017), debe hacer referencia a un miembro del mismo nivel. Así, por ejemplo, puede obtener el valor de la celda para Time.2017, pero no para Time.2017.May.

La sintaxis es como la que se muestra en Referencia a diferentes miembros o, en caso de que esté utilizando otra jerarquía, como en el segundo código a continuación donde puede concatenar diferentes miembros con ";".

.. code-block:: xml
:linenos:
:caption: Refiriéndose a diferentes miembros.

            <dimension's name>.<member's name>or[<dimension's name>].[<member's name>]

.. \_referringdiffmembers:
.. code-block:: xml
:linenos:
:caption: Se refiere a diferentes miembros de otra jerarquía.

            <dimension's name>.<hierarchy's name>.<member's name>or[<dimension's name>].[< hierarchy's name>].[<member's name>]

También puede referirse a miembros que están en el mismo nivel pero que no son miembros hermanos:
supongamos que, por ejemplo, la tupla de la celda es como en el código siguiente:

.. code-block:: xml
:linenos:
:caption: Ejemplo de tupla de celda.

            [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],
            [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]

Tenga en cuenta que puede consultar la tupla

.. code-block:: xml
:linenos:
:caption: Ejemplo de tupla de celda.

            [Measures].[Store Sales], [Product].[Drink].[Alcoholic Beverages],
            [Version].[0], [Region].[Mexico Central], [Customers].[All Customers],
            [Customers].[All Customers]

solo con:

.. code-block:: xml
:linenos:
:caption: Acortar el código de sintaxis.

            [Product].[Drink.Alcoholic Beverages]

Otro ejemplo de Code a continuación

.. code-block:: xml
:linenos:
:caption: Ejemplo de tupla de celda.

          [Measures].[Store Sales], [Product].[Food].[Deli].[Meat],
          [Version].[0], [Region].[Mexico Central], [Customers].[All Customers],

al código a continuación

.. code-block:: xml
:linenos:
:caption: Ejemplo de tupla de celda.

            [Measures].[Store Sales], [Product].[Drink].[Alcoholic Beverages].[Beer and Wine], [Version].[0],
            [Region].[Mexico Central], [Customers].[AllCustomers], [Customers].[All Customers]

es como en el código siguiente

.. code-block:: xml
:linenos:
:caption: Expresión usada.

            [Product].[Drink.Alcoholic Beverages.Beer and Wine]

Tenga en cuenta que la última parte de la expresión es la parte de la ruta de acceso al miembro de destino que difiere de la ruta de acceso del miembro de la celda. Algunos otros ejemplos:

.. code-block:: xml
:linenos:
:caption: Otro ejemplo.

            [Product].[Food]

## Implementación de análisis hipotéticos

En este capítulo trataremos algunas características técnicas del análisis What-If que solo pueden ser manejadas por usuarios expertos.

Descripción del flujo de trabajo\*

```

When you perform a what-if analysis the schema is shared in order to be used as a data source. Therefore each time a document linked to a schema can be edited only by one user per time. This behaviour is managed by the Workflow of the schema. The administrator can configure a workflow opening the details of the model in OLAP schema catalogue, selecting the schema and going on the workflow tab available on the top of the right sided area. The tab is red circled below.

.. figure:: media/image220.png

    Workflow tab.

Referring to the next figure, the interface for the definition of the workflow is composed of a double list where

-  the **available users** area contains all the users,
-  the **workflow** area contains the sequence of users for the workflow.

.. _workflowtabinterf:
.. figure:: media/image221.png

     Workflow tab interface.

When an administrator clicks on the user in the list “available users” the user will be added in the workflow as shown in Figure 10.3.

Administrator can move the users in the sequence or remove them clicking on the “action buttons”. When the workflow is defined, the administrator can start it clicking on the button start. To start a workflow means to enable the first user of the sequence to apply the what-if on that schema. When a workflow is started it can not be edited by anyone else and an icon appears in the row of actual active user so that the administrators can monitor the state of the schema. An example is provided by Figure 10.4

Schema definition\*
```

Como dijimos anteriormente, el análisis What-If requiere alguna modificación en la base de datos. El primer paso es crear una nueva tabla en la base de datos para almacenar la versión con nombre de los datos modificados. A continuación, el usuario cambiará los valores del cubo; a continuación, es obligatorio crear una nueva tabla con una estructura similar al cubo analizado y una nueva tabla (wbversion) que contendrá el control de versiones de las definiciones establecidas en el análisis.

Por lo tanto, la estructura de la nueva tabla de hechos debe contener:

*   todas las claves externas de las cotas (todas las visibles en el cubo),

.. figura:: media/image222.png

       Selecting users for workflows.

.. figura:: media/image223.png

       Selecting users for workflows.

*   todas las medidas editables,
*   una nueva columna numérica que es una clave externa que hace referencia a la tabla de versiones.

En la figura siguiente, hay un ejemplo en el que se sales_fact\_1998 el cubo y se sales_fact\_1998\_virtual la nueva tabla.

.. figura:: media/image224.png

      Cube and new virtual table example.

La tabla sales_fact\_1998\_virtual debe inicializarse con los mismos datos contenidos en sales_fact\_1998 más 0 que la versión; la tabla wbversion debe inicializarse con un registro con wbversion = 0 y un nombre más una descripción para los "valores originales".

Cambios en el esquema mondrian\*

```

Now you should map the new tables in the mondrian schema. In order to merge the fact table and the table with the editable measure we create a virtual cube. A virtual cube is a special cube where the values are the result of the join of other cubes. In our case the join keys are the dimensions. The actions to be performed in the mondrian schema are listed right below.

-  To create a new "Version" dimension as inChanging the Mondrian Schema.

.. code-block:: xml
   :linenos:
   :caption: Changing the Mondrian Schema.

       <Dimension name="Version">
          <Hierarchy hasAll="false" primaryKey="wbversion"
          defaultMember="[Version ].[0]" >
          <Table name="wbversion"/>
          <Level name="Version" column="wbversion" uniqueMembers="true"
          captionColumn="version_name"/>
          </Hierarchy>
       </Dimension>

-  To create the mapping of the editable cube (in our example the table sales_fact_1998_virtual) as shown in Code Creating the mapping of the editable cube.

.. code-block:: xml
   :linenos:
   :caption: Creating the mapping of the editable cube.

       <Cube name="Sales_Edit">
          <Table name="sales_fact_1998_virtual"/>
          <DimensionUsage name="Product" source="Product"
                          foreignKey="product_id" />
          <DimensionUsage name="Region" source="Region"
                          foreignKey="store_id"/>
          <DimensionUsage name="Customers" source="Customers" foreignKey="customer_id"/>
          <DimensionUsage name="Version" source="Version"
          foreignKey="wbversion"/>
          <Measure name="Store Sales" column="store_sales" aggregator="sum"
          formatString="#,###.00"/>
       </Cube>

The name of the cube ("Sales_Edit") is the value of the edit Cube attribute of the tag scenario in the template. Note that the name of the dimension Version must be exactly "Version"!!

• To create the virtual cube that will contain the mapping of the columns as in Code below.

.. code-block:: xml
   :linenos:
   :caption: Creating the virtual cube.

       <VirtualCube name="Sales_V">
          <CubeUsages>
             <CubeUsage cubeName="Sales_Edit" ignoreUnrelatedDimensions="true"/>
             <CubeUsage cubeName="Sales" ignoreUnrelatedDimensions="true"/>
          </CubeUsages>

          <VirtualCubeDimension cubeName="Sales" name="Customers"/>
          <VirtualCubeDimension cubeName="Sales" name="Product"/>
          <VirtualCubeDimension cubeName="Sales" name="Region"/>
          <VirtualCubeDimension cubeName="Sales_Edit" name="Customers"/>
          <VirtualCubeDimension cubeName="Sales_Edit" name="Product"/>
          <VirtualCubeDimension cubeName="Sales_Edit" name="Region"/>
          <VirtualCubeDimension cubeName="Sales_Edit" name="Version"/>
          <VirtualCubeMeasure cubeName="Sales" name="[Measures].[Unit Sales Original]" visible="false"/>
          <VirtualCubeMeasure cubeName="Sales" name="[Measures].[Sales Count Original]" visible="false"/>
          <VirtualCubeMeasure cubeName="Sales_Edit" name="[Measures].[Store Sales]" visible="true"/>
          <VirtualCubeMeasure cubeName="Sales_Edit" name="[Measures].[Store Cost]" visible="true"/>

          <CalculatedMember name="Sales Count" dimension="Measures">
             <Formula>VALIDMEASURE([Measures].[Sales Count Original])</Formula>
          </CalculatedMember>

          <CalculatedMember name="Unit Sales" dimension="Measures">
             <Formula>VALIDMEASURE([Measures].[Unit Sales Original])</Formula>
          </CalculatedMember>
       </VirtualCube>

Specifically, in the virtual cube you should specify:

- the list of cubes to be joined (CubeUsages);
- the list of the dimensions of the cube (as you can see it contains all the common dimensions, plus the Version that belongs only to the editable cube);
- the list of the measures. You can perceive that there is a calculated member for the measure Sales Count Original (Sales Count Original is the name of a measure in the Sales cube). This is a trick for the not editable measures. This type of measure lives only in the DWH cube and not in the editable cube. This is due to the fact that the engine doesnt know how to give a value for these measures for the different values of the Version dimension (remember that only the editable cube has the Version dimension). The calculated field solve this problem propagating the same version of the not editable (and versionable) measure for all the version.

Now all the MDX queries can be performed in the virtual cube.
```
