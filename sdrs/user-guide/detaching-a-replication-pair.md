# Detaching a Replication Pair<a name="sdrs_ug_pi_0005"></a>

## Scenarios<a name="section11716195481510"></a>

You can perform steps provided in this section to detach a replication pair from a protected instance. Then, data of the servers in the protected instance will not be written in to the disks in the replication pair.

## **Prerequisites**<a name="section189551041174318"></a>

-   The protection group is in the  **Available**,  **Protecting**,  **Failover complete**,  **Enabling protection failed**,  **Disabling protection failed**,  **Planned failover failed**, or  **Failover failed**  state.
-   The protected instance is in the  **Available**,  **Protecting**,  **Failover complete**,  **Enabling protection failed**,  **Disabling protection failed**,  **Planned failover failed**,  **Failover failed**,  **Deletion failed**,  **Re-enabling protection failed**,  **Modifying specifications failed**,  **Invalid**, or  **Faulty**  state.
-   The replication pair is in the  **Available**,  **Protecting**,  **Failover complete**,  **Attaching failed**,  **Detaching failed**,  **Enabling protection failed**,  **Disabling protection failed**,  **Planned failover failed**,  **Failover failed**,  **Deletion failed**,  **Re-enabling protection failed**,  **Expansion failed**,  **Invalid**, or  **Faulty**  state.
-   The replication pair has been attached to a protected instance.
-   Disks in the  **In-use**  state have been attached to the production and DR site servers.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A system disk \(mounted on the  **/dev/sda**  or  **/dev/vda**  mount point\) can be detached from a server only when the server is in the  **Stopped**  state. Therefore, stop the server before detaching the system disk.  
>-   A data disk can be detached from a server online or offline, specifically, when the server is in the  **Stopped**  or  **Running**  state.   
>    For details about how to detach a disk online, see  **Storage**  \>  **Detaching an EVS Disk from a Running ECS**  in the  _Elastic Cloud Server User Guide_.  

## Procedure<a name="section12665542174816"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which the replication pair is to be detached from the protected instance, click  **Protected Instances**.

    The operation page for the protection group is displayed.

4.  On the  **Protected Instances**  tab, locate the row containing the desired protected instance and click  **Detach**  in the  **Operation**  column.

    The  **Detach Replication Pair**  page is displayed.

    **Figure  1**  Detaching a replication pair<a name="fig0379114115717"></a>  
    ![](figures/detaching-a-replication-pair.png "detaching-a-replication-pair")

5.  Select the replication pair to be detached and click  **Yes**.

    Then, data of the servers in the protected instance will not be written in to the disks in the replication pair. 


