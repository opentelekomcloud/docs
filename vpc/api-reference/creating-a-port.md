# Creating a Port<a name="vpc_port02_0003"></a>

## Function<a name="en-us_topic_0062207340_section45663083"></a>

This API is used to create a port.

## URI<a name="en-us_topic_0062207340_section8314568"></a>

POST /v2.0/ports

## Request Message<a name="en-us_topic_0062207340_section21522370"></a>

**Table  1**  Request parameter

<a name="en-us_topic_0062207340_table29618759"></a>
<table><thead align="left"><tr id="en-us_topic_0062207340_row3151905"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.1"><p id="en-us_topic_0062207340_p53977738"><a name="en-us_topic_0062207340_p53977738"></a><a name="en-us_topic_0062207340_p53977738"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.2%" id="mcps1.2.5.1.2"><p id="en-us_topic_0062207340_p10120656"><a name="en-us_topic_0062207340_p10120656"></a><a name="en-us_topic_0062207340_p10120656"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8.16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0062207340_p14466778"><a name="en-us_topic_0062207340_p14466778"></a><a name="en-us_topic_0062207340_p14466778"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="67.35%" id="mcps1.2.5.1.4"><p id="en-us_topic_0062207340_p30958352"><a name="en-us_topic_0062207340_p30958352"></a><a name="en-us_topic_0062207340_p30958352"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207340_row24598620"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0062207340_p46331171"><a name="en-us_topic_0062207340_p46331171"></a><a name="en-us_topic_0062207340_p46331171"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0062207340_p61837391"><a name="en-us_topic_0062207340_p61837391"></a><a name="en-us_topic_0062207340_p61837391"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="8.16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0062207340_p42772808"><a name="en-us_topic_0062207340_p42772808"></a><a name="en-us_topic_0062207340_p42772808"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.35%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0062207340_p42045429"><a name="en-us_topic_0062207340_p42045429"></a><a name="en-us_topic_0062207340_p42045429"></a>Specifies the port object list. For details, see <a href="#table15919752145624">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **port**  objects

<a name="table15919752145624"></a>
<table><thead align="left"><tr id="row28529169145624"><th class="cellrowborder" valign="top" width="21.617838216178384%" id="mcps1.2.5.1.1"><p id="p42540009145658"><a name="p42540009145658"></a><a name="p42540009145658"></a><strong id="b11881021268"><a name="b11881021268"></a><a name="b11881021268"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.90830916908309%" id="mcps1.2.5.1.2"><p id="p12649155111318"><a name="p12649155111318"></a><a name="p12649155111318"></a><strong id="b66517222619"><a name="b66517222619"></a><a name="b66517222619"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.947805219478052%" id="mcps1.2.5.1.3"><p id="p23188741145658"><a name="p23188741145658"></a><a name="p23188741145658"></a><strong id="b158071422560"><a name="b158071422560"></a><a name="b158071422560"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.52604739526047%" id="mcps1.2.5.1.4"><p id="p13444574145658"><a name="p13444574145658"></a><a name="p13444574145658"></a><strong id="b18647523462"><a name="b18647523462"></a><a name="b18647523462"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1387566145624"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p20696121145658"><a name="p20696121145658"></a><a name="p20696121145658"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p1164911519139"><a name="p1164911519139"></a><a name="p1164911519139"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p65773124145658"><a name="p65773124145658"></a><a name="p65773124145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p10771861145658"><a name="p10771861145658"></a><a name="p10771861145658"></a>Specifies the port name.</p>
</td>
</tr>
<tr id="row36437767145624"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p949776145658"><a name="p949776145658"></a><a name="p949776145658"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p13649951101311"><a name="p13649951101311"></a><a name="p13649951101311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p9822997145658"><a name="p9822997145658"></a><a name="p9822997145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p36061910145658"><a name="p36061910145658"></a><a name="p36061910145658"></a>Specifies the ID of the network to which the port belongs.</p>
</td>
</tr>
<tr id="row59425565145624"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p25296431145658"><a name="p25296431145658"></a><a name="p25296431145658"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p7649105119133"><a name="p7649105119133"></a><a name="p7649105119133"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p19425171418512"><a name="p19425171418512"></a><a name="p19425171418512"></a>Array of <a href="#table1424105920176">fixed_ip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p48560910145658"><a name="p48560910145658"></a><a name="p48560910145658"></a>Specifies the port IP address. For details, see <a href="#table1424105920176">Table 7</a>. For example, the value is <strong id="b958516471573"><a name="b958516471573"></a><a name="b958516471573"></a>"fixed_ips": [{"subnet_id": "4dc70db6-cb7f-4200-9790-a6a910776bba", "ip_address": "192.169.25.79"}]</strong>.</p>
</td>
</tr>
<tr id="row36940776145630"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p48921078145658"><a name="p48921078145658"></a><a name="p48921078145658"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p265175111316"><a name="p265175111316"></a><a name="p265175111316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p3184354145658"><a name="p3184354145658"></a><a name="p3184354145658"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p4527282145658"><a name="p4527282145658"></a><a name="p4527282145658"></a>Specifies the UUID of the security group, for example, <strong id="b6478759179"><a name="b6478759179"></a><a name="b6478759179"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p103001912487"><a name="p103001912487"></a><a name="p103001912487"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row17626705145630"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p41382197145658"><a name="p41382197145658"></a><a name="p41382197145658"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p3651451141318"><a name="p3651451141318"></a><a name="p3651451141318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p380974085115"><a name="p380974085115"></a><a name="p380974085115"></a>Array of <a href="#en-us_topic_0062207355_table57914257">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p30975735145658"><a name="p30975735145658"></a><a name="p30975735145658"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#en-us_topic_0062207355_table57914257">Table 3</a>. </p>
<p id="p7136530194312"><a name="p7136530194312"></a><a name="p7136530194312"></a>Instructions:</p>
<a name="ul18386852174311"></a><a name="ul18386852174311"></a><ul id="ul18386852174311"><li>The IP address cannot be <strong id="b3629517151219"><a name="b3629517151219"></a><a name="b3629517151219"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b312571915121"><a name="b312571915121"></a><a name="b312571915121"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b17915420121216"><a name="b17915420121216"></a><a name="b17915420121216"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b9220102512123"><a name="b9220102512123"></a><a name="b9220102512123"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row938573145630"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p34089655145658"><a name="p34089655145658"></a><a name="p34089655145658"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p76511051151311"><a name="p76511051151311"></a><a name="p76511051151311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p157814465211"><a name="p157814465211"></a><a name="p157814465211"></a>Array of <a href="#table5056075615524">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p45787521145658"><a name="p45787521145658"></a><a name="p45787521145658"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table5056075615524">Table 4</a>.</p>
</td>
</tr>
<tr id="row46629855145636"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p62371645145658"><a name="p62371645145658"></a><a name="p62371645145658"></a>binding:vif_details</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p18651251131319"><a name="p18651251131319"></a><a name="p18651251131319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p18938488145658"><a name="p18938488145658"></a><a name="p18938488145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p62312767145658"><a name="p62312767145658"></a><a name="p62312767145658"></a>Specifies the VIF details. Parameter <strong id="b131522581122"><a name="b131522581122"></a><a name="b131522581122"></a>ovs_hybrid_plug</strong> specifies whether the OVS/bridge hybrid mode is used.</p>
</td>
</tr>
<tr id="row35771758145636"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p7522524145658"><a name="p7522524145658"></a><a name="p7522524145658"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p9651115116136"><a name="p9651115116136"></a><a name="p9651115116136"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p5344685145658"><a name="p5344685145658"></a><a name="p5344685145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p4278449145658"><a name="p4278449145658"></a><a name="p4278449145658"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p38506045145658"><a name="p38506045145658"></a><a name="p38506045145658"></a>Instructions:</p>
<a name="ul11010089145658"></a><a name="ul11010089145658"></a><ul id="ul11010089145658"><li>The <strong id="b68651729191315"><a name="b68651729191315"></a><a name="b68651729191315"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b716672631919"><a name="b716672631919"></a><a name="b716672631919"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p041674418210"><a name="p041674418210"></a><a name="p041674418210"></a>Example:</p>
<p id="p1774284092111"><a name="p1774284092111"></a><a name="p1774284092111"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b206501345171913"><a name="b206501345171913"></a><a name="b206501345171913"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b133681147121913"><a name="b133681147121913"></a><a name="b133681147121913"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b1836914717198"><a name="b1836914717198"></a><a name="b1836914717198"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b5186954121919"><a name="b5186954121919"></a><a name="b5186954121919"></a>true</strong>.<p id="p19402030145658"><a name="p19402030145658"></a><a name="p19402030145658"></a>Example:</p>
<p id="p40400544145658"><a name="p40400544145658"></a><a name="p40400544145658"></a>{"disable_security_groups": true },</p>
<p id="p28060583145658"><a name="p28060583145658"></a><a name="p28060583145658"></a>Currently, the value can only be set to <strong id="b2899195713194"><a name="b2899195713194"></a><a name="b2899195713194"></a>true</strong>. When the value is set to <strong id="b99004578197"><a name="b99004578197"></a><a name="b99004578197"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul12109162518113"></a><a name="ul12109162518113"></a>
<a name="ul51218659145658"></a><a name="ul51218659145658"></a>
</td>
</tr>
<tr id="row63233200145636"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p4700493145658"><a name="p4700493145658"></a><a name="p4700493145658"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.2 "><p id="p2065120517132"><a name="p2065120517132"></a><a name="p2065120517132"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.947805219478052%" headers="mcps1.2.5.1.3 "><p id="p45195649145658"><a name="p45195649145658"></a><a name="p45195649145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.52604739526047%" headers="mcps1.2.5.1.4 "><p id="p42146344145658"><a name="p42146344145658"></a><a name="p42146344145658"></a>Specifies the type of the bound vNIC.</p>
<p id="p43772780145658"><a name="p43772780145658"></a><a name="p43772780145658"></a><strong id="b7806739142814"><a name="b7806739142814"></a><a name="b7806739142814"></a>normal</strong>: Softswitch</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **allow\_address\_pair**  objects

<a name="en-us_topic_0062207355_table57914257"></a>
<table><thead align="left"><tr id="en-us_topic_0062207355_row41852331"><th class="cellrowborder" valign="top" width="19.759999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0062207355_p34595685"><a name="en-us_topic_0062207355_p34595685"></a><a name="en-us_topic_0062207355_p34595685"></a><strong id="b13295101410302"><a name="b13295101410302"></a><a name="b13295101410302"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.879999999999999%" id="mcps1.2.5.1.2"><p id="p158591550182213"><a name="p158591550182213"></a><a name="p158591550182213"></a><strong id="b20437151953012"><a name="b20437151953012"></a><a name="b20437151953012"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.5.1.3"><p id="en-us_topic_0062207355_p50787128"><a name="en-us_topic_0062207355_p50787128"></a><a name="en-us_topic_0062207355_p50787128"></a><strong id="b54619218308"><a name="b54619218308"></a><a name="b54619218308"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.67%" id="mcps1.2.5.1.4"><p id="en-us_topic_0062207355_p52626454"><a name="en-us_topic_0062207355_p52626454"></a><a name="en-us_topic_0062207355_p52626454"></a><strong id="b1143462223010"><a name="b1143462223010"></a><a name="b1143462223010"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207355_row34884411"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0062207355_p7065065"><a name="en-us_topic_0062207355_p7065065"></a><a name="en-us_topic_0062207355_p7065065"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.5.1.2 "><p id="p108591150162214"><a name="p108591150162214"></a><a name="p108591150162214"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0062207355_p35399367"><a name="en-us_topic_0062207355_p35399367"></a><a name="en-us_topic_0062207355_p35399367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.67%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0062207355_p64721603"><a name="en-us_topic_0062207355_p64721603"></a><a name="en-us_topic_0062207355_p64721603"></a>Specifies the IP address.</p>
<p id="en-us_topic_0062207355_p45623521"><a name="en-us_topic_0062207355_p45623521"></a><a name="en-us_topic_0062207355_p45623521"></a>This parameter cannot be <strong id="b19761744113012"><a name="b19761744113012"></a><a name="b19761744113012"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0062207355_row7958508"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0062207355_p40659381"><a name="en-us_topic_0062207355_p40659381"></a><a name="en-us_topic_0062207355_p40659381"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.5.1.2 "><p id="p68591350122211"><a name="p68591350122211"></a><a name="p68591350122211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0062207355_p5075526"><a name="en-us_topic_0062207355_p5075526"></a><a name="en-us_topic_0062207355_p5075526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.67%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0062207355_p51982593"><a name="en-us_topic_0062207355_p51982593"></a><a name="en-us_topic_0062207355_p51982593"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **extra\_dhcp\_opt**  objects

<a name="table5056075615524"></a>
<table><thead align="left"><tr id="row739480215524"><th class="cellrowborder" valign="top" width="19.88%" id="mcps1.2.5.1.1"><p id="p3368663215532"><a name="p3368663215532"></a><a name="p3368663215532"></a><strong id="b19684544303"><a name="b19684544303"></a><a name="b19684544303"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.64%" id="mcps1.2.5.1.2"><p id="p578413122319"><a name="p578413122319"></a><a name="p578413122319"></a><strong id="b12231855193020"><a name="b12231855193020"></a><a name="b12231855193020"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.9%" id="mcps1.2.5.1.3"><p id="p4426268215532"><a name="p4426268215532"></a><a name="p4426268215532"></a><strong id="b0184156123018"><a name="b0184156123018"></a><a name="b0184156123018"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.58%" id="mcps1.2.5.1.4"><p id="p3407518415532"><a name="p3407518415532"></a><a name="p3407518415532"></a><strong id="b139588561303"><a name="b139588561303"></a><a name="b139588561303"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2636755215524"><td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.2.5.1.1 "><p id="p2765891815532"><a name="p2765891815532"></a><a name="p2765891815532"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="14.64%" headers="mcps1.2.5.1.2 "><p id="p878411362316"><a name="p878411362316"></a><a name="p878411362316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.9%" headers="mcps1.2.5.1.3 "><p id="p2577986315532"><a name="p2577986315532"></a><a name="p2577986315532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.2.5.1.4 "><p id="p5884162715532"><a name="p5884162715532"></a><a name="p5884162715532"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row3942590315524"><td class="cellrowborder" valign="top" width="19.88%" headers="mcps1.2.5.1.1 "><p id="p1298235215532"><a name="p1298235215532"></a><a name="p1298235215532"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="14.64%" headers="mcps1.2.5.1.2 "><p id="p1278420314232"><a name="p1278420314232"></a><a name="p1278420314232"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.9%" headers="mcps1.2.5.1.3 "><p id="p4493762615532"><a name="p4493762615532"></a><a name="p4493762615532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.2.5.1.4 "><p id="p5057146315532"><a name="p5057146315532"></a><a name="p5057146315532"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="en-us_topic_0062207340_section59483605"></a>

**Table  5**  Response parameter

<a name="en-us_topic_0062207340_table42633357"></a>
<table><thead align="left"><tr id="en-us_topic_0062207340_row53195707"><th class="cellrowborder" valign="top" width="15.559999999999999%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207340_p13884972"><a name="en-us_topic_0062207340_p13884972"></a><a name="en-us_topic_0062207340_p13884972"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.110000000000001%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207340_p50940942"><a name="en-us_topic_0062207340_p50940942"></a><a name="en-us_topic_0062207340_p50940942"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="73.33%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207340_p21379907"><a name="en-us_topic_0062207340_p21379907"></a><a name="en-us_topic_0062207340_p21379907"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207340_row54050919"><td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207340_p16048282"><a name="en-us_topic_0062207340_p16048282"></a><a name="en-us_topic_0062207340_p16048282"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="11.110000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207340_p24842503"><a name="en-us_topic_0062207340_p24842503"></a><a name="en-us_topic_0062207340_p24842503"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="73.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207340_p51342761"><a name="en-us_topic_0062207340_p51342761"></a><a name="en-us_topic_0062207340_p51342761"></a>Specifies the port information. For details, see <a href="#table923516594178">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **port**  objects

<a name="table923516594178"></a>
<table><thead align="left"><tr id="row323595915177"><th class="cellrowborder" valign="top" width="28.499999999999996%" id="mcps1.2.4.1.1"><p id="p823545971716"><a name="p823545971716"></a><a name="p823545971716"></a><strong id="b11869162313118"><a name="b11869162313118"></a><a name="b11869162313118"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.4.1.2"><p id="p12361759201719"><a name="p12361759201719"></a><a name="p12361759201719"></a><strong id="b1573644319314"><a name="b1573644319314"></a><a name="b1573644319314"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.74%" id="mcps1.2.4.1.3"><p id="p10236459121717"><a name="p10236459121717"></a><a name="p10236459121717"></a><strong id="b285464413311"><a name="b285464413311"></a><a name="b285464413311"></a>Description</strong></p>
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
<tr id="row14236145911171"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p172361159151713"><a name="p172361159151713"></a><a name="p172361159151713"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p16236165941716"><a name="p16236165941716"></a><a name="p16236165941716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p523605911719"><a name="p523605911719"></a><a name="p523605911719"></a>Specifies the port name.</p>
</td>
</tr>
<tr id="row9236185901720"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p82367590175"><a name="p82367590175"></a><a name="p82367590175"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p17236159191713"><a name="p17236159191713"></a><a name="p17236159191713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p16236175961717"><a name="p16236175961717"></a><a name="p16236175961717"></a>Specifies the ID of the network to which the port belongs.</p>
</td>
</tr>
<tr id="row2236115914175"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p17236155920178"><a name="p17236155920178"></a><a name="p17236155920178"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p223615598178"><a name="p223615598178"></a><a name="p223615598178"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p152361598171"><a name="p152361598171"></a><a name="p152361598171"></a>Specifies the administrative status.</p>
<p id="p2236259111714"><a name="p2236259111714"></a><a name="p2236259111714"></a>The value can only be <strong id="b1217512267376"><a name="b1217512267376"></a><a name="b1217512267376"></a>true</strong>.</p>
</td>
</tr>
<tr id="row11261085145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p58114882145658"><a name="p58114882145658"></a><a name="p58114882145658"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p9685031145658"><a name="p9685031145658"></a><a name="p9685031145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p8831008145658"><a name="p8831008145658"></a><a name="p8831008145658"></a>Specifies the port MAC address. For example, <strong id="b192048275398"><a name="b192048275398"></a><a name="b192048275398"></a>"mac_address": "fa:16:3e:9e:ff:55"</strong>.</p>
<p id="p12370211145658"><a name="p12370211145658"></a><a name="p12370211145658"></a>This value can only be dynamically assigned by the system.</p>
</td>
</tr>
<tr id="row122362059111720"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p8236195911712"><a name="p8236195911712"></a><a name="p8236195911712"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p449815610539"><a name="p449815610539"></a><a name="p449815610539"></a>Array of <a href="#table1424105920176">fixed_ip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p023685911174"><a name="p023685911174"></a><a name="p023685911174"></a>Specifies the port IP address. For details, see <a href="#table1424105920176">Table 7</a>. For example, the value is <strong id="b14271104810399"><a name="b14271104810399"></a><a name="b14271104810399"></a>"fixed_ips": [{"subnet_id": "4dc70db6-cb7f-4200-9790-a6a910776bba", "ip_address": "192.169.25.79"}]</strong>.</p>
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
<p id="p2837225125711"><a name="p2837225125711"></a><a name="p2837225125711"></a>This parameter value cannot be updated. You can only set <strong id="b1468214587433"><a name="b1468214587433"></a><a name="b1468214587433"></a>device_owner</strong> to <strong id="b116834585433"><a name="b116834585433"></a><a name="b116834585433"></a>neutron:VIP_PORT</strong> for a virtual IP address port during port creation. If this parameter of a port is not left blank, the port can only be deleted when this parameter value is <strong id="b16851858114315"><a name="b16851858114315"></a><a name="b16851858114315"></a>neutron:VIP_PORT</strong>.</p>
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
<tr id="row1323718599176"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p3237195910174"><a name="p3237195910174"></a><a name="p3237195910174"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p1623716594171"><a name="p1623716594171"></a><a name="p1623716594171"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p523717591175"><a name="p523717591175"></a><a name="p523717591175"></a>Specifies the port status. The value can be <strong id="b1913512224418"><a name="b1913512224418"></a><a name="b1913512224418"></a>ACTIVE</strong>, <strong id="b213517224442"><a name="b213517224442"></a><a name="b213517224442"></a>BUILD</strong>, or <strong id="b1136182215448"><a name="b1136182215448"></a><a name="b1136182215448"></a>DOWN</strong>.</p>
<p id="p823735915171"><a name="p823735915171"></a><a name="p823735915171"></a>The status of a HANA SR-IOV VM port is always <strong id="b971422614410"><a name="b971422614410"></a><a name="b971422614410"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row823725971717"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1523705981720"><a name="p1523705981720"></a><a name="p1523705981720"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p02377596178"><a name="p02377596178"></a><a name="p02377596178"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p162375598174"><a name="p162375598174"></a><a name="p162375598174"></a>Specifies the UUID of the security group, for example, <strong id="b271411334449"><a name="b271411334449"></a><a name="b271411334449"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p1723714597175"><a name="p1723714597175"></a><a name="p1723714597175"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row16237259141710"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1823705901716"><a name="p1823705901716"></a><a name="p1823705901716"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p5114142220534"><a name="p5114142220534"></a><a name="p5114142220534"></a>Array of <a href="#table13242185941715">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p52370591173"><a name="p52370591173"></a><a name="p52370591173"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#table13242185941715">Table 8</a>. </p>
<p id="p1023712595179"><a name="p1023712595179"></a><a name="p1023712595179"></a>Instructions:</p>
<a name="ul182371859131719"></a><a name="ul182371859131719"></a><ul id="ul182371859131719"><li>The IP address cannot be <strong id="b951347124414"><a name="b951347124414"></a><a name="b951347124414"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b205451448144418"><a name="b205451448144418"></a><a name="b205451448144418"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b146521151134414"><a name="b146521151134414"></a><a name="b146521151134414"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b1867318544440"><a name="b1867318544440"></a><a name="b1867318544440"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row9238165915173"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p9238459131711"><a name="p9238459131711"></a><a name="p9238459131711"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p1779121305411"><a name="p1779121305411"></a><a name="p1779121305411"></a>Array of <a href="#table1243759131714">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p32381959151718"><a name="p32381959151718"></a><a name="p32381959151718"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table1243759131714">Table 9</a>.</p>
</td>
</tr>
<tr id="row923835951719"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1123810593174"><a name="p1123810593174"></a><a name="p1123810593174"></a>binding:vif_details</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p14238159171719"><a name="p14238159171719"></a><a name="p14238159171719"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p7238155916178"><a name="p7238155916178"></a><a name="p7238155916178"></a>Specifies the VIF details. Parameter <strong id="b6244153574520"><a name="b6244153574520"></a><a name="b6244153574520"></a>ovs_hybrid_plug</strong> specifies whether the OVS/bridge hybrid mode is used.</p>
</td>
</tr>
<tr id="row1423875901713"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p182381859111716"><a name="p182381859111716"></a><a name="p182381859111716"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p16238115911176"><a name="p16238115911176"></a><a name="p16238115911176"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p12238759201715"><a name="p12238759201715"></a><a name="p12238759201715"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p1423817599179"><a name="p1423817599179"></a><a name="p1423817599179"></a>Instructions:</p>
<a name="ul1323895918178"></a><a name="ul1323895918178"></a><ul id="ul1323895918178"><li>The <strong id="b18641175415455"><a name="b18641175415455"></a><a name="b18641175415455"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b63161758184510"><a name="b63161758184510"></a><a name="b63161758184510"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p72380595178"><a name="p72380595178"></a><a name="p72380595178"></a>Example:</p>
<p id="p16238195914173"><a name="p16238195914173"></a><a name="p16238195914173"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b41303512466"><a name="b41303512466"></a><a name="b41303512466"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b1618713315466"><a name="b1618713315466"></a><a name="b1618713315466"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b1618883117464"><a name="b1618883117464"></a><a name="b1618883117464"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b83768715313"><a name="b83768715313"></a><a name="b83768715313"></a>true</strong>.<p id="p17238175951711"><a name="p17238175951711"></a><a name="p17238175951711"></a>Example:</p>
<p id="p523916592177"><a name="p523916592177"></a><a name="p523916592177"></a>{"disable_security_groups": true },</p>
<p id="p423995931715"><a name="p423995931715"></a><a name="p423995931715"></a>Currently, the value can only be set to <strong id="b155712011932"><a name="b155712011932"></a><a name="b155712011932"></a>true</strong>. When the value is set to <strong id="b75723114316"><a name="b75723114316"></a><a name="b75723114316"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul88867533115"></a><a name="ul88867533115"></a>
</td>
</tr>
<tr id="row1923995919171"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p82391459121715"><a name="p82391459121715"></a><a name="p82391459121715"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p224035916176"><a name="p224035916176"></a><a name="p224035916176"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1524025912179"><a name="p1524025912179"></a><a name="p1524025912179"></a>Specifies the type of the bound vNIC.</p>
<p id="p13240185916172"><a name="p13240185916172"></a><a name="p13240185916172"></a><strong id="b10470194413"><a name="b10470194413"></a><a name="b10470194413"></a>normal</strong>: Softswitch</p>
</td>
</tr>
<tr id="row8784124710810"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p759775317217"><a name="p759775317217"></a><a name="p759775317217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p13416184120236"><a name="p13416184120236"></a><a name="p13416184120236"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row19797526919"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the port is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i31011552942"><a name="i31011552942"></a><a name="i31011552942"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row124097610917"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the port is updated.</p>
<p id="p096314469434"><a name="p096314469434"></a><a name="p096314469434"></a>Format: <em id="i10386835512"><a name="i10386835512"></a><a name="i10386835512"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  7** **fixed\_ip**  objects

<a name="table1424105920176"></a>
<table><thead align="left"><tr id="row82411959181716"><th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.1"><p id="p12241155901717"><a name="p12241155901717"></a><a name="p12241155901717"></a><strong id="b117351694514"><a name="b117351694514"></a><a name="b117351694514"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.2"><p id="p19242135915171"><a name="p19242135915171"></a><a name="p19242135915171"></a><strong id="b1559451018510"><a name="b1559451018510"></a><a name="b1559451018510"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.09480948094809%" id="mcps1.2.4.1.3"><p id="p22425592175"><a name="p22425592175"></a><a name="p22425592175"></a><strong id="b0402101113515"><a name="b0402101113515"></a><a name="b0402101113515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1824216590171"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p10242135912173"><a name="p10242135912173"></a><a name="p10242135912173"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p13242175917172"><a name="p13242175917172"></a><a name="p13242175917172"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p16242165917172"><a name="p16242165917172"></a><a name="p16242165917172"></a>Specifies the ID of the subnet to which the port belongs.</p>
<p id="p18242559181712"><a name="p18242559181712"></a><a name="p18242559181712"></a>This parameter cannot be updated.</p>
</td>
</tr>
<tr id="row19242115921715"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p52421597171"><a name="p52421597171"></a><a name="p52421597171"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p19242159101715"><a name="p19242159101715"></a><a name="p19242159101715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p1324225914173"><a name="p1324225914173"></a><a name="p1324225914173"></a>Specifies the port IP address.</p>
<p id="p142421597171"><a name="p142421597171"></a><a name="p142421597171"></a>This parameter cannot be updated.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **allow\_address\_pair**  objects

<a name="table13242185941715"></a>
<table><thead align="left"><tr id="row1424216590179"><th class="cellrowborder" valign="top" width="25.89%" id="mcps1.2.4.1.1"><p id="p192423596172"><a name="p192423596172"></a><a name="p192423596172"></a><strong id="b165131428856"><a name="b165131428856"></a><a name="b165131428856"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.07%" id="mcps1.2.4.1.2"><p id="p22424595171"><a name="p22424595171"></a><a name="p22424595171"></a><strong id="b176798311056"><a name="b176798311056"></a><a name="b176798311056"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.04%" id="mcps1.2.4.1.3"><p id="p824225991716"><a name="p824225991716"></a><a name="p824225991716"></a><strong id="b347518334515"><a name="b347518334515"></a><a name="b347518334515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row132423598170"><td class="cellrowborder" valign="top" width="25.89%" headers="mcps1.2.4.1.1 "><p id="p424285961710"><a name="p424285961710"></a><a name="p424285961710"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="26.07%" headers="mcps1.2.4.1.2 "><p id="p12431859111711"><a name="p12431859111711"></a><a name="p12431859111711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.04%" headers="mcps1.2.4.1.3 "><p id="p4243135921717"><a name="p4243135921717"></a><a name="p4243135921717"></a>Specifies the IP address.</p>
<p id="p424395914172"><a name="p424395914172"></a><a name="p424395914172"></a>This parameter cannot be <strong id="b102431537251"><a name="b102431537251"></a><a name="b102431537251"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="row424375911712"><td class="cellrowborder" valign="top" width="25.89%" headers="mcps1.2.4.1.1 "><p id="p3243145918179"><a name="p3243145918179"></a><a name="p3243145918179"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="26.07%" headers="mcps1.2.4.1.2 "><p id="p14243175911711"><a name="p14243175911711"></a><a name="p14243175911711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.04%" headers="mcps1.2.4.1.3 "><p id="p16243659181717"><a name="p16243659181717"></a><a name="p16243659181717"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **extra\_dhcp\_opt**  objects

<a name="table1243759131714"></a>
<table><thead align="left"><tr id="row172431659121719"><th class="cellrowborder" valign="top" width="25.892589258925895%" id="mcps1.2.4.1.1"><p id="p3243125918170"><a name="p3243125918170"></a><a name="p3243125918170"></a><strong id="b522918441159"><a name="b522918441159"></a><a name="b522918441159"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.332633263326333%" id="mcps1.2.4.1.2"><p id="p624314592174"><a name="p624314592174"></a><a name="p624314592174"></a><strong id="b131315451351"><a name="b131315451351"></a><a name="b131315451351"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.774777477747776%" id="mcps1.2.4.1.3"><p id="p3243359191710"><a name="p3243359191710"></a><a name="p3243359191710"></a><strong id="b12858845555"><a name="b12858845555"></a><a name="b12858845555"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1224395911717"><td class="cellrowborder" valign="top" width="25.892589258925895%" headers="mcps1.2.4.1.1 "><p id="p15244259171718"><a name="p15244259171718"></a><a name="p15244259171718"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="26.332633263326333%" headers="mcps1.2.4.1.2 "><p id="p14244145916177"><a name="p14244145916177"></a><a name="p14244145916177"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p182446594178"><a name="p182446594178"></a><a name="p182446594178"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row924445915176"><td class="cellrowborder" valign="top" width="25.892589258925895%" headers="mcps1.2.4.1.1 "><p id="p1244155931716"><a name="p1244155931716"></a><a name="p1244155931716"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="26.332633263326333%" headers="mcps1.2.4.1.2 "><p id="p32441590178"><a name="p32441590178"></a><a name="p32441590178"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p7244125921713"><a name="p7244125921713"></a><a name="p7244125921713"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0062207340_section65590400"></a>

Example request

```
POST https://{Endpoint}/v2.0/ports

{
    "port": {
       "admin_state_up": true,
        "network_id": "00ae08c5-f727-49ab-ad4b-b069398aa171",
        "name": "port-test"
    }
}
```

Example response

```
{
    "port": {
        "id": "a7d98f3c-b42f-460b-96a1-07601e145961",
        "name": "port-test",
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
        "updated_at": "2018-09-20T01:45:26"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

