# Performing Reprotection<a name="sdrs_ug_pg_0006"></a>

## Scenarios<a name="section10115010427"></a>

Once the failover is started, data synchronization stops. After the failover is complete, the protection group is in the  **Protection disabled**  state. To restart data synchronization, perform steps provided in this section.

## **Prerequisites**<a name="section1037911514214"></a>

-   The protection group has replication pairs.
-   The protection group is in the  **Failover complete**  or  **Re-enabling protection failed**.
-   The DR site server is stopped.

## Procedure<a name="section57791291427"></a>

1.  Log in to the management console. 
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the desired protection group, click  **Protected Instances**.
4.  In the upper right corner of the page, click  **More**  and choose  **Reprotect**  from the drop-down list. 

    The  **Reprotect**  dialog box is displayed.

5.  Check whether all the DR site servers in this protection group are stopped.
    -   If yes, go to step  [6](#li812255515532).
    -   If no, select the servers to be stopped and click  **Stop**.

6.  <a name="li812255515532"></a>On the  **Reprotect**  dialog box, click  **Reprotect**.

    During the reprotection, do not start the DR site servers in the protection group. Otherwise, the reprotection may fail.


