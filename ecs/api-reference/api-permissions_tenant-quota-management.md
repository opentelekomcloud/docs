# Tenant Quota Management<a name="EN-US_TOPIC_0103071517"></a>

<a name="table151682922617"></a>
<table><thead align="left"><tr id="row19171029162611"><th class="cellrowborder" valign="top" width="31.274929827153198%" id="mcps1.1.4.1.1"><p id="p417102942614"><a name="p417102942614"></a><a name="p417102942614"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="34.052297237405824%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="34.672772935440975%" id="mcps1.1.4.1.3"><p id="p14177299263"><a name="p14177299263"></a><a name="p14177299263"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row67071724254"><td class="cellrowborder" valign="top" width="31.274929827153198%" headers="mcps1.1.4.1.1 "><p id="p159161514254"><a name="p159161514254"></a><a name="p159161514254"></a>GET /v1/{project_id}/cloudservers/limits</p>
</td>
<td class="cellrowborder" valign="top" width="34.052297237405824%" headers="mcps1.1.4.1.2 "><p id="p5916450254"><a name="p5916450254"></a><a name="p5916450254"></a>Querying the Tenant Quota</p>
</td>
<td class="cellrowborder" valign="top" width="34.672772935440975%" headers="mcps1.1.4.1.3 "><a name="ul7916155102513"></a><a name="ul7916155102513"></a><ul id="ul7916155102513"><li>ecs:cloudServerQuotas:get</li></ul>
</td>
</tr>
<tr id="row4171029192612"><td class="cellrowborder" valign="top" width="31.274929827153198%" headers="mcps1.1.4.1.1 "><p id="p6985345192613"><a name="p6985345192613"></a><a name="p6985345192613"></a>GET /v2/{project_id}/os-quota-sets/{project_id}?user_id={user_id}</p>
<p id="p16953157123914"><a name="p16953157123914"></a><a name="p16953157123914"></a>GET /v2.1/{project_id}/os-quota-sets/{project_id}?user_id={user_id}</p>
</td>
<td class="cellrowborder" valign="top" width="34.052297237405824%" headers="mcps1.1.4.1.2 "><p id="p1171215418449"><a name="p1171215418449"></a><a name="p1171215418449"></a>Querying Quotas of a Tenant (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.672772935440975%" headers="mcps1.1.4.1.3 "><a name="ul3985154519264"></a><a name="ul3985154519264"></a><ul id="ul3985154519264"><li>ecs:quotas:get</li></ul>
</td>
</tr>
<tr id="row8177294260"><td class="cellrowborder" valign="top" width="31.274929827153198%" headers="mcps1.1.4.1.1 "><p id="p14985445102614"><a name="p14985445102614"></a><a name="p14985445102614"></a>GET /v2/{project_id}/os-quota-sets/{project_id}/defaults</p>
<p id="p1233141273910"><a name="p1233141273910"></a><a name="p1233141273910"></a>GET /v2.1/{project_id}/os-quota-sets/{project_id}/defaults</p>
</td>
<td class="cellrowborder" valign="top" width="34.052297237405824%" headers="mcps1.1.4.1.2 "><p id="p971212424418"><a name="p971212424418"></a><a name="p971212424418"></a>Querying Default Quota (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.672772935440975%" headers="mcps1.1.4.1.3 "><a name="ul7985104532610"></a><a name="ul7985104532610"></a><ul id="ul7985104532610"><li>ecs:quotas:get</li></ul>
</td>
</tr>
</tbody>
</table>

