# Expanding Capacity for an In-use EVS Disk<a name="evs_01_0007"></a>

## Scenarios<a name="section4199781203421"></a>

This topic describes how to expand the capacity of an In-use EVS disk on the management console. The In-use status indicates that the disk has been attached to a server. You do not need to detach the disk when expanding an In-use disk. 

## Constraints<a name="section158147122515"></a>

-   Currently, disk capacities can only be expanded, but cannot be reduced.
-   When expanding an In-use disk, the server containing this disk must be in the  **Running**  or  **Stopped**  state.
-   A shared disk cannot be expanded in the  **In-use**  state. To expand a shared In-use disk, you must detach it from all its servers, wait until its status changes to  **Available**, and then expand its capacity. For more information, see  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).
-   Only some server OSs support capacity expansion of In-use disks. For details, see the official document of the corresponding OS.

    If the server OS does not support capacity expansion of In-use disks, detach the disk and then expand its capacity. Otherwise, you may need to stop and then start the server after the expansion to make the expansion takes effect.


## Procedure<a name="section5287890203514"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  Determine whether to view the server information before expanding the disk.
    -   If you need to view the server information, perform the following procedure:
        1.  In the disk list, click the name of the to-be-expanded disk.

            The disk details page is displayed.

        2.  Click the  **Attachments**  tab to view the server where the target disk has been attached.
        3.  Click  **Expand Capacity**  in the upper right corner of the page.

            The expansion page is displayed.

    -   If you do not need to view the server information, perform the following procedure:
        1.  In the disk list, locate the row that contains the target disk and click  **Expand Capacity**  in the  **Operation**  column.

            The expansion page is displayed.


5.  Set the  **Add Capacity \(GB\)**  parameter and click  **Next**.
6.  On the  **Details**  page, check the disk information again.

    -   If you do not need to modify the specifications, click  **Submit**  to start the expansion.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.

    After the specifications are submitted, the disk list page is displayed.

7.  In the disk list, view the capacity of the target disk.

    When the disk status changes from  **Expanding**  to  **In-use**  and the disk capacity increases, the expansion has succeeded.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the expansion fails, customer service personnel will contact you and help you handle this error. Do not perform any operations on the disk before the customer service personnel contact you. If you require that the error be handled as soon as possible, contact our customer service personnel. The disk will no longer be charged once its status changes to  **Expansion failed**.  

8.  After a disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly. You must log in to the server and extend the disk partition and file system.

    The operation method varies depending on the server OS.

    -   In Windows, see  [Extending Disk Partitions and File Systems \(Windows\)](extending-disk-partitions-and-file-systems-(windows).md).
    -   In Linux, see  [Partition and File System Extension Preparations \(Linux\)](partition-and-file-system-extension-preparations-(linux).md).


