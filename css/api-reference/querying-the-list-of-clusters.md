# Querying the List of Clusters<a name="css_03_0018"></a>

## Function<a name="section139713321413"></a>

This API is used to query and display the cluster list and cluster status.

## URI<a name="section117917455419"></a>

```
GET /v1.0/{project_id}/clusters
```

**Table  1**  Parameter description

<a name="table122471622164219"></a>
<table><thead align="left"><tr id="row3277722174218"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p22775224425"><a name="p22775224425"></a><a name="p22775224425"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p132781122134213"><a name="p132781122134213"></a><a name="p132781122134213"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.3"><p id="p1627842254215"><a name="p1627842254215"></a><a name="p1627842254215"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p527842214429"><a name="p527842214429"></a><a name="p527842214429"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row727812216429"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p727814223429"><a name="p727814223429"></a><a name="p727814223429"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p7278202204212"><a name="p7278202204212"></a><a name="p7278202204212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p13278122294220"><a name="p13278122294220"></a><a name="p13278122294220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8278122213423"><a name="p8278122213423"></a><a name="p8278122213423"></a>Project ID.</p>
</td>
</tr>
<tr id="row288124713592"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p14974120409"><a name="p14974120409"></a><a name="p14974120409"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p79741001606"><a name="p79741001606"></a><a name="p79741001606"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p20974803013"><a name="p20974803013"></a><a name="p20974803013"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p49741306019"><a name="p49741306019"></a><a name="p49741306019"></a>Start value of the query. The default value is 1, indicating that the query starts from the first cluster.</p>
</td>
</tr>
<tr id="row75125712591"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p697419013018"><a name="p697419013018"></a><a name="p697419013018"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p119741601605"><a name="p119741601605"></a><a name="p119741601605"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p15974503020"><a name="p15974503020"></a><a name="p15974503020"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p59741011015"><a name="p59741011015"></a><a name="p59741011015"></a>Number of clusters to be queried. The default value is 10, indicating that 10 clusters are queried at a time.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section4136174564211"></a>

None

## Response<a name="section1756817474311"></a>

[Table 2](#table29413185430)  describes the response parameters.

**Table  2**  Parameter description

<a name="table29413185430"></a>
<table><thead align="left"><tr id="row4149121944318"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p614911197434"><a name="p614911197434"></a><a name="p614911197434"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p12149111974320"><a name="p12149111974320"></a><a name="p12149111974320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p11149171944314"><a name="p11149171944314"></a><a name="p11149171944314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row151491199431"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p191497198431"><a name="p191497198431"></a><a name="p191497198431"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p19149219124316"><a name="p19149219124316"></a><a name="p19149219124316"></a>Array of clusters objects</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p11491819144310"><a name="p11491819144310"></a><a name="p11491819144310"></a>List of cluster objects. For details, see <a href="#table9282914163610">Table 3</a>.</p>
</td>
</tr>
<tr id="row11149201954311"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1914931917439"><a name="p1914931917439"></a><a name="p1914931917439"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p11149191914313"><a name="p11149191914313"></a><a name="p11149191914313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p81491019174319"><a name="p81491019174319"></a><a name="p81491019174319"></a>Last modification time of a cluster. The format is <strong id="b85741858173115"><a name="b85741858173115"></a><a name="b85741858173115"></a>ISO8601: CCYY-MM-DDThh:mm:ss</strong>.</p>
</td>
</tr>
<tr id="row16149111944310"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p514941984311"><a name="p514941984311"></a><a name="p514941984311"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p714914196436"><a name="p714914196436"></a><a name="p714914196436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p12149141917435"><a name="p12149141917435"></a><a name="p12149141917435"></a>Cluster name.</p>
</td>
</tr>
<tr id="row1014981919434"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p12149519174314"><a name="p12149519174314"></a><a name="p12149519174314"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p6149619174316"><a name="p6149619174316"></a><a name="p6149619174316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p814921984315"><a name="p814921984315"></a><a name="p814921984315"></a>Time when a cluster is created. The format is <strong id="b097012147321"><a name="b097012147321"></a><a name="b097012147321"></a>ISO8601: CCYY-MM-DDThh:mm:ss</strong>.</p>
<div class="note" id="note15267102019118"><a name="note15267102019118"></a><a name="note15267102019118"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7268152011118"><a name="p7268152011118"></a><a name="p7268152011118"></a>The returned cluster list is sorted by creation time in descending order. Specifically, the cluster with the latest creation time is at the top.</p>
</div></div>
</td>
</tr>
<tr id="row11149101994318"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p7149121974318"><a name="p7149121974318"></a><a name="p7149121974318"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p1414921994314"><a name="p1414921994314"></a><a name="p1414921994314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p5149151920435"><a name="p5149151920435"></a><a name="p5149151920435"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row1214931913432"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1115041918437"><a name="p1115041918437"></a><a name="p1115041918437"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p51501219194319"><a name="p51501219194319"></a><a name="p51501219194319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1615051920435"><a name="p1615051920435"></a><a name="p1615051920435"></a>Return value.</p>
<a name="ul4150519114313"></a><a name="ul4150519114313"></a><ul id="ul4150519114313"><li><strong id="b84235270621011"><a name="b84235270621011"></a><a name="b84235270621011"></a>100</strong>: The cluster is being created.</li><li><strong id="b842352706103933"><a name="b842352706103933"></a><a name="b842352706103933"></a>200</strong>: The cluster is available.</li><li><strong id="b842352706103945"><a name="b842352706103945"></a><a name="b842352706103945"></a>303</strong>: The cluster is unavailable.</li></ul>
</td>
</tr>
<tr id="row6150161915439"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p191501019204311"><a name="p191501019204311"></a><a name="p191501019204311"></a>endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p8150161910432"><a name="p8150161910432"></a><a name="p8150161910432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p11502196435"><a name="p11502196435"></a><a name="p11502196435"></a>Indicates the IP address and port number of the user used to access the VPC.</p>
</td>
</tr>
<tr id="row155651249193812"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p156516499385"><a name="p156516499385"></a><a name="p156516499385"></a>actionProgress</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p356564933817"><a name="p356564933817"></a><a name="p356564933817"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p18565114933810"><a name="p18565114933810"></a><a name="p18565114933810"></a>Cluster operation progress, which indicates the progress of cluster creation and expansion in percentage. <strong id="b350518228231"><a name="b350518228231"></a><a name="b350518228231"></a>CREATING</strong> specifies the progress of creation.</p>
</td>
</tr>
<tr id="row413014373917"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p17130124323920"><a name="p17130124323920"></a><a name="p17130124323920"></a>actions</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p51301043163914"><a name="p51301043163914"></a><a name="p51301043163914"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p153001932115510"><a name="p153001932115510"></a><a name="p153001932115510"></a>Current behavior on a cluster. Value <strong id="b679445135411"><a name="b679445135411"></a><a name="b679445135411"></a>REBOOTING</strong> indicates that the cluster is being restarted, <strong id="b4795451135415"><a name="b4795451135415"></a><a name="b4795451135415"></a>GROWING</strong> indicates that capacity expansion is being performed on the cluster, <strong id="b7797451105419"><a name="b7797451105419"></a><a name="b7797451105419"></a>RESTORING</strong> indicates that the cluster is being restored, and <strong id="b137976519542"><a name="b137976519542"></a><a name="b137976519542"></a>SNAPSHOTTING</strong> indicates that the snapshot is being created.</p>
</td>
</tr>
<tr id="row74291511811"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p184292111710"><a name="p184292111710"></a><a name="p184292111710"></a>failed_reasons</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p542941113112"><a name="p542941113112"></a><a name="p542941113112"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1542912113115"><a name="p1542912113115"></a><a name="p1542912113115"></a>Failure cause. If the cluster is in the Available state, this parameter is not returned. For details, see <a href="#table8178483813">Table 6</a>.</p>
</td>
</tr>
<tr id="row17234113252420"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p159683215247"><a name="p159683215247"></a><a name="p159683215247"></a>httpsEnable</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p259612323242"><a name="p259612323242"></a><a name="p259612323242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1059663272410"><a name="p1059663272410"></a><a name="p1059663272410"></a>Communication encryption status.</p>
<p id="p45811323112515"><a name="p45811323112515"></a><a name="p45811323112515"></a>Value <strong id="b16437155910303"><a name="b16437155910303"></a><a name="b16437155910303"></a>false</strong> indicates that communication encryption is not enabled.</p>
<p id="p1049103413259"><a name="p1049103413259"></a><a name="p1049103413259"></a>Value <strong id="b378111119323"><a name="b378111119323"></a><a name="b378111119323"></a>true</strong> indicates that communication encryption is enabled.</p>
</td>
</tr>
<tr id="row864571914810"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1646151911817"><a name="p1646151911817"></a><a name="p1646151911817"></a>diskEncrypted</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p1264681912812"><a name="p1264681912812"></a><a name="p1264681912812"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1564616191089"><a name="p1564616191089"></a><a name="p1564616191089"></a>Whether disks are encrypted.</p>
<a name="ul422423465514"></a><a name="ul422423465514"></a><ul id="ul422423465514"><li>Value <strong id="b317033913413"><a name="b317033913413"></a><a name="b317033913413"></a>true</strong> indicates that disks are encrypted.</li><li>Value <strong id="b142591752184119"><a name="b142591752184119"></a><a name="b142591752184119"></a>false</strong> indicates that disks are not encrypted.</li></ul>
</td>
</tr>
<tr id="row18414585102"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p141414813108"><a name="p141414813108"></a><a name="p141414813108"></a>cmkId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p104148841011"><a name="p104148841011"></a><a name="p104148841011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p84142817108"><a name="p84142817108"></a><a name="p84142817108"></a>Key ID used for disk encryption.</p>
</td>
</tr>
<tr id="row1370552412295"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p12706182413297"><a name="p12706182413297"></a><a name="p12706182413297"></a>vpcId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p77061924162910"><a name="p77061924162910"></a><a name="p77061924162910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p13706112422917"><a name="p13706112422917"></a><a name="p13706112422917"></a>VPC ID.</p>
</td>
</tr>
<tr id="row147634418317"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p876318463116"><a name="p876318463116"></a><a name="p876318463116"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p1676314103119"><a name="p1676314103119"></a><a name="p1676314103119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p20763944311"><a name="p20763944311"></a><a name="p20763944311"></a>Subnet ID.</p>
</td>
</tr>
<tr id="row1545617535312"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p12456145311313"><a name="p12456145311313"></a><a name="p12456145311313"></a>securityGroupId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p1145615311314"><a name="p1145615311314"></a><a name="p1145615311314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p3456125353110"><a name="p3456125353110"></a><a name="p3456125353110"></a>Security group ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **clusters**  field data structure description

<a name="table9282914163610"></a>
<table><thead align="left"><tr id="row1528231473610"><th class="cellrowborder" valign="top" width="25.353535353535356%" id="mcps1.2.4.1.1"><p id="p980024833617"><a name="p980024833617"></a><a name="p980024833617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.202020202020204%" id="mcps1.2.4.1.2"><p id="p78001648113620"><a name="p78001648113620"></a><a name="p78001648113620"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.44444444444444%" id="mcps1.2.4.1.3"><p id="p17800114815360"><a name="p17800114815360"></a><a name="p17800114815360"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1828241419368"><td class="cellrowborder" valign="top" width="25.353535353535356%" headers="mcps1.2.4.1.1 "><p id="p886374511362"><a name="p886374511362"></a><a name="p886374511362"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="26.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p12878194514368"><a name="p12878194514368"></a><a name="p12878194514368"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.44444444444444%" headers="mcps1.2.4.1.3 "><p id="p4878184511366"><a name="p4878184511366"></a><a name="p4878184511366"></a>Type of the data search engine. For details, see <a href="#table9975151812430">Table 4</a>.</p>
</td>
</tr>
<tr id="row192821014153614"><td class="cellrowborder" valign="top" width="25.353535353535356%" headers="mcps1.2.4.1.1 "><p id="p887864510362"><a name="p887864510362"></a><a name="p887864510362"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="26.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p188781745123613"><a name="p188781745123613"></a><a name="p188781745123613"></a>Array of instance objects</p>
</td>
<td class="cellrowborder" valign="top" width="48.44444444444444%" headers="mcps1.2.4.1.3 "><p id="p158784457364"><a name="p158784457364"></a><a name="p158784457364"></a>List of node objects. For details, see <a href="#table13982151814439">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **datastore**  field data structure description

<a name="table9975151812430"></a>
<table><thead align="left"><tr id="row13150121911438"><th class="cellrowborder" valign="top" width="25.622562256225624%" id="mcps1.2.4.1.1"><p id="p31501719104317"><a name="p31501719104317"></a><a name="p31501719104317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.1025102510251%" id="mcps1.2.4.1.2"><p id="p0150319114315"><a name="p0150319114315"></a><a name="p0150319114315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.27492749274928%" id="mcps1.2.4.1.3"><p id="p51501519184319"><a name="p51501519184319"></a><a name="p51501519184319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4150101911430"><td class="cellrowborder" valign="top" width="25.622562256225624%" headers="mcps1.2.4.1.1 "><p id="p5150131914312"><a name="p5150131914312"></a><a name="p5150131914312"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25.1025102510251%" headers="mcps1.2.4.1.2 "><p id="p13150101914312"><a name="p13150101914312"></a><a name="p13150101914312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27492749274928%" headers="mcps1.2.4.1.3 "><p id="p121511419174313"><a name="p121511419174313"></a><a name="p121511419174313"></a>Supported type: elasticsearch</p>
</td>
</tr>
<tr id="row12151101984314"><td class="cellrowborder" valign="top" width="25.622562256225624%" headers="mcps1.2.4.1.1 "><p id="p01511719204313"><a name="p01511719204313"></a><a name="p01511719204313"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="25.1025102510251%" headers="mcps1.2.4.1.2 "><p id="p16151201913437"><a name="p16151201913437"></a><a name="p16151201913437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27492749274928%" headers="mcps1.2.4.1.3 "><p id="p8151191912439"><a name="p8151191912439"></a><a name="p8151191912439"></a>Engine version number. The current engine version is 6.2.3.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **instances**  field data structure description

<a name="table13982151814439"></a>
<table><thead align="left"><tr id="row1215121974312"><th class="cellrowborder" valign="top" width="23.962396239623963%" id="mcps1.2.4.1.1"><p id="p14151181964317"><a name="p14151181964317"></a><a name="p14151181964317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.112311231123112%" id="mcps1.2.4.1.2"><p id="p17151201911433"><a name="p17151201911433"></a><a name="p17151201911433"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.92529252925292%" id="mcps1.2.4.1.3"><p id="p1151161944313"><a name="p1151161944313"></a><a name="p1151161944313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1815117192431"><td class="cellrowborder" valign="top" width="23.962396239623963%" headers="mcps1.2.4.1.1 "><p id="p11151101920433"><a name="p11151101920433"></a><a name="p11151101920433"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="23.112311231123112%" headers="mcps1.2.4.1.2 "><p id="p2015271994316"><a name="p2015271994316"></a><a name="p2015271994316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.92529252925292%" headers="mcps1.2.4.1.3 "><p id="p10152191964318"><a name="p10152191964318"></a><a name="p10152191964318"></a>Supported type: ess (indicating the Elasticsearch node)</p>
</td>
</tr>
<tr id="row01521919194312"><td class="cellrowborder" valign="top" width="23.962396239623963%" headers="mcps1.2.4.1.1 "><p id="p51521019134316"><a name="p51521019134316"></a><a name="p51521019134316"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.112311231123112%" headers="mcps1.2.4.1.2 "><p id="p2015211914310"><a name="p2015211914310"></a><a name="p2015211914310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.92529252925292%" headers="mcps1.2.4.1.3 "><p id="p61523191437"><a name="p61523191437"></a><a name="p61523191437"></a>Instance ID.</p>
</td>
</tr>
<tr id="row1515291994319"><td class="cellrowborder" valign="top" width="23.962396239623963%" headers="mcps1.2.4.1.1 "><p id="p715212193434"><a name="p715212193434"></a><a name="p715212193434"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.112311231123112%" headers="mcps1.2.4.1.2 "><p id="p715241915437"><a name="p715241915437"></a><a name="p715241915437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.92529252925292%" headers="mcps1.2.4.1.3 "><p id="p1615251915435"><a name="p1615251915435"></a><a name="p1615251915435"></a>Instance name.</p>
</td>
</tr>
<tr id="row2015291934315"><td class="cellrowborder" valign="top" width="23.962396239623963%" headers="mcps1.2.4.1.1 "><p id="p8152101944315"><a name="p8152101944315"></a><a name="p8152101944315"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23.112311231123112%" headers="mcps1.2.4.1.2 "><p id="p201521219114311"><a name="p201521219114311"></a><a name="p201521219114311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.92529252925292%" headers="mcps1.2.4.1.3 "><p id="p121521196435"><a name="p121521196435"></a><a name="p121521196435"></a>Instance state.</p>
<a name="ul16840111884318"></a><a name="ul16840111884318"></a><ul id="ul16840111884318"><li><strong id="b19472182915515"><a name="b19472182915515"></a><a name="b19472182915515"></a>100</strong>: The instance is being created.</li><li><strong id="b444678707"><a name="b444678707"></a><a name="b444678707"></a>200</strong>: The instance is available.</li><li><strong id="b614959071"><a name="b614959071"></a><a name="b614959071"></a>303</strong>: The instance is unavailable.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  6** **failed\_reasons**  field data structure description

<a name="table8178483813"></a>
<table><thead align="left"><tr id="row8253482812"><th class="cellrowborder" valign="top" width="18.98189818981898%" id="mcps1.2.4.1.1"><p id="p18281848480"><a name="p18281848480"></a><a name="p18281848480"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.15261526152615%" id="mcps1.2.4.1.2"><p id="p2312481489"><a name="p2312481489"></a><a name="p2312481489"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.865486548654864%" id="mcps1.2.4.1.3"><p id="p2334487817"><a name="p2334487817"></a><a name="p2334487817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1338648286"><td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.4.1.1 "><p id="p14284815811"><a name="p14284815811"></a><a name="p14284815811"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="26.15261526152615%" headers="mcps1.2.4.1.2 "><p id="p1144134815812"><a name="p1144134815812"></a><a name="p1144134815812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.865486548654864%" headers="mcps1.2.4.1.3 "><p id="p13335142981118"><a name="p13335142981118"></a><a name="p13335142981118"></a>Error code.</p>
<a name="ul83351829161110"></a><a name="ul83351829161110"></a><ul id="ul83351829161110"><li>CSS.6000: indicates that a cluster fails to be created.</li><li>CSS.6001: indicates that capacity expansion of a cluster fails.</li><li>CSS.6002: indicates that a cluster fails to be restarted.</li><li>CSS.6004: indicates that a node fails to be created in a cluster.</li><li>CSS.6005: indicates that the service fails to be initialized.</li></ul>
</td>
</tr>
<tr id="row1048548282"><td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.4.1.1 "><p id="p185013481281"><a name="p185013481281"></a><a name="p185013481281"></a>error_msg</p>
</td>
<td class="cellrowborder" valign="top" width="26.15261526152615%" headers="mcps1.2.4.1.2 "><p id="p155214489814"><a name="p155214489814"></a><a name="p155214489814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.865486548654864%" headers="mcps1.2.4.1.3 "><p id="p65415487814"><a name="p65415487814"></a><a name="p65415487814"></a>Detailed error information.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section17653145262114"></a>

-   Example request
    -   Example request of querying all clusters

        ```
        GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters
        ```

    -   Example request of querying clusters by page

        Example 1: Query the first two clusters.

        Method 1

        ```
        GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters?start=1&limit=2
        ```

        Method 2

        ```
        GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters?limit=2
        ```

        Example 2: Query the first 10 clusters.

        Method 1

        ```
        GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters?start=1&limit=10
        ```

        Method 2

        ```
        GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters?start=1
        ```


-   Example response

    ```
    {
      "clusters": [
        {
          "datastore": {
            "type": "elasticsearch",
            "version": "6.2.3"
          },
          "instances": [
            {
              "status": "200",
              "type": "ess",
              "id": "a8922be2-5e41-4cd1-8486-630c04c2d1e3",
              "name": "ES-new1-ess-esn-1-1"
            }
          ],
          "updated": "2017-11-27T10:36:18",
          "name": "ES-new1",
          "created": "2017-11-27T10:36:18",
          "id": "306e5597-d7a9-4cbe-866c-33428440d0e3",
          "status": "200",
          "endpoint": "192.168.0.219:9200",
          "httpsEnable": false,
          "diskEncrypted" : true,
          "cmkId" : "42546bb1-8025-4ad1-868f-600729c341ae",
          "actionProgress": {
          "CREATING": "5%"
          },
          "actions": []
        },
        {
          "datastore": {
            "type": "elasticsearch",
            "version": "6.2.3"
          },
          "instances": [
            {
              "status": "200",
              "type": "ess",
              "id": "9635de45-895c-45e1-ba0b-d9f497c8ce52",
              "name": "Es-Test1-ess-esn-1-1"
            }
          ],
          "updated": "2017-11-14T12:32:00",
          "name": "Es-Test1",
          "created": "2017-11-14T12:32:00",
          "id": "c99b1514-647e-4418-8b6d-2748255f2f95",
          "status": "200",
          "endpoint": "192.168.0.127:9200",
          "httpsEnable": false,
          "diskEncrypted" : true,
          "cmkId" : "42546bb1-8025-4ad1-868f-600729c341ae",
          "vpcId": "07761987-bb61-4bbf-9d14-a7e6b6909224",
          "subnetId": "675ae21c-cc1c-4fc5-9cb4-4c07fce79648",
          "securityGroupId": "e9e098c8-2116-4b92-823c-036f0f17360b",
          "actionProgress": {},
          "actions": [
            "REBOOTING"
          ]
        }
      ]
    }
    ```


## Status Code<a name="section87962546391"></a>

[Table 7](#table6970123517140)  describes the status code.

**Table  7**  Status code

<a name="table6970123517140"></a>
<table><thead align="left"><tr id="row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="p14560134151414"><a name="p14560134151414"></a><a name="p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="p5563194141411"><a name="p5563194141411"></a><a name="p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="p256616411143"><a name="p256616411143"></a><a name="p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p1957004131410"><a name="p1957004131410"></a><a name="p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="p165731141171419"><a name="p165731141171419"></a><a name="p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="p65778413148"><a name="p65778413148"></a><a name="p65778413148"></a>Invalid request.</p>
<p id="p1557974171415"><a name="p1557974171415"></a><a name="p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p75841441191410"><a name="p75841441191410"></a><a name="p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="p258716416142"><a name="p258716416142"></a><a name="p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="p15589154118141"><a name="p15589154118141"></a><a name="p15589154118141"></a>The requested resource cannot be found.</p>
<p id="p14590164151410"><a name="p14590164151410"></a><a name="p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p13595164131416"><a name="p13595164131416"></a><a name="p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="p9598741131416"><a name="p9598741131416"></a><a name="p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="p659994115146"><a name="p659994115146"></a><a name="p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

