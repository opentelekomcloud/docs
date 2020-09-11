# Adding Cluster Instance Nodes<a name="en-us_topic_increase_nodes"></a>

## **Scenarios**<a name="section34286219201027"></a>

This section guides you on how to add nodes to a DB instance.

>![](/images/icon-note.gif) **NOTE:**   
>-   You can add nodes when the instance status is  **Available**,  **Deleting backup**, or  **Checking restoration**.  
>-   A DB instance cannot be deleted when one or more nodes are being added.  

## Add mongos<a name="section51046890162836"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **DB Instance Topology**  area on the  **Basic Information**  page, click  ![](figures/icon-add.png)  next to the mongos nodes. 
4.  On the displayed page, specify  **Node Class**,  **mongos Quantity**, and  **Parameter Group**. Then, click  **Submit**.

    A cluster instance of Community Edition supports a maximum of 12 mongos nodes.

5.  View the result of adding nodes.
    -   This process takes about 10 to 15 minutes. The status of the DB instance in the instance list is  **Adding node**. 
    -   In the upper right corner of the DB instance list, click  ![](figures/icon-fresh.png)  to refresh the list. The instance status changes to  **Available**.
    -   On the  **mongos**  tab in the  **Node Information**  area, view the information about the node you added.
    -   If the mongos fail to be added, you can revert them in batches or delete them one by one. For details, see section  [Reverting Cluster Instance Nodes](reverting-cluster-instance-nodes.md).


## Add shard<a name="section3495337616353"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **DB Instance Topology**  area on the  **Basic Information**  page, click  ![](figures/icon-add.png)  next to the shard nodes. 
4.  On the displayed page, specify  **Node Class**,  **Storage Space**,  **shard Quantity**, and  **Parameter Group**. Then, click  **Submit**.
    -   The storage space you applied for will contain the system overhead required for inode, reserved block, and database operation. The storage space must be an integer multiple of 10.
    -   A cluster instance of Community Edition supports a maximum of 12 shard nodes.

5.  View the result of adding nodes.
    -   This process takes about 10 to 15 minutes. The status of the DB instance in the instance list is  **Adding node**. 
    -   In the upper right corner of the DB instance list, click  ![](figures/icon-fresh.png)  to refresh the list. The instance status changes to  **Available**.
    -   On the  **shard**  tab in the  **Node Information**  area, view the information about the node you added.
    -   If the shards fail to be added, you can revert them in batches or delete them one by one. For details, see section  [Reverting Cluster Instance Nodes](reverting-cluster-instance-nodes.md).


