# Decommissioning and Recommissioning Role Instances<a name="EN-US_TOPIC_0125375638"></a>

## Scenario<a name="section6659216414560"></a>

If a Core or Task node is faulty, the cluster status may become abnormal. In an MRS cluster, data can be stored on different Core nodes. Users can decommission the specified role instance on MRS Manager to stop the role instance from providing services. After fault rectification, users can recommission the role instance.

For MRS versions earlier than MRS 1.6.0, the following role instances can be decommissioned and recommissioned.

-   DataNode role instance on HDFS
-   NodeManager role instance on Yarn

For MRS 1.6.0 or later, the following role instances can be decommissioned and recommissioned.

-   DataNode role instance on HDFS

-   NodeManager role instance on Yarn
-   RegionServer role instance on HBase
-   Broker role instance on Kafka

Restrictions:

-   If the number of DataNodes is less than or equal to the number of HDFS copies, decommissioning cannot be performed. For example, if the number of HDFS copies is three and the number of DataNodes is less than four in the system, decommissioning cannot be performed. After the decommissioning is performed for 30 minutes, an error will be reported, which forces MRS Manager to exit the decommissioning.
-   If the number of Kafka Broker instances is less than or equal to that of Kafka  Broker  copies, decommissioning cannot be performed. For example, if the number of  Kafka Broker  copies is two and the number of nodes is less than three in the system, decommissioning cannot be performed. Role instance decommissioning will fail on MRS Manager and exit.
-   To reuse a decommissioned role instance, users must recommission and restart it.

## Procedure<a name="section4436513915031"></a>

1.  On MRS Manager, click  **Service**.
2.  In the service list, click the target service.
3.  Click the  **Instance**  tab.
4.  Select the check box in front of the specified role instance name.
5.  Click  **More**, and select **Decommission** **Role Instance**  or **Recommission**  from the drop-down list.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the target service is restarted in another browser or window while the instance decommissioning operation is in progress, MRS Manager displays a message indicating that the decommissioning is suspended and **Operating Status** is **Started**. However, the instance decommissioning is actually complete in the background. You need to decommission the instance again to synchronize the status.  


