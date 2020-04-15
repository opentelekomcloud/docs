# OS::Nova::ServerGroup<a name="EN-US_TOPIC_0088407079"></a>

A resource for managing a Nova server group.

Server groups allow you to make sure instances are on the same hypervisor host or on a different one.

## Optional Properties<a name="section8131023165714"></a>

<a name="table1873317541955"></a>
<table><thead align="left"><tr id="row615615415290"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p13734554251"><a name="p13734554251"></a><a name="p13734554251"></a><strong id="b41626692614"><a name="b41626692614"></a><a name="b41626692614"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p37342541351"><a name="p37342541351"></a><a name="p37342541351"></a><strong id="b18163263268"><a name="b18163263268"></a><a name="b18163263268"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row181565442912"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p7734854654"><a name="p7734854654"></a><a name="p7734854654"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p29857914"><a name="p29857914"></a><a name="p29857914"></a>Server Group name.</p>
<p id="p285771"><a name="p285771"></a><a name="p285771"></a>String value expected.</p>
<p id="p2571942"><a name="p2571942"></a><a name="p2571942"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row11561747293"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1773415549513"><a name="p1773415549513"></a><a name="p1773415549513"></a>policies</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p7000775"><a name="p7000775"></a><a name="p7000775"></a>A list of string policies to apply. Defaults to anti-affinity.</p>
<p id="p63006983"><a name="p63006983"></a><a name="p63006983"></a>List value expected.</p>
<p id="p30191941"><a name="p30191941"></a><a name="p30191941"></a>Updates cause replacement.</p>
<p id="p3292018"><a name="p3292018"></a><a name="p3292018"></a>Defaults to "['anti-affinity']".</p>
<p id="p29628167"><a name="p29628167"></a><a name="p29628167"></a>Allowed values: anti-affinity, affinity</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section284203005717"></a>

<a name="table13712104512612"></a>
<table><thead align="left"><tr id="row105813515308"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p19713134514618"><a name="p19713134514618"></a><a name="p19713134514618"></a><strong id="b1158213583014"><a name="b1158213583014"></a><a name="b1158213583014"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p1671419452614"><a name="p1671419452614"></a><a name="p1671419452614"></a><strong id="b25821557307"><a name="b25821557307"></a><a name="b25821557307"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row185826543019"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p971512451611"><a name="p971512451611"></a><a name="p971512451611"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p14716845765"><a name="p14716845765"></a><a name="p14716845765"></a>Detailed information about resource.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section15739938125719"></a>

```
heat_template_version: 2015-04-30
...
resources:
  ...
  the_resource:
    type: OS::Nova::ServerGroup
    properties:
      name: String
      policies: [String, String, ...]
```

