# OSE::ELB::Member<a name="EN-US_TOPIC_0088407025"></a>

A resource for member.

## Required Properties<a name="section157954239719"></a>

<a name="table59063491672"></a>
<table><thead align="left"><tr id="row19436221547"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1090684917719"><a name="p1090684917719"></a><a name="p1090684917719"></a><strong id="b1849833520414"><a name="b1849833520414"></a><a name="b1849833520414"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p13906124912714"><a name="p13906124912714"></a><a name="p13906124912714"></a><strong id="b149923516410"><a name="b149923516410"></a><a name="b149923516410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6436021244"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1790634918718"><a name="p1790634918718"></a><a name="p1790634918718"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p28839657"><a name="p28839657"></a><a name="p28839657"></a>The ID of listener associated.</p>
<p id="p58230324"><a name="p58230324"></a><a name="p58230324"></a>String value expected.</p>
<p id="p54310869"><a name="p54310869"></a><a name="p54310869"></a>Updates cause replacement.</p>
<p id="p19035773"><a name="p19035773"></a><a name="p19035773"></a>Value must be of type elb.ls</p>
</td>
</tr>
<tr id="row1743772448"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p209060491774"><a name="p209060491774"></a><a name="p209060491774"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p65502606"><a name="p65502606"></a><a name="p65502606"></a>The servers to add as members.</p>
<p id="p52652545"><a name="p52652545"></a><a name="p52652545"></a>List value expected.</p>
<p id="p4110864"><a name="p4110864"></a><a name="p4110864"></a>Can be updated without replacement.</p>
<p id="p36997778"><a name="p36997778"></a><a name="p36997778"></a>Value length: from 1 to 6, include 1 and 6.</p>
<p id="p64544554"><a name="p64544554"></a><a name="p64544554"></a>List contents:</p>
<a name="ul44030080"></a><a name="ul44030080"></a><ul id="ul44030080"><li>*<p id="p9666738"><a name="p9666738"></a><a name="p9666738"></a>Map value expected.</p>
<p id="p19891785"><a name="p19891785"></a><a name="p19891785"></a>Can be updated without replacement.</p>
<p id="p10199381780"><a name="p10199381780"></a><a name="p10199381780"></a>Map properties:</p>
<a name="ul45081544389"></a><a name="ul45081544389"></a><ul id="ul45081544389"><li>address<p id="p1533060291"><a name="p1533060291"></a><a name="p1533060291"></a>The private address of the server to add.</p>
<p id="p333030890"><a name="p333030890"></a><a name="p333030890"></a>String value expected.</p>
<p id="p13330001099"><a name="p13330001099"></a><a name="p13330001099"></a>Can be updated without replacement.</p>
</li><li>server_id<p id="p11484481994"><a name="p11484481994"></a><a name="p11484481994"></a>ID of the server to add.</p>
<p id="p748418815916"><a name="p748418815916"></a><a name="p748418815916"></a>String value expected.</p>
<p id="p1148413818915"><a name="p1148413818915"></a><a name="p1148413818915"></a>Can be updated without replacement.</p>
<p id="p1485281691"><a name="p1485281691"></a><a name="p1485281691"></a>Value must be of type nova.server</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section460715321779"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::ELB::Member
    properties:
      listener_id: String
      members: [{"address": String, "server_id": String}, {"address": String, "server_id": String}, …]
```

