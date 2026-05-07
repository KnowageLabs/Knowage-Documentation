# Glosario y linaje de datos

El **Glosario** la funcionalidad ofrece una forma de encontrar documentos navegando por una página de índice.

## Gestión del glosario

La gestión del glosario se divide en dos secciones. Una vez que ha iniciado sesión, el usuario puede encontrar los dos elementos del menú: **Definición del glosario** y **Uso del glosario**, como se muestra a continuación.

.. figura:: media/image456.png

    Glossary menu items.

Para crear un nuevo glosario, haga clic en el elemento de menú Definición de glosario que puede encontrar en el cuadro **Catálogos** sección del Knowage
interfaz. Como se muestra en la figura a continuación, la página contiene dos áreas:

*   **Palabra**: aquí hay una lista de términos. Estos últimos se utilizan como etiquetas para adjuntar a objetos analíticos como conjuntos de datos o documentos con el fin de vincular esos objetos al glosario;

*   **Glosario**: se pretende una estructura jerárquica formada por "Palabras".

.. \_glossarydefwindow:
.. figura:: media/image457.png

    Glossary definition window.

A continuación damos más información técnica sobre estos dos apartados.

En el área "Palabra" se enumeran, si las hay, las palabras creadas en un momento anterior. Para explorar el detalle de cada uno de ellos, el usuario solo tiene que hacer clic derecho en él. Se mostrará un panel que contiene tres características, como se destaca en la figura a continuación.

.. figura:: media/image458.png

    Exploring an existing word.

Al explorar el detalle, aparecerá un asistente que mostrará las siguientes características:

*   descripción
*   estado
*   categoría
*   una descripción de la fórmula,
*   una lista de enlaces a otras palabras,
*   una lista de atributos a los que se puede añadir un valor.

El mismo panel se puede utilizar para modificar o eliminar la palabra.

Para agregar una nueva palabra, haga clic en el icono "Más" disponible en la esquina derecha arriba del área "Palabra" como se muestra en la figura a continuación. Se abrirá un formato en la mitad derecha de la pantalla. Inserte "Nombre" y "Descripción", que son todos campos obligatorios y agregue detalles adicionales por necesidad. Luego haga clic en el botón Guardar. Observe que es posible buscar una "Palabra" utilizando el filtro dedicado disponible en la parte superior de la lista de palabras. Escriba una cadena en el cuadro y la investigación se iniciará automáticamente. Recuerde cancelar la cadena del cuadro para volver a la lista completa.

.. \_addanewword:
.. figura:: media/image459.png

    Add a new word.

En el área "Glosario" se enumeran, si los hubiera, todos los glosarios creados en un momento anterior. Para explorar un glosario existente, el usuario simplemente debe hacer clic en el elemento. La siguiente figura muestra un ejemplo. Aquí se subraya la estructura jerárquica del glosario. Para agregar un nuevo glosario, haga clic en el icono "Más" en la esquina superior derecha del área designada.

.. figura:: media/image460.png

    Exploring a glossary from the menu.

Al hacer clic con el botón derecho en la etiqueta del glosario como se muestra en la siguiente figura (lado derecho), el usuario puede agregar un nuevo hijo. Se abrirá el asistente "Nuevo nodo". Es obligatorio dar un Nombre al nodo mientras que se recomienda agregar un Código y una Descripción. Una vez que el usuario ha configurado los nodos, es posible agregar hijos o palabras a cada uno de ellos.

.. \_newglossnewahild:
.. figura:: media/image46162.png

    (Left) New glossary wizard. (Right) Add a new child to the glossary.

En particular, si uno hace clic derecho en el nombre del nodo, como en la siguiente figura, se abrirá un panel. Permite al usuario agregar un (o más) hijo o palabra al nodo. En ambos casos, el usuario deberá rellenar los campos obligatorios. Observamos que si el usuario elige agregar una palabra a través del elemento del panel, la palabra se creará desde cero y se agregará a la lista de Word después de guardarla. Para agregar una palabra existente, el usuario tiene que arrastrar y soltar la palabra de la lista al nodo.

.. \_additemstonode:
.. figura:: media/image463.png

    Add items to the node(s).

Complete la estructura de árbol del glosario. Utilice las características del panel de cada nodo o del propio glosario (recuerde hacer clic derecho en los elementos para obtener dicho panel) para agregar, modificar, inspeccionar o eliminar elementos.

## Uso del glosario

Esta funcionalidad se perfila de acuerdo con el rol de usuario e incluye características que permiten

*   visualizar el glosario,
*   visualizar las asociaciones,
*   gestionar las asociaciones entre el glosario y los documentos,
*   gestionar las asociaciones entre el glosario y los conjuntos de datos.

Seleccionar **Uso del glosario** en el menú contextual Catálogos, el usuario se encuentra con la página que se muestra a continuación. Aquí hay cuatro pestañas disponibles:**Glosario**, **Navegación**, **Gestión Documental** y **Administración de conjuntos de datos**.

.. figura:: media/image464.png

    Glossary Usage graphic interface.

La pestaña Glosario ofrece la posibilidad de visualizar los glosarios existentes. Seleccione un glosario del cuadro combinado disponible en esta página para inspeccionar sus elementos. Utilice el icono con una "i" con un círculo para visualizar los detalles del elemento relacionado, como se muestra a continuación. Tenga en cuenta que está habilitada la posibilidad de buscar una palabra utilizando el cuadro de investigación configurado.

.. figura:: media/image465.png

    Visualization of glossary details.

Las rutas de navegación se pueden explorar en la segunda pestaña. Esta ventana tiene una lógica asociativa que facilita la navegación por las asociaciones. En otros términos, aquí es posible verificar las relaciones entre documentos o conjuntos de datos y palabras de un glosario. Un
ejemplo se da en la siguiente figura.

.. figura:: media/image466.png

    Navigation tab window.

Para utilizar esta funcionalidad, seleccione un glosario utilizando el cuadro combinado designado disponible en la parte superior de la columna "palabra". La ventana mostrará todas las palabras asociadas a ese glosario. Al seleccionar una de esas palabras, se mostrará una lista de documentos en el área en el medio de la página. Utilice el icono i con un círculo para inspeccionar los detalles del documento y, además, para ejecutarlo. De hecho, el botón "Ejecutar" está disponible en la esquina inferior derecha del panel de detalles, como se muestra a continuación.

.. figura:: media/image46768.png

    Execution documents by means of the glossary.

Los filtros elegidos por el usuario se pueden eliminar a través del icono rojo del filtro o seleccionando el **Borrar filtro** botón |image475| ubicado en la esquina superior derecha de la lista de palabras.

.. |imagen475| imagen:: media/image469.png
:ancho: 30

Tenga en cuenta que es posible inspeccionar los detalles de cada elemento utilizando el icono específico.

La pestaña Gestión de documentos es el lugar donde establecer las asociaciones entre los documentos analíticos y las palabras de un glosario. Esta funcionalidad se perfila a través de la autorización **Administrar glosario técnico**.

La página se compone de tres colums: el de "documentos" uno a la izquierda, la "palabra" en el centro y el "glosario" a la derecha. Para asociar una palabra a un documento o ver qué palabras están relacionadas con él, el usuario debe seleccionar un documento de la lista de la columna del lado izquierdo. Luego es obligatorio seleccionar un glosario del cuadro combinado disponible en la columna del lado derecho. Finalmente, arrastre y suelte palabras desde el árbol del glosario hasta la columna "palabra" en el centro de la página. Tenga en cuenta que el usuario debe arrastrar y soltar la palabra al principio de la lista: cuando aparece un cuadro azul claro con bordes punteados es posible finalizar la acción. Para anular la selección, el usuario puede hacer clic en el icono |image476| aparte de cada palabra. Este procedimiento se resume en la figura a continuación.

.. |imagen476| imagen:: media/image470.png
:ancho: 30

.. figura:: media/image47172.png

    Managing the association with a document: (Left) Select the documnet. (Right) Associate one (or more) word(s).

Si uno vuelve a la pestaña de navegación y selecciona el glosario utilizado en el paso anterior, es posible verificar la asociación que acaba de establecer.

Del mismo modo, la función de administración de conjuntos de datos permite al usuario establecer las asociaciones entre conjuntos de datos y glosarios. La siguiente figura muestra un ejemplo. La ventana se divide en cuatro áreas: **Conjunto de datos**, **Conjunto de datos/Word**, **Columna/Palabra** y **Glosario**. Primero, el usuario debe seleccionar un conjunto de datos en el área izquierda. El conjunto de datos elegido se resalta y sus campos aparecen en el área Columna/Word. Ahora, el usuario selecciona un glosario usando el cuadro combinado en el área del lado derecho. Finalmente, el usuario puede arrastrar y soltar palabras desde el árbol del glosario al conjunto de datos o a los campos individuales del conjunto de datos.

.. \_datasetmanagmtab:
.. figura:: media/image473.png

    Dataset management tab.

Una vez que los conjuntos de datos o los documentos están vinculados a los glosarios, el usuario puede ingresar al elemento de menú Uso del glosario para navegar fácilmente por el
elementos dentro de la suite Knowage.

## Funcionalidad de Ayuda en línea

El usuario puede inspeccionar la asociación de un elemento analítico específico (conjunto de datos, documento o modelo) utilizando el **Ayuda en línea** funcitonalidad. Se puede llegar a este último:

*   desde el explorador de documentos,
*   desde la barra de herramientas de cada documento, una vez iniciado,
*   de cada conjunto de datos,
*   de cada entidad del modelo Qbe,
*   de los informes Birt,
*   desde la cabina.

Como ejemplo, mostramos en la figura a continuación la interfaz gráfica que el usuario encontrará una vez que haya lanzado un documento y desee utilizar la funcionalidad de Ayuda en línea.

.. figura:: media/image474.png

    Help Online wizard.
