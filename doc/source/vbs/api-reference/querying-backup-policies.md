# Querying Backup Policies<a name="EN-US_TOPIC_0043410558"></a>

## Function<a name="section63962185"></a>

This interface is used to query all backup policies of a tenant.

## URI<a name="section38788755"></a>

-   URI format

    GET /v2/\{project\_id\}/backuppolicy

-   Parameter description

    <a name="table60344938"></a>
    <table><thead align="left"><tr id="row59011071"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p15167431"><a name="p15167431"></a><a name="p15167431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p20602375"><a name="p20602375"></a><a name="p20602375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p58179688"><a name="p58179688"></a><a name="p58179688"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14934289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1717931"><a name="p1717931"></a><a name="p1717931"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4934750"><a name="p4934750"></a><a name="p4934750"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

None

## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="31.009999999999998%" id="mcps1.1.4.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.92%" id="mcps1.1.4.1.2"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.06999999999999%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p34048608151944"><a name="p34048608151944"></a><a name="p34048608151944"></a>backup_policies</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>List of backup policies</p>
    </td>
    </tr>
    <tr id="row15240089153211"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p42050300153340"><a name="p42050300153340"></a><a name="p42050300153340"></a>backup_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p7483329153340"><a name="p7483329153340"></a><a name="p7483329153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p2169918153340"><a name="p2169918153340"></a><a name="p2169918153340"></a>Backup policy name</p>
    </td>
    </tr>
    <tr id="row49142966153315"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p38366875153340"><a name="p38366875153340"></a><a name="p38366875153340"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p66829450153340"><a name="p66829450153340"></a><a name="p66829450153340"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p44476387153340"><a name="p44476387153340"></a><a name="p44476387153340"></a>Details about the scheduling policy</p>
    </td>
    </tr>
    <tr id="row37005886153318"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p9704892153340"><a name="p9704892153340"></a><a name="p9704892153340"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p54594377153340"><a name="p54594377153340"></a><a name="p54594377153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p60068455153340"><a name="p60068455153340"></a><a name="p60068455153340"></a>Backup execution time (on a full hour), which is expressed in the UTC format. If you want to set multiple execution times, separate them using commas (,).</p>
    </td>
    </tr>
    <tr id="row27429961153321"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p34924824153340"><a name="p34924824153340"></a><a name="p34924824153340"></a>frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p32108888153340"><a name="p32108888153340"></a><a name="p32108888153340"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p50683125153340"><a name="p50683125153340"></a><a name="p50683125153340"></a>Backup interval (1 to 14 days)</p>
    </td>
    </tr>
    <tr id="row313175912238"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p12131659122317"><a name="p12131659122317"></a><a name="p12131659122317"></a>week_frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p6132859102318"><a name="p6132859102318"></a><a name="p6132859102318"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p1213255912318"><a name="p1213255912318"></a><a name="p1213255912318"></a>Week information list</p>
    </td>
    </tr>
    <tr id="row59676584153324"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p38123120153340"><a name="p38123120153340"></a><a name="p38123120153340"></a>rentention_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p11054614153340"><a name="p11054614153340"></a><a name="p11054614153340"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p23008573153340"><a name="p23008573153340"></a><a name="p23008573153340"></a>Number of retained backups. The value must be an integer from 2 to 14.</p>
    </td>
    </tr>
    <tr id="row7868192102420"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p1786872162420"><a name="p1786872162420"></a><a name="p1786872162420"></a>rentention_day</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p4869112192418"><a name="p4869112192418"></a><a name="p4869112192418"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p1586912292417"><a name="p1586912292417"></a><a name="p1586912292417"></a>Retention days of backups. The value is an integer ranging from 2 to 999999. If you enter a floating point number, the number will be rounded down to the nearest integer when you send the request.</p>
    </td>
    </tr>
    <tr id="row17757769153327"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p63142605153340"><a name="p63142605153340"></a><a name="p63142605153340"></a>remain_first_backup_of_curMonth</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p15615278153340"><a name="p15615278153340"></a><a name="p15615278153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p56878007153340"><a name="p56878007153340"></a><a name="p56878007153340"></a>Whether to retain the first backup in the current month</p>
    <a name="ul42140023153340"></a><a name="ul42140023153340"></a><ul id="ul42140023153340"><li>Y</li><li>N</li></ul>
    </td>
    </tr>
    <tr id="row55800042153331"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p63777303153340"><a name="p63777303153340"></a><a name="p63777303153340"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p19118878153340"><a name="p19118878153340"></a><a name="p19118878153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p5125282153340"><a name="p5125282153340"></a><a name="p5125282153340"></a>Backup policy status</p>
    <a name="ul46127545153340"></a><a name="ul46127545153340"></a><ul id="ul46127545153340"><li>ON</li><li>OFF</li></ul>
    </td>
    </tr>
    <tr id="row20363174153334"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p38804430153334"><a name="p38804430153334"></a><a name="p38804430153334"></a>backup_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p51073112153433"><a name="p51073112153433"></a><a name="p51073112153433"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p46879559153334"><a name="p46879559153334"></a><a name="p46879559153334"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row61449844153338"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p11381506153338"><a name="p11381506153338"></a><a name="p11381506153338"></a>policy_resource_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p49008211153338"><a name="p49008211153338"></a><a name="p49008211153338"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p10242150153338"><a name="p10242150153338"></a><a name="p10242150153338"></a>Number of volumes associated with the backup policy</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row19551115418376"><td class="cellrowborder" valign="top" width="31.009999999999998%" headers="mcps1.1.4.1.1 "><p id="p17551185433714"><a name="p17551185433714"></a><a name="p17551185433714"></a>time_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.92%" headers="mcps1.1.4.1.2 "><p id="p655165433716"><a name="p655165433716"></a><a name="p655165433716"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.06999999999999%" headers="mcps1.1.4.1.3 "><p id="p45511054163715"><a name="p45511054163715"></a><a name="p45511054163715"></a>Time zone of the execution time</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "backup_policies" : [
        {
            "backup_policy_id" : "XX",
            "backup_policy_name": "plan01",
            "scheduled_policy" : {
                "remain_first_backup_of_curMonth" : "Y",
                "rentention_num" : 10,
                "frequency" : 1,
                "start_time" : "12:00",
                "status" : "ON"
            },
            "policy_resource_count": 0
        },
        {
            "backup_policy_id" : "YY",
            "backup_policy_name ": "plan02",
            "scheduled_policy" : {
                "remain_first_backup_of_curMonth" : "Y",
                "rentention_num" : 10,
                "frequency" : 1,
                "start_time" : "14:00",
                "status" : "ON"
            },
            "policy_resource_count": 10
        }]
    }
    ```

    or

    ```
    {
        "error": {
            "code": "XXXX",
            "message": "XXX"
        }
    }
    ```


## Status Codes<a name="section24171358"></a>

-   Normal

    200

-   Abnormal

    <a name="table51230787"></a>
    <table><thead align="left"><tr id="row60503138"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1807185"><a name="p1807185"></a><a name="p1807185"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p12164329"><a name="p12164329"></a><a name="p12164329"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45786577"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17725233"><a name="p17725233"></a><a name="p17725233"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26457778"><a name="p26457778"></a><a name="p26457778"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row36793414"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row31979016"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4499052116376"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2035357816376"><a name="p2035357816376"></a><a name="p2035357816376"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3802708716376"><a name="p3802708716376"></a><a name="p3802708716376"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8462523163725"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14375766163725"><a name="p14375766163725"></a><a name="p14375766163725"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p23586373163725"><a name="p23586373163725"></a><a name="p23586373163725"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60343628163758"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55995701163758"><a name="p55995701163758"></a><a name="p55995701163758"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p39357967163758"><a name="p39357967163758"></a><a name="p39357967163758"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row32079544163754"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p48306260163754"><a name="p48306260163754"></a><a name="p48306260163754"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20492948163754"><a name="p20492948163754"></a><a name="p20492948163754"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28680770163738"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p41441040163738"><a name="p41441040163738"></a><a name="p41441040163738"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1281119163738"><a name="p1281119163738"></a><a name="p1281119163738"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row65552906164354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8185203164354"><a name="p8185203164354"></a><a name="p8185203164354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59021712164354"><a name="p59021712164354"></a><a name="p59021712164354"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row19714506"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p53371190"><a name="p53371190"></a><a name="p53371190"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28099101"><a name="p28099101"></a><a name="p28099101"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row32688750164938"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30543097164938"><a name="p30543097164938"></a><a name="p30543097164938"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p58071768164938"><a name="p58071768164938"></a><a name="p58071768164938"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row11809518164943"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17046908164943"><a name="p17046908164943"></a><a name="p17046908164943"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38622347164943"><a name="p38622347164943"></a><a name="p38622347164943"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row38399341164956"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23338889164956"><a name="p23338889164956"></a><a name="p23338889164956"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11401882164956"><a name="p11401882164956"></a><a name="p11401882164956"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row51565323"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16041657"><a name="p16041657"></a><a name="p16041657"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

