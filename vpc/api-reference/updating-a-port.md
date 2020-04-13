# Updating a Port<a name="vpc_port02_0004"></a>

## Function<a name="en-us_topic_0062207392_section23646388"></a>

This API is used to update a port.

## URI<a name="en-us_topic_0062207392_section11490904"></a>

PUT /v2.0/ports/\{port\_id\}

[Table 1](#table1855162528)  describes the parameters.

**Table  1**  Parameter description

<a name="table1855162528"></a>
<table><thead align="left"><tr id="vpc_port02_0002_row1394617591304"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="vpc_port02_0002_p159467591307"><a name="vpc_port02_0002_p159467591307"></a><a name="vpc_port02_0002_p159467591307"></a><strong id="vpc_port02_0002_b5836335194617"><a name="vpc_port02_0002_b5836335194617"></a><a name="vpc_port02_0002_b5836335194617"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="vpc_port02_0002_p1094612597019"><a name="vpc_port02_0002_p1094612597019"></a><a name="vpc_port02_0002_p1094612597019"></a><strong id="vpc_port02_0002_b040313816465"><a name="vpc_port02_0002_b040313816465"></a><a name="vpc_port02_0002_b040313816465"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="vpc_port02_0002_p29466591203"><a name="vpc_port02_0002_p29466591203"></a><a name="vpc_port02_0002_p29466591203"></a><strong id="vpc_port02_0002_b1192918393464"><a name="vpc_port02_0002_b1192918393464"></a><a name="vpc_port02_0002_b1192918393464"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_port02_0002_row1494695918012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="vpc_port02_0002_p9946159600"><a name="vpc_port02_0002_p9946159600"></a><a name="vpc_port02_0002_p9946159600"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="vpc_port02_0002_p09465594017"><a name="vpc_port02_0002_p09465594017"></a><a name="vpc_port02_0002_p09465594017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="vpc_port02_0002_p394618591401"><a name="vpc_port02_0002_p394618591401"></a><a name="vpc_port02_0002_p394618591401"></a>Specifies the port ID, which uniquely identifies the port.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0062207392_section55370462"></a>

**Table  2**  Request parameter

<a name="en-us_topic_0062207392_table10296933"></a>
<table><thead align="left"><tr id="en-us_topic_0062207392_row62640398"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.1"><p id="en-us_topic_0062207392_p40707460"><a name="en-us_topic_0062207392_p40707460"></a><a name="en-us_topic_0062207392_p40707460"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0062207392_p8970000"><a name="en-us_topic_0062207392_p8970000"></a><a name="en-us_topic_0062207392_p8970000"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.3"><p id="en-us_topic_0062207392_p55481367"><a name="en-us_topic_0062207392_p55481367"></a><a name="en-us_topic_0062207392_p55481367"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.31%" id="mcps1.2.5.1.4"><p id="en-us_topic_0062207392_p64805763"><a name="en-us_topic_0062207392_p64805763"></a><a name="en-us_topic_0062207392_p64805763"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207392_row14775484"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0062207392_p55963561"><a name="en-us_topic_0062207392_p55963561"></a><a name="en-us_topic_0062207392_p55963561"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="8.16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0062207392_p36754611"><a name="en-us_topic_0062207392_p36754611"></a><a name="en-us_topic_0062207392_p36754611"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0062207392_p24333505"><a name="en-us_topic_0062207392_p24333505"></a><a name="en-us_topic_0062207392_p24333505"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.31%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0062207386_p50516929"><a name="en-us_topic_0062207386_p50516929"></a><a name="en-us_topic_0062207386_p50516929"></a>Specifies the port object list. For details, see <a href="#table17891153981819">Table 3</a>.</p>
<p id="en-us_topic_0062207392_p22385437"><a name="en-us_topic_0062207392_p22385437"></a><a name="en-us_topic_0062207392_p22385437"></a>You must specify at least one attribute when updating a port.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **port**  objects

<a name="table17891153981819"></a>
<table><thead align="left"><tr id="row188929398187"><th class="cellrowborder" valign="top" width="26.35736426357364%" id="mcps1.2.5.1.1"><p id="p0892193917186"><a name="p0892193917186"></a><a name="p0892193917186"></a><strong id="b209646555714"><a name="b209646555714"></a><a name="b209646555714"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.608439156084392%" id="mcps1.2.5.1.2"><p id="p18759144481919"><a name="p18759144481919"></a><a name="p18759144481919"></a><strong id="b15692145610716"><a name="b15692145610716"></a><a name="b15692145610716"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.50814918508149%" id="mcps1.2.5.1.3"><p id="p6892163916182"><a name="p6892163916182"></a><a name="p6892163916182"></a><strong id="b1518413920817"><a name="b1518413920817"></a><a name="b1518413920817"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.52604739526047%" id="mcps1.2.5.1.4"><p id="p1389210394189"><a name="p1389210394189"></a><a name="p1389210394189"></a><strong id="b108212101087"><a name="b108212101087"></a><a name="b108212101087"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8892203921814"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p8892143913188"><a name="p8892143913188"></a><a name="p8892143913188"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p10759744131910"><a name="p10759744131910"></a><a name="p10759744131910"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p168921639181817"><a name="p168921639181817"></a><a name="p168921639181817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p18892339201812"><a name="p18892339201812"></a><a name="p18892339201812"></a>Specifies the port name.</p>
</td>
</tr>
<tr id="row689363918186"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p128953395185"><a name="p128953395185"></a><a name="p128953395185"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p15759134419199"><a name="p15759134419199"></a><a name="p15759134419199"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p448220335811"><a name="p448220335811"></a><a name="p448220335811"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p9895123951816"><a name="p9895123951816"></a><a name="p9895123951816"></a>Specifies the UUID of the security group, for example, <strong id="b31851922889"><a name="b31851922889"></a><a name="b31851922889"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p1389519392188"><a name="p1389519392188"></a><a name="p1389519392188"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row15895183961814"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p18895039131819"><a name="p18895039131819"></a><a name="p18895039131819"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p14761104411912"><a name="p14761104411912"></a><a name="p14761104411912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p5114142220534"><a name="p5114142220534"></a><a name="p5114142220534"></a>Array of <a href="#table1389733912184">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p1789510391184"><a name="p1789510391184"></a><a name="p1789510391184"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#table1389733912184">Table 4</a>. </p>
<p id="p19895203921819"><a name="p19895203921819"></a><a name="p19895203921819"></a>Instructions:</p>
<a name="ul14895163913188"></a><a name="ul14895163913188"></a><ul id="ul14895163913188"><li>The IP address cannot be <strong id="b163476546130"><a name="b163476546130"></a><a name="b163476546130"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b525318586139"><a name="b525318586139"></a><a name="b525318586139"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b12504172953010"><a name="b12504172953010"></a><a name="b12504172953010"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b11495545203017"><a name="b11495545203017"></a><a name="b11495545203017"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row1889513921812"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p289516398183"><a name="p289516398183"></a><a name="p289516398183"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p5761174412193"><a name="p5761174412193"></a><a name="p5761174412193"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p173831731195712"><a name="p173831731195712"></a><a name="p173831731195712"></a>Array of <a href="#table10898183911816">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p1989543981819"><a name="p1989543981819"></a><a name="p1989543981819"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table10898183911816">Table 5</a>.</p>
</td>
</tr>
<tr id="row2895739131813"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p4895123911810"><a name="p4895123911810"></a><a name="p4895123911810"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p4761174416192"><a name="p4761174416192"></a><a name="p4761174416192"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p489543912186"><a name="p489543912186"></a><a name="p489543912186"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p9895133913188"><a name="p9895133913188"></a><a name="p9895133913188"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p158951395181"><a name="p158951395181"></a><a name="p158951395181"></a>Instructions:</p>
<a name="ul198951339131813"></a><a name="ul198951339131813"></a><ul id="ul198951339131813"><li>The <strong id="b15825384319"><a name="b15825384319"></a><a name="b15825384319"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b192182010143117"><a name="b192182010143117"></a><a name="b192182010143117"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p14895143901818"><a name="p14895143901818"></a><a name="p14895143901818"></a>Example:</p>
<p id="p1689593911185"><a name="p1689593911185"></a><a name="p1689593911185"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b7282619173114"><a name="b7282619173114"></a><a name="b7282619173114"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b20538822203114"><a name="b20538822203114"></a><a name="b20538822203114"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b1353952203111"><a name="b1353952203111"></a><a name="b1353952203111"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b522563873112"><a name="b522563873112"></a><a name="b522563873112"></a>true</strong>.<p id="p489520395187"><a name="p489520395187"></a><a name="p489520395187"></a>Example:</p>
<p id="p1789513951810"><a name="p1789513951810"></a><a name="p1789513951810"></a>{"disable_security_groups": true },</p>
<p id="p9895539101812"><a name="p9895539101812"></a><a name="p9895539101812"></a>Currently, the value can only be set to <strong id="b3562751153112"><a name="b3562751153112"></a><a name="b3562751153112"></a>true</strong>. When the value is set to <strong id="b145632514319"><a name="b145632514319"></a><a name="b145632514319"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul181891610121218"></a><a name="ul181891610121218"></a>
<a name="ul16895739131811"></a><a name="ul16895739131811"></a>
</td>
</tr>
<tr id="row2895143912187"><td class="cellrowborder" valign="top" width="26.35736426357364%" headers="mcps1.2.5.1.1 "><p id="p14895123921817"><a name="p14895123921817"></a><a name="p14895123921817"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="15.608439156084392%" headers="mcps1.2.5.1.2 "><p id="p117612443198"><a name="p117612443198"></a><a name="p117612443198"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.50814918508149%" headers="mcps1.2.5.1.3 "><p id="p1289518390188"><a name="p1289518390188"></a><a name="p1289518390188"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p1289523951811"><a name="p1289523951811"></a><a name="p1289523951811"></a>Specifies the type of the bound vNIC.</p>
<p id="p618195116205"><a name="p618195116205"></a><a name="p618195116205"></a><strong id="b1452793373216"><a name="b1452793373216"></a><a name="b1452793373216"></a>normal</strong>: Softswitch</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **allow\_address\_pair**  objects

<a name="table1389733912184"></a>
<table><thead align="left"><tr id="row6898123971818"><th class="cellrowborder" valign="top" width="27.87%" id="mcps1.2.4.1.1"><p id="p989817398184"><a name="p989817398184"></a><a name="p989817398184"></a><strong id="b781312016331"><a name="b781312016331"></a><a name="b781312016331"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.67%" id="mcps1.2.4.1.2"><p id="p19898163910181"><a name="p19898163910181"></a><a name="p19898163910181"></a><strong id="b1586871123315"><a name="b1586871123315"></a><a name="b1586871123315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.459999999999994%" id="mcps1.2.4.1.3"><p id="p5898173961815"><a name="p5898173961815"></a><a name="p5898173961815"></a><strong id="b20462112113319"><a name="b20462112113319"></a><a name="b20462112113319"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row158982395184"><td class="cellrowborder" valign="top" width="27.87%" headers="mcps1.2.4.1.1 "><p id="p78981539151812"><a name="p78981539151812"></a><a name="p78981539151812"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="p1689833981819"><a name="p1689833981819"></a><a name="p1689833981819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p1689819398187"><a name="p1689819398187"></a><a name="p1689819398187"></a>Specifies the IP address.</p>
<p id="p1089812395185"><a name="p1089812395185"></a><a name="p1089812395185"></a>This parameter cannot be <strong id="b1035316518339"><a name="b1035316518339"></a><a name="b1035316518339"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="row98981639201812"><td class="cellrowborder" valign="top" width="27.87%" headers="mcps1.2.4.1.1 "><p id="p389873910186"><a name="p389873910186"></a><a name="p389873910186"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="p148981139191816"><a name="p148981139191816"></a><a name="p148981139191816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p11898133911813"><a name="p11898133911813"></a><a name="p11898133911813"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **extra\_dhcp\_opt**  objects

<a name="table10898183911816"></a>
<table><thead align="left"><tr id="row18899143991812"><th class="cellrowborder" valign="top" width="28.162816281628167%" id="mcps1.2.4.1.1"><p id="p68991939161818"><a name="p68991939161818"></a><a name="p68991939161818"></a><strong id="b424211923311"><a name="b424211923311"></a><a name="b424211923311"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.621962196219624%" id="mcps1.2.4.1.2"><p id="p78991639111813"><a name="p78991639111813"></a><a name="p78991639111813"></a><strong id="b440212103336"><a name="b440212103336"></a><a name="b440212103336"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.21522152215221%" id="mcps1.2.4.1.3"><p id="p28991391181"><a name="p28991391181"></a><a name="p28991391181"></a><strong id="b144611113338"><a name="b144611113338"></a><a name="b144611113338"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10899339141820"><td class="cellrowborder" valign="top" width="28.162816281628167%" headers="mcps1.2.4.1.1 "><p id="p98991039151815"><a name="p98991039151815"></a><a name="p98991039151815"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="19.621962196219624%" headers="mcps1.2.4.1.2 "><p id="p118999393186"><a name="p118999393186"></a><a name="p118999393186"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.4.1.3 "><p id="p189953910181"><a name="p189953910181"></a><a name="p189953910181"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row18899143971815"><td class="cellrowborder" valign="top" width="28.162816281628167%" headers="mcps1.2.4.1.1 "><p id="p48991939171810"><a name="p48991939171810"></a><a name="p48991939171810"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="19.621962196219624%" headers="mcps1.2.4.1.2 "><p id="p98998398186"><a name="p98998398186"></a><a name="p98998398186"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.4.1.3 "><p id="p168991839151814"><a name="p168991839151814"></a><a name="p168991839151814"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="en-us_topic_0062207392_section28572113"></a>

**Table  6**  Response parameter

<a name="en-us_topic_0062207392_table1281126"></a>
<table><thead align="left"><tr id="en-us_topic_0062207392_row10321460"><th class="cellrowborder" valign="top" width="15.559999999999999%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207392_p30731970"><a name="en-us_topic_0062207392_p30731970"></a><a name="en-us_topic_0062207392_p30731970"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.33%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207392_p6261652"><a name="en-us_topic_0062207392_p6261652"></a><a name="en-us_topic_0062207392_p6261652"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71.11%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207392_p12079142"><a name="en-us_topic_0062207392_p12079142"></a><a name="en-us_topic_0062207392_p12079142"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207392_row38886454"><td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207392_p62795050"><a name="en-us_topic_0062207392_p62795050"></a><a name="en-us_topic_0062207392_p62795050"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="13.33%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207392_p53234283"><a name="en-us_topic_0062207392_p53234283"></a><a name="en-us_topic_0062207392_p53234283"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="71.11%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207392_p35602929"><a name="en-us_topic_0062207392_p35602929"></a><a name="en-us_topic_0062207392_p35602929"></a>Specifies the port object list. For details, see <a href="#table15919752145624">Table 7</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **port**  objects

<a name="table15919752145624"></a>
<table><thead align="left"><tr id="row28529169145624"><th class="cellrowborder" valign="top" width="28.499999999999996%" id="mcps1.2.4.1.1"><p id="p42540009145658"><a name="p42540009145658"></a><a name="p42540009145658"></a><strong id="b3138182513314"><a name="b3138182513314"></a><a name="b3138182513314"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.4.1.2"><p id="p23188741145658"><a name="p23188741145658"></a><a name="p23188741145658"></a><strong id="b998952512331"><a name="b998952512331"></a><a name="b998952512331"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.74%" id="mcps1.2.4.1.3"><p id="p13444574145658"><a name="p13444574145658"></a><a name="p13444574145658"></a><strong id="b5652122611339"><a name="b5652122611339"></a><a name="b5652122611339"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13166425145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p28807446145658"><a name="p28807446145658"></a><a name="p28807446145658"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p51701793145658"><a name="p51701793145658"></a><a name="p51701793145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p5183528145658"><a name="p5183528145658"></a><a name="p5183528145658"></a>Specifies the port ID. A maximum of 255 characters are allowed.</p>
<p id="p189962619371"><a name="p189962619371"></a><a name="p189962619371"></a>This parameter is not mandatory when you query ports.</p>
</td>
</tr>
<tr id="row1387566145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p20696121145658"><a name="p20696121145658"></a><a name="p20696121145658"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p65773124145658"><a name="p65773124145658"></a><a name="p65773124145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p10771861145658"><a name="p10771861145658"></a><a name="p10771861145658"></a>Specifies the port name.</p>
</td>
</tr>
<tr id="row36437767145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p949776145658"><a name="p949776145658"></a><a name="p949776145658"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p9822997145658"><a name="p9822997145658"></a><a name="p9822997145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p36061910145658"><a name="p36061910145658"></a><a name="p36061910145658"></a>Specifies the ID of the network to which the port belongs.</p>
</td>
</tr>
<tr id="row41410455145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p49567182145658"><a name="p49567182145658"></a><a name="p49567182145658"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p55518807145658"><a name="p55518807145658"></a><a name="p55518807145658"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p26909682145658"><a name="p26909682145658"></a><a name="p26909682145658"></a>Specifies the administrative status.</p>
<p id="p40860550145658"><a name="p40860550145658"></a><a name="p40860550145658"></a>The value can only be <strong id="b1485682017355"><a name="b1485682017355"></a><a name="b1485682017355"></a>true</strong>.</p>
</td>
</tr>
<tr id="row11261085145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p58114882145658"><a name="p58114882145658"></a><a name="p58114882145658"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p9685031145658"><a name="p9685031145658"></a><a name="p9685031145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p8831008145658"><a name="p8831008145658"></a><a name="p8831008145658"></a>Specifies the port MAC address. For example, <strong id="b11336102343513"><a name="b11336102343513"></a><a name="b11336102343513"></a>"mac_address": "fa:16:3e:9e:ff:55"</strong>.</p>
<p id="p12370211145658"><a name="p12370211145658"></a><a name="p12370211145658"></a>This value can only be dynamically assigned by the system.</p>
</td>
</tr>
<tr id="row59425565145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p25296431145658"><a name="p25296431145658"></a><a name="p25296431145658"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p52484625913"><a name="p52484625913"></a><a name="p52484625913"></a>Array of <a href="#table4290920914597">fixed_ip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p48560910145658"><a name="p48560910145658"></a><a name="p48560910145658"></a>Specifies the port IP address. For details, see <a href="#table4290920914597">Table 8</a>. For example, the value is <strong id="b33862029103516"><a name="b33862029103516"></a><a name="b33862029103516"></a>"fixed_ips": [{"subnet_id": "4dc70db6-cb7f-4200-9790-a6a910776bba", "ip_address": "192.169.25.79"}]</strong>.</p>
</td>
</tr>
<tr id="row52336547145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p42357933145658"><a name="p42357933145658"></a><a name="p42357933145658"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p8440512145658"><a name="p8440512145658"></a><a name="p8440512145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p23990357145658"><a name="p23990357145658"></a><a name="p23990357145658"></a>Specifies the device ID.</p>
<p id="p14586626145658"><a name="p14586626145658"></a><a name="p14586626145658"></a>This value is automatically maintained by the system and cannot be set or updated manually. The port with this field specified cannot be deleted.</p>
</td>
</tr>
<tr id="row8304195145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p30450002145658"><a name="p30450002145658"></a><a name="p30450002145658"></a>device_owner</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p50531130145658"><a name="p50531130145658"></a><a name="p50531130145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p60282892145658"><a name="p60282892145658"></a><a name="p60282892145658"></a>Specifies the DHCP, router or Nova to which a device belongs.</p>
<p id="p2837225125711"><a name="p2837225125711"></a><a name="p2837225125711"></a>This parameter value cannot be updated. You can only set <strong id="b1827316507354"><a name="b1827316507354"></a><a name="b1827316507354"></a>device_owner</strong> to <strong id="b10273195013355"><a name="b10273195013355"></a><a name="b10273195013355"></a>neutron:VIP_PORT</strong> for a virtual IP address port during port creation. If this parameter of a port is not left blank, the port can only be deleted when this parameter value is <strong id="b7274150173514"><a name="b7274150173514"></a><a name="b7274150173514"></a>neutron:VIP_PORT</strong>.</p>
<p id="p1458812975819"><a name="p1458812975819"></a><a name="p1458812975819"></a>The port with this field specified cannot be deleted.</p>
</td>
</tr>
<tr id="row47218120145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p43524921145658"><a name="p43524921145658"></a><a name="p43524921145658"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p35857692145658"><a name="p35857692145658"></a><a name="p35857692145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row925022145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p12676379145658"><a name="p12676379145658"></a><a name="p12676379145658"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p20153784145658"><a name="p20153784145658"></a><a name="p20153784145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p12312282145658"><a name="p12312282145658"></a><a name="p12312282145658"></a>Specifies the port status. The value can be <strong id="b1855017234378"><a name="b1855017234378"></a><a name="b1855017234378"></a>ACTIVE</strong>, <strong id="b45511223193713"><a name="b45511223193713"></a><a name="b45511223193713"></a>BUILD</strong>, or <strong id="b5552823173712"><a name="b5552823173712"></a><a name="b5552823173712"></a>DOWN</strong>.</p>
<p id="p43701677145658"><a name="p43701677145658"></a><a name="p43701677145658"></a>The status of a HANA SR-IOV VM port is always <strong id="b12875142033719"><a name="b12875142033719"></a><a name="b12875142033719"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row36940776145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p48921078145658"><a name="p48921078145658"></a><a name="p48921078145658"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p3184354145658"><a name="p3184354145658"></a><a name="p3184354145658"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p4527282145658"><a name="p4527282145658"></a><a name="p4527282145658"></a>Specifies the UUID of the security group, for example, <strong id="b1545710381372"><a name="b1545710381372"></a><a name="b1545710381372"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p103001912487"><a name="p103001912487"></a><a name="p103001912487"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row17626705145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p41382197145658"><a name="p41382197145658"></a><a name="p41382197145658"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p11976131610013"><a name="p11976131610013"></a><a name="p11976131610013"></a>Array of <a href="#en-us_topic_0062207355_table57914257">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p30975735145658"><a name="p30975735145658"></a><a name="p30975735145658"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#en-us_topic_0062207355_table57914257">Table 9</a>. </p>
<p id="p7136530194312"><a name="p7136530194312"></a><a name="p7136530194312"></a>Instructions:</p>
<a name="ul18386852174311"></a><a name="ul18386852174311"></a><ul id="ul18386852174311"><li>The IP address cannot be <strong id="b6423115873710"><a name="b6423115873710"></a><a name="b6423115873710"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b19239023815"><a name="b19239023815"></a><a name="b19239023815"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b9454025383"><a name="b9454025383"></a><a name="b9454025383"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b85381901401"><a name="b85381901401"></a><a name="b85381901401"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row938573145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p34089655145658"><a name="p34089655145658"></a><a name="p34089655145658"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p251517111015"><a name="p251517111015"></a><a name="p251517111015"></a>Array of <a href="#table5056075615524">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p45787521145658"><a name="p45787521145658"></a><a name="p45787521145658"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table5056075615524">Table 10</a>.</p>
</td>
</tr>
<tr id="row46629855145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p62371645145658"><a name="p62371645145658"></a><a name="p62371645145658"></a>binding:vif_details</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p18938488145658"><a name="p18938488145658"></a><a name="p18938488145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p62312767145658"><a name="p62312767145658"></a><a name="p62312767145658"></a>Specifies the VIF details. Parameter <strong id="b377111453416"><a name="b377111453416"></a><a name="b377111453416"></a>ovs_hybrid_plug</strong> specifies whether the OVS/bridge hybrid mode is used.</p>
</td>
</tr>
<tr id="row35771758145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p7522524145658"><a name="p7522524145658"></a><a name="p7522524145658"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p5344685145658"><a name="p5344685145658"></a><a name="p5344685145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p4278449145658"><a name="p4278449145658"></a><a name="p4278449145658"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p38506045145658"><a name="p38506045145658"></a><a name="p38506045145658"></a>Instructions:</p>
<a name="ul11010089145658"></a><a name="ul11010089145658"></a><ul id="ul11010089145658"><li>The <strong id="b179115284220"><a name="b179115284220"></a><a name="b179115284220"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b3619616194211"><a name="b3619616194211"></a><a name="b3619616194211"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p041674418210"><a name="p041674418210"></a><a name="p041674418210"></a>Example:</p>
<p id="p1774284092111"><a name="p1774284092111"></a><a name="p1774284092111"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b15880162774213"><a name="b15880162774213"></a><a name="b15880162774213"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b1623183784619"><a name="b1623183784619"></a><a name="b1623183784619"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b4626337114611"><a name="b4626337114611"></a><a name="b4626337114611"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b1634717553465"><a name="b1634717553465"></a><a name="b1634717553465"></a>true</strong>.<p id="p19402030145658"><a name="p19402030145658"></a><a name="p19402030145658"></a>Example:</p>
<p id="p40400544145658"><a name="p40400544145658"></a><a name="p40400544145658"></a>{"disable_security_groups": true },</p>
<p id="p28060583145658"><a name="p28060583145658"></a><a name="p28060583145658"></a>Currently, the value can only be set to <strong id="b986412710471"><a name="b986412710471"></a><a name="b986412710471"></a>true</strong>. When the value is set to <strong id="b686616734719"><a name="b686616734719"></a><a name="b686616734719"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul83681416151219"></a><a name="ul83681416151219"></a>
<a name="ul51218659145658"></a><a name="ul51218659145658"></a>
</td>
</tr>
<tr id="row63233200145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p4700493145658"><a name="p4700493145658"></a><a name="p4700493145658"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p45195649145658"><a name="p45195649145658"></a><a name="p45195649145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p42146344145658"><a name="p42146344145658"></a><a name="p42146344145658"></a>Specifies the type of the bound vNIC.</p>
<p id="p43772780145658"><a name="p43772780145658"></a><a name="p43772780145658"></a><strong id="b9306541488"><a name="b9306541488"></a><a name="b9306541488"></a>normal</strong>: Softswitch</p>
</td>
</tr>
<tr id="row8784124710810"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p759775317217"><a name="p759775317217"></a><a name="p759775317217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p765335213239"><a name="p765335213239"></a><a name="p765335213239"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row19797526919"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the port is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i216393813480"><a name="i216393813480"></a><a name="i216393813480"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row124097610917"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the port is updated.</p>
<p id="p17388812174410"><a name="p17388812174410"></a><a name="p17388812174410"></a>Format: <em id="i13656194220485"><a name="i13656194220485"></a><a name="i13656194220485"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  8** **fixed\_ip**  objects

<a name="table4290920914597"></a>
<table><thead align="left"><tr id="row3523499914597"><th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.1"><p id="p6174509115118"><a name="p6174509115118"></a><a name="p6174509115118"></a><strong id="b1696964413480"><a name="b1696964413480"></a><a name="b1696964413480"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.2"><p id="p3529643715118"><a name="p3529643715118"></a><a name="p3529643715118"></a><strong id="b7304184712484"><a name="b7304184712484"></a><a name="b7304184712484"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.09480948094809%" id="mcps1.2.4.1.3"><p id="p2048854115118"><a name="p2048854115118"></a><a name="p2048854115118"></a><strong id="b02021350194818"><a name="b02021350194818"></a><a name="b02021350194818"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2319879914597"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p626497215118"><a name="p626497215118"></a><a name="p626497215118"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p3770069415118"><a name="p3770069415118"></a><a name="p3770069415118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p2612244315118"><a name="p2612244315118"></a><a name="p2612244315118"></a>Specifies the ID of the subnet to which the port belongs.</p>
<p id="p3377540315118"><a name="p3377540315118"></a><a name="p3377540315118"></a>This parameter cannot be updated.</p>
</td>
</tr>
<tr id="row636738414597"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p6042468915118"><a name="p6042468915118"></a><a name="p6042468915118"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p6256165915118"><a name="p6256165915118"></a><a name="p6256165915118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p1336175915118"><a name="p1336175915118"></a><a name="p1336175915118"></a>Specifies the port IP address.</p>
<p id="p5314696715118"><a name="p5314696715118"></a><a name="p5314696715118"></a>This parameter cannot be updated.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **allow\_address\_pair**  objects

<a name="en-us_topic_0062207355_table57914257"></a>
<table><thead align="left"><tr id="en-us_topic_0062207355_row41852331"><th class="firstcol" valign="top" width="25.81%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207355_p34595685"><a name="en-us_topic_0062207355_p34595685"></a><a name="en-us_topic_0062207355_p34595685"></a><strong id="b108271120134918"><a name="b108271120134918"></a><a name="b108271120134918"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.240000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207355_p50787128"><a name="en-us_topic_0062207355_p50787128"></a><a name="en-us_topic_0062207355_p50787128"></a><strong id="b09412222492"><a name="b09412222492"></a><a name="b09412222492"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.949999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207355_p52626454"><a name="en-us_topic_0062207355_p52626454"></a><a name="en-us_topic_0062207355_p52626454"></a><strong id="b3836172216492"><a name="b3836172216492"></a><a name="b3836172216492"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207355_row34884411"><th class="firstcol" valign="top" width="25.81%" id="mcps1.2.5.1.1" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p7065065"><a name="en-us_topic_0062207355_p7065065"></a><a name="en-us_topic_0062207355_p7065065"></a>ip_address</p>
</th>
<td class="cellrowborder" valign="top" width="26.240000000000002%" headers="mcps1.2.5.1.1 mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p35399367"><a name="en-us_topic_0062207355_p35399367"></a><a name="en-us_topic_0062207355_p35399367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.949999999999996%" headers="mcps1.2.5.1.1 mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p64721603"><a name="en-us_topic_0062207355_p64721603"></a><a name="en-us_topic_0062207355_p64721603"></a>Specifies the IP address.</p>
<p id="en-us_topic_0062207355_p45623521"><a name="en-us_topic_0062207355_p45623521"></a><a name="en-us_topic_0062207355_p45623521"></a>This parameter cannot be <strong id="b112312279495"><a name="b112312279495"></a><a name="b112312279495"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0062207355_row7958508"><th class="firstcol" valign="top" width="25.81%" id="mcps1.2.5.2.1" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p40659381"><a name="en-us_topic_0062207355_p40659381"></a><a name="en-us_topic_0062207355_p40659381"></a>mac_address</p>
</th>
<td class="cellrowborder" valign="top" width="26.240000000000002%" headers="mcps1.2.5.2.1 mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p5075526"><a name="en-us_topic_0062207355_p5075526"></a><a name="en-us_topic_0062207355_p5075526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.949999999999996%" headers="mcps1.2.5.2.1 mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p51982593"><a name="en-us_topic_0062207355_p51982593"></a><a name="en-us_topic_0062207355_p51982593"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **extra\_dhcp\_opt**  objects

<a name="table5056075615524"></a>
<table><thead align="left"><tr id="row739480215524"><th class="cellrowborder" valign="top" width="25.892589258925895%" id="mcps1.2.4.1.1"><p id="p3368663215532"><a name="p3368663215532"></a><a name="p3368663215532"></a><strong id="b18895143118496"><a name="b18895143118496"></a><a name="b18895143118496"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.072607260726073%" id="mcps1.2.4.1.2"><p id="p4426268215532"><a name="p4426268215532"></a><a name="p4426268215532"></a><strong id="b96821932144917"><a name="b96821932144917"></a><a name="b96821932144917"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.03480348034804%" id="mcps1.2.4.1.3"><p id="p3407518415532"><a name="p3407518415532"></a><a name="p3407518415532"></a><strong id="b1448493324917"><a name="b1448493324917"></a><a name="b1448493324917"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2636755215524"><td class="cellrowborder" valign="top" width="25.892589258925895%" headers="mcps1.2.4.1.1 "><p id="p2765891815532"><a name="p2765891815532"></a><a name="p2765891815532"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="26.072607260726073%" headers="mcps1.2.4.1.2 "><p id="p2577986315532"><a name="p2577986315532"></a><a name="p2577986315532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.03480348034804%" headers="mcps1.2.4.1.3 "><p id="p5884162715532"><a name="p5884162715532"></a><a name="p5884162715532"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row3942590315524"><td class="cellrowborder" valign="top" width="25.892589258925895%" headers="mcps1.2.4.1.1 "><p id="p1298235215532"><a name="p1298235215532"></a><a name="p1298235215532"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="26.072607260726073%" headers="mcps1.2.4.1.2 "><p id="p4493762615532"><a name="p4493762615532"></a><a name="p4493762615532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.03480348034804%" headers="mcps1.2.4.1.3 "><p id="p5057146315532"><a name="p5057146315532"></a><a name="p5057146315532"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0062207392_section55822426"></a>

Example request

```
PUT https://{Endpoint}/v2.0/ports/7a9a954a-eb41-4954-a300-11ab17a361a2 
 
{
    "port": {
           "name": "port-test02"
    }
}
```

Example response

```
{
    "port": {
        "id": "a7d98f3c-b42f-460b-96a1-07601e145961",
        "name": "port-test02",
        "status": "DOWN",
        "admin_state_up": true,
        "fixed_ips": [],
        "mac_address": "fa:16:3e:01:f7:90",
        "network_id": "00ae08c5-f727-49ab-ad4b-b069398aa171",
        "tenant_id": "db82c9e1415a464ea68048baa8acc6b8",
        "project_id": "db82c9e1415a464ea68048baa8acc6b8",
        "device_id": "",
        "device_owner": "",
        "security_groups": [
            "d0d58aa9-cda9-414c-9c52-6c3daf8534e6"
        ],
        "extra_dhcp_opts": [],
        "allowed_address_pairs": [],
        "binding:vnic_type": "normal",
        "binding:vif_details": {},
        "binding:profile": {},
        "port_security_enabled": true,
        "created_at": "2018-09-20T01:45:26",
        "updated_at": "2018-09-20T01:48:56"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

