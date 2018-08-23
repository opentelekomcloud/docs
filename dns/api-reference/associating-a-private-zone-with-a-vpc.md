# Associating a Private Zone with a VPC<a name="EN-US_TOPIC_0057329431"></a>

## Function<a name="section3569153217343"></a>

Associate a private zone with a VPC.

## URI<a name="section6163262617350"></a>

-   URI format

    POST /v2/zones/\{zone\_id\}/associaterouter


-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table14024165"></a><table><thead align="left"><tr id="row26592044"><th class="cellrowborder" valign="top" width="18.84188418841884%" id="mcps1.2.5.1.1"><p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.03190319031903%" id="mcps1.2.5.1.2"><p id="p54465313"><a name="p54465313"></a><a name="p54465313"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.711471147114713%" id="mcps1.2.5.1.3"><p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.41474147414741%" id="mcps1.2.5.1.4"><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41071365"><td class="cellrowborder" valign="top" width="18.84188418841884%" headers="mcps1.2.5.1.1 "><p id="p38446258"><a name="p38446258"></a><a name="p38446258"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.03190319031903%" headers="mcps1.2.5.1.2 "><p id="p27139175"><a name="p27139175"></a><a name="p27139175"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.711471147114713%" headers="mcps1.2.5.1.3 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.41474147414741%" headers="mcps1.2.5.1.4 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4207148117353"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table3720408817742"></a><table><thead align="left"><tr id="row6225671717742"><th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.2.5.1.1"><p id="p5153686617742"><a name="p5153686617742"></a><a name="p5153686617742"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.35%" id="mcps1.2.5.1.2"><p id="p473035017742"><a name="p473035017742"></a><a name="p473035017742"></a><strong id="b593421527191713_1"><a name="b593421527191713_1"></a><a name="b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.65%" id="mcps1.2.5.1.3"><p id="p386753717742"><a name="p386753717742"></a><a name="p386753717742"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.96%" id="mcps1.2.5.1.4"><p id="p5956810717742"><a name="p5956810717742"></a><a name="p5956810717742"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1329410717742"><td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.5.1.1 "><p id="p2681781817157"><a name="p2681781817157"></a><a name="p2681781817157"></a>router</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.35%" headers="mcps1.2.5.1.2 "><p id="p6603174617742"><a name="p6603174617742"></a><a name="p6603174617742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.65%" headers="mcps1.2.5.1.3 "><p id="p9188475171518"><a name="p9188475171518"></a><a name="p9188475171518"></a>Router</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.5.1.4 "><p id="p10335706111018"><a name="p10335706111018"></a><a name="p10335706111018"></a>Router information (VPC associated with the zone)</p>
    <p id="p36712148171536"><a name="p36712148171536"></a><a name="p36712148171536"></a>For details, see <a href="#EN-US_TOPIC_0057329431__table4448008117179">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **router**  field

    <a name="table4448008117179"></a><table><thead align="left"><tr id="row6132935617179"><th class="cellrowborder" valign="top" width="17.34%" id="mcps1.2.5.1.1"><p id="p36588677171719"><a name="p36588677171719"></a><a name="p36588677171719"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.49%" id="mcps1.2.5.1.2"><p id="p10892865171719"><a name="p10892865171719"></a><a name="p10892865171719"></a><strong id="b593421527191713_2"><a name="b593421527191713_2"></a><a name="b593421527191713_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.58%" id="mcps1.2.5.1.3"><p id="p9906869171719"><a name="p9906869171719"></a><a name="p9906869171719"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.59%" id="mcps1.2.5.1.4"><p id="p64258954171719"><a name="p64258954171719"></a><a name="p64258954171719"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row266872817179"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.5.1.1 "><p id="p25118582171719"><a name="p25118582171719"></a><a name="p25118582171719"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p21339228171719"><a name="p21339228171719"></a><a name="p21339228171719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.5.1.3 "><p id="p50755907171719"><a name="p50755907171719"></a><a name="p50755907171719"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.59%" headers="mcps1.2.5.1.4 "><p id="p17587794171719"><a name="p17587794171719"></a><a name="p17587794171719"></a>Router ID (VPC ID)</p>
    </td>
    </tr>
    <tr id="row6657832817179"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.5.1.1 "><p id="p3709384171719"><a name="p3709384171719"></a><a name="p3709384171719"></a>router_region</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.2 "><p id="p32024676171719"><a name="p32024676171719"></a><a name="p32024676171719"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.5.1.3 "><p id="p43861924171719"><a name="p43861924171719"></a><a name="p43861924171719"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.59%" headers="mcps1.2.5.1.4 "><p id="p63154928171719"><a name="p63154928171719"></a><a name="p63154928171719"></a>Region of the router (VPC)</p>
    <p id="p31477322172059"><a name="p31477322172059"></a><a name="p31477322172059"></a>If it is left blank, the region of the project in the token takes effect by default.</p>
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

    <a name="table4512106017551"></a><table><thead align="left"><tr id="row2225931917551"><th class="cellrowborder" valign="top" width="21.63%" id="mcps1.2.4.1.1"><p id="p5817443517551"><a name="p5817443517551"></a><a name="p5817443517551"></a><strong id="b162774213314533_3"><a name="b162774213314533_3"></a><a name="b162774213314533_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.38%" id="mcps1.2.4.1.2"><p id="p3436442517551"><a name="p3436442517551"></a><a name="p3436442517551"></a><strong id="b84235270619112_3"><a name="b84235270619112_3"></a><a name="b84235270619112_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.99%" id="mcps1.2.4.1.3"><p id="p3205505917551"><a name="p3205505917551"></a><a name="p3205505917551"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4632297717551"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p6117366017551"><a name="p6117366017551"></a><a name="p6117366017551"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p4937778317551"><a name="p4937778317551"></a><a name="p4937778317551"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.4.1.3 "><p id="p4017744717551"><a name="p4017744717551"></a><a name="p4017744717551"></a>Router ID (VPC ID)</p>
    </td>
    </tr>
    <tr id="row2605270417551"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p2989427417551"><a name="p2989427417551"></a><a name="p2989427417551"></a>router_region</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p4423327117551"><a name="p4423327117551"></a><a name="p4423327117551"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.4.1.3 "><p id="p2612521117551"><a name="p2612521117551"></a><a name="p2612521117551"></a>Region of the router (VPC)</p>
    </td>
    </tr>
    <tr id="row16652885175519"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p38120631175524"><a name="p38120631175524"></a><a name="p38120631175524"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.38%" headers="mcps1.2.4.1.2 "><p id="p57184665175519"><a name="p57184665175519"></a><a name="p57184665175519"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.4.1.3 "><p id="p1635999216648"><a name="p1635999216648"></a><a name="p1635999216648"></a>Task status</p>
    <p id="p24990280175620"><a name="p24990280175620"></a><a name="p24990280175620"></a>The value can be <strong id="b842352706111124"><a name="b842352706111124"></a><a name="b842352706111124"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b842352706111131"><a name="b842352706111131"></a><a name="b842352706111131"></a>PENDING_DELETE</strong>,&nbsp;<strong id="b842352706111136"><a name="b842352706111136"></a><a name="b842352706111136"></a>ACTIVE</strong>, or&nbsp;<strong id="b842352706111142"><a name="b842352706111142"></a><a name="b842352706111142"></a>ERROR</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "status": "PENDING_CREATE",
        "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
        "router_region": "xx"
    }
    
    ```


## **Returned Value**<a name="section1917896317411"></a>

See  [General Request Return Code](general-request-return-code.md).

