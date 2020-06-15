# Adding a Backend Server<a name="EN-US_TOPIC_0096561556"></a>

## Function<a name="section12327657133113"></a>

This API is used to add a backend server to a specific backend server group. After a backend server group is added to a listener, traffic is distributed to backend servers in this server group using the specified load balancing algorithm.

## URI<a name="en-us_topic_0049139657_section1420113"></a>

POST /v2.0/lbaas/pools/\{pool\_id\}/members

**Table  1**  Parameter description

<a name="table1853663311511"></a>
<table><thead align="left"><tr id="row17575233151512"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p145751333181512"><a name="p145751333181512"></a><a name="p145751333181512"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="p45284312273"><a name="p45284312273"></a><a name="p45284312273"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p8575933191519"><a name="p8575933191519"></a><a name="p8575933191519"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p7575433161518"><a name="p7575433161518"></a><a name="p7575433161518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4575183319152"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p4575433161515"><a name="p4575433161515"></a><a name="p4575433161515"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p457623311517"><a name="p457623311517"></a><a name="p457623311517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1957613311515"><a name="p1957613311515"></a><a name="p1957613311515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p957653301520"><a name="p957653301520"></a><a name="p957653301520"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139657_section12781022"></a>

Two backend servers in a backend server group cannot have the same private IP address and port number.

The subnet specified during server creation must be in the same VPC as the subnet from which the private IP address of the load balancer is assigned.

## Request<a name="en-us_topic_0049139657_section56342274"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0049139657_table20060988"></a>
<table><thead align="left"><tr id="en-us_topic_0049139657_row42045429"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139657_p50236607"><a name="en-us_topic_0049139657_p50236607"></a><a name="en-us_topic_0049139657_p50236607"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p1165111299278"><a name="p1165111299278"></a><a name="p1165111299278"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049139657_p42633357"><a name="en-us_topic_0049139657_p42633357"></a><a name="en-us_topic_0049139657_p42633357"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="p872854182812"><a name="p872854182812"></a><a name="p872854182812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139657_row20823715"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139657_p8999315"><a name="en-us_topic_0049139657_p8999315"></a><a name="en-us_topic_0049139657_p8999315"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p867665092712"><a name="p867665092712"></a><a name="p867665092712"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049139657_p55815296"><a name="en-us_topic_0049139657_p55815296"></a><a name="en-us_topic_0049139657_p55815296"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139657_p24745166"><a name="en-us_topic_0049139657_p24745166"></a><a name="en-us_topic_0049139657_p24745166"></a>Specifies the backend server. For details, see <a href="#table1686816641616">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **members**  parameter description

<a name="table1686816641616"></a>
<table><thead align="left"><tr id="row1248177161610"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p134810712160"><a name="p134810712160"></a><a name="p134810712160"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p54816721618"><a name="p54816721618"></a><a name="p54816721618"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p24817761618"><a name="p24817761618"></a><a name="p24817761618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="p16486771617"><a name="p16486771617"></a><a name="p16486771617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row648147111617"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139654_p691901312412"><a name="en-us_topic_0049139654_p691901312412"></a><a name="en-us_topic_0049139654_p691901312412"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p10490713160"><a name="p10490713160"></a><a name="p10490713160"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1548178167"><a name="p1548178167"></a><a name="p1548178167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p14191130133014"><a name="p14191130133014"></a><a name="p14191130133014"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p1649137101619"><a name="p1649137101619"></a><a name="p1649137101619"></a>The value must be the same as the value of <strong id="b31354117540"><a name="b31354117540"></a><a name="b31354117540"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row17492716167"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p3494771611"><a name="p3494771611"></a><a name="p3494771611"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p10491674163"><a name="p10491674163"></a><a name="p10491674163"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p11492771610"><a name="p11492771610"></a><a name="p11492771610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p1549137131615"><a name="p1549137131615"></a><a name="p1549137131615"></a>Specifies the backend server name. The value is an empty character string by default.</p>
<p id="p9157446165019"><a name="p9157446165019"></a><a name="p9157446165019"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row2499741612"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1749107141620"><a name="p1749107141620"></a><a name="p1749107141620"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p134916717160"><a name="p134916717160"></a><a name="p134916717160"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p12494731617"><a name="p12494731617"></a><a name="p12494731617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p121434772311"><a name="p121434772311"></a><a name="p121434772311"></a>Specifies the private IP address of the backend server. This IP address must be in the subnet specified by <strong id="b3212124818188"><a name="b3212124818188"></a><a name="b3212124818188"></a>subnet_id</strong>.</p>
<p id="p31969789144950"><a name="p31969789144950"></a><a name="p31969789144950"></a>This parameter can be set only to the IP address of the primary NIC, for example, 192.168.3.11.</p>
<p id="p127189485507"><a name="p127189485507"></a><a name="p127189485507"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row124997171613"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p04927111617"><a name="p04927111617"></a><a name="p04927111617"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p7491579161"><a name="p7491579161"></a><a name="p7491579161"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p3491073166"><a name="p3491073166"></a><a name="p3491073166"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p174915731618"><a name="p174915731618"></a><a name="p174915731618"></a>Specifies the port used by the backend server. The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="row3494713167"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p24910716162"><a name="p24910716162"></a><a name="p24910716162"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p104918701610"><a name="p104918701610"></a><a name="p104918701610"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p158985942913"><a name="p158985942913"></a><a name="p158985942913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p3542138124217"><a name="p3542138124217"></a><a name="p3542138124217"></a>Specifies the ID of the subnet where the backend server works.</p>
<p id="p27021957153415"><a name="p27021957153415"></a><a name="p27021957153415"></a>The private IP address of the backend server is in this subnet.</p>
<p id="p317019213435"><a name="p317019213435"></a><a name="p317019213435"></a>Only IPv4 subnets are supported.</p>
</td>
</tr>
<tr id="row34912710165"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1649679163"><a name="p1649679163"></a><a name="p1649679163"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p10498712165"><a name="p10498712165"></a><a name="p10498712165"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p114910781618"><a name="p114910781618"></a><a name="p114910781618"></a>Booleger</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p1558456113514"><a name="p1558456113514"></a><a name="p1558456113514"></a>Specifies the administrative status of the backend server. The value can be <strong id="b104154116316"><a name="b104154116316"></a><a name="b104154116316"></a>true</strong> or <strong id="b15104123110"><a name="b15104123110"></a><a name="b15104123110"></a>false</strong>.</p>
<p id="p88618783610"><a name="p88618783610"></a><a name="p88618783610"></a>Currently, the value can only be <strong id="b204617453313"><a name="b204617453313"></a><a name="b204617453313"></a>true</strong>.</p>
<div class="note" id="note1628355713358"><a name="note1628355713358"></a><a name="note1628355713358"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10283205710352"><a name="p10283205710352"></a><a name="p10283205710352"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="b84235270615599"><a name="b84235270615599"></a><a name="b84235270615599"></a>true</strong>. Otherwise, the value is <strong id="b842352706155915"><a name="b842352706155915"></a><a name="b842352706155915"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row10492076165"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p15494741610"><a name="p15494741610"></a><a name="p15494741610"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p8498791613"><a name="p8498791613"></a><a name="p8498791613"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1849197101610"><a name="p1849197101610"></a><a name="p1849197101610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p93020435366"><a name="p93020435366"></a><a name="p93020435366"></a>Specifies the backend server weight. The value ranges from <strong id="b18125124111810"><a name="b18125124111810"></a><a name="b18125124111810"></a>0</strong> to <strong id="b0469161061813"><a name="b0469161061813"></a><a name="b0469161061813"></a>100</strong>.</p>
<p id="p72901421173616"><a name="p72901421173616"></a><a name="p72901421173616"></a>If the value is <strong id="b7373131251815"><a name="b7373131251815"></a><a name="b7373131251815"></a>0</strong>, the backend server will not accept new requests. The default value is <strong>1</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139657_section37318421"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0049139657_table54050919"></a>
<table><thead align="left"><tr id="en-us_topic_0049139657_row57900534"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139657_p59431671"><a name="en-us_topic_0049139657_p59431671"></a><a name="en-us_topic_0049139657_p59431671"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139657_p49236012"><a name="en-us_topic_0049139657_p49236012"></a><a name="en-us_topic_0049139657_p49236012"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="p11701040112915"><a name="p11701040112915"></a><a name="p11701040112915"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139657_row21061526"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139657_p28262061"><a name="en-us_topic_0049139657_p28262061"></a><a name="en-us_topic_0049139657_p28262061"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139657_p7525633"><a name="en-us_topic_0049139657_p7525633"></a><a name="en-us_topic_0049139657_p7525633"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139657_p50666366"><a name="en-us_topic_0049139657_p50666366"></a><a name="en-us_topic_0049139657_p50666366"></a>Backend server parameters For details, see <a href="#table1096713051618">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **members**  parameter description

<a name="table1096713051618"></a>
<table><thead align="left"><tr id="row1215463171615"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p1315410319169"><a name="p1315410319169"></a><a name="p1315410319169"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p141541431101611"><a name="p141541431101611"></a><a name="p141541431101611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="p2154153161615"><a name="p2154153161615"></a><a name="p2154153161615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row161541231151616"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p71549319164"><a name="p71549319164"></a><a name="p71549319164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p937416199308"><a name="p937416199308"></a><a name="p937416199308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p6154231141610"><a name="p6154231141610"></a><a name="p6154231141610"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="row8154123119164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p2015420313169"><a name="p2015420313169"></a><a name="p2015420313169"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p131565312169"><a name="p131565312169"></a><a name="p131565312169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p201561631141618"><a name="p201561631141618"></a><a name="p201561631141618"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="p4289054517"><a name="p4289054517"></a><a name="p4289054517"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row41561731101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p2015683161617"><a name="p2015683161617"></a><a name="p2015683161617"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p915643117163"><a name="p915643117163"></a><a name="p915643117163"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p13156193151618"><a name="p13156193151618"></a><a name="p13156193151618"></a>Specifies the backend server name.</p>
<p id="p126641735112"><a name="p126641735112"></a><a name="p126641735112"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row12156113141613"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p215633112161"><a name="p215633112161"></a><a name="p215633112161"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p61561331181617"><a name="p61561331181617"></a><a name="p61561331181617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p2611194017408"><a name="p2611194017408"></a><a name="p2611194017408"></a>Specifies the private IP address of the backend server. This IP address must be in the subnet specified by <strong id="b17159113041919"><a name="b17159113041919"></a><a name="b17159113041919"></a>subnet_id</strong>.</p>
<p id="p18611164024019"><a name="p18611164024019"></a><a name="p18611164024019"></a>This parameter can be set only to the IP address of the primary NIC, for example, 192.168.3.11.</p>
<p id="p1314571145112"><a name="p1314571145112"></a><a name="p1314571145112"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row121562031101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1115653101620"><a name="p1115653101620"></a><a name="p1115653101620"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p111561631171619"><a name="p111561631171619"></a><a name="p111561631171619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p141561431161615"><a name="p141561431161615"></a><a name="p141561431161615"></a>Specifies the port used by the backend server. The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="row111561931111610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p171561231151617"><a name="p171561231151617"></a><a name="p171561231151617"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1577372523116"><a name="p1577372523116"></a><a name="p1577372523116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p986015317414"><a name="p986015317414"></a><a name="p986015317414"></a>Specifies the ID of the subnet where the backend server works. The private IP address of the backend server is in this subnet.</p>
<p id="p88604374112"><a name="p88604374112"></a><a name="p88604374112"></a>IPv6 subnets are not supported.</p>
</td>
</tr>
<tr id="row111561331101617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p19156231141611"><a name="p19156231141611"></a><a name="p19156231141611"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1915603181610"><a name="p1915603181610"></a><a name="p1915603181610"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p38145286413"><a name="p38145286413"></a><a name="p38145286413"></a>Specifies the administrative status of the backend server. The value can be <strong id="b1686217011263"><a name="b1686217011263"></a><a name="b1686217011263"></a>true</strong> or <strong id="b1886220182612"><a name="b1886220182612"></a><a name="b1886220182612"></a>false</strong>.</p>
<p id="p1881412814419"><a name="p1881412814419"></a><a name="p1881412814419"></a>Currently, the value can only be <strong id="b5251147172616"><a name="b5251147172616"></a><a name="b5251147172616"></a>true</strong>.</p>
<div class="note" id="note1873514247366"><a name="note1873514247366"></a><a name="note1873514247366"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1773662413613"><a name="p1773662413613"></a><a name="p1773662413613"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="b1772198369"><a name="b1772198369"></a><a name="b1772198369"></a>true</strong>. Otherwise, the value is <strong id="b2084725659"><a name="b2084725659"></a><a name="b2084725659"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row8156193116164"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p171561931151617"><a name="p171561931151617"></a><a name="p171561931151617"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p4156103110161"><a name="p4156103110161"></a><a name="p4156103110161"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p8605175104117"><a name="p8605175104117"></a><a name="p8605175104117"></a>Specifies the backend server weight. The value ranges from <strong id="b736895210190"><a name="b736895210190"></a><a name="b736895210190"></a>0</strong> to <strong id="b10369135211196"><a name="b10369135211196"></a><a name="b10369135211196"></a>100</strong>.</p>
<p id="p1460555119418"><a name="p1460555119418"></a><a name="p1460555119418"></a>If the value is <strong id="b142577543194"><a name="b142577543194"></a><a name="b142577543194"></a>0</strong>, the backend server will not accept new requests. The default value is <strong id="b7720155541911"><a name="b7720155541911"></a><a name="b7720155541911"></a>1</strong>.</p>
</td>
</tr>
<tr id="row7156631161615"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p31561031161610"><a name="p31561031161610"></a><a name="p31561031161610"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p715663171614"><a name="p715663171614"></a><a name="p715663171614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p187109210289"><a name="p187109210289"></a><a name="p187109210289"></a>Specifies the health check result of the backend server. The value can be one of the following:</p>
<a name="ul1229315244282"></a><a name="ul1229315244282"></a><ul id="ul1229315244282"><li><strong id="b1785155722116"><a name="b1785155722116"></a><a name="b1785155722116"></a>ONLINE</strong>: The health check is successfully conducted and the backend server is running properly.</li><li><strong id="b1827011282210"><a name="b1827011282210"></a><a name="b1827011282210"></a>OFFLINE</strong>: The health check is abnormal and the backend server is running improperly. The load balancer stops distributing traffic to this server until it recovers.</li><li><strong id="b23251732215"><a name="b23251732215"></a><a name="b23251732215"></a>NO_MONITOR</strong>: No health check is conducted. No health checks are configured, or the value of <strong id="b18170131918319"><a name="b18170131918319"></a><a name="b18170131918319"></a>admin_state_up</strong> is <strong id="b074113410326"><a name="b074113410326"></a><a name="b074113410326"></a>false</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section37264574173"></a>

-   <a name="li1069222685516"></a>Step 1: Query the subnet ID and IP address using the server ID.  **device\_id**  in the request indicates the server ID. Obtain the values of  **subnet\_id**  and  **ip\_address**  of the primary NIC \(the port for which  **primary\_interface**  is  **true**\) in the response body.

    ```
    GET https://{VPCEndpoint}/v2.0/ports?device_id=f738c464-b5c2-45df-86c0-7f436620cd54
    ```

    Example response

    ```
    {
        "ports": [
            {
                "id": "94971c39-46f0-443a-85e8-31cb7497c78e",
                "name": "",
                "status": "ACTIVE",
                "admin_state_up": true,
                "fixed_ips": [
                    {
                        "subnet_id": "33d8b01a-bbe6-41f4-bc45-78a1d284d503",
                        "ip_address": "192.168.44.11"
                    }
                ],
                "mac_address": "fa:16:3e:5c:d2:57",
                "network_id": "1b76b9c2-9b7e-4ced-81bd-d13f7389d7c9",
                "tenant_id": "04dd36f978800fe22f9bc00bea090736",
                "project_id": "04dd36f978800fe22f9bc00bea090736",
                "device_id": "f738c464-b5c2-45df-86c0-7f436620cd54",
                "device_owner": "compute:cn-north-4a",
                "security_groups": [
                    "a10dfc31-0055-4b84-b36e-1291b918125c",
                    "7a233393-5be2-4dff-8360-1558dd950f6e"
                ],
                "extra_dhcp_opts": [],
                "allowed_address_pairs": [],
                "binding:vnic_type": "normal",
                "binding:vif_details": {
                    "primary_interface": true
                },
                "binding:profile": {},
                "port_security_enabled": true,
                "created_at": "2019-11-12T17:17:51",
                "updated_at": "2019-11-12T17:17:51"
            }
        ]
    }
    ```

-   Step 2: Use the subnet ID and IP address obtained in  [▪ Step 1](#li1069222685516)  to add a backend server.

    ```
    POST https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members
    
    {
        "member": {
            "subnet_id": "33d8b01a-bbe6-41f4-bc45-78a1d284d503",
            "protocol_port": 88,
            "name": "member-jy-tt-1",
            "address": "192.168.44.11"
        }
    }
    ```

    Example response

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

