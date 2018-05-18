
   The **What-if** analysis is the capability to make hypothesis and see
   how these impacts on the business. In practise user can perform
   What-if analysis using an extension of the OLAP tool. The process of
   What-if is composed in three phases:

-  data preparation,

-  workflow definition,

-  hypothesis definition.

   We start then focusing on this last phase.

Interface details
---------------------

   The workflow has an impact on data visualization. A user can
   understand the state of the workflow looking at the What-if section
   of the sidebar. There are three possibilities described in the
   following.

-  The user can perform the What-if analysis: in this case the What-If
      section contains the buttons to edit values; see Figure 9.1 to
      check those buttons.

   Interface details

   |image209|

   Figure 9.1: What-If buttons inside the sidebar.

-  The schema is locked by another user. In this case a message appears
      with the name of the active user in the workflow as shown in
      Figure 9.2.


   |image210|

   Figure 9.2: The What-If is used by another user.

    Meta-language description • The workflow is finished.

   |image211|

   Figure 9.3: The What-If is finished.

   We briefly recall the fuctionality of the main buttons:

-  Unlock model: it changes the state of the workflow in order to move
      control to next user.

-  Save: it persists modification in the database.

-  Save as new version: it persists modification in the database in a
      new version.

-  Undo: it undoes last modification.

-  Delete versions: it opens a wizard user can use to delete versions.

-  Output wizard: it allows user to export the edit cube in two
      different formats, table and csv in the specific.

 Meta-language description
-----------------------------

   We saw that the What-If engine allows the final user to change data
   values. Here we see how it is possible to modify a cell value through
   a formula, unconditionally from the aggragation level of the cell.
   The formula must be written using a particular language called
   **meta-language** that is described below. Firstly the available
   arithmetic symbols are: + - :sub:`\*` / ( ) %.

   The computation 100 + 10% is a simple example of usage of the
   operation %. Note that the formula can start with "=", but this is
   not mandatory.

   To activate the editing of a measure cell that is not shown in the
   OLAP you must first click on the filter icon of the measure filter
   card and check the target measure. Then select the version you want
   to use and change values of Figure 9.4 shows where are available
   these objects in the interface.

   |image212|

   Figure 9.4: Checking measures and selecting version.

   Then double-click on the target measure cell and a box will appear
   allowing you to insert a formula. Type the computation syntax and
   click on the *f*\ (*x*) icon to convalidate it or cancel it, as shown
   in Figure 9.5.

   |image213|

   Figure 9.5: Inserting formula and its convalidation.

   We stress that you can also refer to members that are not included in
   the tuple represented by the cell that is going to be modified. Let’s
   see some examples. For example suppose the cell refers to the
   following tuple reported in Code 9.1:

+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],     |
| [Region].[                                                            |
|                                                                       |
|    Mexico Central], [Customers].[All Customers], [Customers].[All     |
|    Customers]                                                         |
+-----------------------------------------------------------------------+


    Product.Deli

   you can refer to the tuple in Product.Eggs with just Product.Eggs and at
   the same time to the tuple in Product.Eggs; Measures.Unit Sales with just :sub:`Product.Eggs;
   Measures.Unit Sales`.

+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Food].[Eggs], [Version].[0],     |
| [Region].[                                                            |
|                                                                       |
|    Mexico Central], [Customers].[All Customers], [Customers].[All     |
|    Customers]                                                         |
+-----------------------------------------------------------------------+



   Product.Eggs

+-----------------------------------------------------------------------+
| [Measures].[Unit Sales], [Product].[Food].[Eggs], [Version].[0],      |
| [Region].[                                                            |
|                                                                       |
|    Mexico Central], [Customers].[All Customers], [Customers].[All     |
|    Customers]                                                         |
+-----------------------------------------------------------------------+


   Product.Eggs; Measures.Unit Sales

   Note that if you create a formula on a cell and you want to move it
   along a dimension (for example the cell refers to member Time.2016
   and you want to get value for Time.2017) you have to refer to a
   member of same level. So for example you can get value of the cell
   for Time.2017, but not for Time.2017.May.

   The syntax is as the one shown in Referring to different members or, in case you are using
   another hierarchy, as in Code 9.5 where you can concatenate different
   members with ";".

+-----------------------------------------------------------------------+
| <dimension's name>.<member's name>or[<dimension's name>].[<member's   |
| name>]                                                                |
+-----------------------------------------------------------------------+

    Referring to different members.

+-----------------------------------------------------------------------+
| <dimension's name>.<hierarchy's name>.<member's name>or[<dimension's  |
| name>].[< hierarchy's name>].[<member's name>]                        |
+-----------------------------------------------------------------------+



    Referring to different members of another hierarchy.

   You can also refer to members that are on the same level but they are
   not sibling members:

   suppose that, for example, the cell’s tuple is as in  Example of cell’s tuple.

+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Food].[Deli], [Version].[0],     |
| [Region].[                                                            |
|                                                                       |
|    Mexico Central], [Customers].[All Customers], [Customers].[All     |
|    Customers]                                                         |
+-----------------------------------------------------------------------+


   Example of cell’s tuple.

   Note that you can refer to the tuple

+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Drink].[Alcoholic Beverages],    |
| [Version                                                              |
|                                                                       |
|    ].[0], [Region].[Mexico Central], [Customers].[All Customers],     |
|    [Customers                                                         |
|                                                                       |
|    ].[All Customers]                                                  |
+-----------------------------------------------------------------------+


    Example of cell’s tuple

   just with:

+---------------------------------------+
| [Product].[Drink.Alcoholic Beverages] |
+---------------------------------------+



   Shorten syntax code.



+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Food].[Deli].[Meat],             |
| [Version].[0], [                                                      |
|                                                                       |
| Region].[Mexico Central], [Customers].[All Customers],                |
| [Customers].[All                                                      |
|                                                                       |
|    Customers]                                                         |
+-----------------------------------------------------------------------+


    Example of cell’s tuple



+-----------------------------------------------------------------------+
| [Measures].[Store Sales], [Product].[Drink].[Alcoholic                |
| Beverages].[Beer and                                                  |
|                                                                       |
|    Wine], [Version].[0], [Region].[Mexico Central], [Customers].[All  |
|    Customers                                                          |
|                                                                       |
|    ], [Customers].[All Customers]                                     |
+-----------------------------------------------------------------------+


    Example of shorten cell’s tuple

   is as in Used expression.

+-----------------------------------------------------+
| [Product].[Drink.Alcoholic Beverages.Beer and Wine] |
+-----------------------------------------------------+



   Used expression.

   Note that the last part of the expression is the portion of the path
   to the target member that differs from the path of the cell’s member.
   Some other examples:

+------------------+
| [Product].[Food] |
+------------------+



   Further example.
   
     .. include:: whatIfThumbinals.rst