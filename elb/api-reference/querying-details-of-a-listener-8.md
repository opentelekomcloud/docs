# Querying Details of a Listener<a name="EN-US_TOPIC_0096561540"></a>

## Function<a name="en-us_topic_0049139641_section19137160"></a>

This API is used to query details about a listener using its ID.

## URI<a name="en-us_topic_0049139641_section38016717"></a>

GET /v2.0/lbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="table154765473473"></a>
<table><thead align="left"><tr id="row251511470478"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p1151618474475"><a name="p1151618474475"></a><a name="p1151618474475"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.2"><p id="p5516144724717"><a name="p5516144724717"></a><a name="p5516144724717"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33%" id="mcps1.2.5.1.3"><p id="p5516164784711"><a name="p5516164784711"></a><a name="p5516164784711"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p6516184717476"><a name="p6516184717476"></a><a name="p6516184717476"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row751634716478"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p13516174764715"><a name="p13516174764715"></a><a name="p13516174764715"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.2 "><p id="p8516847144719"><a name="p8516847144719"></a><a name="p8516847144719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.3 "><p id="p1871353355117"><a name="p1871353355117"></a><a name="p1871353355117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p165161147164711"><a name="p165161147164711"></a><a name="p165161147164711"></a>Specifies the listener ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section189131654165420"></a>

None

## Response<a name="section1387714365516"></a>

**Table  2**  Response parameters

<a name="table47901746151717"></a>
<table><thead align="left"><tr id="row0791124610170"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.4.1.1"><p id="p379194618173"><a name="p379194618173"></a><a name="p379194618173"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.4.1.2"><p id="p6791124617173"><a name="p6791124617173"></a><a name="p6791124617173"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75.24752475247524%" id="mcps1.2.4.1.3"><p id="p11791446191715"><a name="p11791446191715"></a><a name="p11791446191715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row0792184681720"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.1 "><p id="p1879219462172"><a name="p1879219462172"></a><a name="p1879219462172"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.4.1.2 "><p id="p167924467178"><a name="p167924467178"></a><a name="p167924467178"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="75.24752475247524%" headers="mcps1.2.4.1.3 "><p id="p6792246151717"><a name="p6792246151717"></a><a name="p6792246151717"></a>Lists the listeners. For details, see <a href="#table7513153305114">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **listeners**  parameter description

<a name="table7513153305114"></a>
<table><thead align="left"><tr id="en-us_topic_0096561542_row34671725195410"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561542_p946792525418"><a name="en-us_topic_0096561542_p946792525418"></a><a name="en-us_topic_0096561542_p946792525418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561542_p8467142519541"><a name="en-us_topic_0096561542_p8467142519541"></a><a name="en-us_topic_0096561542_p8467142519541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561542_p104671125165411"><a name="en-us_topic_0096561542_p104671125165411"></a><a name="en-us_topic_0096561542_p104671125165411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561542_row12467122519549"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p8467425205419"><a name="en-us_topic_0096561542_p8467425205419"></a><a name="en-us_topic_0096561542_p8467425205419"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3467192515543"><a name="en-us_topic_0096561542_p3467192515543"></a><a name="en-us_topic_0096561542_p3467192515543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p9467132535416"><a name="en-us_topic_0096561542_p9467132535416"></a><a name="en-us_topic_0096561542_p9467132535416"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row124679252544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p44682025175413"><a name="en-us_topic_0096561542_p44682025175413"></a><a name="en-us_topic_0096561542_p44682025175413"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p146811253546"><a name="en-us_topic_0096561542_p146811253546"></a><a name="en-us_topic_0096561542_p146811253546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p19468192515548"><a name="en-us_topic_0096561542_p19468192515548"></a><a name="en-us_topic_0096561542_p19468192515548"></a>Specifies the ID of the project where the listener is used.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row746816255547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p184683251549"><a name="en-us_topic_0096561542_p184683251549"></a><a name="en-us_topic_0096561542_p184683251549"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1046842519548"><a name="en-us_topic_0096561542_p1046842519548"></a><a name="en-us_topic_0096561542_p1046842519548"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p44681425125418"><a name="en-us_topic_0096561542_p44681425125418"></a><a name="en-us_topic_0096561542_p44681425125418"></a>Specifies the listener name.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1046812512541"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p546862545411"><a name="en-us_topic_0096561542_p546862545411"></a><a name="en-us_topic_0096561542_p546862545411"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p154685252543"><a name="en-us_topic_0096561542_p154685252543"></a><a name="en-us_topic_0096561542_p154685252543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p14468172517540"><a name="en-us_topic_0096561542_p14468172517540"></a><a name="en-us_topic_0096561542_p14468172517540"></a>Provides supplementary information about the listener.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1046832595418"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p17468125125414"><a name="en-us_topic_0096561542_p17468125125414"></a><a name="en-us_topic_0096561542_p17468125125414"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p746811255546"><a name="en-us_topic_0096561542_p746811255546"></a><a name="en-us_topic_0096561542_p746811255546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p201601841193216"><a name="en-us_topic_0096561542_p201601841193216"></a><a name="en-us_topic_0096561542_p201601841193216"></a>Specifies the load balancer protocol.</p>
<p id="en-us_topic_0096561542_p0300344103218"><a name="en-us_topic_0096561542_p0300344103218"></a><a name="en-us_topic_0096561542_p0300344103218"></a>The value can be <strong id="en-us_topic_0096561542_b103871119189"><a name="en-us_topic_0096561542_b103871119189"></a><a name="en-us_topic_0096561542_b103871119189"></a>TCP</strong>, <strong id="en-us_topic_0096561542_b1038921117183"><a name="en-us_topic_0096561542_b1038921117183"></a><a name="en-us_topic_0096561542_b1038921117183"></a>HTTP</strong>, <strong id="en-us_topic_0096561542_b183906115182"><a name="en-us_topic_0096561542_b183906115182"></a><a name="en-us_topic_0096561542_b183906115182"></a>UDP</strong>, or <strong id="en-us_topic_0096561542_b193911311181810"><a name="en-us_topic_0096561542_b193911311181810"></a><a name="en-us_topic_0096561542_b193911311181810"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1346912520548"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p144691225205414"><a name="en-us_topic_0096561542_p144691225205414"></a><a name="en-us_topic_0096561542_p144691225205414"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p446952515416"><a name="en-us_topic_0096561542_p446952515416"></a><a name="en-us_topic_0096561542_p446952515416"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p18323468323"><a name="en-us_topic_0096561542_p18323468323"></a><a name="en-us_topic_0096561542_p18323468323"></a>Specifies the port used by the load balancer.</p>
<p id="en-us_topic_0096561542_p7688104743213"><a name="en-us_topic_0096561542_p7688104743213"></a><a name="en-us_topic_0096561542_p7688104743213"></a>The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1546932511547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p19469202585413"><a name="en-us_topic_0096561542_p19469202585413"></a><a name="en-us_topic_0096561542_p19469202585413"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p546911258548"><a name="en-us_topic_0096561542_p546911258548"></a><a name="en-us_topic_0096561542_p546911258548"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p16788191994017"><a name="en-us_topic_0096561542_p16788191994017"></a><a name="en-us_topic_0096561542_p16788191994017"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row16469625125411"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p3469112575415"><a name="en-us_topic_0096561542_p3469112575415"></a><a name="en-us_topic_0096561542_p3469112575415"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p144691725185411"><a name="en-us_topic_0096561542_p144691725185411"></a><a name="en-us_topic_0096561542_p144691725185411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p636816504321"><a name="en-us_topic_0096561542_p636816504321"></a><a name="en-us_topic_0096561542_p636816504321"></a>Specifies the maximum number of connections.</p>
<p id="en-us_topic_0096561542_p17992184321313"><a name="en-us_topic_0096561542_p17992184321313"></a><a name="en-us_topic_0096561542_p17992184321313"></a>The value ranges from <strong id="en-us_topic_0096561542_b1262188182"><a name="en-us_topic_0096561542_b1262188182"></a><a name="en-us_topic_0096561542_b1262188182"></a>-1</strong> to <strong id="en-us_topic_0096561542_b182018161820"><a name="en-us_topic_0096561542_b182018161820"></a><a name="en-us_topic_0096561542_b182018161820"></a>2147483647</strong>. The default value is <strong id="en-us_topic_0096561542_b780161918188"><a name="en-us_topic_0096561542_b780161918188"></a><a name="en-us_topic_0096561542_b780161918188"></a>-1</strong>, indicating that there is no restriction on maximum connections.</p>
<p id="en-us_topic_0096561542_p8758551203215"><a name="en-us_topic_0096561542_p8758551203215"></a><a name="en-us_topic_0096561542_p8758551203215"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row44691325175419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p446922525410"><a name="en-us_topic_0096561542_p446922525410"></a><a name="en-us_topic_0096561542_p446922525410"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3469102512549"><a name="en-us_topic_0096561542_p3469102512549"></a><a name="en-us_topic_0096561542_p3469102512549"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p257371723315"><a name="en-us_topic_0096561542_p257371723315"></a><a name="en-us_topic_0096561542_p257371723315"></a>Specifies the administrative status of the listener.</p>
<p id="en-us_topic_0096561542_p1316712043315"><a name="en-us_topic_0096561542_p1316712043315"></a><a name="en-us_topic_0096561542_p1316712043315"></a>This parameter is reserved. The value can only be <strong id="en-us_topic_0096561542_b17553924141815"><a name="en-us_topic_0096561542_b17553924141815"></a><a name="en-us_topic_0096561542_b17553924141815"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row155261945821"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p149771721230"><a name="en-us_topic_0096561542_p149771721230"></a><a name="en-us_topic_0096561542_p149771721230"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p149775217319"><a name="en-us_topic_0096561542_p149775217319"></a><a name="en-us_topic_0096561542_p149775217319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p483792111330"><a name="en-us_topic_0096561542_p483792111330"></a><a name="en-us_topic_0096561542_p483792111330"></a>Specifies whether to use HTTP/2.</p>
<p id="en-us_topic_0096561542_p183584202475"><a name="en-us_topic_0096561542_p183584202475"></a><a name="en-us_topic_0096561542_p183584202475"></a>The value can be <strong id="en-us_topic_0096561542_b53581020204716"><a name="en-us_topic_0096561542_b53581020204716"></a><a name="en-us_topic_0096561542_b53581020204716"></a>true</strong> or <strong id="en-us_topic_0096561542_b93584201473"><a name="en-us_topic_0096561542_b93584201473"></a><a name="en-us_topic_0096561542_b93584201473"></a>false</strong>.</p>
<a name="en-us_topic_0096561542_ul2055452614479"></a><a name="en-us_topic_0096561542_ul2055452614479"></a><ul id="en-us_topic_0096561542_ul2055452614479"><li><strong id="en-us_topic_0096561542_b155372615476"><a name="en-us_topic_0096561542_b155372615476"></a><a name="en-us_topic_0096561542_b155372615476"></a>true</strong>: HTTP/2 is used.</li><li><strong id="en-us_topic_0096561542_b366918288476"><a name="en-us_topic_0096561542_b366918288476"></a><a name="en-us_topic_0096561542_b366918288476"></a>false</strong>: HTTP/2 is not used.</li></ul>
<p id="en-us_topic_0096561542_p3519192712331"><a name="en-us_topic_0096561542_p3519192712331"></a><a name="en-us_topic_0096561542_p3519192712331"></a>This parameter is valid only when the load balancer protocol is set to <strong id="en-us_topic_0096561542_b167901226151113"><a name="en-us_topic_0096561542_b167901226151113"></a><a name="en-us_topic_0096561542_b167901226151113"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1547012555419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p20470112585411"><a name="en-us_topic_0096561542_p20470112585411"></a><a name="en-us_topic_0096561542_p20470112585411"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p9470525195410"><a name="en-us_topic_0096561542_p9470525195410"></a><a name="en-us_topic_0096561542_p9470525195410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p3466142973313"><a name="en-us_topic_0096561542_p3466142973313"></a><a name="en-us_topic_0096561542_p3466142973313"></a>Specifies the ID of the associated backend server group.</p>
<p id="en-us_topic_0096561542_p149661432143316"><a name="en-us_topic_0096561542_p149661432143316"></a><a name="en-us_topic_0096561542_p149661432143316"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="en-us_topic_0096561542_b125951581919"><a name="en-us_topic_0096561542_b125951581919"></a><a name="en-us_topic_0096561542_b125951581919"></a>null</strong>, the listener has no default backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row94701258544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p114701625185416"><a name="en-us_topic_0096561542_p114701625185416"></a><a name="en-us_topic_0096561542_p114701625185416"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p194705259542"><a name="en-us_topic_0096561542_p194705259542"></a><a name="en-us_topic_0096561542_p194705259542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p8103123513337"><a name="en-us_topic_0096561542_p8103123513337"></a><a name="en-us_topic_0096561542_p8103123513337"></a>Specifies the ID of the server certificate used by the listener. For details, see <a href="certificate-14.md">Certificate</a>.</p>
<p id="en-us_topic_0096561542_p15749173783317"><a name="en-us_topic_0096561542_p15749173783317"></a><a name="en-us_topic_0096561542_p15749173783317"></a>This parameter is mandatory when <strong id="en-us_topic_0096561542_b771517531197"><a name="en-us_topic_0096561542_b771517531197"></a><a name="en-us_topic_0096561542_b771517531197"></a>protocol</strong> is set to <strong id="en-us_topic_0096561542_b11716753181920"><a name="en-us_topic_0096561542_b11716753181920"></a><a name="en-us_topic_0096561542_b11716753181920"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row174701325205420"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p347010254548"><a name="en-us_topic_0096561542_p347010254548"></a><a name="en-us_topic_0096561542_p347010254548"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p4470825185414"><a name="en-us_topic_0096561542_p4470825185414"></a><a name="en-us_topic_0096561542_p4470825185414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p1867105844415"><a name="en-us_topic_0096561542_p1867105844415"></a><a name="en-us_topic_0096561542_p1867105844415"></a>Specifies the ID of the CA certificate used by the listener. For details, see <a href="certificate-14.md">Certificate</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1947122517545"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p1247117256543"><a name="en-us_topic_0096561542_p1247117256543"></a><a name="en-us_topic_0096561542_p1247117256543"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p7471172515547"><a name="en-us_topic_0096561542_p7471172515547"></a><a name="en-us_topic_0096561542_p7471172515547"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p33961341163319"><a name="en-us_topic_0096561542_p33961341163319"></a><a name="en-us_topic_0096561542_p33961341163319"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
<p id="en-us_topic_0096561542_p8259184619337"><a name="en-us_topic_0096561542_p8259184619337"></a><a name="en-us_topic_0096561542_p8259184619337"></a>If the parameter value is an empty list, the SNI feature is disabled.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row18840123882117"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p38408381214"><a name="en-us_topic_0096561542_p38408381214"></a><a name="en-us_topic_0096561542_p38408381214"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p12840538162110"><a name="en-us_topic_0096561542_p12840538162110"></a><a name="en-us_topic_0096561542_p12840538162110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p19840203842114"><a name="en-us_topic_0096561542_p19840203842114"></a><a name="en-us_topic_0096561542_p19840203842114"></a>Tags the listener.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row109815596568"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p18781627124910"><a name="en-us_topic_0096561542_p18781627124910"></a><a name="en-us_topic_0096561542_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p18781627204916"><a name="en-us_topic_0096561542_p18781627204916"></a><a name="en-us_topic_0096561542_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p15848951122220"><a name="en-us_topic_0096561542_p15848951122220"></a><a name="en-us_topic_0096561542_p15848951122220"></a>Specifies the time when the listener was created. The UTC time is in <em id="en-us_topic_0096561542_i1017723733015"><a name="en-us_topic_0096561542_i1017723733015"></a><a name="en-us_topic_0096561542_i1017723733015"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row122703319572"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p1541843114495"><a name="en-us_topic_0096561542_p1541843114495"></a><a name="en-us_topic_0096561542_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1810172112506"><a name="en-us_topic_0096561542_p1810172112506"></a><a name="en-us_topic_0096561542_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p341843144919"><a name="en-us_topic_0096561542_p341843144919"></a><a name="en-us_topic_0096561542_p341843144919"></a>Specifies the time when the listener was updated. The UTC time is in <em id="en-us_topic_0096561542_i12883301256"><a name="en-us_topic_0096561542_i12883301256"></a><a name="en-us_topic_0096561542_i12883301256"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row674511497493"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p15804713184311"><a name="en-us_topic_0096561542_p15804713184311"></a><a name="en-us_topic_0096561542_p15804713184311"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p78041413134319"><a name="en-us_topic_0096561542_p78041413134319"></a><a name="en-us_topic_0096561542_p78041413134319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p546123425013"><a name="en-us_topic_0096561542_p546123425013"></a><a name="en-us_topic_0096561542_p546123425013"></a>Specifies the security policy used by the listener. This parameter is valid only when the load balancer protocol is set to <strong id="en-us_topic_0096561542_b156051134122510"><a name="en-us_topic_0096561542_b156051134122510"></a><a name="en-us_topic_0096561542_b156051134122510"></a>TERMINATED_HTTPS</strong>.</p>
<p id="en-us_topic_0096561542_p3241114918325"><a name="en-us_topic_0096561542_p3241114918325"></a><a name="en-us_topic_0096561542_p3241114918325"></a>The value can be <strong id="en-us_topic_0096561542_b13885173792519"><a name="en-us_topic_0096561542_b13885173792519"></a><a name="en-us_topic_0096561542_b13885173792519"></a>tls-1-0</strong>, <strong id="en-us_topic_0096561542_b15887123752517"><a name="en-us_topic_0096561542_b15887123752517"></a><a name="en-us_topic_0096561542_b15887123752517"></a>tls-1-1</strong>, <strong id="en-us_topic_0096561542_b9887123742520"><a name="en-us_topic_0096561542_b9887123742520"></a><a name="en-us_topic_0096561542_b9887123742520"></a>tls-1-2</strong>, or <strong id="en-us_topic_0096561542_b13889133713252"><a name="en-us_topic_0096561542_b13889133713252"></a><a name="en-us_topic_0096561542_b13889133713252"></a>tls-1-2-strict</strong>, and the default value is <strong id="en-us_topic_0096561542_b2088953792517"><a name="en-us_topic_0096561542_b2088953792517"></a><a name="en-us_topic_0096561542_b2088953792517"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="adding-a-listener-6.md#table1247813103533">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section137461211133710"></a>

-   Example request: Viewing details of a listener

    ```
    GET https://{Endpoint}/v2.0/lbaas/listeners/09e64049-2ab0-4763-a8c5-f4207875dc3e
    ```


-   Example response

    ```
    {
        "listener": {
            "protocol_port": 8000,
            "protocol": "TCP",
            "description": "",
            "client_ca_tls_container_ref": null,
            "default_tls_container_ref": null,
            "admin_state_up": true,
            "http2_enable": false,
            "loadbalancers": [
                {
                    "id": "3d77894d-2ffe-4411-ac0a-0d57689779b8"
                }
            ],
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
            "sni_container_refs": [],
            "connection_limit": -1,
            "default_pool_id": "b7e53dbd-62ab-4505-a280-5c066078a5c9",
            "id": "09e64049-2ab0-4763-a8c5-f4207875dc3e",
            "tags": [],
            "name": "listener-2",
            "tls_ciphers_policy": null,
            "created_at": "2018-07-25T01:54:13", 
            "updated_at": "2018-07-25T01:54:14"
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139641_section49320909"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

