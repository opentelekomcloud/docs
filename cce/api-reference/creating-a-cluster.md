# Creating a Cluster<a name="cce_02_0236"></a>

## Function<a name="section1686113493165"></a>

This API is used to create an empty cluster, which has only master nodes but do not have worker nodes. After creating a cluster by calling this API, you can add nodes to the cluster. For details, see  [Creating a Node](creating-a-node.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   By default, info collect agent \(ICAgent\) is not installed for the cluster created by this API. ICAgent is an O&M data collection agent used by Application Performance Management \(APM\) service. It runs on each server to collect data from probes in real time. ICAgent is the prerequisite for achieving application O&M. If ICAgent is not installed, the application O&M functions cannot be used.  
>-   Before creating a cluster,  [Creating a VPC and Subnet](creating-a-vpc-and-subnet.md). If a VPC and subnet already exists, you do not need to create them again.  
>-   By default, an account can create a maximum of five clusters in each region.  

## URI<a name="section8403243161416"></a>

POST /api/v3/projects/\{project\_id\}/clusters

[Table 1](#table2027961241820)  describes the parameters of this API.

**Table  1**  Parameters

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p1320413331216"><a name="p1320413331216"></a><a name="p1320413331216"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table165001054142614)  and  [Table 3](#table34052983203655)  describe the request parameters.

**Table  2**  Parameters in the request header

<a name="table165001054142614"></a>
<table><thead align="left"><tr id="row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p115009545264"><a name="p115009545264"></a><a name="p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p175001547265"><a name="p175001547265"></a><a name="p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="p16500154162611"><a name="p16500154162611"></a><a name="p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p69808112344"><a name="p69808112344"></a><a name="p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p3980111103414"><a name="p3980111103414"></a><a name="p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p169801011203416"><a name="p169801011203416"></a><a name="p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="ul7385444163617"></a><a name="ul7385444163617"></a><ul id="ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p105001654202618"><a name="p105001654202618"></a><a name="p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p20500954182618"><a name="p20500954182618"></a><a name="p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p18824197845"><a name="p18824197845"></a><a name="p18824197845"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameters in the request body

<a name="table34052983203655"></a>
<table><thead align="left"><tr id="row30254333203655"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p34681881203655"><a name="p34681881203655"></a><a name="p34681881203655"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p333122111014"><a name="p333122111014"></a><a name="p333122111014"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p57769002203655"><a name="p57769002203655"></a><a name="p57769002203655"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p58673482203655"><a name="p58673482203655"></a><a name="p58673482203655"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54931625203655"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p44731858185518"><a name="p44731858185518"></a><a name="p44731858185518"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p20715132635516"><a name="p20715132635516"></a><a name="p20715132635516"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p57145269553"><a name="p57145269553"></a><a name="p57145269553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. For a cluster management API, the parameter must be set to <strong id="b8304143918315"><a name="b8304143918315"></a><a name="b8304143918315"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row15234185203655"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p2709192613559"><a name="p2709192613559"></a><a name="p2709192613559"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b95215361854"><a name="b95215361854"></a><a name="b95215361854"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1122635417553"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p144741558135518"><a name="p144741558135518"></a><a name="p144741558135518"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p112261154155517"><a name="p112261154155517"></a><a name="p112261154155517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p16227554165511"><a name="p16227554165511"></a><a name="p16227554165511"></a><a href="#table888212551117">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p102271654195515"><a name="p102271654195515"></a><a name="p102271654195515"></a>Basic information about a cluster. metadata is a collection of attributes.</p>
</td>
</tr>
<tr id="row9619511127"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4785161212"><a name="p4785161212"></a><a name="p4785161212"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p97205171219"><a name="p97205171219"></a><a name="p97205171219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p67105119126"><a name="p67105119126"></a><a name="p67105119126"></a><a href="#table1034041612134">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p10785112129"><a name="p10785112129"></a><a name="p10785112129"></a>Detailed description of the cluster to be created. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **metadata**  field

<a name="table888212551117"></a>
<table><thead align="left"><tr id="row18888115514119"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p11890655514"><a name="p11890655514"></a><a name="p11890655514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p289311553114"><a name="p289311553114"></a><a name="p289311553114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p128941055417"><a name="p128941055417"></a><a name="p128941055417"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p1289615519119"><a name="p1289615519119"></a><a name="p1289615519119"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1489715551111"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1289114562017"><a name="p1289114562017"></a><a name="p1289114562017"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p716614322018"><a name="p716614322018"></a><a name="p716614322018"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p9195144141410"><a name="p9195144141410"></a><a name="p9195144141410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1630772215148"><a name="p1630772215148"></a><a name="p1630772215148"></a>Cluster name.</p>
<p id="p9110173318412"><a name="p9110173318412"></a><a name="p9110173318412"></a>Enter 4 to 128 characters starting with a letter and not ending with a hyphen (-). Only lowercase letters, digits, and hyphens (-) are allowed.</p>
</td>
</tr>
<tr id="row6865639152015"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p689194513209"><a name="p689194513209"></a><a name="p689194513209"></a>labels</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1886511394203"><a name="p1886511394203"></a><a name="p1886511394203"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p919624191418"><a name="p919624191418"></a><a name="p919624191418"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1831411614564"><a name="p1831411614564"></a><a name="p1831411614564"></a>Cluster labels in the format of key-value pairs.</p>
<p id="p1671617184505"><a name="p1671617184505"></a><a name="p1671617184505"></a>Labels are used to select objects that meet certain criteria.</p>
<p id="p93074221142"><a name="p93074221142"></a><a name="p93074221142"></a>Example:</p>
<pre class="screen" id="screen38331124185416"><a name="screen38331124185416"></a><a name="screen38331124185416"></a>"labels": {
  "key" : "value"
}</pre>
</td>
</tr>
<tr id="row1267164013200"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p889194582016"><a name="p889194582016"></a><a name="p889194582016"></a>annotations</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p116764015202"><a name="p116764015202"></a><a name="p116764015202"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p15196841191420"><a name="p15196841191420"></a><a name="p15196841191420"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p13308162211145"><a name="p13308162211145"></a><a name="p13308162211145"></a>Cluster annotations in the format of key-value pairs.</p>
<pre class="screen" id="screen1163751913466"><a name="screen1163751913466"></a><a name="screen1163751913466"></a>"annotations": {
  "key1" : "value1",
  "key2" : "value2"
}</pre>
<div class="note" id="note1558316436525"><a name="note1558316436525"></a><a name="note1558316436525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p258444365217"><a name="p258444365217"></a><a name="p258444365217"></a>Annotations are not used to identify or select objects. The metadata in Annotations may be small or large, structured or unstructured, and may include characters that are not allowed in labels.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **spec**  field

<a name="table1034041612134"></a>
<table><thead align="left"><tr id="row14348121616132"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p133505167139"><a name="p133505167139"></a><a name="p133505167139"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p6353201611319"><a name="p6353201611319"></a><a name="p6353201611319"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.353535353535353%" id="mcps1.2.5.1.3"><p id="p735501615139"><a name="p735501615139"></a><a name="p735501615139"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.313131313131315%" id="mcps1.2.5.1.4"><p id="p15357151631311"><a name="p15357151631311"></a><a name="p15357151631311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row178365271483"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p146521540191916"><a name="p146521540191916"></a><a name="p146521540191916"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p202632127"><a name="p202632127"></a><a name="p202632127"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p1052510179227"><a name="p1052510179227"></a><a name="p1052510179227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p1691385774411"><a name="p1691385774411"></a><a name="p1691385774411"></a>Cluster type. Possible values:</p>
<a name="ul123801520452"></a><a name="ul123801520452"></a><ul id="ul123801520452"><li><strong id="b122221723185118"><a name="b122221723185118"></a><a name="b122221723185118"></a>VirtualMachine</strong>: The cluster is a hybrid cluster.<p id="p138192583535"><a name="p138192583535"></a><a name="p138192583535"></a>A hybrid cluster manages a group of node resources based on Kubernetes. It can manage VMs, physical machines (PMs), or a combination of both. Kubernetes automatically schedules containers onto available nodes. Before creating a containerized workload, ensure that a cluster is available.</p>
</li><li><strong id="b2026825310204"><a name="b2026825310204"></a><a name="b2026825310204"></a>BareMetal</strong>: The cluster is a BMS cluster.<p id="p13891132020474"><a name="p13891132020474"></a><a name="p13891132020474"></a>BMS clusters are Kubernetes container clusters with high computing and high network performance. To use a BMS cluster, <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053536894.html" target="_blank" rel="noopener noreferrer">apply for a BMS</a>. To provide a high-speed container network, add a high-speed network interface card (NIC) when creating a BMS. For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053537013.html" target="_blank" rel="noopener noreferrer">Managing High-Speed Networks</a>.</p>
</li></ul>
</td>
</tr>
<tr id="row111221127144415"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1612362713448"><a name="p1612362713448"></a><a name="p1612362713448"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p1112372718448"><a name="p1112372718448"></a><a name="p1112372718448"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p1512392713442"><a name="p1512392713442"></a><a name="p1512392713442"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p16621941104417"><a name="p16621941104417"></a><a name="p16621941104417"></a>Cluster flavor, which cannot be changed after the cluster is created.</p>
<a name="ul154851748174415"></a><a name="ul154851748174415"></a><ul id="ul154851748174415"><li><strong id="b11489836273"><a name="b11489836273"></a><a name="b11489836273"></a>cce.s1.small</strong>: small-scale, single-master VM cluster (≤ 50 nodes)</li><li><strong id="b367910942720"><a name="b367910942720"></a><a name="b367910942720"></a>cce.s1.medium</strong>: medium-scale, single-master VM cluster (≤ 200 nodes)</li><li><strong id="b6271153114279"><a name="b6271153114279"></a><a name="b6271153114279"></a>cce.s1.large</strong>: large-scale, single-master VM cluster (≤ 1,000 nodes)</li><li><strong id="b181461333281"><a name="b181461333281"></a><a name="b181461333281"></a>cce.t1.small</strong>: small-scale, single-master BMS cluster (≤ 10 nodes)</li><li><strong id="b1961019276282"><a name="b1961019276282"></a><a name="b1961019276282"></a>cce.t1.medium</strong>: medium-scale, single-master BMS cluster (≤ 100 nodes)</li><li><strong id="b3357144892811"><a name="b3357144892811"></a><a name="b3357144892811"></a>cce.t1.large</strong>: large-scale, single-master BMS cluster (≤ 500 nodes)</li><li><strong id="b1081317262919"><a name="b1081317262919"></a><a name="b1081317262919"></a>cce.s2.small</strong>: small-scale, high availability VM cluster (≤ 50 nodes)</li><li><strong id="b1689322115296"><a name="b1689322115296"></a><a name="b1689322115296"></a>cce.s2.medium</strong>: medium-scale, high availability VM cluster (≤ 200 nodes)</li><li><strong id="b57413316296"><a name="b57413316296"></a><a name="b57413316296"></a>cce.s2.large</strong>: large-scale, high availability VM cluster (≤ 1,000 nodes)</li><li><strong id="b12121245192917"><a name="b12121245192917"></a><a name="b12121245192917"></a>cce.t2.small</strong>: small-scale, high availability BMS cluster (≤ 10 nodes)</li><li><strong id="b01951338302"><a name="b01951338302"></a><a name="b01951338302"></a>cce.t2.medium</strong>: medium-scale, high availability BMS cluster (≤ 100 nodes)</li><li><strong id="b198171213303"><a name="b198171213303"></a><a name="b198171213303"></a>cce.t2.large</strong>: large-scale, high availability BMS cluster (≤ 500 nodes)</li></ul>
<div class="note" id="note10821115618447"><a name="note10821115618447"></a><a name="note10821115618447"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul13821356164415"></a><a name="ul13821356164415"></a><ul id="ul13821356164415"><li>s1: single-master VM cluster</li><li>s2: high availability VM cluster</li><li>t1: single-master BMS cluster</li><li>t2: high-availability BMS cluster</li><li>For example, <strong id="b1251010481560"><a name="b1251010481560"></a><a name="b1251010481560"></a>≤ 50 nodes</strong> indicates that the maximum number of nodes that can be managed by the cluster is 50.</li><li>A single-master cluster has only one master node. If the master node is down, the cluster will become unavailable and stop serving new workloads. However, existing workloads in the cluster are not affected.</li><li>A high-availability cluster has multiple master nodes. Faults in a single master node will not take the cluster down.</li></ul>
</div></div>
</td>
</tr>
<tr id="row83711516191317"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1565217404195"><a name="p1565217404195"></a><a name="p1565217404195"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p43761516111313"><a name="p43761516111313"></a><a name="p43761516111313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p252511174227"><a name="p252511174227"></a><a name="p252511174227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p0929195015409"><a name="p0929195015409"></a><a name="p0929195015409"></a>Cluster's baseline Kubernetes version. The latest version is recommended.</p>
<div class="note" id="note19341279382"><a name="note19341279382"></a><a name="note19341279382"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1993516279385"><a name="p1993516279385"></a><a name="p1993516279385"></a>If this parameter is not set, the cluster of the latest version is created by default.</p>
</div></div>
</td>
</tr>
<tr id="row438141651319"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1653144010196"><a name="p1653144010196"></a><a name="p1653144010196"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p9485133718193"><a name="p9485133718193"></a><a name="p9485133718193"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p65261417142217"><a name="p65261417142217"></a><a name="p65261417142217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p1318113472302"><a name="p1318113472302"></a><a name="p1318113472302"></a>Cluster description, for example, which purpose the cluster is intended to serve. By default, this parameter is left unspecified. To modify cluster description after the cluster is created, call the <a href="updating-a-specified-cluster.md">API that is used to update information about a specified cluster</a> or go to the cluster details page on the CCE console.</p>
</td>
</tr>
<tr id="row17011947507"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4701194125011"><a name="p4701194125011"></a><a name="p4701194125011"></a>hostNetwok</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p1570134145017"><a name="p1570134145017"></a><a name="p1570134145017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p167012042507"><a name="p167012042507"></a><a name="p167012042507"></a><a href="#table1622013552507">hostNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p123281848104313"><a name="p123281848104313"></a><a name="p123281848104313"></a>Node network parameters, including a VPC and subnet ID. <strong id="b13136114517294"><a name="b13136114517294"></a><a name="b13136114517294"></a>hostNetwok</strong> is mandatory because nodes in a cluster communicate with each other by using a VPC.</p>
</td>
</tr>
<tr id="row651719205217"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p851151955212"><a name="p851151955212"></a><a name="p851151955212"></a>containerNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p11511019115210"><a name="p11511019115210"></a><a name="p11511019115210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p7514193520"><a name="p7514193520"></a><a name="p7514193520"></a><a href="#table882310145412">containerNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p16930187201117"><a name="p16930187201117"></a><a name="p16930187201117"></a>Container network parameters, including a container network model and container CIDR block.</p>
</td>
</tr>
<tr id="row9493123913567"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2493239145620"><a name="p2493239145620"></a><a name="p2493239145620"></a><span>authentication</span></p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p2493123917565"><a name="p2493123917565"></a><a name="p2493123917565"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p6493113918562"><a name="p6493113918562"></a><a name="p6493113918562"></a><a href="#table71529332533">authentication</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p14939395566"><a name="p14939395566"></a><a name="p14939395566"></a>Configurations of the cluster authentication mode.</p>
</td>
</tr>
<tr id="row97803915130"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p156284113136"><a name="p156284113136"></a><a name="p156284113136"></a>kubernetesSvcIpRange</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p8782169151311"><a name="p8782169151311"></a><a name="p8782169151311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p0703163016251"><a name="p0703163016251"></a><a name="p0703163016251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p7782199181315"><a name="p7782199181315"></a><a name="p7782199181315"></a>Service CIDR block or the IP address range which the <strong id="b1853831421311"><a name="b1853831421311"></a><a name="b1853831421311"></a>kubernetes clusterIp</strong> must fall within. This parameter is available only for clusters of v1.11.7 and later.</p>
</td>
</tr>
<tr id="row10323532155414"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p14324183215541"><a name="p14324183215541"></a><a name="p14324183215541"></a>kubeProxyMode</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p9324183255411"><a name="p9324183255411"></a><a name="p9324183255411"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p232415326549"><a name="p232415326549"></a><a name="p232415326549"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p113568261434"><a name="p113568261434"></a><a name="p113568261434"></a>Service forwarding mode. Two modes are available:</p>
<a name="ul1435618265318"></a><a name="ul1435618265318"></a><ul id="ul1435618265318"><li><strong id="b106749431705"><a name="b106749431705"></a><a name="b106749431705"></a>iptables</strong>: Traditional kube-proxy uses iptables rules to implement service load balancing. In this mode, too many iptables rules will be generated when many services are deployed. In addition, non-incremental updates will cause a latency and even obvious performance issues in the case of heavy service traffic.</li><li><strong id="b17542918173615"><a name="b17542918173615"></a><a name="b17542918173615"></a>ipvs</strong>: Optimized kube-proxy mode with higher throughput and faster speed. This mode supports incremental updates and can keep connections uninterrupted during service updates. It is suitable for large-sized clusters.</li></ul>
</td>
</tr>
<tr id="row1441131711197"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p6345128161614"><a name="p6345128161614"></a><a name="p6345128161614"></a>billingMode</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p183451883168"><a name="p183451883168"></a><a name="p183451883168"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p734518141613"><a name="p734518141613"></a><a name="p734518141613"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p1834638101617"><a name="p1834638101617"></a><a name="p1834638101617"></a>Billing mode of a node.</p>
<div class="note" id="note0702131124412"><a name="note0702131124412"></a><a name="note0702131124412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p77026184417"><a name="p77026184417"></a><a name="p77026184417"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row1384175110463"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p484119516469"><a name="p484119516469"></a><a name="p484119516469"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p084112512463"><a name="p084112512463"></a><a name="p084112512463"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.353535353535353%" headers="mcps1.2.5.1.3 "><p id="p19841451184614"><a name="p19841451184614"></a><a name="p19841451184614"></a><a href="#table17575013586">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.313131313131315%" headers="mcps1.2.5.1.4 "><p id="p13817123194716"><a name="p13817123194716"></a><a name="p13817123194716"></a>Extended fields in the format of key-value pairs.</p>
<p id="p128174394710"><a name="p128174394710"></a><a name="p128174394710"></a>If the cluster will span across AZs or belong to a specified enterprise project, set extended fields as described in <a href="#table17575013586">Table 10</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the  **hostNetwork**  field

<a name="table1622013552507"></a>
<table><thead align="left"><tr id="row922065525010"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p687613311518"><a name="p687613311518"></a><a name="p687613311518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p589116375111"><a name="p589116375111"></a><a name="p589116375111"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p168912031515"><a name="p168912031515"></a><a name="p168912031515"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="p158914355111"><a name="p158914355111"></a><a name="p158914355111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1622075519505"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1465319402192"><a name="p1465319402192"></a><a name="p1465319402192"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p12810837131913"><a name="p12810837131913"></a><a name="p12810837131913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p1452691718229"><a name="p1452691718229"></a><a name="p1452691718229"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p2018164753013"><a name="p2018164753013"></a><a name="p2018164753013"></a>ID of the VPC used to create a master node. The VPC ID is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row322025520508"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1665317409195"><a name="p1665317409195"></a><a name="p1665317409195"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p103711385193"><a name="p103711385193"></a><a name="p103711385193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p185261417112213"><a name="p185261417112213"></a><a name="p185261417112213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p111816472307"><a name="p111816472307"></a><a name="p111816472307"></a>Network ID of the subnet. The value is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row10220125555018"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p46541240151913"><a name="p46541240151913"></a><a name="p46541240151913"></a>highwaySubnet</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p11229838171913"><a name="p11229838171913"></a><a name="p11229838171913"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p1752614175225"><a name="p1752614175225"></a><a name="p1752614175225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p15181134718309"><a name="p15181134718309"></a><a name="p15181134718309"></a>ID of the high-speed network that is used to create a BMS node. The value is obtained from <a href="(optional)-creating-a-high-speed-network.md">(Optional) Creating a High-Speed Network</a>. This parameter is required for creating a BMS cluster.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the  **authentication** field

<a name="table71529332533"></a>
<table><thead align="left"><tr id="row131521433135310"><th class="cellrowborder" valign="top" width="21.29%" id="mcps1.2.5.1.1"><p id="p16152133325312"><a name="p16152133325312"></a><a name="p16152133325312"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.71%" id="mcps1.2.5.1.2"><p id="p837012427533"><a name="p837012427533"></a><a name="p837012427533"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.36%" id="mcps1.2.5.1.3"><p id="p1215283312531"><a name="p1215283312531"></a><a name="p1215283312531"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.64%" id="mcps1.2.5.1.4"><p id="p51521533135318"><a name="p51521533135318"></a><a name="p51521533135318"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17153133125315"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.5.1.1 "><p id="p415313335535"><a name="p415313335535"></a><a name="p415313335535"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.2 "><p id="p5370942185310"><a name="p5370942185310"></a><a name="p5370942185310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.5.1.3 "><p id="p81531333165318"><a name="p81531333165318"></a><a name="p81531333165318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.64%" headers="mcps1.2.5.1.4 "><p id="p10153113314537"><a name="p10153113314537"></a><a name="p10153113314537"></a>Cluster authentication mode.</p>
<a name="ul3255399454"></a><a name="ul3255399454"></a><ul id="ul3255399454"><li>Clusters of Kubernetes v1.11 and earlier<a name="ul1491611368019"></a><a name="ul1491611368019"></a><ul id="ul1491611368019"><li>Possible values: x509, rbac, and authenticating_proxy</li><li>Default value: x509</li></ul>
</li><li>Clusters of Kubernetes v1.13 and later<a name="ul1469415101216"></a><a name="ul1469415101216"></a><ul id="ul1469415101216"><li>Possible values: rbac and authenticating_proxy</li><li>Default value: rbac</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1790141562916"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.5.1.1 "><p id="p149011915202913"><a name="p149011915202913"></a><a name="p149011915202913"></a>authenticatingProxy</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.2 "><p id="p1290171520290"><a name="p1290171520290"></a><a name="p1290171520290"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.5.1.3 "><p id="p8901161513297"><a name="p8901161513297"></a><a name="p8901161513297"></a><a href="#table17313161473013">authenticatingProxy</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="43.64%" headers="mcps1.2.5.1.4 "><p id="p2901121513292"><a name="p2901121513292"></a><a name="p2901121513292"></a>Configurations of the <strong id="b1076411138231"><a name="b1076411138231"></a><a name="b1076411138231"></a>authenticating_proxy</strong> mode.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the  **authenticatingProxy**  field

<a name="table17313161473013"></a>
<table><thead align="left"><tr id="row1531310142305"><th class="cellrowborder" valign="top" width="25.575757575757574%" id="mcps1.2.4.1.1"><p id="p1931491463016"><a name="p1931491463016"></a><a name="p1931491463016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.87878787878788%" id="mcps1.2.4.1.2"><p id="p0314131443011"><a name="p0314131443011"></a><a name="p0314131443011"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.4.1.3"><p id="p33141014163014"><a name="p33141014163014"></a><a name="p33141014163014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row931417146309"><td class="cellrowborder" valign="top" width="25.575757575757574%" headers="mcps1.2.4.1.1 "><p id="p3314191412304"><a name="p3314191412304"></a><a name="p3314191412304"></a>ca</p>
</td>
<td class="cellrowborder" valign="top" width="19.87878787878788%" headers="mcps1.2.4.1.2 "><p id="p7314151433012"><a name="p7314151433012"></a><a name="p7314151433012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p1931431423013"><a name="p1931431423013"></a><a name="p1931431423013"></a>CA root certificate provided in the <strong id="b331411473019"><a name="b331411473019"></a><a name="b331411473019"></a>authenticating_proxy</strong> mode. The CA root certificate is encoded to the Base64 format.</p>
</td>
</tr>
</tbody>
</table>

**Table  9**  Data structure of the  **containerNetwork**  field

<a name="table882310145412"></a>
<table><thead align="left"><tr id="row1682316016545"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p1694819205543"><a name="p1694819205543"></a><a name="p1694819205543"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p149646206541"><a name="p149646206541"></a><a name="p149646206541"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p11964620145410"><a name="p11964620145410"></a><a name="p11964620145410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p09648200542"><a name="p09648200542"></a><a name="p09648200542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row482317016541"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p2082320195415"><a name="p2082320195415"></a><a name="p2082320195415"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p2082310011547"><a name="p2082310011547"></a><a name="p2082310011547"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p28237014542"><a name="p28237014542"></a><a name="p28237014542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p2398131181613"><a name="p2398131181613"></a><a name="p2398131181613"></a>Container network model. Select one of the following possible values:</p>
<a name="ul1085141916166"></a><a name="ul1085141916166"></a><ul id="ul1085141916166"><li><strong id="b1892704916116"><a name="b1892704916116"></a><a name="b1892704916116"></a>overlay_l2</strong>: an overlay_l2 network built for containers by using OpenVSwitch (OVS).</li><li><strong id="b1514161620019"><a name="b1514161620019"></a><a name="b1514161620019"></a>underlay_ipvlan</strong>: an underlay_l2 network built for BMS nodes by using ipvlan.</li><li><strong id="b15370163183618"><a name="b15370163183618"></a><a name="b15370163183618"></a>vpc-router</strong>: an underlay_l2 network built for containers by using ipvlan and custom VPC routes.</li></ul>
<div class="note" id="note1860516155199"><a name="note1860516155199"></a><a name="note1860516155199"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul21791736131915"></a><a name="ul21791736131915"></a><ul id="ul21791736131915"><li>Tunnel network: Under this model, the container network is an overlay network on top of a VPC network based on the VXLAN technology. VXLAN encapsulates Ethernet packets as UDP packets for tunnel transmission. Though at some cost of performance, the tunnel encapsulation enables higher interoperability and compatibility with advanced features (such as network policy-based isolation), meeting the requirements of most applications.</li><li>VPC network: Routing is implemented within a VPC network according to custom VPC routes. Each node is assigned a CIDR block of a fixed size. vpc-router networks are free of tunnel encapsulation overheads and provide better container network performance than tunnel networks. In addition, as routes to node IP addresses and the containers have been configured on vpc-router, container instances can be directly accessed from outside the cluster.</li></ul>
</div></div>
</td>
</tr>
<tr id="row482313013542"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1982310145419"><a name="p1982310145419"></a><a name="p1982310145419"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p082314014543"><a name="p082314014543"></a><a name="p082314014543"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p19823401545"><a name="p19823401545"></a><a name="p19823401545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p674711410131"><a name="p674711410131"></a><a name="p674711410131"></a>Container CIDR block. Recommended: 10.0.0.0/12-19, 172.16.0.0/16-19, or 192.168.0.0/16-19. If the selected CIDR block conflicts with existing CIDR blocks, the system automatically selects another CIDR block.</p>
<p id="p181514571229"><a name="p181514571229"></a><a name="p181514571229"></a>If the maximum number of pods on a node is 110, each of the recommended container CIDR blocks supports at least 582 nodes. This parameter cannot be modified after the cluster is created. Exercise caution when setting this parameter.</p>
</td>
</tr>
</tbody>
</table>

**Table  10**  Data structure of the  **extendParam**  field

<a name="table17575013586"></a>
<table><thead align="left"><tr id="row51071750155814"><th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.1"><p id="p41071050115816"><a name="p41071050115816"></a><a name="p41071050115816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.73%" id="mcps1.2.5.1.2"><p id="p9808942152218"><a name="p9808942152218"></a><a name="p9808942152218"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.5.1.3"><p id="p1312155019587"><a name="p1312155019587"></a><a name="p1312155019587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.790000000000006%" id="mcps1.2.5.1.4"><p id="p13121155016582"><a name="p13121155016582"></a><a name="p13121155016582"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1457961164816"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p14579101174811"><a name="p14579101174811"></a><a name="p14579101174811"></a>clusterAZ</p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p8809184232210"><a name="p8809184232210"></a><a name="p8809184232210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p205793194812"><a name="p205793194812"></a><a name="p205793194812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p114561146513"><a name="p114561146513"></a><a name="p114561146513"></a>If you want to enable multiple AZs for the cluster, enter {"clusterAZ": "multi_az"}.</p>
<div class="note" id="note193489237289"><a name="note193489237289"></a><a name="note193489237289"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p134992342810"><a name="p134992342810"></a><a name="p134992342810"></a>Only HA clusters support multiple AZs. To be specific, this field can be configured only when the <strong id="b5383153416301"><a name="b5383153416301"></a><a name="b5383153416301"></a>flavor</strong> field in <a href="#table1034041612134">Table 5</a> is set to <strong id="b109089113316"><a name="b109089113316"></a><a name="b109089113316"></a>cce.s2.small</strong>, <strong id="b1695118368313"><a name="b1695118368313"></a><a name="b1695118368313"></a>cce.s2.medium</strong>, <strong id="b6135146133115"><a name="b6135146133115"></a><a name="b6135146133115"></a>cce.s2.large</strong>, <strong id="b1768451113115"><a name="b1768451113115"></a><a name="b1768451113115"></a>cce.t2.small</strong>, <strong id="b1766555113114"><a name="b1766555113114"></a><a name="b1766555113114"></a>cce.t2.medium</strong>, or <strong id="b135489019329"><a name="b135489019329"></a><a name="b135489019329"></a>cce.t2.large</strong>. After multi-AZ deployment is enabled, the three master nodes of the cluster are distributed in different AZs. The cluster remains available even when one of the AZs is down.</p>
</div></div>
</td>
</tr>
<tr id="row15380172523019"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p113811255309"><a name="p113811255309"></a><a name="p113811255309"></a>dssMasterVolumes</p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p080911421227"><a name="p080911421227"></a><a name="p080911421227"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p113813253300"><a name="p113813253300"></a><a name="p113813253300"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1038132513014"><a name="p1038132513014"></a><a name="p1038132513014"></a>Whether the system and data disks of a master node use dedicated distributed storage. If this parameter is omitted or left unspecified, EVS disks are used by default.</p>
</td>
</tr>
<tr id="row2685716193113"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p136861116153119"><a name="p136861116153119"></a><a name="p136861116153119"></a><span id="ph129965585111"><a name="ph129965585111"></a><a name="ph129965585111"></a>clusterExternalIP</span></p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p768621620318"><a name="p768621620318"></a><a name="p768621620318"></a><span id="ph162983218522"><a name="ph162983218522"></a><a name="ph162983218522"></a>No</span></p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p1686191683110"><a name="p1686191683110"></a><a name="p1686191683110"></a><span id="ph1550142365319"><a name="ph1550142365319"></a><a name="ph1550142365319"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1667535984212"><a name="p1667535984212"></a><a name="p1667535984212"></a>EIP used to access the cluster.</p>
</td>
</tr>
<tr id="row2863140104013"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p9864604409"><a name="p9864604409"></a><a name="p9864604409"></a><span id="ph10968151564019"><a name="ph10968151564019"></a><a name="ph10968151564019"></a>alpha.cce/fixPoolMask</span></p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p10864150134011"><a name="p10864150134011"></a><a name="p10864150134011"></a><span id="ph1731053019404"><a name="ph1731053019404"></a><a name="ph1731053019404"></a>No</span></p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p178642084019"><a name="p178642084019"></a><a name="p178642084019"></a><span id="ph146031733184015"><a name="ph146031733184015"></a><a name="ph146031733184015"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p368203111208"><a name="p368203111208"></a><a name="p368203111208"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row20579145174016"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p1157918534017"><a name="p1157918534017"></a><a name="p1157918534017"></a><span id="ph1850612184016"><a name="ph1850612184016"></a><a name="ph1850612184016"></a>kubernetes.io/cpuManagerPolicy</span></p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p105797584015"><a name="p105797584015"></a><a name="p105797584015"></a><span id="ph19912930104016"><a name="ph19912930104016"></a><a name="ph19912930104016"></a>No</span></p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p20579151409"><a name="p20579151409"></a><a name="p20579151409"></a><span id="ph1757513367404"><a name="ph1757513367404"></a><a name="ph1757513367404"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1756334142010"><a name="p1756334142010"></a><a name="p1756334142010"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row816313919408"><td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.1 "><p id="p191639915401"><a name="p191639915401"></a><a name="p191639915401"></a><span id="ph1532562694020"><a name="ph1532562694020"></a><a name="ph1532562694020"></a>upgradefrom</span></p>
</td>
<td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.2.5.1.2 "><p id="p111637994010"><a name="p111637994010"></a><a name="p111637994010"></a><span id="ph25012317405"><a name="ph25012317405"></a><a name="ph25012317405"></a>No</span></p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p1163189174016"><a name="p1163189174016"></a><a name="p1163189174016"></a><span id="ph819020387405"><a name="ph819020387405"></a><a name="ph819020387405"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p7176173622017"><a name="p7176173622017"></a><a name="p7176173622017"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
</tbody>
</table>

**Example Request**

-   Request for creating a hybrid cluster

    ```
    {
        "kind": "Cluster",
        "apiVersion": "v3",
        "metadata": {
            "name": "mycluster",
            "labels": {
                "foo": "bar"
            },
            "annotations": {
                "foo2": "bar2"
            }
        },
        "spec": {
            "type": "VirtualMachine",
            "flavor": "cce.s2.small",
            "version": "v1.15.6-r1",
            "description": "this is a demo cluster",
            "hostNetwork": {
                "vpc": "23d3725f-6ffe-400e-8fb6-b4f9a7b3e8c1",
                "subnet": "c90b3ce5-e1f1-4c87-a006-644d78846438"
            },
            "containerNetwork": {
                "mode": "overlay_l2",
                "cidr": "172.16.0.0/16"
            },
            "authentication": {
                "mode": "rbac",
                "authenticatingProxy": {
                    "ca": "LS0tLS1CRUdJTiBD****8JUSUZJQ0FURS0tLS0t"
                }
            },
            "kubeProxyMode": "iptables",
            "billingMode": 0,
            "extendParam": {
                "clusterAZ": "multi_az"
            }
        }
    }
    ```

-   Request for creating a BMS cluster:

    ```
    {
        "kind":"Cluster",
        "apiVersion":"v3",
        "metadata":{
            "name":"mycluster-baremetal",
            "labels":{
                "foo":"bar"
            },
            "annotations":{
                "foo2":"bar2"
            }
        },
        "spec":{
            "type":"BareMetal",
            "flavor":"cce.t1.small",
            "version":"v1.11.7-r2",
            "description":"this is a demo cluster",
            "hostNetwork":{
                "vpc":"09f9ee41-6a1e-475b-977b-a16adf0b14c5",
                "subnet":"2ca132cd-cddf-4c01-9abc-373610c8d5f6",
                "highwaySubnet":"a95d96e3-1f13-442a-8f06-f9cb4211eaa4"
            },
            "containerNetwork":{
                "mode":"underlay_ipvlan",
                "cidr":"10.1.0.0/16"
            },
            "extendParam":{
                "foo":"bar"
            }
        }
    }
    ```


## Response<a name="section61819725020"></a>

**Response parameters:**

[Table 11](#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242)  describes the response parameters.

**Table  11**  Response parameters

<a name="en-us_topic_0079616779_en-us_topic_0079614912_ref458774242"></a>
<table><thead align="left"><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row38450714"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1654581422214"><a name="p1654581422214"></a><a name="p1654581422214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p125451914132219"><a name="p125451914132219"></a><a name="p125451914132219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row48220637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p108391536181311"><a name="p108391536181311"></a><a name="p108391536181311"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1056311621716"><a name="p1056311621716"></a><a name="p1056311621716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p75781816181715"><a name="p75781816181715"></a><a name="p75781816181715"></a>API type. The value is fixed at <strong id="b11847261531"><a name="b11847261531"></a><a name="b11847261531"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1785493610136"><a name="p1785493610136"></a><a name="p1785493610136"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p757801610179"><a name="p757801610179"></a><a name="p757801610179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12578616151718"><a name="p12578616151718"></a><a name="p12578616151718"></a>API version. The value is fixed at <strong id="b1677919249511"><a name="b1677919249511"></a><a name="b1677919249511"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1185493615135"><a name="p1185493615135"></a><a name="p1185493615135"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1334385071712"><a name="p1334385071712"></a><a name="p1334385071712"></a><a href="#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10343195011177"><a name="p10343195011177"></a><a name="p10343195011177"></a>Cluster metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row125326326151"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6532732161518"><a name="p6532732161518"></a><a name="p6532732161518"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p5359350141715"><a name="p5359350141715"></a><a name="p5359350141715"></a><a href="#table195921039143517">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p173598507179"><a name="p173598507179"></a><a name="p173598507179"></a>Detailed description of the cluster to be created. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row22041436171514"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1920413611513"><a name="p1920413611513"></a><a name="p1920413611513"></a><a href="#table6749834132215">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p9204133661512"><a name="p9204133661512"></a><a name="p9204133661512"></a>Cluster status and jobID of the cluster creation job.</p>
</td>
</tr>
</tbody>
</table>

**Table  12**  Data structure of the  **metadata**  field

<a name="table669019286188"></a>
<table><thead align="left"><tr id="row869032841815"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p196902028151813"><a name="p196902028151813"></a><a name="p196902028151813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p126901728121814"><a name="p126901728121814"></a><a name="p126901728121814"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p1069010288189"><a name="p1069010288189"></a><a name="p1069010288189"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15690328101814"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11771347194"><a name="p11771347194"></a><a name="p11771347194"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p577117401918"><a name="p577117401918"></a><a name="p577117401918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1977117411193"><a name="p1977117411193"></a><a name="p1977117411193"></a>Cluster name.</p>
</td>
</tr>
<tr id="row1169042813188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6786241193"><a name="p6786241193"></a><a name="p6786241193"></a>uid</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p14111627201917"><a name="p14111627201917"></a><a name="p14111627201917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1786447194"><a name="p1786447194"></a><a name="p1786447194"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row1569018282188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16180152612019"><a name="p16180152612019"></a><a name="p16180152612019"></a>creationTimestamp</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p191801726182014"><a name="p191801726182014"></a><a name="p191801726182014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p20180132652013"><a name="p20180132652013"></a><a name="p20180132652013"></a>Time when the cluster was created.</p>
</td>
</tr>
<tr id="row669012861812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6180202692018"><a name="p6180202692018"></a><a name="p6180202692018"></a>updateTimestamp</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p166835167215"><a name="p166835167215"></a><a name="p166835167215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p91641926182011"><a name="p91641926182011"></a><a name="p91641926182011"></a>Time when the cluster was updated.</p>
</td>
</tr>
<tr id="row66901028161820"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1786194191915"><a name="p1786194191915"></a><a name="p1786194191915"></a>labels</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p17401032131916"><a name="p17401032131916"></a><a name="p17401032131916"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1080274161918"><a name="p1080274161918"></a><a name="p1080274161918"></a>Cluster labels in the format of key-value pairs. The response parameter <strong id="b69436271915"><a name="b69436271915"></a><a name="b69436271915"></a>metadata.labels</strong> is the same as the request parameter <strong id="b13546164512918"><a name="b13546164512918"></a><a name="b13546164512918"></a>metadata.labels</strong>.</p>
</td>
</tr>
<tr id="row1269015284182"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1180210415193"><a name="p1180210415193"></a><a name="p1180210415193"></a>annotations</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p14802164201917"><a name="p14802164201917"></a><a name="p14802164201917"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p18181491919"><a name="p18181491919"></a><a name="p18181491919"></a>Cluster annotations in the format of key-value pairs. The response parameter <strong id="b1573820449715"><a name="b1573820449715"></a><a name="b1573820449715"></a>metadata.annotations</strong> is the same as the request parameter <strong id="b2116414121020"><a name="b2116414121020"></a><a name="b2116414121020"></a>metadata.annotations</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  13**  Data structure of the  **spec**  field

<a name="table195921039143517"></a>
<table><thead align="left"><tr id="row1960853920353"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p11624153903519"><a name="p11624153903519"></a><a name="p11624153903519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p11624183910351"><a name="p11624183910351"></a><a name="p11624183910351"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p1962419396356"><a name="p1962419396356"></a><a name="p1962419396356"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7639113912353"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p3639039143513"><a name="p3639039143513"></a><a name="p3639039143513"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p76391539183511"><a name="p76391539183511"></a><a name="p76391539183511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p13501152113195"><a name="p13501152113195"></a><a name="p13501152113195"></a>Cluster type. Possible values:</p>
<a name="ul750132119199"></a><a name="ul750132119199"></a><ul id="ul750132119199"><li><strong id="b161768187422"><a name="b161768187422"></a><a name="b161768187422"></a>VirtualMachine</strong>: The cluster is a hybrid cluster.<p id="p15501182110199"><a name="p15501182110199"></a><a name="p15501182110199"></a>A hybrid cluster manages a group of node resources based on Kubernetes. It can manage VMs, PMs, or a combination of both. Kubernetes automatically schedules containers onto available nodes. Before creating a containerized workload, ensure that a cluster is available.</p>
</li><li><strong id="b47051851714"><a name="b47051851714"></a><a name="b47051851714"></a>BareMetal</strong>: The cluster is a BMS cluster.<p id="p17501921151917"><a name="p17501921151917"></a><a name="p17501921151917"></a>BMS clusters are Kubernetes container clusters with high computing and high network performance. To use a BMS cluster, <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053536894.html" target="_blank" rel="noopener noreferrer">apply for a BMS</a>. To provide a high-speed container network, add a high-speed NIC when creating a BMS. For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053537013.html" target="_blank" rel="noopener noreferrer">Managing High-Speed Networks</a>.</p>
</li></ul>
</td>
</tr>
<tr id="row5117135719491"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p2011765764910"><a name="p2011765764910"></a><a name="p2011765764910"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1011715718499"><a name="p1011715718499"></a><a name="p1011715718499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p980431118507"><a name="p980431118507"></a><a name="p980431118507"></a>Cluster flavor, which cannot be changed after the cluster is created.</p>
<a name="ul4805141115020"></a><a name="ul4805141115020"></a><ul id="ul4805141115020"><li><strong id="b1361644114489"><a name="b1361644114489"></a><a name="b1361644114489"></a>cce.s1.small</strong>: small-scale, single-master VM cluster (≤ 50 nodes)</li><li><strong id="b189955528487"><a name="b189955528487"></a><a name="b189955528487"></a>cce.s1.medium</strong>: medium-scale, single-master VM cluster (≤ 200 nodes)</li><li><strong id="b18882321499"><a name="b18882321499"></a><a name="b18882321499"></a>cce.s1.large</strong>: large-scale, single-master VM cluster (≤ 1,000 nodes)</li><li><strong id="b871517715492"><a name="b871517715492"></a><a name="b871517715492"></a>cce.t1.small</strong>: small-scale, single-master BMS cluster (≤ 10 nodes)</li><li><strong id="b1174819294498"><a name="b1174819294498"></a><a name="b1174819294498"></a>cce.t1.medium</strong>: medium-scale, single-master BMS cluster (≤ 100 nodes)</li><li><strong id="b1089055211498"><a name="b1089055211498"></a><a name="b1089055211498"></a>cce.t1.large</strong>: large-scale, single-master BMS cluster (≤ 500 nodes)</li><li><strong id="b171341359503"><a name="b171341359503"></a><a name="b171341359503"></a>cce.s2.small</strong>: small-scale, high availability VM cluster (≤ 50 nodes)</li><li><strong id="b156801714145012"><a name="b156801714145012"></a><a name="b156801714145012"></a>cce.s2.medium</strong>: medium-scale, high availability VM cluster (≤ 200 nodes)</li><li><strong id="b17214152675012"><a name="b17214152675012"></a><a name="b17214152675012"></a>cce.s2.large</strong>: large-scale, high availability VM cluster (≤ 1,000 nodes)</li><li><strong id="b0706638105015"><a name="b0706638105015"></a><a name="b0706638105015"></a>cce.t2.small</strong>: small-scale, high availability BMS cluster (≤ 10 nodes)</li><li><strong id="b151666556501"><a name="b151666556501"></a><a name="b151666556501"></a>cce.t2.medium</strong>: medium-scale, high availability BMS cluster (≤ 100 nodes)</li><li><strong id="b169821430511"><a name="b169821430511"></a><a name="b169821430511"></a>cce.t2.large</strong>: large-scale, high availability BMS cluster (≤ 500 nodes)</li></ul>
<div class="note" id="note4806191195020"><a name="note4806191195020"></a><a name="note4806191195020"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul13806131119500"></a><a name="ul13806131119500"></a><ul id="ul13806131119500"><li>s1: single-master VM cluster</li><li>s2: high availability VM cluster</li><li>t1: single-master BMS cluster</li><li>t2: high-availability BMS cluster</li><li>For example, <strong id="b16794622013"><a name="b16794622013"></a><a name="b16794622013"></a>≤ 50 nodes</strong> indicates that the maximum number of nodes that can be managed by the cluster is 50.</li><li>A single-master cluster is a cluster that has only one master node. If the master node is down, the cluster will become unavailable and stop serving new workloads. However, existing workloads in the cluster are not affected.</li><li>A high-availability cluster has multiple master nodes. Faults in a single master node will not take the cluster down.</li></ul>
</div></div>
</td>
</tr>
<tr id="row767203910354"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p166721839133515"><a name="p166721839133515"></a><a name="p166721839133515"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1368643913517"><a name="p1368643913517"></a><a name="p1368643913517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14701915145510"><a name="p14701915145510"></a><a name="p14701915145510"></a>Cluster's baseline Kubernetes version. The latest version is recommended.</p>
</td>
</tr>
<tr id="row198601644104612"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p14861194416463"><a name="p14861194416463"></a><a name="p14861194416463"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p16861144484619"><a name="p16861144484619"></a><a name="p16861144484619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12861174454615"><a name="p12861174454615"></a><a name="p12861174454615"></a>AZ of the cluster.</p>
</td>
</tr>
<tr id="row9686193912354"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p5686133953518"><a name="p5686133953518"></a><a name="p5686133953518"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p370263913354"><a name="p370263913354"></a><a name="p370263913354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1370233913517"><a name="p1370233913517"></a><a name="p1370233913517"></a>Cluster description.</p>
</td>
</tr>
<tr id="row815323371218"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p181548333122"><a name="p181548333122"></a><a name="p181548333122"></a><span id="ph8375436138"><a name="ph8375436138"></a><a name="ph8375436138"></a>ipv6enable</span></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p18154173311127"><a name="p18154173311127"></a><a name="p18154173311127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14159181552117"><a name="p14159181552117"></a><a name="p14159181552117"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row770233993516"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p871733903513"><a name="p871733903513"></a><a name="p871733903513"></a>hostNetwok</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p77172039133514"><a name="p77172039133514"></a><a name="p77172039133514"></a><a href="#table662821045911">hostNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p373417399356"><a name="p373417399356"></a><a name="p373417399356"></a>Node network parameters.</p>
</td>
</tr>
<tr id="row97341339143516"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1773433923516"><a name="p1773433923516"></a><a name="p1773433923516"></a>containerNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p19734539193517"><a name="p19734539193517"></a><a name="p19734539193517"></a><a href="#table882310145412">containerNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12749539163518"><a name="p12749539163518"></a><a name="p12749539163518"></a>Container network parameters.</p>
</td>
</tr>
<tr id="row22451425161415"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1245112501418"><a name="p1245112501418"></a><a name="p1245112501418"></a><span id="ph1065916354144"><a name="ph1065916354144"></a><a name="ph1065916354144"></a>eniNetwork</span></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p72451025161414"><a name="p72451025161414"></a><a name="p72451025161414"></a><span id="ph781214821711"><a name="ph781214821711"></a><a name="ph781214821711"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p127119222211"><a name="p127119222211"></a><a name="p127119222211"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row2751113913367"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p167519392363"><a name="p167519392363"></a><a name="p167519392363"></a>authentication</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p87512392363"><a name="p87512392363"></a><a name="p87512392363"></a><a href="#table7220112133716">authentication</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p175133914366"><a name="p175133914366"></a><a name="p175133914366"></a>Configurations of the cluster authentication mode.</p>
</td>
</tr>
<tr id="row591414201496"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p725352519911"><a name="p725352519911"></a><a name="p725352519911"></a>billingMode</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p32531825295"><a name="p32531825295"></a><a name="p32531825295"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p3253162511916"><a name="p3253162511916"></a><a name="p3253162511916"></a>Billing mode of a node.</p>
<div class="note" id="note20254925394"><a name="note20254925394"></a><a name="note20254925394"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p17254112516910"><a name="p17254112516910"></a><a name="p17254112516910"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row87645397351"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p3764239143515"><a name="p3764239143515"></a><a name="p3764239143515"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p127641039153517"><a name="p127641039153517"></a><a name="p127641039153517"></a><a href="#table0102129153810">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p378014396351"><a name="p378014396351"></a><a name="p378014396351"></a>Extended fields in the format of key-value pairs.</p>
</td>
</tr>
<tr id="row41742581998"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12478124151010"><a name="p12478124151010"></a><a name="p12478124151010"></a>kubernetesSvcIpRange</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p6175155812919"><a name="p6175155812919"></a><a name="p6175155812919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1828218189101"><a name="p1828218189101"></a><a name="p1828218189101"></a>Service CIDR block or the IP address range which the kubernetes clusterIp must fall within. This parameter is available only for clusters of v1.11.7 and later.</p>
</td>
</tr>
<tr id="row359216881519"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p13592387156"><a name="p13592387156"></a><a name="p13592387156"></a><span id="ph2026714158150"><a name="ph2026714158150"></a><a name="ph2026714158150"></a>kubeProxyMode</span></p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p65920851519"><a name="p65920851519"></a><a name="p65920851519"></a><span id="ph1321172621616"><a name="ph1321172621616"></a><a name="ph1321172621616"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1912138191611"><a name="p1912138191611"></a><a name="p1912138191611"></a>Service forwarding mode. Two modes are available:</p>
<a name="ul1912738101620"></a><a name="ul1912738101620"></a><ul id="ul1912738101620"><li><strong id="b141263810163"><a name="b141263810163"></a><a name="b141263810163"></a>iptables</strong>: Traditional kube-proxy uses iptables rules to implement service load balancing. In this mode, too many iptables rules will be generated when many services are deployed. In addition, non-incremental updates will cause a latency and even obvious performance issues in the case of heavy service traffic.</li><li><strong id="b312173821614"><a name="b312173821614"></a><a name="b312173821614"></a>ipvs</strong>: Optimized kube-proxy mode with higher throughput and faster speed. This mode supports incremental updates and can keep connections uninterrupted during service updates. It is suitable for large-sized clusters.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  14**  Data structure of the  **hostNetwork**  field

<a name="table662821045911"></a>
<table><thead align="left"><tr id="row66291710205919"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p36296101596"><a name="p36296101596"></a><a name="p36296101596"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.84%" id="mcps1.2.4.1.2"><p id="p1162951019598"><a name="p1162951019598"></a><a name="p1162951019598"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.169999999999995%" id="mcps1.2.4.1.3"><p id="p3629110175918"><a name="p3629110175918"></a><a name="p3629110175918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row136291210195917"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p2062921035918"><a name="p2062921035918"></a><a name="p2062921035918"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p6629310115911"><a name="p6629310115911"></a><a name="p6629310115911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p26291410175913"><a name="p26291410175913"></a><a name="p26291410175913"></a>ID of the VPC used to create a master node. The VPC ID is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row062910104591"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1463011075911"><a name="p1463011075911"></a><a name="p1463011075911"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p163001075914"><a name="p163001075914"></a><a name="p163001075914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p163019106595"><a name="p163019106595"></a><a name="p163019106595"></a>Network ID of the subnet. The value is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row163101010598"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p186312101594"><a name="p186312101594"></a><a name="p186312101594"></a>highwaySubnet</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p16312010185916"><a name="p16312010185916"></a><a name="p16312010185916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p10631161017597"><a name="p10631161017597"></a><a name="p10631161017597"></a>ID of the high-speed network that is used to create a BMS node. The value is obtained from <a href="(optional)-creating-a-high-speed-network.md">(Optional) Creating a High-Speed Network</a>. This parameter is required for creating a BMS cluster.</p>
</td>
</tr>
<tr id="row6852515165918"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p13853161510596"><a name="p13853161510596"></a><a name="p13853161510596"></a>SecurityGroup</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p148539152594"><a name="p148539152594"></a><a name="p148539152594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p364513385321"><a name="p364513385321"></a><a name="p364513385321"></a>ID of the default security group created for the node during cluster creation.</p>
</td>
</tr>
</tbody>
</table>

**Table  15**  Data structure of the  **authentication**  field

<a name="table7220112133716"></a>
<table><thead align="left"><tr id="row7252191263710"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="p162521412143717"><a name="p162521412143717"></a><a name="p162521412143717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.2"><p id="p925241243714"><a name="p925241243714"></a><a name="p925241243714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.4.1.3"><p id="p22521112163712"><a name="p22521112163712"></a><a name="p22521112163712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12679127377"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p426711263719"><a name="p426711263719"></a><a name="p426711263719"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p826791263713"><a name="p826791263713"></a><a name="p826791263713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p9613105172620"><a name="p9613105172620"></a><a name="p9613105172620"></a>Cluster authentication mode.</p>
<a name="ul851344502618"></a><a name="ul851344502618"></a><ul id="ul851344502618"><li>Clusters of Kubernetes v1.11 or earlier support <strong id="b1716420411726"><a name="b1716420411726"></a><a name="b1716420411726"></a>x509</strong>, <strong id="b11446947027"><a name="b11446947027"></a><a name="b11446947027"></a>rbac</strong>, and <strong id="b131547533219"><a name="b131547533219"></a><a name="b131547533219"></a>authenticating_proxy</strong>. The default value is <strong id="b14677195811216"><a name="b14677195811216"></a><a name="b14677195811216"></a>x509</strong>.</li><li>Clusters of Kubernetes v1.13 or later support <strong id="b9936306314"><a name="b9936306314"></a><a name="b9936306314"></a>rbac</strong> and <strong id="b09381401336"><a name="b09381401336"></a><a name="b09381401336"></a>authenticating_proxy</strong>. The default value is <strong id="b181096471934"><a name="b181096471934"></a><a name="b181096471934"></a>rbac</strong>.</li></ul>
</td>
</tr>
<tr id="row14283191212372"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p1283111212373"><a name="p1283111212373"></a><a name="p1283111212373"></a>authenticatingProxy</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p62831212143713"><a name="p62831212143713"></a><a name="p62831212143713"></a><a href="#table15520124212381">authenticatingProxy</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p11283612183716"><a name="p11283612183716"></a><a name="p11283612183716"></a>Configurations of the <strong id="b94391351174718"><a name="b94391351174718"></a><a name="b94391351174718"></a>authenticating_proxy</strong> mode.</p>
</td>
</tr>
</tbody>
</table>

**Table  16**  Data structure of the  **authenticatingProxy**  field

<a name="table15520124212381"></a>
<table><thead align="left"><tr id="row8552742173812"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="p35521942103816"><a name="p35521942103816"></a><a name="p35521942103816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.2"><p id="p195661442203812"><a name="p195661442203812"></a><a name="p195661442203812"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.4.1.3"><p id="p135661542173814"><a name="p135661542173814"></a><a name="p135661542173814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5566124223813"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p1658210422386"><a name="p1658210422386"></a><a name="p1658210422386"></a>ca</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p13582242183819"><a name="p13582242183819"></a><a name="p13582242183819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p058274219383"><a name="p058274219383"></a><a name="p058274219383"></a>CA root certificate provided in the <strong id="b3607192519495"><a name="b3607192519495"></a><a name="b3607192519495"></a>authenticating_proxy</strong> mode. The CA root certificate is encoded to the Base64 format.</p>
</td>
</tr>
</tbody>
</table>

**Table  17**  Data structure of the extendParam field

<a name="table0102129153810"></a>
<table><thead align="left"><tr id="row81032096382"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.4.1.1"><p id="p410369123818"><a name="p410369123818"></a><a name="p410369123818"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.740000000000002%" id="mcps1.2.4.1.2"><p id="p310317973810"><a name="p310317973810"></a><a name="p310317973810"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.67%" id="mcps1.2.4.1.3"><p id="p5104209103816"><a name="p5104209103816"></a><a name="p5104209103816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row101045918387"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p010419933820"><a name="p010419933820"></a><a name="p010419933820"></a>clusterAZ</p>
</td>
<td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.4.1.2 "><p id="p1010412916388"><a name="p1010412916388"></a><a name="p1010412916388"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p110413993815"><a name="p110413993815"></a><a name="p110413993815"></a>If you want to enable multiple AZs for the cluster, enter {"clusterAZ": "multi_az"}.</p>
<div class="note" id="note2010439103815"><a name="note2010439103815"></a><a name="note2010439103815"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2104598383"><a name="p2104598383"></a><a name="p2104598383"></a>Only HA clusters support multiple AZs. To be specific, this field can be configured only when the <strong id="b410417943816"><a name="b410417943816"></a><a name="b410417943816"></a>flavor</strong> field in <a href="#table1034041612134">Table 5</a> is set to <strong id="b191049963818"><a name="b191049963818"></a><a name="b191049963818"></a>cce.s2.small</strong>, <strong id="b10105493386"><a name="b10105493386"></a><a name="b10105493386"></a>cce.s2.medium</strong>, <strong id="b151052923816"><a name="b151052923816"></a><a name="b151052923816"></a>cce.s2.large</strong>, <strong id="b110511916384"><a name="b110511916384"></a><a name="b110511916384"></a>cce.t2.small</strong>, <strong id="b4105399386"><a name="b4105399386"></a><a name="b4105399386"></a>cce.t2.medium</strong>, or <strong id="b10105129193813"><a name="b10105129193813"></a><a name="b10105129193813"></a>cce.t2.large</strong>. After multi-AZ deployment is enabled, the three master nodes of the cluster are distributed in different AZs. The cluster remains available even when one of the AZs is down.</p>
</div></div>
</td>
</tr>
<tr id="row161058923820"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p810516914387"><a name="p810516914387"></a><a name="p810516914387"></a>dssMasterVolumes</p>
</td>
<td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.4.1.2 "><p id="p101061191384"><a name="p101061191384"></a><a name="p101061191384"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p6106294381"><a name="p6106294381"></a><a name="p6106294381"></a>Whether the system and data disks of a master node use dedicated distributed storage. If this parameter is omitted or left unspecified, EVS disks are used by default.</p>
</td>
</tr>
<tr id="row2010619103816"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p510639153818"><a name="p510639153818"></a><a name="p510639153818"></a><span id="ph7374114012810"><a name="ph7374114012810"></a><a name="ph7374114012810"></a>clusterExternalIP</span></p>
</td>
<td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.4.1.2 "><p id="p3106159153812"><a name="p3106159153812"></a><a name="p3106159153812"></a><span id="ph79173712543"><a name="ph79173712543"></a><a name="ph79173712543"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p139831857192418"><a name="p139831857192418"></a><a name="p139831857192418"></a>EIP used to access the cluster.</p>
</td>
</tr>
</tbody>
</table>

**Table  18**  Data structure of the  **status**  field

<a name="table6749834132215"></a>
<table><thead align="left"><tr id="row14749534122218"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="p37490340223"><a name="p37490340223"></a><a name="p37490340223"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.2"><p id="p7749734112218"><a name="p7749734112218"></a><a name="p7749734112218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.4.1.3"><p id="p67491034152211"><a name="p67491034152211"></a><a name="p67491034152211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1749834132213"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p16749153410220"><a name="p16749153410220"></a><a name="p16749153410220"></a>phase</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p4749193482216"><a name="p4749193482216"></a><a name="p4749193482216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p19996100113820"><a name="p19996100113820"></a><a name="p19996100113820"></a>Cluster status. Possible values:</p>
<a name="ul954920813385"></a><a name="ul954920813385"></a><ul id="ul954920813385"><li><strong id="b1490361952318"><a name="b1490361952318"></a><a name="b1490361952318"></a>Available</strong>: The cluster is running properly.</li><li><strong id="b11507102716231"><a name="b11507102716231"></a><a name="b11507102716231"></a>Unavailable</strong>: The cluster is exhibiting unexpected behavior. Manually delete the cluster or contact the administrator to delete the cluster.</li><li><strong id="b1277171719249"><a name="b1277171719249"></a><a name="b1277171719249"></a>ScalingUp</strong>: Nodes are being added to the cluster.</li><li><strong id="b1376363119242"><a name="b1376363119242"></a><a name="b1376363119242"></a>ScalingDown</strong>: The cluster is being downsized to fewer nodes.</li><li><strong id="b139541128192817"><a name="b139541128192817"></a><a name="b139541128192817"></a>Creating</strong>: The cluster is being created.</li><li><strong id="b3795163611280"><a name="b3795163611280"></a><a name="b3795163611280"></a>Deleting</strong>: The cluster is being deleted.</li><li><strong id="b1359145216284"><a name="b1359145216284"></a><a name="b1359145216284"></a>Upgrading</strong>: The cluster is being upgraded.</li><li><strong id="b1971185942813"><a name="b1971185942813"></a><a name="b1971185942813"></a>Empty</strong>: The cluster has no resources.</li></ul>
</td>
</tr>
<tr id="row77494342221"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="p6749143432216"><a name="p6749143432216"></a><a name="p6749143432216"></a>jobID</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p117745018256"><a name="p117745018256"></a><a name="p117745018256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.4.1.3 "><p id="p1774918349229"><a name="p1774918349229"></a><a name="p1774918349229"></a>ID of the cluster creation job. You can <a href="reading-job-progress.md">query job progress</a> by job ID to keep updated on cluster creation progress.</p>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
    "kind": "Cluster",
    "apiVersion": "v3",
    "metadata": {
        "name": "test-create-cluster",
        "uid": "d6a883a1-8529-11ea-8e34-0255ac101108",
        "creationTimestamp": "2020-04-23 06:15:32.974281119 +0000 UTC",
        "updateTimestamp": "2020-04-23 06:15:32.974281688 +0000 UTC",
        "labels": {
            "foo": "bar"
        },
        "annotations": {
            "foo2": "bar2"
        }
    },
    "spec": {
        "type": "VirtualMachine",
        "flavor": "cce.s2.small",
        "version": "v1.15.6-r1",
        "description": "this is a demo cluster",
        "ipv6enable": false,
        "hostNetwork": {
            "vpc": "23d3725f-6ffe-400e-8fb6-b4f9a7b3e8c1",
            "subnet": "c90b3ce5-e1f1-4c87-a006-644d78846438"
        },
        "containerNetwork": {
            "mode": "overlay_l2",
            "cidr": "172.16.0.0/16"
        },
        "eniNetwork": {},
        "authentication": {
            "mode": "rbac",
            "authenticatingProxy": {}
        },
        "billingMode": 0,
        "extendParam": {
            "clusterAZ": "multi_az"
        },
        "kubernetesSvcIpRange": "10.247.0.0/16",
        "kubeProxyMode": "iptables"
    },
    "status": {
        "phase": "Creating",
        "jobID": "d6bcbb0b-8529-11ea-8e34-0255ac101108"
    }
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 19](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  19**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>The job for creating a cluster is successfully delivered.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

