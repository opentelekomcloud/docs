# Clearing the Configuration of a Queue<a name="EN-US_TOPIC_0125376151"></a>

## Scenario<a name="section1730587820922"></a>

Users can clear the configuration of a queue on MRS Manager when the queue does not need resources from a resource pool or if a resource pool needs to be disassociated from the queue. Clearing the configuration of a queue means that the resource capacity policy of the queue is canceled.

## Prerequisites<a name="section6339023820857"></a>

If a queue needs to be unbound from a resource pool, this resource pool cannot serve as the default resource pool of the queue. Therefore, you  must first change the default resource pool of the queue to another one. For details, see [Configuring a Queue](configuring-a-queue.md).

## Procedure<a name="section798537920847"></a>

1.  On MRS Manager, click  **Tenant**.
2.  Click the  **Dynamic Resource Plan**  tab.
3.  In  **Resource Pool**, select a specified resource pool.
4.  Locate the specified queue in the  **Resource Allocation** table, and click **Clear** in the **Operation**  column.

    In  **Clear Queue Configuration**, click **OK**  to clear the queue configuration in the current resource pool.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If no resource capacity policy is configured for a queue, the clearance function is unavailable for the queue by default.  


