# Disassociating a VPC from a Private Zone<a name="EN-US_TOPIC_0057331452"></a>

## Function<a name="section3569153217343"></a>

Disassociate a VPC from a private zone.

When a private zone is associated with only one VPC, you cannot disassociate it.

## URI<a name="section6163262617350"></a>

-   URI format

    POST /v2/zones/\{zone\_id\}/disassociaterouter


-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table14024165"></a><table><thead align="left"><tr id="row26592044"><th class="cellrowborder" valign="top" width="19.971997199719972%" id="mcps1.2.5.1.1"><p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.971997199719972%" id="mcps1.2.5.1.2"><p id="p54465313"><a name="p54465313"></a><a name="p54465313"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.331433143314332%" id="mcps1.2.5.1.3"><p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.72457245724572%" id="mcps1.2.5.1.4"><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41071365"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p38446258"><a name="p38446258"></a><a name="p38446258"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.2 "><p id="p27139175"><a name="p27139175"></a><a name="p27139175"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.331433143314332%" headers="mcps1.2.5.1.3 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.72457245724572%" headers="mcps1.2.5.1.4 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4207148117353"></a>

-   Parameter description

    **Table  2**  Parameter in the request

    <a name="table72706611815"></a><table><thead align="left"><tr id="row255897031815"><th class="cellrowborder" valign="top" width="18.85%" id="mcps1.2.5.1.1"><p id="p595000771815"><a name="p595000771815"></a><a name="p595000771815"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.16%" id="mcps1.2.5.1.2"><p id="p547769391815"><a name="p547769391815"></a><a name="p547769391815"></a><strong id="b593421527191713_1"><a name="b593421527191713_1"></a><a name="b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.219999999999999%" id="mcps1.2.5.1.3"><p id="p77471141815"><a name="p77471141815"></a><a name="p77471141815"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.77%" id="mcps1.2.5.1.4"><p id="p235365301815"><a name="p235365301815"></a><a name="p235365301815"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row274107621815"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.5.1.1 "><p id="p56792261815"><a name="p56792261815"></a><a name="p56792261815"></a>router</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.2.5.1.2 "><p id="p573641711815"><a name="p573641711815"></a><a name="p573641711815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.219999999999999%" headers="mcps1.2.5.1.3 "><p id="p159862761815"><a name="p159862761815"></a><a name="p159862761815"></a>Router</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.77%" headers="mcps1.2.5.1.4 "><p id="p48582827111646"><a name="p48582827111646"></a><a name="p48582827111646"></a>Router information (VPC associated with the zone)</p>
    <p id="p198200141815"><a name="p198200141815"></a><a name="p198200141815"></a>For details, see <a href="#EN-US_TOPIC_0057331452__table441624051815">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **router**  field

    <a name="table441624051815"></a><table><thead align="left"><tr id="row9315751815"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.5.1.1"><p id="p83487181815"><a name="p83487181815"></a><a name="p83487181815"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.24%" id="mcps1.2.5.1.2"><p id="p51575781815"><a name="p51575781815"></a><a name="p51575781815"></a><strong id="b593421527191713_2"><a name="b593421527191713_2"></a><a name="b593421527191713_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.82%" id="mcps1.2.5.1.3"><p id="p151107071815"><a name="p151107071815"></a><a name="p151107071815"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.85%" id="mcps1.2.5.1.4"><p id="p160077601815"><a name="p160077601815"></a><a name="p160077601815"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row215602021815"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.5.1.1 "><p id="p15459281815"><a name="p15459281815"></a><a name="p15459281815"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.2.5.1.2 "><p id="p581113471815"><a name="p581113471815"></a><a name="p581113471815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.82%" headers="mcps1.2.5.1.3 "><p id="p93986421815"><a name="p93986421815"></a><a name="p93986421815"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.85%" headers="mcps1.2.5.1.4 "><p id="p230925261815"><a name="p230925261815"></a><a name="p230925261815"></a>Router ID (VPC ID)</p>
    </td>
    </tr>
    <tr id="row65061421815"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.5.1.1 "><p id="p572354551815"><a name="p572354551815"></a><a name="p572354551815"></a>router_region</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.2.5.1.2 "><p id="p55602731815"><a name="p55602731815"></a><a name="p55602731815"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.82%" headers="mcps1.2.5.1.3 "><p id="p477289551815"><a name="p477289551815"></a><a name="p477289551815"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.85%" headers="mcps1.2.5.1.4 "><p id="p408401661815"><a name="p408401661815"></a><a name="p408401661815"></a>Region of the router (VPC)</p>
    <p id="p50046718172120"><a name="p50046718172120"></a><a name="p50046718172120"></a>If it is left blank, the region of the project in the token takes effect by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "router": {
            "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
            "router_region": "xx"
        }
    }
    ```


## Response<a name="section2142173017358"></a>

-   Parameter description

    **Table  4**  Parameters in the response

    <a name="table3895302218844"></a><table><thead align="left"><tr id="row4896688518844"><th class="cellrowborder" valign="top" width="21.63%" id="mcps1.2.4.1.1"><p id="p689472918844"><a name="p689472918844"></a><a name="p689472918844"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.02%" id="mcps1.2.4.1.2"><p id="p2160217018844"><a name="p2160217018844"></a><a name="p2160217018844"></a><strong id="b84235270619112_3"><a name="b84235270619112_3"></a><a name="b84235270619112_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.35%" id="mcps1.2.4.1.3"><p id="p494531118844"><a name="p494531118844"></a><a name="p494531118844"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6502588818844"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p3260560718844"><a name="p3260560718844"></a><a name="p3260560718844"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.02%" headers="mcps1.2.4.1.2 "><p id="p2380847318844"><a name="p2380847318844"></a><a name="p2380847318844"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.35%" headers="mcps1.2.4.1.3 "><p id="p4943817618844"><a name="p4943817618844"></a><a name="p4943817618844"></a>Router ID (VPC ID)</p>
    </td>
    </tr>
    <tr id="row4229040718844"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p297095218844"><a name="p297095218844"></a><a name="p297095218844"></a>router_region</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.02%" headers="mcps1.2.4.1.2 "><p id="p3932056118844"><a name="p3932056118844"></a><a name="p3932056118844"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.35%" headers="mcps1.2.4.1.3 "><p id="p3084890718844"><a name="p3084890718844"></a><a name="p3084890718844"></a>Region of the router (VPC)</p>
    </td>
    </tr>
    <tr id="row920471418844"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p738436818844"><a name="p738436818844"></a><a name="p738436818844"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.02%" headers="mcps1.2.4.1.2 "><p id="p6126290618844"><a name="p6126290618844"></a><a name="p6126290618844"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.35%" headers="mcps1.2.4.1.3 "><p id="p940787516628"><a name="p940787516628"></a><a name="p940787516628"></a>Task status</p>
    <p id="p6334833618844"><a name="p6334833618844"></a><a name="p6334833618844"></a>The value can be <strong id="b842352706111124"><a name="b842352706111124"></a><a name="b842352706111124"></a>PENDING_CREATE</strong>, <strong id="b842352706111131"><a name="b842352706111131"></a><a name="b842352706111131"></a>PENDING_DELETE</strong>, <strong id="b842352706111136"><a name="b842352706111136"></a><a name="b842352706111136"></a>ACTIVE</strong>, or <strong id="b842352706111142"><a name="b842352706111142"></a><a name="b842352706111142"></a>ERROR</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "status": "PENDING_DELETE",
        "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
        "router_region": "xx"
    }
    
    ```


## **Returned Value**<a name="section1917896317411"></a>

See  [General Request Return Code](general-request-return-code.md).

