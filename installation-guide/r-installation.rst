R Engine
================

As for Python, also the R functionalities leverage on a standalone webservice, this time written in R. Take a look at the official R Project documentation and find out how to get R (https://www.r-project.org/).
The official supported version is R >=3.5.1, but we recommend to use 3.6.x whenever it's possible.

Install knowage-r webservice
-------------------

Inside the Knowage-Server github repository, under the Knowage-R folder you can find the sources of the knowage-r webservice.

Once you have downloaded the source code, you will have to create the configuration for the webservice. This configuration will be contained inside a file called ``configs.R`` and placed inside the ``Knowage-R`` folder.

The configuration is indeed really simple since you only need to specify the Knowage HMAC key contained in the server.xml file.

In the ``constants.R`` file you can set the default webservice port and a whitelist of IP addresses that can contact the webservice.

Run knowage-r webservice
-------------------

Once you have installed all the requirements, you need to get the r-webservice running. 
In order to do so, it's enough to run the main file "knowage-r.R" with the basic R interpreter, via the RScript command or an equivalent one.

.. important::
     **Webservice permissions**

     The knowage-r webservice must have the rights to read/write in its own folder. 


Configure Knowage to enable Python/R functionalities
================

From the Knowage interface you can now enable the Python/R functionalities. 

Go to the ``Roles management`` section, in the *Authorizations* tab under *Widgets* check the ``Edit Python Scripts`` option.
Now you will be able to see the Python and R Dataset and Widget among the list of available ones.

Go to the ``Configuration management`` section, and create new variables of category ``PYTHON_CONFIGURATION`` and ``R_CONFIGURATION``. The value of this variables will specify the addresses of the Python and R webservices (es. ``python.webservice.address.com/domain``).
Now you will be able to see the addresses of the so configured environments when creating a Dataset or a Widget.

**Be aware that depending on the architecture of your solution, you might have to define two different addresses for reaching the same instance of Python.**

*  One address is for reaching Python from the client (browser) and will be used when creating a widget,
*  One address is for reaching Python from the server (Knowage) and will be used when creating a Dataset.

