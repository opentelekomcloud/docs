# Updating an IPsec VPN Connection<a name="en_topic_0093011495"></a>

## **Function**<a name="section55622396"></a>

This interface is used to update an IPsec VPN connection.

## URI<a name="section30839519"></a>

PUT /v2.0/vpn/ipsec-site-connections/\{connection\_id\}

**Table  1**  Parameter description

<a name="table9861172982416"></a>
<table><thead align="left"><tr id="row19884629102416"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p3884192972412"><a name="p3884192972412"></a><a name="p3884192972412"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p13893112952410"><a name="p13893112952410"></a><a name="p13893112952410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p49011329112410"><a name="p49011329112410"></a><a name="p49011329112410"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1490112914244"><a name="p1490112914244"></a><a name="p1490112914244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row139091529142413"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p990917292242"><a name="p990917292242"></a><a name="p990917292242"></a>connection_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1390982912240"><a name="p1390982912240"></a><a name="p1390982912240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12917112917246"><a name="p12917112917246"></a><a name="p12917112917246"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p79171129172411"><a name="p79171129172411"></a><a name="p79171129172411"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section14973148"></a>

[Table 2](#table38559395)  describes the request parameters.

**Table  2**  Request parameters

<a name="table38559395"></a>
<table><thead align="left"><tr id="row16046317"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p24683273"><a name="p24683273"></a><a name="p24683273"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p53188122"><a name="p53188122"></a><a name="p53188122"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p13270664"><a name="p13270664"></a><a name="p13270664"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1182010"><a name="p1182010"></a><a name="p1182010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32355065"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3514615"><a name="p3514615"></a><a name="p3514615"></a>ipsec_site_connection</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p16248438"><a name="p16248438"></a><a name="p16248438"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p41055134"><a name="p41055134"></a><a name="p41055134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37131542"><a name="p37131542"></a><a name="p37131542"></a>Specifies the IPsec VPN connection object.</p>
</td>
</tr>
<tr id="row65748423"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24022075"><a name="p24022075"></a><a name="p24022075"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p66739923"><a name="p66739923"></a><a name="p66739923"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37224696"><a name="p37224696"></a><a name="p37224696"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p62410385"><a name="p62410385"></a><a name="p62410385"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row24822557"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p64470080"><a name="p64470080"></a><a name="p64470080"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p54693963"><a name="p54693963"></a><a name="p54693963"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1026023"><a name="p1026023"></a><a name="p1026023"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15999035"><a name="p15999035"></a><a name="p15999035"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row9773594"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53463670"><a name="p53463670"></a><a name="p53463670"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35590047"><a name="p35590047"></a><a name="p35590047"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64221564"><a name="p64221564"></a><a name="p64221564"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34564214"><a name="p34564214"></a><a name="p34564214"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row42642473"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p31488280"><a name="p31488280"></a><a name="p31488280"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p413912"><a name="p413912"></a><a name="p413912"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p33526929"><a name="p33526929"></a><a name="p33526929"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31326698"><a name="p31326698"></a><a name="p31326698"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong> or <strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row13504826"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20149094"><a name="p20149094"></a><a name="p20149094"></a>interval</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p21463943"><a name="p21463943"></a><a name="p21463943"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60857861"><a name="p60857861"></a><a name="p60857861"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30539719"><a name="p30539719"></a><a name="p30539719"></a>Specifies the DPD interval in seconds. The default value is <strong id="b460615530142328"><a name="b460615530142328"></a><a name="b460615530142328"></a>30</strong>.</p>
</td>
</tr>
<tr id="row6422022"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50421737"><a name="p50421737"></a><a name="p50421737"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57628934"><a name="p57628934"></a><a name="p57628934"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37432067"><a name="p37432067"></a><a name="p37432067"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p12098568"><a name="p12098568"></a><a name="p12098568"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i842352697222235"><a name="i842352697222235"></a><a name="i842352697222235"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row41778254"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p28595379"><a name="p28595379"></a><a name="p28595379"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p34524340"><a name="p34524340"></a><a name="p34524340"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p45008187"><a name="p45008187"></a><a name="p45008187"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p21784493"><a name="p21784493"></a><a name="p21784493"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row61842715"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43203995"><a name="p43203995"></a><a name="p43203995"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9862716"><a name="p9862716"></a><a name="p9862716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60682533"><a name="p60682533"></a><a name="p60682533"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p16338175"><a name="p16338175"></a><a name="p16338175"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row12825854"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32261252"><a name="p32261252"></a><a name="p32261252"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p63024590"><a name="p63024590"></a><a name="p63024590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p4718148"><a name="p4718148"></a><a name="p4718148"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46625744"><a name="p46625744"></a><a name="p46625744"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row16978512"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33082261"><a name="p33082261"></a><a name="p33082261"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p62417507"><a name="p62417507"></a><a name="p62417507"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p22653281"><a name="p22653281"></a><a name="p22653281"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p22976439"><a name="p22976439"></a><a name="p22976439"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row5461363"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p39717249"><a name="p39717249"></a><a name="p39717249"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p62980604"><a name="p62980604"></a><a name="p62980604"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1155275"><a name="p1155275"></a><a name="p1155275"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p26468439"><a name="p26468439"></a><a name="p26468439"></a>Specifies the DPD timeout. The default value is 120 seconds.</p>
</td>
</tr>
<tr id="row36889359"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p35248064"><a name="p35248064"></a><a name="p35248064"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5405340"><a name="p5405340"></a><a name="p5405340"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p35179415"><a name="p35179415"></a><a name="p35179415"></a>Specifies the DPD action. The value can be <strong id="b842352706165431"><a name="b842352706165431"></a><a name="b842352706165431"></a>clear</strong>, <strong id="b842352706165434"><a name="b842352706165434"></a><a name="b842352706165434"></a>hold</strong>, <strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>restart</strong>, <strong id="b842352706165443"><a name="b842352706165443"></a><a name="b842352706165443"></a>disabled</strong>, or <strong id="b842352706165447"><a name="b842352706165447"></a><a name="b842352706165447"></a>restart-by-peer</strong>. The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>hold</strong>.</p>
</td>
</tr>
<tr id="row48179284"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10207955"><a name="p10207955"></a><a name="p10207955"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p21538022"><a name="p21538022"></a><a name="p21538022"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p66858230"><a name="p66858230"></a><a name="p66858230"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46807530"><a name="p46807530"></a><a name="p46807530"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row18614589"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p31386755"><a name="p31386755"></a><a name="p31386755"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p59299233"><a name="p59299233"></a><a name="p59299233"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p38508608"><a name="p38508608"></a><a name="p38508608"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p32189576"><a name="p32189576"></a><a name="p32189576"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row21270730"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p45207585"><a name="p45207585"></a><a name="p45207585"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p37935797"><a name="p37935797"></a><a name="p37935797"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p52900717"><a name="p52900717"></a><a name="p52900717"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p57099698"><a name="p57099698"></a><a name="p57099698"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**,  **peer\_id**,  **dpd**, and  **local\_id**  parameters are not supported.  
>2.  The  **connection\_id**  parameter must be specified.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters. This parameter has been used by internal components, and you are not allowed to configure the parameter.  
>5.  The value of  **peer\_address**  can contain a maximum of 250 characters.  
>6.  The value of  **peer\_id**  can contain a maximum of 250 characters and is unconfigurable.  
>7.  The value of  **mtu**  can only be  **1500**.  
>8.  The value of  **initiator**  can only be  **bi-directional**.  
>9.  The value of  **admin\_state\_up**  can only be  **true**.  
>10. A PSK can contain 6 to 128 characters. Spaces and question marks \(?\) are not allowed in a PSK. The PSK cannot contain only asterisks \(\*\).  

## Response Message<a name="section540607"></a>

[Table 3](#table23987813)  describes the response parameters.

**Table  3**  Response parameters

<a name="table23987813"></a>
<table><thead align="left"><tr id="row32303446"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p66442352"><a name="p66442352"></a><a name="p66442352"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p13121422"><a name="p13121422"></a><a name="p13121422"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p56089592"><a name="p56089592"></a><a name="p56089592"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46963092"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45914068"><a name="p45914068"></a><a name="p45914068"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28052000"><a name="p28052000"></a><a name="p28052000"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36672255"><a name="p36672255"></a><a name="p36672255"></a>Specifies the IPsec VPN connection status. The value can be <strong id="b842352706164927"><a name="b842352706164927"></a><a name="b842352706164927"></a>ACTIVE</strong>, <strong id="b842352706164931"><a name="b842352706164931"></a><a name="b842352706164931"></a>DOWN</strong>, <strong id="b842352706164935"><a name="b842352706164935"></a><a name="b842352706164935"></a>BUILD</strong>, <strong id="b842352706164939"><a name="b842352706164939"></a><a name="b842352706164939"></a>ERROR</strong>, <strong id="b842352706164943"><a name="b842352706164943"></a><a name="b842352706164943"></a>PENDING_CREATE</strong>, <strong id="b842352706164948"><a name="b842352706164948"></a><a name="b842352706164948"></a>PENDING_UPDATE</strong>, or <strong id="b84235270616508"><a name="b84235270616508"></a><a name="b84235270616508"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row61614844"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24746480"><a name="p24746480"></a><a name="p24746480"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58307827"><a name="p58307827"></a><a name="p58307827"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37134413"><a name="p37134413"></a><a name="p37134413"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row65774263"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26115080"><a name="p26115080"></a><a name="p26115080"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34946701"><a name="p34946701"></a><a name="p34946701"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41427285"><a name="p41427285"></a><a name="p41427285"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row37301245"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1501989"><a name="p1501989"></a><a name="p1501989"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54552261"><a name="p54552261"></a><a name="p54552261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25816719"><a name="p25816719"></a><a name="p25816719"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
<tr id="row31023887"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29906904"><a name="p29906904"></a><a name="p29906904"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p6540158"><a name="p6540158"></a><a name="p6540158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27413374"><a name="p27413374"></a><a name="p27413374"></a>Specifies the administrative status. The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
<tr id="row45393782"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53017722"><a name="p53017722"></a><a name="p53017722"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p66577119"><a name="p66577119"></a><a name="p66577119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p887019"><a name="p887019"></a><a name="p887019"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row7983171"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42657133"><a name="p42657133"></a><a name="p42657133"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32675739"><a name="p32675739"></a><a name="p32675739"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39815461"><a name="p39815461"></a><a name="p39815461"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row22794832"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34442073"><a name="p34442073"></a><a name="p34442073"></a>auth_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38344490"><a name="p38344490"></a><a name="p38344490"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54179398"><a name="p54179398"></a><a name="p54179398"></a>Specifies the authentication mode. The default value is <strong id="b84235270616111"><a name="b84235270616111"></a><a name="b84235270616111"></a>psk</strong>.</p>
</td>
</tr>
<tr id="row17852540"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36769646"><a name="p36769646"></a><a name="p36769646"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25551373"><a name="p25551373"></a><a name="p25551373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4618864"><a name="p4618864"></a><a name="p4618864"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i1708920422"><a name="i1708920422"></a><a name="i1708920422"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row41569778"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11708839"><a name="p11708839"></a><a name="p11708839"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8891917"><a name="p8891917"></a><a name="p8891917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22268426"><a name="p22268426"></a><a name="p22268426"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row66198114"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p60446980"><a name="p60446980"></a><a name="p60446980"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64367227"><a name="p64367227"></a><a name="p64367227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p64409607"><a name="p64409607"></a><a name="p64409607"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row42815556"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45508046"><a name="p45508046"></a><a name="p45508046"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62273137"><a name="p62273137"></a><a name="p62273137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15289375"><a name="p15289375"></a><a name="p15289375"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row3386651"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5883351"><a name="p5883351"></a><a name="p5883351"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17381814465"><a name="p17381814465"></a><a name="p17381814465"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52015891"><a name="p52015891"></a><a name="p52015891"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row65489840"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3076790"><a name="p3076790"></a><a name="p3076790"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47893437"><a name="p47893437"></a><a name="p47893437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25141484"><a name="p25141484"></a><a name="p25141484"></a>Specifies the route advertising mode. The default value is <strong id="b409160175141644"><a name="b409160175141644"></a><a name="b409160175141644"></a>static</strong>.</p>
</td>
</tr>
<tr id="row24946770"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7422478"><a name="p7422478"></a><a name="p7422478"></a>vpnservice_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64349806"><a name="p64349806"></a><a name="p64349806"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17214779"><a name="p17214779"></a><a name="p17214779"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row20715291"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p217030"><a name="p217030"></a><a name="p217030"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17579482"><a name="p17579482"></a><a name="p17579482"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45953370"><a name="p45953370"></a><a name="p45953370"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row10927149"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12683857"><a name="p12683857"></a><a name="p12683857"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p20759490"><a name="p20759490"></a><a name="p20759490"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39129256"><a name="p39129256"></a><a name="p39129256"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row16618991"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3961063"><a name="p3961063"></a><a name="p3961063"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52410671"><a name="p52410671"></a><a name="p52410671"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p594640"><a name="p594640"></a><a name="p594640"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row5351764"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30839753"><a name="p30839753"></a><a name="p30839753"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14992050"><a name="p14992050"></a><a name="p14992050"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48357378"><a name="p48357378"></a><a name="p48357378"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
<tr id="row32563220"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20375168"><a name="p20375168"></a><a name="p20375168"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p39775908"><a name="p39775908"></a><a name="p39775908"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50474807"><a name="p50474807"></a><a name="p50474807"></a>Provides supplementary information about the IPsec VPN connection.</p>
</td>
</tr>
<tr id="row51620080"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20476957"><a name="p20476957"></a><a name="p20476957"></a>ipsec_site_connection</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48020839"><a name="p48020839"></a><a name="p48020839"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55719536"><a name="p55719536"></a><a name="p55719536"></a>Specifies the IPsec VPN connection object.</p>
</td>
</tr>
<tr id="row31713777"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18679162"><a name="p18679162"></a><a name="p18679162"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36617123"><a name="p36617123"></a><a name="p36617123"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p62319862"><a name="p62319862"></a><a name="p62319862"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row24007848"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65587574"><a name="p65587574"></a><a name="p65587574"></a>interval</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10993288"><a name="p10993288"></a><a name="p10993288"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52047770"><a name="p52047770"></a><a name="p52047770"></a>Specifies the DPD interval in seconds. The default value is <strong id="b540152244"><a name="b540152244"></a><a name="b540152244"></a>30</strong>.</p>
</td>
</tr>
<tr id="row65776751"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26316604"><a name="p26316604"></a><a name="p26316604"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51270161"><a name="p51270161"></a><a name="p51270161"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33904373"><a name="p33904373"></a><a name="p33904373"></a>Specifies the DPD timeout. The default value is 120 seconds.</p>
</td>
</tr>
<tr id="row36703909"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="_GoBack"><a name="_GoBack"></a><a name="_GoBack"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27748670"><a name="p27748670"></a><a name="p27748670"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59789225"><a name="p59789225"></a><a name="p59789225"></a>Specifies the DPD action. The value can be <strong id="b650049411"><a name="b650049411"></a><a name="b650049411"></a>clear</strong>, <strong id="b1377281285"><a name="b1377281285"></a><a name="b1377281285"></a>hold</strong>, <strong id="b226805162"><a name="b226805162"></a><a name="b226805162"></a>restart</strong>, <strong id="b1092009837"><a name="b1092009837"></a><a name="b1092009837"></a>disabled</strong>, or <strong id="b1560212833"><a name="b1560212833"></a><a name="b1560212833"></a>restart-by-peer</strong>. The default value is <strong id="b798414169"><a name="b798414169"></a><a name="b798414169"></a>hold</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section4865465"></a>

-   Example Request

    ```
    PUT /v2.0/vpn/ipsec-site-connections/{connection_id}
    {
      "ipsec_site_connection" : {
        "mtu" : 1200,
      }
    }
    ```


-   Example Response

    ```
    {
        "ipsec_site_connection": {
            "status": "DOWN",
            "psk": "secret",
            "initiator": "bi-directional",
            "name": "vpnconnection1",
            "admin_state_up": true,
            "project_id": "10039663455a446d8ba2cbb058b0f578",
            "tenant_id": "10039663455a446d8ba2cbb058b0f578",
            "auth_mode": "psk",
            "peer_cidrs": [],
            "mtu": 1200,
            "peer_ep_group_id": "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
            "ikepolicy_id": "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
            "vpnservice_id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
            "dpd": {
                "action": "hold",
                "interval": 30,
                "timeout": 120
            },
            "route_mode": "static",
            "ipsecpolicy_id": "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
            "local_ep_group_id": "3e1815dd-e212-43d0-8f13-b494fa553e68",
            "peer_address": "172.24.4.233",
            "peer_id": "172.24.4.233",
            "id": "851f280f-5639-4ea3-81aa-e298525ab74b",
            "description": "New description"
        }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

