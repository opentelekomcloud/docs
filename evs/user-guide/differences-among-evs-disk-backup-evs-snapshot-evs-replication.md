# Differences Among EVS Disk Backup/EVS Snapshot/EVS Replication<a name="evs_01_0022"></a>

EVS disk backup, EVS snapshot, and EVS replication all provide redundancies for the EVS disk data to improve data reliability.  [Table 1](#table20229141185044)  lists the differences among them.

**Table  1**  Differences among EVS disk backup, EVS snapshot, and EVS replication

<a name="table20229141185044"></a>
<table><thead align="left"><tr id="row15865513185044"><th class="cellrowborder" valign="top" width="16.43%" id="mcps1.2.6.1.1"><p id="p23234826185044"><a name="p23234826185044"></a><a name="p23234826185044"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="22.82%" id="mcps1.2.6.1.2"><p id="p2972717185044"><a name="p2972717185044"></a><a name="p2972717185044"></a>Storage Solution</p>
</th>
<th class="cellrowborder" valign="top" width="22.82%" id="mcps1.2.6.1.3"><p id="p39463562185044"><a name="p39463562185044"></a><a name="p39463562185044"></a>Data Synchronization</p>
</th>
<th class="cellrowborder" valign="top" width="17.93%" id="mcps1.2.6.1.4"><p id="p42431943185044"><a name="p42431943185044"></a><a name="p42431943185044"></a>DR Range</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p14435340185044"><a name="p14435340185044"></a><a name="p14435340185044"></a>Service Recovery</p>
</th>
</tr>
</thead>
<tbody><tr id="row62809202185044"><td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.6.1.1 "><p id="p54380567185044"><a name="p54380567185044"></a><a name="p54380567185044"></a>EVS disk backup</p>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.2 "><p id="p42749784185044"><a name="p42749784185044"></a><a name="p42749784185044"></a>The backup data is stored in the OBS service, isolated from the EVS disk data.</p>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.3 "><p id="p36687371185155"><a name="p36687371185155"></a><a name="p36687371185155"></a>Saving the EVS disk data at specific time points</p>
</td>
<td class="cellrowborder" valign="top" width="17.93%" headers="mcps1.2.6.1.4 "><p id="p33395921185044"><a name="p33395921185044"></a><a name="p33395921185044"></a>The backups and disks must be in the same region, but can be in different AZs.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p55913259185228"><a name="p55913259185228"></a><a name="p55913259185228"></a>Data can be retrieved and services can be restored by restoring the backup data to original disks or creating new disks from backups.</p>
</td>
</tr>
<tr id="row52218143185044"><td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.6.1.1 "><p id="p1811200185044"><a name="p1811200185044"></a><a name="p1811200185044"></a>EVS snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.2 "><p id="p4522786718532"><a name="p4522786718532"></a><a name="p4522786718532"></a>The snapshot data is stored with the disk data.</p>
<div class="note" id="note439761918532"><a name="note439761918532"></a><a name="note439761918532"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3957857618532"><a name="p3957857618532"></a><a name="p3957857618532"></a>It requires a certain period of time to create a backup because data needs to be transferred. Therefore, creating or rolling back a snapshot consumes less time than creating a backup.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.3 "><p id="p5975691185310"><a name="p5975691185310"></a><a name="p5975691185310"></a>Saving the EVS disk data at specific time points</p>
</td>
<td class="cellrowborder" valign="top" width="17.93%" headers="mcps1.2.6.1.4 "><p id="p63972361185316"><a name="p63972361185316"></a><a name="p63972361185316"></a>Same AZ as the EVS disks</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1833826517212"><a name="p1833826517212"></a><a name="p1833826517212"></a>Data can be retrieved and services can be restored by rolling back the snapshot data to original disks or creating new disks from snapshots.</p>
</td>
</tr>
<tr id="row2633138185044"><td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.6.1.1 "><p id="p11957608185044"><a name="p11957608185044"></a><a name="p11957608185044"></a>EVS replication</p>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.2 "><p id="p29042228185044"><a name="p29042228185044"></a><a name="p29042228185044"></a>Data in the DR disks is stored in the data center of another AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="22.82%" headers="mcps1.2.6.1.3 "><p id="p46269656185359"><a name="p46269656185359"></a><a name="p46269656185359"></a>Synchronizing the data with production disks in real time</p>
<div class="note" id="note13773726185359"><a name="note13773726185359"></a><a name="note13773726185359"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p56854676185359"><a name="p56854676185359"></a><a name="p56854676185359"></a>DR disks can synchronize the data with production disks in real time, achieving a Recovery Point Objective (RPO) of zero and ensuring tight consistency between production data and replication data.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="17.93%" headers="mcps1.2.6.1.4 "><p id="p441147185452"><a name="p441147185452"></a><a name="p441147185452"></a>Different AZs with no more than 100 km in physical distance</p>
<div class="note" id="note3970330185452"><a name="note3970330185452"></a><a name="note3970330185452"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p35732974185452"><a name="p35732974185452"></a><a name="p35732974185452"></a>You can specify the secondary AZ, and the distance between the data centers in the primary and secondary AZs must be less than 100 km.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p4615848215626"><a name="p4615848215626"></a><a name="p4615848215626"></a>Services are restored directly by the existing DR disks and DR servers.</p>
<p id="p64436640185044"><a name="p64436640185044"></a><a name="p64436640185044"></a>If the primary AZ is faulty, services in the primary AZ will be stopped, and DR resources in the secondary AZ will be enabled to restore services.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

