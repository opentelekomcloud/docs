# Querying Job Execution Object Details<a name="EN-US_TOPIC_0172486184"></a>

## Function<a name="section5957478711297"></a>

This API is used to query detailed information about a job execution object. This API is compatible with Sahara.

## URI<a name="section9153250112933"></a>

-   Format

    GET /v1.1/\{project\_id\}/job-executions/\{job\_execution\_id\}

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
<tbody><tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13817546144526"><a name="p13817546144526"></a><a name="p13817546144526"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p30606123144557"><a name="p30606123144557"></a><a name="p30606123144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60102458144812"><a name="p60102458144812"></a><a name="p60102458144812"></a>Key-value pair set, containing job running information returned by Oozie</p>
</td>
</tr>
<tr id="row1794513155918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6661651144526"><a name="p6661651144526"></a><a name="p6661651144526"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p31721435144557"><a name="p31721435144557"></a><a name="p31721435144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p59713193144812"><a name="p59713193144812"></a><a name="p59713193144812"></a>Cluster ID</p>
</td>
</tr>
<tr id="row23363161601"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24505987144526"><a name="p24505987144526"></a><a name="p24505987144526"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p39477276144557"><a name="p39477276144557"></a><a name="p39477276144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p44374042144812"><a name="p44374042144812"></a><a name="p44374042144812"></a>Job ID</p>
</td>
</tr>
<tr id="row3699425711725"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2908760411735"><a name="p2908760411735"></a><a name="p2908760411735"></a>engine_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5327575811735"><a name="p5327575811735"></a><a name="p5327575811735"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2036912311735"><a name="p2036912311735"></a><a name="p2036912311735"></a>Workflow ID of Oozie</p>
</td>
</tr>
<tr id="row52664138135611"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13907076144526"><a name="p13907076144526"></a><a name="p13907076144526"></a>oozie_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56340641144557"><a name="p56340641144557"></a><a name="p56340641144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2204786144812"><a name="p2204786144812"></a><a name="p2204786144812"></a>Workflow ID returned by Oozie</p>
</td>
</tr>
<tr id="row15896716111552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4820169144526"><a name="p4820169144526"></a><a name="p4820169144526"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1702693144557"><a name="p1702693144557"></a><a name="p1702693144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1499019144114"><a name="p1499019144114"></a><a name="p1499019144114"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row14374745135652"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24242445144526"><a name="p24242445144526"></a><a name="p24242445144526"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p33303851144557"><a name="p33303851144557"></a><a name="p33303851144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60295112144812"><a name="p60295112144812"></a><a name="p60295112144812"></a>Job execution object creation time</p>
</td>
</tr>
<tr id="row26626414135718"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p23111379144526"><a name="p23111379144526"></a><a name="p23111379144526"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52207806144557"><a name="p52207806144557"></a><a name="p52207806144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p65939764144812"><a name="p65939764144812"></a><a name="p65939764144812"></a>Job execution object update time</p>
</td>
</tr>
<tr id="row12439792135751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3870758144526"><a name="p3870758144526"></a><a name="p3870758144526"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p8765234144557"><a name="p8765234144557"></a><a name="p8765234144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20141538144812"><a name="p20141538144812"></a><a name="p20141538144812"></a>Job start time</p>
</td>
</tr>
<tr id="row62845631135831"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3210842144526"><a name="p3210842144526"></a><a name="p3210842144526"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p14513632144557"><a name="p14513632144557"></a><a name="p14513632144557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p53449181144812"><a name="p53449181144812"></a><a name="p53449181144812"></a>Job end time</p>
</td>
</tr>
<tr id="row8652083151249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p35508397144628"><a name="p35508397144628"></a><a name="p35508397144628"></a>return_code</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4796924214477"><a name="p4796924214477"></a><a name="p4796924214477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p41312377144812"><a name="p41312377144812"></a><a name="p41312377144812"></a>Response code after job execution</p>
</td>
</tr>
<tr id="row12228393151256"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p48708808144628"><a name="p48708808144628"></a><a name="p48708808144628"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2298335114477"><a name="p2298335114477"></a><a name="p2298335114477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p51951887144812"><a name="p51951887144812"></a><a name="p51951887144812"></a>Input data source ID of a job execution object</p>
</td>
</tr>
<tr id="row4987054814430"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8132410144628"><a name="p8132410144628"></a><a name="p8132410144628"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4217960116818"><a name="p4217960116818"></a><a name="p4217960116818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p23526852144812"><a name="p23526852144812"></a><a name="p23526852144812"></a>Output data source ID of a job execution object</p>
</td>
</tr>
<tr id="row2224933814447"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p22947053144628"><a name="p22947053144628"></a><a name="p22947053144628"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p11644244144713"><a name="p11644244144713"></a><a name="p11644244144713"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p38315074144812"><a name="p38315074144812"></a><a name="p38315074144812"></a>Whether a job execution object is protected</p>
<a name="ul3872134516111"></a><a name="ul3872134516111"></a><ul id="ul3872134516111"><li>true</li><li>false</li></ul>
<p id="p4213768316111"><a name="p4213768316111"></a><a name="p4213768316111"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row16657075144831"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5285514144839"><a name="p5285514144839"></a><a name="p5285514144839"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p36146066144831"><a name="p36146066144831"></a><a name="p36146066144831"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4609155144939"><a name="p4609155144939"></a><a name="p4609155144939"></a>Whether a job execution object is public</p>
<a name="ul46123066163139"></a><a name="ul46123066163139"></a><ul id="ul46123066163139"><li>true</li><li>false</li></ul>
<p id="p2174695163139"><a name="p2174695163139"></a><a name="p2174695163139"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row21026887144831"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p27934653144839"><a name="p27934653144839"></a><a name="p27934653144839"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p35577089144831"><a name="p35577089144831"></a><a name="p35577089144831"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p18799330153318"><a name="p18799330153318"></a><a name="p18799330153318"></a>Key-value pair set for saving job running configurations</p>
<p id="p4630887144939"><a name="p4630887144939"></a><a name="p4630887144939"></a>For details, see <a href="#table2159451151623">Table 3</a>.</p>
</td>
</tr>
<tr id="row65803519144414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p30376291144839"><a name="p30376291144839"></a><a name="p30376291144839"></a>data_source_urls</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52405738144713"><a name="p52405738144713"></a><a name="p52405738144713"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20473823144939"><a name="p20473823144939"></a><a name="p20473823144939"></a>Data source URL of a job execution object</p>
</td>
</tr>
<tr id="row42012596144424"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p65500602144839"><a name="p65500602144839"></a><a name="p65500602144839"></a>Id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32531313144713"><a name="p32531313144713"></a><a name="p32531313144713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p27249228144939"><a name="p27249228144939"></a><a name="p27249228144939"></a>Job execution object ID</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **job\_configs**  parameter description

<a name="table2159451151623"></a>
<table><thead align="left"><tr id="row39264552151623"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p26312167151623"><a name="p26312167151623"></a><a name="p26312167151623"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p30132362151623"><a name="p30132362151623"></a><a name="p30132362151623"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p24802238151623"><a name="p24802238151623"></a><a name="p24802238151623"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62824255151623"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6619242151712"><a name="p6619242151712"></a><a name="p6619242151712"></a>configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p54007068151623"><a name="p54007068151623"></a><a name="p54007068151623"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60121498151741"><a name="p60121498151741"></a><a name="p60121498151741"></a>Key-value pair set configured for a job</p>
</td>
</tr>
<tr id="row45358292151623"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p60698656151712"><a name="p60698656151712"></a><a name="p60698656151712"></a>args</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20654414151623"><a name="p20654414151623"></a><a name="p20654414151623"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6484022151741"><a name="p6484022151741"></a><a name="p6484022151741"></a>List of arguments</p>
</td>
</tr>
<tr id="row24682943151623"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24579100151712"><a name="p24579100151712"></a><a name="p24579100151712"></a>params</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p26950389151623"><a name="p26950389151623"></a><a name="p26950389151623"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p29231764151741"><a name="p29231764151741"></a><a name="p29231764151741"></a>Key-value pair set for running a job</p>
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
            "created_at": "2017-06-22T06:23:51",
            "updated_at": "2017-06-22T06:23:51",
            "id": "852042ea-a32c-424b-aacf-df2e6d6642b5",
            "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
            "job_id": "",
            "start_time": "2017-06-22T06:23:51",
            "end_time": null,
            "cluster_id": "33dff020-7f96-4270-9c3a-88b99627f6e2",
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

[Table 4](#table1584477916050)  describes the status code of this API.

**Table  4**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job execution object details are queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

