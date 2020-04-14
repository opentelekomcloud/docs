# OS::Neutron::LBaaS::PoolMember<a name="EN-US_TOPIC_0088407163"></a>

A resource for managing LBaaS v2 Pool Members.

A pool member represents a single backend node.

## Required Properties<a name="section03651213153317"></a>

<a name="table166061443133415"></a>
<table><thead align="left"><tr id="row964719396425"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p15606174310343"><a name="p15606174310343"></a><a name="p15606174310343"></a><strong id="b6201122424114"><a name="b6201122424114"></a><a name="b6201122424114"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p1560654313344"><a name="p1560654313344"></a><a name="p1560654313344"></a><strong id="b1202192414413"><a name="b1202192414413"></a><a name="b1202192414413"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1964711397425"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p7606343203419"><a name="p7606343203419"></a><a name="p7606343203419"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p38878096"><a name="p38878096"></a><a name="p38878096"></a>IP address of the pool member on the pool network.</p>
<p id="p14358552"><a name="p14358552"></a><a name="p14358552"></a>String value expected.</p>
<p id="p62118104"><a name="p62118104"></a><a name="p62118104"></a>Updates cause replacement.</p>
<p id="p22192026"><a name="p22192026"></a><a name="p22192026"></a>Value must be of type ip_addr</p>
</td>
</tr>
<tr id="row56473391421"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p76061443133411"><a name="p76061443133411"></a><a name="p76061443133411"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p52723697"><a name="p52723697"></a><a name="p52723697"></a>Name or ID of the load balancing pool.</p>
<p id="p4751232"><a name="p4751232"></a><a name="p4751232"></a>String value expected.</p>
<p id="p42761093"><a name="p42761093"></a><a name="p42761093"></a>Updates cause replacement.</p>
<p id="p49305521"><a name="p49305521"></a><a name="p49305521"></a>Value must be of type neutron.lbaas.pool</p>
</td>
</tr>
<tr id="row16473392427"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p16063439344"><a name="p16063439344"></a><a name="p16063439344"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p34324266"><a name="p34324266"></a><a name="p34324266"></a>Port on which the pool member listens for requests or connections.</p>
<p id="p40482946"><a name="p40482946"></a><a name="p40482946"></a>Integer value expected.</p>
<p id="p28802196"><a name="p28802196"></a><a name="p28802196"></a>Updates cause replacement.</p>
<p id="p57893179"><a name="p57893179"></a><a name="p57893179"></a>The value must be in the range 1 to 65535, include 1 and 65535.</p>
</td>
</tr>
<tr id="row16647139104210"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1860634323411"><a name="p1860634323411"></a><a name="p1860634323411"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p58835921"><a name="p58835921"></a><a name="p58835921"></a>Subnet name or ID of this member.</p>
<p id="p59761242"><a name="p59761242"></a><a name="p59761242"></a>String value expected.</p>
<p id="p980267"><a name="p980267"></a><a name="p980267"></a>Updates cause replacement.</p>
<p id="p8822405"><a name="p8822405"></a><a name="p8822405"></a>Value must be of type neutron.subnet</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section328442319338"></a>

<a name="table5627184183616"></a>
<table><thead align="left"><tr id="row1273616258506"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p96281543366"><a name="p96281543366"></a><a name="p96281543366"></a><strong id="b273610253504"><a name="b273610253504"></a><a name="b273610253504"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p1162918412364"><a name="p1162918412364"></a><a name="p1162918412364"></a><strong id="b13737122585019"><a name="b13737122585019"></a><a name="b13737122585019"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1373722515015"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p5630154203616"><a name="p5630154203616"></a><a name="p5630154203616"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p37523045"><a name="p37523045"></a><a name="p37523045"></a>The administrative state of the pool member.</p>
<p id="p2163093"><a name="p2163093"></a><a name="p2163093"></a>Boolean value expected.</p>
<p id="p19467837"><a name="p19467837"></a><a name="p19467837"></a>Updates are not supported.</p>
<p id="p40992807"><a name="p40992807"></a><a name="p40992807"></a>Allowed values: True</p>
</td>
</tr>
<tr id="row1473952512507"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1118019338365"><a name="p1118019338365"></a><a name="p1118019338365"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p32083086"><a name="p32083086"></a><a name="p32083086"></a>Weight of pool member in the pool (default to 1).</p>
<p id="p20312325"><a name="p20312325"></a><a name="p20312325"></a>Integer value expected.</p>
<p id="p48593202"><a name="p48593202"></a><a name="p48593202"></a>Can be updated without replacement.</p>
<p id="p34685638"><a name="p34685638"></a><a name="p34685638"></a>Defaults to "1".</p>
<p id="p43735290"><a name="p43735290"></a><a name="p43735290"></a>The value must be in the range 0 to 256, include 0 and 256.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section9427153020337"></a>

<a name="table798095683619"></a>
<table><thead align="left"><tr id="row10800019105119"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p2983756123616"><a name="p2983756123616"></a><a name="p2983756123616"></a><strong id="b480171935115"><a name="b480171935115"></a><a name="b480171935115"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p49841456103610"><a name="p49841456103610"></a><a name="p49841456103610"></a><strong id="b28021819145112"><a name="b28021819145112"></a><a name="b28021819145112"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12803181916513"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p89851256133611"><a name="p89851256133611"></a><a name="p89851256133611"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p139891456203618"><a name="p139891456203618"></a><a name="p139891456203618"></a>The IP address of the pool member.</p>
</td>
</tr>
<tr id="row20806121916511"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p16990956113616"><a name="p16990956113616"></a><a name="p16990956113616"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p109921656133612"><a name="p109921656133612"></a><a name="p109921656133612"></a>The ID of the pool to which the pool member belongs.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section9211938133310"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::LBaaS::PoolMember
    properties:
      address: String
      admin_state_up: Boolean
      pool: String
      protocol_port: Integer
      subnet: String
      weight: Integer
```

