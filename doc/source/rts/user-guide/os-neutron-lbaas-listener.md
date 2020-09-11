# OS::Neutron::LBaaS::Listener<a name="EN-US_TOPIC_0088407158"></a>

A resource for managing LBaaS v2 Listeners.

This resource creates and manages Neutron LBaaS v2 Listeners, which represent a listening endpoint for the vip.

## Required Properties<a name="section2061419115183"></a>

<a name="table12498112013"></a>
<table><thead align="left"><tr id="row14471811149"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p4468132010"><a name="p4468132010"></a><a name="p4468132010"></a><strong id="b322115114124"><a name="b322115114124"></a><a name="b322115114124"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p84782205"><a name="p84782205"></a><a name="p84782205"></a><strong id="b5222135120127"><a name="b5222135120127"></a><a name="b5222135120127"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row747181141416"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1144820207"><a name="p1144820207"></a><a name="p1144820207"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p23878979"><a name="p23878979"></a><a name="p23878979"></a>ID or name of the load balancer with which listener is associated.</p>
<p id="p13584221"><a name="p13584221"></a><a name="p13584221"></a>String value expected.</p>
<p id="p55149127"><a name="p55149127"></a><a name="p55149127"></a>Updates cause replacement.</p>
<p id="p26580098"><a name="p26580098"></a><a name="p26580098"></a>Value must be of type neutron.lbaas.loadbalancer</p>
</td>
</tr>
<tr id="row4470119143"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p543812017"><a name="p543812017"></a><a name="p543812017"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p5504344"><a name="p5504344"></a><a name="p5504344"></a>Protocol on which to listen for the client traffic. It must be the same as the value of OS::Neutron::LBaaS::Pool's protocol.</p>
<p id="p49539101"><a name="p49539101"></a><a name="p49539101"></a>String value expected.</p>
<p id="p43198726"><a name="p43198726"></a><a name="p43198726"></a>Updates cause replacement.</p>
<p id="p53244222"><a name="p53244222"></a><a name="p53244222"></a>Allowed values: TCP, HTTP</p>
</td>
</tr>
<tr id="row347016149"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p145108122014"><a name="p145108122014"></a><a name="p145108122014"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p17814757"><a name="p17814757"></a><a name="p17814757"></a>TCP or UDP port on which to listen for client traffic.</p>
<p id="p26115085"><a name="p26115085"></a><a name="p26115085"></a>Integer value expected.</p>
<p id="p33709175"><a name="p33709175"></a><a name="p33709175"></a>Updates cause replacement.</p>
<p id="p34947125"><a name="p34947125"></a><a name="p34947125"></a>The value must be in the range 1 to 65535, include 1 and 65535.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section122342011131819"></a>

<a name="table1342582282117"></a>
<table><thead align="left"><tr id="row9303142261513"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p15425132220217"><a name="p15425132220217"></a><a name="p15425132220217"></a><strong id="b2559134315151"><a name="b2559134315151"></a><a name="b2559134315151"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p4425722102113"><a name="p4425722102113"></a><a name="p4425722102113"></a><strong id="b95591043171515"><a name="b95591043171515"></a><a name="b95591043171515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4303172251512"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1242642211216"><a name="p1242642211216"></a><a name="p1242642211216"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p12713024"><a name="p12713024"></a><a name="p12713024"></a>The administrative state of this listener.</p>
<p id="p47308357"><a name="p47308357"></a><a name="p47308357"></a>Boolean value expected.</p>
<p id="p23122032"><a name="p23122032"></a><a name="p23122032"></a>Updates are not supported.</p>
<p id="p6771698"><a name="p6771698"></a><a name="p6771698"></a>Allowed values: True</p>
</td>
</tr>
<tr id="row1303142291516"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p144261222215"><a name="p144261222215"></a><a name="p144261222215"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p11636647"><a name="p11636647"></a><a name="p11636647"></a>The maximum number of connections permitted for this load balancer. Defaults to -1, which is infinite.</p>
<p id="p37620965"><a name="p37620965"></a><a name="p37620965"></a>Integer value expected.</p>
<p id="p3044365"><a name="p3044365"></a><a name="p3044365"></a>Can be updated without replacement.</p>
<p id="p27399290"><a name="p27399290"></a><a name="p27399290"></a>Defaults to "-1".</p>
<p id="p45267019"><a name="p45267019"></a><a name="p45267019"></a>The value must be in the range -1 to 2147483647, include -1 and 2147483647.</p>
</td>
</tr>
<tr id="row330314224158"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p15426132272111"><a name="p15426132272111"></a><a name="p15426132272111"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p42749962"><a name="p42749962"></a><a name="p42749962"></a>Description of this listener.</p>
<p id="p49205346"><a name="p49205346"></a><a name="p49205346"></a>String value expected.</p>
<p id="p40194930"><a name="p40194930"></a><a name="p40194930"></a>Can be updated without replacement.</p>
<p id="p26210052"><a name="p26210052"></a><a name="p26210052"></a>Defaults to " ".</p>
</td>
</tr>
<tr id="row16303132210151"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1542620223214"><a name="p1542620223214"></a><a name="p1542620223214"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p42639483"><a name="p42639483"></a><a name="p42639483"></a>Name of this listener.</p>
<p id="p48211034"><a name="p48211034"></a><a name="p48211034"></a>String value expected.</p>
<p id="p31246127"><a name="p31246127"></a><a name="p31246127"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1330352211511"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p0426122142120"><a name="p0426122142120"></a><a name="p0426122142120"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p47908359"><a name="p47908359"></a><a name="p47908359"></a>The ID of the tenant who owns the listener.</p>
<p id="p28522052"><a name="p28522052"></a><a name="p28522052"></a>String value expected.</p>
<p id="p55371884"><a name="p55371884"></a><a name="p55371884"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section245391831810"></a>

<a name="table205697717231"></a>
<table><thead align="left"><tr id="row10741018161712"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p1657014782312"><a name="p1657014782312"></a><a name="p1657014782312"></a><strong id="b166987316176"><a name="b166987316176"></a><a name="b166987316176"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p2570107112313"><a name="p2570107112313"></a><a name="p2570107112313"></a><strong id="b9699031181713"><a name="b9699031181713"></a><a name="b9699031181713"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row197441851715"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p175708702320"><a name="p175708702320"></a><a name="p175708702320"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p65705717235"><a name="p65705717235"></a><a name="p65705717235"></a>ID of the default pool this listener is associated to.</p>
</td>
</tr>
<tr id="row1975141821710"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p18570878235"><a name="p18570878235"></a><a name="p18570878235"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p105706772319"><a name="p105706772319"></a><a name="p105706772319"></a>ID of the load balancer this listener is associated to.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section1048163151911"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Neutron::LBaaS::Listener
    properties:
      admin_state_up: Boolean
      connection_limit: Integer
      default_tls_container_ref: String
      description: String
      loadbalancer: String
      name: String
      protocol: String
      protocol_port: Integer
      sni_container_refs: [Value, Value, ...]
      tenant_id: String
```

