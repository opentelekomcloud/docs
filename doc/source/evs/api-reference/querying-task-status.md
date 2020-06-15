# Querying Task Status<a name="evs_04_0054"></a>

## Function<a name="section48616240"></a>

This API is used to query the execution status of tasks, such as the status of disk creation, capacity expansion, and deletion.

## URI<a name="section34892981"></a>

-   URI format

    GET /v1/\{project\_id\}/jobs/\{job\_id\}

-   Parameter description

    <a name="table64553311"></a>
    <table><thead align="left"><tr id="row24013807"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p66070243"><a name="p66070243"></a><a name="p66070243"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.2"><p id="p50089467"><a name="p50089467"></a><a name="p50089467"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.620000000000005%" id="mcps1.1.4.1.3"><p id="p188321746194612"><a name="p188321746194612"></a><a name="p188321746194612"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4890297"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p60569775"><a name="p60569775"></a><a name="p60569775"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p7204713"><a name="p7204713"></a><a name="p7204713"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.1.4.1.3 "><p id="p46710863"><a name="p46710863"></a><a name="p46710863"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row17744591"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p28025763"><a name="p28025763"></a><a name="p28025763"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p55494360"><a name="p55494360"></a><a name="p55494360"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.1.4.1.3 "><p id="p65858198"><a name="p65858198"></a><a name="p65858198"></a>Specifies the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45601378"></a>

The following example shows how to query the status of the task whose task ID is ff808081692a62c70169b4dcf9514264.

-   Example request

    ```
     GET https://{endpoint}/v1/{project_id}/jobs/ff808081692a62c70169b4dcf9514264
    ```


## Response<a name="section7759225"></a>

-   Parameter description

    <a name="table50130391201921"></a>
    <table><thead align="left"><tr id="row66097272201921"><th class="cellrowborder" valign="top" width="20.48%" id="mcps1.1.4.1.1"><p id="p52278782201921"><a name="p52278782201921"></a><a name="p52278782201921"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.69%" id="mcps1.1.4.1.2"><p id="p2711067815824"><a name="p2711067815824"></a><a name="p2711067815824"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.830000000000005%" id="mcps1.1.4.1.3"><p id="p7687988201921"><a name="p7687988201921"></a><a name="p7687988201921"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18747316201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p42137645201921"><a name="p42137645201921"></a><a name="p42137645201921"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p4848132715824"><a name="p4848132715824"></a><a name="p4848132715824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p4804017891027"><a name="p4804017891027"></a><a name="p4804017891027"></a>Specifies the task status.</p>
    <a name="ul2970842091027"></a><a name="ul2970842091027"></a><ul id="ul2970842091027"><li><strong>SUCCESS</strong>: The task is successfully executed.</li><li><strong>RUNNING</strong>: The task is in progress.</li><li><strong>FAIL</strong>: The task fails.</li><li><strong>INIT</strong>: The task is being initialized.</li></ul>
    </td>
    </tr>
    <tr id="row57564514201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p32214083201921"><a name="p32214083201921"></a><a name="p32214083201921"></a>entities</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p3467338415824"><a name="p3467338415824"></a><a name="p3467338415824"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p1736414177101"><a name="p1736414177101"></a><a name="p1736414177101"></a>Specifies the task response information. For details, see <a href="#li134182540818">Parameter in the entities field</a>.</p>
    <p id="p30792195201921"><a name="p30792195201921"></a><a name="p30792195201921"></a>The contents for each type of task are different.</p>
    </td>
    </tr>
    <tr id="row8694306201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p33150149201921"><a name="p33150149201921"></a><a name="p33150149201921"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p5708068115824"><a name="p5708068115824"></a><a name="p5708068115824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p65414495201921"><a name="p65414495201921"></a><a name="p65414495201921"></a>Specifies the task ID.</p>
    </td>
    </tr>
    <tr id="row51859545201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p39873610201921"><a name="p39873610201921"></a><a name="p39873610201921"></a>job_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p6013244315824"><a name="p6013244315824"></a><a name="p6013244315824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p20403760201921"><a name="p20403760201921"></a><a name="p20403760201921"></a>Specifies the task type.</p>
    <a name="ul15245145655114"></a><a name="ul15245145655114"></a><ul id="ul15245145655114"><li><strong id="b842352706203022"><a name="b842352706203022"></a><a name="b842352706203022"></a>createVolume</strong>: creates a disk.</li><li><strong id="b842352706203040"><a name="b842352706203040"></a><a name="b842352706203040"></a>batchCreateVolume</strong>: batch creates disks.</li><li><strong id="b842352706203121"><a name="b842352706203121"></a><a name="b842352706203121"></a>deleteVolume</strong>: deletes a disk.</li><li><strong id="b842352706203137"><a name="b842352706203137"></a><a name="b842352706203137"></a>extendVolume</strong>: expands the disk capacity.</li><li><strong id="b84235270620324"><a name="b84235270620324"></a><a name="b84235270620324"></a>bulkDeleteVolume</strong>: batch deletes disks.</li><li><strong id="b842352706203238"><a name="b842352706203238"></a><a name="b842352706203238"></a>deleteSingleVolume</strong>: deletes disks one by one during a batch deletion.</li></ul>
    </td>
    </tr>
    <tr id="row49416119201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p43282735201921"><a name="p43282735201921"></a><a name="p43282735201921"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p3888970115824"><a name="p3888970115824"></a><a name="p3888970115824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p40422711201921"><a name="p40422711201921"></a><a name="p40422711201921"></a>Specifies the time when the task was started.</p>
    <p id="p221831420710"><a name="p221831420710"></a><a name="p221831420710"></a>Time format: YYYY-MM-DDTHH:MM:SS.SSS'Z'</p>
    </td>
    </tr>
    <tr id="row28260084201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p7365468201921"><a name="p7365468201921"></a><a name="p7365468201921"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p6305809615824"><a name="p6305809615824"></a><a name="p6305809615824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p6457786201921"><a name="p6457786201921"></a><a name="p6457786201921"></a>Specifies the time when the task finished.</p>
    <p id="p5536657812"><a name="p5536657812"></a><a name="p5536657812"></a>Time format: YYYY-MM-DDTHH:MM:SS.SSS'Z'</p>
    </td>
    </tr>
    <tr id="row58120078201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p10105857201921"><a name="p10105857201921"></a><a name="p10105857201921"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p743216415824"><a name="p743216415824"></a><a name="p743216415824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p971080201921"><a name="p971080201921"></a><a name="p971080201921"></a>Specifies the returned error code when the task execution fails.</p>
    </td>
    </tr>
    <tr id="row8739724201921"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p36829011201921"><a name="p36829011201921"></a><a name="p36829011201921"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p6513437515824"><a name="p6513437515824"></a><a name="p6513437515824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p43235704201921"><a name="p43235704201921"></a><a name="p43235704201921"></a>Specifies the cause of the task execution failure.</p>
    </td>
    </tr>
    <tr id="row208351118145015"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.830000000000005%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li134182540818"></a>Parameter in the  **entities**  field

    <a name="table165761957483"></a>
    <table><thead align="left"><tr id="row1957611571285"><th class="cellrowborder" valign="top" width="20.23202320232023%" id="mcps1.1.4.1.1"><p id="p1276131916910"><a name="p1276131916910"></a><a name="p1276131916910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.972197219721973%" id="mcps1.1.4.1.2"><p id="p14276101916912"><a name="p14276101916912"></a><a name="p14276101916912"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.795779577957795%" id="mcps1.1.4.1.3"><p id="p627610191596"><a name="p627610191596"></a><a name="p627610191596"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row135768571586"><td class="cellrowborder" valign="top" width="20.23202320232023%" headers="mcps1.1.4.1.1 "><p id="p239893649137"><a name="p239893649137"></a><a name="p239893649137"></a>sub_jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.972197219721973%" headers="mcps1.1.4.1.2 "><p id="p640903559137"><a name="p640903559137"></a><a name="p640903559137"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.795779577957795%" headers="mcps1.1.4.1.3 "><p id="p597890789137"><a name="p597890789137"></a><a name="p597890789137"></a>Specifies the execution information of a sub-task. When no sub-task exists, the value of this parameter is left blank. The structure of each sub-task is similar to that of the parent task.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "status": "RUNNING", 
        "entities": {
            "volume_id": "bdf1bb37-f20f-4266-9a04-f43e0a127376"
        }, 
        "job_id": "4010a32d535527910153552b492c0002", 
        "job_type": "createVolume", 
        "begin_time": "2016-03-08T07:40:13.219Z", 
        "end_time": "", 
        "error_code": null, 
        "fail_reason": null
    }
    ```

    or

    ```
    {
        "status": "SUCCESS", 
        "entities": {
            "sub_jobs": [
                {
                    "status": "SUCCESS", 
                    "entities": {
                        "volume_id": "0b549095-4937-4849-8e4c-52aa027d64f7"
                    }, 
                    "job_id": "21917a8d52a19b040152a9f2f2e50041", 
                    "job_type": "createVolume", 
                    "begin_time": "2016-02-04T01:43:37.445Z", 
                    "end_time": "2016-02-04T01:44:02.239Z", 
                    "error_code": null, 
                    "fail_reason": null
                }, 
                {
                    "status": "SUCCESS", 
                    "entities": {
                        "volume_id": "e7bca1a2-d3ed-434f-86f4-a1f11aa80072"
                    }, 
                    "job_id": "21917a8d52a19b040152a9f2f2f60042", 
                    "job_type": "createVolume", 
                    "begin_time": "2016-02-04T01:43:37.462Z", 
                    "end_time": "2016-02-04T01:44:02.245Z", 
                    "error_code": null, 
                    "fail_reason": null
                }
            ]
        }, 
        "job_id": "21917a8d52a19b040152a9f2f1eb003e", 
        "job_type": "batchCreateVolume", 
        "begin_time": "2016-02-04T01:43:37.193Z", 
        "end_time": "2016-02-04T01:44:08.283Z", 
        "error_code": null, 
        "fail_reason": null
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


## Status Codes<a name="section2724161"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

