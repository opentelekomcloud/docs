# File System Encryption<a name="sfs_01_0006"></a>

SFS provides you with the encryption function. You can encrypt your data on the newly created file systems if needed.

Keys for encrypting file systems are provided by Key Management Service \(KMS\), which is secure and convenient. You do not need to establish and maintain key management infrastructure. If you want to use your own key material, you can use the key import function on KMS Console to create a customer master key \(CMK\) whose key material is empty, and import the key material to the CMK. For details, see "Importing a Key" in the  _Key Management Service User Guide_.

## Encryption Key<a name="section17331463223115"></a>

The keys provided by KMS include a default master key and CMKs.

-   Default master key: SFS automatically creates a default master key and names it  **sfs/default**.

    The default master key cannot be disabled and does not support scheduled deletion.

-   CMKs: Existing or newly created CMKs. For details, see "Creating a CMK" in the  _Key Management Service User Guide_.

    If the CMK used by the encrypted file system is disabled or planned to be deleted, the file system can only be used within a certain period of time \(30s by default\). Exercise caution in this case.


## Who Has the Rights to Encrypt File Systems?<a name="section4401454411508"></a>

-   The security administrator who has the "Security Administrator" permission can grant the KMS access rights for encryption.
-   A common user who does not have the "Security Administrator" permission needs to contact the system administrator to obtain the "Security Administrator" permission.

As long as the KMS access rights have been granted to SFS, all common users in the same region can directly use the encryption function.

If there are multiple projects in the current region, the KMS access rights need to be granted to each project in this region.

