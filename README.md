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
    
      Code

### Example

```
.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.
    
      <COLUMNS> 
        <COLUMN field="store_id" visible="false" editable="false" /> 

```
