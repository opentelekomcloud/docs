# Querying Details of a Health Check<a name="EN-US_TOPIC_0096561562"></a>

## Function<a name="en-us_topic_0049139664_section19450451"></a>

This API is used to query details about a health check.

## URI<a name="en-us_topic_0049139664_section40836337"></a>

GET /v2.0/lbaas/healthmonitors/\{healthmonitor\_id\}

**Table  1**  Parameter description

<a name="table176971727192716"></a>
<table><thead align="left"><tr id="row197661727142714"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p9766142719279"><a name="p9766142719279"></a><a name="p9766142719279"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="p2766132715279"><a name="p2766132715279"></a><a name="p2766132715279"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p87661627142718"><a name="p87661627142718"></a><a name="p87661627142718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p7766112732717"><a name="p7766112732717"></a><a name="p7766112732717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row67681227162719"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1576822718273"><a name="p1576822718273"></a><a name="p1576822718273"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p20768122711272"><a name="p20768122711272"></a><a name="p20768122711272"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1768827202719"><a name="p1768827202719"></a><a name="p1768827202719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p7768162762710"><a name="p7768162762710"></a><a name="p7768162762710"></a>Specifies the health check ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0049139664_section28625159"></a>

None

## Response<a name="en-us_topic_0049139664_section56299846"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0049139664_table15263883"></a>
<table><thead align="left"><tr id="en-us_topic_0049139664_row23849822"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139664_p52787457"><a name="en-us_topic_0049139664_p52787457"></a><a name="en-us_topic_0049139664_p52787457"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139664_p47925604"><a name="en-us_topic_0049139664_p47925604"></a><a name="en-us_topic_0049139664_p47925604"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63.63636363636363%" id="mcps1.2.4.1.3"><p id="p6230154717271"><a name="p6230154717271"></a><a name="p6230154717271"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139664_row5163807"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139664_p15615252"><a name="en-us_topic_0049139664_p15615252"></a><a name="en-us_topic_0049139664_p15615252"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139664_p56875922"><a name="en-us_topic_0049139664_p56875922"></a><a name="en-us_topic_0049139664_p56875922"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="63.63636363636363%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139664_p37641542"><a name="en-us_topic_0049139664_p37641542"></a><a name="en-us_topic_0049139664_p37641542"></a>Specifies the health check. For details, see <a href="#table167973062820">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **healthmonitor**  parameter description

<a name="table167973062820"></a>
<table><thead align="left"><tr id="en-us_topic_0096561563_row19929157112914"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561563_p59295713297"><a name="en-us_topic_0096561563_p59295713297"></a><a name="en-us_topic_0096561563_p59295713297"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561563_p79292720293"><a name="en-us_topic_0096561563_p79292720293"></a><a name="en-us_topic_0096561563_p79292720293"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561563_p1258101218348"><a name="en-us_topic_0096561563_p1258101218348"></a><a name="en-us_topic_0096561563_p1258101218348"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561563_row1192911772916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p5929177112912"><a name="en-us_topic_0096561563_p5929177112912"></a><a name="en-us_topic_0096561563_p5929177112912"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p5947132518343"><a name="en-us_topic_0096561563_p5947132518343"></a><a name="en-us_topic_0096561563_p5947132518343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p109296702911"><a name="en-us_topic_0096561563_p109296702911"></a><a name="en-us_topic_0096561563_p109296702911"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row792915762911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p59290711296"><a name="en-us_topic_0096561563_p59290711296"></a><a name="en-us_topic_0096561563_p59290711296"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1792918772913"><a name="en-us_topic_0096561563_p1792918772913"></a><a name="en-us_topic_0096561563_p1792918772913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p269292715918"><a name="en-us_topic_0096561563_p269292715918"></a><a name="en-us_topic_0096561563_p269292715918"></a>Specifies the ID of the project where the health check is performed.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row209291674295"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p692919752912"><a name="en-us_topic_0096561563_p692919752912"></a><a name="en-us_topic_0096561563_p692919752912"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p131123323411"><a name="en-us_topic_0096561563_p131123323411"></a><a name="en-us_topic_0096561563_p131123323411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p199294713299"><a name="en-us_topic_0096561563_p199294713299"></a><a name="en-us_topic_0096561563_p199294713299"></a>Specifies the health check name.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row5929279299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p892987162910"><a name="en-us_topic_0096561563_p892987162910"></a><a name="en-us_topic_0096561563_p892987162910"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p792918772915"><a name="en-us_topic_0096561563_p792918772915"></a><a name="en-us_topic_0096561563_p792918772915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p119293720295"><a name="en-us_topic_0096561563_p119293720295"></a><a name="en-us_topic_0096561563_p119293720295"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="en-us_topic_0096561563_b53341117227"><a name="en-us_topic_0096561563_b53341117227"></a><a name="en-us_topic_0096561563_b53341117227"></a>1</strong> to <strong id="en-us_topic_0096561563_b1233617116226"><a name="en-us_topic_0096561563_b1233617116226"></a><a name="en-us_topic_0096561563_b1233617116226"></a>50</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row179291072296"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p15929157192911"><a name="en-us_topic_0096561563_p15929157192911"></a><a name="en-us_topic_0096561563_p15929157192911"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p178711239193411"><a name="en-us_topic_0096561563_p178711239193411"></a><a name="en-us_topic_0096561563_p178711239193411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p189309702917"><a name="en-us_topic_0096561563_p189309702917"></a><a name="en-us_topic_0096561563_p189309702917"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="en-us_topic_0096561563_b8737342112519"><a name="en-us_topic_0096561563_b8737342112519"></a><a name="en-us_topic_0096561563_b8737342112519"></a>fail</strong> to <strong id="en-us_topic_0096561563_b97392422258"><a name="en-us_topic_0096561563_b97392422258"></a><a name="en-us_topic_0096561563_b97392422258"></a>success</strong>. The value ranges from <strong id="en-us_topic_0096561563_b18741134213251"><a name="en-us_topic_0096561563_b18741134213251"></a><a name="en-us_topic_0096561563_b18741134213251"></a>1</strong> to <strong id="en-us_topic_0096561563_b18742842132513"><a name="en-us_topic_0096561563_b18742842132513"></a><a name="en-us_topic_0096561563_b18742842132513"></a>10</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1193097152917"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p1793016712298"><a name="en-us_topic_0096561563_p1793016712298"></a><a name="en-us_topic_0096561563_p1793016712298"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p893015710294"><a name="en-us_topic_0096561563_p893015710294"></a><a name="en-us_topic_0096561563_p893015710294"></a>Specifies the ID of the backend server group associated with the health check.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row2930197182911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p79301777292"><a name="en-us_topic_0096561563_p79301777292"></a><a name="en-us_topic_0096561563_p79301777292"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p293017715298"><a name="en-us_topic_0096561563_p293017715298"></a><a name="en-us_topic_0096561563_p293017715298"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p88489418492"><a name="en-us_topic_0096561563_p88489418492"></a><a name="en-us_topic_0096561563_p88489418492"></a>Specifies the administrative status of the health check.</p>
<p id="en-us_topic_0096561563_p19848040494"><a name="en-us_topic_0096561563_p19848040494"></a><a name="en-us_topic_0096561563_p19848040494"></a>The value can be <strong id="en-us_topic_0096561563_b13310921202213"><a name="en-us_topic_0096561563_b13310921202213"></a><a name="en-us_topic_0096561563_b13310921202213"></a>true</strong> or <strong id="en-us_topic_0096561563_b131282110226"><a name="en-us_topic_0096561563_b131282110226"></a><a name="en-us_topic_0096561563_b131282110226"></a>false</strong>. The default value is <strong id="en-us_topic_0096561563_b83981522142217"><a name="en-us_topic_0096561563_b83981522142217"></a><a name="en-us_topic_0096561563_b83981522142217"></a>true</strong>.</p>
<a name="en-us_topic_0096561563_ul1848244497"></a><a name="en-us_topic_0096561563_ul1848244497"></a><ul id="en-us_topic_0096561563_ul1848244497"><li><strong id="en-us_topic_0096561563_b1572441093412"><a name="en-us_topic_0096561563_b1572441093412"></a><a name="en-us_topic_0096561563_b1572441093412"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="en-us_topic_0096561563_b157791112193412"><a name="en-us_topic_0096561563_b157791112193412"></a><a name="en-us_topic_0096561563_b157791112193412"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561563_row09302716299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p19303782913"><a name="en-us_topic_0096561563_p19303782913"></a><a name="en-us_topic_0096561563_p19303782913"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p179315732915"><a name="en-us_topic_0096561563_p179315732915"></a><a name="en-us_topic_0096561563_p179315732915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p37112334494"><a name="en-us_topic_0096561563_p37112334494"></a><a name="en-us_topic_0096561563_p37112334494"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="en-us_topic_0096561563_b1380316275226"><a name="en-us_topic_0096561563_b1380316275226"></a><a name="en-us_topic_0096561563_b1380316275226"></a>1</strong> to <strong id="en-us_topic_0096561563_b1580411278227"><a name="en-us_topic_0096561563_b1580411278227"></a><a name="en-us_topic_0096561563_b1580411278227"></a>50</strong>.</p>
<div class="note" id="en-us_topic_0096561563_note77113384910"><a name="en-us_topic_0096561563_note77113384910"></a><a name="en-us_topic_0096561563_note77113384910"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561563_p57123374911"><a name="en-us_topic_0096561563_p57123374911"></a><a name="en-us_topic_0096561563_p57123374911"></a>You are advised to set the value less than that of parameter <strong id="en-us_topic_0096561563_b10582112915225"><a name="en-us_topic_0096561563_b10582112915225"></a><a name="en-us_topic_0096561563_b10582112915225"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1793116752912"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p6931579296"><a name="en-us_topic_0096561563_p6931579296"></a><a name="en-us_topic_0096561563_p6931579296"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p49311173296"><a name="en-us_topic_0096561563_p49311173296"></a><a name="en-us_topic_0096561563_p49311173296"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p87193317494"><a name="en-us_topic_0096561563_p87193317494"></a><a name="en-us_topic_0096561563_p87193317494"></a>Specifies the health check protocol.</p>
<p id="en-us_topic_0096561563_p5711533184919"><a name="en-us_topic_0096561563_p5711533184919"></a><a name="en-us_topic_0096561563_p5711533184919"></a>The value can be <strong id="en-us_topic_0096561563_b9594432122210"><a name="en-us_topic_0096561563_b9594432122210"></a><a name="en-us_topic_0096561563_b9594432122210"></a>TCP</strong>, <strong id="en-us_topic_0096561563_b19595183219229"><a name="en-us_topic_0096561563_b19595183219229"></a><a name="en-us_topic_0096561563_b19595183219229"></a>UDP_CONNECT</strong>, or <strong id="en-us_topic_0096561563_b14595123282211"><a name="en-us_topic_0096561563_b14595123282211"></a><a name="en-us_topic_0096561563_b14595123282211"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row79313702914"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p29315710299"><a name="en-us_topic_0096561563_p29315710299"></a><a name="en-us_topic_0096561563_p29315710299"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1193119762917"><a name="en-us_topic_0096561563_p1193119762917"></a><a name="en-us_topic_0096561563_p1193119762917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p19915125974920"><a name="en-us_topic_0096561563_p19915125974920"></a><a name="en-us_topic_0096561563_p19915125974920"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="en-us_topic_0096561563_p1891535916496"><a name="en-us_topic_0096561563_p1891535916496"></a><a name="en-us_topic_0096561563_p1891535916496"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row129325719290"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p4639141253611"><a name="en-us_topic_0096561563_p4639141253611"></a><a name="en-us_topic_0096561563_p4639141253611"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1263931216363"><a name="en-us_topic_0096561563_p1263931216363"></a><a name="en-us_topic_0096561563_p1263931216363"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p30010494"><a name="en-us_topic_0096561563_p30010494"></a><a name="en-us_topic_0096561563_p30010494"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="en-us_topic_0096561563_p1658995"><a name="en-us_topic_0096561563_p1658995"></a><a name="en-us_topic_0096561563_p1658995"></a>A single value, such as 200</p>
<p id="en-us_topic_0096561563_p14930959"><a name="en-us_topic_0096561563_p14930959"></a><a name="en-us_topic_0096561563_p14930959"></a>A list of values, such as 200 and 202</p>
<p id="en-us_topic_0096561563_p160907"><a name="en-us_topic_0096561563_p160907"></a><a name="en-us_topic_0096561563_p160907"></a>A value range, such as 200 to 204</p>
<p id="en-us_topic_0096561563_p1448168"><a name="en-us_topic_0096561563_p1448168"></a><a name="en-us_topic_0096561563_p1448168"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b6389401468"><a name="en-us_topic_0096561563_b6389401468"></a><a name="en-us_topic_0096561563_b6389401468"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b113907012461"><a name="en-us_topic_0096561563_b113907012461"></a><a name="en-us_topic_0096561563_b113907012461"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p13033520"><a name="en-us_topic_0096561563_p13033520"></a><a name="en-us_topic_0096561563_p13033520"></a>Currently, this parameter is not supported and is fixed at <strong id="en-us_topic_0096561563_b84235270619455"><a name="en-us_topic_0096561563_b84235270619455"></a><a name="en-us_topic_0096561563_b84235270619455"></a>200</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1993247182913"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p159326713290"><a name="en-us_topic_0096561563_p159326713290"></a><a name="en-us_topic_0096561563_p159326713290"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p179321712912"><a name="en-us_topic_0096561563_p179321712912"></a><a name="en-us_topic_0096561563_p179321712912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p12394754125016"><a name="en-us_topic_0096561563_p12394754125016"></a><a name="en-us_topic_0096561563_p12394754125016"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="en-us_topic_0096561563_p73941354135010"><a name="en-us_topic_0096561563_p73941354135010"></a><a name="en-us_topic_0096561563_p73941354135010"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b55255217488"><a name="en-us_topic_0096561563_b55255217488"></a><a name="en-us_topic_0096561563_b55255217488"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b1752620264817"><a name="en-us_topic_0096561563_b1752620264817"></a><a name="en-us_topic_0096561563_b1752620264817"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p14394115411501"><a name="en-us_topic_0096561563_p14394115411501"></a><a name="en-us_topic_0096561563_p14394115411501"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="en-us_topic_0096561563_p15394145435010"><a name="en-us_topic_0096561563_p15394145435010"></a><a name="en-us_topic_0096561563_p15394145435010"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="en-us_topic_0096561563_b67911125183711"><a name="en-us_topic_0096561563_b67911125183711"></a><a name="en-us_topic_0096561563_b67911125183711"></a>www.test.com</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row593217719299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p793277152911"><a name="en-us_topic_0096561563_p793277152911"></a><a name="en-us_topic_0096561563_p793277152911"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1593247182917"><a name="en-us_topic_0096561563_p1593247182917"></a><a name="en-us_topic_0096561563_p1593247182917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p6417986512"><a name="en-us_topic_0096561563_p6417986512"></a><a name="en-us_topic_0096561563_p6417986512"></a>Specifies the HTTP request path for the health check. The default value is <strong id="en-us_topic_0096561563_b1437591082310"><a name="en-us_topic_0096561563_b1437591082310"></a><a name="en-us_topic_0096561563_b1437591082310"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="en-us_topic_0096561563_p64181884511"><a name="en-us_topic_0096561563_p64181884511"></a><a name="en-us_topic_0096561563_p64181884511"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b16827165119475"><a name="en-us_topic_0096561563_b16827165119475"></a><a name="en-us_topic_0096561563_b16827165119475"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b188288512479"><a name="en-us_topic_0096561563_b188288512479"></a><a name="en-us_topic_0096561563_b188288512479"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p1341818185114"><a name="en-us_topic_0096561563_p1341818185114"></a><a name="en-us_topic_0096561563_p1341818185114"></a>An example value is <strong id="en-us_topic_0096561563_b20236172942318"><a name="en-us_topic_0096561563_b20236172942318"></a><a name="en-us_topic_0096561563_b20236172942318"></a>/test</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row3932167132916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p793218711296"><a name="en-us_topic_0096561563_p793218711296"></a><a name="en-us_topic_0096561563_p793218711296"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1893212710291"><a name="en-us_topic_0096561563_p1893212710291"></a><a name="en-us_topic_0096561563_p1893212710291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p48511267514"><a name="en-us_topic_0096561563_p48511267514"></a><a name="en-us_topic_0096561563_p48511267514"></a>Specifies the HTTP request method. The default value is <strong id="en-us_topic_0096561563_b19886729123413"><a name="en-us_topic_0096561563_b19886729123413"></a><a name="en-us_topic_0096561563_b19886729123413"></a>GET</strong>.</p>
<p id="en-us_topic_0096561563_p11851326135110"><a name="en-us_topic_0096561563_p11851326135110"></a><a name="en-us_topic_0096561563_p11851326135110"></a>The value can be <strong id="en-us_topic_0096561563_b205241432133411"><a name="en-us_topic_0096561563_b205241432133411"></a><a name="en-us_topic_0096561563_b205241432133411"></a>GET</strong>, <strong id="en-us_topic_0096561563_b1524432123415"><a name="en-us_topic_0096561563_b1524432123415"></a><a name="en-us_topic_0096561563_b1524432123415"></a>HEAD</strong>, <strong id="en-us_topic_0096561563_b1452533293413"><a name="en-us_topic_0096561563_b1452533293413"></a><a name="en-us_topic_0096561563_b1452533293413"></a>POST</strong>, <strong id="en-us_topic_0096561563_b12525832163420"><a name="en-us_topic_0096561563_b12525832163420"></a><a name="en-us_topic_0096561563_b12525832163420"></a>PUT</strong>, <strong id="en-us_topic_0096561563_b452653210347"><a name="en-us_topic_0096561563_b452653210347"></a><a name="en-us_topic_0096561563_b452653210347"></a>DELETE</strong>, <strong id="en-us_topic_0096561563_b2052773214341"><a name="en-us_topic_0096561563_b2052773214341"></a><a name="en-us_topic_0096561563_b2052773214341"></a>TRACE</strong>, <strong id="en-us_topic_0096561563_b152812324344"><a name="en-us_topic_0096561563_b152812324344"></a><a name="en-us_topic_0096561563_b152812324344"></a>OPTIONS</strong>, <strong id="en-us_topic_0096561563_b75281932203417"><a name="en-us_topic_0096561563_b75281932203417"></a><a name="en-us_topic_0096561563_b75281932203417"></a>CONNECT</strong>, and <strong id="en-us_topic_0096561563_b7529193220347"><a name="en-us_topic_0096561563_b7529193220347"></a><a name="en-us_topic_0096561563_b7529193220347"></a>PATCH</strong>.</p>
<p id="en-us_topic_0096561563_p485142665115"><a name="en-us_topic_0096561563_p485142665115"></a><a name="en-us_topic_0096561563_p485142665115"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b782231144617"><a name="en-us_topic_0096561563_b782231144617"></a><a name="en-us_topic_0096561563_b782231144617"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b178221611124616"><a name="en-us_topic_0096561563_b178221611124616"></a><a name="en-us_topic_0096561563_b178221611124616"></a>HTTP</strong>.</p>
<div class="note" id="en-us_topic_0096561563_note985119267515"><a name="en-us_topic_0096561563_note985119267515"></a><a name="en-us_topic_0096561563_note985119267515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561563_p1885112263511"><a name="en-us_topic_0096561563_p1885112263511"></a><a name="en-us_topic_0096561563_p1885112263511"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1138642934813"></a>

-   Example request: Querying details of a health check

    ```
    GET https://{Endpoint}/v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412
    ```

-   Example response

    ```
    {
      "healthmonitor": {
        "name": "",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
        "domain_name": null,
        "delay": 10,
        "expected_codes": "200-204,300-302,401",
        "max_retries": 10,
        
        "http_method": "GET",
        "timeout": 10,
        "pools": [
          {
            "id": "bb44bffb-05d9-412c-9d9c-b189d9e14193"
          }
        ],
        "url_path": "/",
        "type": "HTTP",
        "id": "61c24cba-19bb-45c1-a013-7565e5f98872",
        "monitor_port": 112
      }
    }
    ```


## Status Code<a name="en-us_topic_0049139664_section36936567"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

