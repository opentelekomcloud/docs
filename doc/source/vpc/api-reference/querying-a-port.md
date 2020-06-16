# Querying a Port<a name="vpc_port02_0002"></a>

## Function<a name="en-us_topic_0062207351_section48492792"></a>

This API is used to query details about a specified port.

## URI<a name="en-us_topic_0062207351_section33781949"></a>

GET /v2.0/ports/\{port\_id\}

[Table 1](#table59011559707)  describes the parameters.

**Table  1**  Parameter description

<a name="table59011559707"></a>
<table><thead align="left"><tr id="row1394617591304"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p159467591307"><a name="p159467591307"></a><a name="p159467591307"></a><strong id="b5836335194617"><a name="b5836335194617"></a><a name="b5836335194617"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1094612597019"><a name="p1094612597019"></a><a name="p1094612597019"></a><strong id="b040313816465"><a name="b040313816465"></a><a name="b040313816465"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p29466591203"><a name="p29466591203"></a><a name="p29466591203"></a><strong id="b1192918393464"><a name="b1192918393464"></a><a name="b1192918393464"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1494695918012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9946159600"><a name="p9946159600"></a><a name="p9946159600"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p09465594017"><a name="p09465594017"></a><a name="p09465594017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p394618591401"><a name="p394618591401"></a><a name="p394618591401"></a>Specifies the port ID, which uniquely identifies the port.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0062207351_section65197270"></a>

None

## Response Message<a name="en-us_topic_0062207351_section49904522"></a>

**Table  2**  Response parameter

<a name="en-us_topic_0062207351_table21718662"></a>
<table><thead align="left"><tr id="en-us_topic_0062207351_row2001795"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207351_p27927672"><a name="en-us_topic_0062207351_p27927672"></a><a name="en-us_topic_0062207351_p27927672"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207351_p47548937"><a name="en-us_topic_0062207351_p47548937"></a><a name="en-us_topic_0062207351_p47548937"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207351_p46581538"><a name="en-us_topic_0062207351_p46581538"></a><a name="en-us_topic_0062207351_p46581538"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207351_row15008249"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207351_p7708685"><a name="en-us_topic_0062207351_p7708685"></a><a name="en-us_topic_0062207351_p7708685"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207351_p20423749"><a name="en-us_topic_0062207351_p20423749"></a><a name="en-us_topic_0062207351_p20423749"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207351_p50928963"><a name="en-us_topic_0062207351_p50928963"></a><a name="en-us_topic_0062207351_p50928963"></a>Specifies the port object list. For details, see <a href="#table15919752145624">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **port**  objects

<a name="table15919752145624"></a>
<table><thead align="left"><tr id="row28529169145624"><th class="cellrowborder" valign="top" width="28.499999999999996%" id="mcps1.2.4.1.1"><p id="p42540009145658"><a name="p42540009145658"></a><a name="p42540009145658"></a><strong id="b3360132825412"><a name="b3360132825412"></a><a name="b3360132825412"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.4.1.2"><p id="p23188741145658"><a name="p23188741145658"></a><a name="p23188741145658"></a><strong id="b1978242915548"><a name="b1978242915548"></a><a name="b1978242915548"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.74%" id="mcps1.2.4.1.3"><p id="p13444574145658"><a name="p13444574145658"></a><a name="p13444574145658"></a><strong id="b964253018544"><a name="b964253018544"></a><a name="b964253018544"></a>Description</strong></p>
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
<p id="p40860550145658"><a name="p40860550145658"></a><a name="p40860550145658"></a>The value can only be <strong id="b89691088552"><a name="b89691088552"></a><a name="b89691088552"></a>true</strong>.</p>
</td>
</tr>
<tr id="row11261085145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p58114882145658"><a name="p58114882145658"></a><a name="p58114882145658"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p9685031145658"><a name="p9685031145658"></a><a name="p9685031145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p8831008145658"><a name="p8831008145658"></a><a name="p8831008145658"></a>Specifies the port MAC address. For example, <strong id="b594616110554"><a name="b594616110554"></a><a name="b594616110554"></a>"mac_address": "fa:16:3e:9e:ff:55"</strong>.</p>
<p id="p12370211145658"><a name="p12370211145658"></a><a name="p12370211145658"></a>This value can only be dynamically assigned by the system.</p>
</td>
</tr>
<tr id="row59425565145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p25296431145658"><a name="p25296431145658"></a><a name="p25296431145658"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p1059419436401"><a name="p1059419436401"></a><a name="p1059419436401"></a>Array of <a href="#table4290920914597">fixed_ip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p48560910145658"><a name="p48560910145658"></a><a name="p48560910145658"></a>Specifies the port IP address. For details, see <a href="#table4290920914597">Table 4</a>. For example, the value is <strong id="b101500277552"><a name="b101500277552"></a><a name="b101500277552"></a>"fixed_ips": [{"subnet_id": "4dc70db6-cb7f-4200-9790-a6a910776bba", "ip_address": "192.169.25.79"}]</strong>.</p>
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
<p id="p2837225125711"><a name="p2837225125711"></a><a name="p2837225125711"></a>This parameter value cannot be updated. You can only set <strong id="b57641952175519"><a name="b57641952175519"></a><a name="b57641952175519"></a>device_owner</strong> to <strong id="b376445211554"><a name="b376445211554"></a><a name="b376445211554"></a>neutron:VIP_PORT</strong> for a virtual IP address port during port creation. If this parameter of a port is not left blank, the port can only be deleted when this parameter value is <strong id="b9765652125517"><a name="b9765652125517"></a><a name="b9765652125517"></a>neutron:VIP_PORT</strong>.</p>
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
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p12312282145658"><a name="p12312282145658"></a><a name="p12312282145658"></a>Specifies the port status. The value can be <strong id="b15116122335618"><a name="b15116122335618"></a><a name="b15116122335618"></a>ACTIVE</strong>, <strong id="b4116192314563"><a name="b4116192314563"></a><a name="b4116192314563"></a>BUILD</strong>, or <strong id="b211711233564"><a name="b211711233564"></a><a name="b211711233564"></a>DOWN</strong>.</p>
<p id="p43701677145658"><a name="p43701677145658"></a><a name="p43701677145658"></a>The status of a HANA SR-IOV VM port is always <strong id="b1078516252566"><a name="b1078516252566"></a><a name="b1078516252566"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row36940776145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p48921078145658"><a name="p48921078145658"></a><a name="p48921078145658"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p3184354145658"><a name="p3184354145658"></a><a name="p3184354145658"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p4527282145658"><a name="p4527282145658"></a><a name="p4527282145658"></a>Specifies the UUID of the security group, for example, <strong id="b12877330105616"><a name="b12877330105616"></a><a name="b12877330105616"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p103001912487"><a name="p103001912487"></a><a name="p103001912487"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row17626705145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p41382197145658"><a name="p41382197145658"></a><a name="p41382197145658"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p94821354415"><a name="p94821354415"></a><a name="p94821354415"></a>Array of <a href="#en-us_topic_0062207355_table57914257">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p30975735145658"><a name="p30975735145658"></a><a name="p30975735145658"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#en-us_topic_0062207355_table57914257">Table 5</a>.</p>
<p id="p7136530194312"><a name="p7136530194312"></a><a name="p7136530194312"></a>Instructions:</p>
<a name="ul18386852174311"></a><a name="ul18386852174311"></a><ul id="ul18386852174311"><li>The IP address cannot be <strong id="b11284040175611"><a name="b11284040175611"></a><a name="b11284040175611"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b9945174155619"><a name="b9945174155619"></a><a name="b9945174155619"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b5151174417566"><a name="b5151174417566"></a><a name="b5151174417566"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b1521512483562"><a name="b1521512483562"></a><a name="b1521512483562"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row938573145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p34089655145658"><a name="p34089655145658"></a><a name="p34089655145658"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p9798680145658"><a name="p9798680145658"></a><a name="p9798680145658"></a>Array of <a href="#table5056075615524">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p45787521145658"><a name="p45787521145658"></a><a name="p45787521145658"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table5056075615524">Table 6</a>.</p>
</td>
</tr>
<tr id="row46629855145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p62371645145658"><a name="p62371645145658"></a><a name="p62371645145658"></a>binding:vif_details</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p18938488145658"><a name="p18938488145658"></a><a name="p18938488145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p62312767145658"><a name="p62312767145658"></a><a name="p62312767145658"></a>Specifies the VIF details. Parameter <strong id="b12448138155717"><a name="b12448138155717"></a><a name="b12448138155717"></a>ovs_hybrid_plug</strong> specifies whether the OVS/bridge hybrid mode is used.</p>
</td>
</tr>
<tr id="row35771758145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p7522524145658"><a name="p7522524145658"></a><a name="p7522524145658"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p5344685145658"><a name="p5344685145658"></a><a name="p5344685145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p4278449145658"><a name="p4278449145658"></a><a name="p4278449145658"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p38506045145658"><a name="p38506045145658"></a><a name="p38506045145658"></a>Instructions:</p>
<a name="ul11010089145658"></a><a name="ul11010089145658"></a><ul id="ul11010089145658"><li>The <strong id="b421212955918"><a name="b421212955918"></a><a name="b421212955918"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b2088271185910"><a name="b2088271185910"></a><a name="b2088271185910"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p041674418210"><a name="p041674418210"></a><a name="p041674418210"></a>Example:</p>
<p id="p1774284092111"><a name="p1774284092111"></a><a name="p1774284092111"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b18449305592"><a name="b18449305592"></a><a name="b18449305592"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b592883235917"><a name="b592883235917"></a><a name="b592883235917"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b1292923255911"><a name="b1292923255911"></a><a name="b1292923255911"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b1796144065916"><a name="b1796144065916"></a><a name="b1796144065916"></a>true</strong>.<p id="p19402030145658"><a name="p19402030145658"></a><a name="p19402030145658"></a>Example:</p>
<p id="p40400544145658"><a name="p40400544145658"></a><a name="p40400544145658"></a>{"disable_security_groups": true },</p>
<p id="p28060583145658"><a name="p28060583145658"></a><a name="p28060583145658"></a>Currently, the value can only be set to <strong id="b1895884416596"><a name="b1895884416596"></a><a name="b1895884416596"></a>true</strong>. When the value is set to <strong id="b2095844420596"><a name="b2095844420596"></a><a name="b2095844420596"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul51218659145658"></a><a name="ul51218659145658"></a>
</td>
</tr>
<tr id="row63233200145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p4700493145658"><a name="p4700493145658"></a><a name="p4700493145658"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p45195649145658"><a name="p45195649145658"></a><a name="p45195649145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p42146344145658"><a name="p42146344145658"></a><a name="p42146344145658"></a>Specifies the type of the bound vNIC.</p>
<p id="p43772780145658"><a name="p43772780145658"></a><a name="p43772780145658"></a><strong id="b11218719012"><a name="b11218719012"></a><a name="b11218719012"></a>normal</strong>: Softswitch</p>
</td>
</tr>
<tr id="row8784124710810"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p759775317217"><a name="p759775317217"></a><a name="p759775317217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p363353052314"><a name="p363353052314"></a><a name="p363353052314"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row19797526919"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the port is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1532513481439"><a name="i1532513481439"></a><a name="i1532513481439"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row124097610917"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the port is updated.</p>
<p id="p1242622584318"><a name="p1242622584318"></a><a name="p1242622584318"></a>Format: <em id="i51810361242"><a name="i51810361242"></a><a name="i51810361242"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fixed\_ip**  objects

<a name="table4290920914597"></a>
<table><thead align="left"><tr id="row3523499914597"><th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.1"><p id="p6174509115118"><a name="p6174509115118"></a><a name="p6174509115118"></a><strong id="b1198812371548"><a name="b1198812371548"></a><a name="b1198812371548"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.2"><p id="p3529643715118"><a name="p3529643715118"></a><a name="p3529643715118"></a><strong id="b167413397418"><a name="b167413397418"></a><a name="b167413397418"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.09480948094809%" id="mcps1.2.4.1.3"><p id="p2048854115118"><a name="p2048854115118"></a><a name="p2048854115118"></a><strong id="b665712391649"><a name="b665712391649"></a><a name="b665712391649"></a>Description</strong></p>
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

**Table  5** **allow\_address\_pair**  objects

<a name="en-us_topic_0062207355_table57914257"></a>
<table><thead align="left"><tr id="en-us_topic_0062207355_row41852331"><th class="cellrowborder" valign="top" width="27.87%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207355_p34595685"><a name="en-us_topic_0062207355_p34595685"></a><a name="en-us_topic_0062207355_p34595685"></a><strong id="b17909511947"><a name="b17909511947"></a><a name="b17909511947"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207355_p50787128"><a name="en-us_topic_0062207355_p50787128"></a><a name="en-us_topic_0062207355_p50787128"></a><strong id="b151815210417"><a name="b151815210417"></a><a name="b151815210417"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.459999999999994%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207355_p52626454"><a name="en-us_topic_0062207355_p52626454"></a><a name="en-us_topic_0062207355_p52626454"></a><strong id="b0870852344"><a name="b0870852344"></a><a name="b0870852344"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207355_row34884411"><td class="cellrowborder" valign="top" width="27.87%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p7065065"><a name="en-us_topic_0062207355_p7065065"></a><a name="en-us_topic_0062207355_p7065065"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p35399367"><a name="en-us_topic_0062207355_p35399367"></a><a name="en-us_topic_0062207355_p35399367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p64721603"><a name="en-us_topic_0062207355_p64721603"></a><a name="en-us_topic_0062207355_p64721603"></a>Specifies the IP address.</p>
<p id="en-us_topic_0062207355_p45623521"><a name="en-us_topic_0062207355_p45623521"></a><a name="en-us_topic_0062207355_p45623521"></a>This parameter cannot be <strong id="b13867655047"><a name="b13867655047"></a><a name="b13867655047"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0062207355_row7958508"><td class="cellrowborder" valign="top" width="27.87%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p40659381"><a name="en-us_topic_0062207355_p40659381"></a><a name="en-us_topic_0062207355_p40659381"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p5075526"><a name="en-us_topic_0062207355_p5075526"></a><a name="en-us_topic_0062207355_p5075526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p51982593"><a name="en-us_topic_0062207355_p51982593"></a><a name="en-us_topic_0062207355_p51982593"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **extra\_dhcp\_opt**  objects

<a name="table5056075615524"></a>
<table><thead align="left"><tr id="row739480215524"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p3368663215532"><a name="p3368663215532"></a><a name="p3368663215532"></a><strong id="b13157115557"><a name="b13157115557"></a><a name="b13157115557"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p4426268215532"><a name="p4426268215532"></a><a name="p4426268215532"></a><strong id="b13718619520"><a name="b13718619520"></a><a name="b13718619520"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3407518415532"><a name="p3407518415532"></a><a name="p3407518415532"></a><strong id="b3392712516"><a name="b3392712516"></a><a name="b3392712516"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2636755215524"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2765891815532"><a name="p2765891815532"></a><a name="p2765891815532"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2577986315532"><a name="p2577986315532"></a><a name="p2577986315532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5884162715532"><a name="p5884162715532"></a><a name="p5884162715532"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row3942590315524"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1298235215532"><a name="p1298235215532"></a><a name="p1298235215532"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4493762615532"><a name="p4493762615532"></a><a name="p4493762615532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5057146315532"><a name="p5057146315532"></a><a name="p5057146315532"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0062207351_section46487516"></a>

Example request

```
GET https://{Endpoint}/v2.0/ports/791870bd-36a7-4d9b-b015-a78e9b06af08
```

Example response

```
{
    "port": {
        "id": "791870bd-36a7-4d9b-b015-a78e9b06af08",
        "name": "port-test",
        "status": "DOWN",
        "admin_state_up": true,
        "fixed_ips": [],
        "mac_address": "fa:16:3e:01:e0:b2",
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
        "created_at": "2018-09-13T01:43:41",
        "updated_at": "2018-09-13T01:43:41"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

