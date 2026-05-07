# Informes de Jasper

Jasper es una herramienta de informes independiente desarrollada por la Comunidad jaspersoft. Un ejemplo del informe Jasper se representa en la siguiente figura. Jasper Report Engine administra plantillas de informes de Jasper dentro de Knowage Server. Una plantilla de informe para Jasper es un archivo de texto con extensión .jrxml que puede ser modificado manualmente por usuarios muy expertos mediante la edición de código XML. De lo contrario, iReport, un diseñador gráfico de plantillas, se proporciona a todos los desarrolladores que desean diseñar fácilmente un informe para este motor.

.. \_exjasperreprt:
.. figura:: media/image342.png

    Example of a Jasper report.

Plese tenga en cuenta que este motor está disponible solo en KnowageER.

## Definición de documentos\*

A diferencia del diseñador BIRT, iReport no está integrado en Eclipse. Por lo tanto, antes de comenzar a desarrollar el informe, debe descargarlo del sitio web http://community.jaspersoft.com/project/ireport-designer/releases.

.. nota::
**Descarga de iReport**

         Download the iReport designer at <http://community.jaspersoft.com/project/ireport-designer/releases>. Knowage support any kind of version.

Luego tendrá que establecer la ruta al diseñador de iReport en Knowage Studio. Abra Ventana > Preferencias > Configuración del Editor de iReport y establezca la ruta correcta al archivo ireport.exe.

.. figura:: media/image343.png

    iReport Configuration in Knowage Studio.

Al igual que en el caso de un informe BIRT, el diseño y la implementación de un informe Jasper con Knowage Studio consta de los siguientes pasos:

*   crear el documento vacío,
*   cambiar a la perspectiva del diseñador de informes,
*   crear el origen de datos,
*   crear el conjunto de datos,
*   diseñar el informe a través de la interfaz gráfica,
*   implementar el informe en el servidor.

Para crear un nuevo informe de Jasper, haga clic con el botón derecho en el botón **Análisis de Negocio** y seleccione **Informe** > **Informe con Jasper**. Esto abrirá un editor donde puede elegir un nombre para su documento. El nuevo documento se creará en la carpeta Análisis de negocio.

Haga doble clic en el informe para abrir el editor: el editor de iReport se iniciará dentro de Knowage Studio. Ahora está listo para comenzar a desarrollar su informe.

Los siguientes pasos consisten en la creación de un origen de datos y de un conjunto de datos. Como se describe en la sección "Definición de conjunto de datos", Knowage Studio permite el desarrollo de documentos analíticos utilizando conjuntos de datos internos o externos. En este ejemplo mostraremos cómo crear un informe con un conjunto de datos interno.

Haga clic en el pequeño icono |image348| de la barra de menús. Se abrirá el editor de creación de orígenes de datos.

.. |imagen348| imagen:: media/image344.png
:ancho: 30

Seleccione un origen de datos JDBC, establezca los parámetros adecuados y asigne un nombre al origen de datos. En la figura siguiente se muestran los asistentes que se presentan en este procedimiento.

.. figura:: media/image345.png

    Creation of a JDBC data source in a Jasper report.

Una vez que haya definido el origen de datos, cree el conjunto de datos. Tenga en cuenta que Jasper solo permite un conjunto de datos principal. Por cierto, se pueden agregar conjuntos de datos secundarios si es necesario. Haga clic con el botón derecho en el elemento de informe y seleccione **Agregar conjunto de datos**. El editor de conjuntos de datos le guiará a través de la definición del conjunto de datos. Puede editar manualmente la consulta SQL o utilizar la herramienta de consulta de diseño proporcionada por iReport.

El árbol situado en la parte izquierda de la ventana muestra los elementos del informe. A la derecha, el **Paleta** muestra todos los elementos gráficos que puede agregar. Puede elegir ver su informe dentro del **Diseñador**, para inspeccionar el **XML** código o para mirar el **Vista previa** de su informe. Si hace clic en el |image350| puede editar y obtener una vista previa de la consulta. Como puede ver, el diseñador de iReport permite la creación de informes complejos, con diferentes elementos gráficos como pestañas cruzadas, gráficos, imágenes y diferentes áreas de texto. Ahora vemos ahora en breve cómo diseñar un informe muy simple, es decir, un informe que contiene una tabla que muestra datos del conjunto de datos definido.

.. |image350| imagen:: media/image346.png
:ancho: 30

.. figura:: media/image347.png

    Data Set definition.

Para crear una tabla, haga clic en el elemento de la paleta y utilice el asistente. La siguiente figura muestra la interfaz del editor de Jasper.

.. figura:: media/image348.png

    iReport graphical editor.

Para insertar columnas de conjunto de datos en el informe, utilice la sintaxis que se muestra en la sintaxis siguiente para insertar columnas de conjunto de datos.

.. code-block:: bash
:linenos:
:caption: Sintaxis para insertar columnas de dataset.

             $F{name_of_dataset_column}

Una vez que se ha desarrollado el documento, los usuarios técnicos pueden utilizar el servicio de implementación de Knowage Studio para registrar fácilmente el informe con su plantilla en Knowage Server. Alternativamente, cualquier plantilla válida de Jasper (desarrollada con o sin Knowage Studio) se puede cargar directamente en Knowage Server utilizando la interfaz web para la gestión de documentos.

Esta sección no proporciona más detalles sobre el desarrollo gráfico, ya que se centra en aspectos específicos de Knowage Jasper Report Engine. Todas las funcionalidades estándar de Jasper funcionan con Jasper Report Engine. Para obtener una visión general completa de la herramienta de informes de Jasper y una guía detallada para desarrolladores, consulte la documentación oficial en `http://community.jaspersoft.com/`.
