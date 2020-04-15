# Canceling Job Execution<a name="EN-US_TOPIC_0172486179"></a>

## Function<a name="section5957478711297"></a>

This API is used to cancel a job object being executed. This API is compatible with Sahara.

## URI<a name="section9153250112933"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-executions/\{job\_execution\_id\}/cancel

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6505449415356"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3492262515356"><a name="p3492262515356"></a><a name="p3492262515356"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1016041415356"><a name="p1016041415356"></a><a name="p1016041415356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row20659256153330"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p14068949143358"><a name="p14068949143358"></a><a name="p14068949143358"></a>job_execution_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p36449896143358"><a name="p36449896143358"></a><a name="p36449896143358"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p59095518143358"><a name="p59095518143358"></a><a name="p59095518143358"></a>Job execution object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

None.

## Response<a name="section38599577193858"></a>

**Table  2**  Response parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42399257145341"><a name="p42399257145341"></a><a name="p42399257145341"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1428203814541"><a name="p1428203814541"></a><a name="p1428203814541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p31671624145411"><a name="p31671624145411"></a><a name="p31671624145411"></a>Key-value pair set, containing job running information returned by Oozie</p>
</td>
</tr>
<tr id="row1794513155918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p38981597145341"><a name="p38981597145341"></a><a name="p38981597145341"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p973236414541"><a name="p973236414541"></a><a name="p973236414541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3164852145411"><a name="p3164852145411"></a><a name="p3164852145411"></a>Cluster ID</p>
</td>
</tr>
<tr id="row23363161601"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p30535368145341"><a name="p30535368145341"></a><a name="p30535368145341"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4688460014391"><a name="p4688460014391"></a><a name="p4688460014391"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25475938145411"><a name="p25475938145411"></a><a name="p25475938145411"></a>Job ID</p>
</td>
</tr>
<tr id="row52664138135611"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p47249950145341"><a name="p47249950145341"></a><a name="p47249950145341"></a>oozie_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p57515029144652"><a name="p57515029144652"></a><a name="p57515029144652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p49912669145411"><a name="p49912669145411"></a><a name="p49912669145411"></a>Workflow ID returned by Oozie</p>
</td>
</tr>
<tr id="row15896716111552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18366376145341"><a name="p18366376145341"></a><a name="p18366376145341"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p46523794144652"><a name="p46523794144652"></a><a name="p46523794144652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p147081301415"><a name="p147081301415"></a><a name="p147081301415"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row14374745135652"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p34424442145341"><a name="p34424442145341"></a><a name="p34424442145341"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p43975827144652"><a name="p43975827144652"></a><a name="p43975827144652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p55323279145411"><a name="p55323279145411"></a><a name="p55323279145411"></a>Job execution object creation time</p>
</td>
</tr>
<tr id="row26626414135718"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p63812528145341"><a name="p63812528145341"></a><a name="p63812528145341"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p39284672144652"><a name="p39284672144652"></a><a name="p39284672144652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p65352516145411"><a name="p65352516145411"></a><a name="p65352516145411"></a>Job execution object update time</p>
</td>
</tr>
<tr id="row12439792135751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12890412145341"><a name="p12890412145341"></a><a name="p12890412145341"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p50067010144652"><a name="p50067010144652"></a><a name="p50067010144652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p61799874145411"><a name="p61799874145411"></a><a name="p61799874145411"></a>Job start time</p>
</td>
</tr>
<tr id="row62845631135831"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p60124904145442"><a name="p60124904145442"></a><a name="p60124904145442"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5570686214391"><a name="p5570686214391"></a><a name="p5570686214391"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p27080332145541"><a name="p27080332145541"></a><a name="p27080332145541"></a>Job end time</p>
</td>
</tr>
<tr id="row8652083151249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8967486145442"><a name="p8967486145442"></a><a name="p8967486145442"></a>return_code</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4796924214477"><a name="p4796924214477"></a><a name="p4796924214477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11556241145541"><a name="p11556241145541"></a><a name="p11556241145541"></a>Response code after job execution</p>
</td>
</tr>
<tr id="row12228393151256"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p27737544145442"><a name="p27737544145442"></a><a name="p27737544145442"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2298335114477"><a name="p2298335114477"></a><a name="p2298335114477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p35891861145541"><a name="p35891861145541"></a><a name="p35891861145541"></a>Input data source ID of a job execution object</p>
</td>
</tr>
<tr id="row4987054814430"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20901786145442"><a name="p20901786145442"></a><a name="p20901786145442"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1786488314430"><a name="p1786488314430"></a><a name="p1786488314430"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p59818779145541"><a name="p59818779145541"></a><a name="p59818779145541"></a>Output data source ID of a job execution object</p>
</td>
</tr>
<tr id="row2224933814447"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3690448145442"><a name="p3690448145442"></a><a name="p3690448145442"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p11644244144713"><a name="p11644244144713"></a><a name="p11644244144713"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p54237486145541"><a name="p54237486145541"></a><a name="p54237486145541"></a>Whether a job execution object is protected</p>
<a name="ul1671978416321"></a><a name="ul1671978416321"></a><ul id="ul1671978416321"><li>true</li><li>false</li></ul>
<p id="p4201874516321"><a name="p4201874516321"></a><a name="p4201874516321"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row65803519144414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5982284145442"><a name="p5982284145442"></a><a name="p5982284145442"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52405738144713"><a name="p52405738144713"></a><a name="p52405738144713"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12006946145541"><a name="p12006946145541"></a><a name="p12006946145541"></a>Whether a job execution object is public</p>
<a name="ul3872134516111"></a><a name="ul3872134516111"></a><ul id="ul3872134516111"><li>true</li><li>false</li></ul>
<p id="p4213768316111"><a name="p4213768316111"></a><a name="p4213768316111"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row42012596144424"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p66117752145442"><a name="p66117752145442"></a><a name="p66117752145442"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32531313144713"><a name="p32531313144713"></a><a name="p32531313144713"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p28911440145541"><a name="p28911440145541"></a><a name="p28911440145541"></a>Key-value pair set for saving job running configurations</p>
</td>
</tr>
<tr id="row35356831145431"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15677449145442"><a name="p15677449145442"></a><a name="p15677449145442"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p28767711145431"><a name="p28767711145431"></a><a name="p28767711145431"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4256989145541"><a name="p4256989145541"></a><a name="p4256989145541"></a>Job execution object ID</p>
</td>
</tr>
<tr id="row62941536101347"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p65099693101347"><a name="p65099693101347"></a><a name="p65099693101347"></a>oozie_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p38277647101347"><a name="p38277647101347"></a><a name="p38277647101347"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p13481717101347"><a name="p13481717101347"></a><a name="p13481717101347"></a>Workflow ID returned by Oozie</p>
</td>
</tr>
<tr id="row23776573101354"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p46854231101354"><a name="p46854231101354"></a><a name="p46854231101354"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52014329101354"><a name="p52014329101354"></a><a name="p52014329101354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p52411088101354"><a name="p52411088101354"></a><a name="p52411088101354"></a>Key-value pair set, containing job running information returned by Oozie</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    None.

-   Example response

    ```
    {
        "job_execution": {
            "created_at": "2017-05-25T07:28:12",
            "updated_at": "2017-05-25T07:28:13",
            "id": "2de74673-1a78-48af-a95b-e1fec4a4ae9c",
            "tenant_id": "37caa80116e1403ab603e5eeb48a2f74",
            "job_id": "",
            "start_time": "2017-05-25T07:28:12",
            "end_time": null,
            "cluster_id": "ef7b54f2-3d92-49b2-a6d7-94607e1ea7df",
            "oozie_job_id": null,
            "return_code": null,
            "input_id": null,
            "output_id": null,
            "is_protected": null,
            "is_public": null,
            "engine_job_id": null,
            "job_configs": null,
            "data_source_urls": null,
            "info": null
        }
    }
    ```


## Status Code<a name="section25088328113020"></a>

[Table 3](#table1584477916050)  describes the status code of this API.

**Table  3**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object being executed has been canceled successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

