# Expanding Capacity for an Available EVS Disk<a name="evs_01_0008"></a>

## Scenarios<a name="section12031252191210"></a>

This topic describes how to expand the capacity of an Available EVS disk on the management console. The Available status indicates that the disk has not been attached to any server. 

## Constraints<a name="section2096213105282"></a>

-   Currently, disk capacities can only be expanded, but cannot be reduced.
-   A shared disk cannot be expanded in the  **In-use**  state. To expand a shared In-use disk, you must detach it from all its servers, wait until its status changes to  **Available**, and then expand its capacity.

## Procedure<a name="section12383539191210"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  \(Optional\) If the target disk has been attached to a server, detach it first. For details, see  [Detaching a System Disk](detaching-a-system-disk.md)  or  [Detaching a Data Disk](detaching-a-data-disk.md).

    When the disk status changes to  **Available**, the disk is successfully detached.

5.  In the disk list, locate the row that contains the target disk and click  **Expand Capacity**  in the  **Operation**  column.

    The expansion page is displayed.

6.  Set the  **Add Capacity \(GB\)**  parameter and click  **Next**.
7.  On the  **Details**  page, check the disk information again.

    -   If you do not need to modify the specifications, click  **Submit**  to start the expansion.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.

    After the specifications are submitted, the disk list page is displayed.

8.  In the disk list, view the capacity of the target disk.

    When the disk status changes from  **Expanding**  to  **Available**  and the disk capacity increases, the expansion has succeeded.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the expansion fails, customer service personnel will contact you and help you handle this error. Do not perform any operations on the disk before the customer service personnel contact you. If you require that the error be handled as soon as possible, contact our customer service personnel. The disk will no longer be charged once its status changes to  **Expansion failed**.  

9.  Attach the disk to the server. For details, see  [Attach an EVS Disk](attach-an-evs-disk.md).
10. After a disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly. You must log in to the server and extend the disk partition and file system.

    The operation method varies depending on the server OS.

    -   In Windows, see  [Extending Disk Partitions and File Systems \(Windows\)](extending-disk-partitions-and-file-systems-(windows).md).
    -   In Linux, see  [Partition and File System Extension Preparations \(Linux\)](partition-and-file-system-extension-preparations-(linux).md).


