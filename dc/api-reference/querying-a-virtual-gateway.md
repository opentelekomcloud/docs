# Querying a Virtual Gateway<a name="en-dc_topic_0055025325"></a>

## Function<a name="section17487184"></a>

This API is used to query a virtual gateway.

## URI<a name="section23166934"></a>

GET /v2.0/dcaas/virtual-gateways/\{virtual\_gateway\_id\}

**Table  1**  Parameter description

<a name="table78013327231"></a>
<table><thead align="left"><tr id="row128753217231"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p1587432182316"><a name="p1587432182316"></a><a name="p1587432182316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p1694123232312"><a name="p1694123232312"></a><a name="p1694123232312"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p894632182312"><a name="p894632182312"></a><a name="p894632182312"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p7941332152315"><a name="p7941332152315"></a><a name="p7941332152315"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1994932152311"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p1594203215232"><a name="p1594203215232"></a><a name="p1594203215232"></a>virtual_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p794173252315"><a name="p794173252315"></a><a name="p794173252315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p2103173217239"><a name="p2103173217239"></a><a name="p2103173217239"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p010343252316"><a name="p010343252316"></a><a name="p010343252316"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section64582388"></a>

[Table 2](#table2198437322244)  lists the request parameter.

**Table  2**  Request parameter

<a name="table2198437322244"></a>
<table><thead align="left"><tr id="row4304807922244"><th class="cellrowborder" valign="top" width="23.9%" id="mcps1.2.5.1.1"><p id="p6505580022244"><a name="p6505580022244"></a><a name="p6505580022244"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.09%" id="mcps1.2.5.1.2"><p id="p329696222244"><a name="p329696222244"></a><a name="p329696222244"></a><strong id="b1713129951"><a name="b1713129951"></a><a name="b1713129951"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.64%" id="mcps1.2.5.1.3"><p id="p3257067222244"><a name="p3257067222244"></a><a name="p3257067222244"></a><strong id="b60477892"><a name="b60477892"></a><a name="b60477892"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.370000000000005%" id="mcps1.2.5.1.4"><p id="p5470821922244"><a name="p5470821922244"></a><a name="p5470821922244"></a><strong id="b309779065"><a name="b309779065"></a><a name="b309779065"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5451891922244"><td class="cellrowborder" valign="top" width="23.9%" headers="mcps1.2.5.1.1 "><p id="p5675124985931"><a name="p5675124985931"></a><a name="p5675124985931"></a>virtual_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.2.5.1.2 "><p id="p757920222316"><a name="p757920222316"></a><a name="p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.5.1.3 "><p id="p4706384922316"><a name="p4706384922316"></a><a name="p4706384922316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.2.5.1.4 "><p id="p970883222316"><a name="p970883222316"></a><a name="p970883222316"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section44370581"></a>

[Table 3](#table50992744154526)  lists the response parameter.

**Table  3**  Response parameter

<a name="table50992744154526"></a>
<table><thead align="left"><tr id="row20073554154526"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.2.5.1.1"><p id="p15345186154526"><a name="p15345186154526"></a><a name="p15345186154526"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.2"><p id="p35000534154526"><a name="p35000534154526"></a><a name="p35000534154526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.21%" id="mcps1.2.5.1.3"><p id="p16470999154526"><a name="p16470999154526"></a><a name="p16470999154526"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p59082508154526"><a name="p59082508154526"></a><a name="p59082508154526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20953821154526"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.2.5.1.1 "><p id="p19537972154526"><a name="p19537972154526"></a><a name="p19537972154526"></a>virtual_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.2 "><p id="p39071862154526"><a name="p39071862154526"></a><a name="p39071862154526"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.2.5.1.3 "><p id="p10704269154526"><a name="p10704269154526"></a><a name="p10704269154526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p61739489154526"><a name="p61739489154526"></a><a name="p61739489154526"></a>Specifies the <strong id="b842352706191711"><a name="b842352706191711"></a><a name="b842352706191711"></a>virtual_gateway</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_gateway**

<a name="table14681450"></a>
<table><thead align="left"><tr id="row21069217"><th class="cellrowborder" valign="top" width="23.712371237123715%" id="mcps1.1.5.1.1"><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a><strong id="b654760381"><a name="b654760381"></a><a name="b654760381"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.471447144714473%" id="mcps1.1.5.1.2"><p id="p57985771"><a name="p57985771"></a><a name="p57985771"></a><strong id="b266068753"><a name="b266068753"></a><a name="b266068753"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.64176417641764%" id="mcps1.1.5.1.3"><p id="p66335909"><a name="p66335909"></a><a name="p66335909"></a><strong id="b1426267678"><a name="b1426267678"></a><a name="b1426267678"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.174417441744176%" id="mcps1.1.5.1.4"><p id="p4499576"><a name="p4499576"></a><a name="p4499576"></a><strong id="b1444937998"><a name="b1444937998"></a><a name="b1444937998"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6614602622620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p48182202101925"><a name="p48182202101925"></a><a name="p48182202101925"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p59780196101925"><a name="p59780196101925"></a><a name="p59780196101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p57616342101925"><a name="p57616342101925"></a><a name="p57616342101925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p37888342101925"><a name="p37888342101925"></a><a name="p37888342101925"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row4620915422620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p25488408101925"><a name="p25488408101925"></a><a name="p25488408101925"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p7310480101925"><a name="p7310480101925"></a><a name="p7310480101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p39773566101925"><a name="p39773566101925"></a><a name="p39773566101925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p10834414101925"><a name="p10834414101925"></a><a name="p10834414101925"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row1146602622620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p47477478101925"><a name="p47477478101925"></a><a name="p47477478101925"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p42000430101925"><a name="p42000430101925"></a><a name="p42000430101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p23940980101925"><a name="p23940980101925"></a><a name="p23940980101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p27885293101925"><a name="p27885293101925"></a><a name="p27885293101925"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row2411573022620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p37379319101925"><a name="p37379319101925"></a><a name="p37379319101925"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p61432386101925"><a name="p61432386101925"></a><a name="p61432386101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p47858240101925"><a name="p47858240101925"></a><a name="p47858240101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p7737903101925"><a name="p7737903101925"></a><a name="p7737903101925"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row1544898622620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p3619574101925"><a name="p3619574101925"></a><a name="p3619574101925"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p14771586101925"><a name="p14771586101925"></a><a name="p14771586101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p49017265101925"><a name="p49017265101925"></a><a name="p49017265101925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p5953066101925"><a name="p5953066101925"></a><a name="p5953066101925"></a>Specifies the ID of the VPC to be accessed.</p>
</td>
</tr>
<tr id="row1078246722620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p32281271101925"><a name="p32281271101925"></a><a name="p32281271101925"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p5541315101925"><a name="p5541315101925"></a><a name="p5541315101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p13983600101925"><a name="p13983600101925"></a><a name="p13983600101925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p63958699101925"><a name="p63958699101925"></a><a name="p63958699101925"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
</td>
</tr>
<tr id="row6138324222620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p32997247101925"><a name="p32997247101925"></a><a name="p32997247101925"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p46107109101925"><a name="p46107109101925"></a><a name="p46107109101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p18466692101925"><a name="p18466692101925"></a><a name="p18466692101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p15415539101925"><a name="p15415539101925"></a><a name="p15415539101925"></a>Specifies the ID of the physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row1031192022620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p18325622101925"><a name="p18325622101925"></a><a name="p18325622101925"></a>redundant_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p65292128101925"><a name="p65292128101925"></a><a name="p65292128101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p12099082101925"><a name="p12099082101925"></a><a name="p12099082101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p5906576101925"><a name="p5906576101925"></a><a name="p5906576101925"></a>Specifies the ID of the redundant physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row5851285614284"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p3405905314286"><a name="p3405905314286"></a><a name="p3405905314286"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p731994814286"><a name="p731994814286"></a><a name="p731994814286"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p5604494814286"><a name="p5604494814286"></a><a name="p5604494814286"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p4334692414286"><a name="p4334692414286"></a><a name="p4334692414286"></a>Specifies the virtual gateway type. The value can be <strong id="b842352706232310"><a name="b842352706232310"></a><a name="b842352706232310"></a>default</strong> or <strong id="b842352706232316"><a name="b842352706232316"></a><a name="b842352706232316"></a>double ipsec</strong>.</p>
</td>
</tr>
<tr id="row28672334104255"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p29292169104258"><a name="p29292169104258"></a><a name="p29292169104258"></a>ipsec_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p23855509104258"><a name="p23855509104258"></a><a name="p23855509104258"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p53248110104258"><a name="p53248110104258"></a><a name="p53248110104258"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p18129659104258"><a name="p18129659104258"></a><a name="p18129659104258"></a>Specifies the IPsec VPN access bandwidth in Mbit/s.</p>
</td>
</tr>
<tr id="row2493971716352"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p36808787163513"><a name="p36808787163513"></a><a name="p36808787163513"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p28721748163513"><a name="p28721748163513"></a><a name="p28721748163513"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p44760283163513"><a name="p44760283163513"></a><a name="p44760283163513"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p1704269163513"><a name="p1704269163513"></a><a name="p1704269163513"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row5093362822620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p23708553101925"><a name="p23708553101925"></a><a name="p23708553101925"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p26982350101925"><a name="p26982350101925"></a><a name="p26982350101925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p12644435101925"><a name="p12644435101925"></a><a name="p12644435101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p66585217144345"><a name="p66585217144345"></a><a name="p66585217144345"></a>Specifies the virtual gateway status.</p>
<p id="p36504862101925"><a name="p36504862101925"></a><a name="p36504862101925"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, or <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row1902755522620"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.1.5.1.1 "><p id="p53417473101925"><a name="p53417473101925"></a><a name="p53417473101925"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.471447144714473%" headers="mcps1.1.5.1.2 "><p id="p58004377101925"><a name="p58004377101925"></a><a name="p58004377101925"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.1.5.1.3 "><p id="p18351805101925"><a name="p18351805101925"></a><a name="p18351805101925"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44.174417441744176%" headers="mcps1.1.5.1.4 "><p id="p59611472144350"><a name="p59611472144350"></a><a name="p59611472144350"></a>Specifies the administrative state of the virtual gateway.</p>
<p id="p51204156101925"><a name="p51204156101925"></a><a name="p51204156101925"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section63790914"></a>

-   Example request

    ```
    GET /v2.0/dcaas/virtual-gateways/{virtual_gateway_id}
    ```


-   Example response

    ```
    {    
        "virtual_gateway" : {
            "id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389", 
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual gateway1",
            "description" : "",
            "vpc_id" : "908d9cf3-da64-4acb-393f-e5eb6b9e838a",
            "local_ep_group_id" : "f8834cf1-5468-87c7-223d-56e78b9699ab",
            "device_id" : "aaa_01"
        }
    }
    ```


## Returned Value<a name="section32595206173323"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

