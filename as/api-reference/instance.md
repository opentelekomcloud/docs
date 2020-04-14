# Instance<a name="EN-US_TOPIC_0120434955"></a>

<a name="table195929912148"></a>
<table><thead align="left"><tr id="row65927971413"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.1"><p id="p226374317618"><a name="p226374317618"></a><a name="p226374317618"></a><strong id="b14203122381617"><a name="b14203122381617"></a><a name="b14203122381617"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.282828282828287%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b18555227151619"><a name="b18555227151619"></a><a name="b18555227151619"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.35353535353536%" id="mcps1.1.5.1.3"><p id="p1841555914555"><a name="p1841555914555"></a><a name="p1841555914555"></a><strong id="b59333011613"><a name="b59333011613"></a><a name="b59333011613"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.5.1.4"><p id="p76761627369"><a name="p76761627369"></a><a name="p76761627369"></a><strong id="b94563322164"><a name="b94563322164"></a><a name="b94563322164"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1059211912142"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.1 "><p id="p14210743158"><a name="p14210743158"></a><a name="p14210743158"></a>Querying instances in an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.1.5.1.2 "><p id="p135921795142"><a name="p135921795142"></a><a name="p135921795142"></a>as:instances:list</p>
</td>
<td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.3 "><a name="ul159418416586"></a><a name="ul159418416586"></a><ul id="ul159418416586"><li>Supported:<a name="ul12943144113582"></a><a name="ul12943144113582"></a><ul id="ul12943144113582"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul14945174175813"></a><a name="ul14945174175813"></a><ul id="ul14945174175813"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.4 "><p id="p967622717620"><a name="p967622717620"></a><a name="p967622717620"></a>GET /autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/list</p>
</td>
</tr>
<tr id="row195927915143"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.1 "><p id="p19210043159"><a name="p19210043159"></a><a name="p19210043159"></a>Removing instances from an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.1.5.1.2 "><p id="p1059249141411"><a name="p1059249141411"></a><a name="p1059249141411"></a>as:instances:delete</p>
</td>
<td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.3 "><a name="ul1985675217116"></a><a name="ul1985675217116"></a><ul id="ul1985675217116"><li>Supported:<a name="ul685845211117"></a><a name="ul685845211117"></a><ul id="ul685845211117"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul17859105211114"></a><a name="ul17859105211114"></a><ul id="ul17859105211114"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.4 "><p id="p967613271564"><a name="p967613271564"></a><a name="p967613271564"></a>DELETE /autoscaling-api/v1/{project_id}/scaling_group_instance/{instance_id}</p>
</td>
</tr>
<tr id="row55926921417"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.1 "><p id="p8210134318511"><a name="p8210134318511"></a><a name="p8210134318511"></a>Performing operations on instances in batches</p>
</td>
<td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.1.5.1.2 "><p id="p5592090148"><a name="p5592090148"></a><a name="p5592090148"></a>as:instances:batchAction</p>
</td>
<td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.3 "><a name="ul19673454131111"></a><a name="ul19673454131111"></a><ul id="ul19673454131111"><li>Supported:<a name="ul1467414544117"></a><a name="ul1467414544117"></a><ul id="ul1467414544117"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul166751547118"></a><a name="ul166751547118"></a><ul id="ul166751547118"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.4 "><p id="p467714271610"><a name="p467714271610"></a><a name="p467714271610"></a>POST /autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action</p>
</td>
</tr>
</tbody>
</table>

