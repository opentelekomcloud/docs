# Managing an Encrypted EVS Disk<a name="evs_01_0009"></a>

## Relationships Among Encrypted Disks, Backups and Snapshots<a name="section3026922421034"></a>

The encryption function can be used to encrypt system disks, data disks, backups and snapshots. The details are as follows:

-   System disk encryption relates to the image that is used to create the server.
    -   If an encrypted image is used to create the server, the encryption function is enabled for the system disk by default, and the system disk and image share the same encryption method. For details, see  **Managing Private Images**  \>  **Encrypting Images**  in the  _Image Management Service User Guide_.

-   When creating an empty disk, you can determine whether to encrypt the disk or not. The disk encryption attribute cannot be changed after the disk has been created.
-   If a disk is created from a snapshot, the encryption attribute of the disk will be the same as that of the snapshot's source disk.
-   If a disk is created from a backup, the encryption attribute of the disk will be the same as that of the backup's source disk.
-   If a snapshot is created for a disk, the encryption attribute of the snapshot is the same as that of the disk.

## Creating an Encrypted EVS Disk<a name="section909365011371"></a>

Before you use the disk encryption function, KMS access rights need to be granted to EVS. If you have the Security Administrator rights, grant the KMS access rights to EVS directly. If you do not have this permission, contact a user with the security administrator rights to grant KMS access rights to EVS, then repeat the preceding operations.

For details about how to create an encrypted disk, see  [Create an EVS Disk](create-an-evs-disk.md).

## Detaching an Encrypted EVS Disk<a name="section54711302212445"></a>

Before you detach an EVS disk encrypted by a CMK, check whether the CMK is disabled or scheduled for deletion. If the CMK is unavailable, the disk can still be used, but normal read/write operations are not guaranteed permanently. If the disk is detached and then re-attached, re-attaching this disk will fail. In this case, do not detach the disk and restore the CMK status first.

The restoration method varies depending on the current CMK status. For details, see  [EVS Disk Encryption](evs-disk-encryption.md).

If the CMK is available, the disk can be detached and re-attached, and data on the disk will not be lost.

For details about how to detach an encrypted disk, see  [Detaching a Data Disk](detaching-a-data-disk.md).

