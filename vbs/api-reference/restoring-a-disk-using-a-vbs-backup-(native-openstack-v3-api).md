# Restoring a Disk Using a VBS Backup \(Native OpenStack V3 API\)<a name="EN-US_TOPIC_0143705539"></a>

## Function<a name="section11854613"></a>

This interface is used to restore a disk using a VBS backup.

## URI<a name="section39582655"></a>

-   URI format

    POST /v3/\{project\_id\}/native/backups/\{backup\_id\}/restore

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
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p12633819"><a name="p12633819"></a><a name="p12633819"></a>ID of the backup used to restore a disk</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20699582"></a>

-   Parameter description

    <a name="table1687812615267"></a>
    <table><thead align="left"><tr id="row2087872611268"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570766171331"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.1 "><p id="p46232095171331"><a name="p46232095171331"></a><a name="p46232095171331"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.1.5.1.2 "><p id="p53812216171331"><a name="p53812216171331"></a><a name="p53812216171331"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.5.1.3 "><p id="p63822274171331"><a name="p63822274171331"></a><a name="p63822274171331"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.5.1.4 "><p id="p2221733171331"><a name="p2221733171331"></a><a name="p2221733171331"></a>Information about the disk to be restored</p>
    </td>
    </tr>
    <tr id="row1087972612265"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.1 "><p id="p587932612615"><a name="p587932612615"></a><a name="p587932612615"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.1.5.1.2 "><p id="p28792262264"><a name="p28792262264"></a><a name="p28792262264"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.5.1.3 "><p id="p17879326202615"><a name="p17879326202615"></a><a name="p17879326202615"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.5.1.4 "><p id="p18791262269"><a name="p18791262269"></a><a name="p18791262269"></a>ID of the disk to be restored</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "restore": {
            "volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024"
        }
    }
    ```


## Response<a name="section52078514"></a>

-   Parameter description

    <a name="table46024180171524"></a>
    <table><thead align="left"><tr id="row56596790171524"><th class="cellrowborder" valign="top" width="23.53%" id="mcps1.1.4.1.1"><p id="p16959711142017"><a name="p16959711142017"></a><a name="p16959711142017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p12959111102013"><a name="p12959111102013"></a><a name="p12959111102013"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.120000000000005%" id="mcps1.1.4.1.3"><p id="p5959101112208"><a name="p5959101112208"></a><a name="p5959101112208"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25919714171524"><td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.1 "><p id="p19122053171524"><a name="p19122053171524"></a><a name="p19122053171524"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p1383663416487"><a name="p1383663416487"></a><a name="p1383663416487"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.1.4.1.3 "><p id="p15309284171524"><a name="p15309284171524"></a><a name="p15309284171524"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row3565834171524"><td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.1 "><p id="p20397103171524"><a name="p20397103171524"></a><a name="p20397103171524"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p0602173694819"><a name="p0602173694819"></a><a name="p0602173694819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.1.4.1.3 "><p id="p30566249171524"><a name="p30566249171524"></a><a name="p30566249171524"></a>Volume ID</p>
    </td>
    </tr>
    <tr id="row6660791171524"><td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.1 "><p id="p2653175171524"><a name="p2653175171524"></a><a name="p2653175171524"></a>volume_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p13580632171524"><a name="p13580632171524"></a><a name="p13580632171524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.120000000000005%" headers="mcps1.1.4.1.3 "><p id="p49067419171524"><a name="p49067419171524"></a><a name="p49067419171524"></a>Volume name</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "restore": {
            "backup_id": "1d1139d8-8989-49d3-8aa1-83eb691e6db2", 
            "volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024"
            "volume_name": "test_volume"
        }
    }
    ```


## Status Codes<a name="section66053444"></a>

-   Normal

    202

-   Abnormal

    <a name="table17411442203238"></a>
    <table><thead align="left"><tr id="row20469972203238"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p47455040203238"><a name="p47455040203238"></a><a name="p47455040203238"></a>Status Codes</p>
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
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p287223203238"><a name="p287223203238"></a><a name="p287223203238"></a>The server could not find the requested page or resources.</p>
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

