# Listing All Node Pools in a Specified Cluster<a name="cce_02_0269"></a>

## Function<a name="section1686113493165"></a>

This API is used to obtain information about all node pools in a specified cluster.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/nodepools

[Table 1](#table2027961241820)  describes the parameters of this API.

**Table  1**  Description

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
<tr id="row1649094164612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p749015414462"><a name="p749015414462"></a><a name="p749015414462"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1849084134615"><a name="p1849084134615"></a><a name="p1849084134615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p8491141114617"><a name="p8491141114617"></a><a name="p8491141114617"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table18227235515)  describes the request parameters.

**Table  2**  Parameters in the request header

<a name="table18227235515"></a>
<table><thead align="left"><tr id="en-us_topic_0102499074_row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102499074_p115009545264"><a name="en-us_topic_0102499074_p115009545264"></a><a name="en-us_topic_0102499074_p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102499074_p175001547265"><a name="en-us_topic_0102499074_p175001547265"></a><a name="en-us_topic_0102499074_p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102499074_p16500154162611"><a name="en-us_topic_0102499074_p16500154162611"></a><a name="en-us_topic_0102499074_p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102499074_row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p69808112344"><a name="en-us_topic_0102499074_p69808112344"></a><a name="en-us_topic_0102499074_p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p3980111103414"><a name="en-us_topic_0102499074_p3980111103414"></a><a name="en-us_topic_0102499074_p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499074_p169801011203416"><a name="en-us_topic_0102499074_p169801011203416"></a><a name="en-us_topic_0102499074_p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="en-us_topic_0102499074_ul7385444163617"></a><a name="en-us_topic_0102499074_ul7385444163617"></a><ul id="en-us_topic_0102499074_ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="en-us_topic_0102499074_row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p105001654202618"><a name="en-us_topic_0102499074_p105001654202618"></a><a name="en-us_topic_0102499074_p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p20500954182618"><a name="en-us_topic_0102499074_p20500954182618"></a><a name="en-us_topic_0102499074_p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p18824197845"><a name="p18824197845"></a><a name="p18824197845"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

N/A

## Response<a name="section61819725020"></a>

**Response parameters**:

[Table 3](#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242)  describes response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0079616779_en-us_topic_0079614912_ref458774242"></a>
<table><thead align="left"><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row38450714"><th class="cellrowborder" valign="top" width="24.504950495049506%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.01980198019802%" id="mcps1.2.4.1.2"><p id="p1654581422214"><a name="p1654581422214"></a><a name="p1654581422214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.475247524752476%" id="mcps1.2.4.1.3"><p id="p125451914132219"><a name="p125451914132219"></a><a name="p125451914132219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row48220637"><td class="cellrowborder" valign="top" width="24.504950495049506%" headers="mcps1.2.4.1.1 "><p id="p44731858185518"><a name="p44731858185518"></a><a name="p44731858185518"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="23.01980198019802%" headers="mcps1.2.4.1.2 "><p id="p57145269553"><a name="p57145269553"></a><a name="p57145269553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. The value is fixed to <strong id="b743574523913"><a name="b743574523913"></a><a name="b743574523913"></a>List</strong>.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="24.504950495049506%" headers="mcps1.2.4.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="23.01980198019802%" headers="mcps1.2.4.1.2 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b57361554103911"><a name="b57361554103911"></a><a name="b57361554103911"></a>v3</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="24.504950495049506%" headers="mcps1.2.4.1.1 "><p id="p9274125074915"><a name="p9274125074915"></a><a name="p9274125074915"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="23.01980198019802%" headers="mcps1.2.4.1.2 "><p id="p77956277365"><a name="p77956277365"></a><a name="p77956277365"></a><a href="#table1644211019">items</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="52.475247524752476%" headers="mcps1.2.4.1.3 "><p id="p19274550164914"><a name="p19274550164914"></a><a name="p19274550164914"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **items**  field

<a name="table1644211019"></a>
<table><thead align="left"><tr id="row13647211510"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p26442115115"><a name="p26442115115"></a><a name="p26442115115"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p46415215116"><a name="p46415215116"></a><a name="p46415215116"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p1864192116112"><a name="p1864192116112"></a><a name="p1864192116112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3648211216"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p108391536181311"><a name="p108391536181311"></a><a name="p108391536181311"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1056311621716"><a name="p1056311621716"></a><a name="p1056311621716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p75781816181715"><a name="p75781816181715"></a><a name="p75781816181715"></a>API type. The value is fixed to <strong id="b4321115944110"><a name="b4321115944110"></a><a name="b4321115944110"></a>NodePool</strong>.</p>
</td>
</tr>
<tr id="row20802211618"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1785493610136"><a name="p1785493610136"></a><a name="p1785493610136"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p757801610179"><a name="p757801610179"></a><a name="p757801610179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p12578616151718"><a name="p12578616151718"></a><a name="p12578616151718"></a>API version. The value is fixed at <strong id="b1742215914427"><a name="b1742215914427"></a><a name="b1742215914427"></a>v3</strong>.</p>
</td>
</tr>
<tr id="row20809211716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1185493615135"><a name="p1185493615135"></a><a name="p1185493615135"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1334385071712"><a name="p1334385071712"></a><a name="p1334385071712"></a><a href="#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p10343195011177"><a name="p10343195011177"></a><a name="p10343195011177"></a>Node pool metadata.</p>
</td>
</tr>
<tr id="row12484123982118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6532732161518"><a name="p6532732161518"></a><a name="p6532732161518"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1436685371011"><a name="p1436685371011"></a><a name="p1436685371011"></a><a href="#table620623542313">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p173598507179"><a name="p173598507179"></a><a name="p173598507179"></a>Detailed node pool parameters.</p>
</td>
</tr>
<tr id="row1482918413216"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p1920413611513"><a name="p1920413611513"></a><a name="p1920413611513"></a><a href="#table5445161610255">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p9204133661512"><a name="p9204133661512"></a><a name="p9204133661512"></a>Node pool status.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **metadata**  field

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
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1977117411193"><a name="p1977117411193"></a><a name="p1977117411193"></a>Node name.</p>
</td>
</tr>
<tr id="row1169042813188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6786241193"><a name="p6786241193"></a><a name="p6786241193"></a>uid</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p14111627201917"><a name="p14111627201917"></a><a name="p14111627201917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1786447194"><a name="p1786447194"></a><a name="p1786447194"></a>Node ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the  **spec**  field

<a name="table620623542313"></a>
<table><thead align="left"><tr id="row520663552315"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p208332952414"><a name="p208332952414"></a><a name="p208332952414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.2"><p id="p1184914917244"><a name="p1184914917244"></a><a name="p1184914917244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p118491295245"><a name="p118491295245"></a><a name="p118491295245"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12895162713712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p88959272719"><a name="p88959272719"></a><a name="p88959272719"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p1389512271710"><a name="p1389512271710"></a><a name="p1389512271710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p289511273714"><a name="p289511273714"></a><a name="p289511273714"></a>Node Type. Currently, only VM nodes are supported.</p>
</td>
</tr>
<tr id="row199858145610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p210115875615"><a name="p210115875615"></a><a name="p210115875615"></a>initialNodeCount</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p1210105825615"><a name="p1210105825615"></a><a name="p1210105825615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p13101858205614"><a name="p13101858205614"></a><a name="p13101858205614"></a>Number of initialized nodes in the node pool.</p>
</td>
</tr>
<tr id="row12206153513232"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6206135142317"><a name="p6206135142317"></a><a name="p6206135142317"></a>nodeTemplate</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p13234357570"><a name="p13234357570"></a><a name="p13234357570"></a><a href="#table3150105216225">nodeTemplate</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p19206135162314"><a name="p19206135162314"></a><a name="p19206135162314"></a>Detailed parameters of the node pool template.</p>
</td>
</tr>
<tr id="row9206123518238"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12061135112315"><a name="p12061135112315"></a><a name="p12061135112315"></a>autoscaling</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p1920643502317"><a name="p1920643502317"></a><a name="p1920643502317"></a><a href="#table1472543502018">autoscaling</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p18206113582316"><a name="p18206113582316"></a><a name="p18206113582316"></a>Auto scaling parameters.</p>
</td>
</tr>
<tr id="row72396288246"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p823992812416"><a name="p823992812416"></a><a name="p823992812416"></a>nodeManagement</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p023912892419"><a name="p023912892419"></a><a name="p023912892419"></a><a href="#table1778609171919">nodeManagement</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p99811242122710"><a name="p99811242122710"></a><a name="p99811242122710"></a>Node management parameters.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the  **nodeTemplate **field

<a name="table3150105216225"></a>
<table><thead align="left"><tr id="row6150125212219"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p6731192632411"><a name="p6731192632411"></a><a name="p6731192632411"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.4.1.2"><p id="p27311226112410"><a name="p27311226112410"></a><a name="p27311226112410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.32%" id="mcps1.2.4.1.3"><p id="p15746192612248"><a name="p15746192612248"></a><a name="p15746192612248"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61507522224"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p333015583253"><a name="p333015583253"></a><a name="p333015583253"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p131508522226"><a name="p131508522226"></a><a name="p131508522226"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p71501352102211"><a name="p71501352102211"></a><a name="p71501352102211"></a>Node specifications.</p>
</td>
</tr>
<tr id="row12150165217223"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p181506529221"><a name="p181506529221"></a><a name="p181506529221"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p111505520222"><a name="p111505520222"></a><a name="p111505520222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p151501252102216"><a name="p151501252102216"></a><a name="p151501252102216"></a>AZ of the node.</p>
</td>
</tr>
<tr id="row1396733435612"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p096753412561"><a name="p096753412561"></a><a name="p096753412561"></a>os</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p4968934125616"><a name="p4968934125616"></a><a name="p4968934125616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p1054912457413"><a name="p1054912457413"></a><a name="p1054912457413"></a>Node OS.</p>
<a name="ul107124557553"></a><a name="ul107124557553"></a><ul id="ul107124557553"><li>Nodes in clusters of Kubernetes v1.11 or earlier support EulerOS 2.2.</li><li>Nodes in clusters of Kubernetes v1.13 or later support EulerOS 2.5.</li></ul>
</td>
</tr>
<tr id="row1150165232219"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p0393194582610"><a name="p0393194582610"></a><a name="p0393194582610"></a>login</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p1715065215226"><a name="p1715065215226"></a><a name="p1715065215226"></a><a href="#table10946114617286">login</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p212268155816"><a name="p212268155816"></a><a name="p212268155816"></a>Node login mode, which can be key pair or password.</p>
</td>
</tr>
<tr id="row111501952182214"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p0677490262"><a name="p0677490262"></a><a name="p0677490262"></a>rootVolume</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p16150052162211"><a name="p16150052162211"></a><a name="p16150052162211"></a><a href="#table1638317374346">rootVolume</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p15150125219222"><a name="p15150125219222"></a><a name="p15150125219222"></a>System disk parameters of the node.</p>
</td>
</tr>
<tr id="row1515016528222"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1859810527263"><a name="p1859810527263"></a><a name="p1859810527263"></a>dataVolumes</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p13150652142210"><a name="p13150652142210"></a><a name="p13150652142210"></a><a href="#table876891063712">dataVolumes</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p1915035219225"><a name="p1915035219225"></a><a name="p1915035219225"></a>Data disk parameters of the node.</p>
</td>
</tr>
<tr id="row215045242210"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p13629105762613"><a name="p13629105762613"></a><a name="p13629105762613"></a>publicIP</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p131501952192211"><a name="p131501952192211"></a><a name="p131501952192211"></a><a href="#table139179586343">publicIP</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p16919183682318"><a name="p16919183682318"></a><a name="p16919183682318"></a>EIP parameters of a node.</p>
</td>
</tr>
<tr id="row1920172414719"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p1292112474716"><a name="p1292112474716"></a><a name="p1292112474716"></a><span id="ph741675015303"><a name="ph741675015303"></a><a name="ph741675015303"></a>nodeNicSpec</span></p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p11921122418478"><a name="p11921122418478"></a><a name="p11921122418478"></a><a href="#table322873620312">nodeNicSpec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p218217915619"><a name="p218217915619"></a><a name="p218217915619"></a>Description about the node NIC.</p>
</td>
</tr>
<tr id="row2587175915438"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p258835914437"><a name="p258835914437"></a><a name="p258835914437"></a>billingMode</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p1558875914435"><a name="p1558875914435"></a><a name="p1558875914435"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p558875914438"><a name="p558875914438"></a><a name="p558875914438"></a>Billing mode of a node.</p>
<div class="note" id="note0702131124412"><a name="note0702131124412"></a><a name="note0702131124412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p77026184417"><a name="p77026184417"></a><a name="p77026184417"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row04202261820"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p642012610210"><a name="p642012610210"></a><a name="p642012610210"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p6420182613211"><a name="p6420182613211"></a><a name="p6420182613211"></a><a href="#table153332427337">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p1038263410216"><a name="p1038263410216"></a><a name="p1038263410216"></a>Extended parameter. Format: Key-value pair.</p>
</td>
</tr>
<tr id="row15875955114618"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p587515516469"><a name="p587515516469"></a><a name="p587515516469"></a>k8sTags</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p1487655534616"><a name="p1487655534616"></a><a name="p1487655534616"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p1932218501944"><a name="p1932218501944"></a><a name="p1932218501944"></a>Tag of a Kubernetes node.</p>
<p id="p5876455194611"><a name="p5876455194611"></a><a name="p5876455194611"></a>The format is key-value pair. The number of key-value pairs cannot exceed 20.</p>
<a name="ul102539423175"></a><a name="ul102539423175"></a><ul id="ul102539423175"><li><strong id="b26119351759"><a name="b26119351759"></a><a name="b26119351759"></a>Key</strong>: Enter 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain can be prefixed to a key and contain a maximum of 253 characters. Example DNS subdomain: example.com/my-key</li><li><strong id="b1541015592398"><a name="b1541015592398"></a><a name="b1541015592398"></a>Value</strong>: The value can be left blank or a string of 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed in the character string.</li></ul>
<p id="p1644615065413"><a name="p1644615065413"></a><a name="p1644615065413"></a>Example:</p>
<pre class="screen" id="screen851218415616"><a name="screen851218415616"></a><a name="screen851218415616"></a>"k8sTags": {
	"key": "value"
}</pre>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the  **login**  field

<a name="table10946114617286"></a>
<table><thead align="left"><tr id="row094684614289"><th class="cellrowborder" valign="top" width="22.73%" id="mcps1.2.4.1.1"><p id="p1544713542283"><a name="p1544713542283"></a><a name="p1544713542283"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.45%" id="mcps1.2.4.1.2"><p id="p0447145472811"><a name="p0447145472811"></a><a name="p0447145472811"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.82000000000001%" id="mcps1.2.4.1.3"><p id="p17447254132813"><a name="p17447254132813"></a><a name="p17447254132813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row69467461289"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.4.1.1 "><p id="p994654602818"><a name="p994654602818"></a><a name="p994654602818"></a>sshKey</p>
</td>
<td class="cellrowborder" valign="top" width="20.45%" headers="mcps1.2.4.1.2 "><p id="p2094614692816"><a name="p2094614692816"></a><a name="p2094614692816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.82000000000001%" headers="mcps1.2.4.1.3 "><p id="p5946104616288"><a name="p5946104616288"></a><a name="p5946104616288"></a>Name of the key pair used for node login. For details on how to create a key pair, see <a href="creating-a-key-pair.md">Creating a Key Pair</a>.</p>
</td>
</tr>
<tr id="row714415129439"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.4.1.1 "><p id="p11145012144318"><a name="p11145012144318"></a><a name="p11145012144318"></a>userPassword</p>
</td>
<td class="cellrowborder" valign="top" width="20.45%" headers="mcps1.2.4.1.2 "><p id="p6145412134310"><a name="p6145412134310"></a><a name="p6145412134310"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.82000000000001%" headers="mcps1.2.4.1.3 "><p id="p1414581284311"><a name="p1414581284311"></a><a name="p1414581284311"></a>Password used for node login.</p>
<div class="note" id="note8602141912241"><a name="note8602141912241"></a><a name="note8602141912241"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1260214190247"><a name="p1260214190247"></a><a name="p1260214190247"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  9**  Data structure of the  **rootVolume**  field

<a name="table1638317374346"></a>
<table><thead align="left"><tr id="row23831377343"><th class="cellrowborder" valign="top" width="23.13%" id="mcps1.2.4.1.1"><p id="p1229312516355"><a name="p1229312516355"></a><a name="p1229312516355"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.4%" id="mcps1.2.4.1.2"><p id="p182934513511"><a name="p182934513511"></a><a name="p182934513511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.47%" id="mcps1.2.4.1.3"><p id="p63081054356"><a name="p63081054356"></a><a name="p63081054356"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row263118285255"><td class="cellrowborder" valign="top" width="23.13%" headers="mcps1.2.4.1.1 "><p id="p4631728142516"><a name="p4631728142516"></a><a name="p4631728142516"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p463115285250"><a name="p463115285250"></a><a name="p463115285250"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p35816473259"><a name="p35816473259"></a><a name="p35816473259"></a>Disk type. For details, see the description of <strong id="b185814710254"><a name="b185814710254"></a><a name="b185814710254"></a>root_volume</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
<a name="ul1458114792517"></a><a name="ul1458114792517"></a><ul id="ul1458114792517"><li><strong id="b1558194742518"><a name="b1558194742518"></a><a name="b1558194742518"></a>SATA</strong>: common I/O disk type.</li><li><strong id="b859547132512"><a name="b859547132512"></a><a name="b859547132512"></a>SAS</strong>: high I/O disk type.</li><li><strong id="b17590476252"><a name="b17590476252"></a><a name="b17590476252"></a>SSD</strong>: ultra-high I/O disk type.</li></ul>
</td>
</tr>
<tr id="row15383637103414"><td class="cellrowborder" valign="top" width="23.13%" headers="mcps1.2.4.1.1 "><p id="p10383203712348"><a name="p10383203712348"></a><a name="p10383203712348"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p1738312379349"><a name="p1738312379349"></a><a name="p1738312379349"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p1875317289426"><a name="p1875317289426"></a><a name="p1875317289426"></a>Specifies the system disk size, in GB. The value ranges from 40 to 1024.</p>
</td>
</tr>
</tbody>
</table>

**Table  10**  Data structure of the  **dataVolumes**  field

<a name="table876891063712"></a>
<table><thead align="left"><tr id="row187686108377"><th class="cellrowborder" valign="top" width="23.13%" id="mcps1.2.4.1.1"><p id="p8768131063717"><a name="p8768131063717"></a><a name="p8768131063717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.4%" id="mcps1.2.4.1.2"><p id="p117681210123710"><a name="p117681210123710"></a><a name="p117681210123710"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.47%" id="mcps1.2.4.1.3"><p id="p1776813105373"><a name="p1776813105373"></a><a name="p1776813105373"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17769121013375"><td class="cellrowborder" valign="top" width="23.13%" headers="mcps1.2.4.1.1 "><p id="p476913104370"><a name="p476913104370"></a><a name="p476913104370"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p17693107374"><a name="p17693107374"></a><a name="p17693107374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p476941073711"><a name="p476941073711"></a><a name="p476941073711"></a>Disk type. </p>
<a name="ul1376951016373"></a><a name="ul1376951016373"></a><ul id="ul1376951016373"><li><strong id="b1776918109370"><a name="b1776918109370"></a><a name="b1776918109370"></a>SATA</strong>: common I/O disk type.</li><li><strong id="b1976931033715"><a name="b1976931033715"></a><a name="b1976931033715"></a>SAS</strong>: high I/O disk type.</li><li><strong id="b4769141083718"><a name="b4769141083718"></a><a name="b4769141083718"></a>SSD</strong>: ultra-high I/O disk type.</li></ul>
</td>
</tr>
<tr id="row1769131043719"><td class="cellrowborder" valign="top" width="23.13%" headers="mcps1.2.4.1.1 "><p id="p127691410173715"><a name="p127691410173715"></a><a name="p127691410173715"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p876971033717"><a name="p876971033717"></a><a name="p876971033717"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p1128183517418"><a name="p1128183517418"></a><a name="p1128183517418"></a>Specifies the data disk size, in GB. The value ranges from 100 to 32768.</p>
</td>
</tr>
<tr id="row1417275014222"><td class="cellrowborder" valign="top" width="23.13%" headers="mcps1.2.4.1.1 "><p id="p1117215508227"><a name="p1117215508227"></a><a name="p1117215508227"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.2 "><p id="p20172550152210"><a name="p20172550152210"></a><a name="p20172550152210"></a><a href="#table1392912448262">extendParam</a><span id="ph51764331270"><a name="ph51764331270"></a><a name="ph51764331270"></a> object</span></p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p1117255015226"><a name="p1117255015226"></a><a name="p1117255015226"></a><span id="ph226254862413"><a name="ph226254862413"></a><a name="ph226254862413"></a>Extended fields in the format of key-value pairs.</span></p>
</td>
</tr>
</tbody>
</table>

**Table  11**  Data structure of the  **extendParam**  field

<a name="table1392912448262"></a>
<table><thead align="left"><tr id="row1193094417264"><th class="cellrowborder" valign="top" width="23.25767423257674%" id="mcps1.2.4.1.1"><p id="p49302445262"><a name="p49302445262"></a><a name="p49302445262"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.768023197680233%" id="mcps1.2.4.1.2"><p id="p109307442266"><a name="p109307442266"></a><a name="p109307442266"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.97430256974302%" id="mcps1.2.4.1.3"><p id="p3930944162611"><a name="p3930944162611"></a><a name="p3930944162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20930544172616"><td class="cellrowborder" valign="top" width="23.25767423257674%" headers="mcps1.2.4.1.1 "><p id="p2777050102619"><a name="p2777050102619"></a><a name="p2777050102619"></a>useType</p>
</td>
<td class="cellrowborder" valign="top" width="19.768023197680233%" headers="mcps1.2.4.1.2 "><p id="p877535092610"><a name="p877535092610"></a><a name="p877535092610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.97430256974302%" headers="mcps1.2.4.1.3 "><p id="p4217121113227"><a name="p4217121113227"></a><a name="p4217121113227"></a>Specifies how the data disk is used.</p>
</td>
</tr>
</tbody>
</table>

**Table  12**  Data structure of the  **publicIP**  field

<a name="table139179586343"></a>
<table><thead align="left"><tr id="row16917115833416"><th class="cellrowborder" valign="top" width="23.25767423257674%" id="mcps1.2.4.1.1"><p id="p147361906402"><a name="p147361906402"></a><a name="p147361906402"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.768023197680233%" id="mcps1.2.4.1.2"><p id="p675120144011"><a name="p675120144011"></a><a name="p675120144011"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.97430256974302%" id="mcps1.2.4.1.3"><p id="p77514064014"><a name="p77514064014"></a><a name="p77514064014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14917155811345"><td class="cellrowborder" valign="top" width="23.25767423257674%" headers="mcps1.2.4.1.1 "><p id="p169171958153418"><a name="p169171958153418"></a><a name="p169171958153418"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="19.768023197680233%" headers="mcps1.2.4.1.2 "><p id="p1491785863418"><a name="p1491785863418"></a><a name="p1491785863418"></a><a href="#table135065714419">eip</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.97430256974302%" headers="mcps1.2.4.1.3 "><p id="p20917105813410"><a name="p20917105813410"></a><a name="p20917105813410"></a>EIP.</p>
<div class="notice" id="note1160713522814"><a name="note1160713522814"></a><a name="note1160713522814"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p186191852988"><a name="p186191852988"></a><a name="p186191852988"></a>The <strong id="b4485585571"><a name="b4485585571"></a><a name="b4485585571"></a>count</strong> and <strong id="b194845815716"><a name="b194845815716"></a><a name="b194845815716"></a>eip</strong> parameters must be set simultaneously.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  13**  Data structure of the  **eip**  field

<a name="table135065714419"></a>
<table><thead align="left"><tr id="row4350185774110"><th class="cellrowborder" valign="top" width="24.14%" id="mcps1.2.4.1.1"><p id="p162565424423"><a name="p162565424423"></a><a name="p162565424423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.54%" id="mcps1.2.4.1.2"><p id="p727315425421"><a name="p727315425421"></a><a name="p727315425421"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.32%" id="mcps1.2.4.1.3"><p id="p4273104254210"><a name="p4273104254210"></a><a name="p4273104254210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14350155784118"><td class="cellrowborder" valign="top" width="24.14%" headers="mcps1.2.4.1.1 "><p id="p5350165719413"><a name="p5350165719413"></a><a name="p5350165719413"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.4.1.2 "><p id="p1035013570419"><a name="p1035013570419"></a><a name="p1035013570419"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="56.32%" headers="mcps1.2.4.1.3 "><p id="p15350757104113"><a name="p15350757104113"></a><a name="p15350757104113"></a>Bandwidth parameters of the EIP.</p>
</td>
</tr>
</tbody>
</table>

**Table  14**  Data structure of the  **nodeNicSpec**  field

<a name="table322873620312"></a>
<table><thead align="left"><tr id="row132296364316"><th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.1"><p id="p622943603116"><a name="p622943603116"></a><a name="p622943603116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.61%" id="mcps1.2.4.1.2"><p id="p11229193612317"><a name="p11229193612317"></a><a name="p11229193612317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.24%" id="mcps1.2.4.1.3"><p id="p9229136163117"><a name="p9229136163117"></a><a name="p9229136163117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3229193616310"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p20278134019444"><a name="p20278134019444"></a><a name="p20278134019444"></a>primaryNic</p>
</td>
<td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.2.4.1.2 "><p id="p3276124012443"><a name="p3276124012443"></a><a name="p3276124012443"></a><a href="#table1054732719504">primaryNic</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="57.24%" headers="mcps1.2.4.1.3 "><p id="p327417407445"><a name="p327417407445"></a><a name="p327417407445"></a>Description about the primary NIC.</p>
</td>
</tr>
</tbody>
</table>

**Table  15**  Data structure of the  **primaryNic**  field

<a name="table1054732719504"></a>
<table><thead align="left"><tr id="row654742745013"><th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.1"><p id="p14547162711509"><a name="p14547162711509"></a><a name="p14547162711509"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.61%" id="mcps1.2.4.1.2"><p id="p193671951669"><a name="p193671951669"></a><a name="p193671951669"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.24%" id="mcps1.2.4.1.3"><p id="p1254762710508"><a name="p1254762710508"></a><a name="p1254762710508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row254872715011"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p1654818277503"><a name="p1654818277503"></a><a name="p1654818277503"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.2.4.1.2 "><p id="p5548327205011"><a name="p5548327205011"></a><a name="p5548327205011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.24%" headers="mcps1.2.4.1.3 "><p id="p18541105273310"><a name="p18541105273310"></a><a name="p18541105273310"></a>ID of the subnet to which the NIC belongs.</p>
</td>
</tr>
</tbody>
</table>

**Table  16**  Data structure of the  **extendParam**  field

<a name="table153332427337"></a>
<table><thead align="left"><tr id="row1333194263315"><th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.1"><p id="p1833364243316"><a name="p1833364243316"></a><a name="p1833364243316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.61%" id="mcps1.2.4.1.2"><p id="p73331942143320"><a name="p73331942143320"></a><a name="p73331942143320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.24%" id="mcps1.2.4.1.3"><p id="p93331942183314"><a name="p93331942183314"></a><a name="p93331942183314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1941456173613"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p594212564360"><a name="p594212564360"></a><a name="p594212564360"></a><span>maxPods</span></p>
</td>
<td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.2.4.1.2 "><p id="p1094255614368"><a name="p1094255614368"></a><a name="p1094255614368"></a><span>Integer</span></p>
</td>
<td class="cellrowborder" valign="top" width="57.24%" headers="mcps1.2.4.1.3 "><p id="p73419192371"><a name="p73419192371"></a><a name="p73419192371"></a>Maximum number of pods on the node.</p>
</td>
</tr>
</tbody>
</table>

**Table  17**  Data structure of the  **autoscaling**  field

<a name="table1472543502018"></a>
<table><thead align="left"><tr id="row574220353207"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="p6742103519207"><a name="p6742103519207"></a><a name="p6742103519207"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p20742103511206"><a name="p20742103511206"></a><a name="p20742103511206"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p97421935162010"><a name="p97421935162010"></a><a name="p97421935162010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14742113519208"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p13757103512202"><a name="p13757103512202"></a><a name="p13757103512202"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p19773103519202"><a name="p19773103519202"></a><a name="p19773103519202"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p1077323532019"><a name="p1077323532019"></a><a name="p1077323532019"></a>Whether to enable auto scaling.</p>
</td>
</tr>
<tr id="row33071322119"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p143071138211"><a name="p143071138211"></a><a name="p143071138211"></a>minNodeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p730723142112"><a name="p730723142112"></a><a name="p730723142112"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p9307123182115"><a name="p9307123182115"></a><a name="p9307123182115"></a>Minimum number of nodes allowed if auto scaling is enabled.</p>
</td>
</tr>
<tr id="row264916692110"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p564956102116"><a name="p564956102116"></a><a name="p564956102116"></a>maxNodeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p1964956122118"><a name="p1964956122118"></a><a name="p1964956122118"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p7874156112314"><a name="p7874156112314"></a><a name="p7874156112314"></a>Maximum number of nodes allowed if auto scaling is enabled.</p>
</td>
</tr>
</tbody>
</table>

**Table  18**  Data structure of the  **nodeManagement**  field

<a name="table1778609171919"></a>
<table><thead align="left"><tr id="row78023911913"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="p20802139131913"><a name="p20802139131913"></a><a name="p20802139131913"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p680279171914"><a name="p680279171914"></a><a name="p680279171914"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p780214941912"><a name="p780214941912"></a><a name="p780214941912"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row118171192197"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p8817149151911"><a name="p8817149151911"></a><a name="p8817149151911"></a>serverGroupReference</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p12817189181910"><a name="p12817189181910"></a><a name="p12817189181910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p138171696199"><a name="p138171696199"></a><a name="p138171696199"></a>Relationship with the IaaS cloud server group.</p>
</td>
</tr>
</tbody>
</table>

**Table  19**  Data structure of the  **status**  field

<a name="table5445161610255"></a>
<table><thead align="left"><tr id="row184611916162519"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.1"><p id="p19320122372514"><a name="p19320122372514"></a><a name="p19320122372514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p103201823182517"><a name="p103201823182517"></a><a name="p103201823182517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.3"><p id="p12336122362513"><a name="p12336122362513"></a><a name="p12336122362513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6461141613257"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p6461916102517"><a name="p6461916102517"></a><a name="p6461916102517"></a>currentNode</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p11461131692514"><a name="p11461131692514"></a><a name="p11461131692514"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p1346114167250"><a name="p1346114167250"></a><a name="p1346114167250"></a>Number of nodes in the node pool.</p>
</td>
</tr>
<tr id="row6112105414818"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.1 "><p id="p1411319547483"><a name="p1411319547483"></a><a name="p1411319547483"></a>phase</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p311315547483"><a name="p311315547483"></a><a name="p311315547483"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.3 "><p id="p18842161515251"><a name="p18842161515251"></a><a name="p18842161515251"></a>Node status.</p>
<a name="ul1196732915227"></a><a name="ul1196732915227"></a><ul id="ul1196732915227"><li><strong id="b12967529142214"><a name="b12967529142214"></a><a name="b12967529142214"></a>Synchronizing</strong>: Nodes are being synchronized.</li><li><strong id="b1296782910224"><a name="b1296782910224"></a><a name="b1296782910224"></a>Synchronized</strong>: Nodes have been synchronized.</li><li><strong id="b79671129182210"><a name="b79671129182210"></a><a name="b79671129182210"></a>SoldOut</strong>: All nodes have been sold out.</li><li><strong id="b1096717293222"><a name="b1096717293222"></a><a name="b1096717293222"></a>Deleting</strong>: Nodes are being deleted.</li><li><strong id="b096792919222"><a name="b096792919222"></a><a name="b096792919222"></a>Error</strong>: Nodes fail to be added.</li></ul>
<div class="note" id="note1693693618122"><a name="note1693693618122"></a><a name="note1693693618122"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1445370122317"><a name="p1445370122317"></a><a name="p1445370122317"></a>If <strong id="b245300122317"><a name="b245300122317"></a><a name="b245300122317"></a>phase</strong> is left blank, nodes are in the normal state.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Response example**:

```
{
    "kind": "List",
    "apiVersion": "v3",
    "items": [
        {
            "kind": "NodePool",
            "apiVersion": "v3",
            "metadata": {
                "name": "afaq-cluster-01-nodepool-01",
                "uid": "10a8eba4-4b29-11ea-8f1c-0255ac11160f"
            },
            "spec": {
                "type": "vm",
                "nodeTemplate": {
                    "flavor": "s3.large.2",
                    "az": "eu-de-02",
                    "os": "EulerOS 2.5",
                    "login": {
                        "sshKey": "KeyPair-demo",
                        "userPassword": {}
                    },
                    "rootVolume": {
                        "volumetype": "SATA",
                        "size": 40
                    },
                    "dataVolumes": [
                        {
                            "volumetype": "SATA",
                            "size": 100,
                            "extendParam": {
                                "useType": "docker"
                            }
                        }
                    ],
                    "publicIP": {
                        "eip": {
                            "bandwidth": {}
                        }
                    },
                    "billingMode": 0,
                    "nodeNicSpec": {
                        "primaryNic": {
                            "subnetId": "66bbd626-e7a6-4741-900b-242859acc434"
                        }
                    },
                    "extendParam": {
                        "maxPods": 110
                    },
                    "k8sTags": {
                        "cce.cloud.com/cce-nodepool": "afaq-cluster-01-nodepool-01"
                    }
                },
                "autoscaling": {
                    "enable": true,
                    "maxNodeCount": 1
                },
                "nodeManagement": {}
            },
            "status": {
                "phase": ""
            }
        },
        {
            "kind": "NodePool",
            "apiVersion": "v3",
            "metadata": {
                "name": "DefaultPool",
                "uid": "DefaultPool"
            },
            "spec": {
                "initialNodeCount": 3,
                "nodeTemplate": {
                    "flavor": "s2.xlarge.2",
                    "login": {
                        "sshKey": "KeyPair-demo",
                        "userPassword": {}
                    },
                    "rootVolume": {},
                    "publicIP": {
                        "eip": {
                            "bandwidth": {}
                        }
                    },
                    "nodeNicSpec": {
                        "primaryNic": {}
                    }
                },
                "autoscaling": {},
                "nodeManagement": {}
            },
            "status": {
                "currentNode": 3,
                "phase": ""
            }
        }
    ]
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 20](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  20**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13826175311229"><a name="p13826175311229"></a><a name="p13826175311229"></a>Information about all node pools in the cluster is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

