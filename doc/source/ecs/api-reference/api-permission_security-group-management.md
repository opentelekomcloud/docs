# Security Group Management<a name="EN-US_TOPIC_0103072347"></a>

<a name="table614680103012"></a>
<table><thead align="left"><tr id="row121463017301"><th class="cellrowborder" valign="top" width="31.175124512047383%" id="mcps1.1.4.1.1"><p id="p201463083017"><a name="p201463083017"></a><a name="p201463083017"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="30.448243370574772%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="38.376632117377845%" id="mcps1.1.4.1.3"><p id="p51461506309"><a name="p51461506309"></a><a name="p51461506309"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row141469023019"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p3958113214303"><a name="p3958113214303"></a><a name="p3958113214303"></a>POST /v2/{project_id}/os-security-groups</p>
<p id="p174241828203118"><a name="p174241828203118"></a><a name="p174241828203118"></a>POST /v2.1/{project_id}/os-security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p1610821144210"><a name="p1610821144210"></a><a name="p1610821144210"></a>Creating a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul119581321306"></a><a name="ul119581321306"></a><ul id="ul119581321306"><li>ecs:securityGroups:use</li></ul>
<a name="ul1958632173018"></a><a name="ul1958632173018"></a><ul id="ul1958632173018"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:create</li><li>vpc:securityGroups:update</li></ul>
</td>
</tr>
<tr id="row714610173016"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p795853223014"><a name="p795853223014"></a><a name="p795853223014"></a>DELETE /v2/{project_id}/os-security-groups/{security_group_id}</p>
<p id="p1572117398318"><a name="p1572117398318"></a><a name="p1572117398318"></a>DELETE /v2.1/{project_id}/os-security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p111012111429"><a name="p111012111429"></a><a name="p111012111429"></a>Deleting a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul4958153215300"></a><a name="ul4958153215300"></a><ul id="ul4958153215300"><li>ecs:securityGroups:use</li></ul>
<a name="ul129581832173018"></a><a name="ul129581832173018"></a><ul id="ul129581832173018"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:delete</li><li>vpc:securityGroups:update</li></ul>
</td>
</tr>
<tr id="row111468093016"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p14959173216308"><a name="p14959173216308"></a><a name="p14959173216308"></a>GET /v2/{project_id}/os-security-groups/{security_group_id}</p>
<p id="p16711195820310"><a name="p16711195820310"></a><a name="p16711195820310"></a>GET /v2.1/{project_id}/os-security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p1010132174219"><a name="p1010132174219"></a><a name="p1010132174219"></a>Querying Details About a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul29591632103018"></a><a name="ul29591632103018"></a><ul id="ul29591632103018"><li>ecs:securityGroups:use</li></ul>
<a name="ul396053212304"></a><a name="ul396053212304"></a><ul id="ul396053212304"><li>vpc:securityGroups:get</li></ul>
</td>
</tr>
<tr id="row1914610012300"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p39605329307"><a name="p39605329307"></a><a name="p39605329307"></a>GET /v2/{project_id}/os-security-groups</p>
<p id="p11337939321"><a name="p11337939321"></a><a name="p11337939321"></a>GET /v2.1/{project_id}/os-security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p310221114218"><a name="p310221114218"></a><a name="p310221114218"></a>Querying Security Groups (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul696013326305"></a><a name="ul696013326305"></a><ul id="ul696013326305"><li>ecs:securityGroups:use</li></ul>
<a name="ul13960732183020"></a><a name="ul13960732183020"></a><ul id="ul13960732183020"><li>vpc:securityGroups:get</li></ul>
</td>
</tr>
<tr id="row9146903301"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p1796033203011"><a name="p1796033203011"></a><a name="p1796033203011"></a>POST /v2/{project_id}/os-security-group-rules</p>
<p id="p15127771327"><a name="p15127771327"></a><a name="p15127771327"></a>POST /v2.1/{project_id}/os-security-group-rules</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p20101421114212"><a name="p20101421114212"></a><a name="p20101421114212"></a>Creating a Security Group Rule (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul196063215305"></a><a name="ul196063215305"></a><ul id="ul196063215305"><li>ecs:securityGroups:use</li></ul>
<a name="ul12960193215307"></a><a name="ul12960193215307"></a><ul id="ul12960193215307"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:update</li><li>vpc:securityGroupRules:get</li><li>vpc:securityGroupRules:create</li></ul>
</td>
</tr>
<tr id="row19146707308"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p89601432143014"><a name="p89601432143014"></a><a name="p89601432143014"></a>DELETE /v2/{project_id}/os-security-group-rules/{security_group_rule_id}</p>
<p id="p554073153218"><a name="p554073153218"></a><a name="p554073153218"></a>DELETE /v2.1/{project_id}/os-security-group-rules/{security_group_rule_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p161062164211"><a name="p161062164211"></a><a name="p161062164211"></a>Deleting a Security Group Rule (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul1896013217300"></a><a name="ul1896013217300"></a><ul id="ul1896013217300"><li>ecs:securityGroups:use</li></ul>
<a name="ul59602032133019"></a><a name="ul59602032133019"></a><ul id="ul59602032133019"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:update</li><li>vpc:securityGroupRules:get</li><li>vpc:securityGroupRules:delete</li></ul>
</td>
</tr>
<tr id="row5146906301"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p9960932203012"><a name="p9960932203012"></a><a name="p9960932203012"></a>PUT /v2/{project_id}/os-security-groups/{security_group_id}</p>
<p id="p1623064263217"><a name="p1623064263217"></a><a name="p1623064263217"></a>PUT /v2.1/{project_id}/os-security-groups/{security_group_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p811102104214"><a name="p811102104214"></a><a name="p811102104214"></a>Updating Information About a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul189601632173011"></a><a name="ul189601632173011"></a><ul id="ul189601632173011"><li>ecs:securityGroups:use</li></ul>
<a name="ul16960153212306"></a><a name="ul16960153212306"></a><ul id="ul16960153212306"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:update</li></ul>
</td>
</tr>
<tr id="row511081915302"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p296113324304"><a name="p296113324304"></a><a name="p296113324304"></a>GET /v2/{project_id}/servers/{server_id}/os-security-groups</p>
<p id="p56631353123214"><a name="p56631353123214"></a><a name="p56631353123214"></a>GET /v2.1/{project_id}/servers/{server_id}/os-security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p101132114219"><a name="p101132114219"></a><a name="p101132114219"></a>Querying Security Groups to Which an ECS Belongs (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul69612324300"></a><a name="ul69612324300"></a><ul id="ul69612324300"><li>ecs:securityGroups:use</li></ul>
<a name="ul17961143212308"></a><a name="ul17961143212308"></a><ul id="ul17961143212308"><li>vpc:securityGroups:get</li></ul>
</td>
</tr>
<tr id="row41101119143010"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p296133223013"><a name="p296133223013"></a><a name="p296133223013"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p99431459183215"><a name="p99431459183215"></a><a name="p99431459183215"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p81112111424"><a name="p81112111424"></a><a name="p81112111424"></a>Adding a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul1796133213309"></a><a name="ul1796133213309"></a><ul id="ul1796133213309"><li>ecs:securityGroups:use</li><li>ecs:servers:get</li></ul>
<a name="ul16961133293017"></a><a name="ul16961133293017"></a><ul id="ul16961133293017"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:create</li><li>vpc:securityGroups:update</li><li>vpc:ports:get</li><li>vpc:ports:update</li></ul>
</td>
</tr>
<tr id="row51102019153019"><td class="cellrowborder" valign="top" width="31.175124512047383%" headers="mcps1.1.4.1.1 "><p id="p1596133211307"><a name="p1596133211307"></a><a name="p1596133211307"></a>POST /v2/{project_id}/servers/{server_id}/action</p>
<p id="p54371318143319"><a name="p54371318143319"></a><a name="p54371318143319"></a>POST /v2.1/{project_id}/servers/{server_id}/action</p>
</td>
<td class="cellrowborder" valign="top" width="30.448243370574772%" headers="mcps1.1.4.1.2 "><p id="p161172134216"><a name="p161172134216"></a><a name="p161172134216"></a>Removing a Security Group (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="38.376632117377845%" headers="mcps1.1.4.1.3 "><a name="ul59611132123017"></a><a name="ul59611132123017"></a><ul id="ul59611132123017"><li>ecs:securityGroups:use</li><li>ecs:servers:get</li></ul>
<a name="ul199611432183017"></a><a name="ul199611432183017"></a><ul id="ul199611432183017"><li>vpc:securityGroups:get</li><li>vpc:securityGroups:delete</li><li>vpc:securityGroups:update</li><li>vpc:ports:get</li><li>vpc:ports:update</li></ul>
</td>
</tr>
</tbody>
</table>

