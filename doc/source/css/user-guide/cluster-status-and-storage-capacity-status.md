# Cluster Status and Storage Capacity Status<a name="css_01_0053"></a>

On the  **Dashboard**  page of the CSS management console, you can view information about the status and storage capacity status of existing clusters.

**Table  1**  Cluster status description

<a name="table17964125910288"></a>
<table><thead align="left"><tr id="row69651559162818"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p99651459142815"><a name="p99651459142815"></a><a name="p99651459142815"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p18965105916281"><a name="p18965105916281"></a><a name="p18965105916281"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17965105972814"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p20965205918287"><a name="p20965205918287"></a><a name="p20965205918287"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p880114324315"><a name="p880114324315"></a><a name="p880114324315"></a>Indicates that the cluster is running properly and provides services for users.</p>
</td>
</tr>
<tr id="row492694223914"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p664519463399"><a name="p664519463399"></a><a name="p664519463399"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p106451546173910"><a name="p106451546173910"></a><a name="p106451546173910"></a>Indicates that cluster creation failed or the cluster is unavailable.</p>
<p id="p73354923710"><a name="p73354923710"></a><a name="p73354923710"></a>If a cluster is in the <span class="parmname" id="parmname1011512339487"><a name="parmname1011512339487"></a><a name="parmname1011512339487"></a><b>Unavailable</b></span> state, the cluster can be deleted or snapshots of the cluster can be restored to other clusters. However, operations such as expanding cluster capacity, accessing Kibana, creating snapshots, and restoring snapshots to the cluster are not allowed. Data importing is not recommended to avoid data loss. You can view the cluster metrics or restart the cluster. However, the operations may fail because of cluster faults. If the operations fail, contact the customer service personnel in a timely manner.</p>
</td>
</tr>
<tr id="row19965105914284"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p996515942812"><a name="p996515942812"></a><a name="p996515942812"></a>Processing</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p79661859162818"><a name="p79661859162818"></a><a name="p79661859162818"></a>Indicates that the cluster is in the middle of a restart, expansion, backup, or recovery.</p>
</td>
</tr>
<tr id="row3968103032413"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p096853010241"><a name="p096853010241"></a><a name="p096853010241"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p296893019243"><a name="p296893019243"></a><a name="p296893019243"></a>Indicates that a cluster is being created.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Cluster storage capacity status description

<a name="table10563055122911"></a>
<table><thead align="left"><tr id="row125631055152913"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p05632554295"><a name="p05632554295"></a><a name="p05632554295"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p14563255182920"><a name="p14563255182920"></a><a name="p14563255182920"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11563105582912"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p25631855102912"><a name="p25631855102912"></a><a name="p25631855102912"></a>Idle</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p1156318559293"><a name="p1156318559293"></a><a name="p1156318559293"></a>Indicates that the storage capacity usage of all nodes in a cluster is less than 50%.</p>
</td>
</tr>
<tr id="row12563135512919"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p12563185522910"><a name="p12563185522910"></a><a name="p12563185522910"></a>Warning</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p556314552298"><a name="p556314552298"></a><a name="p556314552298"></a>Indicates that the storage capacity usage of any node in a cluster is from 50% to less than 80%.</p>
</td>
</tr>
<tr id="row115631755142919"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6563125516293"><a name="p6563125516293"></a><a name="p6563125516293"></a>Danger</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p195641554291"><a name="p195641554291"></a><a name="p195641554291"></a>Indicates that the storage capacity usage of any node in a cluster is greater than or equal to 80%. You are advised to increase the storage space of the cluster to achieve normal data search or analysis.</p>
</td>
</tr>
<tr id="row1564855142918"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p55642554298"><a name="p55642554298"></a><a name="p55642554298"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p95642553294"><a name="p95642553294"></a><a name="p95642553294"></a>Indicates that the cluster storage capacity usage is unknown. For example, if the status of a cluster is <span class="parmname"><b>Abnormal</b></span> due to faults, the storage space status of the cluster is <span class="parmname"><b>Abnormal</b></span>.</p>
</td>
</tr>
</tbody>
</table>

