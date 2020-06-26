# Creating a Ranger Cluster<a name="EN-US_TOPIC_0228886234"></a>

1.  Create a cluster by referring to  [Creating a Cluster](creating-a-cluster.md). Select the Ranger component \(available only for MRS 1.9.2\).

    Currently, only normal clusters support Ranger. Security clusters with Kerberos authentication enabled do not support Ranger.

2.  Configure other parameters and create the cluster by referring to  [Creating a Cluster](creating-a-cluster.md).

    >![](/images/icon-note.gif) **NOTE:**   
    >-   After the cluster is created, Ranger does not control users' permissions to access Hive and HBase.  
    >-   When Ranger is used to manage component permissions, for example, manage Hive table permissions, if a user submits a Hive job \(operation on Hive data tables\) on the interface or client, a message may be displayed indicating that the user does not have permission. In this case, you need to configure the database or table permission for the user who submits the job in Ranger. For details, see the step for adding a policy in  [Configuring Hive Access Permissions in Ranger](configuring-hive-access-permissions-in-ranger.md)  or  [Configuring HBase Access Permissions in Ranger](configuring-hbase-access-permissions-in-ranger.md).  


