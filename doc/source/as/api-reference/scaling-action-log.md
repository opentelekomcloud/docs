# Scaling Action Log<a name="EN-US_TOPIC_0120434958"></a>

<a name="table6297203615613"></a>
<table><thead align="left"><tr id="row12297636266"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.1"><p id="p61031358882"><a name="p61031358882"></a><a name="p61031358882"></a><strong id="b132646871713"><a name="b132646871713"></a><a name="b132646871713"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b59821810111710"><a name="b59821810111710"></a><a name="b59821810111710"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.313131313131315%" id="mcps1.1.5.1.3"><p id="p197010343178"><a name="p197010343178"></a><a name="p197010343178"></a><strong id="b14131813201716"><a name="b14131813201716"></a><a name="b14131813201716"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.272727272727277%" id="mcps1.1.5.1.4"><p id="p7355162712816"><a name="p7355162712816"></a><a name="p7355162712816"></a><strong id="b11617015171719"><a name="b11617015171719"></a><a name="b11617015171719"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row829720361060"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.1 "><p id="p18451949152018"><a name="p18451949152018"></a><a name="p18451949152018"></a>Querying scaling action logs</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p329713361468"><a name="p329713361468"></a><a name="p329713361468"></a>as:activityLogs:list</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.1.5.1.3 "><a name="ul97965417158"></a><a name="ul97965417158"></a><ul id="ul97965417158"><li>Supported:<a name="ul1881195410154"></a><a name="ul1881195410154"></a><ul id="ul1881195410154"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1584754161519"></a><a name="ul1584754161519"></a><ul id="ul1584754161519"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27.272727272727277%" headers="mcps1.1.5.1.4 "><p id="p1729711367610"><a name="p1729711367610"></a><a name="p1729711367610"></a>GET /autoscaling-api/v1/{project_id}/scaling_activity_log/{scaling_group_id}</p>
</td>
</tr>
<tr id="row795812513117"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.1 "><p id="p1395995810"><a name="p1395995810"></a><a name="p1395995810"></a>Querying scaling action logs (V2)</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p2959195119"><a name="p2959195119"></a><a name="p2959195119"></a>as:activityLogs:list</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.1.5.1.3 "><a name="ul959215129220"></a><a name="ul959215129220"></a><ul id="ul959215129220"><li>Supported:<a name="ul15592012424"></a><a name="ul15592012424"></a><ul id="ul15592012424"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul35931112929"></a><a name="ul35931112929"></a><ul id="ul35931112929"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="27.272727272727277%" headers="mcps1.1.5.1.4 "><p id="p1832531318110"><a name="p1832531318110"></a><a name="p1832531318110"></a>GET /autoscaling-api/v2/{project_id}/scaling_activity_log/{scaling_group_id}</p>
</td>
</tr>
</tbody>
</table>

