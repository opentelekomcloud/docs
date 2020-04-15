# Rolling Back Data from a Snapshot<a name="evs_01_0012"></a>

## Scenarios<a name="section1820473161254"></a>

If the data on an EVS disk is incorrect or damaged, you can roll back the data from a snapshot to the source disk to restore data. Snapshot rollback has the following constraints:

-   A snapshot can be rolled back only to its source EVS disk. A rollback to another disk is not possible.
-   A snapshot can be rolled back only when the snapshot status is  **Available**  and the source disk status is  **Available**  \(not attached to any server\) or  **Rollback failed**.

## Procedure<a name="section23223906174233"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.
4.  In the navigation tree on the left, choose  **Elastic Volume Service**  \>  **Snapshots**.

    The  **Snapshots**  page is displayed.

5.  In the snapshot list, locate the row that contains the target snapshot and click  **Roll Back Disk**  in the  **Operation**  column.
6.  In the displayed dialog box, click  **Yes**.
7.  The snapshot list is displayed. After the snapshot status changes from  **Rolling back**  to  **Available**, the data rollback is successful.

