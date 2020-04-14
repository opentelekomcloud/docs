# OS::Neutron::LBaaS::Pool<a name="EN-US_TOPIC_0088407173"></a>

The resource is not allowed to be updated.

A resource for managing LBaaS v2 Pools.

This resources manages Neutron-LBaaS v2 Pools, which represent a group of nodes. Pools define the subnet where nodes reside, balancing algorithm, and the nodes themselves.

## Required Properties<a name="section2014711336282"></a>

<a name="table1196091619293"></a>
<table><thead align="left"><tr id="row613701515254"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p29609164299"><a name="p29609164299"></a><a name="p29609164299"></a><strong id="b11716651112313"><a name="b11716651112313"></a><a name="b11716651112313"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p14960916122910"><a name="p14960916122910"></a><a name="p14960916122910"></a><strong id="b1717145132313"><a name="b1717145132313"></a><a name="b1717145132313"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13137181542514"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p10960161618292"><a name="p10960161618292"></a><a name="p10960161618292"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p53096560"><a name="p53096560"></a><a name="p53096560"></a>The algorithm used to distribute load between the members of the pool.</p>
<p id="p8106996"><a name="p8106996"></a><a name="p8106996"></a>String value expected.</p>
<p id="p5854107"><a name="p5854107"></a><a name="p5854107"></a>Can be updated without replacement.</p>
<p id="p52686964"><a name="p52686964"></a><a name="p52686964"></a>Allowed values: ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP</p>
</td>
</tr>
<tr id="row013781515250"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p7960916122912"><a name="p7960916122912"></a><a name="p7960916122912"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p39785709"><a name="p39785709"></a><a name="p39785709"></a>Listener name or ID to be associated with this pool.</p>
<p id="p22527062"><a name="p22527062"></a><a name="p22527062"></a>String value expected.</p>
<p id="p1416966"><a name="p1416966"></a><a name="p1416966"></a>Updates cause replacement.</p>
<p id="p12752694"><a name="p12752694"></a><a name="p12752694"></a>Value must be of type neutron.lbaas.listener</p>
</td>
</tr>
<tr id="row613791542512"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p109613161292"><a name="p109613161292"></a><a name="p109613161292"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p26335266"><a name="p26335266"></a><a name="p26335266"></a>Protocol of the pool. It must be the same as the value of OS::Neutron::LBaaS::Listener's protocol.</p>
<p id="p35690809"><a name="p35690809"></a><a name="p35690809"></a>String value expected.</p>
<p id="p52781827"><a name="p52781827"></a><a name="p52781827"></a>Can not be updated.</p>
<p id="p5274403"><a name="p5274403"></a><a name="p5274403"></a>Allowed values: TCP, HTTP</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section107561841102819"></a>

<a name="table972342614307"></a>
<table><thead align="left"><tr id="row1383723843810"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p472313269303"><a name="p472313269303"></a><a name="p472313269303"></a><strong id="b28161553183811"><a name="b28161553183811"></a><a name="b28161553183811"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p572342620305"><a name="p572342620305"></a><a name="p572342620305"></a><strong id="b58171053163816"><a name="b58171053163816"></a><a name="b58171053163816"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row198374381382"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p10723926203011"><a name="p10723926203011"></a><a name="p10723926203011"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p61666563"><a name="p61666563"></a><a name="p61666563"></a>The administrative state of this pool.</p>
<p id="p18128159"><a name="p18128159"></a><a name="p18128159"></a>Boolean value expected.</p>
<p id="p28935706"><a name="p28935706"></a><a name="p28935706"></a>Updates are not supported.</p>
<p id="p59094765"><a name="p59094765"></a><a name="p59094765"></a>Allowed values: True</p>
</td>
</tr>
<tr id="row5837438153818"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1472318264306"><a name="p1472318264306"></a><a name="p1472318264306"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p21946664"><a name="p21946664"></a><a name="p21946664"></a>Description of this pool.</p>
<p id="p63302249"><a name="p63302249"></a><a name="p63302249"></a>String value expected.</p>
<p id="p32849335"><a name="p32849335"></a><a name="p32849335"></a>Can be updated without replacement.</p>
<p id="p27208562"><a name="p27208562"></a><a name="p27208562"></a>Defaults to " ".</p>
</td>
</tr>
<tr id="row19837113803812"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p17231826143020"><a name="p17231826143020"></a><a name="p17231826143020"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p56409883"><a name="p56409883"></a><a name="p56409883"></a>Name of this pool.</p>
<p id="p37926899"><a name="p37926899"></a><a name="p37926899"></a>String value expected.</p>
<p id="p5797772"><a name="p5797772"></a><a name="p5797772"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row7837938103812"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p9723426113016"><a name="p9723426113016"></a><a name="p9723426113016"></a>session_persistence</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p66966382"><a name="p66966382"></a><a name="p66966382"></a>Configuration of session persistence.</p>
<p id="p65826528"><a name="p65826528"></a><a name="p65826528"></a>Map value expected.</p>
<p id="p55567848"><a name="p55567848"></a><a name="p55567848"></a>Updates cause replacement.</p>
<p id="p30348590"><a name="p30348590"></a><a name="p30348590"></a><em id="i5922205216840"><a name="i5922205216840"></a><a name="i5922205216840"></a>Map properties:</em></p>
<a name="ul42316736"></a><a name="ul42316736"></a><ul id="ul42316736"><li>cookie_name<p id="p5103615"><a name="p5103615"></a><a name="p5103615"></a>Name of the cookie, required if type is APP_COOKIE. It only support cookie_name in the 'APP_COOKIE' type.</p>
<p id="p45932538"><a name="p45932538"></a><a name="p45932538"></a>String value expected.</p>
<p id="p22603405317"><a name="p22603405317"></a><a name="p22603405317"></a>Updates cause replacement.</p>
</li><li>type<p id="p44588724"><a name="p44588724"></a><a name="p44588724"></a>Method of implementation of session persistence feature.</p>
<p id="p65754198"><a name="p65754198"></a><a name="p65754198"></a>String value expected.</p>
<p id="p54916873"><a name="p54916873"></a><a name="p54916873"></a>Updates cause replacement.</p>
<p id="p1092125010310"><a name="p1092125010310"></a><a name="p1092125010310"></a>Allowed values: SOURCE_IP, HTTP_COOKIE, APP_COOKIE</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section103412480286"></a>

<a name="table10916198173216"></a>
<table><thead align="left"><tr id="row6450212184116"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p191718123218"><a name="p191718123218"></a><a name="p191718123218"></a><strong id="b6201122424114"><a name="b6201122424114"></a><a name="b6201122424114"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p9917982327"><a name="p9917982327"></a><a name="p9917982327"></a><strong id="b1202192414413"><a name="b1202192414413"></a><a name="b1202192414413"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row144501312104112"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p3917128183210"><a name="p3917128183210"></a><a name="p3917128183210"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p191714811326"><a name="p191714811326"></a><a name="p191714811326"></a>ID of the health monitor associated with this pool.</p>
</td>
</tr>
<tr id="row14450812164114"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p159171384329"><a name="p159171384329"></a><a name="p159171384329"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p09178812324"><a name="p09178812324"></a><a name="p09178812324"></a>Listener associated with this pool.</p>
</td>
</tr>
<tr id="row12450212104119"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1591719813215"><a name="p1591719813215"></a><a name="p1591719813215"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p291710813322"><a name="p291710813322"></a><a name="p291710813322"></a>Members associated with this pool.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section16759042299"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::LBaaS::Pool
    properties:
      admin_state_up: Boolean
      description: String
      lb_algorithm: String
      listener: String
      name: String
      protocol: String
      session_persistence: {"type": String, "cookie_name": String}
```

