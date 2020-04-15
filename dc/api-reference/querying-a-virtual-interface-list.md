# Querying a Virtual Interface List<a name="en-dc_topic_0055025330"></a>

## Function<a name="section17487184"></a>

This API is used to query a virtual interface list.

## URI<a name="section23166934"></a>

GET /v2.0/dcaas/virtual-interfaces

## Request<a name="section64582388"></a>

[Table 1](#table2198437322244)  lists the request parameter.

**Table  1**  Request parameter

<a name="table2198437322244"></a>
<table><thead align="left"><tr id="row4304807922244"><th class="cellrowborder" valign="top" width="17.511751175117514%" id="mcps1.2.5.1.1"><p id="p6505580022244"><a name="p6505580022244"></a><a name="p6505580022244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.221522152215222%" id="mcps1.2.5.1.2"><p id="p329696222244"><a name="p329696222244"></a><a name="p329696222244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.64176417641764%" id="mcps1.2.5.1.3"><p id="p3257067222244"><a name="p3257067222244"></a><a name="p3257067222244"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49.62496249624962%" id="mcps1.2.5.1.4"><p id="p5470821922244"><a name="p5470821922244"></a><a name="p5470821922244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5451891922244"><td class="cellrowborder" valign="top" width="17.511751175117514%" headers="mcps1.2.5.1.1 "><p id="p6157819622316"><a name="p6157819622316"></a><a name="p6157819622316"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="15.221522152215222%" headers="mcps1.2.5.1.2 "><p id="p757920222316"><a name="p757920222316"></a><a name="p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.64176417641764%" headers="mcps1.2.5.1.3 "><p id="p4706384922316"><a name="p4706384922316"></a><a name="p4706384922316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.62496249624962%" headers="mcps1.2.5.1.4 "><p id="p28609808152757"><a name="p28609808152757"></a><a name="p28609808152757"></a>Specifies the parameters expected to be returned.</p>
<p id="p970883222316"><a name="p970883222316"></a><a name="p970883222316"></a>If you do not specify it, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section44370581"></a>

[Table 2](#table10476506155243)  lists the response parameter.

**Table  2**  Response parameter

<a name="table10476506155243"></a>
<table><thead align="left"><tr id="row28606500155243"><th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.4.1.1"><p id="p28732152155335"><a name="p28732152155335"></a><a name="p28732152155335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.4.1.2"><p id="p45602971155335"><a name="p45602971155335"></a><a name="p45602971155335"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.4.1.3"><p id="p29780927155335"><a name="p29780927155335"></a><a name="p29780927155335"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17724599155243"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p26406454155243"><a name="p26406454155243"></a><a name="p26406454155243"></a>virtual_interfaces</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.4.1.2 "><p id="p58548062155243"><a name="p58548062155243"></a><a name="p58548062155243"></a>List data structure</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.3 "><p id="p2699206155243"><a name="p2699206155243"></a><a name="p2699206155243"></a>Specifies the virtual interface list.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interfaces**

<a name="table14681450"></a>
<table><thead align="left"><tr id="row21069217"><th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.1.4.1.1"><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.1.4.1.2"><p id="p57985771"><a name="p57985771"></a><a name="p57985771"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.1.4.1.3"><p id="p4499576"><a name="p4499576"></a><a name="p4499576"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28785503142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p54569191142315"><a name="p54569191142315"></a><a name="p54569191142315"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p41421726142315"><a name="p41421726142315"></a><a name="p41421726142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p17104065142315"><a name="p17104065142315"></a><a name="p17104065142315"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
<tr id="row21517991142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p4563876142315"><a name="p4563876142315"></a><a name="p4563876142315"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p47935545142315"><a name="p47935545142315"></a><a name="p47935545142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p7252844142315"><a name="p7252844142315"></a><a name="p7252844142315"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row39252187142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p27399442142315"><a name="p27399442142315"></a><a name="p27399442142315"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p51949177142315"><a name="p51949177142315"></a><a name="p51949177142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p27300093142315"><a name="p27300093142315"></a><a name="p27300093142315"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row9820119142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p62556265142315"><a name="p62556265142315"></a><a name="p62556265142315"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p42012219142315"><a name="p42012219142315"></a><a name="p42012219142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p51707266142315"><a name="p51707266142315"></a><a name="p51707266142315"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row24079154142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p44220931142315"><a name="p44220931142315"></a><a name="p44220931142315"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p24161680142315"><a name="p24161680142315"></a><a name="p24161680142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p8116402142315"><a name="p8116402142315"></a><a name="p8116402142315"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row2026400142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p343562142315"><a name="p343562142315"></a><a name="p343562142315"></a>vgw_ id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p24624790142315"><a name="p24624790142315"></a><a name="p24624790142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p1221885142315"><a name="p1221885142315"></a><a name="p1221885142315"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row22414652142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p10673824142315"><a name="p10673824142315"></a><a name="p10673824142315"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p5440057142315"><a name="p5440057142315"></a><a name="p5440057142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p44068500142315"><a name="p44068500142315"></a><a name="p44068500142315"></a>Specifies the interface type. The value can be <strong id="b842352706142157"><a name="b842352706142157"></a><a name="b842352706142157"></a>public</strong> or <strong id="b84235270614220"><a name="b84235270614220"></a><a name="b84235270614220"></a>private</strong>.</p>
</td>
</tr>
<tr id="row13919876142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p14759603142315"><a name="p14759603142315"></a><a name="p14759603142315"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p24751912142315"><a name="p24751912142315"></a><a name="p24751912142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p45173146142315"><a name="p45173146142315"></a><a name="p45173146142315"></a>Specifies the access service type. The value can be <strong id="b1650500527142036"><a name="b1650500527142036"></a><a name="b1650500527142036"></a>vpc</strong>, <strong id="b26378606142036"><a name="b26378606142036"></a><a name="b26378606142036"></a>public service</strong>, or <strong id="b1032837367142036"><a name="b1032837367142036"></a><a name="b1032837367142036"></a>vpc and public service</strong>.</p>
</td>
</tr>
<tr id="row30135492142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p12348862142315"><a name="p12348862142315"></a><a name="p12348862142315"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p15690831212825"><a name="p15690831212825"></a><a name="p15690831212825"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p32938441142315"><a name="p32938441142315"></a><a name="p32938441142315"></a>Specifies the VLAN used by the local gateway to communicate with the remote gateway.</p>
</td>
</tr>
<tr id="row52865460142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p4471746142315"><a name="p4471746142315"></a><a name="p4471746142315"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p5039092419428"><a name="p5039092419428"></a><a name="p5039092419428"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p57231560142315"><a name="p57231560142315"></a><a name="p57231560142315"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row1174788142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p61891493142315"><a name="p61891493142315"></a><a name="p61891493142315"></a>local_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p38024775142315"><a name="p38024775142315"></a><a name="p38024775142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p47464297142315"><a name="p47464297142315"></a><a name="p47464297142315"></a>Specifies the IPv4 address of the local gateway.</p>
</td>
</tr>
<tr id="row26869652142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p17829191142315"><a name="p17829191142315"></a><a name="p17829191142315"></a>remote_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p66652503142315"><a name="p66652503142315"></a><a name="p66652503142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p35789093142315"><a name="p35789093142315"></a><a name="p35789093142315"></a>Specifies the IPv4 address of the remote gateway.</p>
</td>
</tr>
<tr id="row34897189142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p58744713142315"><a name="p58744713142315"></a><a name="p58744713142315"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p41137545142315"><a name="p41137545142315"></a><a name="p41137545142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p42045432142315"><a name="p42045432142315"></a><a name="p42045432142315"></a>Specifies the routing mode. The value can be <strong id="b84235270614653"><a name="b84235270614653"></a><a name="b84235270614653"></a>static</strong> or <strong id="b84235270614655"><a name="b84235270614655"></a><a name="b84235270614655"></a>bgp</strong>.</p>
</td>
</tr>
<tr id="row49988660142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p10808702142315"><a name="p10808702142315"></a><a name="p10808702142315"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p10133025142315"><a name="p10133025142315"></a><a name="p10133025142315"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p10631678142315"><a name="p10631678142315"></a><a name="p10631678142315"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row59271874142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p28139793142315"><a name="p28139793142315"></a><a name="p28139793142315"></a>bgp_md5</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p7655701142315"><a name="p7655701142315"></a><a name="p7655701142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p35180781142315"><a name="p35180781142315"></a><a name="p35180781142315"></a>Specifies the MD5 password of the BGP peer.</p>
</td>
</tr>
<tr id="row35617238142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p58325078142315"><a name="p58325078142315"></a><a name="p58325078142315"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p63792250142315"><a name="p63792250142315"></a><a name="p63792250142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p27037394142315"><a name="p27037394142315"></a><a name="p27037394142315"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row55969893142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p14866898142315"><a name="p14866898142315"></a><a name="p14866898142315"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p40698992142315"><a name="p40698992142315"></a><a name="p40698992142315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p16622126142315"><a name="p16622126142315"></a><a name="p16622126142315"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row27199761161621"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p30626851161624"><a name="p30626851161624"></a><a name="p30626851161624"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p17559799161624"><a name="p17559799161624"></a><a name="p17559799161624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p11516750161624"><a name="p11516750161624"></a><a name="p11516750161624"></a>Specifies the time when the virtual interface is created.</p>
</td>
</tr>
<tr id="row60433793171435"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p1811107171457"><a name="p1811107171457"></a><a name="p1811107171457"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p12482015171457"><a name="p12482015171457"></a><a name="p12482015171457"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p21686962171457"><a name="p21686962171457"></a><a name="p21686962171457"></a>Specifies the time when the virtual interface is deleted.</p>
</td>
</tr>
<tr id="row3640871019435"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p3412662319438"><a name="p3412662319438"></a><a name="p3412662319438"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p1279309419438"><a name="p1279309419438"></a><a name="p1279309419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p12169474152744"><a name="p12169474152744"></a><a name="p12169474152744"></a>Specifies the virtual interface status.</p>
<p id="p4941528219438"><a name="p4941528219438"></a><a name="p4941528219438"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>, <strong id="b100464761233116"><a name="b100464761233116"></a><a name="b100464761233116"></a>DELETED</strong>, <strong id="b1139764118233116"><a name="b1139764118233116"></a><a name="b1139764118233116"></a>AUTHORIZATION</strong>, or <strong id="b1189284423233116"><a name="b1189284423233116"></a><a name="b1189284423233116"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row50456942142315"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p44246765142315"><a name="p44246765142315"></a><a name="p44246765142315"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p9366191142315"><a name="p9366191142315"></a><a name="p9366191142315"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p10509913152738"><a name="p10509913152738"></a><a name="p10509913152738"></a>Specifies the administrative state of the virtual interface.</p>
<p id="p32769743142315"><a name="p32769743142315"></a><a name="p32769743142315"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
<tr id="row1050793415013"><td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.4.1.1 "><p id="p042015412503"><a name="p042015412503"></a><a name="p042015412503"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.4.1.2 "><p id="p542016416507"><a name="p542016416507"></a><a name="p542016416507"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.1.4.1.3 "><p id="p5420194155012"><a name="p5420194155012"></a><a name="p5420194155012"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b19931171675112"><a name="b19931171675112"></a><a name="b19931171675112"></a>true</strong> or <strong id="b15931141611519"><a name="b15931141611519"></a><a name="b15931141611519"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section63790914"></a>

-   Example request

    1.  All parameters are returned:

    ```
    GET /v2.0/dcaas/virtual-interfaces
    ```

    1.  Filtered parameters are returned \(for example, the filter is ID\):

    ```
    GET /v2.0/dcaas/virtual-interfaces?id=67c59cf4-1a64-46c7-763f-22eb1b9e8986
    ```


-   Example response

    ```
    {
        "virtual_interfaces" : [{
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
        }]
    }
    ```


## Returned Value<a name="section44742592173353"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

