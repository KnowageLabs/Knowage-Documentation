AI management
=============

.. important:: Enterprise Edition (EE) only

   AI Management is reserved for **Knowage Enterprise Edition (EE)**.
   It requires an EE license, the configured AI integration and an authorized role.

Open **AI Management** from the authorized modules. The integration requires a configured
``KNOWAGE.AI.URL`` and the ``EngGPTIntegration`` functionality on the role.
The engine overview shows the configured service, reachability and
synchronization state.

1. Check the engine overview and resolve connection errors before synchronizing.
2. Review the business-model list and choose which models to include for AI use.
3. Synchronize the included business models and the knowledge base using the
   corresponding actions, then check the reported status.
4. Select a business model to maintain its gold queries, where supported by
   the configured service. Save the changes before leaving that model.
5. Test the :doc:`/user-guide/ai-assistant` with a representative reader account.

Gold queries are curated examples associated with a business model. Keep their
questions, queries and expected business meaning aligned with that model's
schema. Recheck synchronization after changing model metadata or the available
source structure.

.. figure:: /_static/screenshots/9.1/chapter-4-ai-management-9-1-ai-management.png

   AI engine status, model inclusion and synchronization.

The external AI service, model configuration and connectivity are deployment
prerequisites. Configure them through the distribution's supported integration
settings; the management page reports the state of that integration.
