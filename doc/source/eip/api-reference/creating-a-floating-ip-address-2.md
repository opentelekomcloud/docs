# Creating a Floating IP Address<a name="eip_openstackapi_0008"></a>

## Function<a name="en-us_topic_0201534249_section3174871621549"></a>

When creating a floating IP address, you need to obtain the external network ID  **floating\_network\_id**  of the floating IP address. 

You can use  **GET /v2.0/networks?router:external=True**  or run the  **neutron net-external-list**  command to obtain the UUID of the external network required for creating a floating IP address. 

## URI<a name="en-us_topic_0201534249_section5936537521549"></a>

POST /v2.0/floatingips

## Request Message<a name="en-us_topic_0201534249_section5012846321549"></a>

**Table  1**  Request parameter

<a name="en-us_topic_0201534249_table3387369821549"></a>
<table><thead align="left"><tr id="en-us_topic_0201534249_row1358409521549"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534249_p2656991721549"><a name="en-us_topic_0201534249_p2656991721549"></a><a name="en-us_topic_0201534249_p2656991721549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534249_p467970821549"><a name="en-us_topic_0201534249_p467970821549"></a><a name="en-us_topic_0201534249_p467970821549"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534249_p4351210021549"><a name="en-us_topic_0201534249_p4351210021549"></a><a name="en-us_topic_0201534249_p4351210021549"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.550000000000004%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534249_p3481919621549"><a name="en-us_topic_0201534249_p3481919621549"></a><a name="en-us_topic_0201534249_p3481919621549"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534249_row178260421549"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534249_p1017324521549"><a name="en-us_topic_0201534249_p1017324521549"></a><a name="en-us_topic_0201534249_p1017324521549"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534249_p1872651821549"><a name="en-us_topic_0201534249_p1872651821549"></a><a name="en-us_topic_0201534249_p1872651821549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534249_p4045302421549"><a name="en-us_topic_0201534249_p4045302421549"></a><a name="en-us_topic_0201534249_p4045302421549"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534249_p499181352148"><a name="en-us_topic_0201534249_p499181352148"></a><a name="en-us_topic_0201534249_p499181352148"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534249_table15863423175513">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **floatingip**  objects

<a name="en-us_topic_0201534249_table15863423175513"></a>
<table><thead align="left"><tr id="en-us_topic_0201534249_row48631623155511"><th class="cellrowborder" valign="top" width="19.939999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534249_p23806019164"><a name="en-us_topic_0201534249_p23806019164"></a><a name="en-us_topic_0201534249_p23806019164"></a><strong id="en-us_topic_0201534249_b17125172310222"><a name="en-us_topic_0201534249_b17125172310222"></a><a name="en-us_topic_0201534249_b17125172310222"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="8.49%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534249_p868823916540"><a name="en-us_topic_0201534249_p868823916540"></a><a name="en-us_topic_0201534249_p868823916540"></a><strong id="en-us_topic_0201534249_b1799613238229"><a name="en-us_topic_0201534249_b1799613238229"></a><a name="en-us_topic_0201534249_b1799613238229"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534249_p1928287519164"><a name="en-us_topic_0201534249_p1928287519164"></a><a name="en-us_topic_0201534249_p1928287519164"></a><strong id="en-us_topic_0201534249_b14709142422212"><a name="en-us_topic_0201534249_b14709142422212"></a><a name="en-us_topic_0201534249_b14709142422212"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.09%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534249_p4943306019164"><a name="en-us_topic_0201534249_p4943306019164"></a><a name="en-us_topic_0201534249_p4943306019164"></a><strong id="en-us_topic_0201534249_b12411025162214"><a name="en-us_topic_0201534249_b12411025162214"></a><a name="en-us_topic_0201534249_b12411025162214"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534249_row7864323175518"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534249_p2022646619164"><a name="en-us_topic_0201534249_p2022646619164"></a><a name="en-us_topic_0201534249_p2022646619164"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="8.49%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534249_p17689839165418"><a name="en-us_topic_0201534249_p17689839165418"></a><a name="en-us_topic_0201534249_p17689839165418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534249_p2773103519164"><a name="en-us_topic_0201534249_p2773103519164"></a><a name="en-us_topic_0201534249_p2773103519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534249_p2292670119164"><a name="en-us_topic_0201534249_p2292670119164"></a><a name="en-us_topic_0201534249_p2292670119164"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row1686417238557"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534249_p345796219164"><a name="en-us_topic_0201534249_p345796219164"></a><a name="en-us_topic_0201534249_p345796219164"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.49%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534249_p1068933955414"><a name="en-us_topic_0201534249_p1068933955414"></a><a name="en-us_topic_0201534249_p1068933955414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534249_p1165952819164"><a name="en-us_topic_0201534249_p1165952819164"></a><a name="en-us_topic_0201534249_p1165952819164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534249_p1389784219164"><a name="en-us_topic_0201534249_p1389784219164"></a><a name="en-us_topic_0201534249_p1389784219164"></a>Specifies the external network ID.</p>
<p id="en-us_topic_0201534249_p186012181292"><a name="en-us_topic_0201534249_p186012181292"></a><a name="en-us_topic_0201534249_p186012181292"></a>You can only use fixed external network. </p>
<p id="en-us_topic_0201534249_p095071919913"><a name="en-us_topic_0201534249_p095071919913"></a><a name="en-us_topic_0201534249_p095071919913"></a>You can use <strong id="en-us_topic_0201534249_b14361511172314"><a name="en-us_topic_0201534249_b14361511172314"></a><a name="en-us_topic_0201534249_b14361511172314"></a>GET /v2.0/networks?router:external=True</strong> or</p>
<p id="en-us_topic_0201534249_p520001217911"><a name="en-us_topic_0201534249_p520001217911"></a><a name="en-us_topic_0201534249_p520001217911"></a><strong id="en-us_topic_0201534249_b1416252572310"><a name="en-us_topic_0201534249_b1416252572310"></a><a name="en-us_topic_0201534249_b1416252572310"></a>GET /v2.0/networks?name={floating_network}</strong> or</p>
<p id="en-us_topic_0201534249_p5797172119164"><a name="en-us_topic_0201534249_p5797172119164"></a><a name="en-us_topic_0201534249_p5797172119164"></a>run the <strong id="en-us_topic_0201534249_b156372056245"><a name="en-us_topic_0201534249_b156372056245"></a><a name="en-us_topic_0201534249_b156372056245"></a>neutron net-external-list mode</strong> command to obtain information about the external network. </p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row98641023145511"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534249_p4886025919164"><a name="en-us_topic_0201534249_p4886025919164"></a><a name="en-us_topic_0201534249_p4886025919164"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.49%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534249_p1868973975414"><a name="en-us_topic_0201534249_p1868973975414"></a><a name="en-us_topic_0201534249_p1868973975414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534249_p6536694419164"><a name="en-us_topic_0201534249_p6536694419164"></a><a name="en-us_topic_0201534249_p6536694419164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534249_p2628234219164"><a name="en-us_topic_0201534249_p2628234219164"></a><a name="en-us_topic_0201534249_p2628234219164"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row1086519236554"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534249_p3380179719164"><a name="en-us_topic_0201534249_p3380179719164"></a><a name="en-us_topic_0201534249_p3380179719164"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="8.49%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534249_p368912399543"><a name="en-us_topic_0201534249_p368912399543"></a><a name="en-us_topic_0201534249_p368912399543"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534249_p5359099919164"><a name="en-us_topic_0201534249_p5359099919164"></a><a name="en-us_topic_0201534249_p5359099919164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534249_p1829247919164"><a name="en-us_topic_0201534249_p1829247919164"></a><a name="en-us_topic_0201534249_p1829247919164"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="en-us_topic_0201534249_section6384765421549"></a>

**Table  3**  Response parameter

<a name="en-us_topic_0201534249_table427745721549"></a>
<table><thead align="left"><tr id="en-us_topic_0201534249_row435809221549"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534249_p1746120521549"><a name="en-us_topic_0201534249_p1746120521549"></a><a name="en-us_topic_0201534249_p1746120521549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534249_p507150621549"><a name="en-us_topic_0201534249_p507150621549"></a><a name="en-us_topic_0201534249_p507150621549"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534249_p5526791421549"><a name="en-us_topic_0201534249_p5526791421549"></a><a name="en-us_topic_0201534249_p5526791421549"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534249_row4751605321549"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p2359506021549"><a name="en-us_topic_0201534249_p2359506021549"></a><a name="en-us_topic_0201534249_p2359506021549"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p3215169621549"><a name="en-us_topic_0201534249_p3215169621549"></a><a name="en-us_topic_0201534249_p3215169621549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p2411791621549"><a name="en-us_topic_0201534249_p2411791621549"></a><a name="en-us_topic_0201534249_p2411791621549"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534249_table8139247714">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **floatingip**  objects

<a name="en-us_topic_0201534249_table8139247714"></a>
<table><thead align="left"><tr id="en-us_topic_0201534249_row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534249_p101201250870"><a name="en-us_topic_0201534249_p101201250870"></a><a name="en-us_topic_0201534249_p101201250870"></a><strong id="en-us_topic_0201534249_b20758153582519"><a name="en-us_topic_0201534249_b20758153582519"></a><a name="en-us_topic_0201534249_b20758153582519"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534249_p161211850674"><a name="en-us_topic_0201534249_p161211850674"></a><a name="en-us_topic_0201534249_p161211850674"></a><strong id="en-us_topic_0201534249_b165690362259"><a name="en-us_topic_0201534249_b165690362259"></a><a name="en-us_topic_0201534249_b165690362259"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534249_p41217502719"><a name="en-us_topic_0201534249_p41217502719"></a><a name="en-us_topic_0201534249_p41217502719"></a><strong id="en-us_topic_0201534249_b62611537152516"><a name="en-us_topic_0201534249_b62611537152516"></a><a name="en-us_topic_0201534249_b62611537152516"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534249_row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p6028218019164"><a name="en-us_topic_0201534249_p6028218019164"></a><a name="en-us_topic_0201534249_p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p5101843519164"><a name="en-us_topic_0201534249_p5101843519164"></a><a name="en-us_topic_0201534249_p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p6000412319164"><a name="en-us_topic_0201534249_p6000412319164"></a><a name="en-us_topic_0201534249_p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534249_b1077611394252"><a name="en-us_topic_0201534249_b1077611394252"></a><a name="en-us_topic_0201534249_b1077611394252"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534249_b18777939192511"><a name="en-us_topic_0201534249_b18777939192511"></a><a name="en-us_topic_0201534249_b18777939192511"></a>DOWN</strong>, or <strong id="en-us_topic_0201534249_b3777183912515"><a name="en-us_topic_0201534249_b3777183912515"></a><a name="en-us_topic_0201534249_b3777183912515"></a>ERROR</strong>.</p>
<a name="en-us_topic_0201534249_ul10603143175810"></a><a name="en-us_topic_0201534249_ul10603143175810"></a><ul id="en-us_topic_0201534249_ul10603143175810"><li><strong id="en-us_topic_0201534249_b127219610379"><a name="en-us_topic_0201534249_b127219610379"></a><a name="en-us_topic_0201534249_b127219610379"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="en-us_topic_0201534249_b25619810374"><a name="en-us_topic_0201534249_b25619810374"></a><a name="en-us_topic_0201534249_b25619810374"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534249_b148881088379"><a name="en-us_topic_0201534249_b148881088379"></a><a name="en-us_topic_0201534249_b148881088379"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534249_row4141241070"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p5513524919164"><a name="en-us_topic_0201534249_p5513524919164"></a><a name="en-us_topic_0201534249_p5513524919164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p212111505713"><a name="en-us_topic_0201534249_p212111505713"></a><a name="en-us_topic_0201534249_p212111505713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p4121850371"><a name="en-us_topic_0201534249_p4121850371"></a><a name="en-us_topic_0201534249_p4121850371"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row614132416712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p1912112509713"><a name="en-us_topic_0201534249_p1912112509713"></a><a name="en-us_topic_0201534249_p1912112509713"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p11211850072"><a name="en-us_topic_0201534249_p11211850072"></a><a name="en-us_topic_0201534249_p11211850072"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p16122205017713"><a name="en-us_topic_0201534249_p16122205017713"></a><a name="en-us_topic_0201534249_p16122205017713"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row115102414717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p61223503712"><a name="en-us_topic_0201534249_p61223503712"></a><a name="en-us_topic_0201534249_p61223503712"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p1812220507714"><a name="en-us_topic_0201534249_p1812220507714"></a><a name="en-us_topic_0201534249_p1812220507714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p16122550274"><a name="en-us_topic_0201534249_p16122550274"></a><a name="en-us_topic_0201534249_p16122550274"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row19155241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p201223504719"><a name="en-us_topic_0201534249_p201223504719"></a><a name="en-us_topic_0201534249_p201223504719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p1122155015714"><a name="en-us_topic_0201534249_p1122155015714"></a><a name="en-us_topic_0201534249_p1122155015714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p812212506713"><a name="en-us_topic_0201534249_p812212506713"></a><a name="en-us_topic_0201534249_p812212506713"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row101514247714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p412218502718"><a name="en-us_topic_0201534249_p412218502718"></a><a name="en-us_topic_0201534249_p412218502718"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p612213506716"><a name="en-us_topic_0201534249_p612213506716"></a><a name="en-us_topic_0201534249_p612213506716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p141228504716"><a name="en-us_topic_0201534249_p141228504716"></a><a name="en-us_topic_0201534249_p141228504716"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row3164249715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p01237508720"><a name="en-us_topic_0201534249_p01237508720"></a><a name="en-us_topic_0201534249_p01237508720"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p111239501770"><a name="en-us_topic_0201534249_p111239501770"></a><a name="en-us_topic_0201534249_p111239501770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p1712316501972"><a name="en-us_topic_0201534249_p1712316501972"></a><a name="en-us_topic_0201534249_p1712316501972"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row21662416711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p812355018717"><a name="en-us_topic_0201534249_p812355018717"></a><a name="en-us_topic_0201534249_p812355018717"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p612316509712"><a name="en-us_topic_0201534249_p612316509712"></a><a name="en-us_topic_0201534249_p612316509712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p10487112"><a name="en-us_topic_0201534249_p10487112"></a><a name="en-us_topic_0201534249_p10487112"></a>Specifies the project ID.</p>
<p id="en-us_topic_0201534249_p51231950174"><a name="en-us_topic_0201534249_p51231950174"></a><a name="en-us_topic_0201534249_p51231950174"></a></p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row11176241720"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p11222111885214"><a name="en-us_topic_0201534249_p11222111885214"></a><a name="en-us_topic_0201534249_p11222111885214"></a>dns_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p122232018115215"><a name="en-us_topic_0201534249_p122232018115215"></a><a name="en-us_topic_0201534249_p122232018115215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p18223161825216"><a name="en-us_topic_0201534249_p18223161825216"></a><a name="en-us_topic_0201534249_p18223161825216"></a>Specifies the DNS name.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row17174241670"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p492133065713"><a name="en-us_topic_0201534249_p492133065713"></a><a name="en-us_topic_0201534249_p492133065713"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p16929300573"><a name="en-us_topic_0201534249_p16929300573"></a><a name="en-us_topic_0201534249_p16929300573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p3921230175711"><a name="en-us_topic_0201534249_p3921230175711"></a><a name="en-us_topic_0201534249_p3921230175711"></a>Specifies the DNS domain.</p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row1418142410714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p1953114119914"><a name="en-us_topic_0201534249_p1953114119914"></a><a name="en-us_topic_0201534249_p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p595318416919"><a name="en-us_topic_0201534249_p595318416919"></a><a name="en-us_topic_0201534249_p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p1395374115919"><a name="en-us_topic_0201534249_p1395374115919"></a><a name="en-us_topic_0201534249_p1395374115919"></a>Specifies the time when the floating IP address was created.</p>
<p id="en-us_topic_0201534249_p1232884613478"><a name="en-us_topic_0201534249_p1232884613478"></a><a name="en-us_topic_0201534249_p1232884613478"></a>UTC time is used.</p>
<p id="en-us_topic_0201534249_p2070141994713"><a name="en-us_topic_0201534249_p2070141994713"></a><a name="en-us_topic_0201534249_p2070141994713"></a>Format: <em id="en-us_topic_0201534249_i162066913389"><a name="en-us_topic_0201534249_i162066913389"></a><a name="en-us_topic_0201534249_i162066913389"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="en-us_topic_0201534249_row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534249_p139719548912"><a name="en-us_topic_0201534249_p139719548912"></a><a name="en-us_topic_0201534249_p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534249_p53971154594"><a name="en-us_topic_0201534249_p53971154594"></a><a name="en-us_topic_0201534249_p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534249_p1339713549918"><a name="en-us_topic_0201534249_p1339713549918"></a><a name="en-us_topic_0201534249_p1339713549918"></a>Specifies the time when the floating IP address was updated.</p>
<p id="en-us_topic_0201534249_p876511114816"><a name="en-us_topic_0201534249_p876511114816"></a><a name="en-us_topic_0201534249_p876511114816"></a>UTC time is used.</p>
<p id="en-us_topic_0201534249_p137222218476"><a name="en-us_topic_0201534249_p137222218476"></a><a name="en-us_topic_0201534249_p137222218476"></a>Format: <em id="en-us_topic_0201534249_i1787011319382"><a name="en-us_topic_0201534249_i1787011319382"></a><a name="en-us_topic_0201534249_i1787011319382"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0201534249_section1573465921549"></a>

Example request

```
POST https://{Endpoint}/v2.0/floatingips 

{
    "floatingip": {
           "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975"
    }
}
```

Example response

```
{
    "floatingip": {
        "id": "b997e0d4-3359-4c74-8f88-bc0af81cd5a2",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": null,
        "floating_ip_address": "88.88.215.205",
        "port_id": null,
        "created_at": "2018-09-20T02:10:02",
        "updated_at": "2018-09-20T02:10:02"
    }
}
```

## Status Code<a name="en-us_topic_0201534249_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534249_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

