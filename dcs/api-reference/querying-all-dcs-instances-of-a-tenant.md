# Querying All DCS Instances of a Tenant<a name="dcs-api-0312006"></a>

## Function<a name="section152981849191118"></a>

This API is used to query DCS instances of a tenant, and allows you to specify query criteria.

## URI<a name="section241813305156"></a>

GET /v1.0/\{project\_id\}/instances?start=\{start\}&limit=\{limit\}&name=\{name\}&status=\{status\}&id=\{id\}&includeFailure=\{includeFailure\}&isExactMatchName=\{isExactMatchName\}

[Table 1](#table1971216413394)  describes the parameters.

**Table  1**  Parameter description

<a name="table1971216413394"></a>
<table><thead align="left"><tr id="row471164123918"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p1671124183918"><a name="p1671124183918"></a><a name="p1671124183918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p9711640395"><a name="p9711640395"></a><a name="p9711640395"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.3"><p id="p6711134123919"><a name="p6711134123919"></a><a name="p6711134123919"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.55555555555556%" id="mcps1.2.5.1.4"><p id="p371111419391"><a name="p371111419391"></a><a name="p371111419391"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1971164153918"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1871118413915"><a name="p1871118413915"></a><a name="p1871118413915"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p67119403914"><a name="p67119403914"></a><a name="p67119403914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p1971114133914"><a name="p1971114133914"></a><a name="p1971114133914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p1571112453911"><a name="p1571112453911"></a><a name="p1571112453911"></a>Project ID.</p>
</td>
</tr>
<tr id="row35781458193419"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1056385913419"><a name="p1056385913419"></a><a name="p1056385913419"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p1656455973412"><a name="p1656455973412"></a><a name="p1656455973412"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p35641259133416"><a name="p35641259133416"></a><a name="p35641259133416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p155291255164420"><a name="p155291255164420"></a><a name="p155291255164420"></a>Start number for querying DCS instances. It cannot be lower than 1.</p>
<p id="p874301694015"><a name="p874301694015"></a><a name="p874301694015"></a>By default, the start number is 1.</p>
</td>
</tr>
<tr id="row369210914352"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p982313289356"><a name="p982313289356"></a><a name="p982313289356"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p1282382873520"><a name="p1282382873520"></a><a name="p1282382873520"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p208234286356"><a name="p208234286356"></a><a name="p208234286356"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p31411454192212"><a name="p31411454192212"></a><a name="p31411454192212"></a>Number of DCS instances displayed on each page.</p>
<p id="p18991528226"><a name="p18991528226"></a><a name="p18991528226"></a>Minimum value: <strong id="b12604124814265"><a name="b12604124814265"></a><a name="b12604124814265"></a>1</strong></p>
<p id="p687663014320"><a name="p687663014320"></a><a name="p687663014320"></a>Maximum value: <strong id="b8502123603218"><a name="b8502123603218"></a><a name="b8502123603218"></a>2000</strong></p>
<p id="p117431016134018"><a name="p117431016134018"></a><a name="p117431016134018"></a>If this parameter is left unspecified, a maximum of 1000 DCS instances are displayed on each page.</p>
</td>
</tr>
<tr id="row571194103917"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1071194183918"><a name="p1071194183918"></a><a name="p1071194183918"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p1971194143913"><a name="p1971194143913"></a><a name="p1971194143913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p1271154103919"><a name="p1271154103919"></a><a name="p1271154103919"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p971115443917"><a name="p971115443917"></a><a name="p971115443917"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row29521548173814"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1681750143817"><a name="p1681750143817"></a><a name="p1681750143817"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p5681650143817"><a name="p5681650143817"></a><a name="p5681650143817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p66855016386"><a name="p66855016386"></a><a name="p66855016386"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p268205023811"><a name="p268205023811"></a><a name="p268205023811"></a>Instance ID.</p>
</td>
</tr>
<tr id="row12786653163512"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p38591137369"><a name="p38591137369"></a><a name="p38591137369"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p15859333361"><a name="p15859333361"></a><a name="p15859333361"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p285910343614"><a name="p285910343614"></a><a name="p285910343614"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p885911333617"><a name="p885911333617"></a><a name="p885911333617"></a>DCS instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row1755617651610"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p35567641610"><a name="p35567641610"></a><a name="p35567641610"></a>includeFailure</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p1555618621616"><a name="p1555618621616"></a><a name="p1555618621616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p9556563163"><a name="p9556563163"></a><a name="p9556563163"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p7669181914458"><a name="p7669181914458"></a><a name="p7669181914458"></a>An indicator of whether the number of DCS instances that failed to be created will be returned to the API caller.</p>
<p id="p1293413195320"><a name="p1293413195320"></a><a name="p1293413195320"></a>Options:</p>
<a name="ul1614112811458"></a><a name="ul1614112811458"></a><ul id="ul1614112811458"><li><strong id="b209751421194520"><a name="b209751421194520"></a><a name="b209751421194520"></a>true</strong>: The number of DCS instances that failed to be created will be returned to the API caller.</li><li><strong id="b164651564234"><a name="b164651564234"></a><a name="b164651564234"></a>false</strong> or others: The number of DCS instances that failed to be created will not be returned to the API caller.</li></ul>
</td>
</tr>
<tr id="row34061958105318"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p104075583533"><a name="p104075583533"></a><a name="p104075583533"></a>isExactMatchName</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p154081558205319"><a name="p154081558205319"></a><a name="p154081558205319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p640819584533"><a name="p640819584533"></a><a name="p640819584533"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="p1375212486256"><a name="p1375212486256"></a><a name="p1375212486256"></a>An indicator of whether to perform an exact or fuzzy match based on instance name.</p>
<p id="p18345175411542"><a name="p18345175411542"></a><a name="p18345175411542"></a>Options:</p>
<a name="ul68491558162511"></a><a name="ul68491558162511"></a><ul id="ul68491558162511"><li><strong id="b2481105110254"><a name="b2481105110254"></a><a name="b2481105110254"></a>true</strong>: exact match</li><li><strong id="b67053537253"><a name="b67053537253"></a><a name="b67053537253"></a>false</strong>: fuzzy match</li></ul>
<p id="p640875825310"><a name="p640875825310"></a><a name="p640875825310"></a>Default value: <strong id="b158981742112411"><a name="b158981742112411"></a><a name="b158981742112411"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET https://{dcs_endpoint}/v1.0/bd6b78e2ff9e4e47bc260803ddcc7a21/instances?start=1&limit=10&name=&status=&id=&includeFailure=true&isExactMatchName=false  
```

## Request<a name="section12833102510169"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section1357695041617"></a>

**Response parameters**

[Table 2](#table189371511113913)  describes the response parameters.

**Table  2**  Parameter description

<a name="table189371511113913"></a>
<table><thead align="left"><tr id="row19371311103911"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1793761183919"><a name="p1793761183919"></a><a name="p1793761183919"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1093731111398"><a name="p1093731111398"></a><a name="p1093731111398"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p17937111153918"><a name="p17937111153918"></a><a name="p17937111153918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3202104544912"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2281341504"><a name="p2281341504"></a><a name="p2281341504"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p172816412505"><a name="p172816412505"></a><a name="p172816412505"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22822425019"><a name="p22822425019"></a><a name="p22822425019"></a>Array of DCS instance details.</p>
</td>
</tr>
<tr id="row893791193918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p149376118392"><a name="p149376118392"></a><a name="p149376118392"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1193711112392"><a name="p1193711112392"></a><a name="p1193711112392"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19937711123913"><a name="p19937711123913"></a><a name="p19937711123913"></a>Number of DCS instances.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the instance array

<a name="table369734810017"></a>
<table><thead align="left"><tr id="row669810481608"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p2698848701"><a name="p2698848701"></a><a name="p2698848701"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p16698134812020"><a name="p16698134812020"></a><a name="p16698134812020"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p2069814482002"><a name="p2069814482002"></a><a name="p2069814482002"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row569813481702"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1869994817016"><a name="p1869994817016"></a><a name="p1869994817016"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6699204817015"><a name="p6699204817015"></a><a name="p6699204817015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p4699448306"><a name="p4699448306"></a><a name="p4699448306"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row969954818015"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p3699194818010"><a name="p3699194818010"></a><a name="p3699194818010"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1169911481205"><a name="p1169911481205"></a><a name="p1169911481205"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p66991848702"><a name="p66991848702"></a><a name="p66991848702"></a>Cache engine.</p>
</td>
</tr>
<tr id="row73791340465"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p11395113184611"><a name="p11395113184611"></a><a name="p11395113184611"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p2039520135468"><a name="p2039520135468"></a><a name="p2039520135468"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p18782152184620"><a name="p18782152184620"></a><a name="p18782152184620"></a>Cache capacity.</p>
<p id="p1074361620405"><a name="p1074361620405"></a><a name="p1074361620405"></a>Unit: GB.</p>
</td>
</tr>
<tr id="row193961184614"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p284717204463"><a name="p284717204463"></a><a name="p284717204463"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p10848102018461"><a name="p10848102018461"></a><a name="p10848102018461"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p198485207467"><a name="p198485207467"></a><a name="p198485207467"></a>IP address for connecting to the DCS instance. For a cluster instance, multiple IP addresses are returned and separated by commas (,). For example, 192.168.0.1,192.168.0.2.</p>
</td>
</tr>
<tr id="row113761049104515"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p384812034619"><a name="p384812034619"></a><a name="p384812034619"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p7848122013462"><a name="p7848122013462"></a><a name="p7848122013462"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p108481520134614"><a name="p108481520134614"></a><a name="p108481520134614"></a>Port number of the cache node.</p>
</td>
</tr>
<tr id="row104917353465"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p2043125115467"><a name="p2043125115467"></a><a name="p2043125115467"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p0431951114611"><a name="p0431951114611"></a><a name="p0431951114611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p6431105164611"><a name="p6431105164611"></a><a name="p6431105164611"></a>Cache instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row9591173417615"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1922216541369"><a name="p1922216541369"></a><a name="p1922216541369"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p922213543615"><a name="p922213543615"></a><a name="p922213543615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p4163813193015"><a name="p4163813193015"></a><a name="p4163813193015"></a>Overall memory size.</p>
<p id="p1312171063014"><a name="p1312171063014"></a><a name="p1312171063014"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row56279371966"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p192220546614"><a name="p192220546614"></a><a name="p192220546614"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1922213541860"><a name="p1922213541860"></a><a name="p1922213541860"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p117951449303"><a name="p117951449303"></a><a name="p117951449303"></a>Size of the used memory.</p>
<p id="p13743116144015"><a name="p13743116144015"></a><a name="p13743116144015"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row47802328460"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p166055815469"><a name="p166055815469"></a><a name="p166055815469"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p460658144617"><a name="p460658144617"></a><a name="p460658144617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p186114581469"><a name="p186114581469"></a><a name="p186114581469"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row694618119478"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1922812198471"><a name="p1922812198471"></a><a name="p1922812198471"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p16228151919475"><a name="p16228151919475"></a><a name="p16228151919475"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1822812195472"><a name="p1822812195472"></a><a name="p1822812195472"></a>Resource specifications.</p>
<a name="ul103859344523"></a><a name="ul103859344523"></a><ul id="ul103859344523"><li><strong id="b795502413017"><a name="b795502413017"></a><a name="b795502413017"></a>dcs.single_node</strong>: indicates a DCS instance in single-node mode.</li><li><strong id="b1373103283019"><a name="b1373103283019"></a><a name="b1373103283019"></a>dcs.master_standby</strong>: indicates a DCS instance in master/standby mode.</li><li><strong id="b12699340183014"><a name="b12699340183014"></a><a name="b12699340183014"></a>dcs.cluster</strong>: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row1769904814011"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1699348901"><a name="p1699348901"></a><a name="p1699348901"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p76991483017"><a name="p76991483017"></a><a name="p76991483017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p106999489010"><a name="p106999489010"></a><a name="p106999489010"></a>Cache engine version.</p>
</td>
</tr>
<tr id="row1169916481907"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p96991848800"><a name="p96991848800"></a><a name="p96991848800"></a>internal_version</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p9699104812010"><a name="p9699104812010"></a><a name="p9699104812010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1269934817017"><a name="p1269934817017"></a><a name="p1269934817017"></a>Internal DCS version.</p>
</td>
</tr>
<tr id="row8699134814017"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1369913481403"><a name="p1369913481403"></a><a name="p1369913481403"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p126992481601"><a name="p126992481601"></a><a name="p126992481601"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p39546309494"><a name="p39546309494"></a><a name="p39546309494"></a>Billing mode. <strong id="b22127498117"><a name="b22127498117"></a><a name="b22127498117"></a>0</strong>: pay-per-use.</p>
</td>
</tr>
<tr id="row193781351113220"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1815911534325"><a name="p1815911534325"></a><a name="p1815911534325"></a>capacity_minor</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p81659537320"><a name="p81659537320"></a><a name="p81659537320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1716914531324"><a name="p1716914531324"></a><a name="p1716914531324"></a>Small-scale cache capacity. Unit: GB.</p>
</td>
</tr>
<tr id="row1570074814019"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p970012481002"><a name="p970012481002"></a><a name="p970012481002"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1270012481407"><a name="p1270012481407"></a><a name="p1270012481407"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p18700114816015"><a name="p18700114816015"></a><a name="p18700114816015"></a>VPC ID.</p>
</td>
</tr>
<tr id="row207001048803"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p157009481802"><a name="p157009481802"></a><a name="p157009481802"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p157001748203"><a name="p157001748203"></a><a name="p157001748203"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p670074820013"><a name="p670074820013"></a><a name="p670074820013"></a>VPC name.</p>
</td>
</tr>
<tr id="row570084820016"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p117009481706"><a name="p117009481706"></a><a name="p117009481706"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p77008481401"><a name="p77008481401"></a><a name="p77008481401"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1870013481502"><a name="p1870013481502"></a><a name="p1870013481502"></a>Time at which the DCS instance is created. For example, 2017-03-31<strong id="b134311842153518"><a name="b134311842153518"></a><a name="b134311842153518"></a>T</strong>12:24:46.297<strong id="b13431174214354"><a name="b13431174214354"></a><a name="b13431174214354"></a>Z</strong>.</p>
</td>
</tr>
<tr id="row19101720521"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1912813665211"><a name="p1912813665211"></a><a name="p1912813665211"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p21281736165212"><a name="p21281736165212"></a><a name="p21281736165212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p4128153619521"><a name="p4128153619521"></a><a name="p4128153619521"></a>Error code returned when the DCS instance fails to be created or is in abnormal status. For details about error codes, see <a href="querying-a-dcs-instance.md#table691509456">Table 3</a>.</p>
</td>
</tr>
<tr id="row366816435535"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p11801751135315"><a name="p11801751135315"></a><a name="p11801751135315"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p318015515539"><a name="p318015515539"></a><a name="p318015515539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p191801051165317"><a name="p191801051165317"></a><a name="p191801051165317"></a>User ID.</p>
</td>
</tr>
<tr id="row55081444537"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p2018075115531"><a name="p2018075115531"></a><a name="p2018075115531"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p91804516534"><a name="p91804516534"></a><a name="p91804516534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1818085118536"><a name="p1818085118536"></a><a name="p1818085118536"></a>Username.</p>
</td>
</tr>
<tr id="row114981744170"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p13545101053910"><a name="p13545101053910"></a><a name="p13545101053910"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p354520108395"><a name="p354520108395"></a><a name="p354520108395"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p65461110173913"><a name="p65461110173913"></a><a name="p65461110173913"></a>Time at which the maintenance time window starts. Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row931451171715"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p654621033913"><a name="p654621033913"></a><a name="p654621033913"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p125461810203910"><a name="p125461810203910"></a><a name="p125461810203910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p15546610113919"><a name="p15546610113919"></a><a name="p15546610113919"></a>Time at which the maintenance time window ends. Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row10102225175414"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1510242510546"><a name="p1510242510546"></a><a name="p1510242510546"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p25821513486"><a name="p25821513486"></a><a name="p25821513486"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1458214131886"><a name="p1458214131886"></a><a name="p1458214131886"></a>Security group name.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "instances": [
        {           
            "name": "dcs-lxy",            
            "engine": "Redis",
            "capacity": 4,
            "ip": "192.168.7.146",
           
            "port": 6379,
            "status": "CREATING",
            "max_memory": 3277,
            "used_memory": 0,
            "instance_id": "a4d31cb6-3d72-4fdc-8ec9-6e3a41e47f71",
             "resource_spec_code": "dcs.master_standby",
            "engine_version": "3.0",
            "internal_version": null,
            "charging_mode": 0,          
            "capacity_minor": null,
            "vpc_id": "c71d9731-9b0c-43e9-ab2a-716af9d9fd55",
            "vpc_name": "CCE-AutoCreate-VPC-7qvs1",       
            "created_at": "2019-09-23T02:40:06.123Z",
            "error_code": null,
            "user_id": "50a4156d334a4a82b8745dc730dc1e00",
            "user_name": "hwstaff_f00443635",
            "maintain_begin": "02:00:00",
            "maintain_end": "06:00:00",
            "security_group_id": "0cc8fdb7-872a-49da-a062-88ccc39463b5"
        }],
    "instance_num": 1
}

```

## Status Code<a name="section11445132514139"></a>

[Table 4](#table3445625171318)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table3445625171318"></a>
<table><thead align="left"><tr id="row184461225121311"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.3.1.1"><p id="p144682518130"><a name="p144682518130"></a><a name="p144682518130"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84%" id="mcps1.2.3.1.2"><p id="p244602517132"><a name="p244602517132"></a><a name="p244602517132"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94465257132"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.3.1.1 "><p id="p194464259135"><a name="p194464259135"></a><a name="p194464259135"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84%" headers="mcps1.2.3.1.2 "><p id="p1444614258139"><a name="p1444614258139"></a><a name="p1444614258139"></a>All DCS instances of the tenant queried successfully.</p>
</td>
</tr>
</tbody>
</table>

