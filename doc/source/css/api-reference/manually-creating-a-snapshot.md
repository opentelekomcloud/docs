# Manually Creating a Snapshot<a name="css_03_0033"></a>

## Function<a name="section874853215915"></a>

This API is used to manually create a snapshot.

## URI<a name="section8763193210910"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster where index data is to be backed up.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

[Table 2](#table82481020121413)  describes the request parameters.

**Table  2**  Parameter description

<a name="table82481020121413"></a>
<table><thead align="left"><tr id="row18248112010149"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p10441033494"><a name="p10441033494"></a><a name="p10441033494"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p74493316910"><a name="p74493316910"></a><a name="p74493316910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p1044533896"><a name="p1044533896"></a><a name="p1044533896"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p154413335917"><a name="p154413335917"></a><a name="p154413335917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18248182013148"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p837215054813"><a name="p837215054813"></a><a name="p837215054813"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p4441233891"><a name="p4441233891"></a><a name="p4441233891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p186181046114912"><a name="p186181046114912"></a><a name="p186181046114912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p9448924192218"><a name="p9448924192218"></a><a name="p9448924192218"></a>Snapshot name. The snapshot name must start with a letter and contains 4 to 64 characters consisting of only lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row243315404483"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1343434015485"><a name="p1343434015485"></a><a name="p1343434015485"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p443424054812"><a name="p443424054812"></a><a name="p443424054812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1543414094815"><a name="p1543414094815"></a><a name="p1543414094815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p194341340174817"><a name="p194341340174817"></a><a name="p194341340174817"></a>Description of a snapshot. The value contains 0 to 256 characters, and angle brackets (&lt;) and (&gt;) are not allowed.</p>
</td>
</tr>
<tr id="row1795115595819"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p19952165545814"><a name="p19952165545814"></a><a name="p19952165545814"></a>indices</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p139521155125816"><a name="p139521155125816"></a><a name="p139521155125816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1995220551584"><a name="p1995220551584"></a><a name="p1995220551584"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p131436419191"><a name="p131436419191"></a><a name="p131436419191"></a>Name of the index to be backed up. Multiple index names are separated by commas (,). By default, data of all indices is backed up. You can use the asterisk (*) to back up data of certain indices. For example, if you enter <strong id="b188021711487"><a name="b188021711487"></a><a name="b188021711487"></a>2018-06*</strong>, then data of indices with the name prefix of <strong id="b16917656184811"><a name="b16917656184811"></a><a name="b16917656184811"></a>2018-06</strong> will be backed up.</p>
<p id="p14971123115432"><a name="p14971123115432"></a><a name="p14971123115432"></a>The value contains 0 to 1024 characters. Uppercase letters, spaces, and certain special characters (including "\&lt;|&gt;/?) are not allowed.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19810103220915"></a>

[Table 3](#table4974113513176)  describes the response parameters.

**Table  3**  Parameter description

<a name="table4974113513176"></a>
<table><thead align="left"><tr id="row8974235191715"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p179743351172"><a name="p179743351172"></a><a name="p179743351172"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.2"><p id="p89741735101716"><a name="p89741735101716"></a><a name="p89741735101716"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.32000000000001%" id="mcps1.2.4.1.3"><p id="p69741435141716"><a name="p69741435141716"></a><a name="p69741435141716"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row89745358176"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1299073511715"><a name="p1299073511715"></a><a name="p1299073511715"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p119901135101715"><a name="p119901135101715"></a><a name="p119901135101715"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p1799083571720"><a name="p1799083571720"></a><a name="p1799083571720"></a>Snapshot object. For details, see <a href="#table6765160249">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **backup**  field data structure description

<a name="table6765160249"></a>
<table><thead align="left"><tr id="row57631611243"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p187610163246"><a name="p187610163246"></a><a name="p187610163246"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p129281642410"><a name="p129281642410"></a><a name="p129281642410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p169211162246"><a name="p169211162246"></a><a name="p169211162246"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29241618240"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p29215168244"><a name="p29215168244"></a><a name="p29215168244"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p992141620243"><a name="p992141620243"></a><a name="p992141620243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p09212160241"><a name="p09212160241"></a><a name="p09212160241"></a>Time when a snapshot is created.</p>
</td>
</tr>
<tr id="row79231616245"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p692416122411"><a name="p692416122411"></a><a name="p692416122411"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1292171613246"><a name="p1292171613246"></a><a name="p1292171613246"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p39231615245"><a name="p39231615245"></a><a name="p39231615245"></a>Type of the data search engine. For details, see <a href="#table19534102925018">Table 5</a>.</p>
</td>
</tr>
<tr id="row15445112994513"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p174457296455"><a name="p174457296455"></a><a name="p174457296455"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p044519292457"><a name="p044519292457"></a><a name="p044519292457"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1244512954513"><a name="p1244512954513"></a><a name="p1244512954513"></a>Description of the snapshot.</p>
</td>
</tr>
<tr id="row17462183794515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4462113714453"><a name="p4462113714453"></a><a name="p4462113714453"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1446263784518"><a name="p1446263784518"></a><a name="p1446263784518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1946253714457"><a name="p1946253714457"></a><a name="p1946253714457"></a>ID of the snapshot.</p>
</td>
</tr>
<tr id="row13382104314455"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p13382154317451"><a name="p13382154317451"></a><a name="p13382154317451"></a>clusterId</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p538217437459"><a name="p538217437459"></a><a name="p538217437459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1038217438454"><a name="p1038217438454"></a><a name="p1038217438454"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row153531053154617"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p103531553154614"><a name="p103531553154614"></a><a name="p103531553154614"></a>clusterName</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p13531553144610"><a name="p13531553144610"></a><a name="p13531553144610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p13531753104613"><a name="p13531753104613"></a><a name="p13531753104613"></a>Cluster name.</p>
</td>
</tr>
<tr id="row1921216589468"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1221235811463"><a name="p1221235811463"></a><a name="p1221235811463"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6212185864618"><a name="p6212185864618"></a><a name="p6212185864618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p721235814618"><a name="p721235814618"></a><a name="p721235814618"></a>Snapshot name.</p>
</td>
</tr>
<tr id="row1054010424710"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1754012412474"><a name="p1754012412474"></a><a name="p1754012412474"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1854015414472"><a name="p1854015414472"></a><a name="p1854015414472"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p35401849476"><a name="p35401849476"></a><a name="p35401849476"></a>Snapshot status.</p>
</td>
</tr>
<tr id="row153529111472"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1335251114474"><a name="p1335251114474"></a><a name="p1335251114474"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p13352201164714"><a name="p13352201164714"></a><a name="p13352201164714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p535241113478"><a name="p535241113478"></a><a name="p535241113478"></a>Whether the snapshot status is updated.</p>
</td>
</tr>
<tr id="row767013112512"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p5670191117512"><a name="p5670191117512"></a><a name="p5670191117512"></a>backupType</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6670181185113"><a name="p6670181185113"></a><a name="p6670181185113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p76702011105118"><a name="p76702011105118"></a><a name="p76702011105118"></a>Value <strong id="b9294164874019"><a name="b9294164874019"></a><a name="b9294164874019"></a>0</strong> indicates that automatic snapshot creation is enabled. Value <strong id="b1994202310417"><a name="b1994202310417"></a><a name="b1994202310417"></a>1</strong> indicates that you need to manually create the snapshot.</p>
</td>
</tr>
<tr id="row8107131535110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p10107315205114"><a name="p10107315205114"></a><a name="p10107315205114"></a>backupMethod</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p151072015125115"><a name="p151072015125115"></a><a name="p151072015125115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p19107151585117"><a name="p19107151585117"></a><a name="p19107151585117"></a>Snapshot creation mode.</p>
</td>
</tr>
<tr id="row552292193916"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p11522172173916"><a name="p11522172173916"></a><a name="p11522172173916"></a>backupExpectedStartTime</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p65221121390"><a name="p65221121390"></a><a name="p65221121390"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1852214214397"><a name="p1852214214397"></a><a name="p1852214214397"></a>Time when the snapshot starts to be executed.</p>
</td>
</tr>
<tr id="row16397122763910"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4412927153912"><a name="p4412927153912"></a><a name="p4412927153912"></a>backupKeepDay</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p104121727163918"><a name="p104121727163918"></a><a name="p104121727163918"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p141212713397"><a name="p141212713397"></a><a name="p141212713397"></a>Snapshot retention period.</p>
</td>
</tr>
<tr id="row1664782333916"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p106470237399"><a name="p106470237399"></a><a name="p106470237399"></a>backupPeriod</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p549441618427"><a name="p549441618427"></a><a name="p549441618427"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1264716233396"><a name="p1264716233396"></a><a name="p1264716233396"></a>Time when a snapshot is executed every day.</p>
</td>
</tr>
<tr id="row7116182019391"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p61161820113914"><a name="p61161820113914"></a><a name="p61161820113914"></a>indices</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p17116152016393"><a name="p17116152016393"></a><a name="p17116152016393"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p2011610205396"><a name="p2011610205396"></a><a name="p2011610205396"></a>Indices that need to be backed up.</p>
</td>
</tr>
<tr id="row24021968432"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p184021669438"><a name="p184021669438"></a><a name="p184021669438"></a>totalShards</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p540213619436"><a name="p540213619436"></a><a name="p540213619436"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1940211644313"><a name="p1940211644313"></a><a name="p1940211644313"></a>Total number of shards of the indices to be backed up.</p>
</td>
</tr>
<tr id="row1663716103439"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p56378106431"><a name="p56378106431"></a><a name="p56378106431"></a>failedShards</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p46371109436"><a name="p46371109436"></a><a name="p46371109436"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p12637110184313"><a name="p12637110184313"></a><a name="p12637110184313"></a>Number of shards that fail to be backed up.</p>
</td>
</tr>
<tr id="row93551114124316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p203551214134319"><a name="p203551214134319"></a><a name="p203551214134319"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p93551148439"><a name="p93551148439"></a><a name="p93551148439"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p16355914164319"><a name="p16355914164319"></a><a name="p16355914164319"></a>Version of the snapshot.</p>
</td>
</tr>
<tr id="row12170740154519"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p11704401451"><a name="p11704401451"></a><a name="p11704401451"></a>restoreStatus</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p15170440194517"><a name="p15170440194517"></a><a name="p15170440194517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p141701040184513"><a name="p141701040184513"></a><a name="p141701040184513"></a>Snapshot restoration status.</p>
</td>
</tr>
<tr id="row11123144411456"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1012314454519"><a name="p1012314454519"></a><a name="p1012314454519"></a>startTime</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p131231244154513"><a name="p131231244154513"></a><a name="p131231244154513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p11123204494516"><a name="p11123204494516"></a><a name="p11123204494516"></a>Timestamp when the snapshot starts to be executed.</p>
</td>
</tr>
<tr id="row11610164311474"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p261074394711"><a name="p261074394711"></a><a name="p261074394711"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p2610143154710"><a name="p2610143154710"></a><a name="p2610143154710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p11610164319470"><a name="p11610164319470"></a><a name="p11610164319470"></a>Timestamp when the snapshot execution ends.</p>
</td>
</tr>
<tr id="row138141620104811"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p581412024817"><a name="p581412024817"></a><a name="p581412024817"></a>bucketName</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p15814182014815"><a name="p15814182014815"></a><a name="p15814182014815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1081412207482"><a name="p1081412207482"></a><a name="p1081412207482"></a>Bucket for storing snapshot data.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **datastore**  field data structure description

<a name="table19534102925018"></a>
<table><thead align="left"><tr id="row2054915296508"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p3549529125014"><a name="p3549529125014"></a><a name="p3549529125014"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.2"><p id="p15491929175011"><a name="p15491929175011"></a><a name="p15491929175011"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.32000000000001%" id="mcps1.2.4.1.3"><p id="p054962912508"><a name="p054962912508"></a><a name="p054962912508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1754916293505"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p1856618297503"><a name="p1856618297503"></a><a name="p1856618297503"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p12566112919503"><a name="p12566112919503"></a><a name="p12566112919503"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p056642914507"><a name="p056642914507"></a><a name="p056642914507"></a>Service type corresponding to the snapshot.</p>
</td>
</tr>
<tr id="row101451022135113"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p141451922205119"><a name="p141451922205119"></a><a name="p141451922205119"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.2 "><p id="p191451422135113"><a name="p191451422135113"></a><a name="p191451422135113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p131458223515"><a name="p131458223515"></a><a name="p131458223515"></a>Service version corresponding to the snapshot.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section0893774312"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot
{
    "name":"snapshot_001",
    "indices":"myindex1,myindex2",
    "description":""
}
```

Example response

```
{
    "backup":{
       "created" : "2018-07-31T04:02:47",
       "datastore" : {
           "type" : "elasticsearch",
           "version" : "6.2.3"
       },
       "description" : "Index backup",
       "id" : "9dc4f5c9-33c0-45c7-9378-ae35ae350682",
       "clusterId": "e0164652-421b-40ad-8b0b-650c18c83df5",
       "clusterName": "Es-xfx",
       "name": "snapshot_101",
       "status": "BUILDING",
       "updated": null,
       "backupType": "1",
       "backupMethod": "manual",
       "backupExpectedStartTime": null,
       "backupKeepDay": 33,
       "backupPeriod": "13:00",
       "indices": "myindex1,myindex2",
       "totalShards": null,
       "failedShards": null,
       "version": null,
       "restoreStatus": "none",
       "startTime": 1533009767542,
       "endTime": 0,
       "bucketName": "obs-es-backup1532662640948"
    }
}
```

## Status Code<a name="section87962546391"></a>

[Table 6](#table1728411482811)  describes the status code.

**Table  6**  Status code

<a name="table1728411482811"></a>
<table><thead align="left"><tr id="row19286184172819"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0122640420_p51562446"><a name="en-us_topic_0122640420_p51562446"></a><a name="en-us_topic_0122640420_p51562446"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0122640420_p15808580"><a name="en-us_topic_0122640420_p15808580"></a><a name="en-us_topic_0122640420_p15808580"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0122640420_p5426640"><a name="en-us_topic_0122640420_p5426640"></a><a name="en-us_topic_0122640420_p5426640"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row132861042286"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1128617411288"><a name="p1128617411288"></a><a name="p1128617411288"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p58675139"><a name="en-us_topic_0122640420_p58675139"></a><a name="en-us_topic_0122640420_p58675139"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p55065844"><a name="en-us_topic_0122640420_p55065844"></a><a name="en-us_topic_0122640420_p55065844"></a>The request for creating a resource has been fulfilled.</p>
</td>
</tr>
<tr id="row102861341287"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p132862452815"><a name="p132862452815"></a><a name="p132862452815"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p5333744"><a name="en-us_topic_0122640420_p5333744"></a><a name="en-us_topic_0122640420_p5333744"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p29380125"><a name="en-us_topic_0122640420_p29380125"></a><a name="en-us_topic_0122640420_p29380125"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="row7286641285"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p162861349281"><a name="p162861349281"></a><a name="p162861349281"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p19980869"><a name="en-us_topic_0122640420_p19980869"></a><a name="en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p7837682"><a name="en-us_topic_0122640420_p7837682"></a><a name="en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="row92861142287"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2028654202814"><a name="p2028654202814"></a><a name="p2028654202814"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p35800417"><a name="en-us_topic_0122640420_p35800417"></a><a name="en-us_topic_0122640420_p35800417"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p14152689"><a name="en-us_topic_0122640420_p14152689"></a><a name="en-us_topic_0122640420_p14152689"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="row54071148132818"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13407184815280"><a name="p13407184815280"></a><a name="p13407184815280"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p50789473"><a name="en-us_topic_0122640420_p50789473"></a><a name="en-us_topic_0122640420_p50789473"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p20306648"><a name="en-us_topic_0122640420_p20306648"></a><a name="en-us_topic_0122640420_p20306648"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="en-us_topic_0122640420_p48542107"><a name="en-us_topic_0122640420_p48542107"></a><a name="en-us_topic_0122640420_p48542107"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row111035537283"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4103105342812"><a name="p4103105342812"></a><a name="p4103105342812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p11193990"><a name="en-us_topic_0122640420_p11193990"></a><a name="en-us_topic_0122640420_p11193990"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p34297999"><a name="en-us_topic_0122640420_p34297999"></a><a name="en-us_topic_0122640420_p34297999"></a>Invalid request.</p>
<p id="en-us_topic_0122640420_p40246543"><a name="en-us_topic_0122640420_p40246543"></a><a name="en-us_topic_0122640420_p40246543"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
</tbody>
</table>

