# Creating a Node<a name="cce_02_0242"></a>

## Function<a name="section1686113493165"></a>

This API is used to create a node in a specified cluster.

## URI<a name="section8403243161416"></a>

POST /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/nodes

[Table 1](#table2027961241820)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.030000000000001%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="67.97%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.97%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row1410610454440"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p4106245124416"><a name="p4106245124416"></a><a name="p4106245124416"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.4.1.2 "><p id="p11061345164415"><a name="p11061345164415"></a><a name="p11061345164415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.97%" headers="mcps1.2.4.1.3 "><p id="p15106445114416"><a name="p15106445114416"></a><a name="p15106445114416"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table2582312171119)  and  [Table 3](#table34052983203655)  describe the request parameters.

**Table  2**  Parameters in the request header

<a name="table2582312171119"></a>
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
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. The value is fixed at <strong id="b74472311522"><a name="b74472311522"></a><a name="b74472311522"></a>Node</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row15234185203655"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p2709192613559"><a name="p2709192613559"></a><a name="p2709192613559"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b560354017214"><a name="b560354017214"></a><a name="b560354017214"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1122635417553"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p144741558135518"><a name="p144741558135518"></a><a name="p144741558135518"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p112261154155517"><a name="p112261154155517"></a><a name="p112261154155517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p16227554165511"><a name="p16227554165511"></a><a name="p16227554165511"></a><a href="#table65041257514">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p102271654195515"><a name="p102271654195515"></a><a name="p102271654195515"></a>Node's metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row9619511127"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4785161212"><a name="p4785161212"></a><a name="p4785161212"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p97205171219"><a name="p97205171219"></a><a name="p97205171219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p67105119126"><a name="p67105119126"></a><a name="p67105119126"></a><a href="#table3150105216225">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p10785112129"><a name="p10785112129"></a><a name="p10785112129"></a>Detailed description of the node targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **metadata**  field

<a name="table65041257514"></a>
<table><thead align="left"><tr id="row1250482515512"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p11890655514"><a name="p11890655514"></a><a name="p11890655514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p289311553114"><a name="p289311553114"></a><a name="p289311553114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p128941055417"><a name="p128941055417"></a><a name="p128941055417"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p1289615519119"><a name="p1289615519119"></a><a name="p1289615519119"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row155045251758"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1289114562017"><a name="p1289114562017"></a><a name="p1289114562017"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p716614322018"><a name="p716614322018"></a><a name="p716614322018"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p9195144141410"><a name="p9195144141410"></a><a name="p9195144141410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1630772215148"><a name="p1630772215148"></a><a name="p1630772215148"></a>Node name.</p>
<div class="note" id="note71095339418"><a name="note71095339418"></a><a name="note71095339418"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9110173318412"><a name="p9110173318412"></a><a name="p9110173318412"></a>Enter 4 to 32 characters starting with a letter and not ending with a hyphen (-). Only lowercase letters, digits, and hyphens (-) are allowed.</p>
</div></div>
</td>
</tr>
<tr id="row1450412518519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p689194513209"><a name="p689194513209"></a><a name="p689194513209"></a>labels</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1886511394203"><a name="p1886511394203"></a><a name="p1886511394203"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p919624191418"><a name="p919624191418"></a><a name="p919624191418"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p354112509451"><a name="p354112509451"></a><a name="p354112509451"></a>CCE node label (not the native Kubernetes label).</p>
<p id="p1671617184505"><a name="p1671617184505"></a><a name="p1671617184505"></a>Labels are used to select objects that meet certain criteria. A label is a key-value pair.</p>
<p id="p93074221142"><a name="p93074221142"></a><a name="p93074221142"></a>Example:</p>
<pre class="screen" id="screen38331124185416"><a name="screen38331124185416"></a><a name="screen38331124185416"></a>"labels": {
  "key" : "value"
}</pre>
</td>
</tr>
<tr id="row8504102517519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p889194582016"><a name="p889194582016"></a><a name="p889194582016"></a>annotations</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p116764015202"><a name="p116764015202"></a><a name="p116764015202"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p15196841191420"><a name="p15196841191420"></a><a name="p15196841191420"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p131221035104512"><a name="p131221035104512"></a><a name="p131221035104512"></a>CCE node annotation in key-value pair format (not the native Kubernetes annotations).</p>
<p id="p678583015406"><a name="p678583015406"></a><a name="p678583015406"></a>Example:</p>
<pre class="screen" id="screen1163751913466"><a name="screen1163751913466"></a><a name="screen1163751913466"></a>"annotations": {
  "key1" : "value1",
  "key2" : "value2"
}</pre>
<div class="note" id="note1558316436525"><a name="note1558316436525"></a><a name="note1558316436525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p258444365217"><a name="p258444365217"></a><a name="p258444365217"></a><strong id="b13990160855"><a name="b13990160855"></a><a name="b13990160855"></a>Annotations</strong> are not used to identify or select objects. The metadata in <strong id="b19661658155112"><a name="b19661658155112"></a><a name="b19661658155112"></a>Annotations</strong> may be small or large, structured or unstructured, and may include characters that are not allowed in labels.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **spec**  field

<a name="table3150105216225"></a>
<table><thead align="left"><tr id="row6150125212219"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p6731192632411"><a name="p6731192632411"></a><a name="p6731192632411"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p1373132617245"><a name="p1373132617245"></a><a name="p1373132617245"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p27311226112410"><a name="p27311226112410"></a><a name="p27311226112410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p15746192612248"><a name="p15746192612248"></a><a name="p15746192612248"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61507522224"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p333015583253"><a name="p333015583253"></a><a name="p333015583253"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p18150115219222"><a name="p18150115219222"></a><a name="p18150115219222"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p131508522226"><a name="p131508522226"></a><a name="p131508522226"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p71501352102211"><a name="p71501352102211"></a><a name="p71501352102211"></a>Node specifications. For details, see the description of the <strong id="b0244615535"><a name="b0244615535"></a><a name="b0244615535"></a>flavorRef</strong> parameter in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
<div class="note" id="note148961115125815"><a name="note148961115125815"></a><a name="note148961115125815"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1389415451812"><a name="p1389415451812"></a><a name="p1389415451812"></a>When adding a BMS node, check whether the flavor of the node to be added supports local disks. If local disks are not supported, add at least one 100 GB EVS disk.</p>
</div></div>
</td>
</tr>
<tr id="row12150165217223"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p181506529221"><a name="p181506529221"></a><a name="p181506529221"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p197861438122719"><a name="p197861438122719"></a><a name="p197861438122719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p111505520222"><a name="p111505520222"></a><a name="p111505520222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p151501252102216"><a name="p151501252102216"></a><a name="p151501252102216"></a>AZ of the node. For details, see the description of the <strong id="b214031310212"><a name="b214031310212"></a><a name="b214031310212"></a>availability_zone</strong> parameter in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
</td>
</tr>
<tr id="row1396733435612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p096753412561"><a name="p096753412561"></a><a name="p096753412561"></a>os</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p14968143425612"><a name="p14968143425612"></a><a name="p14968143425612"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p4968934125616"><a name="p4968934125616"></a><a name="p4968934125616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1054912457413"><a name="p1054912457413"></a><a name="p1054912457413"></a>Node OS.</p>
<a name="ul3549345241"></a><a name="ul3549345241"></a><ul id="ul3549345241"><li>Nodes in clusters of Kubernetes v1.11 or earlier support EulerOS 2.2.</li><li>Nodes in clusters of Kubernetes v1.13 or later support EulerOS 2.5.</li></ul>
</td>
</tr>
<tr id="row6201163842315"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1420217389236"><a name="p1420217389236"></a><a name="p1420217389236"></a>dedicatedHostId</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1020273822317"><a name="p1020273822317"></a><a name="p1020273822317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p17202238192311"><a name="p17202238192311"></a><a name="p17202238192311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1657345220513"><a name="p1657345220513"></a><a name="p1657345220513"></a>ID of the dedicated host to which nodes will be scheduled.</p>
</td>
</tr>
<tr id="row1150165232219"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p0393194582610"><a name="p0393194582610"></a><a name="p0393194582610"></a>login</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p8150105252219"><a name="p8150105252219"></a><a name="p8150105252219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1715065215226"><a name="p1715065215226"></a><a name="p1715065215226"></a><a href="#table10946114617286">login</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p41509523227"><a name="p41509523227"></a><a name="p41509523227"></a>Node login mode, which can be key pair or password.</p>
</td>
</tr>
<tr id="row111501952182214"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p0677490262"><a name="p0677490262"></a><a name="p0677490262"></a>rootVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p51501552132210"><a name="p51501552132210"></a><a name="p51501552132210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p16150052162211"><a name="p16150052162211"></a><a name="p16150052162211"></a><a href="#table1359314517">rootVolume</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p15150125219222"><a name="p15150125219222"></a><a name="p15150125219222"></a>System disk parameters of the node.</p>
</td>
</tr>
<tr id="row1515016528222"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1859810527263"><a name="p1859810527263"></a><a name="p1859810527263"></a>dataVolumes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p161501852152218"><a name="p161501852152218"></a><a name="p161501852152218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p13150652142210"><a name="p13150652142210"></a><a name="p13150652142210"></a><a href="#table876891063712">dataVolumes</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1915035219225"><a name="p1915035219225"></a><a name="p1915035219225"></a>Data disk parameters of the node.</p>
</td>
</tr>
<tr id="row215045242210"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p13629105762613"><a name="p13629105762613"></a><a name="p13629105762613"></a>publicIP</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p3150135292215"><a name="p3150135292215"></a><a name="p3150135292215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p131501952192211"><a name="p131501952192211"></a><a name="p131501952192211"></a><a href="#table139179586343">publicIP</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p51501752122215"><a name="p51501752122215"></a><a name="p51501752122215"></a>EIP used by the node to access public networks.</p>
</td>
</tr>
<tr id="row13868164643712"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1486984693719"><a name="p1486984693719"></a><a name="p1486984693719"></a><span id="ph1930412532375"><a name="ph1930412532375"></a><a name="ph1930412532375"></a>billingMode</span></p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1786984616373"><a name="p1786984616373"></a><a name="p1786984616373"></a><span id="ph16303145623719"><a name="ph16303145623719"></a><a name="ph16303145623719"></a>No</span></p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p98699462378"><a name="p98699462378"></a><a name="p98699462378"></a><span id="ph191141193818"><a name="ph191141193818"></a><a name="ph191141193818"></a>Integer</span></p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p558875914438"><a name="p558875914438"></a><a name="p558875914438"></a>Billing mode of a node.</p>
<div class="note" id="note0702131124412"><a name="note0702131124412"></a><a name="note0702131124412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p77026184417"><a name="p77026184417"></a><a name="p77026184417"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row133895911576"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p13898935713"><a name="p13898935713"></a><a name="p13898935713"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1338916913573"><a name="p1338916913573"></a><a name="p1338916913573"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p938920995713"><a name="p938920995713"></a><a name="p938920995713"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1714112632020"><a name="p1714112632020"></a><a name="p1714112632020"></a>Number of nodes to be created in a batch. The value must be a positive integer greater than or equal to 1.</p>
</td>
</tr>
<tr id="row1920172414719"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1292112474716"><a name="p1292112474716"></a><a name="p1292112474716"></a><span id="ph741675015303"><a name="ph741675015303"></a><a name="ph741675015303"></a>nodeNicSpec</span></p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p29211924104714"><a name="p29211924104714"></a><a name="p29211924104714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p11921122418478"><a name="p11921122418478"></a><a name="p11921122418478"></a><a href="#table322873620312">nodeNicSpec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p218217915619"><a name="p218217915619"></a><a name="p218217915619"></a>Description about the node NIC.</p>
</td>
</tr>
<tr id="row04202261820"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p642012610210"><a name="p642012610210"></a><a name="p642012610210"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p194201026527"><a name="p194201026527"></a><a name="p194201026527"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p6420182613211"><a name="p6420182613211"></a><a name="p6420182613211"></a><a href="#table153332427337">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1038263410216"><a name="p1038263410216"></a><a name="p1038263410216"></a>Extended parameter. Format: Key-value pair.</p>
</td>
</tr>
<tr id="row550282612218"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p145037262222"><a name="p145037262222"></a><a name="p145037262222"></a>userTags</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p45031426132210"><a name="p45031426132210"></a><a name="p45031426132210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p9503202618229"><a name="p9503202618229"></a><a name="p9503202618229"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p7534153516413"><a name="p7534153516413"></a><a name="p7534153516413"></a>Tag of a VM.</p>
<p id="p336932192717"><a name="p336932192717"></a><a name="p336932192717"></a>The format is key-value pair. The number of key-value pairs cannot exceed 20.</p>
<a name="ul89974419513"></a><a name="ul89974419513"></a><ul id="ul89974419513"><li><strong id="b17052059141212"><a name="b17052059141212"></a><a name="b17052059141212"></a>Key</strong>: Only letters, digits, hyphens (-), underscores (_), and at signs (@) are supported.</li><li><strong id="b251321101314"><a name="b251321101314"></a><a name="b251321101314"></a>Value</strong>: Only letters, digits, hyphens (-), underscores (_), and at signs (@) are supported.</li></ul>
<p id="p109975417513"><a name="p109975417513"></a><a name="p109975417513"></a>Example:</p>
<pre class="screen" id="screen1963243983116"><a name="screen1963243983116"></a><a name="screen1963243983116"></a>"userTags": [
            {
                "key": "tag1",
                "value": "aaaa"
            },
            {
                "key": "tag2",
                "value": "bbbb"
            }</pre>
</td>
</tr>
<tr id="row15875955114618"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p587515516469"><a name="p587515516469"></a><a name="p587515516469"></a>k8sTags</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p687685520467"><a name="p687685520467"></a><a name="p687685520467"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1487655534616"><a name="p1487655534616"></a><a name="p1487655534616"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1932218501944"><a name="p1932218501944"></a><a name="p1932218501944"></a>Tag of a Kubernetes node.</p>
<p id="p5876455194611"><a name="p5876455194611"></a><a name="p5876455194611"></a>The format is key-value pair. The number of key-value pairs cannot exceed 20.</p>
<a name="ul102539423175"></a><a name="ul102539423175"></a><ul id="ul102539423175"><li><strong id="b26119351759"><a name="b26119351759"></a><a name="b26119351759"></a>Key</strong>: Enter 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain can be prefixed to a key and contain a maximum of 253 characters. Example DNS subdomain: example.com/my-key</li><li><strong id="b1541015592398"><a name="b1541015592398"></a><a name="b1541015592398"></a>Value</strong>: The value can be left blank or a string of 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed in the character string.</li></ul>
<p id="p1644615065413"><a name="p1644615065413"></a><a name="p1644615065413"></a>Example:</p>
<pre class="screen" id="screen851218415616"><a name="screen851218415616"></a><a name="screen851218415616"></a>"k8sTags": {
	"key": "value"
}</pre>
</td>
</tr>
<tr id="row17268125919467"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1026914596460"><a name="p1026914596460"></a><a name="p1026914596460"></a>taints</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1926945954612"><a name="p1926945954612"></a><a name="p1926945954612"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1612932717412"><a name="p1612932717412"></a><a name="p1612932717412"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><div class="p" id="p81066511617"><a name="p81066511617"></a><a name="p81066511617"></a>You can add taints to created nodes to configure anti-affinity. Each taint contains the following parameters:<a name="ul17274222121015"></a><a name="ul17274222121015"></a><ul id="ul17274222121015"><li><strong id="b14101664369"><a name="b14101664369"></a><a name="b14101664369"></a>Key</strong>: A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</li><li><strong id="b1538010103366"><a name="b1538010103366"></a><a name="b1538010103366"></a>Value</strong>: A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</li><li><strong id="b23151718366"><a name="b23151718366"></a><a name="b23151718366"></a>Effect</strong>: Available options are <strong id="b13216173361"><a name="b13216173361"></a><a name="b13216173361"></a>NoSchedule</strong>, <strong id="b1933201719369"><a name="b1933201719369"></a><a name="b1933201719369"></a>PreferNoSchedule</strong>, and <strong id="b3345173368"><a name="b3345173368"></a><a name="b3345173368"></a>NoExecute</strong>.</li></ul>
</div>
<p id="p98321812817"><a name="p98321812817"></a><a name="p98321812817"></a>Example:</p>
<pre class="screen" id="screen19127268812"><a name="screen19127268812"></a><a name="screen19127268812"></a>"taints": [{
	"key": "status",
	"value": "unavailable",
	"effect": "NoSchedule"
}, {
	"key": "looks",
	"value": "bad",
	"effect": "NoSchedule"
}]</pre>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the nodeNicSpec field

<a name="table322873620312"></a>
<table><thead align="left"><tr id="row132296364316"><th class="cellrowborder" valign="top" width="18.970588235294116%" id="mcps1.2.5.1.1"><p id="p622943603116"><a name="p622943603116"></a><a name="p622943603116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.362745098039214%" id="mcps1.2.5.1.2"><p id="p42290361314"><a name="p42290361314"></a><a name="p42290361314"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.64705882352941%" id="mcps1.2.5.1.3"><p id="p11229193612317"><a name="p11229193612317"></a><a name="p11229193612317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01960784313725%" id="mcps1.2.5.1.4"><p id="p9229136163117"><a name="p9229136163117"></a><a name="p9229136163117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3229193616310"><td class="cellrowborder" valign="top" width="18.970588235294116%" headers="mcps1.2.5.1.1 "><p id="p20278134019444"><a name="p20278134019444"></a><a name="p20278134019444"></a>primaryNic</p>
</td>
<td class="cellrowborder" valign="top" width="14.362745098039214%" headers="mcps1.2.5.1.2 "><p id="p4277340184413"><a name="p4277340184413"></a><a name="p4277340184413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p3276124012443"><a name="p3276124012443"></a><a name="p3276124012443"></a><a href="#table1054732719504">primaryNic</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p327417407445"><a name="p327417407445"></a><a name="p327417407445"></a>Description about the primary NIC.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the primaryNic field

<a name="table1054732719504"></a>
<table><thead align="left"><tr id="row654742745013"><th class="cellrowborder" valign="top" width="18.970588235294116%" id="mcps1.2.5.1.1"><p id="p14547162711509"><a name="p14547162711509"></a><a name="p14547162711509"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.362745098039214%" id="mcps1.2.5.1.2"><p id="p55471427175011"><a name="p55471427175011"></a><a name="p55471427175011"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.64705882352941%" id="mcps1.2.5.1.3"><p id="p193671951669"><a name="p193671951669"></a><a name="p193671951669"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01960784313725%" id="mcps1.2.5.1.4"><p id="p1254762710508"><a name="p1254762710508"></a><a name="p1254762710508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row254872715011"><td class="cellrowborder" valign="top" width="18.970588235294116%" headers="mcps1.2.5.1.1 "><p id="p1654818277503"><a name="p1654818277503"></a><a name="p1654818277503"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="14.362745098039214%" headers="mcps1.2.5.1.2 "><p id="p2054842713508"><a name="p2054842713508"></a><a name="p2054842713508"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p5548327205011"><a name="p5548327205011"></a><a name="p5548327205011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p18541105273310"><a name="p18541105273310"></a><a name="p18541105273310"></a>ID of the subnet to which the NIC belongs.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the extendParam field

<a name="table153332427337"></a>
<table><thead align="left"><tr id="row1333194263315"><th class="cellrowborder" valign="top" width="18.970588235294116%" id="mcps1.2.5.1.1"><p id="p1833364243316"><a name="p1833364243316"></a><a name="p1833364243316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.362745098039214%" id="mcps1.2.5.1.2"><p id="p173331842193317"><a name="p173331842193317"></a><a name="p173331842193317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.64705882352941%" id="mcps1.2.5.1.3"><p id="p73331942143320"><a name="p73331942143320"></a><a name="p73331942143320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01960784313725%" id="mcps1.2.5.1.4"><p id="p93331942183314"><a name="p93331942183314"></a><a name="p93331942183314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1941456173613"><td class="cellrowborder" valign="top" width="18.970588235294116%" headers="mcps1.2.5.1.1 "><p id="p594212564360"><a name="p594212564360"></a><a name="p594212564360"></a><span>maxPods</span></p>
</td>
<td class="cellrowborder" valign="top" width="14.362745098039214%" headers="mcps1.2.5.1.2 "><p id="p149421756133614"><a name="p149421756133614"></a><a name="p149421756133614"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p1094255614368"><a name="p1094255614368"></a><a name="p1094255614368"></a><span>Integer</span></p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p73419192371"><a name="p73419192371"></a><a name="p73419192371"></a>Maximum number of pods on the node.</p>
</td>
</tr>
<tr id="row9333104293318"><td class="cellrowborder" valign="top" width="18.970588235294116%" headers="mcps1.2.5.1.1 "><p id="p203338425338"><a name="p203338425338"></a><a name="p203338425338"></a>alpha.cce/preInstall</p>
</td>
<td class="cellrowborder" valign="top" width="14.362745098039214%" headers="mcps1.2.5.1.2 "><p id="p1033318426332"><a name="p1033318426332"></a><a name="p1033318426332"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p15333164220338"><a name="p15333164220338"></a><a name="p15333164220338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p3333154263315"><a name="p3333154263315"></a><a name="p3333154263315"></a>Script required before the installation</p>
<div class="note" id="note137011215354"><a name="note137011215354"></a><a name="note137011215354"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p270172113358"><a name="p270172113358"></a><a name="p270172113358"></a>The input value must be encoded using Base64. (Command: <strong id="b10861022802"><a name="b10861022802"></a><a name="b10861022802"></a>echo -n "<em id="i155831735103"><a name="i155831735103"></a><a name="i155831735103"></a>Content to be encoded</em>" | base64</strong>)</p>
</div></div>
</td>
</tr>
<tr id="row5367951183319"><td class="cellrowborder" valign="top" width="18.970588235294116%" headers="mcps1.2.5.1.1 "><p id="p173671051153311"><a name="p173671051153311"></a><a name="p173671051153311"></a>alpha.cce/postInstall</p>
</td>
<td class="cellrowborder" valign="top" width="14.362745098039214%" headers="mcps1.2.5.1.2 "><p id="p163671751203313"><a name="p163671751203313"></a><a name="p163671751203313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p103676513337"><a name="p103676513337"></a><a name="p103676513337"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p53689516336"><a name="p53689516336"></a><a name="p53689516336"></a>Script required after the installation</p>
<div class="note" id="note19617843103510"><a name="note19617843103510"></a><a name="note19617843103510"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1161734320357"><a name="p1161734320357"></a><a name="p1161734320357"></a>The input value must be encoded using Base64. (Command: <strong id="b1169154420012"><a name="b1169154420012"></a><a name="b1169154420012"></a>echo -n "<em id="i95364410019"><a name="i95364410019"></a><a name="i95364410019"></a>Content to be encoded</em>" | base64</strong>)</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  9**  Data structure of the  **login**  field

<a name="table10946114617286"></a>
<table><thead align="left"><tr id="row094684614289"><th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.1"><p id="p1544713542283"><a name="p1544713542283"></a><a name="p1544713542283"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.725490196078432%" id="mcps1.2.5.1.2"><p id="p8447155482810"><a name="p8447155482810"></a><a name="p8447155482810"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.64705882352941%" id="mcps1.2.5.1.3"><p id="p0447145472811"><a name="p0447145472811"></a><a name="p0447145472811"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01960784313725%" id="mcps1.2.5.1.4"><p id="p17447254132813"><a name="p17447254132813"></a><a name="p17447254132813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row69467461289"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="p994654602818"><a name="p994654602818"></a><a name="p994654602818"></a>sshKey</p>
</td>
<td class="cellrowborder" valign="top" width="13.725490196078432%" headers="mcps1.2.5.1.2 "><p id="p1694654614287"><a name="p1694654614287"></a><a name="p1694654614287"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p2094614692816"><a name="p2094614692816"></a><a name="p2094614692816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p5946104616288"><a name="p5946104616288"></a><a name="p5946104616288"></a>Name of the key pair used for node login. For details on how to create a key pair, see <a href="creating-a-key-pair.md">Creating a Key Pair</a>.</p>
</td>
</tr>
<tr id="row359392111369"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="p159412211365"><a name="p159412211365"></a><a name="p159412211365"></a>userPassword</p>
</td>
<td class="cellrowborder" valign="top" width="13.725490196078432%" headers="mcps1.2.5.1.2 "><p id="p4594221193618"><a name="p4594221193618"></a><a name="p4594221193618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p659482143614"><a name="p659482143614"></a><a name="p659482143614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="p059411218363"><a name="p059411218363"></a><a name="p059411218363"></a>Password used for node login.</p>
<div class="note" id="note19491185043612"><a name="note19491185043612"></a><a name="note19491185043612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19491115003619"><a name="p19491115003619"></a><a name="p19491115003619"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  10**  Data structure of the  **rootVolume**  field

<a name="table1359314517"></a>
<table><thead align="left"><tr id="row86123184512"><th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.2.5.1.1"><p id="p5603104518"><a name="p5603104518"></a><a name="p5603104518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.07%" id="mcps1.2.5.1.2"><p id="p335493817453"><a name="p335493817453"></a><a name="p335493817453"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.5.1.3"><p id="p146532454"><a name="p146532454"></a><a name="p146532454"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.22%" id="mcps1.2.5.1.4"><p id="p765334510"><a name="p765334510"></a><a name="p765334510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row263118285255"><td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.1 "><p id="p4631728142516"><a name="p4631728142516"></a><a name="p4631728142516"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="13.07%" headers="mcps1.2.5.1.2 "><p id="p235483818451"><a name="p235483818451"></a><a name="p235483818451"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p463115285250"><a name="p463115285250"></a><a name="p463115285250"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.22%" headers="mcps1.2.5.1.4 "><p id="p35816473259"><a name="p35816473259"></a><a name="p35816473259"></a>Disk type. For details, see the description of <strong id="b185814710254"><a name="b185814710254"></a><a name="b185814710254"></a>root_volume</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
<a name="ul1458114792517"></a><a name="ul1458114792517"></a><ul id="ul1458114792517"><li><strong id="b1558194742518"><a name="b1558194742518"></a><a name="b1558194742518"></a>SATA</strong>: common I/O disk type.</li><li><strong id="b859547132512"><a name="b859547132512"></a><a name="b859547132512"></a>SAS</strong>: high I/O disk type.</li><li><strong id="b17590476252"><a name="b17590476252"></a><a name="b17590476252"></a>SSD</strong>: ultra-high I/O disk type.</li></ul>
</td>
</tr>
<tr id="row19703174511"><td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.1 "><p id="p1971731452"><a name="p1971731452"></a><a name="p1971731452"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="13.07%" headers="mcps1.2.5.1.2 "><p id="p1835412386451"><a name="p1835412386451"></a><a name="p1835412386451"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p2071304513"><a name="p2071304513"></a><a name="p2071304513"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.22%" headers="mcps1.2.5.1.4 "><p id="p1875317289426"><a name="p1875317289426"></a><a name="p1875317289426"></a>Specifies the system disk size, in GB. The value ranges from 40 to 1024.</p>
</td>
</tr>
</tbody>
</table>

**Table  11**  Data structure of the  **dataVolumes**  field

<a name="table876891063712"></a>
<table><thead align="left"><tr id="row187686108377"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.5.1.1"><p id="p8768131063717"><a name="p8768131063717"></a><a name="p8768131063717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.43%" id="mcps1.2.5.1.2"><p id="p1638419435458"><a name="p1638419435458"></a><a name="p1638419435458"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.5.1.3"><p id="p117681210123710"><a name="p117681210123710"></a><a name="p117681210123710"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.22%" id="mcps1.2.5.1.4"><p id="p1776813105373"><a name="p1776813105373"></a><a name="p1776813105373"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17769121013375"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.5.1.1 "><p id="p476913104370"><a name="p476913104370"></a><a name="p476913104370"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="12.43%" headers="mcps1.2.5.1.2 "><p id="p63841643204511"><a name="p63841643204511"></a><a name="p63841643204511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p17693107374"><a name="p17693107374"></a><a name="p17693107374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.22%" headers="mcps1.2.5.1.4 "><p id="p476941073711"><a name="p476941073711"></a><a name="p476941073711"></a>Disk type. For details, see the description of <strong id="b476911100378"><a name="b476911100378"></a><a name="b476911100378"></a>data_volumes</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
<a name="ul1376951016373"></a><a name="ul1376951016373"></a><ul id="ul1376951016373"><li><strong id="b1776918109370"><a name="b1776918109370"></a><a name="b1776918109370"></a>SATA</strong>: common I/O disk type.</li><li><strong id="b1976931033715"><a name="b1976931033715"></a><a name="b1976931033715"></a>SAS</strong>: high I/O disk type.</li><li><strong id="b4769141083718"><a name="b4769141083718"></a><a name="b4769141083718"></a>SSD</strong>: ultra-high I/O disk type.</li></ul>
</td>
</tr>
<tr id="row1769131043719"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.5.1.1 "><p id="p127691410173715"><a name="p127691410173715"></a><a name="p127691410173715"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="12.43%" headers="mcps1.2.5.1.2 "><p id="p3384843164515"><a name="p3384843164515"></a><a name="p3384843164515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p876971033717"><a name="p876971033717"></a><a name="p876971033717"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.22%" headers="mcps1.2.5.1.4 "><p id="p1128183517418"><a name="p1128183517418"></a><a name="p1128183517418"></a>Specifies the data disk size, in GB. The value ranges from 100 to 32768.</p>
</td>
</tr>
</tbody>
</table>

**Table  12**  Data structure of the  **publicIP**  field

<a name="table139179586343"></a>
<table><thead align="left"><tr id="row16917115833416"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p147361906402"><a name="p147361906402"></a><a name="p147361906402"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p773630144015"><a name="p773630144015"></a><a name="p773630144015"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p675120144011"><a name="p675120144011"></a><a name="p675120144011"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p77514064014"><a name="p77514064014"></a><a name="p77514064014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row139177581341"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p79179585341"><a name="p79179585341"></a><a name="p79179585341"></a>ids</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p159172586348"><a name="p159172586348"></a><a name="p159172586348"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p69201306371"><a name="p69201306371"></a><a name="p69201306371"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p159171586349"><a name="p159171586349"></a><a name="p159171586349"></a>List of IDs of the existing EIPs.</p>
<div class="notice" id="note1048219251376"><a name="note1048219251376"></a><a name="note1048219251376"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p14831251077"><a name="p14831251077"></a><a name="p14831251077"></a>If <strong id="b164005813575"><a name="b164005813575"></a><a name="b164005813575"></a>ids</strong> is set, you do not need to set <strong id="b74015865711"><a name="b74015865711"></a><a name="b74015865711"></a>count</strong> and <strong id="b94085865712"><a name="b94085865712"></a><a name="b94085865712"></a>eip</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row291745883414"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1691715585341"><a name="p1691715585341"></a><a name="p1691715585341"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1091755873415"><a name="p1091755873415"></a><a name="p1091755873415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p15917358153417"><a name="p15917358153417"></a><a name="p15917358153417"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p8917185813344"><a name="p8917185813344"></a><a name="p8917185813344"></a>Number of EIPs to be dynamically created.</p>
<div class="notice" id="note1619810214816"><a name="note1619810214816"></a><a name="note1619810214816"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p720116214812"><a name="p720116214812"></a><a name="p720116214812"></a>The <strong id="b444155895713"><a name="b444155895713"></a><a name="b444155895713"></a>count</strong> and <strong id="b1544195819572"><a name="b1544195819572"></a><a name="b1544195819572"></a>eip</strong> parameters must be set simultaneously.</p>
</div></div>
</td>
</tr>
<tr id="row14917155811345"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p169171958153418"><a name="p169171958153418"></a><a name="p169171958153418"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p9917135853415"><a name="p9917135853415"></a><a name="p9917135853415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p1491785863418"><a name="p1491785863418"></a><a name="p1491785863418"></a><a href="#table135065714419">eip</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p20917105813410"><a name="p20917105813410"></a><a name="p20917105813410"></a>EIP.</p>
<div class="notice" id="note1160713522814"><a name="note1160713522814"></a><a name="note1160713522814"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p186191852988"><a name="p186191852988"></a><a name="p186191852988"></a>The <strong id="b4485585571"><a name="b4485585571"></a><a name="b4485585571"></a>count</strong> and <strong id="b194845815716"><a name="b194845815716"></a><a name="b194845815716"></a>eip</strong> parameters must be set simultaneously.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If no EIP has been created, configure  **count**  and  **eip**. The system will automatically create EIPs based on  **count**  and  **eip**.  

**Table  13**  Data structure of the  **eip**  field

<a name="table135065714419"></a>
<table><thead align="left"><tr id="row4350185774110"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p162565424423"><a name="p162565424423"></a><a name="p162565424423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p12566427429"><a name="p12566427429"></a><a name="p12566427429"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p727315425421"><a name="p727315425421"></a><a name="p727315425421"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p4273104254210"><a name="p4273104254210"></a><a name="p4273104254210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10350145754113"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p835013575413"><a name="p835013575413"></a><a name="p835013575413"></a>iptype</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p2035010573419"><a name="p2035010573419"></a><a name="p2035010573419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p16350205710419"><a name="p16350205710419"></a><a name="p16350205710419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p2035016576417"><a name="p2035016576417"></a><a name="p2035016576417"></a>EIP type. For details, see the description of the <strong id="b12315155585520"><a name="b12315155585520"></a><a name="b12315155585520"></a>iptype</strong> parameter in the <strong id="b63155559559"><a name="b63155559559"></a><a name="b63155559559"></a>eip</strong> field in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Data Structure for Creating ECSs</a>.</p>
</td>
</tr>
<tr id="row14350155784118"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p5350165719413"><a name="p5350165719413"></a><a name="p5350165719413"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p14350105734113"><a name="p14350105734113"></a><a name="p14350105734113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p1035013570419"><a name="p1035013570419"></a><a name="p1035013570419"></a><a href="#table16381121974213">bandwidth</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p15350757104113"><a name="p15350757104113"></a><a name="p15350757104113"></a>Bandwidth parameters of the EIP.</p>
</td>
</tr>
</tbody>
</table>

**Table  14**  Data structure of the  **bandwidth**  field

<a name="table16381121974213"></a>
<table><thead align="left"><tr id="row638121920426"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p3460174310425"><a name="p3460174310425"></a><a name="p3460174310425"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p946020432428"><a name="p946020432428"></a><a name="p946020432428"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.3"><p id="p164601943134214"><a name="p164601943134214"></a><a name="p164601943134214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p1646014312426"><a name="p1646014312426"></a><a name="p1646014312426"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13811519104217"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p538131914211"><a name="p538131914211"></a><a name="p538131914211"></a>chargemode</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p1438113199428"><a name="p1438113199428"></a><a name="p1438113199428"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p6381919144212"><a name="p6381919144212"></a><a name="p6381919144212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><a name="uec6c42f83e4e473680a784b2d1ba9be0"></a><a name="uec6c42f83e4e473680a784b2d1ba9be0"></a><ul id="uec6c42f83e4e473680a784b2d1ba9be0"><li>If this field is not carried, the node is charged by bandwidth.</li><li>If this field is carried but is left blank, the node is charged by bandwidth.</li><li>If this field is set to <strong id="en-us_topic_0102499099_b321210217596"><a name="en-us_topic_0102499099_b321210217596"></a><a name="en-us_topic_0102499099_b321210217596"></a>traffic</strong>, the node is charged by traffic.</li><li>If this parameter is set to another value, the ECS creation will fail.</li></ul>
</td>
</tr>
<tr id="row938121964218"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p12381121914421"><a name="p12381121914421"></a><a name="p12381121914421"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p43813193421"><a name="p43813193421"></a><a name="p43813193421"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p13811519124216"><a name="p13811519124216"></a><a name="p13811519124216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p638111195428"><a name="p638111195428"></a><a name="p638111195428"></a>Bandwidth size. For details, see the description of the <strong id="b17637209175614"><a name="b17637209175614"></a><a name="b17637209175614"></a>size</strong> parameter in the <strong id="b5637495569"><a name="b5637495569"></a><a name="b5637495569"></a>bandwidth</strong> field in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Data Structure for Creating ECSs</a>.</p>
</td>
</tr>
<tr id="row8381121911425"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p15381219154214"><a name="p15381219154214"></a><a name="p15381219154214"></a>sharetype</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p14381101919423"><a name="p14381101919423"></a><a name="p14381101919423"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p14381919174213"><a name="p14381919174213"></a><a name="p14381919174213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p65751022144316"><a name="p65751022144316"></a><a name="p65751022144316"></a>Shared bandwidth type. For details, see the description of the <strong id="b1688715194563"><a name="b1688715194563"></a><a name="b1688715194563"></a>sharetype</strong> parameter in the <strong id="b5887181911565"><a name="b5887181911565"></a><a name="b5887181911565"></a>bandwidth</strong> field in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Data Structure for Creating ECSs</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

```
{
    "kind": "Node",
    "apiVersion": "v3",
    "metadata": {
        "name": "myhost",
        "labels": {
            "foo": "bar"
        },
        "annotations": {
            "annotation1": "abc"
        }
    },
    "spec": {
        "flavor": "s1.medium",
        "az": "eu-de-01",
        "login": {
            "sshKey": "Keypair-demo"
        },
        "rootVolume": {
            "size": 40,
            "volumetype": "SATA"
        },
        "dataVolumes": [
            {
                "size": 100,
                "volumetype": "SATA"
            }
        ],
        "userTags": [
            {
                "key": "tag1",
                "value": "aaaa"
            },
            {
                "key": "tag2",
                "value": "bbbb"
            }
        ],
        "k8sTags": {
            "label-test": "test"
        },
        "publicIP": {
            "count": 2,
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "chargemode": "traffic",
                    "size": 10,
                    "sharetype": "PER"
                }
            }
        },
        "count": 2,
        "nodeNicSpec": {
            "primaryNic": {
                "subnetId": "bbfc0a20-d66c-4f36-b4c1-265d669b8c62"
            }
        },
        "extendParam": {
            "alpha.cce/postInstall": "IyEvYml******C50eHQ="
        }
    }
}
```

## Response<a name="section61819725020"></a>

**Response parameters**:

[Table 15](#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242)  describes the response parameters.

**Table  15**  Response parameters

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
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p75781816181715"><a name="p75781816181715"></a><a name="p75781816181715"></a>API type. The value is fixed at <strong id="b937912401982"><a name="b937912401982"></a><a name="b937912401982"></a>Node</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1785493610136"><a name="p1785493610136"></a><a name="p1785493610136"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p757801610179"><a name="p757801610179"></a><a name="p757801610179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12578616151718"><a name="p12578616151718"></a><a name="p12578616151718"></a>API version. The value is fixed at <strong id="b6380240386"><a name="b6380240386"></a><a name="b6380240386"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1185493615135"><a name="p1185493615135"></a><a name="p1185493615135"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p17798121862812"><a name="p17798121862812"></a><a name="p17798121862812"></a><a href="#table65041257514">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10343195011177"><a name="p10343195011177"></a><a name="p10343195011177"></a>Node's metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row2040016320321"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6532732161518"><a name="p6532732161518"></a><a name="p6532732161518"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p186193171282"><a name="p186193171282"></a><a name="p186193171282"></a><a href="#table13949117115810">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p173598507179"><a name="p173598507179"></a><a name="p173598507179"></a>Detailed description of the node targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row1558873515323"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1920413611513"><a name="p1920413611513"></a><a name="p1920413611513"></a><a href="#table9637161310338">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p9204133661512"><a name="p9204133661512"></a><a name="p9204133661512"></a>Node status and jobID of the node creation job.</p>
</td>
</tr>
</tbody>
</table>

**Table  16**  Data structure of the  **spec**  field

<a name="table13949117115810"></a>
<table><thead align="left"><tr id="row17982473586"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p699720715814"><a name="p699720715814"></a><a name="p699720715814"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p71217875816"><a name="p71217875816"></a><a name="p71217875816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p2012138105813"><a name="p2012138105813"></a><a name="p2012138105813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14121683583"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p122888105817"><a name="p122888105817"></a><a name="p122888105817"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p2280835810"><a name="p2280835810"></a><a name="p2280835810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p134317814582"><a name="p134317814582"></a><a name="p134317814582"></a>Node specifications. For details, see the description of the <strong id="b4161181345919"><a name="b4161181345919"></a><a name="b4161181345919"></a>flavorRef</strong> parameter in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
</td>
</tr>
<tr id="row44348155812"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p164320810589"><a name="p164320810589"></a><a name="p164320810589"></a>az</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p76016816581"><a name="p76016816581"></a><a name="p76016816581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p106048105813"><a name="p106048105813"></a><a name="p106048105813"></a>AZ of the node. For details, see the description of the <strong id="b191248436590"><a name="b191248436590"></a><a name="b191248436590"></a>availability_zone</strong> parameter in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020212668.html" target="_blank" rel="noopener noreferrer">Creating an ECS</a>.</p>
</td>
</tr>
<tr id="row1460168135810"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p9751586589"><a name="p9751586589"></a><a name="p9751586589"></a>os</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p169117845811"><a name="p169117845811"></a><a name="p169117845811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p13161571416"><a name="p13161571416"></a><a name="p13161571416"></a>Node OS. Currently, EulerOS 2.2 and EulerOS 2.5 are supported.</p>
</td>
</tr>
<tr id="row1810788135812"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p61071980585"><a name="p61071980585"></a><a name="p61071980585"></a>login</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p3130161112911"><a name="p3130161112911"></a><a name="p3130161112911"></a><a href="#table10946114617286">login</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p212268155816"><a name="p212268155816"></a><a name="p212268155816"></a>Node login mode, which can be key pair or password.</p>
</td>
</tr>
<tr id="row01388816589"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p121383885813"><a name="p121383885813"></a><a name="p121383885813"></a>rootVolume</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1615348125820"><a name="p1615348125820"></a><a name="p1615348125820"></a><a href="#table1359314517">rootVolume</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12153208195815"><a name="p12153208195815"></a><a name="p12153208195815"></a>System disk parameters of the node.</p>
</td>
</tr>
<tr id="row14169981580"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p21691982580"><a name="p21691982580"></a><a name="p21691982580"></a>dataVolumes</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p818512815812"><a name="p818512815812"></a><a name="p818512815812"></a><a href="#table876891063712">dataVolumes</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10185138205818"><a name="p10185138205818"></a><a name="p10185138205818"></a>Data disk parameters of the node. You can check details in <a href="https://docs.otc.t-systems.com/en-us/usermanual2/cce/cce_01_0202.html" target="_blank" rel="noopener noreferrer">How Do I Format a Data Disk Using Command Line Injection?</a></p>
</td>
</tr>
<tr id="row1518558145816"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p171997885817"><a name="p171997885817"></a><a name="p171997885817"></a>publicIP</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p151993811580"><a name="p151993811580"></a><a name="p151993811580"></a><a href="#table139179586343">publicIP</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1721518815812"><a name="p1721518815812"></a><a name="p1721518815812"></a>EIP parameters of a node.</p>
</td>
</tr>
<tr id="row57611951512"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p17731914151"><a name="p17731914151"></a><a name="p17731914151"></a>nodeNicSpec</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p4771119181512"><a name="p4771119181512"></a><a name="p4771119181512"></a><a href="#table162751117166">nodeNicSpec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p977141911515"><a name="p977141911515"></a><a name="p977141911515"></a>Description about the node NIC.</p>
</td>
</tr>
<tr id="row4760101273510"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p8761141218358"><a name="p8761141218358"></a><a name="p8761141218358"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p980362212353"><a name="p980362212353"></a><a name="p980362212353"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1576219120354"><a name="p1576219120354"></a><a name="p1576219120354"></a>Number of nodes to be created in a batch. The value must be a positive integer greater than or equal to 1.</p>
</td>
</tr>
<tr id="row129261258104912"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p12927158144918"><a name="p12927158144918"></a><a name="p12927158144918"></a>billingMode</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p149271058114917"><a name="p149271058114917"></a><a name="p149271058114917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1467216550"><a name="p1467216550"></a><a name="p1467216550"></a>Billing mode of a node.</p>
<div class="note" id="note647122120558"><a name="note647122120558"></a><a name="note647122120558"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1847202165514"><a name="p1847202165514"></a><a name="p1847202165514"></a>This field is not supported for the current version.</p>
</div></div>
</td>
</tr>
<tr id="row16811419205015"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p9814194502"><a name="p9814194502"></a><a name="p9814194502"></a>extendParam</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p16811419205014"><a name="p16811419205014"></a><a name="p16811419205014"></a><a href="#table17575013586">extendParam</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1152473225511"><a name="p1152473225511"></a><a name="p1152473225511"></a>Extended parameter. Format: Key-value pair.</p>
</td>
</tr>
</tbody>
</table>

**Table  17**  Data structure of the nodeNicSpec field

<a name="table162751117166"></a>
<table><thead align="left"><tr id="row202762011151618"><th class="cellrowborder" valign="top" width="21.83%" id="mcps1.2.4.1.1"><p id="p1927631110164"><a name="p1927631110164"></a><a name="p1927631110164"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.4.1.2"><p id="p10276511181610"><a name="p10276511181610"></a><a name="p10276511181610"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.48%" id="mcps1.2.4.1.3"><p id="p1276711141613"><a name="p1276711141613"></a><a name="p1276711141613"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1627614115168"><td class="cellrowborder" valign="top" width="21.83%" headers="mcps1.2.4.1.1 "><p id="p152761511181614"><a name="p152761511181614"></a><a name="p152761511181614"></a>primaryNic</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p11276131116167"><a name="p11276131116167"></a><a name="p11276131116167"></a><a href="#table18277161111161">primaryNic</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="57.48%" headers="mcps1.2.4.1.3 "><p id="p827651114168"><a name="p827651114168"></a><a name="p827651114168"></a>Description about the primary NIC.</p>
</td>
</tr>
</tbody>
</table>

**Table  18**  Data structure of the primaryNic field

<a name="table18277161111161"></a>
<table><thead align="left"><tr id="row12277191111613"><th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.1"><p id="p102771211161620"><a name="p102771211161620"></a><a name="p102771211161620"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.61%" id="mcps1.2.4.1.2"><p id="p627761111161"><a name="p627761111161"></a><a name="p627761111161"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.24%" id="mcps1.2.4.1.3"><p id="p5277121111168"><a name="p5277121111168"></a><a name="p5277121111168"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6277121112161"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p192778117168"><a name="p192778117168"></a><a name="p192778117168"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.2.4.1.2 "><p id="p16277131117168"><a name="p16277131117168"></a><a name="p16277131117168"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.24%" headers="mcps1.2.4.1.3 "><p id="p62771911181615"><a name="p62771911181615"></a><a name="p62771911181615"></a>ID of the subnet to which the NIC belongs.</p>
</td>
</tr>
</tbody>
</table>

**Table  19**  Data structure of the  **extendParam**  field

<a name="table17575013586"></a>
<table><thead align="left"><tr id="row51071750155814"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p41071050115816"><a name="p41071050115816"></a><a name="p41071050115816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1312155019587"><a name="p1312155019587"></a><a name="p1312155019587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p13121155016582"><a name="p13121155016582"></a><a name="p13121155016582"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1916975011583"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p2185650105819"><a name="p2185650105819"></a><a name="p2185650105819"></a>ecs:performancetype</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p141855504585"><a name="p141855504585"></a><a name="p141855504585"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p72001250115813"><a name="p72001250115813"></a><a name="p72001250115813"></a>Type of the ECS specifications. This field does not exist if the node is a BMS.</p>
</td>
</tr>
<tr id="row663581465617"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1463581475612"><a name="p1463581475612"></a><a name="p1463581475612"></a>init-node-password</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p13635161495612"><a name="p13635161495612"></a><a name="p13635161495612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p11635181465614"><a name="p11635181465614"></a><a name="p11635181465614"></a>Init password of Node.</p>
</td>
</tr>
</tbody>
</table>

**Table  20**  Data structure of the  **status**  field

<a name="table9637161310338"></a>
<table><thead align="left"><tr id="row66375133335"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p37490340223"><a name="p37490340223"></a><a name="p37490340223"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p7749734112218"><a name="p7749734112218"></a><a name="p7749734112218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p67491034152211"><a name="p67491034152211"></a><a name="p67491034152211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16637141310336"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6749143432216"><a name="p6749143432216"></a><a name="p6749143432216"></a>jobID</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p117745018256"><a name="p117745018256"></a><a name="p117745018256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p359145391513"><a name="p359145391513"></a><a name="p359145391513"></a>ID of the node creation job. You can <a href="reading-job-progress.md">query job progress</a> by job ID to keep updated on node creation progress.</p>
</td>
</tr>
</tbody>
</table>

**Example response**:

```
{
    "kind": "Node",
    "apiVersion": "v3",
    "metadata": {
        "name": "myhost",
        "uid": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
        "labels": {
            "foo": "bar"
        },
        "annotations": {
            "annotation1": "abc"
        }
    },
    "spec": {
        "flavor": "s1.medium",
        "az": "eu-de-01",
        "os": "EulerOS 2.5",
        "login": {
            "sshKey": "Keypai-demo"
        },
        "rootVolume": {
            "volumetype": "SATA",
            "size": 40
        },
        "dataVolumes": [
            {
                "volumetype": "SATA",
                "size": 100
            }
        ],
        "publicIP": {
            "count": 2,
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 10,
                    "sharetype": "PER",
                    "chargemode": "traffic"
                }
            }
        },
        "nodeNicSpec": {
            "primaryNic": {
                "subnetId": "2afc3d7f-07d1-4c25-ba2e-8ee48d253d9f"
            }
        },
        "count": 2,
        "extendParam": { 
            "ecs:performancetype": "normal",
            "init-node-password": ""
        }
    },
    "status": {
        "jobID": "2ec9b78d-9368-46f3-8f29-d1a95622a568"
    }
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 21](#en-us_topic_0079614900_table46761928)  describes the status codes of this API.

**Table  21**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>The job for creating a node in a specified cluster is successfully issued.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).

