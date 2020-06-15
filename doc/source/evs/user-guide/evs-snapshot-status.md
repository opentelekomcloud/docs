# EVS Snapshot Status<a name="evs_01_0041"></a>

An EVS snapshot has several statuses.  [Table 1](#evs_faq_0018_table64552624191747)  lists the EVS snapshot statuses, the meaning of each status, and the operations a snapshot in each status allows.

**Table  1**  Snapshot status details

<a name="evs_faq_0018_table64552624191747"></a>
<table><thead align="left"><tr id="evs_faq_0018_row53790844191747"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="evs_faq_0018_p4696184819180"><a name="evs_faq_0018_p4696184819180"></a><a name="evs_faq_0018_p4696184819180"></a>Snapshot Status</p>
</th>
<th class="cellrowborder" valign="top" width="53.63%" id="mcps1.2.4.1.2"><p id="evs_faq_0018_p16533784191747"><a name="evs_faq_0018_p16533784191747"></a><a name="evs_faq_0018_p16533784191747"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.3"><p id="evs_faq_0018_p44528397191747"><a name="evs_faq_0018_p44528397191747"></a><a name="evs_faq_0018_p44528397191747"></a>Allowed Operation</p>
</th>
</tr>
</thead>
<tbody><tr id="evs_faq_0018_row35291149191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p40463785165345"><a name="evs_faq_0018_p40463785165345"></a><a name="evs_faq_0018_p40463785165345"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p56341191165345"><a name="evs_faq_0018_p56341191165345"></a><a name="evs_faq_0018_p56341191165345"></a>The snapshot is being created.</p>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p233769165345"><a name="evs_faq_0018_p233769165345"></a><a name="evs_faq_0018_p233769165345"></a>No operations are allowed.</p>
</td>
</tr>
<tr id="evs_faq_0018_row12893053191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p2259935191846"><a name="evs_faq_0018_p2259935191846"></a><a name="evs_faq_0018_p2259935191846"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p16383851191846"><a name="evs_faq_0018_p16383851191846"></a><a name="evs_faq_0018_p16383851191846"></a>The snapshot is successfully created.</p>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><a name="evs_faq_0018_ul62104117182653"></a><a name="evs_faq_0018_ul62104117182653"></a><ul id="evs_faq_0018_ul62104117182653"><li>Creating EVS disks using snapshots</li><li>Deleting snapshots</li><li>Rolling back snapshots to source EVS disks</li></ul>
</td>
</tr>
<tr id="evs_faq_0018_row721621712446"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p3658433212455"><a name="evs_faq_0018_p3658433212455"></a><a name="evs_faq_0018_p3658433212455"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p3682527212455"><a name="evs_faq_0018_p3682527212455"></a><a name="evs_faq_0018_p3682527212455"></a>The snapshot is being deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p4587262812455"><a name="evs_faq_0018_p4587262812455"></a><a name="evs_faq_0018_p4587262812455"></a>No operations are allowed.</p>
</td>
</tr>
<tr id="evs_faq_0018_row57957852194514"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p7460362194521"><a name="evs_faq_0018_p7460362194521"></a><a name="evs_faq_0018_p7460362194521"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p526628519467"><a name="evs_faq_0018_p526628519467"></a><a name="evs_faq_0018_p526628519467"></a>An error occurs when you try to create a snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p2242870194521"><a name="evs_faq_0018_p2242870194521"></a><a name="evs_faq_0018_p2242870194521"></a>Deleting</p>
</td>
</tr>
<tr id="evs_faq_0018_row51729329191747"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p23982637191747"><a name="evs_faq_0018_p23982637191747"></a><a name="evs_faq_0018_p23982637191747"></a>Deletion failed</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p5387879619469"><a name="evs_faq_0018_p5387879619469"></a><a name="evs_faq_0018_p5387879619469"></a>An error occurs when you try to delete a snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p56250197191747"><a name="evs_faq_0018_p56250197191747"></a><a name="evs_faq_0018_p56250197191747"></a>No operations are allowed.</p>
</td>
</tr>
<tr id="evs_faq_0018_row57899957175726"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p51337573175726"><a name="evs_faq_0018_p51337573175726"></a><a name="evs_faq_0018_p51337573175726"></a>Rolling back</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p3842076519239"><a name="evs_faq_0018_p3842076519239"></a><a name="evs_faq_0018_p3842076519239"></a>The snapshot is rolling back data.</p>
<div class="note" id="evs_faq_0018_note1024257119239"><a name="evs_faq_0018_note1024257119239"></a><a name="evs_faq_0018_note1024257119239"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="evs_faq_0018_ul2507428319239"></a><a name="evs_faq_0018_ul2507428319239"></a><ul id="evs_faq_0018_ul2507428319239"><li>When you roll back a snapshot to an EVS disk, you can only roll back the snapshot to the source EVS disk. Rollback to a specified disk is not supported.</li><li>You can roll back an EVS disk from a snapshot only when the disk is in the <span class="wintitle" id="evs_faq_0018_wintitle355923761181956"><a name="evs_faq_0018_wintitle355923761181956"></a><a name="evs_faq_0018_wintitle355923761181956"></a><b>Available</b></span> or <span class="wintitle" id="evs_faq_0018_wintitle698955377181956"><a name="evs_faq_0018_wintitle698955377181956"></a><a name="evs_faq_0018_wintitle698955377181956"></a><b>Rollback failed</b></span> state.</li></ul>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p6428254175726"><a name="evs_faq_0018_p6428254175726"></a><a name="evs_faq_0018_p6428254175726"></a>No operations are allowed.</p>
</td>
</tr>
<tr id="evs_faq_0018_row202341611579"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="evs_faq_0018_p283543201579"><a name="evs_faq_0018_p283543201579"></a><a name="evs_faq_0018_p283543201579"></a>Backing up</p>
</td>
<td class="cellrowborder" valign="top" width="53.63%" headers="mcps1.2.4.1.2 "><p id="evs_faq_0018_p149985721579"><a name="evs_faq_0018_p149985721579"></a><a name="evs_faq_0018_p149985721579"></a>This status is available only to temporary snapshots. When you create a backup for an EVS disk, a temporary snapshot is automatically created. This status indicates that a temporary snapshot is being created during the backup creation.</p>
<div class="note" id="evs_faq_0018_note1132117458266"><a name="evs_faq_0018_note1132117458266"></a><a name="evs_faq_0018_note1132117458266"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_faq_0018_p9762105912191"><a name="evs_faq_0018_p9762105912191"></a><a name="evs_faq_0018_p9762105912191"></a>Temporary snapshots are created through the VBS service. Do not perform any operation on these snapshots.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.3 "><p id="evs_faq_0018_p69247801579"><a name="evs_faq_0018_p69247801579"></a><a name="evs_faq_0018_p69247801579"></a>No operations are allowed.</p>
</td>
</tr>
</tbody>
</table>

