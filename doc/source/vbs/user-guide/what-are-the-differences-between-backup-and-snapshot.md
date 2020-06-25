# What Are the Differences Between Backup and Snapshot?<a name="EN-US_TOPIC_0126537916"></a>

Both backup and snapshot provide data redundancy for EVS disks to improve data reliability.  [Table 1](#table20229141185044)  lists the differences between them.

**Table  1**  Differences between backup and snapshot

<a name="table20229141185044"></a>
<table><thead align="left"><tr id="row15865513185044"><th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.6.1.1"><p id="p23234826185044"><a name="p23234826185044"></a><a name="p23234826185044"></a>Technology</p>
</th>
<th class="cellrowborder" valign="top" width="22.63%" id="mcps1.2.6.1.2"><p id="p2972717185044"><a name="p2972717185044"></a><a name="p2972717185044"></a>Saved In</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p39463562185044"><a name="p39463562185044"></a><a name="p39463562185044"></a>Synchronization</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p42431943185044"><a name="p42431943185044"></a><a name="p42431943185044"></a>DR Range</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p14435340185044"><a name="p14435340185044"></a><a name="p14435340185044"></a>Service Recovery</p>
</th>
</tr>
</thead>
<tbody><tr id="row62809202185044"><td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.6.1.1 "><p id="p54380567185044"><a name="p54380567185044"></a><a name="p54380567185044"></a>Backup</p>
</td>
<td class="cellrowborder" valign="top" width="22.63%" headers="mcps1.2.6.1.2 "><p id="p42749784185044"><a name="p42749784185044"></a><a name="p42749784185044"></a>Backup data is stored in OBS, instead of EVS disks. This realizes data restoration upon EVS disk data loss or corruption.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p36687371185155"><a name="p36687371185155"></a><a name="p36687371185155"></a>A backup is the data copy of an EVS disk at a given point in time. VBS provides automatic backup by configuring backup policies. Deleting an EVS disk will not clear its backups.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p33395921185044"><a name="p33395921185044"></a><a name="p33395921185044"></a>A snapshot and its source EVS disk reside in the same AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p55913259185228"><a name="p55913259185228"></a><a name="p55913259185228"></a>Data can be retrieved and services can be restored by restoring the backup data to original disks or creating new disks from backups, ensuring superb data reliability.</p>
</td>
</tr>
<tr id="row52218143185044"><td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.6.1.1 "><p id="p1811200185044"><a name="p1811200185044"></a><a name="p1811200185044"></a>Snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="22.63%" headers="mcps1.2.6.1.2 "><p id="p4522786718532"><a name="p4522786718532"></a><a name="p4522786718532"></a>Snapshot data is stored with EVS disk data.</p>
<div class="note" id="note439761918532"><a name="note439761918532"></a><a name="note439761918532"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3957857618532"><a name="p3957857618532"></a><a name="p3957857618532"></a>Creation of and rollback to snapshots are faster than creation of and restoration from backups, because the latter requires data migration that consumes extra time.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p5975691185310"><a name="p5975691185310"></a><a name="p5975691185310"></a>A snapshot is the state of an EVS disk at a specific point in time. When you delete an EVS disk, the snapshots of the EVS disk are also deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p63972361185316"><a name="p63972361185316"></a><a name="p63972361185316"></a>A snapshot and its source EVS disk reside in the same AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1833826517212"><a name="p1833826517212"></a><a name="p1833826517212"></a>You can use a snapshot to roll back its original EVS disk or create an EVS disk for data retrieve and service recovery.</p>
</td>
</tr>
</tbody>
</table>

