# Configuring the Queue Capacity Policy of a Resource Pool<a name="EN-US_TOPIC_0125375915"></a>

## Scenario<a name="section3046557620546"></a>

After a resource pool is added, the capacity policies of available resources need to be configured for Yarn task queues. This ensures that tasks in the resource pool are running properly. Each queue can be configured with the queue capacity policy of only one resource pool. Users can view the queues in any resource pool and configure queue capacity policies. After the queue policies are configured, Yarn task queues and resource pools are associated.

## Prerequisites<a name="section1748565020533"></a>

-   A resource pool has been added.
-   The task queues are not associated with other resource pools. By default, all task queues are associated with the default resource pool.

## Procedure<a name="section5215752720514"></a>

1.  On MRS Manager, click  **Tenant**.
2.  Click the  **Dynamic Resource Plan**  tab.
3.  In  **Resource Pool**, select a specified resource pool.

    **Available Resource Quota**: indicates that all resources in each resource pool are available for queues by default.

4.  Locate the specified queue in the  **Resource Allocation** table, and click **Modify** in the **Operation**  column.
5.  In  **Modify Resource Allocation**, configure the resource capacity policy of the task queue in the resource pool.
    -   **Capacity \(%\)**: specifies the percentage of the current tenant's computing resource usage.
    -   **Maximum Capacity \(%\)**: specifies the percentage of the current tenant's maximum computing resource usage.

6.  Click  **OK**  to save the settings.

