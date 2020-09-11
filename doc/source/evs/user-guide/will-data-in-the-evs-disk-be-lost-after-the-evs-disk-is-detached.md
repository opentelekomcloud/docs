# Will Data in the EVS Disk Be Lost After the EVS Disk Is Detached?<a name="evs_faq_0012"></a>

Before you detach an EVS disk encrypted by a CMK, check whether the CMK is disabled or scheduled for deletion. If the CMK is unavailable, the disk can still be used, but normal read/write operations are not guaranteed permanently. If the disk is detached and then re-attached, re-attaching this disk will fail. In this case, do not detach the disk and restore the CMK status first.

The restoration method varies depending on the current CMK status. For details, see  [EVS Disk Encryption](evs-disk-encryption.md).

If the CMK used to encrypt the disk is available or the disk is a non-encrypted disk, the disk can be detached and re-attached, and data on the disk will not be lost.

To prevent data loss when you detach an EVS disk, perform the following operations:

-   For EVS disks not supporting online detachment:
    1.  Stop the server where the target EVS disk has been attached.
    2.  After the server has been stopped, detach the EVS disk.

-   For EVS disks supporting online detachment:

    Detach the EVS disk from a running ECS. For details, see  **Management**  \>  **Detaching an EVS Disk from a Running ECS**  in the  _Elastic Cloud Server User Guide_.


