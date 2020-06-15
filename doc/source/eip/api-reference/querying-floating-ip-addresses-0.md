# Querying Floating IP Addresses<a name="eip_openstackapi_0006"></a>

## Function<a name="en-us_topic_0201534068_section310981132148"></a>

This API is used to query all floating IP addresses accessible to the tenant submitting the request. 

You can query the detailed information about a specified floating IP address using the API for  [Querying a Floating IP Address](querying-a-floating-ip-address-1.md#eip_openstackapi_0007).

## URI<a name="en-us_topic_0201534068_section548377002148"></a>

GET /v2.0/floatingips

[Table 1](#en-us_topic_0201534068_table107561756154818)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534068_table107561756154818"></a>
<table><thead align="left"><tr id="en-us_topic_0201534068_row167571556104810"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534068_p0685313416"><a name="en-us_topic_0201534068_p0685313416"></a><a name="en-us_topic_0201534068_p0685313416"></a><strong id="en-us_topic_0201534068_b148411237111018"><a name="en-us_topic_0201534068_b148411237111018"></a><a name="en-us_topic_0201534068_b148411237111018"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534068_p768561134110"><a name="en-us_topic_0201534068_p768561134110"></a><a name="en-us_topic_0201534068_p768561134110"></a><strong id="en-us_topic_0201534068_b95571238181017"><a name="en-us_topic_0201534068_b95571238181017"></a><a name="en-us_topic_0201534068_b95571238181017"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534068_p368681134120"><a name="en-us_topic_0201534068_p368681134120"></a><a name="en-us_topic_0201534068_p368681134120"></a><strong id="en-us_topic_0201534068_b471793991020"><a name="en-us_topic_0201534068_b471793991020"></a><a name="en-us_topic_0201534068_b471793991020"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534068_p668612124119"><a name="en-us_topic_0201534068_p668612124119"></a><a name="en-us_topic_0201534068_p668612124119"></a><strong id="en-us_topic_0201534068_b1198784071014"><a name="en-us_topic_0201534068_b1198784071014"></a><a name="en-us_topic_0201534068_b1198784071014"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534068_row27572562488"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p176864111411"><a name="en-us_topic_0201534068_p176864111411"></a><a name="en-us_topic_0201534068_p176864111411"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p136865110419"><a name="en-us_topic_0201534068_p136865110419"></a><a name="en-us_topic_0201534068_p136865110419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p16861211413"><a name="en-us_topic_0201534068_p16861211413"></a><a name="en-us_topic_0201534068_p16861211413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p1068611114119"><a name="en-us_topic_0201534068_p1068611114119"></a><a name="en-us_topic_0201534068_p1068611114119"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row1757105620480"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p868615164111"><a name="en-us_topic_0201534068_p868615164111"></a><a name="en-us_topic_0201534068_p868615164111"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p1468611134120"><a name="en-us_topic_0201534068_p1468611134120"></a><a name="en-us_topic_0201534068_p1468611134120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p1668716114415"><a name="en-us_topic_0201534068_p1668716114415"></a><a name="en-us_topic_0201534068_p1668716114415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p76878124112"><a name="en-us_topic_0201534068_p76878124112"></a><a name="en-us_topic_0201534068_p76878124112"></a>Specifies the floating IPv6 address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row16757125613485"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p1668781104117"><a name="en-us_topic_0201534068_p1668781104117"></a><a name="en-us_topic_0201534068_p1668781104117"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p1668731204116"><a name="en-us_topic_0201534068_p1668731204116"></a><a name="en-us_topic_0201534068_p1668731204116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p1687610411"><a name="en-us_topic_0201534068_p1687610411"></a><a name="en-us_topic_0201534068_p1687610411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p14687611411"><a name="en-us_topic_0201534068_p14687611411"></a><a name="en-us_topic_0201534068_p14687611411"></a>Specifies the external network ID.</p>
<p id="en-us_topic_0201534068_p4687818419"><a name="en-us_topic_0201534068_p4687818419"></a><a name="en-us_topic_0201534068_p4687818419"></a>You can only use fixed external network. </p>
<p id="en-us_topic_0201534068_p9687151144115"><a name="en-us_topic_0201534068_p9687151144115"></a><a name="en-us_topic_0201534068_p9687151144115"></a>You can use <strong id="en-us_topic_0201534068_b17545134515504"><a name="en-us_topic_0201534068_b17545134515504"></a><a name="en-us_topic_0201534068_b17545134515504"></a>GET /v2.0/networks?router:external=True</strong> or</p>
<p id="en-us_topic_0201534068_p1568711118416"><a name="en-us_topic_0201534068_p1568711118416"></a><a name="en-us_topic_0201534068_p1568711118416"></a><strong id="en-us_topic_0201534068_b12677425124620"><a name="en-us_topic_0201534068_b12677425124620"></a><a name="en-us_topic_0201534068_b12677425124620"></a>GET /v2.0/networks?name={floating_network}</strong> or run the <strong id="en-us_topic_0201534068_b967818252466"><a name="en-us_topic_0201534068_b967818252466"></a><a name="en-us_topic_0201534068_b967818252466"></a>neutron net-external-list</strong> command to obtain information about the external network. </p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row67574563489"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p106871419413"><a name="en-us_topic_0201534068_p106871419413"></a><a name="en-us_topic_0201534068_p106871419413"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p1268712115416"><a name="en-us_topic_0201534068_p1268712115416"></a><a name="en-us_topic_0201534068_p1268712115416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p6687015419"><a name="en-us_topic_0201534068_p6687015419"></a><a name="en-us_topic_0201534068_p6687015419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p668714111415"><a name="en-us_topic_0201534068_p668714111415"></a><a name="en-us_topic_0201534068_p668714111415"></a>Specifies the ID of the belonged router. </p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row17757155634812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p1868717104113"><a name="en-us_topic_0201534068_p1868717104113"></a><a name="en-us_topic_0201534068_p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p26871119419"><a name="en-us_topic_0201534068_p26871119419"></a><a name="en-us_topic_0201534068_p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p66889116414"><a name="en-us_topic_0201534068_p66889116414"></a><a name="en-us_topic_0201534068_p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p14688213413"><a name="en-us_topic_0201534068_p14688213413"></a><a name="en-us_topic_0201534068_p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row1375718561481"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p868818134116"><a name="en-us_topic_0201534068_p868818134116"></a><a name="en-us_topic_0201534068_p868818134116"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p568817111417"><a name="en-us_topic_0201534068_p568817111417"></a><a name="en-us_topic_0201534068_p568817111417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p96881617413"><a name="en-us_topic_0201534068_p96881617413"></a><a name="en-us_topic_0201534068_p96881617413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p1668816118413"><a name="en-us_topic_0201534068_p1668816118413"></a><a name="en-us_topic_0201534068_p1668816118413"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row11758105613489"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534068_p968813113416"><a name="en-us_topic_0201534068_p968813113416"></a><a name="en-us_topic_0201534068_p968813113416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534068_p468815111414"><a name="en-us_topic_0201534068_p468815111414"></a><a name="en-us_topic_0201534068_p468815111414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534068_p12688141154119"><a name="en-us_topic_0201534068_p12688141154119"></a><a name="en-us_topic_0201534068_p12688141154119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534068_p10487112"><a name="en-us_topic_0201534068_p10487112"></a><a name="en-us_topic_0201534068_p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

Example:

```
GET https://{Endpoint}/v2.0/floatingips?id={fip_id}&router_id={router_id}&floating_network_id={net_id}&floating_ip_address={floating_ip}&port_id={port_id}&fixed_ip_address={fixed_ip}&tenant_id={tenant_id}
```

## Request Message<a name="en-us_topic_0201534068_section656683442148"></a>

None

## Response Message<a name="en-us_topic_0201534068_section236032922148"></a>

**Table  2**  Response parameter

<a name="en-us_topic_0201534068_table328184742148"></a>
<table><thead align="left"><tr id="en-us_topic_0201534068_row308815332148"><th class="cellrowborder" valign="top" width="15.559999999999999%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534068_p183762202148"><a name="en-us_topic_0201534068_p183762202148"></a><a name="en-us_topic_0201534068_p183762202148"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534068_p120788402148"><a name="en-us_topic_0201534068_p120788402148"></a><a name="en-us_topic_0201534068_p120788402148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.11%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534068_p608097322148"><a name="en-us_topic_0201534068_p608097322148"></a><a name="en-us_topic_0201534068_p608097322148"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534068_row266412852148"><td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p104605152148"><a name="en-us_topic_0201534068_p104605152148"></a><a name="en-us_topic_0201534068_p104605152148"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p109471238618"><a name="en-us_topic_0201534068_p109471238618"></a><a name="en-us_topic_0201534068_p109471238618"></a>Array of <a href="#en-us_topic_0201534068_table8139247714">floatingip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="61.11%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p499181352148"><a name="en-us_topic_0201534068_p499181352148"></a><a name="en-us_topic_0201534068_p499181352148"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534068_table8139247714">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floatingip**  objects

<a name="en-us_topic_0201534068_table8139247714"></a>
<table><thead align="left"><tr id="en-us_topic_0201534068_row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534068_p101201250870"><a name="en-us_topic_0201534068_p101201250870"></a><a name="en-us_topic_0201534068_p101201250870"></a><strong id="en-us_topic_0201534068_b679955995412"><a name="en-us_topic_0201534068_b679955995412"></a><a name="en-us_topic_0201534068_b679955995412"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534068_p161211850674"><a name="en-us_topic_0201534068_p161211850674"></a><a name="en-us_topic_0201534068_p161211850674"></a><strong id="en-us_topic_0201534068_b13646184535515"><a name="en-us_topic_0201534068_b13646184535515"></a><a name="en-us_topic_0201534068_b13646184535515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534068_p41217502719"><a name="en-us_topic_0201534068_p41217502719"></a><a name="en-us_topic_0201534068_p41217502719"></a><strong id="en-us_topic_0201534068_b732864665514"><a name="en-us_topic_0201534068_b732864665514"></a><a name="en-us_topic_0201534068_b732864665514"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534068_row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p6028218019164"><a name="en-us_topic_0201534068_p6028218019164"></a><a name="en-us_topic_0201534068_p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p5101843519164"><a name="en-us_topic_0201534068_p5101843519164"></a><a name="en-us_topic_0201534068_p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p6000412319164"><a name="en-us_topic_0201534068_p6000412319164"></a><a name="en-us_topic_0201534068_p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534068_b16246154416596"><a name="en-us_topic_0201534068_b16246154416596"></a><a name="en-us_topic_0201534068_b16246154416596"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534068_b9247144195915"><a name="en-us_topic_0201534068_b9247144195915"></a><a name="en-us_topic_0201534068_b9247144195915"></a>DOWN</strong>, or <strong id="en-us_topic_0201534068_b0249154485919"><a name="en-us_topic_0201534068_b0249154485919"></a><a name="en-us_topic_0201534068_b0249154485919"></a>ERROR</strong>.</p>
<a name="en-us_topic_0201534068_ul10603143175810"></a><a name="en-us_topic_0201534068_ul10603143175810"></a><ul id="en-us_topic_0201534068_ul10603143175810"><li><strong id="en-us_topic_0201534068_b842352706181834"><a name="en-us_topic_0201534068_b842352706181834"></a><a name="en-us_topic_0201534068_b842352706181834"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="en-us_topic_0201534068_b84235270610164"><a name="en-us_topic_0201534068_b84235270610164"></a><a name="en-us_topic_0201534068_b84235270610164"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534068_b66749771144837"><a name="en-us_topic_0201534068_b66749771144837"></a><a name="en-us_topic_0201534068_b66749771144837"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534068_row4141241070"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p5513524919164"><a name="en-us_topic_0201534068_p5513524919164"></a><a name="en-us_topic_0201534068_p5513524919164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p212111505713"><a name="en-us_topic_0201534068_p212111505713"></a><a name="en-us_topic_0201534068_p212111505713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p4121850371"><a name="en-us_topic_0201534068_p4121850371"></a><a name="en-us_topic_0201534068_p4121850371"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row614132416712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p1912112509713"><a name="en-us_topic_0201534068_p1912112509713"></a><a name="en-us_topic_0201534068_p1912112509713"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p11211850072"><a name="en-us_topic_0201534068_p11211850072"></a><a name="en-us_topic_0201534068_p11211850072"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p16122205017713"><a name="en-us_topic_0201534068_p16122205017713"></a><a name="en-us_topic_0201534068_p16122205017713"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row115102414717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p61223503712"><a name="en-us_topic_0201534068_p61223503712"></a><a name="en-us_topic_0201534068_p61223503712"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p1812220507714"><a name="en-us_topic_0201534068_p1812220507714"></a><a name="en-us_topic_0201534068_p1812220507714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p16122550274"><a name="en-us_topic_0201534068_p16122550274"></a><a name="en-us_topic_0201534068_p16122550274"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row19155241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p201223504719"><a name="en-us_topic_0201534068_p201223504719"></a><a name="en-us_topic_0201534068_p201223504719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p1122155015714"><a name="en-us_topic_0201534068_p1122155015714"></a><a name="en-us_topic_0201534068_p1122155015714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p812212506713"><a name="en-us_topic_0201534068_p812212506713"></a><a name="en-us_topic_0201534068_p812212506713"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row101514247714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p412218502718"><a name="en-us_topic_0201534068_p412218502718"></a><a name="en-us_topic_0201534068_p412218502718"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p612213506716"><a name="en-us_topic_0201534068_p612213506716"></a><a name="en-us_topic_0201534068_p612213506716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p141228504716"><a name="en-us_topic_0201534068_p141228504716"></a><a name="en-us_topic_0201534068_p141228504716"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row3164249715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p01237508720"><a name="en-us_topic_0201534068_p01237508720"></a><a name="en-us_topic_0201534068_p01237508720"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p111239501770"><a name="en-us_topic_0201534068_p111239501770"></a><a name="en-us_topic_0201534068_p111239501770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p1712316501972"><a name="en-us_topic_0201534068_p1712316501972"></a><a name="en-us_topic_0201534068_p1712316501972"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row21662416711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p812355018717"><a name="en-us_topic_0201534068_p812355018717"></a><a name="en-us_topic_0201534068_p812355018717"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p612316509712"><a name="en-us_topic_0201534068_p612316509712"></a><a name="en-us_topic_0201534068_p612316509712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p1597110240277"><a name="en-us_topic_0201534068_p1597110240277"></a><a name="en-us_topic_0201534068_p1597110240277"></a>Specifies the project ID.</p>
<p id="en-us_topic_0201534068_p51231950174"><a name="en-us_topic_0201534068_p51231950174"></a><a name="en-us_topic_0201534068_p51231950174"></a></p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row11176241720"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p11222111885214"><a name="en-us_topic_0201534068_p11222111885214"></a><a name="en-us_topic_0201534068_p11222111885214"></a>dns_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p122232018115215"><a name="en-us_topic_0201534068_p122232018115215"></a><a name="en-us_topic_0201534068_p122232018115215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p18223161825216"><a name="en-us_topic_0201534068_p18223161825216"></a><a name="en-us_topic_0201534068_p18223161825216"></a>Specifies the DNS name.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row17174241670"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p492133065713"><a name="en-us_topic_0201534068_p492133065713"></a><a name="en-us_topic_0201534068_p492133065713"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p16929300573"><a name="en-us_topic_0201534068_p16929300573"></a><a name="en-us_topic_0201534068_p16929300573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p3921230175711"><a name="en-us_topic_0201534068_p3921230175711"></a><a name="en-us_topic_0201534068_p3921230175711"></a>Specifies the DNS domain.</p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row1418142410714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p1953114119914"><a name="en-us_topic_0201534068_p1953114119914"></a><a name="en-us_topic_0201534068_p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p595318416919"><a name="en-us_topic_0201534068_p595318416919"></a><a name="en-us_topic_0201534068_p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p1395374115919"><a name="en-us_topic_0201534068_p1395374115919"></a><a name="en-us_topic_0201534068_p1395374115919"></a>Specifies the time when the floating IP address was created.</p>
<p id="en-us_topic_0201534068_p1232884613478"><a name="en-us_topic_0201534068_p1232884613478"></a><a name="en-us_topic_0201534068_p1232884613478"></a>UTC time is used.</p>
<p id="en-us_topic_0201534068_p2070141994713"><a name="en-us_topic_0201534068_p2070141994713"></a><a name="en-us_topic_0201534068_p2070141994713"></a>Format: <em id="en-us_topic_0201534068_i1169023151616"><a name="en-us_topic_0201534068_i1169023151616"></a><a name="en-us_topic_0201534068_i1169023151616"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="en-us_topic_0201534068_row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534068_p139719548912"><a name="en-us_topic_0201534068_p139719548912"></a><a name="en-us_topic_0201534068_p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534068_p53971154594"><a name="en-us_topic_0201534068_p53971154594"></a><a name="en-us_topic_0201534068_p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534068_p1339713549918"><a name="en-us_topic_0201534068_p1339713549918"></a><a name="en-us_topic_0201534068_p1339713549918"></a>Specifies the time when the floating IP address was updated.</p>
<p id="en-us_topic_0201534068_p876511114816"><a name="en-us_topic_0201534068_p876511114816"></a><a name="en-us_topic_0201534068_p876511114816"></a>UTC time is used.</p>
<p id="en-us_topic_0201534068_p137222218476"><a name="en-us_topic_0201534068_p137222218476"></a><a name="en-us_topic_0201534068_p137222218476"></a>Format: <em id="en-us_topic_0201534068_i35911393172"><a name="en-us_topic_0201534068_i35911393172"></a><a name="en-us_topic_0201534068_i35911393172"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0201534068_section466100362148"></a>

Example request

```
GET https://{Endpoint}/v2.0/floatingips?limit=1
```

Example response

```
{
    "floatingips": [
        {
            "id": "1a3a2818-d9b4-4a9c-8a19-5252c499d1cd",
            "status": "DOWN",
            "router_id": null,
            "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
            "fixed_ip_address": null,
            "floating_ip_address": "99.99.99.84",
            "port_id": null,
            "created_at": "2017-10-19T12:21:28",
            "updated_at": "2018-07-30T12:52:13"
        }
    ]
}
```

## Status Code<a name="en-us_topic_0201534068_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534068_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

