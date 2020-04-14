# Deleting a VBS Backup \(Deprecated\)<a name="EN-US_TOPIC_0020237256"></a>

## Function<a name="section11854613"></a>

This interface is used to delete a VBS backup. This API is deprecated. You are advised to use the API described in  [Deleting a VBS Backup \(Native OpenStack API\)](deleting-a-vbs-backup-(native-openstack-api).md)  to delete a backup.

## URI<a name="section39582655"></a>

-   URI format

    POST /v2/\{project\_id\}/cloudbackups/\{backup\_id\}

-   Parameter description

    <a name="table53872188"></a>
    <table><thead align="left"><tr id="row40420929"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p52869820"><a name="p52869820"></a><a name="p52869820"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p54597003"><a name="p54597003"></a><a name="p54597003"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p60281111"><a name="p60281111"></a><a name="p60281111"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50931783"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row30749271"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p7663035"><a name="p7663035"></a><a name="p7663035"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p16726062"><a name="p16726062"></a><a name="p16726062"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p12633819"><a name="p12633819"></a><a name="p12633819"></a>ID of the backup to be deleted</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20699582"></a>

None

## Response<a name="section52078514"></a>

-   Parameter description

    <a name="table268079921728"></a>
    <table><thead align="left"><tr id="row423693971728"><th class="cellrowborder" valign="top" width="14.87%" id="mcps1.1.4.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.189999999999998%" id="mcps1.1.4.1.2"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.94%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row462910891728"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p585907101728"><a name="p585907101728"></a><a name="p585907101728"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p140797381728"><a name="p140797381728"></a><a name="p140797381728"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p667170331728"><a name="p667170331728"></a><a name="p667170331728"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row635823931728"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p499001711728"><a name="p499001711728"></a><a name="p499001711728"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p379878621728"><a name="p379878621728"></a><a name="p379878621728"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p571179821728"><a name="p571179821728"></a><a name="p571179821728"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row442997951728"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p315136771728"><a name="p315136771728"></a><a name="p315136771728"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p659391231728"><a name="p659391231728"></a><a name="p659391231728"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p394687181728"><a name="p394687181728"></a><a name="p394687181728"></a>Error code returned after an error occurs</p>
    <p id="p196741461728"><a name="p196741461728"></a><a name="p196741461728"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
    }
    ```

    or

    ```
    {
    "error": {
    "message": "XXXX",
    "code": "XXX"
    }
    }
    ```


## Status Codes<a name="section66053444"></a>

-   Normal

    200

-   Abnormal

    <a name="table17411442203238"></a>
    <table><thead align="left"><tr id="row20469972203238"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p47455040203238"><a name="p47455040203238"></a><a name="p47455040203238"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p18653028203238"><a name="p18653028203238"></a><a name="p18653028203238"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34500329203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p43063287203238"><a name="p43063287203238"></a><a name="p43063287203238"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p65574197203238"><a name="p65574197203238"></a><a name="p65574197203238"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row53296861203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22078503203238"><a name="p22078503203238"></a><a name="p22078503203238"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p43528309203238"><a name="p43528309203238"></a><a name="p43528309203238"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row56210465203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p56753841203238"><a name="p56753841203238"></a><a name="p56753841203238"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p33658426203238"><a name="p33658426203238"></a><a name="p33658426203238"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row34490379203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p42257275203238"><a name="p42257275203238"></a><a name="p42257275203238"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p287223203238"><a name="p287223203238"></a><a name="p287223203238"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row2585014203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8059568203238"><a name="p8059568203238"></a><a name="p8059568203238"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p48845291203238"><a name="p48845291203238"></a><a name="p48845291203238"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row36954440203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40519687203238"><a name="p40519687203238"></a><a name="p40519687203238"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p60869210203238"><a name="p60869210203238"></a><a name="p60869210203238"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row10951983203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14695420203238"><a name="p14695420203238"></a><a name="p14695420203238"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p49478353203238"><a name="p49478353203238"></a><a name="p49478353203238"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row42651999203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p32259860203238"><a name="p32259860203238"></a><a name="p32259860203238"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62911845203238"><a name="p62911845203238"></a><a name="p62911845203238"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row29335700203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27381532203238"><a name="p27381532203238"></a><a name="p27381532203238"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3311604203238"><a name="p3311604203238"></a><a name="p3311604203238"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row29804437203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p65349225203238"><a name="p65349225203238"></a><a name="p65349225203238"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p58795873203238"><a name="p58795873203238"></a><a name="p58795873203238"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row59400814203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p46736664203238"><a name="p46736664203238"></a><a name="p46736664203238"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p27573467203238"><a name="p27573467203238"></a><a name="p27573467203238"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46834613203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p35507279203238"><a name="p35507279203238"></a><a name="p35507279203238"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p57517333203238"><a name="p57517333203238"></a><a name="p57517333203238"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row47893957203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p54205305203238"><a name="p54205305203238"></a><a name="p54205305203238"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28553614203238"><a name="p28553614203238"></a><a name="p28553614203238"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row55655940203238"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p11837325203238"><a name="p11837325203238"></a><a name="p11837325203238"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19299274203238"><a name="p19299274203238"></a><a name="p19299274203238"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

