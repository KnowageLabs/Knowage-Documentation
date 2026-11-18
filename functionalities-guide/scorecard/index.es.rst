# Scorecard

El **Scorecard** La función, disponible en la suite Knowage como se destaca en la siguiente figura, permite supervisar diferentes KPI al mismo tiempo. Esta opción ofrece una visión general completa exclusiva de la situación de los KPI cuando el usuario no está interesado en una comprobación de umbral único. De hecho, esta herramienta es útil cuando se trata de supervisar la superación de dos o más valores críticos de KPI.

.. \_scorcardforthecontmenu:
.. figura:: media/image161.png

    Scorecard from the contextual menu.

## Desarrollo de cuadros de mando

Un cuadro de mandos está estructurado en niveles jerárquicos. En breve, hay un primer nivel llamado **Perspectiva** compuesto por KPIs agrupados en objetivos. De otra manera **Objetivos** se les asigna un umbral en función de los KPI de los que se componen. A continuación describiremos en detalle una configuración de cuadro de mandos. Al hacer clic en el elemento de menú Cuadro de mandos, se abre la ventana de la figura siguiente. Aquí se enumeran los cuadros de mando implementados y se pueden explorar una vez seleccionados y editados.

.. \_scorcardwindow:
.. figura:: media/image162.png

    Scorecard window.

El icono "Plus" disponible en la esquina superior derecha de la página abre una nueva ventana donde establecer un nuevo cuadro de mandos, como se muestra a continuación. Asigne un nombre y haga clic en **Añadir perspectiva** (Figura a continuación).

.. figura:: media/image163.png

Definición de un nuevo cuadro de mandos.

Una perspectiva le permite organizar el monitoreo sobre los objetivos.

.. figura:: media/image164.png

    Add perspective to the scorecard.

En la siguiente figura se da un ejemplo.

.. \_perspectlistexample:
.. figura:: media/image165.png

    Perspective list example.

De hecho, cada perspectiva gestiona uno o más objetivos de acuerdo con los requisitos del usuario. Un destino consta de uno o más KPI y se le asigna un color umbral según el elegido **Criterio de evaluación**. De hecho, si uno selecciona:

*   **Política "Mayoritaria"** el objetivo obtiene el umbral del umbral de KPI que supera numéricamente a los demás,
*   **Política "Mayoría con prioridad"** el objetivo obtiene el umbral de un KPI específico,
*   **Política "Prioritaria"** el objetivo obtiene el umbral mayoritario de los KPI en caso de que el KPI primario declarado devuelva el umbral inferior, es decir, el "verde", mientras que obtiene el umbral de un KPI declarado primario en caso de que este último devuelva los otros umbrales, a saber, el "amarillo" o el "rojo".

.. advertencia::
**Los umbrales de los KPI seleccionados deben tener los colores correctos**

       Note that the scorecard shows the right colors accordingly with the selected policy only if the KPIs which compose the targets          have **no filters** and **standard colors** (see Section 7.1, Step 2 for definitions) to highlight the threshold.

.. advertencia::
**Colores "estándar" para umbrales**

       When the targets contain parametric KPIs the target/perspective evaluation cannot be completed for value absence. Therefore the          warning lights turn grey. The right visualization of the scorecard must be implemented through a scorecard document. Check              Section 8.2 to have more details on how to develop a scorecard document.

A continuación se muestra un ejemplo.

.. figura:: media/image166.png

    Select the KPI with priority.

La misma opción está disponible en el nivel de perspectiva (consulte la siguiente figura), es decir:

*   **Política "Mayoritaria"** la perspectiva obtiene el umbral del umbral objetivo que supera numéricamente a los demás,
*   **Política "Mayoría con prioridad"** la perspectiva obtiene el umbral de un objetivo específico,
*   **Política "Prioritaria"** la perspectiva obtiene el umbral mayoritario de los objetivos en caso de que el objetivo principal declarado devuelva el umbral inferior, es decir, el "verde", mientras que obtiene el umbral de un objetivo declarado primario en caso de que este último devuelva los otros umbrales, a saber, el "amarillo" o el "rojo".

.. \_prespectpolicy:
.. figura:: media/image167.png

    Perspective policy.

Recuerde guardar una vez que se hayan establecido las perspectivas y los objetivos.

## Creación de un documento de cuadro de mandos

Una vez guardado, es posible desarrollar un documento de cuadro de mando que puede ser fácilmente consultado por los usuarios finales (autorizados). Para crear un documento de cuadro de mandos, haga clic en el icono "Más" disponible en el navegador de documentos y luego en "Documento genérico" del panel como se muestra a continuación. Aquí rellena

.. figura:: media/image168.png

    Create a generic document from document browser.

en los campos obligatorios (marcados con un asterisco) y seleccione el tipo KPI y **Motor KPI**. Luego abra la "Compilación de plantilla". Aquí seleccione la opción "Cuadro de mandos" como en la figura siguiente9 y, en consecuencia, Creación de un documento de cuadro de mandos, elija un cuadro de mandos existente de la lista. Realice las personalizaciones deseadas y guárdelas.

.. figura:: media/image169.png

    Template creation window.

La siguiente figura muestra un ejemplo de la interfaz del documento del cuadro de mandos. Las flechas señalan las perspectivas de logro de los objetivos o, por el contrario, la falta de los objetivos. Además, el logro / fracaso de los objetivos individuales se identifica mediante las señales de flecha cerca de cada objetivo.

.. figura:: media/image170.png

    Scorecard document interface.

Tenga en cuenta que es posible verificar la política utilizada para cada perspectiva. De hecho, al hacer clic en uno de ellos se abre un asistente que muestra la política adoptada y el objetivo obtenido por ach KPI.

.. figura:: media/image170.png

    Scorecard document interface.
