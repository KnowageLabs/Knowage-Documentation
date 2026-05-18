# Conocimiento de un vistazo

## Descubriendo Knowage

Knowage es la suite de inteligencia de negocios desarrollada y administrada por Engineering Group. El conocimiento es *flexible*, ya que se basa en una arquitectura modular y estándares abiertos con el fin de facilitar su personalización e integración según las necesidades de los usuarios. También proporciona un *comprensivo* conjunto de características y capacidades analíticas que van desde herramientas tradicionales de informes y gráficos, hasta análisis más avanzados.

.. importante::
**Solo Enterprise Edition**

         KnowageER and KnowageSI, as submodules of Knowage Enterprise Edition, also supports **multi-tenancy** (i.e. a single Knowage instance serving multiple organizations, called tenants). In a multi-tenancy architecture, each tenant owns and manages his own users, documents, configuration and parameters, which are completely independent from those owned by other tenants.

## Módulos

.. figure:: media/image6.png

Módulos de conocimiento.

Servidor Knowage
El núcleo de la suite, que incluye todas las características analíticas. Este es el entorno de referencia para el usuario final y el administrador;
Knowage Meta
El entorno que soporta la creación y gestión de modelos de metadatos. Este módulo está concebido para desarrolladores de BI.
Estudio Knowage
El entorno que permite a los desarrolladores de BI configurar el análisis y las características analíticas relacionadas que luego se publican y se ponen a disposición del usuario final en el servidor.
Knowage SDK
Un conjunto de API compatibles con la arquitectura SOA, lo que permite que las aplicaciones externas interactúen con Knowage Server y sus metadatos.
Aplicaciones de Knowage
Un conjunto de modelos analíticos listos para usar en dominios de negocio específicos.

Aquí nos centramos en Knowage Server teniendo en cuenta la perspectiva del administrador.

Es el módulo principal de la suite, que proporciona, como veremos, todo el poder analítico del producto y todo lo administrativo
Funcionalidades.

Representa una solución de nivel empresarial para BI, soportando todo el ciclo de vida del proyecto, gestionando la seguridad y garantizando la escalabilidad, el clustering y las arquitecturas de alta disponibilidad. Además, es la principal referencia para todos los usuarios y usos potenciales; lidera la tendencia de desarrollo en términos de características, servicios y modelos de entrega.

## Capas

La arquitectura de Knowage Server está funcionalmente en capas en tres niveles principales.

.. figure:: media/image7.png

Estructura de la arquitectura de Knowage Server.

Capa de entrega
Gestiona todos los usos posibles del servidor por parte de los usuarios finales o de aplicaciones externas.
Capa analítica
Proporciona todas las funcionalidades analíticas del producto.
Capa de datos
Regula la carga de datos a través de muchas estrategias de acceso.

Cada capa de la arquitectura funcional se compone de diferentes módulos de aplicación.

.. figure:: media/image8.png

Detalle de la arquitectura de Knowage Server.

Capa de entrega

```

The delivery layer covers all publication requirements. It can be accessed by third-party applications, and it offers end users all features and services needed to perform their BI analysis.

It can be accessed in different ways:

BI Webapp
   It is the default use mode. Knowage suite provides a web application, working on a standard application server A customizable web application is provided, working on a standard application server (e.g. Tomcat, JBoss, WAS). The administrator can define the layout and specific views for each end user type.
BI Mobile
   Thanks to the interaction between Knowage Server and the remote client interface, users’ reports, charts or cockpits can also be accessed and displayed on mobile devices, such as tablets and smartphones.
BI Service
   Web services allowing Knowage components to interact with external applications or to collect the results of static documents (report, image of a chart, etc.).
BI Tag
   Tag libraries allowing you to encapsulate a dynamic document (OLAP, GEO, etc.) into a different context.
BI API
   For the integration of enterprise applications behind or without the end user GUI.

Analytical layer
```

La capa analítica es el núcleo del servidor. Proporciona todas las características y capacidades analíticas, en un acceso seguro y basado en roles.
modo. Sus principales componentes son:

Motores analíticos
cubriendo todos los requisitos analíticos, proporciona diferentes herramientas para cada tipo de análisis (por ejemplo, informes, gráficos, cabinas), con el fin de garantizar una alta flexibilidad y la satisfacción de los usuarios finales.
Motores operativos
interactuar con sistemas OLTP mediante ETL o procesos, y gestionar registros básicos de BI como datos maestros o dominios de búsqueda;
Modelo de comportamiento
que regula la visibilidad sobre documentos y datos, según los roles de los usuarios finales.

Al ofrecer múltiples soluciones para el mismo requerimiento analítico y/o múltiples instancias para el mismo motor, la lógica y arquitectura de Knowage proporcionan diversos beneficios, tales como: carga de trabajo limitada en cada motor, garantizando altos rendimientos; apertura para mejorar o ampliar la suite y sus capacidades, minimizando el impacto en los entornos salientes; alta flexibilidad y modularidad; alta escalabilidad, con un mínimo impacto económico, de infraestructura y a nivel de aplicación.

Capa de datos

```

The data layer allows data and metadata storage and usage. BI data is often located in a data warehouse, whose design is out of the BI product scope and strictly related to the specific customer’s world. Most of Knowage products offer a specific ETL tool allowing to load data at this level, covering the whole BI stack.

Knowage can directly access the data warehouse through JDBC connections (for instance, using SQL queries) or, on a higher level, it can use a specific access strategy based on metamodels, built through Knowage Meta.

As described in the next chapters, Knowage can also access less traditional data sources, like Big Data and NoSQL data sources.

All Knowage metadata are stored in a private repository hosted on a generic RDBMS and accessed by means of a generic description based on Hibernate technology. Knowage metadata contains technical information, business metadata and metamodels registry.

What you can do with Knowage
----------------------------

This section focuses on Knowage analytical and operational functionalities, administration tools and cross services.

It is important to point out that Knowage adopts an evolutionary approach, allowing you to use and adapt the different features provided
by the suite according to your specific needs, and adapt them over time. The Server reflects this strategy, guaranteeing security and
consistency, thanks to the independence of the behavioural model that regulates visibility over documents and data.

Moreover, Knowage has a distributed logic and handles more instances of a same engine. This allows the workload distribution on several servers, ensuring the linear system scalability.

Analytical and operational functionalities
```

Knowage server proporciona una amplia gama de funcionalidades analíticas,
cubierto por los diferentes productos de la suite.

En cuanto al nivel operativo, Knowage Server trabaja con:

*   **ETL**, no solo para la carga continua de datos de origen en el DWH, sino incluso para el movimiento interno de datos, consolidaciones de alto nivel o devolución de la información producida a los sistemas operativos.
*   **Procesos externos**, para una interacción bidireccional con sistemas operativos y externos.
*   **Datos maestros**, para administrar manualmente los datos del dominio.

Herramientas administrativas y servicios cruzados

```

Besides its analytical, delivery and data access capabilities, Knowage Server provides all the administration tool needed to handle your
Knowage instance, as well as several cross-product services to make its features even more powerful.

The **administrative tools** support developers, testers and administrators in their daily work, providing various functionalities, such as: scheduler, profiling system, import/export capabilities, menu designer, map catalogue, management of repository, analytical model, behavioural model and engines, configuration of data sources and data sets, audit & monitoring analysis, subscriptions, management of value domains, configuration settings and metadata, management of user data, hierarchies editor and community management.

The **cross services** include the common features of the product, shared by all analytical engines and documents. They are: single sign on, alert and notification, workflow, search engine, collaborative tools, sending e-mails, ranking, multiformat exporter, RT events, document browser, personal folders, cross navigation, subscription service, hot link, metadata view.
```
