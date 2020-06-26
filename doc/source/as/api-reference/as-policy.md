# AS Policy<a name="EN-US_TOPIC_0120434956"></a>

<a name="table1169817313568"></a>
<table><thead align="left"><tr id="row1669883115561"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.1.5.1.1"><p id="p57088391710"><a name="p57088391710"></a><a name="p57088391710"></a><strong id="b1788213392168"><a name="b1788213392168"></a><a name="b1788213392168"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.2"><p id="p17522185717013"><a name="p17522185717013"></a><a name="p17522185717013"></a><strong id="b14103124271614"><a name="b14103124271614"></a><a name="b14103124271614"></a>Actions</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.1.5.1.3"><p id="p36609120137"><a name="p36609120137"></a><a name="p36609120137"></a><strong id="b1551010447164"><a name="b1551010447164"></a><a name="b1551010447164"></a>Authorization Scope</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.1.5.1.4"><p id="p9124185916617"><a name="p9124185916617"></a><a name="p9124185916617"></a><strong id="b3831154571618"><a name="b3831154571618"></a><a name="b3831154571618"></a>APIs</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row126986314564"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p124818817137"><a name="p124818817137"></a><a name="p124818817137"></a>Creating an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p569833155616"><a name="p569833155616"></a><a name="p569833155616"></a>as:policies:create</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul19673454131111"></a><a name="ul19673454131111"></a><ul id="ul19673454131111"><li>Supported:<a name="ul1467414544117"></a><a name="ul1467414544117"></a><ul id="ul1467414544117"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul166751547118"></a><a name="ul166751547118"></a><ul id="ul166751547118"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p11698931175612"><a name="p11698931175612"></a><a name="p11698931175612"></a>POST /autoscaling-api/v1/{project_id}/scaling_policy</p>
</td>
</tr>
<tr id="row14698163120569"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p132487814137"><a name="p132487814137"></a><a name="p132487814137"></a>Modifying an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p669819314569"><a name="p669819314569"></a><a name="p669819314569"></a>as:policies:update</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul0561951161513"></a><a name="ul0561951161513"></a><ul id="ul0561951161513"><li>Supported:<a name="ul135825117154"></a><a name="ul135825117154"></a><ul id="ul135825117154"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul2601351121518"></a><a name="ul2601351121518"></a><ul id="ul2601351121518"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p86986312569"><a name="p86986312569"></a><a name="p86986312569"></a>PUT /autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}</p>
</td>
</tr>
<tr id="row1069863195615"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p824813812135"><a name="p824813812135"></a><a name="p824813812135"></a>Querying AS policies</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p1269893119568"><a name="p1269893119568"></a><a name="p1269893119568"></a>as:policies:list</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul97965417158"></a><a name="ul97965417158"></a><ul id="ul97965417158"><li>Supported:<a name="ul1881195410154"></a><a name="ul1881195410154"></a><ul id="ul1881195410154"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1584754161519"></a><a name="ul1584754161519"></a><ul id="ul1584754161519"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p20698731115613"><a name="p20698731115613"></a><a name="p20698731115613"></a>GET /autoscaling-api/v1/{project_id}/scaling_policy/{scaling_group_id}/list</p>
</td>
</tr>
<tr id="row369863111566"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p12248158151311"><a name="p12248158151311"></a><a name="p12248158151311"></a>Querying AS policy details</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p8698183135619"><a name="p8698183135619"></a><a name="p8698183135619"></a>as:policies:get</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul1791955521519"></a><a name="ul1791955521519"></a><ul id="ul1791955521519"><li>Supported:<a name="ul69213551159"></a><a name="ul69213551159"></a><ul id="ul69213551159"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul59241555191513"></a><a name="ul59241555191513"></a><ul id="ul59241555191513"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p106981631175618"><a name="p106981631175618"></a><a name="p106981631175618"></a>GET /autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}</p>
</td>
</tr>
<tr id="row1269843120568"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p1124819851317"><a name="p1124819851317"></a><a name="p1124819851317"></a>Executing, enabling, or disabling an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p2069813165620"><a name="p2069813165620"></a><a name="p2069813165620"></a>as:policies:action</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul8389115813152"></a><a name="ul8389115813152"></a><ul id="ul8389115813152"><li>Supported:<a name="ul6390155821518"></a><a name="ul6390155821518"></a><ul id="ul6390155821518"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul4393158131519"></a><a name="ul4393158131519"></a><ul id="ul4393158131519"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p17698153111564"><a name="p17698153111564"></a><a name="p17698153111564"></a>POST /autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}/action</p>
</td>
</tr>
<tr id="row3698431185616"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p112496819132"><a name="p112496819132"></a><a name="p112496819132"></a>Deleting an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p12698131195614"><a name="p12698131195614"></a><a name="p12698131195614"></a>as:policies:delete</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul685881111620"></a><a name="ul685881111620"></a><ul id="ul685881111620"><li>Supported:<a name="ul19859191121610"></a><a name="ul19859191121610"></a><ul id="ul19859191121610"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul188621714161"></a><a name="ul188621714161"></a><ul id="ul188621714161"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p46981831205611"><a name="p46981831205611"></a><a name="p46981831205611"></a>DELETE /autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}</p>
</td>
</tr>
<tr id="row1269873165613"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p122493821312"><a name="p122493821312"></a><a name="p122493821312"></a>Creating an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p1869863111562"><a name="p1869863111562"></a><a name="p1869863111562"></a>as:policies:create</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul1228018457215"></a><a name="ul1228018457215"></a><ul id="ul1228018457215"><li>Supported:<p id="p1328194519210"><a name="p1328194519210"></a><a name="p1328194519210"></a>Project</p>
</li></ul>
<a name="ul1728210451429"></a><a name="ul1728210451429"></a><ul id="ul1728210451429"><li>Unsupported:<p id="p14284164515217"><a name="p14284164515217"></a><a name="p14284164515217"></a>Enterprise project</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p16698183111564"><a name="p16698183111564"></a><a name="p16698183111564"></a>POST /autoscaling-api/v2/{project_id}/scaling_policy</p>
</td>
</tr>
<tr id="row1569843113565"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p4249781138"><a name="p4249781138"></a><a name="p4249781138"></a>Modifying an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p1669883113567"><a name="p1669883113567"></a><a name="p1669883113567"></a>as:policies:update</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul164564962918"></a><a name="ul164564962918"></a><ul id="ul164564962918"><li>Supported:<a name="ul1646144932913"></a><a name="ul1646144932913"></a><ul id="ul1646144932913"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul8650174912295"></a><a name="ul8650174912295"></a><ul id="ul8650174912295"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p186981331175620"><a name="p186981331175620"></a><a name="p186981331175620"></a>PUT /autoscaling-api/v2/{project_id}/scaling_policy/{scaling_policy_id}</p>
</td>
</tr>
<tr id="row3698631195614"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p1124948161317"><a name="p1124948161317"></a><a name="p1124948161317"></a>Querying AS policies</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p196981031165619"><a name="p196981031165619"></a><a name="p196981031165619"></a>as:policies:list</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul534265312918"></a><a name="ul534265312918"></a><ul id="ul534265312918"><li>Supported:<a name="ul2344145382919"></a><a name="ul2344145382919"></a><ul id="ul2344145382919"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul23519535291"></a><a name="ul23519535291"></a><ul id="ul23519535291"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p1969810318566"><a name="p1969810318566"></a><a name="p1969810318566"></a>GET /autoscaling-api/v2/{project_id}/scaling_policy/{scaling_resource_id}/list</p>
</td>
</tr>
<tr id="row1047211305165"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p885514016169"><a name="p885514016169"></a><a name="p885514016169"></a>Querying AS policies</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p125127513217"><a name="p125127513217"></a><a name="p125127513217"></a>as:groups:get</p>
<p id="p138561040111617"><a name="p138561040111617"></a><a name="p138561040111617"></a>as:policies:list</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul1888125611292"></a><a name="ul1888125611292"></a><ul id="ul1888125611292"><li>Supported:<a name="ul0883195613294"></a><a name="ul0883195613294"></a><ul id="ul0883195613294"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul118861056172919"></a><a name="ul118861056172919"></a><ul id="ul118861056172919"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p497022510534"><a name="p497022510534"></a><a name="p497022510534"></a>GET /autoscaling-api/v2/{project_id}/scaling_policy{? scaling_resource_id, scaling_resource_type ,scaling_policy_name, scaling_policy_id,scaling_policy_type,start_number,limit,sort_by,order,enterprise_project_id}</p>
</td>
</tr>
<tr id="row669853195615"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p62494815132"><a name="p62494815132"></a><a name="p62494815132"></a>Querying AS policy details</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p1169853145613"><a name="p1169853145613"></a><a name="p1169853145613"></a>as:policies:get</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul1140330183014"></a><a name="ul1140330183014"></a><ul id="ul1140330183014"><li>Supported:<a name="ul114070014306"></a><a name="ul114070014306"></a><ul id="ul114070014306"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul18410160103010"></a><a name="ul18410160103010"></a><ul id="ul18410160103010"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p9698113115563"><a name="p9698113115563"></a><a name="p9698113115563"></a>GET /autoscaling-api/v2/{project_id}/scaling_policy/{scaling_policy_id}</p>
<p id="p83161735163419"><a name="p83161735163419"></a><a name="p83161735163419"></a>s</p>
</td>
</tr>
<tr id="row56513461142"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p72491587135"><a name="p72491587135"></a><a name="p72491587135"></a>Performing operations on AS policies in batches</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p265184619417"><a name="p265184619417"></a><a name="p265184619417"></a>as:policies:batchAction</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.1.5.1.3 "><a name="ul1964063113014"></a><a name="ul1964063113014"></a><ul id="ul1964063113014"><li>Supported:<a name="ul3642183173016"></a><a name="ul3642183173016"></a><ul id="ul3642183173016"><li>Project</li><li>Enterprise project</li></ul>
</li></ul>
<a name="ul1064683183014"></a><a name="ul1064683183014"></a><ul id="ul1064683183014"><li>Unsupported: none</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.1.5.1.4 "><p id="p665115468416"><a name="p665115468416"></a><a name="p665115468416"></a>POST /autoscaling-api/v1/{project_id}/scaling_policies/action</p>
</td>
</tr>
</tbody>
</table>

