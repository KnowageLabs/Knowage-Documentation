# Preparación de datos

## ¿Para qué sirve eso?

**Preparación de datos** es una funcionalidad disponible desde la versión 8.1 que permite a los usuarios crear un conjunto de datos preparado, a partir de uno existente.
De esta manera, los usuarios pueden crear un conjunto de datos preparado y luego usarlo dentro de un panel o simplemente usarlo como otro conjunto de datos.
Los usuarios tienen la capacidad de crear conjuntos de datos complejos y específicos con bastante facilidad y rapidez, con el fin de utilizarlos para cualquier propósito.

## Preparación de un conjunto de datos

El primer paso es seleccionar un conjunto de datos para trabajar.
Puede hacerlo seleccionando el conjunto de datos deseado en la sección de su espacio de trabajo (también debe haber un  **Preparación de datos** entrada):

.. figura:: media/image1.png

    The Data Preparation entry.

Hay dos formas de preparar e iniciar un proceso de preparación de datos.
El primero es a partir de la sección MyData.
Haga clic en MyData y seleccione el conjunto de datos que desee.

.. figura:: media/image2.png

    Search for your dataset example.

Luego haga clic con el botón derecho del mouse y seleccione "Preparación de datos abiertos":

.. figura:: media/image5.png

    Select "Open Data Preparation"

Esta operación desencadena el proceso de creación de avro-file.

.. figura:: media/image6.png

    For more info about what "Preparing avro file" means please refer to "Data Preparation technical detail" section.

La segunda forma es hacer clic en + botton en la parte superior derecha de la sección Preparación de datos:

.. figura:: media/image3.png

    Click on + botton on the top right of the page.

Y luego seleccione su conjunto de datos de origen.

.. figura:: media/image4.png

    Search for your dataset example.

Si el archivo avro se crea ahora, debería poder abrir la pantalla de preparación de datos, debería haber un icono de verificación junto al menú de acciones:

.. figura:: media/image7.png

    There is a check icon on the left icons menu for your selected dataset.

Pantalla principal de preparación de datos:

.. figura:: media/image8.png

    Data Preparation main screen.

## Transformaciones de preparación de datos

Puede aplicar transformaciones al dataset de origen simplemente eligiendo la acción de transformación, paso a paso, hasta que alcance el resultado deseado.

En el menú de la barra de herramientas principal, hay un conjunto de transformaciones principales (la mayoría de ellas se pueden aplicar en muchas columnas al mismo tiempo):

.. figura:: media/image33.png

    Transformations toolbar icons.

*   **Agregar columna**: agrega una nueva columna como campo calculado.
*   **Combinar columnas**: agrega una nueva columna que combina dos seleccionadas.
*   **Dividir columnas**: Agrega dos columnas dividiendo una seleccionada.
*   **Filtro**: Filtra una columna seleccionada por condiciones matemáticas (más información más adelante).
*   **Relleno**: agrega caracteres en el lado izquierdo o derecho de una columna seleccionada.
*   **Eliminar duplicados**: elimina duplicados de las columnas seleccionadas.
*   **Eliminar null**: quita los valores nulos de las columnas seleccionadas.
*   **Reemplazar**: Reemplace los valores seleccionados de columnas específicas.
*   **Recortar**: elimina los espacios en blanco de columnas específicas. (Disponible solo para una sola columna)
*   **Soltar**: Elimine una columna específica. (Disponible solo para una sola columna)

El **Agregar columna** La transformación permite al usuario agregar un **campo calculado** de tipo numérico, string o temporal.
Estas funciones son un subconjunto de las funciones del lenguaje Spark SQL y se utilizan para cálculos o manipulación de datos.
Para obtener más información, consulte https://spark.apache.org/docs/2.4.8/api/sql/index.html.

.. figura:: media/image9.png

    Available functions are a subset of Spark SQL language functions

**Combinar columnas**: agrega una nueva columna que combina dos seleccionadas mediante un separador.

.. figura:: media/image10.png

    Merge columns dialog example.

**Dividir columnas**: Crea dos nuevas columnas dividiendo una seleccionada utilizando una condición específica (es decir, un carácter).

.. figura:: media/image11.png

    Split columns dialog example.

**Filtro**: Filtra una columna seleccionada por condiciones especiales.

.. figura:: media/image12.png

.. figura:: media/image12a.png

.. figura:: media/image12b.png

    Filter dialog example.

**Relleno**: agrega caracteres en el lado izquierdo o derecho de una columna seleccionada.

.. figura:: media/image13.png

    Padding dialog example.

**Eliminar duplicados**: elimina duplicados de las columnas seleccionadas.

.. figura:: media/image14.png

    Remove duplicates dialog example.

**Eliminar null**: quita los valores nulos de las columnas seleccionadas.

.. figura:: media/image15.png

    Remove null dialog example.

**Reemplazar**: Reemplace los valores seleccionados de columnas específicas. El carbón viejo es el valor antiguo que se reemplazará.

.. figura:: media/image16.png

    Replace dialog example.

Dos transformaciones más están presentes solo haciendo clic en una columna específica: **RECORTAR** y **SOLTAR** Transformaciones.

.. figura:: media/image17.png

**Columna de caída**: quita una columna específica de la tabla.

.. figura:: media/image18.png

    Drop columns dialog warning.

**Columna de recorte**: Quita los espacios en blanco de la columna.

.. figura:: media/image19.png

    Trim column dialog example.

## Detalle técnico de preparación de datos

**¿Qué es un archivo AVRO?**

Avro es un sistema de serialización de datos.

Avro es un marco de serialización de datos desarrollado dentro del proyecto Hadoop de Apache. Utiliza JSON para definir tipos de datos y protocolos, y serializa los datos en un formato binario compacto.

Avro se basa en esquemas. Cuando se leen los datos de Avro, el esquema utilizado al escribirlos siempre está presente. Esto permite que cada dato se escriba sin gastos generales por valor, lo que hace que la serialización sea rápida y pequeña. Esto también facilita el uso con lenguajes de scripting dinámicos, ya que los datos, junto con su esquema, son completamente autodescriptivos.

Cuando los datos de Avro se almacenan en un archivo, su esquema se almacena con él, de modo que los archivos pueden ser procesados más tarde por cualquier programa. Si el programa que lee los datos espera un esquema diferente, esto se puede resolver fácilmente, ya que ambos esquemas están presentes.

Consulte la documentación oficial para obtener más información: https://avro.apache.org/

Avro se utiliza para almacenar datos y esquemas de conjuntos de datos de Knowage (con metadatos de columnas) con el fin de utilizarlos como fuente de entrada para el proceso de preparación de datos.

Cuando el usuario abre un conjunto de datos para la preparación de datos por primera vez, se crea un archivo ad avro.
Este archivo se lee y luego se utilizará como fuente de datos para las transformaciones de datos que se enviarán a Livy-Spark.

## Guardar y usar un conjunto de datos preparado

Ahora veamos cómo guardar un conjunto de datos preparado. Para nuestro ejemplo de documentación utilizamos dos transformaciones: DROP y luego un FILTER en la columna "edad".

Eliminamos la columna "golden_members":

.. figura:: media/image23.png

    Drop columns dialog example.

Y luego filtramos por edad menor de 60 años:

.. figura:: media/image21.png

    Filter columns dialog example.

La cadena de transformaciones resultante se puede ver a la derecha de la página:

.. figura:: media/image22.png

    Transformations list is present on the right panel.

Como puede ver, puede eliminar o obtener una vista previa de la última operación (en nuestro caso la transformación FILTER).

Para ver una descripción de la transformación, simplemente haga clic en el icono del ojo (si está presente, algunas transformaciones no lo necesitan):

.. figura:: media/image24.png

    Transformation preview dialog example.

Puede ver cómo se ha configurado la transformación.
Luego también puede eliminar la transformación haciendo clic en la papelera:

.. figura:: media/image25.png

    You can delete the last one only.

Si desea guardar el conjunto de datos preparado, haga clic en el icono de guardar en la parte superior derecha de la página:

.. figura:: media/image26.png

    Save panel example.

Aquí puede elegir el nombre, la descripción y la programación si desea actualizar el conjunto de datos, utilizando la transformación seleccionada, periódicamente.

.. figura:: media/image27.png

    Split columns dialog example.

Después de hacer clic en el botón GUARDAR, verá un mensaje de confirmación:

.. figura:: media/image28.png

    Saving confirmation.

Después de eso, esperando unos momentos, podrá ver sus datos guardados en la fuente de datos seleccionada haciendo clic en el icono del ojo a la derecha en la sección de preparación de datos.

.. figura:: media/image29.png

    Prepared data preview panel.

Si la operación de ingesta aún no ha finalizado o si hubo problemas para guardar datos, verá un mensaje de advertencia que indica que la operación no se ha completado.

Puede monitorear el proceso usando la sección de monitoreo, haga clic derecho en su conjunto de datos preparado guardado y haga clic en "Monitoreo":

.. figura:: media/image30.png

    Select monitoring entry.

Verá una ventana emergente con los resultados del proceso, en caso de errores puede descargar un archivo de registro.
En el lado izquierdo también puede cambiar la programación de la actualización periódica del conjunto de datos preparado.

.. figura:: media/image31.png

    Schedulations and monitoring panel example.

Ahora es posible ver el conjunto de datos preparado en la sección Administración de conjuntos de datos o en la sección MyData Workpace, por lo que, por ejemplo, puede usarlo más adelante para un panel.

.. figura:: media/image32.png

    Dataset Management panel example.
