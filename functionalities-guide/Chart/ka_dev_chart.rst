Charts
======

Stand alone charts\*
------------------------

The previous chapters were dedicated to the end user approaching the Knowage Chart engine. We stressed how the final user must pass through the Cockpit interface to develop graphs. We want now spend some words about the developer experience. Indeed, if you are a technical user you can also create a chart as a stand alone document.

Once you enter the Knowage environment with developer credentials, open the technical menu directly into the **Documents Development** area, as shown in Figure 6.31.

   |image124|

   Figure 6.31: Documents Development.


Then click on the “Plus” icon of the **Create Document** feature and select **Generic Document**.

   |image125|

   Figure 6.32: Create a new document.

You will be asked to fill in the form. We give an example in Figure 6.33.The fields marked with an asterisk are mandatory. Select the Chart type and engine. Choose the dataset with which you want to manage your analysis. Use the magnifier to choose among the available datasets. Remember to pick out in which folder you want your chart to be stored (see Figure 6.34) and finally save.


   |image126|

   Figure 6.33: Document Details.

   |image127|

   Figure 6.34: Select the folder in which you want your chart to be saved.


A new template can be generated through the editor clicking on **Template build** as showed in Figure 6.35 or a template previously created can be uploaded.

   |image128|

   Figure 6.35: Template build.

If you choose to implement the new Chart through the Template Build feature, the steps to follow are exactly the same of those seen for the final user. In fact, once you click on the Template Build icon, you are redirected to the Chart designer. In this case, by the way, another functionality is enabled, the Cross Navigation.


Cross Navigation\*
----------------------

When you develop a standalone chart it is possible to add a cross navigation path to it. This means that, once the chart is launched, its elements becomes clickable and it redirects the user to a second document.

For charts documents outputs parameters are automatically generated during the creation of the document. Therefore you can define cross
navigation in the default way, as explained in Cross Navigation.

.. include:: chartThumbinals.rst
