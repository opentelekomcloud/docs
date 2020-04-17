# Replication Consistency Group Status \(Deprecated\)<a name="evs_04_0043"></a>

<a name="table236938720159"></a>
<table><thead align="left"><tr id="row5510109820159"><th class="cellrowborder" valign="top" width="37.4%" id="mcps1.1.3.1.1"><p id="p34958953181156"><a name="p34958953181156"></a><a name="p34958953181156"></a>Replication Consistency Group Status</p>
</th>
<th class="cellrowborder" valign="top" width="62.6%" id="mcps1.1.3.1.2"><p id="p285700520159"><a name="p285700520159"></a><a name="p285700520159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3009088020159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p2144219520159"><a name="p2144219520159"></a><a name="p2144219520159"></a>creating</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p5909620620159"><a name="p5909620620159"></a><a name="p5909620620159"></a>The replication consistency group is being created.</p>
</td>
</tr>
<tr id="row6210381020159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p6435275020159"><a name="p6435275020159"></a><a name="p6435275020159"></a>available</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p4519022920159"><a name="p4519022920159"></a><a name="p4519022920159"></a>The replication consistency group is successfully created and is available for use.</p>
</td>
</tr>
<tr id="row405888320159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p6033412920159"><a name="p6033412920159"></a><a name="p6033412920159"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p5522625520159"><a name="p5522625520159"></a><a name="p5522625520159"></a>An error occurs when you try to create a replication consistency group.</p>
</td>
</tr>
<tr id="row2727424720159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p6173041720159"><a name="p6173041720159"></a><a name="p6173041720159"></a>deleting</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p3410787120159"><a name="p3410787120159"></a><a name="p3410787120159"></a>The replication consistency group is being deleted.</p>
</td>
</tr>
<tr id="row3853538720159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p3435866720159"><a name="p3435866720159"></a><a name="p3435866720159"></a>updating</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p3158866020159"><a name="p3158866020159"></a><a name="p3158866020159"></a>The replication consistency group is being updated. The update includes adding EVS replication pairs to and deleting EVS replication pairs from the replication consistency group.</p>
</td>
</tr>
<tr id="row1586248520159"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p979286920159"><a name="p979286920159"></a><a name="p979286920159"></a>reversing</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p428881661260"><a name="p428881661260"></a><a name="p428881661260"></a>The replication consistency group is being migrated as planned.</p>
</td>
</tr>
<tr id="row04317176146"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p817612362143"><a name="p817612362143"></a><a name="p817612362143"></a>error_reversing</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p10176103641413"><a name="p10176103641413"></a><a name="p10176103641413"></a>An error occurs during a planned migration of the replication consistency group.</p>
</td>
</tr>
<tr id="row3117160512650"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p4187209412650"><a name="p4187209412650"></a><a name="p4187209412650"></a>failovering</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p3619642312650"><a name="p3619642312650"></a><a name="p3619642312650"></a>The failover of the replication consistency group is in progress.</p>
</td>
</tr>
<tr id="row1341122181414"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p139528303145"><a name="p139528303145"></a><a name="p139528303145"></a>failovered</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p59521130131414"><a name="p59521130131414"></a><a name="p59521130131414"></a>The replication consistency group failover is successful.</p>
</td>
</tr>
<tr id="row0138925141419"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p199522307146"><a name="p199522307146"></a><a name="p199522307146"></a>error_failovering</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p8952203013140"><a name="p8952203013140"></a><a name="p8952203013140"></a>An error occurs during a failover of the replication consistency group.</p>
</td>
</tr>
<tr id="row3602356712655"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p3222780612655"><a name="p3222780612655"></a><a name="p3222780612655"></a>error_deleting</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p6031551812655"><a name="p6031551812655"></a><a name="p6031551812655"></a>An error occurs during the deletion of the replication consistency group.</p>
</td>
</tr>
</tbody>
</table>

<a name="table60462243123253"></a>
<table><thead align="left"><tr id="row43432371123253"><th class="cellrowborder" valign="top" width="37.4%" id="mcps1.1.3.1.1"><p id="p822111818126"><a name="p822111818126"></a><a name="p822111818126"></a>Replication Consistency Group Replication Status</p>
</th>
<th class="cellrowborder" valign="top" width="62.6%" id="mcps1.1.3.1.2"><p id="p15552060123253"><a name="p15552060123253"></a><a name="p15552060123253"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51757323123253"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p31593623123253"><a name="p31593623123253"></a><a name="p31593623123253"></a>active</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p8946631123253"><a name="p8946631123253"></a><a name="p8946631123253"></a>The replication status of the replication consistency group is normal, and the data in production disks is consistent with the data in DR disks.</p>
</td>
</tr>
<tr id="row13410816123253"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p12534306123253"><a name="p12534306123253"></a><a name="p12534306123253"></a>active-stopped</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p1699578412049"><a name="p1699578412049"></a><a name="p1699578412049"></a>The replication status of the replication consistency group is paused, and the data between production disks and DR disks within the group is inconsistent.</p>
</td>
</tr>
<tr id="row18032558123253"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p51351131123253"><a name="p51351131123253"></a><a name="p51351131123253"></a>copying</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p65800936123253"><a name="p65800936123253"></a><a name="p65800936123253"></a>The data of the replication consistency group is being synchronized.</p>
</td>
</tr>
<tr id="row15269918114058"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p28903875114058"><a name="p28903875114058"></a><a name="p28903875114058"></a>inactive</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p6320036311416"><a name="p6320036311416"></a><a name="p6320036311416"></a>The replication status of the replication consistency group is paused. The data between production disks and DR disks within the group is inconsistent and needs to be synchronized.</p>
</td>
</tr>
<tr id="row55337514123253"><td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.1.3.1.1 "><p id="p53153643123253"><a name="p53153643123253"></a><a name="p53153643123253"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.1.3.1.2 "><p id="p10477792123253"><a name="p10477792123253"></a><a name="p10477792123253"></a>The replication status of the replication consistency group becomes abnormal.</p>
</td>
</tr>
</tbody>
</table>

