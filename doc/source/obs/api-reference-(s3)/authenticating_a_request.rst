=========================
Authenticating a Request
=========================


For authentication purposes you are issued an access key ID \(AK\) and a secret access key \(SK\) upon registration in OBS. A request sent to OBS can be authenticated using its  **Authorization**  header that contains a signature generated using the SK and request parameters. Before authentication, the names of buckets and objects are URL encoded and then authentication information begins to generate.

OBS supports two authentication modes: V2 authentication and V4 authentication. In OBS however, the recommended authentication mode is V4 as V2 authentication is more susceptible to security breaches. There are three differences between V2 and V4 authentication modes:

-   V4 authentication uses the HMAC-SHA256 algorithm to enhance security.
-   V4 authentication enables user data to incorporate into signature calculation.
-   Users can specify the header that is used for signature calculation in V4 authentication.


.. image:: /images/icon-notice.gif

**NOTICE:**
V4 authentication is recommended because V2 authentication is more susceptible to security breaches.


.. toctree::
   :maxdepth: 1

   ak-and-sk-generation.md
   v2-common-request.md
   v2-temporarily-authorized-request.md
   v4-common-request.md
   v4-temporarily-authorized-request.md
   v4-browser-based-authorized-post-request.md


