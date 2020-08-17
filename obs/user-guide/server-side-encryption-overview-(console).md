# Server-Side Encryption Overview<a name="en-us_topic_0066036553"></a>

After server-side encryption is enabled, objects to be uploaded will be encrypted and stored on the server. When downloading the encrypted objects, the encrypted data will be decrypted on the server and displayed in plaintext to users.

Key Management Service \(KMS\) uses Hardware Secure Modules \(HSMs\) to ensure key security, enabling users to easily create and manage encryption keys. Keys are not displayed in plaintext outside HSMs, which prevents key disclosure. All operations performed on keys are controlled and logged, and usage of all keys is recorded, meeting regulatory compliance requirements.

The objects to be uploaded can be encrypted from the server side using the encryption service provided by KMS. You need to create a key using KMS or use the default key provided by KMS. Then you can use the key to perform server-side encryption when uploading objects to OBS.

OBS supports both SSE-KMS and server-side encryption with customer-provided keys \(SSE-C\) by calling APIs. In SSE-C mode, OBS encrypts objects on the server side using the keys and MD5 values provided by customers.

