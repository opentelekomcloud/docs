# Adding a Backend Server Group<a name="EN-US_TOPIC_0096561549"></a>

## Function<a name="section488813333155"></a>

This API is used to add a backend server group. After multiple backend servers are added to a backend server group, requests are distributed among backend servers based on the load balancing algorithm configured for the backend server group and the weight set for each backend server.

## URI<a name="section62303417159"></a>

POST /v2.0/lbaas/pools

## Constraints<a name="en-us_topic_0049139649_section52809326"></a>

-   Backend server groups using different protocols cannot be added to the same listener.
-   If parameter  **session-persistence**  is configured, parameter  **cookie\_name**  is available only when the value of  **type**  is  **APP\_COOKIE**.

## Request<a name="section769952881520"></a>

**Table  1**  Request parameters

<a name="en-us_topic_0049139649_table36216906"></a>
<table><thead align="left"><tr id="en-us_topic_0049139649_row55337852"><th class="cellrowborder" valign="top" width="21.357864213578644%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139649_p53181042"><a name="en-us_topic_0049139649_p53181042"></a><a name="en-us_topic_0049139649_p53181042"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.1985801419858%" id="mcps1.2.5.1.2"><p id="en-us_topic_0049139649_p21836431"><a name="en-us_topic_0049139649_p21836431"></a><a name="en-us_topic_0049139649_p21836431"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.108689131086889%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049139649_p12697152"><a name="en-us_topic_0049139649_p12697152"></a><a name="en-us_topic_0049139649_p12697152"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.334866513348665%" id="mcps1.2.5.1.4"><p id="p204001542132510"><a name="p204001542132510"></a><a name="p204001542132510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139649_row58513871"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139649_p42003087"><a name="en-us_topic_0049139649_p42003087"></a><a name="en-us_topic_0049139649_p42003087"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="14.1985801419858%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049139649_p33262233"><a name="en-us_topic_0049139649_p33262233"></a><a name="en-us_topic_0049139649_p33262233"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049139649_p46806896"><a name="en-us_topic_0049139649_p46806896"></a><a name="en-us_topic_0049139649_p46806896"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.334866513348665%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139649_p9886387"><a name="en-us_topic_0049139649_p9886387"></a><a name="en-us_topic_0049139649_p9886387"></a>Specifies the backend server group. For details, see <a href="#table1263319159">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **pool**  parameter description 

<a name="table1263319159"></a>
<table><thead align="left"><tr id="row148461091857"><th class="cellrowborder" valign="top" width="19.98%" id="mcps1.2.5.1.1"><p id="p208461391457"><a name="p208461391457"></a><a name="p208461391457"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.5.1.2"><p id="p9846398519"><a name="p9846398519"></a><a name="p9846398519"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.32%" id="mcps1.2.5.1.3"><p id="p6846791456"><a name="p6846791456"></a><a name="p6846791456"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.59%" id="mcps1.2.5.1.4"><p id="p44213134276"><a name="p44213134276"></a><a name="p44213134276"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1984619916516"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p88461695515"><a name="p88461695515"></a><a name="p88461695515"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p1084618910518"><a name="p1084618910518"></a><a name="p1084618910518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p188466919514"><a name="p188466919514"></a><a name="p188466919514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p11846891258"><a name="p11846891258"></a><a name="p11846891258"></a>Specifies the ID of the project where the backend server group is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p1965918447911"><a name="p1965918447911"></a><a name="p1965918447911"></a>The value must be the same as the value of <strong id="b18165148016"><a name="b18165148016"></a><a name="b18165148016"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row20846149157"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p284639456"><a name="p284639456"></a><a name="p284639456"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p6846189858"><a name="p6846189858"></a><a name="p6846189858"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p16846797514"><a name="p16846797514"></a><a name="p16846797514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p208461591857"><a name="p208461591857"></a><a name="p208461591857"></a>Specifies the backend server group name.</p>
<p id="p25162146396"><a name="p25162146396"></a><a name="p25162146396"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row12847149652"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p884715912511"><a name="p884715912511"></a><a name="p884715912511"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p11847991259"><a name="p11847991259"></a><a name="p11847991259"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p48471091558"><a name="p48471091558"></a><a name="p48471091558"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p108472913513"><a name="p108472913513"></a><a name="p108472913513"></a>Provides supplementary information about the backend server group.</p>
<p id="p2726516103912"><a name="p2726516103912"></a><a name="p2726516103912"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row9847491854"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p1847159356"><a name="p1847159356"></a><a name="p1847159356"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p184759753"><a name="p184759753"></a><a name="p184759753"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p1984759551"><a name="p1984759551"></a><a name="p1984759551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p121005279227"><a name="p121005279227"></a><a name="p121005279227"></a>Specifies the protocol that the backend server group uses to receive requests.</p>
<p id="p187979311223"><a name="p187979311223"></a><a name="p187979311223"></a>TCP, UDP, and HTTP are supported.</p>
<p id="p109081234192220"><a name="p109081234192220"></a><a name="p109081234192220"></a>When a backend server group is added to a specific listener, the relationships between the load balancer protocol and the backend server group protocol are as follows:</p>
<a name="ul118471640122214"></a><a name="ul118471640122214"></a><ul id="ul118471640122214"><li>When the load balancer protocol is <strong id="b104827316296"><a name="b104827316296"></a><a name="b104827316296"></a>UDP</strong>, the backend server group protocol must be <strong id="b148233172911"><a name="b148233172911"></a><a name="b148233172911"></a>UDP</strong>.</li><li>When the load balancer protocol is <strong id="b55824518295"><a name="b55824518295"></a><a name="b55824518295"></a>TCP</strong>, the backend server group protocol must be <strong id="b125821855294"><a name="b125821855294"></a><a name="b125821855294"></a>TCP</strong>.</li><li>When the load balancer protocol is <strong id="b7390280296"><a name="b7390280296"></a><a name="b7390280296"></a>HTTP</strong> or <strong id="b113912812297"><a name="b113912812297"></a><a name="b113912812297"></a>TERMINATED_HTTPS</strong>, the backend server group protocol must be <strong id="b639111832912"><a name="b639111832912"></a><a name="b639111832912"></a>HTTP</strong>.</li></ul>
</td>
</tr>
<tr id="row8847191155"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p28471891959"><a name="p28471891959"></a><a name="p28471891959"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p2847491552"><a name="p2847491552"></a><a name="p2847491552"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p138471197510"><a name="p138471197510"></a><a name="p138471197510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p14750174732220"><a name="p14750174732220"></a><a name="p14750174732220"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="p197431549162210"><a name="p197431549162210"></a><a name="p197431549162210"></a>The value can be one of the following:<a name="ul142123811119"></a><a name="ul142123811119"></a><ul id="ul142123811119"><li><strong id="b935711055713"><a name="b935711055713"></a><a name="b935711055713"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="b61874358576"><a name="b61874358576"></a><a name="b61874358576"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="b9160652165718"><a name="b9160652165718"></a><a name="b9160652165718"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm.</li></ul>
</div>
<p id="p45737526223"><a name="p45737526223"></a><a name="p45737526223"></a>When the value is <strong id="b1588125814818"><a name="b1588125814818"></a><a name="b1588125814818"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid.</p>
</td>
</tr>
<tr id="row1184711916511"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p158471791356"><a name="p158471791356"></a><a name="p158471791356"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p284779659"><a name="p284779659"></a><a name="p284779659"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p684710918519"><a name="p684710918519"></a><a name="p684710918519"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p1265335414227"><a name="p1265335414227"></a><a name="p1265335414227"></a>Specifies the administrative status of the backend server group.</p>
<p id="p3794185692216"><a name="p3794185692216"></a><a name="p3794185692216"></a>This parameter is reserved. The default value is <strong id="b5767112019917"><a name="b5767112019917"></a><a name="b5767112019917"></a>true</strong>.</p>
</td>
</tr>
<tr id="row28477917512"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p1484789054"><a name="p1484789054"></a><a name="p1484789054"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p284718915510"><a name="p284718915510"></a><a name="p284718915510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p1685120531266"><a name="p1685120531266"></a><a name="p1685120531266"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p73704032312"><a name="p73704032312"></a><a name="p73704032312"></a>Specifies the ID of the listener associated with the backend server group.</p>
<p id="p534811219232"><a name="p534811219232"></a><a name="p534811219232"></a>Either <strong id="b81508491193"><a name="b81508491193"></a><a name="b81508491193"></a>listener_id</strong> or <strong id="b1615118491398"><a name="b1615118491398"></a><a name="b1615118491398"></a>loadbalancer_id</strong> must be specified.</p>
</td>
</tr>
<tr id="row7849191658"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p3849391351"><a name="p3849391351"></a><a name="p3849391351"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p08491096510"><a name="p08491096510"></a><a name="p08491096510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p241919557261"><a name="p241919557261"></a><a name="p241919557261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p19931853231"><a name="p19931853231"></a><a name="p19931853231"></a>Specifies the ID of the load balancer associated with the backend server group.</p>
<p id="p1489712782310"><a name="p1489712782310"></a><a name="p1489712782310"></a>Either <strong id="b5953165511916"><a name="b5953165511916"></a><a name="b5953165511916"></a>listener_id</strong> or <strong id="b119544551192"><a name="b119544551192"></a><a name="b119544551192"></a>loadbalancer_id</strong> must be specified.</p>
</td>
</tr>
<tr id="row14849891059"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.5.1.1 "><p id="p158491098517"><a name="p158491098517"></a><a name="p158491098517"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.2 "><p id="p118491092053"><a name="p118491092053"></a><a name="p118491092053"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.32%" headers="mcps1.2.5.1.3 "><p id="p884919555"><a name="p884919555"></a><a name="p884919555"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.59%" headers="mcps1.2.5.1.4 "><p id="p15990791234"><a name="p15990791234"></a><a name="p15990791234"></a>Specifies the sticky session timeout duration in minutes. For details, see <a href="#table168044271458">Table 3</a>.</p>
<p id="p17157712162320"><a name="p17157712162320"></a><a name="p17157712162320"></a>If the value is <strong id="b1526414918108"><a name="b1526414918108"></a><a name="b1526414918108"></a>null</strong>, the sticky session feature is disabled.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **session\_persistence**  parameter description

<a name="table168044271458"></a>
<table><thead align="left"><tr id="row18875271455"><th class="cellrowborder" valign="top" width="20.217978202179783%" id="mcps1.2.5.1.1"><p id="p6887192711513"><a name="p6887192711513"></a><a name="p6887192711513"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.348365163483653%" id="mcps1.2.5.1.2"><p id="p198874276517"><a name="p198874276517"></a><a name="p198874276517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.18858114188581%" id="mcps1.2.5.1.3"><p id="p168878271513"><a name="p168878271513"></a><a name="p168878271513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.24507549245076%" id="mcps1.2.5.1.4"><p id="p08872027454"><a name="p08872027454"></a><a name="p08872027454"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row588772720514"><td class="cellrowborder" valign="top" width="20.217978202179783%" headers="mcps1.2.5.1.1 "><p id="p6887172711519"><a name="p6887172711519"></a><a name="p6887172711519"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.2.5.1.2 "><p id="p1688782715511"><a name="p1688782715511"></a><a name="p1688782715511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.18858114188581%" headers="mcps1.2.5.1.3 "><p id="p588710276512"><a name="p588710276512"></a><a name="p588710276512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.24507549245076%" headers="mcps1.2.5.1.4 "><p id="p19681233142510"><a name="p19681233142510"></a><a name="p19681233142510"></a>Specifies the sticky session type.</p>
<div class="p" id="p297923402516"><a name="p297923402516"></a><a name="p297923402516"></a>The value can be one of the following:<a name="ul96910511656"></a><a name="ul96910511656"></a><ul id="ul96910511656"><li><strong id="b95828597720"><a name="b95828597720"></a><a name="b95828597720"></a>SOURCE_IP</strong>: Requests are distributed based on the client's IP address. Requests from the same IP address are sent to the same backend server.</li><li><strong id="b68641331082"><a name="b68641331082"></a><a name="b68641331082"></a>HTTP_COOKIE</strong>: When the client sends a request for the first time, the load balancer automatically generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to the backend server that processes the first request.</li><li><strong id="b16575810819"><a name="b16575810819"></a><a name="b16575810819"></a>APP_COOKIE</strong>: When the client sends a request for the first time, the backend server that receives the request generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to this backend server.</li></ul>
</div>
<p id="p143821832101217"><a name="p143821832101217"></a><a name="p143821832101217"></a>When the backend server group protocol is TCP, only <strong id="b1748011881415"><a name="b1748011881415"></a><a name="b1748011881415"></a>SOURCE_IP</strong> takes effect. When the backend server group protocol is HTTP, <strong id="b103532318141"><a name="b103532318141"></a><a name="b103532318141"></a>HTTP_COOKIE</strong> or <strong id="b13969626141412"><a name="b13969626141412"></a><a name="b13969626141412"></a>APP_COOKIE</strong> take effect.</p>
</td>
</tr>
<tr id="row1188716271451"><td class="cellrowborder" valign="top" width="20.217978202179783%" headers="mcps1.2.5.1.1 "><p id="p158871927855"><a name="p158871927855"></a><a name="p158871927855"></a>cookie_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.2.5.1.2 "><p id="p1288742719514"><a name="p1288742719514"></a><a name="p1288742719514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.18858114188581%" headers="mcps1.2.5.1.3 "><p id="p08876276516"><a name="p08876276516"></a><a name="p08876276516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.24507549245076%" headers="mcps1.2.5.1.4 "><p id="p74201830102516"><a name="p74201830102516"></a><a name="p74201830102516"></a>Specifies the cookie name.</p>
<p id="p47902276252"><a name="p47902276252"></a><a name="p47902276252"></a>This parameter is mandatory when the sticky session type is <strong id="b1655012542119"><a name="b1655012542119"></a><a name="b1655012542119"></a>APP_COOKIE</strong>.</p>
</td>
</tr>
<tr id="row5123330103411"><td class="cellrowborder" valign="top" width="20.217978202179783%" headers="mcps1.2.5.1.1 "><p id="p10835205182919"><a name="p10835205182919"></a><a name="p10835205182919"></a>persistence_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.2.5.1.2 "><p id="p3836195192911"><a name="p3836195192911"></a><a name="p3836195192911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.18858114188581%" headers="mcps1.2.5.1.3 "><p id="p1883514502914"><a name="p1883514502914"></a><a name="p1883514502914"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.24507549245076%" headers="mcps1.2.5.1.4 "><p id="p79347431251"><a name="p79347431251"></a><a name="p79347431251"></a>Specifies the sticky session timeout duration in minutes.</p>
<p id="p1865846122518"><a name="p1865846122518"></a><a name="p1865846122518"></a>This parameter is invalid when <strong id="b335872616125"><a name="b335872616125"></a><a name="b335872616125"></a>type</strong> is set to <strong id="b1636092617122"><a name="b1636092617122"></a><a name="b1636092617122"></a>APP_COOKIE</strong>.</p>
<div class="p" id="p44301549162511"><a name="p44301549162511"></a><a name="p44301549162511"></a>The value range varies depending on the backend server group protocol:<a name="ul14784431191918"></a><a name="ul14784431191918"></a><ul id="ul14784431191918"><li>When the protocol of the backend server group is TCP or UDP, the value ranges from <strong id="b19673183352516"><a name="b19673183352516"></a><a name="b19673183352516"></a>1</strong> to <strong id="b175187369254"><a name="b175187369254"></a><a name="b175187369254"></a>60</strong>.</li><li>When the protocol of the backend server group is HTTP, the value ranges from <strong id="b146571880262"><a name="b146571880262"></a><a name="b146571880262"></a>1</strong> to <strong id="b6511121342614"><a name="b6511121342614"></a><a name="b6511121342614"></a>1440</strong>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section09871086161"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0049139649_table26528280"></a>
<table><thead align="left"><tr id="en-us_topic_0049139649_row4346180"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139649_p16496329"><a name="en-us_topic_0049139649_p16496329"></a><a name="en-us_topic_0049139649_p16496329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139649_p61134295"><a name="en-us_topic_0049139649_p61134295"></a><a name="en-us_topic_0049139649_p61134295"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139649_p59539371"><a name="en-us_topic_0049139649_p59539371"></a><a name="en-us_topic_0049139649_p59539371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139649_row57959746"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139649_p64227841"><a name="en-us_topic_0049139649_p64227841"></a><a name="en-us_topic_0049139649_p64227841"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139649_p35072657"><a name="en-us_topic_0049139649_p35072657"></a><a name="en-us_topic_0049139649_p35072657"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139649_p62521411"><a name="en-us_topic_0049139649_p62521411"></a><a name="en-us_topic_0049139649_p62521411"></a>Specifies the backend server group. For details, see <a href="#table549816561954">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **pools**  parameter description

<a name="table549816561954"></a>
<table><thead align="left"><tr id="row129412056850"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p8941556758"><a name="p8941556758"></a><a name="p8941556758"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p5941205616511"><a name="p5941205616511"></a><a name="p5941205616511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p19941155610513"><a name="p19941155610513"></a><a name="p19941155610513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1994112561351"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p6941956051"><a name="p6941956051"></a><a name="p6941956051"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p6395118132915"><a name="p6395118132915"></a><a name="p6395118132915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p394185614510"><a name="p394185614510"></a><a name="p394185614510"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
<tr id="row694135617510"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p18941356653"><a name="p18941356653"></a><a name="p18941356653"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p6942145615514"><a name="p6942145615514"></a><a name="p6942145615514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p133818413522"><a name="p133818413522"></a><a name="p133818413522"></a>Specifies the ID of the project where the backend server group is used.</p>
<p id="p17033816399"><a name="p17033816399"></a><a name="p17033816399"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row189421561755"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p99422562513"><a name="p99422562513"></a><a name="p99422562513"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p169421456857"><a name="p169421456857"></a><a name="p169421456857"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p894213562510"><a name="p894213562510"></a><a name="p894213562510"></a>Specifies the backend server group name.</p>
<p id="p11736124214399"><a name="p11736124214399"></a><a name="p11736124214399"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row7942165615511"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p694235612516"><a name="p694235612516"></a><a name="p694235612516"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p99423564514"><a name="p99423564514"></a><a name="p99423564514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p17942115615520"><a name="p17942115615520"></a><a name="p17942115615520"></a>Provides supplementary information about the backend server group.</p>
<p id="p12272194573912"><a name="p12272194573912"></a><a name="p12272194573912"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row6942115618510"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p129428561458"><a name="p129428561458"></a><a name="p129428561458"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p209421556751"><a name="p209421556751"></a><a name="p209421556751"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p12345548148"><a name="p12345548148"></a><a name="p12345548148"></a>Specifies the protocol that the backend server group uses to receive requests.</p>
<p id="p205871558161412"><a name="p205871558161412"></a><a name="p205871558161412"></a>TCP, UDP, and HTTP are supported.</p>
<p id="p12123121610154"><a name="p12123121610154"></a><a name="p12123121610154"></a>When a backend server group is added to a specific listener, the relationships between the load balancer protocol and the backend server group protocol are as follows:</p>
<a name="ul162192018201516"></a><a name="ul162192018201516"></a><ul id="ul162192018201516"><li>When the load balancer protocol is <strong id="b1432783628"><a name="b1432783628"></a><a name="b1432783628"></a>UDP</strong>, the backend server group protocol must be <strong id="b1237569188"><a name="b1237569188"></a><a name="b1237569188"></a>UDP</strong>.</li><li>When the load balancer protocol is <strong id="b407068730"><a name="b407068730"></a><a name="b407068730"></a>TCP</strong>, the backend server group protocol must be <strong id="b1702959678"><a name="b1702959678"></a><a name="b1702959678"></a>TCP</strong>.</li><li>When the load balancer protocol is <strong id="b1612906869"><a name="b1612906869"></a><a name="b1612906869"></a>HTTP</strong> or <strong id="b837298715"><a name="b837298715"></a><a name="b837298715"></a>TERMINATED_HTTPS</strong>, the backend server group protocol must be <strong id="b808591938"><a name="b808591938"></a><a name="b808591938"></a>HTTP</strong>.</li></ul>
</td>
</tr>
<tr id="row694235612512"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p199426561657"><a name="p199426561657"></a><a name="p199426561657"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p149431356051"><a name="p149431356051"></a><a name="p149431356051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p1190711287157"><a name="p1190711287157"></a><a name="p1190711287157"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="p17447183017153"><a name="p17447183017153"></a><a name="p17447183017153"></a>The value can be one of the following:<a name="ul1064992814235"></a><a name="ul1064992814235"></a><ul id="ul1064992814235"><li><strong id="b1794111372911"><a name="b1794111372911"></a><a name="b1794111372911"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="b16960191417295"><a name="b16960191417295"></a><a name="b16960191417295"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="b8945715182910"><a name="b8945715182910"></a><a name="b8945715182910"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm. When the value is <strong id="b3577112981412"><a name="b3577112981412"></a><a name="b3577112981412"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid.</li></ul>
</div>
</td>
</tr>
<tr id="row1194465616515"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p14944256556"><a name="p14944256556"></a><a name="p14944256556"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p12944656151"><a name="p12944656151"></a><a name="p12944656151"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p139440561151"><a name="p139440561151"></a><a name="p139440561151"></a>Lists the IDs of backend servers in the backend server group.</p>
</td>
</tr>
<tr id="row159441356956"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p17944155618514"><a name="p17944155618514"></a><a name="p17944155618514"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p10245320142912"><a name="p10245320142912"></a><a name="p10245320142912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p159441556659"><a name="p159441556659"></a><a name="p159441556659"></a>Specifies the ID of the health check configured for the backend server group.</p>
</td>
</tr>
<tr id="row49441756554"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1594419562516"><a name="p1594419562516"></a><a name="p1594419562516"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p5944135616511"><a name="p5944135616511"></a><a name="p5944135616511"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p114391647141511"><a name="p114391647141511"></a><a name="p114391647141511"></a>Specifies the administrative status of the backend server group.</p>
<p id="p2458849201516"><a name="p2458849201516"></a><a name="p2458849201516"></a>This parameter is reserved. The default value is <strong id="b1758963513112"><a name="b1758963513112"></a><a name="b1758963513112"></a>true</strong>.</p>
</td>
</tr>
<tr id="row0944135615511"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p15944165613512"><a name="p15944165613512"></a><a name="p15944165613512"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p59448565512"><a name="p59448565512"></a><a name="p59448565512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p12944125619511"><a name="p12944125619511"></a><a name="p12944125619511"></a>Lists the IDs of listeners associated with the backend server group.</p>
</td>
</tr>
<tr id="row494419564513"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p594495614516"><a name="p594495614516"></a><a name="p594495614516"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p694413561519"><a name="p694413561519"></a><a name="p694413561519"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p189451656658"><a name="p189451656658"></a><a name="p189451656658"></a>Lists the IDs of load balancers associated with the backend server group.</p>
</td>
</tr>
<tr id="row209451156154"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p16945185612516"><a name="p16945185612516"></a><a name="p16945185612516"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p109451564513"><a name="p109451564513"></a><a name="p109451564513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p18458175215155"><a name="p18458175215155"></a><a name="p18458175215155"></a>Specifies whether to enable the sticky session feature. For details, see <a href="#table1659974218492">Table 6</a>.</p>
<p id="p166781654171513"><a name="p166781654171513"></a><a name="p166781654171513"></a>Once the sticky session feature is enabled, requests from the same client are sent to the same backend server within the specified period.</p>
<p id="p19438135717159"><a name="p19438135717159"></a><a name="p19438135717159"></a>When this feature is disabled, the parameter value is <strong id="b1929513138366"><a name="b1929513138366"></a><a name="b1929513138366"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **session\_persistence**  parameter description

<a name="table1659974218492"></a>
<table><thead align="left"><tr id="row12652114216495"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p8652134218493"><a name="p8652134218493"></a><a name="p8652134218493"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p965284214496"><a name="p965284214496"></a><a name="p965284214496"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="p3652164264914"><a name="p3652164264914"></a><a name="p3652164264914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16652114264914"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p106528426495"><a name="p106528426495"></a><a name="p106528426495"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p665216429491"><a name="p665216429491"></a><a name="p665216429491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p1082720181618"><a name="p1082720181618"></a><a name="p1082720181618"></a>Specifies the sticky session type.</p>
<div class="p" id="p79701533165"><a name="p79701533165"></a><a name="p79701533165"></a>The value can be one of the following:<a name="ul258091011289"></a><a name="ul258091011289"></a><ul id="ul258091011289"><li><strong id="b13160219163613"><a name="b13160219163613"></a><a name="b13160219163613"></a>SOURCE_IP</strong>: Requests are distributed based on the client's IP address. Requests from the same IP address are sent to the same backend server.</li><li><strong id="b13123122818366"><a name="b13123122818366"></a><a name="b13123122818366"></a>HTTP_COOKIE</strong>: When the client sends a request for the first time, the load balancer automatically generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to the backend server that processes the first request.</li><li><strong id="b9757628366"><a name="b9757628366"></a><a name="b9757628366"></a>APP_COOKIE</strong>: When the client sends a request for the first time, the backend server that receives the request generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to this backend server.</li></ul>
</div>
<p id="p1382521641612"><a name="p1382521641612"></a><a name="p1382521641612"></a>When the backend server group protocol is TCP, only <strong id="b9575159612"><a name="b9575159612"></a><a name="b9575159612"></a>SOURCE_IP</strong> takes effect. When the backend server group protocol is HTTP, <strong id="b1758181519614"><a name="b1758181519614"></a><a name="b1758181519614"></a>HTTP_COOKIE</strong> or <strong id="b45814151266"><a name="b45814151266"></a><a name="b45814151266"></a>APP_COOKIE</strong> take effect.</p>
</td>
</tr>
<tr id="row765217429490"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p26521442114916"><a name="p26521442114916"></a><a name="p26521442114916"></a>cookie_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p16653174214493"><a name="p16653174214493"></a><a name="p16653174214493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p1184122312164"><a name="p1184122312164"></a><a name="p1184122312164"></a>Specifies the cookie name.</p>
<p id="p8672254169"><a name="p8672254169"></a><a name="p8672254169"></a>This parameter is mandatory when the sticky session type is <strong id="b567882366"><a name="b567882366"></a><a name="b567882366"></a>APP_COOKIE</strong>.</p>
</td>
</tr>
<tr id="row268634152316"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1190604118422"><a name="p1190604118422"></a><a name="p1190604118422"></a>persistence_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p19102413425"><a name="p19102413425"></a><a name="p19102413425"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p31964815179"><a name="p31964815179"></a><a name="p31964815179"></a>Specifies the sticky session timeout duration in minutes.</p>
<p id="p18281115101717"><a name="p18281115101717"></a><a name="p18281115101717"></a>This parameter is invalid when <strong id="b20486547017"><a name="b20486547017"></a><a name="b20486547017"></a>type</strong> is set to <strong id="b7485541101"><a name="b7485541101"></a><a name="b7485541101"></a>APP_COOKIE</strong>.</p>
<a name="ul460616103285"></a><a name="ul460616103285"></a><ul id="ul460616103285"><li>Optional value ranges are as follows:<a name="ul19618201052818"></a><a name="ul19618201052818"></a><ul id="ul19618201052818"><li>When the protocol of the backend server group is TCP or UDP, the value ranges from <strong id="b58831904373"><a name="b58831904373"></a><a name="b58831904373"></a>1</strong> to <strong id="b2883005377"><a name="b2883005377"></a><a name="b2883005377"></a>60</strong>.</li><li>When the protocol of the backend server group is HTTP, the value ranges from <strong id="b12263162193715"><a name="b12263162193715"></a><a name="b12263162193715"></a>1</strong> to <strong id="b1226418233720"><a name="b1226418233720"></a><a name="b1226418233720"></a>1440</strong>.</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section550584316282"></a>

-   Example request 1: Adding a backend server group with the sticky session feature disabled

    ```
    POST https://{Endpoint}/v2.0/lbaas/pools 
    
    {
        "pool": {
            "lb_algorithm":"ROUND_ROBIN",
            "loadbalancer_id": "63ad9dfe-4750-479f-9630-ada43ccc8117",
            "protocol":"HTTP"
        }
    }
    ```


-   Example response 1

    ```
    {
        "pool": {
            "lb_algorithm": "ROUND_ROBIN",
            "protocol": "HTTP",
            "description": "",
            "admin_state_up": true,
            "loadbalancers": [
                {
                    "id": "63ad9dfe-4750-479f-9630-ada43ccc8117"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
            "session_persistence": null,
            "healthmonitor_id": null,
            "listeners": [],
            "members": [],
            "id": "4e496951-befb-47bf-9573-c1cd11825c07",
            "name": ""
        }
    }
    ```

-   Example request 2: Adding an HTTP backend server group with the value of  **type**  set to  **APP\_COOKIE**

    ```
    POST https://{Endpoint}/v2.0/lbaas/pools 
    
    { 
      "pool": { 
        "lb_algorithm": "ROUND_ROBIN", 
        "listener_id": "370fb112-e920-486a-b051-1d0d30704dd3", 
        "protocol": "HTTP", 
        "session_persistence": { 
          "cookie_name": "my_cookie", 
          "type": "APP_COOKIE", 
          "persistence_timeout": 1 
        }, 
        "admin_state_up": true 
      } 
    }
    ```

-   Example response 2

    ```
    { 
      "pool": { 
        "lb_algorithm": "ROUND_ROBIN", 
        "protocol": "HTTP", 
        "description": "", 
        "admin_state_up": true, 
        "loadbalancers": [ 
          { 
            "id": "6b041b9e-976b-40ba-b075-375be6110b53" 
          } 
        ], 
        "tenant_id": "145483a5107745e9b3d80f956713e6a3", 
     
        "session_persistence": { 
          "cookie_name": "my_cookie", 
          "type": "APP_COOKIE", 
          "persistence_timeout": 1 
        }, 
        "healthmonitor_id": null, 
        "listeners": [ 
          { 
            "id": "370fb112-e920-486a-b051-1d0d30704dd3" 
          } 
        ], 
        "members": [ 
     
        ], 
        "id": "307f8968-9474-4d0c-8434-66be09dabcc1", 
        "name": "" 
      } 
    } 
    ```

-   Example request 3: Adding an HTTP backend server group with the value of  **type**  set to  **HTTP\_COOKIE**

    ```
    POST https://{Endpoint}/v2.0/lbaas/pools 
    
    {
        "pool": {
            "lb_algorithm":"ROUND_ROBIN",
            "loadbalancer_id": "63ad9dfe-4750-479f-9630-ada43ccc8117",
            "protocol":"HTTP",
            "session_persistence":{
            	"type":"HTTP_COOKIE"
            }
        }
    }
    ```

-   Example response 3

    ```
    {
        "pool": {
            "lb_algorithm": "ROUND_ROBIN",
            "protocol": "HTTP",
            "description": "",
            "admin_state_up": true,
            "loadbalancers": [
                {
                    "id": "63ad9dfe-4750-479f-9630-ada43ccc8117"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
            "session_persistence": {
                "persistence_timeout": 1440,
                "cookie_name": null,
                "type": "HTTP_COOKIE"
            },
            "healthmonitor_id": null,
            "listeners": [],
            "members": [],
            "id": "d46eab56-d76b-4cd3-8952-3c3c4cf113aa",
            "name": ""
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139649_section57465365"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

