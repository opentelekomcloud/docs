# Counting Backup Shares<a name="EN-US_TOPIC_0078214154"></a>

## Function<a name="section1293613541013"></a>

This interface is used to count backup shares with conditions.

## URI<a name="section893718351108"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-backup-sharing/count

-   Parameter description

    <a name="table6939133551012"></a>
    <table><thead align="left"><tr id="row14221636111013"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1625418168917"><a name="p1625418168917"></a><a name="p1625418168917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p9254916897"><a name="p9254916897"></a><a name="p9254916897"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1254191615916"><a name="p1254191615916"></a><a name="p1254191615916"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1422193614101"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1025419164915"><a name="p1025419164915"></a><a name="p1025419164915"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3254171615911"><a name="p3254171615911"></a><a name="p3254171615911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  parameter description

    <a name="table49421357102"></a>
    <table><thead align="left"><tr id="row922213363102"><th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11222436101017"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p722212367106"><a name="p722212367106"></a><a name="p722212367106"></a>share_to_me</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p18222736171019"><a name="p18222736171019"></a><a name="p18222736171019"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p2222103612104"><a name="p2222103612104"></a><a name="p2222103612104"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p48092119105"><a name="p48092119105"></a><a name="p48092119105"></a>If this parameter is set to <strong id="b84235270673034"><a name="b84235270673034"></a><a name="b84235270673034"></a>true</strong>, this interface will list the backups shared with the current project. Otherwise, this interface will list the backups shared by the current project.</p>
    </td>
    </tr>
    <tr id="row1322243614107"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p15222736191018"><a name="p15222736191018"></a><a name="p15222736191018"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p1361614191303"><a name="p1361614191303"></a><a name="p1361614191303"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p122229361101"><a name="p122229361101"></a><a name="p122229361101"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p1580221161020"><a name="p1580221161020"></a><a name="p1580221161020"></a>Volume ID</p>
    </td>
    </tr>
    <tr id="row1222293621017"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p3222936181011"><a name="p3222936181011"></a><a name="p3222936181011"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p2619919208"><a name="p2619919208"></a><a name="p2619919208"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p62224361106"><a name="p62224361106"></a><a name="p62224361106"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p1381122131012"><a name="p1381122131012"></a><a name="p1381122131012"></a>Backup name. Fuzzy match is supported.</p>
    </td>
    </tr>
    <tr id="row102221736161019"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p18222183621012"><a name="p18222183621012"></a><a name="p18222183621012"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p1462217198015"><a name="p1462217198015"></a><a name="p1462217198015"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p52221136171015"><a name="p52221136171015"></a><a name="p52221136171015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p1581102131018"><a name="p1581102131018"></a><a name="p1581102131018"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row1522316365108"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p1223236151015"><a name="p1223236151015"></a><a name="p1223236151015"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p06260192007"><a name="p06260192007"></a><a name="p06260192007"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p192237366102"><a name="p192237366102"></a><a name="p192237366102"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p281182111013"><a name="p281182111013"></a><a name="p281182111013"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row5223236131014"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p9223133619106"><a name="p9223133619106"></a><a name="p9223133619106"></a>from_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p1629319809"><a name="p1629319809"></a><a name="p1629319809"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p18223736141015"><a name="p18223736141015"></a><a name="p18223736141015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p58342117100"><a name="p58342117100"></a><a name="p58342117100"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row15223143691017"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p1522320369103"><a name="p1522320369103"></a><a name="p1522320369103"></a>to_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p76347198011"><a name="p76347198011"></a><a name="p76347198011"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p922393616107"><a name="p922393616107"></a><a name="p922393616107"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p383102141010"><a name="p383102141010"></a><a name="p383102141010"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row6223133661012"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.1 "><p id="p18223123631014"><a name="p18223123631014"></a><a name="p18223123631014"></a>avalilability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.2 "><p id="p863710190019"><a name="p863710190019"></a><a name="p863710190019"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p112231436131013"><a name="p112231436131013"></a><a name="p112231436131013"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p138362110103"><a name="p138362110103"></a><a name="p138362110103"></a>AZ name</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section598663551014"></a>

None

## Response<a name="section1898763541014"></a>

-   Parameter description

    <a name="table998883518102"></a>
    <table><thead align="left"><tr id="row322418363104"><th class="cellrowborder" valign="top" width="21.52%" id="mcps1.1.4.1.1"><p id="p994172819233"><a name="p994172819233"></a><a name="p994172819233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.26%" id="mcps1.1.4.1.2"><p id="p89413284232"><a name="p89413284232"></a><a name="p89413284232"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.220000000000006%" id="mcps1.1.4.1.3"><p id="p811072813234"><a name="p811072813234"></a><a name="p811072813234"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1122453618109"><td class="cellrowborder" valign="top" width="21.52%" headers="mcps1.1.4.1.1 "><p id="p82242362102"><a name="p82242362102"></a><a name="p82242362102"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.26%" headers="mcps1.1.4.1.2 "><p id="p8224143611105"><a name="p8224143611105"></a><a name="p8224143611105"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.220000000000006%" headers="mcps1.1.4.1.3 "><p id="p182241369102"><a name="p182241369102"></a><a name="p182241369102"></a>Total count</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
         "count": 2 
    }
    ```


## Status Codes<a name="section1399611359100"></a>

-   Normal

    200

-   Abnormal

    <a name="table59178184203255"></a>
    <table><thead align="left"><tr id="row54047877203255"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15801936203255"><a name="p15801936203255"></a><a name="p15801936203255"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p4888452203255"><a name="p4888452203255"></a><a name="p4888452203255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60420295203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p62205764203255"><a name="p62205764203255"></a><a name="p62205764203255"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5502113203255"><a name="p5502113203255"></a><a name="p5502113203255"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row49519019203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p51617596203255"><a name="p51617596203255"></a><a name="p51617596203255"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20275713203255"><a name="p20275713203255"></a><a name="p20275713203255"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48263690203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17044857203255"><a name="p17044857203255"></a><a name="p17044857203255"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38456209203255"><a name="p38456209203255"></a><a name="p38456209203255"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row10561563203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50180290203255"><a name="p50180290203255"></a><a name="p50180290203255"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38071718203255"><a name="p38071718203255"></a><a name="p38071718203255"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7101146203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38321955203255"><a name="p38321955203255"></a><a name="p38321955203255"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p17070685203255"><a name="p17070685203255"></a><a name="p17070685203255"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row19418444203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p29390130203255"><a name="p29390130203255"></a><a name="p29390130203255"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31790300203255"><a name="p31790300203255"></a><a name="p31790300203255"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row17677246203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22570826203255"><a name="p22570826203255"></a><a name="p22570826203255"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16297614203255"><a name="p16297614203255"></a><a name="p16297614203255"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row12460805203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2692305203255"><a name="p2692305203255"></a><a name="p2692305203255"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16750186203255"><a name="p16750186203255"></a><a name="p16750186203255"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row16533951203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64181621203255"><a name="p64181621203255"></a><a name="p64181621203255"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31328812203255"><a name="p31328812203255"></a><a name="p31328812203255"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row13523855203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p21690474203255"><a name="p21690474203255"></a><a name="p21690474203255"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12097945203255"><a name="p12097945203255"></a><a name="p12097945203255"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row41772644203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28140973203255"><a name="p28140973203255"></a><a name="p28140973203255"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p64826302203255"><a name="p64826302203255"></a><a name="p64826302203255"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46565809203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13734210203255"><a name="p13734210203255"></a><a name="p13734210203255"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38729264203255"><a name="p38729264203255"></a><a name="p38729264203255"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row13019061203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p47911033203255"><a name="p47911033203255"></a><a name="p47911033203255"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p55588428203255"><a name="p55588428203255"></a><a name="p55588428203255"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row30533812203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57319716203255"><a name="p57319716203255"></a><a name="p57319716203255"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12385400203255"><a name="p12385400203255"></a><a name="p12385400203255"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

