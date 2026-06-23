# Alerta

El **Alerta** funcionalidad disponible en el marco del **Herramienta** del menú principal de Knowage, como se muestra en la figura a continuación, le permite implementar un control sobre los eventos. Técnicamente consiste en monitorizar la posible superación de umbrales fijos y la consiguiente señal de anomalías mediante un correo electrónico o mediante el lanzamiento de un proceso ETL. En los siguientes apartados veremos en detalle cómo configurar las alarmas utilizando la función Alerta.

.. \_alertfunctfrom:
.. figura:: media/image172.png

    Alert functionality from contextual menu.

## Implementación de alertas

La ventana definición de alerta (consulte la figura anterior) reproduce la lista de alertas existentes y un cuadro de búsqueda en la parte superior de la página para facilitar la navegación por los elementos. En la esquina superior derecha está disponible el icono "Plus" para configurar una nueva alerta.

Al hacer clic en el icono "Más", se abre la página de la siguiente figura.

.. figura:: media/image173.png

    Alert definition window.

Asigne un nombre y seleccione la opción **Oyente de KPI** desde el cuadro combinado. A continuación, indique la fecha de inicio, la hora de inicio y, finalmente, la fecha de finalización de la implementación de alert. Especifique el intervalo de tiempo y cuántas veces debe repetirse. En este punto elige entre **Ejecución única** y **Evento antes de desencadenar acciones**: en el primer caso la alerta debe señalar la anomalía una sola vez que se produce, mientras que en el otro caso debe enviar las alarmas cuando se produce la irregularidad tantas veces como se especifique. Tenga en cuenta que el cuadro es editable y debe contener un número que indique el número de irregularidades que deben detectarse antes de que comience la alerta.

.. figura:: media/image174.png

    Alert settings.

En la parte inferior de la página asocie el KPI de interés y seleccione la acción haciendo clic en el botón **Agregar acción** botón. Aquí puedes elegir entre **Enviar correo** o **Ejecutar un documento**.

Si se elige el "Enviar correo", se solicita al usuario que inserte los umbrales que deben ser monitoreados: en caso de que estos últimos sean superados, la funcionalidad envía el correo electrónico a los sujetos indicados. Recuerde insertar todos los campos obligatorios (nombre, umbrales y asuntos del correo) y, en particular, seleccionar el usuario al que se envía el correo electrónico. Tenga en cuenta que en el cuadro asuntos de correo puede escribir tanto direcciones de correo como nombres de usuario (por ejemplo, "user_admin"), ayudado por el texto de inserción automática es como se muestra en la siguiente figura. De hecho, el servidor de Knowage seleccionará la dirección de correo del atributo de perfil asociado a ese usuario. Por lo tanto, recomendamos establecer el atributo de perfil previamente. En particular, recuerde que el atributo profile *mosto* Se denomina implementación de Alert "\ *Correo electrónico*\ ".

.. \_sendemailconf:
.. figura:: media/image175.png

    Send email configuration.

Además, tenga en cuenta que el cuerpo del correo puede contener un mensaje de texto sin formato o una tabla que muestre los valores de KPI registrados que activaron la alerta. Para habilitar la opción de visualización de tablas, debe insertar el marcador de posición \*TABLE_VALUE\* en el cuerpo del correo como se muestra en la figura siguiente.

.. figura:: media/image176.png

Envíe un correo electrónico que contenga una tabla con los valores detectados.

Si se selecciona la opción "Ejecutar un documento", la alerta iniciará un proceso ETL cuando se detecten los umbrales elegidos. Es decir, la funcionalidad lanzará un proceso para ejecutar acciones por lotes como la escritura de tablas adecuadas de un DWH, la creación de un archivo, la llamada a un servicio de registro. Tenga en cuenta que el proceso ETL debe existir como un documento en el servidor de Knowage. En la siguiente figura se da un ejemplo.

Guarde la acción y los valores de configuración de la alerta para almacenar la alerta. Recuerde que es posible programar más de un monitoreo sobre la misma definición de alerta.

.. \_executedocument:
.. figura:: media/image177.png

    Execute document configuration.
