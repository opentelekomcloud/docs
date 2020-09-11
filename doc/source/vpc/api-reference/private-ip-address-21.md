# Private IP Address<a name="vpc_permission_0007"></a>

<a name="table967413133817"></a>
<table><thead align="left"><tr id="row9708231163820"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.4.1.1"><p id="p1970823143813"><a name="p1970823143813"></a><a name="p1970823143813"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="29.72972972972973%" id="mcps1.1.4.1.2"><p id="p12638211185918"><a name="p12638211185918"></a><a name="p12638211185918"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="20.27027027027027%" id="mcps1.1.4.1.3"><p id="p137081931143810"><a name="p137081931143810"></a><a name="p137081931143810"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row197081331113817"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p17091031143815"><a name="p17091031143815"></a><a name="p17091031143815"></a>POST /v1/{project_id}/privateips</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p9638111155912"><a name="p9638111155912"></a><a name="p9638111155912"></a>Assigns a private IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p13892440173820"><a name="p13892440173820"></a><a name="p13892440173820"></a>vpc:privateIps:create</p>
</td>
</tr>
<tr id="row15709203163811"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p7709103117385"><a name="p7709103117385"></a><a name="p7709103117385"></a>GET /v1/{project_id}/privateips/{privateip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p363851114598"><a name="p363851114598"></a><a name="p363851114598"></a>Queries a private IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p9226104210387"><a name="p9226104210387"></a><a name="p9226104210387"></a>vpc:privateIps:get</p>
</td>
</tr>
<tr id="row1670914317388"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p17709831173812"><a name="p17709831173812"></a><a name="p17709831173812"></a>GET /v1/{project_id}/subnets/{subnet_id}/privateips</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p8638811165911"><a name="p8638811165911"></a><a name="p8638811165911"></a>Queries private IP addresses.</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p1724712431387"><a name="p1724712431387"></a><a name="p1724712431387"></a>vpc:privateIps:list</p>
</td>
</tr>
<tr id="row6709163118385"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.1 "><p id="p14709143173818"><a name="p14709143173818"></a><a name="p14709143173818"></a>DELETE /v1/{project_id}/privateips/{privateip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="29.72972972972973%" headers="mcps1.1.4.1.2 "><p id="p6638181175920"><a name="p6638181175920"></a><a name="p6638181175920"></a>Deletes a private IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="20.27027027027027%" headers="mcps1.1.4.1.3 "><p id="p12681044203812"><a name="p12681044203812"></a><a name="p12681044203812"></a>vpc:privateIps:delete</p>
</td>
</tr>
</tbody>
</table>

