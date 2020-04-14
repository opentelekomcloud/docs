# Querying a VPC Peering Connection<a name="vpc_peering_0002"></a>

## Function<a name="section1018045115610"></a>

This API is used to query details about a VPC peering connection.

## URI<a name="section121811651468"></a>

GET /v2.0/vpc/peerings/\{peering\_id\}

[Table 1](#table18880184689)  describes the parameters.

**Table  1**  Parameter description

<a name="table18880184689"></a>
<table><thead align="left"><tr id="row13968641385"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p209684410817"><a name="p209684410817"></a><a name="p209684410817"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p69681441386"><a name="p69681441386"></a><a name="p69681441386"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p1096813412811"><a name="p1096813412811"></a><a name="p1096813412811"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p139686416813"><a name="p139686416813"></a><a name="p139686416813"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1013244217196"><a name="p1013244217196"></a><a name="p1013244217196"></a>peering_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies the VPC peering connection ID, which uniquely identifies the VPC peering connection. The <strong id="b842352706144243"><a name="b842352706144243"></a><a name="b842352706144243"></a>peering_id</strong> value is used as the filter.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section101901751566"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0/vpc/peerings/22b76469-08e3-4937-8c1d-7aad34892be1
    ```


## Response Message<a name="section101901851869"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table919115511064"></a>
    <table><thead align="left"><tr id="row436713511462"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p23677513619"><a name="p23677513619"></a><a name="p23677513619"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p18367251264"><a name="p18367251264"></a><a name="p18367251264"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p1136715519612"><a name="p1136715519612"></a><a name="p1136715519612"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row93671514617"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p13367651061"><a name="p13367651061"></a><a name="p13367651061"></a>peering</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p936745111620"><a name="p936745111620"></a><a name="p936745111620"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p1036719511614"><a name="p1036719511614"></a><a name="p1036719511614"></a>Specifies the VPC peering connection object list. For details, see <a href="#table1026243410414">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **peering**  objects

    <a name="table1026243410414"></a>
    <table><thead align="left"><tr id="row145386341548"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p553843415417"><a name="p553843415417"></a><a name="p553843415417"></a><strong id="b13521521193113"><a name="b13521521193113"></a><a name="b13521521193113"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p453814344418"><a name="p453814344418"></a><a name="p453814344418"></a><strong id="b8393522113112"><a name="b8393522113112"></a><a name="b8393522113112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p13539183410412"><a name="p13539183410412"></a><a name="p13539183410412"></a><strong id="b10312132312313"><a name="b10312132312313"></a><a name="b10312132312313"></a>Description</strong></p>
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
    <a name="ul6640134318521"></a><a name="ul6640134318521"></a><ul id="ul6640134318521"><li><strong id="b1662883413311"><a name="b1662883413311"></a><a name="b1662883413311"></a>PENDING_ACCEPTANCE</strong></li><li><strong id="b104441235133118"><a name="b104441235133118"></a><a name="b104441235133118"></a>REJECTED</strong></li><li><strong id="b11641036133114"><a name="b11641036133114"></a><a name="b11641036133114"></a>EXPIRED</strong></li><li><strong id="b12730103733120"><a name="b12730103733120"></a><a name="b12730103733120"></a>DELETED</strong></li><li><strong id="b6352938163119"><a name="b6352938163119"></a><a name="b6352938163119"></a>ACTIVE</strong></li></ul>
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
    <p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1085175123211"><a name="i1085175123211"></a><a name="i1085175123211"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    <tr id="row15465113115319"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p74651838533"><a name="p74651838533"></a><a name="p74651838533"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p8465203125315"><a name="p8465203125315"></a><a name="p8465203125315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p271618182568"><a name="p271618182568"></a><a name="p271618182568"></a>Specifies the time (UTC) when the VPC peering connection is updated.</p>
    <p id="p187161918125617"><a name="p187161918125617"></a><a name="p187161918125617"></a>Format: <em id="i12818202683215"><a name="i12818202683215"></a><a name="i12818202683215"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **vpc\_info**  objects

    <a name="table1132310347417"></a>
    <table><thead align="left"><tr id="row65431034046"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p14543173418413"><a name="p14543173418413"></a><a name="p14543173418413"></a><strong id="b130133015324"><a name="b130133015324"></a><a name="b130133015324"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p1354353413410"><a name="p1354353413410"></a><a name="p1354353413410"></a><strong id="b09719317322"><a name="b09719317322"></a><a name="b09719317322"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p19543634641"><a name="p19543634641"></a><a name="p19543634641"></a><strong id="b138551031203220"><a name="b138551031203220"></a><a name="b138551031203220"></a>Description</strong></p>
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
        "peering": { 
            "name": "test", 
            "id": "22b76469-08e3-4937-8c1d-7aad34892be1",
            "request_vpc_info": {
               "vpc_id": "9daeac7c-a98f-430f-8e38-67f9c044e299",
               "tenant_id": "f65e9ebc-ed5d-418b-a931-9a723718ba4e"
            },
            "accept_vpc_info": {
               "vpc_id": "f583c072-0bb8-4e19-afb2-afb7c1693be5",
               "tenant_id": "f65e9ebc-ed5d-418b-a931-9a723718ba4e"
            }, 
            "status": "ACTIVE"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

