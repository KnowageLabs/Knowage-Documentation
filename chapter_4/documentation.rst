Documentation
########################################################################################################################

The **Documentation** section allows you to publish and browse internal Markdown-based documentation directly inside Knowage, without leaving the application. It is accessible at ``/docs`` and shows a sidebar menu on the left and the document content on the right.

How to access it
------------------------------------------------------------------------------------------------------------------------

Navigate to ``/docs`` in your Knowage instance. If the section has not been set up yet, you will be redirected to a 404 page.

How to set it up
------------------------------------------------------------------------------------------------------------------------

The documentation system reads its content from the Knowage **Resource Server**. You need to create a folder named exactly **docs** at the root level of the resource server, and place your files inside it.

Minimum required structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   docs/
   ├── config.json    ← defines the sidebar menu
   └── index.md       ← home page shown when opening /docs

You can organise your Markdown files freely in subfolders:

.. code-block:: none

   docs/
   ├── config.json
   ├── index.md
   ├── getting-started.md
   └── advanced/
       ├── configuration.md
       └── troubleshooting.md

The ``config.json`` file
------------------------------------------------------------------------------------------------------------------------

This file controls what appears in the sidebar menu: the title, an optional logo, and the list of pages with their labels and links.

Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "title": "My Documentation",
     "logo": true,
     "content": [
       {
         "label": "Introduction",
         "path": "/index.md"
       },
       {
         "label": "Advanced",
         "content": [
           {
             "label": "Configuration",
             "path": "/advanced/configuration.md"
           },
           {
             "label": "Troubleshooting",
             "path": "/advanced/troubleshooting.md"
           }
         ]
       },
       {
         "label": "Admin only page",
         "path": "/admin.md",
         "roles": ["ROLE_ADMIN"]
       }
     ]
   }

Available fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Top-level**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Field
     - Description
   * - ``title``
     - Optional. Text displayed at the top of the sidebar.
   * - ``logo``
     - Optional. Set to ``true`` to show the tenant logo, or provide a direct image URL (e.g. ``"https://example.com/logo.png"``). If omitted, no logo is shown.
   * - ``maxLevel``
     - Optional. Maximum nesting depth rendered in the sidebar menu. Accepted values: ``1``, ``2``, ``3``. Defaults to ``3``.
   * - ``content``
     - Required. The list of menu items (see below).

**Menu item fields**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Field
     - Description
   * - ``label``
     - The text displayed in the sidebar for this item.
   * - ``path``
     - The path to the ``.md`` file to open, relative to the ``docs`` folder (e.g. ``/advanced/configuration.md``). **If omitted, the item is shown as a non-clickable section heading**, useful for grouping related pages.
   * - ``content``
     - A list of child items. You can nest up to **3 levels** deep.
   * - ``roles``
     - Optional. A list of Knowage roles. If provided, the item (and all its children) will only be visible to users whose role matches one of the listed values. Other users will not see it at all.

Writing pages
------------------------------------------------------------------------------------------------------------------------

Each page is a standard **Markdown** (``.md``) file. The following formatting features are supported:

- Headings (``#``, ``##``, ``###``)
- Bold, italic, lists, tables
- Inline code and code blocks (with syntax highlighting)
- Hyperlinks
- **Mermaid diagrams** — write a fenced code block with the language set to ``mermaid`` and it will be automatically rendered as a diagram:

.. code-block:: markdown

   ```mermaid
   graph TD
     A[Start] --> B[Step 1]
     B --> C[End]
   ```

Sidebar behaviour
------------------------------------------------------------------------------------------------------------------------

- Clicking an item with a ``path`` opens the corresponding page.
- Items **without** a ``path`` act as section headers: they are not clickable, but their children are.
- The currently open page is highlighted in the sidebar with a coloured left border.
- On small screens, the sidebar is hidden by default and can be toggled with the **☰** button at the top left.

Copying a page link
------------------------------------------------------------------------------------------------------------------------

Each page has a **🔗** button in the top right corner. Clicking it copies the direct URL of the current page to your clipboard, so you can share it with other users.

Customising the appearance
------------------------------------------------------------------------------------------------------------------------

All colours, fonts and sizes can be changed from **Theme Management** → **documentation** section. Changes apply to the entire Documentation section immediately after saving the theme.

**Sidebar**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Description
   * - Drawer Background Color
     - Background colour of the sidebar
   * - Drawer Text Color
     - Default text colour for menu items (levels 2 and below)
   * - Drawer Active Link Color
     - Colour of the active item and hover highlight
   * - Drawer Font Family
     - Font used in the sidebar (levels 2 and below)
   * - Drawer Font Size
     - Font size in the sidebar (levels 2 and below)
   * - Drawer Level 1 Text Color
     - Text colour for top-level menu items only
   * - Drawer Level 1 Font Family
     - Font for top-level menu items only
   * - Drawer Level 1 Font Size
     - Font size for top-level menu items only

**Content area**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Description
   * - Content Background
     - Background of the page content area (supports any CSS value, including gradients)
   * - Content Text Color
     - Body text colour
   * - Content Font Family
     - Body font
   * - Content Font Size
     - Body font size
   * - Content Heading Color
     - Colour applied to ``h1``, ``h2``, ``h3`` headings
   * - Link Color
     - Colour of hyperlinks
   * - Code Background Color
     - Background of code blocks
   * - Code Text Color
     - Text colour inside code blocks
   * - Code Border Radius
     - Corner rounding of code blocks
