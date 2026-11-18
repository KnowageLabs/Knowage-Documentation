# Galería de widgets

El **Galería de widgets** es una funcionalidad disponible desde la versión 8.0 que permite a los usuarios y editores crear una plantilla y compartirla en varios paneles.
Al crear una plantilla y luego usarla dentro de un panel, los usuarios tendrán la capacidad de crear elementos complejos del panel de control de manera bastante fácil y rápida, manteniendo una plantilla base común.

Esta funcionalidad está disponible para:

*   Widget HTML
*   Widget gráfico personalizado
*   Widget de Python

El primer paso es crear una galería de plantillas o subir alguna plantilla.

## Gestión de galerías

Dentro del panel de administrador debe aparecer un nuevo elemento denominado **Gestión de galerías**.
Este enlace lo llevará a la administración de la galería, la galería de creación de plantillas de widgets.

.. figura:: media/image2.png

    Gallery management example.

En la parte izquierda de la interfaz está disponible la lista de las plantillas de widgets. Al principio, esta sección probablemente estará vacía.

Hay dos formas de agregar nuevas plantillas:

*   Agregar una nueva plantilla
*   importar una plantilla

Si está agregando una nueva plantilla, verá la sección de detalles a la derecha y tendrá la posibilidad de crear una plantilla.

Usando la importación verá un cuadro de diálogo para elegir la plantilla a importar. Al hacer clic en "importar", se agregará a la lista actual.

Un **Plantilla** es un archivo json que contiene una colección de propiedades que describen el widget y el código que lo compondrá.

Estarán presentes los siguientes campos:

*   **Nombre**: Obligatorio. El nombre de la plantilla de widget
*   **Tipo**: Obligatorio. El tipo de widget.
*   **Tipo de salida**: Disponible solo para el widget de Python. Establecerá el tipo de salida del código python.
*   **Descripción**: Opcional. La descripción de la plantilla de widget será visible como información sobre herramientas en la selección del panel.
*   **Etiquetas**: Opcional. Una lista de etiquetas únicas para categorizar fácilmente las plantillas. También es posible buscar usando etiquetas. Los valores permitidos para las etiquetas son letras mayúsculas y minúsculas, números, '-', '\_'. El carácter de espacio no está permitido.
*   **Imagen**: Opcional. La imagen del widget que se mostrará en la selección del panel. El tamaño máximo de la imagen es de 200k.
*   **Sección de código**: Obligatorio. El editor de código.

Dependiendo del tipo de widget seleccionado, los editores disponibles cambiarán de esta manera:

*   **Widget HTML**: Editores HTML, CSS
*   **Widget de gráfico personalizado**: Editor HTML, CSS y JS
*   **Widget de Python**: Editor de código Python

.. figura:: media/image1.png

    Selected widget template.

Para guardar la plantilla, es posible hacer clic en la barra de herramientas superior derecha en el *salvar* botón. Si el botón Guardar está deshabilitado, uno o más campos obligatorios están vacíos o no son válidos.
También es posible exportar la única plantilla seleccionada o simplemente cerrar la página y elegir otra.

.. figura:: media/image3.png

    Toolbar icons.

## Galería de paneles

Dentro de la funcionalidad de la cabina o del tablero, una nueva pestaña estará presente al crear un nuevo widget de los tipos disponibles.

.. figura:: media/image4.png

    New widget templates list.

Esta pestaña no estará disponible cuando no se defina ninguna plantilla y si el widget se abre después de que se guarde por primera vez.

La primera plantilla siempre será la "vacía", para permitir a los usuarios crear un widget personalizado sin partir de una plantilla.
Las otras plantillas estarán disponibles después de la vacía y mostrarán la imagen, las etiquetas establecidas por el editor y, al pasar el cursor, la descripción de la plantilla.

Al hacer clic en un elemento, el código establecido en la administración de la galería se copiará en la nueva plantilla de widget, preparando el widget para las personalizaciones definitivas.
El usuario solo tendrá que vincular datos dinámicos o cambiar la sección css específica para crear el widget deseado.

.. figura:: media/image5.png

    Selected template editor.
