# Querying DCS Instance Backup Records<a name="dcs-api-0312022"></a>

## Function<a name="section10329193461017"></a>

This API is used to query the backup records of a specified DCS instance.

## URI<a name="section10627123311133"></a>

GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups?start=\{start\}&limit=\{limit\}&beginTime=\{beginTime\}&endTime=\{endTime\}

[Table 1](#table1899262913382)  describes the parameters.

**Table  1**  Parameter description

<a name="table1899262913382"></a>
<table><thead align="left"><tr id="row1599115293389"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15991152913819"><a name="p15991152913819"></a><a name="p15991152913819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p129916298387"><a name="p129916298387"></a><a name="p129916298387"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p13991142913384"><a name="p13991142913384"></a><a name="p13991142913384"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p1991329193814"><a name="p1991329193814"></a><a name="p1991329193814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11992929163813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1523414741010"><a name="p1523414741010"></a><a name="p1523414741010"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p142349718103"><a name="p142349718103"></a><a name="p142349718103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1323411714108"><a name="p1323411714108"></a><a name="p1323411714108"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p102346716103"><a name="p102346716103"></a><a name="p102346716103"></a>Project ID.</p>
</td>
</tr>
<tr id="row313125212916"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1223415719101"><a name="p1223415719101"></a><a name="p1223415719101"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1923416720108"><a name="p1923416720108"></a><a name="p1923416720108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p62341677106"><a name="p62341677106"></a><a name="p62341677106"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1923487181015"><a name="p1923487181015"></a><a name="p1923487181015"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row615705910920"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p52344791015"><a name="p52344791015"></a><a name="p52344791015"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p13235475101"><a name="p13235475101"></a><a name="p13235475101"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p62357791015"><a name="p62357791015"></a><a name="p62357791015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p023519761019"><a name="p023519761019"></a><a name="p023519761019"></a>Start sequence number of the backup record that is to be queried. By default, this parameter is set to <strong id="b418831779"><a name="b418831779"></a><a name="b418831779"></a>1</strong>.</p>
</td>
</tr>
<tr id="row12603175214915"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p723516711103"><a name="p723516711103"></a><a name="p723516711103"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1023514714106"><a name="p1023514714106"></a><a name="p1023514714106"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1223519711016"><a name="p1223519711016"></a><a name="p1223519711016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p323517191011"><a name="p323517191011"></a><a name="p323517191011"></a>Number of backup records displayed on each page. The minimum value of this parameter is <strong id="b698477872"><a name="b698477872"></a><a name="b698477872"></a>1</strong>. If this parameter is not set, 10 backup records are displayed on each page by default.</p>
</td>
</tr>
<tr id="row199112521997"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p423510710103"><a name="p423510710103"></a><a name="p423510710103"></a>beginTime</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p22351572101"><a name="p22351572101"></a><a name="p22351572101"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p323517712103"><a name="p323517712103"></a><a name="p323517712103"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p023514711109"><a name="p023514711109"></a><a name="p023514711109"></a>Start time of the period to be queried. Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
<tr id="row12965536911"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19235147111015"><a name="p19235147111015"></a><a name="p19235147111015"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1123511719102"><a name="p1123511719102"></a><a name="p1123511719102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1323577141014"><a name="p1323577141014"></a><a name="p1323577141014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1523514741020"><a name="p1523514741020"></a><a name="p1523514741020"></a>End time of the period to be queried. Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17412144620133"></a>

**Request parameters**

None.

**Example request**

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/backups?start={start}&limit={limit}&beginTime={beginTime}&endTime={endTime}
```

## Response<a name="section1417213312142"></a>

**Response parameters**

[Table 2](#table1861319576383)  describes the response parameters.

**Table  2**  Parameter description

<a name="table1861319576383"></a>
<table><thead align="left"><tr id="row1961225712388"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p136126577389"><a name="p136126577389"></a><a name="p136126577389"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p76121757113816"><a name="p76121757113816"></a><a name="p76121757113816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p26121157123820"><a name="p26121157123820"></a><a name="p26121157123820"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row166121557203812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1694215159152"><a name="p1694215159152"></a><a name="p1694215159152"></a>backup_record_response</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1394211511516"><a name="p1394211511516"></a><a name="p1394211511516"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p994291518159"><a name="p994291518159"></a><a name="p994291518159"></a>Array of the backup records. For details about backup_record_response, see <a href="#table82951233189">Table 3</a>.</p>
</td>
</tr>
<tr id="row13767421219"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1237615425118"><a name="p1237615425118"></a><a name="p1237615425118"></a>total_num</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p4376042714"><a name="p4376042714"></a><a name="p4376042714"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p113765421411"><a name="p113765421411"></a><a name="p113765421411"></a>Number of obtained backup records.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  backup\_record\_response parameter description

<a name="table82951233189"></a>
<table><thead align="left"><tr id="row1529552361817"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p19295182361812"><a name="p19295182361812"></a><a name="p19295182361812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p5295142341812"><a name="p5295142341812"></a><a name="p5295142341812"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p17295182391816"><a name="p17295182391816"></a><a name="p17295182391816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1129512317181"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1353145413181"><a name="p1353145413181"></a><a name="p1353145413181"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p153119547184"><a name="p153119547184"></a><a name="p153119547184"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1453195431814"><a name="p1453195431814"></a><a name="p1453195431814"></a>Backup status. Options:</p>
<a name="ul7204867542"></a><a name="ul7204867542"></a><ul id="ul7204867542"><li><strong id="b128611546141815"><a name="b128611546141815"></a><a name="b128611546141815"></a>waiting</strong>: DCS instance restoration is waiting to begin.</li><li><strong id="b19181248181814"><a name="b19181248181814"></a><a name="b19181248181814"></a>backuping</strong>: DCS instance backup is in progress.</li><li><strong id="b20126174961816"><a name="b20126174961816"></a><a name="b20126174961816"></a>succeed</strong>: DCS instance backup succeeded.</li><li><strong id="b82725151816"><a name="b82725151816"></a><a name="b82725151816"></a>failed</strong>: DCS instance backup failed.</li><li><strong id="b14902105118186"><a name="b14902105118186"></a><a name="b14902105118186"></a>expired</strong>: The backup file expires.</li><li><strong id="b2979145221810"><a name="b2979145221810"></a><a name="b2979145221810"></a>deleted</strong>: The backup file has been deleted manually. </li></ul>
</td>
</tr>
<tr id="row1329517231188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1553115413185"><a name="p1553115413185"></a><a name="p1553115413185"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p7531195417183"><a name="p7531195417183"></a><a name="p7531195417183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p19532854121812"><a name="p19532854121812"></a><a name="p19532854121812"></a>Description of DCS instance backup</p>
</td>
</tr>
<tr id="row89511348141815"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4532135411187"><a name="p4532135411187"></a><a name="p4532135411187"></a>period</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1853215544184"><a name="p1853215544184"></a><a name="p1853215544184"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p18532135414189"><a name="p18532135414189"></a><a name="p18532135414189"></a>Time segment in which DCS instance backup was performed</p>
</td>
</tr>
<tr id="row3237649111810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17532175416181"><a name="p17532175416181"></a><a name="p17532175416181"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p3532954171818"><a name="p3532954171818"></a><a name="p3532954171818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p85325542188"><a name="p85325542188"></a><a name="p85325542188"></a>Backup progress</p>
</td>
</tr>
<tr id="row639864912186"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p05323546184"><a name="p05323546184"></a><a name="p05323546184"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1253219547187"><a name="p1253219547187"></a><a name="p1253219547187"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p6532115419183"><a name="p6532115419183"></a><a name="p6532115419183"></a>Size of the backup file. Unit: byte.</p>
</td>
</tr>
<tr id="row177581437173119"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3758123723116"><a name="p3758123723116"></a><a name="p3758123723116"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p20759163719311"><a name="p20759163719311"></a><a name="p20759163719311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p67591837173119"><a name="p67591837173119"></a><a name="p67591837173119"></a>DCS instance ID</p>
</td>
</tr>
<tr id="row1858120491183"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p253215417181"><a name="p253215417181"></a><a name="p253215417181"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p3532115471814"><a name="p3532115471814"></a><a name="p3532115471814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p95321054161817"><a name="p95321054161817"></a><a name="p95321054161817"></a>ID of the backup record</p>
</td>
</tr>
<tr id="row10758144910189"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p105321554191816"><a name="p105321554191816"></a><a name="p105321554191816"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p2532115419180"><a name="p2532115419180"></a><a name="p2532115419180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p5532185417187"><a name="p5532185417187"></a><a name="p5532185417187"></a>Time at which the backup task is created</p>
</td>
</tr>
<tr id="row8908349191817"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12532115461819"><a name="p12532115461819"></a><a name="p12532115461819"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1853255431810"><a name="p1853255431810"></a><a name="p1853255431810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p6532145417182"><a name="p6532145417182"></a><a name="p6532145417182"></a>Time at which DCS instance backup is completed</p>
</td>
</tr>
<tr id="row89415477414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29421847114119"><a name="p29421847114119"></a><a name="p29421847114119"></a>execution_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p694274712413"><a name="p694274712413"></a><a name="p694274712413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p3942204734120"><a name="p3942204734120"></a><a name="p3942204734120"></a>Time at which the backup starts.</p>
</td>
</tr>
<tr id="row14234450101811"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p105331954101820"><a name="p105331954101820"></a><a name="p105331954101820"></a>backup_type</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p753365411815"><a name="p753365411815"></a><a name="p753365411815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p195331354111818"><a name="p195331354111818"></a><a name="p195331354111818"></a>Backup type. Options:</p>
<a name="ul6533954131811"></a><a name="ul6533954131811"></a><ul id="ul6533954131811"><li><strong id="b1376692421019"><a name="b1376692421019"></a><a name="b1376692421019"></a>manual</strong>: manual backup</li><li><strong id="b688010283104"><a name="b688010283104"></a><a name="b688010283104"></a>auto</strong>: automatic backup</li></ul>
</td>
</tr>
<tr id="row5539165051818"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1353317547181"><a name="p1353317547181"></a><a name="p1353317547181"></a>backup_name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p11533105471820"><a name="p11533105471820"></a><a name="p11533105471820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p553313540185"><a name="p553313540185"></a><a name="p553313540185"></a>Name of the backup record</p>
</td>
</tr>
<tr id="row12951323121812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p115331954111810"><a name="p115331954111810"></a><a name="p115331954111810"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19533105415189"><a name="p19533105415189"></a><a name="p19533105415189"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p5533185491810"><a name="p5533185491810"></a><a name="p5533185491810"></a>Error code returned if DCS instance backup fails. For details about error codes, see <a href="#table1255361919491">Table 4</a>.</p>
</td>
</tr>
<tr id="row2060041023717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1860121043718"><a name="p1860121043718"></a><a name="p1860121043718"></a>is_support_restore</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1479155312376"><a name="p1479155312376"></a><a name="p1479155312376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p796540154715"><a name="p796540154715"></a><a name="p796540154715"></a>An indicator of whether restoration is supported. Options: <strong id="b1932918451192"><a name="b1932918451192"></a><a name="b1932918451192"></a>TRUE</strong> or <strong id="b1932917456918"><a name="b1932917456918"></a><a name="b1932917456918"></a>FALSE</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Error codes returned in case of a backup or restoration failure

<a name="table1255361919491"></a>
<table><thead align="left"><tr id="row1755412199492"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p2554171914492"><a name="p2554171914492"></a><a name="p2554171914492"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p14554121914917"><a name="p14554121914917"></a><a name="p14554121914917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6554319154918"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p115547197491"><a name="p115547197491"></a><a name="p115547197491"></a>dcs.08.0001</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1155412195491"><a name="p1155412195491"></a><a name="p1155412195491"></a>Failed to start the backup and restore tool.</p>
</td>
</tr>
<tr id="row145541819124918"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p85541319184920"><a name="p85541319184920"></a><a name="p85541319184920"></a>dcs.08.0002</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1455401916493"><a name="p1455401916493"></a><a name="p1455401916493"></a>Operation timed out.</p>
</td>
</tr>
<tr id="row2554519114913"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p555401924915"><a name="p555401924915"></a><a name="p555401924915"></a>dcs.08.0003</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p355417197494"><a name="p355417197494"></a><a name="p355417197494"></a>Failed to delete bucket.</p>
</td>
</tr>
<tr id="row75548193491"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p25541319144917"><a name="p25541319144917"></a><a name="p25541319144917"></a>dcs.08.0004</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p3554121974914"><a name="p3554121974914"></a><a name="p3554121974914"></a>Failed to obtain AK/SK.</p>
</td>
</tr>
<tr id="row1355415199491"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p12554111915490"><a name="p12554111915490"></a><a name="p12554111915490"></a>dcs.08.0005</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p355421919494"><a name="p355421919494"></a><a name="p355421919494"></a>Failed to create bucket.</p>
</td>
</tr>
<tr id="row18554719144912"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1755581920499"><a name="p1755581920499"></a><a name="p1755581920499"></a>dcs.08.0006</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p19555151914490"><a name="p19555151914490"></a><a name="p19555151914490"></a>Failed to obtain backup file size.</p>
</td>
</tr>
<tr id="row2555161914910"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p15555131994918"><a name="p15555131994918"></a><a name="p15555131994918"></a>dcs.08.0007</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p2555319144916"><a name="p2555319144916"></a><a name="p2555319144916"></a>Data synchronization failed during instance restoration.</p>
</td>
</tr>
<tr id="row1111512213330"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1811642113319"><a name="p1811642113319"></a><a name="p1811642113319"></a>dcs.08.0008</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p011617219332"><a name="p011617219332"></a><a name="p011617219332"></a>Automatic backup of the instance cannot start because the instance is running other jobs.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "backup_record_response": [
        {
            "status": "succeed",
            "remark": "001",
            "period": null,
            "progress": "100.00",
            "size": 880232,
            "instance_id": "5560df16-cebf-4473-95c4-d1b573c16e79",
            "backup_id": "4631832a-14c6-45b0-a0b3-3abd8f591ad1",
            "created_at": "2019-05-10T08:31:16.166Z",
            "updated_at": "2019-05-10T08:32:30.546Z",
            "execution_at": "2019-05-10T08:31:21.461Z",
            "backup_type": "manual",
            "backup_name": "backup_20190510163116",
            "error_code": null,
            "is_support_restore": "TRUE"
        }
    ],
    "total_num": 1
}
```

## Status Code<a name="section4860101417132"></a>

[Table 5](#table486141410130)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  5**  Status code

<a name="table486141410130"></a>
<table><thead align="left"><tr id="row18616141139"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1986191418133"><a name="p1986191418133"></a><a name="p1986191418133"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p18861111415138"><a name="p18861111415138"></a><a name="p18861111415138"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row786131451312"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p6861114181311"><a name="p6861114181311"></a><a name="p6861114181311"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p48619143136"><a name="p48619143136"></a><a name="p48619143136"></a>DCS instance backup records queried successfully.</p>
</td>
</tr>
</tbody>
</table>

