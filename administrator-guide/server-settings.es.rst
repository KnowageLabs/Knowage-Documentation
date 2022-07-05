# Configuración del servidor

En este capítulo describimos todas las funcionalidades disponibles en el panel Configuración del servidor del menú Administrador que se muestra a continuación.

.. figura:: media/image93.png

Panel de configuración del servidor.

Editores similares le dan acceso a configuraciones y dominios. Vamos a proporcionar un ejemplo de ambos casos para que entiendas cómo funciona su gestión. Una visión general completa de la creación, edición y gestión de metadatos concluye este capítulo.

## Gestión de la configuración

Haciendo clic en el botón **Configuración del servidor** > **Gestión de la configuración**, puede administrar muchos elementos de configuración. Por ejemplo, aquí puede establecer el idioma predeterminado, así como la configuración de correo. Empieza a escribir `DEFAULT` en el formulario de búsqueda, como se muestra a continuación, para filtrar entre los artículos disponibles y encontrar lo que le interesa.

.. figura:: media/image94.png

Lista de categorías de configuración.

Proporcionamos un ejemplo para que pueda comprender el uso de la interfaz. Supongamos que desea establecer el italiano como idioma predeterminado. Seleccione la fila con `SPAGOBI.LANGUAGE_SUPPORTED.LANGUAGE`. predeterminado como etiqueta y haga clic en el icono del lápiz al final de la fila para editar el elemento. Insertar `it,IT` como **Comprobación de valor** como clic **Salvar**.

Puede ver los idiomas disponibles y su código (**Columna Comprobación de valor)** en la fila SPAGOBI. LANGUAGE_SUPPORTED. IDIOMAS.

      .. warning::
         **Warning**

         Knowage Server may take up to 1 minute to apply the configuration changes.

## Gestión de dominios

Haciendo clic en **Gestión de dominios** menú de elementos, puede administrar categorías. En la siguiente figura mostramos el editor de Gestión de Dominios. Puede agregar, por ejemplo, nuevas categorías para un modelo de negocio, para un conjunto de datos y para todos los dominios que puede ver en el **Columna de nombre de dominio**.

.. figura:: media/image95.png

Editor de gestión de dominios.

Proporcionamos un ejemplo para describir cómo funciona. Supongamos que desea agregar una nueva categoría entre los conjuntos de datos, denominada "Costos". A continuación puedes ver las categorías ya existentes.

.. figura:: media/image96.png

Categorías de modelos de negocio ya existentes.

Haga clic en el botón rojo más en la esquina superior derecha y, por defecto, se abrirá una nueva página con el formulario que debe completar. Un ejemplo se muestra en la figura a continuación. Rellene las columnas de la siguiente manera:

.. figura:: media/image97.png

Formulario a rellenar para crear una nueva categoría.

*   **Código de valor**: Costos
*   **Valor name_image**: Costos
*   **Código de dominio**: CATEGORY_TYPE
*   **name_image de dominio**: Conjuntos de datos de costos
*   **Descripción del valor**: Conjuntos de datos de costos

Todos los valores excepto el **Código de dominio** a ti. estos últimos son obligatorios para una correcta configuración. Ahora haga clic en Guardar. Ha creado correctamente la nueva categoría de conjunto de datos.

También puede modificar un dominio existente seleccionando su fila dedicada y haciendo clic en el botón de edición.

## Menú Exportadores

El menú Exportadores es la nueva característica de Knowage. Esta característica permite al administrador configurar los exportadores de los documentos. Al abrir este catálogo, en el lado izquierdo puede ver la lista de exportadores creados y si desea ver los detalles de uno de ellos o cambiarlo, puede hacerlo seleccionándolo en la lista. Puede agregar un nuevo exportador haciendo clic en un icono más. Vea la figura a continuación.

.. figura:: media/image101.png

Adición de un nuevo exportador.

En el lado derecho del catálogo tiene dos menús desplegables donde puede elegir motor y exportador para vincularlo con el motor. Después de seleccionar el motor y el exportador, puede guardarlo haciendo clic en un botón Guardar en la esquina superior derecha. En la siguiente figura puede ver el ejemplo de creación de un nuevo exportador.

.. figura:: media/image102.png

Creación de un nuevo exportador.

También tiene la posibilidad de cambiar el exportador existente y eliminarlo.

## Metadatos

Knowage ofrece la posibilidad de definir categorías de metadatos y luego darles un valor para cada documento analítico y para cada subobjeto.

En la página de metadatos, que se muestra a continuación, puede ver la lista de metadatos existentes. Aquí también puede definir un nuevo metadato utilizando el botón dedicado.

.. figura:: media/image98.png

Lista de metadatos existentes.

Para definir un nuevo metadato, asígnele un **Etiqueta**un **Nombre**un **Descripción** y un **Tipo**. El **Etiqueta** es un identificador único, el **Nombre** es lo que se mostrará al usuario final y el **Tipo** puede ser `SHORT TEXT` o `LONG TEXT`.

Recordamos que la visibilidad de los metadatos es una de las autorizaciones que puede establecer al crear roles. Solo los usuarios asociados a roles que tienen esta autorización verán los metadatos. Además, para editar metadatos, los roles de usuario deben tener otra autorización llamada **Guardar metadatos**.
