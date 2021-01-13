Dossier
========

A dossier document allows you to obtain a file processed starting from an input template. A typical example of using this feature is the creation of a file with variable content updated at each run. To do this, you need to create a dossier document with a well-configured XML template.

.. important::
       **Enterprise Edition**

       If you purchased Knowage EE, the following features are available only in KnowageER license.


XML Template
------------

Tags and properties
~~~~~~~~~~~~~~~~~~~~

XML template is an XML file used to configure parameters needed to the elaboration. This file is uploaded during document creation and can be updated using the HISTORY tab visible in document edit mode.

In particular, tag allowed are:

-  **DOSSIER**: main tag used to define the dossier template;
-  **PPT_TEMPLATE**: contains properties related to the PPT template  (incompatible with DOC_TEMPLATE). You can specify:

  - *name*: the name of the template file name (Supported file types are PPT, PPTX);

-  **DOC_TEMPLATE**: contains properties related to the DOC template (incompatible with PPT_TEMPLATE). You can specify:

  - *name*: the name of the template file name (Supported file types are PPT, DOCX);
  - *downloadable*: true/false. Enable/disable the download of the template (optional);
  - *uploadable*: true/false. Enable/disable the upload of the template (optional);

-  **REPORT**: contains document's properties. You can specify:

  - *label*: the label of the document to be executed;
  - *imageName*: the name of the image to be replaced;
  - *sheetWidth*: the width of the document sheet (optional);
  - *sheetHeight*: the height of the document sheet (optional);
  - *deviceScaleFactor*: the scale factor to apply to the image during taking the screenshots (optional);

-  **REPORTS**: encloses all REPORT tags;
-  **PARAMETER**: sets parameter for the document's execution. You can specify:

  -  *type*: static/dynamic. Defines the type of the analytical driver. It must be the same as the one of the document to be executed;
  -  *url_name*: the url name of the analytical driver to be used. It must be the same as the one of the document to be executed;
  -  *url_name_description*: the description displayed in the driver value input panel for the analytical driver;
  -  *dossier_url_name*: the url name of the analytical driver set into detail mode;
  -  *value*: the value to be set into the driver (mandatory if type="static");

-  **PARAMETERS**: encloses all PARAMETER tags;
-  **PLACEHOLDER**: sets the placeholder. You can specify:

  -  *value*: the text to be replaced;

-  **PLACEHOLDERS**: encloses all PLACEHOLDER tags.


Image adding (PPT_TEMPLATE)
------------------------------

Suppose you have to create a ppt/pptx file where to place the images relating to one or more reports. You have only to configure XML template defining some placeholders to be use for replacing and execute it. Below is shown an example of an XML template used for this purpose.

.. code-block:: xml
    :linenos:
    :caption: Example (a) of template for Dossier for Image replacement on docx file.

    <?xml version='1.0' encoding='utf-8'?>
    <DOSSIER>
    	<PPT_TEMPLATE name="PPT_TEMPLATE.pptx"/>
    	<REPORTS>
    		<REPORT label="Report-multivalue-parameter">
    			<PLACEHOLDERS>
    				<PLACEHOLDER value = "ph1"/>
    			<PLACEHOLDERS>
    			<PARAMETERS>
    				<PARAMETER type="static" dossier_url_name="state" url_name="state" value="Canada"/>
    			</PARAMETERS>
    		</REPORT>
    	</REPORTS>
    </DOSSIER>

The example above is using one placeholder and one static analytical driver.

.. warning::

    Please note that the file to be used as a template must be placed in ``TOMCAT_HOME/resources/<TENANT_NAME>/dossier`` path.


Image replacing (DOC_TEMPLATE)
--------------------------------

Suppose that you have to draw up a document where text is static but images related to need to be updated.

By this functionality you will be able to use a docx file as a template and replace images inside it. More precisely, you can configure your XML and docx templates to allow Knowage to replace specific images with new ones obtained by the execution of specified documents.

Below is shown an example of an XML template used for this purpose.

.. code-block:: xml
    :linenos:
    :caption: Example (a) of template for Dossier for Image replacement on docx file.

    <?xml version='1.0' encoding='utf-8'?>
    <DOSSIER>
    	<DOC_TEMPLATE name="DOC_TEMPLATE.docx" downloadable="true" uploadable="true" />
    	<REPORTS>
    		<REPORT label="DOC_01" imageName="img_DOC_01" sheetWidth="1366" sheetHeight="650" deviceScaleFactor="1.5">
                <PARAMETERS>
    				<PARAMETER type="dynamic" dossier_url_name="family_dossier" url_name="family_document"/>
    				<PARAMETER type="dynamic" dossier_url_name="category_dossier" url_name="category_document"/>
                </PARAMETERS>
    		</REPORT>
    		<REPORT label="DOC_02" imageName="img_DOC_02" sheetWidth="1366" sheetHeight="650" deviceScaleFactor="1.5">
                <PARAMETERS>
    				<PARAMETER type="dynamic" dossier_url_name="family_dossier" url_name="family_document"/>
    				<PARAMETER type="dynamic" dossier_url_name="category_dossier" url_name="category_document"/>
                </PARAMETERS>
    		</REPORT>
    		<REPORT label="DOC_03" imageName="img_DOC_03" sheetWidth="1366" sheetHeight="650" deviceScaleFactor="1.5">
                <PARAMETERS>
    				<PARAMETER type="dynamic" dossier_url_name="family_dossier" url_name="family_document"/>
    				<PARAMETER type="dynamic" dossier_url_name="category_dossier" url_name="category_document"/>
                </PARAMETERS>
    		</REPORT>
    	</REPORTS>
    </DOSSIER>

My first dossier
----------------

You can create a dossier document by using the plus button and choosing "Generic Document". Proceed by filling in the necessary fields, choosing the XML template and selecting "Collaboration" as the type and "Dossier engine" as the engine. If the documents to be executed have one or more analytical drivers, these drivers must be added to the dossier document from the DRIVER tab.

.. figure:: media/image000.png

    Dossier document creation interface.

After saving the document, you can access the dossier activity page by clicking the play button.

.. figure:: media/image001.png

    Dossier activity interface.

If one or more dynamic analytic drivers are set, the required inputs must be provided in the sliding menu that appears from the right. You will then go to the dossier activity page.

.. figure:: media/image002.png

    Dossier activity interface.

If upload/download are enabled, file template can be uploaded/downloaded using the three dot menu on the top right of the "Details" tab.

.. warning::

       This feature is available only for image replacing procedure.


If you want to execute your document, you must enter a name for the activity and click on "LAUNCH ACTIVITY". A new task will be started in the STARTED state and a new row will be visible in the table below. At the end of the execution of the task, the processed file can be downloaded with the appropriate download icon.

.. figure:: media/image003.png

    Dossier activity execution finished.

Each line allows you to see useful information on the activity (such as the values of the drivers used for execution) by clicking on the info icon, download the processed file by clicking on the download icon and remove itself by clicking on the trash icon.
