# OS::Neutron::FloatingIPAssociation<a name="EN-US_TOPIC_0088407217"></a>

A resource for associating floating IP addresses and ports.

This resource allows associating a floating IP to a port with at least one IP address to associate with this floating IP.

## Required Properties<a name="section191574062312"></a>

<a name="table185461036171010"></a>
<table><thead align="left"><tr id="row13644105914342"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p116211135123211"><a name="p116211135123211"></a><a name="p116211135123211"></a><strong id="b762293516324"><a name="b762293516324"></a><a name="b762293516324"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p146221435163216"><a name="p146221435163216"></a><a name="p146221435163216"></a><strong id="b162316356327"><a name="b162316356327"></a><a name="b162316356327"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row106447594347"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p186441959113417"><a name="p186441959113417"></a><a name="p186441959113417"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p43973663"><a name="p43973663"></a><a name="p43973663"></a>ID of the floating IP to associate.</p>
<p id="p60218649"><a name="p60218649"></a><a name="p60218649"></a>String value expected.</p>
<p id="p5096933"><a name="p5096933"></a><a name="p5096933"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row964405913343"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p18644125923417"><a name="p18644125923417"></a><a name="p18644125923417"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p10198465"><a name="p10198465"></a><a name="p10198465"></a>ID of an existing port with at least one IP address to associate with this floating IP. The port must be associated to a Nova instance.</p>
<p id="p24677321"><a name="p24677321"></a><a name="p24677321"></a>String value expected.</p>
<p id="p20769304"><a name="p20769304"></a><a name="p20769304"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section186445714237"></a>

<a name="table19846577247"></a>
<table><thead align="left"><tr id="row141711616163618"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p101721016163611"><a name="p101721016163611"></a><a name="p101721016163611"></a><strong id="b191729168363"><a name="b191729168363"></a><a name="b191729168363"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p161722016163620"><a name="p161722016163620"></a><a name="p161722016163620"></a><strong id="b117231614367"><a name="b117231614367"></a><a name="b117231614367"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12172316143617"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1017321613610"><a name="p1017321613610"></a><a name="p1017321613610"></a>fixed_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p55840624"><a name="p55840624"></a><a name="p55840624"></a>IP address to use if the port has multiple addresses.</p>
<p id="p32803570"><a name="p32803570"></a><a name="p32803570"></a>String value expected.</p>
<p id="p26796681"><a name="p26796681"></a><a name="p26796681"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section193501122182312"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::FloatingIPAssociation
    properties:
      fixed_ip_address: String
      floatingip_id: String
      port_id: String
```

