# Querying DCS Instance Backup Records<a name="EN-US_TOPIC_0237964371"></a>

## Function<a name="section19934082"></a>

This API is used to query the backup records of a specified DCS instance.

## URI<a name="section45189012"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups?start=\{start\}&limit=\{limit\}&beginTime=\{beginTime\}&endTime=\{endTime\}

-   Parameter description:

    [Table 1](#d0e6212)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e6212"></a>
<table><thead align="left"><tr id="row6427492"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p50864815"><a name="p50864815"></a><a name="p50864815"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p26409355"><a name="p26409355"></a><a name="p26409355"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p58783007"><a name="p58783007"></a><a name="p58783007"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p63803156"><a name="p63803156"></a><a name="p63803156"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row673170"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p54526784"><a name="p54526784"></a><a name="p54526784"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p54593350"><a name="p54593350"></a><a name="p54593350"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p59985229"><a name="p59985229"></a><a name="p59985229"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p26965372"><a name="p26965372"></a><a name="p26965372"></a>Project ID.</p>
</td>
</tr>
<tr id="row41361763"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61968482"><a name="p61968482"></a><a name="p61968482"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p53391134"><a name="p53391134"></a><a name="p53391134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p29714558"><a name="p29714558"></a><a name="p29714558"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p58068970"><a name="p58068970"></a><a name="p58068970"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row52858689"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53695403"><a name="p53695403"></a><a name="p53695403"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p54360406"><a name="p54360406"></a><a name="p54360406"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p41116778"><a name="p41116778"></a><a name="p41116778"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p42124685"><a name="p42124685"></a><a name="p42124685"></a>Start sequence number of the to-be-queried backup record. By default, this parameter is set to <strong id="b43577853"><a name="b43577853"></a><a name="b43577853"></a>1</strong>.</p>
</td>
</tr>
<tr id="row56656362"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25762599"><a name="p25762599"></a><a name="p25762599"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p6395756"><a name="p6395756"></a><a name="p6395756"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p48294242"><a name="p48294242"></a><a name="p48294242"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p19519536"><a name="p19519536"></a><a name="p19519536"></a>Number of backup records displayed on each page. The minimum value of this parameter is <strong id="b41458104"><a name="b41458104"></a><a name="b41458104"></a>1</strong>. If this parameter is not specified, 10 backup records are displayed on each page by default.</p>
</td>
</tr>
<tr id="row37578623"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p23969655"><a name="p23969655"></a><a name="p23969655"></a>beginTime</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p62493887"><a name="p62493887"></a><a name="p62493887"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p28840063"><a name="p28840063"></a><a name="p28840063"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p54343776"><a name="p54343776"></a><a name="p54343776"></a>Start time of the period to be queried.</p>
<p id="p19331940"><a name="p19331940"></a><a name="p19331940"></a>Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
<tr id="row39769737"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p123299"><a name="p123299"></a><a name="p123299"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p9987286"><a name="p9987286"></a><a name="p9987286"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p3663817"><a name="p3663817"></a><a name="p3663817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p28333732"><a name="p28333732"></a><a name="p28333732"></a>End time of the period to be queried.</p>
<p id="p53677000"><a name="p53677000"></a><a name="p53677000"></a>Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section4047927"></a>

None.

## Response<a name="section36431349"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#d0e6339)  describes the response parameters.


**Table  2**  Parameter description

<a name="d0e6339"></a>
<table><thead align="left"><tr id="row36684175"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p18628187"><a name="p18628187"></a><a name="p18628187"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p32488139"><a name="p32488139"></a><a name="p32488139"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p14293575"><a name="p14293575"></a><a name="p14293575"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16928952"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29067910"><a name="p29067910"></a><a name="p29067910"></a>backup_record_response</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p5690520"><a name="p5690520"></a><a name="p5690520"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p58278999"><a name="p58278999"></a><a name="p58278999"></a>Array of the backup records. For details about backup_record_response, see <a href="#table39834343">Table 3</a>.</p>
</td>
</tr>
<tr id="row22978474"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p49317114"><a name="p49317114"></a><a name="p49317114"></a>total_num</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p35263278"><a name="p35263278"></a><a name="p35263278"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p37753263"><a name="p37753263"></a><a name="p37753263"></a>Number of obtained backup records.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the backup\_record\_response array

<a name="table39834343"></a>
<table><thead align="left"><tr id="row28888142"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p58238181"><a name="p58238181"></a><a name="p58238181"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p19672249"><a name="p19672249"></a><a name="p19672249"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p49948337"><a name="p49948337"></a><a name="p49948337"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19283510"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18460463"><a name="p18460463"></a><a name="p18460463"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p18902533"><a name="p18902533"></a><a name="p18902533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p54710175"><a name="p54710175"></a><a name="p54710175"></a>Backup status.</p>
<a name="ul22629529"></a><a name="ul22629529"></a><ul id="ul22629529"><li><strong id="b21052565"><a name="b21052565"></a><a name="b21052565"></a>waiting</strong>: DCS instance backup is waiting to begin.</li><li><strong id="b27536201"><a name="b27536201"></a><a name="b27536201"></a>backuping</strong>: DCS instance backup is in progress.</li><li><strong id="b15839838"><a name="b15839838"></a><a name="b15839838"></a>succeed</strong>: DCS instance backup succeeded.</li><li><strong id="b7958524"><a name="b7958524"></a><a name="b7958524"></a>failed</strong>: DCS instance backup failed.</li><li><strong id="b40660682"><a name="b40660682"></a><a name="b40660682"></a>expired</strong>: The backup file has expired.</li><li><strong id="b5180912"><a name="b5180912"></a><a name="b5180912"></a>deleted</strong>: The backup file has been deleted manually.</li></ul>
</td>
</tr>
<tr id="row46628212"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18788818"><a name="p18788818"></a><a name="p18788818"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p45499293"><a name="p45499293"></a><a name="p45499293"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p61564092"><a name="p61564092"></a><a name="p61564092"></a>Description of the DCS instance backup.</p>
</td>
</tr>
<tr id="row17205919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p51502168"><a name="p51502168"></a><a name="p51502168"></a>period</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p10926041"><a name="p10926041"></a><a name="p10926041"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p12594123"><a name="p12594123"></a><a name="p12594123"></a>Time segment in which DCS instance backup was performed.</p>
</td>
</tr>
<tr id="row46238245"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p54310403"><a name="p54310403"></a><a name="p54310403"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p37066533"><a name="p37066533"></a><a name="p37066533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p49599220"><a name="p49599220"></a><a name="p49599220"></a>Backup progress.</p>
</td>
</tr>
<tr id="row43739799"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p53262868"><a name="p53262868"></a><a name="p53262868"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19325041"><a name="p19325041"></a><a name="p19325041"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p21824470"><a name="p21824470"></a><a name="p21824470"></a>Size of the backup file.</p>
<p id="p62202508"><a name="p62202508"></a><a name="p62202508"></a>Unit: byte.</p>
</td>
</tr>
<tr id="row22951660"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47145178"><a name="p47145178"></a><a name="p47145178"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p60663113"><a name="p60663113"></a><a name="p60663113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p14765153"><a name="p14765153"></a><a name="p14765153"></a>DCS instance ID</p>
</td>
</tr>
<tr id="row65777515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p26378514"><a name="p26378514"></a><a name="p26378514"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p56284918"><a name="p56284918"></a><a name="p56284918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p62784510"><a name="p62784510"></a><a name="p62784510"></a>ID of the backup record.</p>
</td>
</tr>
<tr id="row28189683"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1663021"><a name="p1663021"></a><a name="p1663021"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p487040"><a name="p487040"></a><a name="p487040"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p39450259"><a name="p39450259"></a><a name="p39450259"></a>Time at which the backup task is created.</p>
</td>
</tr>
<tr id="row19508012"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p36645122"><a name="p36645122"></a><a name="p36645122"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p15464942"><a name="p15464942"></a><a name="p15464942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p44700757"><a name="p44700757"></a><a name="p44700757"></a>Time at which DCS instance backup is completed.</p>
</td>
</tr>
<tr id="row66762499"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p39053361"><a name="p39053361"></a><a name="p39053361"></a>execution_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p9205647"><a name="p9205647"></a><a name="p9205647"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p7459909"><a name="p7459909"></a><a name="p7459909"></a>Time at which the backup starts.</p>
</td>
</tr>
<tr id="row30321"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2456031"><a name="p2456031"></a><a name="p2456031"></a>backup_type</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p64720826"><a name="p64720826"></a><a name="p64720826"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p7895529"><a name="p7895529"></a><a name="p7895529"></a>Backup type.</p>
<p id="p3950900"><a name="p3950900"></a><a name="p3950900"></a>Options:</p>
<a name="ul35558101"></a><a name="ul35558101"></a><ul id="ul35558101"><li><strong id="b61633893"><a name="b61633893"></a><a name="b61633893"></a>manual</strong>: manual backup.</li><li><strong id="b26289409"><a name="b26289409"></a><a name="b26289409"></a>auto</strong>: automatic backup.</li></ul>
</td>
</tr>
<tr id="row35278096"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p38953514"><a name="p38953514"></a><a name="p38953514"></a>backup_name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1118085"><a name="p1118085"></a><a name="p1118085"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p23456073"><a name="p23456073"></a><a name="p23456073"></a>Name of the backup record.</p>
</td>
</tr>
<tr id="row9778065"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p53825796"><a name="p53825796"></a><a name="p53825796"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p64922228"><a name="p64922228"></a><a name="p64922228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p24209096"><a name="p24209096"></a><a name="p24209096"></a>Error code returned if DCS instance backup fails.</p>
<p id="p16555275"><a name="p16555275"></a><a name="p16555275"></a>For details about error codes, see <a href="#table19168847155017">Table 4</a>.</p>
</td>
</tr>
<tr id="row65908913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p37021743"><a name="p37021743"></a><a name="p37021743"></a>is_support_restore</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p45971246"><a name="p45971246"></a><a name="p45971246"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p32683478"><a name="p32683478"></a><a name="p32683478"></a>An indicator of whether restoration is supported. The value can be <strong id="b25715848"><a name="b25715848"></a><a name="b25715848"></a>TRUE</strong> or <strong id="b30116046"><a name="b30116046"></a><a name="b30116046"></a>FALSE</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Error codes returned in case of a backup or restoration failure

<a name="table19168847155017"></a>
<table><thead align="left"><tr id="row39099120"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p12912137"><a name="p12912137"></a><a name="p12912137"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p39250175"><a name="p39250175"></a><a name="p39250175"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25147577"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p23687839"><a name="p23687839"></a><a name="p23687839"></a>dcs.08.0001</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p39666843"><a name="p39666843"></a><a name="p39666843"></a>Failed to start the backup and restore tool.</p>
</td>
</tr>
<tr id="row21457267"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p60317096"><a name="p60317096"></a><a name="p60317096"></a>dcs.08.0002</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p53846630"><a name="p53846630"></a><a name="p53846630"></a>Operation timed out.</p>
</td>
</tr>
<tr id="row14857623"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p62616820"><a name="p62616820"></a><a name="p62616820"></a>dcs.08.0003</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p38797678"><a name="p38797678"></a><a name="p38797678"></a>Failed to delete bucket.</p>
</td>
</tr>
<tr id="row13634785"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p30675792"><a name="p30675792"></a><a name="p30675792"></a>dcs.08.0004</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1711248"><a name="p1711248"></a><a name="p1711248"></a>Failed to obtain AK/SK.</p>
</td>
</tr>
<tr id="row15401238"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p39540754"><a name="p39540754"></a><a name="p39540754"></a>dcs.08.0005</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p48684466"><a name="p48684466"></a><a name="p48684466"></a>Failed to create bucket.</p>
</td>
</tr>
<tr id="row35507011"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p57495637"><a name="p57495637"></a><a name="p57495637"></a>dcs.08.0006</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p26635007"><a name="p26635007"></a><a name="p26635007"></a>Failed to obtain backup file size.</p>
</td>
</tr>
<tr id="row38388477"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p22458943"><a name="p22458943"></a><a name="p22458943"></a>dcs.08.0007</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p7235118"><a name="p7235118"></a><a name="p7235118"></a>Data synchronization failed during instance restoration.</p>
</td>
</tr>
<tr id="row65116065"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p39909950"><a name="p39909950"></a><a name="p39909950"></a>dcs.08.0008</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p11480507"><a name="p11480507"></a><a name="p11480507"></a>Automatic backup of the instance cannot start because the instance is running other jobs.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

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


