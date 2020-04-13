# Application Scenarios<a name="EN-US_TOPIC_0237964738"></a>

For e-commerce, video sharing, gaming, and other data-intensive applications, it is essential to retrieve data fast. The primary purpose of DCS is to provide fast yet inexpensive data retrieval. With DCS, you can retrieve data from in-memory data stores instead of relying entirely on slower disk-based databases.

DCS instances are also fully managed. You no longer need to perform management tasks such as hardware provisioning, software patching, monitoring, or failure recovery. Consider using DCS when you need to cache the following types of data:

-   Web pages

    Caching the content of web pages improves page load times. The cached content can include static data such as Hypertext Markup Language \(HTML\) pages, Cascading Style Sheets \(CSS\), and images.

-   Status

    DCS provides quick and simple queries of session status and application-scaling status, enabling easy sharing of status information.

-   Application objects

    DCS serves as a level-2 cache at the service layer and provides data storage and access for external entities. Storing frequently requested data in DCS instances can off load databases and reduce access latency.

-   Events

    DCS provides continuous event querying, allowing streams of events to be processed as they occur.


