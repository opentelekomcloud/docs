# Adding a Forwarding Rule<a name="EN-US_TOPIC_0116649236"></a>

## Function<a name="en-us_topic_0082661927_section6060641715826"></a>

This API is used to add a forwarding rule. After you add a forwarding rule, the load balancer matches the domain name and path in the request and distributes the traffic to the backend server group specified by  **redirect\_pool\_id**  of the associated with the forwarding policy.

## URI<a name="en-us_topic_0082661927_section2444552715826"></a>

POST /v2.0/lbaas/l7policies/\{l7policy\_id\}/rules

**Table  1**  Parameter description

<a name="table1811925195814"></a>
<table><thead align="left"><tr id="row384482517585"><th class="cellrowborder" valign="top" width="24.717528247175284%" id="mcps1.2.5.1.1"><p id="p884462535814"><a name="p884462535814"></a><a name="p884462535814"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.478352164783523%" id="mcps1.2.5.1.2"><p id="p784472511581"><a name="p784472511581"></a><a name="p784472511581"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="9.37906209379062%" id="mcps1.2.5.1.3"><p id="p38443253584"><a name="p38443253584"></a><a name="p38443253584"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.42505749425058%" id="mcps1.2.5.1.4"><p id="p1484422514585"><a name="p1484422514585"></a><a name="p1484422514585"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row284402519581"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p15844182595811"><a name="p15844182595811"></a><a name="p15844182595811"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p7845925155817"><a name="p7845925155817"></a><a name="p7845925155817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.3 "><p id="p9844122512581"><a name="p9844122512581"></a><a name="p9844122512581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.42505749425058%" headers="mcps1.2.5.1.4 "><p id="p8845152595816"><a name="p8845152595816"></a><a name="p8845152595816"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section74358317182"></a>

The match type of forwarding rules in a forwarding policy must be unique.

## Request<a name="section9798645173116"></a>

**Table  2**  Request parameters

<a name="table579815451314"></a>
<table><thead align="left"><tr id="row10798645203114"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.1"><p id="p127981345193117"><a name="p127981345193117"></a><a name="p127981345193117"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p2073114981812"><a name="p2073114981812"></a><a name="p2073114981812"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p179854563116"><a name="p179854563116"></a><a name="p179854563116"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.56565656565656%" id="mcps1.2.5.1.4"><p id="p11448125981812"><a name="p11448125981812"></a><a name="p11448125981812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9814164517312"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="p178141145113118"><a name="p178141145113118"></a><a name="p178141145113118"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p77215497189"><a name="p77215497189"></a><a name="p77215497189"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p5814114583114"><a name="p5814114583114"></a><a name="p5814114583114"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.56565656565656%" headers="mcps1.2.5.1.4 "><p id="p14814154518318"><a name="p14814154518318"></a><a name="p14814154518318"></a>Specifies the forwarding rule. For details, see <a href="#table857349145816">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **rule**  parameter description

<a name="table857349145816"></a>
<table><thead align="left"><tr id="row1813794914585"><th class="cellrowborder" valign="top" width="25.930000000000003%" id="mcps1.2.5.1.1"><p id="p18137204925818"><a name="p18137204925818"></a><a name="p18137204925818"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.47%" id="mcps1.2.5.1.2"><p id="p3137449195820"><a name="p3137449195820"></a><a name="p3137449195820"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.110000000000003%" id="mcps1.2.5.1.3"><p id="p15137104917584"><a name="p15137104917584"></a><a name="p15137104917584"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.49%" id="mcps1.2.5.1.4"><p id="p171891142121911"><a name="p171891142121911"></a><a name="p171891142121911"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row013714975814"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0082661924_p9082858145533"><a name="en-us_topic_0082661924_p9082858145533"></a><a name="en-us_topic_0082661924_p9082858145533"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p12137124955813"><a name="p12137124955813"></a><a name="p12137124955813"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p9137134955817"><a name="p9137134955817"></a><a name="p9137134955817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p2038118462238"><a name="p2038118462238"></a><a name="p2038118462238"></a>The value must be the same as the value of <strong id="b413981815456"><a name="b413981815456"></a><a name="b413981815456"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row61371149115814"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p113714490586"><a name="p113714490586"></a><a name="p113714490586"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p17137164945815"><a name="p17137164945815"></a><a name="p17137164945815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p151371449135815"><a name="p151371449135815"></a><a name="p151371449135815"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b189613284512"><a name="b189613284512"></a><a name="b189613284512"></a>true</strong> or <strong id="b1898163213455"><a name="b1898163213455"></a><a name="b1898163213455"></a>false</strong>.</p>
<p id="p1610904293213"><a name="p1610904293213"></a><a name="p1610904293213"></a>This parameter is reserved. The default value is <strong id="b6325132119442"><a name="b6325132119442"></a><a name="b6325132119442"></a>true</strong>.</p>
</td>
</tr>
<tr id="row1213718492586"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p1513719494585"><a name="p1513719494585"></a><a name="p1513719494585"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p131371749155817"><a name="p131371749155817"></a><a name="p131371749155817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p181371749135814"><a name="p181371749135814"></a><a name="p181371749135814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p1161972619482"><a name="p1161972619482"></a><a name="p1161972619482"></a>Specifies the match type of a forwarding rule.</p>
<p id="p9536114413489"><a name="p9536114413489"></a><a name="p9536114413489"></a>The value can be one of the following:</p>
<a name="ul3525953124817"></a><a name="ul3525953124817"></a><ul id="ul3525953124817"><li><strong id="b11692141531616"><a name="b11692141531616"></a><a name="b11692141531616"></a>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong id="b4424141754616"><a name="b4424141754616"></a><a name="b4424141754616"></a>PATH</strong>: matches the path in the request.</li></ul>
<p id="p15285166489"><a name="p15285166489"></a><a name="p15285166489"></a>The match type of forwarding rules in a forwarding policy must be unique.</p>
</td>
</tr>
<tr id="row91371498580"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p8137249165813"><a name="p8137249165813"></a><a name="p8137249165813"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p513714497583"><a name="p513714497583"></a><a name="p513714497583"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p513794918587"><a name="p513794918587"></a><a name="p513794918587"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p51371649125820"><a name="p51371649125820"></a><a name="p51371649125820"></a>Specifies the match mode. The options are as follows:</p>
<p id="p10794420115116"><a name="p10794420115116"></a><a name="p10794420115116"></a>When <strong id="b195318525450"><a name="b195318525450"></a><a name="b195318525450"></a>type</strong> is set to <strong id="b16430100124613"><a name="b16430100124613"></a><a name="b16430100124613"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="ul15305619145114"></a><a name="ul15305619145114"></a><ul id="ul15305619145114"><li><strong id="b204396121545"><a name="b204396121545"></a><a name="b204396121545"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="p13663103020517"><a name="p13663103020517"></a><a name="p13663103020517"></a>When <strong id="b118113317464"><a name="b118113317464"></a><a name="b118113317464"></a>type</strong> is set to <strong id="b123241234104615"><a name="b123241234104615"></a><a name="b123241234104615"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="ul17531436125112"></a><a name="ul17531436125112"></a><ul id="ul17531436125112"><li><strong id="b1148622019474"><a name="b1148622019474"></a><a name="b1148622019474"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="b64314219474"><a name="b64314219474"></a><a name="b64314219474"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="b193647516516"><a name="b193647516516"></a><a name="b193647516516"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="row1946012463715"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p7401231193715"><a name="p7401231193715"></a><a name="p7401231193715"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p19401153118372"><a name="p19401153118372"></a><a name="p19401153118372"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p154011731133717"><a name="p154011731133717"></a><a name="p154011731133717"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p1238515351377"><a name="p1238515351377"></a><a name="p1238515351377"></a>Specifies whether reverse match is supported.</p>
<p id="p1938543553715"><a name="p1938543553715"></a><a name="p1938543553715"></a>The value can be <strong id="b13218122265"><a name="b13218122265"></a><a name="b13218122265"></a>true</strong> or <strong id="b1121913221068"><a name="b1121913221068"></a><a name="b1121913221068"></a>false</strong>. The default value is <strong id="b84235270616032"><a name="b84235270616032"></a><a name="b84235270616032"></a>false</strong>.</p>
<p id="p183851435173713"><a name="p183851435173713"></a><a name="p183851435173713"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row1413713493580"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p5137649185812"><a name="p5137649185812"></a><a name="p5137649185812"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p131371549135810"><a name="p131371549135810"></a><a name="p131371549135810"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p1013794914584"><a name="p1013794914584"></a><a name="p1013794914584"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p82048119202"><a name="p82048119202"></a><a name="p82048119202"></a>Specifies the key of the match content. The default value is <strong id="b163819591160"><a name="b163819591160"></a><a name="b163819591160"></a>null</strong>.</p>
<p id="p1747128122016"><a name="p1747128122016"></a><a name="p1747128122016"></a>This parameter is reserved.</p>
<p id="p1678425732713"><a name="p1678425732713"></a><a name="p1678425732713"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row18137184955815"><td class="cellrowborder" valign="top" width="25.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p121375495589"><a name="p121375495589"></a><a name="p121375495589"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.5.1.2 "><p id="p1413718493586"><a name="p1413718493586"></a><a name="p1413718493586"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.110000000000003%" headers="mcps1.2.5.1.3 "><p id="p141372496586"><a name="p141372496586"></a><a name="p141372496586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.49%" headers="mcps1.2.5.1.4 "><p id="p16872195212010"><a name="p16872195212010"></a><a name="p16872195212010"></a>Specifies the value of the match content. The value cannot contain spaces.</p>
<p id="p92220411286"><a name="p92220411286"></a><a name="p92220411286"></a>The value contains a maximum of 128 characters.</p>
<a name="ul75251828131120"></a><a name="ul75251828131120"></a><ul id="ul75251828131120"><li>When <strong id="b8423527069613"><a name="b8423527069613"></a><a name="b8423527069613"></a>type</strong> is set to <strong id="b559618228713"><a name="b559618228713"></a><a name="b559618228713"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="b84235270616193"><a name="b84235270616193"></a><a name="b84235270616193"></a>type</strong> is set to <strong id="b84235270611227"><a name="b84235270611227"></a><a name="b84235270611227"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="b84235270611314"><a name="b84235270611314"></a><a name="b84235270611314"></a>compare_type</strong> is set to <strong id="b84235270611323"><a name="b84235270611323"></a><a name="b84235270611323"></a>STARTS_WITH</strong> or <strong id="b84235270611326"><a name="b84235270611326"></a><a name="b84235270611326"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:| \/()[]{}</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section65071157321"></a>

**Table  4**  Response parameters

<a name="table14507554326"></a>
<table><thead align="left"><tr id="row1250714553214"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p125078553211"><a name="p125078553211"></a><a name="p125078553211"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.89%" id="mcps1.2.4.1.2"><p id="p1350718563211"><a name="p1350718563211"></a><a name="p1350718563211"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p81525464202"><a name="p81525464202"></a><a name="p81525464202"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1150716512324"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p350711512323"><a name="p350711512323"></a><a name="p350711512323"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p1150725193215"><a name="p1150725193215"></a><a name="p1150725193215"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p650713517328"><a name="p650713517328"></a><a name="p650713517328"></a>Specifies the forwarding rule. For details, see <a href="#table1212118142596">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **rule**  parameter description

<a name="table1212118142596"></a>
<table><thead align="left"><tr id="row18222814135918"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p102227144592"><a name="p102227144592"></a><a name="p102227144592"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p922291411591"><a name="p922291411591"></a><a name="p922291411591"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p98675571208"><a name="p98675571208"></a><a name="p98675571208"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row102221114205912"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p122261415596"><a name="p122261415596"></a><a name="p122261415596"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p923119572119"><a name="p923119572119"></a><a name="p923119572119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p52228141594"><a name="p52228141594"></a><a name="p52228141594"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
<tr id="row202222146591"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p11222111412593"><a name="p11222111412593"></a><a name="p11222111412593"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p4222914145911"><a name="p4222914145911"></a><a name="p4222914145911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1266711718204"><a name="p1266711718204"></a><a name="p1266711718204"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="p54077531303"><a name="p54077531303"></a><a name="p54077531303"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row722213149597"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1622251465915"><a name="p1622251465915"></a><a name="p1622251465915"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p19222111414597"><a name="p19222111414597"></a><a name="p19222111414597"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1979757131619"><a name="p1979757131619"></a><a name="p1979757131619"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="p179812717162"><a name="p179812717162"></a><a name="p179812717162"></a>The value can be <strong id="b194855147820"><a name="b194855147820"></a><a name="b194855147820"></a>true</strong> or <strong id="b1248715141382"><a name="b1248715141382"></a><a name="b1248715141382"></a>false</strong>.</p>
<p id="p159731852204013"><a name="p159731852204013"></a><a name="p159731852204013"></a>This parameter is reserved. The default value is <strong id="b136295564412"><a name="b136295564412"></a><a name="b136295564412"></a>true</strong>.</p>
</td>
</tr>
<tr id="row4224114155917"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p92241147592"><a name="p92241147592"></a><a name="p92241147592"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p222481475913"><a name="p222481475913"></a><a name="p222481475913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p199311319151611"><a name="p199311319151611"></a><a name="p199311319151611"></a>Specifies the match type of a forwarding rule.</p>
<p id="p293131991615"><a name="p293131991615"></a><a name="p293131991615"></a>The value can be one of the following:</p>
<a name="ul13931161917169"></a><a name="ul13931161917169"></a><ul id="ul13931161917169"><li><strong id="b142851011164818"><a name="b142851011164818"></a><a name="b142851011164818"></a>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong id="b11681722194812"><a name="b11681722194812"></a><a name="b11681722194812"></a>PATH</strong>: matches the path in the request.</li></ul>
</td>
</tr>
<tr id="row622461465910"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p162241814165916"><a name="p162241814165916"></a><a name="p162241814165916"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p12241214105911"><a name="p12241214105911"></a><a name="p12241214105911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p928234417166"><a name="p928234417166"></a><a name="p928234417166"></a>Specifies the match mode. The options are as follows:</p>
<p id="p112828447167"><a name="p112828447167"></a><a name="p112828447167"></a>When <strong id="b164379297485"><a name="b164379297485"></a><a name="b164379297485"></a>type</strong> is set to <strong id="b2043819291487"><a name="b2043819291487"></a><a name="b2043819291487"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="ul128264412167"></a><a name="ul128264412167"></a><ul id="ul128264412167"><li><strong id="b16405014151016"><a name="b16405014151016"></a><a name="b16405014151016"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="p2028224451611"><a name="p2028224451611"></a><a name="p2028224451611"></a>When <strong id="b18170829496"><a name="b18170829496"></a><a name="b18170829496"></a>type</strong> is set to <strong id="b517115211498"><a name="b517115211498"></a><a name="b517115211498"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="ul162821144131610"></a><a name="ul162821144131610"></a><ul id="ul162821144131610"><li><strong id="b1628118511493"><a name="b1628118511493"></a><a name="b1628118511493"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="b8539988491"><a name="b8539988491"></a><a name="b8539988491"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="b39271823111019"><a name="b39271823111019"></a><a name="b39271823111019"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="row322461410591"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p622481485911"><a name="p622481485911"></a><a name="p622481485911"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1622411412594"><a name="p1622411412594"></a><a name="p1622411412594"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1837110431511"><a name="p1837110431511"></a><a name="p1837110431511"></a>Specifies whether reverse match is supported.</p>
<p id="p1497849152414"><a name="p1497849152414"></a><a name="p1497849152414"></a>The value can be <strong id="b27267458912"><a name="b27267458912"></a><a name="b27267458912"></a>true</strong> or <strong id="b27281845194"><a name="b27281845194"></a><a name="b27281845194"></a>false</strong>. The default value is <strong id="b189421423910"><a name="b189421423910"></a><a name="b189421423910"></a>false</strong>.</p>
<p id="p1828957181510"><a name="p1828957181510"></a><a name="p1828957181510"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row19224714125916"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p172241014165910"><a name="p172241014165910"></a><a name="p172241014165910"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p922415146591"><a name="p922415146591"></a><a name="p922415146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p781771561717"><a name="p781771561717"></a><a name="p781771561717"></a>Specifies the key of the match content. The default value is <strong id="b485293415910"><a name="b485293415910"></a><a name="b485293415910"></a>null</strong>.</p>
<p id="p198171615161716"><a name="p198171615161716"></a><a name="p198171615161716"></a>This parameter is reserved.</p>
<p id="p463514574308"><a name="p463514574308"></a><a name="p463514574308"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row622481417593"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p15224151413595"><a name="p15224151413595"></a><a name="p15224151413595"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p622413146591"><a name="p622413146591"></a><a name="p622413146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p19314172610176"><a name="p19314172610176"></a><a name="p19314172610176"></a>Specifies the value of the match content.</p>
<p id="p162351209317"><a name="p162351209317"></a><a name="p162351209317"></a>The value contains a maximum of 128 characters.</p>
<a name="ul731432621713"></a><a name="ul731432621713"></a><ul id="ul731432621713"><li>When <strong id="b1980151018456"><a name="b1980151018456"></a><a name="b1980151018456"></a>type</strong> is set to <strong id="b128101044518"><a name="b128101044518"></a><a name="b128101044518"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="b6358111534519"><a name="b6358111534519"></a><a name="b6358111534519"></a>type</strong> is set to <strong id="b1835881514459"><a name="b1835881514459"></a><a name="b1835881514459"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="b17222517692"><a name="b17222517692"></a><a name="b17222517692"></a>compare_type</strong> is set to <strong id="b522313171592"><a name="b522313171592"></a><a name="b522313171592"></a>STARTS_WITH</strong> or <strong id="b102253171193"><a name="b102253171193"></a><a name="b102253171193"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:| \/()[]{}</li></ul>
</td>
</tr>
<tr id="row2224191419593"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2022412148597"><a name="p2022412148597"></a><a name="p2022412148597"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p622431415599"><a name="p622431415599"></a><a name="p622431415599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p14704205693714"><a name="p14704205693714"></a><a name="p14704205693714"></a>Specifies the provisioning status of the forwarding rule. The value can be <strong id="b931816301281"><a name="b931816301281"></a><a name="b931816301281"></a>ACTIVE</strong>, <strong id="b331911301289"><a name="b331911301289"></a><a name="b331911301289"></a>PENDING_CREATE</strong>, or <strong id="b2320630687"><a name="b2320630687"></a><a name="b2320630687"></a>ERROR</strong>.</p>
<p id="p178421832011"><a name="p178421832011"></a><a name="p178421832011"></a>The default value is <strong id="b134024270811"><a name="b134024270811"></a><a name="b134024270811"></a>ACTIVE</strong>.</p>
<p id="p210952312206"><a name="p210952312206"></a><a name="p210952312206"></a>This parameter is reserved.</p>
<p id="p81819140317"><a name="p81819140317"></a><a name="p81819140317"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1986856543"></a>

-   Example request: Adding a forwarding rule

    ```
    POST https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586/rules  
    
    {
        "rule": {
            "compare_type": "EQUAL_TO", 
            "type": "PATH", 
            "value": "/bbb.html"
        }
    }
    ```

-   Example response

    ```
    {
        "rule": {
            "compare_type": "EQUAL_TO", 
            "admin_state_up": true, 
            "provisioning_status": "ACTIVE",
            "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819", 
     
            "invert": false, 
            "value": "/bbb.html", 
            "key": null, 
            "type": "PATH", 
            "id": "c6f457b8-bf6f-45d7-be5c-a3226945b7b1"
        }
    }
    ```


## Status Code<a name="section1771830192518"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

