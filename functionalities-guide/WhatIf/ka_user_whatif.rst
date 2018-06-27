What-if analysis
=================

The **What-if** analysis is the capability to make hypothesis and see how these impacts on the business. In practise user can perform What-if analysis using an extension of the OLAP tool. The process of What-if is composed in three phases:

-  data preparation,
-  workflow definition,
-  hypothesis definition.

We start then focusing on this last phase.

Interface details
-------------------

The workflow has an impact on data visualization. A user can understand the state of the workflow looking at the What-if section of the sidebar. There are three possibilities described in the following.

-  The user can perform the What-if analysis: in this case the What-If section contains the buttons to edit values; see figure below to
   check those buttons.
      
.. figure:: media/image213.png

      What-If buttons inside the sidebar.

-  The schema is locked by another user. In this case a message appears with the name of the active user in the workflow as shown below.

.. figure:: media/image214.png

     The What-If is used by another user.
    
-   The workflow is finished.

.. figure:: media/image215.png

      The What-If is finished.

We briefly recall the fuctionality of the main buttons:

-  Unlock model: it changes the state of the workflow in order to move control to next user.
-  Save: it persists modification in the database.
-  Save as new version: it persists modification in the database in a new version.
-  Undo: it undoes last modification.
-  Delete versions: it opens a wizard user can use to delete versions.
-  Output wizard: it allows user to export the edit cube in two different formats, table and csv in the specific.

Meta-language description
---------------------------

We saw that the What-If engine allows the final user to change data values. Here we see how it is possible to modify a cell value through a formula, unconditionally from the aggragation level of the cell. The formula must be written using a particular language called **meta-language** that is described below. Firstly the available arithmetic symbols are: + - :sub:`\*` / ( ) %.

The computation 100 + 10% is a simple example of usage of the operation %. Note that the formula can start with "=", but this is not mandatory.

To activate the editing of a measure cell that is not shown in the OLAP you must first click on the filter icon of the measure filter card and check the target measure. Then select the version you want to use and change values of figure below shows where are available these objects in the interface.

.. figure:: media/image216.png

    Checking measures and selecting version.

Then double-click on the target measure cell and a box will appear allowing you to insert a formula. Type the computation syntax and click on the *f*\ (*x*) icon to convalidate it or cancel it, as shown below.

.. figure:: media/image218.png

    Inserting formula and its convalidation.

We stress that you can also refer to members that are not included in the tuple represented by the cell that is going to be modified. Let’s see some examples. For example suppose the cell refers to the following tuple reported in Code below:

.. code-block:: 
   :linenos:
   :caption: Product.Deli

    [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],   
    [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]


You can refer to the tuple in :numref:`producteggs` with just Product.Eggs and at the same time to the tuple in Code 9.3 with just Product.Eggs; Measures.Unit Sales 

.. _producteggs:
.. code-block:: 
   :linenos:
   :caption: Product.Eggs
   
    [Measures].[Store Sales], [Product].[Food].[Eggs], [Version].[0],        
    [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]   


.. code-block:: 
   :linenos:
   :caption: Product.Eggs; Measures.Unit Sales
   
      [Measures].[Unit Sales], [Product].[Food].[Eggs], [Version].[0],                              
      [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers] 


Note that if you create a formula on a cell and you want to move it along a dimension (for example the cell refers to member Time.2016 and you want to get value for Time.2017) you have to refer to a member of same level. So for example you can get value of the cell for Time.2017, but not for Time.2017.May.

The syntax is as the one shown in Referring to different members or, in case you are using another hierarchy, as in :numref:`referringdiffmembers` where you can concatenate different members with ";".

.. code-block:: 
   :linenos:
   :caption: Referring to different members.
   
      <dimension's name>.<member's name>or[<dimension's name>].[<member's name>]                      

.. _referringdiffmembers:
.. code-block:: 
   :linenos:
   :caption: Referring to different members of another hierarchy.
   
      <dimension's name>.<hierarchy's name>.<member's name>or[<dimension's name>].[< hierarchy's name>].[<member's name>]  


You can also refer to members that are on the same level but they are not sibling members:
suppose that, for example, the cell’s tuple is as in Code below:

.. code-block:: 
   :linenos:
   :caption: Example of cell’s tuple.
   
   [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],        
   [Region].[Mexico Central], [Customers].[All Customers], [Customers].[All Customers]


Note that you can refer to the tuple

.. code-block:: 
   :linenos:
   :caption: Example of cell’s tuple.
   
      [Measures].[Store Sales], [Product].[Drink].[Alcoholic Beverages],  
      [Version].[0], [Region].[Mexico Central], [Customers].[All Customers],  
      [Customers].[All Customers]                                                  

just with:

.. code-block:: 
   :linenos:
   :caption: Shorten syntax code.
   
      [Product].[Drink.Alcoholic Beverages] 

Another example from Code below

.. code-block:: 
   :linenos:
   :caption: Example of cell’s tuple.
   
       [Measures].[Store Sales], [Product].[Food].[Deli].[Meat],            
       [Version].[0], [Region].[Mexico Central], [Customers].[All Customers],

to Code below

.. code-block:: 
   :linenos:
   :caption: Example of cell’s tuple.
   
     [Measures].[Store Sales], [Product].[Drink].[Alcoholic Beverages].[Beer and Wine], [Version].[0], 
     [Region].[Mexico Central], [Customers].[AllCustomers], [Customers].[All Customers]                                                                          
is as in the following code

.. code-block:: 
   :linenos:
   :caption: Used expression.
   
      [Product].[Drink.Alcoholic Beverages.Beer and Wine] 

Note that the last part of the expression is the portion of the path to the target member that differs from the path of the cell’s member. Some other examples:

.. code-block:: 
   :linenos:
   :caption: Further example.
   
      [Product].[Food]

   
.. include:: whatIfThumbinals.rst
