# Programador

Knowage scheduler permite programar la ejecución de uno o más documentos analíticos publicados en el Servidor. Los documentos ejecutados por el programador se pueden distribuir a lo largo de diferentes canales de despacho. A continuación describimos cómo crear una actividad, programarla y despachar los resultados.

## Crear una actividad

Para definir una nueva actividad programada, el administrador debe especificar qué documentos componen la actividad y cómo ejecutarlos. La lista de todas las actividades programadas se puede ver seleccionando **Herramientas** > **Programador**. Para crear una nueva actividad, haga clic en el icono "Más" en la parte superior de la página en el área izquierda. En la siguiente figura puede ver la página principal del programador y la nueva GUI de actividad.

.. figura:: media/image4041.PNG

Izquierda: página principal del programador. Derecha: Nueva GUI de actividad

Asigne un nombre y una descripción a la nueva actividad. Luego seleccione los documentos que lo componen haciendo clic en el icono "Más" y seleccionándolos del asistente emergente, consulte la Figura a continuación.

.. figura:: media/image42.png

Agregar un documento a una actividad.

Ahora debe especificar cómo el programador debe manejar los controladores analíticos de cada documento seleccionado que tenga parámetros.

.. \_manageparameters:
.. figura:: media/image43.png

Administrar parámetros.

Hay dos posibilidades:

*   seleccionar un valor de los disponibles para el controlador analítico específico en el momento de la definición;
*   ejecutando el informe una vez para cada posible valor del controlador analítico.

Una actividad programada puede estar compuesta por más de un informe. También es posible añadir el mismo informe a una actividad programada más veces. Puede utilizar el icono |image50| para duplicar fácilmente un documento. Una vez que se hayan agregado todos los documentos deseados y se haya configurado la configuración de administración de sus parámetros, guarde la actividad haciendo clic en el botón Guardar. La nueva actividad se muestra en la lista y se puede modificar o eliminar utilizando los iconos específicos previstos.

.. |image50| imagen:: media/image44.png
:ancho: 30

Puede administrar su actividad en cualquier momento simplemente haciendo clic en el nombre del elemento de programación (lado izquierdo de la ventana) y todas sus características se mostrarán a un lado (mitad derecha de la ventana).

Para ver y modificar la lista de los horarios asociados a una actividad, haga clic en el icono "Más" que se encuentra en el área de schedulation en la parte inferior derecha. Del mismo modo, haga clic en el mismo botón para asociar horarios
a actividades de nueva creación.

Se abren los detalles de la schedulación (Figura a continuación).

.. figura:: media/image45.png

    Schedulation detail panel.

Está compuesto por dos áreas: **Detalle** y **Gestión de documentos**.
La pestaña de detalles le permite establecer todas las propiedades de su schedulation. De hecho, aquí usted decide su nombre, descripción y momento.
Se puede hacer una schedulation en una fecha y hora elegidas si usted elige **Ejecución única** como tipo.
De lo contrario, se puede realizar por períodos fijos o comenzar en un evento fijo.

Puede decidirlo, eligiendo el tipo de schedulation.

Los tipos de schedulation disponibles son:

*   Ejecución única;
*   Ejecución personalizada;
*   Ejecución de eventos.

Un **Ejecución única** es una ejecución fija para una fecha y una hora que ocurre solo una vez. Un **Ejecución personalizada** repite su programación periódicamente de acuerdo con su configuración. El **Ejecución de eventos** inicia la programación cuando ocurre un evento.

Puede elegir entre estos tipos de eventos:

*   Servicio REST,
*   Cola JMS,
*   Mensaje de ContextBroker,
*   Verificación de conjuntos de datos.

Si eliges **Verificación del conjunto de datos**, debe seleccionar un conjunto de datos estructurado a la derecha. Tiene que dar como resultados sólo verdadero o falso. A continuación, establezca la frecuencia en segundos. Esta es la frecuencia con la que se verificará el conjunto de datos. Por ejemplo, si lo establece en 10 segundos, significa que cada 10 segundos se ejecuta el conjunto de datos. Si el resultado de su ejecución es verdadero, la schedulation se triza de lo contrario no lo es.

Una vez que haya terminado, cambie al **Gestión Documental** pestaña.

.. figura:: media/image46.png

    Document management.

Aquí puede encontrar las configuraciones de despacho, que pueden ser diferentes para todos los documentos que componen la actividad programada. Todos los documentos que componen la actividad tienen su propia configuración de despacho y el mismo documento se puede distribuir a lo largo de múltiples canales de despacho. Puede cambiar entre los documentos incluidos en su actividad haciendo clic en su nombre en la barra de herramientas superior. Hay muchos canales de despacho posibles diferentes que se pueden utilizar para distribuir los resultados de la ejecución de una actividad programada:

*   Guardar como instantánea,
*   Guardar como archivo,
*   Guardar como documento,
*   Enviar a la clase Java,
*   Enviar correo

En los siguientes apartados los explicamos en detalle.

Guardar como instantánea

```

The executed document can be saved as snapshots in cyclic buffers of configurable size. For example, it is possible to store in the buffer the last 12 snapshots (the **History Length** field) of one report, scheduled to be executed one per month, in order to have a one-year long history.

The list of all snapshots contained in the buffer can be accessed from the **Show scheduled executions** contained in the **Shortcuts** menu. You can find it in the document toolbar at the top right corner. Each snapshot can be opened or deleted from this panel. These steps are shown in the following figure. A snapshot contains data queried from the database at the moment of its execution performed by the scheduler.

.. figure:: media/image47.png

    Steps to open saved snapshots

Save as file
~~~~~~~~~~~~

The executed document can be saved as file on the filesystem in the path /knowage-<version> /resources (if no destination folder is specified). Otherwise, you can create the relative path of this subfolder by writing your subfolder name. For instance, if you write “MyFirstScheduler” as file name and “Schedulation” as destination folder, after the schedulation execution a subfolder Schedulation containing the file “MyFirstScheduler” is created in /knowage-<version> /resources. If the subfolder Schedulation already exist your file is added to this subfolder. You can have a look at the form in Figure below.

.. figure:: media/image51.png

   Save as File form.
   
If you prefer to generate a .zip file containing the scheduled documents, you can check the dedicated mark.

Save as document
```

El documento ejecutado se puede guardar como un **Informes ad hoc** en el árbol de funcionalidades de Knowage. La ejecución del documento se guardará en la carpeta especificada y será visible para todos los que puedan acceder a esa carpeta en particular. Para aquellos documentos cuya ejecución se repite sobre un valor de parámetro, también es posible utilizar el valor del parámetro para decidir a qué carpeta se enviará el documento. Para ello, defina un conjunto de datos de asignación compuesto por dos columnas:

*   el primero contiene un valor de parámetro específico;
*   el segundo que contenga la etiqueta de la carpeta donde se expedirá el documento cuando se ejecute el documento con el valor de parámetro correspondiente.

Una vez que haya definido el conjunto de datos de asignación, puede usarlo en las opciones de configuración del despachador de documentos. Al igual que en el caso anterior, el programador ejecutará el informe una vez para cada valor posible del parámetro. Esta vez, sin embargo, los resultados de la ejecución se distribuirán en diferentes carpetas, de acuerdo con la asignación definida en el conjunto de datos.

Enviar a la clase Java

```

The executed document can be sent to a Java class implementing a custom dispatch logic. The custom class must extend the abstract class JavaClassDestination that implements the method execute. This method is called by the scheduler after document execution. Below an example of Java class.
   
.. code-block:: java
         :linenos:
         :caption: Java Class Code Example.

            package it.eng.spagobi.tools;
            import it.eng.spagobi.analiticalmodel.document.bo.BIObject
            public abstract class JavaClassDestination
            implements IJavaClassDestination {
            BIObject biObj=null;
            byte[] documentByte=null;
            public abstract void execute();
            public byte[] getDocumentByte() { 
            return documentByte;
            } public void setDocumentByte(byte[] documentByte) {
            this.documentByte = documentByte;
            }
            public BIObject getBiObj() {
            return biObj;
            }
            public void setBiObj(BIObject biObj) {
            this.biObj = biObj;
            }
            }


The method getDocumentByte can be used to get the executed document, while the method getBiObj can be used to get all metadata related to the executed document. The following code snippet shows an example of a possible extension of class JavaClassDestination.
   
.. code-block:: java
         :linenos:
         :caption: JavaClassDestination example.

         public class FileDestination extends JavaClassDestination {
         public static final String OUTPUT_FILE_DIR = "D:\\ScheduledRpts\\";
         public static final String OUTPUT_FILE_NAME = "output.dat";
         private static transient Logger logger = Logger.getLogger(FileDestination.class);
         public void execute() {
         File outputDir;
         File outputFile;
         OutputStream out;
         byte[] content = this.getDocumentByte();
         String outputFileName;
         logger.debug("IN");
         outputFile = null;
         out = null;
         try {
         outputFileName = getFileName();
         logger.debug("Output dir [" + OUTPUT_FILE_DIR + "]");
         logger.debug("Output filename [" + outputFileName + "]");
         outputDir = new File(OUTPUT_FILE_DIR);
         outputFile = new File(outputDir, outputFileName);
         if(!outputDir.exists()) {
         logger.debug("Creating output dir [" + OUTPUT_FILE_DIR + "] ...");
         if(outputDir.mkdirs()) {
         logger.debug("Output dir [" + OUTPUT_FILE_DIR + "] succesfully created");
         } else {
         throw new SpagoBIRuntimeException( "Impossible to create outputd dir
         [" + OUTPUT_FILE_DIR + "]");
         }
         } else {
         if(!outputDir.isDirectory()) {
         throw new SpagoBIRuntimeException( "Outputd dir [" + OUTPUT_FILE_DIR + "]
         is not a valid directory");
         }
         }
         try {
         out = new BufferedOutputStream( new FileOutputStream(outputFile));
         } catch (FileNotFoundException e) {
         throw new SpagoBIRuntimeException(
         "Impossible to open a byte stream to file
         [" + outputFile.getName() + "]", e);
         } try {
         out.write(content);
         } catch (IOException e) {
         throw new SpagoBIRuntimeException( "Impossible to write on file
         [" + outputFile.getName() + "]", e);
         }
         } catch(Throwable t) {
         throw new SpagoBIRuntimeException( "An unexpected error occurs while saving
         document" + " to file [" + outputFile.getName() + "]", t);
         } finally {
         if(out != null) {
         try {
         out.flush(); out.close();
         } catch (IOException e) {
         throw new SpagoBIRuntimeException( "Impossible to properly close file
         [" + outputFile.getName() + "]", e);
         }
         }
         logger.debug("OUT");
         }
         }
         private String getFileName() {
         String filename = "";
         BIObject analyticalDoc;
         List analyticalDrivers;
         BIObjectParameter analyticalDriver;
         String extension = "pdf";
         analyticalDoc = getBiObj();
         analyticalDrivers = analyticalDoc.getBiObjectParameters();
         for(int i = 0; i < analyticalDrivers.size(); i++) {
         analyticalDriver = (BIObjectParameter)analyticalDrivers.get(i);
         String parameterUrlName = analyticalDriver.getParameterUrlName();
         List values = analyticalDriver.getParameterValues();
         if(!parameterUrlName.equalsIgnoreCase("outputType")){
         filename += values.get(0);
         } else {
         extension = "" + values.get(0);
         }
         }
         filename = filename.replaceAll("[^a-zA-Z0-9]", "_");
         filename += "." + extension;
         return filename;
         }
         }

The class FileDestination copies the executed documents to the local filesystem in a folder named D:\\textbackslashScheduledRpts . The name of the report file is generated concatenating all the parameter values used by the scheduler during execution. Once implemented and properly compiled, the Java class must be exposed to the classpath of Knowage web application. For example, you can pack the compiled class into a .jar file, copy it into the lib folder of Knowage web application and restart the server. As a last step, it is necessary to assign the fully qualified name of the new class, e.g., it.eng.spagobi.tools.DestinationFile., to the configuration property classpath.

Send mail
~~~~~~~~~

.. important::
         **Enterprise Edition only**

         This feature is available only with KnowageER and KnowageSI, submodules of Knowage Enterprise Edition

The executed document can be sent to one or more mail recipients. The list of mail addresses to be used to forward the executed document can be defined in three different ways:

-  statically;
-  dynamically, using a mapping dataset;
-  dynamically, using a script.

In Figure below you can have a look at the mail form. In the following we will focus on each typology, clicking on the info icon you get detailed information.

.. figure:: media/image52.png

    Sending mail form.

Static list
^^^^^^^^^^^^

If you want to choose a static list, check the option **Fixed list of recipients** and fill the configuration property **Mail to** with the list of desired mail addresses separated by a comma. An mail for each executed document will be sent to all the mail addresses contained in the list.

Dynamic list with mapping dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, you have to define a two-column dataset:

-  the first containing a specific parameter value;
-  the second containing each mail address the executed document should be dispatched to.

   You can see an example of dataset in the following Figure.
   
.. figure:: media/image54.png

Example of mapping dataset for dynamic distribution list

Basically, when the parameter has a given value, the document will be sent to the corresponding email address. Once you have defined the mapping dataset, you can use it in the configuration settings of the document dispatcher. With this configuration, the scheduler will execute the report one time for each possible value of the parameter **Position**, then dispatching the results to different recipients. Specifically, all execution results passing a value of the **Position** parameter to the report starting with VP will be sent to ``name1surname1@gmail.com``, the ones starting with HQ will sent to ``name2surname2@gmail.com`` and the ones starting with President will be sent to ``namesurname@gmail.com``.

Dynamic List with script
^^^^^^^^^^^^^^^^^^^^^^^^

Check the option **Use an expression** and assign a value to the configuration property **Expression** with a parameter-dependent expression like the following:

.. code-block:: bash
         :linenos:

         $P{dealer}@eng.it

Here dealer is a document parameter label (``$P{dealer}`` will be replaced by the parameter value of the scheduled execution).

Schedulation panel
------------------

To conclude our overview on the scheduler features, save your settings and go back to the main scheduler page.

Here you can select one of the available scheduled activities to explore details. 

.. figure:: media/image55a.png

    Exploring the detailed of a scheduled activity.

A general overview of the selected schedulation is given in the right side of the page. You can inspect two tabs: **Overview activity** and **Detail**. In the Overview activity tab the main details of the schedulation are displayed summed up. Namely it is showed the documents involved, the related parameters and their eventually default values, what kind of scheduling has been chosen (Single Execution, Customized Execution or Event Exectution), the start date and so on. Note that at the end of the row you have the possibilities to explore more details by clicking on the “three dots” icon.

Here you find the following information:

- **Schedulation informations**, it give some extra information about your schedulation concerning sending emails
   
- **Schedulation detail**, it opens the scheduling configuration and let you change them.
   
   .. figure:: media/image57.png

    Schedulation information pop up example
    
- **Execute now**, by clicking it you immediately start the execution of your schedulation.
- **Pause schedulation**, it lets you pause your schedulation.
- **Resume schedulation**, it appears after having paused a schedulation, it enables you to resume it.
- **Delete Schedulation**, it lets you delete a schedulation.

In the **Detail** tab you can analyze the settings on document, that is which parameters are associated to it and how to manage them.

.. _scheduldettab:
.. figure:: media/image58.png

    Schedulation detail tab

Scheduler Monitor
----------------------

You can monitor the whole scheduling situation by entering the **Scheduler Monitor** item from the Knowage Menu. This feature allows you to check which schedulations are active in a certain future time interval and, eventually, to be redirected to the schedulation area in order to modify the selected schedulation.
  
.. figure:: media/image59.png

    Schedulation detail tab
```
