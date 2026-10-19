Create and manage datasets
==========================

A dataset supplies tabular data to analytical documents. Its definition
contains the source, query or retrieval logic, parameters and column metadata.

1. Open **Modules** > **Data Providers** > **Dataset Management** with a role
   authorized to create datasets. Workspace also exposes the data operations
   permitted to end users.
2. Create a dataset and enter a unique label, name and description.
3. Choose its type and complete the source-specific settings described below.
4. Define any parameters, then run a preview with representative values.
5. Review the metadata: data types, aliases and attribute/measure roles.
6. Save the dataset and verify its availability with the roles that will use it.

Use the list actions to reopen, clone or delete a dataset when permitted.
Review references from documents and other objects before renaming or deleting
it. A document author selects an available dataset and maps its parameters to
the inputs required by that document.

.. figure:: /_static/screenshots/9.1/chapter-3-create-dataset-index-9-1-dataset-management.png

   Dataset list, type selection and editor in Knowage 9.1.

.. toctree::
   :maxdepth: 1

   query
   file
   flat
   rest
   solr
   python
   qbe
   advanced
