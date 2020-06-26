# Updating a Floating IP Address<a name="eip_openstackapi_0009"></a>

## Function<a name="en-us_topic_0201534103_section6285365021641"></a>

This API is used to update a floating IP address.

During the update, the ID of the floating IP address must be provided in the URL.

If  **port\_id**  is left blank, the floating IP address has been unbound from the port.

Restrictions

When you bind a floating IP address, if the floating IP address is in the  **error**  state, try unbinding the address first.

You are not allowed to bind a floating IP address that has been bound to a port to another port. You must first unbind the IP address from its original port and bind it to the required port.

## URI<a name="en-us_topic_0201534103_section5206576221641"></a>

PUT /v2.0/floatingips/\{floatingip\_id\}

[Table 1](#en-us_topic_0201534103_table5388109319164)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534103_table5388109319164"></a>
<table><thead align="left"><tr id="en-us_topic_0201534103_row6462628919164"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534103_p23806019164"><a name="en-us_topic_0201534103_p23806019164"></a><a name="en-us_topic_0201534103_p23806019164"></a><strong id="en-us_topic_0201534103_b78917553286"><a name="en-us_topic_0201534103_b78917553286"></a><a name="en-us_topic_0201534103_b78917553286"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.66%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534103_p868823916540"><a name="en-us_topic_0201534103_p868823916540"></a><a name="en-us_topic_0201534103_p868823916540"></a><strong id="en-us_topic_0201534103_b119011056102810"><a name="en-us_topic_0201534103_b119011056102810"></a><a name="en-us_topic_0201534103_b119011056102810"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.28%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534103_p1928287519164"><a name="en-us_topic_0201534103_p1928287519164"></a><a name="en-us_topic_0201534103_p1928287519164"></a><strong id="en-us_topic_0201534103_b180005719282"><a name="en-us_topic_0201534103_b180005719282"></a><a name="en-us_topic_0201534103_b180005719282"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.89%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534103_p4943306019164"><a name="en-us_topic_0201534103_p4943306019164"></a><a name="en-us_topic_0201534103_p4943306019164"></a><strong id="en-us_topic_0201534103_b585785862817"><a name="en-us_topic_0201534103_b585785862817"></a><a name="en-us_topic_0201534103_b585785862817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534103_row316619519164"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534103_p115515499553"><a name="en-us_topic_0201534103_p115515499553"></a><a name="en-us_topic_0201534103_p115515499553"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534103_p0689103915411"><a name="en-us_topic_0201534103_p0689103915411"></a><a name="en-us_topic_0201534103_p0689103915411"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534103_p3677022419164"><a name="en-us_topic_0201534103_p3677022419164"></a><a name="en-us_topic_0201534103_p3677022419164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534103_p2690811319164"><a name="en-us_topic_0201534103_p2690811319164"></a><a name="en-us_topic_0201534103_p2690811319164"></a>Specifies the floating IP address ID.</p>
<p id="en-us_topic_0201534103_p6641157838"><a name="en-us_topic_0201534103_p6641157838"></a><a name="en-us_topic_0201534103_p6641157838"></a>This parameter is not required when you assign a floating IP address. This parameter is mandatory when you query, update, or delete a floating IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534103_section2938074421641"></a>

**Table  2**  Request parameter

<a name="en-us_topic_0201534103_table3103003021641"></a>
<table><thead align="left"><tr id="en-us_topic_0201534103_row5907300221641"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534103_p2018384621641"><a name="en-us_topic_0201534103_p2018384621641"></a><a name="en-us_topic_0201534103_p2018384621641"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.03%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534103_p2427879021641"><a name="en-us_topic_0201534103_p2427879021641"></a><a name="en-us_topic_0201534103_p2427879021641"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.4%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534103_p2042494621641"><a name="en-us_topic_0201534103_p2042494621641"></a><a name="en-us_topic_0201534103_p2042494621641"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.98%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534103_p4380795521641"><a name="en-us_topic_0201534103_p4380795521641"></a><a name="en-us_topic_0201534103_p4380795521641"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534103_row5878350521641"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534103_p6384347521641"><a name="en-us_topic_0201534103_p6384347521641"></a><a name="en-us_topic_0201534103_p6384347521641"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534103_p393901021641"><a name="en-us_topic_0201534103_p393901021641"></a><a name="en-us_topic_0201534103_p393901021641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534103_p5062438921641"><a name="en-us_topic_0201534103_p5062438921641"></a><a name="en-us_topic_0201534103_p5062438921641"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.98%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534103_p557124874610"><a name="en-us_topic_0201534103_p557124874610"></a><a name="en-us_topic_0201534103_p557124874610"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534103_table547993685510">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floatingip**  objects

<a name="en-us_topic_0201534103_table547993685510"></a>
<table><thead align="left"><tr id="en-us_topic_0201534103_row966719362553"><th class="cellrowborder" valign="top" width="19.878012198780123%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534103_p0685313416"><a name="en-us_topic_0201534103_p0685313416"></a><a name="en-us_topic_0201534103_p0685313416"></a><strong id="en-us_topic_0201534103_b14322115343414"><a name="en-us_topic_0201534103_b14322115343414"></a><a name="en-us_topic_0201534103_b14322115343414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.938706129387059%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534103_p768561134110"><a name="en-us_topic_0201534103_p768561134110"></a><a name="en-us_topic_0201534103_p768561134110"></a><strong id="en-us_topic_0201534103_b3756754163410"><a name="en-us_topic_0201534103_b3756754163410"></a><a name="en-us_topic_0201534103_b3756754163410"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.84871512848715%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534103_p368681134120"><a name="en-us_topic_0201534103_p368681134120"></a><a name="en-us_topic_0201534103_p368681134120"></a><strong id="en-us_topic_0201534103_b85211556143419"><a name="en-us_topic_0201534103_b85211556143419"></a><a name="en-us_topic_0201534103_b85211556143419"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.334566543345666%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534103_p668612124119"><a name="en-us_topic_0201534103_p668612124119"></a><a name="en-us_topic_0201534103_p668612124119"></a><strong id="en-us_topic_0201534103_b12100759133410"><a name="en-us_topic_0201534103_b12100759133410"></a><a name="en-us_topic_0201534103_b12100759133410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534103_row1667163613554"><td class="cellrowborder" valign="top" width="19.878012198780123%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534103_p1868717104113"><a name="en-us_topic_0201534103_p1868717104113"></a><a name="en-us_topic_0201534103_p1868717104113"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.938706129387059%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534103_p26871119419"><a name="en-us_topic_0201534103_p26871119419"></a><a name="en-us_topic_0201534103_p26871119419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.84871512848715%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534103_p66889116414"><a name="en-us_topic_0201534103_p66889116414"></a><a name="en-us_topic_0201534103_p66889116414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.334566543345666%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534103_p14688213413"><a name="en-us_topic_0201534103_p14688213413"></a><a name="en-us_topic_0201534103_p14688213413"></a>Specifies the port ID. </p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="en-us_topic_0201534103_section2485220121641"></a>

**Table  4**  Response parameter

<a name="en-us_topic_0201534103_table6687125821641"></a>
<table><thead align="left"><tr id="en-us_topic_0201534103_row2678790321641"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534103_p2233651921641"><a name="en-us_topic_0201534103_p2233651921641"></a><a name="en-us_topic_0201534103_p2233651921641"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534103_p6442759121641"><a name="en-us_topic_0201534103_p6442759121641"></a><a name="en-us_topic_0201534103_p6442759121641"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534103_p5780308921641"><a name="en-us_topic_0201534103_p5780308921641"></a><a name="en-us_topic_0201534103_p5780308921641"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534103_row5153866721641"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p1388252621641"><a name="en-us_topic_0201534103_p1388252621641"></a><a name="en-us_topic_0201534103_p1388252621641"></a>floatingip</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p5074280121641"><a name="en-us_topic_0201534103_p5074280121641"></a><a name="en-us_topic_0201534103_p5074280121641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p6355285621641"><a name="en-us_topic_0201534103_p6355285621641"></a><a name="en-us_topic_0201534103_p6355285621641"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534103_table8139247714">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **floatingip**  objects

<a name="en-us_topic_0201534103_table8139247714"></a>
<table><thead align="left"><tr id="en-us_topic_0201534103_row18132240714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534103_p101201250870"><a name="en-us_topic_0201534103_p101201250870"></a><a name="en-us_topic_0201534103_p101201250870"></a><strong id="en-us_topic_0201534103_b4848194719387"><a name="en-us_topic_0201534103_b4848194719387"></a><a name="en-us_topic_0201534103_b4848194719387"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534103_p161211850674"><a name="en-us_topic_0201534103_p161211850674"></a><a name="en-us_topic_0201534103_p161211850674"></a><strong id="en-us_topic_0201534103_b5423951113817"><a name="en-us_topic_0201534103_b5423951113817"></a><a name="en-us_topic_0201534103_b5423951113817"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534103_p41217502719"><a name="en-us_topic_0201534103_p41217502719"></a><a name="en-us_topic_0201534103_p41217502719"></a><strong id="en-us_topic_0201534103_b047975220387"><a name="en-us_topic_0201534103_b047975220387"></a><a name="en-us_topic_0201534103_b047975220387"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534103_row2014192410713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p6028218019164"><a name="en-us_topic_0201534103_p6028218019164"></a><a name="en-us_topic_0201534103_p6028218019164"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p5101843519164"><a name="en-us_topic_0201534103_p5101843519164"></a><a name="en-us_topic_0201534103_p5101843519164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p6000412319164"><a name="en-us_topic_0201534103_p6000412319164"></a><a name="en-us_topic_0201534103_p6000412319164"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534103_b347325413814"><a name="en-us_topic_0201534103_b347325413814"></a><a name="en-us_topic_0201534103_b347325413814"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534103_b547445453819"><a name="en-us_topic_0201534103_b547445453819"></a><a name="en-us_topic_0201534103_b547445453819"></a>DOWN</strong>, or <strong id="en-us_topic_0201534103_b19474135473816"><a name="en-us_topic_0201534103_b19474135473816"></a><a name="en-us_topic_0201534103_b19474135473816"></a>ERROR</strong>.</p>
<a name="en-us_topic_0201534103_ul10603143175810"></a><a name="en-us_topic_0201534103_ul10603143175810"></a><ul id="en-us_topic_0201534103_ul10603143175810"><li><strong id="en-us_topic_0201534103_b148291056183815"><a name="en-us_topic_0201534103_b148291056183815"></a><a name="en-us_topic_0201534103_b148291056183815"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li><li><strong id="en-us_topic_0201534103_b105673119392"><a name="en-us_topic_0201534103_b105673119392"></a><a name="en-us_topic_0201534103_b105673119392"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534103_b250519383917"><a name="en-us_topic_0201534103_b250519383917"></a><a name="en-us_topic_0201534103_b250519383917"></a>ERROR</strong> indicates that the floating IP address is abnormal. </li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534103_row4141241070"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p5513524919164"><a name="en-us_topic_0201534103_p5513524919164"></a><a name="en-us_topic_0201534103_p5513524919164"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p212111505713"><a name="en-us_topic_0201534103_p212111505713"></a><a name="en-us_topic_0201534103_p212111505713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p4121850371"><a name="en-us_topic_0201534103_p4121850371"></a><a name="en-us_topic_0201534103_p4121850371"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row614132416712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p1912112509713"><a name="en-us_topic_0201534103_p1912112509713"></a><a name="en-us_topic_0201534103_p1912112509713"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p11211850072"><a name="en-us_topic_0201534103_p11211850072"></a><a name="en-us_topic_0201534103_p11211850072"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p16122205017713"><a name="en-us_topic_0201534103_p16122205017713"></a><a name="en-us_topic_0201534103_p16122205017713"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row115102414717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p61223503712"><a name="en-us_topic_0201534103_p61223503712"></a><a name="en-us_topic_0201534103_p61223503712"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p1812220507714"><a name="en-us_topic_0201534103_p1812220507714"></a><a name="en-us_topic_0201534103_p1812220507714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p16122550274"><a name="en-us_topic_0201534103_p16122550274"></a><a name="en-us_topic_0201534103_p16122550274"></a>Specifies the external network ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row19155241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p201223504719"><a name="en-us_topic_0201534103_p201223504719"></a><a name="en-us_topic_0201534103_p201223504719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p1122155015714"><a name="en-us_topic_0201534103_p1122155015714"></a><a name="en-us_topic_0201534103_p1122155015714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p812212506713"><a name="en-us_topic_0201534103_p812212506713"></a><a name="en-us_topic_0201534103_p812212506713"></a>Specifies the ID of the belonged router.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row101514247714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p412218502718"><a name="en-us_topic_0201534103_p412218502718"></a><a name="en-us_topic_0201534103_p412218502718"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p612213506716"><a name="en-us_topic_0201534103_p612213506716"></a><a name="en-us_topic_0201534103_p612213506716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p141228504716"><a name="en-us_topic_0201534103_p141228504716"></a><a name="en-us_topic_0201534103_p141228504716"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row3164249715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p01237508720"><a name="en-us_topic_0201534103_p01237508720"></a><a name="en-us_topic_0201534103_p01237508720"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p111239501770"><a name="en-us_topic_0201534103_p111239501770"></a><a name="en-us_topic_0201534103_p111239501770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p1712316501972"><a name="en-us_topic_0201534103_p1712316501972"></a><a name="en-us_topic_0201534103_p1712316501972"></a>Specifies the private IP address of the associated port.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row21662416711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p812355018717"><a name="en-us_topic_0201534103_p812355018717"></a><a name="en-us_topic_0201534103_p812355018717"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p612316509712"><a name="en-us_topic_0201534103_p612316509712"></a><a name="en-us_topic_0201534103_p612316509712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p10487112"><a name="en-us_topic_0201534103_p10487112"></a><a name="en-us_topic_0201534103_p10487112"></a>Specifies the project ID.</p>
<p id="en-us_topic_0201534103_p51231950174"><a name="en-us_topic_0201534103_p51231950174"></a><a name="en-us_topic_0201534103_p51231950174"></a></p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row11176241720"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p11222111885214"><a name="en-us_topic_0201534103_p11222111885214"></a><a name="en-us_topic_0201534103_p11222111885214"></a>dns_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p122232018115215"><a name="en-us_topic_0201534103_p122232018115215"></a><a name="en-us_topic_0201534103_p122232018115215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p18223161825216"><a name="en-us_topic_0201534103_p18223161825216"></a><a name="en-us_topic_0201534103_p18223161825216"></a>Specifies the DNS name.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row17174241670"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p492133065713"><a name="en-us_topic_0201534103_p492133065713"></a><a name="en-us_topic_0201534103_p492133065713"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p16929300573"><a name="en-us_topic_0201534103_p16929300573"></a><a name="en-us_topic_0201534103_p16929300573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p3921230175711"><a name="en-us_topic_0201534103_p3921230175711"></a><a name="en-us_topic_0201534103_p3921230175711"></a>Specifies the DNS domain.</p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row1418142410714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p1953114119914"><a name="en-us_topic_0201534103_p1953114119914"></a><a name="en-us_topic_0201534103_p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p595318416919"><a name="en-us_topic_0201534103_p595318416919"></a><a name="en-us_topic_0201534103_p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p1395374115919"><a name="en-us_topic_0201534103_p1395374115919"></a><a name="en-us_topic_0201534103_p1395374115919"></a>Specifies the time (UTC) when the floating IP address is created.</p>
<p id="en-us_topic_0201534103_p2070141994713"><a name="en-us_topic_0201534103_p2070141994713"></a><a name="en-us_topic_0201534103_p2070141994713"></a>Format: <em id="en-us_topic_0201534103_i1163119166405"><a name="en-us_topic_0201534103_i1163119166405"></a><a name="en-us_topic_0201534103_i1163119166405"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="en-us_topic_0201534103_row1188246714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534103_p139719548912"><a name="en-us_topic_0201534103_p139719548912"></a><a name="en-us_topic_0201534103_p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534103_p53971154594"><a name="en-us_topic_0201534103_p53971154594"></a><a name="en-us_topic_0201534103_p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534103_p1339713549918"><a name="en-us_topic_0201534103_p1339713549918"></a><a name="en-us_topic_0201534103_p1339713549918"></a>Specifies the time (UTC) when the floating IP address is updated.</p>
<p id="en-us_topic_0201534103_p137222218476"><a name="en-us_topic_0201534103_p137222218476"></a><a name="en-us_topic_0201534103_p137222218476"></a>Format: <em id="en-us_topic_0201534103_i64778275404"><a name="en-us_topic_0201534103_i64778275404"></a><a name="en-us_topic_0201534103_i64778275404"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0201534103_section3510479621641"></a>

Example request 1 \(Binding a floating IP address to a port\)

```
PUT https://{Endpoint}/v2.0/floatingips/b997e0d4-3359-4c74-8f88-bc0af81cd5a2 
 
{
    "floatingip": {
           "port_id": "f91f5763-c5a2-4458-979d-61e48b3c3fac"
    }
}
```

Example response 1 \(Binding a floating IP address to a port\)

```
{
    "floatingip": {
        "id": "b997e0d4-3359-4c74-8f88-bc0af81cd5a2",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": "192.168.10.3",
        "floating_ip_address": "88.88.215.205",
        "port_id": 00587256-27e3-489b-96bf-ea80c1da4aeb,
        "created_at": "2018-09-20T02:10:02",
        "updated_at": "2018-09-20T02:10:07"
    }
}
```

Example request 2 \(Unbinding a floating IP address from a port\)

```
PUT https://{Endpoint}/v2.0/floatingips/b997e0d4-3359-4c74-8f88-bc0af81cd5a2

{
    "floatingip": {
        "port_id": null
    }
}
```

Example response 2 \(Unbinding a floating IP address from a port\)

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
        "updated_at": "2018-09-20T02:10:07"
    }
}
```

## Status Code<a name="en-us_topic_0201534103_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534103_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

