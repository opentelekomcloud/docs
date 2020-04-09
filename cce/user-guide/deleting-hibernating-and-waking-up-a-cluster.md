# Deleting, Hibernating, and Waking Up a Cluster<a name="cce_01_0031"></a>

After a cluster is created, you can delete, hibernate, or wake up the cluster.

## Deleting a Cluster<a name="section186941617125315"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Exercise caution when deleting a cluster because this operation will destroy the nodes in the cluster and running services.  

This section takes VM clusters as an example. The procedure for BMS clusters is the same.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**.
2.  Choose  **More \> Delete**.
3.  The  **Delete Cluster**  dialog box then appears.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Deleting the cluster will delete all nodes in the cluster and the running workloads and services.  
    >-   The delete operation takes 1 to 3 minutes to complete.  
    >-   Enter  **DELETE**  into the text box below to confirm that the delete operation will continue.  
    >-   If a cluster whose status is Unavailable is deleted, some storage resources of the cluster may need to be manually deleted.  

4.  Click  **OK**  to start deleting the cluster.

## Hibernating a Cluster<a name="section080654155210"></a>

If you do not need to use a cluster temporarily, you are advised to hibernate the cluster to save cluster management costs.

After a cluster is hibernated, resources such as workloads cannot be created or managed in the cluster.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**.
2.  Choose  **More**  \>  **Hibernate**  for the target cluster.
3.  In the  **Hibernate**  dialog box, read the precautions and select  **Stop all the nodes in the cluster**, and click  **OK**.

    Wait until the cluster hibernation is complete.

    **Figure  1**  Hibernating a Cluster<a name="fig27367109201"></a>  
    ![](figures/hibernating-a-cluster.png "hibernating-a-cluster")


## Waking Up a Cluster<a name="section35851974575"></a>

A hibernated cluster can be quickly woken up and used normally.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**.
2.  Choose  **More**  \>  **Wake**.
3.  In the displayed dialog box, click  **OK**.

    Wait until the cluster is woken up.

    **Figure  2**  Waking up a cluster<a name="fig15105161315251"></a>  
    ![](figures/waking-up-a-cluster.png "waking-up-a-cluster")


