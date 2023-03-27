Resource manager
#######


.. important::
         **Enterprise Edition only**

         With the Knowage Community Edition the Resource Manager  will be able to manage just the **models** folder in order to define metadata for data mining analysis. With the Knowage Enterprise Edition,  will be able to manage all Knowage's installation resources.

The **Resource Manager** functionality available under the **TOOLS** section of Knowage main menu, as shown in Figure below, allows you to manage all files within the Resources folder of the Knowage's installation. In next sections we will see in details how to use the Resource Manager feature.

.. figure:: media/resource_mng_1_8.1.png

    Resource Manager from menu.
   
As default, the system shows files starting by the root directory:

.. figure:: media/resource_mng_2.png

    Resource Manager starting view.

Resource Manager functionalities
--------------------------------

The Resource Manager window diplays two sections: on the left the tree representing the existing system resources; on the right the details of the selected left-folder. On the right-top is available the current path:

.. figure:: media/resource_mng_2_bis.png

    Resource Manager detail view.

**Tree functionalities**

The tree shows exactly the phisical structure of the file system from the **resources** folder. On the top bar are present two funcionalities: **Refresh tree** and **Create new folder**:

.. figure:: media/resource_mng_0.png

    Tree view.

.. figure:: media/resource_mng_0_bis.png

    Creation detail.


.. figure:: media/resource_mng_0_ter.png

    Creation result.

The new folder will be created under the selected folder of the tree ( in this case, 'KNOWAGE-5058').

By clicking on the *Download* icon of a specific folder, you can download all files contained:

.. figure:: media/resource_mng_tree_1.png

    Download functionality icon.
   
Select a folder for the download and give a name to the zip file to be available in your local system.

.. figure:: media/resource_mng_3.png

    Download functionality.

By clicking on the *Delete* icon of a specific folder, the folder can be fisically removed from the Knowage server after confirming the operation.
Please remember that the deletion of a folder is an irrecoverable operation.

.. figure:: media/resource_mng_tree_2.png

    Delete functionality icon.


.. figure:: media/resource_mng_tree_3.png

    Delete functionality confirmation.

**Detail panel**

When a folder is selected, the right panel shows the properties *Name*, *Size* and *Last Modified Date* of all contained files.

.. figure:: media/resource_mng_6.png

    Detail view.

All items are selectable for downloading or removal trough specific icons of the toolbar.

.. figure:: media/resource_mng_7.png

   Functionalities available for selected files

An **Upload** functionality is also available through a dedicated icon. See image below.

.. figure:: media/resource_mng_5.png

   Upload files

.. figure:: media/resource_mng_5_bis.png

   Selection file popup

In case of a zipped file want to be uploaded, it is possible to keep the file zipped.

.. figure:: media/resource_mng_5_ter.png

   Uploaded zipped file

It is also possible to unzip the file to upload selecting the *Extract Files*. See figure below.

.. figure:: media/resource_mng_5_quat.png

   Upload unzipped file

.. figure:: media/resource_mng_3_bis.png

   Uploaded unzipped files result

**Model Metadata Definition**

As already told at the beginning, **models** is the unique folder managed both by the Community and the Enterprise Edition. It contains all the data-mining models usable by the Knowage Function Catalog.

For each model it is possible to define its metadata, download and/or delete the model using directly the tree options:

.. figure:: media/resource_mng_8.png

   Models folder options

*Metadata management*

The **Metadata** option opens a gui in which the user can defines metadata information about the model in use.
   
So, it's possible insert:
   - a more specific Name for the model
   - the Version number of the model
   - the Type of analytics: a value selectable between 'Descriptive', 'Predictive' and 'Prescriptive'
   - an image to represent the logic of the model uploadable througth the specific icon
   - a detailed description
   - information about the Accuracy and then Performance for the model
   - information about the way of usage of the model
   - information about formats for input and output data

.. figure:: media/resource_meta_4.png

   Metadata example