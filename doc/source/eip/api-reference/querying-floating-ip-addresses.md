# Querying Floating IP Addresses<a name="eip_apifloatip_0001"></a>

## Function<a name="en-us_topic_0201534081_section14945458192213"></a>

This API is used to query all floating IP addresses accessible to the tenant submitting the request.

## URI<a name="en-us_topic_0201534081_section494655812215"></a>

GET /v2.0/eip/floatingips\_v6

Example:

```
GET https://{Endpoint}/v2.0/eip/floatingips_v6?id={id}&router_id={router_id}&floating_network_id={floating_network_id}&floating_ip_address={floating_ip_address}&port_id={port_id }&fixed_ip_address={fixed_ip_address}&tenant_id={tenant_id}
```

[Table 1](#en-us_topic_0201534081_table668331194113)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534081_table668331194113"></a>
<table><thead align="left"><tr id="en-us_topic_0201534081_row10685111104111"><th class="cellrowborder" valign="top" width="23.43765623437656%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534081_p0685313416"><a name="en-us_topic_0201534081_p0685313416"></a><a name="en-us_topic_0201534081_p0685313416"></a><strong id="en-us_topic_0201534081_b91094311293"><a name="en-us_topic_0201534081_b91094311293"></a><a name="en-us_topic_0201534081_b91094311293"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.37906209379062%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534081_p768561134110"><a name="en-us_topic_0201534081_p768561134110"></a><a name="en-us_topic_0201534081_p768561134110"></a><strong id="en-us_topic_0201534081_b5814142784412"><a name="en-us_topic_0201534081_b5814142784412"></a><a name="en-us_topic_0201534081_b5814142784412"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.43765623437656%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534081_p368681134120"><a name="en-us_topic_0201534081_p368681134120"></a><a name="en-us_topic_0201534081_p368681134120"></a><strong id="en-us_topic_0201534081_b994730174413"><a name="en-us_topic_0201534081_b994730174413"></a><a name="en-us_topic_0201534081_b994730174413"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.745625437456255%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534081_p668612124119"><a name="en-us_topic_0201534081_p668612124119"></a><a name="en-us_topic_0201534081_p668612124119"></a><strong id="en-us_topic_0201534081_b1313533174414"><a name="en-us_topic_0201534081_b1313533174414"></a><a name="en-us_topic_0201534081_b1313533174414"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534081_row3686171204116"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p176864111411"><a name="en-us_topic_0201534081_p176864111411"></a><a name="en-us_topic_0201534081_p176864111411"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p136865110419"><a name="en-us_topic_0201534081_p136865110419"></a><a name="en-us_topic_0201534081_p136865110419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p16861211413"><a name="en-us_topic_0201534081_p16861211413"></a><a name="en-us_topic_0201534081_p16861211413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p1068611114119"><a name="en-us_topic_0201534081_p1068611114119"></a><a name="en-us_topic_0201534081_p1068611114119"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row19686619418"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p868615164111"><a name="en-us_topic_0201534081_p868615164111"></a><a name="en-us_topic_0201534081_p868615164111"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p1468611134120"><a name="en-us_topic_0201534081_p1468611134120"></a><a name="en-us_topic_0201534081_p1468611134120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p1668716114415"><a name="en-us_topic_0201534081_p1668716114415"></a><a name="en-us_topic_0201534081_p1668716114415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p76878124112"><a name="en-us_topic_0201534081_p76878124112"></a><a name="en-us_topic_0201534081_p76878124112"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row126871811412"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p1668781104117"><a name="en-us_topic_0201534081_p1668781104117"></a><a name="en-us_topic_0201534081_p1668781104117"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p1668731204116"><a name="en-us_topic_0201534081_p1668731204116"></a><a name="en-us_topic_0201534081_p1668731204116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p1687610411"><a name="en-us_topic_0201534081_p1687610411"></a><a name="en-us_topic_0201534081_p1687610411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p14687611411"><a name="en-us_topic_0201534081_p14687611411"></a><a name="en-us_topic_0201534081_p14687611411"></a>Specifies the external network ID.</p>
<p id="en-us_topic_0201534081_p4687818419"><a name="en-us_topic_0201534081_p4687818419"></a><a name="en-us_topic_0201534081_p4687818419"></a>You can only use fixed external network. </p>
<p id="en-us_topic_0201534081_p9687151144115"><a name="en-us_topic_0201534081_p9687151144115"></a><a name="en-us_topic_0201534081_p9687151144115"></a>You can use <strong id="en-us_topic_0201534081_b16947183205511"><a name="en-us_topic_0201534081_b16947183205511"></a><a name="en-us_topic_0201534081_b16947183205511"></a>GET /v2.0/networks?router:external=True</strong> or</p>
<p id="en-us_topic_0201534081_p1568711118416"><a name="en-us_topic_0201534081_p1568711118416"></a><a name="en-us_topic_0201534081_p1568711118416"></a><strong id="en-us_topic_0201534081_b1132415435015"><a name="en-us_topic_0201534081_b1132415435015"></a><a name="en-us_topic_0201534081_b1132415435015"></a>GET /v2.0/networks?name={floating_network}</strong> or run the <strong id="en-us_topic_0201534081_b14326354145013"><a name="en-us_topic_0201534081_b14326354145013"></a><a name="en-us_topic_0201534081_b14326354145013"></a>neutron net-external-list</strong> command to obtain information about the external network. </p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row5687814417"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p106871419413"><a name="en-us_topic_0201534081_p106871419413"></a><a name="en-us_topic_0201534081_p106871419413"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p1268712115416"><a name="en-us_topic_0201534081_p1268712115416"></a><a name="en-us_topic_0201534081_p1268712115416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p6687015419"><a name="en-us_topic_0201534081_p6687015419"></a><a name="en-us_topic_0201534081_p6687015419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p668714111415"><a name="en-us_topic_0201534081_p668714111415"></a><a name="en-us_topic_0201534081_p668714111415"></a>Specifies the ID of the belonged router. </p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row116871516414"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p1868717104113"><a name="en-us_topic_0201534081_p1868717104113"></a><a name="en-us_topic_0201534081_p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p26871119419"><a name="en-us_topic_0201534081_p26871119419"></a><a name="en-us_topic_0201534081_p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p66889116414"><a name="en-us_topic_0201534081_p66889116414"></a><a name="en-us_topic_0201534081_p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p14688213413"><a name="en-us_topic_0201534081_p14688213413"></a><a name="en-us_topic_0201534081_p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row1168817194115"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p868818134116"><a name="en-us_topic_0201534081_p868818134116"></a><a name="en-us_topic_0201534081_p868818134116"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p568817111417"><a name="en-us_topic_0201534081_p568817111417"></a><a name="en-us_topic_0201534081_p568817111417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p96881617413"><a name="en-us_topic_0201534081_p96881617413"></a><a name="en-us_topic_0201534081_p96881617413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p1668816118413"><a name="en-us_topic_0201534081_p1668816118413"></a><a name="en-us_topic_0201534081_p1668816118413"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row116884115417"><td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534081_p968813113416"><a name="en-us_topic_0201534081_p968813113416"></a><a name="en-us_topic_0201534081_p968813113416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="9.37906209379062%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534081_p468815111414"><a name="en-us_topic_0201534081_p468815111414"></a><a name="en-us_topic_0201534081_p468815111414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="23.43765623437656%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534081_p12688141154119"><a name="en-us_topic_0201534081_p12688141154119"></a><a name="en-us_topic_0201534081_p12688141154119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.745625437456255%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534081_p10487112"><a name="en-us_topic_0201534081_p10487112"></a><a name="en-us_topic_0201534081_p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534081_section5957155814226"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="en-us_topic_0201534081_section2957195852214"></a>

-   Response parameter

**Table  2**  Response parameter

<a name="en-us_topic_0201534081_table395825872218"></a>
<table><thead align="left"><tr id="en-us_topic_0201534081_row15122195992213"><th class="cellrowborder" valign="top" width="15.381538153815383%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534081_p1612211591220"><a name="en-us_topic_0201534081_p1612211591220"></a><a name="en-us_topic_0201534081_p1612211591220"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.072307230723073%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534081_p7122185916226"><a name="en-us_topic_0201534081_p7122185916226"></a><a name="en-us_topic_0201534081_p7122185916226"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.546154615461546%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534081_p512212594226"><a name="en-us_topic_0201534081_p512212594226"></a><a name="en-us_topic_0201534081_p512212594226"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534081_row412225982219"><td class="cellrowborder" valign="top" width="15.381538153815383%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p3122155914223"><a name="en-us_topic_0201534081_p3122155914223"></a><a name="en-us_topic_0201534081_p3122155914223"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="23.072307230723073%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p1112214593223"><a name="en-us_topic_0201534081_p1112214593223"></a><a name="en-us_topic_0201534081_p1112214593223"></a>Array of <a href="#en-us_topic_0201534081_table129961748135412">floatingip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="61.546154615461546%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p10123059152213"><a name="en-us_topic_0201534081_p10123059152213"></a><a name="en-us_topic_0201534081_p10123059152213"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534081_table129961748135412">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floatingip**  objects

<a name="en-us_topic_0201534081_table129961748135412"></a>
<table><thead align="left"><tr id="en-us_topic_0201534081_row5993648185411"><th class="cellrowborder" valign="top" width="24.452445244524455%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534081_p9993174855413"><a name="en-us_topic_0201534081_p9993174855413"></a><a name="en-us_topic_0201534081_p9993174855413"></a><strong id="en-us_topic_0201534081_b727017471321"><a name="en-us_topic_0201534081_b727017471321"></a><a name="en-us_topic_0201534081_b727017471321"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.931793179317932%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534081_p16993194812541"><a name="en-us_topic_0201534081_p16993194812541"></a><a name="en-us_topic_0201534081_p16993194812541"></a><strong id="en-us_topic_0201534081_b146834910215"><a name="en-us_topic_0201534081_b146834910215"></a><a name="en-us_topic_0201534081_b146834910215"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.615761576157624%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534081_p99938485541"><a name="en-us_topic_0201534081_p99938485541"></a><a name="en-us_topic_0201534081_p99938485541"></a><strong id="en-us_topic_0201534081_b150314501422"><a name="en-us_topic_0201534081_b150314501422"></a><a name="en-us_topic_0201534081_b150314501422"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534081_row399444818546"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p109931248105412"><a name="en-us_topic_0201534081_p109931248105412"></a><a name="en-us_topic_0201534081_p109931248105412"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p209935484543"><a name="en-us_topic_0201534081_p209935484543"></a><a name="en-us_topic_0201534081_p209935484543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p1099384811549"><a name="en-us_topic_0201534081_p1099384811549"></a><a name="en-us_topic_0201534081_p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534081_b81252317598"><a name="en-us_topic_0201534081_b81252317598"></a><a name="en-us_topic_0201534081_b81252317598"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534081_b61280316597"><a name="en-us_topic_0201534081_b61280316597"></a><a name="en-us_topic_0201534081_b61280316597"></a>DOWN</strong>, or <strong id="en-us_topic_0201534081_b31301031175917"><a name="en-us_topic_0201534081_b31301031175917"></a><a name="en-us_topic_0201534081_b31301031175917"></a>ERROR</strong>.</p>
<a name="en-us_topic_0201534081_ul10994124825413"></a><a name="en-us_topic_0201534081_ul10994124825413"></a><ul id="en-us_topic_0201534081_ul10994124825413"><li><strong id="en-us_topic_0201534081_b1416416131052"><a name="en-us_topic_0201534081_b1416416131052"></a><a name="en-us_topic_0201534081_b1416416131052"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534081_b377055614519"><a name="en-us_topic_0201534081_b377055614519"></a><a name="en-us_topic_0201534081_b377055614519"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="en-us_topic_0201534081_b165241699718"><a name="en-us_topic_0201534081_b165241699718"></a><a name="en-us_topic_0201534081_b165241699718"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534081_row209948489541"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p6994144818541"><a name="en-us_topic_0201534081_p6994144818541"></a><a name="en-us_topic_0201534081_p6994144818541"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p1399416486549"><a name="en-us_topic_0201534081_p1399416486549"></a><a name="en-us_topic_0201534081_p1399416486549"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p1899418480541"><a name="en-us_topic_0201534081_p1899418480541"></a><a name="en-us_topic_0201534081_p1899418480541"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row99941448115418"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p29942484542"><a name="en-us_topic_0201534081_p29942484542"></a><a name="en-us_topic_0201534081_p29942484542"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p9994348155412"><a name="en-us_topic_0201534081_p9994348155412"></a><a name="en-us_topic_0201534081_p9994348155412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p8994174818549"><a name="en-us_topic_0201534081_p8994174818549"></a><a name="en-us_topic_0201534081_p8994174818549"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row1499474865414"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p119948483548"><a name="en-us_topic_0201534081_p119948483548"></a><a name="en-us_topic_0201534081_p119948483548"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p89942482546"><a name="en-us_topic_0201534081_p89942482546"></a><a name="en-us_topic_0201534081_p89942482546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p59942486544"><a name="en-us_topic_0201534081_p59942486544"></a><a name="en-us_topic_0201534081_p59942486544"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row89951548125411"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p99954487543"><a name="en-us_topic_0201534081_p99954487543"></a><a name="en-us_topic_0201534081_p99954487543"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p1999574817544"><a name="en-us_topic_0201534081_p1999574817544"></a><a name="en-us_topic_0201534081_p1999574817544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p1199594812543"><a name="en-us_topic_0201534081_p1199594812543"></a><a name="en-us_topic_0201534081_p1199594812543"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row1699515482547"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p399515488546"><a name="en-us_topic_0201534081_p399515488546"></a><a name="en-us_topic_0201534081_p399515488546"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p499534814543"><a name="en-us_topic_0201534081_p499534814543"></a><a name="en-us_topic_0201534081_p499534814543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p16995248135411"><a name="en-us_topic_0201534081_p16995248135411"></a><a name="en-us_topic_0201534081_p16995248135411"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row15995124813546"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p2099514875417"><a name="en-us_topic_0201534081_p2099514875417"></a><a name="en-us_topic_0201534081_p2099514875417"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p1599514484541"><a name="en-us_topic_0201534081_p1599514484541"></a><a name="en-us_topic_0201534081_p1599514484541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p6995134819542"><a name="en-us_topic_0201534081_p6995134819542"></a><a name="en-us_topic_0201534081_p6995134819542"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row8996124875412"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p139951748155418"><a name="en-us_topic_0201534081_p139951748155418"></a><a name="en-us_topic_0201534081_p139951748155418"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p209957480545"><a name="en-us_topic_0201534081_p209957480545"></a><a name="en-us_topic_0201534081_p209957480545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p12687170546"><a name="en-us_topic_0201534081_p12687170546"></a><a name="en-us_topic_0201534081_p12687170546"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534081_row4719141983620"><td class="cellrowborder" valign="top" width="24.452445244524455%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534081_p7719171912368"><a name="en-us_topic_0201534081_p7719171912368"></a><a name="en-us_topic_0201534081_p7719171912368"></a>floatingips_links</p>
</td>
<td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534081_p20720819203612"><a name="en-us_topic_0201534081_p20720819203612"></a><a name="en-us_topic_0201534081_p20720819203612"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="57.615761576157624%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534081_p15720419103617"><a name="en-us_topic_0201534081_p15720419103617"></a><a name="en-us_topic_0201534081_p15720419103617"></a>Specifies the request URL.</p>
</td>
</tr>
</tbody>
</table>

-   Example response

    ```
    {
      "floatingips": [
        {
          "id": "861a4c5b-b17b-4a1d-b653-f3e95dcb3345",
          "status": "DOWN",
          "router_id": null,
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "project_id": "26ae5181a416420998eb2093aaed84d9",
          "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
          "fixed_ip_address": null,
          "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c613:16e3",
          "port_id": null,
          "created_at": "2019-03-26T09:52:41",
          "updated_at": "2019-03-26T09:52:45"
        }
      ],
      "floatingips_links": [
        {
          "href": "https://network.region.cn-southwest-2.hwclouds.com/v2.0/floatingips_v6?marker=861a4c5b-b17b-4a1d-b653-f3e95dcb3345&page_reverse=true&page_reverse=True",
          "rel": "previous"
        }
      ]
    }
    ```


## Status Code<a name="en-us_topic_0201534081_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534081_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

