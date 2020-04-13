# Querying VPC Peering Connections<a name="vpc_peering_0001"></a>

## Function<a name="section16041996617"></a>

This API is used to query all VPC peering connections accessible to the tenant submitting the request. The connections are filtered based on the filtering condition. For details about pagination query, see section  [Pagination](pagination.md).

## URI<a name="section13605791466"></a>

GET /v2.0/vpc/peerings

Example:

```
GET https://{Endpoint}/v2.0/vpc/peerings?id={id}&name={name}&status={status}&tenant_id={tenant_id}&vpc_id={vpc_id}&limit={limit}&marker={marker}
```

[Table 1](#table18880184689)  describes the parameters.

**Table  1**  Parameter description

<a name="table18880184689"></a>
<table><thead align="left"><tr id="row13968641385"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p209684410817"><a name="p209684410817"></a><a name="p209684410817"></a><strong id="b3371155162638"><a name="b3371155162638"></a><a name="b3371155162638"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p69681441386"><a name="p69681441386"></a><a name="p69681441386"></a><strong id="b842352706145619"><a name="b842352706145619"></a><a name="b842352706145619"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p1096813412811"><a name="p1096813412811"></a><a name="p1096813412811"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p139686416813"><a name="p139686416813"></a><a name="p139686416813"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p9968124681"><a name="p9968124681"></a><a name="p9968124681"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies that the VPC peering connection ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row19701641482"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p16970114781"><a name="p16970114781"></a><a name="p16970114781"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p199701142815"><a name="p199701142815"></a><a name="p199701142815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p79702041182"><a name="p79702041182"></a><a name="p79702041182"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><a name="ul159912181345"></a><a name="ul159912181345"></a><ul id="ul159912181345"><li>Specifies that the peering connection name is used as the filter.</li><li>The value can contain no more than 64 characters.</li></ul>
</td>
</tr>
<tr id="row3970246817"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p189701141985"><a name="p189701141985"></a><a name="p189701141985"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p179703415816"><a name="p179703415816"></a><a name="p179703415816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p7970749816"><a name="p7970749816"></a><a name="p7970749816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p149701242818"><a name="p149701242818"></a><a name="p149701242818"></a>Specifies that the VPC peering connection status is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1497012413813"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p199701941181"><a name="p199701941181"></a><a name="p199701941181"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1297013420819"><a name="p1297013420819"></a><a name="p1297013420819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p12970114088"><a name="p12970114088"></a><a name="p12970114088"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p169701241984"><a name="p169701241984"></a><a name="p169701241984"></a>Specifies that the tenant ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row297024581"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p39709420813"><a name="p39709420813"></a><a name="p39709420813"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p169701241084"><a name="p169701241084"></a><a name="p169701241084"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p1997074181"><a name="p1997074181"></a><a name="p1997074181"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p1997014414818"><a name="p1997014414818"></a><a name="p1997014414818"></a>Specifies that the VPC ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row119701147813"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p199701641815"><a name="p199701641815"></a><a name="p199701641815"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p19970164582"><a name="p19970164582"></a><a name="p19970164582"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p209701447813"><a name="p209701447813"></a><a name="p209701447813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p15970134789"><a name="p15970134789"></a><a name="p15970134789"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row139701041081"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p159700419815"><a name="p159700419815"></a><a name="p159700419815"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p49705419812"><a name="p49705419812"></a><a name="p49705419812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p17970447810"><a name="p17970447810"></a><a name="p17970447810"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><a name="ul163210261944"></a><a name="ul163210261944"></a><ul id="ul163210261944"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li><li>The default value is <strong id="b990318110244"><a name="b990318110244"></a><a name="b990318110244"></a>2000</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section20611598617"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0/vpc/peerings
    ```


## Response Message<a name="section19612491665"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table116121920611"></a>
    <table><thead align="left"><tr id="row7829129169"><th class="cellrowborder" valign="top" width="22.09%" id="mcps1.2.4.1.1"><p id="p382916918611"><a name="p382916918611"></a><a name="p382916918611"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.42%" id="mcps1.2.4.1.2"><p id="p16829391367"><a name="p16829391367"></a><a name="p16829391367"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1282919368"><a name="p1282919368"></a><a name="p1282919368"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row882919669"><td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.2.4.1.1 "><p id="p138291791061"><a name="p138291791061"></a><a name="p138291791061"></a>peerings</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.42%" headers="mcps1.2.4.1.2 "><p id="p23471057175910"><a name="p23471057175910"></a><a name="p23471057175910"></a>Array of <a href="#table1026243410414">peering</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p5829109666"><a name="p5829109666"></a><a name="p5829109666"></a>Specifies the VPC peering connection object list. For details, see <a href="#table1026243410414">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **peering**  objects

    <a name="table1026243410414"></a>
    <table><thead align="left"><tr id="row145386341548"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p553843415417"><a name="p553843415417"></a><a name="p553843415417"></a><strong id="b111375042420"><a name="b111375042420"></a><a name="b111375042420"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p453814344418"><a name="p453814344418"></a><a name="p453814344418"></a><strong id="b20671165110249"><a name="b20671165110249"></a><a name="b20671165110249"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p13539183410412"><a name="p13539183410412"></a><a name="p13539183410412"></a><strong id="b9221155314242"><a name="b9221155314242"></a><a name="b9221155314242"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row195391034944"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p1053943410414"><a name="p1053943410414"></a><a name="p1053943410414"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p753963414417"><a name="p753963414417"></a><a name="p753963414417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p17539123411413"><a name="p17539123411413"></a><a name="p17539123411413"></a>Specifies the VPC peering connection ID.</p>
    </td>
    </tr>
    <tr id="row185391134449"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p15540123413417"><a name="p15540123413417"></a><a name="p15540123413417"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p85405341547"><a name="p85405341547"></a><a name="p85405341547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p1654017341747"><a name="p1654017341747"></a><a name="p1654017341747"></a>Specifies the VPC peering connection name.</p>
    </td>
    </tr>
    <tr id="row45401734847"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p354083416417"><a name="p354083416417"></a><a name="p354083416417"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p11540034946"><a name="p11540034946"></a><a name="p11540034946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p11298143785016"><a name="p11298143785016"></a><a name="p11298143785016"></a>Specifies the VPC peering connection status. Possible values are as follows:</p>
    <a name="ul6640134318521"></a><a name="ul6640134318521"></a><ul id="ul6640134318521"><li><strong id="b1115813562257"><a name="b1115813562257"></a><a name="b1115813562257"></a>PENDING_ACCEPTANCE</strong></li><li><strong id="b6368115792515"><a name="b6368115792515"></a><a name="b6368115792515"></a>REJECTED</strong></li><li><strong id="b3204112972619"><a name="b3204112972619"></a><a name="b3204112972619"></a>EXPIRED</strong></li><li><strong id="b92416425268"><a name="b92416425268"></a><a name="b92416425268"></a>DELETED</strong></li><li><strong id="b3500154916263"><a name="b3500154916263"></a><a name="b3500154916263"></a>ACTIVE</strong></li></ul>
    </td>
    </tr>
    <tr id="row155415343411"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p185411334349"><a name="p185411334349"></a><a name="p185411334349"></a>request_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p1854183414414"><a name="p1854183414414"></a><a name="p1854183414414"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p155422348412"><a name="p155422348412"></a><a name="p155422348412"></a>Specifies information about the local VPC. For details, see <a href="#table1132310347417">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row145425341249"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p25421834641"><a name="p25421834641"></a><a name="p25421834641"></a>accept_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p354211341141"><a name="p354211341141"></a><a name="p354211341141"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p3542143419414"><a name="p3542143419414"></a><a name="p3542143419414"></a>Specifies information about the peer VPC. For details, see <a href="#table1132310347417">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row17791105316527"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p9792195385219"><a name="p9792195385219"></a><a name="p9792195385219"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p3792205365218"><a name="p3792205365218"></a><a name="p3792205365218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p10792953155215"><a name="p10792953155215"></a><a name="p10792953155215"></a>Provides supplementary information about the VPC peering connection.</p>
    </td>
    </tr>
    <tr id="row4121155915218"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p1312155914528"><a name="p1312155914528"></a><a name="p1312155914528"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p201218597524"><a name="p201218597524"></a><a name="p201218597524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the VPC peering connection is created.</p>
    <p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i795319519271"><a name="i795319519271"></a><a name="i795319519271"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    <tr id="row15465113115319"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p74651838533"><a name="p74651838533"></a><a name="p74651838533"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p8465203125315"><a name="p8465203125315"></a><a name="p8465203125315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p271618182568"><a name="p271618182568"></a><a name="p271618182568"></a>Specifies the time (UTC) when the VPC peering connection is updated.</p>
    <p id="p187161918125617"><a name="p187161918125617"></a><a name="p187161918125617"></a>Format: <em id="i81512617280"><a name="i81512617280"></a><a name="i81512617280"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **vpc\_info**  objects

    <a name="table1132310347417"></a>
    <table><thead align="left"><tr id="row65431034046"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p14543173418413"><a name="p14543173418413"></a><a name="p14543173418413"></a><strong id="b1140044442814"><a name="b1140044442814"></a><a name="b1140044442814"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p1354353413410"><a name="p1354353413410"></a><a name="p1354353413410"></a><strong id="b3357134617282"><a name="b3357134617282"></a><a name="b3357134617282"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p19543634641"><a name="p19543634641"></a><a name="p19543634641"></a><strong id="b915154732817"><a name="b915154732817"></a><a name="b915154732817"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4543434247"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p13544163416415"><a name="p13544163416415"></a><a name="p13544163416415"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p654410341549"><a name="p654410341549"></a><a name="p654410341549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p55448348416"><a name="p55448348416"></a><a name="p55448348416"></a>Specifies the ID of a VPC involved in a VPC peering connection.</p>
    </td>
    </tr>
    <tr id="row65441334646"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p14544034945"><a name="p14544034945"></a><a name="p14544034945"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p454413347419"><a name="p454413347419"></a><a name="p454413347419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p105449344410"><a name="p105449344410"></a><a name="p105449344410"></a>Specifies the ID of the project to which a VPC involved in the VPC peering connection belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "peerings": [
            {
                "request_vpc_info": {
                    "vpc_id": "9daeac7c-a98f-430f-8e38-67f9c044e299",
                    "tenant_id": "f65e9ebc-ed5d-418b-a931-9a723718ba4e"
                },
                "accept_vpc_info": {
                    "vpc_id": "f583c072-0bb8-4e19-afb2-afb7c1693be5",
                    "tenant_id": "f65e9ebc-ed5d-418b-a931-9a723718ba4e"
                },
                "name": "test",
                "id": "b147a74b-39bb-4c7a-aed5-19cac4c2df13",
                "status": "ACTIVE"
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

