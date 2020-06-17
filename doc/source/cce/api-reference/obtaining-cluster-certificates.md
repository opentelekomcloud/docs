# Obtaining Cluster Certificates<a name="cce_02_0248"></a>

## Function<a name="section1686113493165"></a>

This API is used to obtain certificates of a specified cluster.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/clustercert

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
<tr id="row19993973274"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1699317712718"><a name="p1699317712718"></a><a name="p1699317712718"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p89934722719"><a name="p89934722719"></a><a name="p89934722719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p1149162812272"><a name="p1149162812272"></a><a name="p1149162812272"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table538113720514)  describes the request parameters.

**Table  2**  Parameters in the request header

<a name="table538113720514"></a>
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

[Table 3](#table10794441185312)  describes the response parameters.

**Table  3**  Response parameters

<a name="table10794441185312"></a>
<table><thead align="left"><tr id="row479704155313"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p1479884175317"><a name="p1479884175317"></a><a name="p1479884175317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1279917411533"><a name="p1279917411533"></a><a name="p1279917411533"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p7800174116531"><a name="p7800174116531"></a><a name="p7800174116531"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row280113412539"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12340185616220"><a name="p12340185616220"></a><a name="p12340185616220"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1822894016484"><a name="p1822894016484"></a><a name="p1822894016484"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p722774012483"><a name="p722774012483"></a><a name="p722774012483"></a>API type. The value is fixed at <strong id="b199262510521"><a name="b199262510521"></a><a name="b199262510521"></a>Config</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row68061041135317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p23406568227"><a name="p23406568227"></a><a name="p23406568227"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p622611406488"><a name="p622611406488"></a><a name="p622611406488"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p162251840154816"><a name="p162251840154816"></a><a name="p162251840154816"></a>API version. The value is fixed at <strong id="b892253618533"><a name="b892253618533"></a><a name="b892253618533"></a>v1</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row75713500227"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1340145692215"><a name="p1340145692215"></a><a name="p1340145692215"></a>preferences</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1157220503223"><a name="p1157220503223"></a><a name="p1157220503223"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p145729504227"><a name="p145729504227"></a><a name="p145729504227"></a>This field is not used currently and is left unspecified by default.</p>
</td>
</tr>
<tr id="row1481016412536"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1234075612226"><a name="p1234075612226"></a><a name="p1234075612226"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p8224204054815"><a name="p8224204054815"></a><a name="p8224204054815"></a><a href="#table2157957598">clusters</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p16223840194816"><a name="p16223840194816"></a><a name="p16223840194816"></a>Cluster list.</p>
</td>
</tr>
<tr id="row178131418531"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15340175622213"><a name="p15340175622213"></a><a name="p15340175622213"></a>users</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p222117402485"><a name="p222117402485"></a><a name="p222117402485"></a><a href="#table7846125310316">users</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10221174014489"><a name="p10221174014489"></a><a name="p10221174014489"></a>-</p>
</td>
</tr>
<tr id="row581674195314"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1034085618224"><a name="p1034085618224"></a><a name="p1034085618224"></a>contexts</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p19219104018481"><a name="p19219104018481"></a><a name="p19219104018481"></a><a href="#table1653965354">contexts</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p221974010482"><a name="p221974010482"></a><a name="p221974010482"></a>Context list.</p>
</td>
</tr>
<tr id="row16820841145310"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17340756192216"><a name="p17340756192216"></a><a name="p17340756192216"></a>current-context</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p20820114145010"><a name="p20820114145010"></a><a name="p20820114145010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p9820191425019"><a name="p9820191425019"></a><a name="p9820191425019"></a>Current context.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **clusters**  field

<a name="table2157957598"></a>
<table><thead align="left"><tr id="row1161175165911"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p111637517599"><a name="p111637517599"></a><a name="p111637517599"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p11651358593"><a name="p11651358593"></a><a name="p11651358593"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p416645155912"><a name="p416645155912"></a><a name="p416645155912"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row616710518596"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8749132512311"><a name="p8749132512311"></a><a name="p8749132512311"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p181688520596"><a name="p181688520596"></a><a name="p181688520596"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p69881827105120"><a name="p69881827105120"></a><a name="p69881827105120"></a>Cluster name.</p>
<a name="ul189480357510"></a><a name="ul189480357510"></a><ul id="ul189480357510"><li>If the <strong id="b6196437211"><a name="b6196437211"></a><a name="b6196437211"></a>publicIp</strong> parameter does not exist (that is, no EIP exists), there is only one cluster in the cluster list, and the value of this parameter is <strong id="b108621843"><a name="b108621843"></a><a name="b108621843"></a>internalCluster</strong>.</li><li>If the <strong id="b84042716416"><a name="b84042716416"></a><a name="b84042716416"></a>publicIp</strong> parameter exists (that is, the EIP exists), there is more than one cluster in the cluster list, and the value of this parameter is <strong id="b154115271644"><a name="b154115271644"></a><a name="b154115271644"></a>externalCluster</strong>.</li></ul>
</td>
</tr>
<tr id="row1717013525912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1474962552312"><a name="p1474962552312"></a><a name="p1474962552312"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1617116516594"><a name="p1617116516594"></a><a name="p1617116516594"></a><a href="#table519211353218">cluster</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p197819347238"><a name="p197819347238"></a><a name="p197819347238"></a>Cluster information.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Data structure of the  **cluster**  field

<a name="table519211353218"></a>
<table><thead align="left"><tr id="row321083518215"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p12164356219"><a name="p12164356219"></a><a name="p12164356219"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p17224123512111"><a name="p17224123512111"></a><a name="p17224123512111"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p122293355211"><a name="p122293355211"></a><a name="p122293355211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3234635142115"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p464235772320"><a name="p464235772320"></a><a name="p464235772320"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1015317134399"><a name="p1015317134399"></a><a name="p1015317134399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p151548136395"><a name="p151548136395"></a><a name="p151548136395"></a>Node IP address.</p>
</td>
</tr>
<tr id="row16252935192119"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p166421257162313"><a name="p166421257162313"></a><a name="p166421257162313"></a>certificate-authority-data</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1022104625510"><a name="p1022104625510"></a><a name="p1022104625510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p222016469555"><a name="p222016469555"></a><a name="p222016469555"></a>Certificate authorization data.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Data structure of the  **users**  field

<a name="table7846125310316"></a>
<table><thead align="left"><tr id="row18491253439"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p1185213531136"><a name="p1185213531136"></a><a name="p1185213531136"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p168531539311"><a name="p168531539311"></a><a name="p168531539311"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p48557530314"><a name="p48557530314"></a><a name="p48557530314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48561353538"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1081619137243"><a name="p1081619137243"></a><a name="p1081619137243"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p8681520149"><a name="p8681520149"></a><a name="p8681520149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p2681320241"><a name="p2681320241"></a><a name="p2681320241"></a>The value is fixed to <strong id="b56951334589"><a name="b56951334589"></a><a name="b56951334589"></a>user</strong>.</p>
</td>
</tr>
<tr id="row2086016536310"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1481615137243"><a name="p1481615137243"></a><a name="p1481615137243"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p26718205410"><a name="p26718205410"></a><a name="p26718205410"></a><a href="#table205311581434">user</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p266920549"><a name="p266920549"></a><a name="p266920549"></a>Stores the certificate information and ClientKey information of a specified user.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the  **user**  field

<a name="table205311581434"></a>
<table><thead align="left"><tr id="row14571558933"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p1558125817311"><a name="p1558125817311"></a><a name="p1558125817311"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p116015581134"><a name="p116015581134"></a><a name="p116015581134"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p12611058739"><a name="p12611058739"></a><a name="p12611058739"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row126110585314"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4958942122415"><a name="p4958942122415"></a><a name="p4958942122415"></a>client-certificate-data</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p69201306371"><a name="p69201306371"></a><a name="p69201306371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p6155132833316"><a name="p6155132833316"></a><a name="p6155132833316"></a>Client certificate.</p>
</td>
</tr>
<tr id="row1266155814310"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p169582420243"><a name="p169582420243"></a><a name="p169582420243"></a>client-key-data</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1890215353719"><a name="p1890215353719"></a><a name="p1890215353719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p16973125711346"><a name="p16973125711346"></a><a name="p16973125711346"></a>Contains PEM encoding data from the TLS client key file.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the  **contexts**  field

<a name="table1653965354"></a>
<table><thead align="left"><tr id="row1654419517516"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p754585755"><a name="p754585755"></a><a name="p754585755"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p3546952053"><a name="p3546952053"></a><a name="p3546952053"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p11548135655"><a name="p11548135655"></a><a name="p11548135655"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25491955514"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1115011101251"><a name="p1115011101251"></a><a name="p1115011101251"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p12552755513"><a name="p12552755513"></a><a name="p12552755513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p55125122395"><a name="p55125122395"></a><a name="p55125122395"></a>Context name.</p>
<a name="ul157991814135715"></a><a name="ul157991814135715"></a><ul id="ul157991814135715"><li>If the <strong id="b16909127171319"><a name="b16909127171319"></a><a name="b16909127171319"></a>publicIp</strong> parameter does not exist (that is, no EIP exists), there is only one cluster in the cluster list, and the value of this parameter is <strong id="b19104701314"><a name="b19104701314"></a><a name="b19104701314"></a>internal</strong>.</li><li>If the <strong id="b193515299133"><a name="b193515299133"></a><a name="b193515299133"></a>publicIp</strong> parameter exists (that is, the EIP exists), there is more than one cluster in the cluster list, and the value of this parameter is <strong id="b1538129121311"><a name="b1538129121311"></a><a name="b1538129121311"></a>external</strong>.</li></ul>
</td>
</tr>
<tr id="row125534519519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p19150610112518"><a name="p19150610112518"></a><a name="p19150610112518"></a>context</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p12556559518"><a name="p12556559518"></a><a name="p12556559518"></a><a href="#table47913919518">context</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p107081923192519"><a name="p107081923192519"></a><a name="p107081923192519"></a>Context information.</p>
</td>
</tr>
</tbody>
</table>

**Table  9**  Data structure of the  **context**  field

<a name="table47913919518"></a>
<table><thead align="left"><tr id="row2851791957"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p387896517"><a name="p387896517"></a><a name="p387896517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1891591554"><a name="p1891591554"></a><a name="p1891591554"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p119112912513"><a name="p119112912513"></a><a name="p119112912513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row793396511"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1997111301250"><a name="p1997111301250"></a><a name="p1997111301250"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p2951292054"><a name="p2951292054"></a><a name="p2951292054"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p879115407257"><a name="p879115407257"></a><a name="p879115407257"></a>Cluster context.</p>
</td>
</tr>
<tr id="row15979918515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15971153052514"><a name="p15971153052514"></a><a name="p15971153052514"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p9100891155"><a name="p9100891155"></a><a name="p9100891155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1791940192516"><a name="p1791940192516"></a><a name="p1791940192516"></a>User context.</p>
</td>
</tr>
</tbody>
</table>

**Response example**:

```
{
    "kind": "Config",
    "apiVersion": "v1",
    "preferences": {},
    "clusters": [
        {
            "name": "internalCluster",
            "cluster": {
                "server": "https://192.168.1.7:5443",
                "certificate-authority-data": ""
            }
        }
    ],
    "users": [
        {
            "name": "user",
            "user": {
                "client-certificate-data": "",
                "client-key-data": ""
            }
        }
    ],
    "contexts": [
        {
            "name": "internal",
            "context": {
                "cluster": "internalCluster",
                "user": "user"
            }
        }
    ],
    "current-context": "internal"
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Certificates of the specified cluster are successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

