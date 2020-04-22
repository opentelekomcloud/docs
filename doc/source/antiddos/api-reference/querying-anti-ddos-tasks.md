# Querying Anti-DDoS Tasks<a name="antiddos_02_0022"></a>

## Function<a name="section32049974"></a>

This API enables you to query the execution status of a specified Anti-DDoS configuration task.

## URI<a name="section20014316"></a>

-   URI format

    GET /v1/\{project\_id\}/query\_task\_status

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can use  **?**  and  **&**  behind the URI to add query conditions, as shown in the request example.  


-   Parameter description

    <a name="table61165617"></a>
    <table><thead align="left"><tr id="row11133117"><th class="cellrowborder" valign="top" width="19.11191119111911%" id="mcps1.1.5.1.1"><p id="p29367308"><a name="p29367308"></a><a name="p29367308"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.06200620062006%" id="mcps1.1.5.1.2"><p id="p29941743"><a name="p29941743"></a><a name="p29941743"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.37123712371237%" id="mcps1.1.5.1.3"><p id="p9362127"><a name="p9362127"></a><a name="p9362127"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.45484548454845%" id="mcps1.1.5.1.4"><p id="p20134803"><a name="p20134803"></a><a name="p20134803"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60087991151245"><td class="cellrowborder" valign="top" width="19.11191119111911%" headers="mcps1.1.5.1.1 "><p id="p59638706151259"><a name="p59638706151259"></a><a name="p59638706151259"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.06200620062006%" headers="mcps1.1.5.1.2 "><p id="p66005896151259"><a name="p66005896151259"></a><a name="p66005896151259"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.37123712371237%" headers="mcps1.1.5.1.3 "><p id="p44877366151259"><a name="p44877366151259"></a><a name="p44877366151259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.45484548454845%" headers="mcps1.1.5.1.4 "><p id="p11188069151259"><a name="p11188069151259"></a><a name="p11188069151259"></a>A user's ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45911124"></a>

-   Parameter description

    <a name="table688625362710"></a>
    <table><thead align="left"><tr id="row1088885302714"><th class="cellrowborder" valign="top" width="20.05%" id="mcps1.1.5.1.1"><p id="p1788925311271"><a name="p1788925311271"></a><a name="p1788925311271"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.12%" id="mcps1.1.5.1.2"><p id="p1688995317277"><a name="p1688995317277"></a><a name="p1688995317277"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.379999999999999%" id="mcps1.1.5.1.3"><p id="p889045314271"><a name="p889045314271"></a><a name="p889045314271"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45%" id="mcps1.1.5.1.4"><p id="p8891135312272"><a name="p8891135312272"></a><a name="p8891135312272"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1089585352717"><td class="cellrowborder" valign="top" width="20.05%" headers="mcps1.1.5.1.1 "><p id="p17896953172711"><a name="p17896953172711"></a><a name="p17896953172711"></a>task_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.1.5.1.2 "><p id="p589615332710"><a name="p589615332710"></a><a name="p589615332710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.379999999999999%" headers="mcps1.1.5.1.3 "><p id="p1689795313275"><a name="p1689795313275"></a><a name="p1689795313275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45%" headers="mcps1.1.5.1.4 "><p id="p17898105342710"><a name="p17898105342710"></a><a name="p17898105342710"></a>Task ID (nonnegative integer) character string</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/query_task_status?task_id=4a4fefe7-34a1-40e2-a87c-16932af3ac4a
    ```


## Response<a name="section10546933"></a>

-   Element description

    <a name="table64725245"></a>
    <table><thead align="left"><tr id="row61244824"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.1.4.1.1"><p id="p61883722"><a name="p61883722"></a><a name="p61883722"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.2"><p id="p46525609"><a name="p46525609"></a><a name="p46525609"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.1.4.1.3"><p id="p10477980"><a name="p10477980"></a><a name="p10477980"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43410060"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.4.1.1 "><p id="p26553952"><a name="p26553952"></a><a name="p26553952"></a>task_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.2 "><p id="p3386497"><a name="p3386497"></a><a name="p3386497"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.4.1.3 "><div class="p" id="p41609089162611"><a name="p41609089162611"></a><a name="p41609089162611"></a>Status of a task, which can be one of the following:<a name="ul26350006162615"></a><a name="ul26350006162615"></a><ul id="ul26350006162615"><li>success</li><li>failed</li><li>waiting</li><li>running</li><li>preprocess</li><li>ready</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row52837255"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.4.1.1 "><p id="p51959302"><a name="p51959302"></a><a name="p51959302"></a>task_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.2 "><p id="p47953966"><a name="p47953966"></a><a name="p47953966"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.1.4.1.3 "><p id="p59066022"><a name="p59066022"></a><a name="p59066022"></a>Additional information about a task</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "task_status": "running",
       "task_msg": ""
    }
    ```


## Returned Value<a name="section27813538"></a>

See  [Status Code](status-code.md).

