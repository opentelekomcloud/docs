# Server-Side Encryption<a name="EN-US_TOPIC_0125560343"></a>

Users can upload and download objects in common mode or using server-side encryption.

Object Storage Service \(OBS\) supports server-side encryption.

Users can implement this function based on various the key management types to meet site requirements. OBS supports two server-side encryption modes:

-   Server-side encryption with KMS-managed keys \(SSE-KMS\).
-   Server-side encryption with customer-provided keys \(SSE-C\).

In SSE-KMS mode, OBS uses the keys provided by Key Management Service \(KMS\) for server-side encryption.

In SSE-C mode, OBS uses the keys and MD5 values provided by customers for server-side encryption.

When server-side encryption is used, the returned ETag value is not the MD5 value of the object. When server-side encryption is used to upload an object, the server does not verify the imported Content-MD5 value.

-   **[SSE-KMS](sse-kms.md)**  

-   **[SSE-C](sse-c.md)**  

-   **[Interfaces Related to Server-Side Encryption](interfaces-related-to-server-side-encryption.md)**  


