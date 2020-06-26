# Server-Side Encryption Overview<a name="obs_03_0420"></a>

After server-side encryption is enabled, objects to be uploaded will be encrypted and stored on the server. When downloading the encrypted objects, the encrypted data will be decrypted on the server and displayed in plaintext to users.

Key Management Service \(KMS\) uses Hardware Secure Modules \(HSMs\) to ensure key security, enabling users to easily create and manage encryption keys. Keys are not displayed in plaintext outside HSMs, which prevents key disclosure. All operations performed on keys are controlled and logged, and usage of all keys is recorded, meeting regulatory compliance requirements.

OBS Browser supports server-side encryption with KMS-managed keys \(SSE-KMS\). In the SSE-KMS mode, OBS uses the keys provided by KMS for server-side encryption.

With OBS Browser, you can make API calls to use keys provided by KMS for server-side encryption.

