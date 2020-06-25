# Step 7: Viewing Other Documents and Clearing Resources<a name="dws_01_0079"></a>

## Viewing Other Relevant Documents<a name="section4208640165543"></a>

After performing the preceding steps, you can refer to the following resources to learn more about DWS:

-   : This guide provides detailed information about the concepts and operations related to creating, managing, monitoring, and connecting clusters.
-   _Data Warehouse Service Database Developer Guide_: This guide provides comprehensive and detailed information on how to build, manage, and query the DWS databases, including SQL syntax, user management, and data import and export.

## Clearing Resources<a name="section1947515211228"></a>

After performing the preceding steps, if you do not need to use the sample data, clusters, ECSs, and VPCs in the created examples, delete these resources to prevent them from wasting and occupying quotas.

1.  Delete the ECS created in section  [Step 3: Connecting to a Cluster](step-3-connecting-to-a-cluster.md)  for connecting to the data warehouse cluster.
    1.  Log in to the public cloud management console.
    2.  Click  **Service List**  and choose  **Computing**  \>  **Elastic Cloud Server**  to enter the ECS console.
    3.  In the navigation tree on the left, click  **Elastic Cloud Server**. In the ECS list, select the ECS to be deleted and click  **Delete**. You can choose to delete the associated EIP and data disks at the same time. If you do not delete them, they are reserved. If necessary, you can manually delete them later.
    4.  Click  **OK**.

2.  Delete a data warehouse cluster.

    On the DWS management console, click  **Cluster Management**, locate the row that contains  **dws-demo**  in the cluster list, and choose  **More \> Delete**. In the dialog box that is displayed, select  **Release the EIP bound with the cluster**  click  **OK**.

    If the cluster to be deleted uses an automatically created security group that is not used by other clusters, the security group is automatically deleted when the cluster is deleted.

3.  Delete a subnet. Before deleting the subnet, ensure that it is not bound to other resources.

    Log in to the VPC management console. In the navigation tree on the left, click  **Virtual Private Cloud**. In the VPC list, click  **vpc-dws**. In the subnet list, locate the row that contains  **subnet-dws**  and click  **Delete**.

4.  Delete a VPC. Before deleting the VPC, ensure that it is not bound to other resources.

    Log in to the VPC management console, locate the row that contains  **vpc-dws**  in the VPC list, and click  **Delete**.

    For details, see section  **Deleting a VPC**  in the  _Virtual Private Cloud User Guide_.


