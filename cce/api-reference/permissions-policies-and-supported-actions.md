# Permissions Policies and Supported Actions<a name="cce_02_0327"></a>

This chapter describes fine-grained permissions management for your CCE. If your cloud account does not need individual IAM users, then you may skip over this chapter.

A policy is a set of permissions defined in JSON format. By default, new IAM users do not have any permissions assigned. You need to add a user to one or more groups, and assign permissions policies to these groups. The user then inherits permissions from the groups it is a member of. This process is called authorization. After authorization, the user can perform specified operations on specified cloud services based on the permissions.

There are fine-grained policies and role-based access control \(RBAC\) policies. An RBAC policy consists of permissions for an entire service. Users in a group with such a policy assigned are granted all of the permissions required for that service. A fine-grained policy consists of API-based permissions for operations on specific resource types. Fine-grained policies, as the name suggests, allow for more fine-grained control than RBAC policies.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Fine-grained policies are currently available for open beta testing. You can apply to the fine-grained access control function free of charge.  
>-   If you want to allow or deny the access to an API, fine-grained authorization is a good choice.  

An account has all of the permissions required to call all APIs, but IAM users must have the required permissions specifically assigned. The permissions required for calling an API are determined by the actions supported by the API. Only users who have been granted permissions can call the API successfully. For example, if an IAM user queries CCE clusters using an API, the user must have been granted permissions that allow the  **cce:cluster:list**  action.

## Supported Actions<a name="section65555736"></a>

Operations supported by a fine-grained policy are specific to APIs. The following describes the headers of the action tables provided in this chapter:

-   Permissions: Defined by actions in a custom policy.
-   Actions: Added to a custom policy to control permissions for specific operations.
-   Authorization Scope: A custom policy can be applied to IAM projects or enterprise projects or both. Policies that contain actions supporting both IAM and enterprise projects can be assigned to user groups and take effect in both IAM and Enterprise Management. Policies that only contain actions supporting IAM projects can be assigned to user groups and only take effect for IAM. Such policies will not take effect if they are assigned to user groups in Enterprise Management.
-   APIs: REST APIs that can be called in a custom policy.

**Table  1**  CCE actions

<a name="table2746927"></a>
<table><thead align="left"><tr id="row5041122"><th class="cellrowborder" valign="top" width="19.971997199719972%" id="mcps1.2.5.1.1"><p id="p5677776"><a name="p5677776"></a><a name="p5677776"></a>Permissions</p>
</th>
<th class="cellrowborder" valign="top" width="19.971997199719972%" id="mcps1.2.5.1.2"><p id="p57246722"><a name="p57246722"></a><a name="p57246722"></a>Actions</p>
</th>
<th class="cellrowborder" valign="top" width="25.722572257225725%" id="mcps1.2.5.1.3"><p id="p6472929"><a name="p6472929"></a><a name="p6472929"></a>Authorization Scope</p>
</th>
<th class="cellrowborder" valign="top" width="34.33343334333433%" id="mcps1.2.5.1.4"><p id="p54545236"><a name="p54545236"></a><a name="p54545236"></a>APIs</p>
</th>
</tr>
</thead>
<tbody><tr id="row6218729231"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1121922162320"><a name="p1121922162320"></a><a name="p1121922162320"></a>Listing clusters in a specified project</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p11811740142814"><a name="p11811740142814"></a><a name="p11811740142814"></a>cce:cluster:list</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p8223154812713"><a name="p8223154812713"></a><a name="p8223154812713"></a>Supported:</p>
<a name="ul16993175752714"></a><a name="ul16993175752714"></a><ul id="ul16993175752714"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p12219102172319"><a name="p12219102172319"></a><a name="p12219102172319"></a>GET /api/v3/projects/{project_id}/clusters</p>
</td>
</tr>
<tr id="row60174342914"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p160184313297"><a name="p160184313297"></a><a name="p160184313297"></a>Obtaining information about a specified cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p11841940182811"><a name="p11841940182811"></a><a name="p11841940182811"></a>cce:cluster:get</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p6418052132815"><a name="p6418052132815"></a><a name="p6418052132815"></a>Supported:</p>
<a name="ul141885222814"></a><a name="ul141885222814"></a><ul id="ul141885222814"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p140174319298"><a name="p140174319298"></a><a name="p140174319298"></a>GET /api/v3/projects/{project_id}/clusters/{cluster_id}</p>
</td>
</tr>
<tr id="row1930454173014"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p63049414303"><a name="p63049414303"></a><a name="p63049414303"></a>Creating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p131861940132813"><a name="p131861940132813"></a><a name="p131861940132813"></a>cce:cluster:create</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p166562058112816"><a name="p166562058112816"></a><a name="p166562058112816"></a>Supported:</p>
<a name="ul5656185812283"></a><a name="ul5656185812283"></a><ul id="ul5656185812283"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p113042493011"><a name="p113042493011"></a><a name="p113042493011"></a>POST /api/v3/projects/{project_id}/clusters</p>
</td>
</tr>
<tr id="row47112191304"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p177161912304"><a name="p177161912304"></a><a name="p177161912304"></a>Updating information about a specified cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p618964012812"><a name="p618964012812"></a><a name="p618964012812"></a>cce:cluster:update</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p22873392916"><a name="p22873392916"></a><a name="p22873392916"></a>Supported:</p>
<a name="ul18288153122920"></a><a name="ul18288153122920"></a><ul id="ul18288153122920"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p2071191943010"><a name="p2071191943010"></a><a name="p2071191943010"></a>PUT /api/v3/projects/{project_id}/clusters/{cluster_id}</p>
</td>
</tr>
<tr id="row12227515103011"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1422715151309"><a name="p1422715151309"></a><a name="p1422715151309"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p1819154012288"><a name="p1819154012288"></a><a name="p1819154012288"></a>cce:cluster:delete</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p7462111811298"><a name="p7462111811298"></a><a name="p7462111811298"></a>Supported:</p>
<a name="ul1946361817296"></a><a name="ul1946361817296"></a><ul id="ul1946361817296"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p3227101553017"><a name="p3227101553017"></a><a name="p3227101553017"></a>DELETE /api/v3/projects/{project_id}/clusters/{cluster_id}</p>
</td>
</tr>
<tr id="row3113121214304"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1114201211303"><a name="p1114201211303"></a><a name="p1114201211303"></a>Obtaining a cluster certificate</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p1919204020283"><a name="p1919204020283"></a><a name="p1919204020283"></a>cce:cluster:get</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p153527249297"><a name="p153527249297"></a><a name="p153527249297"></a>Supported:</p>
<a name="ul5352152462918"></a><a name="ul5352152462918"></a><ul id="ul5352152462918"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p6114111223018"><a name="p6114111223018"></a><a name="p6114111223018"></a>GET /api/v3/projects/{project_id}/clusters/{cluster_id}/clustercert</p>
</td>
</tr>
<tr id="row712118133018"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p7121386305"><a name="p7121386305"></a><a name="p7121386305"></a>Listing all nodes in a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p219419401287"><a name="p219419401287"></a><a name="p219419401287"></a>cce:node:list</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p721073022910"><a name="p721073022910"></a><a name="p721073022910"></a>Supported:</p>
<a name="ul142101130162911"></a><a name="ul142101130162911"></a><ul id="ul142101130162911"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p8121118173014"><a name="p8121118173014"></a><a name="p8121118173014"></a>GET /api/v3/projects/{project_id}/clusters/{cluster_id}/nodes</p>
</td>
</tr>
<tr id="row7285718304"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1828520153019"><a name="p1828520153019"></a><a name="p1828520153019"></a>Obtaining information about a specified node</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p181969408283"><a name="p181969408283"></a><a name="p181969408283"></a>cce:node:get</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p1345293432912"><a name="p1345293432912"></a><a name="p1345293432912"></a>Supported:</p>
<a name="ul9452234182918"></a><a name="ul9452234182918"></a><ul id="ul9452234182918"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p1428631153012"><a name="p1428631153012"></a><a name="p1428631153012"></a>GET /api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}</p>
</td>
</tr>
<tr id="row1115415718293"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p31540575297"><a name="p31540575297"></a><a name="p31540575297"></a>Creating a node</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p18197184022819"><a name="p18197184022819"></a><a name="p18197184022819"></a>cce:node:create</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p98812419293"><a name="p98812419293"></a><a name="p98812419293"></a>Supported:</p>
<a name="ul16882124118297"></a><a name="ul16882124118297"></a><ul id="ul16882124118297"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p1015485711292"><a name="p1015485711292"></a><a name="p1015485711292"></a>POST /api/v3/projects/{project_id}/clusters/{cluster_id}/nodes</p>
</td>
</tr>
<tr id="row19110195011296"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p15110125052916"><a name="p15110125052916"></a><a name="p15110125052916"></a>Updating information about a specified node</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p6198740202813"><a name="p6198740202813"></a><a name="p6198740202813"></a>cce:node:update</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p1020814519293"><a name="p1020814519293"></a><a name="p1020814519293"></a>Supported:</p>
<a name="ul320844512913"></a><a name="ul320844512913"></a><ul id="ul320844512913"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p121114507298"><a name="p121114507298"></a><a name="p121114507298"></a>PUT /api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}</p>
</td>
</tr>
<tr id="row1274117447385"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p12742134413383"><a name="p12742134413383"></a><a name="p12742134413383"></a>Deleting a node</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p20200154012812"><a name="p20200154012812"></a><a name="p20200154012812"></a>cce:node:delete</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p03737499298"><a name="p03737499298"></a><a name="p03737499298"></a>Supported:</p>
<a name="ul16373549102913"></a><a name="ul16373549102913"></a><ul id="ul16373549102913"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p374224411384"><a name="p374224411384"></a><a name="p374224411384"></a>DELETE /api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}</p>
</td>
</tr>
<tr id="row17957174053811"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p295824012386"><a name="p295824012386"></a><a name="p295824012386"></a>Obtaining job progress</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p14202184022811"><a name="p14202184022811"></a><a name="p14202184022811"></a>cce:job:get</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p11263135317292"><a name="p11263135317292"></a><a name="p11263135317292"></a>Supported:</p>
<a name="ul1726365382915"></a><a name="ul1726365382915"></a><ul id="ul1726365382915"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p295834043816"><a name="p295834043816"></a><a name="p295834043816"></a>GET /api/v3/projects/{project_id}/jobs/{job_id}</p>
</td>
</tr>
<tr id="row410533613813"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p111061364386"><a name="p111061364386"></a><a name="p111061364386"></a>Listing all node pools in a specified cluster</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p18205240142818"><a name="p18205240142818"></a><a name="p18205240142818"></a>cce:nodepool:list</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p06431359132911"><a name="p06431359132911"></a><a name="p06431359132911"></a>Supported:</p>
<a name="ul1964355912911"></a><a name="ul1964355912911"></a><ul id="ul1964355912911"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p181067361383"><a name="p181067361383"></a><a name="p181067361383"></a>GET /api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools</p>
</td>
</tr>
<tr id="row2807038114916"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p14808153894913"><a name="p14808153894913"></a><a name="p14808153894913"></a>Creating a PersistentVolumeClaim</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p920720408285"><a name="p920720408285"></a><a name="p920720408285"></a>cce:storage:create</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p123010493013"><a name="p123010493013"></a><a name="p123010493013"></a>Supported:</p>
<a name="ul923014153018"></a><a name="ul923014153018"></a><ul id="ul923014153018"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p1808133812494"><a name="p1808133812494"></a><a name="p1808133812494"></a>POST /api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims</p>
</td>
</tr>
<tr id="row6393123454917"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p10394163484915"><a name="p10394163484915"></a><a name="p10394163484915"></a>Deleting a PersistentVolumeClaim</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p13208194062813"><a name="p13208194062813"></a><a name="p13208194062813"></a>cce:storage:delete</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p1671371301"><a name="p1671371301"></a><a name="p1671371301"></a>Supported:</p>
<a name="ul20712733015"></a><a name="ul20712733015"></a><ul id="ul20712733015"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p03951034114917"><a name="p03951034114917"></a><a name="p03951034114917"></a>DELETE /api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims/{name}</p>
</td>
</tr>
<tr id="row16815153135017"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p4815103119507"><a name="p4815103119507"></a><a name="p4815103119507"></a>Creating a PersistentVolume</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p12101140182815"><a name="p12101140182815"></a><a name="p12101140182815"></a>cce:storage:create</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p44131011103015"><a name="p44131011103015"></a><a name="p44131011103015"></a>Supported:</p>
<a name="ul14413811193014"></a><a name="ul14413811193014"></a><ul id="ul14413811193014"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p168151331195012"><a name="p168151331195012"></a><a name="p168151331195012"></a>POST /api/v1/cloudpersistentvolumes</p>
</td>
</tr>
<tr id="row4807128185016"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p780782812506"><a name="p780782812506"></a><a name="p780782812506"></a>Deleting a PersistentVolume</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p421254072818"><a name="p421254072818"></a><a name="p421254072818"></a>cce:storage:delete</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p1035511420308"><a name="p1035511420308"></a><a name="p1035511420308"></a>Supported:</p>
<a name="ul63552014133014"></a><a name="ul63552014133014"></a><ul id="ul63552014133014"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><p id="p188079281502"><a name="p188079281502"></a><a name="p188079281502"></a>DELETE /api/v1/cloudpersistentvolumes/{name}</p>
</td>
</tr>
<tr id="row175605401338"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1956117401232"><a name="p1956117401232"></a><a name="p1956117401232"></a>Operating on Kubernetes resources</p>
</td>
<td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p1221316407289"><a name="p1221316407289"></a><a name="p1221316407289"></a>cce:kubernetes:*</p>
</td>
<td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.5.1.3 "><p id="p146157176300"><a name="p146157176300"></a><a name="p146157176300"></a>Supported:</p>
<a name="ul1661541793019"></a><a name="ul1661541793019"></a><ul id="ul1661541793019"><li>IAM projects</li><li>Enterprise projects</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34.33343334333433%" headers="mcps1.2.5.1.4 "><a name="ul279419181352"></a><a name="ul279419181352"></a><ul id="ul279419181352"><li>/api/*</li><li>/apis/*</li></ul>
</td>
</tr>
</tbody>
</table>

