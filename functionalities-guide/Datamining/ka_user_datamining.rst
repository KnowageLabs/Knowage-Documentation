
Data Mining
===========

Knowage supports advanced data analysis allowing you to extract knowledge from large volumes of data, to improve your decision-making
and business strategies. In particular, Knowage **Data Mining Engine** integrates R and Python scripting capabilities.

R is a programming language and software environment for statistical computing and graphics. The R language is widely used among statisticians and data miners for developing andvanced algorithms andm data analysis tools. Polls and surveys show that R’s popularity is continually increasing. As well, Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Rather than requiring all desired functionality to be built into the language’s core, Python was designed to be highly extensible and it is intended to be a highly readable language.

Thanks to Knowage **Data Mining Engine**, it is possible to execute multiple R and Pyhton scripts in an interactive way and visualise several outputs, including the powerful R graphics. Another importang thing to notice is that it allows users to perform statistical or data mining analysis on different files or Knowage datasets.

The data scientists can thus integrate its own algorithm within Knowage and deliver their output to the end user, together with new advanced visualization options useful to discover meaningful insights hidden in the data.

Data Mining document interface
-----------------------------------

Data Mining can be implemented using R or Python language as we just said. The starting point for developing a data mining document is to write down a template which consists of an XML file. We refer to My first data datamining document for a more detailed description of the template features. We disclose here that to comunicate the engine which language you are going to use you must add the tag **LANGUAGE** as shown in Code syntax to recall the variable input

.. figure:: media/image384.png

    Setting the language for data mining.

For both R and Python languages, the engine yields different kind of outputs. The outputs can be of type:

-  text,
-  dataset,
-  images,
-  html file (only when using the R language).

Once again the outputs are set at template level. In the following we will describe how to browse and visualise each type of output. The Data Mining document execution is very simple in all cases. Once configured the document, the execution starts clicking on the document’s icon from Knowage Document Browser interface as shown below.

.. figure:: media/image385.png

    Document browsing on server.

We suppose to open a document with text outputs. At the top of the page you find the command box. When the document is lauched, it is automatically executed with the default command (which is the one set to **auto** in the template file) and you get the corresponding outputs displayed in different tabs. If you wish to change the command to get other outputs you can use the dedicated combobox as emphasized in :numref:`selectingcommandapp`. We say in advance that the command are set in the template file. As you can check in :numref:`commandtags` the template must contain the **COMMAND TAGS**. In the example each command (two in this case) is made up of instructions to be executed in order to compute one or more measures.

.. _selectingcommandapp:
.. figure:: media/image386.png

    Selecting the command to be applied.
    
.. _commandtags:
.. figure:: media/image387.png

    The command tags.

The combobox will then reflect the command settings inside the template. Therefore it is important that the final user is told the meaning of each using “speaking” names or furnishing information with a documentation.

To switch to a different command, use the combobox and click on the target command. The simple click activates the execution.

The computed outputs are visualized in the half bottom of the page: each output populates a tab.

If the command refers to a script that needs one or more datasets, than these datasets are displayed between the command combobox and the outputs tabs. You can use the combobox which list the Knowage dataset matched to the document throught the template. Otherwise you can upload a file for Knowage datasets that cannot be changed from the GUI. Clicking on the **FILE** button it is possible to upload the file to replace the default dataset. Remember to click on the |image404| to start the upload. Then a **Run script** button will appear to re-execute the document as indicated in :numref:`executbuttupload`.

.. figure:: media/image389.png

    Changing dataset related to a command.

.. _executbuttupload:
.. figure:: media/image390.png

    Execution button after the upload.

As well as for other analysis tools, data mining allows to filter data through parameters. In this case the setting of the parameters can be done in the script tag or the command tag. The main parts of the code for the configuration of parameters are highlighted in figure below.

.. figure:: media/image391.png

    Setting parameters.

We will not go further into details of R or Python code so we leave the user to take care about the issue. Generally you can use two kind of parameters (when defined by developers): output parameters and command parameters. These may be required for changing factors or more generally fields (string or numbers) inside the script or in the output functions.

When dealing with output parameters, you can update the corresponding values by filling the input box appearing in the respective output tab panel. Once you re-run the document, the modifications are applied to a single output, the one which the parameter is associated to.

On the other hand, when dealing with command parameters, you can update the variable value by clicking the double gear icon (circled in :numref:`clickdoublebuttchange`) displayed next to the command name. The button updates the interface and opens a box (:numref:`changingparamvalues`) where you can change a convalidate the modification. The variable value is passed to the whole command and hence it updates the variables of all command outputs.

.. _clickdoublebuttchange:
.. figure:: media/image392.png

    Click on the double gear button to change the .

.. _changingparamvalues:
.. figure:: media/image393.png

    Changing the parameter values.

In case the commands produce image outputs the interface is essentially the same as the text output case. So you can change commands, dataset and set parameter values. The output tabs will though display data through graphics. An example is given below.

.. figure:: media/image394.png

    Image outputs.

Also in the dataset output case there are not considerable changes in the window organization. A Data Mining document with dataset output transform a query over a data source or a plain data container into a dataset on Knowage Server. For instance, this kind of output comes to be really useful when the user needs to convert a .xlsx or .csv file into a dataset on Server. The output tab will accordingly shows a message stating the name of the dataset as stored in Knowage Server, under Data Provider » data set menu item. The following figure gives an example.

.. figure:: media/image395.png

    Dataset outputs.

Only when using R language, the outputs can be set to html type. In this case, the document execution will provoke the opening of a web page containing the results requested through the command instructions.

Functions Catalog
----------------------

The Data Mining can also be managed through the **Functions** framework. In this section we will see how to explore and handle this part, while in Create a new function in Function Catalog we will see how to create a new function.

First click on the **Functions Catalog** from the Knowage main page as shown below.

.. figure:: media/image396.png

    Functions Catalog from Knowage menu.

You will enter a page like the one shown in figure below.

.. _functioncatalinterf:
.. figure:: media/image397.png

   Functions Catalog interface.

The actions that a user can perform depend on the user’s role. However, indipendently from the user’s role, once entered the feature all functions are shown by default. Referring to :numref:`functioncatalinterf`, one has the page made up of:

-  **categories**: these are set by an administrator user and are used to classify the functions accordingly to their definition and goals. Moreover they’re of help in browsing the functions; only the admin user can add and/or modify categories.

-  **tags**: they are used to easily sharpen the research and esily recall the functions that are tagged with that word; once again only the admin user can add and/or modify tags;

-  **list of functions** (if there are any): these are visible and explorable by any kind of user. Anyway only an admin user can add and/or modify them.

.. hint::
    **Add or modify the categories**
         
         The admin can add a new category using the Domain management available on Knowage Server under the Server Settings section. To know more about this section, please refer to Section “Server settings” of the General Administration Manual.

The categories for functions depends on an admin user. Taking :numref:`functioncatalinterf` as an example, we have:

1. **Text Analysis**: make sense of unstructured text,

2. **Machine Learning**: teach your app to teach himself,

3. **Computer Vision**: identify objects in images,

4. **Utilities**: ready to use microservices,

5. **All**: visualizes all your functions; this is the only category that cannot be changed or removed.

To facilitate the comprehension we created some functions to be examined. We recall here that one can look for a function in different ways: using the categories or the tags or using the Functions Catalog “Search” box available at the top of the functions list as highlighted below.

.. figure:: media/image398.png

    Search box to look for a function.

We suppose here to select one category, which means to click on the category box, in order to be able to analize the functions belonging to it.

Note that the underlined part in figure below contains a list of tags. These help to focus on the subjects and therefore fuctions associated to that category. Viceversa when all functions are shown, all tags are shown as well and they can be used to pick up functions related to that subject.

.. figure:: media/image399.png

    Using tags and categories to look for functions.

A function can be executed using the icon .. figure:: media/image401.png which launches a demo (i.e. the function with default values) or using the icon which lauches the computation after the insertion of new values for data. Use the icon for deleting the function. Only the an admin user can use the three options, while the final user can use only the “execution” button.

To create a new function an admin user must click on the “Plus” icon available at the right top corner of the page. The action opens the interface shown below. Here you have four tabs that we describe shortly in the following subsections.

.. _creatingnewfunct:
.. figure:: media/image404.png

    Creating a new function.

The General tab\*
~~~~~~~~~~~~~~~~~

In this tab the user gives the general information about the function as :numref:`creatingnewfunct` shows. The admin user must type: the *name* of the function, the *label* with which it is identified uniquely (remember to use only numbers or letters and do not leave spaces between them). The *keywords* are were tags are defined. Finally the *Description* is where the user can insert a text or images to be shown when the function outputs are visualized.

The Input tab\*
~~~~~~~~~~~~~~~

As shown in the following figure, the function admits three kind of input: the *dataset*, the *variables* and the *files* one.

.. figure:: media/image405.png

    Input tab.

In the “Dataset” instance the function takes values from a Knowage dataset. It can be chosen from the combobox available in the dedicated area. Note that the combobox shows the labels of the datasets. It is also possible to ask for the preview so the user can check if the values suit the wished requests.

.. figure:: media/image406.png

    The dataset input of the function settings.

In the “Variable” case, the user must insert one or more variables and match them with values using the dedicated area.

.. figure:: media/image407.png

    The variable input of the function settings.

In the “File” case, the user is asked to browse folders and upload the wished document remembering to give an alias to it. Files as videos, images, etc are all supported by the functionalities.

.. figure:: media/image408.png

    The file input of the function settings.

The Script tab\*
~~~~~~~~~~~~~~~~

The script tab is where an expert user defines the function through the usage of datamining languages R or Python, as shown in Figure below, or calling for an external link. In particular, it is possible to choose between the two options **Local** and **Remote**.

.. figure:: media/image409.png

    The script tab.

We suppose we have chosen the “Local” modality and that we selected a dataset in the previous input tab. In this case the dataset is transformed into an R dataframe that can be recalled while editing the script using the same name of the dataset label. The following figure   shows an example.

.. figure:: media/image410.png

    Using the dataset dataframe generated by the software to edit the R script.

Note that if the function takes variables or files as input you can recall them through their name (as specified in the input tab). In particular, refer to Code syntax to recall the variable input in the variable instance, while for the file case remember that the alias will contain the file path.

.. code-block:: bash
         :caption: Code syntax to recall the variable input
         :linenos:
 
           $P{variable_name}
 
We suppose now to have chosen a dataset and the local modality but to want to use the Python language (:numref:`usedatafrmpandas`). In this case the  dataset is saved and read by the script as a dataframe of the pandas libraries: `http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`__

.. _usedatafrmpandas:
.. figure:: media/image412.png

    Using the dataset dataframe of the pandas libraries generated by the software to edit the Python script. 
 
The “Remote” instance is used for external services and when the user wants to use a language which is not supported by Knowage server. When selecting this modality the user is asked to insert an URL calling for an external web site that supports and runs the requested language.

Technically, remote functions are recorded in the catalog list. The input data of those functions are specified by the local Knowage request and the code is not stored inside Knowage. On the contrary it is located at the address specified by the URL.

.. figure:: media/image413.png

    Input definition for remote function.

To define a remote function you have to perform the steps seen above, therefore to specify label, name, inputs and outputs. Figure below shows an example.

.. figure:: media/image413.png

    Remote function definition.

When opening the Script tab, select the Remote Radio button. The action will create a remote address and the editor where to insert the code will not be available and the user will have only the chance to specify the URL where the code is placed.

The function that you are defining must be a REST service, in particular of POST type, and it will receive the input data in the JSON format with the syntax showed in JSON format for remote function.

.. code-block:: json
         :caption: JSON format for remote function
         :linenos:

          [  "type":"variablesIn", "items":                                                
             {   {                                                                            
                  "demoVarName1":"3",                   
                  "demoVarName2":"3"                                                  
                 }                                 
             },  "type":"datasetsIn", "items":                                                
              {      {                               
                  "demoDsName1":"df1",                                              
                  "demoDsName2":"df2"                                             
                      }                               
              },  "type":"filesIn", "items":                                                   
              {   { "demoFileAlias1":                                                       
                      {                                                                   
                     "filename:filename1, base64 :..                                    
                       },   "demoFileAlias2": 
                     {
                      "filename:filename2, base64 :.. 
                     }
                   }
              }       
          ]
          

 When the call runs successfully, the remote function must answer answer with a JSON element like the one exhibited in Code below.
 
.. code-block:: json
         :caption: JSON answer of a remote function
         :linenos:

            {                                                                           
            "resultType":"Image",                  
            "result":".image content in base64.",  
            "resultName":"res"                     
            },                                                                               
            {                                         
            "resultType":"Dataset",                
            "result":"outDatasetLabel",            
            "resultName":"datasetName"             
            },                                     
            { "resultType":"File", "result":       
            {                                      
            "filesize":"54836", --optional            
            "filetype":"image/jpeg", --optional      
            "filename":"chart.jpg", --optional        
            "base64":".file content in base64." }, 
            "resultName":"fileToBeSave"            
            }                                         

If an error occur the function must returns the lines as shown in JSON format for remote function.

.. code-block:: json
         :caption: JSON answer of a remote function
         :linenos:

          { 
            "service":"",                                                                          
            errors":[                            
              {                                     
               "message":"Here the error message."  
               ]                                     
          }


The Output tab\*
~~~~~~~~~~~~~~~~

Finally it is important to specify what kind of outputs the function will produce. Using the “Output“ tab shown below, you can choose between:

.. figure:: media/image414.png

    Choosing the output type in the function definition.

-  **Dataset**: the function will return a set of records as a the Knowage dataset way;
-  **Image**: the function will return one or more graphics showing the results through bar or pie charts or other kind of visual tools;
-  **Text**: the function will return a window containing some text;
-  **File**: the function will return a file.

It is possible to define more than one output for the same function. As an example, in :numref:`execofdemoforfunct` you can see the execution of the demo for a function called “Heart diseases”. The latter was set to have two outputs, one is of type “Dataset” and the other of type “Image”. The execution opens then a window with two tabs. The first tab contains the Dataset type output, which is translated visually with a table. While the second tab contains the Image output namely a set of graphics as configured to.

.. _execofdemoforfunct:
.. figure:: media/image415.png

    Execution of demo for a function.

Clicking on the second execution icon you be asked to insert the new value and run the function after filling all boxes in. Figure below  shows the window opening when one asks for inserting new data values.

.. figure:: media/image417.png

    Inserting new data values for function.

Finally clicking on the function name as shown below you can enter function configuration details and modify them.

.. figure:: media/image418.png

    Clicking on function name to modify it.

As well as for the input case, the script can recall the output elements. We need to distinguish between the R and the Python language. Note that, in the dataset case, the user needs to name the output as reported in the script body. :numref:`usedatafrmpandas` and :numref:`defoutpexample` show an example.

.. _defoutpexample:
.. figure:: media/image419.png

    Defining the output example.

When using Python the datasetOut variable is a “pandas” dataframe while, when using R it is a dataframe. Then it is important in fact  to consider the objects’ stucture (input and output type must match).

When the script runs using a certain output dataset Knowage server produces a dataset whose name and label is label <User_Name> functionsCatalog <label specified in the Output tab>.

As an example the function of :numref:`usedatafrmpandas` produces a dataFrame whose label and name are biadmin_functionsCatalog_datasetOut.

.. include:: dataminingThumbinals.rst
