# Querying Details of a Backend Server Group<a name="EN-US_TOPIC_0096561548"></a>

## Function<a name="section568684581417"></a>

This API is used to query details about a backend server group using its ID.

## URI<a name="section718210614158"></a>

GET /v2.0/lbaas/pools/\{pool\_id\}

**Table  1**  Parameter description

<a name="table122987220314"></a>
<table><thead align="left"><tr id="row11338921238"><th class="cellrowborder" valign="top" width="18.98%" id="mcps1.2.5.1.1"><p id="p143381921233"><a name="p143381921233"></a><a name="p143381921233"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.5.1.2"><p id="p93382027317"><a name="p93382027317"></a><a name="p93382027317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.259999999999998%" id="mcps1.2.5.1.3"><p id="p23381221834"><a name="p23381221834"></a><a name="p23381221834"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.28%" id="mcps1.2.5.1.4"><p id="p233862336"><a name="p233862336"></a><a name="p233862336"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17338221936"><td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.2.5.1.1 "><p id="p0338121632"><a name="p0338121632"></a><a name="p0338121632"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.5.1.2 "><p id="p3338326320"><a name="p3338326320"></a><a name="p3338326320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p14390152311214"><a name="p14390152311214"></a><a name="p14390152311214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.28%" headers="mcps1.2.5.1.4 "><p id="p63384218319"><a name="p63384218319"></a><a name="p63384218319"></a>Specifies the backend server group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section192783553133"></a>

None

## Response<a name="section0395724111415"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0049139648_table16393628"></a>
<table><thead align="left"><tr id="en-us_topic_0049139648_row17403488"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139648_p396418"><a name="en-us_topic_0049139648_p396418"></a><a name="en-us_topic_0049139648_p396418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139648_p32109884"><a name="en-us_topic_0049139648_p32109884"></a><a name="en-us_topic_0049139648_p32109884"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.396039603960396%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139648_p18229659"><a name="en-us_topic_0049139648_p18229659"></a><a name="en-us_topic_0049139648_p18229659"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139648_row207374"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139648_p16797371"><a name="en-us_topic_0049139648_p16797371"></a><a name="en-us_topic_0049139648_p16797371"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.2 "><p id="p839212319212"><a name="p839212319212"></a><a name="p839212319212"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139648_p57853219"><a name="en-us_topic_0049139648_p57853219"></a><a name="en-us_topic_0049139648_p57853219"></a>Specifies the backend server group. For details, see <a href="#table374714321310">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **pools**  parameter description

<a name="table374714321310"></a>
<table><thead align="left"><tr id="en-us_topic_0096561549_row129412056850"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561549_p8941556758"><a name="en-us_topic_0096561549_p8941556758"></a><a name="en-us_topic_0096561549_p8941556758"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561549_p5941205616511"><a name="en-us_topic_0096561549_p5941205616511"></a><a name="en-us_topic_0096561549_p5941205616511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561549_p19941155610513"><a name="en-us_topic_0096561549_p19941155610513"></a><a name="en-us_topic_0096561549_p19941155610513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561549_row1994112561351"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p6941956051"><a name="en-us_topic_0096561549_p6941956051"></a><a name="en-us_topic_0096561549_p6941956051"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p6395118132915"><a name="en-us_topic_0096561549_p6395118132915"></a><a name="en-us_topic_0096561549_p6395118132915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p394185614510"><a name="en-us_topic_0096561549_p394185614510"></a><a name="en-us_topic_0096561549_p394185614510"></a>Specifies the backend server group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row694135617510"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p18941356653"><a name="en-us_topic_0096561549_p18941356653"></a><a name="en-us_topic_0096561549_p18941356653"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p6942145615514"><a name="en-us_topic_0096561549_p6942145615514"></a><a name="en-us_topic_0096561549_p6942145615514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p133818413522"><a name="en-us_topic_0096561549_p133818413522"></a><a name="en-us_topic_0096561549_p133818413522"></a>Specifies the ID of the project where the backend server group is used.</p>
<p id="en-us_topic_0096561549_p17033816399"><a name="en-us_topic_0096561549_p17033816399"></a><a name="en-us_topic_0096561549_p17033816399"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row189421561755"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p99422562513"><a name="en-us_topic_0096561549_p99422562513"></a><a name="en-us_topic_0096561549_p99422562513"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p169421456857"><a name="en-us_topic_0096561549_p169421456857"></a><a name="en-us_topic_0096561549_p169421456857"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p894213562510"><a name="en-us_topic_0096561549_p894213562510"></a><a name="en-us_topic_0096561549_p894213562510"></a>Specifies the backend server group name.</p>
<p id="en-us_topic_0096561549_p11736124214399"><a name="en-us_topic_0096561549_p11736124214399"></a><a name="en-us_topic_0096561549_p11736124214399"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row7942165615511"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p694235612516"><a name="en-us_topic_0096561549_p694235612516"></a><a name="en-us_topic_0096561549_p694235612516"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p99423564514"><a name="en-us_topic_0096561549_p99423564514"></a><a name="en-us_topic_0096561549_p99423564514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p17942115615520"><a name="en-us_topic_0096561549_p17942115615520"></a><a name="en-us_topic_0096561549_p17942115615520"></a>Provides supplementary information about the backend server group.</p>
<p id="en-us_topic_0096561549_p12272194573912"><a name="en-us_topic_0096561549_p12272194573912"></a><a name="en-us_topic_0096561549_p12272194573912"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row6942115618510"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p129428561458"><a name="en-us_topic_0096561549_p129428561458"></a><a name="en-us_topic_0096561549_p129428561458"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p209421556751"><a name="en-us_topic_0096561549_p209421556751"></a><a name="en-us_topic_0096561549_p209421556751"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p12345548148"><a name="en-us_topic_0096561549_p12345548148"></a><a name="en-us_topic_0096561549_p12345548148"></a>Specifies the protocol that the backend server group uses to receive requests.</p>
<p id="en-us_topic_0096561549_p205871558161412"><a name="en-us_topic_0096561549_p205871558161412"></a><a name="en-us_topic_0096561549_p205871558161412"></a>TCP, UDP, and HTTP are supported.</p>
<p id="en-us_topic_0096561549_p12123121610154"><a name="en-us_topic_0096561549_p12123121610154"></a><a name="en-us_topic_0096561549_p12123121610154"></a>When a backend server group is added to a specific listener, the relationships between the load balancer protocol and the backend server group protocol are as follows:</p>
<a name="en-us_topic_0096561549_ul162192018201516"></a><a name="en-us_topic_0096561549_ul162192018201516"></a><ul id="en-us_topic_0096561549_ul162192018201516"><li>When the load balancer protocol is <strong id="en-us_topic_0096561549_b436022940"><a name="en-us_topic_0096561549_b436022940"></a><a name="en-us_topic_0096561549_b436022940"></a>UDP</strong>, the backend server group protocol must be <strong id="en-us_topic_0096561549_b1412247205"><a name="en-us_topic_0096561549_b1412247205"></a><a name="en-us_topic_0096561549_b1412247205"></a>UDP</strong>.</li><li>When the load balancer protocol is <strong id="en-us_topic_0096561549_b1792008295"><a name="en-us_topic_0096561549_b1792008295"></a><a name="en-us_topic_0096561549_b1792008295"></a>TCP</strong>, the backend server group protocol must be <strong id="en-us_topic_0096561549_b1893471636"><a name="en-us_topic_0096561549_b1893471636"></a><a name="en-us_topic_0096561549_b1893471636"></a>TCP</strong>.</li><li>When the load balancer protocol is <strong id="en-us_topic_0096561549_b278095684"><a name="en-us_topic_0096561549_b278095684"></a><a name="en-us_topic_0096561549_b278095684"></a>HTTP</strong> or <strong id="en-us_topic_0096561549_b230303621"><a name="en-us_topic_0096561549_b230303621"></a><a name="en-us_topic_0096561549_b230303621"></a>TERMINATED_HTTPS</strong>, the backend server group protocol must be <strong id="en-us_topic_0096561549_b1612389007"><a name="en-us_topic_0096561549_b1612389007"></a><a name="en-us_topic_0096561549_b1612389007"></a>HTTP</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561549_row694235612512"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p199426561657"><a name="en-us_topic_0096561549_p199426561657"></a><a name="en-us_topic_0096561549_p199426561657"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p149431356051"><a name="en-us_topic_0096561549_p149431356051"></a><a name="en-us_topic_0096561549_p149431356051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p1190711287157"><a name="en-us_topic_0096561549_p1190711287157"></a><a name="en-us_topic_0096561549_p1190711287157"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="en-us_topic_0096561549_p17447183017153"><a name="en-us_topic_0096561549_p17447183017153"></a><a name="en-us_topic_0096561549_p17447183017153"></a>The value can be one of the following:<a name="en-us_topic_0096561549_ul1064992814235"></a><a name="en-us_topic_0096561549_ul1064992814235"></a><ul id="en-us_topic_0096561549_ul1064992814235"><li><strong id="en-us_topic_0096561549_b1794111372911"><a name="en-us_topic_0096561549_b1794111372911"></a><a name="en-us_topic_0096561549_b1794111372911"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="en-us_topic_0096561549_b16960191417295"><a name="en-us_topic_0096561549_b16960191417295"></a><a name="en-us_topic_0096561549_b16960191417295"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="en-us_topic_0096561549_b8945715182910"><a name="en-us_topic_0096561549_b8945715182910"></a><a name="en-us_topic_0096561549_b8945715182910"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm. When the value is <strong id="en-us_topic_0096561549_b3577112981412"><a name="en-us_topic_0096561549_b3577112981412"></a><a name="en-us_topic_0096561549_b3577112981412"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0096561549_row1194465616515"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p14944256556"><a name="en-us_topic_0096561549_p14944256556"></a><a name="en-us_topic_0096561549_p14944256556"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p12944656151"><a name="en-us_topic_0096561549_p12944656151"></a><a name="en-us_topic_0096561549_p12944656151"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p139440561151"><a name="en-us_topic_0096561549_p139440561151"></a><a name="en-us_topic_0096561549_p139440561151"></a>Lists the IDs of backend servers in the backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row159441356956"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p17944155618514"><a name="en-us_topic_0096561549_p17944155618514"></a><a name="en-us_topic_0096561549_p17944155618514"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p10245320142912"><a name="en-us_topic_0096561549_p10245320142912"></a><a name="en-us_topic_0096561549_p10245320142912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p159441556659"><a name="en-us_topic_0096561549_p159441556659"></a><a name="en-us_topic_0096561549_p159441556659"></a>Specifies the ID of the health check configured for the backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row49441756554"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p1594419562516"><a name="en-us_topic_0096561549_p1594419562516"></a><a name="en-us_topic_0096561549_p1594419562516"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p5944135616511"><a name="en-us_topic_0096561549_p5944135616511"></a><a name="en-us_topic_0096561549_p5944135616511"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p114391647141511"><a name="en-us_topic_0096561549_p114391647141511"></a><a name="en-us_topic_0096561549_p114391647141511"></a>Specifies the administrative status of the backend server group.</p>
<p id="en-us_topic_0096561549_p2458849201516"><a name="en-us_topic_0096561549_p2458849201516"></a><a name="en-us_topic_0096561549_p2458849201516"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0096561549_b1758963513112"><a name="en-us_topic_0096561549_b1758963513112"></a><a name="en-us_topic_0096561549_b1758963513112"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row0944135615511"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p15944165613512"><a name="en-us_topic_0096561549_p15944165613512"></a><a name="en-us_topic_0096561549_p15944165613512"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p59448565512"><a name="en-us_topic_0096561549_p59448565512"></a><a name="en-us_topic_0096561549_p59448565512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p12944125619511"><a name="en-us_topic_0096561549_p12944125619511"></a><a name="en-us_topic_0096561549_p12944125619511"></a>Lists the IDs of listeners associated with the backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row494419564513"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p594495614516"><a name="en-us_topic_0096561549_p594495614516"></a><a name="en-us_topic_0096561549_p594495614516"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p694413561519"><a name="en-us_topic_0096561549_p694413561519"></a><a name="en-us_topic_0096561549_p694413561519"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p189451656658"><a name="en-us_topic_0096561549_p189451656658"></a><a name="en-us_topic_0096561549_p189451656658"></a>Lists the IDs of load balancers associated with the backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row209451156154"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p16945185612516"><a name="en-us_topic_0096561549_p16945185612516"></a><a name="en-us_topic_0096561549_p16945185612516"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p109451564513"><a name="en-us_topic_0096561549_p109451564513"></a><a name="en-us_topic_0096561549_p109451564513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p18458175215155"><a name="en-us_topic_0096561549_p18458175215155"></a><a name="en-us_topic_0096561549_p18458175215155"></a>Specifies whether to enable the sticky session feature. For details, see <a href="adding-a-backend-server-group.md#table1659974218492">Table 6</a>.</p>
<p id="en-us_topic_0096561549_p166781654171513"><a name="en-us_topic_0096561549_p166781654171513"></a><a name="en-us_topic_0096561549_p166781654171513"></a>Once the sticky session feature is enabled, requests from the same client are sent to the same backend server within the specified period.</p>
<p id="en-us_topic_0096561549_p19438135717159"><a name="en-us_topic_0096561549_p19438135717159"></a><a name="en-us_topic_0096561549_p19438135717159"></a>When this feature is disabled, the parameter value is <strong id="en-us_topic_0096561549_b1929513138366"><a name="en-us_topic_0096561549_b1929513138366"></a><a name="en-us_topic_0096561549_b1929513138366"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **session\_persistence**  parameter description

<a name="table1925152813472"></a>
<table><thead align="left"><tr id="en-us_topic_0096561549_row12652114216495"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561549_p8652134218493"><a name="en-us_topic_0096561549_p8652134218493"></a><a name="en-us_topic_0096561549_p8652134218493"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561549_p965284214496"><a name="en-us_topic_0096561549_p965284214496"></a><a name="en-us_topic_0096561549_p965284214496"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561549_p3652164264914"><a name="en-us_topic_0096561549_p3652164264914"></a><a name="en-us_topic_0096561549_p3652164264914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561549_row16652114264914"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p106528426495"><a name="en-us_topic_0096561549_p106528426495"></a><a name="en-us_topic_0096561549_p106528426495"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p665216429491"><a name="en-us_topic_0096561549_p665216429491"></a><a name="en-us_topic_0096561549_p665216429491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p1082720181618"><a name="en-us_topic_0096561549_p1082720181618"></a><a name="en-us_topic_0096561549_p1082720181618"></a>Specifies the sticky session type.</p>
<div class="p" id="en-us_topic_0096561549_p79701533165"><a name="en-us_topic_0096561549_p79701533165"></a><a name="en-us_topic_0096561549_p79701533165"></a>The value can be one of the following:<a name="en-us_topic_0096561549_ul258091011289"></a><a name="en-us_topic_0096561549_ul258091011289"></a><ul id="en-us_topic_0096561549_ul258091011289"><li><strong id="en-us_topic_0096561549_b13160219163613"><a name="en-us_topic_0096561549_b13160219163613"></a><a name="en-us_topic_0096561549_b13160219163613"></a>SOURCE_IP</strong>: Requests are distributed based on the client's IP address. Requests from the same IP address are sent to the same backend server.</li><li><strong id="en-us_topic_0096561549_b13123122818366"><a name="en-us_topic_0096561549_b13123122818366"></a><a name="en-us_topic_0096561549_b13123122818366"></a>HTTP_COOKIE</strong>: When the client sends a request for the first time, the load balancer automatically generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to the backend server that processes the first request.</li><li><strong id="en-us_topic_0096561549_b9757628366"><a name="en-us_topic_0096561549_b9757628366"></a><a name="en-us_topic_0096561549_b9757628366"></a>APP_COOKIE</strong>: When the client sends a request for the first time, the backend server that receives the request generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to this backend server.</li></ul>
</div>
<p id="en-us_topic_0096561549_p1382521641612"><a name="en-us_topic_0096561549_p1382521641612"></a><a name="en-us_topic_0096561549_p1382521641612"></a>When the backend server group protocol is TCP, only <strong id="en-us_topic_0096561549_b9575159612"><a name="en-us_topic_0096561549_b9575159612"></a><a name="en-us_topic_0096561549_b9575159612"></a>SOURCE_IP</strong> takes effect. When the backend server group protocol is HTTP, <strong id="en-us_topic_0096561549_b1758181519614"><a name="en-us_topic_0096561549_b1758181519614"></a><a name="en-us_topic_0096561549_b1758181519614"></a>HTTP_COOKIE</strong> or <strong id="en-us_topic_0096561549_b45814151266"><a name="en-us_topic_0096561549_b45814151266"></a><a name="en-us_topic_0096561549_b45814151266"></a>APP_COOKIE</strong> take effect.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row765217429490"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p26521442114916"><a name="en-us_topic_0096561549_p26521442114916"></a><a name="en-us_topic_0096561549_p26521442114916"></a>cookie_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p16653174214493"><a name="en-us_topic_0096561549_p16653174214493"></a><a name="en-us_topic_0096561549_p16653174214493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p1184122312164"><a name="en-us_topic_0096561549_p1184122312164"></a><a name="en-us_topic_0096561549_p1184122312164"></a>Specifies the cookie name.</p>
<p id="en-us_topic_0096561549_p8672254169"><a name="en-us_topic_0096561549_p8672254169"></a><a name="en-us_topic_0096561549_p8672254169"></a>This parameter is mandatory when the sticky session type is <strong id="en-us_topic_0096561549_b1207136354"><a name="en-us_topic_0096561549_b1207136354"></a><a name="en-us_topic_0096561549_b1207136354"></a>APP_COOKIE</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561549_row268634152316"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561549_p1190604118422"><a name="en-us_topic_0096561549_p1190604118422"></a><a name="en-us_topic_0096561549_p1190604118422"></a>persistence_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561549_p19102413425"><a name="en-us_topic_0096561549_p19102413425"></a><a name="en-us_topic_0096561549_p19102413425"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561549_p31964815179"><a name="en-us_topic_0096561549_p31964815179"></a><a name="en-us_topic_0096561549_p31964815179"></a>Specifies the sticky session timeout duration in minutes.</p>
<p id="en-us_topic_0096561549_p18281115101717"><a name="en-us_topic_0096561549_p18281115101717"></a><a name="en-us_topic_0096561549_p18281115101717"></a>This parameter is invalid when <strong id="en-us_topic_0096561549_b20486547017"><a name="en-us_topic_0096561549_b20486547017"></a><a name="en-us_topic_0096561549_b20486547017"></a>type</strong> is set to <strong id="en-us_topic_0096561549_b7485541101"><a name="en-us_topic_0096561549_b7485541101"></a><a name="en-us_topic_0096561549_b7485541101"></a>APP_COOKIE</strong>.</p>
<a name="en-us_topic_0096561549_ul460616103285"></a><a name="en-us_topic_0096561549_ul460616103285"></a><ul id="en-us_topic_0096561549_ul460616103285"><li>Optional value ranges are as follows:<a name="en-us_topic_0096561549_ul19618201052818"></a><a name="en-us_topic_0096561549_ul19618201052818"></a><ul id="en-us_topic_0096561549_ul19618201052818"><li>When the protocol of the backend server group is TCP or UDP, the value ranges from <strong id="en-us_topic_0096561549_b58831904373"><a name="en-us_topic_0096561549_b58831904373"></a><a name="en-us_topic_0096561549_b58831904373"></a>1</strong> to <strong id="en-us_topic_0096561549_b2883005377"><a name="en-us_topic_0096561549_b2883005377"></a><a name="en-us_topic_0096561549_b2883005377"></a>60</strong>.</li><li>When the protocol of the backend server group is HTTP, the value ranges from <strong id="en-us_topic_0096561549_b12263162193715"><a name="en-us_topic_0096561549_b12263162193715"></a><a name="en-us_topic_0096561549_b12263162193715"></a>1</strong> to <strong id="en-us_topic_0096561549_b1226418233720"><a name="en-us_topic_0096561549_b1226418233720"></a><a name="en-us_topic_0096561549_b1226418233720"></a>1440</strong>.</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## **Example**<a name="section1496616510489"></a>

-   Example request: Querying details of a backend server group

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332
    ```


-   Example response

    ```
    {
        "pool": {
            "lb_algorithm": "SOURCE_IP",
            "protocol": "TCP",
            "description": "",
            "admin_state_up": true,
            "loadbalancers": [
                {
                    "id": "6f52004c-3fe9-4c09-b8ce-ed9d9c74a3b1"
                }
            ],
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
            "session_persistence": null,
            "healthmonitor_id": null,
            "listeners": [
                {
                    "id": "6e29b2cd-4e53-40f6-ae7b-29e918de67f2"
                }
            ],
            "members": [],
            "id": "5a9a3e9e-d1aa-448e-af37-a70171f2a332",
            "name": "my-pool"
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139648_section57966003"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

