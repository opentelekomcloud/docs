# ECS Group Management<a name="EN-US_TOPIC_0103071520"></a>

<a name="table818845922715"></a>
<table><thead align="left"><tr id="row7188175902716"><th class="cellrowborder" valign="top" width="34.89055384163361%" id="mcps1.1.4.1.1"><p id="p2188659102719"><a name="p2188659102719"></a><a name="p2188659102719"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="33.5683854855296%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="31.541060672836785%" id="mcps1.1.4.1.3"><p id="p319018598276"><a name="p319018598276"></a><a name="p319018598276"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row1739712213368"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p1657484819494"><a name="p1657484819494"></a><a name="p1657484819494"></a>DELETE /v1/{project_id}/cloudservers/os-server-groups/{server_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p1575164811495"><a name="p1575164811495"></a><a name="p1575164811495"></a>Deleting an ECS Group</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p1274584810234"><a name="p1274584810234"></a><a name="p1274584810234"></a>ecs:cloudServers:delete</p>
</td>
</tr>
<tr id="row1039722293615"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p95442162314"><a name="p95442162314"></a><a name="p95442162314"></a>POST /v1{project_id}/cloudservers/os-server-groups</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p75420219238"><a name="p75420219238"></a><a name="p75420219238"></a>Creating an ECS Group</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p208565404263"><a name="p208565404263"></a><a name="p208565404263"></a>ecs:cloudServers:create</p>
</td>
</tr>
<tr id="row1939702214363"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p84911316183615"><a name="p84911316183615"></a><a name="p84911316183615"></a>POST /v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p72697214365"><a name="p72697214365"></a><a name="p72697214365"></a>Adding an ECS to an ECS Group</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p1468917516588"><a name="p1468917516588"></a><a name="p1468917516588"></a>ecs:cloudServers:create</p>
</td>
</tr>
<tr id="row19398922143617"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p73117467262"><a name="p73117467262"></a><a name="p73117467262"></a>POST /v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p19927185164112"><a name="p19927185164112"></a><a name="p19927185164112"></a>Removing an ECS from an ECS Group</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p9381117115812"><a name="p9381117115812"></a><a name="p9381117115812"></a>ecs:cloudServers:delete</p>
</td>
</tr>
<tr id="row7844171811376"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p12373424103718"><a name="p12373424103718"></a><a name="p12373424103718"></a>GET /v1/{project_id}/cloudservers/os-server-groups</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p1737322415375"><a name="p1737322415375"></a><a name="p1737322415375"></a>Querying ECS Groups</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p384858105817"><a name="p384858105817"></a><a name="p384858105817"></a>ecs:cloudServers:list</p>
</td>
</tr>
<tr id="row1867422113710"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p153741624143719"><a name="p153741624143719"></a><a name="p153741624143719"></a>GET /v1/{project_id}/cloudservers/os-server-groups/{server_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p1137442483716"><a name="p1137442483716"></a><a name="p1137442483716"></a>Querying Details About an ECS Group</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p54311710185811"><a name="p54311710185811"></a><a name="p54311710185811"></a>ecs:cloudServers:get</p>
</td>
</tr>
<tr id="row1919025918277"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p1372441410284"><a name="p1372441410284"></a><a name="p1372441410284"></a>POST /v2/{project_id}/os-server-groups</p>
<p id="p1261552114219"><a name="p1261552114219"></a><a name="p1261552114219"></a>POST /v2.1/{project_id}/os-server-groups</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p51751858144418"><a name="p51751858144418"></a><a name="p51751858144418"></a>Creating an ECS Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p467571520586"><a name="p467571520586"></a><a name="p467571520586"></a>ecs:serverGroups:manage</p>
</td>
</tr>
<tr id="row2190135914273"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p15724514122814"><a name="p15724514122814"></a><a name="p15724514122814"></a>GET /v2/{project_id}/os-server-groups</p>
<p id="p3901573429"><a name="p3901573429"></a><a name="p3901573429"></a>GET /v2.1/{project_id}/os-server-groups</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p131751358184415"><a name="p131751358184415"></a><a name="p131751358184415"></a>Querying ECS Groups (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p13672101811581"><a name="p13672101811581"></a><a name="p13672101811581"></a>ecs:serverGroups:manage</p>
</td>
</tr>
<tr id="row278754211811"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p1957614616816"><a name="p1957614616816"></a><a name="p1957614616816"></a>GET /v2/{project_id}/os-server-groups/{server_group_id}</p>
<p id="p7494181134210"><a name="p7494181134210"></a><a name="p7494181134210"></a>GET /v2.1/{project_id}/os-server-groups/{server_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p95762046684"><a name="p95762046684"></a><a name="p95762046684"></a>Querying Details About an ECS Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p187419208581"><a name="p187419208581"></a><a name="p187419208581"></a>ecs:serverGroups:manage</p>
</td>
</tr>
<tr id="row13190135952716"><td class="cellrowborder" valign="top" width="34.89055384163361%" headers="mcps1.1.4.1.1 "><p id="p117241514142819"><a name="p117241514142819"></a><a name="p117241514142819"></a>DELETE /v2/{project_id}/os-server-groups/{server_group_id}</p>
<p id="p73221016204211"><a name="p73221016204211"></a><a name="p73221016204211"></a>DELETE /v2.1/{project_id}/os-server-groups/{server_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.5683854855296%" headers="mcps1.1.4.1.2 "><p id="p1017511584446"><a name="p1017511584446"></a><a name="p1017511584446"></a>Deleting an ECS Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="31.541060672836785%" headers="mcps1.1.4.1.3 "><p id="p372392155815"><a name="p372392155815"></a><a name="p372392155815"></a>ecs:serverGroups:manage</p>
</td>
</tr>
</tbody>
</table>

