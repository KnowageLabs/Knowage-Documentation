
REGISTRY
========

A Registry document allows users to write, cancel and modify items of a datamart. Knowage allows users to implement a Registry document through the **Qbe Engine**. By the way it has a different graphical interface compared to the Qbe one. An example is given in Figure 12.1. In next chapters we will see how to navigate a Registry document  and how to create a new one :ref:`(Section 12.2) <Registry development>` (Section 12.2).

   |image333|

   Figure 12.1: Example of Registry document.
   

Registry features
-------------------

The execution of a Registry document opens a plain table: the records are shown in rows and they can be browsed using the pagination available at the bottom of the window. We underline that it is possible to edit each item of the table. Just double-click on a cell you may wish to rearrange and type a string or a numeric value accordingly. Some examples are highlighted in Figure 12.2.


   |image334|

   Figure 12.2: Editing table cells.

Moreover, you can add new rows from scratch selecting the “Plus” icon |image335| on the left of the functionality bar (Figure 12.3) available at the top of the window. Insert in each cell the corresponding value: string or number.

   |image336|

   Figure 12.3: Functionality bar.

   |image337|

   Figure 12.4: Adding a new row.

Vice versa, you can delete one or more rows using the “Minus” icon |image338| of the functionality bar (Figure 12.3) available at the top of the window. 

It is important to click on the Save button |image339| to store the adjustments done in the datamart.

Furthermore you can use filters, if implemented, of the functionality bar. Pick one field out of the combobox. Click on the “Filter” icon |image340| to run the functionality. Otherwise, click on the “Cancel” icon |image341| to clear the boxes off.

Note that, since records are displayed in a plain table, it is available a combobox (see Figure 12.5) which allows the user to visualize all fields related to the record of the previous cell and then change from one to another to get all data.

   |image342|

   Figure 12.5: Select one field from a combobox.

JPivot Registry characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to implement also a JPivot Registry document. The graphical features are very similar to the ones exposed in Section 12.1. An example is given in Figure 12.6.

   |image343|

   Figure 12.6: Example of Jpivot Registry document.

In this case the table shows columns organized in a hierarchical way and a grouping function is implemented. From the left to the right the columns contain fields at different detail levels. The last column in our example in Figure 12.6 contains numeric data. Such a field is grouped at the “country” level. The grouping level depends on the configurations made on template building.

In the JPivot instance it is not allowed to add, modify or cancel rows. Furthermore, it is not permitted to edit cells which contain string items while the numeric ones are still changeable. If implemented filters are still available.
   
        .. include:: registryThumbinals.rst
