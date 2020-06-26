# Querying IPsec VPN Connections<a name="en_topic_0093011494"></a>

## **Function**<a name="section23308753"></a>

This interface is used to query IPsec VPN connections.

## URI<a name="ole_link144"></a>

GET /v2.0/vpn/ipsec-site-connections

## Request Message<a name="section13538688"></a>

[Table 1](#table56415606)  describes the request parameters.

**Table  1**  Request parameters

<a name="table56415606"></a>
<table><thead align="left"><tr id="row24881480"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2134014"><a name="p2134014"></a><a name="p2134014"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p38637452"><a name="p38637452"></a><a name="p38637452"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p42625947"><a name="p42625947"></a><a name="p42625947"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p30149715"><a name="p30149715"></a><a name="p30149715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26207835"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42459867"><a name="p42459867"></a><a name="p42459867"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p16697212"><a name="p16697212"></a><a name="p16697212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p10296933"><a name="p10296933"></a><a name="p10296933"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28745279"><a name="p28745279"></a><a name="p28745279"></a>Controls which parameters are returned. If this parameter is not specified, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>The  **project\_id**, **peer\_id**, **dpd**, and **local\_id**  parameters are not supported.  

## Response Message<a name="section54739329"></a>

[Table 2](#table46666290)  describes the response parameters.

**Table  2**  Response parameters

<a name="table46666290"></a>
<table><thead align="left"><tr id="row8970000"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p55481367"><a name="p55481367"></a><a name="p55481367"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p64805763"><a name="p64805763"></a><a name="p64805763"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p55963561"><a name="p55963561"></a><a name="p55963561"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36754611"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24333505"><a name="p24333505"></a><a name="p24333505"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24856892"><a name="p24856892"></a><a name="p24856892"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11530135"><a name="p11530135"></a><a name="p11530135"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i842352697222235"><a name="i842352697222235"></a><a name="i842352697222235"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row36662351"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16860416"><a name="p16860416"></a><a name="p16860416"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23516450"><a name="p23516450"></a><a name="p23516450"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8152279"><a name="p8152279"></a><a name="p8152279"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row6261652"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p37431827"><a name="p37431827"></a><a name="p37431827"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12079142"><a name="p12079142"></a><a name="p12079142"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p62795050"><a name="p62795050"></a><a name="p62795050"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row28284541"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9346499"><a name="p9346499"></a><a name="p9346499"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18868961"><a name="p18868961"></a><a name="p18868961"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50514376"><a name="p50514376"></a><a name="p50514376"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row51976202"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49322849"><a name="p49322849"></a><a name="p49322849"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35727861"><a name="p35727861"></a><a name="p35727861"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p66346226"><a name="p66346226"></a><a name="p66346226"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row60245124"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48016903"><a name="p48016903"></a><a name="p48016903"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64163914"><a name="p64163914"></a><a name="p64163914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5536817"><a name="p5536817"></a><a name="p5536817"></a>Specifies the route advertising mode. The default value is <strong id="b409160175141644"><a name="b409160175141644"></a><a name="b409160175141644"></a>static</strong>.</p>
</td>
</tr>
<tr id="row49831357"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9808084"><a name="p9808084"></a><a name="p9808084"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p56257360"><a name="p56257360"></a><a name="p56257360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5792918"><a name="p5792918"></a><a name="p5792918"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row52136268"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62288179"><a name="p62288179"></a><a name="p62288179"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12177730"><a name="p12177730"></a><a name="p12177730"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38543611"><a name="p38543611"></a><a name="p38543611"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row11348180"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p46787348"><a name="p46787348"></a><a name="p46787348"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31678816"><a name="p31678816"></a><a name="p31678816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8565311"><a name="p8565311"></a><a name="p8565311"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
<tr id="row9978940"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2987824"><a name="p2987824"></a><a name="p2987824"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40687155"><a name="p40687155"></a><a name="p40687155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p56478093"><a name="p56478093"></a><a name="p56478093"></a>Provides supplementary information about the IPsec VPN connection.</p>
</td>
</tr>
<tr id="row38540791"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34796360"><a name="p34796360"></a><a name="p34796360"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p67041741"><a name="p67041741"></a><a name="p67041741"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29369493"><a name="p29369493"></a><a name="p29369493"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row62998845"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2632805"><a name="p2632805"></a><a name="p2632805"></a>interval</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11930629"><a name="p11930629"></a><a name="p11930629"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27925455"><a name="p27925455"></a><a name="p27925455"></a>Specifies the DPD interval in seconds. The default value is <strong id="b460615530142328"><a name="b460615530142328"></a><a name="b460615530142328"></a>30</strong>.</p>
</td>
</tr>
<tr id="row50002511"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23671576"><a name="p23671576"></a><a name="p23671576"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38349502"><a name="p38349502"></a><a name="p38349502"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19952318"><a name="p19952318"></a><a name="p19952318"></a>Specifies the DPD timeout. The default value is 120 seconds.</p>
</td>
</tr>
<tr id="row45353142"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49725882"><a name="p49725882"></a><a name="p49725882"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1264671"><a name="p1264671"></a><a name="p1264671"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43121195"><a name="p43121195"></a><a name="p43121195"></a>Specifies the DPD action. The value can be <strong id="b842352706165431"><a name="b842352706165431"></a><a name="b842352706165431"></a>clear</strong>,&nbsp;<strong id="b842352706165434"><a name="b842352706165434"></a><a name="b842352706165434"></a>hold</strong>,&nbsp;<strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>restart</strong>,&nbsp;<strong id="b842352706165443"><a name="b842352706165443"></a><a name="b842352706165443"></a>disabled</strong>, or&nbsp;<strong id="b842352706165447"><a name="b842352706165447"></a><a name="b842352706165447"></a>restart-by-peer</strong>. The default value is&nbsp;<strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>hold</strong>.</p>
</td>
</tr>
<tr id="row55687056"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14357657"><a name="p14357657"></a><a name="p14357657"></a>vpnservice_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22119530"><a name="p22119530"></a><a name="p22119530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36875142"><a name="p36875142"></a><a name="p36875142"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row63440828"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38433454"><a name="p38433454"></a><a name="p38433454"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26102093"><a name="p26102093"></a><a name="p26102093"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61122992"><a name="p61122992"></a><a name="p61122992"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row13236018"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65484519"><a name="p65484519"></a><a name="p65484519"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2645837"><a name="p2645837"></a><a name="p2645837"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45253450"><a name="p45253450"></a><a name="p45253450"></a>Specifies the IPsec VPN connection status. The value can be <strong id="b842352706164927"><a name="b842352706164927"></a><a name="b842352706164927"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706164931"><a name="b842352706164931"></a><a name="b842352706164931"></a>DOWN</strong>,&nbsp;<strong id="b842352706164935"><a name="b842352706164935"></a><a name="b842352706164935"></a>BUILD</strong>,&nbsp;<strong id="b842352706164939"><a name="b842352706164939"></a><a name="b842352706164939"></a>ERROR</strong>,&nbsp;<strong id="b842352706164943"><a name="b842352706164943"></a><a name="b842352706164943"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b842352706164948"><a name="b842352706164948"></a><a name="b842352706164948"></a>PENDING_UPDATE</strong>, or&nbsp;<strong id="b84235270616508"><a name="b84235270616508"></a><a name="b84235270616508"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row4627874"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39313476"><a name="p39313476"></a><a name="p39313476"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p30275003"><a name="p30275003"></a><a name="p30275003"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59171655"><a name="p59171655"></a><a name="p59171655"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row62782852"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52246286"><a name="p52246286"></a><a name="p52246286"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4090801"><a name="p4090801"></a><a name="p4090801"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63310175"><a name="p63310175"></a><a name="p63310175"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row32920667"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49328407"><a name="p49328407"></a><a name="p49328407"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36177998"><a name="p36177998"></a><a name="p36177998"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p66906707"><a name="p66906707"></a><a name="p66906707"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
<tr id="row65289456"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53954550"><a name="p53954550"></a><a name="p53954550"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8242429"><a name="p8242429"></a><a name="p8242429"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55943724"><a name="p55943724"></a><a name="p55943724"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row33731474"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47894862"><a name="p47894862"></a><a name="p47894862"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54278574"><a name="p54278574"></a><a name="p54278574"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42092667"><a name="p42092667"></a><a name="p42092667"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row43289691"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18955034"><a name="p18955034"></a><a name="p18955034"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11253402"><a name="p11253402"></a><a name="p11253402"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row34171757"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16448913"><a name="p16448913"></a><a name="p16448913"></a>auth_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p57293570"><a name="p57293570"></a><a name="p57293570"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26365928"><a name="p26365928"></a><a name="p26365928"></a>Specifies the authentication mode. The default value is <strong id="b84235270616111"><a name="b84235270616111"></a><a name="b84235270616111"></a>psk</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section22891915"></a>

```
GET /v2.0/vpn/ipsec-site-connections
```

## Example Response<a name="section4700647"></a>

```
{
  "ipsec_site_connections" : [ {
    "status" : "PENDING CREATE",
    "psk" : "secret",
    "initiator" : "bi-directional",
    "name" : "vpnconnection1",
    "admin_state_up" : true,
    "project_id" : "10039663455a446d8ba2cbb058b0f578",
    "tenant_id" : "10039663455a446d8ba2cbb058b0f578",
    "auth_mode" : "psk",
    "peer_cidrs" : [ ],
    "mtu" : 1500,
    "peer_ep_group_id" : "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
    "ikepolicy_id" : "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
    "vpnservice_id" : "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
    "dpd" : {
      "action" : "hold",
      "interval" : 30,
      "timeout" : 120
    },
    "route_mode" : "static",
    "ipsecpolicy_id" : "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
    "local_ep_group_id" : "3e1815dd-e212-43d0-8f13-b494fa553e68",
    "peer_address" : "172.24.4.226",
    "peer_id" : "172.24.4.226",
    "id" : "851f280f-5639-4ea3-81aa-e298525ab74b",
    "description" : ""
  } ]
}
```

## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

