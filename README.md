# Knowage Documentation
[![Documentation badge](https://readthedocs.org/projects/spagobi/badge/?version=latest)](http://spagobi.readthedocs.org/en/latest/)

## How to contribute

The contribution process is based on GitHub pull requests (https://help.github.com/articles/about-pull-requests/).
Contributions are taken into account as soon as possible, reviewed by Knowage Labs team and merged only if they comply with our standard (see below).

## How to write it

This documentation is written using ***reStructuredText*** format. reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system.

Official resources to learn:
- http://docutils.sourceforge.net/rst.html
- http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Other useful resources:
- https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

This documentation is intent to be used as source for Sphinx (http://www.sphinx-doc.org/en/master/index.html) and Read the Docs (https://readthedocs.org/) to render the documentation.

## Our standards

If you wish to contribute, in the following sections you can find standards and best practices. 

### Structure
                                              
Titles are underlined with a nonalphanumeric character at least as long as the text.
* `#` for parts
* `=` for chapters
* `-` for sections
* `~` for subsections
* `^` for paragraphs

#### Example

```rst
Part I
########

Chapter 2
===========

Section 3
-----------
```

---

### Codes

To adding a code you need to use this syntax:

```rst
.. code-block:: Type of language
    :linenos:
    :caption: Title.
      Text of the code
```

#### Example

```rst
.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.
    
      <COLUMNS> 
        <COLUMN field="store_id" visible="false" editable="false" /> 
```

---

### Images

There are three differents way to add an image, its depend if it is inline of the text, if it is out of the text or if it is inside a table.

1. Added an image inline:

  Insert the `|imageX|` inside the text and then recall it outside the text (anywhere in the text) whit this syntax:
  
  ```rst
  .. |imageX| image:: media/imageX.png
              :width: dimension
  ```
                   
2. Added an image oustide:

  At the point you need to insert an image use this:
  
  ```rst
  .. figure:: media/imageX.png

    Caption of the image.
  ```

3. Added an immage inside a table:

```rst
   +-------------------------------+-----------------------+
   |    Icon                       | Name                  |
   +===============================+=======================+
   | .. figure:: media/imageX.png  | Name ImageX           |
   |                               |                       |
   |                               |                       |
   +-------------------------------+-----------------------+
   | .. figure:: media/imageY.png  | Name ImageY           |
   |                               |                       |
   |                               |                       |
   +-------------------------------+-----------------------+
 
```

#### Example

```rst
1. If your dataset is similar to another existing dataset, you can click the **Clone** icon |image16|.

    .. |image16| image:: media/image23.png
       :width: 30
   
2. In the **Detail** tab you define the Name, the Label and an optional Description of the dataset (refer to figure below). 

    .. figure:: media/image22.png

        Dataset Panel.
 
3. +-------------------------------+-----------------------+-----------------------+
   |    Icon                       | Name                  | Description           |
   +===============================+=======================+=======================+
   | .. figure:: media/image8.png  | Knowage user          | Open a hidden menu    |
   |                               |                       | with extra            |
   |                               |                       | functionalities.      |
   +-------------------------------+-----------------------+-----------------------+
   | .. figure:: media/image9.png  | Select role           | Select the            |
   |                               |                       | authentication role   |
   |                               |                       | (available if you are |
   |                               |                       | associated to more    |
   |                               |                       | than one role).       |
   +-------------------------------+-----------------------+-----------------------+
        
```

---

### Tables

To create a table into the document you need to "draw" the contours of the table physically as shown below. 
     
     +------------+------------+--------------+
     | HeaderA    | HeaderB    | HeaderC      |
     +============+============+==============+
     |    AA      | BA         | CA           |
     |            |            |              |
     +------------+------------+--------------+
     |    AB      | BB         | BC           |
     |            |            |              |
     +------------+------------+--------------+



#### Example

```rst
     +-----------------------+-----------------------+-----------------------+
     |    Dataset            | Private               | Public                |
     +=======================+=======================+=======================+
     |    User               | Created from file     | Dataset created from  |
     |                       | (CSV, XLS) or from    | file (CSV, XLS) or    |
     |                       | QbE (My Data) for     | from QbE (My Data)    |
     |                       | personal use only.    | and shared with other |
     |                       |                       | users.                |
     +-----------------------+-----------------------+-----------------------+
     |    Technical          | Not applicable.       | Dataset created by a  |
     |                       |                       | BI developer to be    |
     |                       |                       | used in one or more   |  
     |                       |                       | documents.            |
     |                       |                       |                       |
     |                       |                       | Not visible to end    |
     |                       |                       | users.                |
     +-----------------------+-----------------------+-----------------------+
     |    Enterprise         | Not applicable.       | Dataset of any type   |
     |                       |                       | created by a          | 
     |                       |                       | technical user and    |
     |                       |                       | certified by a        |
     |                       |                       | trusted entity within |
     |                       |                       | the organization, and |
     |                       |                       | made available to all |
     |                       |                       | end users for reuse.  |    
     +-----------------------+-----------------------+-----------------------+
```

---

### Text style

There are several ways to optimize parts or words in the text.

1. Bold text:
 
 ```rst 
 **text to be emphasized**
 ```
 
 2. Italic text:
 
 ```rst 
 *text to be emphasized*
 ```
 
 3. Highlighted text (e.g. code, filename, parameter, and so on):
 
  ```rst 
 ``text to be emphasized``
 ```
 
 4. Bulleted list:
 
  ```rst 
 - First step
 - Second step
 - Third step
 ```
 
#### Example

 ```rst 
1.
Let us suppose to enter, with end user credentials, the data management area clicking on the **Workspace** icon from BI functionalities menu as shown in figure below and the **Data** section of the window.
2.
Click the *Add* icon
3.
Define the ``JAVA_HOME`` variable inside the users’ file ``.bash_profile`` used in the installation process
4.
- **My dataset**: datasets created by yourself uploading a CSV or XLS file or creating a query on a business model using the Qbe interface;
- **Enterprise dataset**: certified datasets,namely datasets created by the technical/experts users and shared with the end user.
- **Shared dataset**: datasets created and shared by other end users;

 ```
 ---

### Box

Sometimes into the text you need to draw attention with a box. We use four differents type of boxes.

```rst
.. note::
      **Read more**
         
      Text of the note.
         
.. warning::
      **Warning**
         
      Text of the warning.
         
.. hint::
      **Advice**
         
      Text of the hint.
         
.. important::
      **Notable content**
         
      Text of the important.  
```
  
#### Example

 ```rst
.. hint::
      **Authentication Management**:
      The choice of handling authentication internally or delegating it to an external SSO system typically depends on the presence of an authentication system already in place. If this is the case, Knowage can seamlessly integrate with the existing authentication infrastructure.
```

---
