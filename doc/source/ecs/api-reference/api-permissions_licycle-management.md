# Lifecycle Management<a name="EN-US_TOPIC_0103071510"></a>

<a name="table1587111571724"></a>
<table><thead align="left"><tr id="row5871165713215"><th class="cellrowborder" valign="top" width="43.25925925925926%" id="mcps1.1.4.1.1"><p id="p11871195719215"><a name="p11871195719215"></a><a name="p11871195719215"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="30.814814814814817%" id="mcps1.1.4.1.2"><p id="p28621644185118"><a name="p28621644185118"></a><a name="p28621644185118"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="25.925925925925924%" id="mcps1.1.4.1.3"><p id="p38711657129"><a name="p38711657129"></a><a name="p38711657129"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row6118143811524"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p9828202281915"><a name="p9828202281915"></a><a name="p9828202281915"></a>POST /v1/{project_id}/cloudservers</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p1286344465110"><a name="p1286344465110"></a><a name="p1286344465110"></a>Creating ECSs</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul9828142210192"></a><a name="ul9828142210192"></a><ul id="ul9828142210192"><li>Assigning a New EIP<a name="ul233121516335"></a><a name="ul233121516335"></a><ul id="ul233121516335"><li>ecs:cloudServers:create</li><li>vpc:publicIps:create</li></ul>
</li><li>Using an Existing EIP<a name="ul1287616455335"></a><a name="ul1287616455335"></a><ul id="ul1287616455335"><li>ecs:cloudServers:create</li><li>vpc:publicIps:update</li></ul>
</li></ul>
</td>
</tr>
<tr id="row78644281610"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p1382822218198"><a name="p1382822218198"></a><a name="p1382822218198"></a>POST /v1/{project_id}/cloudservers/delete</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p08634442517"><a name="p08634442517"></a><a name="p08634442517"></a>Deleting ECSs</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul12828162216195"></a><a name="ul12828162216195"></a><ul id="ul12828162216195"><li>ecs:cloudServers:delete</li></ul>
</td>
</tr>
<tr id="row38713577219"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p725331122516"><a name="p725331122516"></a><a name="p725331122516"></a>GET /v2/{project_id}/servers/detail</p>
<p id="p16337193516315"><a name="p16337193516315"></a><a name="p16337193516315"></a>GET /v2.1/{project_id}/servers/detail</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p369615322438"><a name="p369615322438"></a><a name="p369615322438"></a>Querying Details About ECSs (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul1933753518319"></a><a name="ul1933753518319"></a><ul id="ul1933753518319"><li>ecs:servers:list</li><li>ecs:servers:get</li></ul>
<a name="ul933763510316"></a><a name="ul933763510316"></a><ul id="ul933763510316"><li>ecs:serverVolumes:use</li><li>ecs:diskConfigs:use</li><li>ecs:securityGroups:use</li><li>ecs:serverKeypairs:get</li></ul>
<a name="ul1033718356310"></a><a name="ul1033718356310"></a><ul id="ul1033718356310"><li>vpc:securityGroups:get</li><li>vpc:securityGroupRules:get</li><li>vpc:networks:get</li><li>vpc:subnets:get</li><li>vpc:ports:get</li><li>vpc:routers:get</li></ul>
</td>
</tr>
<tr id="row58713574219"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p172163919520"><a name="p172163919520"></a><a name="p172163919520"></a>GET /v2/{project_id}/servers</p>
<p id="p292383619252"><a name="p292383619252"></a><a name="p292383619252"></a>GET /v2.1/{project_id}/servers</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p1386254410510"><a name="p1386254410510"></a><a name="p1386254410510"></a>Querying ECSs (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul372239658"></a><a name="ul372239658"></a><ul id="ul372239658"><li>ecs:servers:list</li></ul>
</td>
</tr>
<tr id="row88711057321"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p2723392051"><a name="p2723392051"></a><a name="p2723392051"></a>GET /v2/{project_id}/servers/{server_id}</p>
<p id="p41651192619"><a name="p41651192619"></a><a name="p41651192619"></a>GET /v2.1/{project_id}/servers/{server_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p108621644105118"><a name="p108621644105118"></a><a name="p108621644105118"></a>Querying Details About an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul87293914516"></a><a name="ul87293914516"></a><ul id="ul87293914516"><li>ecs:servers:get</li></ul>
<a name="ul169877811527"></a><a name="ul169877811527"></a><ul id="ul169877811527"><li>ecs:serverVolumes:use</li><li>ecs:diskConfigs:use</li><li>ecs:securityGroups:use</li><li>ecs:serverKeypairs:get</li></ul>
<a name="ul1698713811526"></a><a name="ul1698713811526"></a><ul id="ul1698713811526"><li>vpc:securityGroups:get</li><li>vpc:securityGroupRules:get</li><li>vpc:networks:get</li><li>vpc:subnets:get</li><li>vpc:ports:get</li><li>vpc:routers:get</li></ul>
</td>
</tr>
<tr id="row19755103191416"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p183216467273"><a name="p183216467273"></a><a name="p183216467273"></a>POST /v2/{project_id}/servers</p>
<p id="p032113463271"><a name="p032113463271"></a><a name="p032113463271"></a>POST /v2/{project_id}/os-volumes_boot</p>
<p id="p5883772911"><a name="p5883772911"></a><a name="p5883772911"></a>POST /v2.1/{project_id}/servers</p>
<p id="p11883670913"><a name="p11883670913"></a><a name="p11883670913"></a>POST /v2.1/{project_id}/os-volumes_boot</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p18605195717538"><a name="p18605195717538"></a><a name="p18605195717538"></a>Creating an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul1388313711917"></a><a name="ul1388313711917"></a><ul id="ul1388313711917"><li>ecs:servers:create</li><li>ecs:servers:get</li><li>ecs:serverInterfaces:use</li><li>ecs:serverInterfaces:get</li><li>ecs:flavors:get</li><li>ecs:securityGroups:use</li></ul>
<a name="ul688318715914"></a><a name="ul688318715914"></a><ul id="ul688318715914"><li>evs:volumes:list</li><li>evs:volumes:get</li><li>evs:volumes:create</li><li>evs:volumes:attach</li><li>evs:volumes:manage</li><li>vpc:securityGroups:get</li></ul>
<a name="ul28841471697"></a><a name="ul28841471697"></a><ul id="ul28841471697"><li>vpc:networks:get</li><li>vpc:networks:update</li><li>vpc:subnets:get</li><li>vpc:subnets:update</li><li>vpc:ports:create</li><li>vpc:ports:update</li><li>vpc:ports:get</li><li>vpc:ports:delete</li><li>vpc:networks:create</li><li>vpc:subnets:create</li><li>vpc:routers:get</li><li>vpc:routers:update</li></ul>
<a name="ul13884117497"></a><a name="ul13884117497"></a><ul id="ul13884117497"><li>ims:images:list</li><li>ims:images:get</li></ul>
</td>
</tr>
<tr id="row328513471419"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p114321317142817"><a name="p114321317142817"></a><a name="p114321317142817"></a>DELETE /v2/{project_id}/servers/{server_id}</p>
<p id="p33197248919"><a name="p33197248919"></a><a name="p33197248919"></a>DELETE /v2.1/{project_id}/servers/{server_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p260615717539"><a name="p260615717539"></a><a name="p260615717539"></a>Deleting an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul1631916243919"></a><a name="ul1631916243919"></a><ul id="ul1631916243919"><li>ecs:servers:delete</li></ul>
</td>
</tr>
<tr id="row1262503681417"><td class="cellrowborder" valign="top" width="43.25925925925926%" headers="mcps1.1.4.1.1 "><p id="p1492018285282"><a name="p1492018285282"></a><a name="p1492018285282"></a>PUT /v2/{project_id}/servers/{server_id}</p>
<p id="p731918241919"><a name="p731918241919"></a><a name="p731918241919"></a>PUT /v2.1/{project_id}/servers/{server_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.814814814814817%" headers="mcps1.1.4.1.2 "><p id="p116062577537"><a name="p116062577537"></a><a name="p116062577537"></a>Modifying an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="25.925925925925924%" headers="mcps1.1.4.1.3 "><a name="ul03191224499"></a><a name="ul03191224499"></a><ul id="ul03191224499"><li>ecs:servers:update</li><li>ecs:servers:get</li></ul>
</td>
</tr>
</tbody>
</table>

