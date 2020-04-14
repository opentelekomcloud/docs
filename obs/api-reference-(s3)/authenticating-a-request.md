# Authenticating a Request<a name="EN-US_TOPIC_0125560435"></a>

For authentication purposes you are issued an access key ID \(AK\) and a secret access key \(SK\) upon registration in OBS. A request sent to OBS can be authenticated using its  **Authorization**  header that contains a signature generated using the SK and request parameters. Before authentication, the names of buckets and objects are URL encoded and then authentication information begins to generate.

OBS supports two authentication modes: V2 authentication and V4 authentication. In OBS however, the recommended authentication mode is V4 as V2 authentication is more susceptible to security breaches. There are three differences between V2 and V4 authentication modes:

-   V4 authentication uses the HMAC-SHA256 algorithm to enhance security.
-   V4 authentication enables user data to incorporate into signature calculation.
-   Users can specify the header that is used for signature calculation in V4 authentication.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>V4 authentication is recommended because V2 authentication is more susceptible to security breaches.  

-   **[AK and SK Generation](ak-and-sk-generation.md)**  

-   **[V2 Common Request](v2-common-request.md)**  

-   **[V2 Temporarily Authorized Request](v2-temporarily-authorized-request.md)**  

-   **[V4 Common Request](v4-common-request.md)**  

-   **[V4 Temporarily Authorized Request](v4-temporarily-authorized-request.md)**  

-   **[V4 Browser-based Authorized POST Request](v4-browser-based-authorized-post-request.md)**  


