# Querying a Virtual Interface<a name="en-dc_topic_0055025332"></a>

## Function<a name="section62587221143243"></a>

This API is used to query a virtual interface.

## URI<a name="section13727974143243"></a>

GET /v2.0/dcaas/virtual-interfaces/\{virtual\_interface\_id\}

**Table  1**  Parameter description

<a name="table1222245015813"></a>
<table><thead align="left"><tr id="row12230205015819"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p162305501281"><a name="p162305501281"></a><a name="p162305501281"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p9230650285"><a name="p9230650285"></a><a name="p9230650285"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p19230450783"><a name="p19230450783"></a><a name="p19230450783"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p152371550289"><a name="p152371550289"></a><a name="p152371550289"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row023735012814"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p2023716501788"><a name="p2023716501788"></a><a name="p2023716501788"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p123716501816"><a name="p123716501816"></a><a name="p123716501816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p4244175012817"><a name="p4244175012817"></a><a name="p4244175012817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p1624475015815"><a name="p1624475015815"></a><a name="p1624475015815"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section48686650143243"></a>

[Table 2](#table7546806143243)  lists the request parameter.

**Table  2**  Request parameter

<a name="table7546806143243"></a>
<table><thead align="left"><tr id="row9156029143243"><th class="cellrowborder" valign="top" width="25.4%" id="mcps1.2.5.1.1"><p id="p18912799143243"><a name="p18912799143243"></a><a name="p18912799143243"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.09%" id="mcps1.2.5.1.2"><p id="p46366729143243"><a name="p46366729143243"></a><a name="p46366729143243"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.5.1.3"><p id="p7326913143243"><a name="p7326913143243"></a><a name="p7326913143243"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.43%" id="mcps1.2.5.1.4"><p id="p5940989143243"><a name="p5940989143243"></a><a name="p5940989143243"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18016354143243"><td class="cellrowborder" valign="top" width="25.4%" headers="mcps1.2.5.1.1 "><p id="p43004679143243"><a name="p43004679143243"></a><a name="p43004679143243"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.2.5.1.2 "><p id="p44279538143243"><a name="p44279538143243"></a><a name="p44279538143243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.5.1.3 "><p id="p8623001143243"><a name="p8623001143243"></a><a name="p8623001143243"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.43%" headers="mcps1.2.5.1.4 "><p id="p13272417143243"><a name="p13272417143243"></a><a name="p13272417143243"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section60387869143243"></a>

[Table 3](#table10476506155243)  lists the response parameter.

**Table  3**  Response parameter

<a name="table10476506155243"></a>
<table><thead align="left"><tr id="row28606500155243"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p28732152155335"><a name="p28732152155335"></a><a name="p28732152155335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p45602971155335"><a name="p45602971155335"></a><a name="p45602971155335"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p29780927155335"><a name="p29780927155335"></a><a name="p29780927155335"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17724599155243"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p26406454155243"><a name="p26406454155243"></a><a name="p26406454155243"></a>virtual_interface</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p58548062155243"><a name="p58548062155243"></a><a name="p58548062155243"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p2699206155243"><a name="p2699206155243"></a><a name="p2699206155243"></a>Specifies the <strong id="b842352706193939"><a name="b842352706193939"></a><a name="b842352706193939"></a>virtual_interface</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interface**

<a name="table13084897143243"></a>
<table><thead align="left"><tr id="row63914967143243"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p41919048143243"><a name="p41919048143243"></a><a name="p41919048143243"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.4.1.2"><p id="p60468452143243"><a name="p60468452143243"></a><a name="p60468452143243"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.4.1.3"><p id="p55013545143243"><a name="p55013545143243"></a><a name="p55013545143243"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53726974143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p12584516143546"><a name="p12584516143546"></a><a name="p12584516143546"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p49386488143546"><a name="p49386488143546"></a><a name="p49386488143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p45354670143546"><a name="p45354670143546"></a><a name="p45354670143546"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
<tr id="row4176548143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p44986957143546"><a name="p44986957143546"></a><a name="p44986957143546"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p31860680143546"><a name="p31860680143546"></a><a name="p31860680143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p23896857143546"><a name="p23896857143546"></a><a name="p23896857143546"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row65710368143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p52697866143546"><a name="p52697866143546"></a><a name="p52697866143546"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p10086124143546"><a name="p10086124143546"></a><a name="p10086124143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p20902416143546"><a name="p20902416143546"></a><a name="p20902416143546"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row19355927143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p48892798143546"><a name="p48892798143546"></a><a name="p48892798143546"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p22343196143546"><a name="p22343196143546"></a><a name="p22343196143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p20562460143546"><a name="p20562460143546"></a><a name="p20562460143546"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row34730217143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p7641284143546"><a name="p7641284143546"></a><a name="p7641284143546"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p38562298143546"><a name="p38562298143546"></a><a name="p38562298143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p35796647143546"><a name="p35796647143546"></a><a name="p35796647143546"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row36563176143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p8926816143546"><a name="p8926816143546"></a><a name="p8926816143546"></a>vgw_ id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p24519566143546"><a name="p24519566143546"></a><a name="p24519566143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p28461994143546"><a name="p28461994143546"></a><a name="p28461994143546"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row36603909143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p43021704143546"><a name="p43021704143546"></a><a name="p43021704143546"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p11645223143546"><a name="p11645223143546"></a><a name="p11645223143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p40836314143546"><a name="p40836314143546"></a><a name="p40836314143546"></a>Specifies the interface type. The value can be <strong id="b842352706142157"><a name="b842352706142157"></a><a name="b842352706142157"></a>public</strong> or <strong id="b84235270614220"><a name="b84235270614220"></a><a name="b84235270614220"></a>private</strong>.</p>
</td>
</tr>
<tr id="row44061354143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p22611601143546"><a name="p22611601143546"></a><a name="p22611601143546"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p20247790143546"><a name="p20247790143546"></a><a name="p20247790143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p31831409143546"><a name="p31831409143546"></a><a name="p31831409143546"></a>Specifies the access service type. The value can be <strong id="b1650500527142036"><a name="b1650500527142036"></a><a name="b1650500527142036"></a>vpc</strong>, <strong id="b26378606142036"><a name="b26378606142036"></a><a name="b26378606142036"></a>public service</strong>, or <strong id="b1032837367142036"><a name="b1032837367142036"></a><a name="b1032837367142036"></a>vpc and public service</strong>.</p>
</td>
</tr>
<tr id="row53174924143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p57907931143546"><a name="p57907931143546"></a><a name="p57907931143546"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p15690831212825"><a name="p15690831212825"></a><a name="p15690831212825"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p3896574143546"><a name="p3896574143546"></a><a name="p3896574143546"></a>Specifies the VLAN used by the local gateway to communicate with the remote gateway.</p>
</td>
</tr>
<tr id="row44429599143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p2367582143546"><a name="p2367582143546"></a><a name="p2367582143546"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p5717726819440"><a name="p5717726819440"></a><a name="p5717726819440"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p39737423143546"><a name="p39737423143546"></a><a name="p39737423143546"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row14409097143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p12644148143546"><a name="p12644148143546"></a><a name="p12644148143546"></a>local_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p35923497143546"><a name="p35923497143546"></a><a name="p35923497143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p3939547143546"><a name="p3939547143546"></a><a name="p3939547143546"></a>Specifies the IPv4 address of the local gateway.</p>
</td>
</tr>
<tr id="row49533369143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p25908295143546"><a name="p25908295143546"></a><a name="p25908295143546"></a>remote_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p52274971143546"><a name="p52274971143546"></a><a name="p52274971143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p48820178143546"><a name="p48820178143546"></a><a name="p48820178143546"></a>Specifies the IPv4 address of the remote gateway.</p>
</td>
</tr>
<tr id="row7065973143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p25025401143546"><a name="p25025401143546"></a><a name="p25025401143546"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p9245370143546"><a name="p9245370143546"></a><a name="p9245370143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p52631845143546"><a name="p52631845143546"></a><a name="p52631845143546"></a>Specifies the routing mode. The value can be <strong id="b84235270614653"><a name="b84235270614653"></a><a name="b84235270614653"></a>static</strong> or <strong id="b84235270614655"><a name="b84235270614655"></a><a name="b84235270614655"></a>bgp</strong>.</p>
</td>
</tr>
<tr id="row62791961143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p7702136143546"><a name="p7702136143546"></a><a name="p7702136143546"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p27569269143546"><a name="p27569269143546"></a><a name="p27569269143546"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p44565943143546"><a name="p44565943143546"></a><a name="p44565943143546"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row58065084143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p45788287143546"><a name="p45788287143546"></a><a name="p45788287143546"></a>bgp_md5</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p43941858143546"><a name="p43941858143546"></a><a name="p43941858143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p38906626143546"><a name="p38906626143546"></a><a name="p38906626143546"></a>Specifies the MD5 password of the BGP peer.</p>
</td>
</tr>
<tr id="row54977426143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p5096015143546"><a name="p5096015143546"></a><a name="p5096015143546"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p51775955143546"><a name="p51775955143546"></a><a name="p51775955143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p55585133143546"><a name="p55585133143546"></a><a name="p55585133143546"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row32539190143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p19542158143546"><a name="p19542158143546"></a><a name="p19542158143546"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p45749592143546"><a name="p45749592143546"></a><a name="p45749592143546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p33407370143546"><a name="p33407370143546"></a><a name="p33407370143546"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row2152096161637"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p26810415161640"><a name="p26810415161640"></a><a name="p26810415161640"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p12233240161640"><a name="p12233240161640"></a><a name="p12233240161640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p56556788161640"><a name="p56556788161640"></a><a name="p56556788161640"></a>Specifies the time when the virtual interface is created.</p>
</td>
</tr>
<tr id="row32718554171555"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p5120253317162"><a name="p5120253317162"></a><a name="p5120253317162"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p5376451317162"><a name="p5376451317162"></a><a name="p5376451317162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p2478359417162"><a name="p2478359417162"></a><a name="p2478359417162"></a>Specifies the time when the virtual interface is deleted.</p>
</td>
</tr>
<tr id="row3274315019446"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p5495181219448"><a name="p5495181219448"></a><a name="p5495181219448"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p2191175019448"><a name="p2191175019448"></a><a name="p2191175019448"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p54377194155258"><a name="p54377194155258"></a><a name="p54377194155258"></a>Specifies the virtual interface status.</p>
<p id="p1580958519448"><a name="p1580958519448"></a><a name="p1580958519448"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>, <strong id="b1047171556233155"><a name="b1047171556233155"></a><a name="b1047171556233155"></a>DELETED</strong>, <strong id="b1391270644233155"><a name="b1391270644233155"></a><a name="b1391270644233155"></a>AUTHORIZATION</strong>, or <strong id="b741943905233155"><a name="b741943905233155"></a><a name="b741943905233155"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row18618790143546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p54352348143546"><a name="p54352348143546"></a><a name="p54352348143546"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p4968436143546"><a name="p4968436143546"></a><a name="p4968436143546"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p5500751815534"><a name="p5500751815534"></a><a name="p5500751815534"></a>Specifies the administrative state of the virtual interface.</p>
<p id="p49075090143546"><a name="p49075090143546"></a><a name="p49075090143546"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
<tr id="row1917945155117"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p12835141012514"><a name="p12835141012514"></a><a name="p12835141012514"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.2 "><p id="p98351610105120"><a name="p98351610105120"></a><a name="p98351610105120"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.4.1.3 "><p id="p18835191019516"><a name="p18835191019516"></a><a name="p18835191019516"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b2038123114512"><a name="b2038123114512"></a><a name="b2038123114512"></a>true</strong> or <strong id="b439183118514"><a name="b439183118514"></a><a name="b439183118514"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section23585659143243"></a>

-   Example request

    ```
    GET /v2.0/dcaas/virtual-interfaces/{virtual_interface_id}
    ```


-   Example response

    ```
    {    
        "virtual_interface" : {
            "id" : "67c59cf4-1a64-46c7-763f-22eb1b9e8986",  
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual interface1",
            "description" : "",
            "direct_connect_id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
            "vgw_id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389",
            "type" : "private",
            "service_type" : "vpc",
            "vlan" : 100,
            "bandwidth" : 10,
            "local_gateway_v4_ip" : "180.1.1.1/24",
            "remote_gateway_v4_ip"  : "180.1.1.2/24",
            "route_mode"  : "static",
            "remote_ep_group_id" : "78e34cf1-5468-87c7-223d-56e78b9699ef"
        }
    }
    ```


## Returned Value<a name="section14947747173413"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

