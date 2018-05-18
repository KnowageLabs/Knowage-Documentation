


STARTING YOUR PROJECT
=====================

This chapter describes advanced features, i.e. available only in
KnowageBD and KnowageSI products, to access data as end user.

A dataset is a way to read data from different sources and represents
the portion of data used by various documents. Suppose you want to
create a bar chart showing the sales trend for the current year; in this
case you need to pass to the document the total sales amount for each
month of the current year. You can create your own dataset uploading an
XLS or a CSV file or use a dataset already defined. Knowage offers you
also the chance to download open data from WEB thanks to CKAN
integration. Moreover you can create your own and more complete dataset
from different sources through the dataset federation. In the following
we will describe all these functionalities.

Let us suppose to enter, with end user credentials, the data management
area clicking on the **Workspace** icon from BI functionalities menu as
shown in Figure 2.1 and the **Data** section of the window.

   |image1|

   Figure 2.1: Access to **My Data** area

Afterward you have the subsections: **Dataset** and **Models**. Select
**Models** to explore the models and the **Dataset Federation** area.
Please note that the **Dataset Federation** functionality is available
only in KnowageBD and KnowageSI.


 Dataset
-----------

Into the “Dataset” area we find all the datasets classified according to
their types. The datasets are categorised as follows:

   **My dataset**: datasets created by yourself uploading a CSV or XLS
   file or creating a query on a business model using the Qbe interface;

   **Enterprise dataset**: certified datasets,namely datasets created by
   the technical/experts users and shared with the end user.

   **Shared dataset**: datasets created and shared by other end users;

   **CKAN dataset**: in this area you can download public datasets and
   visualize your CKAN datasets;

   **All dataset**: in this folder are stored all the available
   datasets, namely all datasets contained in the classes just
   described.

My dataset
~~~~~~~~~~

In this area you can create datasets uploading your own files.

   |image2|

   Figure 2.2: Dataset creation.

Click **Create Dataset** to open the dataset wizard which guides you
through the dataset creation. You can choose between XLS or CSV file as
in Figure 2.2. In the example shown in Figure 2.3, we upload an XLS
file.

The wizard, shown in Figure 2.4, leads the user to insert some
information to configure the dataset. For instance to specify the number
of rows to skip or to limit and which sheet (of the XLS file) to pick up
values from.

My dataset

   |image3|

   Figure 2.3: Uploading XLS for dataset.

|image4|

   Figure 2.4: Configuration features.

My dataset

Once you have uploaded the file, you can check and define the metadata
(measure or attribute) of each column. To switch a measure to an
**attribute** (or viceversa), click on **Value** column of the
interested row field as shown in Figure 2.5.

   |image5|

   Figure 2.5: Change metadata.

Just few steps before saving the dataset:

-  Check the data preview in order to verify the accuracy of your data;

-  enable or disable the persistance of dataset. Thanks to this
      functionality the server creates a snapshot of the extracted data
      in order to avoid to reload the dataset each time that the user
      revokes it;

-  finally, name and save the dataset as shown in Figure 2.6.


   |image6|

   Figure 2.6: Saving dataset.

As we discussed previously, you find all created datasets under **My
dataset** area. You can share/unshare them by clicking on the **share**
icon (have a look at Figure 2.7). The colour of the icon changes from
white to red when sharing is turned to active. A shared dataset is
visible to all other users having your same role.

Note that dedicated area “\ **Shared Dataset**\ ” contains all acquired
datasets thanks to the sharCKAN integration

ing of other users.

   |image7|

   Figure 2.7: Share a dataset.

CKAN integration
~~~~~~~~~~~~~~~~

Thanks to CKAN integration you can easily access to datasets published
in the World Wide Web (e.g. datahub.io, data.gov, data.lab.fiware.org,
dati.gov.it, and more). Indeed, CKAN is the world’s leading open-source
data portal platform. It is a powerful data management system that makes
data accessible by providing tools to streamline publishing, sharing,
finding and using data. CKAN is addressed to data publishers (national
and regional governments, companies and organizations) who want to make
their data open and available. So you can search and handle open data in
a self-service manner.

   CKAN Datasets

   |image8|\ CKAN datasets can be divided in four main categories:
   “Public”, “Organization private”, “Acquired”, “User private”. You can
   download and use only the datasets having a **Public** category.

CKAN datasets access method
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To start using CKAN datasets inside Knowage suite, go to the **CKAN
Dataset** tab in the “Dataset” subsection of “Data” section under “My
Workspace”. As shown in Figure 2.8, choose from the combobox the
repository that you are interested in and then click on the repository
name to access it.

A preview of datasets stored in the chosen repository will be shown.

These are not usable yet, but you can start to handle them as we will
show in the following sections. The datasets are shown with their name
and description. By moving the cursor over a Export dataset

   |image9|

   Figure 2.8: CKAN Repositories.

dataset, a list of available actions will appear. Clicking on the
**Info** button, a set of information from the original CKAN resource
and about the dataset status (e.g. visibility, last modification date)
will be displayed by Knowage, as in Figure 2.9. To use one of them you
have to import metadata information and then analyse the dataset on
demand.

   |image10|

   Figure 2.9: CKAN dataset details.

Export dataset
^^^^^^^^^^^^^^

Note that once the dataset has been created, the user may find useful to
get an excel from it. Knowage has designed a specific button to fulfil
this need that the user can find exploring the detail panel of the
dataset, as reported in Figure 2.10.

Save and handle dataset

   |image11|

   Figure 2.10: Export dataset.

Save and handle dataset
^^^^^^^^^^^^^^^^^^^^^^^

If you want to use a dataset not used yet, any action on it will start
the metadata import wizard. You access it by clicking the magnifier
icon. As a first step, you have to insert some mandatory parameters to
set the parser configuration.

As a second step the user have to specify how the dataset will appear
and to check metadata. Be careful to choose the proper data type
(String, Integer, Double) and field type (Measure, Attribute). After
that, click on **Next** to see the validation results, confirm and
finalize dataset import. Once completed the dataset importation, the
selected dataset will appear in the **DataSet** tab too. These actions
just listed on the dataset change for downloded datasets. In particular
you have the eye-shaped icon to refresh the dataset or change metadata
by repeating the download process and the magnifier icon to inquire it
throught the QbE interface.

2.2 Models
----------

Here you find the models that the a technical user has built for you.
You can query it using the QbE interface and create your own dataset
from them.

2.3 Dataset federation
----------------------

Dataset federation is a functionality available only in KnowageBD and
KnowageSI. Thanks to the Data federation functionality, you can create a
new dataset combining two or more datasets according to your role
permissions Let us give you an example. Suppose you have stored in a
database your products information, i.e. sales, costs, promotions ecc.)
and you find as open data the customers feedbacks on these products. If
you create datasets on these Dataset federation

resources sharing at least one column, then you can join them on the
common column and improve your analysis.

Click on **Create Federation** to see all available datasets and choose
the ones you want to federate. Click **Next** and choose which columns
the join have to be made on and click the plus icon to add it to the
**Association list**. In our example in Figure 2.11 we choose Product.

   |image12|

   Figure 2.11: Federated dataset details.

Once saved, The new federation has been created in **Federation
definition**\ and you can find it in Federation definition. Open it by
clicking the magnifier icon on the federation. In this way you open it
with QbE tool. All details on how to use the QbE interface to perform
free inquiries can be found in the dedicated chapter. You can create new
datasets, save them and retrieve them from the **Dataset** section.



.. include:: myDataAndDataSetThumbinals.rst