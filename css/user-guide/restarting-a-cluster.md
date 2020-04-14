# Restarting a Cluster<a name="css_01_0014"></a>

If a cluster stops working, you can restart it to restore normal running. Only clusters in the  **Available**  or  **Abnormal**  status can be restarted.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   During the restart, the cluster is unavailable. If the restart fails, data may be lost or the cluster may become unavailable. Therefore, exercise caution when performing this operation.  
>-   If the cluster you want to restart is available, you are advised to stop all data processing tasks on the cluster before restarting it. If there are running tasks, for example, importing data, searching for data, backing up or restoring snapshots, then the snapshots or transmitted data may be lost upon the restart. Therefore you are advised to stop all cluster tasks before restarting the cluster.  

## Prerequisites<a name="section19268114314472"></a>

-   The cluster is in the  **Available**  or  **Abnormal**  status.
-   There are no running tasks, such as importing data, searching for data, creating snapshots, and restoring snapshots, on the cluster.

## Procedure<a name="section1859217234819"></a>

1.  Log in to the CSS management console.
2.  Click  **Clusters**  to switch to the  **Clusters**  page. In the row where the cluster you want to restart is located, click  **More \> Restart**  in the  **Operation**  column.
3.  It takes several minutes for the cluster to restart. Refresh the page and check the cluster status. During the restart, the cluster status is  **Processing**, and the task status is  **Restarting**. If the cluster status changes to  **Available**, the cluster has been restarted successfully. If the cluster status changes to  **Abnormal**, you are advised to contact customer service for troubleshooting.

