   KnowAge

   Installation and configuration manual

   *Release 1.0* Editor

Contents

1. Before starting 1

   1. Documentation structure . . . . . . . . . . . . . . . . . . . . .
      . . . . . . . . 1

2. Goal of the document 4

3. Prerequisites 5

   2.  Operative systems . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 5

   3.  Disk usage . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 6

   4.  JDK version . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 6

   5.  Application server . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 8

   6.  JBoss Enterprise Application Platform (EAP) 6 . . . . . . . . . .
       . . . . . . . . 8

   7.  Tomcat 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 9

   8.  Database schema for metadata . . . . . . . . . . . . . . . . . .
       . . . . . . . . 10

   9.  Database schema for data. . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 10

   10. R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 10

4. Released files description 12

   11. Installation procedure . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 12

   12. Installer usage . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 13

   13. Uninstaller . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 21

5. Manual installation 24

   14. Metadata database . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 24

   15. Dependencies . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 24

   16. File system resources . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 25

   17. Metadata database connection . . . . . . . . . . . . . . . . . .
       . . . . . . . . 25

   18. Data database connection . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 26

   19. Environment variables definition . . . . . . . . . . . . . . . .
       . . . . . . . . . 27

   20. Applications deploy . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 28

   21. Datasource link within the applications . . . . . . . . . . . . .
       . . . . . . . . 29

   22. Configuration of the metadata db dialect . . . . . . . . . . . .
       . . . . . . . . 29

   23. Modification of the Quartz configuration . . . . . . . . . . . .
       . . . . . . . . 30

   24. Pool of thread definition . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 31

Contents Contents

25. Check of the memory settings . . . . . . . . . . . . . . . . . . . .
    . . . . . . . 32

26. LOG files . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . 33

27. Configuration file . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . 33

28. JAR library file . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . 35

29. server-config.wsdd tests . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . 35

6. R installation 37

7. Python installation 40

   30. JPY installation . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 40

8. CAS installation 43

   31. Deploy of the CAS application . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 43

   32. HTTPS certificate . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 44

   33. Configuration of the HTTPS protocol for Tomcat . . . . . . . . .
       . . . . . . . 45

   34. Configuration of the HTTPS protocol for JBoss . . . . . . . . . .
       . . . . . . . 45

   35. Knowage configuration . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 46

9. Advanced configuration 49

   36. Thread manager . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 49

   37. Cache parameters . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 50

   38. Logging . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 53

   39. Mail server . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 54

   40. Maximum file size . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 55

   41. Date format . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 56

   42. Language . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 56

   43. Security connectors . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 57

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
   installation on certified environments will be described, including
   the optional use of CAS as a SSO solution and the use of HTTPS
   protocol.

..

   Documentation structure

-  **General User Manual**: it is aimed at end users. It provides a
   first approach to Knowage interface and functionalities. It can be
   used as a first approach to Knowage. It focus on all those elements
   which are shared among the products and involves the end user.

-  **General Administrator Manual**: it is aimed at Knowage
   admnistrator. It describes all the management and configuration tools
   shared by all Knowage products.

-  **Product Manuals**: as we mentioned above, these books are specific
   for each product. They are aimed both at end users and Knowage
   developers. Almost each chapter is divided in two parts: the first
   one can be interesting for both users and developers, while the
   second one is for developers only. The developer parts are marked by
   a \* to be easy recognised. We can conlcude that you just need to
   read all the parts not marked by \* to have a complete introduction
   to all BI functionalities included in your products.

About conventions
=================

Some graphical conventions have been adopted to allow readers to easily
identify special contents such as notes, summaries and essential
information. All conventions are explained hereafter.

   |image0|

   Documentation structure

The following fonts have been adopted, to easily identify special words
and expressions:

-  **Menu**, **Menu items** and **static label** refer to specific
   element of Knowage GUI;

-  Input field is a label referencing input fields in Knowage GUI;

-  Code example is a piece of code showing configuration patterns or
   parts of document template.

..