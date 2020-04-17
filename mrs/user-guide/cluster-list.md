# Cluster List<a name="EN-US_TOPIC_0125375384"></a>

The cluster list contains all clusters in MRS. You can view clusters in various states. If a large number of clusters are involved, navigate through multiple pages to view all of the clusters.

MRS, as a platform managing and analyzing massive data, provides a PB-level data processing capability. Multiple clusters can be created. The cluster quantity is subject to the ECS quantity.

## Active Cluster<a name="section54595606153022"></a>

Clusters are listed in chronological order by default in the cluster list, with the most recent cluster displayed at the top.  [Table 1](#table3950169215120)  describes parameters of the cluster list.

-   Active Clusters: contains all clusters except the clusters in the  **Failed** or **Terminated**  state.
-   Failed Tasks: contains only the tasks in the  **Failed**  state. Task failures include:
    -   Cluster creation failure
    -   Cluster termination failure
    -   Cluster capacity expansion failure
    -   Cluster capacity shrink failure


**Table  1**  Parameters in the active cluster list

<a name="table3950169215120"></a>
<table><thead align="left"><tr id="row2555468715120"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p4021197415120"><a name="p4021197415120"></a><a name="p4021197415120"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p3594448915120"><a name="p3594448915120"></a><a name="p3594448915120"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5506494715120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3107569315120"><a name="p3107569315120"></a><a name="p3107569315120"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3410318715120"><a name="p3410318715120"></a><a name="p3410318715120"></a>Cluster name, which is set when a cluster is created.</p>
</td>
</tr>
<tr id="row3849323515120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3094432715120"><a name="p3094432715120"></a><a name="p3094432715120"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2346258815120"><a name="p2346258815120"></a><a name="p2346258815120"></a>Unique identifier of a cluster, which is automatically assigned when a cluster is created.</p>
</td>
</tr>
<tr id="row983670615120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p5857575515120"><a name="p5857575515120"></a><a name="p5857575515120"></a>Nodes</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4701572015120"><a name="p4701572015120"></a><a name="p4701572015120"></a>Number of nodes that can be deployed in a cluster. This parameter is set when a cluster is created.</p>
<div class="note" id="note6501898815365"><a name="note6501898815365"></a><a name="note6501898815365"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4829998515365"><a name="p4829998515365"></a><a name="p4829998515365"></a>A small value may cause slow cluster running. Properly set a value based on data to be processed.</p>
</div></div>
</td>
</tr>
<tr id="row2048830215120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4893976515120"><a name="p4893976515120"></a><a name="p4893976515120"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p469802015120"><a name="p469802015120"></a><a name="p469802015120"></a>Status and operation progress description of a cluster.</p>
<div class="p" id="p45743426144251"><a name="p45743426144251"></a><a name="p45743426144251"></a>The cluster creation progress includes:<a name="ul32079651144736"></a><a name="ul32079651144736"></a><ul id="ul32079651144736"><li>Verifying cluster parameters</li><li>Applying for cluster resources</li><li>Creating VM</li><li>Initializing VM</li><li>Installing MRS Manager</li><li>Deploying cluster</li><li>Cluster installation failed</li></ul>
</div>
<div class="p" id="p14934120144251"><a name="p14934120144251"></a><a name="p14934120144251"></a>The cluster expansion progress includes:<a name="ul28347778144637"></a><a name="ul28347778144637"></a><ul id="ul28347778144637"><li>Preparing for cluster expansion</li><li>Creating VM</li><li>Initializing VM</li><li>Adding node to the cluster</li><li>Cluster expansion failed</li></ul>
</div>
<div class="p" id="p34508913144251"><a name="p34508913144251"></a><a name="p34508913144251"></a>The cluster shrink progress includes:<a name="ul6362098144647"></a><a name="ul6362098144647"></a><ul id="ul6362098144647"><li>Preparing for cluster shrink</li><li>Decommissioning instance</li><li>Deleting VM</li><li>Deleting node from the cluster</li><li>Cluster shrink failed</li></ul>
</div>
<p id="p3115026214200"><a name="p3115026214200"></a><a name="p3115026214200"></a>It displays causes of cluster installation, expansion, and shrink failures. For details, see <a href="creating-a-cluster.md#table41545811153550">Table 7</a>.</p>
</td>
</tr>
<tr id="row4228218715120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p230509815120"><a name="p230509815120"></a><a name="p230509815120"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5249523815120"><a name="p5249523815120"></a><a name="p5249523815120"></a>Time when MRS starts charging MRS clusters of the customer.</p>
</td>
</tr>
<tr id="row2749009915120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1210558515120"><a name="p1210558515120"></a><a name="p1210558515120"></a>AZ</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4102833915120"><a name="p4102833915120"></a><a name="p4102833915120"></a>An availability zone of the working zone in the cluster, which is set when a cluster is created.</p>
</td>
</tr>
<tr id="row1662880815250"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p475621615250"><a name="p475621615250"></a><a name="p475621615250"></a>Operation</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5314123011558"><a name="p5314123011558"></a><a name="p5314123011558"></a>Terminate: If you want to terminate a cluster after jobs are complete, click <span class="uicontrol" id="uicontrol6655990592844"><a name="uicontrol6655990592844"></a><a name="uicontrol6655990592844"></a><b>Terminate</b></span>. The cluster status changes from&nbsp;<span class="parmvalue" id="parmvalue6525274192844"><a name="parmvalue6525274192844"></a><a name="parmvalue6525274192844"></a><b>Running</b></span>&nbsp;to&nbsp;<span class="parmvalue" id="parmvalue40357961112958"><a name="parmvalue40357961112958"></a><a name="parmvalue40357961112958"></a><b>Terminating</b></span>. After the cluster is terminated, the cluster status will change to&nbsp;<span class="parmvalue" id="parmvalue3579548692844"><a name="parmvalue3579548692844"></a><a name="parmvalue3579548692844"></a><b>Terminated</b></span>&nbsp;and will be displayed in&nbsp;<span class="parmname" id="parmname8754458144114"><a name="parmname8754458144114"></a><a name="parmname8754458144114"></a><b>Cluster&nbsp;History</b></span>. If the MRS cluster fails to be deployed, the cluster is automatically terminated.</p>
<div class="p" id="p63987746163812"><a name="p63987746163812"></a><a name="p63987746163812"></a>This parameter is displayed in <span class="parmname" id="parmname8489716101159"><a name="parmname8489716101159"></a><a name="parmname8489716101159"></a><b>Active Cluster</b></span> only.<div class="note" id="note28456577111427"><a name="note28456577111427"></a><a name="note28456577111427"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p54782608111427"><a name="p54782608111427"></a><a name="p54782608111427"></a>If a cluster is terminated before data processing and analysis are completed, data loss may occur. Therefore, exercise caution when terminating a cluster.</p>
</div></div>
</div>
</td>
</tr>
</tbody>
</table>

**Table  2**  Button description

<a name="table14995478145753"></a>
<table><thead align="left"><tr id="row34648328145753"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p25698260145753"><a name="p25698260145753"></a><a name="p25698260145753"></a>Button</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p1184341145753"><a name="p1184341145753"></a><a name="p1184341145753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10659077145753"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p29791436944"><a name="p29791436944"></a><a name="p29791436944"></a><a name="image1395517363416"></a><a name="image1395517363416"></a><span><img id="image1395517363416" src="figures/icon_mrs_cluster_state.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5199799815013"><a name="p5199799815013"></a><a name="p5199799815013"></a>In the drop-down list, select a state to filter clusters:</p>
<a name="ul6532879915013"></a><a name="ul6532879915013"></a><ul id="ul6532879915013"><li>Active Cluster<a name="ul6709732015416"></a><a name="ul6709732015416"></a><ul id="ul6709732015416"><li>All (<em id="i5714138415013"><a name="i5714138415013"></a><a name="i5714138415013"></a>Num</em>): displays all existing clusters.</li><li>Starting (<em id="i6504936115013"><a name="i6504936115013"></a><a name="i6504936115013"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue47203909151430"><a name="parmvalue47203909151430"></a><a name="parmvalue47203909151430"></a><b>Starting</b></span> state.</li><li>Running (<em id="i4453476515152"><a name="i4453476515152"></a><a name="i4453476515152"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue6029771715612"><a name="parmvalue6029771715612"></a><a name="parmvalue6029771715612"></a><b>Running</b></span> state.</li><li>Expanding (<em id="i62390153162921"><a name="i62390153162921"></a><a name="i62390153162921"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue52967420163029"><a name="parmvalue52967420163029"></a><a name="parmvalue52967420163029"></a><b>Expanding</b></span> state.</li><li>Shrinking (<em id="i16957925102714"><a name="i16957925102714"></a><a name="i16957925102714"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue11589919102752"><a name="parmvalue11589919102752"></a><a name="parmvalue11589919102752"></a><b>Shrinking</b></span> state.</li><li>Abnormal (<em id="i455344615013"><a name="i455344615013"></a><a name="i455344615013"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue5559333151610"><a name="parmvalue5559333151610"></a><a name="parmvalue5559333151610"></a><b>Abnormal</b></span> state.</li><li>Terminating (<em id="i4313604715323"><a name="i4313604715323"></a><a name="i4313604715323"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue62334137151614"><a name="parmvalue62334137151614"></a><a name="parmvalue62334137151614"></a><b>Terminating</b></span> state.</li><li>Frozen (<em id="i57797939104143"><a name="i57797939104143"></a><a name="i57797939104143"></a>Num</em>): displays existing clusters in the&nbsp;<span class="parmvalue" id="parmvalue20285493104143"><a name="parmvalue20285493104143"></a><a name="parmvalue20285493104143"></a><b>Frozen</b></span> state.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row6551537320431"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p13010212617"><a name="p13010212617"></a><a name="p13010212617"></a><a name="image11988520068"></a><a name="image11988520068"></a><span><img id="image11988520068" src="figures/icon_mrs_critical.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p42927285203153"><a name="p42927285203153"></a><a name="p42927285203153"></a>Click <a name="image57127449203153"></a><a name="image57127449203153"></a><span><img id="image57127449203153" src="figures/icon_mrs_critical.jpg"></span> to open the page for managing failed task.</p>
<p id="p4630505820431"><a name="p4630505820431"></a><a name="p4630505820431"></a><a name="image9529156202650"></a><a name="image9529156202650"></a><span><img id="image9529156202650" src="figures/icon_mrs_critical.jpg"></span>&nbsp;<em id="i7175372203052"><a name="i7175372203052"></a><a name="i7175372203052"></a>Num</em>: displays the failed tasks in the&nbsp;<span class="parmvalue" id="parmvalue53418218203137"><a name="parmvalue53418218203137"></a><a name="parmvalue53418218203137"></a><b>Failed</b></span> state.</p>
</td>
</tr>
<tr id="row60954660145753"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1487413013161"><a name="p1487413013161"></a><a name="p1487413013161"></a><a name="image58611001162"></a><a name="image58611001162"></a><span><img id="image58611001162" src="figures/icon_mrs_search_l.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2095556215013"><a name="p2095556215013"></a><a name="p2095556215013"></a>Enter a cluster name in the search bar and click <a name="image56757458143417"></a><a name="image56757458143417"></a><span><img id="image56757458143417" src="figures/icon_mrs_search_l.png"></span> to search for a cluster.</p>
</td>
</tr>
<tr id="row62041377145753"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p14105111091817"><a name="p14105111091817"></a><a name="p14105111091817"></a><a name="image11931102184"></a><a name="image11931102184"></a><span><img id="image11931102184" src="figures/icon_mrs_fresh_r.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3196483515013"><a name="p3196483515013"></a><a name="p3196483515013"></a>Click <a name="image25452204143458"></a><a name="image25452204143458"></a><span><img id="image25452204143458" src="figures/icon_mrs_fresh_r.png"></span> to manually refresh the cluster list.</p>
</td>
</tr>
</tbody>
</table>

## Cluster History<a name="section24332599153050"></a>

Historical Cluster: contains only the clusters in the  **Failed** or **Terminated**  state. Only clusters terminated within the last six months are displayed. If you want to view clusters terminated six months ago, contact technical support engineers.

**Table  3**  Parameters in the historical cluster list

<a name="table17652784164645"></a>
<table><thead align="left"><tr id="row64139603164645"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p27925330164645"><a name="p27925330164645"></a><a name="p27925330164645"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p47359246164645"><a name="p47359246164645"></a><a name="p47359246164645"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10893678164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p9972698164645"><a name="p9972698164645"></a><a name="p9972698164645"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2482235164645"><a name="p2482235164645"></a><a name="p2482235164645"></a>Cluster name, which is set when a cluster is created.</p>
</td>
</tr>
<tr id="row43848941164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p62103341164645"><a name="p62103341164645"></a><a name="p62103341164645"></a>Nodes</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p64314705164645"><a name="p64314705164645"></a><a name="p64314705164645"></a>Number of nodes that can be deployed in a cluster. This parameter is set when a cluster is created.</p>
<div class="note" id="note41961436164645"><a name="note41961436164645"></a><a name="note41961436164645"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p42108610164645"><a name="p42108610164645"></a><a name="p42108610164645"></a>A small value may cause slow cluster running. Properly set a value based on data to be processed.</p>
</div></div>
</td>
</tr>
<tr id="row55354215164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p54506408164645"><a name="p54506408164645"></a><a name="p54506408164645"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p52942959164645"><a name="p52942959164645"></a><a name="p52942959164645"></a>Status of a cluster</p>
</td>
</tr>
<tr id="row6724583164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p7820335164645"><a name="p7820335164645"></a><a name="p7820335164645"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p29467375164645"><a name="p29467375164645"></a><a name="p29467375164645"></a>Time when MRS starts charging MRS clusters of the customer.</p>
</td>
</tr>
<tr id="row63879788164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6880340164645"><a name="p6880340164645"></a><a name="p6880340164645"></a>Terminated</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p20436681164645"><a name="p20436681164645"></a><a name="p20436681164645"></a>Termination time of a cluster, that is, time when charging for the cluster stops. This parameter is displayed in <span class="parmname" id="parmname16171627104220"><a name="parmname16171627104220"></a><a name="parmname16171627104220"></a><b>Cluster&nbsp;History</b></span> only.</p>
</td>
</tr>
<tr id="row60459796164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p65405312164645"><a name="p65405312164645"></a><a name="p65405312164645"></a>AZ</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p63338916164645"><a name="p63338916164645"></a><a name="p63338916164645"></a>An availability zone of the working zone in the cluster, which is set when a cluster is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Button description

<a name="table60068939164645"></a>
<table><thead align="left"><tr id="row14387112164645"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p24505462164645"><a name="p24505462164645"></a><a name="p24505462164645"></a>Button</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p38785416164645"><a name="p38785416164645"></a><a name="p38785416164645"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56571792164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p350121162613"><a name="p350121162613"></a><a name="p350121162613"></a><a name="image184751615264"></a><a name="image184751615264"></a><span><img id="image184751615264" src="figures/icon_mrs_search_l.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p29860423164645"><a name="p29860423164645"></a><a name="p29860423164645"></a>Enter a cluster name in the search bar and click <a name="image12659508143616"></a><a name="image12659508143616"></a><span><img id="image12659508143616" src="figures/icon_mrs_search_l.png"></span> to search for a cluster.</p>
</td>
</tr>
<tr id="row2775207164645"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p19480111162110"><a name="p19480111162110"></a><a name="p19480111162110"></a><a name="image1846851182111"></a><a name="image1846851182111"></a><span><img id="image1846851182111" src="figures/icon_mrs_fresh_r.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p60475996164645"><a name="p60475996164645"></a><a name="p60475996164645"></a>Click <a name="image50505335143542"></a><a name="image50505335143542"></a><span><img id="image50505335143542" src="figures/icon_mrs_fresh_r.png"></span> to manually refresh the cluster list.</p>
</td>
</tr>
</tbody>
</table>

