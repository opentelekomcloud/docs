# AS Group<a name="EN-US_TOPIC_0120434953"></a>

<a name="table0875101134712"></a>
<table><thead align="left"><tr id="row18876111184718"><th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.1"><p id="p87863593711"><a name="p87863593711"></a><a name="p87863593711"></a><strong id="b13514161121512"><a name="b13514161121512"></a><a name="b13514161121512"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.2"><p id="p445499619223"><a name="p445499619223"></a><a name="p445499619223"></a><strong id="b17856311181510"><a name="b17856311181510"></a><a name="b17856311181510"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.1.5.1.3"><p id="p10846171016373"><a name="p10846171016373"></a><a name="p10846171016373"></a><strong id="b18911172761516"><a name="b18911172761516"></a><a name="b18911172761516"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.1.5.1.4"><p id="p143591540411"><a name="p143591540411"></a><a name="p143591540411"></a><strong id="b20533196111610"><a name="b20533196111610"></a><a name="b20533196111610"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1087651164712"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p1978805103716"><a name="p1978805103716"></a><a name="p1978805103716"></a>Creating an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p7876111124719"><a name="p7876111124719"></a><a name="p7876111124719"></a>as:groups:create</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul4585726103915"></a><a name="ul4585726103915"></a><ul id="ul4585726103915"><li>Supported:<a name="ul1990621105811"></a><a name="ul1990621105811"></a><ul id="ul1990621105811"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul358511268394"></a><a name="ul358511268394"></a><ul id="ul358511268394"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p687631194719"><a name="p687631194719"></a><a name="p687631194719"></a>POST /autoscaling-api/v1/{project_id}/scaling_group</p>
</td>
</tr>
<tr id="row1987631124714"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p778812543717"><a name="p778812543717"></a><a name="p778812543717"></a>Querying AS groups</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p198771412470"><a name="p198771412470"></a><a name="p198771412470"></a>as:groups:list</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul11596102055819"></a><a name="ul11596102055819"></a><ul id="ul11596102055819"><li>Supported:<a name="ul2059892013582"></a><a name="ul2059892013582"></a><ul id="ul2059892013582"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul86001920205812"></a><a name="ul86001920205812"></a><ul id="ul86001920205812"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p12876214478"><a name="p12876214478"></a><a name="p12876214478"></a>GET /autoscaling-api/v1/{project_id}/scaling_group</p>
</td>
</tr>
<tr id="row15877416470"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p19788858377"><a name="p19788858377"></a><a name="p19788858377"></a>Querying AS group details</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p1987714114710"><a name="p1987714114710"></a><a name="p1987714114710"></a>as:groups:get</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul153755253588"></a><a name="ul153755253588"></a><ul id="ul153755253588"><li>Supported:<a name="ul14376825125812"></a><a name="ul14376825125812"></a><ul id="ul14376825125812"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul83791325125818"></a><a name="ul83791325125818"></a><ul id="ul83791325125818"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p198779104712"><a name="p198779104712"></a><a name="p198779104712"></a>GET /autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}</p>
</td>
</tr>
<tr id="row13877101184716"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p187881516379"><a name="p187881516379"></a><a name="p187881516379"></a>Modifying an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p48771184715"><a name="p48771184715"></a><a name="p48771184715"></a>as:groups:update</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul148141132115812"></a><a name="ul148141132115812"></a><ul id="ul148141132115812"><li>Supported:<a name="ul681413326589"></a><a name="ul681413326589"></a><ul id="ul681413326589"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul13818173215812"></a><a name="ul13818173215812"></a><ul id="ul13818173215812"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p78771214472"><a name="p78771214472"></a><a name="p78771214472"></a>PUT /autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}</p>
</td>
</tr>
<tr id="row987713116474"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p0788175103715"><a name="p0788175103715"></a><a name="p0788175103715"></a>Deleting an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p13877719474"><a name="p13877719474"></a><a name="p13877719474"></a>as:groups:delete</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul9523136145820"></a><a name="ul9523136145820"></a><ul id="ul9523136145820"><li>Supported:<a name="ul652473610588"></a><a name="ul652473610588"></a><ul id="ul652473610588"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul852693619589"></a><a name="ul852693619589"></a><ul id="ul852693619589"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p14877813478"><a name="p14877813478"></a><a name="p14877813478"></a>DELETE /autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}</p>
</td>
</tr>
<tr id="row287761164713"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.1 "><p id="p67888518378"><a name="p67888518378"></a><a name="p67888518378"></a>Enabling or disabling an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.2 "><p id="p987731144714"><a name="p987731144714"></a><a name="p987731144714"></a>as:groups:action</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><a name="ul159418416586"></a><a name="ul159418416586"></a><ul id="ul159418416586"><li>Supported:<a name="ul12943144113582"></a><a name="ul12943144113582"></a><ul id="ul12943144113582"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul14945174175813"></a><a name="ul14945174175813"></a><ul id="ul14945174175813"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="p787741104720"><a name="p787741104720"></a><a name="p787741104720"></a>POST /autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}/action</p>
</td>
</tr>
</tbody>
</table>

