# EVS Replication Pair Status \(Deprecated\)<a name="evs_04_0042"></a>

<a name="table294040819524"></a>
<table><thead align="left"><tr id="row1757352919524"><th class="cellrowborder" valign="top" width="35.339999999999996%" id="mcps1.1.3.1.1"><p id="p1031057218958"><a name="p1031057218958"></a><a name="p1031057218958"></a>EVS Replication Pair Status</p>
</th>
<th class="cellrowborder" valign="top" width="64.66%" id="mcps1.1.3.1.2"><p id="p690096519524"><a name="p690096519524"></a><a name="p690096519524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6210869019524"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p6474802819524"><a name="p6474802819524"></a><a name="p6474802819524"></a>creating</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p1009894319524"><a name="p1009894319524"></a><a name="p1009894319524"></a>The EVS replication pair is being created.</p>
</td>
</tr>
<tr id="row2378162519524"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p4726344319524"><a name="p4726344319524"></a><a name="p4726344319524"></a>available</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p313365719524"><a name="p313365719524"></a><a name="p313365719524"></a>The EVS replication pair is successfully created and is available for use.</p>
</td>
</tr>
<tr id="row2820292119524"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p273526119524"><a name="p273526119524"></a><a name="p273526119524"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p2022961819524"><a name="p2022961819524"></a><a name="p2022961819524"></a>An error occurs when you try to create an EVS replication pair.</p>
</td>
</tr>
<tr id="row4784884019524"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p5055086519524"><a name="p5055086519524"></a><a name="p5055086519524"></a>deleting</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p97940619524"><a name="p97940619524"></a><a name="p97940619524"></a>The EVS replication pair is being deleted.</p>
</td>
</tr>
<tr id="row881466019524"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p4289885919524"><a name="p4289885919524"></a><a name="p4289885919524"></a>error_deleting</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p5225554619524"><a name="p5225554619524"></a><a name="p5225554619524"></a>An error occurs when you try to delete an EVS replication pair.</p>
</td>
</tr>
</tbody>
</table>

<a name="table236938720159"></a>
<table><thead align="left"><tr id="row5510109820159"><th class="cellrowborder" valign="top" width="35.339999999999996%" id="mcps1.1.3.1.1"><p id="p527151318955"><a name="p527151318955"></a><a name="p527151318955"></a>EVS Replication Pair Replication Status</p>
</th>
<th class="cellrowborder" valign="top" width="64.66%" id="mcps1.1.3.1.2"><p id="p285700520159"><a name="p285700520159"></a><a name="p285700520159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3009088020159"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p2144219520159"><a name="p2144219520159"></a><a name="p2144219520159"></a>active</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p5909620620159"><a name="p5909620620159"></a><a name="p5909620620159"></a>The replication status of the EVS replication pair is normal, and the data in the production disk is consistent with the data in the DR disk.</p>
</td>
</tr>
<tr id="row6210381020159"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p6435275020159"><a name="p6435275020159"></a><a name="p6435275020159"></a>active-stopped</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p4519022920159"><a name="p4519022920159"></a><a name="p4519022920159"></a>The replication status of the EVS replication pair is paused, and the data in the production disk is consistent with the data in the DR disk.</p>
</td>
</tr>
<tr id="row2727424720159"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p6173041720159"><a name="p6173041720159"></a><a name="p6173041720159"></a>copying</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p3410787120159"><a name="p3410787120159"></a><a name="p3410787120159"></a>The data in the two disks of the EVS replication pair is being synchronized.</p>
</td>
</tr>
<tr id="row18360861111731"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p10834779111731"><a name="p10834779111731"></a><a name="p10834779111731"></a>inactive</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p5201946111731"><a name="p5201946111731"></a><a name="p5201946111731"></a>The replication status of the EVS replication pair is paused, or the data replication is interrupted. Data in the two disks is inconsistent and needs to be synchronized.</p>
</td>
</tr>
<tr id="row155444291216"><td class="cellrowborder" valign="top" width="35.339999999999996%" headers="mcps1.1.3.1.1 "><p id="p511392621216"><a name="p511392621216"></a><a name="p511392621216"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="64.66%" headers="mcps1.1.3.1.2 "><p id="p486395961216"><a name="p486395961216"></a><a name="p486395961216"></a>The replication status of the EVS replication pair becomes abnormal.</p>
</td>
</tr>
</tbody>
</table>

