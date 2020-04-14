# Router \(OpenStack Neutron API\)<a name="vpc_permission_0013"></a>

<a name="table12370152544218"></a>
<table><thead align="left"><tr id="row54522258420"><th class="cellrowborder" valign="top" width="47.369863013698634%" id="mcps1.1.4.1.1"><p id="p14452192514212"><a name="p14452192514212"></a><a name="p14452192514212"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="21.123287671232877%" id="mcps1.1.4.1.2"><p id="p12397123817417"><a name="p12397123817417"></a><a name="p12397123817417"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="31.506849315068497%" id="mcps1.1.4.1.3"><p id="p15453152544217"><a name="p15453152544217"></a><a name="p15453152544217"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row184535258423"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p18453152554210"><a name="p18453152554210"></a><a name="p18453152554210"></a>GET /v2.0/routers</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p739783814417"><a name="p739783814417"></a><a name="p739783814417"></a>Queries routers.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><p id="p155319335423"><a name="p155319335423"></a><a name="p155319335423"></a>vpc:routers:get</p>
</td>
</tr>
<tr id="row745342513426"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p345362534211"><a name="p345362534211"></a><a name="p345362534211"></a>GET /v2.0/routers/{router_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p153978386410"><a name="p153978386410"></a><a name="p153978386410"></a>Queries a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><p id="p5859534164219"><a name="p5859534164219"></a><a name="p5859534164219"></a>vpc:routers:get</p>
</td>
</tr>
<tr id="row54531525184217"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p15453925114210"><a name="p15453925114210"></a><a name="p15453925114210"></a>POST /v2.0/routers</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p103976387420"><a name="p103976387420"></a><a name="p103976387420"></a>Creates a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><p id="p2990735114210"><a name="p2990735114210"></a><a name="p2990735114210"></a>vpc:routers:create</p>
</td>
</tr>
<tr id="row174531925144217"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p84531425114218"><a name="p84531425114218"></a><a name="p84531425114218"></a>PUT /v2.0/routers/{router_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p1139718381747"><a name="p1139718381747"></a><a name="p1139718381747"></a>Updates a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><p id="p1124333711420"><a name="p1124333711420"></a><a name="p1124333711420"></a>vpc:routers:update</p>
</td>
</tr>
<tr id="row1345318250425"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p1045312259426"><a name="p1045312259426"></a><a name="p1045312259426"></a>DELETE /v2.0/routers/{router_id}</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p143970384417"><a name="p143970384417"></a><a name="p143970384417"></a>Deletes a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><p id="p1094017388427"><a name="p1094017388427"></a><a name="p1094017388427"></a>vpc:routers:delete</p>
</td>
</tr>
<tr id="row545315256423"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p1045312515428"><a name="p1045312515428"></a><a name="p1045312515428"></a>PUT /v2.0/routers/{router_id}/add_router_interface</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p1339716386413"><a name="p1339716386413"></a><a name="p1339716386413"></a>Adds an interface to a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><a name="ul15454162520421"></a><a name="ul15454162520421"></a><ul id="ul15454162520421"><li>vpc:routers:addInterface</li><li>vpc:routers:get</li></ul>
</td>
</tr>
<tr id="row145472554213"><td class="cellrowborder" valign="top" width="47.369863013698634%" headers="mcps1.1.4.1.1 "><p id="p1745412518421"><a name="p1745412518421"></a><a name="p1745412518421"></a>PUT /v2.0/routers/{router_id}/remove_router_interface</p>
</td>
<td class="cellrowborder" valign="top" width="21.123287671232877%" headers="mcps1.1.4.1.2 "><p id="p1539712389410"><a name="p1539712389410"></a><a name="p1539712389410"></a>Removes an interface from a router.</p>
</td>
<td class="cellrowborder" valign="top" width="31.506849315068497%" headers="mcps1.1.4.1.3 "><a name="ul18454122574216"></a><a name="ul18454122574216"></a><ul id="ul18454122574216"><li>vpc:routers:removeInterface</li><li>vpc:routers:get</li></ul>
</td>
</tr>
</tbody>
</table>

