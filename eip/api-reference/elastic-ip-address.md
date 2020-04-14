# Elastic IP Address<a name="eip_apipermission_0002"></a>

<a name="en-us_topic_0201534207_table3381441153612"></a>
<table><thead align="left"><tr id="en-us_topic_0201534207_row134361241153612"><th class="cellrowborder" valign="top" width="47.88732394366197%" id="mcps1.1.4.1.1"><p id="en-us_topic_0201534207_p24367414363"><a name="en-us_topic_0201534207_p24367414363"></a><a name="en-us_topic_0201534207_p24367414363"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="30.985915492957744%" id="mcps1.1.4.1.2"><p id="en-us_topic_0201534207_p423285813514"><a name="en-us_topic_0201534207_p423285813514"></a><a name="en-us_topic_0201534207_p423285813514"></a>API Function</p>
</th>
<th class="cellrowborder" valign="top" width="21.12676056338028%" id="mcps1.1.4.1.3"><p id="en-us_topic_0201534207_p2436194193616"><a name="en-us_topic_0201534207_p2436194193616"></a><a name="en-us_topic_0201534207_p2436194193616"></a>Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534207_row943674133617"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534207_p144365416368"><a name="en-us_topic_0201534207_p144365416368"></a><a name="en-us_topic_0201534207_p144365416368"></a>POST /v1/{project_id}/publicips</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534207_p13232958145117"><a name="en-us_topic_0201534207_p13232958145117"></a><a name="en-us_topic_0201534207_p13232958145117"></a>Assigns an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534207_p17904175011365"><a name="en-us_topic_0201534207_p17904175011365"></a><a name="en-us_topic_0201534207_p17904175011365"></a>vpc:publicIps:create</p>
</td>
</tr>
<tr id="en-us_topic_0201534207_row343704173619"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534207_p174371341133618"><a name="en-us_topic_0201534207_p174371341133618"></a><a name="en-us_topic_0201534207_p174371341133618"></a>GET /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534207_p1623218589512"><a name="en-us_topic_0201534207_p1623218589512"></a><a name="en-us_topic_0201534207_p1623218589512"></a>Queries an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534207_p8360152113611"><a name="en-us_topic_0201534207_p8360152113611"></a><a name="en-us_topic_0201534207_p8360152113611"></a>vpc:publicIps:get</p>
</td>
</tr>
<tr id="en-us_topic_0201534207_row34371241143616"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534207_p16437174193619"><a name="en-us_topic_0201534207_p16437174193619"></a><a name="en-us_topic_0201534207_p16437174193619"></a>GET /v1/{project_id}/publicips</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534207_p182321558155116"><a name="en-us_topic_0201534207_p182321558155116"></a><a name="en-us_topic_0201534207_p182321558155116"></a>Queries EIPs.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534207_p35961753143612"><a name="en-us_topic_0201534207_p35961753143612"></a><a name="en-us_topic_0201534207_p35961753143612"></a>vpc:publicIps:list</p>
</td>
</tr>
<tr id="en-us_topic_0201534207_row443713412363"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534207_p4437194193614"><a name="en-us_topic_0201534207_p4437194193614"></a><a name="en-us_topic_0201534207_p4437194193614"></a>PUT /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534207_p623295805113"><a name="en-us_topic_0201534207_p623295805113"></a><a name="en-us_topic_0201534207_p623295805113"></a>Updates an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534207_p1060705413366"><a name="en-us_topic_0201534207_p1060705413366"></a><a name="en-us_topic_0201534207_p1060705413366"></a>vpc:publicIps:update</p>
</td>
</tr>
<tr id="en-us_topic_0201534207_row10437144143617"><td class="cellrowborder" valign="top" width="47.88732394366197%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0201534207_p2437114115362"><a name="en-us_topic_0201534207_p2437114115362"></a><a name="en-us_topic_0201534207_p2437114115362"></a>DELETE /v1/{project_id}/publicips/{publicip_id}</p>
</td>
<td class="cellrowborder" valign="top" width="30.985915492957744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0201534207_p923213587517"><a name="en-us_topic_0201534207_p923213587517"></a><a name="en-us_topic_0201534207_p923213587517"></a>Releases an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="21.12676056338028%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0201534207_p986195516362"><a name="en-us_topic_0201534207_p986195516362"></a><a name="en-us_topic_0201534207_p986195516362"></a>vpc:publicIps:delete</p>
</td>
</tr>
</tbody>
</table>

