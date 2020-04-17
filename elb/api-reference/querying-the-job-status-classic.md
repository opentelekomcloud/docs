# Querying the Job Status<a name="EN-US_TOPIC_0096561527"></a>

## Function<a name="en-us_topic_0078894911_section2957267418129"></a>

This API is used to query the job status, such as the execution status of creating or deleting a load balancer.

## URI<a name="en-us_topic_0078894911_section10998726181234"></a>

GET /v1.0/\{project\_id\}/jobs/\{job\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0078894911_table60560348181313"></a>
<table><thead align="left"><tr id="en-us_topic_0078894911_row48803910181313"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0078894911_p60802653181313"><a name="en-us_topic_0078894911_p60802653181313"></a><a name="en-us_topic_0078894911_p60802653181313"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0078894911_p26067889181313"><a name="en-us_topic_0078894911_p26067889181313"></a><a name="en-us_topic_0078894911_p26067889181313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0078894911_p201141243448"><a name="en-us_topic_0078894911_p201141243448"></a><a name="en-us_topic_0078894911_p201141243448"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0078894911_p31124265181313"><a name="en-us_topic_0078894911_p31124265181313"></a><a name="en-us_topic_0078894911_p31124265181313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0078894911_row38037550181313"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p101243509202"><a name="en-us_topic_0078894911_p101243509202"></a><a name="en-us_topic_0078894911_p101243509202"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p53611261181313"><a name="en-us_topic_0078894911_p53611261181313"></a><a name="en-us_topic_0078894911_p53611261181313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894911_p511416240441"><a name="en-us_topic_0078894911_p511416240441"></a><a name="en-us_topic_0078894911_p511416240441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p47544855181313"><a name="en-us_topic_0078894911_p47544855181313"></a><a name="en-us_topic_0078894911_p47544855181313"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0078894911_row25250513181313"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p32025677181313"><a name="en-us_topic_0078894911_p32025677181313"></a><a name="en-us_topic_0078894911_p32025677181313"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p43943041181313"><a name="en-us_topic_0078894911_p43943041181313"></a><a name="en-us_topic_0078894911_p43943041181313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894911_p1114624134411"><a name="en-us_topic_0078894911_p1114624134411"></a><a name="en-us_topic_0078894911_p1114624134411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p2616598181313"><a name="en-us_topic_0078894911_p2616598181313"></a><a name="en-us_topic_0078894911_p2616598181313"></a>Specifies the job ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0078894911_section67000459181355"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0078894911_section63584406181359"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0078894911_table51081423181516"></a>
    <table><thead align="left"><tr id="en-us_topic_0078894911_row39092678181516"><th class="cellrowborder" valign="top" width="21.12%" id="mcps1.2.5.1.1"><p id="en-us_topic_0078894911_p12390336181516"><a name="en-us_topic_0078894911_p12390336181516"></a><a name="en-us_topic_0078894911_p12390336181516"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.45%" id="mcps1.2.5.1.2"><p id="en-us_topic_0078894911_p24165023181516"><a name="en-us_topic_0078894911_p24165023181516"></a><a name="en-us_topic_0078894911_p24165023181516"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.86%" id="mcps1.2.5.1.3"><p id="en-us_topic_0078894911_p64093179181516"><a name="en-us_topic_0078894911_p64093179181516"></a><a name="en-us_topic_0078894911_p64093179181516"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.57%" id="mcps1.2.5.1.4"><p id="en-us_topic_0078894911_p11209810181516"><a name="en-us_topic_0078894911_p11209810181516"></a><a name="en-us_topic_0078894911_p11209810181516"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0078894911_row35579455181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p63363596181516"><a name="en-us_topic_0078894911_p63363596181516"></a><a name="en-us_topic_0078894911_p63363596181516"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p56251495181516"><a name="en-us_topic_0078894911_p56251495181516"></a><a name="en-us_topic_0078894911_p56251495181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894911_p32177633181516"><a name="en-us_topic_0078894911_p32177633181516"></a><a name="en-us_topic_0078894911_p32177633181516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p60077253181516"><a name="en-us_topic_0078894911_p60077253181516"></a><a name="en-us_topic_0078894911_p60077253181516"></a>Specifies the job status.</p>
    <a name="en-us_topic_0078894911_ul3824373181516"></a><a name="en-us_topic_0078894911_ul3824373181516"></a><ul id="en-us_topic_0078894911_ul3824373181516"><li><strong>SUCCESS</strong>: The job was successfully executed.</li><li><strong>RUNNING</strong>: The job is in progress.</li><li><strong id="b46231590154042"><a name="b46231590154042"></a><a name="b46231590154042"></a>FAIL</strong>: The job failed.</li><li><strong>INIT</strong>: The job is being initialized.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4125700181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p65746260181516"><a name="en-us_topic_0078894911_p65746260181516"></a><a name="en-us_topic_0078894911_p65746260181516"></a>entities</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p52546942181516"><a name="en-us_topic_0078894911_p52546942181516"></a><a name="en-us_topic_0078894911_p52546942181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894911_p23846853181516"><a name="en-us_topic_0078894911_p23846853181516"></a><a name="en-us_topic_0078894911_p23846853181516"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p28443944181516"><a name="en-us_topic_0078894911_p28443944181516"></a><a name="en-us_topic_0078894911_p28443944181516"></a>Specifies the response to the job. Each type of job has different contents.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row54668911181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p66105669181516"><a name="en-us_topic_0078894911_p66105669181516"></a><a name="en-us_topic_0078894911_p66105669181516"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p61815973181516"><a name="en-us_topic_0078894911_p61815973181516"></a><a name="en-us_topic_0078894911_p61815973181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p9293135016562"><a name="p9293135016562"></a><a name="p9293135016562"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p41037953181516"><a name="en-us_topic_0078894911_p41037953181516"></a><a name="en-us_topic_0078894911_p41037953181516"></a>Specifies the job ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row33797257181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p53223326181516"><a name="en-us_topic_0078894911_p53223326181516"></a><a name="en-us_topic_0078894911_p53223326181516"></a>job_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p30827530181516"><a name="en-us_topic_0078894911_p30827530181516"></a><a name="en-us_topic_0078894911_p30827530181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p2190125385614"><a name="p2190125385614"></a><a name="p2190125385614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p14001968181516"><a name="en-us_topic_0078894911_p14001968181516"></a><a name="en-us_topic_0078894911_p14001968181516"></a>Specifies the job type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row58908852181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p6887698181516"><a name="en-us_topic_0078894911_p6887698181516"></a><a name="en-us_topic_0078894911_p6887698181516"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p25924604181516"><a name="en-us_topic_0078894911_p25924604181516"></a><a name="en-us_topic_0078894911_p25924604181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p869965416566"><a name="p869965416566"></a><a name="p869965416566"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p19518168181516"><a name="en-us_topic_0078894911_p19518168181516"></a><a name="en-us_topic_0078894911_p19518168181516"></a>Specifies the time when the job started.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row41445784181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p1665305181516"><a name="en-us_topic_0078894911_p1665305181516"></a><a name="en-us_topic_0078894911_p1665305181516"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p54432917181516"><a name="en-us_topic_0078894911_p54432917181516"></a><a name="en-us_topic_0078894911_p54432917181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p132445611568"><a name="p132445611568"></a><a name="p132445611568"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p46990176181516"><a name="en-us_topic_0078894911_p46990176181516"></a><a name="en-us_topic_0078894911_p46990176181516"></a>Specifies the time when the job ended.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row20258405181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p30318132181516"><a name="en-us_topic_0078894911_p30318132181516"></a><a name="en-us_topic_0078894911_p30318132181516"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p6594039181516"><a name="en-us_topic_0078894911_p6594039181516"></a><a name="en-us_topic_0078894911_p6594039181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p16738165711563"><a name="p16738165711563"></a><a name="p16738165711563"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p64355131181516"><a name="en-us_topic_0078894911_p64355131181516"></a><a name="en-us_topic_0078894911_p64355131181516"></a>Specifies the error code returned after the job fails to execute.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row42325270181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p5794860181516"><a name="en-us_topic_0078894911_p5794860181516"></a><a name="en-us_topic_0078894911_p5794860181516"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p36463241181516"><a name="en-us_topic_0078894911_p36463241181516"></a><a name="en-us_topic_0078894911_p36463241181516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p544925913567"><a name="p544925913567"></a><a name="p544925913567"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p732577181516"><a name="en-us_topic_0078894911_p732577181516"></a><a name="en-us_topic_0078894911_p732577181516"></a>Indicates the cause of the execution failure.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row6593195181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p64286802181516"><a name="en-us_topic_0078894911_p64286802181516"></a><a name="en-us_topic_0078894911_p64286802181516"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p6503230181516"><a name="en-us_topic_0078894911_p6503230181516"></a><a name="en-us_topic_0078894911_p6503230181516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p16241314573"><a name="p16241314573"></a><a name="p16241314573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p56999635181516"><a name="en-us_topic_0078894911_p56999635181516"></a><a name="en-us_topic_0078894911_p56999635181516"></a>Specifies the message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row43234669181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p12347328181516"><a name="en-us_topic_0078894911_p12347328181516"></a><a name="en-us_topic_0078894911_p12347328181516"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p10421710181516"><a name="en-us_topic_0078894911_p10421710181516"></a><a name="en-us_topic_0078894911_p10421710181516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="p1075719218578"><a name="p1075719218578"></a><a name="p1075719218578"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p38852186181516"><a name="en-us_topic_0078894911_p38852186181516"></a><a name="en-us_topic_0078894911_p38852186181516"></a>Specifies the error code returned when an error occurs.</p>
    <p id="en-us_topic_0078894911_p14125358181516"><a name="en-us_topic_0078894911_p14125358181516"></a><a name="en-us_topic_0078894911_p14125358181516"></a>For details of error code, see <a href="error-codes-for-classic-load-balancers.md">Error Codes for Classic Load Balancers</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row60019358181516"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894911_p29729859181516"><a name="en-us_topic_0078894911_p29729859181516"></a><a name="en-us_topic_0078894911_p29729859181516"></a>sub_jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894911_p39251151181516"><a name="en-us_topic_0078894911_p39251151181516"></a><a name="en-us_topic_0078894911_p39251151181516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.86%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894911_p59308401181516"><a name="en-us_topic_0078894911_p59308401181516"></a><a name="en-us_topic_0078894911_p59308401181516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.57%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894911_p25226629181516"><a name="en-us_topic_0078894911_p25226629181516"></a><a name="en-us_topic_0078894911_p25226629181516"></a>Specifies the execution information of a subjob. When no subjob exists, the value of this parameter is left empty. The structure of each subjob is similar to that of the parent job.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
        "status": "SUCCESS", 
        "entities": 
         {
          "elb": 
           {
            "id": "ef265755daf84333baf4ddc1d91cbc2f",
            "name": "1",
            "type": "External",
            "status": "ACTIVE", 
            "bandwidth": 1, 
            "vip_address": "10.154.53.4", 
            "tenant_id": "cbc08e2f8c354c7aa7abb88d0a7d11dc", 
            "admin_state_up": false, 
            "vpc_id": "21838be1-c1ce-4c09-9184-228cdb43038d" 
            } 
          }, 
         "job_id": "ff8080825ecc523f015ecd0a98f82f77", 
         "job_type": "createELB", 
         "begin_time": "2017-09-29T09:49:37.399Z", 
         "end_time": "2017-09-29T09:50:03.272Z", 
         "error_code": null, 
         "fail_reason": null 
    }
    ```


## Status Code<a name="en-us_topic_0078894911_section28345171181428"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0078894911_table971093418175"></a>
    <table><thead align="left"><tr id="en-us_topic_0078894911_row4282355018175"><th class="cellrowborder" valign="top" width="11.73%" id="mcps1.1.4.1.1"><p id="en-us_topic_0078894911_p4615550318175"><a name="en-us_topic_0078894911_p4615550318175"></a><a name="en-us_topic_0078894911_p4615550318175"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.03%" id="mcps1.1.4.1.2"><p id="p1227112265285"><a name="p1227112265285"></a><a name="p1227112265285"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.24%" id="mcps1.1.4.1.3"><p id="en-us_topic_0078894911_p4760829418175"><a name="en-us_topic_0078894911_p4760829418175"></a><a name="en-us_topic_0078894911_p4760829418175"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0078894911_row3106656818175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p3336409518175"><a name="en-us_topic_0078894911_p3336409518175"></a><a name="en-us_topic_0078894911_p3336409518175"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p78144618282"><a name="p78144618282"></a><a name="p78144618282"></a>Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p1813720318175"><a name="en-us_topic_0078894911_p1813720318175"></a><a name="en-us_topic_0078894911_p1813720318175"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row2901710318175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p157514418175"><a name="en-us_topic_0078894911_p157514418175"></a><a name="en-us_topic_0078894911_p157514418175"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p3818461286"><a name="p3818461286"></a><a name="p3818461286"></a>Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p6047787418175"><a name="en-us_topic_0078894911_p6047787418175"></a><a name="en-us_topic_0078894911_p6047787418175"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row742996118175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p6495596718175"><a name="en-us_topic_0078894911_p6495596718175"></a><a name="en-us_topic_0078894911_p6495596718175"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p58184642810"><a name="p58184642810"></a><a name="p58184642810"></a>Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p2694194518175"><a name="en-us_topic_0078894911_p2694194518175"></a><a name="en-us_topic_0078894911_p2694194518175"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4115091518175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p4488982318175"><a name="en-us_topic_0078894911_p4488982318175"></a><a name="en-us_topic_0078894911_p4488982318175"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p88194618288"><a name="p88194618288"></a><a name="p88194618288"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p1219704318175"><a name="en-us_topic_0078894911_p1219704318175"></a><a name="en-us_topic_0078894911_p1219704318175"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4266453018175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p3327492618175"><a name="en-us_topic_0078894911_p3327492618175"></a><a name="en-us_topic_0078894911_p3327492618175"></a>405</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p2811846142814"><a name="p2811846142814"></a><a name="p2811846142814"></a>Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p1091451918175"><a name="en-us_topic_0078894911_p1091451918175"></a><a name="en-us_topic_0078894911_p1091451918175"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row3112181218175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p3783881018175"><a name="en-us_topic_0078894911_p3783881018175"></a><a name="en-us_topic_0078894911_p3783881018175"></a>406</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p88113465285"><a name="p88113465285"></a><a name="p88113465285"></a>Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p4504476918175"><a name="en-us_topic_0078894911_p4504476918175"></a><a name="en-us_topic_0078894911_p4504476918175"></a>Response generated by the server is not acceptable to the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row274974018175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p2140239118175"><a name="en-us_topic_0078894911_p2140239118175"></a><a name="en-us_topic_0078894911_p2140239118175"></a>407</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p1081124611281"><a name="p1081124611281"></a><a name="p1081124611281"></a>Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p5587208618175"><a name="en-us_topic_0078894911_p5587208618175"></a><a name="en-us_topic_0078894911_p5587208618175"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row3308672918175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p6277936218175"><a name="en-us_topic_0078894911_p6277936218175"></a><a name="en-us_topic_0078894911_p6277936218175"></a>408</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p48114466286"><a name="p48114466286"></a><a name="p48114466286"></a>Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p5196352318175"><a name="en-us_topic_0078894911_p5196352318175"></a><a name="en-us_topic_0078894911_p5196352318175"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row6501852618175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p3200927918175"><a name="en-us_topic_0078894911_p3200927918175"></a><a name="en-us_topic_0078894911_p3200927918175"></a>409</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p58115462289"><a name="p58115462289"></a><a name="p58115462289"></a>Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p4261484518175"><a name="en-us_topic_0078894911_p4261484518175"></a><a name="en-us_topic_0078894911_p4261484518175"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4798929018175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p6192729418175"><a name="en-us_topic_0078894911_p6192729418175"></a><a name="en-us_topic_0078894911_p6192729418175"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p1782194662815"><a name="p1782194662815"></a><a name="p1782194662815"></a>Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p5005488118175"><a name="en-us_topic_0078894911_p5005488118175"></a><a name="en-us_topic_0078894911_p5005488118175"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4784075318175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p4989579318175"><a name="en-us_topic_0078894911_p4989579318175"></a><a name="en-us_topic_0078894911_p4989579318175"></a>501</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p1382546132811"><a name="p1382546132811"></a><a name="p1382546132811"></a>Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p1502741318175"><a name="en-us_topic_0078894911_p1502741318175"></a><a name="en-us_topic_0078894911_p1502741318175"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row102899218175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p1623954218175"><a name="en-us_topic_0078894911_p1623954218175"></a><a name="en-us_topic_0078894911_p1623954218175"></a>502</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p1382246122815"><a name="p1382246122815"></a><a name="p1382246122815"></a>Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p4033453218175"><a name="en-us_topic_0078894911_p4033453218175"></a><a name="en-us_topic_0078894911_p4033453218175"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row2746647618175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p1019211518175"><a name="en-us_topic_0078894911_p1019211518175"></a><a name="en-us_topic_0078894911_p1019211518175"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p11823468288"><a name="p11823468288"></a><a name="p11823468288"></a>Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p2025494918175"><a name="en-us_topic_0078894911_p2025494918175"></a><a name="en-us_topic_0078894911_p2025494918175"></a>Failed to complete the request because the system is out of service temporarily.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894911_row4807681918175"><td class="cellrowborder" valign="top" width="11.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0078894911_p190824318175"><a name="en-us_topic_0078894911_p190824318175"></a><a name="en-us_topic_0078894911_p190824318175"></a>504</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.03%" headers="mcps1.1.4.1.2 "><p id="p15821446102819"><a name="p15821446102819"></a><a name="p15821446102819"></a>Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.24%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0078894911_p2035000418175"><a name="en-us_topic_0078894911_p2035000418175"></a><a name="en-us_topic_0078894911_p2035000418175"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


