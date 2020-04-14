# Querying the Connection List<a name="en-dc_topic_0055025316"></a>

## Function<a name="section17487184"></a>

This API is used to query the connection list.

## URI<a name="section23166934"></a>

GET /v2.0/dcaas/direct-connects

**Table  1**  Parameter description

<a name="table7306830153125"></a>
<table><thead align="left"><tr id="row59179138153125"><th class="cellrowborder" valign="top" width="31.443144314431443%" id="mcps1.2.5.1.1"><p id="p6185651415404"><a name="p6185651415404"></a><a name="p6185651415404"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.842084208420843%" id="mcps1.2.5.1.2"><p id="p4432173215404"><a name="p4432173215404"></a><a name="p4432173215404"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.271627162716275%" id="mcps1.2.5.1.3"><p id="p1845161220516"><a name="p1845161220516"></a><a name="p1845161220516"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="31.443144314431443%" id="mcps1.2.5.1.4"><p id="p1217810515404"><a name="p1217810515404"></a><a name="p1217810515404"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37905744153125"><td class="cellrowborder" valign="top" width="31.443144314431443%" headers="mcps1.2.5.1.1 "><p id="p50466461153125"><a name="p50466461153125"></a><a name="p50466461153125"></a>direct_connects</p>
</td>
<td class="cellrowborder" valign="top" width="20.842084208420843%" headers="mcps1.2.5.1.2 "><p id="p61251530153125"><a name="p61251530153125"></a><a name="p61251530153125"></a>List data structure</p>
</td>
<td class="cellrowborder" valign="top" width="16.271627162716275%" headers="mcps1.2.5.1.3 "><p id="p98450125519"><a name="p98450125519"></a><a name="p98450125519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="31.443144314431443%" headers="mcps1.2.5.1.4 "><p id="p23412453153125"><a name="p23412453153125"></a><a name="p23412453153125"></a>Indicates the direct connection list.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section64582388"></a>

[Table 2](#table2198437322244)  lists the request parameter.

**Table  2**  Request parameter

<a name="table2198437322244"></a>
<table><thead align="left"><tr id="row4304807922244"><th class="cellrowborder" valign="top" width="19.009999999999998%" id="mcps1.2.5.1.1"><p id="p6505580022244"><a name="p6505580022244"></a><a name="p6505580022244"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.2.5.1.2"><p id="p329696222244"><a name="p329696222244"></a><a name="p329696222244"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.46%" id="mcps1.2.5.1.3"><p id="p3257067222244"><a name="p3257067222244"></a><a name="p3257067222244"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p5470821922244"><a name="p5470821922244"></a><a name="p5470821922244"></a><strong id="b84235270616553"><a name="b84235270616553"></a><a name="b84235270616553"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5451891922244"><td class="cellrowborder" valign="top" width="19.009999999999998%" headers="mcps1.2.5.1.1 "><p id="p6157819622316"><a name="p6157819622316"></a><a name="p6157819622316"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.2 "><p id="p757920222316"><a name="p757920222316"></a><a name="p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.46%" headers="mcps1.2.5.1.3 "><p id="p4706384922316"><a name="p4706384922316"></a><a name="p4706384922316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p25148225203247"><a name="p25148225203247"></a><a name="p25148225203247"></a>Indicates the parameters expected to be returned.</p>
<p id="p970883222316"><a name="p970883222316"></a><a name="p970883222316"></a>If you do not specify it, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section44370581"></a>

[Table 3](#table122627546489)  lists the response parameter.

**Table  3**  Response parameter

<a name="table122627546489"></a>
<table><thead align="left"><tr id="row14268954154817"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.1"><p id="p3271165444819"><a name="p3271165444819"></a><a name="p3271165444819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p1927375411483"><a name="p1927375411483"></a><a name="p1927375411483"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.3"><p id="p11275205411482"><a name="p11275205411482"></a><a name="p11275205411482"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15278185419486"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p22793548488"><a name="p22793548488"></a><a name="p22793548488"></a>direct_connects</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p6280125454816"><a name="p6280125454816"></a><a name="p6280125454816"></a>List data structure</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p4282454124812"><a name="p4282454124812"></a><a name="p4282454124812"></a>Indicates the direct connection list.</p>
</td>
</tr>
</tbody>
</table>

[Table 4](#table14681450)  lists the  **direct\_connects**  parameters.

**Table  4**  Parameter description

<a name="table14681450"></a>
<table><thead align="left"><tr id="row21069217"><th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.4.1.1"><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a><strong id="b8423527069918_1"><a name="b8423527069918_1"></a><a name="b8423527069918_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.4.1.2"><p id="p57985771"><a name="p57985771"></a><a name="p57985771"></a><strong id="b842352706165439_1"><a name="b842352706165439_1"></a><a name="b842352706165439_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.495049504950494%" id="mcps1.2.4.1.3"><p id="p4499576"><a name="p4499576"></a><a name="p4499576"></a><strong id="b84235270616553_1"><a name="b84235270616553_1"></a><a name="b84235270616553_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6614602622620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p104601622620"><a name="p104601622620"></a><a name="p104601622620"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p3780831222620"><a name="p3780831222620"></a><a name="p3780831222620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p6365199022620"><a name="p6365199022620"></a><a name="p6365199022620"></a>Indicates the connection ID.</p>
</td>
</tr>
<tr id="row4620915422620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p136439822620"><a name="p136439822620"></a><a name="p136439822620"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p1144325422620"><a name="p1144325422620"></a><a name="p1144325422620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p3142744522620"><a name="p3142744522620"></a><a name="p3142744522620"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="row1146602622620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p2234447922620"><a name="p2234447922620"></a><a name="p2234447922620"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p1619677822620"><a name="p1619677822620"></a><a name="p1619677822620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p1148802322620"><a name="p1148802322620"></a><a name="p1148802322620"></a>Indicates the connection name.</p>
</td>
</tr>
<tr id="row2411573022620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p1496908622620"><a name="p1496908622620"></a><a name="p1496908622620"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p4630189822620"><a name="p4630189822620"></a><a name="p4630189822620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p4094974622620"><a name="p4094974622620"></a><a name="p4094974622620"></a>Provides supplementary information about the connection.</p>
</td>
</tr>
<tr id="row1544898622620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p2442012722620"><a name="p2442012722620"></a><a name="p2442012722620"></a>port_type</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p5863434722620"><a name="p5863434722620"></a><a name="p5863434722620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p3460603522620"><a name="p3460603522620"></a><a name="p3460603522620"></a>Indicates the type of the port used by the connection. The value can be <strong id="b370581214151058"><a name="b370581214151058"></a><a name="b370581214151058"></a>1G</strong> or <strong id="b263825441151058"><a name="b263825441151058"></a><a name="b263825441151058"></a>10G</strong>.</p>
</td>
</tr>
<tr id="row1078246722620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p2127372522620"><a name="p2127372522620"></a><a name="p2127372522620"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p6251142822620"><a name="p6251142822620"></a><a name="p6251142822620"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p6355872822620"><a name="p6355872822620"></a><a name="p6355872822620"></a>Indicates the bandwidth used by the connection (unit: Mbit/s).</p>
</td>
</tr>
<tr id="row6138324222620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p2577865322620"><a name="p2577865322620"></a><a name="p2577865322620"></a>location</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p5818642122620"><a name="p5818642122620"></a><a name="p5818642122620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p2785218222620"><a name="p2785218222620"></a><a name="p2785218222620"></a>Indicates the connection access location.</p>
</td>
</tr>
<tr id="row1031192022620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p4000130522620"><a name="p4000130522620"></a><a name="p4000130522620"></a>peer_location</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p224384122620"><a name="p224384122620"></a><a name="p224384122620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p5548563322620"><a name="p5548563322620"></a><a name="p5548563322620"></a>Indicates the physical location of the peer device accessed by the connection. The value can be a street, city, and province, or an IDC.</p>
</td>
</tr>
<tr id="row5093362822620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p1229275522620"><a name="p1229275522620"></a><a name="p1229275522620"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p6254979622620"><a name="p6254979622620"></a><a name="p6254979622620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p2855146722620"><a name="p2855146722620"></a><a name="p2855146722620"></a>Indicates the gateway device ID of the connection.</p>
</td>
</tr>
<tr id="row1902755522620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p891189122620"><a name="p891189122620"></a><a name="p891189122620"></a>interface_name</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p6140524222620"><a name="p6140524222620"></a><a name="p6140524222620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p3269683422620"><a name="p3269683422620"></a><a name="p3269683422620"></a>Indicates the name of the interface accessed by the connection.</p>
</td>
</tr>
<tr id="row900780202931"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p45745187202934"><a name="p45745187202934"></a><a name="p45745187202934"></a>redundant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p14372684202934"><a name="p14372684202934"></a><a name="p14372684202934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p11226534202934"><a name="p11226534202934"></a><a name="p11226534202934"></a>Indicates the ID of the redundant connection using the same gateway.</p>
</td>
</tr>
<tr id="row3024899622620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p6677751222620"><a name="p6677751222620"></a><a name="p6677751222620"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p10213722620"><a name="p10213722620"></a><a name="p10213722620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p315340922620"><a name="p315340922620"></a><a name="p315340922620"></a>Indicates the connection provider.</p>
</td>
</tr>
<tr id="row3795490222620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p63158017145530"><a name="p63158017145530"></a><a name="p63158017145530"></a>provider_status</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p2507357145530"><a name="p2507357145530"></a><a name="p2507357145530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p20421711145530"><a name="p20421711145530"></a><a name="p20421711145530"></a>Indicates the status of the provider's connection. The value can be <strong id="b842352706171439"><a name="b842352706171439"></a><a name="b842352706171439"></a>ACTIVE</strong> or <strong id="b842352706171443"><a name="b842352706171443"></a><a name="b842352706171443"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row32659018114157"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p47484664114259"><a name="p47484664114259"></a><a name="p47484664114259"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p21052557114259"><a name="p21052557114259"></a><a name="p21052557114259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p14271920839"><a name="p14271920839"></a><a name="p14271920839"></a>Indicates the connection type. The value can be <strong id="b842352706152446"><a name="b842352706152446"></a><a name="b842352706152446"></a>hosted</strong>.</p>
</td>
</tr>
<tr id="row49434738114151"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p34409240114259"><a name="p34409240114259"></a><a name="p34409240114259"></a>hosting_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p35685018114259"><a name="p35685018114259"></a><a name="p35685018114259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p53689989114259"><a name="p53689989114259"></a><a name="p53689989114259"></a>Indicates the ID of the hosting connection mapped to the hosted connection.</p>
</td>
</tr>
<tr id="row15221921114148"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p15534634114259"><a name="p15534634114259"></a><a name="p15534634114259"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p50345876114259"><a name="p50345876114259"></a><a name="p50345876114259"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p9469274114259"><a name="p9469274114259"></a><a name="p9469274114259"></a>Indicates the pre-allocated VLAN to the hosted connection.</p>
</td>
</tr>
<tr id="row60028731114142"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p9233764114259"><a name="p9233764114259"></a><a name="p9233764114259"></a>charge_mode</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p9737440114259"><a name="p9737440114259"></a><a name="p9737440114259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p66820134114259"><a name="p66820134114259"></a><a name="p66820134114259"></a>Indicates the billing mode. The value can be <strong id="b842352706153349"><a name="b842352706153349"></a><a name="b842352706153349"></a>prepayment</strong>, <strong id="b842352706153353"><a name="b842352706153353"></a><a name="b842352706153353"></a>bandwidth</strong>, or <strong id="b842352706153357"><a name="b842352706153357"></a><a name="b842352706153357"></a>traffic</strong>.</p>
</td>
</tr>
<tr id="row57077793114145"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p57951811114259"><a name="p57951811114259"></a><a name="p57951811114259"></a>apply_time</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p63585106114259"><a name="p63585106114259"></a><a name="p63585106114259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p33187083114259"><a name="p33187083114259"></a><a name="p33187083114259"></a>Indicates the time when the connection is applied for.</p>
</td>
</tr>
<tr id="row50379004114139"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p34192548114259"><a name="p34192548114259"></a><a name="p34192548114259"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p18132976114259"><a name="p18132976114259"></a><a name="p18132976114259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p53553871114259"><a name="p53553871114259"></a><a name="p53553871114259"></a>Indicates the time when the connection is created.</p>
</td>
</tr>
<tr id="row6268727111435"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p4450422211435"><a name="p4450422211435"></a><a name="p4450422211435"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p22189825114323"><a name="p22189825114323"></a><a name="p22189825114323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p28318692114323"><a name="p28318692114323"></a><a name="p28318692114323"></a>Indicates the time when the connection is deleted.</p>
</td>
</tr>
<tr id="row19481759155050"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p10877557155053"><a name="p10877557155053"></a><a name="p10877557155053"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p8666938155053"><a name="p8666938155053"></a><a name="p8666938155053"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p22574473155053"><a name="p22574473155053"></a><a name="p22574473155053"></a>Indicates the order number of a connection.</p>
</td>
</tr>
<tr id="row53490214155047"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p15119229155053"><a name="p15119229155053"></a><a name="p15119229155053"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p16698041155053"><a name="p16698041155053"></a><a name="p16698041155053"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p34183938155053"><a name="p34183938155053"></a><a name="p34183938155053"></a>Indicates the product ID corresponding to a connection order.</p>
</td>
</tr>
<tr id="row680867422620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p31385215145530"><a name="p31385215145530"></a><a name="p31385215145530"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p16453893145530"><a name="p16453893145530"></a><a name="p16453893145530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p17672464145530"><a name="p17672464145530"></a><a name="p17672464145530"></a>Indicates the connection status. The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b573557709231737"><a name="b573557709231737"></a><a name="b573557709231737"></a>PENDING_DELETE</strong>, <strong id="b810642512231737"><a name="b810642512231737"></a><a name="b810642512231737"></a>DELETED</strong>, <strong id="b17872564231737"><a name="b17872564231737"></a><a name="b17872564231737"></a>APPLY</strong>, <strong id="b1765160533231737"><a name="b1765160533231737"></a><a name="b1765160533231737"></a>DENY</strong>, <strong id="b1723423809231737"><a name="b1723423809231737"></a><a name="b1723423809231737"></a>PENDING_PAY</strong>, <strong id="b733428447231737"><a name="b733428447231737"></a><a name="b733428447231737"></a>PAID</strong>, <strong id="b1888084103231737"><a name="b1888084103231737"></a><a name="b1888084103231737"></a>ORDERING</strong>, <strong id="b842352706151915"><a name="b842352706151915"></a><a name="b842352706151915"></a>ACCEPT</strong>, or <strong id="b1504845468231737"><a name="b1504845468231737"></a><a name="b1504845468231737"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row4489054622620"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p1796992022620"><a name="p1796992022620"></a><a name="p1796992022620"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.4.1.2 "><p id="p1608399722620"><a name="p1608399722620"></a><a name="p1608399722620"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.495049504950494%" headers="mcps1.2.4.1.3 "><p id="p21461799203337"><a name="p21461799203337"></a><a name="p21461799203337"></a>Indicates the administrative state of the connection.</p>
<p id="p5197321322620"><a name="p5197321322620"></a><a name="p5197321322620"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section63790914"></a>

-   Example request

    1.  All parameters are returned:

    ```
    GET /v2.0/dcaas/direct-connects
    ```

    1.  Filtered parameters are returned \(for example, the filter is ID\):

    ```
    GET /v2.0/dcaas/direct-connects?id=6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a
    ```


-   Example response

    ```
    {
        "direct_connect" : [{
            "id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",        
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "direct connect1",
            "description" : "",
            "port_type" : "10G",
            "bandwidth" : 100,
            "location" : "Biere", 
            "device_id" : "172.16.40.2", 
            "provider" : "OTC"
        }]
    }
    ```


## Returned Value<a name="section6416329132915"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

