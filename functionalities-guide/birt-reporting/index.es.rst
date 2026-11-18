# Informes BIRT

Los informes representan el tipo más popular de análisis de negocios. De hecho, permiten la visualización de datos de forma estructurada y en consecuencia con formatos predefinidos. Las principales características de un informe son:

*   combinación de datos numéricos (tablas, listas, tablas cruzadas), gráficos e imágenes;
*   diseño estático y perfecto para píxeles;
*   salida multipágina y multiformato (PDF, HTML, DOC, etc.);
*   organización de los datos por grupos y secciones;
*   uso universal (resumen, detalle, analítico u operativo);
*   ser adecuado para la producción y distribución fuera de línea (ejecución programada);
*   facilidad de uso.

Por estas razones, los informes suelen tener un nivel generalizado de uso: son utilizados por los desarrolladores para realizar análisis sintéticos y detallados, teniendo un nivel de dificultad particularmente bajo.

BIRT, acrónimo de Business Intelligence and Reporting Tools, es una plataforma tecnológica de código abierto utilizada para crear visualizaciones e informes de datos. En la siguiente figura puede ver un ejemplo de informe BIRT.

.. figura:: media/image327.png

    Example of a BIRT report.

Knowage Studio contiene birt designer, mientras que Knowage Server contiene el motor de tiempo de ejecución. Una plantilla BIRT consiste en un archivo de texto XML con la extensión .rptdesign que es generada automáticamente por la plataforma Eclipse incrustada en Knowage Studio. Puede ser modificado manualmente por usuarios muy expertos aunque no sea una práctica recomendada. En este manual entraremos en detalles sobre cómo desarrollar un informe BIRT, desde su implementación dentro del Knowage Studio hasta su visualización dentro del Knowage Server. Todas las funcionalidades estándar de BIRT están disponibles en Studio, pero para obtener una visión general completa de las herramientas de informes de BIRT y una guía detallada para desarrolladores, el lector también puede consultar la documentación oficial en `<http://www.eclipse.org/birt>`\_

## Introducción a Knowage Studio

Knowage Studio es el entorno de desarrollo basado en Eclipse. Permite al desarrollador diseñar y modificar algunos documentos analíticos, por ejemplo, informes y cuadros de mando. Este módulo apoya al desarrollador en el diseño de documentos, así como durante los procesos de instalación y prueba, directamente en Knowage Server. La interacción entre estos dos componentes es posible gracias al módulo Knowage SDK. Los usuarios pueden mostrar la lista de documentos analíticos que están disponibles en el servidor y descargarlos, con el fin de modificarlos en su propio ordenador.

Permite construir un proyecto de Knowage dentro de Eclipse, a través del cual los usuarios pueden crear nuevos documentos analíticos. También integra las herramientas necesarias para crear informes Jasper y BIRT.

Para instalar Knowage Studio, primero compruebe que su entorno cumple los siguientes requisitos previos:

*   tiene un JDK 1.7.x ya instalado;
*   tiene la variable JAVA_HOME ya establecida;
*   tiene un sistema operativo certificado (Windows, Linux, Unix son generalmente aceptados). La lista de entornos certificados depende principalmente de los soportados por Eclipse. Consulte las notas de la versión de Knowage Studio para averiguar la versión de Eclipse incluida en cada paquete publicado.

Si es así, el segundo paso es descargar el paquete adecuado desde su área personal en el sitio web de Knowage.

En este punto, solo tienes que descomprimir el paquete descargado bajo una carpeta, teniendo un KnowageStudio\_<version>*<distribution>*<date> subcarpeta. Aquí puedes encontrar y ejecutar un **KnowageStudio.exe** o **Knowage.sh** para iniciar y seleccionar el espacio de trabajo preferido.

El espacio de trabajo seleccionado funciona como un repositorio local para todos los objetos desarrollados (informes, gráficos, cabinas, etc.). Sin embargo, los documentos no son visibles ni reutilizables por otros usuarios hasta que se publican en Knowage Server.

.. advertencia::

    **Connection between Server and Studio**

       Once Knowage Studio has been configured, connect it to Knowage Server. This will be the deployment environment to provide                end-users with all certified objects. The main steps to set the connection are:

       -  select the Knowage perspective;
       -  create a Knowage project;
       -  set Knowage Server connections.

       These points will be described in the following.

En la primera ejecución de Knowage Studio, aparece una página de bienvenida.

El primer paso es crear un proyecto de Knowage seleccionando el icono de Knowage de la siguiente figura en la barra de herramientas ubicada en la parte superior de la página.

.. figura:: media/image328.png

    New Knowage project icon.

Una vez creado el proyecto, aparece un árbol de carpetas estándar. Las carpetas predefinidas son:

*   **Análisis de Negocio:** contiene todos los documentos desarrollados (informes, gráficos, cabinas, etc.) que se pueden cargar o descargar desde Knowage Server. Esta carpeta se puede estructurar con subcarpetas, para organizar libremente los propios documentos;
*   **Carpetas privadas:** contienen la documentación personal o del proyecto de los usuarios. Esta carpeta puede ser administrada libremente por el usuario;
*   **Recursos:** contienen todos los recursos técnicos utilizados en el proyecto (es decir, la referencia a un Servidor Knowage).

Ahora puede configurar referencias a uno o más servidores de Knowage. En otras palabras, cada usuario puede trabajar para muchos proyectos que pueden ser:

*   alojado en diferentes servidores
*   alojado en el mismo servidor con diferentes cuentas de usuario.

Para definir una conexión de servidor, haga clic en el botón **Nuevo servidor** punto de la **Servidor** menú contextual.

.. figura:: media/image329.png

    New Data Source connection.

Un formulario le pedirá:

*   **Nombre del servidor:** un nombre lógico para identificar el servidor. El nombre se usa solo en el espacio de trabajo local y no tiene relación con el físico.
*   **URL:** la url http donde el servidor está alojado y accesible.
*   **Usuario:** el usuario que se autentica en Knowage Server, estableciendo sus derechos de acceso en términos de qué tipo de operaciones puede hacer (cargar y descargar un modelo o un conjunto de datos) y a qué partes del repositorio del servidor puede acceder.
*   **Contraseña:** la contraseña de los usuarios.
*   **Activo:** un indicador que indica el servidor activo. Es particularmente útil cuando el usuario está trabajando con varios servidores. El servidor activo indica que cada operación de carga y descarga hace referencia a esta instancia de Knowage Server.

.. figura:: media/image330.png

    Server configuration wizard.

.. advertencia::

    **Connection to Knowage Server**

       If something in your network configuration has been changed from your first run of Knowage Studio, the connection test of                Knowage Studio to the Server could fail. Most often this problem is due to the proxy settings in your Eclipse environment. If            this is not the case, try to run Knowage Studio from the command line with the clean option (**Knowage.exe** clean) to reset            working settings.

¡En este punto, Knowage Studio está listo para trabajar!

Definición de metadatos

```

Each Knowage document (e.g., report, olap, chart, cockpit, etc.), has its own technical metadata stored in Knowage internal repository. The most relevant technical metadata describing document structure, content and behaviour are:

-  *Template*, which defines the document layout;
-  *Data set*, which defines how data of each document should be read;
-  *Analytical drivers*, which hook the template parameters to the graphical interface (at runtime), managing also the right form for       parameters.

Knowage Studio supports BI developers steering the implementation of the template for each analytical document through an easy graphical interface and simple wizards. Each document type has its own designer and manages the relation with data sources and data sets. Furthermore it enhances technical users with all the needed functionalities to design, develop, test, deploy and maintain Knowage analytical documents. As said above, each document is mainly associated to a template describing its layout and a data set defining how data will fill it. Knowage Studio assists the developer in writing these templates and/or data sets by means of a graphical user interface and of easy-to-use wizards. 

.. warning::
     **Datasets created with the Business Model**

       These data sets are often based on specific business models created through Knowage Meta. By the way, we will concentrate on how        to manage the implementation of a data set using the BIRT Report designer available in Knowage

We want to remark that an expert developer can work directly on the server, managing documents and data sets by hand, thanks to the web  interface for administrators and developers. Usually, this procedure is faster when only small changes are required on already released  documents, whereas the Studio is particularly useful when a developer works on new documents.

The target users of the Studio module are:

-  BI developers, who define analytical documents and data sets to be released onto a remote Knowage Server
-  administrators, who define or update analytical documents and data sets.

In other words, Knowage Studio covers the development processes of more technical documents. On the other hand, high-level documents are created directly through Knowage Server, where a power user can access graphical designers without need to use the Studio, which requires more technical skills to manage the installation and configuration process.

Data set definition
```

Cada tipo de documento tiene su propia forma de definir cómo obtener datos de un origen de datos interno, de acuerdo con una definición de conjunto de datos. Esto permite que el documento acceda directamente al RDBMS, a través del script de carga SQL, que se puede codificar dentro de la plantilla o externamente (es decir, almacenado como recurso de Knowage Server), pero sin ninguna abstracción de las fuentes de datos.

## Desarrollo de un informe BIRT

Para crear un nuevo documento, haga clic con el botón derecho en el botón **Análisis de Negocio** y, para comenzar, elija entre informe y panel. En la siguiente figura elegiremos **Informe con Birt** y dejar la otra opción para el siguiente capítulo.

.. figura:: media/image331.png

    New document creation.

Una vez que se diseña el documento, se almacena como un archivo local, marcado con un icono y una extensión de archivo específica:

*   **.sbidoccomp:** plantillas de documento para el panel que utilizan el motor ComposedDocument;
*   **.rptdesign:** plantilla de documento para informes que utilizan el motor BIRT.

En nuestro caso, obtendremos un archivo .rptdesign. Un doble clic en uno de estos archivos permite abrir la plantilla de documento, con su editor gráfico relacionado.

El diseño y la implementación de un informe BIRT incluye los siguientes pasos:

*   crear el documento vacío;
*   cambiar a la perspectiva del diseñador de informes;
*   crear el origen de datos;
*   crear el conjunto de datos;
*   diseñar el informe a través de la interfaz gráfica;
*   implementar el informe en el servidor.

Para crear un nuevo informe BIRT, como se acaba de anticipar, haga clic con el botón derecho en el botón **Análisis de Negocio** y seleccione **Informe** > **Informe con BIRT**. Esto abrirá un editor donde puede elegir el nombre de su documento. El nuevo documento se creará bajo el **Análisis de Negocio** carpeta.

Haga doble clic en él para abrir el editor. En este punto, todavía estás trabajando en la perspectiva del Knowage. Para diseñar el informe, cambie a la perspectiva real del diseñador BIRT. Haga clic en el icono de perspectiva del editor de Eclipse y seleccione el Diseñador de informes entre las perspectivas disponibles, como se muestra en la figura a continuación.

.. figura:: media/image332.png

    Change perspective.

Los siguientes pasos son la creación de una fuente de datos y de un conjunto de datos. Como se describió anteriormente en la sección Definición de conjunto de datos, Knowage Studio permite el desarrollo de documentos analíticos utilizando conjuntos de datos internos o externos. En este ejemplo específico, mostraremos cómo crear un informe con un conjunto de datos interno. En primer lugar, en el caso de un conjunto de datos interno, defina un **Origen de datos JDBC**.

Haga clic derecho en el botón derecho **Origen de datos** y seleccione el origen de datos correspondiente. Se abrirá un editor emergente que le indicará la configuración de conexión:

*   **Clase de conductor**
*   **URL de la base de datos**
*   **Nombre de usuario** y **contraseña**

Tenga en cuenta que el Studio utilizará estos parámetros de configuración para conectarse a la base de datos y permitir que el informe se ejecute localmente (es decir, dentro del Studio). Asegúrese de que la base de datos establecida en el servidor comparte el mismo esquema del definido en el estudio.

Dado que está estableciendo una referencia local a una base de datos dentro del informe, recuerde establecer una información adicional: esto permitirá a Knowage Server ejecutar correctamente el informe, conectándose al origen de datos al que se hace referencia dentro del servidor y no dentro del informe. Básicamente, debe decirle al servidor que invalide la configuración de la fuente de datos. Por lo tanto, agregue un parámetro al informe, llamado connectionName, haga clic con el botón derecho en el elemento de menú "Parámetros del informe" y seleccione "Nuevo parámetro". Rellene el formulario como se sugiere a continuación.

.. figura:: media/image333.png

    Adding connectionName Parameter.

Luego vaya a **Enlace de propiedades** en el editor de orígenes de datos y establezca la propiedad JNDI URL en el valor del parámetro connectionName, como se muestra a continuación.

.. figura:: media/image334.png

    Setting the connectionName parameter in the Data Source editor 

.. advertencia::

    **JNDI URL**

      Do not forget to define the connectionName parameter in your BIRT report and set the JNDI URL accordingly. Without these                 settings your BIRT report may be unable to access data once it is deployed on the server. In addition, if database and connection       properties change, you need to change the connection properties only in Knowage server.

Una vez configurado el origen de datos, puede continuar con la creación de un conjunto de datos. Por lo tanto, haga clic con el botón derecho en el botón **Conjunto de datos** y seleccione **Nuevo conjunto de datos**. En la siguiente ventana, seleccione el origen de datos, el tipo de consulta y asigne un nombre al conjunto de datos, como se muestra a continuación. El ámbito de este nombre se limita al informe, ya que estamos definiendo un conjunto de datos interno.

.. figura:: media/image335.png

    Dataset definition.

Ahora puede definir su conjunto de datos escribiendo la consulta SQL en el editor y probando los resultados (consulte :numref:`datasetedtwithprw`). En cualquier momento, puede modificar el conjunto de datos haciendo clic en él, lo que volverá a abrir el editor de consultas.

Diseñemos un informe muy simple, que contenga una tabla que muestre los datos del conjunto de datos definido. La forma más fácil de crear una tabla a partir de un conjunto de datos es arrastrar y soltar el conjunto de datos desde el menú del árbol en el área del editor.

La forma más genérica, que se aplica a todos los elementos gráficos, consiste en cambiar a la **Paleta** en el panel izquierdo, manteniendo al diseñador en el panel central. Arrastre y suelte la tabla en el área del editor. Tenga en cuenta que esto se puede hacer con todos los demás elementos enumerados en la paleta. En este punto, puede editar la tabla (así como cualquier otro elemento gráfico del informe) utilizando el **Editor de propiedades** debajo del área del editor.

Al desarrollar un informe, es particularmente útil probarlo regularmente. Para ello, haga clic en el botón **Vista previa** debajo del área del editor. Para volver al editor, simplemente haga clic en el botón **Diseño** pestaña. En **Página maestra** , puede establecer las dimensiones y el diseño del informe; el **Guión** tab admite funcionalidades avanzadas de scripting; por último, el **Origen XML** muestra el código fuente editable del informe.

Al desarrollar un informe, es particularmente útil probarlo regularmente. Con este fin, haga clic en la pestaña Vista previa debajo del área del editor. Para volver al editor, simplemente haga clic en la pestaña Diseño. En la pestaña Página maestra, puede establecer las dimensiones y el diseño del informe; la ficha Script admite funcionalidades avanzadas de scripting; por último, la ficha Origen XML muestra el código fuente editable del informe.

.. \_datasetedtwithprw:
.. figura:: media/image336.png

    Dataset editor, with preview.

.. figura:: media/image337.png

    BIRT Property Editor.

Una vez finalizado el informe, puede implementarlo en Knowage Server.

.. nota::
**Implementación en Knowage Server**

         Please refer to the section *Download and Deploy* in this chapter to find out more on report deployment.

El diseñador de informes BIRT permite la creación de informes complejos, con diferentes elementos gráficos como pestañas cruzadas, gráficos, imágenes y diferentes áreas de texto. En esta sección no proporcionamos ningún detalle sobre el desarrollo gráfico, pero nos centramos en aspectos específicos de Knowage BIRT Report Engine.

.. nota::
**Diseñador BIRT**

         For a detailed explanation of report design, pleas refer to BIRT documentation at www.eclipse.org/birt/.

Uso de un conjunto de datos externo

```

In the afore-described example, we built a report using an internal dataset, i.e., a dataset defined within the report. This has two main implications. First, the dataset is not visible outside the report execution: for example, it cannot be directly reused by other  reports. Second, an internal dataset is always defined as a SQL query and it cannot take advantage of Knowage business model abstraction. For these reasons, Knowage allows the definition of external datasets in reports. An external dataset is defined in Knowage Server and, as a consequence, it is visible to all documents on the server (i.e., it can be used by any of them, if properly linked to the document). External datasets can either be SQL datasets or QbE datasets, that is, datasets defined by queries over a business model.

An external dataset can be included into any BIRT report by downloading it from a Knowage Server. Specifically:

-  define a Knowage Server datasource;
-  download a dataset from the Knowage Server datasource.

We always start by right-clicking on the **Data Source** item. Select **Knowage Server Data Source** and set the appropriate input configuration:

-  **Server URL**
-  **Username** and **password** used to log into the Server (e.g., biadmin).

After filling in the configuration fields, test the connection and save it. The new data source will appear in the left tree menu. Instead of connecting to a database via a JDBC driver, connect to the server as the source of data. Obviously, the actual data source and dataset must have previously been defined on the Server. 

To select the dataset, click on **New Data Set** as above, but this time select the **Knowage Data Source** that you have just defined. Now, instead of choosing a new name for the dataset, insert the correct label of the dataset that you want to import from the Server. If the label is correct, the dataset will be imported in the report by clicking on **Finish**. Notice that the imported dataset may be a SQL or a QbE one. Since both types of datasets are stored in the same repository by Knowage Server, we are enabled to use any BM query in the development of a report.

.. warning::
      
    **Use of BM queries in report development.**

      The ideal use of a business model is to define queries over the BM via Knowage Meta, deploy them on Knowage Server and reuse             them on Knowage Studio as external datasets.

Adding parameters to reports
```

La mayoría de las veces los informes muestran análisis de datos que dependen de parámetros variables, como el tiempo, el lugar y el tipo. Knowage Studio permite al diseñador agregar parámetros a un informe y vincularlos a controladores analíticos definidos en Knowage Server.

Para usar estos parámetros, primero debe agregarlos a su informe. Haga clic derecho en **Parámetros del informe** en el panel de árbol y seleccione **Nuevo parámetro**. Aquí puede establecer el tipo de datos y elegir un nombre para su parámetro.

.. advertencia::

    **Parameters URI**

      Be careful when assigning a name to a parameter inside a report. This name must correspond to the parameters URI when you               deploy the document on Knowage Server.

Una vez que haya definido todos los parámetros, abra el conjunto de datos (o cree uno nuevo). Los parámetros se identifican mediante un signo de interrogación **?** . Para cada uno **?** que inserte en su consulta, debe establecer el vínculo correspondiente en el cuadro de diálogo **Parámetros** : esto permitirá la sustitución de parámetros en el momento de la ejecución del informe.

.. figura:: media/image338.png

    Creation of a new parameter in a BIRT report.

Tenga en cuenta que debe establecer un vínculo para cada signo de interrogación como se muestra a continuación, incluso si el mismo parámetro se produce varias veces en la misma consulta.

.. \_insrtprmintodtsetdef:
.. figura:: media/image339.png

    Insert parameters into the dataset definition.

.. advertencia::

     **Transfer reports from Studio to Server and vice versa**
       
       We saw that developers can use Knowage Studio deployment service to easily register the report with its template on Knowage              Server. Alternatively, any valid BIRT template (developed with or without Knowage Studio) can be directly uploaded in Knowage            Server using the web interface for document management.

Los parámetros también se pueden usar dentro de algunos elementos gráficos, como el texto dinámico, con la siguiente sintaxis:

.. code-block:: javascript
:linenos:
:caption: Sintaxis de parámetros

            params[name_of_parameter].value

## Descargar e implementar

Para modificar un documento ya implementado, primero descargue la plantilla relacionada desde el repositorio de Knowage Server.

Haga clic con el botón derecho en el botón **Análisis de Negocio** o en una de sus subcarpetas. En el menú contextual, seleccione el botón **Descargar** opción. En este punto, aparece el árbol de funcionalidades, que le permite elegir los documentos que se descargarán.

Estos documentos estarán disponibles en la carpeta local que haya seleccionado previamente. Los detalles del documento (es decir, etiqueta, descripción, estado, motor y parámetros) se almacenan como metadatos en el repositorio local. Los metadatos se pueden actualizar desde el servidor haciendo clic en el botón **Actualizar** en el botón **Conocimiento** > **Metadatos del documento** de la ficha **Propiedades** sección. Para abrir Propiedades, haga clic con el botón secundario en el elemento del documento y seleccione **Propiedades**.

De manera similar, después de una actualización del documento, la opción Implementar del mismo menú envía la nueva plantilla al servidor, lista para su uso.

Otra situación posible es cuando el diseñador crea una nueva plantilla desde cero y la implementa en el servidor. En la primera implementación, se crea un vínculo entre la plantilla y un documento en el servidor. Durará hasta que se elimine el documento en el servidor o se modifique su etiqueta. En esos casos, deberá volver a implementar la plantilla desde Studio.

Para implementar una plantilla, haga clic con el botón secundario y seleccione **Desplegar**. Se le pedirá un formulario para metadatos básicos en el nuevo documento. Los datos de entrada requeridos y/o rellenados previamente pueden cambiar según el tipo de documento. Sin embargo, generalmente incluyen:

*   **Etiqueta:** etiqueta libre como código corto;
*   **Nombre:** nombre del documento;
*   **Descripción:** descripción larga;
*   **Tipo:** tipo de documento (informe, gráfico, cabina, etc.);
*   **Conjunto de datos:** el conjunto de datos ya desplegado para documentos que utilizan documentos externos;
*   **Fuente de datos:** la referencia a la fuente de datos que se utilizará en SpagoBI Server para documentos que tienen un conjunto de datos interno, con el fin de trabajar con la fuente oficial en lugar de RDBMS local o en funcionamiento;
*   **Estado:** el estado inicial del documento (desarrollo, prueba, liberación, suspensión) de acuerdo con su política de gestión del ciclo de vida;
*   **Actualizar segundos:** el tiempo de actualización automática;
*   **Posición:** la carpeta en el repositorio remoto de Knowage Server donde se implementan los documentos, estableciendo indirectamente quién puede usarlo y su primer nivel de autorización.

.. advertencia::

```
   **Analytical documents**
  
     The described form sets basic metadata, generally managed as technical metadata on Knowage Server.
  
```

Estos detalles del documento se almacenan como metadatos en el repositorio local y se utilizan para registrarlo también en el repositorio central del servidor. Para ver sus valores locales, seleccione el botón **Propiedades** en el menú contextual del documento y elija **Conocimiento**.

Directamente desde allí, los metadatos locales se pueden actualizar en cualquier momento en el servidor activo, simplemente presionando el botón **Actualizar metadatos en active server** botón.

## Navegación cruzada para informes BIRT

Una característica poderosa de los documentos analíticos de Knowage es la navegación cruzada, es decir, la capacidad de navegar por los documentos de una manera similar a un navegador siguiendo los flujos de datos lógicos. Aunque la crossnavigation se proporciona uniformemente en todos los documentos ejecutados en Knowage Server, cada tipo de documento tiene su propia modalidad para establecer el enlace que apunta a otro documento.

Observe que el puntero puede hacer referencia a cualquier documento de Knowage, independientemente del documento de origen. Por ejemplo, un informe BIRT puede apuntar a un gráfico, una consola, una geografía o cualquier otro documento analítico.

En Knowage existen dos tipologías principales de navegación cruzada: *interno* y *externo*.

*Navegación cruzada interna* actualiza una o más áreas de un documento haciendo clic en una serie, un texto, una imagen o, en general, en un
elemento seleccionado del documento.

*Navegación cruzada externa* abre otro documento haciendo clic en un elemento del documento principal, permitiendo de esta manera la definición de una "ruta de navegación" a lo largo de los documentos analíticos (por lo general, desde información muy general y agregada hasta la información más detallada y específica)). De hecho, puede agregar la navegación cruzada también a un documento alcanzado por la navegación cruzada. Esto puede ser útil para profundizar en un análisis, ya que cada paso de navegación cruzada podría ser una visualización más profunda de los datos que se muestran en el documento inicial.

Obviamente, es posible asociar más de una navegación cruzada a un solo documento. Significa que al hacer clic en diferentes elementos del mismo documento, el usuario puede ser dirigido a diferentes documentos.

Para permitir la navegación cruzada externa en un informe BIRT, debe agregar un hipervínculo al elemento en el que desea que se pueda hacer clic mediante el botón **Propiedades** de Knowage Studio. La mayoría de los elementos de informe pueden hospedar un hipervínculo. Por ejemplo, agreguemos un hipervínculo a una celda de la tabla.

Haga clic en la celda de la tabla y seleccione el botón **Hiperenlace** en el **Propiedades** pestaña. Al hacer clic en Editar, el editor de hipervínculos se abrirá y mostrará tres campos de entrada:

*   **Ubicación:** escriba aquí el URI,
*   **Blanco:** seleccione Self,
*   **Información sobre herramientas.** escriba el texto que desea que aparezca en el enlace, como se muestra en la siguiente figura a continuación.

.. figura:: media/image340.png

    Hyperlink editor.

Para editar la ubicación, haga clic en el botón desplegable derecho y seleccione la sintaxis de JavaScript. Esto abrirá el editor de JavaScript BIRT. Aquí debe escribir la función javascript "javascript:parent.execExternalCrossNavigation" pasando argumentos JSON como ParName: string, null y string.

En la sintaxis de Cross Navigation damos una idea de cómo debe ser la sintaxis:

.. \_crossnavsyntax:
.. code-block:: javascript
:linenos:
:caption: Sintaxis de navegación cruzada.

       "javascript:parent.execExternalCrossNavigation("+         
       "{OUT_PAR:'"+params["par_period"].value+"'"+               
       ",OUT_STRING:'"+string_text+"'"+ 
       ",OUT_NUM:"+numberX+     
       ",OUT_ManualSTRING:'foo'"+    
       ",OUT_ARRAY:['A','B','5']}"+ 
       ",null,"+       
       "'Cross_Navigation_Name');"       

.. advertencia::

```
**Type the right cross navigation name**

   It is important to underline that the "Cross_Navigation_Name" of Cross Navigation syntax is the cross navigation name                    related to the document and set using the "Cross Navigation Definition" feature we described in *Analytical Document* Chapter, *Cross Navigation* Section. 
   
```

Será necesario escribir el nombre de navegación cruzada correcto relacionado con el documento tal como se define utilizando la configuración "Herramienta" del servidor Knowage y definir esos parámetros (OUT_PAR, OUT_STRING, etc.) como parámetros de salida en el documento desplegado en el servidor (consulte *Documento analítico* Capítulo *Navegación cruzada* Sección).

Tenga en cuenta que la sintaxis de la cadena es fija, mientras que debe asignar valores a los parámetros que se pasarán al documento de destino. El editor de JavaScript le ayuda a insertar enlaces de columna de conjunto de datos, como se muestra en la figura siguiente, y a informar de los parámetros automáticamente.

.. figura:: media/image342.png

     Column bindings.

Para administrar parámetros de múltiples valores es suficiente enumerar todos los valores entre corchetes separándolos con comas, como se informa en el código anterior. Más específicamente, la matriz debe contener valores del mismo tipo. Por ejemplo:

.. code-block:: javascript
:linenos:

    OUT_SeveralNames:['Michael','Paul','Sophia'] 

o

.. code-block:: javascript
:linenos:

    OUT_SeveralNames:[5,9,31938]

Finalmente, es posible establecer una especie de navegación "multi"-cruzada si, por ejemplo, el documento de salida está relacionado con más de un documento a través de la Definición de navegación cruzada. Supongamos que el documento de origen va a un documento de destino y el nombre de la navegación es "CrossNav1" y simultáneamente el documento de origen va a un segundo documento de destino y el nombre de la navegación es "CrossNav2". Si en la función JavaScript de *Sintaxis de navegación cruzada* código el "Cross_Navigation_Name" se deja vacío como en el código siguiente, cuando el usuario hace clic en el objeto para el que se ha habilitado la navegación se abre una ventana emergente pidiendo al usuario que elija entre la navegación "CrossNav1" o la "CrossNav2". Este procedimiento permite al usuario tener una navegación más de una posible a partir del mismo objeto.

.. \_crossnavsyntax2:
.. code-block:: javascript
:linenos:
:caption: Sintaxis de navegación cruzada

       "javascript:parent.execExternalCrossNavigation("+                       
       "{OUT_PAR:'"+params["par_period"].value+"'"+                             
       ",OUT_STRING:'"+string_text+"'"+  
       ",OUT_NUM:"+numberX+ 
       ",OUT_ManualSTRING:'foo'"+ 
       ",OUT_ARRAY:['A','B','5']}"+    
       ",null,"+    
       "'');"
