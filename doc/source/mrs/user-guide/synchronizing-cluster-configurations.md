# Synchronizing Cluster Configurations<a name="EN-US_TOPIC_0125375894"></a>

## Scenarios<a name="section3133602710414"></a>

If  **Configuration Status** of any service is **Expired** or **Failed**, users can synchronize configurations to recover the configuration status.

-   If the configuration status of all services in the cluster is  **Failed**, synchronize the cluster configurations with the background configurations.
-   If the configuration status of some services in the cluster is  **Failed**, synchronize the specified service configurations with the background configurations.

## Impact on the System<a name="section422941510445"></a>

After synchronizing cluster configurations, users need to restart the service  that has an expired configuration. The service is unavailable during the restart.

## Procedure<a name="section568019601054"></a>

1.  On MRS Manager, click  **Service**.
2.  Click  **More** above the service list, and choose **Synchronize Configuration**  from the drop-down list.
3.  In the dialog box that is displayed, select  **Restart services or instances whose configurations have expired**, and click **OK**.

    When **Operation succeeded**  is displayed, click **Finish**. The cluster is successfully started.


