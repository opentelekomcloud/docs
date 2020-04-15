# Updating a Backend Server<a name="EN-US_TOPIC_0096561557"></a>

## Function<a name="en-us_topic_0049139658_section45208163"></a>

This API is used to update a backend server. You can modify its name and weight. You can set a larger weight for backend servers that can receive more traffic.

## URI<a name="en-us_topic_0049139658_section4220283"></a>

PUT /v2.0/lbaas/pools/\{pool\_id\}/members/\{member\_id\}

**Table  1**  Parameter description

<a name="table1885913523161"></a>
<table><thead align="left"><tr id="row1089314520167"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="p2893105251618"><a name="p2893105251618"></a><a name="p2893105251618"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.2"><p id="p58949525162"><a name="p58949525162"></a><a name="p58949525162"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p48940529160"><a name="p48940529160"></a><a name="p48940529160"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="p1889413524161"><a name="p1889413524161"></a><a name="p1889413524161"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row389416528162"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="p1289455281617"><a name="p1289455281617"></a><a name="p1289455281617"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.2 "><p id="p18946529167"><a name="p18946529167"></a><a name="p18946529167"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p1689410522165"><a name="p1689410522165"></a><a name="p1689410522165"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p14894135218168"><a name="p14894135218168"></a><a name="p14894135218168"></a>Specifies the backend server group ID.</p>
</td>
</tr>
<tr id="row9894115291615"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="p19894952151616"><a name="p19894952151616"></a><a name="p19894952151616"></a>member_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.2 "><p id="p138941152171612"><a name="p138941152171612"></a><a name="p138941152171612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p11894552121618"><a name="p11894552121618"></a><a name="p11894552121618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p1894125271615"><a name="p1894125271615"></a><a name="p1894125271615"></a>Specifies the backend server ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139658_section37982554"></a>

If the provisioning status of the associated load balancer is not  **ACTIVE**, the backend server cannot be updated.

## Request<a name="en-us_topic_0049139658_section40430446"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0049139658_table2134014"></a>
<table><thead align="left"><tr id="en-us_topic_0049139658_row2911981"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139658_p34543924"><a name="en-us_topic_0049139658_p34543924"></a><a name="en-us_topic_0049139658_p34543924"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="en-us_topic_0049139658_p46594488"><a name="en-us_topic_0049139658_p46594488"></a><a name="en-us_topic_0049139658_p46594488"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049139658_p16057184"><a name="en-us_topic_0049139658_p16057184"></a><a name="en-us_topic_0049139658_p16057184"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="p6768729185511"><a name="p6768729185511"></a><a name="p6768729185511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139658_row57380926"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139658_p17343428"><a name="en-us_topic_0049139658_p17343428"></a><a name="en-us_topic_0049139658_p17343428"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049139658_p62640398"><a name="en-us_topic_0049139658_p62640398"></a><a name="en-us_topic_0049139658_p62640398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049139658_p40707460"><a name="en-us_topic_0049139658_p40707460"></a><a name="en-us_topic_0049139658_p40707460"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139657_p24745166"><a name="en-us_topic_0049139657_p24745166"></a><a name="en-us_topic_0049139657_p24745166"></a>Specifies the backend server. For details, see <a href="#table86692915171">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **member**  parameter description

<a name="table86692915171"></a>
<table><thead align="left"><tr id="row2136102917173"><th class="cellrowborder" valign="top" width="26.632663266326627%" id="mcps1.2.5.1.1"><p id="p51361829161716"><a name="p51361829161716"></a><a name="p51361829161716"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.2"><p id="p213642951714"><a name="p213642951714"></a><a name="p213642951714"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.4013401340134%" id="mcps1.2.5.1.3"><p id="p1113682971717"><a name="p1113682971717"></a><a name="p1113682971717"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.85488548854885%" id="mcps1.2.5.1.4"><p id="p7136182981712"><a name="p7136182981712"></a><a name="p7136182981712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18136132913179"><td class="cellrowborder" valign="top" width="26.632663266326627%" headers="mcps1.2.5.1.1 "><p id="p51361429161716"><a name="p51361429161716"></a><a name="p51361429161716"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.2 "><p id="p11369296173"><a name="p11369296173"></a><a name="p11369296173"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.4013401340134%" headers="mcps1.2.5.1.3 "><p id="p16136129131712"><a name="p16136129131712"></a><a name="p16136129131712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.85488548854885%" headers="mcps1.2.5.1.4 "><p id="p1549137131615"><a name="p1549137131615"></a><a name="p1549137131615"></a>Specifies the backend server name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row16136142991717"><td class="cellrowborder" valign="top" width="26.632663266326627%" headers="mcps1.2.5.1.1 "><p id="p1113613292171"><a name="p1113613292171"></a><a name="p1113613292171"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.2 "><p id="p813792910178"><a name="p813792910178"></a><a name="p813792910178"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.4013401340134%" headers="mcps1.2.5.1.3 "><p id="p713618297172"><a name="p713618297172"></a><a name="p713618297172"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.85488548854885%" headers="mcps1.2.5.1.4 "><p id="p1558456113514"><a name="p1558456113514"></a><a name="p1558456113514"></a>Specifies the administrative status of the backend server. The value can be <strong id="b11681532318"><a name="b11681532318"></a><a name="b11681532318"></a>true</strong> or <strong id="b10257169311"><a name="b10257169311"></a><a name="b10257169311"></a>false</strong>.</p>
<p id="p88618783610"><a name="p88618783610"></a><a name="p88618783610"></a>Currently, the value can only be <strong id="b2082413267302"><a name="b2082413267302"></a><a name="b2082413267302"></a>true</strong>.</p>
<div class="note" id="note1628355713358"><a name="note1628355713358"></a><a name="note1628355713358"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10283205710352"><a name="p10283205710352"></a><a name="p10283205710352"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="b8417129143013"><a name="b8417129143013"></a><a name="b8417129143013"></a>true</strong>. Otherwise, the value is <strong id="b10418172993020"><a name="b10418172993020"></a><a name="b10418172993020"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row113742916172"><td class="cellrowborder" valign="top" width="26.632663266326627%" headers="mcps1.2.5.1.1 "><p id="p913710293172"><a name="p913710293172"></a><a name="p913710293172"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.2 "><p id="p10137172991712"><a name="p10137172991712"></a><a name="p10137172991712"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.4013401340134%" headers="mcps1.2.5.1.3 "><p id="p3137112971714"><a name="p3137112971714"></a><a name="p3137112971714"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.85488548854885%" headers="mcps1.2.5.1.4 "><p id="p1210816309619"><a name="p1210816309619"></a><a name="p1210816309619"></a>Specifies the backend server weight. The value ranges from <strong id="b17722143113012"><a name="b17722143113012"></a><a name="b17722143113012"></a>0</strong> to <strong id="b14723131133010"><a name="b14723131133010"></a><a name="b14723131133010"></a>100</strong>.</p>
<p id="p72901421173616"><a name="p72901421173616"></a><a name="p72901421173616"></a>If the value is <strong id="b1683233143319"><a name="b1683233143319"></a><a name="b1683233143319"></a>0</strong>, the backend server will not accept new requests. The default value is <strong>1</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139658_section28329695"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0049139658_table55481367"></a>
<table><thead align="left"><tr id="en-us_topic_0049139658_row33910007"><th class="cellrowborder" valign="top" width="23.41%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139658_p62356046"><a name="en-us_topic_0049139658_p62356046"></a><a name="en-us_topic_0049139658_p62356046"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139658_p17674957"><a name="en-us_topic_0049139658_p17674957"></a><a name="en-us_topic_0049139658_p17674957"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.59%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139658_p1281126"><a name="en-us_topic_0049139658_p1281126"></a><a name="en-us_topic_0049139658_p1281126"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139658_row36662351"><td class="cellrowborder" valign="top" width="23.41%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139658_p16860416"><a name="en-us_topic_0049139658_p16860416"></a><a name="en-us_topic_0049139658_p16860416"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139658_p23516450"><a name="en-us_topic_0049139658_p23516450"></a><a name="en-us_topic_0049139658_p23516450"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.59%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139658_p8152279"><a name="en-us_topic_0049139658_p8152279"></a><a name="en-us_topic_0049139658_p8152279"></a>Specifies the backend server. For details, see <a href="#table165363113183">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **members**  parameter description

<a name="table165363113183"></a>
<table><thead align="left"><tr id="en-us_topic_0096561556_row1215463171615"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561556_p1315410319169"><a name="en-us_topic_0096561556_p1315410319169"></a><a name="en-us_topic_0096561556_p1315410319169"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561556_p141541431101611"><a name="en-us_topic_0096561556_p141541431101611"></a><a name="en-us_topic_0096561556_p141541431101611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561556_p2154153161615"><a name="en-us_topic_0096561556_p2154153161615"></a><a name="en-us_topic_0096561556_p2154153161615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561556_row161541231151616"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p71549319164"><a name="en-us_topic_0096561556_p71549319164"></a><a name="en-us_topic_0096561556_p71549319164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p937416199308"><a name="en-us_topic_0096561556_p937416199308"></a><a name="en-us_topic_0096561556_p937416199308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p6154231141610"><a name="en-us_topic_0096561556_p6154231141610"></a><a name="en-us_topic_0096561556_p6154231141610"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row8154123119164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p2015420313169"><a name="en-us_topic_0096561556_p2015420313169"></a><a name="en-us_topic_0096561556_p2015420313169"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p131565312169"><a name="en-us_topic_0096561556_p131565312169"></a><a name="en-us_topic_0096561556_p131565312169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p201561631141618"><a name="en-us_topic_0096561556_p201561631141618"></a><a name="en-us_topic_0096561556_p201561631141618"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="en-us_topic_0096561556_p4289054517"><a name="en-us_topic_0096561556_p4289054517"></a><a name="en-us_topic_0096561556_p4289054517"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row41561731101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p2015683161617"><a name="en-us_topic_0096561556_p2015683161617"></a><a name="en-us_topic_0096561556_p2015683161617"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p915643117163"><a name="en-us_topic_0096561556_p915643117163"></a><a name="en-us_topic_0096561556_p915643117163"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p13156193151618"><a name="en-us_topic_0096561556_p13156193151618"></a><a name="en-us_topic_0096561556_p13156193151618"></a>Specifies the backend server name.</p>
<p id="en-us_topic_0096561556_p126641735112"><a name="en-us_topic_0096561556_p126641735112"></a><a name="en-us_topic_0096561556_p126641735112"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row12156113141613"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p215633112161"><a name="en-us_topic_0096561556_p215633112161"></a><a name="en-us_topic_0096561556_p215633112161"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p61561331181617"><a name="en-us_topic_0096561556_p61561331181617"></a><a name="en-us_topic_0096561556_p61561331181617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p2611194017408"><a name="en-us_topic_0096561556_p2611194017408"></a><a name="en-us_topic_0096561556_p2611194017408"></a>Specifies the private IP address of the backend server. This IP address must be in the subnet specified by <strong id="en-us_topic_0096561556_b17159113041919"><a name="en-us_topic_0096561556_b17159113041919"></a><a name="en-us_topic_0096561556_b17159113041919"></a>subnet_id</strong>.</p>
<p id="en-us_topic_0096561556_p18611164024019"><a name="en-us_topic_0096561556_p18611164024019"></a><a name="en-us_topic_0096561556_p18611164024019"></a>This parameter can be set only to the IP address of the primary NIC, for example, 192.168.3.11.</p>
<p id="en-us_topic_0096561556_p1314571145112"><a name="en-us_topic_0096561556_p1314571145112"></a><a name="en-us_topic_0096561556_p1314571145112"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row121562031101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p1115653101620"><a name="en-us_topic_0096561556_p1115653101620"></a><a name="en-us_topic_0096561556_p1115653101620"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p111561631171619"><a name="en-us_topic_0096561556_p111561631171619"></a><a name="en-us_topic_0096561556_p111561631171619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p141561431161615"><a name="en-us_topic_0096561556_p141561431161615"></a><a name="en-us_topic_0096561556_p141561431161615"></a>Specifies the port used by the backend server. The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row111561931111610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p171561231151617"><a name="en-us_topic_0096561556_p171561231151617"></a><a name="en-us_topic_0096561556_p171561231151617"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p1577372523116"><a name="en-us_topic_0096561556_p1577372523116"></a><a name="en-us_topic_0096561556_p1577372523116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p986015317414"><a name="en-us_topic_0096561556_p986015317414"></a><a name="en-us_topic_0096561556_p986015317414"></a>Specifies the ID of the subnet where the backend server works. The private IP address of the backend server is in this subnet.</p>
<p id="en-us_topic_0096561556_p88604374112"><a name="en-us_topic_0096561556_p88604374112"></a><a name="en-us_topic_0096561556_p88604374112"></a>IPv6 subnets are not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row111561331101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p19156231141611"><a name="en-us_topic_0096561556_p19156231141611"></a><a name="en-us_topic_0096561556_p19156231141611"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p1915603181610"><a name="en-us_topic_0096561556_p1915603181610"></a><a name="en-us_topic_0096561556_p1915603181610"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p38145286413"><a name="en-us_topic_0096561556_p38145286413"></a><a name="en-us_topic_0096561556_p38145286413"></a>Specifies the administrative status of the backend server. The value can be <strong id="en-us_topic_0096561556_b1686217011263"><a name="en-us_topic_0096561556_b1686217011263"></a><a name="en-us_topic_0096561556_b1686217011263"></a>true</strong> or <strong id="en-us_topic_0096561556_b1886220182612"><a name="en-us_topic_0096561556_b1886220182612"></a><a name="en-us_topic_0096561556_b1886220182612"></a>false</strong>.</p>
<p id="en-us_topic_0096561556_p1881412814419"><a name="en-us_topic_0096561556_p1881412814419"></a><a name="en-us_topic_0096561556_p1881412814419"></a>Currently, the value can only be <strong id="en-us_topic_0096561556_b5251147172616"><a name="en-us_topic_0096561556_b5251147172616"></a><a name="en-us_topic_0096561556_b5251147172616"></a>true</strong>.</p>
<div class="note" id="en-us_topic_0096561556_note1873514247366"><a name="en-us_topic_0096561556_note1873514247366"></a><a name="en-us_topic_0096561556_note1873514247366"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561556_p1773662413613"><a name="en-us_topic_0096561556_p1773662413613"></a><a name="en-us_topic_0096561556_p1773662413613"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="en-us_topic_0096561556_b909185759"><a name="en-us_topic_0096561556_b909185759"></a><a name="en-us_topic_0096561556_b909185759"></a>true</strong>. Otherwise, the value is <strong id="en-us_topic_0096561556_b1380237858"><a name="en-us_topic_0096561556_b1380237858"></a><a name="en-us_topic_0096561556_b1380237858"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0096561556_row8156193116164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p171561931151617"><a name="en-us_topic_0096561556_p171561931151617"></a><a name="en-us_topic_0096561556_p171561931151617"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p4156103110161"><a name="en-us_topic_0096561556_p4156103110161"></a><a name="en-us_topic_0096561556_p4156103110161"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p8605175104117"><a name="en-us_topic_0096561556_p8605175104117"></a><a name="en-us_topic_0096561556_p8605175104117"></a>Specifies the backend server weight. The value ranges from <strong id="en-us_topic_0096561556_b736895210190"><a name="en-us_topic_0096561556_b736895210190"></a><a name="en-us_topic_0096561556_b736895210190"></a>0</strong> to <strong id="en-us_topic_0096561556_b10369135211196"><a name="en-us_topic_0096561556_b10369135211196"></a><a name="en-us_topic_0096561556_b10369135211196"></a>100</strong>.</p>
<p id="en-us_topic_0096561556_p1460555119418"><a name="en-us_topic_0096561556_p1460555119418"></a><a name="en-us_topic_0096561556_p1460555119418"></a>If the value is <strong id="en-us_topic_0096561556_b142577543194"><a name="en-us_topic_0096561556_b142577543194"></a><a name="en-us_topic_0096561556_b142577543194"></a>0</strong>, the backend server will not accept new requests. The default value is <strong id="en-us_topic_0096561556_b7720155541911"><a name="en-us_topic_0096561556_b7720155541911"></a><a name="en-us_topic_0096561556_b7720155541911"></a>1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561556_row7156631161615"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561556_p31561031161610"><a name="en-us_topic_0096561556_p31561031161610"></a><a name="en-us_topic_0096561556_p31561031161610"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561556_p715663171614"><a name="en-us_topic_0096561556_p715663171614"></a><a name="en-us_topic_0096561556_p715663171614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561556_p187109210289"><a name="en-us_topic_0096561556_p187109210289"></a><a name="en-us_topic_0096561556_p187109210289"></a>Specifies the health check result of the backend server. The value can be one of the following:</p>
<a name="en-us_topic_0096561556_ul1229315244282"></a><a name="en-us_topic_0096561556_ul1229315244282"></a><ul id="en-us_topic_0096561556_ul1229315244282"><li><strong id="en-us_topic_0096561556_b1785155722116"><a name="en-us_topic_0096561556_b1785155722116"></a><a name="en-us_topic_0096561556_b1785155722116"></a>ONLINE</strong>: The health check is successfully conducted and the backend server is running properly.</li><li><strong id="en-us_topic_0096561556_b1827011282210"><a name="en-us_topic_0096561556_b1827011282210"></a><a name="en-us_topic_0096561556_b1827011282210"></a>OFFLINE</strong>: The health check is abnormal and the backend server is running improperly. The load balancer stops distributing traffic to this server until it recovers.</li><li><strong id="en-us_topic_0096561556_b23251732215"><a name="en-us_topic_0096561556_b23251732215"></a><a name="en-us_topic_0096561556_b23251732215"></a>NO_MONITOR</strong>: No health check is conducted. No health checks are configured, or the value of <strong id="en-us_topic_0096561556_b18170131918319"><a name="en-us_topic_0096561556_b18170131918319"></a><a name="en-us_topic_0096561556_b18170131918319"></a>admin_state_up</strong> is <strong id="en-us_topic_0096561556_b074113410326"><a name="en-us_topic_0096561556_b074113410326"></a><a name="en-us_topic_0096561556_b074113410326"></a>false</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1712145517474"></a>

-   Example request: Updating the name and weight of a backend server

    ```
    PUT https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members/c0042496-e220-44f6-914b-e6ca33bab503 
    
    { 
        "member": { 
            "name": "member create test", 
            "weight": 10
        } 
    }
    ```


-   Example response

    ```
    {
        "member": {
            "name": "member-jy-tt-1", 
            "weight": 1, 
            "admin_state_up": true, 
            "subnet_id": "33d8b01a-bbe6-41f4-bc45-78a1d284d503", 
            "tenant_id": "145483a5107745e9b3d80f956713e6a3",
            "address": "192.168.44.11", 
            "protocol_port": 88, 
            "operating_status": "ONLINE", 
            "id": "c0042496-e220-44f6-914b-e6ca33bab503"
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

