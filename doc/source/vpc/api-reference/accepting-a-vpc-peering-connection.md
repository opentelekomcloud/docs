# Accepting a VPC Peering Connection<a name="vpc_peering_0004"></a>

## Function<a name="section33324291770"></a>

After tenant A requests to create a VPC peering connection with a VPC of tenant B. Tenant B must accept the request to make the VPC peering connection take effect. This API is used by a tenant to accept a VPC peering connection request initiated by another tenant.

## URI<a name="section93331298714"></a>

PUT /v2.0/vpc/peerings/\{peering\_id\}/accept

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
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies the VPC peering connection ID, which uniquely identifies the VPC peering connection.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section933915291717"></a>

-   Request parameter

    None


-   Example request

    ```
    PUT https://{Endpoint}/v2.0/vpc/peerings/22b76469-08e3-4937-8c1d-7aad34892be1/accept
    ```


## Response Message<a name="section334002913710"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table14258131481112"></a>
    <table><thead align="left"><tr id="row1525861441116"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p625881431111"><a name="p625881431111"></a><a name="p625881431111"></a><strong id="b4438831711"><a name="b4438831711"></a><a name="b4438831711"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p325891414115"><a name="p325891414115"></a><a name="p325891414115"></a><strong id="b122511157177"><a name="b122511157177"></a><a name="b122511157177"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p1325811410110"><a name="p1325811410110"></a><a name="p1325811410110"></a><strong id="b4673191801718"><a name="b4673191801718"></a><a name="b4673191801718"></a>Description</strong></p>
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
    <tr id="row6258114111117"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p2258514141119"><a name="p2258514141119"></a><a name="p2258514141119"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p172581414111119"><a name="p172581414111119"></a><a name="p172581414111119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p225811149115"><a name="p225811149115"></a><a name="p225811149115"></a>Specifies the VPC peering connection name.</p>
    </td>
    </tr>
    <tr id="row45401734847"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p354083416417"><a name="p354083416417"></a><a name="p354083416417"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p11540034946"><a name="p11540034946"></a><a name="p11540034946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p11298143785016"><a name="p11298143785016"></a><a name="p11298143785016"></a>Specifies the VPC peering connection status. Possible values are as follows:</p>
    <a name="ul6640134318521"></a><a name="ul6640134318521"></a><ul id="ul6640134318521"><li><strong id="b91082154229"><a name="b91082154229"></a><a name="b91082154229"></a>PENDING_ACCEPTANCE</strong></li><li><strong id="b454961722215"><a name="b454961722215"></a><a name="b454961722215"></a>REJECTED</strong></li><li><strong id="b6625121892211"><a name="b6625121892211"></a><a name="b6625121892211"></a>EXPIRED</strong></li><li><strong id="b18918121962210"><a name="b18918121962210"></a><a name="b18918121962210"></a>DELETED</strong></li><li><strong id="b1087352072210"><a name="b1087352072210"></a><a name="b1087352072210"></a>ACTIVE</strong></li></ul>
    </td>
    </tr>
    <tr id="row925801431119"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p825911451110"><a name="p825911451110"></a><a name="p825911451110"></a>request_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p1425911414113"><a name="p1425911414113"></a><a name="p1425911414113"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p12259181441112"><a name="p12259181441112"></a><a name="p12259181441112"></a>Specifies information about the local VPC. For details, see <a href="#table1125991417114">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row0259161401118"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p725941415110"><a name="p725941415110"></a><a name="p725941415110"></a>accept_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p14259111441119"><a name="p14259111441119"></a><a name="p14259111441119"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p1225921416112"><a name="p1225921416112"></a><a name="p1225921416112"></a>Specifies information about the peer VPC. For details, see <a href="#table1125991417114">Table 3</a>.</p>
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
    <p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i357718228239"><a name="i357718228239"></a><a name="i357718228239"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    <tr id="row15465113115319"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p74651838533"><a name="p74651838533"></a><a name="p74651838533"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p8465203125315"><a name="p8465203125315"></a><a name="p8465203125315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p271618182568"><a name="p271618182568"></a><a name="p271618182568"></a>Specifies the time (UTC) when the VPC peering connection is updated.</p>
    <p id="p187161918125617"><a name="p187161918125617"></a><a name="p187161918125617"></a>Format: <em id="i224573272512"><a name="i224573272512"></a><a name="i224573272512"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **vpc\_info**  objects

    <a name="table1125991417114"></a>
    <table><thead align="left"><tr id="row1725931413118"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p122592014121114"><a name="p122592014121114"></a><a name="p122592014121114"></a><strong id="b12293434152513"><a name="b12293434152513"></a><a name="b12293434152513"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p11259121417111"><a name="p11259121417111"></a><a name="p11259121417111"></a><strong id="b108591536162512"><a name="b108591536162512"></a><a name="b108591536162512"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p17259191412115"><a name="p17259191412115"></a><a name="p17259191412115"></a><strong id="b1716163714255"><a name="b1716163714255"></a><a name="b1716163714255"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4259191411115"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p1125911141118"><a name="p1125911141118"></a><a name="p1125911141118"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p1026031417117"><a name="p1026031417117"></a><a name="p1026031417117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p926061418117"><a name="p926061418117"></a><a name="p926061418117"></a>Specifies the ID of a VPC involved in a VPC peering connection.</p>
    </td>
    </tr>
    <tr id="row1326013145116"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p72601514191115"><a name="p72601514191115"></a><a name="p72601514191115"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p3260171410114"><a name="p3260171410114"></a><a name="p3260171410114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p326071415115"><a name="p326071415115"></a><a name="p326071415115"></a>Specifies the ID of the project to which a VPC involved in the VPC peering connection belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {  
        "name": "test", 
       "id": "22b76469-08e3-4937-8c1d-7aad34892be1",
        "request_vpc_info": {
            "vpc_id": "9daeac7c-a98f-430f-8e38-67f9c044e299",
            "tenant_id": "f65e9ebc-ed5d-418b-a931-9a723718ba4e"
        },
        "accept_vpc_info": {
            "vpc_id": "f583c072-0bb8-4e19-afb2-afb7c1693be5",
             "tenant_id": "059a737356594b41b447b557bf0aae56"
        }, 
        "status": "ACTIVE"
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

