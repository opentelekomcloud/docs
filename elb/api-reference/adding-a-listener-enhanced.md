# Adding a Listener<a name="EN-US_TOPIC_0096561542"></a>

## Function<a name="en-us_topic_0049139642_section1462819"></a>

This API is used to add a listener to a load balancer.

## URI<a name="en-us_topic_0049139642_section13165375"></a>

POST /v2.0/lbaas/listeners

## Constraints<a name="en-us_topic_0049139642_section51379511"></a>

When  **protocol**  is set to  **TCP**  and  **protocol\_port**  to  **0**, the listener works in IP mode \(DR mode\).

## Request<a name="section112126467011"></a>

**Table  1**  Request parameters

<a name="table122881844161815"></a>
<table><thead align="left"><tr id="row1528814471819"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.1"><p id="p02881944101816"><a name="p02881944101816"></a><a name="p02881944101816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.389999999999999%" id="mcps1.2.5.1.2"><p id="p9288104491819"><a name="p9288104491819"></a><a name="p9288104491819"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.1%" id="mcps1.2.5.1.3"><p id="p1628844491814"><a name="p1628844491814"></a><a name="p1628844491814"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.2.5.1.4"><p id="p112889445184"><a name="p112889445184"></a><a name="p112889445184"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19289114471819"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.1 "><p id="p14289344171817"><a name="p14289344171817"></a><a name="p14289344171817"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.2 "><p id="p1928964471819"><a name="p1928964471819"></a><a name="p1928964471819"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.1%" headers="mcps1.2.5.1.3 "><p id="p19272639181111"><a name="p19272639181111"></a><a name="p19272639181111"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.2.5.1.4 "><p id="p142892443189"><a name="p142892443189"></a><a name="p142892443189"></a>Specifies the listener. For details, see <a href="#table3499100135410">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **listener**  parameter description

<a name="table3499100135410"></a>
<table><thead align="left"><tr id="row064317014542"><th class="cellrowborder" valign="top" width="21.099999999999998%" id="mcps1.2.5.1.1"><p id="p18643190205416"><a name="p18643190205416"></a><a name="p18643190205416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.61%" id="mcps1.2.5.1.2"><p id="p1564318075420"><a name="p1564318075420"></a><a name="p1564318075420"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.26%" id="mcps1.2.5.1.3"><p id="p86431055413"><a name="p86431055413"></a><a name="p86431055413"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.03%" id="mcps1.2.5.1.4"><p id="p1664316014546"><a name="p1664316014546"></a><a name="p1664316014546"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row864310075414"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p16643140135418"><a name="p16643140135418"></a><a name="p16643140135418"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p13644150165414"><a name="p13644150165414"></a><a name="p13644150165414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p3643170135418"><a name="p3643170135418"></a><a name="p3643170135418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p1564410175417"><a name="p1564410175417"></a><a name="p1564410175417"></a>Specifies the ID of the project where the listener is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p2038118462238"><a name="p2038118462238"></a><a name="p2038118462238"></a>The value must be the same as the value of <strong id="b19143931716"><a name="b19143931716"></a><a name="b19143931716"></a>project_id</strong> in the token.</p>
<p id="p38262421513"><a name="p38262421513"></a><a name="p38262421513"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1964412016546"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p064410165412"><a name="p064410165412"></a><a name="p064410165412"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p146444045415"><a name="p146444045415"></a><a name="p146444045415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p46441102547"><a name="p46441102547"></a><a name="p46441102547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p106444014545"><a name="p106444014545"></a><a name="p106444014545"></a>Specifies the listener name.</p>
<p id="p84618511617"><a name="p84618511617"></a><a name="p84618511617"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row464412025415"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p06447018548"><a name="p06447018548"></a><a name="p06447018548"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p56441504543"><a name="p56441504543"></a><a name="p56441504543"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p116441301547"><a name="p116441301547"></a><a name="p116441301547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p206440012544"><a name="p206440012544"></a><a name="p206440012544"></a>Provides supplementary information about the listener.</p>
<p id="p16635135313117"><a name="p16635135313117"></a><a name="p16635135313117"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row196444065412"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p1644150175410"><a name="p1644150175410"></a><a name="p1644150175410"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p462249153815"><a name="p462249153815"></a><a name="p462249153815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p2644807540"><a name="p2644807540"></a><a name="p2644807540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p1434418339294"><a name="p1434418339294"></a><a name="p1434418339294"></a>Specifies the load balancer protocol.</p>
<p id="p1342193518290"><a name="p1342193518290"></a><a name="p1342193518290"></a>The value can be <strong id="b37719544155919"><a name="b37719544155919"></a><a name="b37719544155919"></a>TCP</strong>, <strong id="b3931576155919"><a name="b3931576155919"></a><a name="b3931576155919"></a>HTTP</strong>, <strong id="b842352706155831"><a name="b842352706155831"></a><a name="b842352706155831"></a>UDP</strong>, or <strong id="b148866620519381"><a name="b148866620519381"></a><a name="b148866620519381"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row12644103548"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p156445075418"><a name="p156445075418"></a><a name="p156445075418"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p1064515019547"><a name="p1064515019547"></a><a name="p1064515019547"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p146441802549"><a name="p146441802549"></a><a name="p146441802549"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p1305737162912"><a name="p1305737162912"></a><a name="p1305737162912"></a>Specifies the port used by the load balancer.</p>
<p id="p17184113813293"><a name="p17184113813293"></a><a name="p17184113813293"></a>The port number ranges from 1 to 65535.</p>
<div class="note" id="note283220448294"><a name="note283220448294"></a><a name="note283220448294"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p158337444299"><a name="p158337444299"></a><a name="p158337444299"></a>If the listener protocol is UDP, the port number cannot be 4789.</p>
</div></div>
</td>
</tr>
<tr id="row106459010540"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p364512016547"><a name="p364512016547"></a><a name="p364512016547"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p136451407547"><a name="p136451407547"></a><a name="p136451407547"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p1032993444813"><a name="p1032993444813"></a><a name="p1032993444813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p3645170135410"><a name="p3645170135410"></a><a name="p3645170135410"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="row13645509545"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p6645120145417"><a name="p6645120145417"></a><a name="p6645120145417"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p16573171183812"><a name="p16573171183812"></a><a name="p16573171183812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p12645902548"><a name="p12645902548"></a><a name="p12645902548"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p35248213012"><a name="p35248213012"></a><a name="p35248213012"></a>Specifies the maximum number of connections.</p>
<p id="p0590933306"><a name="p0590933306"></a><a name="p0590933306"></a>The value ranges from <strong id="b842352706194030"><a name="b842352706194030"></a><a name="b842352706194030"></a>-1</strong> to <strong id="b842352706194035"><a name="b842352706194035"></a><a name="b842352706194035"></a>2147483647</strong>. The default value is <strong id="b6898417171220"><a name="b6898417171220"></a><a name="b6898417171220"></a>-1</strong>, indicating that there is no restriction on maximum connections.</p>
<p id="p176373514306"><a name="p176373514306"></a><a name="p176373514306"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row1264500115411"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p8645708547"><a name="p8645708547"></a><a name="p8645708547"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p12390167113820"><a name="p12390167113820"></a><a name="p12390167113820"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p96457019548"><a name="p96457019548"></a><a name="p96457019548"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p4676198103013"><a name="p4676198103013"></a><a name="p4676198103013"></a>Specifies the administrative status of the listener.</p>
<p id="p136141610163013"><a name="p136141610163013"></a><a name="p136141610163013"></a>This parameter is reserved. The value can only be <strong id="b831363601917"><a name="b831363601917"></a><a name="b831363601917"></a>true</strong>.</p>
</td>
</tr>
<tr id="row92631030637"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p852915407320"><a name="p852915407320"></a><a name="p852915407320"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p19530104019310"><a name="p19530104019310"></a><a name="p19530104019310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p353015409313"><a name="p353015409313"></a><a name="p353015409313"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p427111614307"><a name="p427111614307"></a><a name="p427111614307"></a>Specifies whether to use HTTP/2.</p>
<p id="p1217445083313"><a name="p1217445083313"></a><a name="p1217445083313"></a>The value can be <strong id="b417475083318"><a name="b417475083318"></a><a name="b417475083318"></a>true</strong> or <strong id="b131741450173320"><a name="b131741450173320"></a><a name="b131741450173320"></a>false</strong>.</p>
<a name="ul84755623314"></a><a name="ul84755623314"></a><ul id="ul84755623314"><li><strong id="b1246356143314"><a name="b1246356143314"></a><a name="b1246356143314"></a>true</strong>: HTTP/2 is used.</li><li><strong id="b1311758113320"><a name="b1311758113320"></a><a name="b1311758113320"></a>false</strong>: HTTP/2 is not used.</li></ul>
<p id="p1547317505556"><a name="p1547317505556"></a><a name="p1547317505556"></a>The default value is <strong id="b1755343613127"><a name="b1755343613127"></a><a name="b1755343613127"></a>false</strong>.</p>
<p id="p8409182313011"><a name="p8409182313011"></a><a name="p8409182313011"></a>This parameter is valid only when the load balancer protocol is set to <strong id="b243971411113"><a name="b243971411113"></a><a name="b243971411113"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row57349363204"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p1874565118208"><a name="p1874565118208"></a><a name="p1874565118208"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p87451651142014"><a name="p87451651142014"></a><a name="p87451651142014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p1621934644815"><a name="p1621934644815"></a><a name="p1621934644815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p123367270306"><a name="p123367270306"></a><a name="p123367270306"></a>Specifies the ID of the associated backend server group.</p>
<p id="p95518286302"><a name="p95518286302"></a><a name="p95518286302"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="b842352706201335"><a name="b842352706201335"></a><a name="b842352706201335"></a>null</strong>, the listener has no default backend server group.</p>
<div class="p" id="p0582785813"><a name="p0582785813"></a><a name="p0582785813"></a>This parameter has the following constraints:<a name="ul7527145916134"></a><a name="ul7527145916134"></a><ul id="ul7527145916134"><li>Its value cannot be the ID of any backend server group of other listeners.</li><li>Its value cannot be the ID of any backend server group associated with the forwarding policies set for other listeners.</li></ul>
</div>
<div class="p" id="p18499711086"><a name="p18499711086"></a><a name="p18499711086"></a>The relationships between the load balancer protocol and the backend server group protocol are as follows:<a name="ul10547150145714"></a><a name="ul10547150145714"></a><ul id="ul10547150145714"><li>When the load balancer protocol is <strong id="b18591025183313"><a name="b18591025183313"></a><a name="b18591025183313"></a>TCP</strong>, the backend server group protocol must be <strong id="b985813330339"><a name="b985813330339"></a><a name="b985813330339"></a>TCP</strong>.</li><li>When the load balancer protocol is <strong id="b178916472337"><a name="b178916472337"></a><a name="b178916472337"></a>UDP</strong>, the backend server group protocol must be <strong id="b583815116332"><a name="b583815116332"></a><a name="b583815116332"></a>UDP</strong>.</li><li>When the load balancer protocol is <strong id="b842352706203755"><a name="b842352706203755"></a><a name="b842352706203755"></a>HTTP</strong> or <strong id="b842352706203759"><a name="b842352706203759"></a><a name="b842352706203759"></a>TERMINATED_HTTPS</strong>, the backend server group protocol must be <strong id="b6420858143312"><a name="b6420858143312"></a><a name="b6420858143312"></a>HTTP</strong>.</li></ul>
</div>
</td>
</tr>
<tr id="row1172544022017"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p10745151172020"><a name="p10745151172020"></a><a name="p10745151172020"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p1174685116203"><a name="p1174685116203"></a><a name="p1174685116203"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p1874515182018"><a name="p1874515182018"></a><a name="p1874515182018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p18168203914301"><a name="p18168203914301"></a><a name="p18168203914301"></a>Specifies the ID of the server certificate used by the listener. </p>
<p id="p19265194233012"><a name="p19265194233012"></a><a name="p19265194233012"></a>This parameter is mandatory when <strong id="b842352706203838"><a name="b842352706203838"></a><a name="b842352706203838"></a>protocol</strong> is set to <strong id="b842352706203841"><a name="b842352706203841"></a><a name="b842352706203841"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p1746719819484"><a name="p1746719819484"></a><a name="p1746719819484"></a>The default value is <strong id="b431014617404"><a name="b431014617404"></a><a name="b431014617404"></a>null</strong> when <strong id="b5595101012409"><a name="b5595101012409"></a><a name="b5595101012409"></a>protocol</strong> is not set to <strong id="b119501515194012"><a name="b119501515194012"></a><a name="b119501515194012"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p517965328"><a name="p517965328"></a><a name="p517965328"></a>The value contains a maximum of 128 characters.</p>
<div class="note" id="note11834424141915"><a name="note11834424141915"></a><a name="note11834424141915"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4834524191915"><a name="p4834524191915"></a><a name="p4834524191915"></a>This parameter is valid only when <strong id="b1662475311403"><a name="b1662475311403"></a><a name="b1662475311403"></a>protocol</strong> is set to <strong id="b186491812415"><a name="b186491812415"></a><a name="b186491812415"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row867712216579"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p53859232572"><a name="p53859232572"></a><a name="p53859232572"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p938542315573"><a name="p938542315573"></a><a name="p938542315573"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p7385223185710"><a name="p7385223185710"></a><a name="p7385223185710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p1744120112011"><a name="p1744120112011"></a><a name="p1744120112011"></a>Specifies the ID of the CA certificate used by the listener. </p>
<p id="p16389354164819"><a name="p16389354164819"></a><a name="p16389354164819"></a>The default value is <strong id="b59926172414"><a name="b59926172414"></a><a name="b59926172414"></a>null</strong>.</p>
<p id="p53343171428"><a name="p53343171428"></a><a name="p53343171428"></a>The value contains a maximum of 128 characters.</p>
<div class="note" id="note10163165821918"><a name="note10163165821918"></a><a name="note10163165821918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12163155819194"><a name="p12163155819194"></a><a name="p12163155819194"></a>This parameter is valid only when <strong id="b174134182414"><a name="b174134182414"></a><a name="b174134182414"></a>protocol</strong> is set to <strong id="b441419188419"><a name="b441419188419"></a><a name="b441419188419"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1076020151219"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p157613020122"><a name="p157613020122"></a><a name="p157613020122"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p976130161215"><a name="p976130161215"></a><a name="p976130161215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p767224410308"><a name="p767224410308"></a><a name="p767224410308"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
<p id="p18240124723012"><a name="p18240124723012"></a><a name="p18240124723012"></a>If the parameter value is an empty list, the SNI feature is disabled.</p>
<p id="p3793414918"><a name="p3793414918"></a><a name="p3793414918"></a>The default value is <strong id="b183676445413"><a name="b183676445413"></a><a name="b183676445413"></a>[]</strong>.</p>
<div class="note" id="note1034218110209"><a name="note1034218110209"></a><a name="note1034218110209"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7342191102014"><a name="p7342191102014"></a><a name="p7342191102014"></a>This parameter is valid only when <strong id="b686024411418"><a name="b686024411418"></a><a name="b686024411418"></a>protocol</strong> is set to <strong id="b986154410411"><a name="b986154410411"></a><a name="b986154410411"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row145771026185211"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p108551029191718"><a name="p108551029191718"></a><a name="p108551029191718"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.2.5.1.2 "><p id="p1985511298179"><a name="p1985511298179"></a><a name="p1985511298179"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.2.5.1.3 "><p id="p18855429181713"><a name="p18855429181713"></a><a name="p18855429181713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.03%" headers="mcps1.2.5.1.4 "><p id="p39741913115313"><a name="p39741913115313"></a><a name="p39741913115313"></a>Specifies the security policy used by the listener. This parameter is valid only when the load balancer protocol is set to <strong id="b1645319448239"><a name="b1645319448239"></a><a name="b1645319448239"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p567518010317"><a name="p567518010317"></a><a name="p567518010317"></a>The value can be <strong id="b97011824122417"><a name="b97011824122417"></a><a name="b97011824122417"></a>tls-1-0</strong>, <strong id="b181532711249"><a name="b181532711249"></a><a name="b181532711249"></a>tls-1-1</strong>, <strong id="b9944113042418"><a name="b9944113042418"></a><a name="b9944113042418"></a>tls-1-2</strong>, or <strong id="b13993634152413"><a name="b13993634152413"></a><a name="b13993634152413"></a>tls-1-2-strict</strong>, and the default value is <strong id="b1058214842413"><a name="b1058214842413"></a><a name="b1058214842413"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="#table1247813103533">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tls\_ciphers\_policy**  parameter description

<a name="table1247813103533"></a>
<table><thead align="left"><tr id="row204784101539"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.1"><p id="p147851075312"><a name="p147851075312"></a><a name="p147851075312"></a>Security Policy</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="p2478181015313"><a name="p2478181015313"></a><a name="p2478181015313"></a>TLS Version</p>
</th>
<th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="p5478131085310"><a name="p5478131085310"></a><a name="p5478131085310"></a>Cipher Suite</p>
</th>
</tr>
</thead>
<tbody><tr id="row125843182408"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="p12584131812401"><a name="p12584131812401"></a><a name="p12584131812401"></a>tls-1-0</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p1358411811405"><a name="p1358411811405"></a><a name="p1358411811405"></a>TLSv1.2 TLSv1.1 TLSv1</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p152111143203617"><a name="p152111143203617"></a><a name="p152111143203617"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA</p>
</td>
</tr>
<tr id="row1250119222406"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p050232216409"><a name="p050232216409"></a><a name="p050232216409"></a>tls-1-1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p185021822194019"><a name="p185021822194019"></a><a name="p185021822194019"></a>TLSv1.2 TLSv1.1</p>
</td>
</tr>
<tr id="row19159426144017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p31598266400"><a name="p31598266400"></a><a name="p31598266400"></a>tls-1-2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p315914265406"><a name="p315914265406"></a><a name="p315914265406"></a>TLSv1.2</p>
</td>
</tr>
<tr id="row148501331204010"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="p18850153164010"><a name="p18850153164010"></a><a name="p18850153164010"></a>tls-1-2-strict</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p3850531104014"><a name="p3850531104014"></a><a name="p3850531104014"></a>TLSv1.2</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p12274148203711"><a name="p12274148203711"></a><a name="p12274148203711"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1393614221812"></a>

**Table  4**  Response parameters

<a name="table89971153151815"></a>
<table><thead align="left"><tr id="row199855361813"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.4.1.1"><p id="p599818535187"><a name="p599818535187"></a><a name="p599818535187"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="p4998165315188"><a name="p4998165315188"></a><a name="p4998165315188"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.3069306930693%" id="mcps1.2.4.1.3"><p id="p8998175331817"><a name="p8998175331817"></a><a name="p8998175331817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1599914530183"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.4.1.1 "><p id="p0999653151816"><a name="p0999653151816"></a><a name="p0999653151816"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p3999165310187"><a name="p3999165310187"></a><a name="p3999165310187"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.3069306930693%" headers="mcps1.2.4.1.3 "><p id="p799915331810"><a name="p799915331810"></a><a name="p799915331810"></a>Specifies the listener. For details, see <a href="#table5301132505414">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **listeners**  parameter description

<a name="table5301132505414"></a>
<table><thead align="left"><tr id="row34671725195410"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p946792525418"><a name="p946792525418"></a><a name="p946792525418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p8467142519541"><a name="p8467142519541"></a><a name="p8467142519541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.4.1.3"><p id="p104671125165411"><a name="p104671125165411"></a><a name="p104671125165411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12467122519549"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p8467425205419"><a name="p8467425205419"></a><a name="p8467425205419"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p3467192515543"><a name="p3467192515543"></a><a name="p3467192515543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p9467132535416"><a name="p9467132535416"></a><a name="p9467132535416"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="row124679252544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p44682025175413"><a name="p44682025175413"></a><a name="p44682025175413"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p146811253546"><a name="p146811253546"></a><a name="p146811253546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p19468192515548"><a name="p19468192515548"></a><a name="p19468192515548"></a>Specifies the ID of the project where the listener is used.</p>
</td>
</tr>
<tr id="row746816255547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p184683251549"><a name="p184683251549"></a><a name="p184683251549"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1046842519548"><a name="p1046842519548"></a><a name="p1046842519548"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p44681425125418"><a name="p44681425125418"></a><a name="p44681425125418"></a>Specifies the listener name.</p>
</td>
</tr>
<tr id="row1046812512541"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p546862545411"><a name="p546862545411"></a><a name="p546862545411"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p154685252543"><a name="p154685252543"></a><a name="p154685252543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p14468172517540"><a name="p14468172517540"></a><a name="p14468172517540"></a>Provides supplementary information about the listener.</p>
</td>
</tr>
<tr id="row1046832595418"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p17468125125414"><a name="p17468125125414"></a><a name="p17468125125414"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p746811255546"><a name="p746811255546"></a><a name="p746811255546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p201601841193216"><a name="p201601841193216"></a><a name="p201601841193216"></a>Specifies the load balancer protocol.</p>
<p id="p0300344103218"><a name="p0300344103218"></a><a name="p0300344103218"></a>The value can be <strong id="b103871119189"><a name="b103871119189"></a><a name="b103871119189"></a>TCP</strong>, <strong id="b1038921117183"><a name="b1038921117183"></a><a name="b1038921117183"></a>HTTP</strong>, <strong id="b183906115182"><a name="b183906115182"></a><a name="b183906115182"></a>UDP</strong>, or <strong id="b193911311181810"><a name="b193911311181810"></a><a name="b193911311181810"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row1346912520548"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p144691225205414"><a name="p144691225205414"></a><a name="p144691225205414"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p446952515416"><a name="p446952515416"></a><a name="p446952515416"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p18323468323"><a name="p18323468323"></a><a name="p18323468323"></a>Specifies the port used by the load balancer.</p>
<p id="p7688104743213"><a name="p7688104743213"></a><a name="p7688104743213"></a>The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="row1546932511547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p19469202585413"><a name="p19469202585413"></a><a name="p19469202585413"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p546911258548"><a name="p546911258548"></a><a name="p546911258548"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p16788191994017"><a name="p16788191994017"></a><a name="p16788191994017"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="row16469625125411"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p3469112575415"><a name="p3469112575415"></a><a name="p3469112575415"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p144691725185411"><a name="p144691725185411"></a><a name="p144691725185411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p636816504321"><a name="p636816504321"></a><a name="p636816504321"></a>Specifies the maximum number of connections.</p>
<p id="p17992184321313"><a name="p17992184321313"></a><a name="p17992184321313"></a>The value ranges from <strong id="b1262188182"><a name="b1262188182"></a><a name="b1262188182"></a>-1</strong> to <strong id="b182018161820"><a name="b182018161820"></a><a name="b182018161820"></a>2147483647</strong>. The default value is <strong id="b780161918188"><a name="b780161918188"></a><a name="b780161918188"></a>-1</strong>, indicating that there is no restriction on maximum connections.</p>
<p id="p8758551203215"><a name="p8758551203215"></a><a name="p8758551203215"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row44691325175419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p446922525410"><a name="p446922525410"></a><a name="p446922525410"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p3469102512549"><a name="p3469102512549"></a><a name="p3469102512549"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p257371723315"><a name="p257371723315"></a><a name="p257371723315"></a>Specifies the administrative status of the listener.</p>
<p id="p1316712043315"><a name="p1316712043315"></a><a name="p1316712043315"></a>This parameter is reserved. The value can only be <strong id="b17553924141815"><a name="b17553924141815"></a><a name="b17553924141815"></a>true</strong>.</p>
</td>
</tr>
<tr id="row155261945821"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p149771721230"><a name="p149771721230"></a><a name="p149771721230"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p149775217319"><a name="p149775217319"></a><a name="p149775217319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p483792111330"><a name="p483792111330"></a><a name="p483792111330"></a>Specifies whether to use HTTP/2.</p>
<p id="p183584202475"><a name="p183584202475"></a><a name="p183584202475"></a>The value can be <strong id="b53581020204716"><a name="b53581020204716"></a><a name="b53581020204716"></a>true</strong> or <strong id="b93584201473"><a name="b93584201473"></a><a name="b93584201473"></a>false</strong>.</p>
<a name="ul2055452614479"></a><a name="ul2055452614479"></a><ul id="ul2055452614479"><li><strong id="b155372615476"><a name="b155372615476"></a><a name="b155372615476"></a>true</strong>: HTTP/2 is used.</li><li><strong id="b366918288476"><a name="b366918288476"></a><a name="b366918288476"></a>false</strong>: HTTP/2 is not used.</li></ul>
<p id="p3519192712331"><a name="p3519192712331"></a><a name="p3519192712331"></a>This parameter is valid only when the load balancer protocol is set to <strong id="b167901226151113"><a name="b167901226151113"></a><a name="b167901226151113"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row1547012555419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p20470112585411"><a name="p20470112585411"></a><a name="p20470112585411"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p9470525195410"><a name="p9470525195410"></a><a name="p9470525195410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p3466142973313"><a name="p3466142973313"></a><a name="p3466142973313"></a>Specifies the ID of the associated backend server group.</p>
<p id="p149661432143316"><a name="p149661432143316"></a><a name="p149661432143316"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="b125951581919"><a name="b125951581919"></a><a name="b125951581919"></a>null</strong>, the listener has no default backend server group.</p>
</td>
</tr>
<tr id="row94701258544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p114701625185416"><a name="p114701625185416"></a><a name="p114701625185416"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p194705259542"><a name="p194705259542"></a><a name="p194705259542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p8103123513337"><a name="p8103123513337"></a><a name="p8103123513337"></a>Specifies the ID of the server certificate used by the listener. For details, see <a href="certificate-enhanced.md">Certificate</a>.</p>
<p id="p15749173783317"><a name="p15749173783317"></a><a name="p15749173783317"></a>This parameter is mandatory when <strong id="b771517531197"><a name="b771517531197"></a><a name="b771517531197"></a>protocol</strong> is set to <strong id="b11716753181920"><a name="b11716753181920"></a><a name="b11716753181920"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row174701325205420"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p347010254548"><a name="p347010254548"></a><a name="p347010254548"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p4470825185414"><a name="p4470825185414"></a><a name="p4470825185414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p1867105844415"><a name="p1867105844415"></a><a name="p1867105844415"></a>Specifies the ID of the CA certificate used by the listener. For details, see <a href="certificate-enhanced.md">Certificate</a>.</p>
</td>
</tr>
<tr id="row1947122517545"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1247117256543"><a name="p1247117256543"></a><a name="p1247117256543"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p7471172515547"><a name="p7471172515547"></a><a name="p7471172515547"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p33961341163319"><a name="p33961341163319"></a><a name="p33961341163319"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
<p id="p8259184619337"><a name="p8259184619337"></a><a name="p8259184619337"></a>If the parameter value is an empty list, the SNI feature is disabled.</p>
</td>
</tr>
<tr id="row18840123882117"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p38408381214"><a name="p38408381214"></a><a name="p38408381214"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p12840538162110"><a name="p12840538162110"></a><a name="p12840538162110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p19840203842114"><a name="p19840203842114"></a><a name="p19840203842114"></a>Tags the listener.</p>
</td>
</tr>
<tr id="row109815596568"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p18781627124910"><a name="p18781627124910"></a><a name="p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p18781627204916"><a name="p18781627204916"></a><a name="p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p15848951122220"><a name="p15848951122220"></a><a name="p15848951122220"></a>Specifies the time when the listener was created. The UTC time is in <em id="i1017723733015"><a name="i1017723733015"></a><a name="i1017723733015"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="row122703319572"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1541843114495"><a name="p1541843114495"></a><a name="p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1810172112506"><a name="p1810172112506"></a><a name="p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p341843144919"><a name="p341843144919"></a><a name="p341843144919"></a>Specifies the time when the listener was updated. The UTC time is in <em id="i12883301256"><a name="i12883301256"></a><a name="i12883301256"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="row674511497493"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p15804713184311"><a name="p15804713184311"></a><a name="p15804713184311"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p78041413134319"><a name="p78041413134319"></a><a name="p78041413134319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="p546123425013"><a name="p546123425013"></a><a name="p546123425013"></a>Specifies the security policy used by the listener. This parameter is valid only when the load balancer protocol is set to <strong id="b156051134122510"><a name="b156051134122510"></a><a name="b156051134122510"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p3241114918325"><a name="p3241114918325"></a><a name="p3241114918325"></a>The value can be <strong id="b13885173792519"><a name="b13885173792519"></a><a name="b13885173792519"></a>tls-1-0</strong>, <strong id="b15887123752517"><a name="b15887123752517"></a><a name="b15887123752517"></a>tls-1-1</strong>, <strong id="b9887123742520"><a name="b9887123742520"></a><a name="b9887123742520"></a>tls-1-2</strong>, or <strong id="b13889133713252"><a name="b13889133713252"></a><a name="b13889133713252"></a>tls-1-2-strict</strong>, and the default value is <strong id="b2088953792517"><a name="b2088953792517"></a><a name="b2088953792517"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="#table1247813103533">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section3821144893619"></a>

-   Example request 1: Adding a TCP listener

    ```
    POST https://{Endpoint}/v2.0/lbaas/listeners 
    
    {
        "listener": {
            "protocol_port": 80,
            "protocol": "TCP",
            "loadbalancer_id": "0416b6f1-877f-4a51-987e-978b3f084253",
            "name": "listener-test",
            "admin_state_up": true,
        }
    }
    ```


-   Example response 1

    ```
    {
        "listener": {
            "protocol_port": 80,
            "protocol": "TCP",
            "description": "",
            "client_ca_tls_container_ref": null,
            "default_tls_container_ref": null,
            "admin_state_up": true,
            "http2_enable": false,
            "loadbalancers": [
                {
                    "id": "0416b6f1-877f-4a51-987e-978b3f084253"
                }
            ],
            "tenant_id": "145483a5107745e9b3d80f956713e6a3",
            "sni_container_refs": [],
            "connection_limit": -1,
            "default_pool_id": null,
            "tags": [],
            "id": "b7f32b52-6f17-4b16-9ec8-063d71b653ce",
            "name": "listener-test",
            "tls_ciphers_policy": null,
            "created_at": "2018-07-25T01:54:13", 
            "updated_at": "2018-07-25T01:54:14"
        }
    }
    
    ```

-   Example request 2: Adding an HTTPS listener

    ```
    POST https://{Endpoint}/v2.0/lbaas/listeners 
    
    { 
        "listener": { 
            "protocol_port": 25, 
            "protocol": "TERMINATED_HTTPS", 
            "default_tls_container_ref": "02dcd56799e045bf8b131533cc911dd6",
            "loadbalancer_id": "0416b6f1-877f-4a51-987e-978b3f084253", 
            "name": "listener-test", 
            "admin_state_up": true
     
        } 
    }
    ```

-   Example response 2

    ```
    {
        "listener": {
            "protocol_port": 25,
            "protocol": "TERMINATED_HTTPS",
            "description": "",
            "default_tls_container_ref": "02dcd56799e045bf8b131533cc911dd6",
            "sni_container_refs": [],
            "loadbalancers": [
                {
                    "id": "0416b6f1-877f-4a51-987e-978b3f084253"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
      
            "created_at": "2019-01-21T12:38:31",
            "client_ca_tls_container_ref": null,
            "connection_limit": -1,
            "updated_at": "2019-01-21T12:38:31",
            "http2_enable": false,
            "admin_state_up": true,
            "default_pool_id": null,
            "tls_ciphers_policy": "tls-1-0",
            "id": "b56634cd-5ba8-460e-b5a2-6de5ba8eaf60",
            "tags": [],
            "name": "listener-test"
      
        }
    }
    ```

-   Example request 3: Adding a listener with the SNI feature enabled

    ```
    POST https://{Endpoint}/v2.0/lbaas/listeners 
    
    {
        "listener": {
            "protocol_port": 27, 
            "protocol": "TERMINATED_HTTPS", 
            "loadbalancer_id": "6bb85e33-4953-457a-85a9-336d76125b7b", 
            "name": "listener-test", 
            "admin_state_up": true,
            "default_tls_container_ref":"02dcd56799e045bf8b131533cc911dd6",
            "sni_container_refs": ["e15d1b5000474adca383c3cd9ddc06d4",
            	              "5882325fd6dd4b95a88d33238d293a0f"]
        }
    }
    ```

-   Example response 3

    ```
    {
        "listener": {
            "protocol_port": 27,
            "protocol": "TERMINATED_HTTPS",
            "description": "",
            "default_tls_container_ref": "02dcd56799e045bf8b131533cc911dd6",
            "sni_container_refs": [
                "5882325fd6dd4b95a88d33238d293a0f",
                "e15d1b5000474adca383c3cd9ddc06d4"
            ],
            "loadbalancers": [
                {
                    "id": "6bb85e33-4953-457a-85a9-336d76125b7b"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
            "project_id": "601240b9c5c94059b63d484c92cfe308",
            "created_at": "2019-01-21T12:43:55",
            "client_ca_tls_container_ref": null,
            "connection_limit": -1,
            "updated_at": "2019-01-21T12:43:55",
            "http2_enable": false,
            "admin_state_up": true,
            "default_pool_id": null,
            "": "tls-1-0",
            "id": "b2cfda5b-52fe-4320-8845-34e8d4dac2c7",
            "tags": [],
            "name": "listener-test"
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139642_section51272187"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

