# Expanding Replication Pair Capacity<a name="sdrs_ug_rp_0002"></a>

## Scenarios<a name="section901066538"></a>

If the replication pair capacity of your protection groups cannot meet your service requirements, you can perform steps provided in this section to expand the capacity of the specified replication pair. Replication pairs do not support capacity reduction or rollback after a successful capacity expansion. 

After you expand the capacity of a replication pair, the capacity of both the production and DR site disks are changed.

## **Prerequisites**<a name="section16316613536"></a>

-   The replication pair for which the capacity is to be expanded is in the  **Available**,  **Protecting**, or  **Expansion failed**  state.
-   The disks in the replication pair are in the  **Available**  or  **In-use**  state.
-   If the billing mode of the disks in the replication pair is yearly/monthly, capacity expansion is not supported. If you want to increase the capacity of disks in the replication pair, delete the replication pair, expand the capacity of the production site disk, and then use the disk to create a replication pair.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   When the disks in a replication pair are not shared  
>    If the disks in the replication pair are in the  **In-use**  state, the replication pair capacity can be expanded only when online capacity expansion is supported. If online capacity expansion is not supported,  **Expand Capacity**  in the  **Operation**  column is unavailable.  
>-   When the disks in a replication pair are shared  
>    The replication pair capacity cannot be expanded online if the disks are in the  **In-use**  state.  

## Procedure<a name="section8106123715525"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which the capacity of the replication pair is to be expanded, click  **Replication Pairs**.

    The operation page for the protection group is displayed.

4.  On the  **Replication Pairs**  tab, locate the row containing the replication pair for which the capacity is to be expanded and click  **Expand Capacity**  in the  **Operation**  column.

    The  **Expand Capacity**  page is displayed.

5.  On the  **Expand Capacity**  page, confirm the replication pair information, configure  **Add Capacity**, and click  **Next**. 
6.  If you do not need to modify the information, click  **Submit**.

    If you want to modify the information, click  **Previous**  and modify the information as required.


