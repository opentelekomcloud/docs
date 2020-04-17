# API Actions<a name="evs_04_0045"></a>

This topic describes only the authorization information of EVS v2 APIs. For the v3 APIs that provide the same functions as their v2 APIs, their authorization information is the same as that of the v2 APIs.

For example, the v2 API for creating disks is POST /v2/\{project\_id\}/cloudvolumes, and the v3 API for creating disks is POST /v3/\{project\_id\}/cloudvolumes. The authorization information of both APIs are the same.

## API Version Query<a name="section131754192816"></a>

<a name="table1331719418287"></a>
<table><thead align="left"><tr id="row103171646287"><th class="cellrowborder" valign="top" width="32.97597520020667%" id="mcps1.1.4.1.1"><p id="p153189416282"><a name="p153189416282"></a><a name="p153189416282"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="27.52518729010592%" id="mcps1.1.4.1.2"><p id="p931834172816"><a name="p931834172816"></a><a name="p931834172816"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="39.49883750968743%" id="mcps1.1.4.1.3"><p id="p1317114142817"><a name="p1317114142817"></a><a name="p1317114142817"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row133414414280"><td class="cellrowborder" valign="top" width="32.97597520020667%" headers="mcps1.1.4.1.1 "><p id="p1934254112819"><a name="p1934254112819"></a><a name="p1934254112819"></a>Query API versions (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.52518729010592%" headers="mcps1.1.4.1.2 "><p id="p1634274142812"><a name="p1634274142812"></a><a name="p1634274142812"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="39.49883750968743%" headers="mcps1.1.4.1.3 "><p id="p43411146283"><a name="p43411146283"></a><a name="p43411146283"></a>GET /</p>
</td>
</tr>
<tr id="row734315442811"><td class="cellrowborder" valign="top" width="32.97597520020667%" headers="mcps1.1.4.1.1 "><p id="p234314411288"><a name="p234314411288"></a><a name="p234314411288"></a>Query the API version (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.52518729010592%" headers="mcps1.1.4.1.2 "><p id="p134311482810"><a name="p134311482810"></a><a name="p134311482810"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="39.49883750968743%" headers="mcps1.1.4.1.3 "><p id="p193431342281"><a name="p193431342281"></a><a name="p193431342281"></a>GET /{api_version}</p>
</td>
</tr>
</tbody>
</table>

## EVS Disk<a name="section115958429354"></a>

<a name="table277762312153"></a>
<table><thead align="left"><tr id="row1179882321511"><th class="cellrowborder" valign="top" width="33.204334365325074%" id="mcps1.1.4.1.1"><p id="p15354555517"><a name="p15354555517"></a><a name="p15354555517"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="27.489680082559335%" id="mcps1.1.4.1.2"><p id="p203145195515"><a name="p203145195515"></a><a name="p203145195515"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="39.30598555211558%" id="mcps1.1.4.1.3"><p id="p15324545520"><a name="p15324545520"></a><a name="p15324545520"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row1383192320152"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1848122310157"><a name="p1848122310157"></a><a name="p1848122310157"></a>Create EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1985372313157"><a name="p1985372313157"></a><a name="p1985372313157"></a>evs:volumes:create</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1779243531"><a name="p1779243531"></a><a name="p1779243531"></a>POST /v2/{project_id}/cloudvolumes</p>
</td>
</tr>
<tr id="row1088852331510"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p13898122341512"><a name="p13898122341512"></a><a name="p13898122341512"></a>Create EVS disks (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><a name="ul5903182315153"></a><a name="ul5903182315153"></a><ul id="ul5903182315153"><li>Create empty EVS disks.<p id="p69104235153"><a name="p69104235153"></a><a name="p69104235153"></a>evs:volumes:create</p>
<p id="p041642984516"><a name="p041642984516"></a><a name="p041642984516"></a>evs:volumes:get</p>
</li><li>Create EVS disks from images.<p id="p3918172314157"><a name="p3918172314157"></a><a name="p3918172314157"></a>evs:volumes:create</p>
<p id="p1092172361518"><a name="p1092172361518"></a><a name="p1092172361518"></a>ims:images:get</p>
<p id="p178151131194519"><a name="p178151131194519"></a><a name="p178151131194519"></a>evs:volumes:get</p>
</li><li>Create EVS disks from snapshots.<p id="p14928142361517"><a name="p14928142361517"></a><a name="p14928142361517"></a>evs:volumes:create</p>
<p id="p159301423161510"><a name="p159301423161510"></a><a name="p159301423161510"></a>evs:snapshots:get</p>
<p id="p16155205374412"><a name="p16155205374412"></a><a name="p16155205374412"></a>evs:volumes:get</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1477202455310"><a name="p1477202455310"></a><a name="p1477202455310"></a>POST /v2/{project_id}/volumes</p>
</td>
</tr>
<tr id="row9281224111513"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p04013248156"><a name="p04013248156"></a><a name="p04013248156"></a>Expand the capacity of an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p8441224141517"><a name="p8441224141517"></a><a name="p8441224141517"></a>evs:volumes:extend</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1355838165315"><a name="p1355838165315"></a><a name="p1355838165315"></a>POST /v2/{project_id}/cloudvolumes/{volume_id}/action</p>
</td>
</tr>
<tr id="row71331924131514"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1414315240156"><a name="p1414315240156"></a><a name="p1414315240156"></a>Query EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p16150122401514"><a name="p16150122401514"></a><a name="p16150122401514"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p93556385534"><a name="p93556385534"></a><a name="p93556385534"></a>GET /v2/{project_id}/cloudvolumes</p>
</td>
</tr>
<tr id="row1185102491518"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p111946244151"><a name="p111946244151"></a><a name="p111946244151"></a>Query EVS disks (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1220192411155"><a name="p1220192411155"></a><a name="p1220192411155"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p73551384539"><a name="p73551384539"></a><a name="p73551384539"></a>GET /v2/{project_id}/volumes</p>
</td>
</tr>
<tr id="row32341324101513"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1624352481513"><a name="p1624352481513"></a><a name="p1624352481513"></a>Query details of all EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p3251102410151"><a name="p3251102410151"></a><a name="p3251102410151"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p879824719535"><a name="p879824719535"></a><a name="p879824719535"></a>GET /v2/{project_id}/cloudvolumes/detail</p>
</td>
</tr>
<tr id="row728032419152"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p112913248154"><a name="p112913248154"></a><a name="p112913248154"></a>Querying Details About All Disks</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p9298132441516"><a name="p9298132441516"></a><a name="p9298132441516"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p67986477538"><a name="p67986477538"></a><a name="p67986477538"></a>GET /v2/{project_id}/os-vendor-volumes/detail</p>
</td>
</tr>
<tr id="row1733662417153"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p4348112441514"><a name="p4348112441514"></a><a name="p4348112441514"></a>Query details of all EVS disks (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1352324171519"><a name="p1352324171519"></a><a name="p1352324171519"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p19798947115316"><a name="p19798947115316"></a><a name="p19798947115316"></a>GET /v2/{project_id}/volumes/detail</p>
</td>
</tr>
<tr id="row94419241150"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p16452224141514"><a name="p16452224141514"></a><a name="p16452224141514"></a>Query details of an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p145772413152"><a name="p145772413152"></a><a name="p145772413152"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p177981047105310"><a name="p177981047105310"></a><a name="p177981047105310"></a>GET /v2/{project_id}/volumes/{volume_id}</p>
</td>
</tr>
<tr id="row134911724131511"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1550213243158"><a name="p1550213243158"></a><a name="p1550213243158"></a>Query details of an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p150712416152"><a name="p150712416152"></a><a name="p150712416152"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p296175715532"><a name="p296175715532"></a><a name="p296175715532"></a>GET /v2/{project_id}/cloudvolumes/{volume_id}</p>
</td>
</tr>
<tr id="row2556182411158"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p19565624141519"><a name="p19565624141519"></a><a name="p19565624141519"></a>Delete an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1757111240150"><a name="p1757111240150"></a><a name="p1757111240150"></a>evs:volumes:delete</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p596135710534"><a name="p596135710534"></a><a name="p596135710534"></a>DELETE /v2/{project_id}/cloudvolumes/{volume_id}</p>
</td>
</tr>
<tr id="row18604824121517"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p8614102415156"><a name="p8614102415156"></a><a name="p8614102415156"></a>Delete an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p4620152410152"><a name="p4620152410152"></a><a name="p4620152410152"></a>evs:volumes:delete</p>
<p id="p1262392451511"><a name="p1262392451511"></a><a name="p1262392451511"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p139735795310"><a name="p139735795310"></a><a name="p139735795310"></a>DELETE /v2/{project_id}/volumes/{volume_id}</p>
</td>
</tr>
<tr id="row15656122416156"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p9667202416150"><a name="p9667202416150"></a><a name="p9667202416150"></a>Update EVS disk information.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1967452411512"><a name="p1967452411512"></a><a name="p1967452411512"></a>evs:volumes:update</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p19978570538"><a name="p19978570538"></a><a name="p19978570538"></a>PUT /v2/{project_id}/cloudvolumes/{volume_id}</p>
</td>
</tr>
<tr id="row670792413150"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p8717324111518"><a name="p8717324111518"></a><a name="p8717324111518"></a>Update EVS disk information (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p10721202451517"><a name="p10721202451517"></a><a name="p10721202451517"></a>evs:volumes:update</p>
<p id="p1272392416155"><a name="p1272392416155"></a><a name="p1272392416155"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1697175718538"><a name="p1697175718538"></a><a name="p1697175718538"></a>PUT /v2/{project_id}/volumes/{volume_id}</p>
</td>
</tr>
<tr id="row3758142414155"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p19768182461513"><a name="p19768182461513"></a><a name="p19768182461513"></a>Update one piece of EVS disk metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p7771824101511"><a name="p7771824101511"></a><a name="p7771824101511"></a>evs:volumes:update</p>
<p id="p777492401514"><a name="p777492401514"></a><a name="p777492401514"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p94301450543"><a name="p94301450543"></a><a name="p94301450543"></a>PUT /v2/{project_id}/volumes/{volume_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row28051024111517"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p17816924161515"><a name="p17816924161515"></a><a name="p17816924161515"></a>Update the metadata of an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p58221324171514"><a name="p58221324171514"></a><a name="p58221324171514"></a>evs:volumes:update</p>
<p id="p1982517249156"><a name="p1982517249156"></a><a name="p1982517249156"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p84311857546"><a name="p84311857546"></a><a name="p84311857546"></a>PUT /v2/{project_id}/volumes/{volume_id}/metadata</p>
</td>
</tr>
<tr id="row685918245158"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p138691247154"><a name="p138691247154"></a><a name="p138691247154"></a>Query one piece of EVS disk metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p78721424131514"><a name="p78721424131514"></a><a name="p78721424131514"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p134317545411"><a name="p134317545411"></a><a name="p134317545411"></a>GET /v2/{project_id}/volumes/{volume_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row0906182431511"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1917224111519"><a name="p1917224111519"></a><a name="p1917224111519"></a>Delete one piece of EVS disk metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p18922624201511"><a name="p18922624201511"></a><a name="p18922624201511"></a>evs:volumes:delete</p>
<p id="p159261124181511"><a name="p159261124181511"></a><a name="p159261124181511"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p164314535419"><a name="p164314535419"></a><a name="p164314535419"></a>DELETE /v2/{project_id}/volumes/{volume_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row69611824161516"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p18972102411511"><a name="p18972102411511"></a><a name="p18972102411511"></a>Query the metadata of an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p397915248159"><a name="p397915248159"></a><a name="p397915248159"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p44314512541"><a name="p44314512541"></a><a name="p44314512541"></a>GET /v2/{project_id}/volumes/{volume_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row13967023185011"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p6967102312503"><a name="p6967102312503"></a><a name="p6967102312503"></a>Add the metadata of an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p8107558546"><a name="p8107558546"></a><a name="p8107558546"></a>evs:volumes:update</p>
<p id="p71079583412"><a name="p71079583412"></a><a name="p71079583412"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p27831912165416"><a name="p27831912165416"></a><a name="p27831912165416"></a>POST /v2/{project_id}/volumes/{volume_id}/metadata</p>
</td>
</tr>
<tr id="row18121325111515"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p323192521519"><a name="p323192521519"></a><a name="p323192521519"></a>Query EVS disk types (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p15281025161512"><a name="p15281025161512"></a><a name="p15281025161512"></a>evs:types:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1878391217548"><a name="p1878391217548"></a><a name="p1878391217548"></a>GET /v2/{project_id}/types</p>
</td>
</tr>
<tr id="row156318257153"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p272152591513"><a name="p272152591513"></a><a name="p272152591513"></a>Query details of an EVS disk type (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p13781125111513"><a name="p13781125111513"></a><a name="p13781125111513"></a>evs:types:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p6783121275419"><a name="p6783121275419"></a><a name="p6783121275419"></a>GET /v2/{project_id}/types/{type_id}</p>
</td>
</tr>
<tr id="row51131725111517"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1512517253157"><a name="p1512517253157"></a><a name="p1512517253157"></a>Query tenant quotas (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p1613142514155"><a name="p1613142514155"></a><a name="p1613142514155"></a>evs:quotas:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p07832012145417"><a name="p07832012145417"></a><a name="p07832012145417"></a>GET /v2/{project_id}/os-quota-sets/{project_id}</p>
</td>
</tr>
<tr id="row1416413256152"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p101801725111514"><a name="p101801725111514"></a><a name="p101801725111514"></a>Query extension APIs (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p71841825101510"><a name="p71841825101510"></a><a name="p71841825101510"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p1578441215419"><a name="p1578441215419"></a><a name="p1578441215419"></a>GET /v2/{project_id}/extensions</p>
</td>
</tr>
<tr id="row1121512515155"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p1222822551515"><a name="p1222822551515"></a><a name="p1222822551515"></a>Query information of all AZs (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p14234102520155"><a name="p14234102520155"></a><a name="p14234102520155"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p9598132205417"><a name="p9598132205417"></a><a name="p9598132205417"></a>GET /v2/{project_id}/os-availability-zone</p>
</td>
</tr>
<tr id="row1870171119496"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p870251154914"><a name="p870251154914"></a><a name="p870251154914"></a>Query loading progress of a lazyloading disk.</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p19702411144912"><a name="p19702411144912"></a><a name="p19702411144912"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p17598132285410"><a name="p17598132285410"></a><a name="p17598132285410"></a>GET /v3/{project_id}/os-vendor-volumes/{volume_id}/internal-info</p>
</td>
</tr>
<tr id="row49691171512"><td class="cellrowborder" valign="top" width="33.204334365325074%" headers="mcps1.1.4.1.1 "><p id="p17969127185115"><a name="p17969127185115"></a><a name="p17969127185115"></a>Query EVS disks (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.489680082559335%" headers="mcps1.1.4.1.2 "><p id="p109691273513"><a name="p109691273513"></a><a name="p109691273513"></a>evs:volumes:get</p>
<p id="p41975373350"><a name="p41975373350"></a><a name="p41975373350"></a>evs:volumes:list</p>
</td>
<td class="cellrowborder" valign="top" width="39.30598555211558%" headers="mcps1.1.4.1.3 "><p id="p10598132285414"><a name="p10598132285414"></a><a name="p10598132285414"></a>GET /v3/{project_id}/volumes/summary</p>
</td>
</tr>
</tbody>
</table>

## EVS Disk Actions<a name="section193981335267"></a>

<a name="table11136162518266"></a>
<table><thead align="left"><tr id="row19140152562617"><th class="cellrowborder" valign="top" width="33.50913300746077%" id="mcps1.1.4.1.1"><p id="p5664144515597"><a name="p5664144515597"></a><a name="p5664144515597"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="27.952148186261898%" id="mcps1.1.4.1.2"><p id="p9664104575914"><a name="p9664104575914"></a><a name="p9664104575914"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="38.53871880627733%" id="mcps1.1.4.1.3"><p id="p19664194585915"><a name="p19664194585915"></a><a name="p19664194585915"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row14183202592618"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p1630995419425"><a name="p1630995419425"></a><a name="p1630995419425"></a>Expand the capacity of an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p1350513314414"><a name="p1350513314414"></a><a name="p1350513314414"></a>evs:volumes:extend</p>
<p id="p1938111964"><a name="p1938111964"></a><a name="p1938111964"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p12701151145818"><a name="p12701151145818"></a><a name="p12701151145818"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p870141175817"><a name="p870141175817"></a><a name="p870141175817"></a>action="os-extend"</p>
</td>
</tr>
<tr id="row7188202572612"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p14505173334110"><a name="p14505173334110"></a><a name="p14505173334110"></a>Export the EVS disk data as an image (OpenStack Cinder API).</p>
<p id="p750573324115"><a name="p750573324115"></a><a name="p750573324115"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p1350563310410"><a name="p1350563310410"></a><a name="p1350563310410"></a>evs:volumes:uploadImage</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p1870171125811"><a name="p1870171125811"></a><a name="p1870171125811"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p770151125815"><a name="p770151125815"></a><a name="p770151125815"></a>action="os-volume_upload_image"</p>
</td>
</tr>
<tr id="row919611258261"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p1350513334410"><a name="p1350513334410"></a><a name="p1350513334410"></a>Attach an EVS disk (OpenStack Cinder API).</p>
<p id="p17505183344119"><a name="p17505183344119"></a><a name="p17505183344119"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p3505633174113"><a name="p3505633174113"></a><a name="p3505633174113"></a>evs:volumes:attach</p>
<p id="p7683122512614"><a name="p7683122512614"></a><a name="p7683122512614"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p1771715164586"><a name="p1771715164586"></a><a name="p1771715164586"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p4717516115811"><a name="p4717516115811"></a><a name="p4717516115811"></a>action="os-attach"</p>
</td>
</tr>
<tr id="row520272562611"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p9505233144119"><a name="p9505233144119"></a><a name="p9505233144119"></a>Detach an EVS disk (OpenStack Cinder API).</p>
<p id="p12505833184111"><a name="p12505833184111"></a><a name="p12505833184111"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p75050336410"><a name="p75050336410"></a><a name="p75050336410"></a>evs:volumes:detach</p>
<p id="p924813014617"><a name="p924813014617"></a><a name="p924813014617"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p171791612583"><a name="p171791612583"></a><a name="p171791612583"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p19717171616581"><a name="p19717171616581"></a><a name="p19717171616581"></a>action="os-detach"</p>
</td>
</tr>
<tr id="row72061525202618"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p1550793324114"><a name="p1550793324114"></a><a name="p1550793324114"></a>Reserve an EVS disk (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p150711337412"><a name="p150711337412"></a><a name="p150711337412"></a>evs:volumes:attach</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p9556221585"><a name="p9556221585"></a><a name="p9556221585"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p20551522115817"><a name="p20551522115817"></a><a name="p20551522115817"></a>action="os-reserve"</p>
</td>
</tr>
<tr id="row202111725132618"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p17507153311414"><a name="p17507153311414"></a><a name="p17507153311414"></a>Cancel reservation of an EVS disk (OpenStack Cinder API).</p>
<p id="p1450715338413"><a name="p1450715338413"></a><a name="p1450715338413"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p1250710336417"><a name="p1250710336417"></a><a name="p1250710336417"></a>evs:volumes:attach</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p4551922135816"><a name="p4551922135816"></a><a name="p4551922135816"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p105512210589"><a name="p105512210589"></a><a name="p105512210589"></a>action="os-unreserve"</p>
</td>
</tr>
<tr id="row3216132515266"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p650763354113"><a name="p650763354113"></a><a name="p650763354113"></a>Set the bootable flag for an EVS disk (OpenStack Cinder API).</p>
<p id="p1350713313411"><a name="p1350713313411"></a><a name="p1350713313411"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p2050703394118"><a name="p2050703394118"></a><a name="p2050703394118"></a>evs:volumes:update</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p555822145818"><a name="p555822145818"></a><a name="p555822145818"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p1956132219580"><a name="p1956132219580"></a><a name="p1956132219580"></a>action="os-set_bootable"</p>
</td>
</tr>
<tr id="row122182572614"><td class="cellrowborder" valign="top" width="33.50913300746077%" headers="mcps1.1.4.1.1 "><p id="p1750819334410"><a name="p1750819334410"></a><a name="p1750819334410"></a>Set the read-only attribute for an EVS disk (OpenStack Cinder API).</p>
<p id="p250873310414"><a name="p250873310414"></a><a name="p250873310414"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.952148186261898%" headers="mcps1.1.4.1.2 "><p id="p14508153317415"><a name="p14508153317415"></a><a name="p14508153317415"></a>evs:volumes:update</p>
</td>
<td class="cellrowborder" valign="top" width="38.53871880627733%" headers="mcps1.1.4.1.3 "><p id="p556162215810"><a name="p556162215810"></a><a name="p556162215810"></a>POST /v2/{project_id}/volumes/{volume_id}/action</p>
<p id="p4561722185810"><a name="p4561722185810"></a><a name="p4561722185810"></a>action="os-update_readonly_flag"</p>
</td>
</tr>
</tbody>
</table>

## EVS Snapshot<a name="section176411659163519"></a>

<a name="table8361746185711"></a>
<table><thead align="left"><tr id="row4369184618577"><th class="cellrowborder" valign="top" width="33.15870176335293%" id="mcps1.1.4.1.1"><p id="p446155119220"><a name="p446155119220"></a><a name="p446155119220"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="28.443649373881936%" id="mcps1.1.4.1.2"><p id="p246211511327"><a name="p246211511327"></a><a name="p246211511327"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="38.397648862765145%" id="mcps1.1.4.1.3"><p id="p9462165111219"><a name="p9462165111219"></a><a name="p9462165111219"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row643864695720"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p10520201618586"><a name="p10520201618586"></a><a name="p10520201618586"></a>Create an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p7520191613584"><a name="p7520191613584"></a><a name="p7520191613584"></a>evs:snapshots:create</p>
<p id="p752061675812"><a name="p752061675812"></a><a name="p752061675812"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p1281012372010"><a name="p1281012372010"></a><a name="p1281012372010"></a>POST /v2/{project_id}/snapshots</p>
</td>
</tr>
<tr id="row1075585012810"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p174195720280"><a name="p174195720280"></a><a name="p174195720280"></a>Create an EVS snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p9741105720285"><a name="p9741105720285"></a><a name="p9741105720285"></a>evs:snapshots:create</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p3810163718016"><a name="p3810163718016"></a><a name="p3810163718016"></a>POST /v2/{project_id}/cloudsnapshots</p>
</td>
</tr>
<tr id="row134461346195715"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p186113213712"><a name="p186113213712"></a><a name="p186113213712"></a>Query EVS snapshots (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p2520191615588"><a name="p2520191615588"></a><a name="p2520191615588"></a>evs:snapshots:list</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p781073714013"><a name="p781073714013"></a><a name="p781073714013"></a>GET /v2/{project_id}/snapshots</p>
</td>
</tr>
<tr id="row54658465572"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p157141752374"><a name="p157141752374"></a><a name="p157141752374"></a>Query details of EVS snapshots (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p19520181617589"><a name="p19520181617589"></a><a name="p19520181617589"></a>evs:snapshots:list</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p48116371606"><a name="p48116371606"></a><a name="p48116371606"></a>GET /v2/{project_id}/snapshots/detail</p>
</td>
</tr>
<tr id="row1756178123012"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p85004141305"><a name="p85004141305"></a><a name="p85004141305"></a>Query details about EVS snapshots.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p7500614183020"><a name="p7500614183020"></a><a name="p7500614183020"></a>evs:snapshots:list</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p712412471206"><a name="p712412471206"></a><a name="p712412471206"></a>GET /v2/{project_id}/cloudsnapshots/detail</p>
</td>
</tr>
<tr id="row10475194695719"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p8520916115814"><a name="p8520916115814"></a><a name="p8520916115814"></a>Update an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p1252071613582"><a name="p1252071613582"></a><a name="p1252071613582"></a>evs:snapshots:update</p>
<p id="p205082024154519"><a name="p205082024154519"></a><a name="p205082024154519"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p131247471501"><a name="p131247471501"></a><a name="p131247471501"></a>PUT /v2/{project_id}/snapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row179161013314"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p8988101983119"><a name="p8988101983119"></a><a name="p8988101983119"></a>Update an EVS snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p99887198315"><a name="p99887198315"></a><a name="p99887198315"></a>evs:snapshots:update</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p212413471506"><a name="p212413471506"></a><a name="p212413471506"></a>PUT /v2/{project_id}/cloudsnapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row1217231317314"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p91887436313"><a name="p91887436313"></a><a name="p91887436313"></a>Query details about a single EVS snapshot (OpenStack Cinder API).</p>
<p id="p41881643193114"><a name="p41881643193114"></a><a name="p41881643193114"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p15188194319319"><a name="p15188194319319"></a><a name="p15188194319319"></a>evs:snapshots:get</p>
<p id="p151886434311"><a name="p151886434311"></a><a name="p151886434311"></a></p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p1212564718015"><a name="p1212564718015"></a><a name="p1212564718015"></a>GET /v2/{project_id}/snapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row1412410163210"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p87211922103217"><a name="p87211922103217"></a><a name="p87211922103217"></a>Querying details about an EVS snapshot.</p>
<p id="p107216223328"><a name="p107216223328"></a><a name="p107216223328"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p147211522103211"><a name="p147211522103211"></a><a name="p147211522103211"></a>evs:snapshots:get</p>
<p id="p10721722143211"><a name="p10721722143211"></a><a name="p10721722143211"></a></p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p15894195210018"><a name="p15894195210018"></a><a name="p15894195210018"></a>GET /v2/{project_id}/cloudsnapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row1448414645716"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p568112919919"><a name="p568112919919"></a><a name="p568112919919"></a>Delete an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p15520161665817"><a name="p15520161665817"></a><a name="p15520161665817"></a>evs:snapshots:delete</p>
<p id="p331517388456"><a name="p331517388456"></a><a name="p331517388456"></a>evs:snapshots:get</p>
<p id="p47022010154218"><a name="p47022010154218"></a><a name="p47022010154218"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p1489465219014"><a name="p1489465219014"></a><a name="p1489465219014"></a>DELETE /v2/{project_id}/snapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row413170183313"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p6277117193320"><a name="p6277117193320"></a><a name="p6277117193320"></a>Deleting an EVS snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p32777710334"><a name="p32777710334"></a><a name="p32777710334"></a>evs:snapshots:delete</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p178950520013"><a name="p178950520013"></a><a name="p178950520013"></a>DELETE /v2/{project_id}/cloudsnapshots/{snapshot_id}</p>
</td>
</tr>
<tr id="row20204195133019"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p620517518308"><a name="p620517518308"></a><a name="p620517518308"></a>Roll back a snapshot to an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p1520575163020"><a name="p1520575163020"></a><a name="p1520575163020"></a>evs:snapshots:rollback</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p1489518521303"><a name="p1489518521303"></a><a name="p1489518521303"></a>POST /v2/{project_id}/cloudsnapshots/{snapshot_id}/rollback</p>
</td>
</tr>
<tr id="row58726167563"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p187291614567"><a name="p187291614567"></a><a name="p187291614567"></a>Roll back a snapshot to an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p16872216165614"><a name="p16872216165614"></a><a name="p16872216165614"></a>evs:snapshots:rollback</p>
<p id="p1595325820190"><a name="p1595325820190"></a><a name="p1595325820190"></a>evs:snapshots:get</p>
<p id="p12953115891911"><a name="p12953115891911"></a><a name="p12953115891911"></a>evs:volumes:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p85810014112"><a name="p85810014112"></a><a name="p85810014112"></a>POST /v2/{project_id}/os-vendor-snapshots/{snapshot_id}/rollback</p>
</td>
</tr>
<tr id="row91013379418"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p1710183715412"><a name="p1710183715412"></a><a name="p1710183715412"></a>Add the metadata of an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p1598051014513"><a name="p1598051014513"></a><a name="p1598051014513"></a>evs:snapshots:update</p>
<p id="p29801110185114"><a name="p29801110185114"></a><a name="p29801110185114"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p135811201912"><a name="p135811201912"></a><a name="p135811201912"></a>POST /v2/{project_id}/snapshots/{snapshot_id}/metadata</p>
</td>
</tr>
<tr id="row13111337154116"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p611337134115"><a name="p611337134115"></a><a name="p611337134115"></a>Query the metadata of an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p9114377416"><a name="p9114377416"></a><a name="p9114377416"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p2581202110"><a name="p2581202110"></a><a name="p2581202110"></a>GET /v2/{project_id}/snapshots/{snapshot_id}/metadata</p>
</td>
</tr>
<tr id="row51112374412"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p141163744111"><a name="p141163744111"></a><a name="p141163744111"></a>Update one piece of EVS snapshot metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p73171640105213"><a name="p73171640105213"></a><a name="p73171640105213"></a>evs:snapshots:update</p>
<p id="p103171640135212"><a name="p103171640135212"></a><a name="p103171640135212"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p13582709115"><a name="p13582709115"></a><a name="p13582709115"></a>PUT /v2/{project_id}/snapshots/{snapshot_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row6170194616411"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p6170184618415"><a name="p6170184618415"></a><a name="p6170184618415"></a>Update the metadata of an EVS snapshot (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p7745125617523"><a name="p7745125617523"></a><a name="p7745125617523"></a>evs:snapshots:update</p>
<p id="p12745145635214"><a name="p12745145635214"></a><a name="p12745145635214"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p63151161010"><a name="p63151161010"></a><a name="p63151161010"></a>PUT /v2/{project_id}/snapshots/{snapshot_id}/metadata</p>
</td>
</tr>
<tr id="row141711046124116"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p117174617418"><a name="p117174617418"></a><a name="p117174617418"></a>Query one piece of EVS snapshot metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p0875142255313"><a name="p0875142255313"></a><a name="p0875142255313"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p53151362011"><a name="p53151362011"></a><a name="p53151362011"></a>GET /v2/{project_id}/snapshots/{snapshot_id}/metadata/{key}</p>
</td>
</tr>
<tr id="row71711846104113"><td class="cellrowborder" valign="top" width="33.15870176335293%" headers="mcps1.1.4.1.1 "><p id="p3172164611411"><a name="p3172164611411"></a><a name="p3172164611411"></a>Delete one piece of EVS snapshot metadata (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.443649373881936%" headers="mcps1.1.4.1.2 "><p id="p87548350536"><a name="p87548350536"></a><a name="p87548350536"></a>evs:snapshots:delete</p>
<p id="p7754835105310"><a name="p7754835105310"></a><a name="p7754835105310"></a>evs:snapshots:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.397648862765145%" headers="mcps1.1.4.1.3 "><p id="p1631517615113"><a name="p1631517615113"></a><a name="p1631517615113"></a>DELETE /v2/{project_id}/snapshots/{snapshot_id}/metadata/{key}</p>
</td>
</tr>
</tbody>
</table>

## EVS Tag<a name="section5591717131516"></a>

<a name="table1625762620526"></a>
<table><thead align="left"><tr id="row10257202616527"><th class="cellrowborder" valign="top" width="33.19317023445464%" id="mcps1.1.4.1.1"><p id="p1725711269525"><a name="p1725711269525"></a><a name="p1725711269525"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="28.758919469928646%" id="mcps1.1.4.1.2"><p id="p142571626195215"><a name="p142571626195215"></a><a name="p142571626195215"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="38.04791029561672%" id="mcps1.1.4.1.3"><p id="p3258326175210"><a name="p3258326175210"></a><a name="p3258326175210"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row62581826195217"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p225892613528"><a name="p225892613528"></a><a name="p225892613528"></a>Obtain all EVS tags of a tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul102582026105210"></a><a name="ul102582026105210"></a><ul id="ul102582026105210"><li>EVS disk: evs:volumeTags:list</li><li>Backup: evs:backupTags:list</li><li>Snapshot: evs:snapshotTags:list</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p5258122645210"><a name="p5258122645210"></a><a name="p5258122645210"></a>GET /v2/{project_id}/os-vendor-tags/{resource_type}</p>
</td>
</tr>
<tr id="row1925832655220"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p1525832695213"><a name="p1525832695213"></a><a name="p1525832695213"></a>Query EVS resources by tag.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul1625819264527"></a><a name="ul1625819264527"></a><ul id="ul1625819264527"><li>EVS disk: evs:volumeTags:get</li><li>Backup: evs:backupTags:get</li><li>Snapshot: evs:snapshotTags:get</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p1125962645213"><a name="p1125962645213"></a><a name="p1125962645213"></a>GET /v2/{project_id}/os-vendor-tags/{resource_type}/resource_instances</p>
</td>
</tr>
<tr id="row1825962695218"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p15259142612521"><a name="p15259142612521"></a><a name="p15259142612521"></a>Add or update tags for an EVS resource.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul192591126105213"></a><a name="ul192591126105213"></a><ul id="ul192591126105213"><li>EVS disk: evs:volumeTags:create</li><li>Backup: evs:backupTags:create</li><li>Snapshot: evs:snapshotTags:create</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p2026016265525"><a name="p2026016265525"></a><a name="p2026016265525"></a>POST /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}</p>
</td>
</tr>
<tr id="row1026018261521"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p1126032625213"><a name="p1126032625213"></a><a name="p1126032625213"></a>Obtain tags of an EVS resource.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul102601526185217"></a><a name="ul102601526185217"></a><ul id="ul102601526185217"><li>EVS disk: evs:volumeTags:getById</li><li>Backup: evs:backupTags:getById</li><li>Snapshot: evs:snapshotTags:getById</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p32611726155210"><a name="p32611726155210"></a><a name="p32611726155210"></a>GET /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}</p>
</td>
</tr>
<tr id="row11261132605217"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p18261326205210"><a name="p18261326205210"></a><a name="p18261326205210"></a>Reset the tags of an EVS resource.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul1126116264524"></a><a name="ul1126116264524"></a><ul id="ul1126116264524"><li>EVS disk: evs:volumeTags:update</li><li>Backup: evs:backupTags:update</li><li>Snapshot: evs:snapshotTags:update</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p11261426205217"><a name="p11261426205217"></a><a name="p11261426205217"></a>PUT /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}</p>
</td>
</tr>
<tr id="row7261152611526"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p72611826115213"><a name="p72611826115213"></a><a name="p72611826115213"></a>Batch delete the tags for an EVS resource.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul18262326185216"></a><a name="ul18262326185216"></a><ul id="ul18262326185216"><li>EVS disk: evs:volumeTags:delete<p id="p2262152625220"><a name="p2262152625220"></a><a name="p2262152625220"></a>evs:volumeTags:getById</p>
</li><li>Backup: evs:backupTags:delete<p id="p826242615521"><a name="p826242615521"></a><a name="p826242615521"></a>evs:backupTags:getById</p>
</li><li>Snapshot: evs:snapshotTags:delete<p id="p826222635211"><a name="p826222635211"></a><a name="p826222635211"></a>evs:snapshotTags:getById</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p126222618528"><a name="p126222618528"></a><a name="p126222618528"></a>POST /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}/action</p>
</td>
</tr>
<tr id="row202627265524"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p0262172695219"><a name="p0262172695219"></a><a name="p0262172695219"></a>Delete the tags of an EVS resource by key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul182628268521"></a><a name="ul182628268521"></a><ul id="ul182628268521"><li>EVS disk: evs:volumeTags:getById<p id="p1526252645212"><a name="p1526252645212"></a><a name="p1526252645212"></a>evs:volumeTags:delete</p>
</li><li>Backup: evs:backupTags:getById<p id="p626392611523"><a name="p626392611523"></a><a name="p626392611523"></a>evs:backupTags:delete</p>
</li><li>Snapshot: evs:snapshotTags:getById<p id="p5263326145217"><a name="p5263326145217"></a><a name="p5263326145217"></a>evs:snapshotTags:delete</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p15263526195219"><a name="p15263526195219"></a><a name="p15263526195219"></a>DELETE /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}/{key}</p>
</td>
</tr>
<tr id="row19264626185212"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p102641726135213"><a name="p102641726135213"></a><a name="p102641726135213"></a>Update the tags of an EVS resource by key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><a name="ul326420268527"></a><a name="ul326420268527"></a><ul id="ul326420268527"><li>EVS disk: evs:volumeTags:update</li><li>Backup: evs:backupTags:update</li><li>Snapshot: evs:snapshotTags:update</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p18265926105211"><a name="p18265926105211"></a><a name="p18265926105211"></a>PUT /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}/{key}</p>
</td>
</tr>
<tr id="row142651526145215"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p92651926155219"><a name="p92651926155219"></a><a name="p92651926155219"></a>Batch delete the tags for a specified EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p11265142615520"><a name="p11265142615520"></a><a name="p11265142615520"></a>evs:volumeTags:delete</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p1626582625216"><a name="p1626582625216"></a><a name="p1626582625216"></a>POST /v2/{project_id}/os-vendor-volumes/{volume_id}/tags/action</p>
</td>
</tr>
<tr id="row3265142605219"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p1226612265527"><a name="p1226612265527"></a><a name="p1226612265527"></a>Query the tags of an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p1526619267527"><a name="p1526619267527"></a><a name="p1526619267527"></a>evs:volumeTags:getById</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p926622655210"><a name="p926622655210"></a><a name="p926622655210"></a>GET /v2/{project_id}/os-vendor-volumes/{volume_id}/tags</p>
</td>
</tr>
<tr id="row3266626125210"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p82661026165216"><a name="p82661026165216"></a><a name="p82661026165216"></a>Batch add tags for a specified EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p5266172619527"><a name="p5266172619527"></a><a name="p5266172619527"></a>evs:volumeTags:create</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p1726612266525"><a name="p1726612266525"></a><a name="p1726612266525"></a>POST /v2/{project_id}/os-vendor-volumes/{volume_id}/tags/action</p>
</td>
</tr>
<tr id="row226619266520"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p4267102675218"><a name="p4267102675218"></a><a name="p4267102675218"></a>Query details of EVS disks by tag.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p92671826145218"><a name="p92671826145218"></a><a name="p92671826145218"></a>evs:volumeTags:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p0267726105211"><a name="p0267726105211"></a><a name="p0267726105211"></a>POST /v2/{project_id}/os-vendor-volumes/resource_instances/action</p>
</td>
</tr>
<tr id="row14267162613529"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p426710266524"><a name="p426710266524"></a><a name="p426710266524"></a>Query tags of an EVS resource by key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p122675267529"><a name="p122675267529"></a><a name="p122675267529"></a>evs:volumeTags:getById</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p1426817267521"><a name="p1426817267521"></a><a name="p1426817267521"></a>GET /v2/{project_id}/os-vendor-tags/{resource_type}/{resource_id}/{key}</p>
</td>
</tr>
<tr id="row10268126135211"><td class="cellrowborder" valign="top" width="33.19317023445464%" headers="mcps1.1.4.1.1 "><p id="p9268132685210"><a name="p9268132685210"></a><a name="p9268132685210"></a>Query the number of EVS disks by tag.</p>
</td>
<td class="cellrowborder" valign="top" width="28.758919469928646%" headers="mcps1.1.4.1.2 "><p id="p7268142685215"><a name="p7268142685215"></a><a name="p7268142685215"></a>evs:volumeTags:get</p>
</td>
<td class="cellrowborder" valign="top" width="38.04791029561672%" headers="mcps1.1.4.1.3 "><p id="p162681726115212"><a name="p162681726115212"></a><a name="p162681726115212"></a>POST /v2/{project_id}/os-vendor-volumes/resource_instances/action</p>
</td>
</tr>
</tbody>
</table>

## EVS Disk Transfer<a name="section173078159254"></a>

<a name="table33101915182515"></a>
<table><thead align="left"><tr id="row832041542517"><th class="cellrowborder" valign="top" width="33.23940053797874%" id="mcps1.1.4.1.1"><p id="p1570661181113"><a name="p1570661181113"></a><a name="p1570661181113"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="28.781862431151534%" id="mcps1.1.4.1.2"><p id="p147061615115"><a name="p147061615115"></a><a name="p147061615115"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="37.97873703086973%" id="mcps1.1.4.1.3"><p id="p970715181111"><a name="p970715181111"></a><a name="p970715181111"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row1533321516254"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p178090277285"><a name="p178090277285"></a><a name="p178090277285"></a>Create an EVS disk transfer (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p1355812615270"><a name="p1355812615270"></a><a name="p1355812615270"></a>evs:transfers:create</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p1423372715104"><a name="p1423372715104"></a><a name="p1423372715104"></a>POST /v2/{project_id}/os-volume-transfer</p>
</td>
</tr>
<tr id="row63451215152514"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p3558142672711"><a name="p3558142672711"></a><a name="p3558142672711"></a>Query all EVS disk transfers of a tenant (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p265073320219"><a name="p265073320219"></a><a name="p265073320219"></a>evs:transfers:list</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p52339273102"><a name="p52339273102"></a><a name="p52339273102"></a>GET /v2/{project_id}/os-volume-transfer</p>
</td>
</tr>
<tr id="row8355101572511"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p165581269277"><a name="p165581269277"></a><a name="p165581269277"></a>Query details of all EVS disk transfers of a tenant (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p6652143318216"><a name="p6652143318216"></a><a name="p6652143318216"></a>evs:transfers:list</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p19234172710101"><a name="p19234172710101"></a><a name="p19234172710101"></a>GET /v2/{project_id}/os-volume-transfer/detail</p>
</td>
</tr>
<tr id="row5365101582519"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p65587264271"><a name="p65587264271"></a><a name="p65587264271"></a>Query details of an EVS disk transfer (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p1055817260275"><a name="p1055817260275"></a><a name="p1055817260275"></a>evs:transfers:get</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p15234102751011"><a name="p15234102751011"></a><a name="p15234102751011"></a>GET /v2/{project_id}/os-volume-transfer/{transfer_id}</p>
</td>
</tr>
<tr id="row113831315142516"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p855819261278"><a name="p855819261278"></a><a name="p855819261278"></a>Accept an EVS disk transfer (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p95583265274"><a name="p95583265274"></a><a name="p95583265274"></a>evs:transfers:accept</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p9981123112106"><a name="p9981123112106"></a><a name="p9981123112106"></a>POST /v2/{project_id}/os-volume-transfer/{transfer_id}/accept</p>
</td>
</tr>
<tr id="row997615405218"><td class="cellrowborder" valign="top" width="33.23940053797874%" headers="mcps1.1.4.1.1 "><p id="p1394094642118"><a name="p1394094642118"></a><a name="p1394094642118"></a>Delete an EVS disk transfer (OpenStack Cinder API).</p>
</td>
<td class="cellrowborder" valign="top" width="28.781862431151534%" headers="mcps1.1.4.1.2 "><p id="p179401346122117"><a name="p179401346122117"></a><a name="p179401346122117"></a>evs:transfers:delete</p>
</td>
<td class="cellrowborder" valign="top" width="37.97873703086973%" headers="mcps1.1.4.1.3 "><p id="p498183151012"><a name="p498183151012"></a><a name="p498183151012"></a>DELETE /v2/{project_id}/os-volume-transfer/{transfer_id}</p>
</td>
</tr>
</tbody>
</table>

