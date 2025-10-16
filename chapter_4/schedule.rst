Scheduler
========================================================================================================================

Knowage scheduler allows to schedule the execution of one or more analytical documents published on the Server. Documents executed by the scheduler can then be distributed along different dispatching channels. In the following we describe how to create an activity, schedule it and dispatch the results.

.. figure:: media/scheduler.png

   Scheduler from menu

Create an Activity
------------------------------------------------------------------------------------------------------------------------

In order to define a new scheduled activity the administrator must specify which documents compose the activity and how to execute them. The list of all scheduled activities can be seen selecting **Tools** > **Scheduler**. To create a new activity click the “Plus” icon at the top of the page in the left area. The below image shows the main scheduler page and the new activity GUI.

.. figure:: media/image4041_new.png

   Left: scheduler main page. Right: New activity GUI

After ginving a name and a description to the new activity select the documents that compose it by clicking *Add*. A pop-up will open to select all your documents, see Figure below.

.. figure:: media/image42_new.png

   Adding a document to an activity.

The new activity can contain documents with or without parameters. The below image shows an activity with documents with and without parameters.
In case of parameters an icon will signal the need to specify them by using the pencil icon.

.. figure:: media/image42_b.png

   Adding a documents with and without parameters.

In case of parameters you need to specify how the scheduler will handle the analytical drivers of each selected document having parameters.

.. _manageparameters:
.. figure:: media/image43_new.png

   Manage parameters.

There are two possibilities:

- selecting a value from those available for the specific analytical driver at definition time; 
- executing the report one time for each possible values of the analytical driver.

A scheduled activity can be composed by more than one report. Once all desired documents have been added and the management configuration of their parameters has been set up, save the activity by clicking on the save (disk) icon. The new activity is shown in the list and can be modified or deleted using intended specifically icons.

.. |image50| image:: media/image44.png
   :width: 30

You can manage your activity at any time just clicking on the name of the scheduling item (left side of the window) and all its features will be displayed aside (right half part of the window).

To see and modify the list of the schedules associated to an activity, click the *ADD* option of the "Timing & Output" panel. Similarly, click on the same option to associate schedules
to the newly created activities. The below image shows the *Timing & Output* panel.

.. figure:: media/image45_new.png

    Timing & Output panel.

It is composed by two areas: **Timing** and **Output**.
The Timing tab let you set all properties of you schedulation. Indeed here you decide its description and timing.
A schedulation can be made in a chosen date and time if you choose **Single Execution** as type.
Otherwise it can be realized for fixed periods or start on a fixed event.

You can decide it, by choosing the schedulation type.

Available schedulation type are:

-  Single Execution;
-  Periodic Execution;
-  Event Execution.

A **Single Execution** is a fixed execution for a date and a time which happens only once. A **Periodic Execution** repeats your schedulation periodically according to your settings. The **Event Execution** starts the scheduling when an event happens.

You can choose among these event types:

-  REST WS service,
-  Context Broker message,
-  Dataset.

If you choose **Dataset**, you have to select a right structured dataset. It has to give as results only true or false. Then set the frequency in seconds. This is the frequency the dataset will be verified. For example if you set it on 10 seconds it means that each 10 seconds the dataset is executed. If the result of its execution is true, the schedulation is trigged otherwise it isn’t.

Once you are done, switch to the **Output** tab.

.. figure:: media/image46_new.png

    Output panel.

Here you can find the dispatch configurations, that can be different for all the documents that compose the scheduled activity. All documents that compose the activity have their own dispatch configuration and the same document can be distributed along multiple dispatch channels. You can switch among the documents included in your activity by clicking on their name in the upper toolbar. There are many different possible dispatch channels that can be used to distribute the results of the execution of a scheduled activity:

- Save as snapshot,
- Save as file,
- Save as document,
- Send mail

In the following sections we explain them in detail.

As shown in the image of the Output panel, there is a new option for the *Output type* that allows to choose the type of the document to be produced as a result of the process: HTML, PDF, XLS.

Save as snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The executed document can be saved as snapshots in cyclic buffers of configurable size. For example, it is possible to store in the buffer the last 12 snapshots (the **History Length** field) of one report, scheduled to be executed one per month, in order to have a one-year long history.

The list of all snapshots contained in the buffer can be accessed from the **Show scheduled executions** contained in the **Shortcuts** menu. You can find it in the document toolbar at the top right corner. Each snapshot can be opened or deleted from this panel. These steps are shown in the following figure. A snapshot contains data queried from the database at the moment of its execution performed by the scheduler.

.. figure:: media/image47_b.png

    Steps to open saved snapshots

Save as file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The executed document can be saved as file on the filesystem in the path /knowage-<version> /resources (if no destination folder is specified). Otherwise, you can create the relative path of this subfolder by writing your subfolder name. For instance, if you write “MyFirstScheduler” as file name and “Schedulation” as destination folder, after the schedulation execution a subfolder Schedulation containing the file “MyFirstScheduler” is created in /knowage-<version> /resources. If the subfolder Schedulation already exist your file is added to this subfolder. You can have a look at the form in Figure below.

.. figure:: media/image51_new.png

   Save as File Option.
   
If you prefer to generate a .zip file containing the scheduled documents, you can check the dedicated option.

Save as document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The executed document can be saved as an **Ad hoc reporting** document in the Knowage functionality tree. The document execution will be saved in the specified folder and will be visible to all yous that can access that particular folder. 

For those documents whose execution is iterated over a parameter value, it is also possible to use the value of the parameter to decide to which folder the document shall be dispatched. To do so, define a mapping dataset composed of two columns:

-  the first containing a specific parameter value;
-  the second containing the label of the folder where the document shall be dispatched when the document is executed with the corresponding parameter value.

Once you have defined the mapping dataset, you can use it in the configuration settings of the document dispatcher. Like in the previous case, the scheduler will execute the report one time for each possible value of the parameter. This time, however, execution results will be dispatched in different folders, according to the mapping defined in the dataset.

Send mail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
         **Enterprise Edition only**

         This feature is available only with KnowageER and KnowageSI, submodules of Knowage Enterprise Edition

The executed document can be sent to one or more mail recipients. The list of mail addresses to be used to forward the executed document can be defined in three different ways:

-  statically;
-  dynamically, using a mapping dataset;
-  dynamically, using a script.

In Figure below you can have a look at the mail form. In the following we will focus on each typology, clicking on the info icon you get detailed information.

.. figure:: media/image52_new.png

    Sending mail form.

Static list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to choose a static list, check the option **Fixed list of recipients** and fill the configuration property **Mail to** with the list of desired mail addresses separated by a comma. An mail for each executed document will be sent to all the mail addresses contained in the list.

Dynamic list with mapping dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, you have to define a two-column dataset:

-  the first containing a specific parameter value;
-  the second containing each mail address the executed document should be dispatched to.

   You can see an example of dataset in the following Figure.
   
.. figure:: media/image54.png

Example of mapping dataset for dynamic distribution list

Basically, when the parameter has a given value, the document will be sent to the corresponding email address. Once you have defined the mapping dataset, you can use it in the configuration settings of the document dispatcher. With this configuration, the scheduler will execute the report one time for each possible value of the parameter **Position**, then dispatching the results to different recipients. Specifically, all execution results passing a value of the **Position** parameter to the report starting with VP will be sent to ``name1surname1@gmail.com``, the ones starting with HQ will sent to ``name2surname2@gmail.com`` and the ones starting with President will be sent to ``namesurname@gmail.com``.

Dynamic List with script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check the option **Use an expression** and assign a value to the configuration property **Expression** with a parameter-dependent expression like the following:

.. code-block:: bash
         :linenos:

         $P{dealer}@eng.it

Here dealer is a document parameter label (``$P{dealer}`` will be replaced by the parameter value of the scheduled execution).

Schedulation panel
------------------------------------------------------------------------------------------------------------------------

To conclude our overview on the scheduler features, save your settings and go back to the main scheduler page.

Here you can select one of the available scheduled activities to explore details. 

.. figure:: media/image55a_new.png

    Details of a scheduled activity in Timing & Output panel.

Here you find the following information:

- **Schedulation informations**, gives some extra information about your schedulation concerning sending emails
   
- **Schedulation detail**, opens the scheduling configuration and let you change them.
- **Execute now**, by clicking it you immediately start the execution of your schedulation.
- **Pause schedulation**, it lets you pause your schedulation.
- **Resume schedulation**, it appears after having paused a schedulation, it enables you to resume it.

In case, use the recycle bin icon to delete the scheduling.


Scheduler Monitor
------------------------------------------------------------------------------------------------------------------------

You can monitor the whole scheduling agenda by entering the **Scheduler Monitor** item from the Knowage Menu. 

.. figure:: media/scheduler_m.png

    Details of a scheduled activity in Timing & Output panel.

This feature allows you to check which schedulations are active in a certain future time interval and, eventually, to be redirected to the schedulation area in order to modify the selected schedulation.
  
.. figure:: media/image59_new.png

    Schedulation Agenda
