# Configuring Customized Service Parameters<a name="EN-US_TOPIC_0125375793"></a>

## Scenario<a name="section4762802519184"></a>

Each component of MRS supports all open source parameters. MRS Manager supports the modification of some parameters for key application scenarios. Some component clients may not include all parameters with open source features. To modify the component parameters that are not directly supported by MRS Manager, users can add new parameters for components by using the configuration customization function on MRS Manager. Newly added parameters are saved in component configuration files and take effect after the component is restarted.

## Impact on the System<a name="section52388079191833"></a>

-   After the service attributes are configured, the service needs to be restarted. The service cannot be accessed during the restart.
-   After the attributes of HBase, HDFS, Hive, Spark, Yarn, and MapReduce are configured, the client configurations need to be downloaded to update the files.

## Prerequisites<a name="section41613932191911"></a>

You have learned the meanings of parameters to be added, configuration files to take effect, and impact on components.

## Procedure<a name="section46971658191927"></a>

1.  On MRS Manager, click  **Service**.
2.  Select the target service from the service list.
3.  Click  **Service Configuration**.
4.  Set  **Type** to **All**.
5.  In the navigation tree, choose  **Customization**. The customized parameters of the current component are displayed on MRS Manager.

    The configuration files that save the newly added customized parameters are displayed in  **Parameter File**. Different configuration files may support open source parameters with the same names. After the parameters in different files are set to different values, the configuration effect depends on the sequence of the configuration files that are loaded by components. Service-level and role-level customized parameters are supported. Perform configuration based on the actual service requirements. Customized parameters for a single role instance are not supported.

6.  Based on the configuration files and parameter functions, enter parameter names supported by components in  **Name** and enter the parameter values in the **Value**  column of the row where the parameters are located.
    -   You can click  ![](figures/en-us_image_0125375405.jpg) or ![](figures/en-us_image_0125375887.jpg) to add or delete a customized parameter. A customized parameter can be deleted only after you click ![](figures/en-us_image_0125375908.jpg)  to add the parameter.
    -   You can click  ![](figures/en-us_image_0125375964.jpg)  to restore a parameter value.

7.  Click  **Save Configuration**, select **Restart the affected services or instances**, and click **OK**  to restart the service.

    When  **Operation succeeded** is displayed, click **Finish**. The service is started successfully.


## Task Example<a name="section32890065192053"></a>

**Configuring Customized Hive Parameters**

Hive depends  on HDFS. By default, Hive accesses the client of HDFS. The configuration parameters to take effect are controlled by HDFS in a unified manner. For example, HDFS parameter **ipc.client.rpc.timeout** affects the RPC timeout period for all clients to connect to the HDFS server. If you need to modify the timeout period for Hive to connect to HDFS, you can use the configuration customization function. After this parameter is added to the **core-site.xml** file of Hive, it  can be identified by the Hive service and replace the HDFS configuration.

1.  On MRS Manager, choose  **Service**  \>  **Hive**  \>  **Service Configuration**.
2.  Set  **Type** to **All**.
3.  In the navigation tree, choose  **Customization**  of the Hive service level. The service-level customized parameters supported by Hive are displayed on MRS Manager.
4.  In the  **Name**: column of the  **core.site.customized.configs** parameter in **core-site.xml**, enter **ipc.client.rpc.timeout**, and enter the new parameter value in **Value**. For example, enter **150000**. The unit is millisecond.
5.  Click  **Save Configuration**, select **Restart the affected services or instances**, and click **OK**  to restart the service.

    When **Operation succeeded**  is displayed, click  **Finish**. The service is successfully started.


