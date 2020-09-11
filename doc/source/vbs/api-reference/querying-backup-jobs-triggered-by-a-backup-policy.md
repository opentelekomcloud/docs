# Querying Backup Jobs Triggered by a Backup Policy<a name="EN-US_TOPIC_0043430177"></a>

## Function<a name="section63962185"></a>

This interface is used to query the status of backup jobs triggered by a backup policy.

## URI<a name="section38788755"></a>

-   URI format

    GET /v2/\{project\_id\}/backuppolicy/\{policy\_id\}/backuptasks

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
    <tr id="row49177768142544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p23976272142544"><a name="p23976272142544"></a><a name="p23976272142544"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p63029893142544"><a name="p63029893142544"></a><a name="p63029893142544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5147694142544"><a name="p5147694142544"></a><a name="p5147694142544"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Request filter**  parameter description

    <a name="table25503279151723"></a>
    <table><thead align="left"><tr id="row56230478151723"><th class="cellrowborder" valign="top" width="11.84%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.959999999999999%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.97%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.23%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19937166154259"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p4297722154259"><a name="p4297722154259"></a><a name="p4297722154259"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p12571227154259"><a name="p12571227154259"></a><a name="p12571227154259"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p11636505154259"><a name="p11636505154259"></a><a name="p11636505154259"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p25300480154733"><a name="p25300480154733"></a><a name="p25300480154733"></a>Sorting order. Possible values are <strong id="b15543171634517"><a name="b15543171634517"></a><a name="b15543171634517"></a>asc</strong> (ascending) and <strong id="b1054391620458"><a name="b1054391620458"></a><a name="b1054391620458"></a>desc</strong> (descending).</p>
    </td>
    </tr>
    <tr id="row333354215434"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p158151415434"><a name="p158151415434"></a><a name="p158151415434"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p6099381015434"><a name="p6099381015434"></a><a name="p6099381015434"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p4155159115434"><a name="p4155159115434"></a><a name="p4155159115434"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p1023569615434"><a name="p1023569615434"></a><a name="p1023569615434"></a>Maximum number of query results that can be returned. The default value is 20.</p>
    </td>
    </tr>
    <tr id="row47274742203131"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p426078203131"><a name="p426078203131"></a><a name="p426078203131"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p55980731203131"><a name="p55980731203131"></a><a name="p55980731203131"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p22418100203131"><a name="p22418100203131"></a><a name="p22418100203131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p12282226203131"><a name="p12282226203131"></a><a name="p12282226203131"></a>Start number from which backup jobs are queried. The value is the backup job ID.</p>
    </td>
    </tr>
    <tr id="row36697479203136"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p5637728203136"><a name="p5637728203136"></a><a name="p5637728203136"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p45790305203136"><a name="p45790305203136"></a><a name="p45790305203136"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p2267775203322"><a name="p2267775203322"></a><a name="p2267775203322"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p35967384203445"><a name="p35967384203445"></a><a name="p35967384203445"></a>Backup job ID</p>
    </td>
    </tr>
    <tr id="row44971752203143"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p8713648203143"><a name="p8713648203143"></a><a name="p8713648203143"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p62805252203143"><a name="p62805252203143"></a><a name="p62805252203143"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p17285389203143"><a name="p17285389203143"></a><a name="p17285389203143"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p40478322203143"><a name="p40478322203143"></a><a name="p40478322203143"></a>Backup job status</p>
    <a name="ul47063353161731"></a><a name="ul47063353161731"></a><ul id="ul47063353161731"><li>RUNNING</li><li>EXECUTE_TIMEOUT</li><li>WAITING</li><li>EXECUTE_FAIL</li><li>EXECUTE_SUCCESS</li><li>SKIP</li></ul>
    </td>
    </tr>
    <tr id="row9838157203147"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p15520033203147"><a name="p15520033203147"></a><a name="p15520033203147"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p28137741203147"><a name="p28137741203147"></a><a name="p28137741203147"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p24822778203147"><a name="p24822778203147"></a><a name="p24822778203147"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p9014351203147"><a name="p9014351203147"></a><a name="p9014351203147"></a>Keyword for sorting query results. The value must be <strong id="b1533731523172526"><a name="b1533731523172526"></a><a name="b1533731523172526"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row57908147101022"><td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.1.5.1.1 "><p id="p60048291101022"><a name="p60048291101022"></a><a name="p60048291101022"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p32073375101022"><a name="p32073375101022"></a><a name="p32073375101022"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.97%" headers="mcps1.1.5.1.3 "><p id="p47806608101022"><a name="p47806608101022"></a><a name="p47806608101022"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.23%" headers="mcps1.1.5.1.4 "><p id="p47130078101022"><a name="p47130078101022"></a><a name="p47130078101022"></a>Amount of the offset. The default value is 0.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET /v2/{project_id}/backuppolicy/{policy_id}/backuptasks?limit=10
    ```


## Request<a name="section13554483"></a>

None

## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="30.990000000000002%" id="mcps1.1.4.1.1"><p id="p23381931114710"><a name="p23381931114710"></a><a name="p23381931114710"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.079999999999998%" id="mcps1.1.4.1.2"><p id="p0338331134711"><a name="p0338331134711"></a><a name="p0338331134711"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.93%" id="mcps1.1.4.1.3"><p id="p535303119474"><a name="p535303119474"></a><a name="p535303119474"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p34048608151944"><a name="p34048608151944"></a><a name="p34048608151944"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>Total number of queried jobs</p>
    </td>
    </tr>
    <tr id="row15240089153211"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p42050300153340"><a name="p42050300153340"></a><a name="p42050300153340"></a>tasks</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p7483329153340"><a name="p7483329153340"></a><a name="p7483329153340"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p2169918153340"><a name="p2169918153340"></a><a name="p2169918153340"></a>Details about the backup job</p>
    </td>
    </tr>
    <tr id="row49142966153315"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p38366875153340"><a name="p38366875153340"></a><a name="p38366875153340"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p66829450153340"><a name="p66829450153340"></a><a name="p66829450153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p44476387153340"><a name="p44476387153340"></a><a name="p44476387153340"></a>Backup job status</p>
    <a name="ul24509643143230"></a><a name="ul24509643143230"></a><ul id="ul24509643143230"><li>RUNNING</li><li>EXECUTE_TIMEOUT</li><li>WAITING</li><li>EXECUTE_FAIL</li><li>EXECUTE_SUCCESS</li><li>SKIP</li></ul>
    </td>
    </tr>
    <tr id="row37005886153318"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p9704892153340"><a name="p9704892153340"></a><a name="p9704892153340"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p54594377153340"><a name="p54594377153340"></a><a name="p54594377153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p60068455153340"><a name="p60068455153340"></a><a name="p60068455153340"></a>Backup job ID</p>
    </td>
    </tr>
    <tr id="row27429961153321"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p34924824153340"><a name="p34924824153340"></a><a name="p34924824153340"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p32108888153340"><a name="p32108888153340"></a><a name="p32108888153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p50683125153340"><a name="p50683125153340"></a><a name="p50683125153340"></a>Time the backup job was created. The time is in UTC format, for example, 2016-12-02T09:06:46.706.</p>
    </td>
    </tr>
    <tr id="row59676584153324"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p38123120153340"><a name="p38123120153340"></a><a name="p38123120153340"></a>finished_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p239112391814"><a name="p239112391814"></a><a name="p239112391814"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p23008573153340"><a name="p23008573153340"></a><a name="p23008573153340"></a>Time the backup job was completed. The time is in UTC format, for example, 2016-12-02T13:00:00.121.</p>
    </td>
    </tr>
    <tr id="row3032128414342"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p4010493014342"><a name="p4010493014342"></a><a name="p4010493014342"></a>backup_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p6170234814342"><a name="p6170234814342"></a><a name="p6170234814342"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p3183428014342"><a name="p3183428014342"></a><a name="p3183428014342"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row17757769153327"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p63142605153340"><a name="p63142605153340"></a><a name="p63142605153340"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p15615278153340"><a name="p15615278153340"></a><a name="p15615278153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p45645767143341"><a name="p45645767143341"></a><a name="p45645767143341"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row55800042153331"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p63777303153340"><a name="p63777303153340"></a><a name="p63777303153340"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p19118878153340"><a name="p19118878153340"></a><a name="p19118878153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p46173942143351"><a name="p46173942143351"></a><a name="p46173942143351"></a>Resource type</p>
    </td>
    </tr>
    <tr id="row9537529196"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p853832918910"><a name="p853832918910"></a><a name="p853832918910"></a>vbs_job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p175382291698"><a name="p175382291698"></a><a name="p175382291698"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p12538629595"><a name="p12538629595"></a><a name="p12538629595"></a>VBS backup job ID</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="30.990000000000002%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.079999999999998%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.93%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "tasks": [
        {
          "status": "RUNNING",
          "job_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
          "created_at": "2016-12-03T06:24:34.467",
          "backup_name": "autobk_a61d",
          "resource_id": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
          "resource_type": "volume"
        },
        {
          "status": "EXECUTE_SUCCESS",
          "job_id": "c11b5a18-4559-4731-b7b3-58e2bd89cdb9",
          "created_at": "2016-12-02T09:06:46.706",
          "finished_at": "2016-12-02T13:00:00.121",
          "backup_name": "autobk_e6d2",
          "resource_id": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
          "resource_type": "volume"
        }
      ],
      "count": 2
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

