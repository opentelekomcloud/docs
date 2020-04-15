# Creating an IPsec VPN Connection<a name="en_topic_0093011492"></a>

## **Function**<a name="section36453319"></a>

This interface is used to create an IPsec VPN connection.

## URI<a name="ole_link140"></a>

POST /v2.0/vpn/ipsec-site-connections

## Request Message<a name="section66468500"></a>

[Table 1](#table64761989)  lists the request parameters for creating an IPsec site connection.

**Table  1**  Request parameters

<a name="table64761989"></a>
<table><thead align="left"><tr id="row3648444"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p27088563"><a name="p27088563"></a><a name="p27088563"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p46690023"><a name="p46690023"></a><a name="p46690023"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p23795519"><a name="p23795519"></a><a name="p23795519"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p48388900"><a name="p48388900"></a><a name="p48388900"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27186813"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54648243"><a name="p54648243"></a><a name="p54648243"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p64431533"><a name="p64431533"></a><a name="p64431533"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51571667"><a name="p51571667"></a><a name="p51571667"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p16555535"><a name="p16555535"></a><a name="p16555535"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row51369462"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p176855"><a name="p176855"></a><a name="p176855"></a>local_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p14325289"><a name="p14325289"></a><a name="p14325289"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19497747"><a name="p19497747"></a><a name="p19497747"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p35813694"><a name="p35813694"></a><a name="p35813694"></a>Specifies the ID of the external gateway address of a virtual router.</p>
</td>
</tr>
<tr id="row53887795"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2835298"><a name="p2835298"></a><a name="p2835298"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p28332581"><a name="p28332581"></a><a name="p28332581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p13237733"><a name="p13237733"></a><a name="p13237733"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65623433"><a name="p65623433"></a><a name="p65623433"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row53739988"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p57971786"><a name="p57971786"></a><a name="p57971786"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p65203096"><a name="p65203096"></a><a name="p65203096"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p46959463"><a name="p46959463"></a><a name="p46959463"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p45620191"><a name="p45620191"></a><a name="p45620191"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row7928537"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38231776"><a name="p38231776"></a><a name="p38231776"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9766180"><a name="p9766180"></a><a name="p9766180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p52863116"><a name="p52863116"></a><a name="p52863116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p54054017"><a name="p54054017"></a><a name="p54054017"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row16724107"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12475454"><a name="p12475454"></a><a name="p12475454"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3878833"><a name="p3878833"></a><a name="p3878833"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p45750028"><a name="p45750028"></a><a name="p45750028"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p14764792"><a name="p14764792"></a><a name="p14764792"></a>Specifies the administrative status. The value can be <strong id="b842352706221557_1"><a name="b842352706221557_1"></a><a name="b842352706221557_1"></a>true</strong> or <strong id="b84235270622160_1"><a name="b84235270622160_1"></a><a name="b84235270622160_1"></a>false</strong>.</p>
</td>
</tr>
<tr id="row65774268"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26115459"><a name="p26115459"></a><a name="p26115459"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p34977455"><a name="p34977455"></a><a name="p34977455"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p14601640"><a name="p14601640"></a><a name="p14601640"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p41882197"><a name="p41882197"></a><a name="p41882197"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row41395459"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p64697882"><a name="p64697882"></a><a name="p64697882"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p6037081"><a name="p6037081"></a><a name="p6037081"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19241577"><a name="p19241577"></a><a name="p19241577"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15063922"><a name="p15063922"></a><a name="p15063922"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row1357571"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42854387"><a name="p42854387"></a><a name="p42854387"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p48653295"><a name="p48653295"></a><a name="p48653295"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p48602848"><a name="p48602848"></a><a name="p48602848"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44516654"><a name="p44516654"></a><a name="p44516654"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row65105571"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p39059911"><a name="p39059911"></a><a name="p39059911"></a>vpnservice_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9736186"><a name="p9736186"></a><a name="p9736186"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p50433639"><a name="p50433639"></a><a name="p50433639"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p58592948"><a name="p58592948"></a><a name="p58592948"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row57574486"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33021783"><a name="p33021783"></a><a name="p33021783"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57518732"><a name="p57518732"></a><a name="p57518732"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28505693"><a name="p28505693"></a><a name="p28505693"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p27259828"><a name="p27259828"></a><a name="p27259828"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row44011860"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p8190892"><a name="p8190892"></a><a name="p8190892"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p59482492"><a name="p59482492"></a><a name="p59482492"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p53352557"><a name="p53352557"></a><a name="p53352557"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p26589862"><a name="p26589862"></a><a name="p26589862"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row37982174"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56657239"><a name="p56657239"></a><a name="p56657239"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p25833645"><a name="p25833645"></a><a name="p25833645"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12150471"><a name="p12150471"></a><a name="p12150471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44664077"><a name="p44664077"></a><a name="p44664077"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row66432381"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12313777"><a name="p12313777"></a><a name="p12313777"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57891910"><a name="p57891910"></a><a name="p57891910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p58733156"><a name="p58733156"></a><a name="p58733156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p59765170"><a name="p59765170"></a><a name="p59765170"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
<tr id="row1015618"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p15156252"><a name="p15156252"></a><a name="p15156252"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p19696890"><a name="p19696890"></a><a name="p19696890"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51944261"><a name="p51944261"></a><a name="p51944261"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46735588"><a name="p46735588"></a><a name="p46735588"></a>Provides supplementary information about the IPsec VPN connection.</p>
</td>
</tr>
<tr id="row51151019"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49591885"><a name="p49591885"></a><a name="p49591885"></a>auth_mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57519772"><a name="p57519772"></a><a name="p57519772"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28589951"><a name="p28589951"></a><a name="p28589951"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34084703"><a name="p34084703"></a><a name="p34084703"></a>Specifies the authentication mode. The default value is <strong id="b84235270616111_1"><a name="b84235270616111_1"></a><a name="b84235270616111_1"></a>psk</strong>.</p>
</td>
</tr>
<tr id="row38326873"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17468990"><a name="p17468990"></a><a name="p17468990"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5702100"><a name="p5702100"></a><a name="p5702100"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59216962"><a name="p59216962"></a><a name="p59216962"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31844657"><a name="p31844657"></a><a name="p31844657"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i842352697222235_1"><a name="i842352697222235_1"></a><a name="i842352697222235_1"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row18166465"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62197523"><a name="p62197523"></a><a name="p62197523"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p4834618"><a name="p4834618"></a><a name="p4834618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p56059806"><a name="p56059806"></a><a name="p56059806"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44550438"><a name="p44550438"></a><a name="p44550438"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**,  **peer\_id**,  **dpd**, and  **local\_id**  parameters are not supported.  
>2.  The value of  **tenant\_id**  can contain a maximum of 255 characters.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters. This parameter has been used by internal components, and you are not allowed to configure the parameter.  
>5.  The value of  **peer\_address**  can contain a maximum of 250 characters.  
>6.  The value of  **peer\_id**  can contain a maximum of 250 characters and is unconfigurable.  
>7.  The  **route\_mode**  parameter cannot be configured. The default value is  **static**.  
>8.  The value of  **mtu**  can only be  **1500**.  
>9.  The value of  **initiator**  can only be  **bi-directional**.  
>10. The value of  **auth\_mode**  can only be  **psk**.  
>11. The value of  **admin\_state\_up**  can only be  **true**.  
>12. A PSK can contain 6 to 128 characters. Spaces and question marks \(?\) are not allowed in a PSK. The PSK cannot contain only asterisks \(\*\).  
>13. To enable two IPsec connections to work in active/standby mode, the  **local\_ep\_group\_id**  and  **peer\_ep\_group\_id**  parameters of the active and standby connections must be set to the same value. If the parameter values are different and the  **local\_ep\_group**  and  **peer\_ep\_group**  values are different, the connection cannot work in active/standby mode.  

## Response Message<a name="section61345590"></a>

[Table 2](#table60218927)  describes the response parameters.

**Table  2**  Response parameters

<a name="table60218927"></a>
<table><thead align="left"><tr id="row60011123"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p29062812"><a name="p29062812"></a><a name="p29062812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p5277541"><a name="p5277541"></a><a name="p5277541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p64881656"><a name="p64881656"></a><a name="p64881656"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38551324"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p35649520"><a name="p35649520"></a><a name="p35649520"></a>interval</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1930001"><a name="p1930001"></a><a name="p1930001"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p46270551"><a name="p46270551"></a><a name="p46270551"></a>Specifies the DPD interval in seconds. The default value is <strong id="b460615530142328"><a name="b460615530142328"></a><a name="b460615530142328"></a>30</strong>.</p>
</td>
</tr>
<tr id="row13781782"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42582590"><a name="p42582590"></a><a name="p42582590"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26637750"><a name="p26637750"></a><a name="p26637750"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18797239"><a name="p18797239"></a><a name="p18797239"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row34957427"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12979352"><a name="p12979352"></a><a name="p12979352"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44694577"><a name="p44694577"></a><a name="p44694577"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42495969"><a name="p42495969"></a><a name="p42495969"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row46919403"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42375303"><a name="p42375303"></a><a name="p42375303"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9847515"><a name="p9847515"></a><a name="p9847515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50824398"><a name="p50824398"></a><a name="p50824398"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row54766399"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6893340"><a name="p6893340"></a><a name="p6893340"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p21489686"><a name="p21489686"></a><a name="p21489686"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65217919"><a name="p65217919"></a><a name="p65217919"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row50090360"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30787377"><a name="p30787377"></a><a name="p30787377"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10749578"><a name="p10749578"></a><a name="p10749578"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63674173"><a name="p63674173"></a><a name="p63674173"></a>Specifies the administrative status. The value can be <strong id="b842352706221557_3"><a name="b842352706221557_3"></a><a name="b842352706221557_3"></a>true</strong> or <strong id="b84235270622160_3"><a name="b84235270622160_3"></a><a name="b84235270622160_3"></a>false</strong>.</p>
</td>
</tr>
<tr id="row36196647"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p46247333"><a name="p46247333"></a><a name="p46247333"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55046503"><a name="p55046503"></a><a name="p55046503"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p47314137"><a name="p47314137"></a><a name="p47314137"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row23174054"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65159075"><a name="p65159075"></a><a name="p65159075"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p43393704"><a name="p43393704"></a><a name="p43393704"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30295276"><a name="p30295276"></a><a name="p30295276"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row4222036"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6440667"><a name="p6440667"></a><a name="p6440667"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51931981"><a name="p51931981"></a><a name="p51931981"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14029336"><a name="p14029336"></a><a name="p14029336"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row59155164"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26838981"><a name="p26838981"></a><a name="p26838981"></a>vpnservice_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26473887"><a name="p26473887"></a><a name="p26473887"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17438021"><a name="p17438021"></a><a name="p17438021"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row22724462"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28742116"><a name="p28742116"></a><a name="p28742116"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46410096"><a name="p46410096"></a><a name="p46410096"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23724515"><a name="p23724515"></a><a name="p23724515"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row12194051"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48194049"><a name="p48194049"></a><a name="p48194049"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11403863"><a name="p11403863"></a><a name="p11403863"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61473837"><a name="p61473837"></a><a name="p61473837"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row16393628"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52815467"><a name="p52815467"></a><a name="p52815467"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50194423"><a name="p50194423"></a><a name="p50194423"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22413667"><a name="p22413667"></a><a name="p22413667"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row396418"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p32109884"><a name="p32109884"></a><a name="p32109884"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50763831"><a name="p50763831"></a><a name="p50763831"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p207374"><a name="p207374"></a><a name="p207374"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
<tr id="row1866374"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16958614"><a name="p16958614"></a><a name="p16958614"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31470474"><a name="p31470474"></a><a name="p31470474"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50916928"><a name="p50916928"></a><a name="p50916928"></a>Provides supplementary information about the IPsec VPN connection.</p>
</td>
</tr>
<tr id="row918101"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7257357"><a name="p7257357"></a><a name="p7257357"></a>auth_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50975058"><a name="p50975058"></a><a name="p50975058"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43888289"><a name="p43888289"></a><a name="p43888289"></a>Specifies the authentication mode. The default value is <strong id="b84235270616111_3"><a name="b84235270616111_3"></a><a name="b84235270616111_3"></a>psk</strong>.</p>
</td>
</tr>
<tr id="row59450282"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50743509"><a name="p50743509"></a><a name="p50743509"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16583569"><a name="p16583569"></a><a name="p16583569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p21330650"><a name="p21330650"></a><a name="p21330650"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
<tr id="row57758128"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47896825"><a name="p47896825"></a><a name="p47896825"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54437622"><a name="p54437622"></a><a name="p54437622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11868462"><a name="p11868462"></a><a name="p11868462"></a>Specifies the route advertising mode. The default value is <strong id="b409160175141644"><a name="b409160175141644"></a><a name="b409160175141644"></a>static</strong>.</p>
</td>
</tr>
<tr id="row39707298"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62174594"><a name="p62174594"></a><a name="p62174594"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2977371"><a name="p2977371"></a><a name="p2977371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5852437"><a name="p5852437"></a><a name="p5852437"></a>Specifies the IPsec VPN connection status. The value can be <strong id="b842352706164927"><a name="b842352706164927"></a><a name="b842352706164927"></a>ACTIVE</strong>, <strong id="b842352706164931"><a name="b842352706164931"></a><a name="b842352706164931"></a>DOWN</strong>, <strong id="b842352706164935"><a name="b842352706164935"></a><a name="b842352706164935"></a>BUILD</strong>, <strong id="b842352706164939"><a name="b842352706164939"></a><a name="b842352706164939"></a>ERROR</strong>, <strong id="b842352706164943"><a name="b842352706164943"></a><a name="b842352706164943"></a>PENDING_CREATE</strong>, <strong id="b842352706164948"><a name="b842352706164948"></a><a name="b842352706164948"></a>PENDING_UPDATE</strong>, or <strong id="b84235270616508"><a name="b84235270616508"></a><a name="b84235270616508"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row52671936"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38568449"><a name="p38568449"></a><a name="p38568449"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p37036703"><a name="p37036703"></a><a name="p37036703"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63724816"><a name="p63724816"></a><a name="p63724816"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i842352697222235_3"><a name="i842352697222235_3"></a><a name="i842352697222235_3"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row36652435"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16057296"><a name="p16057296"></a><a name="p16057296"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25572589"><a name="p25572589"></a><a name="p25572589"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9598184"><a name="p9598184"></a><a name="p9598184"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row19274797"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17754702"><a name="p17754702"></a><a name="p17754702"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28844789"><a name="p28844789"></a><a name="p28844789"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3664366"><a name="p3664366"></a><a name="p3664366"></a>Specifies the DPD timeout. The default value is 120 seconds.</p>
</td>
</tr>
<tr id="row32979301"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54077734"><a name="p54077734"></a><a name="p54077734"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18220335"><a name="p18220335"></a><a name="p18220335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22737212"><a name="p22737212"></a><a name="p22737212"></a>Specifies the DPD action. The value can be <strong id="b842352706165431"><a name="b842352706165431"></a><a name="b842352706165431"></a>clear</strong>, <strong id="b842352706165434"><a name="b842352706165434"></a><a name="b842352706165434"></a>hold</strong>, <strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>restart</strong>, <strong id="b842352706165443"><a name="b842352706165443"></a><a name="b842352706165443"></a>disabled</strong>, or <strong id="b842352706165447"><a name="b842352706165447"></a><a name="b842352706165447"></a>restart-by-peer</strong>. The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>hold</strong>.</p>
</td>
</tr>
<tr id="row176301621514"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p4619410115112"><a name="p4619410115112"></a><a name="p4619410115112"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1863112125111"><a name="p1863112125111"></a><a name="p1863112125111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8631142135117"><a name="p8631142135117"></a><a name="p8631142135117"></a>Specifies the time when the IPsec connection was created.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section15239399"></a>

-   Example Request

    ```
    POST /v2.0/vpn/ipsec-site-connections
    {
      "ipsec_site_connection" : {
        "psk" : "secret",
        "initiator" : "bi-directional",
        "ipsecpolicy_id" : "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
        "admin_state_up" : true,
        "mtu" : 1500,
        "peer_ep_group_id" : "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
        "ikepolicy_id" : "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
        "vpnservice_id" : "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
        "local_ep_group_id" : "3e1815dd-e212-43d0-8f13-b494fa553e68",
        "peer_address" : "172.24.4.233",
        "peer_id" : "172.24.4.233",
        "name" : "vpnconnection1"
      }
    }
    ```


-   Example Response

    ```
    {
      "ipsec_site_connection" : {
        "status" : "PENDING_CREATE",
        "psk" : "secret",
        "initiator" : "bi-directional",
        "name" : "vpnconnection1",
        "admin_state_up" : true,
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
        "vpnservice_id": "4754261f-f8c5-4799-a365-78b2e682e38a",
        "ipsecpolicy_id" : "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
        "local_ep_group_id" : "3e1815dd-e212-43d0-8f13-b494fa553e68",
        "peer_address" : "172.24.4.233",
        "created_at": "2018-11-03 14:24:33.749714",
        "peer_id" : "172.24.4.233",
        "id" : "851f280f-5639-4ea3-81aa-e298525ab74b",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section26431778"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

