# Reading a Specified Cluster<a name="cce_02_0238"></a>

## Function<a name="section1686113493165"></a>

This API is used to obtain details about a specified cluster.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}

[Table 1](#table2027961241820)  describes the parameters of this API.

**Table  1**  Parameter description

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
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row126417469411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p5642046194113"><a name="p5642046194113"></a><a name="p5642046194113"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p146484634113"><a name="p146484634113"></a><a name="p146484634113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p664164613418"><a name="p664164613418"></a><a name="p664164613418"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table538113720514)  lists the request parameters.

**Table  2**  Parameters in the request header

<a name="table538113720514"></a>
<table><thead align="left"><tr id="en-us_topic_0199164459_row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0199164459_p115009545264"><a name="en-us_topic_0199164459_p115009545264"></a><a name="en-us_topic_0199164459_p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0199164459_p175001547265"><a name="en-us_topic_0199164459_p175001547265"></a><a name="en-us_topic_0199164459_p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="en-us_topic_0199164459_p16500154162611"><a name="en-us_topic_0199164459_p16500154162611"></a><a name="en-us_topic_0199164459_p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0199164459_row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0199164459_p69808112344"><a name="en-us_topic_0199164459_p69808112344"></a><a name="en-us_topic_0199164459_p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0199164459_p3980111103414"><a name="en-us_topic_0199164459_p3980111103414"></a><a name="en-us_topic_0199164459_p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0199164459_p169801011203416"><a name="en-us_topic_0199164459_p169801011203416"></a><a name="en-us_topic_0199164459_p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="en-us_topic_0199164459_ul7385444163617"></a><a name="en-us_topic_0199164459_ul7385444163617"></a><ul id="en-us_topic_0199164459_ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="en-us_topic_0199164459_row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0199164459_p105001654202618"><a name="en-us_topic_0199164459_p105001654202618"></a><a name="en-us_topic_0199164459_p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0199164459_p20500954182618"><a name="en-us_topic_0199164459_p20500954182618"></a><a name="en-us_topic_0199164459_p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p35202313507"><a name="p35202313507"></a><a name="p35202313507"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

N/A

## Response<a name="section61819725020"></a>

**Response parameters:**

[Table 3](#table34052983203655)  describes the response parameters.

**Table  3**  Response parameters

<a name="table34052983203655"></a>
<table><thead align="left"><tr id="row30254333203655"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p34681881203655"><a name="p34681881203655"></a><a name="p34681881203655"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p57769002203655"><a name="p57769002203655"></a><a name="p57769002203655"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p58673482203655"><a name="p58673482203655"></a><a name="p58673482203655"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54931625203655"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p44731858185518"><a name="p44731858185518"></a><a name="p44731858185518"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p57145269553"><a name="p57145269553"></a><a name="p57145269553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. The value is fixed at <strong id="b14211820173214"><a name="b14211820173214"></a><a name="b14211820173214"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row15234185203655"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b126571459155415"><a name="b126571459155415"></a><a name="b126571459155415"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1122635417553"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p144741558135518"><a name="p144741558135518"></a><a name="p144741558135518"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p18711257121911"><a name="p18711257121911"></a><a name="p18711257121911"></a><a href="creating-a-cluster.md#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p16108141202712"><a name="p16108141202712"></a><a name="p16108141202712"></a>Cluster metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row9619511127"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p4785161212"><a name="p4785161212"></a><a name="p4785161212"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p13198142153113"><a name="p13198142153113"></a><a name="p13198142153113"></a><a href="#table1034041612134">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1896142152710"><a name="p1896142152710"></a><a name="p1896142152710"></a>Detailed description of the cluster targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row4466312313"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p138171915205"><a name="p138171915205"></a><a name="p138171915205"></a><a href="#table6749834132215">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p166941916272"><a name="p166941916272"></a><a name="p166941916272"></a>Cluster status and jobID of the job that reads a specified cluster.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **spec**  field

<a name="table1034041612134"></a>
<table><thead align="left"><tr id="row14348121616132"><th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.4.1.1"><p id="p133505167139"><a name="p133505167139"></a><a name="p133505167139"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p735501615139"><a name="p735501615139"></a><a name="p735501615139"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.81%" id="mcps1.2.4.1.3"><p id="p15357151631311"><a name="p15357151631311"></a><a name="p15357151631311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row178365271483"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p146521540191916"><a name="p146521540191916"></a><a name="p146521540191916"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p1052510179227"><a name="p1052510179227"></a><a name="p1052510179227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p1691385774411"><a name="p1691385774411"></a><a name="p1691385774411"></a>Cluster type. Possible values:</p>
<a name="ul123801520452"></a><a name="ul123801520452"></a><ul id="ul123801520452"><li><strong id="b122221723185118"><a name="b122221723185118"></a><a name="b122221723185118"></a>VirtualMachine</strong>: The cluster is a hybrid cluster.<p id="p138192583535"><a name="p138192583535"></a><a name="p138192583535"></a>A hybrid cluster manages a group of node resources based on Kubernetes. It can manage VMs, physical machines (PMs), or a combination of both. Kubernetes automatically schedules containers onto available nodes. Before creating a containerized workload, ensure that a cluster is available.</p>
</li><li><strong id="b2026825310204"><a name="b2026825310204"></a><a name="b2026825310204"></a>BareMetal</strong>: The cluster is a BMS cluster.<p id="p13891132020474"><a name="p13891132020474"></a><a name="p13891132020474"></a>BMS clusters are Kubernetes container clusters with high computing and high network performance. To use a BMS cluster, <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053536894.html" target="_blank" rel="noopener noreferrer">apply for a BMS</a>. To provide a high-speed container network, add a high-speed network interface card (NIC) when creating a BMS. For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053537013.html" target="_blank" rel="noopener noreferrer">Managing High-Speed Networks</a>.</p>
</li></ul>
</td>
</tr>
<tr id="row111221127144415"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1612362713448"><a name="p1612362713448"></a><a name="p1612362713448"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p1512392713442"><a name="p1512392713442"></a><a name="p1512392713442"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p16621941104417"><a name="p16621941104417"></a><a name="p16621941104417"></a>Cluster flavor, which cannot be changed after the cluster is created.</p>
<a name="ul154851748174415"></a><a name="ul154851748174415"></a><ul id="ul154851748174415"><li><strong id="b11489836273"><a name="b11489836273"></a><a name="b11489836273"></a>cce.s1.small</strong>: small-scale, single-master VM cluster (≤ 50 nodes)</li><li><strong id="b367910942720"><a name="b367910942720"></a><a name="b367910942720"></a>cce.s1.medium</strong>: medium-scale, single-master VM cluster (≤ 200 nodes)</li><li><strong id="b6271153114279"><a name="b6271153114279"></a><a name="b6271153114279"></a>cce.s1.large</strong>: large-scale, single-master VM cluster (≤ 1,000 nodes)</li><li><strong id="b181461333281"><a name="b181461333281"></a><a name="b181461333281"></a>cce.t1.small</strong>: small-scale, single-master BMS cluster (≤ 10 nodes)</li><li><strong id="b1961019276282"><a name="b1961019276282"></a><a name="b1961019276282"></a>cce.t1.medium</strong>: medium-scale, single-master BMS cluster (≤ 100 nodes)</li><li><strong id="b3357144892811"><a name="b3357144892811"></a><a name="b3357144892811"></a>cce.t1.large</strong>: large-scale, single-master BMS cluster (≤ 500 nodes)</li><li><strong id="b1081317262919"><a name="b1081317262919"></a><a name="b1081317262919"></a>cce.s2.small</strong>: small-scale, high availability VM cluster (≤ 50 nodes)</li><li><strong id="b1689322115296"><a name="b1689322115296"></a><a name="b1689322115296"></a>cce.s2.medium</strong>: medium-scale, high availability VM cluster (≤ 200 nodes)</li><li><strong id="b57413316296"><a name="b57413316296"></a><a name="b57413316296"></a>cce.s2.large</strong>: large-scale, high availability VM cluster (≤ 1,000 nodes)</li><li><strong id="b12121245192917"><a name="b12121245192917"></a><a name="b12121245192917"></a>cce.t2.small</strong>: small-scale, high availability BMS cluster (≤ 10 nodes)</li><li><strong id="b01951338302"><a name="b01951338302"></a><a name="b01951338302"></a>cce.t2.medium</strong>: medium-scale, high availability BMS cluster (≤ 100 nodes)</li><li><strong id="b198171213303"><a name="b198171213303"></a><a name="b198171213303"></a>cce.t2.large</strong>: large-scale, high availability BMS cluster (≤ 500 nodes)</li></ul>
<div class="note" id="note10821115618447"><a name="note10821115618447"></a><a name="note10821115618447"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul13821356164415"></a><a name="ul13821356164415"></a><ul id="ul13821356164415"><li>s1: single-master VM cluster</li><li>s2: high availability VM cluster</li><li>t1: single-master BMS cluster</li><li>t2: high-availability BMS cluster</li><li>For example, <strong id="b1251010481560"><a name="b1251010481560"></a><a name="b1251010481560"></a>≤ 50 nodes</strong> indicates that the maximum number of nodes that can be managed by the cluster is 50.</li><li>A single-master cluster has only one master node. If the master node is down, the cluster will become unavailable and stop serving new workloads. However, existing workloads in the cluster are not affected.</li><li>A high-availability cluster has multiple master nodes. Faults in a single master node will not take the cluster down.</li></ul>
</div></div>
</td>
</tr>
<tr id="row83711516191317"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1565217404195"><a name="p1565217404195"></a><a name="p1565217404195"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p252511174227"><a name="p252511174227"></a><a name="p252511174227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p0929195015409"><a name="p0929195015409"></a><a name="p0929195015409"></a>Cluster's baseline Kubernetes version. The latest version is recommended.</p>
</td>
</tr>
<tr id="row533805884917"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1633905884915"><a name="p1633905884915"></a><a name="p1633905884915"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p13391558194914"><a name="p13391558194914"></a><a name="p13391558194914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p56473409213"><a name="p56473409213"></a><a name="p56473409213"></a>AZ of the cluster.</p>
</td>
</tr>
<tr id="row0120134310612"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p61211443864"><a name="p61211443864"></a><a name="p61211443864"></a><span id="ph5508658170"><a name="ph5508658170"></a><a name="ph5508658170"></a>ipv6enable</span></p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p712119434619"><a name="p712119434619"></a><a name="p712119434619"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p10837151832714"><a name="p10837151832714"></a><a name="p10837151832714"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row53621622155010"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1036210224509"><a name="p1036210224509"></a><a name="p1036210224509"></a>supportIstio</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p193621822175012"><a name="p193621822175012"></a><a name="p193621822175012"></a><span id="ph153316358816"><a name="ph153316358816"></a><a name="ph153316358816"></a>Boolean</span></p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p667511366395"><a name="p667511366395"></a><a name="p667511366395"></a>Whether Istio is supported.</p>
<div class="note" id="note14449515181617"><a name="note14449515181617"></a><a name="note14449515181617"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1644917159167"><a name="p1644917159167"></a><a name="p1644917159167"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row20432126134212"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1443386124219"><a name="p1443386124219"></a><a name="p1443386124219"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p1743310614212"><a name="p1743310614212"></a><a name="p1743310614212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p19433156124218"><a name="p19433156124218"></a><a name="p19433156124218"></a>Cluster description.</p>
</td>
</tr>
<tr id="row17011947507"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p4701194125011"><a name="p4701194125011"></a><a name="p4701194125011"></a>hostNetwok</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p167012042507"><a name="p167012042507"></a><a name="p167012042507"></a><a href="#table1622013552507">hostNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p123281848104313"><a name="p123281848104313"></a><a name="p123281848104313"></a>Node network parameters, including a VPC and subnet ID. <strong id="b13136114517294"><a name="b13136114517294"></a><a name="b13136114517294"></a>hostNetwok</strong> is mandatory because nodes in a cluster communicate with each other by using a VPC.</p>
</td>
</tr>
<tr id="row651719205217"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p851151955212"><a name="p851151955212"></a><a name="p851151955212"></a>containerNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p7514193520"><a name="p7514193520"></a><a name="p7514193520"></a><a href="#table882310145412">containerNetwork</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p16930187201117"><a name="p16930187201117"></a><a name="p16930187201117"></a>Container network parameters, including a container network model and container CIDR block.</p>
</td>
</tr>
<tr id="row88640191587"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p128644191585"><a name="p128644191585"></a><a name="p128644191585"></a><span id="ph108264246810"><a name="ph108264246810"></a><a name="ph108264246810"></a>eniNetwork</span></p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p3864161913816"><a name="p3864161913816"></a><a name="p3864161913816"></a><span id="ph17166739489"><a name="ph17166739489"></a><a name="ph17166739489"></a>String</span></p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p556713281277"><a name="p556713281277"></a><a name="p556713281277"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row9493123913567"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p2493239145620"><a name="p2493239145620"></a><a name="p2493239145620"></a><span>authentication</span></p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p6493113918562"><a name="p6493113918562"></a><a name="p6493113918562"></a><a href="creating-a-cluster.md#table71529332533">authentication</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p14939395566"><a name="p14939395566"></a><a name="p14939395566"></a>Configurations of the cluster authentication mode.</p>
</td>
</tr>
<tr id="row138261435110"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p6826841514"><a name="p6826841514"></a><a name="p6826841514"></a>billingMode</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p188261245511"><a name="p188261245511"></a><a name="p188261245511"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p1834638101617"><a name="p1834638101617"></a><a name="p1834638101617"></a>Billing mode of a node.</p>
<div class="note" id="note0702131124412"><a name="note0702131124412"></a><a name="note0702131124412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p77026184417"><a name="p77026184417"></a><a name="p77026184417"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row0552182615116"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p155392619517"><a name="p155392619517"></a><a name="p155392619517"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p165531261511"><a name="p165531261511"></a><a name="p165531261511"></a><a href="#table17575013586">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p13817123194716"><a name="p13817123194716"></a><a name="p13817123194716"></a>Extended fields in the format of key-value pairs.</p>
</td>
</tr>
<tr id="row97803915130"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p156284113136"><a name="p156284113136"></a><a name="p156284113136"></a>kubernetesSvcIpRange</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p0703163016251"><a name="p0703163016251"></a><a name="p0703163016251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p7782199181315"><a name="p7782199181315"></a><a name="p7782199181315"></a>Service CIDR block or the IP address range which the <strong id="b1853831421311"><a name="b1853831421311"></a><a name="b1853831421311"></a>kubernetes clusterIp</strong> must fall within. This parameter is available only for clusters of v1.11.7 and later.</p>
</td>
</tr>
<tr id="row334518801617"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p6345128161614"><a name="p6345128161614"></a><a name="p6345128161614"></a>kubeProxyMode</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p734518141613"><a name="p734518141613"></a><a name="p734518141613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p656873817549"><a name="p656873817549"></a><a name="p656873817549"></a>Service forwarding mode. Two modes are available:</p>
<a name="ul205681238125417"></a><a name="ul205681238125417"></a><ul id="ul205681238125417"><li><strong id="b15681538185418"><a name="b15681538185418"></a><a name="b15681538185418"></a>iptables</strong>: Traditional kube-proxy uses iptables rules to implement service load balancing. In this mode, too many iptables rules will be generated when many services are deployed. In addition, non-incremental updates will cause a latency and even obvious performance issues in the case of heavy service traffic.</li><li><strong id="b156973816540"><a name="b156973816540"></a><a name="b156973816540"></a>ipvs</strong>: Optimized kube-proxy mode with higher throughput and faster speed. This mode supports incremental updates and can keep connections uninterrupted during service updates. It is suitable for large-sized clusters.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **hostNetwork**  field

<a name="table1622013552507"></a>
<table><thead align="left"><tr id="row922065525010"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p687613311518"><a name="p687613311518"></a><a name="p687613311518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.84%" id="mcps1.2.4.1.2"><p id="p168912031515"><a name="p168912031515"></a><a name="p168912031515"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.169999999999995%" id="mcps1.2.4.1.3"><p id="p158914355111"><a name="p158914355111"></a><a name="p158914355111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1622075519505"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1465319402192"><a name="p1465319402192"></a><a name="p1465319402192"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p1452691718229"><a name="p1452691718229"></a><a name="p1452691718229"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p2018164753013"><a name="p2018164753013"></a><a name="p2018164753013"></a>ID of the VPC used to create a master node. The VPC ID is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row322025520508"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1665317409195"><a name="p1665317409195"></a><a name="p1665317409195"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p185261417112213"><a name="p185261417112213"></a><a name="p185261417112213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p111816472307"><a name="p111816472307"></a><a name="p111816472307"></a>Network ID of the subnet. The value is obtained from <a href="creating-a-vpc-and-subnet.md">Creating a VPC and Subnet</a>.</p>
</td>
</tr>
<tr id="row10220125555018"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p46541240151913"><a name="p46541240151913"></a><a name="p46541240151913"></a>highwaySubnet</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p1752614175225"><a name="p1752614175225"></a><a name="p1752614175225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p15181134718309"><a name="p15181134718309"></a><a name="p15181134718309"></a>ID of the high-speed network that is used to create a BMS node. This parameter is required for creating a BMS cluster.</p>
</td>
</tr>
<tr id="row152996116531"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1229917119536"><a name="p1229917119536"></a><a name="p1229917119536"></a>SecurityGroup</p>
</td>
<td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.2.4.1.2 "><p id="p1329981117534"><a name="p1329981117534"></a><a name="p1329981117534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.169999999999995%" headers="mcps1.2.4.1.3 "><p id="p1829921111531"><a name="p1829921111531"></a><a name="p1829921111531"></a>ID of the default security group created for the node during cluster creation.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the  **containerNetwork**  field

<a name="table882310145412"></a>
<table><thead align="left"><tr id="row1682316016545"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p1694819205543"><a name="p1694819205543"></a><a name="p1694819205543"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.4.1.2"><p id="p11964620145410"><a name="p11964620145410"></a><a name="p11964620145410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.32%" id="mcps1.2.4.1.3"><p id="p09648200542"><a name="p09648200542"></a><a name="p09648200542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row482317016541"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p2082320195415"><a name="p2082320195415"></a><a name="p2082320195415"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p28237014542"><a name="p28237014542"></a><a name="p28237014542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p2398131181613"><a name="p2398131181613"></a><a name="p2398131181613"></a>Container network model. Select one of the following possible values:</p>
<a name="ul1085141916166"></a><a name="ul1085141916166"></a><ul id="ul1085141916166"><li><strong id="b1892704916116"><a name="b1892704916116"></a><a name="b1892704916116"></a>overlay_l2</strong>: an overlay_l2 network built for containers by using OpenVSwitch (OVS).</li><li><strong id="b1514161620019"><a name="b1514161620019"></a><a name="b1514161620019"></a>underlay_ipvlan</strong>: an underlay_l2 network built for BMS nodes by using ipvlan.</li><li><strong id="b15370163183618"><a name="b15370163183618"></a><a name="b15370163183618"></a>vpc-router</strong>: an underlay_l2 network built for containers by using ipvlan and custom VPC routes.</li></ul>
<div class="note" id="note1860516155199"><a name="note1860516155199"></a><a name="note1860516155199"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul21791736131915"></a><a name="ul21791736131915"></a><ul id="ul21791736131915"><li>Tunnel network: Under this model, the container network is an overlay network on top of a VPC network based on the VXLAN technology. VXLAN encapsulates Ethernet packets as UDP packets for tunnel transmission. Though at some cost of performance, the tunnel encapsulation enables higher interoperability and compatibility with advanced features (such as network policy-based isolation), meeting the requirements of most applications.</li><li>VPC network: Routing is implemented within a VPC network according to custom VPC routes. Each node is assigned a CIDR block of a fixed size. vpc-router networks are free of tunnel encapsulation overheads and provide better container network performance than tunnel networks. In addition, as routes to node IP addresses and the containers have been configured on vpc-router, container instances can be directly accessed from outside the cluster.</li></ul>
</div></div>
</td>
</tr>
<tr id="row482313013542"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1982310145419"><a name="p1982310145419"></a><a name="p1982310145419"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p19823401545"><a name="p19823401545"></a><a name="p19823401545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p674711410131"><a name="p674711410131"></a><a name="p674711410131"></a>Container CIDR block. Recommended: 10.0.0.0/12-19, 172.16.0.0/16-19, or 192.168.0.0/16-19. If the selected CIDR block conflicts with existing CIDR blocks, the system automatically selects another CIDR block.</p>
<p id="p181514571229"><a name="p181514571229"></a><a name="p181514571229"></a>If the maximum number of pods on a node is 110, each of the recommended container CIDR blocks supports at least 582 nodes. This parameter cannot be modified after the cluster is created. Exercise caution when setting this parameter.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the extendParam field

<a name="table17575013586"></a>
<table><thead align="left"><tr id="row51071750155814"><th class="cellrowborder" valign="top" width="20.71%" id="mcps1.2.4.1.1"><p id="p41071050115816"><a name="p41071050115816"></a><a name="p41071050115816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.4.1.2"><p id="p1312155019587"><a name="p1312155019587"></a><a name="p1312155019587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.67%" id="mcps1.2.4.1.3"><p id="p13121155016582"><a name="p13121155016582"></a><a name="p13121155016582"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1457961164816"><td class="cellrowborder" valign="top" width="20.71%" headers="mcps1.2.4.1.1 "><p id="p1757418610512"><a name="p1757418610512"></a><a name="p1757418610512"></a>alpha.cce/fixPoolMask</p>
</td>
<td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.4.1.2 "><p id="p17573263512"><a name="p17573263512"></a><a name="p17573263512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p1694224152718"><a name="p1694224152718"></a><a name="p1694224152718"></a>Reserved. This parameter is not used in the current version.</p>
</td>
</tr>
<tr id="row15380172523019"><td class="cellrowborder" valign="top" width="20.71%" headers="mcps1.2.4.1.1 "><p id="p1594918321549"><a name="p1594918321549"></a><a name="p1594918321549"></a>kubernetes.io/cpuManagerPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.4.1.2 "><p id="p1994343217412"><a name="p1994343217412"></a><a name="p1994343217412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p1394113321442"><a name="p1394113321442"></a><a name="p1394113321442"></a>CPU management policy of the master node.</p>
</td>
</tr>
<tr id="row9784733459"><td class="cellrowborder" valign="top" width="20.71%" headers="mcps1.2.4.1.1 "><p id="p1578413331758"><a name="p1578413331758"></a><a name="p1578413331758"></a>upgradefrom</p>
</td>
<td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.4.1.2 "><p id="p5784533258"><a name="p5784533258"></a><a name="p5784533258"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><p id="p1875343414011"><a name="p1875343414011"></a><a name="p1875343414011"></a>Version from which this version is upgrade.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the  **status**  field

<a name="table6749834132215"></a>
<table><thead align="left"><tr id="row14749534122218"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p37490340223"><a name="p37490340223"></a><a name="p37490340223"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p7749734112218"><a name="p7749734112218"></a><a name="p7749734112218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p67491034152211"><a name="p67491034152211"></a><a name="p67491034152211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1749834132213"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p16749153410220"><a name="p16749153410220"></a><a name="p16749153410220"></a>phase</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p4749193482216"><a name="p4749193482216"></a><a name="p4749193482216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p19996100113820"><a name="p19996100113820"></a><a name="p19996100113820"></a>Cluster status. Possible values:</p>
<a name="ul954920813385"></a><a name="ul954920813385"></a><ul id="ul954920813385"><li><strong id="b31162290589"><a name="b31162290589"></a><a name="b31162290589"></a>Available</strong>: The cluster is running properly.</li><li><strong id="b271603245815"><a name="b271603245815"></a><a name="b271603245815"></a>Unavailable</strong>: The cluster is exhibiting unexpected behavior. Manually delete the cluster or contact the administrator to delete the cluster.</li><li><strong id="b1618913355587"><a name="b1618913355587"></a><a name="b1618913355587"></a>ScalingUp</strong>: Nodes are being added to the cluster.</li><li><strong id="b182112393582"><a name="b182112393582"></a><a name="b182112393582"></a>ScalingDown</strong>: The cluster is being downsized to fewer nodes.</li><li><strong id="b193081845185818"><a name="b193081845185818"></a><a name="b193081845185818"></a>Creating</strong>: The cluster is being created.</li><li><strong id="b164334713587"><a name="b164334713587"></a><a name="b164334713587"></a>Deleting</strong>: The cluster is being deleted.</li><li><strong id="b18491748105818"><a name="b18491748105818"></a><a name="b18491748105818"></a>Upgrading</strong>: The cluster is being upgraded.</li><li><strong id="b18688456155816"><a name="b18688456155816"></a><a name="b18688456155816"></a>Resizing</strong>: Cluster specifications are being changed.</li><li><strong id="b10115131217599"><a name="b10115131217599"></a><a name="b10115131217599"></a>Empty</strong>: The cluster has no resources.</li></ul>
</td>
</tr>
<tr id="row6749834122215"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p167491634122217"><a name="p167491634122217"></a><a name="p167491634122217"></a>reason</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1870174132519"><a name="p1870174132519"></a><a name="p1870174132519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p8749534142216"><a name="p8749534142216"></a><a name="p8749534142216"></a>Reason of cluster state transition. This parameter is returned if the cluster is not in the Available state.</p>
</td>
</tr>
<tr id="row1574915349227"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p774993432217"><a name="p774993432217"></a><a name="p774993432217"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1571284172519"><a name="p1571284172519"></a><a name="p1571284172519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p48271730459"><a name="p48271730459"></a><a name="p48271730459"></a>Detailed information about why the cluster changes to the current state. This parameter is returned if the cluster is not in the Available state.</p>
</td>
</tr>
<tr id="row9189104316515"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p319094395117"><a name="p319094395117"></a><a name="p319094395117"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p619084316514"><a name="p619084316514"></a><a name="p619084316514"></a><a href="#t3d666891caf940a39046a0807b3c480a">endpoint</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p13190943135116"><a name="p13190943135116"></a><a name="p13190943135116"></a>Access address of the kube-apiserver in the cluster.</p>
</td>
</tr>
</tbody>
</table>

**Table  9**  Data structure of the endpoint field

<a name="t3d666891caf940a39046a0807b3c480a"></a>
<table><thead align="left"><tr id="r21652f7a92354ddc97bb1eced149ff3a"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="a58d65dc53b9d4f2da3791b1612bedd1f"><a name="a58d65dc53b9d4f2da3791b1612bedd1f"></a><a name="a58d65dc53b9d4f2da3791b1612bedd1f"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.732673267326735%" id="mcps1.2.4.1.2"><p id="aa02b4a8b12ab4109b4442ae3ffa03ee4"><a name="aa02b4a8b12ab4109b4442ae3ffa03ee4"></a><a name="aa02b4a8b12ab4109b4442ae3ffa03ee4"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.475247524752476%" id="mcps1.2.4.1.3"><p id="acc10a55b9e224f2d8fe58f509a24b767"><a name="acc10a55b9e224f2d8fe58f509a24b767"></a><a name="acc10a55b9e224f2d8fe58f509a24b767"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r03ad43ab59d1482795974193959e47a1"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="af592733d401946dab4f8b1fe44a7d061"><a name="af592733d401946dab4f8b1fe44a7d061"></a><a name="af592733d401946dab4f8b1fe44a7d061"></a>internal</p>
</td>
<td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.2 "><p id="a98c38a11ab774e22a973311375577841"><a name="a98c38a11ab774e22a973311375577841"></a><a name="a98c38a11ab774e22a973311375577841"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="a57119fe622d9407c9d52289cbd9e1195"><a name="a57119fe622d9407c9d52289cbd9e1195"></a><a name="a57119fe622d9407c9d52289cbd9e1195"></a>Internal network address.</p>
</td>
</tr>
<tr id="r0c8fedfca25f4644899868c111dcc671"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="ad046c7cf6d88431ba221243410dcdcb0"><a name="ad046c7cf6d88431ba221243410dcdcb0"></a><a name="ad046c7cf6d88431ba221243410dcdcb0"></a>external</p>
</td>
<td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.2 "><p id="ac40b6385fc6d45ad8fbc3fee9858d294"><a name="ac40b6385fc6d45ad8fbc3fee9858d294"></a><a name="ac40b6385fc6d45ad8fbc3fee9858d294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499095_p124413401524"><a name="en-us_topic_0102499095_p124413401524"></a><a name="en-us_topic_0102499095_p124413401524"></a>External network address.</p>
</td>
</tr>
<tr id="row1892195682011"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p4741194813586"><a name="p4741194813586"></a><a name="p4741194813586"></a><span>external_otc</span></p>
</td>
<td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.2 "><p id="p107411448155811"><a name="p107411448155811"></a><a name="p107411448155811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p16741148135815"><a name="p16741148135815"></a><a name="p16741148135815"></a>Endpoint of the cluster to be accessed through API Gateway.</p>
</td>
</tr>
</tbody>
</table>

**Response example**:

```
    "kind": "Cluster",
    "apiVersion": "v3",
    "metadata": {
        "name": "mycluster",
        "uid": "365b5e05-846a-11ea-9fe6-0255ac101107",
        "creationTimestamp": "2020-04-22 07:23:50.157883 +0000 UTC",
        "updateTimestamp": "2020-05-08 03:10:12.174334 +0000 UTC"
    },
    "spec": {
        "type": "VirtualMachine",
        "flavor": "cce.s1.small",
        "version": "v1.15.6-r1",
        "description": "new description",
        "az": "eu-de-01",
        "ipv6enable": false,
        "supportIstio": true,
        "hostNetwork": {
            "vpc": "23d3725f-6ffe-400e-8fb6-b4f9a7b3e8c1",
            "subnet": "c90b3ce5-e1f1-4c87-a006-644d78846438",
            "SecurityGroup": "7bf2a95b-f41d-4187-9e72-d0a9a4de8e6d"
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
            "alpha.cce/fixPoolMask": "",
            "kubernetes.io/cpuManagerPolicy": "",
            "upgradefrom": ""
        },
        "kubernetesSvcIpRange": "10.247.0.0/16",
        "kubeProxyMode": "iptables"
    },
    "status": {
        "phase": "Available",
        "endpoints": [
            {
                "url": "https://192.168.0.61:5443",
                "type": "Internal"
            },
            {
                "url": "https://10.185.69.54:5443",
                "type": "External"
            }
{
                "url": "https://a140174a-2f3e-11e9-9f91-0255ac101405.cce.eu-de.otc.t-systems.com",
                "type": "external_otc"
            },
        ]
    }
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 10](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  10**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Information about the specified cluster is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

