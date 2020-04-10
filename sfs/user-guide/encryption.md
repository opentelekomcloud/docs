# Encryption<a name="sfs_01_0042"></a>

## Creating an Encrypted File System<a name="section909365011371"></a>

Before you use the encryption function, the KMS access rights must be granted to SFS. If you have the Security Administrator rights, grant SFS the permissions to access KMS directly. Otherwise, you need to contact the system administrator to obtain the "Security Administrator" rights first. For details, see  [File System Encryption](file-system-encryption.md).

You can create a file system that is encrypted or not, but you cannot change the encryption settings of an existing file system.

For details about how to create an encrypted file system, see  [Step 1: Create a File System](step-1-create-a-file-system.md).

## Unmounting an Encrypted File System<a name="section54711302212445"></a>

If the CMK used by the encrypted file system is disabled or planned to be deleted, the file system can only be used within a certain period of time \(30s by default\). Exercise caution in this case.

For details about how to unmount the file system, see  [Unmounting a File System](step-3-unmount-a-file-system.md).

