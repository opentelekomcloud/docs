# Managing a Shared EVS Disk<a name="evs_01_0010"></a>

## How to Use Shared VBD and SCSI Disks?<a name="section22769430202827"></a>

You can create shared VBD disks or shared SCSI disks. It is recommended that you attach the shared disk to the ECSs in the same ECS group to improve service reliability.

-   Shared VBD EVS disks: The device type of a newly created shared EVS disk is VBD by default. Such disks can be used as virtual block storage devices, but do not support SCSI reservations. If SCSI reservations are required for your applications, create shared SCSI EVS disks.
-   Shared SCSI EVS disks: These EVS disks support SCSI reservations.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >-   To improve data security, you are advised to use SCSI reservations together with the anti-affinity policy of an ECS group. That said, ensure that shared SCSI EVS disks are only attached to ECSs in the same anti-affinity ECS group.  
    >-   If an ECS does not belong to any anti-affinity ECS group, you are advised not to attach shared SCSI EVS disks to this ECS. Otherwise, SCSI reservations may not work properly, which may put your data at risk.  

    Concepts of the anti-affinity ECS group and SCSI reservations:

    -   The anti-affinity policy of an ECS group allows ECSs to be created on different physical servers to improve service reliability.

        For details about ECS groups, see  **Managing ECS Groups**  in the  _Elastic Cloud Server User Guide_.

    -   The SCSI reservation mechanism uses a SCSI reservation command to perform SCSI reservation operations. If an ECS sends such a command to an EVS disk, the disk is displayed as locked to other ECSs, preventing the data damage that may be caused by simultaneous read/write operations to the disk from multiple ECSs.
    -   ECS groups and SCSI reservations have the following relationship: A SCSI reservation on a single EVS disk cannot differentiate multiple ECSs on the same physical host. For that reason, if multiple ECSs that use the same shared EVS disk are running on the same physical host, SCSI reservations will not work properly. Therefore, you are advised to use SCSI reservations only on ECSs that are in the same ECS group, thus having a working anti-affinity policy. 


## Attaching a Shared EVS Disk<a name="section1613814920286"></a>

A common EVS disk can only be attached to one server, whereas a shared EVS disk can be attached to up to 16 servers.

For details about how to attach a shared EVS disk, see  [Attaching a Shared Disk](attaching-a-shared-disk.md).

## Detaching a Shared EVS Disk<a name="section30398521204021"></a>

Because a shared EVS disk can be attached to multiple servers, ensure that the shared EVS disk is detached from all the servers before deletion.

For details about how to detach a shared EVS disk, see  [Deleting an EVS Disk](deleting-an-evs-disk.md).

## Expanding a Shared EVS Disk<a name="section34685374205131"></a>

Shared EVS disks must be expanded when they are in the  **Available**  state. For details, see  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).

## Related Operations<a name="section1613519219248"></a>

For more disk sharing FAQs, see  [Shared Disk FAQs](shared-disk-faqs.md).

