Engine description\*
--------------------------

The **Data Mining Engine** is thought and implemented in order to supply KnowAge with data mining capabilities, but it also enhances OS R and Python with several distinguishing features.

Basically the integration is done through the rJava R package, JRI library and the JPY lbrary for Python. R/Python scripts are written inside the data mining documents template and evaluated server side once the document is executed. Nevertheless, developers can combine several scripts, each one with its own outputs.

The leading component is the command object, that holds the activation of one script, together with its outputs. There can be many commands, but the one which is executed at document start up, is the one with mode set to auto, whilst all of the others will be executed once user clicks on the corresponding element.

Data
~~~~

Each script can run on two kinds of datasets. The first one is the file type, that means users can upload their files, interacting with the GUI. Note that the extension of the file, as well as how to read it (comma separated or tab separated, is header present or not,...) can be specified in the proper DATASET tag in document’s template. The other type of dataset is the Knowage Parametrization and customization dataset. This feature allows to use inside your R scripts data retrieved from many kind of sources, without ad-hoc R packages utilization.

Moreover this is very useful for Big Data data sources (Hive, Impala, Hbase, NoSQL databases as MongoDB, OrientDB, Cassandra etc..), because not all of them are connectable from R, and if they are, in most cases, R must be istalled on their cluster.

Therefore this is the first powerful feature Knowage adds to R. Each Knowage dataset is readable as a CSV file, so developers must apply the proper functions.

Parametrization and customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another characteristic is that the data mining document is customizable both with Knowage Analytical driver and GUI variables. The first choice, enables developers to use the behavioural model to change the results of the Knowage datasets used by the scripts. These parameters don’t modify other data mining document’s parts. On the other hand, setting GUI variables can be useful to change the outputs of the scripts, but they don’t affect the resultsets of the datasets.

As explained at the beginning of the chapter, there are two kind of variables: output variable and command variable. Once the user runs again the document by saving the value of the variable, the value is passed to the output function. On the other hand, by choosing the second option the whole script belonging to the command will benefit of the variable update.

Outputs
~~~~~~~

Knowage data mining document can perform a set of scripts and visualize them according to the associated predefined outputs, that can be images as well as text. This combination of results, that can be modified on-the fly using variables and shared across the network through Knowage web application, can exploit R workloads. Indeed Knowage can provide role’s privileges to the document’s access or execution.

My first data mining document\*
-------------------------------------

Create a new generic document and select **Data Mining** as Type and **Data-Mining Engine** as Engine. Define label, name and description and associate the correct datasource. The next step is the definition of the template.

The template of a data mining document is a simple XML file that enables the developer to configure properly the document behaviour.   Look at Linux and Tomcat example. 

       .. code-block:: xml
         :caption:  Linux and Tomcat example
         :linenos:
 
         <?xml version="1.0" encoding="ISO-8859-15"?> 
         <DATA_MINING>                                
         <DATASETS>                                                            
         <DATASET name="fileDS" readType="table" type="file"                
         label="Dataset_Label_01 " canUpload="true">                        
         <![CDATA[ ...read_options...]]>                                   
         </DATASET>                                                         
         </DATASETS>                                                           
              <SCRIPTS>                                                             
              <SCRIPT name="Script_Name_01" datasets="fileDs"  label="Script_Label_01">                                           
                <![CDATA[.... action_to_call<-function(x){ ... }]]>                
              </SCRIPT>                                                          
              <SCRIPT name="Script_Name_02" datasets="fileDs"  label="Script_Label_01">                                          
         <![CDATA[... z1<-'$P{var1}' ... ]]>                               
              </SCRIPT>                                                          
              <SCRIPT name="Script_Name_03" label="Script_Name_03">              
               <![CDATA[... z2<-$P{var2} ... ]]>                                  
              </SCRIPT>                                                          
              </SCRIPTS>                                                            
            <COMMANDS>                                                            
              <COMMAND name="command1" scriptName="Script_Name_01" label=" Command_Label_01" mode="auto">                                               <OUTPUTS>                                                          
                <OUTPUT type="image" name="a" value="x" function="plot" mode="auto" label="Output_Label_01"/>                                           <OUTPUT type="image" name="c" value="z,k" function="biplot" mode=" manual" label="Output_Label_02"/>                                     <OUTPUT type="text" name="d" value="y" mode="manual" label="   Output_Label_03"/>                                                       </OUTPUTS>                                                         
            </COMMAND>                                                         
              <COMMAND name="command2" scriptName="Script_Name_02" label=" Command_Label_01" mode="manual" action="function1(x)">                        <VARIABLES>                                                        
                    <VARIABLE name="var1" default="valuevar1"/>                        
                </VARIABLES>                                                       
                <OUTPUTS>                                                          
                <OUTPUT type="text" name="c" value="z" function="function2(y,z)"  mode=" manual" label="Output_Label_01"/>                               </OUTPUTS>                                                         
           </COMMAND>                                                         
          <COMMAND name="command3" scriptName="Script_Name_03" label=" Command_Label_03" mode="manual" action="action_to_call">                         <OUTPUTS>                                                          
               <OUTPUT type="text" name="e" value="z2" mode="manual" label=" Output_Label_01">                                                       <VARIABLES>                                                       
            <VARIABLE name="var2" default="valuevar2"/> </VARIABLES>           
               </OUTPUT>                                                          
               <OUTPUT type="image" name="f" value="" function="rectf(z)" mode="auto" label="Output_Label_02"/>                                        </OUTPUTS>                                                         
          </COMMAND>                                                         
          </COMMANDS>                                                           
          </DATA_MINING>                                                        


  As you can see in the example, there are six basic tags:

-  COMMANDS: the leading objects. They call a script execution and can have multiple outputs. They enable interactive document execution where only command in mode=''auto'' is executed automatically. The mode=“manual” requires the user’s click.

-  OUTPUTS: to define which results have to be shown. They work with the Images. Text is the string representation of the script result, while *Image* is the chart generated by R. There are also predefined functions (histogram, plot, biplot) or developer’s functions that generate the output recalled by function.

-  SCRIPTS: they contain the R script (including objects definitions, pre-processing and functions). There can be many scripts depending on commands. The main function execution can be recalled (if needed) by the action attribute. The main script is executed once. Outputs will look for the objects in the user’s workspace.

-  DATASETS: the data used by the scripts. They are executed at the beginning of the document’s execution so that data.frames can be used further by every script. There are two dataset types:

-  file: csv, delim, text, etc., manually loaded by the end user at document execution time;

-  Knowage datasets: defined by label in document’s template, whose resultset is converted in CSV. They can use analytical drivers.

-  PARAMETERS: they corresponds to Knowage analytical drivers and can influence the behaviour of the Knowage dataset. They cannot be   applyed to other components.

-  VARIABLES: are required for changing factors or more generally parameters (strings or numbers) inside the script (referenced by a command) or the output functions.


Once the template has been edited it can be upload on Knowage server to create a usable Data Mining document. Enter then Knowage document browser and click on the “Plus” icon. The insert all mandatory fileds as label, name, engine and datasource. Then you must upload the template file cliking on the icon available at the bottom of the form, highlighted in Figure 16.31.


   |image433|

   Figure 16.31: Creating a new function.


Create a new function in the Function Catalog
--------------------------------------------------

To create a new Function you must click on the “Plus” icon available at the right top side of the page. The action will provoke the opening of the window in Figure 16.32 made up of 4 tabs.

   |image434|

   Figure 16.32: Creating a new function.

-  **General**: here you have to set the Function name, the label which identifies the function univocally, the name of the user who creates the function, the type to which the function belongs to and a brief description of the function usage.

-  **Input**:

   |image435|

   Figure 16.33: Input tabs.

Use the icon |image436| to insert a new dataset or a new variable. And use the icon |image437| to delete the insertion. Choose a dataset from the combobox and use the “Preview button” to check the outcome. While for the variables you must specify the variable name and value. An example is give in Figure 16.34.

   |image440|

   Figure 16.34: Inserting variables.

-  **Script**: here is where the user is required to have knoledge of R or Python language. Figure 16.35 shows an example.

   |image441|

   Figure 16.35: Typing Python script

-  **Output**: referring to Figure 16.36, in the Output tab you have to choose how the output should be visualized. Still use the icon |image438| to insert a new output and the icon |image439| to delete the items. Then insert the output name and once again you can choose among “Text”, “Image”, “Dataset” for both Python and R.

   |image442|

   Figure 16.36: Choosing how to visualise outputs.

Then save and you are ready to use the function.


.. include:: dataminingThumbinals.rst
