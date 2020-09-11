# Reverting Cluster Instance Nodes<a name="dds_03_0018"></a>

## Scenarios<a name="section14511374172320"></a>

This section guides you on how to revert nodes that fail to be added.

## Reverting Nodes in Batches<a name="section42700170172320"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, locate the cluster instance to which nodes fail to be added and choose  **More**  \>  **Revert**  in the  **Operation**  column. 
3.  In the displayed dialog box, click  **Yes**.

    During reversal, the node status is  **Deleting node**. This process takes about 1 to 3 minutes. 


## Deleting a Single Node<a name="section44097393172320"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance to which the node fails to be added.
3.  In the  **Node Information**  area on the  **Basic Information**  tab, click the  **mongos**  or  **shard**  tab, locate the mongos or shard that fail to be added, and choose  **More**  \>  **Delete**.
4.  In the displayed dialog box, click  **Yes**.

    During deletion, the node status is  **Deleting node**. This process takes about 1 to 3 minutes. 


