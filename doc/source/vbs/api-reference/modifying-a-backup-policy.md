# Modifying a Backup Policy<a name="EN-US_TOPIC_0043410559"></a>

## Function<a name="section63962185"></a>

This interface is used to modify a backup policy.

## URI<a name="section38788755"></a>

-   URI format

    PUT /v2/\{project\_id\}/backuppolicy/\{policy\_id\}

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
    <tr id="row38712681154151"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p48719461154151"><a name="p48719461154151"></a><a name="p48719461154151"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p53962265154151"><a name="p53962265154151"></a><a name="p53962265154151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p8867374154151"><a name="p8867374154151"></a><a name="p8867374154151"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

-   Parameter description

    <a name="table48412952"></a>
    <table><thead align="left"><tr id="row28932175"><th class="cellrowborder" valign="top" width="26.697330266973307%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.968703129687032%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35836416358364%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.97560243975603%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row187031441791"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p385596811791"><a name="p385596811791"></a><a name="p385596811791"></a>backup_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p363264551791"><a name="p363264551791"></a><a name="p363264551791"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p567617131791"><a name="p567617131791"></a><a name="p567617131791"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p342960231791"><a name="p342960231791"></a><a name="p342960231791"></a>Backup policy name</p>
    <p id="p65772916460"><a name="p65772916460"></a><a name="p65772916460"></a>The name is a string of 1 to 64 characters consisting of letters, digits, underscores (_), and hyphens (-). It cannot start with <strong id="b8423527069400"><a name="b8423527069400"></a><a name="b8423527069400"></a>default</strong>.</p>
    <p id="p12642541172944"><a name="p12642541172944"></a><a name="p12642541172944"></a>The default backup policy cannot be renamed.</p>
    </td>
    </tr>
    <tr id="row50598521"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p44217312144451"><a name="p44217312144451"></a><a name="p44217312144451"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p56460178"><a name="p56460178"></a><a name="p56460178"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p1152258104112"><a name="p1152258104112"></a><a name="p1152258104112"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p9871675"><a name="p9871675"></a><a name="p9871675"></a>Details about the scheduling policy</p>
    </td>
    </tr>
    <tr id="row21736211"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p43785202144538"><a name="p43785202144538"></a><a name="p43785202144538"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p4945408"><a name="p4945408"></a><a name="p4945408"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p26224039104112"><a name="p26224039104112"></a><a name="p26224039104112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p148191957131719"><a name="p148191957131719"></a><a name="p148191957131719"></a>Backup execution time (UTC), in the format of <strong id="b728462712424"><a name="b728462712424"></a><a name="b728462712424"></a>HH:mm</strong></p>
    <p id="p1972593913185"><a name="p1972593913185"></a><a name="p1972593913185"></a>You need to set the execution time on a full hour. You can set multiple execution times, and use commas (,) to separate one time from another. To set multiple backup execution times, enter them in ascending order by local time. For example, if your local time is 2 hours ahead of UTC and you want to perform backups at the local times 00:00, 02:00, and 04:00, set this parameter to <strong id="b160194444211"><a name="b160194444211"></a><a name="b160194444211"></a>22:00,00:00,02:00</strong> (UTC times) and <strong id="b561134415424"><a name="b561134415424"></a><a name="b561134415424"></a>time_zone</strong> to <strong id="b116124411421"><a name="b116124411421"></a><a name="b116124411421"></a>UTC+02:00</strong>. </p>
    </td>
    </tr>
    <tr id="row48433347"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p8495141519274"><a name="p8495141519274"></a><a name="p8495141519274"></a>frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p10722842"><a name="p10722842"></a><a name="p10722842"></a>No (Either this field or <strong id="b4882019205220"><a name="b4882019205220"></a><a name="b4882019205220"></a>week_frequency</strong> must be specified.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p10496161572714"><a name="p10496161572714"></a><a name="p10496161572714"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p18496121518271"><a name="p18496121518271"></a><a name="p18496121518271"></a>Backup interval (1 to 14 days). Set either this parameter or <strong id="b1637017505523"><a name="b1637017505523"></a><a name="b1637017505523"></a>week_frequency</strong>. If you set both, this parameter prevails.</p>
    </td>
    </tr>
    <tr id="row638925115264"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p549811519276"><a name="p549811519276"></a><a name="p549811519276"></a>week_frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p14855251121517"><a name="p14855251121517"></a><a name="p14855251121517"></a>No (Either this field or <strong>frequency</strong> must be specified.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p249917158279"><a name="p249917158279"></a><a name="p249917158279"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p184991215132718"><a name="p184991215132718"></a><a name="p184991215132718"></a>Specifies on which days of each week backup jobs are executed. The value can be one or more of the following:</p>
    <p id="p144991415132717"><a name="p144991415132717"></a><a name="p144991415132717"></a>SUN, MON, TUE, WED, THU, FRI, SAT</p>
    </td>
    </tr>
    <tr id="row52369142144652"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p1849912158270"><a name="p1849912158270"></a><a name="p1849912158270"></a>rentention_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p1549991572715"><a name="p1549991572715"></a><a name="p1549991572715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p849991513274"><a name="p849991513274"></a><a name="p849991513274"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p6499141518271"><a name="p6499141518271"></a><a name="p6499141518271"></a>Number of retained backups. The value must be integer from 2 to 14. If you set this parameter and <strong id="b156661016536"><a name="b156661016536"></a><a name="b156661016536"></a>rentention_day</strong> at the same time, this parameter prevails.</p>
    </td>
    </tr>
    <tr id="row12890354142616"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p650011562714"><a name="p650011562714"></a><a name="p650011562714"></a>rentention_day</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p95009158273"><a name="p95009158273"></a><a name="p95009158273"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p150011518275"><a name="p150011518275"></a><a name="p150011518275"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p4500181516272"><a name="p4500181516272"></a><a name="p4500181516272"></a>Retention days of backups. The value is an integer ranging from 2 to 99999. If you enter a floating point number, the number will be rounded down to the nearest integer when you send the request.</p>
    </td>
    </tr>
    <tr id="row13400247144843"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p26845495144845"><a name="p26845495144845"></a><a name="p26845495144845"></a>remain_first_backup_of_curMonth</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p6410995144843"><a name="p6410995144843"></a><a name="p6410995144843"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p49528559144843"><a name="p49528559144843"></a><a name="p49528559144843"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p52390368144843"><a name="p52390368144843"></a><a name="p52390368144843"></a>Whether to retain the first backup in the current month</p>
    <a name="ul10334226145125"></a><a name="ul10334226145125"></a><ul id="ul10334226145125"><li>Y</li><li>N</li></ul>
    </td>
    </tr>
    <tr id="row36885943144931"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p34971403144931"><a name="p34971403144931"></a><a name="p34971403144931"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p14111424144931"><a name="p14111424144931"></a><a name="p14111424144931"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p2174718144931"><a name="p2174718144931"></a><a name="p2174718144931"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p37418078145334"><a name="p37418078145334"></a><a name="p37418078145334"></a>Backup policy status</p>
    <a name="ul3077574414513"></a><a name="ul3077574414513"></a><ul id="ul3077574414513"><li>ON</li><li>OFF</li></ul>
    </td>
    </tr>
    <tr id="row327643916386"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p281672492310"><a name="p281672492310"></a><a name="p281672492310"></a>time_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p13816324162312"><a name="p13816324162312"></a><a name="p13816324162312"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p88163249236"><a name="p88163249236"></a><a name="p88163249236"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p134451014203612"><a name="p134451014203612"></a><a name="p134451014203612"></a>Time zone. The value is in the UTC+/-HH:mm format.</p>
    <p id="p13467818248"><a name="p13467818248"></a><a name="p13467818248"></a>This parameter specifies the time zone of the local time with the DST offset, for example, UTC+08:00 or UTC-02:00. If execution times are in different days after converting into UTC times, this parameter must be used with <strong>week_frequency</strong> and <strong>start_time</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "backup_policy_name": "policy_01",
        "scheduled_policy" : {
            "remain_first_backup_of_curMonth" : "Y",
            "rentention_num" : 10,
            "week_frequency" : ["MON"],
            "start_time" : "12:00",
            "status" : "ON"
        },
        "time_zone": "UTC+08:00"
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="29.182918291829186%" id="mcps1.1.4.1.1"><p id="p772371553820"><a name="p772371553820"></a><a name="p772371553820"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.471547154715473%" id="mcps1.1.4.1.2"><p id="p373961583819"><a name="p373961583819"></a><a name="p373961583819"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.345534553455344%" id="mcps1.1.4.1.3"><p id="p773991510384"><a name="p773991510384"></a><a name="p773991510384"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p34048608151944"><a name="p34048608151944"></a><a name="p34048608151944"></a>backup_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>Backup policy ID returned if the operation is successful</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "backup_policy_id": "af8a20b0-117d-4fc3-ae53-aa3968a4f870"
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


## Status Code<a name="section24171358"></a>

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

