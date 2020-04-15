# Querying Details About a Security Group \(Discarded\)<a name="EN-US_TOPIC_0090187681"></a>

## Function<a name="en-us_topic_0057972663_section33142240"></a>

This API is used to query details about a security group.

This API can only query the inbound security group rules. To query the outbound security group rules, see "Querying a Security Group" in "Security Group \(Native OpenStack API\)" in the  _Virtual Private Cloud API Reference_.

## Constraints<a name="en-us_topic_0057972663_section166885"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Querying a Security Group" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972663_section29844704"></a>

GET /v2/\{project\_id\}/os-security-groups/\{security\_group\_id\}

GET /v2.1/\{project\_id\}/os-security-groups/\{security\_group\_id\}

[Table 1](#en-us_topic_0057972663_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972663_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row11302482"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row49888896"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p14468758"><a name="en-us_topic_0057972663_p14468758"></a><a name="en-us_topic_0057972663_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p31118786"><a name="en-us_topic_0057972663_p31118786"></a><a name="en-us_topic_0057972663_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row3928161611210"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p4928516101217"><a name="en-us_topic_0057972663_p4928516101217"></a><a name="en-us_topic_0057972663_p4928516101217"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p18928816181213"><a name="en-us_topic_0057972663_p18928816181213"></a><a name="en-us_topic_0057972663_p18928816181213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p292821613128"><a name="en-us_topic_0057972663_p292821613128"></a><a name="en-us_topic_0057972663_p292821613128"></a>Specifies the security group ID, which is specified in the URI.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972663_section1501966"></a>

None

## Response<a name="en-us_topic_0057972663_section13517702"></a>

[Table 2](#en-us_topic_0057972663_table50358210)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972663_table50358210"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row59455556"><th class="cellrowborder" valign="top" width="29.75%" id="mcps1.2.4.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.46%" id="mcps1.2.4.1.2"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.79%" id="mcps1.2.4.1.3"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row49313939"><td class="cellrowborder" valign="top" width="29.75%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p35006119"><a name="en-us_topic_0057972663_p35006119"></a><a name="en-us_topic_0057972663_p35006119"></a>security_group</p>
<p id="en-us_topic_0057972663_p46619622"><a name="en-us_topic_0057972663_p46619622"></a><a name="en-us_topic_0057972663_p46619622"></a></p>
</td>
<td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p18093058"><a name="en-us_topic_0057972663_p18093058"></a><a name="en-us_topic_0057972663_p18093058"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.79%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p60087944"><a name="en-us_topic_0057972663_p60087944"></a><a name="en-us_topic_0057972663_p60087944"></a>Specifies the security group. For details, see <a href="#en-us_topic_0057972663_table35285314">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **security\_group**  objects

<a name="en-us_topic_0057972663_table35285314"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row39516413"><th class="cellrowborder" valign="top" width="28.54%" id="mcps1.2.4.1.1"><p id="p1383765811115"><a name="p1383765811115"></a><a name="p1383765811115"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.54%" id="mcps1.2.4.1.2"><p id="p883715815113"><a name="p883715815113"></a><a name="p883715815113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.92%" id="mcps1.2.4.1.3"><p id="p98533582112"><a name="p98533582112"></a><a name="p98533582112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row54881489"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p16215635"><a name="en-us_topic_0057972663_p16215635"></a><a name="en-us_topic_0057972663_p16215635"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p548500816121"><a name="en-us_topic_0057972663_p548500816121"></a><a name="en-us_topic_0057972663_p548500816121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p3143429"><a name="en-us_topic_0057972663_p3143429"></a><a name="en-us_topic_0057972663_p3143429"></a>Specifies information about a security group. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row28290863"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p9858548"><a name="en-us_topic_0057972663_p9858548"></a><a name="en-us_topic_0057972663_p9858548"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p347153016121"><a name="en-us_topic_0057972663_p347153016121"></a><a name="en-us_topic_0057972663_p347153016121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p47953287"><a name="en-us_topic_0057972663_p47953287"></a><a name="en-us_topic_0057972663_p47953287"></a>Specifies the security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row28926407"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p61337593"><a name="en-us_topic_0057972663_p61337593"></a><a name="en-us_topic_0057972663_p61337593"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p4539265916121"><a name="en-us_topic_0057972663_p4539265916121"></a><a name="en-us_topic_0057972663_p4539265916121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p53855148"><a name="en-us_topic_0057972663_p53855148"></a><a name="en-us_topic_0057972663_p53855148"></a>Specifies the security group name. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row14934289"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p1717931"><a name="en-us_topic_0057972663_p1717931"></a><a name="en-us_topic_0057972663_p1717931"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p125837516121"><a name="en-us_topic_0057972663_p125837516121"></a><a name="en-us_topic_0057972663_p125837516121"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p30423852"><a name="en-us_topic_0057972663_p30423852"></a><a name="en-us_topic_0057972663_p30423852"></a>Specifies security group rules. For details, see <a href="#en-us_topic_0057972663_table19372405">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row5379216"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p33063388"><a name="en-us_topic_0057972663_p33063388"></a><a name="en-us_topic_0057972663_p33063388"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p3987464816121"><a name="en-us_topic_0057972663_p3987464816121"></a><a name="en-us_topic_0057972663_p3987464816121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p59062984"><a name="en-us_topic_0057972663_p59062984"></a><a name="en-us_topic_0057972663_p59062984"></a>Specifies the tenant or project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **security\_group\_rule**  objects

<a name="en-us_topic_0057972663_table19372405"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row4839561"><th class="cellrowborder" valign="top" width="28.54%" id="mcps1.2.4.1.1"><p id="p175981212129"><a name="p175981212129"></a><a name="p175981212129"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.54%" id="mcps1.2.4.1.2"><p id="p1759810131216"><a name="p1759810131216"></a><a name="p1759810131216"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.92%" id="mcps1.2.4.1.3"><p id="p2059812110124"><a name="p2059812110124"></a><a name="p2059812110124"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row4945408"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p56578005161223"><a name="en-us_topic_0057972663_p56578005161223"></a><a name="en-us_topic_0057972663_p56578005161223"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p18781264161223"><a name="en-us_topic_0057972663_p18781264161223"></a><a name="en-us_topic_0057972663_p18781264161223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p9733511161223"><a name="en-us_topic_0057972663_p9733511161223"></a><a name="en-us_topic_0057972663_p9733511161223"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row63243911"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p26945308161223"><a name="en-us_topic_0057972663_p26945308161223"></a><a name="en-us_topic_0057972663_p26945308161223"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p9056775161223"><a name="en-us_topic_0057972663_p9056775161223"></a><a name="en-us_topic_0057972663_p9056775161223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p55279498161223"><a name="en-us_topic_0057972663_p55279498161223"></a><a name="en-us_topic_0057972663_p55279498161223"></a>Specifies the protocol type or the IP protocol number. The value can be <strong id="en-us_topic_0057972663_b84235270618469"><a name="en-us_topic_0057972663_b84235270618469"></a><a name="en-us_topic_0057972663_b84235270618469"></a>icmp</strong>, <strong id="en-us_topic_0057972663_b84235270619548"><a name="en-us_topic_0057972663_b84235270619548"></a><a name="en-us_topic_0057972663_b84235270619548"></a>tcp</strong>, <strong id="en-us_topic_0057972663_b842352706184613"><a name="en-us_topic_0057972663_b842352706184613"></a><a name="en-us_topic_0057972663_b842352706184613"></a>udp</strong>, or the IP protocol number.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row56252285"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p30626161161223"><a name="en-us_topic_0057972663_p30626161161223"></a><a name="en-us_topic_0057972663_p30626161161223"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p4441238161223"><a name="en-us_topic_0057972663_p4441238161223"></a><a name="en-us_topic_0057972663_p4441238161223"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p6386144517180"><a name="en-us_topic_0057972663_p6386144517180"></a><a name="en-us_topic_0057972663_p6386144517180"></a>Specifies the start port number. The value ranges from <strong id="en-us_topic_0057972663_b842352706202922"><a name="en-us_topic_0057972663_b842352706202922"></a><a name="en-us_topic_0057972663_b842352706202922"></a>1</strong> to <strong id="en-us_topic_0057972663_b842352706202927"><a name="en-us_topic_0057972663_b842352706202927"></a><a name="en-us_topic_0057972663_b842352706202927"></a>65,535</strong> and cannot be greater than <strong id="en-us_topic_0057972663_b84235270692028"><a name="en-us_topic_0057972663_b84235270692028"></a><a name="en-us_topic_0057972663_b84235270692028"></a>to_port</strong>.</p>
<p id="en-us_topic_0057972663_p30133528161223"><a name="en-us_topic_0057972663_p30133528161223"></a><a name="en-us_topic_0057972663_p30133528161223"></a>When <strong id="en-us_topic_0057972663_b842352706184658"><a name="en-us_topic_0057972663_b842352706184658"></a><a name="en-us_topic_0057972663_b842352706184658"></a>ip_protocol</strong> is <strong id="en-us_topic_0057972663_b84235270618473"><a name="en-us_topic_0057972663_b84235270618473"></a><a name="en-us_topic_0057972663_b84235270618473"></a>icmp</strong>, this parameter indicates the ICMP type field with a length from 0 to 255 characters.</p>
<div class="note" id="en-us_topic_0057973221_note136113314412"><a name="en-us_topic_0057973221_note136113314412"></a><a name="en-us_topic_0057973221_note136113314412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057973221_p203633310418"><a name="en-us_topic_0057973221_p203633310418"></a><a name="en-us_topic_0057973221_p203633310418"></a>The ICMP message type is determined by the type field and code field in the packet. For details, see <strong id="en-us_topic_0057973221_b842352706145053"><a name="en-us_topic_0057973221_b842352706145053"></a><a name="en-us_topic_0057973221_b842352706145053"></a>Appendix</strong> &gt; <strong id="en-us_topic_0057973221_b842352706145058"><a name="en-us_topic_0057973221_b842352706145058"></a><a name="en-us_topic_0057973221_b842352706145058"></a>ICMP-Port Range Relationship Table</strong> in <em id="en-us_topic_0057973221_i84235269714516"><a name="en-us_topic_0057973221_i84235269714516"></a><a name="en-us_topic_0057973221_i84235269714516"></a>Virtual Private Cloud API Reference</em>. <strong id="en-us_topic_0057973221_b441067081144424"><a name="en-us_topic_0057973221_b441067081144424"></a><a name="en-us_topic_0057973221_b441067081144424"></a>port_range_min</strong> indicates the ICMP type, and <strong id="en-us_topic_0057973221_b55704280614455"><a name="en-us_topic_0057973221_b55704280614455"></a><a name="en-us_topic_0057973221_b55704280614455"></a>port_range_max</strong> indicates the ICMP code.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972663_row63695501"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p41230774161223"><a name="en-us_topic_0057972663_p41230774161223"></a><a name="en-us_topic_0057972663_p41230774161223"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p37983567161223"><a name="en-us_topic_0057972663_p37983567161223"></a><a name="en-us_topic_0057972663_p37983567161223"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p18967244171848"><a name="en-us_topic_0057972663_p18967244171848"></a><a name="en-us_topic_0057972663_p18967244171848"></a>Specifies the stop port number. The value ranges from 1 to 65,535 and cannot be less than <strong id="b489006133"><a name="b489006133"></a><a name="b489006133"></a>from_port</strong>.</p>
<p id="en-us_topic_0057972663_p1492837161223"><a name="en-us_topic_0057972663_p1492837161223"></a><a name="en-us_topic_0057972663_p1492837161223"></a>When <strong id="b516500155"><a name="b516500155"></a><a name="b516500155"></a>ip_protocol</strong> is <strong id="b959752796"><a name="b959752796"></a><a name="b959752796"></a>icmp</strong>, this parameter indicates the ICMP code field with a length from 0 to 255 characters.</p>
<div class="note" id="note78601422175013"><a name="note78601422175013"></a><a name="note78601422175013"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11860122195012"><a name="p11860122195012"></a><a name="p11860122195012"></a>The ICMP message type is determined by the type field and code field in the packet. For details, see <strong id="b558714517"><a name="b558714517"></a><a name="b558714517"></a>Appendix</strong> &gt; <strong id="b944285491"><a name="b944285491"></a><a name="b944285491"></a>ICMP-Port Range Relationship Table</strong> in <em id="i1316721882"><a name="i1316721882"></a><a name="i1316721882"></a>Virtual Private Cloud API Reference</em>. <strong id="b579001521"><a name="b579001521"></a><a name="b579001521"></a>port_range_min</strong> indicates the ICMP type, and <strong id="b1410627653"><a name="b1410627653"></a><a name="b1410627653"></a>port_range_max</strong> indicates the ICMP code.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972663_row43938279"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p6965923161223"><a name="en-us_topic_0057972663_p6965923161223"></a><a name="en-us_topic_0057972663_p6965923161223"></a>ip_range</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p12065754161223"><a name="en-us_topic_0057972663_p12065754161223"></a><a name="en-us_topic_0057972663_p12065754161223"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p6066882171936"><a name="en-us_topic_0057972663_p6066882171936"></a><a name="en-us_topic_0057972663_p6066882171936"></a>Specifies the peer IP segment in CIDR format. For details, see <a href="#en-us_topic_0057972663_table4101480163218">Table 5</a>.</p>
<p id="en-us_topic_0057972663_p55778039161223"><a name="en-us_topic_0057972663_p55778039161223"></a><a name="en-us_topic_0057972663_p55778039161223"></a>Specify either <strong id="en-us_topic_0057972663_b1800397364144646"><a name="en-us_topic_0057972663_b1800397364144646"></a><a name="en-us_topic_0057972663_b1800397364144646"></a>ip_range</strong> or <strong id="en-us_topic_0057972663_b1399083018144646"><a name="en-us_topic_0057972663_b1399083018144646"></a><a name="en-us_topic_0057972663_b1399083018144646"></a>group</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row16612996"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p66972938161223"><a name="en-us_topic_0057972663_p66972938161223"></a><a name="en-us_topic_0057972663_p66972938161223"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p4606072161223"><a name="en-us_topic_0057972663_p4606072161223"></a><a name="en-us_topic_0057972663_p4606072161223"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p41556366172037"><a name="en-us_topic_0057972663_p41556366172037"></a><a name="en-us_topic_0057972663_p41556366172037"></a>Specifies the name of the peer security group and the ID of the tenant in the peer security group. For details, see <a href="#en-us_topic_0057972663_table9527961163416">Table 6</a>.</p>
<p id="en-us_topic_0057972663_p59656689161223"><a name="en-us_topic_0057972663_p59656689161223"></a><a name="en-us_topic_0057972663_p59656689161223"></a>Specify either <strong id="b1807648052"><a name="b1807648052"></a><a name="b1807648052"></a>ip_range</strong> or <strong id="b535745485"><a name="b535745485"></a><a name="b535745485"></a>group</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row47280229"><td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p40774675161223"><a name="en-us_topic_0057972663_p40774675161223"></a><a name="en-us_topic_0057972663_p40774675161223"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.54%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p61404227161223"><a name="en-us_topic_0057972663_p61404227161223"></a><a name="en-us_topic_0057972663_p61404227161223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p13931595161223"><a name="en-us_topic_0057972663_p13931595161223"></a><a name="en-us_topic_0057972663_p13931595161223"></a>Specifies the security group rule ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **ip\_range**  objects

<a name="en-us_topic_0057972663_table4101480163218"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row55642344163218"><th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.1"><p id="p17550121241216"><a name="p17550121241216"></a><a name="p17550121241216"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.792979297929794%" id="mcps1.2.4.1.2"><p id="p7565312191212"><a name="p7565312191212"></a><a name="p7565312191212"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.184018401840184%" id="mcps1.2.4.1.3"><p id="p12565171216127"><a name="p12565171216127"></a><a name="p12565171216127"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row5649056163218"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p54920430163218"><a name="en-us_topic_0057972663_p54920430163218"></a><a name="en-us_topic_0057972663_p54920430163218"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p19369856163218"><a name="en-us_topic_0057972663_p19369856163218"></a><a name="en-us_topic_0057972663_p19369856163218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.184018401840184%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p48550802163218"><a name="en-us_topic_0057972663_p48550802163218"></a><a name="en-us_topic_0057972663_p48550802163218"></a>Specifies the peer IP segment in CIDR format.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **group**  objects

<a name="en-us_topic_0057972663_table9527961163416"></a>
<table><thead align="left"><tr id="en-us_topic_0057972663_row57542164163416"><th class="cellrowborder" valign="top" width="29.690000000000005%" id="mcps1.2.4.1.1"><p id="p792151481211"><a name="p792151481211"></a><a name="p792151481211"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.460000000000004%" id="mcps1.2.4.1.2"><p id="p199211514141217"><a name="p199211514141217"></a><a name="p199211514141217"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.85%" id="mcps1.2.4.1.3"><p id="p39211914131219"><a name="p39211914131219"></a><a name="p39211914131219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972663_row46600064163416"><td class="cellrowborder" valign="top" width="29.690000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p16508853163416"><a name="en-us_topic_0057972663_p16508853163416"></a><a name="en-us_topic_0057972663_p16508853163416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="29.460000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p62148702163416"><a name="en-us_topic_0057972663_p62148702163416"></a><a name="en-us_topic_0057972663_p62148702163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.85%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p4179246163416"><a name="en-us_topic_0057972663_p4179246163416"></a><a name="en-us_topic_0057972663_p4179246163416"></a>Specifies the ID of the tenant of the peer security group.</p>
</td>
</tr>
<tr id="en-us_topic_0057972663_row37613216163416"><td class="cellrowborder" valign="top" width="29.690000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972663_p26771660163416"><a name="en-us_topic_0057972663_p26771660163416"></a><a name="en-us_topic_0057972663_p26771660163416"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="29.460000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972663_p21020848163416"><a name="en-us_topic_0057972663_p21020848163416"></a><a name="en-us_topic_0057972663_p21020848163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.85%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972663_p9073859163416"><a name="en-us_topic_0057972663_p9073859163416"></a><a name="en-us_topic_0057972663_p9073859163416"></a>Specifies the name of the peer security group.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972663_section54550461"></a>

```
GET https://{endpoint}/v2/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/81f1d23b-b1e2-42cd-bdee-359b4a065a42
GET https://{endpoint}/v2.1/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/81f1d23b-b1e2-42cd-bdee-359b4a065a42
```

## Example Response<a name="section19105192262719"></a>

```
{
    "security_group": {
        "rules": [],
        "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
        "id": "81f1d23b-b1e2-42cd-bdee-359b4a065a42",
        "name": "test-sg",
        "description": "desc-sg"
    }
}
```

## Returned Values<a name="en-us_topic_0057972663_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

