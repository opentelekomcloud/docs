# ECS Status Management<a name="EN-US_TOPIC_0103071511"></a>

<a name="table12570457816"></a>
<table><thead align="left"><tr id="row2025712451682"><th class="cellrowborder" valign="top" width="38.02816901408451%" id="mcps1.1.4.1.1"><p id="p72571745883"><a name="p72571745883"></a><a name="p72571745883"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="26.760563380281692%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="35.21126760563381%" id="mcps1.1.4.1.3"><p id="p162571745883"><a name="p162571745883"></a><a name="p162571745883"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row43301239171419"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p1478183141917"><a name="p1478183141917"></a><a name="p1478183141917"></a>POST /v2/{project_id}/cloudservers/{server_id}/changeos</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p4183378205559"><a name="p4183378205559"></a><a name="p4183378205559"></a>Changing an ECS OS</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul747812371910"></a><a name="ul747812371910"></a><ul id="ul747812371910"><li>ecs:cloudServers:changeOS</li></ul>
</td>
</tr>
<tr id="row1225714451388"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p54781035190"><a name="p54781035190"></a><a name="p54781035190"></a>POST /v2/{project_id}/cloudservers/{server_id}/reinstallos</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p1993921813394"><a name="p1993921813394"></a><a name="p1993921813394"></a>Reinstalling an ECS OS</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul047811315199"></a><a name="ul047811315199"></a><ul id="ul047811315199"><li>ecs:cloudServers:rebuild</li></ul>
</td>
</tr>
<tr id="row113711517144014"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p204781139197"><a name="p204781139197"></a><a name="p204781139197"></a>POST /v1/{project_id}/cloudservers/{server_id}/resize</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p1686224415113"><a name="p1686224415113"></a><a name="p1686224415113"></a>Modifying the Specifications of an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul194781331914"></a><a name="ul194781331914"></a><ul id="ul194781331914"><li>ecs:cloudServers:resize</li></ul>
</td>
</tr>
<tr id="row12332174073420"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p1497201991811"><a name="p1497201991811"></a><a name="p1497201991811"></a>POST /v1/{project_id}/cloudservers/{server_id}/migrate</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p17497171917188"><a name="p17497171917188"></a><a name="p17497171917188"></a>Cold Migrating an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul42841353172214"></a><a name="ul42841353172214"></a><ul id="ul42841353172214"><li>ecs:cloudServers:migrate</li></ul>
</td>
</tr>
<tr id="row52571745582"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p1971991132919"><a name="p1971991132919"></a><a name="p1971991132919"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p032112243919"><a name="p032112243919"></a><a name="p032112243919"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p76061457195316"><a name="p76061457195316"></a><a name="p76061457195316"></a>Stopping an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul632116243917"></a><a name="ul632116243917"></a><ul id="ul632116243917"><li>ecs:servers:stop</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row172571445985"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p152512210291"><a name="p152512210291"></a><a name="p152512210291"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p19321824193"><a name="p19321824193"></a><a name="p19321824193"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p860675714535"><a name="p860675714535"></a><a name="p860675714535"></a>Restarting an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul1332192415914"></a><a name="ul1332192415914"></a><ul id="ul1332192415914"><li>ecs:servers:reboot</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row1525717451489"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p19809103313297"><a name="p19809103313297"></a><a name="p19809103313297"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
<p id="p032110243914"><a name="p032110243914"></a><a name="p032110243914"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p186061757165319"><a name="p186061757165319"></a><a name="p186061757165319"></a>Modifying the Specifications of an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul1632115247916"></a><a name="ul1632115247916"></a><ul id="ul1632115247916"><li>ecs:servers:resize</li><li>ecs:servers:get</li></ul>
<a name="ul13212241396"></a><a name="ul13212241396"></a><ul id="ul13212241396"><li>evs:volumes:list</li><li>evs:volumes:create</li><li>evs:volumes:get</li><li>evs:volumes:attach</li><li>evs:volumes:detach</li><li>evs:volumes:manage</li></ul>
<a name="ul193211124399"></a><a name="ul193211124399"></a><ul id="ul193211124399"><li>vpc:ports:get</li><li>vpc:ports:update</li><li>vpc:ports:create</li><li>vpc:ports:delete</li></ul>
</td>
</tr>
<tr id="row48081934497"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p45019471894"><a name="p45019471894"></a><a name="p45019471894"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p11181391309"><a name="p11181391309"></a><a name="p11181391309"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p6606557155319"><a name="p6606557155319"></a><a name="p6606557155319"></a>Rebuilding an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul550124712916"></a><a name="ul550124712916"></a><ul id="ul550124712916"><li>ecs:servers:rebuild</li><li>ecs:servers:get</li><li>ecs:servers:update</li></ul>
<a name="ul9507479910"></a><a name="ul9507479910"></a><ul id="ul9507479910"><li>ims:images:get</li><li>ims:images:list</li><li>ims:images:update</li></ul>
</td>
</tr>
<tr id="row19808934597"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p1550144717916"><a name="p1550144717916"></a><a name="p1550144717916"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p16597019203015"><a name="p16597019203015"></a><a name="p16597019203015"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p960685795319"><a name="p960685795319"></a><a name="p960685795319"></a>Locking an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul1850647494"></a><a name="ul1850647494"></a><ul id="ul1850647494"><li>ecs:servers:lock</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row1180814349912"><td class="cellrowborder" valign="top" width="38.02816901408451%" headers="mcps1.1.4.1.1 "><p id="p550164716914"><a name="p550164716914"></a><a name="p550164716914"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p3361132313017"><a name="p3361132313017"></a><a name="p3361132313017"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="26.760563380281692%" headers="mcps1.1.4.1.2 "><p id="p560645745312"><a name="p560645745312"></a><a name="p560645745312"></a>Unlocking an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.21126760563381%" headers="mcps1.1.4.1.3 "><a name="ul15020472098"></a><a name="ul15020472098"></a><ul id="ul15020472098"><li>ecs:servers:unlock</li><li>ecs:servers:get</li></ul>
</td>
</tr>
</tbody>
</table>

