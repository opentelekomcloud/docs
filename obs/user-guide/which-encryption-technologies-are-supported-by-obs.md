# Which Encryption Technologies Are Supported by OBS?<a name="obs_faq_0044"></a>

Before uploading your data to OBS, you can encrypt the data to ensure security during transmission and storage. OBS support various encryption technologies used on clients.

OBS allows users to encrypt objects using server-side encryption so that the objects can be securely stored on OBS.

The objects to be uploaded can be encrypted using SSE-KMS. You need to create a key using KMS or use the default key provided by KMS. Then you can use the KMS key to perform server-side encryption when uploading objects on OBS.

After server-side encryption is enabled, objects to be uploaded will be encrypted and stored on the server. When downloading the encrypted objects, the encrypted data will be decrypted on the server and displayed in plaintext to users.

OBS supports both SSE-KMS and server-side encryption with customer-provided keys \(SSE-C\) by invoking APIs. In SSE-C mode, OBS uses the keys and MD5 values provided by customers for server-side encryption.

