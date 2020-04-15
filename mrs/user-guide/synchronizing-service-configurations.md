# Synchronizing Service Configurations<a name="EN-US_TOPIC_0125375914"></a>

## Scenario<a name="section33375023193729"></a>

If  **Configuration Status** of any service is **Expired** or **Failed**, users can synchronize configurations for the cluster or service to recover its configuration status. If the configuration status of all services in the cluster is **Failed**, synchronize the cluster configurations with the background configurations.

## Impact on the System<a name="section49559162193823"></a>

After synchronizing service configuration, users need to restart the service  that had an expired configuration. The service is unavailable during the restart.

## Procedure<a name="section48561947193832"></a>

1.  On MRS Manager, click  **Service**.
2.  Select the target service from the service list.
3.  Click  **More** in the upper pane, and select **Synchronize Configuration**  from the drop-down list.
4.  In the dialog box that is displayed, select  **Restart services or instances whose configurations have expired**, and click **OK**.

    When  **Operation succeeded** is displayed, click **Finish**. The service is started successfully.


