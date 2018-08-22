# Querying VPC Details<a name="EN-US_TOPIC_0020090618"></a>

## Function<a name="section48604061"></a>

This interface is used to query details about a VPC.

## URI<a name="section34783366"></a>

-   GET /v1/\{tenant\_id\}/vpcs/\{vpc\_id\}
-   Parameter description

    <a name="table26431778"></a><table><thead align="left"><tr id="row38955607"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1287621"><a name="p1287621"></a><a name="p1287621"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p37188451"><a name="p37188451"></a><a name="p37188451"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p59474521"><a name="p59474521"></a><a name="p59474521"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52706896"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p41400175"><a name="p41400175"></a><a name="p41400175"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p65079903"><a name="p65079903"></a><a name="p65079903"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p36980808"><a name="p36980808"></a><a name="p36980808"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row64391817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p48354649"><a name="p48354649"></a><a name="p48354649"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p24412469"><a name="p24412469"></a><a name="p24412469"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p31252998"><a name="p31252998"></a><a name="p31252998"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44614845"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section65989290"></a>

-   Parameter description

    <a name="table574587231556"></a><table><thead align="left"><tr id="row118397001556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p194916751556"><a name="p194916751556"></a><a name="p194916751556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.16%" id="mcps1.1.4.1.2"><p id="p424939721556"><a name="p424939721556"></a><a name="p424939721556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.49999999999999%" id="mcps1.1.4.1.3"><p id="p194597361556"><a name="p194597361556"></a><a name="p194597361556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row327347841556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p342718611556"><a name="p342718611556"></a><a name="p342718611556"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.16%" headers="mcps1.1.4.1.2 "><p id="p429876841556"><a name="p429876841556"></a><a name="p429876841556"></a><em id="i513448371556"><a name="i513448371556"></a><a name="i513448371556"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="57.49999999999999%" headers="mcps1.1.4.1.3 "><p id="p652911041556"><a name="p652911041556"></a><a name="p652911041556"></a>Specifies the VPC objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **vpc**  fields

    <a name="table53205180"></a><table><thead align="left"><tr id="row33959011"><th class="cellrowborder" valign="top" width="21.66%" id="mcps1.1.4.1.1"><p id="p66325402"><a name="p66325402"></a><a name="p66325402"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.32%" id="mcps1.1.4.1.2"><p id="p13682832174258"><a name="p13682832174258"></a><a name="p13682832174258"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.02%" id="mcps1.1.4.1.3"><p id="p27088563"><a name="p27088563"></a><a name="p27088563"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46690023"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p23795519"><a name="p23795519"></a><a name="p23795519"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p34567587174258"><a name="p34567587174258"></a><a name="p34567587174258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p27186813"><a name="p27186813"></a><a name="p27186813"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row43354729"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p22072140"><a name="p22072140"></a><a name="p22072140"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p48511134174258"><a name="p48511134174258"></a><a name="p48511134174258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p61491827"><a name="p61491827"></a><a name="p61491827"></a>Specifies the VPC name.</p>
    </td>
    </tr>
    <tr id="row16555535"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p65929926"><a name="p65929926"></a><a name="p65929926"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p37087786174258"><a name="p37087786174258"></a><a name="p37087786174258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p49620939"><a name="p49620939"></a><a name="p49620939"></a>Specifies the range of available subnets in the VPC.</p>
    </td>
    </tr>
    <tr id="row43935272"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p1987246"><a name="p1987246"></a><a name="p1987246"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p51320686174258"><a name="p51320686174258"></a><a name="p51320686174258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p19204580"><a name="p19204580"></a><a name="p19204580"></a>Specifies the status of the VPC.</p>
    <p id="p37916893"><a name="p37916893"></a><a name="p37916893"></a>The value can be <strong>CREATING</strong>,&nbsp;<strong>OK</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>PENDING_UPDATE</strong>,&nbsp;<strong>PENDING_DELETE</strong>, or&nbsp;<strong>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row11226980135054"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p36970168135054"><a name="p36970168135054"></a><a name="p36970168135054"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p29840430135054"><a name="p29840430135054"></a><a name="p29840430135054"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p26256563192136"><a name="p26256563192136"></a><a name="p26256563192136"></a>Specifies the route information.</p>
    <p id="p42971876202757"><a name="p42971876202757"></a><a name="p42971876202757"></a>For details, see descriptions of <strong>route</strong> fields.</p>
    </td>
    </tr>
    <tr id="row16723471238"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p41373254402"><a name="p41373254402"></a><a name="p41373254402"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.1.4.1.2 "><p id="p18137202516409"><a name="p18137202516409"></a><a name="p18137202516409"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.1.4.1.3 "><p id="p51371325174011"><a name="p51371325174011"></a><a name="p51371325174011"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong>&nbsp;indicates that the function is enabled, and the value&nbsp;<strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
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
        "vpc": {
            "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
            "name": "vpc",
            "cidr": "192.168.0.0/16",
            "status": "OK",
    }
    }
    ```


## Returned Value<a name="section57032702"></a>

-   Normal

    200

-   Abnormal

    <a name="table5642170095054"></a><table><thead align="left"><tr id="row2541843995054"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p4562764695054"><a name="p4562764695054"></a><a name="p4562764695054"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p485186695054"><a name="p485186695054"></a><a name="p485186695054"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5745689995054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2349724895054"><a name="p2349724895054"></a><a name="p2349724895054"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2422895495054"><a name="p2422895495054"></a><a name="p2422895495054"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row1673399795054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1327650895054"><a name="p1327650895054"></a><a name="p1327650895054"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p165538895054"><a name="p165538895054"></a><a name="p165538895054"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1489849895054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6592767895054"><a name="p6592767895054"></a><a name="p6592767895054"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3854166295054"><a name="p3854166295054"></a><a name="p3854166295054"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1133063995054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4536656195054"><a name="p4536656195054"></a><a name="p4536656195054"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5081281195054"><a name="p5081281195054"></a><a name="p5081281195054"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row5466212195054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6555569195054"><a name="p6555569195054"></a><a name="p6555569195054"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p841077895054"><a name="p841077895054"></a><a name="p841077895054"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row858814195054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2455085895054"><a name="p2455085895054"></a><a name="p2455085895054"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4246247195054"><a name="p4246247195054"></a><a name="p4246247195054"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row4661792195054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1795525095054"><a name="p1795525095054"></a><a name="p1795525095054"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4508911195054"><a name="p4508911195054"></a><a name="p4508911195054"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row314881695054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5372758395054"><a name="p5372758395054"></a><a name="p5372758395054"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5696699995054"><a name="p5696699995054"></a><a name="p5696699995054"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row4294094595054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5566453695054"><a name="p5566453695054"></a><a name="p5566453695054"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1253359695054"><a name="p1253359695054"></a><a name="p1253359695054"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row4569350495054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1018634595054"><a name="p1018634595054"></a><a name="p1018634595054"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1978765195054"><a name="p1978765195054"></a><a name="p1978765195054"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row4387113895054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6390128895054"><a name="p6390128895054"></a><a name="p6390128895054"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p862181095054"><a name="p862181095054"></a><a name="p862181095054"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1048742895054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4417534495054"><a name="p4417534495054"></a><a name="p4417534495054"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2143310895054"><a name="p2143310895054"></a><a name="p2143310895054"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row5868025195054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5547991195054"><a name="p5547991195054"></a><a name="p5547991195054"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6468784095054"><a name="p6468784095054"></a><a name="p6468784095054"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row4531965395054"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4701324395054"><a name="p4701324395054"></a><a name="p4701324395054"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4997633895054"><a name="p4997633895054"></a><a name="p4997633895054"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

