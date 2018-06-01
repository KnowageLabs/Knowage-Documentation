
Scorecard\*
===========

The **Scorecard** feature, available in Knowage suite as highlighted in Figure 8.1, allows to supervise different KPIs at the same time. This option gives an exclusive complete overview of the KPIs situation when the user is not interested in a single threshold check. This tool is in fact useful when concern is addressed to monitoring the overcoming of two or more critical KPI values.

   |image162|

   Figure 8.1: Scorecard from the contextual menu.

Scorecard development
-------------------------

A scorecard is structured in hierarchical levels. Shortly, there is a first level called **Perspective** composed of KPIs grouped on targets. Otherwise, **Targets** are assigned a threshold depending on the KPIs they are composed of. In the following we will describe in detail a scorecard configuration. When clicking on the Scorecard menu item the window of Figure 8.2 opens. Here the implemented scorecards are listed and can be explored once selected and edited.

   |image163|

   Figure 8.2: Scorecard window.

The “Plus” icon available at the right top corner of the page opens a new window where to set a new scorecard, as shown in Figure 8.3. Assign a name and click on **Add perspective** (Figure 8.4).

   |image164|

   Figure 8.3: Defining a new scorecard.

A perspective allows you to organise the monitoring over targets. An example is given in Figure 8.5.

In fact, each perspective manages one or more targets accordingly to the user’s requirements. A target consists of one or more KPIs, as in Figure 8.7, and it is assigned a threshold color according to the chosen **Evaluation criterion**. In fact, if one selects:

-  **Policy “Majority”** the target gets the threshold of the KPI threshold that numerically exceeds the others,

-  **Policy “Majority with Priority”** the target gets the threshold of a specific KPI,

-  **Policy “Priority”** the target gets the majority threshold of the KPIs in case the primary stated KPI returns the lower threshold,       namely the “green” one, while it gets the threshold of a primary stated KPI in case the latter returns the other thresholds, namely the “yellow” or the “red” one.


   |image165|

   Figure 8.4: Add perspective to the scorecard.

   |image166|

   Figure 8.5: Perspective list example.

    .. warning::
       **Thresholds of selected KPIs must have the right colors**
       
       Note that the scorecard shows the right colors accordingly with the selected policy only if the KPIs which compose the targets          have **no filters** and **standard colors** (see Section 7.1, Step 2 for definitions) to highlight the threshold.

    .. warning:: 
       **“Standard” colors for thresholds**
       
       When the targets contain parametric KPIs the target/perspective evaluation cannot be completed for value absence. Therefore the          warning lights turn grey. The right visualization of the scorecard must be implemented through a scorecard document. Check              Section 8.2 to have more details on how to develop a scorecard document.

An example is showed in Figure 8.6.

   |image168|

   Figure 8.6: Select the KPI with priority.

The same choice is available at the perspective level (refer to Figure 8.7), that is:

-  **Policy “Majority”** the perspective gets the threshold of the target threshold that numerically exceeds the others,

-  **Policy “Majority with Priority”** the perspective gets the threshold of a specific target,

-  **Policy “Priority”** the perspective gets the majority threshold of the targets in case the primary stated target returns the lower    threshold, namely the “green” one, while it gets the threshold of a primary stated target in case the latter returns the other          thresholds, namely the “yellow” or the “red” one.

   |image169|

   Figure 8.7: Perspective policy.

Remember to save once perspectives and targets have been set.

8.2 Creation of a Scorecard document
-------------------------------------

Once saved it is possible to develop a scorecard document which can be easily consulted by (authorized) end users. To create a scorecard document click on the “Plus” icon available in the document browser and then “Generic document” from the panel as shows Figure 8.8. Here fill

   |image170|

   Figure 8.8: Create a generic document from document browser.

in mandatory fields (marked with an asterisk) and select the KPI type and **KPI engine**. Then open the “Template build”. Here select the “Scorecard” option as in Figure 8.9 and consequently Creation of a Scorecard document choose an existing scorecard from the list. Make the desired customizations and save.

   |image171|

   Figure 8.9: Template creation window.

Figure 8.10 gives an example of the scorecard document interface. The arrows point out the perspectives’ achievement of the goals or, on the contrary, the missing of the targets. As well the achievement/failure of the single targets is pinpointed by the arrow signals close to each target.

   |image172|

   Figure 8.10: Scorecard document interface.

Note that it is possible to check the policy used for each perspective. In fact, by clicking on one of them a wizard opens showing the policy adopted and the goal got by ach KPI.

   |image173|

   Figure 8.11: Scorecard document interface.
   
        .. include:: scoreCardThumbinals.rst
