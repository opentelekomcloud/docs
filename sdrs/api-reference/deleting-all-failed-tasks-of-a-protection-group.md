# Deleting All Failed Tasks of a Protection Group<a name="sdrs_05_0904"></a>

## Function<a name="section10712172153513"></a>

This API is used to delete failed tasks in a protection group, such as failed protected instance creation or deletion tasks, and failed replication pair creation and deletion tasks.

## Constraints and Limitations<a name="section7717172173519"></a>

-   None

## URI<a name="section157201821113516"></a>

-   URI format

    DELETE /v1/\{project\_id\}/task-center/\{server\_group\_id\}/failure-jobs/batch

-   Parameter description

    <a name="table77247213354"></a>
    <table><thead align="left"><tr id="row8810132213510"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.1"><p id="p148101922163517"><a name="p148101922163517"></a><a name="p148101922163517"></a><strong id="b1268225553815"><a name="b1268225553815"></a><a name="b1268225553815"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414138%" id="mcps1.1.5.1.2"><p id="p481032223510"><a name="p481032223510"></a><a name="p481032223510"></a><strong id="b15361508397"><a name="b15361508397"></a><a name="b15361508397"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.23232323232323%" id="mcps1.1.5.1.3"><p id="p148101322203518"><a name="p148101322203518"></a><a name="p148101322203518"></a><strong id="b148434223912"><a name="b148434223912"></a><a name="b148434223912"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.1.5.1.4"><p id="p178101222183514"><a name="p178101222183514"></a><a name="p178101222183514"></a><strong id="b1652118815397"><a name="b1652118815397"></a><a name="b1652118815397"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1981012224351"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.1 "><p id="p1810152215359"><a name="p1810152215359"></a><a name="p1810152215359"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414138%" headers="mcps1.1.5.1.2 "><p id="p14810152213353"><a name="p14810152213353"></a><a name="p14810152213353"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.3 "><p id="p7810192217351"><a name="p7810192217351"></a><a name="p7810192217351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.1.5.1.4 "><p id="p28101227354"><a name="p28101227354"></a><a name="p28101227354"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row14810102243515"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.1 "><p id="p15810922193516"><a name="p15810922193516"></a><a name="p15810922193516"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414138%" headers="mcps1.1.5.1.2 "><p id="p881015229351"><a name="p881015229351"></a><a name="p881015229351"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.3 "><p id="p2810322173515"><a name="p2810322173515"></a><a name="p2810322173515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.1.5.1.4 "><p id="p1225754919450"><a name="p1225754919450"></a><a name="p1225754919450"></a>Specifies the ID of a protection group.</p>
    <p id="p3282955163715"><a name="p3282955163715"></a><a name="p3282955163715"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1973942115356"></a>

-   Request parameters

    None

-   Example request

    DELETE https://\{Endpoint\}/v1/\{project\_id\}/task-center/decf224d-87fe-403a-8721-037a1a45c287/failure-jobs/batch


## Response<a name="section17391021133518"></a>

None

## **Returned Value**<a name="section0752821153510"></a>

-   Normal

    <a name="table875592143517"></a>
    <table><thead align="left"><tr id="row19811422123519"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p19811202216355"><a name="p19811202216355"></a><a name="p19811202216355"></a><strong id="b1083343663919"><a name="b1083343663919"></a><a name="b1083343663919"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p5811222153519"><a name="p5811222153519"></a><a name="p5811222153519"></a><strong id="b1365816377395"><a name="b1365816377395"></a><a name="b1365816377395"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8811622173516"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8818112215352"><a name="p8818112215352"></a><a name="p8818112215352"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2081882211354"><a name="p2081882211354"></a><a name="p2081882211354"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


