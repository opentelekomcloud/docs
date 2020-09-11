# Deleting a Snapshot<a name="evs_01_0011"></a>

## Scenarios<a name="section9704285173937"></a>

If a snapshot is no longer used, you can release the virtual resources by deleting the snapshot from the system. Snapshot deletion has the following constraints:

-   A snapshot can be deleted only when its status is  **Available**  or  **Error**.
-   If a disk is deleted, all the snapshots created for this disk will also be deleted.

## Procedure<a name="section63311840155158"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.
4.  In the navigation tree on the left, choose  **Elastic Volume Service**  \>  **Snapshots**.

    The  **Snapshots**  page is displayed.

5.  In the snapshot list, locate the row that contains the target snapshot and click  **Delete**  in the  **Operation**  column.
6.  \(Optional\) If multiple snapshots are to be deleted, select  ![](figures/icon-select.png)  in front of each snapshot and click  **Delete**  in the upper area of the list.
7.  In the displayed dialog box, confirm the information and click  **Yes**.

