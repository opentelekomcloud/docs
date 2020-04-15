# The File System Is Abnormal<a name="sfs_01_0059"></a>

Currently, the file system exceptions include deletion error, expansion error, reduction error, and reduction failure. When the file system is in these statuses, refer to the following handling suggestions.

**Table  1**  Measures for handling file system abnormalities

<a name="table3528559142611"></a>
<table><thead align="left"><tr id="row6529059102613"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.3.1.1"><p id="p15529195917262"><a name="p15529195917262"></a><a name="p15529195917262"></a>Exception</p>
</th>
<th class="cellrowborder" valign="top" width="78%" id="mcps1.2.3.1.2"><p id="p9529205972620"><a name="p9529205972620"></a><a name="p9529205972620"></a>Suggestion</p>
</th>
</tr>
</thead>
<tbody><tr id="row17529105922620"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p85291359172612"><a name="p85291359172612"></a><a name="p85291359172612"></a>Deletion error</p>
</td>
<td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p155291459182612"><a name="p155291459182612"></a><a name="p155291459182612"></a>When the file system is in the deletion error status, it can automatically recover to the available state. If the status cannot be restored to available, contact the administrator.</p>
</td>
</tr>
<tr id="row8529205962612"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p15297593269"><a name="p15297593269"></a><a name="p15297593269"></a>Expansion error</p>
</td>
<td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p4529155912261"><a name="p4529155912261"></a><a name="p4529155912261"></a>When the file system is in the expansion error status, it can automatically recover to the available state. If the status cannot be restored to available, contact the administrator.</p>
</td>
</tr>
<tr id="row152918592263"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p25291959142614"><a name="p25291959142614"></a><a name="p25291959142614"></a>Reduction error</p>
</td>
<td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p8529159132611"><a name="p8529159132611"></a><a name="p8529159132611"></a>When the file system is in the reduction error status, it takes approximately five minutes for the file system to restore to the available state.</p>
</td>
</tr>
<tr id="row19349115292"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p135311182920"><a name="p135311182920"></a><a name="p135311182920"></a>Reduction failure</p>
</td>
<td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p53511192917"><a name="p53511192917"></a><a name="p53511192917"></a>When the file system is in the reduction failure status, it takes approximately five minutes for the file system to restore to the available state.</p>
</td>
</tr>
</tbody>
</table>

