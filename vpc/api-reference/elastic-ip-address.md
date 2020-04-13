# Elastic IP Address<a name="vpc_permission_0002"></a>

<a name="table3381441153612"></a>
<table><thead align="left"><tr id="row134361241153612"><th class="cellrowborder" valign="top" width="47.88732394366197%" id="mcps1.1.4.1.1"><p id="p24367414363"><a name="p24367414363"></a><a name="p24367414363"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="30.985915492957744%" id="mcps1.1.4.1.2"><p id="p423285813514"><a name="p423285813514"></a><a name="p423285813514"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="21.12676056338028%" id="mcps1.1.4.1.3"><p id="p2436194193616"><a name="p2436194193616"></a><a name="p2436194193616"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row943674133617"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="p144365416368"><a name="p144365416368"></a><a name="p144365416368"></a>POST /v1/{project_id}/publicips</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="p13232958145117"><a name="p13232958145117"></a><a name="p13232958145117"></a>Assigns an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="p17904175011365"><a name="p17904175011365"></a><a name="p17904175011365"></a>vpc:publicIps:create</p>
</td>
</tr>
<tr id="row343704173619"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="p174371341133618"><a name="p174371341133618"></a><a name="p174371341133618"></a>GET /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="p1623218589512"><a name="p1623218589512"></a><a name="p1623218589512"></a>Queries an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="p8360152113611"><a name="p8360152113611"></a><a name="p8360152113611"></a>vpc:publicIps:get</p>
</td>
</tr>
<tr id="row34371241143616"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="p16437174193619"><a name="p16437174193619"></a><a name="p16437174193619"></a>GET /v1/{project_id}/publicips</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="p182321558155116"><a name="p182321558155116"></a><a name="p182321558155116"></a>Queries EIPs.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="p35961753143612"><a name="p35961753143612"></a><a name="p35961753143612"></a>vpc:publicIps:list</p>
</td>
</tr>
<tr id="row443713412363"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="p4437194193614"><a name="p4437194193614"></a><a name="p4437194193614"></a>PUT /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="p623295805113"><a name="p623295805113"></a><a name="p623295805113"></a>Updates an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="p1060705413366"><a name="p1060705413366"></a><a name="p1060705413366"></a>vpc:publicIps:update</p>
</td>
</tr>
<tr id="row10437144143617"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="p2437114115362"><a name="p2437114115362"></a><a name="p2437114115362"></a>DELETE /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="p923213587517"><a name="p923213587517"></a><a name="p923213587517"></a>Releases an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="p986195516362"><a name="p986195516362"></a><a name="p986195516362"></a>vpc:publicIps:delete</p>
</td>
</tr>
</tbody>
</table>

