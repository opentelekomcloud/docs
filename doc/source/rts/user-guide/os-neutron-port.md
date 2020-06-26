# OS::Neutron::Port<a name="EN-US_TOPIC_0088407083"></a>

A resource for managing Neutron ports.

A port represents a virtual switch port on a logical network switch. Virtual instances attach their interfaces into ports. The logical port also defines the MAC address and the IP address\(es\) to be assigned to the interfaces plugged into them. When IP addresses are associated to a port, this also implies the port is associated with a subnet, as the IP address was taken from the allocation pool for a specific subnet.

## Required Properties<a name="section1957373324"></a>

<a name="table105281922163315"></a>
<table><thead align="left"><tr id="row365522414254"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p16528152213310"><a name="p16528152213310"></a><a name="p16528152213310"></a><strong id="b166162305398"><a name="b166162305398"></a><a name="b166162305398"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p1052810228330"><a name="p1052810228330"></a><a name="p1052810228330"></a><strong id="b5617143011399"><a name="b5617143011399"></a><a name="b5617143011399"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row665518247254"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p0528192216331"><a name="p0528192216331"></a><a name="p0528192216331"></a>network</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p27571493"><a name="p27571493"></a><a name="p27571493"></a>Network this port belongs to. If you plan to use current port to assign Floating IP, you should specify fixed_ips with subnet. Note if this changes to a different network update, the port will be replaced.</p>
<p id="p46816848"><a name="p46816848"></a><a name="p46816848"></a>String value expected.</p>
<p id="p18698456"><a name="p18698456"></a><a name="p18698456"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section11170134663211"></a>

<a name="table1918420101341"></a>
<table><thead align="left"><tr id="row1860344310266"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p9419920153410"><a name="p9419920153410"></a><a name="p9419920153410"></a><strong id="b1696465482615"><a name="b1696465482615"></a><a name="b1696465482615"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p114201220163420"><a name="p114201220163420"></a><a name="p114201220163420"></a><strong id="b11965354162619"><a name="b11965354162619"></a><a name="b11965354162619"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row136031543172620"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p6185111093410"><a name="p6185111093410"></a><a name="p6185111093410"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p16513657"><a name="p16513657"></a><a name="p16513657"></a>The administrative state of this port.</p>
<p id="p14405187"><a name="p14405187"></a><a name="p14405187"></a>Boolean value expected.</p>
<p id="p62537827"><a name="p62537827"></a><a name="p62537827"></a>Can be updated without replacement.</p>
<p id="p25969537"><a name="p25969537"></a><a name="p25969537"></a>Defaults to "True".</p>
</td>
</tr>
<tr id="row8603543182613"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p3185710203413"><a name="p3185710203413"></a><a name="p3185710203413"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p23157763"><a name="p23157763"></a><a name="p23157763"></a>Additional MAC/IP address pairs allowed to pass through the port.</p>
<p id="p7093282"><a name="p7093282"></a><a name="p7093282"></a>List value expected.</p>
<p id="p63839538"><a name="p63839538"></a><a name="p63839538"></a>Can be updated without replacement.</p>
<p id="p37684933"><a name="p37684933"></a><a name="p37684933"></a><em id="i15271547"><a name="i15271547"></a><a name="i15271547"></a>List contents:</em></p>
<a name="ul32580770"></a><a name="ul32580770"></a><ul id="ul32580770"><li>*<p id="p21796703"><a name="p21796703"></a><a name="p21796703"></a>Map value expected.</p>
<p id="p61952601"><a name="p61952601"></a><a name="p61952601"></a>Can be updated without replacement.</p>
<p id="p98584218354"><a name="p98584218354"></a><a name="p98584218354"></a><em id="i48832851"><a name="i48832851"></a><a name="i48832851"></a>Map properties:</em></p>
<a name="ul20901159153510"></a><a name="ul20901159153510"></a><ul id="ul20901159153510"><li>ip_address<p id="p090820258353"><a name="p090820258353"></a><a name="p090820258353"></a>IP address to allow through this port.</p>
<p id="p1990962563510"><a name="p1990962563510"></a><a name="p1990962563510"></a>String value expected.</p>
<p id="p209093254355"><a name="p209093254355"></a><a name="p209093254355"></a>Can be updated without replacement.</p>
</li><li>mac_address<p id="p11082921"><a name="p11082921"></a><a name="p11082921"></a>MAC address to allow through this port.</p>
<p id="p32637431"><a name="p32637431"></a><a name="p32637431"></a>String value expected.</p>
<p id="p14986633173513"><a name="p14986633173513"></a><a name="p14986633173513"></a>Can be updated without replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row960313435266"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p11185111012345"><a name="p11185111012345"></a><a name="p11185111012345"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p36149492"><a name="p36149492"></a><a name="p36149492"></a>Device ID of this port.</p>
<p id="p56909976"><a name="p56909976"></a><a name="p56909976"></a>String value expected.</p>
<p id="p42427740"><a name="p42427740"></a><a name="p42427740"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row360344342614"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p218521033415"><a name="p218521033415"></a><a name="p218521033415"></a>device_owner</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p14094929"><a name="p14094929"></a><a name="p14094929"></a>Name of the network owning the port. The value is typically network:floatingip or network:router_interface or network:dhcp.</p>
<p id="p59745499"><a name="p59745499"></a><a name="p59745499"></a>String value expected.</p>
<p id="p838586"><a name="p838586"></a><a name="p838586"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row66031243152610"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1185101015349"><a name="p1185101015349"></a><a name="p1185101015349"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p816640"><a name="p816640"></a><a name="p816640"></a>Desired IP addresses for this port.</p>
<p id="p7349761"><a name="p7349761"></a><a name="p7349761"></a>List value expected.</p>
<p id="p66147850"><a name="p66147850"></a><a name="p66147850"></a>Can be updated without replacement.</p>
<p id="p58459740"><a name="p58459740"></a><a name="p58459740"></a><em id="i46817064"><a name="i46817064"></a><a name="i46817064"></a>List contents:</em></p>
<a name="ul37618504"></a><a name="ul37618504"></a><ul id="ul37618504"><li>*<p id="p27199980"><a name="p27199980"></a><a name="p27199980"></a>Map value expected.</p>
<p id="p43473235"><a name="p43473235"></a><a name="p43473235"></a>Can be updated without replacement.</p>
<p id="p16397641143610"><a name="p16397641143610"></a><a name="p16397641143610"></a><em id="i30316242"><a name="i30316242"></a><a name="i30316242"></a>Map properties:</em></p>
<a name="ul9439114816368"></a><a name="ul9439114816368"></a><ul id="ul9439114816368"><li>subnet<p id="p11418710143713"><a name="p11418710143713"></a><a name="p11418710143713"></a>Subnet in which to allocate the IP address for this port.</p>
<p id="p9419510173719"><a name="p9419510173719"></a><a name="p9419510173719"></a>String value expected.</p>
<p id="p84205105376"><a name="p84205105376"></a><a name="p84205105376"></a>Can be updated without replacement.</p>
</li><li>subnet_id<p id="p122119190373"><a name="p122119190373"></a><a name="p122119190373"></a>String value expected.</p>
<p id="p521218191375"><a name="p521218191375"></a><a name="p521218191375"></a>Can be updated without replacement.</p>
</li><li>ip_address<p id="p82864276379"><a name="p82864276379"></a><a name="p82864276379"></a>IP address desired in the subnet for this port.</p>
<p id="p10287527113718"><a name="p10287527113718"></a><a name="p10287527113718"></a>String value expected.</p>
<p id="p17288142793717"><a name="p17288142793717"></a><a name="p17288142793717"></a>Can be updated without replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row160354392616"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p13185181023415"><a name="p13185181023415"></a><a name="p13185181023415"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p27016387"><a name="p27016387"></a><a name="p27016387"></a>MAC address to give to this port.</p>
<p id="p41820892"><a name="p41820892"></a><a name="p41820892"></a>String value expected.</p>
<p id="p40843711"><a name="p40843711"></a><a name="p40843711"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row760394319266"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p181851910113411"><a name="p181851910113411"></a><a name="p181851910113411"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p20006320"><a name="p20006320"></a><a name="p20006320"></a>A symbolic name for this port.</p>
<p id="p45839160"><a name="p45839160"></a><a name="p45839160"></a>String value expected.</p>
<p id="p9899262"><a name="p9899262"></a><a name="p9899262"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row160364312614"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p121852010133419"><a name="p121852010133419"></a><a name="p121852010133419"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1216718143517"><a name="p1216718143517"></a><a name="p1216718143517"></a>Network ID this port belongs to.</p>
<p id="p63642768"><a name="p63642768"></a><a name="p63642768"></a>String value expected.</p>
<p id="p35914007"><a name="p35914007"></a><a name="p35914007"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row11603114311264"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p10185510103418"><a name="p10185510103418"></a><a name="p10185510103418"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p23353418"><a name="p23353418"></a><a name="p23353418"></a>Security group IDs to associate with this port.</p>
<p id="p8854178"><a name="p8854178"></a><a name="p8854178"></a>List value expected.</p>
<p id="p12578743"><a name="p12578743"></a><a name="p12578743"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1160417439261"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p111858109346"><a name="p111858109346"></a><a name="p111858109346"></a>value_specs</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p12245252"><a name="p12245252"></a><a name="p12245252"></a>Extra parameters to include in the request.</p>
<p id="p43098406"><a name="p43098406"></a><a name="p43098406"></a>Map value expected.</p>
<p id="p52341337"><a name="p52341337"></a><a name="p52341337"></a>Can be updated without replacement.</p>
<p id="p1309991"><a name="p1309991"></a><a name="p1309991"></a>Defaults to "{}".</p>
</td>
</tr>
<tr id="row17604643132617"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p12185910113414"><a name="p12185910113414"></a><a name="p12185910113414"></a>replacement_policy</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p39000412"><a name="p39000412"></a><a name="p39000412"></a>Policy on how to respond to a stack-update for this resource. REPLACE_ALWAYS will replace the port regardless of any property changes. AUTO will update the existing port for any changed update-allowed property.</p>
<p id="p15459389"><a name="p15459389"></a><a name="p15459389"></a>String value expected.</p>
<p id="p4916781"><a name="p4916781"></a><a name="p4916781"></a>Can be updated without replacement.</p>
<p id="p44251036"><a name="p44251036"></a><a name="p44251036"></a>Defaults to "AUTO".</p>
<p id="p62715012"><a name="p62715012"></a><a name="p62715012"></a>Allowed values: AUTO, REPLACE_ALWAYS</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section4696125573212"></a>

<a name="table63301238123910"></a>
<table><thead align="left"><tr id="row166551257143320"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p43314385391"><a name="p43314385391"></a><a name="p43314385391"></a><strong id="b691914133415"><a name="b691914133415"></a><a name="b691914133415"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p203311738143914"><a name="p203311738143914"></a><a name="p203311738143914"></a><strong id="b49417141346"><a name="b49417141346"></a><a name="b49417141346"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row865519574337"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p03311738143917"><a name="p03311738143917"></a><a name="p03311738143917"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1033173813395"><a name="p1033173813395"></a><a name="p1033173813395"></a>The administrative state of this port.</p>
</td>
</tr>
<tr id="row665565718334"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p733112389399"><a name="p733112389399"></a><a name="p733112389399"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p13311738163915"><a name="p13311738163915"></a><a name="p13311738163915"></a>Additional MAC/IP address pairs allowed to pass through a port.</p>
</td>
</tr>
<tr id="row2655357173318"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p10331138163920"><a name="p10331138163920"></a><a name="p10331138163920"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1331143812390"><a name="p1331143812390"></a><a name="p1331143812390"></a>Unique identifier for the device.</p>
</td>
</tr>
<tr id="row13655155773320"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p113317383394"><a name="p113317383394"></a><a name="p113317383394"></a>device_owner</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1133163812394"><a name="p1133163812394"></a><a name="p1133163812394"></a>Name of the network owning the port.</p>
</td>
</tr>
<tr id="row196551576337"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p19331103853916"><a name="p19331103853916"></a><a name="p19331103853916"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p103311938193910"><a name="p103311938193910"></a><a name="p103311938193910"></a>Fixed IP addresses.</p>
</td>
</tr>
<tr id="row965595718334"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p16331163813916"><a name="p16331163813916"></a><a name="p16331163813916"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p733183812392"><a name="p733183812392"></a><a name="p733183812392"></a>MAC address of the port.</p>
</td>
</tr>
<tr id="row26551757183319"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p113316382394"><a name="p113316382394"></a><a name="p113316382394"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p16331173814394"><a name="p16331173814394"></a><a name="p16331173814394"></a>Friendly name of the port.</p>
</td>
</tr>
<tr id="row1865515719336"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1333133812394"><a name="p1333133812394"></a><a name="p1333133812394"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p123319388393"><a name="p123319388393"></a><a name="p123319388393"></a>Unique identifier for the network owning the port.</p>
</td>
</tr>
<tr id="row1365512579335"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p163314380395"><a name="p163314380395"></a><a name="p163314380395"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1833173816391"><a name="p1833173816391"></a><a name="p1833173816391"></a>A list of security groups for the port.</p>
</td>
</tr>
<tr id="row1265555793317"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p2331123813911"><a name="p2331123813911"></a><a name="p2331123813911"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p2331183815398"><a name="p2331183815398"></a><a name="p2331183815398"></a>Detailed information about resource.</p>
</td>
</tr>
<tr id="row1065512574339"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p15331183803916"><a name="p15331183803916"></a><a name="p15331183803916"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p233119380395"><a name="p233119380395"></a><a name="p233119380395"></a>The status of the port.</p>
</td>
</tr>
<tr id="row146555573332"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p14331238183911"><a name="p14331238183911"></a><a name="p14331238183911"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1233173853918"><a name="p1233173853918"></a><a name="p1233173853918"></a>A list of all subnet attributes for the port.</p>
</td>
</tr>
<tr id="row665525714333"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p18331193818390"><a name="p18331193818390"></a><a name="p18331193818390"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p4331123816396"><a name="p4331123816396"></a><a name="p4331123816396"></a>Tenant owning the port.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section116810616332"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::Port
    properties:
      admin_state_up: Boolean
      allowed_address_pairs: [{"mac_address": String, "ip_address": String}, {"mac_address": String, "ip_address": String}, ...]
      device_id: String
      device_owner: String
      fixed_ips: [{"subnet_id": String, "ip_address": String, "subnet": String}, {"subnet_id": String, "ip_address": String, "subnet": String}, ...]
      mac_address: String
      name: String
      network: String
      network_id: String
      security_groups: [Value, Value, ...]
      value_specs: {...}
      replacement_policy: String
```

