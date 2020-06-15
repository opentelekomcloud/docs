# Restarting a Cluster<a name="dws_01_0024"></a>

If a cluster is in low performance or cannot work properly, you may need to restart it for restoration. After modifying a cluster's configurations, such as security settings and parameters in the parameter group, manually restart the cluster to make the configurations take effect.

## Impact on the System<a name="section33979687105031"></a>

-   A cluster cannot provide services during the restart. Therefore, before the restart, ensure that no task is running and all data is saved.

    If the cluster is processing service data, such as importing data, querying data, creating snapshots, or restoring snapshots, cluster restarting will cause file damage or restart failure. You are advised to stop all cluster tasks before restarting the cluster.

    View the  **Session Count**  and  **Active SQL Count**  metrics to check whether the cluster has active events. For details, see section  [Monitoring a Cluster](monitoring-a-cluster.md).

-   The time required for restarting a cluster depends on the cluster scale and services. Generally, it takes about 3 minutes to restart a cluster. The duration does not exceed 20 minutes.
-   If the restart fails, the cluster may be unavailable. Contact technical support engineers or try again later.

## **Procedure**<a name="section59074732104918"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  Click  **Cluster Management**.
3.  In the  **Operation**  column of the cluster to be restarted, click  **Restart**.
4.  In the dialog box that is displayed, click  **OK**.

    **Task Information**  changes to  **Restarting**. When  **Cluster Status**  changes to  **Available**  again, the cluster is successfully restarted.


