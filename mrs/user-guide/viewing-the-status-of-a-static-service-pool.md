# Viewing the Status of a Static Service Pool<a name="EN-US_TOPIC_0125375705"></a>

## Scenario<a name="section55506379185015"></a>

The big data management platform uses static service resource pools to manage and isolate service resources that are not running on Yarn. The platform dynamically manages the CPU, I/O, and memory capacity that can be used by HBase, HDFS, and Yarn on the deployment nodes. The system supports time-based automatic policy adjustment for static service resource pools. This enables a cluster to automatically adjust the parameters at different periods to ensure a more efficient utilization of resources.

On MRS Manager, users can view the monitoring indicators of the resources used by each service in static service pools. The following indicators are included:

-   Overall CPU usage of a service
-   Overall disk I/O read rate of a service
-   Overall disk I/O write rate of a service
-   Overall memory used by a service

## Procedure<a name="section23567813185316"></a>

1.  On MRS Manager, click  **System**. In the **Resource** area, click **Configure** **Static Service Pool**.
2.  Click  **Status**.
3.  View the system resource adjustment base.
    -   **System Resource Adjustment Base**  specifies the maximum amount of resources that can be used by services on each node in the cluster. If the node has only one service, this service exclusively uses the available resources on the node. If the node has multiple services, they share the available resources.
    -   **CPU\(%\)**  specifies the maximum number of CPUs that can be used by services on the node.
    -   **Memory\(%\)**  specifies the maximum memory that can be used by services on the node.

4.  View the usage of cluster service resources.

    In the Real-Time Statistics area, select  **All Services**. The resource usage of all services in the service pool is displayed in **Real-Time Statistics**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >**Effective Configuration Group** specifies the resource control configuration group used by cluster services currently. By default, the **default**  configuration group is used at all periods in a day. This configuration group specifies that cluster services can use all CPUs and 70% of the memory of a node.  

5.  View the resource usage status of a single service.

    In the Real-Time Statistics area, select a specified service. The resource usage of the service in the service pool will be displayed in  **Real-Time Statistics**.

6.  Set an interval for automatic page refreshing.

    The following parameters are supported:

    -   **Refresh every 30 seconds**: refreshes the page once every 30 seconds.
    -   **Refresh every 60 seconds**: refreshes the page once every 60 seconds.
    -   **Stop refreshing**: stops page refreshing.


