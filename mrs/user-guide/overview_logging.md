# Overview<a name="EN-US_TOPIC_0125375864"></a>

This section describes remote login, MRS cluster node types, and node functions.

MRS cluster nodes support remote login. The following remote login methods are available:

-   GUI login: Use the remote login function provided by the ECS management console to log in to the Linux interface of the Master node.
-   SSH login: Applies to Linux ECSs only. You can use a remote login tool \(such as PuTTY\) to log in to an ECS. To use this method, you must assign an elastic IP address \(EIP\) to the ECS.

    For details about applying for and binding an elastic IP address for Master nodes, see "Assigning an EIP and Binding It to an ECS" under the "Management" section in the  _VPC User Guide_.

    You can log in to a Linux ECS using either a key pair or password. To use a key pair, you must log in to the Linux ECS as user  **linux**. For the login procedure, see [Logging In to a Linux ECS Using a Key Pair \(SSH\)](logging-in-to-a-linux-ecs-using-a-key-pair-(ssh).md). If you use a password, see [Logging In to a Linux ECS Using a Password \(SSH\)](logging-in-to-a-linux-ecs-using-a-password-(ssh).md).


In an MRS cluster, a node is an ECS.  [Table 1](#table5402098183740)  describes node types and functions.

**Table  1**  Cluster node types

<a name="table5402098183740"></a>
<table><thead align="left"><tr id="row46478794183740"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p6685939183740"><a name="p6685939183740"></a><a name="p6685939183740"></a>Node Type</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p4690148183740"><a name="p4690148183740"></a><a name="p4690148183740"></a>Function</p>
</th>
</tr>
</thead>
<tbody><tr id="row44357702183740"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p36204096183740"><a name="p36204096183740"></a><a name="p36204096183740"></a>Master node</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3153910114246"><a name="p3153910114246"></a><a name="p3153910114246"></a><span>Management node of an MRS cluster. It manages and monitors the cluster.</span></p>
<p id="p46850683183740"><a name="p46850683183740"></a><a name="p46850683183740"></a>In the navigation tree of the MRS management console, choose <span class="menucascade" id="menucascade1151290219249"><a name="menucascade1151290219249"></a><a name="menucascade1151290219249"></a><b><span class="uicontrol" id="uicontrol2364883219249"><a name="uicontrol2364883219249"></a><a name="uicontrol2364883219249"></a>Clusters &gt; Active Clusters</span></b></span>, select a running cluster, and click its name to switch to the cluster details page. On the&nbsp;<span class="parmname" id="parmname5666161214828"><a name="parmname5666161214828"></a><a name="parmname5666161214828"></a><b>Node</b></span>&nbsp;tab page, view the&nbsp;<span class="parmname" id="parmname337660711206"><a name="parmname337660711206"></a><a name="parmname337660711206"></a><b>Name</b></span>. The node that contains&nbsp;<span class="parmvalue" id="parmvalue61796996143113"><a name="parmvalue61796996143113"></a><a name="parmvalue61796996143113"></a><b>master1</b></span>&nbsp;in its name is the Master1 node. The node that contains&nbsp;<span class="parmvalue" id="parmvalue788678911139"><a name="parmvalue788678911139"></a><a name="parmvalue788678911139"></a><b>master2</b></span> in its name is the Master2 node.</p>
<p id="p24298539104313"><a name="p24298539104313"></a><a name="p24298539104313"></a>You can log in to a Master node either using VNC on the ECS management console or using SSH. After logging in to the Master node, you can access Core nodes without entering passwords.</p>
<p id="p11431476162017"><a name="p11431476162017"></a><a name="p11431476162017"></a>The system automatically deploys the Master nodes in active/standby mode and supports the high availability (HA) feature for MRS cluster management. If the active management node fails, the standby management node switches to the active state and takes over services.</p>
<p id="p35774423162017"><a name="p35774423162017"></a><a name="p35774423162017"></a>To determine whether the Master1 node is the active management node, see <a href="viewing-active-and-standby-nodes.md">Viewing Active and Standby Nodes</a>.</p>
</td>
</tr>
<tr id="row62845463183740"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p57317738183740"><a name="p57317738183740"></a><a name="p57317738183740"></a>Core node</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p12225210183740"><a name="p12225210183740"></a><a name="p12225210183740"></a><span>Working node of an MRS cluster. It processes and analyzes data and stores process data on HDFS.</span></p>
</td>
</tr>
</tbody>
</table>

