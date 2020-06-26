# OSE::SFS::Share<a name="EN-US_TOPIC_0103361353"></a>

A resource for creating file sharing resources

Scalable File Service \(SFS\) provides users with a fully hosted shared file storage, which can be scaled to PB scale, providing high availability and durability, and providing powerful support for massive data and high-bandwidth applications. SFS applies to various application scenarios, including media processing, file sharing, content management, and web services.

## Required Properties<a name="section720258104315"></a>

<a name="table8352172438"></a>
<table><thead align="left"><tr id="row637151711436"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p643749201717"><a name="p643749201717"></a><a name="p643749201717"></a><strong id="b573441043311"><a name="b573441043311"></a><a name="b573441043311"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p164371961711"><a name="p164371961711"></a><a name="p164371961711"></a><strong id="b1373541013339"><a name="b1373541013339"></a><a name="b1373541013339"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row837161714432"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p8871524134518"><a name="p8871524134518"></a><a name="p8871524134518"></a>share_proto</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p168711124124513"><a name="p168711124124513"></a><a name="p168711124124513"></a>File system sharing protocol</p>
<p id="p11871624104516"><a name="p11871624104516"></a><a name="p11871624104516"></a>String value expected.</p>
<p id="p15871132414450"><a name="p15871132414450"></a><a name="p15871132414450"></a>Updates cause replacement.</p>
<p id="p12871324154514"><a name="p12871324154514"></a><a name="p12871324154514"></a>Allowed value: NFS</p>
</td>
</tr>
<tr id="row83718179431"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p18871182414513"><a name="p18871182414513"></a><a name="p18871182414513"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p17871124124520"><a name="p17871124124520"></a><a name="p17871124124520"></a>Shared capacity</p>
<p id="p148712241458"><a name="p148712241458"></a><a name="p148712241458"></a>Integer value expected.</p>
<p id="p1087118246451"><a name="p1087118246451"></a><a name="p1087118246451"></a>Can be updated without replacement.</p>
<p id="p1987172434520"><a name="p1987172434520"></a><a name="p1987172434520"></a>Unit: GB</p>
<div class="note" id="note0970732489"><a name="note0970732489"></a><a name="note0970732489"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p139717318488"><a name="p139717318488"></a><a name="p139717318488"></a>The size cannot exceed the quota. Otherwise, the shared storage fails to be created.</p>
</div></div>
</td>
</tr>
<tr id="row2371217164311"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p287122484512"><a name="p287122484512"></a><a name="p287122484512"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p3871724144512"><a name="p3871724144512"></a><a name="p3871724144512"></a>Name of the sharing storage</p>
<p id="p19871182411458"><a name="p19871182411458"></a><a name="p19871182411458"></a>String value expected.</p>
<p id="p1087142434516"><a name="p1087142434516"></a><a name="p1087142434516"></a>Can be updated without replacement.</p>
<p id="p14871112464518"><a name="p14871112464518"></a><a name="p14871112464518"></a>Value range: 1 to 255. The value can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section1151718287460"></a>

<a name="table162881248164613"></a>
<table><thead align="left"><tr id="row929044854613"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p13628018097"><a name="p13628018097"></a><a name="p13628018097"></a><strong id="b114181510338"><a name="b114181510338"></a><a name="b114181510338"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p126295186911"><a name="p126295186911"></a><a name="p126295186911"></a><strong id="b1914215152333"><a name="b1914215152333"></a><a name="b1914215152333"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row929024884612"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p13152992475"><a name="p13152992475"></a><a name="p13152992475"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p161520912475"><a name="p161520912475"></a><a name="p161520912475"></a>Description for a sharing file system</p>
<p id="p1915215984714"><a name="p1915215984714"></a><a name="p1915215984714"></a>String value expected.</p>
<p id="p11521944720"><a name="p11521944720"></a><a name="p11521944720"></a>Can be updated without replacement.</p>
<p id="p71527911475"><a name="p71527911475"></a><a name="p71527911475"></a>Length: 0 to 255</p>
</td>
</tr>
<tr id="row9290448174612"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p171521954712"><a name="p171521954712"></a><a name="p171521954712"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p12153293477"><a name="p12153293477"></a><a name="p12153293477"></a>Sharing range</p>
<p id="p1715315944717"><a name="p1715315944717"></a><a name="p1715315944717"></a>Boolean value expected.</p>
<p id="p161535915476"><a name="p161535915476"></a><a name="p161535915476"></a>Updates cause replacement.</p>
<p id="p815313944715"><a name="p815313944715"></a><a name="p815313944715"></a>The default value is false.</p>
<div class="note" id="note86617423474"><a name="note86617423474"></a><a name="note86617423474"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1066284274714"><a name="p1066284274714"></a><a name="p1066284274714"></a>The Boolean value can be true/false, yes/no, or on/off.</p>
</div></div>
</td>
</tr>
<tr id="row029074817461"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p5651841114817"><a name="p5651841114817"></a><a name="p5651841114817"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p15651134116480"><a name="p15651134116480"></a><a name="p15651134116480"></a>AZ name</p>
<p id="p176511141184817"><a name="p176511141184817"></a><a name="p176511141184817"></a>String value expected.</p>
<p id="p14651441164815"><a name="p14651441164815"></a><a name="p14651441164815"></a>Updates cause replacement.</p>
<p id="p965154119486"><a name="p965154119486"></a><a name="p965154119486"></a>Length: 0 to 255.</p>
<div class="note" id="note780213019492"><a name="note780213019492"></a><a name="note780213019492"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p580213019490"><a name="p580213019490"></a><a name="p580213019490"></a>If no AZ information is entered, the default AZ is used. If no storage resource is available in the default AZ, creating a sharing storage fails.</p>
</div></div>
</td>
</tr>
<tr id="row92904485469"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1065114419489"><a name="p1065114419489"></a><a name="p1065114419489"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1765144117487"><a name="p1765144117487"></a><a name="p1765144117487"></a>Key-value pair of one to more dictionary form</p>
<p id="p7864161217402"><a name="p7864161217402"></a><a name="p7864161217402"></a>Map value expected.</p>
<p id="p15651041134816"><a name="p15651041134816"></a><a name="p15651041134816"></a>Updates cause replacement.</p>
<p id="p665154144812"><a name="p665154144812"></a><a name="p665154144812"></a>The default value is {}.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section666012341495"></a>

<a name="table1138634418492"></a>
<table><thead align="left"><tr id="row19387154494913"><th class="cellrowborder" valign="top" width="38%" id="mcps1.1.3.1.1"><p id="p11174227913"><a name="p11174227913"></a><a name="p11174227913"></a><strong id="b10708161943318"><a name="b10708161943318"></a><a name="b10708161943318"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.1.3.1.2"><p id="p161915221396"><a name="p161915221396"></a><a name="p161915221396"></a><strong id="b2070931919334"><a name="b2070931919334"></a><a name="b2070931919334"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row438964412499"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.3.1.1 "><p id="p01443115503"><a name="p01443115503"></a><a name="p01443115503"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.3.1.2 "><p id="p314412115509"><a name="p314412115509"></a><a name="p314412115509"></a>Sharing file system name</p>
</td>
</tr>
<tr id="row1138934414492"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.3.1.1 "><p id="p141441117502"><a name="p141441117502"></a><a name="p141441117502"></a>export_location</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.3.1.2 "><p id="p181442175017"><a name="p181442175017"></a><a name="p181442175017"></a>Sharing file system mount path</p>
</td>
</tr>
<tr id="row14389154410491"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.3.1.1 "><p id="p1314491145018"><a name="p1314491145018"></a><a name="p1314491145018"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.3.1.2 "><p id="p19144171165014"><a name="p19144171165014"></a><a name="p19144171165014"></a>Key-value pair of one to more dictionary form</p>
</td>
</tr>
<tr id="row1338954484917"><td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.3.1.1 "><p id="p1114491145013"><a name="p1114491145013"></a><a name="p1114491145013"></a>host</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.3.1.2 "><p id="p13145161125010"><a name="p13145161125010"></a><a name="p13145161125010"></a>Shared host name</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section13752111716504"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::SFS::Share
    properties:
      share_proto: String
      size: Integer
      name: String 
      description: String 
      availability_zone: String
      metadata:
        key1: value1
        key2: value2
```

