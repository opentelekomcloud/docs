# What Are the Restrictions on Attaching an EVS Disk to an ECS?<a name="EN-US_TOPIC_0040863659"></a>

-   The EVS disk and the target ECS must be located in the same AZ.
-   For a non-shared disk, the EVS disk must be in  **Available**  state.

    For a shared disk, the target EVS disk must be in  **In-use**  or  **Available**  state.

-   The target ECS must be in  **Running**  or  **Stopped**  state.
-   A SCSI EVS disk cannot be used as an ECS system disk.
-   Certain ECSs support SCSI EVS disk attachment. For details, see  [Which ECSs Can Be Attached with SCSI EVS Disks?](which-ecss-can-be-attached-with-scsi-evs-disks.md)

