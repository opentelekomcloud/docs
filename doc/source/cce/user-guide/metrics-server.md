# metrics-server<a name="cce_01_0205"></a>

From version 1.8 onwards, Kubernetes provides resource usage metrics, such as the container CPU and memory usage, through the Metrics API. These metrics can be directly accessed by users \(for example, by using the  **kubectl top**  command\) or used by controllers \(for example, Horizontal Pod Autoscaler\) in a cluster for decision-making. The specific component is Metrics-Server, which is used to substitute for heapster for providing the similar functions. heapster has been gradually abandoned since v1.11.

Metrics-Server is a cluster-wide aggregator of resource usage data. You can quickly install this add-on on the CCE console.

The official community project and documentation are available at  [https://github.com/kubernetes-sigs/metrics-server](https://github.com/kubernetes-sigs/metrics-server).

## Constraints<a name="section82095773811"></a>

This add-on can be installed only in hybrid and BMS clusters of v1.13 or later.

## Installing the Add-on<a name="section8828031113811"></a>

After metrics-server is installed, you can create an HPA policy on the  **Workload Scaling**  tab page of the  **Auto Scaling**  page. For details, see  [Scaling a Workload](scaling-a-workload.md).

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tab page, click  **Install Add-on**  under  **metrics-server**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next: Configuration**.
3.  Select  **Single**  or  **HA**  for  **Add-on Specifications**, and click  **Install**.

    After the add-on is installed, click  **Back to Add-on List**. On the  **Add-on Instance**  tab page, select the corresponding cluster to view the running instance. This indicates that the add-on has been installed on each node in the cluster.


## Uninstalling the Add-on<a name="section2588209113916"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, click  **Uninstall**  under  **metrics-server**.
2.  In the dialog box that is displayed, click  **OK**  to uninstall the add-on.

