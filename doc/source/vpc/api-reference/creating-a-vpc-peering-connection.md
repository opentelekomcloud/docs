# Creating a VPC Peering Connection<a name="vpc_peering_0003"></a>

## Function<a name="section18987589718"></a>

This API is used to create a VPC peering connection.

If you create a VPC peering connection with another VPC of your own, the connection is created without the need for you to accept the connection.

If you create a VPC peering connection with a VPC of another tenant, the peer tenant must accept the connection so that the connection can be created. If the peer tenant refuses the connection, it cannot be created.

## URI<a name="section29889818711"></a>

POST /v2.0/vpc/peerings

## Request Message<a name="section39941481775"></a>

-   Request parameter

    **Table  1**  Request parameter

    <a name="table1699419817711"></a>
    <table><thead align="left"><tr id="row71471891872"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.5.1.1"><p id="p11147299719"><a name="p11147299719"></a><a name="p11147299719"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="8.129999999999999%" id="mcps1.2.5.1.2"><p id="p81044352112"><a name="p81044352112"></a><a name="p81044352112"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10.09%" id="mcps1.2.5.1.3"><p id="p5147295710"><a name="p5147295710"></a><a name="p5147295710"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="67.64%" id="mcps1.2.5.1.4"><p id="p3147493713"><a name="p3147493713"></a><a name="p3147493713"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row314712915720"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p31471491176"><a name="p31471491176"></a><a name="p31471491176"></a>peering</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.129999999999999%" headers="mcps1.2.5.1.2 "><p id="p31074342118"><a name="p31074342118"></a><a name="p31074342118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.09%" headers="mcps1.2.5.1.3 "><p id="p17147129372"><a name="p17147129372"></a><a name="p17147129372"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.64%" headers="mcps1.2.5.1.4 "><p id="p1036719511614"><a name="p1036719511614"></a><a name="p1036719511614"></a>Specifies the VPC peering connection object list. For details, see <a href="#table1026243410414">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the  **peering**  field

    <a name="table1026243410414"></a>
    <table><thead align="left"><tr id="row145386341548"><th class="cellrowborder" valign="top" width="23.18%" id="mcps1.2.5.1.1"><p id="p553843415417"><a name="p553843415417"></a><a name="p553843415417"></a><strong id="b217918212349"><a name="b217918212349"></a><a name="b217918212349"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.69%" id="mcps1.2.5.1.2"><p id="p98691347587"><a name="p98691347587"></a><a name="p98691347587"></a><strong id="b42607311344"><a name="b42607311344"></a><a name="b42607311344"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.67%" id="mcps1.2.5.1.3"><p id="p453814344418"><a name="p453814344418"></a><a name="p453814344418"></a><strong id="b04994411346"><a name="b04994411346"></a><a name="b04994411346"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.46%" id="mcps1.2.5.1.4"><p id="p13539183410412"><a name="p13539183410412"></a><a name="p13539183410412"></a><strong id="b842714583411"><a name="b842714583411"></a><a name="b842714583411"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row185391134449"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.5.1.1 "><p id="p15540123413417"><a name="p15540123413417"></a><a name="p15540123413417"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.69%" headers="mcps1.2.5.1.2 "><p id="p17869133485814"><a name="p17869133485814"></a><a name="p17869133485814"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.5.1.3 "><p id="p85405341547"><a name="p85405341547"></a><a name="p85405341547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.46%" headers="mcps1.2.5.1.4 "><p id="p1654017341747"><a name="p1654017341747"></a><a name="p1654017341747"></a>Specifies the name of the VPC peering connection. The value can contain 1 to 64 characters.</p>
    </td>
    </tr>
    <tr id="row155415343411"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.5.1.1 "><p id="p185411334349"><a name="p185411334349"></a><a name="p185411334349"></a>request_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.69%" headers="mcps1.2.5.1.2 "><p id="p15869434165816"><a name="p15869434165816"></a><a name="p15869434165816"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.5.1.3 "><p id="p1854183414414"><a name="p1854183414414"></a><a name="p1854183414414"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.46%" headers="mcps1.2.5.1.4 "><p id="p155422348412"><a name="p155422348412"></a><a name="p155422348412"></a>Specifies information about the local VPC. For details, see <a href="#table1132310347417">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row145425341249"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.5.1.1 "><p id="p25421834641"><a name="p25421834641"></a><a name="p25421834641"></a>accept_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.69%" headers="mcps1.2.5.1.2 "><p id="p1869834185812"><a name="p1869834185812"></a><a name="p1869834185812"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.5.1.3 "><p id="p354211341141"><a name="p354211341141"></a><a name="p354211341141"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.46%" headers="mcps1.2.5.1.4 "><p id="p3542143419414"><a name="p3542143419414"></a><a name="p3542143419414"></a>Specifies information about the peer VPC. For details, see <a href="#table1132310347417">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **vpc\_info**  field

    <a name="table1132310347417"></a>
    <table><thead align="left"><tr id="row65431034046"><th class="cellrowborder" valign="top" width="23.45%" id="mcps1.2.5.1.1"><p id="p14543173418413"><a name="p14543173418413"></a><a name="p14543173418413"></a><strong id="b6702339369"><a name="b6702339369"></a><a name="b6702339369"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.5.1.2"><p id="p1178104810017"><a name="p1178104810017"></a><a name="p1178104810017"></a><strong id="b1215103410362"><a name="b1215103410362"></a><a name="b1215103410362"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.5.1.3"><p id="p1354353413410"><a name="p1354353413410"></a><a name="p1354353413410"></a><strong id="b16435143511363"><a name="b16435143511363"></a><a name="b16435143511363"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.47%" id="mcps1.2.5.1.4"><p id="p19543634641"><a name="p19543634641"></a><a name="p19543634641"></a><strong id="b457713618369"><a name="b457713618369"></a><a name="b457713618369"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4543434247"><td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.5.1.1 "><p id="p13544163416415"><a name="p13544163416415"></a><a name="p13544163416415"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.5.1.2 "><p id="p2781104816010"><a name="p2781104816010"></a><a name="p2781104816010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.3 "><p id="p654410341549"><a name="p654410341549"></a><a name="p654410341549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.47%" headers="mcps1.2.5.1.4 "><p id="p55448348416"><a name="p55448348416"></a><a name="p55448348416"></a>Specifies the ID of a VPC involved in a VPC peering connection.</p>
    </td>
    </tr>
    <tr id="row65441334646"><td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.5.1.1 "><p id="p14544034945"><a name="p14544034945"></a><a name="p14544034945"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.5.1.2 "><p id="p2078118481808"><a name="p2078118481808"></a><a name="p2078118481808"></a>Yes (when creating a VPC peering connection with a VPC of another account)</p>
    <p id="p1898312291812"><a name="p1898312291812"></a><a name="p1898312291812"></a>No (when creating a VPC peering connection with a VPC of the same account)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.3 "><p id="p454413347419"><a name="p454413347419"></a><a name="p454413347419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.47%" headers="mcps1.2.5.1.4 "><p id="p105449344410"><a name="p105449344410"></a><a name="p105449344410"></a>Specifies the ID of the project to which a VPC involved in the VPC peering connection belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v2.0/vpc/peerings 
    
    { 
        "peering": { 
            "name": "test",  
            "request_vpc_info": {
               "vpc_id": "9daeac7c-a98f-430f-8e38-67f9c044e299"
            }, 
            "accept_vpc_info": {
               "vpc_id": "f583c072-0bb8-4e19-afb2-afb7c1693be5"
            }
        } 
    }
    ```


## Response Message<a name="section124179176"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table351893713"></a>
    <table><thead align="left"><tr id="row91481295715"><th class="cellrowborder" valign="top" width="15.379999999999999%" id="mcps1.2.4.1.1"><p id="p51481696718"><a name="p51481696718"></a><a name="p51481696718"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.99%" id="mcps1.2.4.1.2"><p id="p18148898716"><a name="p18148898716"></a><a name="p18148898716"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.63%" id="mcps1.2.4.1.3"><p id="p11148891674"><a name="p11148891674"></a><a name="p11148891674"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11148093711"><td class="cellrowborder" valign="top" width="15.379999999999999%" headers="mcps1.2.4.1.1 "><p id="p5148791174"><a name="p5148791174"></a><a name="p5148791174"></a>peering</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.99%" headers="mcps1.2.4.1.2 "><p id="p131495911711"><a name="p131495911711"></a><a name="p131495911711"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.63%" headers="mcps1.2.4.1.3 "><p id="p3149109876"><a name="p3149109876"></a><a name="p3149109876"></a>Specifies the <strong id="b421418227504"><a name="b421418227504"></a><a name="b421418227504"></a>peering</strong> objects. For details, see <a href="#table14258131481112">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **peering**  objects

    <a name="table14258131481112"></a>
    <table><thead align="left"><tr id="row1525861441116"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p625881431111"><a name="p625881431111"></a><a name="p625881431111"></a><strong id="b9829201480"><a name="b9829201480"></a><a name="b9829201480"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p325891414115"><a name="p325891414115"></a><a name="p325891414115"></a><strong id="b189911613486"><a name="b189911613486"></a><a name="b189911613486"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p1325811410110"><a name="p1325811410110"></a><a name="p1325811410110"></a><strong id="b13758823483"><a name="b13758823483"></a><a name="b13758823483"></a>Description</strong></p>
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
    <a name="ul6640134318521"></a><a name="ul6640134318521"></a><ul id="ul6640134318521"><li><strong id="b57549231512"><a name="b57549231512"></a><a name="b57549231512"></a>PENDING_ACCEPTANCE</strong></li><li><strong id="b6171725155120"><a name="b6171725155120"></a><a name="b6171725155120"></a>REJECTED</strong></li><li><strong id="b7986325135118"><a name="b7986325135118"></a><a name="b7986325135118"></a>EXPIRED</strong></li><li><strong id="b974313261515"><a name="b974313261515"></a><a name="b974313261515"></a>DELETED</strong></li><li><strong id="b33731427195115"><a name="b33731427195115"></a><a name="b33731427195115"></a>ACTIVE</strong></li></ul>
    </td>
    </tr>
    <tr id="row925801431119"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p825911451110"><a name="p825911451110"></a><a name="p825911451110"></a>request_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p1425911414113"><a name="p1425911414113"></a><a name="p1425911414113"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p12259181441112"><a name="p12259181441112"></a><a name="p12259181441112"></a>Specifies information about the local VPC. For details, see <a href="#table1125991417114">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row0259161401118"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p725941415110"><a name="p725941415110"></a><a name="p725941415110"></a>accept_vpc_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p14259111441119"><a name="p14259111441119"></a><a name="p14259111441119"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p1225921416112"><a name="p1225921416112"></a><a name="p1225921416112"></a>Specifies information about the peer VPC. For details, see <a href="#table1125991417114">Table 6</a>.</p>
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
    <p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1294974625311"><a name="i1294974625311"></a><a name="i1294974625311"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    <tr id="row15465113115319"><td class="cellrowborder" valign="top" width="32.81%" headers="mcps1.2.4.1.1 "><p id="p74651838533"><a name="p74651838533"></a><a name="p74651838533"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.2.4.1.2 "><p id="p8465203125315"><a name="p8465203125315"></a><a name="p8465203125315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.4.1.3 "><p id="p271618182568"><a name="p271618182568"></a><a name="p271618182568"></a>Specifies the time (UTC) when the VPC peering connection is updated.</p>
    <p id="p187161918125617"><a name="p187161918125617"></a><a name="p187161918125617"></a>Format: <em id="i3939205220536"><a name="i3939205220536"></a><a name="i3939205220536"></a>yyyy-MM-ddTHH:mm:ss</em></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **vpc\_info**  objects

    <a name="table1125991417114"></a>
    <table><thead align="left"><tr id="row1725931413118"><th class="cellrowborder" valign="top" width="32.81%" id="mcps1.2.4.1.1"><p id="p122592014121114"><a name="p122592014121114"></a><a name="p122592014121114"></a><strong id="b4364175675318"><a name="b4364175675318"></a><a name="b4364175675318"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.2.4.1.2"><p id="p11259121417111"><a name="p11259121417111"></a><a name="p11259121417111"></a><strong id="b996455755320"><a name="b996455755320"></a><a name="b996455755320"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.4.1.3"><p id="p17259191412115"><a name="p17259191412115"></a><a name="p17259191412115"></a><strong id="b4834105845313"><a name="b4834105845313"></a><a name="b4834105845313"></a>Description</strong></p>
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

