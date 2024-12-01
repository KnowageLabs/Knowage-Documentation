# Acceso básico a datos

Este capítulo describe las funciones avanzadas, es decir, disponibles solo en los productos KnowageBD y KnowageSI, para acceder a los datos como usuario final.

.. importante::
**Edición Enterprise**

         If you purchased Knowage EE, the following features are available only in KnowageBD and KnowageSI products

Un conjunto de datos es una forma de leer datos de diferentes fuentes y representa la parte de los datos utilizada por varios documentos. Supongamos que desea crear un gráfico de barras que muestre la tendencia de ventas para el año en curso; en este caso, debe pasar al documento el monto total de ventas para cada mes del año en curso. Puede crear su propio conjunto de datos cargando un archivo XLS o CSV o utilizar un conjunto de datos ya definido. Knowage también le ofrece la posibilidad de descargar datos abiertos de WEB gracias a la integración CKAN. Además, puede crear su propio conjunto de datos y más completo a partir de diferentes fuentes a través de la federación de conjuntos de datos. A continuación describiremos todas estas funcionalidades.

Supongamos que debemos introducir, con las credenciales de usuario final, el área de gestión de datos haciendo clic en el botón **Área de trabajo** del menú Funcionalidades de BI como se muestra en la figura siguiente y el icono de funcionalidades de BI **Datos** de la ventana.

.. figura:: media/image56.PNG

    Access to **My Data** area

Después tienes las subsecciones: **Conjunto de datos** y **Modelos**. Escoger **Modelos** para explorar los modelos y el **Federación de conjuntos de datos** área. Tenga en cuenta que el **Federación de conjuntos de datos** la funcionalidad solo está disponible en KnowageBD y KnowageSI.

## Conjunto de datos

En el área "Dataset" encontramos todos los datasets clasificados según sus tipos. Los conjuntos de datos se clasifican de la siguiente manera:

*   **Mi conjunto de datos**: conjuntos de datos creados por usted mismo cargando un archivo CSV o XLS o creando una consulta sobre un modelo de negocio utilizando la interfaz Qbe;
*   **Conjunto de datos empresarial**: conjuntos de datos certificados, es decir, conjuntos de datos creados por los usuarios técnicos/expertos y compartidos con el usuario final.
*   **Conjunto de datos compartido**: conjuntos de datos creados y compartidos por otros usuarios finales;
*   **Conjunto de datos CKAN**: en esta área puede descargar conjuntos de datos públicos y visualizar sus conjuntos de datos CKAN;
*   **Todo el conjunto de datos**: en esta carpeta se almacenan todos los conjuntos de datos disponibles, es decir, todos los conjuntos de datos contenidos en las clases que acabamos de describir.

Mi conjunto de datos

```

In this area you can create datasets uploading your own files.

Click **Create Dataset** to open the dataset wizard which guides you through the dataset creation. You can choose between XLS or CSV file as in the following figure.

.. _datasetcreation:
.. figure:: media/image7.png

    Dataset creation.

In the example shown in the next figure, we upload an XLS file.

.. _uploadingxlsdat:
.. figure:: media/image8.png

    Uploading XLS for dataset.

The wizard, shown below, leads the user to insert some information to configure the dataset. For instance to specify the number of rows to skip or to limit and which sheet (of the XLS file) to pick up values from.

.. _configfeatures:
.. figure:: media/image9.png

    Configuration features.

Once you have uploaded the file, you can check and define the metadata (measure or attribute) of each column. To switch a measure to an **attribute** (or viceversa), click on **Value** column of the interested row field as shown below.

.. figure:: media/image101112.png

    Change metadata.

Just few steps before saving the dataset:

-  Check the data preview in order to verify the accuracy of your data;
-  enable or disable the persistence of dataset. Thanks to this functionality the server creates a snapshot of the extracted data in order to avoid to reload the dataset each time that the user revokes it;
-  finally, name and save the dataset as shown below.

.. figure:: media/image1314.png

    Saving dataset.

As we discussed previously, you find all created datasets under **My dataset** area. You can share/unshare them by clicking on the **share** icon (have a look at the next figure). The colour of the icon changes from white to red when sharing is turned to active. A shared dataset is visible to all other users having your same role.

Note that dedicated area “\ **Shared Dataset**\ ” contains all acquired datasets thanks to the sharing of other users.

.. _sharedataset:
.. figure:: media/image15.png

    Share a dataset.

CKAN integration
```

Gracias a la integración de CKAN, puede acceder fácilmente a los conjuntos de datos publicados en la World Wide Web (por ejemplo, datahub.io, data.gov, data.lab.fiware.org, dati.gov.it y más). De hecho, CKAN es la plataforma de portal de datos de código abierto líder en el mundo. Es un potente sistema de gestión de datos que hace que los datos sean accesibles al proporcionar herramientas para agilizar la publicación, el intercambio, la búsqueda y el uso de datos. CKAN está dirigido a editores de datos (gobiernos nacionales y regionales, empresas y organizaciones) que desean que sus datos sean abiertos y estén disponibles. Por lo tanto, puede buscar y manejar datos abiertos de manera de autoservicio.

.. advertencia::
**Conjuntos de datos CKAN**

      CKAN datasets can be divided into four main categories: “Public”, “Organization private”, “Acquired”, “User private”. You can download and use only the datasets having a **Public** category.

Método de acceso a conjuntos de datos CKAN
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para comenzar a usar conjuntos de datos CKAN dentro de Knowage suite, vaya al **Conjunto de datos CKAN** en la subsección "Conjunto de datos" de la sección "Datos" en "Mi espacio de trabajo". Como se muestra en la figura a continuación, elija del cuadro combinado el repositorio que le interesa y luego haga clic en el nombre del repositorio para acceder a él.

.. figura:: media/image16.png

    CKAN Repositories.

Se mostrará una vista previa de los conjuntos de datos almacenados en el repositorio elegido.

Estos aún no son utilizables, pero puede comenzar a manejarlos como mostraremos en las siguientes secciones. Los conjuntos de datos se muestran con su nombre y descripción. Al mover el cursor sobre un conjunto de datos, aparecerá una lista de acciones disponibles. Haciendo clic en el botón **Información** , un conjunto de información del recurso CKAN original y sobre el estado del conjunto de datos (por ejemplo, visibilidad, fecha de última modificación) no puede ser mostrado por Knowage, como en la siguiente figura. Para utilizar uno de ellos hay que importar información de metadatos y luego analizar el conjunto de datos bajo demanda.

.. figura:: media/image17.png

    CKAN dataset details.

Exportar conjunto de datos
^^^^^^^^^^^^^^

Tenga en cuenta que una vez que se ha creado el conjunto de datos, el usuario puede resultar útil para obtener un Excel de él. Knowage ha diseñado un botón específico para satisfacer esta necesidad que el usuario puede encontrar explorando el panel de detalles del conjunto de datos, como se informa a continuación.

.. figura:: media/image18.png

    Export dataset.

Guardar y manejar el conjunto de datos
^^^^^^^^^^^^^^^^^^^^^^^

Si desea utilizar un conjunto de datos que aún no se ha utilizado, cualquier acción en él iniciará el asistente de importación de metadatos. Se accede a él haciendo clic en el icono de la lupa. Como primer paso, debe insertar algunos parámetros obligatorios para establecer la configuración del analizador.

Como segundo paso, el usuario debe especificar cómo aparecerá el conjunto de datos y verificar los metadatos. Tenga cuidado de elegir el tipo de datos adecuado (Cadena, Entero, Doble) y el tipo de campo (Medida, Atributo). Después de eso, haga clic en **Próximo** para ver los resultados de la validación, confirme y finalice la importación del conjunto de datos. Una vez completada la importación del conjunto de datos, el conjunto de datos seleccionado aparecerá en el **Conjunto de datos** pestaña también. Estas acciones acaban de aparecer en el cambio de conjunto de datos para los conjuntos de datos descargados. En particular, tiene el icono en forma de ojo para actualizar el conjunto de datos o cambiar los metadatos repitiendo el proceso de descarga y el icono de la lupa para consultarlo a través de la interfaz QbE.

## Modelos

Aquí encontrará los modelos que un usuario técnico ha construido para usted. Puede consultarlo utilizando la interfaz QbE y crear su propio conjunto de datos a partir de ellos.

## Federación de conjuntos de datos

La federación de conjuntos de datos es una funcionalidad disponible solo en KnowageBD y KnowageSI. Gracias a la funcionalidad de federación de datos, puede crear un nuevo conjunto de datos que combine dos o más conjuntos de datos de acuerdo con sus permisos de rol. Permítanos darle un ejemplo. Supongamos que ha almacenado en una base de datos la información de sus productos (es decir, ventas, costos, promociones ecc.) y encuentra como datos abiertos los comentarios de los clientes sobre estos productos. Si crea conjuntos de datos en estos recursos de federación de conjuntos de datos que comparten al menos una columna, puede unirlos en la columna común y mejorar el análisis.

Haga clic en **Crear federación** para ver todos los conjuntos de datos disponibles y elegir los que desea federar. Clic **Próximo** y elija en qué columnas debe realizarse la unión y haga clic en el icono más para agregarlo al cuadro de diálogo **Lista de asociaciones**. En nuestro ejemplo de la siguiente figura elegimos Producto.

.. figura:: media/image19.png

     Federated dataset details.

Una vez guardada, la nueva federación se ha creado en **Definición de federación** y puede encontrarlo en la definición de federación. Ábralo haciendo clic en el icono de la lupa en la federación. De esta manera lo abres con la herramienta QbE. Todos los detalles sobre cómo utilizar la interfaz QbE para realizar consultas gratuitas se pueden encontrar en el capítulo dedicado. Puede crear nuevos conjuntos de datos, guardarlos y recuperarlos desde el **Conjunto de datos** sección.
