# Configuring Service Parameters<a name="EN-US_TOPIC_0125375703"></a>

## Scenario<a name="section4364830519950"></a>

On MRS Manager, users can view and modify the default service configurations based on site requirements. Configurations can be imported and exported.

## Impact on the System<a name="section43521686191035"></a>

-   After the attributes of HBase, HDFS, Hive, Spark, Yarn, and MapReduce are configured, the client configurations need to be downloaded to update the files.
-   The parameters of DBService cannot be modified if only one DBService role instance exists in the cluster.

## Procedure<a name="section3663617191025"></a>

-   Modify a service.
    1.  Click  **Service**.
    2.  Select the target service from the service list.
    3.  Click the  **Service Configuration**  tab.
    4.  Set  **Type** to **All**. All configuration parameters of the service are displayed in the navigation tree. The root nodes in the navigation tree represent the service names and role names.
    5.  In the navigation tree, choose a parameter and change its value. You can also enter the parameter name in  **Search**  to search for it and view the result.

        You can click  ![](figures/icon_mrs_cancel.jpg)  to restore a parameter value.

        >![](/images/icon-note.gif) **NOTE:**   
        >You can also use host groups to change role instance configurations in batches. Choose a role name in  **Role**, and then choose **<select hosts\>** in **Host**. Enter a name in **Host Group Name**, select the target host from **All Hosts** and add it to **Selected Hosts**. Click **OK** to add it to the host group. The added host group can be selected from **Host**  and is only valid on the current page. The page cannot be saved after being refreshed.  

    6.  Click  **Save Configuration**, select **Restart the affected services or instances**, and click **OK**  to restart the service.

        Click  **Finish** when the system displays **Operation succeeded**. The service is successfully started.

        >![](/images/icon-note.gif) **NOTE:**   
        >If you do not restart Yarn after upgrading its queue configuration, you can choose  **More**  \>  **Refresh the queue**  for the configuration to take effect.  


-   Export service configuration parameters.
    1.  Click  **Service**.
    2.  Select a service.
    3.  Click  **Service Configuration**.
    4.  Click  **Export Service Configuration**. Select a path for saving the configuration files.

-   Import service configuration parameters.
    1.  Click  **Service**.
    2.  Select a service.
    3.  Click  **Service Configuration**.
    4.  Click  **Import Service Configuration**.
    5.  Select the target configuration file.
    6.  Click  **Save Configuration**, and select **Restart the affected services or instances**. Click **OK**.

        When  **Operation succeeded** is displayed, click **Finish**. The service is started successfully.



