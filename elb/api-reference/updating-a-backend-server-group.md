# Updating a Backend Server Group<a name="EN-US_TOPIC_0096561550"></a>

## Function<a name="section741261418164"></a>

This API is used to update a backend server group.

## URI<a name="section121706227163"></a>

PUT /v2.0/lbaas/pools/\{pool\_id\}

**Table  1**  Parameter description

<a name="table125651517361"></a>
<table><thead align="left"><tr id="row759911171965"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="p14599717264"><a name="p14599717264"></a><a name="p14599717264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.2"><p id="p311515379220"><a name="p311515379220"></a><a name="p311515379220"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p459951717615"><a name="p459951717615"></a><a name="p459951717615"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="p4599717562"><a name="p4599717562"></a><a name="p4599717562"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17599131712616"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="p1259991716614"><a name="p1259991716614"></a><a name="p1259991716614"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.2 "><p id="p1952694519223"><a name="p1952694519223"></a><a name="p1952694519223"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p259981714617"><a name="p259981714617"></a><a name="p259981714617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p059917171364"><a name="p059917171364"></a><a name="p059917171364"></a>Specifies the backend server group ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139651_section32622215"></a>

If the provisioning status of the load balancer associated with a backend server group is not  **ACTIVE**, the backend server group cannot be updated.

## Request<a name="section2184181416172"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0049139651_table27034686"></a>
<table><thead align="left"><tr id="en-us_topic_0049139651_row36995518"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139651_p43846987"><a name="en-us_topic_0049139651_p43846987"></a><a name="en-us_topic_0049139651_p43846987"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="en-us_topic_0049139651_p61945077"><a name="en-us_topic_0049139651_p61945077"></a><a name="en-us_topic_0049139651_p61945077"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049139651_p51495331"><a name="en-us_topic_0049139651_p51495331"></a><a name="en-us_topic_0049139651_p51495331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.5.1.4"><p id="en-us_topic_0049139651_p10372286"><a name="en-us_topic_0049139651_p10372286"></a><a name="en-us_topic_0049139651_p10372286"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139651_row34848813"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139651_p4181593"><a name="en-us_topic_0049139651_p4181593"></a><a name="en-us_topic_0049139651_p4181593"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p139301821182310"><a name="p139301821182310"></a><a name="p139301821182310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049139651_p55015173"><a name="en-us_topic_0049139651_p55015173"></a><a name="en-us_topic_0049139651_p55015173"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139651_p27044054"><a name="en-us_topic_0049139651_p27044054"></a><a name="en-us_topic_0049139651_p27044054"></a>Specifies the backend server group. For details, see <a href="#table14485185810613">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **pool**  parameter description

<a name="table14485185810613"></a>
<table><thead align="left"><tr id="row858312582062"><th class="cellrowborder" valign="top" width="21.97%" id="mcps1.2.5.1.1"><p id="p205839582611"><a name="p205839582611"></a><a name="p205839582611"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.48%" id="mcps1.2.5.1.2"><p id="p25833581618"><a name="p25833581618"></a><a name="p25833581618"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.59%" id="mcps1.2.5.1.3"><p id="p5583145819611"><a name="p5583145819611"></a><a name="p5583145819611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.96%" id="mcps1.2.5.1.4"><p id="p16583658963"><a name="p16583658963"></a><a name="p16583658963"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row358319589620"><td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.2.5.1.1 "><p id="p858317589618"><a name="p858317589618"></a><a name="p858317589618"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p135833587615"><a name="p135833587615"></a><a name="p135833587615"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.3 "><p id="p135839581262"><a name="p135839581262"></a><a name="p135839581262"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.96%" headers="mcps1.2.5.1.4 "><p id="p12583165814610"><a name="p12583165814610"></a><a name="p12583165814610"></a>Specifies the backend server group name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1158345817618"><td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.2.5.1.1 "><p id="p1258316581464"><a name="p1258316581464"></a><a name="p1258316581464"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p105846581062"><a name="p105846581062"></a><a name="p105846581062"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.3 "><p id="p155838587619"><a name="p155838587619"></a><a name="p155838587619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.96%" headers="mcps1.2.5.1.4 "><p id="p1258485819619"><a name="p1258485819619"></a><a name="p1258485819619"></a>Provides supplementary information about the backend server group.</p>
<p id="p20157153713433"><a name="p20157153713433"></a><a name="p20157153713433"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row2584175810619"><td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.2.5.1.1 "><p id="p14584105817612"><a name="p14584105817612"></a><a name="p14584105817612"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p165843581564"><a name="p165843581564"></a><a name="p165843581564"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.3 "><p id="p1458416581617"><a name="p1458416581617"></a><a name="p1458416581617"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.96%" headers="mcps1.2.5.1.4 "><p id="p18276639182316"><a name="p18276639182316"></a><a name="p18276639182316"></a>Specifies the load balancing algorithm of the backend server group.</p>
<div class="p" id="p17139124172319"><a name="p17139124172319"></a><a name="p17139124172319"></a>Optional values are as follows:<a name="ul12277910111012"></a><a name="ul12277910111012"></a><ul id="ul12277910111012"><li><strong id="b27431853015"><a name="b27431853015"></a><a name="b27431853015"></a>ROUND_ROBIN</strong>: indicates the weighted round robin algorithm.</li><li><strong id="b230413199300"><a name="b230413199300"></a><a name="b230413199300"></a>LEAST_CONNECTIONS</strong>: indicates the weighted least connections algorithm.</li><li><strong id="b623952083015"><a name="b623952083015"></a><a name="b623952083015"></a>SOURCE_IP</strong>: indicates the source IP hash algorithm.</li></ul>
</div>
<p id="p1464864319236"><a name="p1464864319236"></a><a name="p1464864319236"></a>When the value is <strong id="b1410815291381"><a name="b1410815291381"></a><a name="b1410815291381"></a>SOURCE_IP</strong>, the weights of backend servers in the server group are invalid.</p>
</td>
</tr>
<tr id="row5120148105420"><td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.2.5.1.1 "><p id="p6906693"><a name="p6906693"></a><a name="p6906693"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p16333686"><a name="p16333686"></a><a name="p16333686"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.3 "><p id="p22571271"><a name="p22571271"></a><a name="p22571271"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="44.96%" headers="mcps1.2.5.1.4 "><p id="p13387548172315"><a name="p13387548172315"></a><a name="p13387548172315"></a>Specifies the administrative status of the backend server group.</p>
<p id="p134521350142318"><a name="p134521350142318"></a><a name="p134521350142318"></a>This parameter is reserved. The default value is <strong id="b1363812819306"><a name="b1363812819306"></a><a name="b1363812819306"></a>true</strong>.</p>
</td>
</tr>
<tr id="row55841458863"><td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.2.5.1.1 "><p id="p2584858366"><a name="p2584858366"></a><a name="p2584858366"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p75848581613"><a name="p75848581613"></a><a name="p75848581613"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.3 "><p id="p165841458768"><a name="p165841458768"></a><a name="p165841458768"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.96%" headers="mcps1.2.5.1.4 "><p id="p16971654182317"><a name="p16971654182317"></a><a name="p16971654182317"></a>Specifies whether to enable the sticky session feature. For details, see <a href="#table112431127175217">Table 7</a>.</p>
<p id="p16532105712234"><a name="p16532105712234"></a><a name="p16532105712234"></a>Once the sticky session feature is enabled, requests from the same client are sent to the same backend server within the specified period.</p>
<p id="p1718817596235"><a name="p1718817596235"></a><a name="p1718817596235"></a>When this feature is disabled, the parameter value is <strong id="b1773043512308"><a name="b1773043512308"></a><a name="b1773043512308"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **session\_persistence**  parameter description

<a name="table329705085113"></a>
<table><thead align="left"><tr id="row03481650155119"><th class="cellrowborder" valign="top" width="20.22202220222022%" id="mcps1.2.5.1.1"><p id="p15348115011518"><a name="p15348115011518"></a><a name="p15348115011518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.531353135313532%" id="mcps1.2.5.1.2"><p id="p634865014513"><a name="p634865014513"></a><a name="p634865014513"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.861586158615863%" id="mcps1.2.5.1.3"><p id="p163488504515"><a name="p163488504515"></a><a name="p163488504515"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.38503850385039%" id="mcps1.2.5.1.4"><p id="p14291113610259"><a name="p14291113610259"></a><a name="p14291113610259"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23481050175115"><td class="cellrowborder" valign="top" width="20.22202220222022%" headers="mcps1.2.5.1.1 "><p id="p3348165019515"><a name="p3348165019515"></a><a name="p3348165019515"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="13.531353135313532%" headers="mcps1.2.5.1.2 "><p id="p1934895095115"><a name="p1934895095115"></a><a name="p1934895095115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.861586158615863%" headers="mcps1.2.5.1.3 "><p id="p03486500513"><a name="p03486500513"></a><a name="p03486500513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.38503850385039%" headers="mcps1.2.5.1.4 "><p id="p1116881214249"><a name="p1116881214249"></a><a name="p1116881214249"></a>Specifies the sticky session type.</p>
<div class="p" id="p20830101317241"><a name="p20830101317241"></a><a name="p20830101317241"></a>Optional values are as follows:<a name="ul96910511656"></a><a name="ul96910511656"></a><ul id="ul96910511656"><li><strong id="b68831041153013"><a name="b68831041153013"></a><a name="b68831041153013"></a>SOURCE_IP</strong>: Requests are distributed based on the client's IP address. Requests from the same IP address are sent to the same backend server.</li><li><strong id="b6638203143116"><a name="b6638203143116"></a><a name="b6638203143116"></a>HTTP_COOKIE</strong>: When the client sends a request for the first time, the load balancer automatically generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to the backend server that processes the first request.</li><li><strong id="b83362357390"><a name="b83362357390"></a><a name="b83362357390"></a>APP_COOKIE</strong>: When the client sends a request for the first time, the backend server that receives the request generates a cookie and inserts the cookie into the response message. Subsequent requests are sent to this backend server.</li></ul>
</div>
<a name="ul41741356171013"></a><a name="ul41741356171013"></a><ul id="ul41741356171013"><li>When the backend server group protocol is TCP, only <strong id="b159651363319"><a name="b159651363319"></a><a name="b159651363319"></a>SOURCE_IP</strong> takes effect. When the backend server group protocol is HTTP, <strong id="b119661536113119"><a name="b119661536113119"></a><a name="b119661536113119"></a>HTTP_COOKIE</strong> or <strong id="b149661636193115"><a name="b149661636193115"></a><a name="b149661636193115"></a>APP_COOKIE</strong> take effect.</li></ul>
</td>
</tr>
<tr id="row1634835020514"><td class="cellrowborder" valign="top" width="20.22202220222022%" headers="mcps1.2.5.1.1 "><p id="p10348125013511"><a name="p10348125013511"></a><a name="p10348125013511"></a>cookie_name</p>
</td>
<td class="cellrowborder" valign="top" width="13.531353135313532%" headers="mcps1.2.5.1.2 "><p id="p53481350165110"><a name="p53481350165110"></a><a name="p53481350165110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.861586158615863%" headers="mcps1.2.5.1.3 "><p id="p834895012515"><a name="p834895012515"></a><a name="p834895012515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.38503850385039%" headers="mcps1.2.5.1.4 "><p id="p5411141752410"><a name="p5411141752410"></a><a name="p5411141752410"></a>Specifies the cookie name.</p>
<p id="p173618196243"><a name="p173618196243"></a><a name="p173618196243"></a>This parameter is mandatory and can be specified when the sticky session type is <strong id="b788725253811"><a name="b788725253811"></a><a name="b788725253811"></a>APP_COOKIE</strong>.</p>
</td>
</tr>
<tr id="row136223117383"><td class="cellrowborder" valign="top" width="20.22202220222022%" headers="mcps1.2.5.1.1 "><p id="p10835205182919"><a name="p10835205182919"></a><a name="p10835205182919"></a>persistence_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13.531353135313532%" headers="mcps1.2.5.1.2 "><p id="p3836195192911"><a name="p3836195192911"></a><a name="p3836195192911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.861586158615863%" headers="mcps1.2.5.1.3 "><p id="p1883514502914"><a name="p1883514502914"></a><a name="p1883514502914"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.38503850385039%" headers="mcps1.2.5.1.4 "><p id="p183251922192416"><a name="p183251922192416"></a><a name="p183251922192416"></a>Specifies the sticky session timeout duration in minutes.</p>
<p id="p194482248248"><a name="p194482248248"></a><a name="p194482248248"></a>This parameter is invalid when <strong id="b1989235503814"><a name="b1989235503814"></a><a name="b1989235503814"></a>type</strong> is set to <strong id="b48931355173811"><a name="b48931355173811"></a><a name="b48931355173811"></a>APP_COOKIE</strong>.</p>
<div class="p" id="p5774142618249"><a name="p5774142618249"></a><a name="p5774142618249"></a>Optional value ranges are as follows:<a name="ul14784431191918"></a><a name="ul14784431191918"></a><ul id="ul14784431191918"><li>When the protocol of the backend server server is TCP or UDP, the value ranges from <strong id="b1163520433317"><a name="b1163520433317"></a><a name="b1163520433317"></a>1</strong> to <strong id="b116361643183117"><a name="b116361643183117"></a><a name="b116361643183117"></a>60</strong>.</li><li>When the protocol of the backend server group is HTTP, the value ranges from <strong id="b99811250123116"><a name="b99811250123116"></a><a name="b99811250123116"></a>1</strong> to <strong id="b18981185043111"><a name="b18981185043111"></a><a name="b18981185043111"></a>1440</strong>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section15665114415173"></a>

**Table  5**  Parameter description

<a name="en-us_topic_0049139651_table43084804"></a>
<table><thead align="left"><tr id="en-us_topic_0049139651_row15842189"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139651_p8148922"><a name="en-us_topic_0049139651_p8148922"></a><a name="en-us_topic_0049139651_p8148922"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139651_p56082927"><a name="en-us_topic_0049139651_p56082927"></a><a name="en-us_topic_0049139651_p56082927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.4.1.3"><p id="p1384510018264"><a name="p1384510018264"></a><a name="p1384510018264"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139651_row42941906"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139651_p55742394"><a name="en-us_topic_0049139651_p55742394"></a><a name="en-us_topic_0049139651_p55742394"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139651_p18840050"><a name="en-us_topic_0049139651_p18840050"></a><a name="en-us_topic_0049139651_p18840050"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139651_p62150771"><a name="en-us_topic_0049139651_p62150771"></a><a name="en-us_topic_0049139651_p62150771"></a>Specifies the backend server group. For details, see <a href="#table186106238710">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **pools**  parameter description

<a name="table186106238710"></a>
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

**Table  7** **session\_persistence**  parameter description

<a name="table112431127175217"></a>
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

## Example<a name="section112191411111"></a>

-   Example request 1: Updating a backend server group

    ```
    PUT https://{Endpoint}/v2.0/lbaas/pools/12ff63af-4127-4074-a251-bcb2ecc53ebe 
    
    { 
        "pool": { 
            "name": "pool2", 
            "description": "pool two", 
            "lb_algorithm": "LEAST_CONNECTIONS" 
        } 
    }
    ```


-   Example response 1

    ```
    {
        "pool": {
            "lb_algorithm": "LEAST_CONNECTIONS",
            "protocol": "HTTP",
            "description": "pool two",
            "loadbalancers": [
                {
                    "id": "63ad9dfe-4750-479f-9630-ada43ccc8117"
                }
            ],
            "admin_state_up": true,
            "tenant_id": "1a3e005cf9ce40308c900bcb08e5320c",
            "session_persistence": {
                "cookie_name": null,
                "type": "HTTP_COOKIE",
                "persistence_timeout": 1
            },
            "healthmonitor_id": null,
            "listeners": [
                {
                    "id": "39de4d56-d663-46e5-85a1-5b9d5fa17829"
                }
            ],
            "members": [],
            "id": "12ff63af-4127-4074-a251-bcb2ecc53ebe",
            "name": "pool2"
        }
    }
    ```

-   Example request 2: Disabling the sticky session feature of a backend server group

    ```
    PUT https://{Endpoint}/v2.0/lbaas/pools/d46eab56-d76b-4cd3-8952-3c3c4cf113aa
    
    {
        "pool": {
            "session_persistence":null
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
                    "id": "63ad9dfe-4750-479f-9630-ada43ccc8117"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
            "session_persistence": null,
            "healthmonitor_id": null,
            "listeners": [],
            "members": [],
            "id": "d46eab56-d76b-4cd3-8952-3c3c4cf113aa",
            "name": ""
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139651_section16378299"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

