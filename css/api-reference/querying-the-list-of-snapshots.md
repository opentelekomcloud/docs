# Querying the List of Snapshots<a name="css_03_0034"></a>

## Function<a name="section874853215915"></a>

This API is used to query all snapshots of a cluster.

## URI<a name="section8763193210910"></a>

```
GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p950595565411"><a name="p950595565411"></a><a name="p950595565411"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p15505145512547"><a name="p15505145512547"></a><a name="p15505145512547"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster, to which the snapshot to be queried belongs.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

None

## Response<a name="section19810103220915"></a>

**Table  2** **backups**  field data structure description

<a name="table134134101673"></a>
<table><thead align="left"><tr id="row34302108710"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p144309102719"><a name="p144309102719"></a><a name="p144309102719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.2"><p id="p24306101877"><a name="p24306101877"></a><a name="p24306101877"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.32000000000001%" id="mcps1.2.4.1.3"><p id="p743071010717"><a name="p743071010717"></a><a name="p743071010717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row164441710172"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p11444191010712"><a name="p11444191010712"></a><a name="p11444191010712"></a>backups</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p94447103718"><a name="p94447103718"></a><a name="p94447103718"></a>Array of backup objects</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1644420107711"><a name="p1644420107711"></a><a name="p1644420107711"></a>Snapshot list. For details, see <a href="querying-the-list-of-snapshots.md">Querying the List of Snapshots</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **backups**  field data structure description

<a name="table6765160249"></a>
<table><thead align="left"><tr id="row57631611243"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p187610163246"><a name="p187610163246"></a><a name="p187610163246"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.2"><p id="p129281642410"><a name="p129281642410"></a><a name="p129281642410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.32000000000001%" id="mcps1.2.4.1.3"><p id="p169211162246"><a name="p169211162246"></a><a name="p169211162246"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29241618240"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p29215168244"><a name="p29215168244"></a><a name="p29215168244"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p992141620243"><a name="p992141620243"></a><a name="p992141620243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p09212160241"><a name="p09212160241"></a><a name="p09212160241"></a>Time when a snapshot is created.</p>
</td>
</tr>
<tr id="row79231616245"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p692416122411"><a name="p692416122411"></a><a name="p692416122411"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p1292171613246"><a name="p1292171613246"></a><a name="p1292171613246"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p39231615245"><a name="p39231615245"></a><a name="p39231615245"></a>Type of the data search engine. For details, see <a href="#table9975151812430">Table 4</a>.</p>
</td>
</tr>
<tr id="row15445112994513"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p174457296455"><a name="p174457296455"></a><a name="p174457296455"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p044519292457"><a name="p044519292457"></a><a name="p044519292457"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1244512954513"><a name="p1244512954513"></a><a name="p1244512954513"></a>Description of the snapshot.</p>
</td>
</tr>
<tr id="row17462183794515"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p4462113714453"><a name="p4462113714453"></a><a name="p4462113714453"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p1446263784518"><a name="p1446263784518"></a><a name="p1446263784518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1946253714457"><a name="p1946253714457"></a><a name="p1946253714457"></a>ID of the snapshot.</p>
</td>
</tr>
<tr id="row13382104314455"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p13382154317451"><a name="p13382154317451"></a><a name="p13382154317451"></a>clusterId</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p538217437459"><a name="p538217437459"></a><a name="p538217437459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1038217438454"><a name="p1038217438454"></a><a name="p1038217438454"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row153531053154617"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p103531553154614"><a name="p103531553154614"></a><a name="p103531553154614"></a>clusterName</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p13531553144610"><a name="p13531553144610"></a><a name="p13531553144610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p13531753104613"><a name="p13531753104613"></a><a name="p13531753104613"></a>Cluster name.</p>
</td>
</tr>
<tr id="row1921216589468"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1221235811463"><a name="p1221235811463"></a><a name="p1221235811463"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p6212185864618"><a name="p6212185864618"></a><a name="p6212185864618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p721235814618"><a name="p721235814618"></a><a name="p721235814618"></a>Snapshot name.</p>
</td>
</tr>
<tr id="row1054010424710"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1754012412474"><a name="p1754012412474"></a><a name="p1754012412474"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p1854015414472"><a name="p1854015414472"></a><a name="p1854015414472"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p35401849476"><a name="p35401849476"></a><a name="p35401849476"></a>Snapshot status.</p>
</td>
</tr>
<tr id="row153529111472"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1335251114474"><a name="p1335251114474"></a><a name="p1335251114474"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p13352201164714"><a name="p13352201164714"></a><a name="p13352201164714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p535241113478"><a name="p535241113478"></a><a name="p535241113478"></a>Whether the snapshot status is updated.</p>
</td>
</tr>
<tr id="row767013112512"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p5670191117512"><a name="p5670191117512"></a><a name="p5670191117512"></a>backupType</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p6670181185113"><a name="p6670181185113"></a><a name="p6670181185113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p76702011105118"><a name="p76702011105118"></a><a name="p76702011105118"></a>Value <strong id="b168121177380"><a name="b168121177380"></a><a name="b168121177380"></a>0</strong> indicates that automatic snapshot creation is enabled. Value <strong id="b5814151723816"><a name="b5814151723816"></a><a name="b5814151723816"></a>1</strong> indicates that you need to manually create the snapshot.</p>
</td>
</tr>
<tr id="row8107131535110"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p10107315205114"><a name="p10107315205114"></a><a name="p10107315205114"></a>backupMethod</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p151072015125115"><a name="p151072015125115"></a><a name="p151072015125115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p19107151585117"><a name="p19107151585117"></a><a name="p19107151585117"></a>Snapshot creation mode.</p>
</td>
</tr>
<tr id="row552292193916"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p11522172173916"><a name="p11522172173916"></a><a name="p11522172173916"></a>backupExpectedStartTime</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p65221121390"><a name="p65221121390"></a><a name="p65221121390"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1852214214397"><a name="p1852214214397"></a><a name="p1852214214397"></a>Time when the snapshot starts to be executed.</p>
</td>
</tr>
<tr id="row16397122763910"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p4412927153912"><a name="p4412927153912"></a><a name="p4412927153912"></a>backupKeepDay</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p104121727163918"><a name="p104121727163918"></a><a name="p104121727163918"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p141212713397"><a name="p141212713397"></a><a name="p141212713397"></a>Snapshot retention period.</p>
</td>
</tr>
<tr id="row1664782333916"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p106470237399"><a name="p106470237399"></a><a name="p106470237399"></a>backupPeriod</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p549441618427"><a name="p549441618427"></a><a name="p549441618427"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1264716233396"><a name="p1264716233396"></a><a name="p1264716233396"></a>Time when a snapshot is executed every day.</p>
</td>
</tr>
<tr id="row7116182019391"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p61161820113914"><a name="p61161820113914"></a><a name="p61161820113914"></a>indices</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p17116152016393"><a name="p17116152016393"></a><a name="p17116152016393"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p2011610205396"><a name="p2011610205396"></a><a name="p2011610205396"></a>Indices that need to be backed up.</p>
</td>
</tr>
<tr id="row24021968432"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p184021669438"><a name="p184021669438"></a><a name="p184021669438"></a>totalShards</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p540213619436"><a name="p540213619436"></a><a name="p540213619436"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1940211644313"><a name="p1940211644313"></a><a name="p1940211644313"></a>Total number of shards of the indices to be backed up.</p>
</td>
</tr>
<tr id="row1663716103439"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p56378106431"><a name="p56378106431"></a><a name="p56378106431"></a>failedShards</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p46371109436"><a name="p46371109436"></a><a name="p46371109436"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p12637110184313"><a name="p12637110184313"></a><a name="p12637110184313"></a>Number of shards that fail to be backed up.</p>
</td>
</tr>
<tr id="row93551114124316"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p203551214134319"><a name="p203551214134319"></a><a name="p203551214134319"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p93551148439"><a name="p93551148439"></a><a name="p93551148439"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p16355914164319"><a name="p16355914164319"></a><a name="p16355914164319"></a>Version of the snapshot.</p>
</td>
</tr>
<tr id="row12170740154519"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p11704401451"><a name="p11704401451"></a><a name="p11704401451"></a>restoreStatus</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p15170440194517"><a name="p15170440194517"></a><a name="p15170440194517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p141701040184513"><a name="p141701040184513"></a><a name="p141701040184513"></a>Snapshot restoration status.</p>
</td>
</tr>
<tr id="row11123144411456"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1012314454519"><a name="p1012314454519"></a><a name="p1012314454519"></a>startTime</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p131231244154513"><a name="p131231244154513"></a><a name="p131231244154513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p11123204494516"><a name="p11123204494516"></a><a name="p11123204494516"></a>Timestamp when the snapshot starts to be executed.</p>
</td>
</tr>
<tr id="row11610164311474"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p261074394711"><a name="p261074394711"></a><a name="p261074394711"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p2610143154710"><a name="p2610143154710"></a><a name="p2610143154710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p11610164319470"><a name="p11610164319470"></a><a name="p11610164319470"></a>Timestamp when the snapshot execution ends.</p>
</td>
</tr>
<tr id="row138141620104811"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p581412024817"><a name="p581412024817"></a><a name="p581412024817"></a>bucketName</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p15814182014815"><a name="p15814182014815"></a><a name="p15814182014815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1081412207482"><a name="p1081412207482"></a><a name="p1081412207482"></a>Bucket for storing snapshot data.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **datastore**  field data structure description

<a name="table9975151812430"></a>
<table><thead align="left"><tr id="row13150121911438"><th class="cellrowborder" valign="top" width="34.34343434343434%" id="mcps1.2.4.1.1"><p id="p31501719104317"><a name="p31501719104317"></a><a name="p31501719104317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.2"><p id="p0150319114315"><a name="p0150319114315"></a><a name="p0150319114315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.4.1.3"><p id="p51501519184319"><a name="p51501519184319"></a><a name="p51501519184319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4150101911430"><td class="cellrowborder" valign="top" width="34.34343434343434%" headers="mcps1.2.4.1.1 "><p id="p5150131914312"><a name="p5150131914312"></a><a name="p5150131914312"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.2 "><p id="p13150101914312"><a name="p13150101914312"></a><a name="p13150101914312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.4.1.3 "><p id="p121511419174313"><a name="p121511419174313"></a><a name="p121511419174313"></a>Supported type: elasticsearch</p>
</td>
</tr>
<tr id="row12151101984314"><td class="cellrowborder" valign="top" width="34.34343434343434%" headers="mcps1.2.4.1.1 "><p id="p01511719204313"><a name="p01511719204313"></a><a name="p01511719204313"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.2 "><p id="p16151201913437"><a name="p16151201913437"></a><a name="p16151201913437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.4.1.3 "><p id="p8151191912439"><a name="p8151191912439"></a><a name="p8151191912439"></a>Engine version number. The current engine version is 6.2.3.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section8463633114416"></a>

Example request

```
GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshots
```

Example response

```
{
   "backups": [
    {
      "created": "2018-03-07T07:34:47",
      "datastore": {
        "type": "elasticsearch",
        "version": "6.2.3"
      },
      "description": "",
      "id": "e29d99c1-3d19-4ea4-ae8d-f252df76cbe9",
      "clusterId": "37cb1075-c38e-4cd8-81df-442d52df3786",
      "clusterName": "Es-xfx",
      "name": "snapshot-002",
      "status": "COMPLETED",
      "updated": "2018-03-07T07:40:12",
      "backupType": "1",
      "backupMethod": "manual",
      "backupExpectedStartTime": null,
      "backupKeepDay": null,
      "backupPeriod": null,
      "indices": ".kibana,website2",
      "totalShards": 6,
      "failedShards": 0,
      "version": "6.2.3",
      "restoreStatus": "success",
      "startTime": 1520408087099,
      "endTime": 1520408412219,
      "bucketName": "obs-b8ed"
    },
    {
      "created": "2018-03-06T15:42:37",
      "datastore": {
        "type": "elasticsearch",
        "version": "6.2.3"
      },
      "description": "",
      "id": "29a2254e-947f-4463-b65a-5f0b17515fae",
      "clusterId": "37cb1075-c38e-4cd8-81df-442d52df3786",
      "clusterName": "Es-xfx",
      "name": "snapshot-001",
      "status": "COMPLETED",
      "updated": "2018-03-06T15:48:04",
      "backupType": "1",
      "backupMethod": "manual",
      "backupExpectedStartTime": null,
      "backupKeepDay": null,
      "backupPeriod": null,
      "indices": ".kibana",
      "totalShards": 1,
      "failedShards": 0,
      "version": "6.2.3",
      "restoreStatus": "none",
      "startTime": 1520350957275,
      "endTime": 1520351284357,
      "bucketName": "obs-b8ed"
    }
  ]
}
```

## Status Code<a name="section87962546391"></a>

[Table 5](#table152931957183117)  describes the status code.

**Table  5**  Status code

<a name="table152931957183117"></a>
<table><thead align="left"><tr id="css_03_0037_row194918333132"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="css_03_0037_p6531343171310"><a name="css_03_0037_p6531343171310"></a><a name="css_03_0037_p6531343171310"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="css_03_0037_p16534124318132"><a name="css_03_0037_p16534124318132"></a><a name="css_03_0037_p16534124318132"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="css_03_0037_p1453710437131"><a name="css_03_0037_p1453710437131"></a><a name="css_03_0037_p1453710437131"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0037_row09491533111315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0037_p1656994351310"><a name="css_03_0037_p1656994351310"></a><a name="css_03_0037_p1656994351310"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0037_p134136431055"><a name="css_03_0037_p134136431055"></a><a name="css_03_0037_p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0037_p134136431458"><a name="css_03_0037_p134136431458"></a><a name="css_03_0037_p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="css_03_0037_row1184954102013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0037_p111841154132019"><a name="css_03_0037_p111841154132019"></a><a name="css_03_0037_p111841154132019"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0037_en-us_topic_0122640420_p19980869"><a name="css_03_0037_en-us_topic_0122640420_p19980869"></a><a name="css_03_0037_en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0037_en-us_topic_0122640420_p7837682"><a name="css_03_0037_en-us_topic_0122640420_p7837682"></a><a name="css_03_0037_en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
</tbody>
</table>

