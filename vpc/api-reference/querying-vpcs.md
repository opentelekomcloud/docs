# Querying VPCs<a name="EN-US_TOPIC_0020090625"></a>

## Function<a name="section14477792"></a>

This interface is used to query VPCs using search criteria and to display the VPCs in a list.

## URI<a name="section63191266"></a>

-   GET /v1/\{tenant\_id\}/vpcs
-   Example:

    ```
    /v1/{tenant_id}/vpcs?limit=10&marker=13551d6b-755d-4757-b956-536f674975c0
    ```

-   Parameter description

    <a name="table39337169"></a><table><thead align="left"><tr id="row33970761"><th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.1.5.1.1"><p id="p168245"><a name="p168245"></a><a name="p168245"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.1.5.1.2"><p id="p13627845"><a name="p13627845"></a><a name="p13627845"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.1.5.1.3"><p id="p17267522174356"><a name="p17267522174356"></a><a name="p17267522174356"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.949999999999996%" id="mcps1.1.5.1.4"><p id="p30113633"><a name="p30113633"></a><a name="p30113633"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23285234"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.1 "><p id="p7055840"><a name="p7055840"></a><a name="p7055840"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.1.5.1.2 "><p id="p34652178"><a name="p34652178"></a><a name="p34652178"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.1.5.1.3 "><p id="p56492018174356"><a name="p56492018174356"></a><a name="p56492018174356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.1.5.1.4 "><p id="p55363057"><a name="p55363057"></a><a name="p55363057"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row28505468"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.1 "><p id="p27241609"><a name="p27241609"></a><a name="p27241609"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.1.5.1.2 "><p id="p59086710"><a name="p59086710"></a><a name="p59086710"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.1.5.1.3 "><p id="p12450755174356"><a name="p12450755174356"></a><a name="p12450755174356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.1.5.1.4 "><p id="p24297067174412"><a name="p24297067174412"></a><a name="p24297067174412"></a>Specifies the resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
    </td>
    </tr>
    <tr id="row21315230"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.1 "><p id="p48812047"><a name="p48812047"></a><a name="p48812047"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.1.5.1.2 "><p id="p61461766"><a name="p61461766"></a><a name="p61461766"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.1.5.1.3 "><p id="p1878236174356"><a name="p1878236174356"></a><a name="p1878236174356"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.1.5.1.4 "><p id="p12347112"><a name="p12347112"></a><a name="p12347112"></a>Specifies the number of records returned on each page.</p>
    <p id="p60592031"><a name="p60592031"></a><a name="p60592031"></a>The value ranges from 0 to intmax.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31850483"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section18218892"></a>

-   Parameter description

    <a name="table6229176715519"></a><table><thead align="left"><tr id="row6055323715519"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p586512615519"><a name="p586512615519"></a><a name="p586512615519"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.97%" id="mcps1.1.4.1.2"><p id="p2771539415519"><a name="p2771539415519"></a><a name="p2771539415519"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.690000000000005%" id="mcps1.1.4.1.3"><p id="p3035446115519"><a name="p3035446115519"></a><a name="p3035446115519"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4279228915519"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p4362334815519"><a name="p4362334815519"></a><a name="p4362334815519"></a>vpcs</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.97%" headers="mcps1.1.4.1.2 "><p id="p6059639815519"><a name="p6059639815519"></a><a name="p6059639815519"></a><em id="i1588689015618"><a name="i1588689015618"></a><a name="i1588689015618"></a>List data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.1.4.1.3 "><p id="p1714182515519"><a name="p1714182515519"></a><a name="p1714182515519"></a>Specifies the VPC list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **vpcs**  fields

    <a name="table65129753"></a><table><thead align="left"><tr id="row16647026"><th class="cellrowborder" valign="top" width="15.78%" id="mcps1.1.4.1.1"><p id="p6231886"><a name="p6231886"></a><a name="p6231886"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.2"><p id="p25347041174441"><a name="p25347041174441"></a><a name="p25347041174441"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.22%" id="mcps1.1.4.1.3"><p id="p18111828"><a name="p18111828"></a><a name="p18111828"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57771982"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p49018956"><a name="p49018956"></a><a name="p49018956"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p39844479174441"><a name="p39844479174441"></a><a name="p39844479174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p27697526"><a name="p27697526"></a><a name="p27697526"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row47951145"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p58837506"><a name="p58837506"></a><a name="p58837506"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p6177377174441"><a name="p6177377174441"></a><a name="p6177377174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p28235388174625"><a name="p28235388174625"></a><a name="p28235388174625"></a>Specifies the VPC name.</p>
    </td>
    </tr>
    <tr id="row2894687"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p33143133"><a name="p33143133"></a><a name="p33143133"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p30605552174441"><a name="p30605552174441"></a><a name="p30605552174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p48285594174625"><a name="p48285594174625"></a><a name="p48285594174625"></a>Specifies the range of available subnets in the VPC.</p>
    </td>
    </tr>
    <tr id="row40205569"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p35425694"><a name="p35425694"></a><a name="p35425694"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p63130643174441"><a name="p63130643174441"></a><a name="p63130643174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p35153815174625"><a name="p35153815174625"></a><a name="p35153815174625"></a>Specifies the status of the VPC.</p>
    <p id="p58654237174625"><a name="p58654237174625"></a><a name="p58654237174625"></a>The value can be <strong>CREATING</strong>,&nbsp;<strong>OK</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>PENDING_UPDATE</strong>,&nbsp;<strong>PENDING_DELETE</strong>, or&nbsp;<strong>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row56256918135346"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p60516514135346"><a name="p60516514135346"></a><a name="p60516514135346"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p32811915135346"><a name="p32811915135346"></a><a name="p32811915135346"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p26256563192136"><a name="p26256563192136"></a><a name="p26256563192136"></a>Specifies the route information.</p>
    <p id="p42971876202757"><a name="p42971876202757"></a><a name="p42971876202757"></a>For details, see descriptions of <strong>route</strong> fields.</p>
    </td>
    </tr>
    <tr id="row1426011201318"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.4.1.1 "><p id="p41373254402"><a name="p41373254402"></a><a name="p41373254402"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="p18137202516409"><a name="p18137202516409"></a><a name="p18137202516409"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.4.1.3 "><p id="p51371325174011"><a name="p51371325174011"></a><a name="p51371325174011"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong>&nbsp;indicates that the function is enabled, and the value&nbsp;<strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **route**  fields

    <a name="table3576833291556"></a><table><thead align="left"><tr id="row921218691556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p798956991556"><a name="p798956991556"></a><a name="p798956991556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.38%" id="mcps1.1.4.1.2"><p id="p754435891556"><a name="p754435891556"></a><a name="p754435891556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.28%" id="mcps1.1.4.1.3"><p id="p711326791556"><a name="p711326791556"></a><a name="p711326791556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3930377391556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p2948903591556"><a name="p2948903591556"></a><a name="p2948903591556"></a>destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p270722191556"><a name="p270722191556"></a><a name="p270722191556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p2740730591556"><a name="p2740730591556"></a><a name="p2740730591556"></a>Specifies the destination network segment of a route.</p>
    <p id="p2436469411021"><a name="p2436469411021"></a><a name="p2436469411021"></a>The value must be in the CIDR format. Currently, only the value <strong id="b842352706144646"><a name="b842352706144646"></a><a name="b842352706144646"></a>0.0.0.0/0</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p5632574211054"><a name="p5632574211054"></a><a name="p5632574211054"></a>Specifies the next hop of a route.</p>
    <p id="p2794258711440"><a name="p2794258711440"></a><a name="p2794258711440"></a>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "vpcs": [
            {
                "id": "13551d6b-755d-4757-b956-536f674975c0",
                "name": "default",
                "cidr": "172.16.0.0/16",
                "status": "OK",
                "routes": null,
                "enable_shared_snat": false
            },
            {
                "id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "name": "222",
                "cidr": "192.168.0.0/16",
                "status": "OK",
                "routes": null,
                "enable_shared_snat": false
            },
            {
                "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
                "name": "vpc",
                "cidr": "192.168.0.0/16",
                "status": "OK",
                "routes": null,
                "enable_shared_snat": false
            }
        ]
    }
    ```


## Returned Value<a name="section29752302"></a>

-   Normal

    200

-   Abnormal

    <a name="table436768729512"></a><table><thead align="left"><tr id="row149039789512"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p663715429512"><a name="p663715429512"></a><a name="p663715429512"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p73858479512"><a name="p73858479512"></a><a name="p73858479512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row613827739512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p59487279512"><a name="p59487279512"></a><a name="p59487279512"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p120849029512"><a name="p120849029512"></a><a name="p120849029512"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row416552579512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p186326949512"><a name="p186326949512"></a><a name="p186326949512"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p328532359512"><a name="p328532359512"></a><a name="p328532359512"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row272436619512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p592529269512"><a name="p592529269512"></a><a name="p592529269512"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p347576679512"><a name="p347576679512"></a><a name="p347576679512"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row443835489512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p382976759512"><a name="p382976759512"></a><a name="p382976759512"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p151040039512"><a name="p151040039512"></a><a name="p151040039512"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row17183019512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p49647089512"><a name="p49647089512"></a><a name="p49647089512"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p665970969512"><a name="p665970969512"></a><a name="p665970969512"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row625029569512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p295746779512"><a name="p295746779512"></a><a name="p295746779512"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p467386719512"><a name="p467386719512"></a><a name="p467386719512"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row179948629512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p482977169512"><a name="p482977169512"></a><a name="p482977169512"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p198008949512"><a name="p198008949512"></a><a name="p198008949512"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row439903209512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64461729512"><a name="p64461729512"></a><a name="p64461729512"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p523779209512"><a name="p523779209512"></a><a name="p523779209512"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row16392399512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p656695559512"><a name="p656695559512"></a><a name="p656695559512"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p176337729512"><a name="p176337729512"></a><a name="p176337729512"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row244862259512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p372271759512"><a name="p372271759512"></a><a name="p372271759512"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p626111989512"><a name="p626111989512"></a><a name="p626111989512"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row266298739512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p95361089512"><a name="p95361089512"></a><a name="p95361089512"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p342272599512"><a name="p342272599512"></a><a name="p342272599512"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row396098789512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p542835199512"><a name="p542835199512"></a><a name="p542835199512"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p348888809512"><a name="p348888809512"></a><a name="p348888809512"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row455644679512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p668432369512"><a name="p668432369512"></a><a name="p668432369512"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p455930749512"><a name="p455930749512"></a><a name="p455930749512"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row76844879512"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p184637239512"><a name="p184637239512"></a><a name="p184637239512"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p191665589512"><a name="p191665589512"></a><a name="p191665589512"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

