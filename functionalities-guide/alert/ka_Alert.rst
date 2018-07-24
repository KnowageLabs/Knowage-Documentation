Alert
===========

The **Alert** functionality available under the **Tool** section of Knowage main menu, as shown in Figure below, allows you to implement a control over events. Technically it consists of monitoring the possible overcoming of fixed thresholds and the consequent signal of anomalies by means of an email or by launching an ETL process. In next sections we will see in details how to configure the alarms using the Alert feature.

.. _alertfunctfrom:
.. figure:: media/image172.png

    Alert functionality from contextual menu.
   
Alert implementation
--------------------

The Alert definition window (refer to the figure above) diplays the list of existing alerts and a search box at the top of the page to facilitate to browse over the items. In the right top corner it is available the “Plus” icon to configure a new alert.

Clicking on the “Plus” icon the page in the following figure opens.

.. figure:: media/image173.png

    Alert definition window.
   
Give a name and select the **KPI listener** from the combobox. Then indicate the start date, the start time and eventually the Alert implementation end date. Specify the time interval and how many times it must be repeated. At this point choose between **Single Execution** and **Event before trigger actions**: in the first case the alert must signal the anomaly just once its occurence while in the other case it must send the alarms when the irregularity occurs as many times as specified. Note indeed that the box is editable and it must contain a number which indicates the number of irregularities that has to be detected before the alert starts.

.. figure:: media/image174.png

    Alert settings.

At the bottom of the page associate the KPI of interest and select the action by clicking on the **Add action** button. Here you can choose between **Send mail** or **Execute a document**.

If the “Send mail” is chosen, the user is asked to insert the thresholds that should be monitored: in case the latter are overcomed thefunctionality sends the email to the indicated subjects. Remember to insert all mandatory fields (name, thresholds and subjects of the mail) and, in particular, to select the user to which the email is sent. Note that in the mail subjects box you can type both mail addresses or usernames (for example “user_admin”), helped by the automatic insertion text is as shown in the next figure. In fact, Knowage server will pick out the mail address from the profile attribute associated to that user. Therefore, we recommend to set the profile attribute previously. In particular, remember that the profile attribute *must* be Alert implementation called “\ *email*\ ”.

.. _sendemailconf:
.. figure:: media/image175.png

    Send email configuration.

Furthermore, note that the mail body can contain a plain text message or a table showing the registered KPI values which activated the alert. To enable table visualization option you must insert the placeholder \*TABLE_VALUE\* in the mail body as shown in Figure below.

.. figure:: media/image176.png

   Send email containing a table with detected values.

If the “Execute a document” option is selected, the alert will launch an ETL process when the chosen thresholds are ovecomed. Namely, the functionality will launch a process to execute batch actions as the writing of proper tables of a DWH, creation of a file, the call to a log service. Note that the ETL process must exist as a document in Knowage server. An example is given in the following figure.

Save both the action and the alert configuration settings to store your alert. Remember that it is possible to schedule more than one monitoring over the same alert definition.

.. _executedocument:
.. figure:: media/image177.png

    Execute document configuration.
