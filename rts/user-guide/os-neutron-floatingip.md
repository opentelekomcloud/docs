# OS::Neutron::FloatingIP<a name="EN-US_TOPIC_0088407176"></a>

A resource for managing Neutron floating IP addresses.

Floating IP addresses can change their association between routers by action of the user. One of the most common use cases for floating IP addresses is to provide public IP addresses to a private cloud, where there are a limited number of IP addresses available. Another is for a cloud system user to have a "static" IP address that can be reassigned when an instance is upgraded or moved.

## Optional Properties<a name="section13574115131710"></a>

<a name="table185461036171010"></a>
<table><thead align="left"><tr id="row1998243853013"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p354718362102"><a name="p354718362102"></a><a name="p354718362102"></a><strong id="b16143824274"><a name="b16143824274"></a><a name="b16143824274"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p13547183614105"><a name="p13547183614105"></a><a name="p13547183614105"></a><strong id="b1014418210273"><a name="b1014418210273"></a><a name="b1014418210273"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row598313381301"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p3547163611017"><a name="p3547163611017"></a><a name="p3547163611017"></a>floating_network</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1733784"><a name="p1733784"></a><a name="p1733784"></a>Network to allocate floating IP from.</p>
<p id="p15604063"><a name="p15604063"></a><a name="p15604063"></a>String value expected.</p>
<p id="p6218840"><a name="p6218840"></a><a name="p6218840"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1498353818306"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1654715368103"><a name="p1654715368103"></a><a name="p1654715368103"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p33964049"><a name="p33964049"></a><a name="p33964049"></a>IP address to use if the port has multiple addresses.</p>
<p id="p37240986"><a name="p37240986"></a><a name="p37240986"></a>String value expected.</p>
<p id="p66733418"><a name="p66733418"></a><a name="p66733418"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1898343817307"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p10378851101511"><a name="p10378851101511"></a><a name="p10378851101511"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p36697739"><a name="p36697739"></a><a name="p36697739"></a>ID of an existing port with at least one IP address to associate with this floating IP. The port must be associated to a Nova instance.</p>
<p id="p61844198"><a name="p61844198"></a><a name="p61844198"></a>String value expected.</p>
<p id="p19726877"><a name="p19726877"></a><a name="p19726877"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row199831384304"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p15812129101911"><a name="p15812129101911"></a><a name="p15812129101911"></a>value_specs</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p54373191"><a name="p54373191"></a><a name="p54373191"></a>Extra parameters to include in the "floatingip" object in the creation request. Parameters are often specific to installed hardware or extensions.</p>
<p id="p42152370"><a name="p42152370"></a><a name="p42152370"></a>Map value expected.</p>
<p id="p43827015"><a name="p43827015"></a><a name="p43827015"></a>Updates cause replacement.</p>
<p id="p58898822"><a name="p58898822"></a><a name="p58898822"></a>Defaults to "{}".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section96241723121719"></a>

<a name="table13695203012207"></a>
<table><thead align="left"><tr id="row5996523113220"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p186951130122010"><a name="p186951130122010"></a><a name="p186951130122010"></a><strong id="b762293516324"><a name="b762293516324"></a><a name="b762293516324"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p146956304201"><a name="p146956304201"></a><a name="p146956304201"></a><strong id="b162316356327"><a name="b162316356327"></a><a name="b162316356327"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59967231321"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p11695153042012"><a name="p11695153042012"></a><a name="p11695153042012"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p15695430122010"><a name="p15695430122010"></a><a name="p15695430122010"></a>IP address of the associated port, if specified.</p>
</td>
</tr>
<tr id="row1599652333216"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p176951430172019"><a name="p176951430172019"></a><a name="p176951430172019"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p3695173032019"><a name="p3695173032019"></a><a name="p3695173032019"></a>The allocated address of this IP.</p>
</td>
</tr>
<tr id="row139965237328"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p10695183018201"><a name="p10695183018201"></a><a name="p10695183018201"></a>floating_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p51678591"><a name="p51678591"></a><a name="p51678591"></a>ID of the network in which this IP is allocated.</p>
<p id="p111272332537"><a name="p111272332537"></a><a name="p111272332537"></a>The network ID used during floating IP address assignment is a fixed external network ID. You can use <strong id="b5365390813958"><a name="b5365390813958"></a><a name="b5365390813958"></a>GET /v2.0/networks?router:external=True</strong>&nbsp;or&nbsp;<strong id="b5099926813958"><a name="b5099926813958"></a><a name="b5099926813958"></a>neutron net-external-list</strong> to obtain the external network information.</p>
</td>
</tr>
<tr id="row19962238329"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p26951130152014"><a name="p26951130152014"></a><a name="p26951130152014"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p2069533014206"><a name="p2069533014206"></a><a name="p2069533014206"></a>ID of the port associated with this IP.</p>
</td>
</tr>
<tr id="row6996102373210"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1069510309207"><a name="p1069510309207"></a><a name="p1069510309207"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p17695130202014"><a name="p17695130202014"></a><a name="p17695130202014"></a>ID of the router used as gateway, set when associated with a port.</p>
</td>
</tr>
<tr id="row139961123163212"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p19695153011205"><a name="p19695153011205"></a><a name="p19695153011205"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p4695183022016"><a name="p4695183022016"></a><a name="p4695183022016"></a>Detailed information about resource.</p>
</td>
</tr>
<tr id="row179961823183219"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p19695153082010"><a name="p19695153082010"></a><a name="p19695153082010"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p369510304201"><a name="p369510304201"></a><a name="p369510304201"></a>The tenant owning this floating IP.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section1470743281718"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::FloatingIP
    properties:
      fixed_ip_address: String
      floating_ip_address: String
      floating_network: String
      port_id: String
      value_specs: {...}
```

