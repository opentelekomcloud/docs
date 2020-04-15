# NIC Management<a name="EN-US_TOPIC_0103071513"></a>

<a name="table166711250142311"></a>
<table><thead align="left"><tr id="row16721750172310"><th class="cellrowborder" valign="top" width="30.630891950688905%" id="mcps1.1.4.1.1"><p id="p1567220502233"><a name="p1567220502233"></a><a name="p1567220502233"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="33.401015228426395%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="35.9680928208847%" id="mcps1.1.4.1.3"><p id="p93075832319"><a name="p93075832319"></a><a name="p93075832319"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row1791015116446"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p18358191824417"><a name="p18358191824417"></a><a name="p18358191824417"></a>POST /v1/{project_id}/cloudservers/{server_id}/nics/delete</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p73585185447"><a name="p73585185447"></a><a name="p73585185447"></a>Deleting NICs from an ECS in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul3358181815441"></a><a name="ul3358181815441"></a><ul id="ul3358181815441"><li>ecs:cloudServerNics:delete</li></ul>
</td>
</tr>
<tr id="row13910171120449"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p1435951874411"><a name="p1435951874411"></a><a name="p1435951874411"></a>POST /v1/{project_id}/cloudservers/{server_id}/nics</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p12359141874418"><a name="p12359141874418"></a><a name="p12359141874418"></a>Adding NICs to an ECS in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul7359151814415"></a><a name="ul7359151814415"></a><ul id="ul7359151814415"><li>ecs:cloudServers:addNics</li></ul>
</td>
</tr>
<tr id="row2672125032316"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p33882125248"><a name="p33882125248"></a><a name="p33882125248"></a>POST /v2/{project_id}/servers/{server_id}/os-interface</p>
<p id="p1210593418340"><a name="p1210593418340"></a><a name="p1210593418340"></a>POST /v2.1/{project_id}/servers/{server_id}/os-interface</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p02271056433"><a name="p02271056433"></a><a name="p02271056433"></a>Adding an ECS NIC (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul1388912122416"></a><a name="ul1388912122416"></a><ul id="ul1388912122416"><li>ecs:serverInterfaces:use</li><li>ecs:serverInterfaces:get</li></ul>
<a name="ul18388612152416"></a><a name="ul18388612152416"></a><ul id="ul18388612152416"><li>vpc:networks:get</li><li>vpc:networks:update</li><li>vpc:subnets:get</li><li>vpc:subnets:update</li><li>vpc:ports:create</li><li>vpc:ports:update</li><li>vpc:ports:get</li><li>vpc:networks:create</li><li>vpc:subnets:create</li><li>vpc:routers:get</li><li>vpc:routers:update</li></ul>
</td>
</tr>
<tr id="row06721150152313"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p1738911218249"><a name="p1738911218249"></a><a name="p1738911218249"></a>DELETE /v2/{project_id}/servers/{server_id}/os-interface/{id}</p>
<p id="p1821244653411"><a name="p1821244653411"></a><a name="p1821244653411"></a>DELETE /v2.1/{project_id}/servers/{server_id}/os-interface/{id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p152273515431"><a name="p152273515431"></a><a name="p152273515431"></a>Deleting an ECS NIC (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul193891312182411"></a><a name="ul193891312182411"></a><ul id="ul193891312182411"><li>ecs:serverInterfaces:use</li><li>ecs:serverInterfaces:get</li><li>ecs:servers:get</li></ul>
<a name="ul2038921282413"></a><a name="ul2038921282413"></a><ul id="ul2038921282413"><li>vpc:networks:create</li><li>vpc:subnets:create</li><li>vpc:networks:get</li><li>vpc:networks:update</li><li>vpc:subnets:get</li><li>vpc:subnets:update</li><li>vpc:ports:delete</li><li>vpc:ports:update</li><li>vpc:ports:get</li><li>vpc:routers:get</li><li>vpc:routers:update</li></ul>
</td>
</tr>
<tr id="row46721250112312"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p1339151212245"><a name="p1339151212245"></a><a name="p1339151212245"></a>GET /v2/{project_id}/servers/{server_id}/os-interface</p>
<p id="p126512573342"><a name="p126512573342"></a><a name="p126512573342"></a>GET /v2.1/{project_id}/servers/{server_id}/os-interface</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p172276511435"><a name="p172276511435"></a><a name="p172276511435"></a>Querying ECS NICs (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul1339121242413"></a><a name="ul1339121242413"></a><ul id="ul1339121242413"><li>ecs:serverInterfaces:get</li></ul>
<a name="ul1339161262419"></a><a name="ul1339161262419"></a><ul id="ul1339161262419"><li>vpc:ports:get</li></ul>
</td>
</tr>
<tr id="row14673195092318"><td class="cellrowborder" valign="top" width="30.630891950688905%" headers="mcps1.1.4.1.1 "><p id="p3392131218246"><a name="p3392131218246"></a><a name="p3392131218246"></a>GET /v2/{project_id}/servers/{server_id}/os-interface/{id}</p>
<p id="p84616163514"><a name="p84616163514"></a><a name="p84616163514"></a>GET /v2.1/{project_id}/servers/{server_id}/os-interface/{id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.401015228426395%" headers="mcps1.1.4.1.2 "><p id="p1022718514437"><a name="p1022718514437"></a><a name="p1022718514437"></a>Querying NIC Information About an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="35.9680928208847%" headers="mcps1.1.4.1.3 "><a name="ul8392181232411"></a><a name="ul8392181232411"></a><ul id="ul8392181232411"><li>ecs:serverInterfaces:get</li></ul>
<a name="ul1392171214243"></a><a name="ul1392171214243"></a><ul id="ul1392171214243"><li>vpc:ports:get</li></ul>
</td>
</tr>
</tbody>
</table>

