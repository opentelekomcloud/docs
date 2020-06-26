# Quota<a name="EN-US_TOPIC_0120460558"></a>

<a name="table136899111019"></a>
<table><thead align="left"><tr id="row76812917100"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.1"><p id="p156502141495"><a name="p156502141495"></a><a name="p156502141495"></a><strong id="b3356122331714"><a name="b3356122331714"></a><a name="b3356122331714"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b15154182881717"><a name="b15154182881717"></a><a name="b15154182881717"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.1.5.1.3"><p id="p197010343178"><a name="p197010343178"></a><a name="p197010343178"></a><strong id="b10958833161719"><a name="b10958833161719"></a><a name="b10958833161719"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.1.5.1.4"><p id="p738119531994"><a name="p738119531994"></a><a name="p738119531994"></a><strong id="b1247043513174"><a name="b1247043513174"></a><a name="b1247043513174"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3682093107"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.1 "><p id="p18112181072314"><a name="p18112181072314"></a><a name="p18112181072314"></a>Querying AS quotas</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p76899181011"><a name="p76899181011"></a><a name="p76899181011"></a>as:quotas:get</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.1.5.1.3 "><a name="ul97965417158"></a><a name="ul97965417158"></a><ul id="ul97965417158"><li>Supported:<a name="ul1881195410154"></a><a name="ul1881195410154"></a><ul id="ul1881195410154"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1584754161519"></a><a name="ul1584754161519"></a><ul id="ul1584754161519"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.5.1.4 "><p id="p106810921012"><a name="p106810921012"></a><a name="p106810921012"></a>GET /autoscaling-api/v1/{project_id}/quotas</p>
</td>
</tr>
<tr id="row868149161012"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.1 "><p id="p111221072312"><a name="p111221072312"></a><a name="p111221072312"></a>Querying AS policy and instance quotas</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p36817981011"><a name="p36817981011"></a><a name="p36817981011"></a>as:quotas:get</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.1.5.1.3 "><a name="ul206152273618"></a><a name="ul206152273618"></a><ul id="ul206152273618"><li>Supported:<a name="ul47142215364"></a><a name="ul47142215364"></a><ul id="ul47142215364"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1170222364"></a><a name="ul1170222364"></a><ul id="ul1170222364"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.5.1.4 "><p id="p196810941019"><a name="p196810941019"></a><a name="p196810941019"></a>GET /autoscaling-api/v1/{project_id}/quotas/{scaling_group_id}</p>
</td>
</tr>
</tbody>
</table>

