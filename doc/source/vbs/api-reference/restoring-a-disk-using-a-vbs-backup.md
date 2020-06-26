# Restoring a Disk Using a VBS Backup<a name="EN-US_TOPIC_0020237257"></a>

## Function<a name="section27869743"></a>

This interface is used to restore a disk using a VBS backup.

## URI<a name="section49501095"></a>

-   URI format

    POST  /v2/\{project\_id\}/cloudbackups/\{backup\_id\}/restore

-   Parameter description

    <a name="table47561922"></a>
    <table><thead align="left"><tr id="row3241099"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p61202487"><a name="p61202487"></a><a name="p61202487"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p58454448"><a name="p58454448"></a><a name="p58454448"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p37189853"><a name="p37189853"></a><a name="p37189853"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59588135"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p61909621"><a name="p61909621"></a><a name="p61909621"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p48623408"><a name="p48623408"></a><a name="p48623408"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row12984378"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a>ID of the backup used to restore a disk</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section42856673"></a>

-   Parameter description

    <a name="table46758891"></a>
    <table><thead align="left"><tr id="row52209455"><th class="cellrowborder" valign="top" width="15.42%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.61%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.25%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1125861217951"><td class="cellrowborder" valign="top" width="15.42%" headers="mcps1.1.5.1.1 "><p id="p3953240217951"><a name="p3953240217951"></a><a name="p3953240217951"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.1.5.1.2 "><p id="p4800796817951"><a name="p4800796817951"></a><a name="p4800796817951"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.3 "><p id="p6344016617951"><a name="p6344016617951"></a><a name="p6344016617951"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.1.5.1.4 "><p id="p3837982117951"><a name="p3837982117951"></a><a name="p3837982117951"></a>Operation of restoring the disk using a backup</p>
    </td>
    </tr>
    <tr id="row803253"><td class="cellrowborder" valign="top" width="15.42%" headers="mcps1.1.5.1.1 "><p id="p65063572"><a name="p65063572"></a><a name="p65063572"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.61%" headers="mcps1.1.5.1.2 "><p id="p35658012"><a name="p35658012"></a><a name="p35658012"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.3 "><p id="p19134484104243"><a name="p19134484104243"></a><a name="p19134484104243"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.1.5.1.4 "><p id="p2617844"><a name="p2617844"></a><a name="p2617844"></a>ID of the disk to be restored</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
    "restore":{
    "volume_id":"c96e4a94-927a-425c-8795-63f9964cfebd"
    }
    }
    ```


## Response<a name="section50165743"></a>

-   Parameter description

    <a name="table1074363117217"></a>
    <table><thead align="left"><tr id="row5713530117217"><th class="cellrowborder" valign="top" width="14.87%" id="mcps1.1.4.1.1"><p id="p1496715471480"><a name="p1496715471480"></a><a name="p1496715471480"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.189999999999998%" id="mcps1.1.4.1.2"><p id="p596716471583"><a name="p596716471583"></a><a name="p596716471583"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.94%" id="mcps1.1.4.1.3"><p id="p16967114718811"><a name="p16967114718811"></a><a name="p16967114718811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4782981617217"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p4900987817217"><a name="p4900987817217"></a><a name="p4900987817217"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p3524563217217"><a name="p3524563217217"></a><a name="p3524563217217"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p3632393217217"><a name="p3632393217217"></a><a name="p3632393217217"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row5847993217217"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p3925401317217"><a name="p3925401317217"></a><a name="p3925401317217"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p4887090517217"><a name="p4887090517217"></a><a name="p4887090517217"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p6622925217217"><a name="p6622925217217"></a><a name="p6622925217217"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row5919236117217"><td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.1.4.1.1 "><p id="p2985196017217"><a name="p2985196017217"></a><a name="p2985196017217"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.1.4.1.2 "><p id="p3504729117217"><a name="p3504729117217"></a><a name="p3504729117217"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.94%" headers="mcps1.1.4.1.3 "><p id="p2025830317217"><a name="p2025830317217"></a><a name="p2025830317217"></a>Error code returned after an error occurs</p>
    <p id="p4810700217217"><a name="p4810700217217"></a><a name="p4810700217217"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
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


## Status Codes<a name="section48838504"></a>

-   Normal

    200

-   Abnormal

    <a name="table11884763203246"></a>
    <table><thead align="left"><tr id="row26015637203246"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p26891838203246"><a name="p26891838203246"></a><a name="p26891838203246"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p30755268203246"><a name="p30755268203246"></a><a name="p30755268203246"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8148750203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p56068996203246"><a name="p56068996203246"></a><a name="p56068996203246"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p45294864203246"><a name="p45294864203246"></a><a name="p45294864203246"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row5000592203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2394837203246"><a name="p2394837203246"></a><a name="p2394837203246"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59764131203246"><a name="p59764131203246"></a><a name="p59764131203246"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1006268203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14398889203246"><a name="p14398889203246"></a><a name="p14398889203246"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p25459379203246"><a name="p25459379203246"></a><a name="p25459379203246"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row27807822203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p37841101203246"><a name="p37841101203246"></a><a name="p37841101203246"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p45230365203246"><a name="p45230365203246"></a><a name="p45230365203246"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row4420107203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22484375203246"><a name="p22484375203246"></a><a name="p22484375203246"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p9295047203246"><a name="p9295047203246"></a><a name="p9295047203246"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row16546560203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p65202978203246"><a name="p65202978203246"></a><a name="p65202978203246"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p46949852203246"><a name="p46949852203246"></a><a name="p46949852203246"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row19895490203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p922004203246"><a name="p922004203246"></a><a name="p922004203246"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p7573523203246"><a name="p7573523203246"></a><a name="p7573523203246"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1052846203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p18171739203246"><a name="p18171739203246"></a><a name="p18171739203246"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62624744203246"><a name="p62624744203246"></a><a name="p62624744203246"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row26751786203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19411051203246"><a name="p19411051203246"></a><a name="p19411051203246"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28791264203246"><a name="p28791264203246"></a><a name="p28791264203246"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row57794785203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50866048203246"><a name="p50866048203246"></a><a name="p50866048203246"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26509256203246"><a name="p26509256203246"></a><a name="p26509256203246"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row37256714203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p65003873203246"><a name="p65003873203246"></a><a name="p65003873203246"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p30822389203246"><a name="p30822389203246"></a><a name="p30822389203246"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row8966049203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55161370203246"><a name="p55161370203246"></a><a name="p55161370203246"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38886020203246"><a name="p38886020203246"></a><a name="p38886020203246"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row14429867203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27968577203246"><a name="p27968577203246"></a><a name="p27968577203246"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50862235203246"><a name="p50862235203246"></a><a name="p50862235203246"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row55106933203246"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p34476593203246"><a name="p34476593203246"></a><a name="p34476593203246"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p41140645203246"><a name="p41140645203246"></a><a name="p41140645203246"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

