# Shrinking a Cluster<a name="EN-US_TOPIC_0125375968"></a>

You can reduce Core nodes or Task nodes based on service requirements to shrink a cluster so that MRS has better storage and computing capabilities at lower O&M costs.

## Background<a name="section19165099103254"></a>

An MRS cluster supports a maximum of 502 nodes. There are two Master nodes by default.  The minimum number of Core nodes is three. The maximum number of 500 Core and Task nodes are supported by default. If more than 500 Core and  Task nodes are required, contact technical support engineers or invoke a background interface to modify the database.

Core and Task nodes can be reduced but Master nodes cannot. After you adjust the number of nodes when shrinking a cluster, the system will automatically select nodes to delete them. At least three Core nodes and 0 Task node must be left.

**Node selection policy**

-   Service components such as ZooKeeper, DBServcie, KrbServer, and LdapServer are fundamental for stable cluster running. Therefore, their nodes cannot be deleted.
-   Core nodes are used to store cluster service data. When shrinking a cluster, data on the nodes to be deleted must be fully migrated to other nodes. Therefore, perform follow-up operations after cluster shrinking only when all services are decommissioned, such as making nodes exit MRS Manager and deleting ECSs. When you select nodes, prefer healthy nodes that store a small volume of data and whose instances can be decommissioned to avoid node decommission failure. For example, if DataNodes are installed on Core nodes in an analysis cluster, healthy DataNodes that store a small volume of data will be preferred.
-   Task nodes are computing nodes and are not used to store cluster data. Therefore, node data migration is not involved. When shrinking a cluster, prefer nodes whose health status is  **Bad**, **Unknown**, or **Partially Healthy**. You can view health status of nodes on the instance management page after logging in to MRS Manager.

## **Cluster shrinking verification policies**<a name="section23577146145756"></a>

Component decommissioning restrictions vary. Cluster shrinking is allowed only after all component decommissioning restrictions are complied with.  [Table 1](#table36043989145756)  describes the component decommissioning restrictions.

**Table  1**  Component decommissioning restrictions

<a name="table36043989145756"></a>
<table><thead align="left"><tr id="row59047728145756"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p60776224145756"><a name="p60776224145756"></a><a name="p60776224145756"></a>Component</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p23927110145756"><a name="p23927110145756"></a><a name="p23927110145756"></a>Decommissioning Restriction</p>
</th>
</tr>
</thead>
<tbody><tr id="row27613415145756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p18136646145756"><a name="p18136646145756"></a><a name="p18136646145756"></a>HDFS/DataNode</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p59782258145756"><a name="p59782258145756"></a><a name="p59782258145756"></a>Restriction: The total volume of HDFS data must not exceed 80% of total volume of the shrunk HDFS cluster.</p>
<p id="p1169410145756"><a name="p1169410145756"></a><a name="p1169410145756"></a>Cause: This ensures that there is sufficient available space to store existing data and some space can be reserved.</p>
</td>
</tr>
<tr id="row4671465145756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p47194149145756"><a name="p47194149145756"></a><a name="p47194149145756"></a>HBase/RegionServer</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p64629758145756"><a name="p64629758145756"></a><a name="p64629758145756"></a>Restriction: <span id="ph59720092164743"><a name="ph59720092164743"></a><a name="ph59720092164743"></a>Total available memory of <span id="ph1878013415147"><a name="ph1878013415147"></a><a name="ph1878013415147"></a>RegionServer</span>s on nodes excluding nodes to be deleted must be greater than 1.2 times of the memory used by RegionServers on the nodes to be deleted.</span></p>
<p id="p44796915145756"><a name="p44796915145756"></a><a name="p44796915145756"></a>Cause: Regions on a node to be decommissioned will be migrated to other nodes. Therefore, available memory of other nodes must be sufficient to bear regions migrated from the decommissioned node.</p>
</td>
</tr>
<tr id="row50083567145756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p42043189145756"><a name="p42043189145756"></a><a name="p42043189145756"></a>Kafka/Broker</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p50055139145756"><a name="p50055139145756"></a><a name="p50055139145756"></a>Restriction: After shrinking, the number of nodes must not be fewer than the maximum number for topic replicas and the used Kafka disk space must not exceed 80% of the total Kafka disk space of the cluster.</p>
<p id="p47843071145756"><a name="p47843071145756"></a><a name="p47843071145756"></a>Cause: This avoids insufficient disk space after cluster shrinking.</p>
</td>
</tr>
<tr id="row12100530145756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p48098925145756"><a name="p48098925145756"></a><a name="p48098925145756"></a>Storm/ Supervisor</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3698841145756"><a name="p3698841145756"></a><a name="p3698841145756"></a>Restriction: The number of slots in the shrunk cluster must be sufficient to run the submitted jobs.</p>
<p id="p33289569145756"><a name="p33289569145756"></a><a name="p33289569145756"></a>Cause: This prevents resources from being insufficient to execute streaming processing tasks.</p>
</td>
</tr>
<tr id="row11096169145756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p41795909145756"><a name="p41795909145756"></a><a name="p41795909145756"></a>Flume/FlumeServer</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p30025494145756"><a name="p30025494145756"></a><a name="p30025494145756"></a>Restriction: If FlumeServer is installed and Flume tasks have been configured on a node, the node cannot be deleted.</p>
<p id="p1793998145756"><a name="p1793998145756"></a><a name="p1793998145756"></a>Cause: This prevents the deployed service applications from being mistakenly deleted.</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section6382765316417"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/wwx437827-中软基础平台部-datasight-image-bbfbe22f-2a2d-4e1b-8f10-a7782fd1d3ed-25.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Resize Cluster** and go to the **Resize Cluster**  page.

    This operation can be performed only on a running cluster in which all nodes are running.

5.  Set  **Node Type** to **Core Node** or **Task Node** and configure the **Nodes After Resize**  parameter.
6.  On the  **Resize Cluster** page, click **OK**.
7.  In the  **Shrink Node**  dialog box, click **OK**.

    Cluster shrinking is explained as follows:

    -   During shrinking: The cluster status is  **Shrinking**. The submitted jobs will be executed and you can submit new jobs. You are not allowed to continue to shrink or terminate the cluster. You are advised not to restart the cluster or modify the cluster configuration.
    -   Successful shrinking: The cluster status is  **Running**. The resources used after node reduction are charged.
    -   Failed shrinking: The cluster status is  **Running**. You are allowed to execute jobs and shrink the cluster again.

    After the cluster shrink is successful, you can view node information on the cluster details page.


