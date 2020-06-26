# OSE::VPC::Vpc<a name="EN-US_TOPIC_0103361351"></a>

A resource for managing Virtual Private Cloud \(VPC\) resources

A VPC can be used to build an isolated, user-configured, and managed virtual network environment for your ECSs.

## Required Properties<a name="section1157821131616"></a>

<a name="table106482028111611"></a>
<table><thead align="left"><tr id="row7648728181616"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p643749201717"><a name="p643749201717"></a><a name="p643749201717"></a><strong id="b1926175111326"><a name="b1926175111326"></a><a name="b1926175111326"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p164371961711"><a name="p164371961711"></a><a name="p164371961711"></a><strong id="b17927135119323"><a name="b17927135119323"></a><a name="b17927135119323"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1764820288166"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p91549462166"><a name="p91549462166"></a><a name="p91549462166"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p1895514508169"><a name="p1895514508169"></a><a name="p1895514508169"></a>Name of a VPC</p>
<p id="p29551950141612"><a name="p29551950141612"></a><a name="p29551950141612"></a>String value expected.</p>
<p id="p209552505160"><a name="p209552505160"></a><a name="p209552505160"></a>Can be updated without replacement.</p>
<p id="p39556507164"><a name="p39556507164"></a><a name="p39556507164"></a>Value range: The value is a string of 1 to 64 characters, including digits, letters, underscores (_), and hyphens (-).</p>
<div class="note" id="note13301168177"><a name="note13301168177"></a><a name="note13301168177"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p73016617179"><a name="p73016617179"></a><a name="p73016617179"></a>If the name is not empty, the name of a tenant must be unique.</p>
</div></div>
</td>
</tr>
<tr id="row56488283165"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1915464610167"><a name="p1915464610167"></a><a name="p1915464610167"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p178541523101811"><a name="p178541523101811"></a><a name="p178541523101811"></a>Range of available subnets in a VPC</p>
<p id="p14854723131816"><a name="p14854723131816"></a><a name="p14854723131816"></a>String value expected.</p>
<p id="p385432317188"><a name="p385432317188"></a><a name="p385432317188"></a>Can be updated without replacement.</p>
<p id="p19842919111520"><a name="p19842919111520"></a><a name="p19842919111520"></a>The value can be updated without replacing the template.</p>
<p id="p284211915158"><a name="p284211915158"></a><a name="p284211915158"></a>Value range: 10.0.0.0/8 to 10.255.255.0/24, 172.16.0.0/12 to 172.31.255.0/24, or 192.168.0.0/16 to 192.168.255.0/24. The value must be in the CIDR format. For example: 192.168.0.0/16.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1798419593199"></a>

<a name="table114781711102020"></a>
<table><thead align="left"><tr id="row16478011102013"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p51021342912"><a name="p51021342912"></a><a name="p51021342912"></a><strong id="b1543519561323"><a name="b1543519561323"></a><a name="b1543519561323"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p151033416911"><a name="p151033416911"></a><a name="p151033416911"></a><strong id="b7437155614325"><a name="b7437155614325"></a><a name="b7437155614325"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1647821132010"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1533983282011"><a name="p1533983282011"></a><a name="p1533983282011"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1833916322200"><a name="p1833916322200"></a><a name="p1833916322200"></a>Name of a VPC</p>
</td>
</tr>
<tr id="row547881132012"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p113391132122019"><a name="p113391132122019"></a><a name="p113391132122019"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p2033917324209"><a name="p2033917324209"></a><a name="p2033917324209"></a>Range of available subnets in a VPC</p>
</td>
</tr>
<tr id="row14781911152012"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p4339732152016"><a name="p4339732152016"></a><a name="p4339732152016"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p163391032102018"><a name="p163391032102018"></a><a name="p163391032102018"></a>Status of a VPC</p>
</td>
</tr>
<tr id="row1647881110205"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p9339203272020"><a name="p9339203272020"></a><a name="p9339203272020"></a>neutron_router_id</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p733973217208"><a name="p733973217208"></a><a name="p733973217208"></a>UUID of a router</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section14309164762018"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::VPC::Vpc
    properties:
      name: String
      cidr: String
```

