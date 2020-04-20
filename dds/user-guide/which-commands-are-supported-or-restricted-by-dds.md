# Which Commands are Supported or Restricted by DDS?<a name="dds_faq_0033"></a>

The following tables list the commands supported and restricted by DDS.

**Table  1**  Commands supported and restricted by DDS

<a name="table5003377115556"></a>
<table><thead align="left"><tr id="row13067384161429"><th class="cellrowborder" valign="top" width="34.92%" id="mcps1.2.4.1.1"><p id="p50497597161429"><a name="p50497597161429"></a><a name="p50497597161429"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="34.92%" id="mcps1.2.4.1.2"><p id="p63773557161429"><a name="p63773557161429"></a><a name="p63773557161429"></a>Supported Command</p>
</th>
<th class="cellrowborder" valign="top" width="30.159999999999997%" id="mcps1.2.4.1.3"><p id="p13684958115813"><a name="p13684958115813"></a><a name="p13684958115813"></a>Restricted Command</p>
</th>
</tr>
</thead>
<tbody><tr id="row4354929615556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p3783205015556"><a name="p3783205015556"></a><a name="p3783205015556"></a>Aggregates Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p4449722515556"><a name="p4449722515556"></a><a name="p4449722515556"></a>aggregate</p>
<p id="p2489632915556"><a name="p2489632915556"></a><a name="p2489632915556"></a>count</p>
<p id="p3003093815556"><a name="p3003093815556"></a><a name="p3003093815556"></a>distinct</p>
<p id="p6667436928"><a name="p6667436928"></a><a name="p6667436928"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p8764258408"><a name="p8764258408"></a><a name="p8764258408"></a>mapReduce</p>
</td>
</tr>
<tr id="row184298815556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p1506436715556"><a name="p1506436715556"></a><a name="p1506436715556"></a>Geospatial Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p1225419415556"><a name="p1225419415556"></a><a name="p1225419415556"></a>geoNear</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p168495819582"><a name="p168495819582"></a><a name="p168495819582"></a>geoSearch</p>
</td>
</tr>
<tr id="row4317888315556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p782861715556"><a name="p782861715556"></a><a name="p782861715556"></a>Query and Write Operation Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p3013827715556"><a name="p3013827715556"></a><a name="p3013827715556"></a>find</p>
<p id="p2620547415556"><a name="p2620547415556"></a><a name="p2620547415556"></a>insert</p>
<p id="p4487372915556"><a name="p4487372915556"></a><a name="p4487372915556"></a>update</p>
<p id="p3093208415556"><a name="p3093208415556"></a><a name="p3093208415556"></a>delete</p>
<p id="p91128615556"><a name="p91128615556"></a><a name="p91128615556"></a>findAndModify</p>
<p id="p6034810615556"><a name="p6034810615556"></a><a name="p6034810615556"></a>getMore</p>
<p id="p3746386815556"><a name="p3746386815556"></a><a name="p3746386815556"></a>getLastError</p>
<p id="p6496098915556"><a name="p6496098915556"></a><a name="p6496098915556"></a>resetError</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p169418187114"><a name="p169418187114"></a><a name="p169418187114"></a>getPrevError</p>
<p id="p9273182213515"><a name="p9273182213515"></a><a name="p9273182213515"></a>eval</p>
<p id="p01348298515"><a name="p01348298515"></a><a name="p01348298515"></a>parallelCollectionScan</p>
</td>
</tr>
<tr id="row4777799215556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p4481216915556"><a name="p4481216915556"></a><a name="p4481216915556"></a>Query Plan Cache Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p590711115556"><a name="p590711115556"></a><a name="p590711115556"></a>planCacheListFilters</p>
<p id="p1131708015556"><a name="p1131708015556"></a><a name="p1131708015556"></a>planCacheSetFilter</p>
<p id="p6286994715556"><a name="p6286994715556"></a><a name="p6286994715556"></a>planCacheClearFilters</p>
<p id="p6394654915556"><a name="p6394654915556"></a><a name="p6394654915556"></a>planCacheListQueryShapes</p>
<p id="p4348280015556"><a name="p4348280015556"></a><a name="p4348280015556"></a>planCacheListPlans</p>
<p id="p2357743815556"><a name="p2357743815556"></a><a name="p2357743815556"></a>planCacheClear</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p11193105312111"><a name="p11193105312111"></a><a name="p11193105312111"></a>-</p>
</td>
</tr>
<tr id="row1087035815556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p808383715556"><a name="p808383715556"></a><a name="p808383715556"></a>Authentication Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p5081102315556"><a name="p5081102315556"></a><a name="p5081102315556"></a>logout</p>
<p id="p6425220515556"><a name="p6425220515556"></a><a name="p6425220515556"></a>authenticate</p>
<p id="p5843953715556"><a name="p5843953715556"></a><a name="p5843953715556"></a>getnonce</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p71491802213"><a name="p71491802213"></a><a name="p71491802213"></a>authSchemaUpgrade</p>
<p id="p5336153141918"><a name="p5336153141918"></a><a name="p5336153141918"></a>copydbgetnonce</p>
</td>
</tr>
<tr id="row2022411425614"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p192243421568"><a name="p192243421568"></a><a name="p192243421568"></a>User Management Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p57147136211"><a name="p57147136211"></a><a name="p57147136211"></a>createUser</p>
<p id="p10714213142117"><a name="p10714213142117"></a><a name="p10714213142117"></a>updateUser</p>
<p id="p1573091317215"><a name="p1573091317215"></a><a name="p1573091317215"></a>dropUser</p>
<p id="p97301813182114"><a name="p97301813182114"></a><a name="p97301813182114"></a>dropAllUsersFromDatabase</p>
<p id="p11730111342117"><a name="p11730111342117"></a><a name="p11730111342117"></a>grantRolesToUser</p>
<p id="p1374641332117"><a name="p1374641332117"></a><a name="p1374641332117"></a>revokeRolesFromUser</p>
<p id="p1474651322111"><a name="p1474651322111"></a><a name="p1474651322111"></a>usersInfo</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p8755192718813"><a name="p8755192718813"></a><a name="p8755192718813"></a>-</p>
</td>
</tr>
<tr id="row5619379215556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p5540330215556"><a name="p5540330215556"></a><a name="p5540330215556"></a>Role Management Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p5848244815556"><a name="p5848244815556"></a><a name="p5848244815556"></a>invalidateUserCache</p>
<p id="p12949193611213"><a name="p12949193611213"></a><a name="p12949193611213"></a>createRole</p>
<p id="p1694912368219"><a name="p1694912368219"></a><a name="p1694912368219"></a>updateRole</p>
<p id="p494919360214"><a name="p494919360214"></a><a name="p494919360214"></a>dropRole</p>
<p id="p4964113622119"><a name="p4964113622119"></a><a name="p4964113622119"></a>dropAllRolesFromDatabase</p>
<p id="p1696463612120"><a name="p1696463612120"></a><a name="p1696463612120"></a>grantPrivilegesToRole</p>
<p id="p11964113618213"><a name="p11964113618213"></a><a name="p11964113618213"></a>revokePrivilegesFromRole</p>
<p id="p9964836182116"><a name="p9964836182116"></a><a name="p9964836182116"></a>grantRolesToRole</p>
<p id="p69801336122120"><a name="p69801336122120"></a><a name="p69801336122120"></a>revokeRolesFromRole</p>
<p id="p1598053622110"><a name="p1598053622110"></a><a name="p1598053622110"></a>rolesInfo</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p876144115812"><a name="p876144115812"></a><a name="p876144115812"></a>-</p>
</td>
</tr>
<tr id="row5657998615556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p1957615815556"><a name="p1957615815556"></a><a name="p1957615815556"></a>Replication Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p4216496215556"><a name="p4216496215556"></a><a name="p4216496215556"></a>isMaster</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p89913198153"><a name="p89913198153"></a><a name="p89913198153"></a>replSetElect</p>
<p id="p119971921511"><a name="p119971921511"></a><a name="p119971921511"></a>replSetUpdatePosition</p>
<p id="p91007193158"><a name="p91007193158"></a><a name="p91007193158"></a>appendOplogNote</p>
<p id="p2100141915159"><a name="p2100141915159"></a><a name="p2100141915159"></a>replSetFreeze</p>
<p id="p21001819101510"><a name="p21001819101510"></a><a name="p21001819101510"></a>replSetGetStatus</p>
<p id="p610013191150"><a name="p610013191150"></a><a name="p610013191150"></a>replSetInitiate</p>
<p id="p141002019181515"><a name="p141002019181515"></a><a name="p141002019181515"></a>replSetMaintenance</p>
<p id="p310021913151"><a name="p310021913151"></a><a name="p310021913151"></a>replSetReconfig</p>
<p id="p410051916155"><a name="p410051916155"></a><a name="p410051916155"></a>replSetStepDown</p>
<p id="p010018196155"><a name="p010018196155"></a><a name="p010018196155"></a>replSetSyncFrom</p>
<p id="p310011192157"><a name="p310011192157"></a><a name="p310011192157"></a>resync</p>
<p id="p161003191156"><a name="p161003191156"></a><a name="p161003191156"></a>applyOps</p>
<p id="p1210021981520"><a name="p1210021981520"></a><a name="p1210021981520"></a>replSetGetConfig</p>
</td>
</tr>
<tr id="row4394034515556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p239821315556"><a name="p239821315556"></a><a name="p239821315556"></a>Sharding Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p6003759815556"><a name="p6003759815556"></a><a name="p6003759815556"></a>enableSharding</p>
<p id="p1243002515556"><a name="p1243002515556"></a><a name="p1243002515556"></a>getShardVersion</p>
<p id="p179193915556"><a name="p179193915556"></a><a name="p179193915556"></a>mergeChunks</p>
<p id="p3125550315556"><a name="p3125550315556"></a><a name="p3125550315556"></a>shardCollection</p>
<p id="p3535730515556"><a name="p3535730515556"></a><a name="p3535730515556"></a>split</p>
<p id="p567157015556"><a name="p567157015556"></a><a name="p567157015556"></a>splitChunk</p>
<p id="p4093413415556"><a name="p4093413415556"></a><a name="p4093413415556"></a>splitVector</p>
<p id="p115986115556"><a name="p115986115556"></a><a name="p115986115556"></a>moveChunk</p>
<p id="p4023262115556"><a name="p4023262115556"></a><a name="p4023262115556"></a>movePrimary</p>
<p id="p300740415556"><a name="p300740415556"></a><a name="p300740415556"></a>isdbgrid</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p08117321004"><a name="p08117321004"></a><a name="p08117321004"></a>flushRouterConfig</p>
<p id="p1581111321909"><a name="p1581111321909"></a><a name="p1581111321909"></a>addShard</p>
<p id="p198113323017"><a name="p198113323017"></a><a name="p198113323017"></a>cleanupOrphaned</p>
<p id="p19811113213013"><a name="p19811113213013"></a><a name="p19811113213013"></a>checkShardingIndex</p>
<p id="p08111332106"><a name="p08111332106"></a><a name="p08111332106"></a>listShards</p>
<p id="p108113321805"><a name="p108113321805"></a><a name="p108113321805"></a>removeShard</p>
<p id="p1381113321102"><a name="p1381113321102"></a><a name="p1381113321102"></a>getShardMap</p>
<p id="p281113321102"><a name="p281113321102"></a><a name="p281113321102"></a>setShardVersion</p>
<p id="p7811203220013"><a name="p7811203220013"></a><a name="p7811203220013"></a>shardingState</p>
<p id="p681115329016"><a name="p681115329016"></a><a name="p681115329016"></a>unsetSharding</p>
</td>
</tr>
<tr id="row2706663915556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p4491416515556"><a name="p4491416515556"></a><a name="p4491416515556"></a>Administration Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p1416875515556"><a name="p1416875515556"></a><a name="p1416875515556"></a>renameCollection</p>
<p id="p4198273815556"><a name="p4198273815556"></a><a name="p4198273815556"></a>dropDatabase</p>
<p id="p377416715556"><a name="p377416715556"></a><a name="p377416715556"></a>listCollections</p>
<p id="p6701354815556"><a name="p6701354815556"></a><a name="p6701354815556"></a>drop</p>
<p id="p6473303715556"><a name="p6473303715556"></a><a name="p6473303715556"></a>create</p>
<p id="p1285292415556"><a name="p1285292415556"></a><a name="p1285292415556"></a>convertToCapped</p>
<p id="p4164960315556"><a name="p4164960315556"></a><a name="p4164960315556"></a>filemd5</p>
<p id="p2935474315556"><a name="p2935474315556"></a><a name="p2935474315556"></a>createIndexes</p>
<p id="p5898952215556"><a name="p5898952215556"></a><a name="p5898952215556"></a>listIndexes</p>
<p id="p5368924015556"><a name="p5368924015556"></a><a name="p5368924015556"></a>dropIndexes</p>
<p id="p1498830615556"><a name="p1498830615556"></a><a name="p1498830615556"></a>fsync</p>
<p id="p5483938015556"><a name="p5483938015556"></a><a name="p5483938015556"></a>connectionStatus</p>
<p id="p4813452215556"><a name="p4813452215556"></a><a name="p4813452215556"></a>collMod</p>
<p id="p5923978215556"><a name="p5923978215556"></a><a name="p5923978215556"></a>reIndex</p>
<p id="p63193746104927"><a name="p63193746104927"></a><a name="p63193746104927"></a>getParameter</p>
<p id="p232014103914"><a name="p232014103914"></a><a name="p232014103914"></a>currentOp</p>
<p id="p3480153815556"><a name="p3480153815556"></a><a name="p3480153815556"></a>killOp</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p17971418118"><a name="p17971418118"></a><a name="p17971418118"></a>clone</p>
<p id="p20971847120"><a name="p20971847120"></a><a name="p20971847120"></a>cloneCollection</p>
<p id="p8971741414"><a name="p8971741414"></a><a name="p8971741414"></a>clean</p>
<p id="p1397941015"><a name="p1397941015"></a><a name="p1397941015"></a>connPoolSync</p>
<p id="p1898141514"><a name="p1898141514"></a><a name="p1898141514"></a>compact</p>
<p id="p99816412118"><a name="p99816412118"></a><a name="p99816412118"></a>setParameter</p>
<p id="p59813413115"><a name="p59813413115"></a><a name="p59813413115"></a>repairDatabase</p>
<p id="p1998442112"><a name="p1998442112"></a><a name="p1998442112"></a>repairCursor</p>
<p id="p1398941814"><a name="p1398941814"></a><a name="p1398941814"></a>touch</p>
<p id="p1598164411"><a name="p1598164411"></a><a name="p1598164411"></a>shutdown</p>
<p id="p10981647119"><a name="p10981647119"></a><a name="p10981647119"></a>cloneCollectionAsCapped</p>
<p id="p398164618"><a name="p398164618"></a><a name="p398164618"></a>copydb</p>
<p id="p098741414"><a name="p098741414"></a><a name="p098741414"></a>logRotate</p>
</td>
</tr>
<tr id="row4477839315556"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p317120315556"><a name="p317120315556"></a><a name="p317120315556"></a>Diagnostic Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p5554091015556"><a name="p5554091015556"></a><a name="p5554091015556"></a>availableQueryOptions</p>
<p id="p2267886615556"><a name="p2267886615556"></a><a name="p2267886615556"></a>buildInfo</p>
<p id="p2411309015556"><a name="p2411309015556"></a><a name="p2411309015556"></a>collStats</p>
<p id="p6302936915556"><a name="p6302936915556"></a><a name="p6302936915556"></a>dataSize</p>
<p id="p4594732215556"><a name="p4594732215556"></a><a name="p4594732215556"></a>dbStats</p>
<p id="p827502415556"><a name="p827502415556"></a><a name="p827502415556"></a>explain</p>
<p id="p5980423915556"><a name="p5980423915556"></a><a name="p5980423915556"></a>features</p>
<p id="p4363771215556"><a name="p4363771215556"></a><a name="p4363771215556"></a>listCommands</p>
<p id="p229112815556"><a name="p229112815556"></a><a name="p229112815556"></a>listDatabases</p>
<p id="p5961995315556"><a name="p5961995315556"></a><a name="p5961995315556"></a>ping</p>
<p id="p4351095815556"><a name="p4351095815556"></a><a name="p4351095815556"></a>serverStatus</p>
<p id="p4410474615556"><a name="p4410474615556"></a><a name="p4410474615556"></a>whatsmyuri</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p72761543211"><a name="p72761543211"></a><a name="p72761543211"></a>connPoolStats</p>
<p id="p18276104318116"><a name="p18276104318116"></a><a name="p18276104318116"></a>cursorInfo</p>
<p id="p327612434110"><a name="p327612434110"></a><a name="p327612434110"></a>dbHash</p>
<p id="p1127654314113"><a name="p1127654314113"></a><a name="p1127654314113"></a>diagLogging</p>
<p id="p1327612431918"><a name="p1327612431918"></a><a name="p1327612431918"></a>driverOIDTest</p>
<p id="p17276124311112"><a name="p17276124311112"></a><a name="p17276124311112"></a>getCmdLineOpts</p>
<p id="p42769433119"><a name="p42769433119"></a><a name="p42769433119"></a>getLog</p>
<p id="p927684313119"><a name="p927684313119"></a><a name="p927684313119"></a>hostInfo</p>
<p id="p6276184314119"><a name="p6276184314119"></a><a name="p6276184314119"></a>isSelf</p>
<p id="p1527610431715"><a name="p1527610431715"></a><a name="p1527610431715"></a>netstat</p>
<p id="p92769436112"><a name="p92769436112"></a><a name="p92769436112"></a>profile</p>
<p id="p112766430111"><a name="p112766430111"></a><a name="p112766430111"></a>shardConnPoolStats</p>
<p id="p227624315120"><a name="p227624315120"></a><a name="p227624315120"></a>top</p>
<p id="p102767439117"><a name="p102767439117"></a><a name="p102767439117"></a>validate</p>
</td>
</tr>
<tr id="row166321419126"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p1427611559213"><a name="p1427611559213"></a><a name="p1427611559213"></a>Internal Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p25498442216"><a name="p25498442216"></a><a name="p25498442216"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p9549044722"><a name="p9549044722"></a><a name="p9549044722"></a>handshake</p>
<p id="p125495441120"><a name="p125495441120"></a><a name="p125495441120"></a>_recvChunkAbort</p>
<p id="p054917442026"><a name="p054917442026"></a><a name="p054917442026"></a>_recvChunkCommit</p>
<p id="p354918442212"><a name="p354918442212"></a><a name="p354918442212"></a>_recvChunkStart</p>
<p id="p105491044329"><a name="p105491044329"></a><a name="p105491044329"></a>_recvChunkStatus</p>
<p id="p1054916449219"><a name="p1054916449219"></a><a name="p1054916449219"></a>_replSetFresh</p>
<p id="p1354994411211"><a name="p1354994411211"></a><a name="p1354994411211"></a>mapreduce.shardedfinish</p>
<p id="p155491944422"><a name="p155491944422"></a><a name="p155491944422"></a>_transferMods</p>
<p id="p2549644826"><a name="p2549644826"></a><a name="p2549644826"></a>replSetHeartbeat</p>
<p id="p154994413219"><a name="p154994413219"></a><a name="p154994413219"></a>replSetGetRBID</p>
<p id="p5549544628"><a name="p5549544628"></a><a name="p5549544628"></a>_migrateClone</p>
<p id="p7549134413214"><a name="p7549134413214"></a><a name="p7549134413214"></a>replSetElect</p>
<p id="p854914441528"><a name="p854914441528"></a><a name="p854914441528"></a>writeBacksQueued</p>
<p id="p155496442024"><a name="p155496442024"></a><a name="p155496442024"></a>writebacklisten</p>
</td>
</tr>
<tr id="row112685241823"><td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.1 "><p id="p132821255729"><a name="p132821255729"></a><a name="p132821255729"></a>System Events Auditing Commands</p>
</td>
<td class="cellrowborder" valign="top" width="34.92%" headers="mcps1.2.4.1.2 "><p id="p1549174416214"><a name="p1549174416214"></a><a name="p1549174416214"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="30.159999999999997%" headers="mcps1.2.4.1.3 "><p id="p95491443212"><a name="p95491443212"></a><a name="p95491443212"></a>logApplicationMessage</p>
</td>
</tr>
</tbody>
</table>

