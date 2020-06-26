# Tag Management<a name="EN-US_TOPIC_0103071521"></a>

<a name="table4509123112811"></a>
<table><thead align="left"><tr id="row19509193152818"><th class="cellrowborder" valign="top" width="31.56266810112964%" id="mcps1.1.4.1.1"><p id="p55099315280"><a name="p55099315280"></a><a name="p55099315280"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="33.552985476062396%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="34.88434642280796%" id="mcps1.1.4.1.3"><p id="p175092031182817"><a name="p175092031182817"></a><a name="p175092031182817"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row169138403108"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p613135211104"><a name="p613135211104"></a><a name="p613135211104"></a>POST  /v1/{project_id}/cloudservers/{server_id}/tags/action</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p168128381113"><a name="p168128381113"></a><a name="p168128381113"></a>Adding or Deleting Tags to or from an ECS in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul741213010125"></a><a name="ul741213010125"></a><ul id="ul741213010125"><li>ecs:cloudServers:put</li></ul>
</td>
</tr>
<tr id="row528011248461"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p162801924124620"><a name="p162801924124620"></a><a name="p162801924124620"></a>GET /v1/{project_id}/cloudservers/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p3280524124613"><a name="p3280524124613"></a><a name="p3280524124613"></a>Querying Project Tags</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul55661041174613"></a><a name="ul55661041174613"></a><ul id="ul55661041174613"><li>ecs:cloudServers:list</li></ul>
</td>
</tr>
<tr id="row19825194020013"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p68258401107"><a name="p68258401107"></a><a name="p68258401107"></a>POST /v1/{project_id}/servers/{server_id}/tags/action</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p168251640902"><a name="p168251640902"></a><a name="p168251640902"></a>Adding Tags in a Batch</p>
<p id="p191425011012"><a name="p191425011012"></a><a name="p191425011012"></a>Deleting Tags in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul1057092653815"></a><a name="ul1057092653815"></a><ul id="ul1057092653815"><li>ecs:servers:setTags</li></ul>
</td>
</tr>
<tr id="row1335672318115"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p1035611231317"><a name="p1035611231317"></a><a name="p1035611231317"></a>POST /v1/{project_id}/servers/resource_instances/action</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p9356423317"><a name="p9356423317"></a><a name="p9356423317"></a>Querying ECSs by Tag</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul465092810389"></a><a name="ul465092810389"></a><ul id="ul465092810389"><li>ecs:servers:getTags</li></ul>
</td>
</tr>
<tr id="row1784614215119"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p128461442119"><a name="p128461442119"></a><a name="p128461442119"></a>GET /v1/{project_id}/servers/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p178476421515"><a name="p178476421515"></a><a name="p178476421515"></a>Querying Project Tags</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul198029307381"></a><a name="ul198029307381"></a><ul id="ul198029307381"><li>ecs:servers:getTags</li></ul>
</td>
</tr>
<tr id="row676275515115"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p776319551911"><a name="p776319551911"></a><a name="p776319551911"></a>GET /v1/{project_id}/servers/{server_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p137631355512"><a name="p137631355512"></a><a name="p137631355512"></a>Querying Tags of an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul1589193215382"></a><a name="ul1589193215382"></a><ul id="ul1589193215382"><li>ecs:servers:getTags</li></ul>
</td>
</tr>
<tr id="row175291830184314"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p79851435134315"><a name="p79851435134315"></a><a name="p79851435134315"></a>GET /v2/{project_id}/servers/{server_id}/tags</p>
<p id="p4238141844315"><a name="p4238141844315"></a><a name="p4238141844315"></a>GET /v2.1/{project_id}/servers/{server_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p1098533511434"><a name="p1098533511434"></a><a name="p1098533511434"></a>Querying Tags of a Specified ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul1898593515437"></a><a name="ul1898593515437"></a><ul id="ul1898593515437"><li>ecs:servers:getTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row553163014438"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p1298513510437"><a name="p1298513510437"></a><a name="p1298513510437"></a>PUT /v2/{project_id}/servers/{server_id}/tags/{tag}</p>
<p id="p447082244315"><a name="p447082244315"></a><a name="p447082244315"></a>PUT /v2.1/{project_id}/servers/{server_id}/tags/{tag}</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p3986435184317"><a name="p3986435184317"></a><a name="p3986435184317"></a>Adding a Tag to an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul29861535184313"></a><a name="ul29861535184313"></a><ul id="ul29861535184313"><li>ecs:servers:setTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row1661113346435"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p1198633514431"><a name="p1198633514431"></a><a name="p1198633514431"></a>PUT /v2/{project_id}/servers/{server_id}/tags</p>
<p id="p988313810430"><a name="p988313810430"></a><a name="p988313810430"></a>PUT /v2.1/{project_id}/servers/{server_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p1998673512438"><a name="p1998673512438"></a><a name="p1998673512438"></a>Creating an ECS Tag (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul298663534316"></a><a name="ul298663534316"></a><ul id="ul298663534316"><li>ecs:servers:setTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row105321930104310"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p5986153519437"><a name="p5986153519437"></a><a name="p5986153519437"></a>DELETE /v2/{project_id}/servers/{server_id}/tags/{tag}</p>
<p id="p127395094318"><a name="p127395094318"></a><a name="p127395094318"></a>DELETE /v2.1/{project_id}/servers/{server_id}/tags/{tag}</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p2987153514433"><a name="p2987153514433"></a><a name="p2987153514433"></a>Deleting a Specified Tag from an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul49875351438"></a><a name="ul49875351438"></a><ul id="ul49875351438"><li>ecs:servers:setTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row353283018431"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p1698733524315"><a name="p1698733524315"></a><a name="p1698733524315"></a>GET /v2/{project_id}/servers/{server_id}/tags/{tag}</p>
<p id="p181272014417"><a name="p181272014417"></a><a name="p181272014417"></a>GET /v2.1/{project_id}/servers/{server_id}/tags/{tag}</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p798713517430"><a name="p798713517430"></a><a name="p798713517430"></a>Querying an ECS Tag (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul59871835174319"></a><a name="ul59871835174319"></a><ul id="ul59871835174319"><li>ecs:servers:getTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row10532193004319"><td class="cellrowborder" valign="top" width="31.56266810112964%" headers="mcps1.1.4.1.1 "><p id="p0987143512438"><a name="p0987143512438"></a><a name="p0987143512438"></a>DELETE /v2/{project_id}/servers/{server_id}/tags</p>
<p id="p7726121014414"><a name="p7726121014414"></a><a name="p7726121014414"></a>DELETE /v2.1/{project_id}/servers/{server_id}/tags</p>
</td>
<td class="cellrowborder" valign="top" width="33.552985476062396%" headers="mcps1.1.4.1.2 "><p id="p129881935204317"><a name="p129881935204317"></a><a name="p129881935204317"></a>Deleting All ECS Tags (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="34.88434642280796%" headers="mcps1.1.4.1.3 "><a name="ul109881035104318"></a><a name="ul109881035104318"></a><ul id="ul109881035104318"><li>ecs:servers:setTags</li><li>ecs:servers:get</li></ul>
</td>
</tr>
</tbody>
</table>

