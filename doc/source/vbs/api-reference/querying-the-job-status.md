# Querying the Job Status<a name="EN-US_TOPIC_0020237251"></a>

## Function<a name="section18389930"></a>

This interface is used to query the execution status of a job, such as VBS backup creation, VBS backup deletion, and VBS backup-based disk restoration.

## URI<a name="section31291646"></a>

-   URI format

    GET /v1/\{project\_id\}/jobs/\{job\_id\}

-   Parameter description

    <a name="table57434139"></a>
    <table><thead align="left"><tr id="row461342"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p27598869"><a name="p27598869"></a><a name="p27598869"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20915929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p16468652"><a name="p16468652"></a><a name="p16468652"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row50048984"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p27435897"><a name="p27435897"></a><a name="p27435897"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p7715150"><a name="p7715150"></a><a name="p7715150"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p20947391"><a name="p20947391"></a><a name="p20947391"></a>Job ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13189358"></a>

None

## Response<a name="section51595365"></a>

-   Parameter description

    <a name="table50477085103826"></a>
    <table><thead align="left"><tr id="row25227453103826"><th class="cellrowborder" valign="top" width="22.439999999999998%" id="mcps1.1.4.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.4.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.17%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45296477103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p45135991103826"><a name="p45135991103826"></a><a name="p45135991103826"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p32136637103826"><a name="p32136637103826"></a><a name="p32136637103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p59539696103826"><a name="p59539696103826"></a><a name="p59539696103826"></a>Job status</p>
    <a name="ul66095222103826"></a><a name="ul66095222103826"></a><ul id="ul66095222103826"><li><strong id="b1653322818304"><a name="b1653322818304"></a><a name="b1653322818304"></a>SUCCESS</strong>: The job is successfully executed.</li><li><strong id="b620064018304"><a name="b620064018304"></a><a name="b620064018304"></a>RUNNING</strong>: The job is in progress.</li><li><strong id="b46231590154042"><a name="b46231590154042"></a><a name="b46231590154042"></a>FAIL</strong>: The job failed.</li><li><strong id="b1356920618304"><a name="b1356920618304"></a><a name="b1356920618304"></a>INIT</strong>: The job is being initialized.</li></ul>
    </td>
    </tr>
    <tr id="row6605554103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p65287884103826"><a name="p65287884103826"></a><a name="p65287884103826"></a>entities</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p53827242103826"><a name="p53827242103826"></a><a name="p53827242103826"></a>map&lt;string, string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p33695892103826"><a name="p33695892103826"></a><a name="p33695892103826"></a>Response to the job. Each type of job has different contents.</p>
    </td>
    </tr>
    <tr id="row34827575103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p2461296103826"><a name="p2461296103826"></a><a name="p2461296103826"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p65147249103826"><a name="p65147249103826"></a><a name="p65147249103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p14748653103826"><a name="p14748653103826"></a><a name="p14748653103826"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row65629019103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p14350333103826"><a name="p14350333103826"></a><a name="p14350333103826"></a>job_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p21526348103826"><a name="p21526348103826"></a><a name="p21526348103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p37322255103826"><a name="p37322255103826"></a><a name="p37322255103826"></a>Job type</p>
    </td>
    </tr>
    <tr id="row355977103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p28834158103826"><a name="p28834158103826"></a><a name="p28834158103826"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p53865476103826"><a name="p53865476103826"></a><a name="p53865476103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p16114017103826"><a name="p16114017103826"></a><a name="p16114017103826"></a>Time when the job started</p>
    </td>
    </tr>
    <tr id="row10808433103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p3067843103826"><a name="p3067843103826"></a><a name="p3067843103826"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p47168746103826"><a name="p47168746103826"></a><a name="p47168746103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p35176150103826"><a name="p35176150103826"></a><a name="p35176150103826"></a>Time when the job finished</p>
    </td>
    </tr>
    <tr id="row48149899103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p7827781103826"><a name="p7827781103826"></a><a name="p7827781103826"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p30070552103826"><a name="p30070552103826"></a><a name="p30070552103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p59941926103826"><a name="p59941926103826"></a><a name="p59941926103826"></a>Error code returned after the job execution fails</p>
    </td>
    </tr>
    <tr id="row2606426103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p9793990103826"><a name="p9793990103826"></a><a name="p9793990103826"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p55115693103826"><a name="p55115693103826"></a><a name="p55115693103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p31507474103826"><a name="p31507474103826"></a><a name="p31507474103826"></a>Cause of the execution failure</p>
    </td>
    </tr>
    <tr id="row15131815103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p17717469103826"><a name="p17717469103826"></a><a name="p17717469103826"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p25828884103826"><a name="p25828884103826"></a><a name="p25828884103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p13428899103826"><a name="p13428899103826"></a><a name="p13428899103826"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row53751233103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p58882605103826"><a name="p58882605103826"></a><a name="p58882605103826"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p4761661103826"><a name="p4761661103826"></a><a name="p4761661103826"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p35637098103826"><a name="p35637098103826"></a><a name="p35637098103826"></a>Error code returned after an error occurs</p>
    <p id="p52298434103826"><a name="p52298434103826"></a><a name="p52298434103826"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row29840800103826"><td class="cellrowborder" valign="top" width="22.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p1185729103826"><a name="p1185729103826"></a><a name="p1185729103826"></a>sub_jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.4.1.2 "><p id="p28935190103826"><a name="p28935190103826"></a><a name="p28935190103826"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.17%" headers="mcps1.1.4.1.3 "><p id="p59915646103826"><a name="p59915646103826"></a><a name="p59915646103826"></a>Execution information about a sub-job. When no sub-job exists, the value of this parameter is left blank. The structure of each sub-job is similar to that of the parent job.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "status": "SUCCESS",
        "entities": {
            "bks_create_volume_name": "autobk_volume",
            "backup_id": "ba5401a2-7cd2-4c01-8c0d-c936ab412d6d",
            "volume_id": "7e5fdc5a-5e36-4b22-8bcc-7f17037290cc",
            "snapshot_id": "a77a96bf-dd18-40bf-a446-fdcefc1719ec"
        },
        "job_id": "4010b39b5281d3590152874bfa3b1604",
        "job_type": "bksCreateBackup",
        "begin_time": "2016-01-28T16:14:09.466Z",
        "end_time": "2016-01-28T16:25:27.690Z",
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


## Status Codes<a name="section61705107"></a>

-   Normal

    200

-   Abnormal

    <a name="table11049312203333"></a>
    <table><thead align="left"><tr id="row18479965203333"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p20482166203333"><a name="p20482166203333"></a><a name="p20482166203333"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p48442711203333"><a name="p48442711203333"></a><a name="p48442711203333"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31545513203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5049747203333"><a name="p5049747203333"></a><a name="p5049747203333"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6376382203333"><a name="p6376382203333"></a><a name="p6376382203333"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row57387443203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17871330203333"><a name="p17871330203333"></a><a name="p17871330203333"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38291621203333"><a name="p38291621203333"></a><a name="p38291621203333"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row9080274203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64413583203333"><a name="p64413583203333"></a><a name="p64413583203333"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50117716203333"><a name="p50117716203333"></a><a name="p50117716203333"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48406266203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28593439203333"><a name="p28593439203333"></a><a name="p28593439203333"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p34367200203333"><a name="p34367200203333"></a><a name="p34367200203333"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row40869351203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22083167203333"><a name="p22083167203333"></a><a name="p22083167203333"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p43906087203333"><a name="p43906087203333"></a><a name="p43906087203333"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row59610464203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p63718308203333"><a name="p63718308203333"></a><a name="p63718308203333"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p60909324203333"><a name="p60909324203333"></a><a name="p60909324203333"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row11313009203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p43938571203333"><a name="p43938571203333"></a><a name="p43938571203333"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2254526203333"><a name="p2254526203333"></a><a name="p2254526203333"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row20290736203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p32936890203333"><a name="p32936890203333"></a><a name="p32936890203333"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50642416203333"><a name="p50642416203333"></a><a name="p50642416203333"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row53128568203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8446748203333"><a name="p8446748203333"></a><a name="p8446748203333"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p13098017203333"><a name="p13098017203333"></a><a name="p13098017203333"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row50773295203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p18996264203333"><a name="p18996264203333"></a><a name="p18996264203333"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62302421203333"><a name="p62302421203333"></a><a name="p62302421203333"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row23850883203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p52873370203333"><a name="p52873370203333"></a><a name="p52873370203333"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p54884569203333"><a name="p54884569203333"></a><a name="p54884569203333"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row24199080203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13968439203333"><a name="p13968439203333"></a><a name="p13968439203333"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p57701763203333"><a name="p57701763203333"></a><a name="p57701763203333"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row49553819203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p54436364203333"><a name="p54436364203333"></a><a name="p54436364203333"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p47269358203333"><a name="p47269358203333"></a><a name="p47269358203333"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row22771040203333"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p32514990203333"><a name="p32514990203333"></a><a name="p32514990203333"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16468544203333"><a name="p16468544203333"></a><a name="p16468544203333"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

