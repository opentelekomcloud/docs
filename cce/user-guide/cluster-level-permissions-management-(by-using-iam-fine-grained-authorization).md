# Cluster-Level Permissions Management \(By Using IAM Fine-Grained Authorization\)<a name="cce_01_0168"></a>

Cluster-level permissions management evolves out of the fine-grained authorization feature of IAM. User groups facilitate centralized user management and streamlined permissions management. Users in the same user group have the same permissions. Currently, two default roles are available:  **CCE Admin**  and  **CCE Viewer**. In this chapter, role and permissions policy are interchangeable. Both represent a set of permissions.

## Permissions Granted by the CCE Admin Role<a name="section118851125135817"></a>

An action describes permissions in the format of  _Service name:Resource type:Operation_. The wildcard \(\*\) is allowed to indicate all of the services, resource types, or operations depending on its location in the action.

**Table  1**  Permissions granted by the CCE Admin role

<a name="table65762630"></a>
<table><thead align="left"><tr id="row64098000"><th class="cellrowborder" valign="top" width="20.4%" id="mcps1.2.4.1.1"><p id="p324219918470"><a name="p324219918470"></a><a name="p324219918470"></a>Action</p>
</th>
<th class="cellrowborder" valign="top" width="26.6%" id="mcps1.2.4.1.2"><p id="p181345334206"><a name="p181345334206"></a><a name="p181345334206"></a>Specific Action</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p24555510"><a name="p24555510"></a><a name="p24555510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33671837142011"><td class="cellrowborder" rowspan="19" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p1224309164711"><a name="p1224309164711"></a><a name="p1224309164711"></a>cce:*:*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p1676861712325"><a name="p1676861712325"></a><a name="p1676861712325"></a>cce:cluster:create</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p17681517143220"><a name="p17681517143220"></a><a name="p17681517143220"></a>Create a cluster</p>
</td>
</tr>
<tr id="row1136803716207"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p476951710329"><a name="p476951710329"></a><a name="p476951710329"></a>cce:cluster:delete</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15769181710326"><a name="p15769181710326"></a><a name="p15769181710326"></a>Delete a cluster</p>
</td>
</tr>
<tr id="row236893713200"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1876918172329"><a name="p1876918172329"></a><a name="p1876918172329"></a>cce:cluster:update</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p157698171326"><a name="p157698171326"></a><a name="p157698171326"></a>Update a cluster, for example, update cluster node scheduling parameters and provide RBAC support to clusters</p>
</td>
</tr>
<tr id="row14369237182014"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1876971713322"><a name="p1876971713322"></a><a name="p1876971713322"></a>cce:cluster:upgrade</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16770181763217"><a name="p16770181763217"></a><a name="p16770181763217"></a>Upgrade a cluster</p>
</td>
</tr>
<tr id="row336911371201"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20770131713323"><a name="p20770131713323"></a><a name="p20770131713323"></a>cce:cluster:start</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p97708172320"><a name="p97708172320"></a><a name="p97708172320"></a>Wake up a cluster</p>
</td>
</tr>
<tr id="row10369173792011"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6770111743216"><a name="p6770111743216"></a><a name="p6770111743216"></a>cce:cluster:stop</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p477121710323"><a name="p477121710323"></a><a name="p477121710323"></a>Hibernate a cluster</p>
</td>
</tr>
<tr id="row9371153720209"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p10772181753213"><a name="p10772181753213"></a><a name="p10772181753213"></a>cce:cluster:list</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p10772817153214"><a name="p10772817153214"></a><a name="p10772817153214"></a>List all clusters</p>
</td>
</tr>
<tr id="row1337193719205"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1377251712329"><a name="p1377251712329"></a><a name="p1377251712329"></a>cce:cluster:get</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1877361717328"><a name="p1877361717328"></a><a name="p1877361717328"></a>Query cluster details</p>
</td>
</tr>
<tr id="row183721437152013"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p27731617163219"><a name="p27731617163219"></a><a name="p27731617163219"></a>cce:node:create</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p107738172328"><a name="p107738172328"></a><a name="p107738172328"></a>Add a cluster node</p>
</td>
</tr>
<tr id="row1337223782012"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20773017103210"><a name="p20773017103210"></a><a name="p20773017103210"></a>cce:node:delete</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p10774717183215"><a name="p10774717183215"></a><a name="p10774717183215"></a>Delete one or more nodes</p>
</td>
</tr>
<tr id="row537316378201"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1177471718323"><a name="p1177471718323"></a><a name="p1177471718323"></a>cce:node:update</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p187751317163218"><a name="p187751317163218"></a><a name="p187751317163218"></a>Update a cluster node, for example, update the node name</p>
</td>
</tr>
<tr id="row9374137182017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p077512178326"><a name="p077512178326"></a><a name="p077512178326"></a>cce:node:get</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2775131773214"><a name="p2775131773214"></a><a name="p2775131773214"></a>Query node details</p>
</td>
</tr>
<tr id="row95581429192015"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1777551743217"><a name="p1777551743217"></a><a name="p1777551743217"></a>cce:node:list</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p5775181718326"><a name="p5775181718326"></a><a name="p5775181718326"></a>List all nodes</p>
</td>
</tr>
<tr id="row4559162992016"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p177641773220"><a name="p177641773220"></a><a name="p177641773220"></a>cce:job:list</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17776517113217"><a name="p17776517113217"></a><a name="p17776517113217"></a>List all cluster jobs</p>
</td>
</tr>
<tr id="row195591929132018"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1877691723215"><a name="p1877691723215"></a><a name="p1877691723215"></a>cce:job:delete</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2777817153217"><a name="p2777817153217"></a><a name="p2777817153217"></a>Delete one or more cluster jobs</p>
</td>
</tr>
<tr id="row2056082962010"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p77771517193210"><a name="p77771517193210"></a><a name="p77771517193210"></a>cce:job:get</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p777718179327"><a name="p777718179327"></a><a name="p777718179327"></a>Read a specified cluster job</p>
</td>
</tr>
<tr id="row176811342112812"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p568154232816"><a name="p568154232816"></a><a name="p568154232816"></a>cce:storage:create</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16681642142819"><a name="p16681642142819"></a><a name="p16681642142819"></a>Create a storage</p>
</td>
</tr>
<tr id="row17431133642816"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6432636162813"><a name="p6432636162813"></a><a name="p6432636162813"></a>cce:storage:delete</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9432133662812"><a name="p9432133662812"></a><a name="p9432133662812"></a>Delete a storage</p>
</td>
</tr>
<tr id="row1355001813192"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13551111818196"><a name="p13551111818196"></a><a name="p13551111818196"></a>cce:kubernetes:*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p19551121810199"><a name="p19551121810199"></a><a name="p19551121810199"></a>Perform operations on all Kubernetes resources. For details, see <a href="namespace-level-permissions-management-(by-using-kubernetes-rbac-authorization).md">Namespace-Level Permissions Management</a>.</p>
</td>
</tr>
<tr id="row7655154602020"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p1592752614810"><a name="p1592752614810"></a><a name="p1592752614810"></a>ecs:*:*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p52094246485"><a name="p52094246485"></a><a name="p52094246485"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p540810333219"><a name="p540810333219"></a><a name="p540810333219"></a>Perform all operations on Elastic Cloud Servers (ECSs)</p>
</td>
</tr>
<tr id="row13685854112019"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p5243793476"><a name="p5243793476"></a><a name="p5243793476"></a>evs:*:*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p1668516546206"><a name="p1668516546206"></a><a name="p1668516546206"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p5545230133217"><a name="p5545230133217"></a><a name="p5545230133217"></a>Perform all operations on Elastic Volume Service (EVS) disks.</p>
<p id="p1666335113594"><a name="p1666335113594"></a><a name="p1666335113594"></a>EVS disks can be attached to cloud servers and scaled to a higher capacity whenever needed.</p>
</td>
</tr>
<tr id="row1222410528205"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p7243119174718"><a name="p7243119174718"></a><a name="p7243119174718"></a>vpc:*:*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p48939132447"><a name="p48939132447"></a><a name="p48939132447"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p112083121013"><a name="p112083121013"></a><a name="p112083121013"></a>Perform all operations on Virtual Private Clouds (VPCs), including enhanced load balancers.</p>
<p id="p8937625175814"><a name="p8937625175814"></a><a name="p8937625175814"></a>A cluster must run in a VPC. When creating a namespace, you need to create or associate a VPC for the namespace so that all containers in the namespace will run in the VPC.</p>
</td>
</tr>
<tr id="row11629359101313"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p1624315964717"><a name="p1624315964717"></a><a name="p1624315964717"></a>sfs:*:get*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p17630135981318"><a name="p17630135981318"></a><a name="p17630135981318"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p16630659191317"><a name="p16630659191317"></a><a name="p16630659191317"></a>View Scalable File Service (SFS) resource details</p>
</td>
</tr>
<tr id="row630418590147"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p14243598475"><a name="p14243598475"></a><a name="p14243598475"></a>aom:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p630419599143"><a name="p630419599143"></a><a name="p630419599143"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p630475941416"><a name="p630475941416"></a><a name="p630475941416"></a>View Application Operations Management (AOM) resource details</p>
</td>
</tr>
<tr id="row1767414251516"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p6244119134714"><a name="p6244119134714"></a><a name="p6244119134714"></a>aom:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p26757261518"><a name="p26757261518"></a><a name="p26757261518"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p116753241514"><a name="p116753241514"></a><a name="p116753241514"></a>List AOM resources</p>
</td>
</tr>
<tr id="row873810362151"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p182440912479"><a name="p182440912479"></a><a name="p182440912479"></a>aom:autoScalingRule:*</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p177391236101516"><a name="p177391236101516"></a><a name="p177391236101516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p2739836171516"><a name="p2739836171516"></a><a name="p2739836171516"></a>Perform all operations on AOM auto scaling rules</p>
</td>
</tr>
</tbody>
</table>

## Permissions Granted by the CCE Viewer Role<a name="section20532642173311"></a>

The default role  **CCE Viewer**  has the following permissions:

**Table  2**  Permissions granted by the CCE Viewer role

<a name="table11562191511348"></a>
<table><thead align="left"><tr id="row156351513348"><th class="cellrowborder" valign="top" width="19.97%" id="mcps1.2.4.1.1"><p id="p19661557182112"><a name="p19661557182112"></a><a name="p19661557182112"></a>Action</p>
</th>
<th class="cellrowborder" valign="top" width="27.029999999999998%" id="mcps1.2.4.1.2"><p id="p3563121543416"><a name="p3563121543416"></a><a name="p3563121543416"></a>Specific Action</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p16563171517347"><a name="p16563171517347"></a><a name="p16563171517347"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20566115103417"><td class="cellrowborder" rowspan="3" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p2966115711217"><a name="p2966115711217"></a><a name="p2966115711217"></a>cce:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p13566141543417"><a name="p13566141543417"></a><a name="p13566141543417"></a>cce:cluster:get</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1356651553417"><a name="p1356651553417"></a><a name="p1356651553417"></a>Query cluster details</p>
</td>
</tr>
<tr id="row1356613154348"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1756601513346"><a name="p1756601513346"></a><a name="p1756601513346"></a>cce:node:get</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p956719151343"><a name="p956719151343"></a><a name="p956719151343"></a>Query node details</p>
</td>
</tr>
<tr id="row5568101519341"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16568111523419"><a name="p16568111523419"></a><a name="p16568111523419"></a>cce:job:get</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p55681415203415"><a name="p55681415203415"></a><a name="p55681415203415"></a>Read a specified cluster job</p>
</td>
</tr>
<tr id="row155691015153414"><td class="cellrowborder" rowspan="3" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p79669573215"><a name="p79669573215"></a><a name="p79669573215"></a>cce:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p135694150342"><a name="p135694150342"></a><a name="p135694150342"></a>cce:cluster:list</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p75691115123419"><a name="p75691115123419"></a><a name="p75691115123419"></a>List all clusters</p>
</td>
</tr>
<tr id="row95691715183418"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p556931517348"><a name="p556931517348"></a><a name="p556931517348"></a>cce:node:list</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1256915155349"><a name="p1256915155349"></a><a name="p1256915155349"></a>List all nodes</p>
</td>
</tr>
<tr id="row65691715113412"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17569131533419"><a name="p17569131533419"></a><a name="p17569131533419"></a>cce:job:list</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p456915157347"><a name="p456915157347"></a><a name="p456915157347"></a>List all cluster jobs</p>
</td>
</tr>
<tr id="row170241171817"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p159661457192112"><a name="p159661457192112"></a><a name="p159661457192112"></a>cce:kubernetes:*</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p77016415184"><a name="p77016415184"></a><a name="p77016415184"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p18702412180"><a name="p18702412180"></a><a name="p18702412180"></a>Perform operations on all Kubernetes resources. For details, see <a href="namespace-level-permissions-management-(by-using-kubernetes-rbac-authorization).md">Namespace-Level Permissions Management</a>.</p>
</td>
</tr>
<tr id="row1557101593414"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p15966145792119"><a name="p15966145792119"></a><a name="p15966145792119"></a>ecs:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p1457113151345"><a name="p1457113151345"></a><a name="p1457113151345"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1357112152343"><a name="p1357112152343"></a><a name="p1357112152343"></a>View details of all resources on an ECS.</p>
<p id="p957215152348"><a name="p957215152348"></a><a name="p957215152348"></a>An ECS with multiple EVS disks is a cluster node in CCE.</p>
</td>
</tr>
<tr id="row486071571816"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p14966175712219"><a name="p14966175712219"></a><a name="p14966175712219"></a>ecs:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p786101511810"><a name="p786101511810"></a><a name="p786101511810"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p118611115101816"><a name="p118611115101816"></a><a name="p118611115101816"></a>List all resources on an ECS</p>
</td>
</tr>
<tr id="row2572115143411"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p4966195742117"><a name="p4966195742117"></a><a name="p4966195742117"></a>evs:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p135727155348"><a name="p135727155348"></a><a name="p135727155348"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1957301523411"><a name="p1957301523411"></a><a name="p1957301523411"></a>View details of all EVS disk resources EVS disks can be attached to cloud servers and scaled to a higher capacity whenever needed.</p>
</td>
</tr>
<tr id="row4788111418218"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p4966357132115"><a name="p4966357132115"></a><a name="p4966357132115"></a>evs:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p578813141211"><a name="p578813141211"></a><a name="p578813141211"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p11788141442118"><a name="p11788141442118"></a><a name="p11788141442118"></a>List all EVS resources</p>
</td>
</tr>
<tr id="row17392173118217"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p109661579216"><a name="p109661579216"></a><a name="p109661579216"></a>evs:*:count</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p16392103172111"><a name="p16392103172111"></a><a name="p16392103172111"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1239210311211"><a name="p1239210311211"></a><a name="p1239210311211"></a>-</p>
</td>
</tr>
<tr id="row12573171515343"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p296715782120"><a name="p296715782120"></a><a name="p296715782120"></a>vpc:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p65732151343"><a name="p65732151343"></a><a name="p65732151343"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p55734154348"><a name="p55734154348"></a><a name="p55734154348"></a>View details of all VPC resources (including enhanced load balancers)</p>
<p id="p1557361573415"><a name="p1557361573415"></a><a name="p1557361573415"></a>A cluster must run in a VPC. When creating a namespace, you need to create or associate a VPC for the namespace so that all containers in the namespace will run in the VPC.</p>
</td>
</tr>
<tr id="row178108018228"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p296725702114"><a name="p296725702114"></a><a name="p296725702114"></a>vpc:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p19810120192214"><a name="p19810120192214"></a><a name="p19810120192214"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p48104012227"><a name="p48104012227"></a><a name="p48104012227"></a>List all VPC resources (including enhanced load balancers)</p>
</td>
</tr>
<tr id="row12542155562412"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p896735715219"><a name="p896735715219"></a><a name="p896735715219"></a>sfs:*:get*</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p554285511240"><a name="p554285511240"></a><a name="p554285511240"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1954215550240"><a name="p1954215550240"></a><a name="p1954215550240"></a>View Scalable File Service (SFS) resource details</p>
</td>
</tr>
<tr id="row5862111011257"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p2096735718214"><a name="p2096735718214"></a><a name="p2096735718214"></a>aom:*:get</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p28624105258"><a name="p28624105258"></a><a name="p28624105258"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p28621210162516"><a name="p28621210162516"></a><a name="p28621210162516"></a>View Application Operations Management (AOM) resource details</p>
</td>
</tr>
<tr id="row1197081652510"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p99674573218"><a name="p99674573218"></a><a name="p99674573218"></a>aom:*:list</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p7970416152513"><a name="p7970416152513"></a><a name="p7970416152513"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p10970151614255"><a name="p10970151614255"></a><a name="p10970151614255"></a>List all AOM resources</p>
</td>
</tr>
<tr id="row107584135256"><td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.2.4.1.1 "><p id="p3967205716219"><a name="p3967205716219"></a><a name="p3967205716219"></a>aom:autoScalingRule:*</p>
</td>
<td class="cellrowborder" valign="top" width="27.029999999999998%" headers="mcps1.2.4.1.2 "><p id="p475811392517"><a name="p475811392517"></a><a name="p475811392517"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p575812138257"><a name="p575812138257"></a><a name="p575812138257"></a>Perform all operations on AOM auto scaling rules</p>
</td>
</tr>
</tbody>
</table>

