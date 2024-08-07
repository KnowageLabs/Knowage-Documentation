SQL Query Data Set
########################################################################################################################

Selecting the query option requires the BI developer to write an SQL statement to retrieve data.

Remember that the SQL dialect depends on the data source that has been chosen. The SQL text must be written in the Query text area. Below a SQL query example.

.. code-block:: sql
         :caption: SQL query example
         :linenos:

          SELECT p.media_type as MEDIA, sum(s.store_sales) as SALES
          FROM sales_fact_1998 s
          JOIN promotion p on s.promotion_id=p.promotion_id
          GROUP BY p.media_type

It is also possible to dynamically change the original text of the query at runtime. This can be done by defining a script (Groovy or JavaScript) and associating it to the query. Click on the **Edit Script** section (see next figure) to open the script editor and write your script. The base query is bounded to the execution context of the script (variable query) together with its parameters (variable parameters) and all the profile attributes of the user that executes the dataset (variable attributes).

.. _scripteditingdataset:
.. figure:: media/image31.png

    Script editing for dataset.

In the script below we use JavaScript to dynamically modify the ``FROM`` clause of the original query according to the value of the parameter *year* selected at runtime by the user. You can notice that the variable ``query``, provided by Knowage, contains the text of the SQL query.

.. code-block:: javascript
         :caption:  Example of a script in a *Query* dataset
         :linenos:

          if(isValid('year')) {		  
		    if( parameters.get('year') == 1997 ) {
                  query = query.replace('FROM sales_fact_1998', 'FROM sales_fact_1997');
              } else { 
                  query = query; // do nothing
              }
            }	  

In the above example we use the function *isValid* to test whether the parameter *year* contains a *null* value or not.