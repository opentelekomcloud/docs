# OSE::SFS::ShareAccessRule<a name="EN-US_TOPIC_0103361354"></a>

A resource for creating file sharing access rules

## Required Properties<a name="section1839672955219"></a>

<a name="table1436012398521"></a>
<table><thead align="left"><tr id="row5362439175216"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p336213910528"><a name="p336213910528"></a><a name="p336213910528"></a><strong id="b57962024133315"><a name="b57962024133315"></a><a name="b57962024133315"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p73621939125214"><a name="p73621939125214"></a><a name="p73621939125214"></a><strong id="b57984242335"><a name="b57984242335"></a><a name="b57984242335"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row236253985220"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p12886195405210"><a name="p12886195405210"></a><a name="p12886195405210"></a>share_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p1588619543527"><a name="p1588619543527"></a><a name="p1588619543527"></a>Sharing ID of access rules</p>
<p id="p3886205411529"><a name="p3886205411529"></a><a name="p3886205411529"></a>String value expected.</p>
<p id="p7886054125219"><a name="p7886054125219"></a><a name="p7886054125219"></a>Updates cause replacement.</p>
<p id="p20886155417525"><a name="p20886155417525"></a><a name="p20886155417525"></a>Value range: Valid shared ID, which is strictly checked using the UUID regular expression.</p>
</td>
</tr>
<tr id="row13362239135216"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p3362139205211"><a name="p3362139205211"></a><a name="p3362139205211"></a>allow_access</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p12357141513543"><a name="p12357141513543"></a><a name="p12357141513543"></a>Sharing file system access policy</p>
<p id="p133572158542"><a name="p133572158542"></a><a name="p133572158542"></a>Map value expected.</p>
<p id="p23571415145414"><a name="p23571415145414"></a><a name="p23571415145414"></a>Map properties:</p>
<a name="ul229519206549"></a><a name="ul229519206549"></a><ul id="ul229519206549"><li>access_level<p id="p3142134719544"><a name="p3142134719544"></a><a name="p3142134719544"></a>Access pPermission level</p>
<p id="p2142154745415"><a name="p2142154745415"></a><a name="p2142154745415"></a>String value expected.</p>
<p id="p5142347135410"><a name="p5142347135410"></a><a name="p5142347135410"></a>Allowed value: ro (read-only), rw (read/write)</p>
</li><li>access_type<p id="p648992195517"><a name="p648992195517"></a><a name="p648992195517"></a>Specifies the type of a access rule. NFS sharing supports only the cert type.</p>
<p id="p104891425558"><a name="p104891425558"></a><a name="p104891425558"></a>String value expected.</p>
<div class="note" id="note12689145195519"><a name="note12689145195519"></a><a name="note12689145195519"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p46891751175516"><a name="p46891751175516"></a><a name="p46891751175516"></a>If the NFS sharing access rule type is cert, set <strong id="b10879520154319"><a name="b10879520154319"></a><a name="b10879520154319"></a>access_to</strong> to the VPC ID.</p>
</div></div>
</li><li>access_to<p id="p513714216568"><a name="p513714216568"></a><a name="p513714216568"></a>Specifies the value of an access rule. Currently, only the VPC ID is supported.</p>
<p id="p525285114560"><a name="p525285114560"></a><a name="p525285114560"></a>String value expected.</p>
<p id="p825211511562"><a name="p825211511562"></a><a name="p825211511562"></a>Value range: The value cannot be empty. The length of the character string must be verified through the regular UUID check.</p>
<div class="note" id="note151111746573"><a name="note151111746573"></a><a name="note151111746573"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1011113417575"><a name="p1011113417575"></a><a name="p1011113417575"></a>Only one VPC ID can be added to a sharing file system. If two or more VPC IDs are added, the sharing file system cannot be mounted.</p>
</div></div>
</li></ul>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section198441347135713"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::SFS::ShareAccessRule
    properties:
      share_id: String
      allow_access:
        access_level: String
        access_type: String
        access_to: String
```

