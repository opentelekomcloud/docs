# Querying a Security Group for a Specified ECS<a name="EN-US_TOPIC_0065817702"></a>

## Function<a name="en-us_topic_0057972666_section55261147"></a>

This API is used to query the security group to which a specified ECS belongs.

## URI<a name="en-us_topic_0057972666_section27588283"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-security-groups

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-security-groups

[Table 1](#en-us_topic_0057972666_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972666_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row44937496"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row1664874"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972666_p637140"><a name="en-us_topic_0057972666_p637140"></a><a name="en-us_topic_0057972666_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972666_p51608407"><a name="en-us_topic_0057972666_p51608407"></a><a name="en-us_topic_0057972666_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row41565035"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972666_p11324657"><a name="en-us_topic_0057972666_p11324657"></a><a name="en-us_topic_0057972666_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972666_p44882061"><a name="en-us_topic_0057972666_p44882061"></a><a name="en-us_topic_0057972666_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972666_p11568292"><a name="en-us_topic_0057972666_p11568292"></a><a name="en-us_topic_0057972666_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972666_section20058459"></a>

None

## Response<a name="en-us_topic_0057972666_section46308405"></a>

[Table 2](#en-us_topic_0057972666_table35383970)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972666_table35383970"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row64935954"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p85762038122710"><a name="p85762038122710"></a><a name="p85762038122710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.48514851485149%" id="mcps1.2.5.1.4"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row55059565"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p30639779"><a name="en-us_topic_0057972666_p30639779"></a><a name="en-us_topic_0057972666_p30639779"></a>security_groups</p>
<p id="en-us_topic_0057972666_p7322556"><a name="en-us_topic_0057972666_p7322556"></a><a name="en-us_topic_0057972666_p7322556"></a></p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p55769386272"><a name="p55769386272"></a><a name="p55769386272"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p56256135"><a name="en-us_topic_0057972666_p56256135"></a><a name="en-us_topic_0057972666_p56256135"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.48514851485149%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p64862199"><a name="en-us_topic_0057972666_p64862199"></a><a name="en-us_topic_0057972666_p64862199"></a>Specifies security groups. For details, see <a href="#en-us_topic_0057972666_table19346796">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **security\_group**  objects

<a name="en-us_topic_0057972666_table19346796"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row58796306"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.1"><p id="p827545914121"><a name="p827545914121"></a><a name="p827545914121"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p11432184172710"><a name="p11432184172710"></a><a name="p11432184172710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p82751759181214"><a name="p82751759181214"></a><a name="p82751759181214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="p127545951215"><a name="p127545951215"></a><a name="p127545951215"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row57297510"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p10586695"><a name="en-us_topic_0057972666_p10586695"></a><a name="en-us_topic_0057972666_p10586695"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1243284132717"><a name="p1243284132717"></a><a name="p1243284132717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p843319816231"><a name="en-us_topic_0057972666_p843319816231"></a><a name="en-us_topic_0057972666_p843319816231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p65280430"><a name="en-us_topic_0057972666_p65280430"></a><a name="en-us_topic_0057972666_p65280430"></a>Specifies information about a security group. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row50652963"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p9249362"><a name="en-us_topic_0057972666_p9249362"></a><a name="en-us_topic_0057972666_p9249362"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1143318416271"><a name="p1143318416271"></a><a name="p1143318416271"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p4089483316231"><a name="en-us_topic_0057972666_p4089483316231"></a><a name="en-us_topic_0057972666_p4089483316231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p34571641"><a name="en-us_topic_0057972666_p34571641"></a><a name="en-us_topic_0057972666_p34571641"></a>Specifies the security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row42709316"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p36902586"><a name="en-us_topic_0057972666_p36902586"></a><a name="en-us_topic_0057972666_p36902586"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p174331541152718"><a name="p174331541152718"></a><a name="p174331541152718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p1599788116231"><a name="en-us_topic_0057972666_p1599788116231"></a><a name="en-us_topic_0057972666_p1599788116231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p55752527"><a name="en-us_topic_0057972666_p55752527"></a><a name="en-us_topic_0057972666_p55752527"></a>Specifies the security group name. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row32010697"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p42729680"><a name="en-us_topic_0057972666_p42729680"></a><a name="en-us_topic_0057972666_p42729680"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p104333410271"><a name="p104333410271"></a><a name="p104333410271"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p5262223416231"><a name="en-us_topic_0057972666_p5262223416231"></a><a name="en-us_topic_0057972666_p5262223416231"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p6918001"><a name="en-us_topic_0057972666_p6918001"></a><a name="en-us_topic_0057972666_p6918001"></a>Specifies security group rules. For details, see <a href="#en-us_topic_0057972666_table44319244">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row62262011"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p10058158"><a name="en-us_topic_0057972666_p10058158"></a><a name="en-us_topic_0057972666_p10058158"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1443354112276"><a name="p1443354112276"></a><a name="p1443354112276"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p4244727716231"><a name="en-us_topic_0057972666_p4244727716231"></a><a name="en-us_topic_0057972666_p4244727716231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p29544808"><a name="en-us_topic_0057972666_p29544808"></a><a name="en-us_topic_0057972666_p29544808"></a>Specifies the tenant or project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **security\_group\_rule**  objects

<a name="en-us_topic_0057972666_table44319244"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row251973"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.1"><p id="p0721526137"><a name="p0721526137"></a><a name="p0721526137"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p5738162171319"><a name="p5738162171319"></a><a name="p5738162171319"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p157217213133"><a name="p157217213133"></a><a name="p157217213133"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.495049504950494%" id="mcps1.2.5.1.4"><p id="p9738112141316"><a name="p9738112141316"></a><a name="p9738112141316"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row7290082"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p13853807162318"><a name="en-us_topic_0057972666_p13853807162318"></a><a name="en-us_topic_0057972666_p13853807162318"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p29429676162318"><a name="en-us_topic_0057972666_p29429676162318"></a><a name="en-us_topic_0057972666_p29429676162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p48416589162318"><a name="en-us_topic_0057972666_p48416589162318"></a><a name="en-us_topic_0057972666_p48416589162318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p34993588162318"><a name="en-us_topic_0057972666_p34993588162318"></a><a name="en-us_topic_0057972666_p34993588162318"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row34897438"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p8957549162318"><a name="en-us_topic_0057972666_p8957549162318"></a><a name="en-us_topic_0057972666_p8957549162318"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p50228537162318"><a name="en-us_topic_0057972666_p50228537162318"></a><a name="en-us_topic_0057972666_p50228537162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p54472897162318"><a name="en-us_topic_0057972666_p54472897162318"></a><a name="en-us_topic_0057972666_p54472897162318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p41979710162318"><a name="en-us_topic_0057972666_p41979710162318"></a><a name="en-us_topic_0057972666_p41979710162318"></a>Specifies the protocol type or the IP protocol number. The value can be <strong id="en-us_topic_0057972666_b84235270618469"><a name="en-us_topic_0057972666_b84235270618469"></a><a name="en-us_topic_0057972666_b84235270618469"></a>icmp</strong>, <strong id="en-us_topic_0057972666_b84235270619548"><a name="en-us_topic_0057972666_b84235270619548"></a><a name="en-us_topic_0057972666_b84235270619548"></a>tcp</strong>, <strong id="en-us_topic_0057972666_b842352706184613"><a name="en-us_topic_0057972666_b842352706184613"></a><a name="en-us_topic_0057972666_b842352706184613"></a>udp</strong>, or the IP protocol number.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row7551780"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p1566835162318"><a name="en-us_topic_0057972666_p1566835162318"></a><a name="en-us_topic_0057972666_p1566835162318"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p12349793162318"><a name="en-us_topic_0057972666_p12349793162318"></a><a name="en-us_topic_0057972666_p12349793162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p59804790162318"><a name="en-us_topic_0057972666_p59804790162318"></a><a name="en-us_topic_0057972666_p59804790162318"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p6565245172437"><a name="en-us_topic_0057972666_p6565245172437"></a><a name="en-us_topic_0057972666_p6565245172437"></a>Specifies the start port number. The value ranges from 1 to 65,535 and cannot be greater than <strong id="en-us_topic_0057972666_b84235270692028"><a name="en-us_topic_0057972666_b84235270692028"></a><a name="en-us_topic_0057972666_b84235270692028"></a>to_port</strong>.</p>
<p id="en-us_topic_0057972666_p60809181162318"><a name="en-us_topic_0057972666_p60809181162318"></a><a name="en-us_topic_0057972666_p60809181162318"></a>When <strong id="en-us_topic_0057972666_b842352706184658"><a name="en-us_topic_0057972666_b842352706184658"></a><a name="en-us_topic_0057972666_b842352706184658"></a>ip_protocol</strong> is <strong id="en-us_topic_0057972666_b84235270618473"><a name="en-us_topic_0057972666_b84235270618473"></a><a name="en-us_topic_0057972666_b84235270618473"></a>icmp</strong>, this parameter specifies a port type with a length from 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row63246244"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p38043040162318"><a name="en-us_topic_0057972666_p38043040162318"></a><a name="en-us_topic_0057972666_p38043040162318"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p22525157162318"><a name="en-us_topic_0057972666_p22525157162318"></a><a name="en-us_topic_0057972666_p22525157162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p61587420162318"><a name="en-us_topic_0057972666_p61587420162318"></a><a name="en-us_topic_0057972666_p61587420162318"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p4318355217257"><a name="en-us_topic_0057972666_p4318355217257"></a><a name="en-us_topic_0057972666_p4318355217257"></a>Specifies the stop port number. The value ranges from 1 to 65,535 and cannot be less than <strong id="b516286221"><a name="b516286221"></a><a name="b516286221"></a>from_port</strong>.</p>
<p id="en-us_topic_0057972666_p12598434162318"><a name="en-us_topic_0057972666_p12598434162318"></a><a name="en-us_topic_0057972666_p12598434162318"></a>When <strong id="en-us_topic_0057972666_b842352706162939"><a name="en-us_topic_0057972666_b842352706162939"></a><a name="en-us_topic_0057972666_b842352706162939"></a>ip_protocol</strong> is <strong id="en-us_topic_0057972666_b842352706162947"><a name="en-us_topic_0057972666_b842352706162947"></a><a name="en-us_topic_0057972666_b842352706162947"></a>icmp</strong>, it specifies the code. The value ranges from 0 to 255. If both <strong id="en-us_topic_0057972666_b842352706163018"><a name="en-us_topic_0057972666_b842352706163018"></a><a name="en-us_topic_0057972666_b842352706163018"></a>from_port</strong> and <strong id="en-us_topic_0057972666_b842352706163116"><a name="en-us_topic_0057972666_b842352706163116"></a><a name="en-us_topic_0057972666_b842352706163116"></a>to_port</strong> are <strong id="en-us_topic_0057972666_b842352706163025"><a name="en-us_topic_0057972666_b842352706163025"></a><a name="en-us_topic_0057972666_b842352706163025"></a>-1</strong>, any ICMP packet can be transmitted.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row26059286"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p57453407162318"><a name="en-us_topic_0057972666_p57453407162318"></a><a name="en-us_topic_0057972666_p57453407162318"></a>ip_range</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p1316814162318"><a name="en-us_topic_0057972666_p1316814162318"></a><a name="en-us_topic_0057972666_p1316814162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p23214382162318"><a name="en-us_topic_0057972666_p23214382162318"></a><a name="en-us_topic_0057972666_p23214382162318"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p34680534172630"><a name="en-us_topic_0057972666_p34680534172630"></a><a name="en-us_topic_0057972666_p34680534172630"></a>Specifies the peer IP segment in CIDR format. For details, see <a href="#en-us_topic_0057972666_table4101480163218">Table 5</a>.</p>
<p id="en-us_topic_0057972666_p39553127162318"><a name="en-us_topic_0057972666_p39553127162318"></a><a name="en-us_topic_0057972666_p39553127162318"></a>The value of <strong id="en-us_topic_0057972666_b84235270618494"><a name="en-us_topic_0057972666_b84235270618494"></a><a name="en-us_topic_0057972666_b84235270618494"></a>ip_range</strong> or <strong id="en-us_topic_0057972666_b84235270618498"><a name="en-us_topic_0057972666_b84235270618498"></a><a name="en-us_topic_0057972666_b84235270618498"></a>group</strong> must be empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row25228285"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p44527008162318"><a name="en-us_topic_0057972666_p44527008162318"></a><a name="en-us_topic_0057972666_p44527008162318"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p16815533162318"><a name="en-us_topic_0057972666_p16815533162318"></a><a name="en-us_topic_0057972666_p16815533162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p49917868162318"><a name="en-us_topic_0057972666_p49917868162318"></a><a name="en-us_topic_0057972666_p49917868162318"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p58652843172711"><a name="en-us_topic_0057972666_p58652843172711"></a><a name="en-us_topic_0057972666_p58652843172711"></a>Specifies the name of the peer security group and the ID of the tenant in the peer security group. For details, see <a href="#en-us_topic_0057972666_table9527961163416">Table 6</a>.</p>
<p id="en-us_topic_0057972666_p19880971162318"><a name="en-us_topic_0057972666_p19880971162318"></a><a name="en-us_topic_0057972666_p19880971162318"></a>The value of <strong id="b2020954818"><a name="b2020954818"></a><a name="b2020954818"></a>ip_range</strong> or <strong id="b522455556"><a name="b522455556"></a><a name="b522455556"></a>group</strong> must be empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row6587426"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p64822556162318"><a name="en-us_topic_0057972666_p64822556162318"></a><a name="en-us_topic_0057972666_p64822556162318"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972666_p31919068162318"><a name="en-us_topic_0057972666_p31919068162318"></a><a name="en-us_topic_0057972666_p31919068162318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p16135647162318"><a name="en-us_topic_0057972666_p16135647162318"></a><a name="en-us_topic_0057972666_p16135647162318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p35307705162318"><a name="en-us_topic_0057972666_p35307705162318"></a><a name="en-us_topic_0057972666_p35307705162318"></a>Specifies the security group rule ID in UUID format.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **ip\_range**  objects

<a name="en-us_topic_0057972666_table4101480163218"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row55642344163218"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.1"><p id="p87155671318"><a name="p87155671318"></a><a name="p87155671318"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p13333193072819"><a name="p13333193072819"></a><a name="p13333193072819"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p147151661134"><a name="p147151661134"></a><a name="p147151661134"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.495049504950494%" id="mcps1.2.5.1.4"><p id="p0715569135"><a name="p0715569135"></a><a name="p0715569135"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row5649056163218"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p54920430163218"><a name="en-us_topic_0057972666_p54920430163218"></a><a name="en-us_topic_0057972666_p54920430163218"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p1133333018288"><a name="p1133333018288"></a><a name="p1133333018288"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p19369856163218"><a name="en-us_topic_0057972666_p19369856163218"></a><a name="en-us_topic_0057972666_p19369856163218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p48550802163218"><a name="en-us_topic_0057972666_p48550802163218"></a><a name="en-us_topic_0057972666_p48550802163218"></a>Specifies the peer IP segment in CIDR format.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **group**  objects

<a name="en-us_topic_0057972666_table9527961163416"></a>
<table><thead align="left"><tr id="en-us_topic_0057972666_row57542164163416"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p478979121310"><a name="p478979121310"></a><a name="p478979121310"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p528573382814"><a name="p528573382814"></a><a name="p528573382814"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p1178918914133"><a name="p1178918914133"></a><a name="p1178918914133"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p878949121318"><a name="p878949121318"></a><a name="p878949121318"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972666_row46600064163416"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p16508853163416"><a name="en-us_topic_0057972666_p16508853163416"></a><a name="en-us_topic_0057972666_p16508853163416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p14286233132819"><a name="p14286233132819"></a><a name="p14286233132819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p62148702163416"><a name="en-us_topic_0057972666_p62148702163416"></a><a name="en-us_topic_0057972666_p62148702163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p4179246163416"><a name="en-us_topic_0057972666_p4179246163416"></a><a name="en-us_topic_0057972666_p4179246163416"></a>Specifies the ID of the tenant of the peer security group.</p>
</td>
</tr>
<tr id="en-us_topic_0057972666_row37613216163416"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972666_p26771660163416"><a name="en-us_topic_0057972666_p26771660163416"></a><a name="en-us_topic_0057972666_p26771660163416"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p7286113310285"><a name="p7286113310285"></a><a name="p7286113310285"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972666_p21020848163416"><a name="en-us_topic_0057972666_p21020848163416"></a><a name="en-us_topic_0057972666_p21020848163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972666_p9073859163416"><a name="en-us_topic_0057972666_p9073859163416"></a><a name="en-us_topic_0057972666_p9073859163416"></a>Specifies the name of the peer security group.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972666_section14122463"></a>

```
GET https://{endpoint}/v2/e73621affb8f44e1bc01898747ca09d4/servers/65fae4c2-3a09-46c6-af12-3b04f1fdba1e/os-security-groups
GET https://{endpoint}/v2.1/e73621affb8f44e1bc01898747ca09d4/servers/65fae4c2-3a09-46c6-af12-3b04f1fdba1e/os-security-groups
```

## Example Response<a name="section1507145117257"></a>

```
{
    "security_groups": [
        {
            "rules": [
                {
                    "from_port": null,
                    "group": {
                        "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
                        "name": "default"
                    },
                    "ip_protocol": null,
                    "to_port": null,
                    "parent_group_id": "bc4ac1d1-dc77-4b7d-a97d-af86eb0dc450",
                    "ip_range": {},
                    "id": "bb3cc988-e06a-49f6-b668-600e8bf193ee"
                },
                {
                    "from_port": null,
                    "group": {
                        "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
                        "name": "default"
                    },
                    "ip_protocol": null,
                    "to_port": null,
                    "parent_group_id": "bc4ac1d1-dc77-4b7d-a97d-af86eb0dc450",
                    "ip_range": {},
                    "id": "f9371051-d7e1-4be4-8748-77b1e0913730"
                }
            ],
            "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
            "description": "default",
            "id": "bc4ac1d1-dc77-4b7d-a97d-af86eb0dc450",
            "name": "default"
        },
        {
            "rules": [
                {
                    "from_port": 200,
                    "group": {},
                    "ip_protocol": "tcp",
                    "to_port": 400,
                    "parent_group_id": "b3e4b615-a40f-4e1c-92af-2e0d382141d5",
                    "ip_range": {
                        "cidr": "0.0.0.0/0"
                    },
                    "id": "3330120d-bbd1-4a73-bda9-0196a84d5670"
                },
                {
                    "from_port": 201,
                    "group": {},
                    "ip_protocol": "tcp",
                    "to_port": 400,
                    "parent_group_id": "b3e4b615-a40f-4e1c-92af-2e0d382141d5",
                    "ip_range": {
                        "cidr": "0.0.0.0/0"
                    },
                    "id": "b550c9a6-970a-462d-984e-265e88020818"
                }
            ],
            "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
            "description": "desc-sg",
            "id": "b3e4b615-a40f-4e1c-92af-2e0d382141d5",
            "name": "test-sg"
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0057972666_section1642564"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

