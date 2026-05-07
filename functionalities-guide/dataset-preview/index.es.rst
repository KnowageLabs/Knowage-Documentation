# Vista previa del conjunto de datos

El **vista previa del conjunto de datos** es una funcionalidad presente en el espacio de trabajo, en la cabina y en el informe BIRT que logrará obtener una vista previa del conjunto de datos y el parámetro seleccionados.

## Estructura de vista previa del conjunto de datos

.. figura:: media/image01.png

    Dataset preview example screenshot.

Como puede ver en el ejemplo, en la vista previa del conjunto de datos puede ver las columnas del conjunto de datos resaltadas con diferentes colores
dependiendo del tipo de datos. Las mismas columnas de tipo de datos compartirán el mismo color.

Para cada columna, podrá leer el nombre de la columna y el tipo de columna dentro del encabezado de la columna.
En la parte inferior aparecerá una paginación si es necesario.

Para algún conjunto de datos específico, la barra de exportación también estará disponible. Si el conjunto de datos seleccionado admite esta funcionalidad
aparecerá una barra en la parte superior del cuadro de diálogo. Al hacer clic en los botones dentro, podrá descargar la vista previa en el
formato seleccionado.

.. figura:: media/image02.png

    Dataset export bar.

## Exportación de vista previa del conjunto de datos

Al hacer clic en el botón de exportación, o si el valor predeterminado para esa vista previa está configurado para descargarse, se realiza un proceso de exportación
comenzará en segundo plano.

Una vez finalizado el proceso, aparecerá una insignia de notificación en el *Descargas* icono de menú.

.. figura:: media/image02b.png

    Download notification badge.

## Dentro del espacio de trabajo

Dentro del espacio de trabajo, puede acceder a la vista previa del conjunto de datos haciendo clic en el botón de vista previa como en el ejemplo a continuación.

.. figura:: media/image03.png

    How to access workspace preview.

## Cabina interior

Dentro de la cabina, puede encontrar la configuración de vista previa del conjunto de datos en la siguiente configuración de widgets:
\- Widget de tabla
\- Widget de gráfico
\- Widget html

Al abrir la configuración del widget, el botón *cruz* estará disponible, con las funcionalidades de navegación cruzada y vista previa.

.. figura:: media/image04.png

    Preview navigation configuration.

Al habilitar el interruptor de vista previa, tendrá la posibilidad de elegir qué conjunto de datos se mostrará en la vista previa.

Si se establecen algunos parámetros del conjunto de datos, estos serán visibles en la lista siguiente.
Es posible establecer el valor del parámetro de diferentes maneras dependiendo del widget seleccionado.

Seleccionar *Descarga directa* permitirá al usuario exportar directamente el resultado de la vista previa en la interacción.
La descarga estará disponible como una exportación de vista previa común dentro del menú de descargas.
