# Creating a Virtual Interface<a name="en-dc_topic_0055025329"></a>

## Function<a name="section54540374"></a>

This API is used to create a virtual interface.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This virtual interface does not support the association with  **double ipsec**  virtual gateway.  

## URI<a name="section21101319"></a>

POST /v2.0/dcaas/virtual-interfaces

## Request<a name="section31485239"></a>

[Table 1](#table10476506155243)  lists the request parameter.

**Table  1**  Request parameter

<a name="table10476506155243"></a>
<table><thead align="left"><tr id="row28606500155243"><th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.5.1.1"><p id="p28732152155335"><a name="p28732152155335"></a><a name="p28732152155335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.5.1.2"><p id="p45602971155335"><a name="p45602971155335"></a><a name="p45602971155335"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.2.5.1.3"><p id="p2853179155335"><a name="p2853179155335"></a><a name="p2853179155335"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.69%" id="mcps1.2.5.1.4"><p id="p29780927155335"><a name="p29780927155335"></a><a name="p29780927155335"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17724599155243"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.5.1.1 "><p id="p26406454155243"><a name="p26406454155243"></a><a name="p26406454155243"></a>virtual_interface</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.5.1.2 "><p id="p58548062155243"><a name="p58548062155243"></a><a name="p58548062155243"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.2.5.1.3 "><p id="p44772566155243"><a name="p44772566155243"></a><a name="p44772566155243"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.2.5.1.4 "><p id="p2699206155243"><a name="p2699206155243"></a><a name="p2699206155243"></a>Specifies the <strong id="b84235270619309"><a name="b84235270619309"></a><a name="b84235270619309"></a>virtual_interface</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interface**

<a name="table26517876"></a>
<table><thead align="left"><tr id="row40476817"><th class="cellrowborder" valign="top" width="16.64%" id="mcps1.1.5.1.1"><p id="p57396781"><a name="p57396781"></a><a name="p57396781"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.030000000000001%" id="mcps1.1.5.1.2"><p id="p18627652"><a name="p18627652"></a><a name="p18627652"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.3"><p id="p32444864"><a name="p32444864"></a><a name="p32444864"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="54.03%" id="mcps1.1.5.1.4"><p id="p10788361"><a name="p10788361"></a><a name="p10788361"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1442054"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p631864211427"><a name="p631864211427"></a><a name="p631864211427"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p46548661212825"><a name="p46548661212825"></a><a name="p46548661212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p40193754212825"><a name="p40193754212825"></a><a name="p40193754212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p5825474911712"><a name="p5825474911712"></a><a name="p5825474911712"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row56455847212711"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5481910311427"><a name="p5481910311427"></a><a name="p5481910311427"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p60303421212825"><a name="p60303421212825"></a><a name="p60303421212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p43405365212825"><a name="p43405365212825"></a><a name="p43405365212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p1870090611712"><a name="p1870090611712"></a><a name="p1870090611712"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row17304671212718"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p829405411427"><a name="p829405411427"></a><a name="p829405411427"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p10454292212825"><a name="p10454292212825"></a><a name="p10454292212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p30649615212825"><a name="p30649615212825"></a><a name="p30649615212825"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p2470420611712"><a name="p2470420611712"></a><a name="p2470420611712"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row10181252212730"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p1566292411427"><a name="p1566292411427"></a><a name="p1566292411427"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p24798963212825"><a name="p24798963212825"></a><a name="p24798963212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p20471702212825"><a name="p20471702212825"></a><a name="p20471702212825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p401290811712"><a name="p401290811712"></a><a name="p401290811712"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row12404882212734"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p1264137011427"><a name="p1264137011427"></a><a name="p1264137011427"></a>vgw_ id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p15690831212825"><a name="p15690831212825"></a><a name="p15690831212825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p31440261212825"><a name="p31440261212825"></a><a name="p31440261212825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p6152911712"><a name="p6152911712"></a><a name="p6152911712"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row13373700212741"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p2128042311427"><a name="p2128042311427"></a><a name="p2128042311427"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p2805339212955"><a name="p2805339212955"></a><a name="p2805339212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p43667943212955"><a name="p43667943212955"></a><a name="p43667943212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p3688129811712"><a name="p3688129811712"></a><a name="p3688129811712"></a>Specifies the interface type. The value can be <strong id="b842352706142157"><a name="b842352706142157"></a><a name="b842352706142157"></a>public</strong> or <strong id="b84235270614220"><a name="b84235270614220"></a><a name="b84235270614220"></a>private</strong>.</p>
</td>
</tr>
<tr id="row568472521295"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p86017311427"><a name="p86017311427"></a><a name="p86017311427"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p46823096212955"><a name="p46823096212955"></a><a name="p46823096212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p59054635212955"><a name="p59054635212955"></a><a name="p59054635212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p6355976011712"><a name="p6355976011712"></a><a name="p6355976011712"></a>Specifies the access service type. The value can be <strong id="b1650500527142036"><a name="b1650500527142036"></a><a name="b1650500527142036"></a>vpc</strong>, <strong id="b26378606142036"><a name="b26378606142036"></a><a name="b26378606142036"></a>public service</strong>, or <strong id="b1032837367142036"><a name="b1032837367142036"></a><a name="b1032837367142036"></a>vpc and public service</strong>.</p>
</td>
</tr>
<tr id="row938903521299"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p15849111427"><a name="p15849111427"></a><a name="p15849111427"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p6620590719243"><a name="p6620590719243"></a><a name="p6620590719243"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p34771507212955"><a name="p34771507212955"></a><a name="p34771507212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p5268943211712"><a name="p5268943211712"></a><a name="p5268943211712"></a>Specifies the VLAN used by the local gateway to communicate with the remote gateway.</p>
</td>
</tr>
<tr id="row47530080212912"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p1414929511427"><a name="p1414929511427"></a><a name="p1414929511427"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p795784219243"><a name="p795784219243"></a><a name="p795784219243"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p63373303212955"><a name="p63373303212955"></a><a name="p63373303212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p2084178111712"><a name="p2084178111712"></a><a name="p2084178111712"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row54509260212915"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5908435411427"><a name="p5908435411427"></a><a name="p5908435411427"></a>local_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p61142987212955"><a name="p61142987212955"></a><a name="p61142987212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p65804377212955"><a name="p65804377212955"></a><a name="p65804377212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p2646666211712"><a name="p2646666211712"></a><a name="p2646666211712"></a>Specifies the IPv4 address of the local gateway.</p>
</td>
</tr>
<tr id="row62300161212918"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5187139511427"><a name="p5187139511427"></a><a name="p5187139511427"></a>remote_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p35371259212955"><a name="p35371259212955"></a><a name="p35371259212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p21643169212955"><a name="p21643169212955"></a><a name="p21643169212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p1626021711712"><a name="p1626021711712"></a><a name="p1626021711712"></a>Specifies the IPv4 address of the remote gateway.</p>
</td>
</tr>
<tr id="row24943363212922"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p3521789411427"><a name="p3521789411427"></a><a name="p3521789411427"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p19656103212955"><a name="p19656103212955"></a><a name="p19656103212955"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p8052318212955"><a name="p8052318212955"></a><a name="p8052318212955"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p1571573511712"><a name="p1571573511712"></a><a name="p1571573511712"></a>Specifies the routing mode. The value can be <strong id="b84235270614653"><a name="b84235270614653"></a><a name="b84235270614653"></a>static</strong> or <strong id="b84235270614655"><a name="b84235270614655"></a><a name="b84235270614655"></a>bgp</strong>.</p>
</td>
</tr>
<tr id="row59943627212941"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5486593211531"><a name="p5486593211531"></a><a name="p5486593211531"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p1752129811559"><a name="p1752129811559"></a><a name="p1752129811559"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p1835599911632"><a name="p1835599911632"></a><a name="p1835599911632"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p6033433511712"><a name="p6033433511712"></a><a name="p6033433511712"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row4015905011457"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p4776526611531"><a name="p4776526611531"></a><a name="p4776526611531"></a>bgp_md5</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p4135238711559"><a name="p4135238711559"></a><a name="p4135238711559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p199791211632"><a name="p199791211632"></a><a name="p199791211632"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p553752511712"><a name="p553752511712"></a><a name="p553752511712"></a>Specifies the MD5 password of the BGP peer.</p>
</td>
</tr>
<tr id="row2948665411455"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p6322989011531"><a name="p6322989011531"></a><a name="p6322989011531"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p650274411559"><a name="p650274411559"></a><a name="p650274411559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p6053173111632"><a name="p6053173111632"></a><a name="p6053173111632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p1541724111712"><a name="p1541724111712"></a><a name="p1541724111712"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row3638891111452"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5801546311531"><a name="p5801546311531"></a><a name="p5801546311531"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p5839959011559"><a name="p5839959011559"></a><a name="p5839959011559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p806962511632"><a name="p806962511632"></a><a name="p806962511632"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p3915992911712"><a name="p3915992911712"></a><a name="p3915992911712"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row5063700111449"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p2411078411531"><a name="p2411078411531"></a><a name="p2411078411531"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p6401534911559"><a name="p6401534911559"></a><a name="p6401534911559"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p3278663311632"><a name="p3278663311632"></a><a name="p3278663311632"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p34476628145745"><a name="p34476628145745"></a><a name="p34476628145745"></a>Specifies the administrative state of the virtual interface.</p>
<p id="p183284011712"><a name="p183284011712"></a><a name="p183284011712"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
<tr id="row146508174413"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p5378216134410"><a name="p5378216134410"></a><a name="p5378216134410"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p14378916204417"><a name="p14378916204417"></a><a name="p14378916204417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p18378121634415"><a name="p18378121634415"></a><a name="p18378121634415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p1378151612447"><a name="p1378151612447"></a><a name="p1378151612447"></a>Specifies the time when the virtual interface is deleted.</p>
</td>
</tr>
<tr id="row1776074174410"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p38861723104420"><a name="p38861723104420"></a><a name="p38861723104420"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p1288632314411"><a name="p1288632314411"></a><a name="p1288632314411"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p6886122314415"><a name="p6886122314415"></a><a name="p6886122314415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.5.1.4 "><p id="p98863234446"><a name="p98863234446"></a><a name="p98863234446"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b129401644155014"><a name="b129401644155014"></a><a name="b129401644155014"></a>true</strong> or <strong id="b173491248175017"><a name="b173491248175017"></a><a name="b173491248175017"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section14931696"></a>

[Table 2](#table15831690155351)  lists the response parameter.

**Table  2**  Response parameter

<a name="table15831690155351"></a>
<table><thead align="left"><tr id="row65470986155351"><th class="cellrowborder" valign="top" width="21.2%" id="mcps1.2.5.1.1"><p id="p1549613155351"><a name="p1549613155351"></a><a name="p1549613155351"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.5.1.2"><p id="p58409866155351"><a name="p58409866155351"></a><a name="p58409866155351"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.27%" id="mcps1.2.5.1.3"><p id="p33578695155351"><a name="p33578695155351"></a><a name="p33578695155351"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44.82%" id="mcps1.2.5.1.4"><p id="p35519756155351"><a name="p35519756155351"></a><a name="p35519756155351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58528002155351"><td class="cellrowborder" valign="top" width="21.2%" headers="mcps1.2.5.1.1 "><p id="p43147728155351"><a name="p43147728155351"></a><a name="p43147728155351"></a>virtual_interface</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.5.1.2 "><p id="p5305119155351"><a name="p5305119155351"></a><a name="p5305119155351"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.2.5.1.3 "><p id="p27061527155351"><a name="p27061527155351"></a><a name="p27061527155351"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.82%" headers="mcps1.2.5.1.4 "><p id="p44500063155351"><a name="p44500063155351"></a><a name="p44500063155351"></a>Specifies the <strong id="b842352706192953"><a name="b842352706192953"></a><a name="b842352706192953"></a>virtual_interface</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interface**

<a name="table31929956"></a>
<table><thead align="left"><tr id="row12454319"><th class="cellrowborder" valign="top" width="17.04%" id="mcps1.1.5.1.1"><p id="p2166929"><a name="p2166929"></a><a name="p2166929"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.030000000000001%" id="mcps1.1.5.1.2"><p id="p41303584"><a name="p41303584"></a><a name="p41303584"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.09%" id="mcps1.1.5.1.3"><p id="p57256003"><a name="p57256003"></a><a name="p57256003"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="53.839999999999996%" id="mcps1.1.5.1.4"><p id="p7224675"><a name="p7224675"></a><a name="p7224675"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48327783"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p2618796021374"><a name="p2618796021374"></a><a name="p2618796021374"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p1461720021374"><a name="p1461720021374"></a><a name="p1461720021374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p482116621374"><a name="p482116621374"></a><a name="p482116621374"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p3207700921374"><a name="p3207700921374"></a><a name="p3207700921374"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
<tr id="row132017831196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p333807371196"><a name="p333807371196"></a><a name="p333807371196"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p173674531196"><a name="p173674531196"></a><a name="p173674531196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p40486021196"><a name="p40486021196"></a><a name="p40486021196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p111380851196"><a name="p111380851196"></a><a name="p111380851196"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row331021501196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p35991691196"><a name="p35991691196"></a><a name="p35991691196"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p405615271196"><a name="p405615271196"></a><a name="p405615271196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p629522941196"><a name="p629522941196"></a><a name="p629522941196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p386641011196"><a name="p386641011196"></a><a name="p386641011196"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row37182191196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p509191201196"><a name="p509191201196"></a><a name="p509191201196"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p320034021196"><a name="p320034021196"></a><a name="p320034021196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p468372521196"><a name="p468372521196"></a><a name="p468372521196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p206113541196"><a name="p206113541196"></a><a name="p206113541196"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row164870161196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p339163151196"><a name="p339163151196"></a><a name="p339163151196"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p281702881196"><a name="p281702881196"></a><a name="p281702881196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p22997811196"><a name="p22997811196"></a><a name="p22997811196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p265460801196"><a name="p265460801196"></a><a name="p265460801196"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row33489941196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p54667311196"><a name="p54667311196"></a><a name="p54667311196"></a>vgw_ id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p642780351196"><a name="p642780351196"></a><a name="p642780351196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p389339591196"><a name="p389339591196"></a><a name="p389339591196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p554614621196"><a name="p554614621196"></a><a name="p554614621196"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row149875021196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p243199781196"><a name="p243199781196"></a><a name="p243199781196"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p571586131196"><a name="p571586131196"></a><a name="p571586131196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p505104541196"><a name="p505104541196"></a><a name="p505104541196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p97609621196"><a name="p97609621196"></a><a name="p97609621196"></a>Specifies the interface type. The value can be <strong id="b1717590200"><a name="b1717590200"></a><a name="b1717590200"></a>public</strong> or <strong id="b1009385088"><a name="b1009385088"></a><a name="b1009385088"></a>private</strong>.</p>
</td>
</tr>
<tr id="row376157571196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p68485931196"><a name="p68485931196"></a><a name="p68485931196"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p439767401196"><a name="p439767401196"></a><a name="p439767401196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p665451531196"><a name="p665451531196"></a><a name="p665451531196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p664450301196"><a name="p664450301196"></a><a name="p664450301196"></a>Specifies the access service type. The value can be <strong id="b565282292"><a name="b565282292"></a><a name="b565282292"></a>vpc</strong>, <strong id="b811334040"><a name="b811334040"></a><a name="b811334040"></a>public service</strong>, or <strong id="b1507529174"><a name="b1507529174"></a><a name="b1507529174"></a>vpc and public service</strong>.</p>
</td>
</tr>
<tr id="row664534611196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p403989971196"><a name="p403989971196"></a><a name="p403989971196"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p2172314019233"><a name="p2172314019233"></a><a name="p2172314019233"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p209297901196"><a name="p209297901196"></a><a name="p209297901196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p371326101196"><a name="p371326101196"></a><a name="p371326101196"></a>Specifies the VLAN used by the local gateway to communicate with the remote gateway.</p>
</td>
</tr>
<tr id="row104245921196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p131328481196"><a name="p131328481196"></a><a name="p131328481196"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p43860619233"><a name="p43860619233"></a><a name="p43860619233"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p384535671196"><a name="p384535671196"></a><a name="p384535671196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p221921381196"><a name="p221921381196"></a><a name="p221921381196"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row76881981196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p732011196"><a name="p732011196"></a><a name="p732011196"></a>local_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p140156581196"><a name="p140156581196"></a><a name="p140156581196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p617673801196"><a name="p617673801196"></a><a name="p617673801196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p551321021196"><a name="p551321021196"></a><a name="p551321021196"></a>Specifies the IPv4 address of the local gateway.</p>
</td>
</tr>
<tr id="row389448591196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p90820861196"><a name="p90820861196"></a><a name="p90820861196"></a>remote_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p33966801196"><a name="p33966801196"></a><a name="p33966801196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p331735681196"><a name="p331735681196"></a><a name="p331735681196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p5039821196"><a name="p5039821196"></a><a name="p5039821196"></a>Specifies the IPv4 address of the remote gateway.</p>
</td>
</tr>
<tr id="row157785221196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p228996541196"><a name="p228996541196"></a><a name="p228996541196"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p666832221196"><a name="p666832221196"></a><a name="p666832221196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p104909101196"><a name="p104909101196"></a><a name="p104909101196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p376926441196"><a name="p376926441196"></a><a name="p376926441196"></a>Specifies the routing mode. The value can be <strong id="b157274550"><a name="b157274550"></a><a name="b157274550"></a>static</strong> or <strong id="b55467061"><a name="b55467061"></a><a name="b55467061"></a>bgp</strong>.</p>
</td>
</tr>
<tr id="row525464161196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p434432011196"><a name="p434432011196"></a><a name="p434432011196"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p598703751196"><a name="p598703751196"></a><a name="p598703751196"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p389021301196"><a name="p389021301196"></a><a name="p389021301196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p581173601196"><a name="p581173601196"></a><a name="p581173601196"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row339764761196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p484958161196"><a name="p484958161196"></a><a name="p484958161196"></a>bgp_md5</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p237595901196"><a name="p237595901196"></a><a name="p237595901196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p632235381196"><a name="p632235381196"></a><a name="p632235381196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p510608971196"><a name="p510608971196"></a><a name="p510608971196"></a>Specifies the MD5 password of the BGP peer.</p>
</td>
</tr>
<tr id="row454942751196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p654298221196"><a name="p654298221196"></a><a name="p654298221196"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p224926471196"><a name="p224926471196"></a><a name="p224926471196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p478014591196"><a name="p478014591196"></a><a name="p478014591196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p269736001196"><a name="p269736001196"></a><a name="p269736001196"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row323284531196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p400671011196"><a name="p400671011196"></a><a name="p400671011196"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p12648791196"><a name="p12648791196"></a><a name="p12648791196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p112447571196"><a name="p112447571196"></a><a name="p112447571196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p207288201196"><a name="p207288201196"></a><a name="p207288201196"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row65161811161542"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p54091007161552"><a name="p54091007161552"></a><a name="p54091007161552"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p30487753161552"><a name="p30487753161552"></a><a name="p30487753161552"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p23326369161552"><a name="p23326369161552"></a><a name="p23326369161552"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p19272895161552"><a name="p19272895161552"></a><a name="p19272895161552"></a>Specifies the time when the virtual interface is created.</p>
</td>
</tr>
<tr id="row2796053219354"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p642858221940"><a name="p642858221940"></a><a name="p642858221940"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p397691041940"><a name="p397691041940"></a><a name="p397691041940"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p720151940"><a name="p720151940"></a><a name="p720151940"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p233835145756"><a name="p233835145756"></a><a name="p233835145756"></a>Specifies the virtual interface status.</p>
<p id="p58332501940"><a name="p58332501940"></a><a name="p58332501940"></a>The value can be <strong id="b49883069145718"><a name="b49883069145718"></a><a name="b49883069145718"></a>ACTIVE</strong>, <strong id="b46294441145718"><a name="b46294441145718"></a><a name="b46294441145718"></a>DOWN</strong>, <strong id="b13996792145718"><a name="b13996792145718"></a><a name="b13996792145718"></a>BUILD</strong>, <strong id="b58862265145718"><a name="b58862265145718"></a><a name="b58862265145718"></a>ERROR</strong>, <strong id="b59998343145718"><a name="b59998343145718"></a><a name="b59998343145718"></a>PENDING_CREATE</strong>, <strong id="b3114178145718"><a name="b3114178145718"></a><a name="b3114178145718"></a>PENDING_UPDATE</strong>, <strong id="b28027603145718"><a name="b28027603145718"></a><a name="b28027603145718"></a>PENDING_DELETE</strong>, <strong id="b841562335232956"><a name="b841562335232956"></a><a name="b841562335232956"></a>DELETED</strong>, <strong id="b16225981232956"><a name="b16225981232956"></a><a name="b16225981232956"></a>AUTHORIZATION</strong>, or <strong id="b1915085873232956"><a name="b1915085873232956"></a><a name="b1915085873232956"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row454576521196"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p5944441196"><a name="p5944441196"></a><a name="p5944441196"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p628989821196"><a name="p628989821196"></a><a name="p628989821196"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p649240481196"><a name="p649240481196"></a><a name="p649240481196"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p4985370514581"><a name="p4985370514581"></a><a name="p4985370514581"></a>Specifies the administrative state of the virtual interface.</p>
<p id="p49345861196"><a name="p49345861196"></a><a name="p49345861196"></a>The value can be <strong id="b1950852145718"><a name="b1950852145718"></a><a name="b1950852145718"></a>true</strong> or <strong id="b17557668145718"><a name="b17557668145718"></a><a name="b17557668145718"></a>false</strong>.</p>
</td>
</tr>
<tr id="row13154715163955"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.1 "><p id="p35942582163959"><a name="p35942582163959"></a><a name="p35942582163959"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.1.5.1.2 "><p id="p25668004163959"><a name="p25668004163959"></a><a name="p25668004163959"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.1.5.1.3 "><p id="p65842410163959"><a name="p65842410163959"></a><a name="p65842410163959"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53.839999999999996%" headers="mcps1.1.5.1.4 "><p id="p31634993163959"><a name="p31634993163959"></a><a name="p31634993163959"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b7552195915014"><a name="b7552195915014"></a><a name="b7552195915014"></a>true</strong> or <strong id="b655375935016"><a name="b655375935016"></a><a name="b655375935016"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section38241653113834"></a>

-   Example request

    ```
    POST /v2.0/dcaas/virtual-interfaces
    {
        "virtual_interface" : {
            "name" : "virtual interface1",
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


-   Example response

    ```
    {
        "virtual_interface" : {
            "id" : "67c59cf4-1a64-46c7-763f-22eb1b9e8986",  
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual interface1",
            "admin_state_up": true, 
            "description" : "",
            "direct_connect_id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
            "vgw_id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389",
            "type" : "private",
            "status": "PENDING_CREATE", 
            "bgp_md5": ""
            "service_type" : "vpc",
            "vlan" : 100,
            "bandwidth" : 10,
            "create_time": "2018-10-19 09:53:50.335431",
            "bgp_asn": null, 
            "service_ep_group_id": null,
            "delete_time": "None", 
            "local_gateway_v4_ip" : "180.1.1.1/24",
            "remote_gateway_v4_ip"  : "180.1.1.2/24",
            "route_mode"  : "static",
            "remote_ep_group_id" : "78e34cf1-5468-87c7-223d-56e78b9699ef"
            "rate_limit": false
        }
    }
    ```


## Response code<a name="section3380319173341"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

