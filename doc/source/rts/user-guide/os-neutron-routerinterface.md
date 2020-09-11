# OS::Neutron::RouterInterface<a name="EN-US_TOPIC_0088407174"></a>

A resource for managing Neutron router interfaces.

Router interfaces associate routers with existing subnets or ports.

## Required Properties<a name="section1019481495112"></a>

<a name="table17759134613511"></a>
<table><thead align="left"><tr id="row1393817824614"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p197608465516"><a name="p197608465516"></a><a name="p197608465516"></a><strong id="b328104754418"><a name="b328104754418"></a><a name="b328104754418"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p9760124615517"><a name="p9760124615517"></a><a name="p9760124615517"></a><strong id="b429347154415"><a name="b429347154415"></a><a name="b429347154415"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row169385844612"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1376074615513"><a name="p1376074615513"></a><a name="p1376074615513"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p26122443"><a name="p26122443"></a><a name="p26122443"></a>The router id.</p>
<p id="p33775403"><a name="p33775403"></a><a name="p33775403"></a>String value expected.</p>
<p id="p35543172"><a name="p35543172"></a><a name="p35543172"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section16581322145114"></a>

<a name="table8912161745214"></a>
<table><thead align="left"><tr id="row529118114717"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p09132175523"><a name="p09132175523"></a><a name="p09132175523"></a><strong id="b99841417184712"><a name="b99841417184712"></a><a name="b99841417184712"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1091361775214"><a name="p1091361775214"></a><a name="p1091361775214"></a><strong id="b14985111715471"><a name="b14985111715471"></a><a name="b14985111715471"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row929118834719"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p18914217155217"><a name="p18914217155217"></a><a name="p18914217155217"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p51511698"><a name="p51511698"></a><a name="p51511698"></a>The port id, either subnet or port_id should be specified.</p>
<p id="p60952106"><a name="p60952106"></a><a name="p60952106"></a>String value expected.</p>
<p id="p11698044"><a name="p11698044"></a><a name="p11698044"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row12916814718"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p22557349539"><a name="p22557349539"></a><a name="p22557349539"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p8017535"><a name="p8017535"></a><a name="p8017535"></a>The subnet, either subnet or port should be specified.</p>
<p id="p5048953"><a name="p5048953"></a><a name="p5048953"></a>String value expected.</p>
<p id="p45440578"><a name="p45440578"></a><a name="p45440578"></a>Updates cause replacement.</p>
<p id="p6312019"><a name="p6312019"></a><a name="p6312019"></a>Value must be of type neutron.subnet</p>
</td>
</tr>
<tr id="row52913815472"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p18213133885314"><a name="p18213133885314"></a><a name="p18213133885314"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p151033914404"><a name="p151033914404"></a><a name="p151033914404"></a>String value expected.</p>
<p id="p41511513"><a name="p41511513"></a><a name="p41511513"></a>Updates cause replacement.</p>
<div class="note" id="note19125754918"><a name="note19125754918"></a><a name="note19125754918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p38059305"><a name="p38059305"></a><a name="p38059305"></a>In the template,</p>
<a name="ul869217122213"></a><a name="ul869217122213"></a><ul id="ul869217122213"><li><strong id="b118521819172317"><a name="b118521819172317"></a><a name="b118521819172317"></a>subnet</strong> and <strong id="b28521719182320"><a name="b28521719182320"></a><a name="b28521719182320"></a>subnet_id</strong> cannot appear at the same time, otherwise the stack will fail to create.</li><li><p id="p15930161372217"><a name="p15930161372217"></a><a name="p15930161372217"></a>At least one of the following properties must be specified: <strong id="b1584443202415"><a name="b1584443202415"></a><a name="b1584443202415"></a>port_id</strong>, <strong id="b17821114142719"><a name="b17821114142719"></a><a name="b17821114142719"></a>subnet </strong>(or<strong id="b9646193312712"><a name="b9646193312712"></a><a name="b9646193312712"></a> subnet_id</strong>).</p>
</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section47201758135416"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::RouterInterface
    properties:
      port_id: String
      router_id: String
      subnet: String
      subnet_id: String
```

