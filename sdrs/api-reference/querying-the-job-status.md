# Querying the Job Status<a name="sdrs_05_0101"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query the execution status of a job.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>After a job, such as creating or deleting a protection group, creating or deleting a protected instance, and creating or deleting a replication pair, is issued,  **job\_id**  is returned, based on which you can query the execution status of the job.  

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/jobs/\{job\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p25151854"><a name="en-us_topic_0079693002_p25151854"></a><a name="en-us_topic_0079693002_p25151854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p1556805116115"><a name="en-us_topic_0079693002_p1556805116115"></a><a name="en-us_topic_0079693002_p1556805116115"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.3"><p id="p553795612375"><a name="p553795612375"></a><a name="p553795612375"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2565159161120"><a name="en-us_topic_0079693002_p2565159161120"></a><a name="en-us_topic_0079693002_p2565159161120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693002_p10190321"><a name="en-us_topic_0079693002_p10190321"></a><a name="en-us_topic_0079693002_p10190321"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p60774950161114"><a name="en-us_topic_0079693002_p60774950161114"></a><a name="en-us_topic_0079693002_p60774950161114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p721813347387"><a name="p721813347387"></a><a name="p721813347387"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p15928101713314"><a name="p15928101713314"></a><a name="p15928101713314"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row91209154712"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p1212115134718"><a name="p1212115134718"></a><a name="p1212115134718"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="p191216112478"><a name="p191216112478"></a><a name="p191216112478"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p1921893473817"><a name="p1921893473817"></a><a name="p1921893473817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p560514594492"><a name="p560514594492"></a><a name="p560514594492"></a>Specifies the job ID.</p>
    <p id="p265974419244"><a name="p265974419244"></a><a name="p265974419244"></a>Specifies the returned parameter when the asynchronous API command is issued. For details, see the description in <a href="#en-us_topic_0079693002_section34649765">Function</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Request parameters

    None

-   Example request

    GET https://\{endpoint\}/v1/\{project\_id\}/jobs/0000000062db92d70162db9d200f000a


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.1"><p id="p56078010555"><a name="p56078010555"></a><a name="p56078010555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.2"><p id="p961219016552"><a name="p961219016552"></a><a name="p961219016552"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="p186139012557"><a name="p186139012557"></a><a name="p186139012557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p261990195515"><a name="p261990195515"></a><a name="p261990195515"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p5556811164115"><a name="p5556811164115"></a><a name="p5556811164115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p12625170165512"><a name="p12625170165512"></a><a name="p12625170165512"></a>Specifies the job status.</p>
    <a name="ul1762511012556"></a><a name="ul1762511012556"></a><ul id="ul1762511012556"><li><strong id="b184471053163215"><a name="b184471053163215"></a><a name="b184471053163215"></a>SUCCESS</strong>: The job was successfully executed.</li><li><strong id="b27241123336"><a name="b27241123336"></a><a name="b27241123336"></a>RUNNING</strong>: The job is in progress.</li><li><strong id="b46231590154042"><a name="b46231590154042"></a><a name="b46231590154042"></a>FAIL</strong>: The job failed.</li><li><strong id="b1264861493318"><a name="b1264861493318"></a><a name="b1264861493318"></a>INIT</strong>: The job is being initialized.</li></ul>
    </td>
    </tr>
    <tr id="row166368013553"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p1663817020550"><a name="p1663817020550"></a><a name="p1663817020550"></a>entities</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p35586114418"><a name="p35586114418"></a><a name="p35586114418"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p15224935105313"><a name="p15224935105313"></a><a name="p15224935105313"></a>Specifies the job object.</p>
    <p id="p1164518018558"><a name="p1164518018558"></a><a name="p1164518018558"></a>The value of this parameter varies depending on the job type. If the job is a protection group-related operation, the value will be <strong id="b436464913486"><a name="b436464913486"></a><a name="b436464913486"></a>server_group_id</strong>. If a subjob is available, details about the subjob are displayed.</p>
    <p id="p107581428152713"><a name="p107581428152713"></a><a name="p107581428152713"></a>For details, see <a href="#table503353570">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row11646110135510"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p06481100551"><a name="p06481100551"></a><a name="p06481100551"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p16558171194112"><a name="p16558171194112"></a><a name="p16558171194112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p1665417018555"><a name="p1665417018555"></a><a name="p1665417018555"></a>Specifies the job ID.</p>
    <p id="p040832117517"><a name="p040832117517"></a><a name="p040832117517"></a>For details, see the description in <a href="#en-us_topic_0079693002_section34649765">Function</a>.</p>
    </td>
    </tr>
    <tr id="row6655401556"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p18657190125511"><a name="p18657190125511"></a><a name="p18657190125511"></a>job_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p1755816116411"><a name="p1755816116411"></a><a name="p1755816116411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p36630014558"><a name="p36630014558"></a><a name="p36630014558"></a>Specifies the job type.</p>
    <a name="ul127879407557"></a><a name="ul127879407557"></a><ul id="ul127879407557"><li><strong id="b10381674414"><a name="b10381674414"></a><a name="b10381674414"></a>createProtectionGroupNoCG</strong>: Creates a protection group.</li><li><strong id="b0162723174118"><a name="b0162723174118"></a><a name="b0162723174118"></a>deleteProtectionGroupNoCG</strong>: Deletes a protection group.</li><li><strong id="b1314695574213"><a name="b1314695574213"></a><a name="b1314695574213"></a>startProtectionGroupNoCG</strong>: Enables protection for a protection group.</li><li><strong id="b3149142294616"><a name="b3149142294616"></a><a name="b3149142294616"></a>reprotectProtectionGroupNoCG</strong>: Enables protection again for a protection group.</li><li><strong id="b5906857125113"><a name="b5906857125113"></a><a name="b5906857125113"></a>stopProtectionGroupNoCG</strong>: Disables protection for a protection group.</li><li><strong id="b14542173745213"><a name="b14542173745213"></a><a name="b14542173745213"></a>failoverProtectionGroupNoCG</strong>: Performs a failover for a protection group.</li><li><strong id="b1020015418585"><a name="b1020015418585"></a><a name="b1020015418585"></a>reverseProtectionGroupNoCG</strong>: Performs a planned failover for a protection group.</li><li><strong id="b1695775135917"><a name="b1695775135917"></a><a name="b1695775135917"></a>createProtectedInstanceNoCG</strong>: Creates a protected instance.</li><li><strong id="b5868163612114"><a name="b5868163612114"></a><a name="b5868163612114"></a>deleteProtectedInstanceNoCG</strong>: Deletes a protected instance.</li><li><strong id="b1665811571817"><a name="b1665811571817"></a><a name="b1665811571817"></a>attachReplicationPairNew</strong>: Attaches a replication pair to a protected instance.</li><li><strong id="b1464372173116"><a name="b1464372173116"></a><a name="b1464372173116"></a>detachReplicationPairNew</strong>: Detaches a replication pair from a protected instance.</li><li><strong id="b94791923103115"><a name="b94791923103115"></a><a name="b94791923103115"></a>addNicNew</strong>: Adds a NIC to a protected instance.</li><li><strong id="b1312411575325"><a name="b1312411575325"></a><a name="b1312411575325"></a>deleteNicNew</strong>: Deletes a NIC from a protected instance.</li><li><strong id="b15519041163410"><a name="b15519041163410"></a><a name="b15519041163410"></a>resizeProtectedInstanceNew</strong>: Modifies the specifications of a protected instance.</li><li><strong id="b206051150153816"><a name="b206051150153816"></a><a name="b206051150153816"></a>createReplicationPairNoCG</strong>: Creates a replication pair.</li><li><strong id="b6280202417395"><a name="b6280202417395"></a><a name="b6280202417395"></a>deleteReplicationPairNoCG</strong>: Deletes a replication pair.</li><li><strong id="b35918410398"><a name="b35918410398"></a><a name="b35918410398"></a>expandReplicationPairNew</strong>: Expands the capacity of a replication pair.</li><li><strong id="b899921114418"><a name="b899921114418"></a><a name="b899921114418"></a>createDisasterRecoveryDrill</strong>: Creates a DR drill.</li><li><strong id="b1980813476440"><a name="b1980813476440"></a><a name="b1980813476440"></a>deleteDisasterRecoveryDrill</strong>: Deletes a DR drill.</li></ul>
    </td>
    </tr>
    <tr id="row156647095510"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p156667025512"><a name="p156667025512"></a><a name="p156667025512"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p3558311194119"><a name="p3558311194119"></a><a name="p3558311194119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p178851320123117"><a name="p178851320123117"></a><a name="p178851320123117"></a>Specifies the start time.</p>
    <p id="p1867150115511"><a name="p1867150115511"></a><a name="p1867150115511"></a>The default format is as follows: "yyyy-MM-dd 'T' HH:mm:ss.SSSZ", for example, <strong id="b1133512190292"><a name="b1133512190292"></a><a name="b1133512190292"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row7672100175511"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p166749095519"><a name="p166749095519"></a><a name="p166749095519"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p1955819111411"><a name="p1955819111411"></a><a name="p1955819111411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p075417312316"><a name="p075417312316"></a><a name="p075417312316"></a>Specifies the end time.</p>
    <p id="p20679150115516"><a name="p20679150115516"></a><a name="p20679150115516"></a>The default format is as follows: "yyyy-MM-dd 'T' HH:mm:ss.SSSZ", for example, <strong id="b1099992715294"><a name="b1099992715294"></a><a name="b1099992715294"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row19681100205515"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p1368312010554"><a name="p1368312010554"></a><a name="p1368312010554"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p135587111415"><a name="p135587111415"></a><a name="p135587111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p18690103557"><a name="p18690103557"></a><a name="p18690103557"></a>Specifies the error code returned upon a job execution failure.</p>
    <p id="p43101514454"><a name="p43101514454"></a><a name="p43101514454"></a>For details, see <a href="error-code-description.md">Error Code Description</a>.</p>
    </td>
    </tr>
    <tr id="row156911205555"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p1269312045516"><a name="p1269312045516"></a><a name="p1269312045516"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p155801114116"><a name="p155801114116"></a><a name="p155801114116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p76991106554"><a name="p76991106554"></a><a name="p76991106554"></a>Specifies the cause of a job execution failure.</p>
    <p id="p529416112003"><a name="p529416112003"></a><a name="p529416112003"></a>For details, see <a href="error-code-description.md">Error Code Description</a>.</p>
    </td>
    </tr>
    <tr id="row6699110115516"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p19701002556"><a name="p19701002556"></a><a name="p19701002556"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p055891174110"><a name="p055891174110"></a><a name="p055891174110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p77073010553"><a name="p77073010553"></a><a name="p77073010553"></a>Specifies the error message returned when an error occurs.</p>
    <p id="p20141415287"><a name="p20141415287"></a><a name="p20141415287"></a>For details, see the abnormal returned values in <a href="#en-us_topic_0079693002_section60507121">Returned Values</a>.</p>
    </td>
    </tr>
    <tr id="row37089012553"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p171060155514"><a name="p171060155514"></a><a name="p171060155514"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.2 "><p id="p65582011144113"><a name="p65582011144113"></a><a name="p65582011144113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p1771615045517"><a name="p1771615045517"></a><a name="p1771615045517"></a>Specifies the error code returned when an error occurs.</p>
    <p id="p143705412551"><a name="p143705412551"></a><a name="p143705412551"></a>For details, see the abnormal returned values in <a href="#en-us_topic_0079693002_section60507121">Returned Values</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **entities**  field description

    <a name="table503353570"></a>
    <table><thead align="left"><tr id="row131163505710"><th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.4.1.1"><p id="p8131435155711"><a name="p8131435155711"></a><a name="p8131435155711"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.4.1.2"><p id="p6251035195718"><a name="p6251035195718"></a><a name="p6251035195718"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.2.4.1.3"><p id="p1727173517574"><a name="p1727173517574"></a><a name="p1727173517574"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1829133585715"><td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p13393545711"><a name="p13393545711"></a><a name="p13393545711"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.4.1.2 "><p id="p113643525715"><a name="p113643525715"></a><a name="p113643525715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.2.4.1.3 "><p id="p13896133075915"><a name="p13896133075915"></a><a name="p13896133075915"></a>Specifies the ID of the protection group being queried.</p>
    </td>
    </tr>
    <tr id="row951117394485"><td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p239893649137"><a name="p239893649137"></a><a name="p239893649137"></a>sub_jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.4.1.2 "><p id="p640903559137"><a name="p640903559137"></a><a name="p640903559137"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.2.4.1.3 "><p id="p597890789137"><a name="p597890789137"></a><a name="p597890789137"></a>Specifies the execution information of a subjob. When no subjob exists, the value of this parameter is left empty. The structure of each subjob is similar to that of the parent job.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
          "status": "SUCCESS",  
          "entities": {  
              "server_group_id": "a59d008e-4bad-4bf3-9b17-6cc25e7da483"  
          },  
          "job_id": "0000000062db92d70162db9d200f000a",  
          "job_type": "createProtectionGroupNoCG",  
          "begin_time": "2018-04-19T01:55:30.443Z",  
          "end_time": "2018-04-19T01:55:45.493Z",  
          "error_code": null,  
          "fail_reason": null  
      }
    ```

    Or

    ```
    {
        "job_id": "ff8080826b45d4a5016b5036242c0025",
        "job_type": "stopProtectionGroupNoCG",
        "begin_time": "2019-06-13T09:40:53.930Z",
        "end_time": "2019-06-13T09:41:01.946Z",
        "status": "SUCCESS",
        "error_code": null,
        "fail_reason": null,
        "entities": {
            "sub_jobs": [
                {
                    "job_id": "ff8080826b45d4a5016b50362868002a",
                    "job_type": "stopProtectionGroupRepNoCG",
                    "begin_time": "2019-06-13T09:40:55.015Z",
                    "end_time": "2019-06-13T09:40:58.951Z",
                    "status": "SUCCESS",
                    "error_code": null,
                    "fail_reason": null,
                    "entities": {
                        "server_group_id": "1fd6903c-48f9-4772-8974-112dfbd74427"
                    }
                },
                {
                    "job_id": "ff8080826b45d4a5016b50362870002b",
                    "job_type": "stopProtectionGroupRepNoCG",
                    "begin_time": "2019-06-13T09:40:55.022Z",
                    "end_time": "2019-06-13T09:40:58.952Z",
                    "status": "SUCCESS",
                    "error_code": null,
                    "fail_reason": null,
                    "entities": {
                        "server_group_id": "1fd6903c-48f9-4772-8974-112dfbd74427"
                    }
                }
            ]
        }
    }
    { 
         "error": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```


## Returned Values<a name="en-us_topic_0079693002_section60507121"></a>

-   Normal

    <a name="table4315991194956"></a>
    <table><thead align="left"><tr id="row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="p1363125894956"><a name="p1363125894956"></a><a name="p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="p3039012494956"><a name="p3039012494956"></a><a name="p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="p847584694956"><a name="p847584694956"></a><a name="p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="p1545496394956"><a name="p1545496394956"></a><a name="p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table22458872203835"></a>
    <table><thead align="left"><tr id="row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p6387753203835"><a name="p6387753203835"></a><a name="p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p47646009203835"><a name="p47646009203835"></a><a name="p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p12381163203835"><a name="p12381163203835"></a><a name="p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p63350108203835"><a name="p63350108203835"></a><a name="p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p11330608203835"><a name="p11330608203835"></a><a name="p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p45364094203835"><a name="p45364094203835"></a><a name="p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p52863895203835"><a name="p52863895203835"></a><a name="p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p54117066203835"><a name="p54117066203835"></a><a name="p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p58438642203835"><a name="p58438642203835"></a><a name="p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p35909542203835"><a name="p35909542203835"></a><a name="p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5599455203835"><a name="p5599455203835"></a><a name="p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50902717203835"><a name="p50902717203835"></a><a name="p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p63988484203835"><a name="p63988484203835"></a><a name="p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p15684678203835"><a name="p15684678203835"></a><a name="p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25623884203835"><a name="p25623884203835"></a><a name="p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62268733203835"><a name="p62268733203835"></a><a name="p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28314670203835"><a name="p28314670203835"></a><a name="p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11786919203835"><a name="p11786919203835"></a><a name="p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2729702203835"><a name="p2729702203835"></a><a name="p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19779281203835"><a name="p19779281203835"></a><a name="p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57799353203835"><a name="p57799353203835"></a><a name="p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p51235984203835"><a name="p51235984203835"></a><a name="p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38504500203835"><a name="p38504500203835"></a><a name="p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31856770203835"><a name="p31856770203835"></a><a name="p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3918444203835"><a name="p3918444203835"></a><a name="p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p48958538203835"><a name="p48958538203835"></a><a name="p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55967806203835"><a name="p55967806203835"></a><a name="p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p37098455203835"><a name="p37098455203835"></a><a name="p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p67010448203835"><a name="p67010448203835"></a><a name="p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59137180203835"><a name="p59137180203835"></a><a name="p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


