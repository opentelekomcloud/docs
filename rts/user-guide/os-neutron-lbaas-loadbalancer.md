# OS::Neutron::LBaaS::LoadBalancer<a name="EN-US_TOPIC_0088407220"></a>

A resource for creating LBaaS v2 Load Balancers.

This resource creates and manages Neutron LBaaS v2 Load Balancers, which allows traffic to be directed between servers.

## Required Properties<a name="section14427159192414"></a>

<a name="table1525134215243"></a>
<table><thead align="left"><tr id="row155976334208"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p0252742112415"><a name="p0252742112415"></a><a name="p0252742112415"></a><strong id="b166987316176"><a name="b166987316176"></a><a name="b166987316176"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p172527426241"><a name="p172527426241"></a><a name="p172527426241"></a><strong id="b9699031181713"><a name="b9699031181713"></a><a name="b9699031181713"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10597133362015"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1125294219249"><a name="p1125294219249"></a><a name="p1125294219249"></a>vip_subnet</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p54339566"><a name="p54339566"></a><a name="p54339566"></a>The name or ID of the subnet on which to allocate the VIP address.</p>
<p id="p19294047"><a name="p19294047"></a><a name="p19294047"></a>String value expected.</p>
<p id="p39428702"><a name="p39428702"></a><a name="p39428702"></a>Updates cause replacement.</p>
<p id="p19314003"><a name="p19314003"></a><a name="p19314003"></a>Value must be of type neutron.subnet</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section6806101602410"></a>

<a name="table7839152712517"></a>
<table><thead align="left"><tr id="row5547144162118"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p58399271251"><a name="p58399271251"></a><a name="p58399271251"></a><strong id="b133346532213"><a name="b133346532213"></a><a name="b133346532213"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p6839727162514"><a name="p6839727162514"></a><a name="p6839727162514"></a><strong id="b1333565322119"><a name="b1333565322119"></a><a name="b1333565322119"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row654704418212"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p158393276257"><a name="p158393276257"></a><a name="p158393276257"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44723749"><a name="p44723749"></a><a name="p44723749"></a>The administrative state of this Load Balancer.</p>
<p id="p66969424"><a name="p66969424"></a><a name="p66969424"></a>Boolean value expected.</p>
<p id="p65853910"><a name="p65853910"></a><a name="p65853910"></a>Updates are not supported.</p>
<p id="p55814278"><a name="p55814278"></a><a name="p55814278"></a>Allowed values: True</p>
</td>
</tr>
<tr id="row11547174411219"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p183911279254"><a name="p183911279254"></a><a name="p183911279254"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p24662676"><a name="p24662676"></a><a name="p24662676"></a>Description of this Load Balancer.</p>
<p id="p20637500"><a name="p20637500"></a><a name="p20637500"></a>String value expected.</p>
<p id="p51519779"><a name="p51519779"></a><a name="p51519779"></a>Can be updated without replacement.</p>
<p id="p61024835"><a name="p61024835"></a><a name="p61024835"></a>Defaults to " ".</p>
</td>
</tr>
<tr id="row4547344122111"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1283922782518"><a name="p1283922782518"></a><a name="p1283922782518"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44064565"><a name="p44064565"></a><a name="p44064565"></a>Name of this Load Balancer.</p>
<p id="p61036771"><a name="p61036771"></a><a name="p61036771"></a>String value expected.</p>
<p id="p12460028"><a name="p12460028"></a><a name="p12460028"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row254714482111"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p983912273251"><a name="p983912273251"></a><a name="p983912273251"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p2629376"><a name="p2629376"></a><a name="p2629376"></a>Provider for this Load Balancer.</p>
<p id="p23664388"><a name="p23664388"></a><a name="p23664388"></a>String value expected.</p>
<p id="p11652904"><a name="p11652904"></a><a name="p11652904"></a>Updates are not supported.</p>
<p id="p37767277"><a name="p37767277"></a><a name="p37767277"></a>Allowed values: vlb</p>
</td>
</tr>
<tr id="row1154744482113"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1684012772511"><a name="p1684012772511"></a><a name="p1684012772511"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p39250631"><a name="p39250631"></a><a name="p39250631"></a>The ID of the tenant who owns the Load Balancer. Only administrative users can specify a tenant ID other than their own.</p>
<p id="p17711366"><a name="p17711366"></a><a name="p17711366"></a>String value expected.</p>
<p id="p25184570"><a name="p25184570"></a><a name="p25184570"></a>Updates cause replacement.</p>
<p id="p25334540"><a name="p25334540"></a><a name="p25334540"></a>Value must be of type keystone.project</p>
</td>
</tr>
<tr id="row1954714462111"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p158401727142512"><a name="p158401727142512"></a><a name="p158401727142512"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p38831830"><a name="p38831830"></a><a name="p38831830"></a>IP address for the VIP.</p>
<p id="p13942152"><a name="p13942152"></a><a name="p13942152"></a>String value expected.</p>
<p id="p58370508"><a name="p58370508"></a><a name="p58370508"></a>Updates cause replacement.</p>
<p id="p55572532"><a name="p55572532"></a><a name="p55572532"></a>Value must be of type ip_addr</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section20802122332412"></a>

<a name="table1812813918277"></a>
<table><thead align="left"><tr id="row20902137102310"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p41291915273"><a name="p41291915273"></a><a name="p41291915273"></a><strong id="b11716651112313"><a name="b11716651112313"></a><a name="b11716651112313"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p17129179162715"><a name="p17129179162715"></a><a name="p17129179162715"></a><strong id="b1717145132313"><a name="b1717145132313"></a><a name="b1717145132313"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row790233719238"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p161296912274"><a name="p161296912274"></a><a name="p161296912274"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p1312999102717"><a name="p1312999102717"></a><a name="p1312999102717"></a>The VIP address of the LoadBalancer.</p>
</td>
</tr>
<tr id="row189026376234"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p212914915272"><a name="p212914915272"></a><a name="p212914915272"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p912919917271"><a name="p912919917271"></a><a name="p912919917271"></a>The VIP port of the LoadBalancer.</p>
</td>
</tr>
<tr id="row9902123742310"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p11129169132716"><a name="p11129169132716"></a><a name="p11129169132716"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p1112918962712"><a name="p1112918962712"></a><a name="p1112918962712"></a>The VIP subnet of the LoadBalancer.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section672643102413"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::LBaaS::LoadBalancer
    properties:
      admin_state_up: Boolean
      description: String
      name: String
      provider: String
      tenant_id: String
      vip_address: String
      vip_subnet: String
```

