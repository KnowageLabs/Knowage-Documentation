# Documentación de Knowage

[![Documentation badge](https://readthedocs.org/projects/spagobi/badge/?version=latest)](http://spagobi.readthedocs.org/en/latest/)

## Cómo contribuir

El knowage está abierto a contribuciones externas. Puede enviar sus contribuciones a este repositorio a través de un pull request.
Antes de comenzar, aquí hay algunas cosas que debes tener en cuenta:

*   Este proyecto se lanza con un [Código de conducta del colaborador](./CODE_OF_CONDUCT.md). Al participar en este
    proyecto, usted acepta cumplir con sus términos.
*   Al abrir un pull request, debe firmar el
    [Acuerdo de licencia de colaborador individual](./CLA.md) indicando en un comentario
    *"He leído el Documento de la CLA y por la presente firmo la CLA"*
*   Por favor, asegúrese de que su contribución pase todas las pruebas. Si hay fallas en las pruebas, deberá abordarlas
    antes de que podamos fusionar su contribución.

Las contribuciones se tienen en cuenta lo antes posible, son revisadas por el equipo de Knowage Labs y se fusionan solo si cumplen con nuestro estándar (ver más abajo).

## Cómo escribirlo

Esta documentación está escrita utilizando ***reStructuredText*** formato. reStructuredText es un sistema de sintaxis y analizador de marcado de texto plano fácil de leer, lo que ves es lo que obtienes.

Recursos oficiales para aprender:

*   http://docutils.sourceforge.net/rst.html
*   http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Otros recursos útiles:

*   https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
*   https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

Esta documentación tiene la intención de ser utilizada como fuente para Sphinx (http://www.sphinx-doc.org/en/master/index.html) y Read the Docs (https://readthedocs.org/) para representar la documentación.

## Nuestros estándares

Si desea contribuir, en las siguientes secciones puede encontrar estándares y mejores prácticas.

### Estructura

Los títulos se subrayan con un carácter no alfanumérico al menos tan largo como el texto.

*   `#` para piezas
*   `=` para capítulos
*   `-` para secciones
*   `~` para subsecciones
*   `^` para párrafos

#### Ejemplo

```rst
Part I
########

Chapter 2
===========

Section 3
-----------
```

***

### Códigos

Para agregar un código, debe usar esta sintaxis:

```rst
.. code-block:: Type of language
    :linenos:
    :caption: Title.
      Text of the code
```

#### Ejemplo

```rst
.. code-block:: xml
    :linenos:
    :caption: Pointing at a numerical column.
    
      <COLUMNS> 
        <COLUMN field="store_id" visible="false" editable="false" /> 
```

***

### Imágenes

Hay tres formas diferentes de agregar una imagen, depende si está en línea del texto, si está fuera del texto o si está dentro de una tabla.

1.  Añadida una imagen en línea:

Inserte el icono `|imageX|` dentro del texto y luego recuérdelo fuera del texto (en cualquier parte del texto) con esta sintaxis:

```rst
.. |imageX| image:: media/imageX.png
            :width: dimension
```

2.  Añadida una imagen esterior:

En el momento en que necesite insertar una imagen, use esto:

```rst
.. figure:: media/imageX.png

  Caption of the image.
```

3.  Se ha añadido un immage dentro de una tabla:

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

#### Ejemplo

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

***

### Tablas

Para crear una tabla en el documento, debe "dibujar" los contornos de la tabla físicamente como se muestra a continuación.

     +------------+------------+--------------+
     | HeaderA    | HeaderB    | HeaderC      |
     +============+============+==============+
     |    AA      | BA         | CA           |
     |            |            |              |
     +------------+------------+--------------+
     |    AB      | BB         | BC           |
     |            |            |              |
     +------------+------------+--------------+

#### Ejemplo

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

***

### Estilo de texto

Hay varias maneras de optimizar partes o palabras en el texto.

1.  Texto en negrita:

```rst
**text to be emphasized**
```

2.  Texto en cursiva:

```rst
*text to be emphasized*
```

3.  Texto resaltado (por ejemplo, código, nombre de archivo, parámetro, etc.):

```rst
``text to be emphasized``
```

4.  Lista con viñetas:

```rst
- First step
- Second step
- Third step
```

#### Ejemplo

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

***

### Box

A veces en el texto necesitas llamar la atención con un cuadro. Utilizamos cuatro tipos diferentes de box.

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

#### Ejemplo

```rst
.. hint::
     **Authentication Management**:
     The choice of handling authentication internally or delegating it to an external SSO system typically depends on the presence of an authentication system already in place. If this is the case, Knowage can seamlessly integrate with the existing authentication infrastructure.
```

***
