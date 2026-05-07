# Indicador clave de rendimiento

KPI significa Indicador Clave de Rendimiento. Denota un conjunto de métricas, generalmente derivadas de medidas simples, que permiten a los gerentes tomar una instantánea de los aspectos clave de su negocio. Las principales características de los KPI siguen:

*   indicadores resumidos,
*   cálculos complejos,
*   umbrales que respalden la evaluación de los resultados,
*   objetivos de referencia,
*   fácil de usar pero que requiere habilidades más específicas para diseñarlo,
*   asociación con alarmas,
*   no se utiliza necesariamente para el análisis en tiempo real,
*   puede referirse a un marco de tiempo específico.

Por estas razones, los KPI siempre son definidos por analistas expertos y luego utilizados para analizar el rendimiento a través de vistas sintéticas que seleccionan y describen solo información significativa.

Knowage permite la configuración de un documento KPI gracias a un documento específico **Motor KPI**. El valor crítico (o valores) se puede calcular y visualizar a través de las funcionalidades disponibles en la sección 'Modelo KPI' del área de menú Knowage (consulte la siguiente figura).

## Desarrollo de KPI

Introducimos la herramienta KPI dividiendo el tema en pasos. Resumimos brevemente aquí los argumentos que cubriremos en las siguientes secciones para tener una visión general de la implementación de KPI.

*   **Definición de la medida**: es necesario definir primero las medidas y atributos, eventualmente con parámetros, para calcular el valor crítico de interés.
*   **Definición de KPI**: aquí se calcula el valor solicitado a través de una fórmula utilizando las medidas y atributos establecidos en el paso anterior y configurar umbrales.
*   **Blanco**: es posible monitorear el valor de uno o más KPI comparándolo con un valor fijo adicional.
*   **Schedulation**: puede programar la ejecución de uno o más KPI, eventualmente filtrados por condiciones.
*   **Creación de documentos**: por último, se desarrolla el documento KPI.

Por lo tanto, entramos en más detalles.

**Definición de la medida.** El primer paso es crear una nueva medida o regla. Escoger **Definición de medida/regla** desde el menú contextual de la página principal, como se muestra a continuación.

.. \_measureruledefmenu:
.. figura:: media/image121.png

    Measure/Rule Definition menu item.

Haga clic en el icono "Más" para establecer una nueva medida/regla. Se abre una página del editor de consultas. Tenga en cuenta que una vez seleccionado el origen de datos, al presionar simultáneamente la tecla CRTL y la barra espaciadora se abre un menú contextual que contiene las columnas de origen de datos disponibles y las palabras clave de la base de datos. Consulte la siguiente figura para tener un ejemplo.

.. figura:: media/image122.png

    Editing the query when defining a KPI.

Cada regla se basa en una consulta a la que puede agregar marcadores de posición. Un marcador de posición representa un filtro que puede agregar a la regla y que puede ser útil para las tareas de generación de perfiles. Es posible asignar valor a un marcador de posición mientras se configura la programación del KPI (este procedimiento se examinará más a fondo en el párrafo "Creación de documentos"). La sintaxis que se debe usar en las consultas para establecer un marcador de posición es columnName=@placeholderName, como se muestra en el ejemplo de la figura siguiente.

.. figura:: media/image123.png

    Setting placeholder in query definition.

Generalmente, la regla de dicha consulta puede devolver una o más medidas y posiblemente un atributo. A continuación se da un ejemplo.

.. figura:: media/image124.png

    Query definition.

Se puede asignar una tipología (medida, atributo y atributo temporal) y una categoría a cada campo devuelto por la consulta utilizando el **Metadatos** como se resalta en la siguiente figura. La tipología es necesaria para asociar un tipo a cada campo devuelto por la consulta. En particular, si el campo es temporal, es obligatorio especificar a qué nivel desea que se considere, es decir, si corresponde a un día, un mes, un año, un siglo o un milenio. Para las medidas y atributos es posible asignar también una categoría para buscarlos fácilmente en un segundo momento.

.. \_metadatasettings:
.. figura:: media/image125.png

    Metadata settings.

Decimos de antemano que, es importante distinguir estas categorías metedata del campo requerido "Categoría" que se produce al guardar la definición de KPI (ver siguiente figura).

.. \_kpidefinitioncat:
.. figura:: media/image161.png

    Category assigned when saving a KPI definition.

De hecho, la categoría asignada al guardar la definición de KPI se agregará (si no existe) en la lista "Categorías de KPI", utilizada para perfilar KPI en roles (consulte la Figura a continuación).

.. \_kpicategory:
.. figura:: media/image126.png

    KPI category.

.. advertencia::
**No confundir la categoría de metadatos con la categoría KPI**

         The category defined in the metadata tab of the "Measure definition" functionally are not the same categories selected in the tab area of the "Roles management" functionality (see the figure above). The first are used to classify the metadata while the second are needed for the profiling issue.

Como dijimos, existe una categorización adecuada para las agregaciones de tipo temporal. De hecho, al asociar "atributo temporal" como tipología de metadatos, el usuario técnico debe indicar el nivel jerárquico de los datos: día, mes o año. Puede ver un ejemplo en la siguiente figura. Tenga en cuenta que el campo establecido como tipo temporal debe contener números (por lo tanto, no se permiten los tipos de cadena). Por ejemplo, si se desea establecer un campo como "mes", dicho campo debe contener {01,02,03,...,12} que se considerará como {enero, febrero, marzo,...,diciembre}.

.. \_hierarchyleveltempattrib:
.. figura:: media/image127.png

    Hierarchy level for temporal attributes.

El **Vista previa** le permite comprobar la ejecución de la consulta y echar un vistazo a una parte del conjunto de resultados.

Examinemos ahora las características adicionales disponibles en la esquina superior derecha. Allí puedes encontrar la siguiente pestaña:

*   **Elías**: puede ver los alias definidos en otras reglas; tenga en cuenta que solo se almacenan y muestran los alias de esos colums guardados como atributo. Esto es útil para evitar alias ya en uso al definir una nueva regla. De hecho, un alias no se puede guardar dos veces, incluso si está contenido en reglas diferentes.

.. figura:: media/image128.png

    Checking aliases.

*   **Marcador**: aquí puede consultar los marcadores de posición existentes. Estos se establecen en la consulta que está editando o en otras.

.. figura:: media/image42930.png

    Setting placeholders in a query.

*   **Salvar**: para guardar la consulta y otros ajustes recién configurados.
*   **Cerrar**: para salir de la ventana de configuración de la regla.

**Definición de KPI.** Seleccione el botón **Definición de KPI** del menú contextual de la página principal de Knowage, como se muestra en la figura siguiente. Haga clic en el icono "Más" para configurar un nuevo KPI.

.. figura:: media/image131.png

    Configure a new KPI.

La ventana abre una primera etiqueta, titulada **Fórmula** (consulte la figura a continuación), donde debe escribir la fórmula para habilitar los cálculos.

.. figura:: media/image132.png

    Formula definition tab.

Presione la tecla CTRL y la barra espaciadora simultáneamente para acceder a todas las medidas definidas en las reglas, como se muestra a continuación.

.. \_pressctrlspacemeasure:
.. figura:: media/image133.png

    Press crtl and space to get measures.

Una vez que se selecciona una medida, debe elegir qué función debe actuar sobre ella. Esto se puede hacer haciendo clic en el botón *f*\ () que rodea a la medida elegida. Vea la figura a continuación.

.. \_formulasyntax:
.. figura:: media/image134.png

    Formula syntax.

Haciendo clic en el botón *f*\ () la interfaz abre una ventana emergente donde puede seleccionar qué función se aplica a la medida, consulte la figura a continuación. Una vez realizada la selección, la fórmula se rellenará automáticamente con la sintax adecuada y podrás seguir editándola.

.. figura:: media/image135.png

    Available functions.

Una vez que se ha insertado una fórmula completa (un ejemplo se da en la figura a continuación), puede pasar a la siguiente pestaña.

.. figura:: media/image136.png

Ejemplo completo de fórmula.

El **Cardinalidad** le permite definir el nivel de granularidad (es decir, el nivel de agrupación) para los atributos de las medidas definidas.

Refiriéndose al siguiente ejemplo, seleccionando (con una comprobación) ambas medidas para el atributo product_name, las medidas de KPI se calculan, agrupadas en cada product_name; de lo contrario, no se realizará ninguna agrupación.

.. figura:: media/image137.png

    Cardinality settings example.

Los valores límite se pueden establecer mediante la ficha Umbral (figura a continuación). Es obligatorio establecer al menos un umbral, de lo contrario no se puede guardar el KPI. Puede elegir un umbral ya definido haciendo clic en la lista "Umbral" o crear uno nuevo.

.. figura:: media/image138.png

    Setting thresholds.

Para insertar un nuevo umbral es obligatorio insertar un nombre y asignar un tipo, mientras que la descripción es opcional. Haciendo clic en **Agregar nuevo umbral** elemento aparece un nuevo elemento. Es necesario definir el **Posición**, **Etiqueta**, **Mínimo** y **Máximo** valores. Es posible elegir si incluir los valores mínimo y máximo en la ranura de valores. El **Severidad** se utiliza para vincular los colores a su significado y hacer que los umbrales sean legibles por otros usuarios técnicos. Tenga en cuenta que el color se puede definir a través del código RGB, el código hexadecimal o eligiéndolo desde el panel.

Recuerde guardar una vez que se hayan establecido todos los umbrales.

.. advertencia::
**Colores "estándar" para umbrales**

         Well call **standard colors** for thresholds the ones listed below (in terms of hexadecimals):
         
            - green: #00FF00,
            - yellow: #FFF00,
            - red: #FF0000.

Finalmente el usuario debe guardar la definición de KPI haciendo clic en el botón "Guardar", disponible en la esquina superior derecha de la página. Una vez que el usuario hace clic en el botón "Guardar", se abre el asistente "Agregar asociaciones de KPI", como puede ver en la siguiente figura. Aquí, es obligatorio asignar un nombre al KPI. Además, el usuario puede establecer la categoría KPI para que solo los usuarios cuyos roles tienen las permmisiones a esta categoría específica puedan acceder al KPI. Recuerde que es posible asignar permisos sobre KPI al definir roles utilizando la funcionalidad "Administración de roles" disponible en la página principal de Knowage. Además, el usuario puede marcar o desmarcar el botón "\ **Habilitar el control de versiones**\ " si desea realizar un seguimiento de las reglas/medidas/objetivos que generan la respuesta de KPI en cada ejecución de KPI.

.. \_savekpidefcategory:
.. figura:: media/image139.png

    Save the KPI definition and set category.

**Blanco.** Este paso no es obligatorio. Introduzca el **Definición del objetivo** como se muestra a continuación.

.. figura:: media/image140.png

    Target Definition menu item.

Al hacer clic en el icono "Más" puede agregar un nuevo objetivo (Figura a continuación).

.. figura:: media/image141.png

    Add a new target.

La definición de un nuevo destino requiere escribir un nombre, una fecha de inicio/fecha de finalización de validez y la asociación a al menos un destino. Es posible asociar un objetivo haciendo clic en el elemento **Agregar KPI** y seleccionando el KPI de interés. Una vez establecida la asociación, el cuadro "Valor" se vuelve editable y puede insertar el valor que desea enviar al KPI seleccionado. Un ejemplo se da en la figura a continuación.

.. \_kpitargetassoc:
.. figura:: media/image142.png

    KPI target association.

En la fase de visualización de KPI, se mostrará un grosor en negrita roja en el valor indicado (consulte la siguiente figura).

.. \_targetmarkkpiscale:
.. figura:: media/image143.png

    Target mark in KPI scale of values.

Tenga en cuenta que una vez establecidos los objetivos, la ventana de la figura 7.20 se rellena con una lista. Tenga en cuenta que aquí la categoría sirve como descripción y solo para ordenar los registros.

**Schedulation.** Una vez definidos los KPI, es necesario programarlos para proceder a la creación de un documento analítico. Para este propósito, haga clic en el botón **Programador de KPI** desde el menú contextual que puedes ver a continuación.

.. figura:: media/image144.png

    KPI Scheduler menu item.

En cuanto a las otras interfaces, basta con hacer clic en el icono "Plus" para crear una nueva programación. La nueva ventana de schedulation presenta varias pestañas.

*   **KPI**: es posible asociar uno o más KPI a la schedulation haciendo clic en "Agregar asociación de KPI".

.. figura:: media/image145.png

    KPI tab window.

*   **Filtros**: aquí se asignan valores a los filtros (si están configurados) asociados a la programación. Tenga en cuenta que es posible asignar valores a los filtros mediante una LOV, una lista fija de valores o una función temporal. En caso de que se elija la opción LOV, recuerde que la LOV debe devolver un valor único. Esta opción puede ser útil para las tareas de generación de perfiles.

.. figura:: media/image146.png

    Filters options.

*   **Frecuencia**: aquí está el lugar donde el intervalo de tiempo de schedulation (fecha de inicio y finalización) se puede establecer junto con su frecuencia.

.. figura:: media/image147.png

     Frequency tab window.

*   **Ejecutar**: aquí puede seleccionar el tipo de ejecución. Las opciones disponibles distinguen entre el almacenamiento y la eliminación de datos registrados antiguos. De hecho, seleccionando **Insertar y actualizar** el programador calcula los valores de KPI actuales (de acuerdo con la elección de frecuencia) y los almacena en tablas adecuadas sin eliminar las mediciones antiguas y todos los archivos de texto de registro de errores están disponibles justo debajo. Al seleccionar **Eliminar e insertar** se eliminan los datos anteriores.

.. figura:: media/image148.png

    Execute tab window.

En la siguiente figura resumimos el caso de ejemplo al que nos hemos referido desde ahora.

.. figura:: media/image149.png

    Overview of the KPI case.

Una vez que se completa la programación, haga clic en el botón "Guardar". Recuerde dar un nombre a la schedulation como en la siguiente figura.

.. figura:: media/image150.png

    Creation of a KPI Document.

## Creación de un documento KPI

**Creación de documentos.** Ahora se ha establecido la programación y es posible visualizar los resultados. Necesitamos en este punto crear un nuevo documento analítico de tipo KPI y que utilice el motor KPI (Figura a continuación). Entonces ahorramos.

.. figura:: media/image151.png

    Overview of the KPI case.

Haga clic en el botón **Compilación de plantillas** para desarrollar la plantilla. Aquí puede elegir entre KPI y Scorecard (consulte el Capítulo de Scorecard para obtener detalles sobre la opción Scorecard). En el caso de KPI es posible elegir entre los dos siguientes tipos de documento.

*   **Lista**: con esta opción es posible añadir varios KPI que se mostrarán en la misma página con una visualización por defecto.
*   **Widget**: con esta opción siempre es posible añadir varios KPI que se mostrarán en la misma página pero en este caso también se le pedirá que seleccione su visualización: Velocímetro o Tarjeta KPI; a continuación, el valor mínimo y el valor máximo que puede asumir el KPI y si desea agregar un prefijo o un sufijo (por ejemplo, la unidad de medida del valor) al valor mostrado.

Luego, prácticamente debe agregar la asociación de KPI utilizando el área Lista de KPI de la interfaz. Como puede ver en la figura a continuación, puede seleccionar el KPI después de hacer clic en el enlace "AGREGAR ASOCIACIÓN DE KPI". Este último abre un asistente que permite recoger una opción múltiple de los KPI. Una vez elegido, debe especificar todos los campos vacíos del formulario, como "Categoría", "Ver como", etc. (consulte la figura a continuación). Tenga en cuenta que el campo "Ver como" es donde puede decidir si el widget será un velocímetro o una tarjeta KPI.

.. figura:: media/image152.png

    Setting the KPI associations using the dedicated area.

Además, puede establecer las otras propiedades del documento KPI utilizando el **Opciones** y el **Estilo** áreas (Figura abajo).

.. figura:: media/image153.png

    Areas of the Template Build for KPI.

En particular, es posible dirigir la granularidad de tiempo utilizada por el motor KPI para mejorar los rendimientos. Para ello, en el área "Opciones" (siguiente figura) se invita al usuario a indicar el nivel de agregación eligiendo entre "día", "semana", "mes", "trimestre", "año".

.. figura:: media/image154.png

    Choose the time granularity.

Finalmente en el área "Estilo" el usuario puede personalizar el tamaño del widget, la fuente, el color y el tamaño de los textos.

.. figura:: media/image155.png

    Style settings.

A continuación, guarde y ejecute el documento. Los ejemplos se muestran en las últimas tres figuras a continuación.

En caso de que el documento contenga KPI que implique agrupar funciones en algunos atributos, es posible filtrar los datos devueltos en esos atributos. Para recuperar fácilmente los atributos en los que se agrupan las medidas, basta con comprobar los campos enumerados en la pestaña "Cardinalidad" de la definición de KPI. Lo recordamos en la imagen de abajo.

.. figura:: media/image137.png

    Cardinality settings example.

Luego, para usarlos para filtrar el documento, primero agregue los controladores analíticos adecuados. Consulte la Sección 5.4 para obtener más información sobre cómo asociar un controlador analítico a un documento (y, por lo tanto, a un documento KPI). Entonces es obligatorio que la URL del controlador analítico *mosto* coinciden con el *alias de atributo* en el que se ha definido la agrupación.

.. \_kpiassociation:
.. figura:: media/image156.png

    KPI association.

.. \_widgetdocument:
.. figura:: media/image157.png

    Widget document.

.. \_kpispeedometer:
.. figura:: media/image158.png

    KPI Speedometer.

.. \_kpicard:
.. figura:: media/image159.png

    KPI Card.

.. \_kkpilist:
.. figura:: media/image160.png

    KPI List.
