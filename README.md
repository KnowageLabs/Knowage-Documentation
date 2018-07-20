# Knowage-Documentation

## Structure
                                                   
Titles are underlined with a nonalphanumeric character at least as long as the text.
* `#` for parts
* `=` for chapters
* `-` for sections
* `~` for subsections
* `^` for paragraphs

### Example

```
Part I
########

Chapter 2
===========

Section 3
-----------
```

## Code

To adding a code you need to use this syntax:

.. code-block:: Type of language
    :linenos:
    :caption: Title.
      Text of the code

### Example

```
.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.
    
      <COLUMNS> 
        <COLUMN field="store_id" visible="false" editable="false" /> 

```

## Image

There are two different way to add an image, its depend if it is inline of the text or is out of the text.

- Added an imaage inlin

  Insert the |imageX| inside the text and then recall it outside the text (anywhere in the text) whit this syntax:
  
.. |imageX| image:: media/imageX.png
   :width: 30

### Example

```
.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.
    
      <COLUMNS> 
        <COLUMN field="store_id" visible="false" editable="false" /> 

```


