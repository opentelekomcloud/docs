# What Are the Differences Between CSBS and VBS?<a name="EN-US_TOPIC_0086521573"></a>

[Table 1](#table1253865610215)  lists the differences between Cloud Server Backup Service \(CSBS\) and Volume Backup Service \(VBS\).

**Table  1**  Differences

<a name="table1253865610215"></a>
<table><thead align="left"><tr id="row653825618217"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p5382183615222"><a name="p5382183615222"></a><a name="p5382183615222"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.4.1.2"><p id="p2382173692218"><a name="p2382173692218"></a><a name="p2382173692218"></a>VBS</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.3"><p id="p3382123682212"><a name="p3382123682212"></a><a name="p3382123682212"></a>CSBS</p>
</th>
</tr>
</thead>
<tbody><tr id="row2053875602111"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p13827368221"><a name="p13827368221"></a><a name="p13827368221"></a>Backup objects</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p173821436152218"><a name="p173821436152218"></a><a name="p173821436152218"></a>One or more specified EVS disks (system or data disks)</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p17382636112219"><a name="p17382636112219"></a><a name="p17382636112219"></a>All EVS disks (including system and data disks) on a single ECS</p>
</td>
</tr>
<tr id="row1453818566215"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p438253632215"><a name="p438253632215"></a><a name="p438253632215"></a>Recommended scenario</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p1138263622212"><a name="p1138263622212"></a><a name="p1138263622212"></a>Only data disks need to be backed up, because the system disk does not contain personal data.</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p1038243614228"><a name="p1038243614228"></a><a name="p1038243614228"></a>An entire ECS that needs to be protected</p>
</td>
</tr>
<tr id="row15538056132111"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1382336192211"><a name="p1382336192211"></a><a name="p1382336192211"></a>Advantages</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p19382113692216"><a name="p19382113692216"></a><a name="p19382113692216"></a>Data is secure while the service is cost-competitive.</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p1438217364227"><a name="p1438217364227"></a><a name="p1438217364227"></a>All EVS disks on an ECS have consistent data. They are backed up at the same time, eliminating the problem of data inconsistency caused by backups generated at different points in time.</p>
</td>
</tr>
</tbody>
</table>

