# Batch Operations<a name="EN-US_TOPIC_0184167662"></a>

<a name="table1587111571724"></a>
<table><thead align="left"><tr id="row20307121620133"><th class="cellrowborder" valign="top" width="33.68533823079278%" id="mcps1.1.4.1.1"><p id="p72571745883"><a name="p72571745883"></a><a name="p72571745883"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="28.221610039791862%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="38.093051729415365%" id="mcps1.1.4.1.3"><p id="p162571745883"><a name="p162571745883"></a><a name="p162571745883"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row137611507177"><td class="cellrowborder" valign="top" width="33.68533823079278%" headers="mcps1.1.4.1.1 "><p id="p1479123111913"><a name="p1479123111913"></a><a name="p1479123111913"></a>POST /v1/{project_id}/cloudservers/action</p>
</td>
<td class="cellrowborder" valign="top" width="28.221610039791862%" headers="mcps1.1.4.1.2 "><p id="p138621244115117"><a name="p138621244115117"></a><a name="p138621244115117"></a>Stopping ECSs in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="38.093051729415365%" headers="mcps1.1.4.1.3 "><a name="ul1747923181916"></a><a name="ul1747923181916"></a><ul id="ul1747923181916"><li>ecs:cloudServers:stop</li></ul>
</td>
</tr>
<tr id="row17373916184"><td class="cellrowborder" valign="top" width="33.68533823079278%" headers="mcps1.1.4.1.1 "><p id="p78289223194"><a name="p78289223194"></a><a name="p78289223194"></a>POST /v1/{project_id}/cloudservers/action</p>
</td>
<td class="cellrowborder" valign="top" width="28.221610039791862%" headers="mcps1.1.4.1.2 "><p id="p086234415116"><a name="p086234415116"></a><a name="p086234415116"></a>Restarting ECSs in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="38.093051729415365%" headers="mcps1.1.4.1.3 "><a name="ul78281922151917"></a><a name="ul78281922151917"></a><ul id="ul78281922151917"><li>ecs:cloudServers:reboot</li></ul>
</td>
</tr>
<tr id="row293217122187"><td class="cellrowborder" valign="top" width="33.68533823079278%" headers="mcps1.1.4.1.1 "><p id="p138281922141912"><a name="p138281922141912"></a><a name="p138281922141912"></a>POST /v1/{project_id}/cloudservers/action</p>
</td>
<td class="cellrowborder" valign="top" width="28.221610039791862%" headers="mcps1.1.4.1.2 "><p id="p10531190133710"><a name="p10531190133710"></a><a name="p10531190133710"></a>Starting ECSs in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="38.093051729415365%" headers="mcps1.1.4.1.3 "><a name="ul188281122151915"></a><a name="ul188281122151915"></a><ul id="ul188281122151915"><li>ecs:cloudServers:start</li></ul>
</td>
</tr>
<tr id="row157372392127"><td class="cellrowborder" valign="top" width="33.68533823079278%" headers="mcps1.1.4.1.1 "><p id="p1398516132315"><a name="p1398516132315"></a><a name="p1398516132315"></a>PUT /v1/{project_id}/cloudservers/server-name</p>
</td>
<td class="cellrowborder" valign="top" width="28.221610039791862%" headers="mcps1.1.4.1.2 "><p id="p1116582181319"><a name="p1116582181319"></a><a name="p1116582181319"></a>Modifying ECSs in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="38.093051729415365%" headers="mcps1.1.4.1.3 "><a name="ul14731322122418"></a><a name="ul14731322122418"></a><ul id="ul14731322122418"><li>ecs:cloudServers:put</li></ul>
</td>
</tr>
<tr id="row135911332185819"><td class="cellrowborder" valign="top" width="33.68533823079278%" headers="mcps1.1.4.1.1 "><p id="p1565303311219"><a name="p1565303311219"></a><a name="p1565303311219"></a>POST /v1/{project_id}/batchaction/attachvolumes/{volume_id}</p>
</td>
<td class="cellrowborder" valign="top" width="28.221610039791862%" headers="mcps1.1.4.1.2 "><p id="p2089333617435"><a name="p2089333617435"></a><a name="p2089333617435"></a>Attaching a Specified Shared EVS Disk to Multiple ECSs in a Batch</p>
</td>
<td class="cellrowborder" valign="top" width="38.093051729415365%" headers="mcps1.1.4.1.3 "><a name="ul7653113317212"></a><a name="ul7653113317212"></a><ul id="ul7653113317212"><li>ecs:cloudServers:attachSharedVolume</li><li>evs:volumes:use</li></ul>
</td>
</tr>
</tbody>
</table>

