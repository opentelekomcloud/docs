# CORS Overview<a name="en-us_topic_0045853680"></a>

CORS is a browser-standard mechanism provided by the World Wide Web Consortium \(W3C\). It defines the interaction methods between client-side web applications in one origin and resources in another origin. For general web page requests, website scripts and contents in one origin cannot interact with those in another origin because of Same Origin Policies \(SOPs\).

The CORS specification is supported to allow cross-origin requests to access OBS resources.

OBS supports static website hosting. Static websites stored in OBS can respond to website requests from another origin only when CORS is configured for the bucket.

Typical application scenarios of CORS are as follows:

-   Enables JavaScript and HTML5 to be used for establishing web applications that can directly access resources in OBS. No proxy servers are required for transfer.
-   Enables the dragging function of HTML5 to be used to upload files to OBS \(with the upload progress displayed\) or update OBS contents using web applications.
-   Hosts external web pages, style sheets, and HTML5 applications in different origins. Web fonts or pictures in OBS can be shared by multiple websites.

The configuration of CORS takes effect within two minutes.

