# How to Use KMS<a name="kms_01_0015"></a>

## Working with OBS<a name="section33868196204127"></a>

Users can upload objects to and download them from Object Storage Service \(OBS\) in common mode or server-side encryption mode. When users upload objects in encryption mode, data is encrypted at the server side and then securely stored on OBS in ciphertext. When users download encrypted objects, the data in ciphertext is decrypted at the server side and then provided to users in plaintext. OBS supports the server-side encryption with KMS-managed keys \(SSE-KMS\) mode. In SSE-KMS mode, OBS uses the keys provided by KMS for server-side encryption.

For details about how to upload objects to OBS in SSE-KMS mode, see the  _Object Storage Service User Guide_.

## Working with EVS<a name="section64832916164527"></a>

If you enable the encryption function when creating an EVS disk and select a CMK provided by KMS to encrypt the EVS disk, data stored to the EVS disk is automatically encrypted.

For details about how to use the encryption function of EVS, see the  _Elastic Volume Service User Guide_.

## Working with IMS<a name="section3172002185912"></a>

When creating a private image using an external image file, you can enable the private image encryption function and select a CMK provided by KMS to encrypt the image.

For details about how to use the private image encryption function of Image Management Service \(IMS\), see the  _Image Management Service User Guide_.

## Working with SFS<a name="section17569161438"></a>

When creating a file system on SFS, the CMK provided by KMS can be selected to encrypt the file system, so that files stored in the file system are automatically encrypted.

For details about how to use the encryption function of SFS, see the  _Scalable File Service User Guide_.

## Working with RDS<a name="section56015594323"></a>

When creating a database instance, you can enable the disk encryption function of the database instance and select a CMK created on KMS to encrypt the disk of the database instance. The enablement of disk encryption will enhance data security.

For details about how to use the disk encryption function of RDS, see the  _Relational Database Service User Guide_.

## Working with User Applications<a name="section5597053693750"></a>

To encrypt plaintext data, a user application can call the necessary KMS APIs to generate a DEK. The DEK can then be used to encrypt the plaintext data. Then the application can store the encrypted data. In addition, the user application can call the necessary KMS APIs to create CMKs. DEKs can be stored in ciphertext after being encrypted with the CMKs. For details, see the  _Key Management Service API Reference_.

