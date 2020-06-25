# AS Configuration<a name="EN-US_TOPIC_0120434954"></a>

<a name="table6521155717015"></a>
<table><thead align="left"><tr id="row452275718014"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.5.1.1"><p id="p4205119652"><a name="p4205119652"></a><a name="p4205119652"></a><strong id="b18880124310154"><a name="b18880124310154"></a><a name="b18880124310154"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.262626262626267%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b17493175013156"><a name="b17493175013156"></a><a name="b17493175013156"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.323232323232325%" id="mcps1.1.5.1.3"><p id="p1841555914555"><a name="p1841555914555"></a><a name="p1841555914555"></a><strong id="b4938205361512"><a name="b4938205361512"></a><a name="b4938205361512"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.4"><p id="p135221579017"><a name="p135221579017"></a><a name="p135221579017"></a><strong id="b1166121131613"><a name="b1166121131613"></a><a name="b1166121131613"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row0522357809"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="p1946563550"><a name="p1946563550"></a><a name="p1946563550"></a>Creating an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="p145221571705"><a name="p145221571705"></a><a name="p145221571705"></a>as:configs:create</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.1.5.1.3 "><a name="ul19673454131111"></a><a name="ul19673454131111"></a><ul id="ul19673454131111"><li>Supported:<a name="ul1467414544117"></a><a name="ul1467414544117"></a><ul id="ul1467414544117"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul166751547118"></a><a name="ul166751547118"></a><ul id="ul166751547118"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.4 "><p id="p352285710017"><a name="p352285710017"></a><a name="p352285710017"></a>POST /autoscaling-api/v1/{project_id}/scaling_configuration</p>
</td>
</tr>
<tr id="row0522185711019"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="p1794105610551"><a name="p1794105610551"></a><a name="p1794105610551"></a>Querying AS configurations</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="p11522175713011"><a name="p11522175713011"></a><a name="p11522175713011"></a>as:configs:list</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.1.5.1.3 "><a name="ul1354014322815"></a><a name="ul1354014322815"></a><ul id="ul1354014322815"><li>Supported:<a name="ul65413430285"></a><a name="ul65413430285"></a><ul id="ul65413430285"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul254354317282"></a><a name="ul254354317282"></a><ul id="ul254354317282"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.4 "><p id="p1352235715016"><a name="p1352235715016"></a><a name="p1352235715016"></a>GET /autoscaling-api/v1/{project_id}/scaling_configuration</p>
</td>
</tr>
<tr id="row15225577015"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="p19445655518"><a name="p19445655518"></a><a name="p19445655518"></a>Querying AS configuration details</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="p2522857407"><a name="p2522857407"></a><a name="p2522857407"></a>as:configs:get</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.1.5.1.3 "><a name="ul66831047122810"></a><a name="ul66831047122810"></a><ul id="ul66831047122810"><li>Supported:<a name="ul46841447112812"></a><a name="ul46841447112812"></a><ul id="ul46841447112812"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul468712474282"></a><a name="ul468712474282"></a><ul id="ul468712474282"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.4 "><p id="p1052245712017"><a name="p1052245712017"></a><a name="p1052245712017"></a>GET /autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}</p>
</td>
</tr>
<tr id="row55221457205"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="p194125615552"><a name="p194125615552"></a><a name="p194125615552"></a>Deleting an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="p1552216578017"><a name="p1552216578017"></a><a name="p1552216578017"></a>as:configs:delete</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.1.5.1.3 "><a name="ul1467110511285"></a><a name="ul1467110511285"></a><ul id="ul1467110511285"><li>Supported:<a name="ul5673165152819"></a><a name="ul5673165152819"></a><ul id="ul5673165152819"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1967412514289"></a><a name="ul1967412514289"></a><ul id="ul1967412514289"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.4 "><p id="p1152285711014"><a name="p1152285711014"></a><a name="p1152285711014"></a>DELETE /autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}</p>
</td>
</tr>
<tr id="row201240287115"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="p49414560559"><a name="p49414560559"></a><a name="p49414560559"></a>Batch deleting AS configurations</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="p1312516282116"><a name="p1312516282116"></a><a name="p1312516282116"></a>as:configs:batchDelete</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.1.5.1.3 "><a name="ul181485552810"></a><a name="ul181485552810"></a><ul id="ul181485552810"><li>Supported:<a name="ul18142559282"></a><a name="ul18142559282"></a><ul id="ul18142559282"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul18166556281"></a><a name="ul18166556281"></a><ul id="ul18166556281"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.4 "><p id="p612562817118"><a name="p612562817118"></a><a name="p612562817118"></a>POST /autoscaling-api/v1/{project_id}/scaling_configurations</p>
</td>
</tr>
</tbody>
</table>

