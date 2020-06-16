# Synchronizing Role Instance Configuration<a name="EN-US_TOPIC_0125375786"></a>

## Scenario<a name="section24187759195439"></a>

When the  **Configuration Status** of a role instance is **Expired** or **Failed**, users can synchronize the configuration data of the role instance with the background configuration.

## Impact on the System<a name="section16190722195456"></a>

After synchronizing a role instance configuration, you need to restart the role instance  that had an expired configuration. The role instance is unavailable during the restart.

## Procedure<a name="section57917676195511"></a>

1.  On MRS Manager, click  **Service**  and choose a service name.
2.  Click the  **Instance**  tab.
3.  Click the target role instance in the role instance list.
4.  Click  **More** in the upper pane, and select **Synchronize Configuration**  from the drop-down list.
5.  In the dialog box that is displayed, select  **Restart services or instances whose configurations have expired**, and click **OK**  to restart a role instance.

    When  **Operation succeeded**  is displayed, click **Finish**. The service is started successfully.


