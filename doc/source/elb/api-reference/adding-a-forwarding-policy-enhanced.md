# Adding a Forwarding Policy<a name="EN-US_TOPIC_0136295317"></a>

## Function<a name="section169151579315"></a>

This API is used to add a forwarding policy. The listener and forwarding policy determine how traffic is forwarded to backend servers.

-   By matching the URL or domain name specified in the forwarding policy when  **action**  is set to  **REDIRECT\_TO\_POOL**, the load balancer distribute the traffic to backend servers in a specific backend server group.
-   When  **action**  is set to  **REDIRECT\_TO\_LISTENER**, the HTTP listener is redirected to an HTTPS listener, and traffic is distributed to this HTTPS listener.

## URI<a name="section1221617474435"></a>

POST /v2.0/lbaas/l7policies

## Constraints<a name="section127141641185420"></a>

Currently, only redirects from an HTTP listener to an HTTPS listener are supported. When  **action**  is set to  **REDIRECT\_TO\_LISTENER**, the listener specified by  **listener\_id**  can only be an HTTP listener, and the listener specified by  **redirect\_listener\_id**  can only be an HTTPS listener.

The load balancer of the HTTPS listener to which traffic is redirected must be the same as that of the HTTP listener.

## Request<a name="section91663145313"></a>

**Table  1**  Request parameters

<a name="table1035231812353"></a>
<table><thead align="left"><tr id="row635281817359"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p1635211819357"><a name="p1635211819357"></a><a name="p1635211819357"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="p15352718153512"><a name="p15352718153512"></a><a name="p15352718153512"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p12352191883510"><a name="p12352191883510"></a><a name="p12352191883510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p4837101211345"><a name="p4837101211345"></a><a name="p4837101211345"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43521918163516"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p123521718143516"><a name="p123521718143516"></a><a name="p123521718143516"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p135231893520"><a name="p135231893520"></a><a name="p135231893520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p9352111810352"><a name="p9352111810352"></a><a name="p9352111810352"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p1335211811358"><a name="p1335211811358"></a><a name="p1335211811358"></a>Specifies the forwarding policy. For details, see <a href="#table173601118133515">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **l7policy**  parameter description

<a name="table173601118133515"></a>
<table><thead align="left"><tr id="row17352191883513"><th class="cellrowborder" valign="top" width="27.37%" id="mcps1.2.5.1.1"><p id="p153521618133514"><a name="p153521618133514"></a><a name="p153521618133514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.86%" id="mcps1.2.5.1.2"><p id="p835291853517"><a name="p835291853517"></a><a name="p835291853517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.860000000000001%" id="mcps1.2.5.1.3"><p id="p163521218193510"><a name="p163521218193510"></a><a name="p163521218193510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.91%" id="mcps1.2.5.1.4"><p id="p1035261883519"><a name="p1035261883519"></a><a name="p1035261883519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19352191816350"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p13352518133510"><a name="p13352518133510"></a><a name="p13352518133510"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p13352131893510"><a name="p13352131893510"></a><a name="p13352131893510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p16352218143518"><a name="p16352218143518"></a><a name="p16352218143518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p5295183141813"><a name="p5295183141813"></a><a name="p5295183141813"></a>Specifies the ID of the project where the forwarding policy is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p2038118462238"><a name="p2038118462238"></a><a name="p2038118462238"></a>The value must be the same as the value of <strong id="b139265135504"><a name="b139265135504"></a><a name="b139265135504"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1636071814351"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p15352141853516"><a name="p15352141853516"></a><a name="p15352141853516"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1436061833510"><a name="p1436061833510"></a><a name="p1436061833510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p3360918113515"><a name="p3360918113515"></a><a name="p3360918113515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p3360718183517"><a name="p3360718183517"></a><a name="p3360718183517"></a>Specifies the forwarding policy name.</p>
<p id="p882413511911"><a name="p882413511911"></a><a name="p882413511911"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row336061812351"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p16360111817356"><a name="p16360111817356"></a><a name="p16360111817356"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p14360918133510"><a name="p14360918133510"></a><a name="p14360918133510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p5360171813353"><a name="p5360171813353"></a><a name="p5360171813353"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b1347623025014"><a name="b1347623025014"></a><a name="b1347623025014"></a>true</strong> or <strong id="b94771630115015"><a name="b94771630115015"></a><a name="b94771630115015"></a>false</strong>.</p>
<p id="p1610904293213"><a name="p1610904293213"></a><a name="p1610904293213"></a>This parameter is reserved. The default value is <strong id="b4189258134219"><a name="b4189258134219"></a><a name="b4189258134219"></a>true</strong>.</p>
</td>
</tr>
<tr id="row183601318123514"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p183601518203517"><a name="p183601518203517"></a><a name="p183601518203517"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p15360618143518"><a name="p15360618143518"></a><a name="p15360618143518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p4360181823519"><a name="p4360181823519"></a><a name="p4360181823519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p1336061815356"><a name="p1336061815356"></a><a name="p1336061815356"></a>Provides supplementary information about the forwarding policy.</p>
<p id="p172902106193"><a name="p172902106193"></a><a name="p172902106193"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row16360171816350"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p1360181812350"><a name="p1360181812350"></a><a name="p1360181812350"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1836011833513"><a name="p1836011833513"></a><a name="p1836011833513"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p1736094314351"><a name="p1736094314351"></a><a name="p1736094314351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p960104714116"><a name="p960104714116"></a><a name="p960104714116"></a>Specifies the ID of the listener to which the forwarding policy is added.</p>
<a name="ul9510181216216"></a><a name="ul9510181216216"></a><ul id="ul9510181216216"><li>When <strong id="b15223586117941"><a name="b15223586117941"></a><a name="b15223586117941"></a>action</strong> is set to <strong id="b15784773317941"><a name="b15784773317941"></a><a name="b15784773317941"></a>REDIRECT_TO_POOL</strong>, forwarding policies can be added to a listener with <strong id="b842352706112543"><a name="b842352706112543"></a><a name="b842352706112543"></a>protocol</strong> set to <strong id="b842352706144254"><a name="b842352706144254"></a><a name="b842352706144254"></a>HTTP</strong> or <strong id="b842352706144258"><a name="b842352706144258"></a><a name="b842352706144258"></a>TERMINATED_HTTPS</strong>.</li><li>When <strong id="b8423527061795"><a name="b8423527061795"></a><a name="b8423527061795"></a>action</strong> is set to <strong id="b8423527061792"><a name="b8423527061792"></a><a name="b8423527061792"></a>REDIRECT_TO_LISTENER</strong>, forwarding policies can be added to a listener with <strong id="b784108613171052"><a name="b784108613171052"></a><a name="b784108613171052"></a>protocol</strong> set to <strong id="b125496110171052"><a name="b125496110171052"></a><a name="b125496110171052"></a>HTTP</strong>.</li></ul>
</td>
</tr>
<tr id="row14360161883515"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p1536091823514"><a name="p1536091823514"></a><a name="p1536091823514"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p16360111853518"><a name="p16360111853518"></a><a name="p16360111853518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p10360518183516"><a name="p10360518183516"></a><a name="p10360518183516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p19912991832"><a name="p19912991832"></a><a name="p19912991832"></a>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</p>
<p id="p136925473311"><a name="p136925473311"></a><a name="p136925473311"></a>The value can be one of the following:</p>
<a name="ul1141318491933"></a><a name="ul1141318491933"></a><ul id="ul1141318491933"><li><strong id="b10603036195113"><a name="b10603036195113"></a><a name="b10603036195113"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to the backend server group specified by <strong id="b1345619091711"><a name="b1345619091711"></a><a name="b1345619091711"></a>redirect_pool_id</strong>.</li><li><strong id="b5665342185111"><a name="b5665342185111"></a><a name="b5665342185111"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected to the HTTPS listener specified by <strong id="b16217153218174"><a name="b16217153218174"></a><a name="b16217153218174"></a>listener_id</strong> to the HTTPS listener specified by <strong id="b52390410176"><a name="b52390410176"></a><a name="b52390410176"></a>redirect_listener_id</strong>.</li></ul>
</td>
</tr>
<tr id="row143601718123515"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p236041814356"><a name="p236041814356"></a><a name="p236041814356"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p4360201814351"><a name="p4360201814351"></a><a name="p4360201814351"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p847312467354"><a name="p847312467354"></a><a name="p847312467354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p115216211498"><a name="p115216211498"></a><a name="p115216211498"></a>Specifies the ID of the backend server group to which traffic is forwarded. The default value is <strong id="b575971416528"><a name="b575971416528"></a><a name="b575971416528"></a>null</strong>.</p>
<p id="p1832361213715"><a name="p1832361213715"></a><a name="p1832361213715"></a>This parameter is mandatory when <strong id="b9321202216207"><a name="b9321202216207"></a><a name="b9321202216207"></a>action</strong> is set to <strong id="b444192722010"><a name="b444192722010"></a><a name="b444192722010"></a>REDIRECT_TO_POOL</strong>.</p>
<p id="p4166102318919"><a name="p4166102318919"></a><a name="p4166102318919"></a>This parameter cannot be specified when <strong id="b842352706171557"><a name="b842352706171557"></a><a name="b842352706171557"></a>action</strong> is set to <strong id="b84235270617161"><a name="b84235270617161"></a><a name="b84235270617161"></a>REDIRECT_TO_LISTENER</strong>.</p>
<p id="p92041223986"><a name="p92041223986"></a><a name="p92041223986"></a>The backend server group must meet the following requirements:</p>
<a name="ul15235151117108"></a><a name="ul15235151117108"></a><ul id="ul15235151117108"><li>Cannot be the default backend server group of the listener.</li><li>Cannot be the backend server group used by forwarding policies of other listeners.</li></ul>
</td>
</tr>
<tr id="row18360171893519"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p1136013182352"><a name="p1136013182352"></a><a name="p1136013182352"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1036091813514"><a name="p1036091813514"></a><a name="p1036091813514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p1957194910353"><a name="p1957194910353"></a><a name="p1957194910353"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p687911951310"><a name="p687911951310"></a><a name="p687911951310"></a>Specifies the ID of the listener that forwards the traffic. The default value is <strong id="b219213305541"><a name="b219213305541"></a><a name="b219213305541"></a>null</strong>.</p>
<p id="p9265143314376"><a name="p9265143314376"></a><a name="p9265143314376"></a>This parameter cannot be specified when <strong id="b1327023314379"><a name="b1327023314379"></a><a name="b1327023314379"></a>action</strong> is set to <strong id="b827612332379"><a name="b827612332379"></a><a name="b827612332379"></a>REDIRECT_TO_POOL</strong>.</p>
<p id="p1736695021210"><a name="p1736695021210"></a><a name="p1736695021210"></a>This parameter is mandatory when <strong id="b51302201227"><a name="b51302201227"></a><a name="b51302201227"></a>action</strong> is set to <strong id="b1561125152211"><a name="b1561125152211"></a><a name="b1561125152211"></a>REDIRECT_TO_LISTENER</strong>, and the listener must meet the following requirements:</p>
<a name="ul17360181816359"></a><a name="ul17360181816359"></a><ul id="ul17360181816359"><li>Can only be an HTTPS listener.</li><li>Can only be a listener of the same load balancer.</li></ul>
</td>
</tr>
<tr id="row8360181814351"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p15360718143516"><a name="p15360718143516"></a><a name="p15360718143516"></a>redirect_url</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p1736011181355"><a name="p1736011181355"></a><a name="p1736011181355"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p436081843519"><a name="p436081843519"></a><a name="p436081843519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p20989131710327"><a name="p20989131710327"></a><a name="p20989131710327"></a>Specifies the URL to which traffic is redirected. The default value is <strong id="b545922715564"><a name="b545922715564"></a><a name="b545922715564"></a>null</strong>.</p>
<p id="p18576435690"><a name="p18576435690"></a><a name="p18576435690"></a>This parameter is reserved.</p>
<p id="p1550221541916"><a name="p1550221541916"></a><a name="p1550221541916"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1136081823514"><td class="cellrowborder" valign="top" width="27.37%" headers="mcps1.2.5.1.1 "><p id="p1360151853516"><a name="p1360151853516"></a><a name="p1360151853516"></a>position</p>
</td>
<td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.2.5.1.2 "><p id="p10360318183511"><a name="p10360318183511"></a><a name="p10360318183511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.860000000000001%" headers="mcps1.2.5.1.3 "><p id="p18360161815354"><a name="p18360161815354"></a><a name="p18360161815354"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.91%" headers="mcps1.2.5.1.4 "><p id="p844522318322"><a name="p844522318322"></a><a name="p844522318322"></a>Specifies the forwarding priority. The value ranges from <strong id="b118068292566"><a name="b118068292566"></a><a name="b118068292566"></a>1</strong> to <strong id="b15806629205617"><a name="b15806629205617"></a><a name="b15806629205617"></a>100</strong>. The default value is <strong id="b4151203111566"><a name="b4151203111566"></a><a name="b4151203111566"></a>100</strong>.</p>
<p id="p1611226143220"><a name="p1611226143220"></a><a name="p1611226143220"></a>This parameter is reserved.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **l7rule**  parameter description

<a name="table16998194317143"></a>
<table><thead align="left"><tr id="en-us_topic_0116649236_row1813794914585"><th class="cellrowborder" valign="top" width="24.19%" id="mcps1.2.5.1.1"><p id="en-us_topic_0116649236_p18137204925818"><a name="en-us_topic_0116649236_p18137204925818"></a><a name="en-us_topic_0116649236_p18137204925818"></a><strong>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.469999999999999%" id="mcps1.2.5.1.2"><p id="en-us_topic_0116649236_p3137449195820"><a name="en-us_topic_0116649236_p3137449195820"></a><a name="en-us_topic_0116649236_p3137449195820"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.34%" id="mcps1.2.5.1.3"><p id="en-us_topic_0116649236_p15137104917584"><a name="en-us_topic_0116649236_p15137104917584"></a><a name="en-us_topic_0116649236_p15137104917584"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="en-us_topic_0116649236_p7137349185814"><a name="en-us_topic_0116649236_p7137349185814"></a><a name="en-us_topic_0116649236_p7137349185814"></a><strong>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0116649236_row61371149115814"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p113714490586"><a name="en-us_topic_0116649236_p113714490586"></a><a name="en-us_topic_0116649236_p113714490586"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p17137164945815"><a name="en-us_topic_0116649236_p17137164945815"></a><a name="en-us_topic_0116649236_p17137164945815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p151371449135815"><a name="en-us_topic_0116649236_p151371449135815"></a><a name="en-us_topic_0116649236_p151371449135815"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p189741017613"><a name="en-us_topic_0116649236_p189741017613"></a><a name="en-us_topic_0116649236_p189741017613"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="en-us_topic_0116649236_p189052592020"><a name="en-us_topic_0116649236_p189052592020"></a><a name="en-us_topic_0116649236_p189052592020"></a>The value can be <strong>true</strong> or <strong>false</strong>.</p>
<p id="en-us_topic_0116649236_p1610904293213"><a name="en-us_topic_0116649236_p1610904293213"></a><a name="en-us_topic_0116649236_p1610904293213"></a>This parameter is reserved. The default value is <strong>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row1213718492586"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p1513719494585"><a name="en-us_topic_0116649236_p1513719494585"></a><a name="en-us_topic_0116649236_p1513719494585"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p131371749155817"><a name="en-us_topic_0116649236_p131371749155817"></a><a name="en-us_topic_0116649236_p131371749155817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p181371749135814"><a name="en-us_topic_0116649236_p181371749135814"></a><a name="en-us_topic_0116649236_p181371749135814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p1161972619482"><a name="en-us_topic_0116649236_p1161972619482"></a><a name="en-us_topic_0116649236_p1161972619482"></a>Specifies the match type of a forwarding rule.</p>
<p id="en-us_topic_0116649236_p9536114413489"><a name="en-us_topic_0116649236_p9536114413489"></a><a name="en-us_topic_0116649236_p9536114413489"></a>The value range varies depending on the backend server group protocol:</p>
<a name="en-us_topic_0116649236_ul3525953124817"></a><a name="en-us_topic_0116649236_ul3525953124817"></a><ul id="en-us_topic_0116649236_ul3525953124817"><li><strong>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong>PATH</strong>: matches the path in the request.</li></ul>
<p id="en-us_topic_0116649236_p15285166489"><a name="en-us_topic_0116649236_p15285166489"></a><a name="en-us_topic_0116649236_p15285166489"></a>The match type of forwarding rules in a forwarding policy must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row91371498580"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p8137249165813"><a name="en-us_topic_0116649236_p8137249165813"></a><a name="en-us_topic_0116649236_p8137249165813"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p513714497583"><a name="en-us_topic_0116649236_p513714497583"></a><a name="en-us_topic_0116649236_p513714497583"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p513794918587"><a name="en-us_topic_0116649236_p513794918587"></a><a name="en-us_topic_0116649236_p513794918587"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p51371649125820"><a name="en-us_topic_0116649236_p51371649125820"></a><a name="en-us_topic_0116649236_p51371649125820"></a>Specifies the match mode. The options are as follows:</p>
<p id="en-us_topic_0116649236_p10794420115116"><a name="en-us_topic_0116649236_p10794420115116"></a><a name="en-us_topic_0116649236_p10794420115116"></a>When <strong>type</strong> is set to <strong>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="en-us_topic_0116649236_ul15305619145114"></a><a name="en-us_topic_0116649236_ul15305619145114"></a><ul id="en-us_topic_0116649236_ul15305619145114"><li><strong>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="en-us_topic_0116649236_p13663103020517"><a name="en-us_topic_0116649236_p13663103020517"></a><a name="en-us_topic_0116649236_p13663103020517"></a>When <strong>type</strong> is set to <strong>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="en-us_topic_0116649236_ul17531436125112"></a><a name="en-us_topic_0116649236_ul17531436125112"></a><ul id="en-us_topic_0116649236_ul17531436125112"><li><strong>REGEX</strong>: indicates regular expression match.</li><li><strong>STARTS_WITH</strong>: indicates prefix match.</li><li><strong>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0116649236_row1946012463715"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p7401231193715"><a name="en-us_topic_0116649236_p7401231193715"></a><a name="en-us_topic_0116649236_p7401231193715"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p19401153118372"><a name="en-us_topic_0116649236_p19401153118372"></a><a name="en-us_topic_0116649236_p19401153118372"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p154011731133717"><a name="en-us_topic_0116649236_p154011731133717"></a><a name="en-us_topic_0116649236_p154011731133717"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p1238515351377"><a name="en-us_topic_0116649236_p1238515351377"></a><a name="en-us_topic_0116649236_p1238515351377"></a>Specifies whether reverse match is supported.</p>
<p id="en-us_topic_0116649236_p1938543553715"><a name="en-us_topic_0116649236_p1938543553715"></a><a name="en-us_topic_0116649236_p1938543553715"></a>The value can be <strong>true</strong> or <strong>false</strong>. The default value is <strong>false</strong>.</p>
<p id="en-us_topic_0116649236_p183851435173713"><a name="en-us_topic_0116649236_p183851435173713"></a><a name="en-us_topic_0116649236_p183851435173713"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row1413713493580"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p5137649185812"><a name="en-us_topic_0116649236_p5137649185812"></a><a name="en-us_topic_0116649236_p5137649185812"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p131371549135810"><a name="en-us_topic_0116649236_p131371549135810"></a><a name="en-us_topic_0116649236_p131371549135810"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p1013794914584"><a name="en-us_topic_0116649236_p1013794914584"></a><a name="en-us_topic_0116649236_p1013794914584"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p82048119202"><a name="en-us_topic_0116649236_p82048119202"></a><a name="en-us_topic_0116649236_p82048119202"></a>Specifies the key of the match content. The default value is <strong>null</strong>.</p>
<p id="en-us_topic_0116649236_p1747128122016"><a name="en-us_topic_0116649236_p1747128122016"></a><a name="en-us_topic_0116649236_p1747128122016"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row18137184955815"><td class="cellrowborder" valign="top" width="24.19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0116649236_p121375495589"><a name="en-us_topic_0116649236_p121375495589"></a><a name="en-us_topic_0116649236_p121375495589"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0116649236_p1413718493586"><a name="en-us_topic_0116649236_p1413718493586"></a><a name="en-us_topic_0116649236_p1413718493586"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.34%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0116649236_p141372496586"><a name="en-us_topic_0116649236_p141372496586"></a><a name="en-us_topic_0116649236_p141372496586"></a>String</p>
<p id="p20577532174810"><a name="p20577532174810"></a><a name="p20577532174810"></a></p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0116649236_p16872195212010"><a name="en-us_topic_0116649236_p16872195212010"></a><a name="en-us_topic_0116649236_p16872195212010"></a>Specifies the value of the match content. The value cannot contain spaces.</p>
<a name="en-us_topic_0116649236_ul75251828131120"></a><a name="en-us_topic_0116649236_ul75251828131120"></a><ul id="en-us_topic_0116649236_ul75251828131120"><li>When <strong id="b1279312397192"><a name="b1279312397192"></a><a name="b1279312397192"></a>type</strong> is set to <strong id="b4795143919197"><a name="b4795143919197"></a><a name="b4795143919197"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong>type</strong> is set to <strong>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong>compare_type</strong> is set to <strong>STARTS_WITH</strong> or <strong>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:|\/()[]{}</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1857702713561"></a>

**Table  4**  Response parameters

<a name="table107875111574"></a>
<table><thead align="left"><tr id="row984216165711"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p484219135719"><a name="p484219135719"></a><a name="p484219135719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p98422014571"><a name="p98422014571"></a><a name="p98422014571"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="p10842215572"><a name="p10842215572"></a><a name="p10842215572"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1984213175716"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="a550100555602476a968f5ccd2a21bd30"><a name="a550100555602476a968f5ccd2a21bd30"></a><a name="a550100555602476a968f5ccd2a21bd30"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="ad5656706454749a2a1229da31098a77c"><a name="ad5656706454749a2a1229da31098a77c"></a><a name="ad5656706454749a2a1229da31098a77c"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p3842161115717"><a name="p3842161115717"></a><a name="p3842161115717"></a>Specifies the forwarding policy. For details, see <a href="#table1251155618376">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **l7policy**  parameter description

<a name="table1251155618376"></a>
<table><thead align="left"><tr id="row10701165673714"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1470214562375"><a name="p1470214562375"></a><a name="p1470214562375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p2702105618372"><a name="p2702105618372"></a><a name="p2702105618372"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="p770265613371"><a name="p770265613371"></a><a name="p770265613371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1170211562375"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p37021956163715"><a name="p37021956163715"></a><a name="p37021956163715"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p154311194575"><a name="p154311194575"></a><a name="p154311194575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p87022056103715"><a name="p87022056103715"></a><a name="p87022056103715"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row5702175643718"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p12491330111414"><a name="p12491330111414"></a><a name="p12491330111414"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1949510305143"><a name="p1949510305143"></a><a name="p1949510305143"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p5927193621418"><a name="p5927193621418"></a><a name="p5927193621418"></a>Specifies the ID of the project where the forwarding policy is used.</p>
</td>
</tr>
<tr id="row67026562371"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p97021056173713"><a name="p97021056173713"></a><a name="p97021056173713"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p9702105619373"><a name="p9702105619373"></a><a name="p9702105619373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p57021564370"><a name="p57021564370"></a><a name="p57021564370"></a>Specifies the forwarding policy name.</p>
</td>
</tr>
<tr id="row17021156193714"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1570220562375"><a name="p1570220562375"></a><a name="p1570220562375"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p270220563373"><a name="p270220563373"></a><a name="p270220563373"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p935075494818"><a name="p935075494818"></a><a name="p935075494818"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="p535095417489"><a name="p535095417489"></a><a name="p535095417489"></a>The value can be <strong id="b12787918559"><a name="b12787918559"></a><a name="b12787918559"></a>true</strong> or <strong id="b1579692551"><a name="b1579692551"></a><a name="b1579692551"></a>false</strong>.</p>
<p id="p1788713318331"><a name="p1788713318331"></a><a name="p1788713318331"></a>This parameter is reserved. The default value is <strong id="b61614114312"><a name="b61614114312"></a><a name="b61614114312"></a>true</strong>.</p>
</td>
</tr>
<tr id="row87021656103712"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p147021156163720"><a name="p147021156163720"></a><a name="p147021156163720"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p2702105663711"><a name="p2702105663711"></a><a name="p2702105663711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p163501654104816"><a name="p163501654104816"></a><a name="p163501654104816"></a>Provides supplementary information about the forwarding policy.</p>
</td>
</tr>
<tr id="row1970325673717"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p207031656133714"><a name="p207031656133714"></a><a name="p207031656133714"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1851734175713"><a name="p1851734175713"></a><a name="p1851734175713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p183501454194816"><a name="p183501454194816"></a><a name="p183501454194816"></a>Specifies the ID of the listener to which the forwarding policy is added.</p>
</td>
</tr>
<tr id="row1970317567371"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p17703115614375"><a name="p17703115614375"></a><a name="p17703115614375"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1170365623715"><a name="p1170365623715"></a><a name="p1170365623715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p2351954164814"><a name="p2351954164814"></a><a name="p2351954164814"></a>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</p>
<p id="p13351145412483"><a name="p13351145412483"></a><a name="p13351145412483"></a>The value can be one of the following:</p>
<a name="ul203511354204814"></a><a name="ul203511354204814"></a><ul id="ul203511354204814"><li><strong id="b17722184917467"><a name="b17722184917467"></a><a name="b17722184917467"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to the backend server group specified by <strong id="b372316496462"><a name="b372316496462"></a><a name="b372316496462"></a>redirect_pool_id</strong>.</li><li><strong id="b194119527467"><a name="b194119527467"></a><a name="b194119527467"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected to the HTTPS listener specified by <strong id="b204255216464"><a name="b204255216464"></a><a name="b204255216464"></a>listener_id</strong> to the HTTPS listener specified by <strong id="b114311529462"><a name="b114311529462"></a><a name="b114311529462"></a>redirect_listener_id</strong>.</li></ul>
</td>
</tr>
<tr id="row77039560374"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p6703195611375"><a name="p6703195611375"></a><a name="p6703195611375"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p9983113655710"><a name="p9983113655710"></a><a name="p9983113655710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p142211521194918"><a name="p142211521194918"></a><a name="p142211521194918"></a>Specifies the ID of the backend server group to which traffic is forwarded.</p>
</td>
</tr>
<tr id="row461412820402"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p35992015134018"><a name="p35992015134018"></a><a name="p35992015134018"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p859901512401"><a name="p859901512401"></a><a name="p859901512401"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p722113215492"><a name="p722113215492"></a><a name="p722113215492"></a>Specifies the ID of the listener that forwards the traffic.</p>
</td>
</tr>
<tr id="row9703135610377"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p18703195613712"><a name="p18703195613712"></a><a name="p18703195613712"></a>redirect_url</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p18703155693720"><a name="p18703155693720"></a><a name="p18703155693720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1714910214509"><a name="p1714910214509"></a><a name="p1714910214509"></a>Specifies the URL to which traffic is redirected.</p>
<p id="p914972185020"><a name="p914972185020"></a><a name="p914972185020"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row5703956183715"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p18703155613719"><a name="p18703155613719"></a><a name="p18703155613719"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1970375611378"><a name="p1970375611378"></a><a name="p1970375611378"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1870195534814"><a name="p1870195534814"></a><a name="p1870195534814"></a>Lists the forwarding rules of the forwarding policy. The following value options are available:</p>
</td>
</tr>
<tr id="row1970312566375"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p770375663720"><a name="p770375663720"></a><a name="p770375663720"></a>position</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1870319564378"><a name="p1870319564378"></a><a name="p1870319564378"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p0275145775019"><a name="p0275145775019"></a><a name="p0275145775019"></a>Specifies the forwarding priority. The value ranges from <strong id="b2339175913554"><a name="b2339175913554"></a><a name="b2339175913554"></a>1</strong> to <strong id="b43407596558"><a name="b43407596558"></a><a name="b43407596558"></a>100</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>100</strong>.</p>
<p id="p122771157115019"><a name="p122771157115019"></a><a name="p122771157115019"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row870395643716"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p6704256183713"><a name="p6704256183713"></a><a name="p6704256183713"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p170405683718"><a name="p170405683718"></a><a name="p170405683718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p14704205693714"><a name="p14704205693714"></a><a name="p14704205693714"></a>Specifies the provisioning status of the forwarding policy. The value can be <strong id="b815719212269"><a name="b815719212269"></a><a name="b815719212269"></a>ACTIVE</strong>, <strong id="b116291426162611"><a name="b116291426162611"></a><a name="b116291426162611"></a>PENDING_CREATE</strong>, or <strong id="b95901229192611"><a name="b95901229192611"></a><a name="b95901229192611"></a>ERROR</strong>.</p>
<p id="p178421832011"><a name="p178421832011"></a><a name="p178421832011"></a>The default value is <strong id="b24467134563"><a name="b24467134563"></a><a name="b24467134563"></a>ACTIVE</strong>.</p>
<p id="p210952312206"><a name="p210952312206"></a><a name="p210952312206"></a>This parameter is reserved.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section766133115014"></a>

-   Example request 1: Adding a forwarding policy

    ```
    POST https://{Endpoint}/v2.0/lbaas/l7policies 
    
    {
        "l7policy": {
            "name": "niubiao_yaqing_api-2", 
            "listener_id": "3e24a3ca-11e5-4aa3-abd4-61ba0a8a18f1", 
            "action": "REDIRECT_TO_POOL", 
            "redirect_pool_id": "6460f13a-76de-43c7-b776-4fefc06a676e", 
            "rules": [
                {
                    "type": "PATH", 
                    "compare_type": "EQUAL_TO", 
                    "value": "/test"
                }, 
                {
                    "type": "HOST_NAME", 
                    "compare_type": "EQUAL_TO", 
                    "value": "www.test.com"
                }
            ]
        }
    }
    ```

-   Example response 1

    ```
    {
        "l7policy": {
            "redirect_pool_id": "6460f13a-76de-43c7-b776-4fefc06a676e", 
            "description": "", 
            "admin_state_up": true, 
            "rules": [
                {
                    "id": "742600d9-2a14-4808-af69-336883dbb590"
                }, 
                {
                    "id": "3251ed77-0d52-412b-9310-733636bb3fbf"
                }
            ], 
            "tenant_id": "573d73c9f90e48d0bddfa0eb202b25c2", 
            "listener_id": "3e24a3ca-11e5-4aa3-abd4-61ba0a8a18f1", 
            "redirect_url": null, 
            "redirect_listener_id": null, 
            "action": "REDIRECT_TO_POOL", 
            "position": 100, 
            "provisioning_status": "ACTIVE", 
     
            "id": "65d6e115-f179-4bcd-9bbb-1484e5f8ee81", 
            "name": "niubiao_yaqing-_api-2"
        }
    }
    ```

-   Example request 2: Creating a redirect

    ```
    POST https://{Endpoint}/v2.0/lbaas/l7policies
    
    {
        "l7policy": {
            "action": "REDIRECT_TO_LISTENER", 
            "listener_id": "4ef8553e-9ef7-4859-a42d-919feaf89d60", 
            "redirect_listener_id": "3ee10199-a7b4-4784-93cd-857afe9d0890", 
            "name": "redirect-test"
        }
    }
    ```

-   Example response 2

    ```
    {
        "l7policy": {
            "redirect_pool_id": null, 
            "description": "", 
            "admin_state_up": true, 
            "rules": [ ], 
            "tenant_id": "573d73c9f90e48d0bddfa0eb202b25c2", 
            "listener_id": "4ef8553e-9ef7-4859-a42d-919feaf89d60", 
            "redirect_url": null, 
            "redirect_listener_id": "3ee10199-a7b4-4784-93cd-857afe9d0890", 
            "action": "REDIRECT_TO_LISTENER", 
            "position": 100, 
            "provisioning_status": "ACTIVE", 
            "id": "bc4e4338-480f-4a98-8245-5bb1964f0e1d", 
            "name": "redirect-test"
        }
    }
    ```


## Status Code<a name="section7837165175814"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

