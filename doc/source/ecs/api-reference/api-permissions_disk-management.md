# Disk Management<a name="EN-US_TOPIC_0103071514"></a>

<a name="table88951955182420"></a>
<table><thead align="left"><tr id="row2670183317019"><th class="cellrowborder" valign="top" width="31.738942515487683%" id="mcps1.1.4.1.1"><p id="p1567220502233"><a name="p1567220502233"></a><a name="p1567220502233"></a>APIs</p>
</th>
<th class="cellrowborder" valign="top" width="32.07030687220861%" id="mcps1.1.4.1.2"><p id="p10605125713535"><a name="p10605125713535"></a><a name="p10605125713535"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="36.1907506123037%" id="mcps1.1.4.1.3"><p id="p93075832319"><a name="p93075832319"></a><a name="p93075832319"></a>Actions</p>
</th>
</tr>
</thead>
<tbody><tr id="row1893621632116"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p865419331215"><a name="p865419331215"></a><a name="p865419331215"></a>DELETE /v1/{project_id}/cloudservers/{server_id}/detachvolume/{attachment_id}</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p0893123616432"><a name="p0893123616432"></a><a name="p0893123616432"></a>Detaching a Disk from a Specified ECS</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul86541333202118"></a><a name="ul86541333202118"></a><ul id="ul86541333202118"><li>ecs:cloudServers:detachVolume</li></ul>
</td>
</tr>
<tr id="row15734520162118"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p3654133142110"><a name="p3654133142110"></a><a name="p3654133142110"></a>POST /v1/{project_id}/cloudservers/{server_id}/attachvolume</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p989316367430"><a name="p989316367430"></a><a name="p989316367430"></a>Attaching a Disk to an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul16654183313217"></a><a name="ul16654183313217"></a><ul id="ul16654183313217"><li>ecs:cloudServers:attach</li></ul>
</td>
</tr>
<tr id="row18432110194915"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p14854133274912"><a name="p14854133274912"></a><a name="p14854133274912"></a>POST /v2/{project_id}/servers/{server_id}/os-volume_attachments</p>
<p id="p14236125619354"><a name="p14236125619354"></a><a name="p14236125619354"></a>POST /v2.1/{project_id}/servers/{server_id}/os-volume_attachments</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p16854163215491"><a name="p16854163215491"></a><a name="p16854163215491"></a>Attaching a Disk to an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul9854832114918"></a><a name="ul9854832114918"></a><ul id="ul9854832114918"><li>ecs:serverVolumeAttachments:create</li><li>ecs:serverVolumes:use</li></ul>
<a name="ul19854153254917"></a><a name="ul19854153254917"></a><ul id="ul19854153254917"><li>evs:volumes:list</li><li>evs:volumes:get</li><li>evs:volumes:update</li><li>evs:volumes:attach</li><li>evs:volumes:manage</li></ul>
</td>
</tr>
<tr id="row74321703496"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p1785543254911"><a name="p1785543254911"></a><a name="p1785543254911"></a>DELETE /v2/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}</p>
<p id="p1297435133610"><a name="p1297435133610"></a><a name="p1297435133610"></a>DELETE /v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p12855432154911"><a name="p12855432154911"></a><a name="p12855432154911"></a>Detaching a Disk from an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul1985513327496"></a><a name="ul1985513327496"></a><ul id="ul1985513327496"><li>ecs:serverVolumeAttachments:delete</li><li>ecs:serverVolumes:use</li></ul>
<a name="ul18551322491"></a><a name="ul18551322491"></a><ul id="ul18551322491"><li>evs:volumes:list</li><li>evs:volumes:get</li><li>evs:volumes:update</li><li>evs:volumes:detach</li><li>evs:volumes:manage</li></ul>
</td>
</tr>
<tr id="row74328064918"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p68561032144910"><a name="p68561032144910"></a><a name="p68561032144910"></a>GET /v2/{project_id}/servers/{server_id}/os-volume_attachments</p>
<p id="p260410182367"><a name="p260410182367"></a><a name="p260410182367"></a>GET /v2.1/{project_id}/servers/{server_id}/os-volume_attachments</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p17856332134918"><a name="p17856332134918"></a><a name="p17856332134918"></a>Querying Information About the Disks Attached to an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul14856183244920"></a><a name="ul14856183244920"></a><ul id="ul14856183244920"><li>ecs:serverVolumeAttachments:list</li><li>ecs:serverVolumes:use</li><li>ecs:servers:get</li></ul>
</td>
</tr>
<tr id="row1434619574918"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p138567323496"><a name="p138567323496"></a><a name="p138567323496"></a>GET /v2/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}</p>
<p id="p15134624103611"><a name="p15134624103611"></a><a name="p15134624103611"></a>GET /v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p7856103211494"><a name="p7856103211494"></a><a name="p7856103211494"></a>Querying Information About a Disk Attached to an ECS (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul5857132104912"></a><a name="ul5857132104912"></a><ul id="ul5857132104912"><li>ecs:serverVolumeAttachments:get</li><li>ecs:serverVolumes:use</li></ul>
</td>
</tr>
<tr id="row1976111120493"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p148571432194918"><a name="p148571432194918"></a><a name="p148571432194918"></a>POST /v2/{project_id}/os-volumes</p>
<p id="p6189165412361"><a name="p6189165412361"></a><a name="p6189165412361"></a>POST /v2.1/{project_id}/os-volumes</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p16857183219496"><a name="p16857183219496"></a><a name="p16857183219496"></a>Creating a Disk (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul13857732194912"></a><a name="ul13857732194912"></a><ul id="ul13857732194912"><li>ecs:serverVolumes:use</li></ul>
<a name="ul585743217493"></a><a name="ul585743217493"></a><ul id="ul585743217493"><li>evs:volumes:create</li></ul>
</td>
</tr>
<tr id="row14762113499"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p168571532144916"><a name="p168571532144916"></a><a name="p168571532144916"></a>DELETE /v2/{project_id}/os-volumes/{volume_id}</p>
<p id="p20452165923617"><a name="p20452165923617"></a><a name="p20452165923617"></a>DELETE /v2.1/{project_id}/os-volumes/{volume_id}</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p14858153214493"><a name="p14858153214493"></a><a name="p14858153214493"></a>Deleting a Disk (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul485893264919"></a><a name="ul485893264919"></a><ul id="ul485893264919"><li>ecs:serverVolumes:use</li></ul>
<a name="ul1185803217490"></a><a name="ul1185803217490"></a><ul id="ul1185803217490"><li>evs:volumes:get</li><li>evs:volumes:delete</li></ul>
</td>
</tr>
<tr id="row97710116497"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p198589328499"><a name="p198589328499"></a><a name="p198589328499"></a>GET /v2/{project_id}/os-volumes/{volume_id}</p>
<p id="p179594113716"><a name="p179594113716"></a><a name="p179594113716"></a>GET /v2.1/{project_id}/os-volumes/{volume_id}</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p12858932104910"><a name="p12858932104910"></a><a name="p12858932104910"></a>Querying a Disk (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul188581532104917"></a><a name="ul188581532104917"></a><ul id="ul188581532104917"><li>ecs:serverVolumes:use</li></ul>
<a name="ul1858183274913"></a><a name="ul1858183274913"></a><ul id="ul1858183274913"><li>evs:volumes:get</li></ul>
</td>
</tr>
<tr id="row37741114911"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p947117562504"><a name="p947117562504"></a><a name="p947117562504"></a>GET /v2/{project_id}/os-volumes</p>
<p id="p984217813370"><a name="p984217813370"></a><a name="p984217813370"></a>GET /v2.1/{project_id}/os-volumes</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p1447115611501"><a name="p1447115611501"></a><a name="p1447115611501"></a>Querying Disks (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul94711356155014"></a><a name="ul94711356155014"></a><ul id="ul94711356155014"><li>ecs:serverVolumes:use</li></ul>
<a name="ul44711756105016"></a><a name="ul44711756105016"></a><ul id="ul44711756105016"><li>evs:volumes:get</li><li>evs:volumes:list</li></ul>
</td>
</tr>
<tr id="row43471056491"><td class="cellrowborder" valign="top" width="31.738942515487683%" headers="mcps1.1.4.1.1 "><p id="p164711856145011"><a name="p164711856145011"></a><a name="p164711856145011"></a>GET /v2/{project_id}/os-volumes/detail</p>
<p id="p1125381323710"><a name="p1125381323710"></a><a name="p1125381323710"></a>GET /v2.1/{project_id}/os-volumes/detail</p>
</td>
<td class="cellrowborder" valign="top" width="32.07030687220861%" headers="mcps1.1.4.1.2 "><p id="p12471115618504"><a name="p12471115618504"></a><a name="p12471115618504"></a>Querying Detailed Disk Information (Native OpenStack API)</p>
</td>
<td class="cellrowborder" valign="top" width="36.1907506123037%" headers="mcps1.1.4.1.3 "><a name="ul647118564506"></a><a name="ul647118564506"></a><ul id="ul647118564506"><li>ecs:serverVolumes:use</li></ul>
<a name="ul6471155645012"></a><a name="ul6471155645012"></a><ul id="ul6471155645012"><li>evs:volumes:get</li><li>evs:volumes:list</li></ul>
</td>
</tr>
</tbody>
</table>

