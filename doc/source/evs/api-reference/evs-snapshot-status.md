# EVS Snapshot Status<a name="evs_04_0041"></a>

<a name="table294040819524"></a>
<table><thead align="left"><tr id="row1757352919524"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1416977319524"><a name="p1416977319524"></a><a name="p1416977319524"></a>EVS Snapshot Status</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p690096519524"><a name="p690096519524"></a><a name="p690096519524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6210869019524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6474802819524"><a name="p6474802819524"></a><a name="p6474802819524"></a>creating</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1009894319524"><a name="p1009894319524"></a><a name="p1009894319524"></a>The EVS snapshot is being created.</p>
</td>
</tr>
<tr id="row2378162519524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4726344319524"><a name="p4726344319524"></a><a name="p4726344319524"></a>available</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p313365719524"><a name="p313365719524"></a><a name="p313365719524"></a>The EVS snapshot is successfully created.</p>
</td>
</tr>
<tr id="row2820292119524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p273526119524"><a name="p273526119524"></a><a name="p273526119524"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2022961819524"><a name="p2022961819524"></a><a name="p2022961819524"></a>An error occurs when you try to create an EVS snapshot.</p>
</td>
</tr>
<tr id="row4784884019524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5055086519524"><a name="p5055086519524"></a><a name="p5055086519524"></a>deleting</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p97940619524"><a name="p97940619524"></a><a name="p97940619524"></a>The EVS snapshot is being deleted.</p>
</td>
</tr>
<tr id="row881466019524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4289885919524"><a name="p4289885919524"></a><a name="p4289885919524"></a>error_deleting</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5225554619524"><a name="p5225554619524"></a><a name="p5225554619524"></a>An error occurs when you try to delete an EVS snapshot.</p>
</td>
</tr>
<tr id="row53787319524"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4356772819524"><a name="p4356772819524"></a><a name="p4356772819524"></a>rollbacking</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14379857182618"><a name="p14379857182618"></a><a name="p14379857182618"></a>The EVS snapshot is rolling back data.</p>
<div class="note" id="note4770122218113"><a name="note4770122218113"></a><a name="note4770122218113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul2407842411214"></a><a name="ul2407842411214"></a><ul id="ul2407842411214"><li>When you roll back a snapshot to an EVS disk, you can only roll back the snapshot to the source EVS disk. Rollback to a specified disk is not possible.</li><li>You can roll back an EVS disk from a snapshot only when the disk is in the <strong id="b842352706192843"><a name="b842352706192843"></a><a name="b842352706192843"></a>available</strong> or <strong id="b842352706192847"><a name="b842352706192847"></a><a name="b842352706192847"></a>error_rollbacking</strong> state.</li></ul>
</div></div>
</td>
</tr>
<tr id="row207855215268"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p152090254243"><a name="p152090254243"></a><a name="p152090254243"></a>backing-up</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p253815332616"><a name="p253815332616"></a><a name="p253815332616"></a>The EVS snapshot is being created from a backup via a native OpenStack API.</p>
<p id="p1439415519264"><a name="p1439415519264"></a><a name="p1439415519264"></a>The system is automatically creating the EVS snapshot when an EVS disk is created from a backup via a VBS API.</p>
</td>
</tr>
</tbody>
</table>

