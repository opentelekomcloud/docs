# Isolating a Host<a name="EN-US_TOPIC_0125375583"></a>

## Scenario<a name="section6535825520147"></a>

If a host is found to be abnormal or faulty, affecting cluster performance or preventing services from being provided, users can temporarily exclude that host from the available nodes in the cluster. In this way, the client can access other available nodes. In scenarios where patches are to be installed in a cluster, users can also exclude a specified node from patch installation.

Users can isolate a host manually on MRS Manager based on the actual service requirements or O&M plan. Only non-management nodes can be isolated.

## Impact on the System<a name="section1812132520224"></a>

-   After a host is isolated, all role instances on the host will be stopped. You cannot start, stop, or configure the host or any  instances on the host.
-   After a host is isolated, statistics of the monitoring status and indicator data of the host hardware and instances cannot be collected or displayed.

## Procedure<a name="section4713394420240"></a>

1.  On MRS Manager, click  **Host**.
2.  Select the check box of the host to be isolated.
3.  Choose  **More**  \>  **Isolate Host**.
4.  In  **Isolate Host**, click **OK**.

    When  **Operation succeeded** is displayed, click **Finish**. The host is isolated successfully, and the value of **Operating Status** becomes **Isolated**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The isolation of a host can be canceled and the host can be added to the cluster again. For details, see  [Canceling Isolation of a Host](canceling-isolation-of-a-host.md).  


