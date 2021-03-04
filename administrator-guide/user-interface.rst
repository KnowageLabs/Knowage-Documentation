User Interface
================

This chapter focuses on Knowage user interface, providing detailed information on the Main Menu.

Main menu
-----------------

Knowage menu gives you access to all its functionalities. By default you find the menu button at the left bottom corner of the home page, click it to open the menu.

.. figure:: media/image9_bis.png

   Home page

You can minimize it by clicking somewhere else outside the menu. In this way the menu button appears and you can reopen the menu according to your needs. You can move this button around the page by dragging and dropping it. Choose the position that best fits with your work.

Knowage main menu is divided in three submenus: the user menu, the BI functionalities menu and the administrator one. The left panel contains the user menu, which is collapsed, and the BI functionalities menu, while the administrator menu is on the right panel.

.. figure:: media/image10.png

   Menu

The user menu (see below) is identified with the first icon in Table above and a label containing your user name. Opening the user menu you have the following extra buttons:

- **My roles** If your user is associated with more than one role, Knowage requests you to specify the default one. You can select it when executing a document, or right after authentication by clicking on this icon and choosing a default role.
- **Languages** To select the language of Knowage environment.
- **Accessibility** To enable or disable accessibility mode.
- **Info** To view the details of current Knowage version.
- **Logout** To go back to log in page.

The BI functionalities menu consists in a set of icons associated with basic features:

- **Documents development** This is a standard functionality of Knowage Server. It enables you to create the analytical document as well as access and execute them.
- **Workspace** From this section you can access the **Models** and create datasets and federations.

.. table:: Menu components - BI Functionalities Menu.
   :widths: auto

   +--------------------------------+-----------------------+-----------------------+
   |    Icon                        | Name                  | Description           |
   +================================+=======================+=======================+
   | .. figure:: media/image105.png | My Account            | Show or update user   |
   |                                |                       | info.                 |
   +--------------------------------+-----------------------+-----------------------+
   | .. figure:: media/image16.png  | Documents development | Document creation and |
   |                                |                       | acces to the archive  |
   |                                |                       | folders.              |
   +--------------------------------+-----------------------+-----------------------+
   | .. figure:: media/image17.png  | Workspace             | Inquiry your business |
   |                                |                       | models, navigate and  |
   |                                |                       | create your datasets. |
   +--------------------------------+-----------------------+-----------------------+
   | .. figure:: media/image103.png | Download              | Open a dialog that    |
   |                                |                       | show the available    |
   |                                |                       | async download.       |
   +--------------------------------+-----------------------+-----------------------+
   | .. figure:: media/image104.png | News                  | Open a dialog that    |
   |                                |                       | show the news.        |
   +--------------------------------+-----------------------+-----------------------+


.. important::
        **My Account** is visible only when ``SPAGOBI.SECURITY.MY_ACCOUNT_MENU`` configuration is enabled.

The administrator menu is divided in subpanels which maps the different managing areas:

- **Data Providers** Here you can set and manage Data Sources.
- **Profile Management** In this panel you can organize the users profilation, authorizations and attributes, but also organize the Analytical model. It means you can create/manage Roles, Users and Attributes as well as configure the functionality tree and the menu, i.e. the list of quick access link to analytical document or other resources provided to the users.
- **Behavioural model** Here you manage all the Behavioural model, which means create analytical drivers and lov. In this area you can access the constraints configuration too.
- **Catalogs** In this area you manage different catalogs, that may vary from product to product: the **Business Model** catalogues used for QbE; the **Layer Catalogs** for the creation of GIS analytical documents and so on.
- **Tools** In this area you can access the different scheduler options.
- **Server Settings** In this panel you have access to all server settings configuration options, such as configuration or domain management.
- **Server Manager** This is an optional package. It gives you access to different server functionalities, such as template management and all the import/export features.

.. table:: Menu components - Administrator Menu.
   :widths: auto

   +--------------------------------+-----------------------+------------------------+
   |    Icon                        | Name                  | Management areas       |
   +================================+=======================+========================+
   | .. figure:: media/image18.png  | Data Providers        | Data source settings.  |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image19.png  | Profile               | Profile Attributes,    |
   |                                | Management            | Roles, User and Menu   |
   |                                |                       | configuration          |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image20.png  | Behavioural model     | Lovs, Analytical       |
   |                                |                       | Driver and Constraints |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image21.png  | Catalogs              | Business Models and    |
   |                                |                       | Layers                 |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image22.png  | Tools                 | Scheduler              |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image23.png  | Server Settings       | User Data Properties,  |
   |                                |                       | Configuration,         |
   |                                |                       | Domains and Metadata   |
   +--------------------------------+-----------------------+------------------------+
   | .. figure:: media/image24.png  | Server Manager        | Template manager and   |
   |                                |                       | Import-Export          |
   |                                |                       | options                |
   +--------------------------------+-----------------------+------------------------+


---------------
My Account menu
---------------

*My account* button, if enabled, allows user to access Modify profile page. Here you can modify your information and also permanently delete your account.

Modify
^^^^^^
With this feature user can modify their own data such as Name, Surname and Email address. Password and Confirm password fields are mandatory so they must be filled before applying changes clicking on "MODIFY".

.. attention::

	If user fills *Password* and *Confirm password* fields with a valid password that is NOT the current password (used to log in), the password will be updated with the new value.

Delete account
^^^^^^^^^^^^^^

With this feature user can delete his account clicking on *DELETE ACCOUNT* button. Then a message confirms the correct cancellation and the login page is displayed.

.. attention::

	Account cancellation is irreversible. User will no longer be able to log into Knowage.

Password change
^^^^^^^^^^^^^^^

If user wants to change his password, he must fill *Password* and *Confirm Password* fields and the click on *MODIFY* button. A confirmation message will be displayed if the update has been successful.

.. figure:: media/image116.png

   My account - Modify profile
