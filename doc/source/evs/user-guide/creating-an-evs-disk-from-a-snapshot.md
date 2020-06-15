# Creating an EVS Disk from a Snapshot<a name="evs_01_0013"></a>

## Scenarios<a name="section63311840155158"></a>

This topic describes how to create an EVS disk on the  **Snapshots**  page. Besides, you can also create an EVS disk from a snapshot by specifying the  **Create from snapshot**  parameter on the disk creation page. For details, see  [Create an EVS Disk](create-an-evs-disk.md).

When a disk is created from a snapshot, the new disk has the following constraints:

-   The disk type of the new disk is the same as that of the snapshot's source disk.
-   The device type of the new disk is the same as that of the snapshot's source disk.
-   The encryption attribute of the new disk is the same as that of the snapshot's source disk.
-   A maximum of 128 disks can be created from this snapshot.
-   Batch disk creation is not possible, and the quantity parameter must be set to  **1**.

## Procedure<a name="section53290500174512"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.
4.  In the navigation tree on the left, choose  **Elastic Volume Service**  \>  **Snapshots**.

    The snapshot list page is displayed.

5.  In the snapshot list, locate the row that contains the target snapshot and click  **Create Disk**  in the  **Operation**  column.
6.  Set the EVS disk parameters. For details, see parameter descriptions and operations provided in  [Create an EVS Disk](create-an-evs-disk.md).

    >![](/images/icon-note.gif) **NOTE:**   
    >A maximum of 128 disks can be created from a snapshot.  
    >If you create a disk from a snapshot, the disk capacity must be greater than or equal to the snapshot size. In the condition that you do not specify the disk capacity, if the snapshot size is smaller than 10 GB, the default capacity 10 GB will be used as the disk capacity; if the snapshot size is greater than 10 GB, the disk capacity will be consistent with the snapshot size.  

7.  Click  **Create Now**.
8.  On the  **Details**  page, check the disk details.
    -   If you do not need to modify the specifications, click  **Submit**  to start the creation.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.

9.  In the disk list, view the disk status.

    When the disk status changes to  **Available**, the disk is successfully created.


