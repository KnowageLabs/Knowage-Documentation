|image0|

Contents

1. Before starting 1

   1. Documentation structure . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . 1

2. Knowage at a glance 4

   2. Discovering Knowage . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . 4

   3. Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . . 4

   4. Layers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . . 5

Delivery layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 7

Analytical layer . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 7

Data layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 8

5. What you can do with Knowage . . . . . . . . . . . . . . . . . . . .
   . . . . . 8

Analytical and operational functionalities . . . . . . . . . . . . . . .
. . . 8

Administrative tools and cross services . . . . . . . . . . . . . . . .
. . . . 9

3. User Interface 10

   6. Main menu . . . . . . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . 10

4. Configure data sources 14

   7. Connect to your data . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . 14

   8. Big Data and NoSQL . . . . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . 16

Hive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 16

Spark SQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 18

HBase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 18

Impala . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 19

MongoDB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . 19

Cassandra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 20

Neo4j . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 21

Drill . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . 21

VoltDB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 22

Others . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 22

5. Behavioural Model 23

   9. Roles, users and attributes . . . . . . . . . . . . . . . . . . .
      . . . . . . . . . . 24

..

   i

Contents Contents

6. Analytical Model 28

   10. Repository structure and rights . . . . . . . . . . . . . . . . .
       . . . . . . . . . 28

   11. Menu configuration . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 30

7. Operational engines 32

   12. ETL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 32

   13. External processes . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 35

8. Scheduler 41

   14. Create an Activity . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 41

Save as snapshot . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . 44

Save as file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 45

Save as document . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . 45

Send to Java class . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 46

Send mail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 50

15. Schedulation panel . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . 51

16. Scheduler Monitor . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . 52

9. Server Manager 55

   17. Tenants Management . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 55

   18. Template Management . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 57

   19. Import\Export . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 57

Documents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 57

Menu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 59

Users . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 60

Catalogs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 61

KPIs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 62

Analytical Drivers . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . 64

Glossay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 67

Catalog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 67

10. Server Settings 69

    20. Configuration Management . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . 69

    21. Domain Management . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . 70

    22. Metadata . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . 71

..

   ii

1.1 Documentation structure
===========================

KnowAge documentation is composed by:

-  **Installation Manual**;

-  **General User Manual**;

-  **General Administrator Manual**;

-  one more book for each product purchased.

The books focusing on products describe all the BI functionalities
included in your installation. For example if you have purchased
KnowageBD subscription, you will get the installation and the two
general manuals plus a third one which focus on the BI functionalities
provided by this product.

Target
======

Each book is thought to be delivered to different users.

-  **Installation Manual**: it is aimed at technical users. It provides
      all the instructions needed to install and configure the Knowage
      suite. Here the essential steps to succeed with the standard
      installation on certified environments will be described,
      including the optional use of CAS as a SSO solution and the use of
      HTTPS protocol.

Documentation structure

-  **General User Manual**: it is aimed at end users. It provides a
      first approach to Knowage interface and functionalities. It can be
      used as a first approach to Knowage. It focus on all those
      elements which are shared among the products and involves the end
      user.

-  **General Administrator Manual**: it is aimed at Knowage
      admnistrator. It describes all the management and configuration
      tools shared by all Knowage products.

-  **Product Manuals**: as we mentioned above, these books are specific
      for each product. They are aimed both at end users and Knowage
      developers. Almost each chapter is divided in two parts: the first
      one can be interesting for both users and developers, while the
      second one is for developers only. The developer parts are marked
      by a \* to be easy recognised. We can conlcude that you just need
      to read all the parts not marked by \* to have a complete
      introduction to all BI functionalities included in your products.