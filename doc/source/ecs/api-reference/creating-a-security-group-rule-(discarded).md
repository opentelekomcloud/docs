# Creating a Security Group Rule \(Discarded\)<a name="EN-US_TOPIC_0065817703"></a>

## Function<a name="en-us_topic_0057972667_section60900816"></a>

This API is used to create a security group rule.

## Constraints<a name="en-us_topic_0057972667_section46967960"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Creating a Security Group Rule" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972667_section11236435"></a>

POST /v2/\{project\_id\}/os-security-group-rules

POST /v2.1/\{project\_id\}/os-security-group-rules

[Table 1](#en-us_topic_0057972667_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972667_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row44937496"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row1664874"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972667_p637140"><a name="en-us_topic_0057972667_p637140"></a><a name="en-us_topic_0057972667_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972667_p51608407"><a name="en-us_topic_0057972667_p51608407"></a><a name="en-us_topic_0057972667_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972667_section37736068"></a>

[Table 2](#en-us_topic_0057972667_table58520811)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972667_table58520811"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row6215498"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p11437144313220"><a name="p11437144313220"></a><a name="p11437144313220"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row16540805"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p64736823"><a name="en-us_topic_0057972667_p64736823"></a><a name="en-us_topic_0057972667_p64736823"></a>security_group_rule</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p1743794310327"><a name="p1743794310327"></a><a name="p1743794310327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p9191297"><a name="en-us_topic_0057972667_p9191297"></a><a name="en-us_topic_0057972667_p9191297"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p40344576"><a name="en-us_topic_0057972667_p40344576"></a><a name="en-us_topic_0057972667_p40344576"></a>Specifies the security group rule, which is configured in the message body. For details, see <a href="#en-us_topic_0057972667_table46685187">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Objects of request parameter  **security\_group\_rule**

<a name="en-us_topic_0057972667_table46685187"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row533144"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p73882475137"><a name="p73882475137"></a><a name="p73882475137"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p1317554715321"><a name="p1317554715321"></a><a name="p1317554715321"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p13388114771314"><a name="p13388114771314"></a><a name="p13388114771314"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p74041747181311"><a name="p74041747181311"></a><a name="p74041747181311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row51313205"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p62728917"><a name="en-us_topic_0057972667_p62728917"></a><a name="en-us_topic_0057972667_p62728917"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p12175164783214"><a name="p12175164783214"></a><a name="p12175164783214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p47877526"><a name="en-us_topic_0057972667_p47877526"></a><a name="en-us_topic_0057972667_p47877526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p54967961"><a name="en-us_topic_0057972667_p54967961"></a><a name="en-us_topic_0057972667_p54967961"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row24949608"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p7652366"><a name="en-us_topic_0057972667_p7652366"></a><a name="en-us_topic_0057972667_p7652366"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p617644720328"><a name="p617644720328"></a><a name="p617644720328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p15861880"><a name="en-us_topic_0057972667_p15861880"></a><a name="en-us_topic_0057972667_p15861880"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p51057338"><a name="en-us_topic_0057972667_p51057338"></a><a name="en-us_topic_0057972667_p51057338"></a>Specifies the IP protocol, which can be <strong id="b40841205105128"><a name="b40841205105128"></a><a name="b40841205105128"></a>icmp</strong>, <strong id="b38036492105132"><a name="b38036492105132"></a><a name="b38036492105132"></a>tcp</strong>, or <strong id="b58731381105136"><a name="b58731381105136"></a><a name="b58731381105136"></a>udp</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row42003681"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p46855021"><a name="en-us_topic_0057972667_p46855021"></a><a name="en-us_topic_0057972667_p46855021"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p141761947173219"><a name="p141761947173219"></a><a name="p141761947173219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p37160390"><a name="en-us_topic_0057972667_p37160390"></a><a name="en-us_topic_0057972667_p37160390"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p3798072492826"><a name="en-us_topic_0057972667_p3798072492826"></a><a name="en-us_topic_0057972667_p3798072492826"></a>Specifies the start port. The value ranges from 1 to 65,535 and is no greater than the value of <strong id="b3778963692826"><a name="b3778963692826"></a><a name="b3778963692826"></a>to_port</strong>.</p>
<p id="p9270301194649"><a name="p9270301194649"></a><a name="p9270301194649"></a>If the value of <strong id="b165497995692024"><a name="b165497995692024"></a><a name="b165497995692024"></a>ip_protocol</strong> is <strong id="b27413749992024"><a name="b27413749992024"></a><a name="b27413749992024"></a>icmp</strong>, this parameter specifies the ICMP type. The value ranges from <strong id="b842352706105229"><a name="b842352706105229"></a><a name="b842352706105229"></a>0</strong> to <strong id="b842352706105232"><a name="b842352706105232"></a><a name="b842352706105232"></a>255</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row25376232"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p42208903"><a name="en-us_topic_0057972667_p42208903"></a><a name="en-us_topic_0057972667_p42208903"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p1417617474328"><a name="p1417617474328"></a><a name="p1417617474328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p63478007"><a name="en-us_topic_0057972667_p63478007"></a><a name="en-us_topic_0057972667_p63478007"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p1102684392845"><a name="en-us_topic_0057972667_p1102684392845"></a><a name="en-us_topic_0057972667_p1102684392845"></a>Specifies the end port. The value ranges from <strong id="b51538573105155"><a name="b51538573105155"></a><a name="b51538573105155"></a>1</strong> to <strong id="b9752629105159"><a name="b9752629105159"></a><a name="b9752629105159"></a>65,535</strong> and cannot be less than <strong id="b2044497892845"><a name="b2044497892845"></a><a name="b2044497892845"></a>from_port</strong>.</p>
<p id="p21363554194649"><a name="p21363554194649"></a><a name="p21363554194649"></a>If <strong id="b190639977692113"><a name="b190639977692113"></a><a name="b190639977692113"></a>ip_protocol</strong> is <strong id="b21927365292113"><a name="b21927365292113"></a><a name="b21927365292113"></a>icmp</strong>, this parameter specifies the ICMP code. The value ranges from 0 to 255. If both <strong id="b39304013292126"><a name="b39304013292126"></a><a name="b39304013292126"></a>from_port</strong> and <strong id="b122500104592126"><a name="b122500104592126"></a><a name="b122500104592126"></a>to_port</strong> are <strong id="b156348073092126"><a name="b156348073092126"></a><a name="b156348073092126"></a>-1</strong>, any ICMP packet can be transmitted.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row14387121"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p24506125"><a name="en-us_topic_0057972667_p24506125"></a><a name="en-us_topic_0057972667_p24506125"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p7176114733219"><a name="p7176114733219"></a><a name="p7176114733219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p38839134"><a name="en-us_topic_0057972667_p38839134"></a><a name="en-us_topic_0057972667_p38839134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p11207934"><a name="en-us_topic_0057972667_p11207934"></a><a name="en-us_topic_0057972667_p11207934"></a>Specifies the IP address range. The address is in CIDR format, such as 192.168.0.0/24.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row33762549"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p50411912"><a name="en-us_topic_0057972667_p50411912"></a><a name="en-us_topic_0057972667_p50411912"></a>group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p1317624711327"><a name="p1317624711327"></a><a name="p1317624711327"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p56833109"><a name="en-us_topic_0057972667_p56833109"></a><a name="en-us_topic_0057972667_p56833109"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17452544194649"><a name="p17452544194649"></a><a name="p17452544194649"></a>Specifies the source security group ID. If both<strong id="b29346720"><a name="b29346720"></a><a name="b29346720"></a> group_id</strong> and <strong id="b62793889"><a name="b62793889"></a><a name="b62793889"></a>cidr</strong> are set, <strong id="b28274094"><a name="b28274094"></a><a name="b28274094"></a>group_id</strong> prevails.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972667_section4080300"></a>

[Table 4](#en-us_topic_0057972667_table37057034)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057972667_table37057034"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row15913018"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p6740115110138"><a name="p6740115110138"></a><a name="p6740115110138"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p18721161611336"><a name="p18721161611336"></a><a name="p18721161611336"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p12740205119137"><a name="p12740205119137"></a><a name="p12740205119137"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p10740195191319"><a name="p10740195191319"></a><a name="p10740195191319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row18911189"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p55411339"><a name="en-us_topic_0057972667_p55411339"></a><a name="en-us_topic_0057972667_p55411339"></a>security_group_rule</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p127215168331"><a name="p127215168331"></a><a name="p127215168331"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p59133445"><a name="en-us_topic_0057972667_p59133445"></a><a name="en-us_topic_0057972667_p59133445"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p18191719"><a name="en-us_topic_0057972667_p18191719"></a><a name="en-us_topic_0057972667_p18191719"></a>Specifies the security group rule, which is configured in the message body. For details, see <a href="#en-us_topic_0057972667_table64243102">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Objects of response parameter  **security\_group\_rule**

<a name="en-us_topic_0057972667_table64243102"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row4043462"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p1714375414138"><a name="p1714375414138"></a><a name="p1714375414138"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p6517142119332"><a name="p6517142119332"></a><a name="p6517142119332"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p16143195491314"><a name="p16143195491314"></a><a name="p16143195491314"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p1515835401311"><a name="p1515835401311"></a><a name="p1515835401311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row14620318"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p43395070"><a name="en-us_topic_0057972667_p43395070"></a><a name="en-us_topic_0057972667_p43395070"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p125171121123310"><a name="p125171121123310"></a><a name="p125171121123310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p25339754"><a name="en-us_topic_0057972667_p25339754"></a><a name="en-us_topic_0057972667_p25339754"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p25475209"><a name="en-us_topic_0057972667_p25475209"></a><a name="en-us_topic_0057972667_p25475209"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row27950294"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p49381354"><a name="en-us_topic_0057972667_p49381354"></a><a name="en-us_topic_0057972667_p49381354"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1051752123315"><a name="p1051752123315"></a><a name="p1051752123315"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p40466701"><a name="en-us_topic_0057972667_p40466701"></a><a name="en-us_topic_0057972667_p40466701"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p19365543"><a name="en-us_topic_0057972667_p19365543"></a><a name="en-us_topic_0057972667_p19365543"></a>Specifies the IP protocol, which can be <strong id="b5311162714"><a name="b5311162714"></a><a name="b5311162714"></a>icmp</strong>, <strong id="b21441698162718"><a name="b21441698162718"></a><a name="b21441698162718"></a>tcp</strong>, or <strong id="b29346275162728"><a name="b29346275162728"></a><a name="b29346275162728"></a>udp</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row40072161"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p24619602"><a name="en-us_topic_0057972667_p24619602"></a><a name="en-us_topic_0057972667_p24619602"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p551782120336"><a name="p551782120336"></a><a name="p551782120336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p48030711"><a name="en-us_topic_0057972667_p48030711"></a><a name="en-us_topic_0057972667_p48030711"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p13512140115024"><a name="en-us_topic_0057972667_p13512140115024"></a><a name="en-us_topic_0057972667_p13512140115024"></a>Specifies the start port number. The value ranges from 1 to 65,535 and cannot be greater than <strong id="en-us_topic_0057972667_b84235270692028"><a name="en-us_topic_0057972667_b84235270692028"></a><a name="en-us_topic_0057972667_b84235270692028"></a>to_port</strong>.</p>
<p id="en-us_topic_0057972667_p53379839"><a name="en-us_topic_0057972667_p53379839"></a><a name="en-us_topic_0057972667_p53379839"></a>When the protocol type is set to ICMP, <strong id="en-us_topic_0057972667_b84235270692125"><a name="en-us_topic_0057972667_b84235270692125"></a><a name="en-us_topic_0057972667_b84235270692125"></a>from_port</strong> is the ICMP type and ranges from 0 to 255.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row10656503"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p57870399"><a name="en-us_topic_0057972667_p57870399"></a><a name="en-us_topic_0057972667_p57870399"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1451772112338"><a name="p1451772112338"></a><a name="p1451772112338"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p56990719"><a name="en-us_topic_0057972667_p56990719"></a><a name="en-us_topic_0057972667_p56990719"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p49982224114937"><a name="en-us_topic_0057972667_p49982224114937"></a><a name="en-us_topic_0057972667_p49982224114937"></a>Specifies the end port number. The value ranges from <strong id="en-us_topic_0057972667_b842352706202844"><a name="en-us_topic_0057972667_b842352706202844"></a><a name="en-us_topic_0057972667_b842352706202844"></a>1</strong> to <strong id="en-us_topic_0057972667_b842352706202850"><a name="en-us_topic_0057972667_b842352706202850"></a><a name="en-us_topic_0057972667_b842352706202850"></a>65,535</strong>.</p>
<a name="en-us_topic_0057972667_ul4865871114949"></a><a name="en-us_topic_0057972667_ul4865871114949"></a><ul id="en-us_topic_0057972667_ul4865871114949"><li>When the protocol type is set to ICMP, <strong id="b1555341283"><a name="b1555341283"></a><a name="b1555341283"></a>to_port</strong> is the ICMP code and ranges from <strong id="en-us_topic_0057972667_b842352706202945"><a name="en-us_topic_0057972667_b842352706202945"></a><a name="en-us_topic_0057972667_b842352706202945"></a>0</strong> to <strong id="en-us_topic_0057972667_b842352706202948"><a name="en-us_topic_0057972667_b842352706202948"></a><a name="en-us_topic_0057972667_b842352706202948"></a>255</strong>.</li><li>If both <strong id="en-us_topic_0057972667_b84235270692421"><a name="en-us_topic_0057972667_b84235270692421"></a><a name="en-us_topic_0057972667_b84235270692421"></a>from_port</strong> and <strong id="en-us_topic_0057972667_b84235270692451"><a name="en-us_topic_0057972667_b84235270692451"></a><a name="en-us_topic_0057972667_b84235270692451"></a>to_port</strong> are <strong id="en-us_topic_0057972667_b84235270692437"><a name="en-us_topic_0057972667_b84235270692437"></a><a name="en-us_topic_0057972667_b84235270692437"></a>-1</strong>, it indicates that any ICMP packet can be transmitted.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057972667_row3908185"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p48127554"><a name="en-us_topic_0057972667_p48127554"></a><a name="en-us_topic_0057972667_p48127554"></a>ip_range</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p95172211332"><a name="p95172211332"></a><a name="p95172211332"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p6017800"><a name="en-us_topic_0057972667_p6017800"></a><a name="en-us_topic_0057972667_p6017800"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p21001840194649"><a name="p21001840194649"></a><a name="p21001840194649"></a>Specifies the IP address range, including the CIDR information, such as <strong id="b32773974"><a name="b32773974"></a><a name="b32773974"></a>"ip_range": {"cidr": "0.0.0.0/0"}</strong>. For details, see the ip_range object.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row32803348"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p39825499"><a name="en-us_topic_0057972667_p39825499"></a><a name="en-us_topic_0057972667_p39825499"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p751722163317"><a name="p751722163317"></a><a name="p751722163317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p4640007"><a name="en-us_topic_0057972667_p4640007"></a><a name="en-us_topic_0057972667_p4640007"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p42776493"><a name="en-us_topic_0057972667_p42776493"></a><a name="en-us_topic_0057972667_p42776493"></a>Nothing is returned.</p>
</td>
</tr>
<tr id="en-us_topic_0057972667_row49444123"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p45551026"><a name="en-us_topic_0057972667_p45551026"></a><a name="en-us_topic_0057972667_p45551026"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1351817212339"><a name="p1351817212339"></a><a name="p1351817212339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p65754481"><a name="en-us_topic_0057972667_p65754481"></a><a name="en-us_topic_0057972667_p65754481"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p39377290"><a name="en-us_topic_0057972667_p39377290"></a><a name="en-us_topic_0057972667_p39377290"></a>Specifies the security group rule ID in UUID format.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **ip\_range**  objects

<a name="en-us_topic_0057972667_table35443891"></a>
<table><thead align="left"><tr id="en-us_topic_0057972667_row42291718"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p1757245818131"><a name="p1757245818131"></a><a name="p1757245818131"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p6837447103311"><a name="p6837447103311"></a><a name="p6837447103311"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p19588958181315"><a name="p19588958181315"></a><a name="p19588958181315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p558820583133"><a name="p558820583133"></a><a name="p558820583133"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972667_row41816140"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972667_p31664161"><a name="en-us_topic_0057972667_p31664161"></a><a name="en-us_topic_0057972667_p31664161"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p18837647103316"><a name="p18837647103316"></a><a name="p18837647103316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972667_p14660263"><a name="en-us_topic_0057972667_p14660263"></a><a name="en-us_topic_0057972667_p14660263"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972667_p18987236"><a name="en-us_topic_0057972667_p18987236"></a><a name="en-us_topic_0057972667_p18987236"></a>Specifies the IP address range. The address is in CIDR format, such as 192.168.0.0/24.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972667_section36722706"></a>

```
POST https://{endpoint}/v2.1/{project_id}/os-security-group-rules
```

```
{
	"security_group_rule": {
		"from_port": "443",
		"ip_protocol": "tcp",
		"to_port": "443",
		"cidr": "0.0.0.0/0",
		"parent_group_id": "48700ff3-30b8-4e63-845f-a79c9633e9fb"
	}
}
```

## Example Response<a name="section08601329298"></a>

```
{
	"security_group_rule": {
		"id": "F4966B29-D21D-B211-B6B4-0018E1C5D866",
		"ip_range": {
			"cidr": "0.0.0.0/0"
		},
		"parent_group_id": "48700ff3-30b8-4e63-845f-a79c9633e9fb",
		"to_port": 443,
		"ip_protocol": "tcp",
		"group": {
			
		},
		"from_port": 443
	}
}
```

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

