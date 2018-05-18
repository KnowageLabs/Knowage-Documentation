
In the previous section we learned what the **QbE Engine** is and how
you can use it. Using the **QbE Engine**, power users can define complex
queries, without dealing with SQL code but still with a similar degree
of complexity. Indeed, end users may not feel comfortable with complex
queries and often prefer to execute queries that have already been
defined by expert users. The **Smart Filter Engine** provides end users
with an intuitive tool to customize queries that have already been
defined by power users. The logic behind the smart filter is more
similar to a filter (hence, the name) than to a query builder: this has
the advantage of being simple and intuitive for end users. At the same
time, users are enabled with different customization options to meet
their various needs in accessing and analyzing data. Before going into
details on the creation of a smart filter document, let us have a look
at the features provided by this engine.

 Overview
-------------

A smart filter document is based on an underlying query defined via the
QbE Engine. When the document is executed, a form is generated starting
from the query and containing all filtering criteria defined over the
base query. The end user can set filters value to extract the data of
interest. Once the end user has extracted the data, he can further
manipulate them by grouping them, viewing them in a master/detail
structure, or use them to build an ad-hoc analysis using the **Worksheet
Engine**.

The end user sees the form shown in Figure 11.1. This way the end user
can select filters according to his preferences and click on Show Data
to view results. In case there are grouping variables defined (e.g., the
“country” and “state_province” in Figure 11.1), the result window will
contain two sections, as shown in Figure 11.2:

   • the master section on the left: it contains all the possible
   combinations of the grouping variables,

Overview

   |image319|

   Figure 11.1: Smart filter selection form.

   |image320|

   Figure 11.2: Smart filter “Show Data” results.

 Smart Filter creation

   • the detail section on the right: when double-clicking on a row in
   the master section, you’ll see the results according to thegrouping
   variables previously selected.

In case no grouping variables are defined, only the detail section is
displayed. From the results page, the user can go back to the form by
clicking on **Back to form**. This allows him to change the filtering
criteria and view data modified accordingly.

     .. include:: smartFilterThumbinals.rst