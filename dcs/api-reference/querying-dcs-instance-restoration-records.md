# Querying DCS Instance Restoration Records<a name="dcs-api-0312023"></a>

## Function<a name="section20779854161013"></a>

This API is used to query the restoration records of a specified DCS instance.

## URI<a name="section10627123311133"></a>

GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/restores?start=\{start\}&limit=\{limit\}&beginTime=\{beginTime\}&endTime=\{endTime\}

[Table 1](#table1899262913382)  describes the parameters.

**Table  1**  Parameter description

<a name="table1899262913382"></a>
<table><thead align="left"><tr id="row1599115293389"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15991152913819"><a name="p15991152913819"></a><a name="p15991152913819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p129916298387"><a name="p129916298387"></a><a name="p129916298387"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p13991142913384"><a name="p13991142913384"></a><a name="p13991142913384"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1991329193814"><a name="p1991329193814"></a><a name="p1991329193814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11992929163813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1256118557236"><a name="p1256118557236"></a><a name="p1256118557236"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1756110555237"><a name="p1756110555237"></a><a name="p1756110555237"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p195611055112314"><a name="p195611055112314"></a><a name="p195611055112314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p19561175562312"><a name="p19561175562312"></a><a name="p19561175562312"></a>Project ID.</p>
</td>
</tr>
<tr id="row1802105014239"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7562555122310"><a name="p7562555122310"></a><a name="p7562555122310"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p25629552238"><a name="p25629552238"></a><a name="p25629552238"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4562135513237"><a name="p4562135513237"></a><a name="p4562135513237"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p45621055152310"><a name="p45621055152310"></a><a name="p45621055152310"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row319585116234"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1562155502313"><a name="p1562155502313"></a><a name="p1562155502313"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p5562135519239"><a name="p5562135519239"></a><a name="p5562135519239"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p356265542319"><a name="p356265542319"></a><a name="p356265542319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p12562455202313"><a name="p12562455202313"></a><a name="p12562455202313"></a>Start sequence number of the restoration record to be queried. By default, this parameter is set to <strong id="b418831779"><a name="b418831779"></a><a name="b418831779"></a>1</strong>.</p>
</td>
</tr>
<tr id="row5563551152313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p75621955142315"><a name="p75621955142315"></a><a name="p75621955142315"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p14562115582312"><a name="p14562115582312"></a><a name="p14562115582312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p12562115515234"><a name="p12562115515234"></a><a name="p12562115515234"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p11562145515237"><a name="p11562145515237"></a><a name="p11562145515237"></a>Number of restoration records displayed on each page. The minimum value of this parameter is <strong id="b698477872"><a name="b698477872"></a><a name="b698477872"></a>1</strong>. If this parameter is not specified, 10 restoration records are displayed on each page by default.</p>
</td>
</tr>
<tr id="row1473645152319"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15631055162314"><a name="p15631055162314"></a><a name="p15631055162314"></a>beginTime</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1956395502312"><a name="p1956395502312"></a><a name="p1956395502312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p14563115522319"><a name="p14563115522319"></a><a name="p14563115522319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p16563175562318"><a name="p16563175562318"></a><a name="p16563175562318"></a>Start time of the period to be queried. Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
<tr id="row1690510515236"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6563755122319"><a name="p6563755122319"></a><a name="p6563755122319"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7563175512318"><a name="p7563175512318"></a><a name="p7563175512318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p8563145519235"><a name="p8563145519235"></a><a name="p8563145519235"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1564355172311"><a name="p1564355172311"></a><a name="p1564355172311"></a>End time of the period to be queried. Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17412144620133"></a>

**Request parameters**

None.

**Example request**

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/restores?start={start}&limit={limit}&beginTime={beginTime}&endTime={endTime}
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
<tbody><tr id="row166121557203812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4952127112514"><a name="p4952127112514"></a><a name="p4952127112514"></a>restore_record_response</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p12952175251"><a name="p12952175251"></a><a name="p12952175251"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p16952576257"><a name="p16952576257"></a><a name="p16952576257"></a>Array of the restoration records.</p>
</td>
</tr>
<tr id="row378033719215"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1490220481211"><a name="p1490220481211"></a><a name="p1490220481211"></a>total_num</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p390214481123"><a name="p390214481123"></a><a name="p390214481123"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p3902248726"><a name="p3902248726"></a><a name="p3902248726"></a>Number of obtained backup records.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  restore\_record\_response parameter description

<a name="table8487183718255"></a>
<table><thead align="left"><tr id="row14488193732512"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="p1348853762517"><a name="p1348853762517"></a><a name="p1348853762517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p4488123742513"><a name="p4488123742513"></a><a name="p4488123742513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p348853716256"><a name="p348853716256"></a><a name="p348853716256"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1048833719252"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p114001551142519"><a name="p114001551142519"></a><a name="p114001551142519"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p10400185162514"><a name="p10400185162514"></a><a name="p10400185162514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p04001251102510"><a name="p04001251102510"></a><a name="p04001251102510"></a>Restoration status</p>
<a name="ul19239161818492"></a><a name="ul19239161818492"></a><ul id="ul19239161818492"><li><strong id="b128611546141815"><a name="b128611546141815"></a><a name="b128611546141815"></a>waiting</strong>: DCS instance restoration is waiting to begin.</li><li><strong id="b17952140548"><a name="b17952140548"></a><a name="b17952140548"></a>restoring</strong>: DCS instance restoration is in progress. </li><li><strong id="b93131151542"><a name="b93131151542"></a><a name="b93131151542"></a>succeed</strong>: DCS instance restoration succeeded. </li><li><strong id="b6563172615544"><a name="b6563172615544"></a><a name="b6563172615544"></a>failed</strong>: DCS instance restoration failed.</li></ul>
</td>
</tr>
<tr id="row010184317256"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p240075117259"><a name="p240075117259"></a><a name="p240075117259"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p240011517257"><a name="p240011517257"></a><a name="p240011517257"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p8400135112252"><a name="p8400135112252"></a><a name="p8400135112252"></a>Restoration progress</p>
</td>
</tr>
<tr id="row1519594318252"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p0400195102512"><a name="p0400195102512"></a><a name="p0400195102512"></a>restore_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p174001751132512"><a name="p174001751132512"></a><a name="p174001751132512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p740075111253"><a name="p740075111253"></a><a name="p740075111253"></a>ID of the restoration record</p>
</td>
</tr>
<tr id="row16385543152519"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p1840055192511"><a name="p1840055192511"></a><a name="p1840055192511"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p13400105118252"><a name="p13400105118252"></a><a name="p13400105118252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p74001851152520"><a name="p74001851152520"></a><a name="p74001851152520"></a>ID of the backup record</p>
</td>
</tr>
<tr id="row856044319253"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p1140010519258"><a name="p1140010519258"></a><a name="p1140010519258"></a>restore_remark</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p640018510255"><a name="p640018510255"></a><a name="p640018510255"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p64001151182518"><a name="p64001151182518"></a><a name="p64001151182518"></a>Description of DCS instance restoration</p>
</td>
</tr>
<tr id="row1272674352515"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p13400195111259"><a name="p13400195111259"></a><a name="p13400195111259"></a>backup_remark</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p144001851182519"><a name="p144001851182519"></a><a name="p144001851182519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p5400195113258"><a name="p5400195113258"></a><a name="p5400195113258"></a>Description of DCS instance backup</p>
</td>
</tr>
<tr id="row284015436258"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p740005102516"><a name="p740005102516"></a><a name="p740005102516"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1400351112519"><a name="p1400351112519"></a><a name="p1400351112519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p0400751152514"><a name="p0400751152514"></a><a name="p0400751152514"></a>Time at which the restoration task is created</p>
</td>
</tr>
<tr id="row5985114332513"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p040105102512"><a name="p040105102512"></a><a name="p040105102512"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p040195119251"><a name="p040195119251"></a><a name="p040195119251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p8401185112516"><a name="p8401185112516"></a><a name="p8401185112516"></a>Time at which DCS instance restoration completed</p>
</td>
</tr>
<tr id="row2015594462514"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p1240115114252"><a name="p1240115114252"></a><a name="p1240115114252"></a>restore_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p74015519256"><a name="p74015519256"></a><a name="p74015519256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p19401851162515"><a name="p19401851162515"></a><a name="p19401851162515"></a>Name of the restoration record</p>
</td>
</tr>
<tr id="row139417445256"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p8401165142516"><a name="p8401165142516"></a><a name="p8401165142516"></a>backup_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p440116515254"><a name="p440116515254"></a><a name="p440116515254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p6401351102519"><a name="p6401351102519"></a><a name="p6401351102519"></a>Name of the backup record</p>
</td>
</tr>
<tr id="row1455424418252"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p94011151172510"><a name="p94011151172510"></a><a name="p94011151172510"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p13401351162517"><a name="p13401351162517"></a><a name="p13401351162517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p940115517252"><a name="p940115517252"></a><a name="p940115517252"></a>Error code returned if DCS instance restoration fails. For details about error codes, see <a href="querying-dcs-instance-backup-records.md#table1255361919491">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "restore_record_response": [
        {
            "status": "succeed",
            "progress": "100.00",
            "restore_id": "a6155972-800c-4170-a479-3231e907d2f6",
            "backup_id": "f4823e9e-fe9b-4ffd-be79-4e5d6de272bb",
            "restore_remark": "doctest",
            "backup_remark": null,
            "created_at": "2017-07-18T21:41:20.721Z",
            "updated_at": "2017-07-18T21:41:35.182Z",
            "restore_name": "restore_20170718214120",
            "backup_name": "backup_20170718000002",
            "error_code": null
        }
    ],
    "total_num": 1
}
```

## Status Code<a name="section4860101417132"></a>

[Table 4](#table486141410130)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table486141410130"></a>
<table><thead align="left"><tr id="row18616141139"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1986191418133"><a name="p1986191418133"></a><a name="p1986191418133"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p18861111415138"><a name="p18861111415138"></a><a name="p18861111415138"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row786131451312"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p6861114181311"><a name="p6861114181311"></a><a name="p6861114181311"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p6330445162818"><a name="p6330445162818"></a><a name="p6330445162818"></a>DCS instance restoration record queried successfully.</p>
</td>
</tr>
</tbody>
</table>

