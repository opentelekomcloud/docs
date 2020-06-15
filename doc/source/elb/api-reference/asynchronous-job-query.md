# Asynchronous Job Query<a name="EN-US_TOPIC_0096565998"></a>

## Function<a name="en-us_topic_0020241359_section6040545315614"></a>

This API is used to query the execution status of an asynchronous job. 

## URI<a name="en-us_topic_0020241359_section1216080715614"></a>

GET /v1.0/\{project\_id\}/jobs/\{job\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020241359_table3389532515614"></a>
<table><thead align="left"><tr id="en-us_topic_0020241359_row413948215614"><th class="cellrowborder" valign="top" width="18.98189818981898%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020241359_p6686266415614"><a name="en-us_topic_0020241359_p6686266415614"></a><a name="en-us_topic_0020241359_p6686266415614"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.372237223722376%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020241359_p4716671415614"><a name="en-us_topic_0020241359_p4716671415614"></a><a name="en-us_topic_0020241359_p4716671415614"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.171917191719174%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020241359_p55120590194459"><a name="en-us_topic_0020241359_p55120590194459"></a><a name="en-us_topic_0020241359_p55120590194459"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.473947394739476%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020241359_p6240751315614"><a name="en-us_topic_0020241359_p6240751315614"></a><a name="en-us_topic_0020241359_p6240751315614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020241359_row2184378815614"><td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020241359_p2451641215614"><a name="en-us_topic_0020241359_p2451641215614"></a><a name="en-us_topic_0020241359_p2451641215614"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.372237223722376%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020241359_p3967233615614"><a name="en-us_topic_0020241359_p3967233615614"></a><a name="en-us_topic_0020241359_p3967233615614"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.171917191719174%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020241359_p63633616194459"><a name="en-us_topic_0020241359_p63633616194459"></a><a name="en-us_topic_0020241359_p63633616194459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.473947394739476%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020241359_p5934264115614"><a name="en-us_topic_0020241359_p5934264115614"></a><a name="en-us_topic_0020241359_p5934264115614"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row6432172115614"><td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020241359_p4267691915614"><a name="en-us_topic_0020241359_p4267691915614"></a><a name="en-us_topic_0020241359_p4267691915614"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.372237223722376%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020241359_p3427845415614"><a name="en-us_topic_0020241359_p3427845415614"></a><a name="en-us_topic_0020241359_p3427845415614"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.171917191719174%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020241359_p5001652194441"><a name="en-us_topic_0020241359_p5001652194441"></a><a name="en-us_topic_0020241359_p5001652194441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.473947394739476%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020241359_p2509142215614"><a name="en-us_topic_0020241359_p2509142215614"></a><a name="en-us_topic_0020241359_p2509142215614"></a>Specifies the unique ID assigned to the job for querying the execution status in Combined API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020241359_section2449620815614"></a>

None

## Response<a name="en-us_topic_0020241359_section1217224715614"></a>

**Table  2**  Parameter description

<a name="en-us_topic_0020241359_table2476666015499"></a>
<table><thead align="left"><tr id="en-us_topic_0020241359_row2427028715499"><th class="cellrowborder" valign="top" width="20.36%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020241359_p1973620315499"><a name="en-us_topic_0020241359_p1973620315499"></a><a name="en-us_topic_0020241359_p1973620315499"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020241359_p2498337919458"><a name="en-us_topic_0020241359_p2498337919458"></a><a name="en-us_topic_0020241359_p2498337919458"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.96%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020241359_p3623457015499"><a name="en-us_topic_0020241359_p3623457015499"></a><a name="en-us_topic_0020241359_p3623457015499"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020241359_row4931906815499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p3542159515499"><a name="en-us_topic_0020241359_p3542159515499"></a><a name="en-us_topic_0020241359_p3542159515499"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p2002722619458"><a name="en-us_topic_0020241359_p2002722619458"></a><a name="en-us_topic_0020241359_p2002722619458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p309164615499"><a name="en-us_topic_0020241359_p309164615499"></a><a name="en-us_topic_0020241359_p309164615499"></a>Specifies the job execution status.</p>
<p id="en-us_topic_0020241359_p2782481615499"><a name="en-us_topic_0020241359_p2782481615499"></a><a name="en-us_topic_0020241359_p2782481615499"></a><strong id="en-us_topic_0020241359_b1114906721483"><a name="en-us_topic_0020241359_b1114906721483"></a><a name="en-us_topic_0020241359_b1114906721483"></a>SUCCESS</strong>: indicates that the job was successfully executed.</p>
<p id="en-us_topic_0020241359_p4909675415499"><a name="en-us_topic_0020241359_p4909675415499"></a><a name="en-us_topic_0020241359_p4909675415499"></a><strong id="en-us_topic_0020241359_b2992161921483"><a name="en-us_topic_0020241359_b2992161921483"></a><a name="en-us_topic_0020241359_b2992161921483"></a>FAIL</strong>: indicates that the job failed.</p>
<p id="en-us_topic_0020241359_p3921760515499"><a name="en-us_topic_0020241359_p3921760515499"></a><a name="en-us_topic_0020241359_p3921760515499"></a><strong>RUNNIGN</strong>: indicates that the job is in progress.</p>
<p id="en-us_topic_0020241359_p1741413115499"><a name="en-us_topic_0020241359_p1741413115499"></a><a name="en-us_topic_0020241359_p1741413115499"></a><strong>INIT</strong>: indicates that the job is being initialized.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row2250945115499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p1132624915499"><a name="en-us_topic_0020241359_p1132624915499"></a><a name="en-us_topic_0020241359_p1132624915499"></a>entities</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p10909742194432"><a name="en-us_topic_0020241359_p10909742194432"></a><a name="en-us_topic_0020241359_p10909742194432"></a><em id="en-us_topic_0020241359_i27842831103443"><a name="en-us_topic_0020241359_i27842831103443"></a><a name="en-us_topic_0020241359_i27842831103443"></a>Dictionary data structure</em></p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p2201371215499"><a name="en-us_topic_0020241359_p2201371215499"></a><a name="en-us_topic_0020241359_p2201371215499"></a>Specifies the resource information or error information. The ELB resource ID is used as an example in the response example.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row6390568215499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p897776915499"><a name="en-us_topic_0020241359_p897776915499"></a><a name="en-us_topic_0020241359_p897776915499"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p11273949194432"><a name="en-us_topic_0020241359_p11273949194432"></a><a name="en-us_topic_0020241359_p11273949194432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p4867422915499"><a name="en-us_topic_0020241359_p4867422915499"></a><a name="en-us_topic_0020241359_p4867422915499"></a>Specifies the unique ID assigned to the job for querying the execution status in Combined API.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row3541488215499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p5003322815499"><a name="en-us_topic_0020241359_p5003322815499"></a><a name="en-us_topic_0020241359_p5003322815499"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p40774709194432"><a name="en-us_topic_0020241359_p40774709194432"></a><a name="en-us_topic_0020241359_p40774709194432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p3856053015499"><a name="en-us_topic_0020241359_p3856053015499"></a><a name="en-us_topic_0020241359_p3856053015499"></a>Specifies the task type.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row1150045115499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p5912132115499"><a name="en-us_topic_0020241359_p5912132115499"></a><a name="en-us_topic_0020241359_p5912132115499"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p14417117194432"><a name="en-us_topic_0020241359_p14417117194432"></a><a name="en-us_topic_0020241359_p14417117194432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p575932415499"><a name="en-us_topic_0020241359_p575932415499"></a><a name="en-us_topic_0020241359_p575932415499"></a>Specifies the error code.</p>
</td>
</tr>
<tr id="en-us_topic_0020241359_row5183392215499"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020241359_p3779817615499"><a name="en-us_topic_0020241359_p3779817615499"></a><a name="en-us_topic_0020241359_p3779817615499"></a>fail_reason</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020241359_p26935805194432"><a name="en-us_topic_0020241359_p26935805194432"></a><a name="en-us_topic_0020241359_p26935805194432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.96%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020241359_p2658139615499"><a name="en-us_topic_0020241359_p2658139615499"></a><a name="en-us_topic_0020241359_p2658139615499"></a>Specifies the cause of an error.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section132942109315"></a>

-   Example request

    None


-   Example response

    ```
    {
        "status":"RUNNING",
        "entities":
        {"elb_id":"ea3e5715b68850a747ec41f335625c08"},
    "job_id":"4010b39b4fd3d5ff014fd943bac41619",
        "job_type":"deleteELB",
    "begin_time":"2015-09-17T03:05:38.756Z",
    "end_time":"",
    "error_code":null,
        "fail_reason":null
    }
    ```


## Returned Values<a name="en-us_topic_0020241359_section665754015614"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020241359_table44094683151636"></a>
    <table><thead align="left"><tr id="en-us_topic_0020241359_row57269861151636"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0020241359_p8347144151636"><a name="en-us_topic_0020241359_p8347144151636"></a><a name="en-us_topic_0020241359_p8347144151636"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0020241359_p5030035151636"><a name="en-us_topic_0020241359_p5030035151636"></a><a name="en-us_topic_0020241359_p5030035151636"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020241359_row4779695151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p51611011151636"><a name="en-us_topic_0020241359_p51611011151636"></a><a name="en-us_topic_0020241359_p51611011151636"></a>400 badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p19742392151636"><a name="en-us_topic_0020241359_p19742392151636"></a><a name="en-us_topic_0020241359_p19742392151636"></a>Request error</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020241359_row43463806151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p30907431151636"><a name="en-us_topic_0020241359_p30907431151636"></a><a name="en-us_topic_0020241359_p30907431151636"></a>401 unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p20473988151636"><a name="en-us_topic_0020241359_p20473988151636"></a><a name="en-us_topic_0020241359_p20473988151636"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020241359_row50048170151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p27369969151636"><a name="en-us_topic_0020241359_p27369969151636"></a><a name="en-us_topic_0020241359_p27369969151636"></a>403 userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p2375008151636"><a name="en-us_topic_0020241359_p2375008151636"></a><a name="en-us_topic_0020241359_p2375008151636"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020241359_row21375079151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p53659814151636"><a name="en-us_topic_0020241359_p53659814151636"></a><a name="en-us_topic_0020241359_p53659814151636"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p51477666151636"><a name="en-us_topic_0020241359_p51477666151636"></a><a name="en-us_topic_0020241359_p51477666151636"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020241359_row60645810151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p13363539151636"><a name="en-us_topic_0020241359_p13363539151636"></a><a name="en-us_topic_0020241359_p13363539151636"></a>500 authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p8704869151636"><a name="en-us_topic_0020241359_p8704869151636"></a><a name="en-us_topic_0020241359_p8704869151636"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020241359_row11234959151636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0020241359_p37616525151636"><a name="en-us_topic_0020241359_p37616525151636"></a><a name="en-us_topic_0020241359_p37616525151636"></a>503 serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0020241359_p27039695151636"><a name="en-us_topic_0020241359_p27039695151636"></a><a name="en-us_topic_0020241359_p27039695151636"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


