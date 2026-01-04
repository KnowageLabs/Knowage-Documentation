# Administrador de recursos

.. importante::
**Solo Enterprise Edition**

         With the Knowage Community Edition the Resource Manager  will be able to manage just the **models** folder in order to define metadata for data mining analysis. With the Knowage Enterprise Edition,  will be able to manage all Knowage's installation resources.

El **Administrador de recursos** funcionalidad disponible en el marco del **Herramienta** del menú principal de Knowage, como se muestra en la figura siguiente, le permite administrar todos los archivos dentro de la carpeta Recursos de la instalación de Knowage. En las siguientes secciones veremos en detalle cómo usar la función Administrador de recursos.

.. figura:: medios/resource_mng\_1.png

    Resource Manager from contextual menu.

De forma predeterminada, el sistema muestra los archivos que comienzan por el directorio raíz:

.. figura:: medios/resource_mng\_2.png

    Resource Manager starting view.

## Funcionalidades de Resource Manager

La ventana Administrador de recursos reproduce dos secciones: a la izquierda, el árbol que representa los recursos del sistema existentes; a la derecha los detalles de la carpeta izquierda seleccionada. En la parte superior derecha está disponible la ruta actual:

.. figura:: medios/resource_mng\_2\_bis.png

    Resource Manager detail view.

**Funcionalidades de árbol**

El árbol muestra exactamente la estructura física del sistema de archivos desde el **Recursos** carpeta. En la barra superior están presentes dos funcionalidades: **Actualizar árbol** y **Crear nueva carpeta**:

.. figura:: medios/resource_mng\_0.png

    Tree view.

.. figura:: medios/resource_mng\_0\_bis.png

    Creation detail.

.. figura:: medios/resource_mng\_0\_ter.png

    Creation result.

Preste atención a que la nueva carpeta se crea adjunta a la carpeta seleccionada en el árbol ('KNOWAGE-5058' en este caso).

Haciendo clic en el icono "Descargar" en una carpeta específica, puede descargar todos los archivos contenidos:

.. figura:: medios/resource_mng_tree\_1.png

    Download functionality icon.

Asigne un nombre, seleccione una carpeta para la descarga y el archivo zip estará disponible en su sistema local.

.. figura:: medios/resource_mng\_3.png

    Download functionality.

Al hacer clic en el icono "Eliminar" en una carpeta específica, puede eliminar la carpeta físicamente del servidor de Knowage (después de confirmar la operación). Por favor, preste atención porque esta es una operación irreversible.

.. figura:: medios/resource_mng_tree\_2.png

    Delete functionality icon.

.. figura:: medios/resource_mng_tree\_3.png

    Delete functionality confirmation.

**Panel de detalles**

Cuando se selecciona una carpeta, el panel derecho muestra todos los archivos que contiene. Para cada uno muestra Nombre, Tamaño y Fecha de la última modificación:

.. figura:: medios/resource_mng\_6.png

    Detail view.

Todos los elementos son verificables, esto le permite seleccionar cuáles desea descargar o eliminar a través de iconos específicos en la barra de herramientas:

.. figura:: medios/resource_mng\_7.png

Funcionalidades masivas disponibles para archivos seleccionados

Si lo desea, también puede agregar uno o más archivos directamente a través del **Subir** en la parte superior de la lista:

.. figura:: medios/resource_mng\_5.png

Subir archivos

.. figura:: medios/resource_mng\_5\_bis.png

Ventana emergente de archivo de selección

En este contexto, si carga un archivo zip, puede elegir si desea administrar el archivo comprimido:

.. figura:: medios/resource_mng\_5\_ter.png

Archivo comprimido cargado

o si desea descomprimirlo a través de la selección de la opción 'Extraer archivos' en la ventana emergente:

.. figura:: medios/resource_mng\_5\_quat.png

Cargar archivo descomprimido

.. figura:: medios/resource_mng\_3\_bis.png

Resultado de los archivos descomprimidos cargados

**Definición de metadatos del modelo**

Como ya se dijo al principio, **modelos** es la carpeta única administrada tanto por la Community como por enterprise Edition. Contiene todos los modelos de minería de datos utilizables por el Catálogo de funciones de Knowage.

Para cada modelo es posible definir sus metadatos, descargar y/o eliminar el modelo utilizando directamente las opciones del árbol:

.. figura:: medios/resource_mng\_8.png

Opciones de la carpeta Modelos

*Gestión de metadatos*

El **Metadatos** abre una interfaz gráfica de usuario en la que el usuario puede definir información de metadatos sobre el modelo en uso.

Por lo tanto, es posible insertar:

*   un nombre más específico para el modelo
*   el número de versión del modelo
*   el tipo de análisis: un valor seleccionable entre 'Descriptivo', 'Predictivo' y 'Prescriptivo'
*   una imagen para representar la lógica del modelo cargable a través del icono específico
*   una descripción detallada
*   información sobre la precisión y, a continuación, el rendimiento del modelo
*   información sobre la forma de uso del modelo
*   Información sobre los formatos de los datos de entrada y salida

.. figura:: medios/resource_meta\_4.png

Ejemplo de metadatos
