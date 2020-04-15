# Querying Security Groups \(Discarded\)<a name="EN-US_TOPIC_0090187679"></a>

## Function<a name="en-us_topic_0057973221_section4176562"></a>

This API is used to query security groups.

## Constraints<a name="en-us_topic_0057973221_section2757266"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Querying Security Groups" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057973221_section37589065"></a>

GET /v2/\{project\_id\}/os-security-groups

GET /v2.1/\{project\_id\}/os-security-groups

[Table 1](#en-us_topic_0057973221_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973221_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row11302482"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row49888896"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p14468758"><a name="en-us_topic_0057973221_p14468758"></a><a name="en-us_topic_0057973221_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p31118786"><a name="en-us_topic_0057973221_p31118786"></a><a name="en-us_topic_0057973221_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Pagination query is not supported.  

## Request<a name="en-us_topic_0057973221_section24815400"></a>

N/A

## Response<a name="en-us_topic_0057973221_section22012011"></a>

[Table 2](#en-us_topic_0057973221_table66376806)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973221_table66376806"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row62274010"><th class="cellrowborder" valign="top" width="30.09%" id="mcps1.2.4.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.09%" id="mcps1.2.4.1.2"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.4.1.3"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row1734205"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p6252912"><a name="en-us_topic_0057973221_p6252912"></a><a name="en-us_topic_0057973221_p6252912"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p62079394"><a name="en-us_topic_0057973221_p62079394"></a><a name="en-us_topic_0057973221_p62079394"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p19210173"><a name="en-us_topic_0057973221_p19210173"></a><a name="en-us_topic_0057973221_p19210173"></a>Specifies security groups. For details, see <a href="#en-us_topic_0057973221_table12520187">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **security\_group**  objects

<a name="en-us_topic_0057973221_table12520187"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row15746475"><th class="cellrowborder" valign="top" width="30.09%" id="mcps1.2.4.1.1"><p id="p183229295112"><a name="p183229295112"></a><a name="p183229295112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.09%" id="mcps1.2.4.1.2"><p id="p632282961111"><a name="p632282961111"></a><a name="p632282961111"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.4.1.3"><p id="p032218298115"><a name="p032218298115"></a><a name="p032218298115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row48113441"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p4874628"><a name="en-us_topic_0057973221_p4874628"></a><a name="en-us_topic_0057973221_p4874628"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5258827116753"><a name="en-us_topic_0057973221_p5258827116753"></a><a name="en-us_topic_0057973221_p5258827116753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p40886591"><a name="en-us_topic_0057973221_p40886591"></a><a name="en-us_topic_0057973221_p40886591"></a>Specifies information about a security group. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row32435006"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p9989850"><a name="en-us_topic_0057973221_p9989850"></a><a name="en-us_topic_0057973221_p9989850"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p4707763316753"><a name="en-us_topic_0057973221_p4707763316753"></a><a name="en-us_topic_0057973221_p4707763316753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p34125466"><a name="en-us_topic_0057973221_p34125466"></a><a name="en-us_topic_0057973221_p34125466"></a>Specifies the security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row38693741"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p47185308"><a name="en-us_topic_0057973221_p47185308"></a><a name="en-us_topic_0057973221_p47185308"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5607075516753"><a name="en-us_topic_0057973221_p5607075516753"></a><a name="en-us_topic_0057973221_p5607075516753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p41135662"><a name="en-us_topic_0057973221_p41135662"></a><a name="en-us_topic_0057973221_p41135662"></a>Specifies the security group name. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row34676638"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p57344266"><a name="en-us_topic_0057973221_p57344266"></a><a name="en-us_topic_0057973221_p57344266"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p658933716753"><a name="en-us_topic_0057973221_p658933716753"></a><a name="en-us_topic_0057973221_p658933716753"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p19833643"><a name="en-us_topic_0057973221_p19833643"></a><a name="en-us_topic_0057973221_p19833643"></a>Specifies security group rules. For details, see <a href="#en-us_topic_0057973221_table34485122">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row44285066"><td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p30320557"><a name="en-us_topic_0057973221_p30320557"></a><a name="en-us_topic_0057973221_p30320557"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="30.09%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5130886116753"><a name="en-us_topic_0057973221_p5130886116753"></a><a name="en-us_topic_0057973221_p5130886116753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p11196300"><a name="en-us_topic_0057973221_p11196300"></a><a name="en-us_topic_0057973221_p11196300"></a>Specifies the tenant or project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **security\_group\_rule**  objects

<a name="en-us_topic_0057973221_table34485122"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row32580689"><th class="cellrowborder" valign="top" width="28.410000000000004%" id="mcps1.2.4.1.1"><p id="p63482327113"><a name="p63482327113"></a><a name="p63482327113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.410000000000004%" id="mcps1.2.4.1.2"><p id="p123484326118"><a name="p123484326118"></a><a name="p123484326118"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.18%" id="mcps1.2.4.1.3"><p id="p6348032131118"><a name="p6348032131118"></a><a name="p6348032131118"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row25689027"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p4000465416720"><a name="en-us_topic_0057973221_p4000465416720"></a><a name="en-us_topic_0057973221_p4000465416720"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p6039325916720"><a name="en-us_topic_0057973221_p6039325916720"></a><a name="en-us_topic_0057973221_p6039325916720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p3085498416720"><a name="en-us_topic_0057973221_p3085498416720"></a><a name="en-us_topic_0057973221_p3085498416720"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row1068468"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p5545514116720"><a name="en-us_topic_0057973221_p5545514116720"></a><a name="en-us_topic_0057973221_p5545514116720"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p717072016720"><a name="en-us_topic_0057973221_p717072016720"></a><a name="en-us_topic_0057973221_p717072016720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p5391322116720"><a name="en-us_topic_0057973221_p5391322116720"></a><a name="en-us_topic_0057973221_p5391322116720"></a>Specifies the protocol type or the IP protocol number. The value can be <strong id="en-us_topic_0057973221_b84235270618469"><a name="en-us_topic_0057973221_b84235270618469"></a><a name="en-us_topic_0057973221_b84235270618469"></a>icmp</strong>, <strong id="en-us_topic_0057973221_b84235270619524"><a name="en-us_topic_0057973221_b84235270619524"></a><a name="en-us_topic_0057973221_b84235270619524"></a>tcp</strong>, <strong id="en-us_topic_0057973221_b842352706184613"><a name="en-us_topic_0057973221_b842352706184613"></a><a name="en-us_topic_0057973221_b842352706184613"></a>udp</strong>, or the IP protocol number.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row34266555"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p4437223016720"><a name="en-us_topic_0057973221_p4437223016720"></a><a name="en-us_topic_0057973221_p4437223016720"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5610229616720"><a name="en-us_topic_0057973221_p5610229616720"></a><a name="en-us_topic_0057973221_p5610229616720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p2095114117818"><a name="en-us_topic_0057973221_p2095114117818"></a><a name="en-us_topic_0057973221_p2095114117818"></a>Specifies the start port number. The value ranges from 1 to 65,535 and cannot be greater than <strong id="en-us_topic_0057973221_b84235270692028"><a name="en-us_topic_0057973221_b84235270692028"></a><a name="en-us_topic_0057973221_b84235270692028"></a>to_port</strong>.</p>
<p id="en-us_topic_0057973221_p660857541795"><a name="en-us_topic_0057973221_p660857541795"></a><a name="en-us_topic_0057973221_p660857541795"></a>When <strong id="en-us_topic_0057973221_b842352706184658"><a name="en-us_topic_0057973221_b842352706184658"></a><a name="en-us_topic_0057973221_b842352706184658"></a>ip_protocol</strong> is <strong id="en-us_topic_0057973221_b84235270618473"><a name="en-us_topic_0057973221_b84235270618473"></a><a name="en-us_topic_0057973221_b84235270618473"></a>icmp</strong>, this parameter indicates the ICMP type field with a length from 0 to 255 characters.</p>
<div class="note" id="en-us_topic_0057973221_note136113314412"><a name="en-us_topic_0057973221_note136113314412"></a><a name="en-us_topic_0057973221_note136113314412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057973221_p203633310418"><a name="en-us_topic_0057973221_p203633310418"></a><a name="en-us_topic_0057973221_p203633310418"></a>The ICMP message type is determined by the type field and code field in the packet. For details, see <strong id="en-us_topic_0057973221_b842352706145053"><a name="en-us_topic_0057973221_b842352706145053"></a><a name="en-us_topic_0057973221_b842352706145053"></a>Appendix</strong> &gt; <strong id="en-us_topic_0057973221_b842352706145058"><a name="en-us_topic_0057973221_b842352706145058"></a><a name="en-us_topic_0057973221_b842352706145058"></a>ICMP-Port Range Relationship Table</strong> in <em id="en-us_topic_0057973221_i84235269714516"><a name="en-us_topic_0057973221_i84235269714516"></a><a name="en-us_topic_0057973221_i84235269714516"></a>Virtual Private Cloud API Reference</em>. <strong id="en-us_topic_0057973221_b441067081144424"><a name="en-us_topic_0057973221_b441067081144424"></a><a name="en-us_topic_0057973221_b441067081144424"></a>port_range_min</strong> indicates the ICMP type field, and <strong id="en-us_topic_0057973221_b55704280614455"><a name="en-us_topic_0057973221_b55704280614455"></a><a name="en-us_topic_0057973221_b55704280614455"></a>port_range_max</strong> indicates the ICMP code field.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057973221_row12065659"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p951704916720"><a name="en-us_topic_0057973221_p951704916720"></a><a name="en-us_topic_0057973221_p951704916720"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5777809316720"><a name="en-us_topic_0057973221_p5777809316720"></a><a name="en-us_topic_0057973221_p5777809316720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p698716017100"><a name="en-us_topic_0057973221_p698716017100"></a><a name="en-us_topic_0057973221_p698716017100"></a>Specifies the stop port number. The value ranges from 1 to 65,535 and cannot be less than <strong id="b1689845510"><a name="b1689845510"></a><a name="b1689845510"></a>from_port</strong>.</p>
<p id="en-us_topic_0057973221_p230471653415"><a name="en-us_topic_0057973221_p230471653415"></a><a name="en-us_topic_0057973221_p230471653415"></a>When <strong id="b161930797"><a name="b161930797"></a><a name="b161930797"></a>ip_protocol</strong> is <strong id="b1554146441"><a name="b1554146441"></a><a name="b1554146441"></a>icmp</strong>, this parameter indicates the ICMP code field with a length from 0 to 255 characters.</p>
<div class="note" id="note8882154911495"><a name="note8882154911495"></a><a name="note8882154911495"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3882649134916"><a name="p3882649134916"></a><a name="p3882649134916"></a>The ICMP message type is determined by the type field and code field in the packet. For details, see <strong id="b1510237663"><a name="b1510237663"></a><a name="b1510237663"></a>Appendix</strong> &gt; <strong id="b1107929195"><a name="b1107929195"></a><a name="b1107929195"></a>ICMP-Port Range Relationship Table</strong> in <em id="i493562660"><a name="i493562660"></a><a name="i493562660"></a>Virtual Private Cloud API Reference</em>. <strong id="b1536730035"><a name="b1536730035"></a><a name="b1536730035"></a>port_range_min</strong> indicates the ICMP type, and <strong id="b2074139154"><a name="b2074139154"></a><a name="b2074139154"></a>port_range_max</strong> indicates the ICMP code.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057973221_row19467483"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p410745516720"><a name="en-us_topic_0057973221_p410745516720"></a><a name="en-us_topic_0057973221_p410745516720"></a>ip_range</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p5877646316720"><a name="en-us_topic_0057973221_p5877646316720"></a><a name="en-us_topic_0057973221_p5877646316720"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p6098836171215"><a name="en-us_topic_0057973221_p6098836171215"></a><a name="en-us_topic_0057973221_p6098836171215"></a>Specifies the peer IP segment in CIDR format. For details, see <a href="#en-us_topic_0057973221_table4101480163218">Table 5</a>.</p>
<p id="en-us_topic_0057973221_p3406419516720"><a name="en-us_topic_0057973221_p3406419516720"></a><a name="en-us_topic_0057973221_p3406419516720"></a>Specify either <strong id="en-us_topic_0057973221_b842352706153434"><a name="en-us_topic_0057973221_b842352706153434"></a><a name="en-us_topic_0057973221_b842352706153434"></a>ip_range</strong> or <strong id="en-us_topic_0057973221_b842352706153439"><a name="en-us_topic_0057973221_b842352706153439"></a><a name="en-us_topic_0057973221_b842352706153439"></a>group</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row8411726"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p1686385816720"><a name="en-us_topic_0057973221_p1686385816720"></a><a name="en-us_topic_0057973221_p1686385816720"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p1304659916720"><a name="en-us_topic_0057973221_p1304659916720"></a><a name="en-us_topic_0057973221_p1304659916720"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p35137339171315"><a name="en-us_topic_0057973221_p35137339171315"></a><a name="en-us_topic_0057973221_p35137339171315"></a>Specifies the name of the peer security group and the ID of the tenant in the peer security group. For details, see <a href="#en-us_topic_0057973221_table9527961163416">Table 6</a>.</p>
<p id="en-us_topic_0057973221_p4707259516720"><a name="en-us_topic_0057973221_p4707259516720"></a><a name="en-us_topic_0057973221_p4707259516720"></a>Specify either <strong id="en-us_topic_0057973221_b1800397364144646"><a name="en-us_topic_0057973221_b1800397364144646"></a><a name="en-us_topic_0057973221_b1800397364144646"></a>ip_range</strong> or <strong id="en-us_topic_0057973221_b1399083018144646"><a name="en-us_topic_0057973221_b1399083018144646"></a><a name="en-us_topic_0057973221_b1399083018144646"></a>group</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row3083532"><td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p65824216720"><a name="en-us_topic_0057973221_p65824216720"></a><a name="en-us_topic_0057973221_p65824216720"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.410000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p3323147916720"><a name="en-us_topic_0057973221_p3323147916720"></a><a name="en-us_topic_0057973221_p3323147916720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p4664414216720"><a name="en-us_topic_0057973221_p4664414216720"></a><a name="en-us_topic_0057973221_p4664414216720"></a>Specifies the security group rule ID in UUID format.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **ip\_range**  objects

<a name="en-us_topic_0057973221_table4101480163218"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row55642344163218"><th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.1"><p id="p163251137161116"><a name="p163251137161116"></a><a name="p163251137161116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.792979297929794%" id="mcps1.2.4.1.2"><p id="p33251637171113"><a name="p33251637171113"></a><a name="p33251637171113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.184018401840184%" id="mcps1.2.4.1.3"><p id="p163403376116"><a name="p163403376116"></a><a name="p163403376116"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row5649056163218"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p54920430163218"><a name="en-us_topic_0057973221_p54920430163218"></a><a name="en-us_topic_0057973221_p54920430163218"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="29.792979297929794%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p19369856163218"><a name="en-us_topic_0057973221_p19369856163218"></a><a name="en-us_topic_0057973221_p19369856163218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.184018401840184%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p48550802163218"><a name="en-us_topic_0057973221_p48550802163218"></a><a name="en-us_topic_0057973221_p48550802163218"></a>Specifies the peer IP segment in CIDR format.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **group**  objects

<a name="en-us_topic_0057973221_table9527961163416"></a>
<table><thead align="left"><tr id="en-us_topic_0057973221_row57542164163416"><th class="cellrowborder" valign="top" width="29.690000000000005%" id="mcps1.2.4.1.1"><p id="p2231840201112"><a name="p2231840201112"></a><a name="p2231840201112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.460000000000004%" id="mcps1.2.4.1.2"><p id="p183984018118"><a name="p183984018118"></a><a name="p183984018118"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.85%" id="mcps1.2.4.1.3"><p id="p03911409118"><a name="p03911409118"></a><a name="p03911409118"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973221_row46600064163416"><td class="cellrowborder" valign="top" width="29.690000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p16508853163416"><a name="en-us_topic_0057973221_p16508853163416"></a><a name="en-us_topic_0057973221_p16508853163416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="29.460000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p62148702163416"><a name="en-us_topic_0057973221_p62148702163416"></a><a name="en-us_topic_0057973221_p62148702163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.85%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p4179246163416"><a name="en-us_topic_0057973221_p4179246163416"></a><a name="en-us_topic_0057973221_p4179246163416"></a>Specifies the ID of the tenant of the peer security group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973221_row37613216163416"><td class="cellrowborder" valign="top" width="29.690000000000005%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973221_p26771660163416"><a name="en-us_topic_0057973221_p26771660163416"></a><a name="en-us_topic_0057973221_p26771660163416"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="29.460000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973221_p21020848163416"><a name="en-us_topic_0057973221_p21020848163416"></a><a name="en-us_topic_0057973221_p21020848163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.85%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973221_p9073859163416"><a name="en-us_topic_0057973221_p9073859163416"></a><a name="en-us_topic_0057973221_p9073859163416"></a>Specifies the name of the peer security group.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973221_section63890372"></a>

```
GET https://{endpoint}/v2/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups
GET https://{endpoint}/v2.1/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups
```

## Example Response<a name="section14391225182618"></a>

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

## Returned Values<a name="en-us_topic_0057973221_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

