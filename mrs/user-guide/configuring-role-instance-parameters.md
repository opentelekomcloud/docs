# Configuring Role Instance Parameters<a name="EN-US_TOPIC_0125375839"></a>

## Scenario<a name="section4364830519950"></a>

View and modify default role instance configurations on MRS Manager. Parameters must be configured based on site requirements. Configurations can be imported and exported.

## Impact on the System<a name="section43521686191035"></a>

After the attributes of HBase, HDFS, Hive, Spark, Yarn, and MapReduce are configured, the client configurations need to be downloaded to update the files.

## Procedure<a name="section3663617191025"></a>

-   Modify role instance configurations.
    1.  On MRS Manager, click  **Service**.
    2.  Select the target service from the service list.
    3.  Click the  **Instance**  tab.
    4.  Click the target role instance in the role instance list.
    5.  Click the  **Instance Configuration**  tab.
    6.  Set  **Type** to **All**. All configuration parameters of the role instances are displayed in the navigation tree.
    7.  In the navigation tree, choose a parameter and change its value. You can also enter the parameter name in  **Search**  to search for the parameter and view the result.

        You can click  ![](figures/en-us_image_0125375386.jpg)  to restore a parameter value.

    8.  Click  **Save Configuration**, select **Restart the role instance**, and click **OK**  to restart the role instance.

        When  **Operation succeeded** is displayed, click **Finish**. The service is started successfully.


-   Export configuration data of a role instance.
    1.  On MRS Manager, click  **Service**.
    2.  Select a service.
    3.  Select a role instance or click  **Instance**.
    4.  Select a role instance on a specified host.
    5.  Click  **Instance Configuration**.
    6.  Click  **Export Instance Configuration**  to export the configuration data of a specified role instance, and choose a path for saving the configuration file.

-   Import configuration data of a role instance.
    1.  Click  **Service**.
    2.  Select a service.
    3.  Select a role instance or click  **Instance**.
    4.  Select a role instance on a specified host.
    5.  Click  **Instance Configuration**.
    6.  Click  **Import Instance Configuration**  to import configuration data of a specified role instance.
    7.  Click  **Save Configuration** and select **Restart the role instance**. Click **OK**.

        When  **Operation succeeded** is displayed, click **Finish**. The service is started successfully.



