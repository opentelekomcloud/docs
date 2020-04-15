# Querying Task Execution Status<a name="EN-US_TOPIC_0022225398"></a>

## Function<a name="section49028201163249"></a>

This API is used to query the execution status of an asynchronous request task.

After an asynchronous request task is issued, for example, creating or deleting an ECS, performing operations on ECSs in a batch, or performing operations on ECS NICs, a task ID will be returned, based on which you can query the execution status of the task.

For details about how to obtain the task ID, see  [Responses \(Task\)](responses-(task).md).

## URI<a name="section39643212163249"></a>

GET /v1/\{project\_id\}/jobs/\{job\_id\}

[Table 1](#table6081678163249)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table6081678163249"></a>
<table><thead align="left"><tr id="row23421905163249"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27217880163249"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p19008506163553"><a name="p19008506163553"></a><a name="p19008506163553"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p63294000163553"><a name="p63294000163553"></a><a name="p63294000163553"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row58263622163612"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p54610556163612"><a name="p54610556163612"></a><a name="p54610556163612"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p61378926163612"><a name="p61378926163612"></a><a name="p61378926163612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p5637133163612"><a name="p5637133163612"></a><a name="p5637133163612"></a>Specifies the ID of an asynchronous request task.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section9500136163249"></a>

None

## Response<a name="section5816336151220"></a>

[Table 2](#table63003337163851)  describes the response parameters.

**Table  2**  Response parameters

<a name="table63003337163851"></a>
<table><thead align="left"><tr id="row65296242163851"><th class="cellrowborder" valign="top" width="19.259999999999998%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.220000000000002%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.52%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44762228163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p20905868102821"><a name="p20905868102821"></a><a name="p20905868102821"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p15653760102821"><a name="p15653760102821"></a><a name="p15653760102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p3084195102821"><a name="p3084195102821"></a><a name="p3084195102821"></a>Specifies the task status.</p>
<a name="ul27757760102821"></a><a name="ul27757760102821"></a><ul id="ul27757760102821"><li><strong>SUCCESS</strong>: indicates the task is successfully executed.</li><li><strong>RUNNING</strong>: indicates that the task is in progress.</li><li><strong id="b46231590154042"><a name="b46231590154042"></a><a name="b46231590154042"></a>FAIL</strong>: indicates that the task failed.</li><li><strong>INIT</strong>: indicates that the task is being initialized.</li></ul>
</td>
</tr>
<tr id="row17040455163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p21767581102821"><a name="p21767581102821"></a><a name="p21767581102821"></a>entities</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p18343614102821"><a name="p18343614102821"></a><a name="p18343614102821"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p78921950203711"><a name="p78921950203711"></a><a name="p78921950203711"></a>Specifies the object of the task. </p>
<p id="p17831309102821"><a name="p17831309102821"></a><a name="p17831309102821"></a>The value of this parameter varies depending on the type of the task. If the task is an ECS-related operation, the value is <strong id="b59118993155433"><a name="b59118993155433"></a><a name="b59118993155433"></a>server_id</strong>. If the task is an NIC operation, the value is <strong id="b30288946155433"><a name="b30288946155433"></a><a name="b30288946155433"></a>nic_id</strong>. If a sub-Job is available, details about the sub-job are displayed.</p>
<p id="p16646155213278"><a name="p16646155213278"></a><a name="p16646155213278"></a>For details, see <a href="#table63816992163249">Table 3</a>.</p>
</td>
</tr>
<tr id="row51515112163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p47013726102821"><a name="p47013726102821"></a><a name="p47013726102821"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p50015490102821"><a name="p50015490102821"></a><a name="p50015490102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p21179423102821"><a name="p21179423102821"></a><a name="p21179423102821"></a>Specifies the ID of an asynchronous request task.</p>
</td>
</tr>
<tr id="row25971152163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p4761320102821"><a name="p4761320102821"></a><a name="p4761320102821"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p50122638102821"><a name="p50122638102821"></a><a name="p50122638102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p32181178102821"><a name="p32181178102821"></a><a name="p32181178102821"></a>Specifies the type of an asynchronous request task.</p>
</td>
</tr>
<tr id="row37164860163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p39085626102821"><a name="p39085626102821"></a><a name="p39085626102821"></a>begin_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p11819105102821"><a name="p11819105102821"></a><a name="p11819105102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p26193501102821"><a name="p26193501102821"></a><a name="p26193501102821"></a>Specifies the time when the task started.</p>
</td>
</tr>
<tr id="row15772661163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p36144979102821"><a name="p36144979102821"></a><a name="p36144979102821"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p42062205102821"><a name="p42062205102821"></a><a name="p42062205102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p61705735102821"><a name="p61705735102821"></a><a name="p61705735102821"></a>Specifies the time when the task finished.</p>
</td>
</tr>
<tr id="row58136329163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p20542517102821"><a name="p20542517102821"></a><a name="p20542517102821"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p53331169102821"><a name="p53331169102821"></a><a name="p53331169102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p22389946102821"><a name="p22389946102821"></a><a name="p22389946102821"></a>Specifies the returned error code when the task execution fails.</p>
<p id="p53921224305"><a name="p53921224305"></a><a name="p53921224305"></a>After the task is executed successfully, the value of this parameter is null.</p>
</td>
</tr>
<tr id="row26946447163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p14816990102821"><a name="p14816990102821"></a><a name="p14816990102821"></a>fail_reason</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p59325580102821"><a name="p59325580102821"></a><a name="p59325580102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p30239861102821"><a name="p30239861102821"></a><a name="p30239861102821"></a>Specifies the cause of the task execution failure.</p>
<p id="p115901930103017"><a name="p115901930103017"></a><a name="p115901930103017"></a>After the task is executed successfully, the value of this parameter is null.</p>
</td>
</tr>
<tr id="row41958503163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p33151312102821"><a name="p33151312102821"></a><a name="p33151312102821"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p901760102821"><a name="p901760102821"></a><a name="p901760102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p53403447102821"><a name="p53403447102821"></a><a name="p53403447102821"></a>Specifies the error message returned when an error occurs in the request to query a task.</p>
</td>
</tr>
<tr id="row47258102163851"><td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p7972234102821"><a name="p7972234102821"></a><a name="p7972234102821"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="16.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p41771195102821"><a name="p41771195102821"></a><a name="p41771195102821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p50886402102821"><a name="p50886402102821"></a><a name="p50886402102821"></a>Specifies the error code returned when an error occurs in the request to query a task.</p>
<p id="p55324436102821"><a name="p55324436102821"></a><a name="p55324436102821"></a>For details about the error code, see <a href="returned-values-for-general-requests.md">Returned Values for General Requests</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **entities**  field description

<a name="table63816992163249"></a>
<table><thead align="left"><tr id="row25378569163249"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="p173103332361"><a name="p173103332361"></a><a name="p173103332361"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.24%" id="mcps1.2.4.1.2"><p id="p2310203316364"><a name="p2310203316364"></a><a name="p2310203316364"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.52%" id="mcps1.2.4.1.3"><p id="p15310123319365"><a name="p15310123319365"></a><a name="p15310123319365"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21068325163249"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p1987866102840"><a name="p1987866102840"></a><a name="p1987866102840"></a>sub_jobs_total</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.2 "><p id="p26799477102840"><a name="p26799477102840"></a><a name="p26799477102840"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p23274041102840"><a name="p23274041102840"></a><a name="p23274041102840"></a>Specifies the number of subtasks. </p>
</td>
</tr>
<tr id="row1957164017643"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p55342196102840"><a name="p55342196102840"></a><a name="p55342196102840"></a>sub_jobs</p>
</td>
<td class="cellrowborder" valign="top" width="16.24%" headers="mcps1.2.4.1.2 "><p id="p53532900102840"><a name="p53532900102840"></a><a name="p53532900102840"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.52%" headers="mcps1.2.4.1.3 "><p id="p35234299102840"><a name="p35234299102840"></a><a name="p35234299102840"></a>Specifies the execution information of a subtask.</p>
<p id="p131011530113215"><a name="p131011530113215"></a><a name="p131011530113215"></a>For details, see <a href="#table1500801817135">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **sub\_jobs**  field description

<a name="table1500801817135"></a>
<table><thead align="left"><tr id="row5502467917135"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="p385318355367"><a name="p385318355367"></a><a name="p385318355367"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p138539354361"><a name="p138539354361"></a><a name="p138539354361"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.53%" id="mcps1.2.4.1.3"><p id="p485303543616"><a name="p485303543616"></a><a name="p485303543616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3836327417140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p5596555610290"><a name="p5596555610290"></a><a name="p5596555610290"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p3691618110290"><a name="p3691618110290"></a><a name="p3691618110290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p124153110290"><a name="p124153110290"></a><a name="p124153110290"></a>Specifies the task status.</p>
<a name="ul1117378710290"></a><a name="ul1117378710290"></a><ul id="ul1117378710290"><li><strong>SUCCESS</strong>: indicates the task is successfully executed.</li><li><strong>RUNNING</strong>: indicates that the task is in progress.</li><li><strong id="b1978948323"><a name="b1978948323"></a><a name="b1978948323"></a>FAIL</strong>: indicates that the task failed.</li><li><strong>INIT</strong>: indicates that the task is being initialized.</li></ul>
</td>
</tr>
<tr id="row1171912617140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p5946004210290"><a name="p5946004210290"></a><a name="p5946004210290"></a>entities</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p5153410710290"><a name="p5153410710290"></a><a name="p5153410710290"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p5450940410290"><a name="p5450940410290"></a><a name="p5450940410290"></a>Specifies the object of the task. The value of this parameter varies depending on the type of the task. If the task is an ECS-related operation, the value is <strong id="b45687457155433"><a name="b45687457155433"></a><a name="b45687457155433"></a>server_id</strong>. If the task is an NIC operation, the value is <strong id="b2498330155433"><a name="b2498330155433"></a><a name="b2498330155433"></a>nic_id</strong>. For details, see <a href="#table2577901102930">Table 5</a>.</p>
</td>
</tr>
<tr id="row875866517140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p890825710290"><a name="p890825710290"></a><a name="p890825710290"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p5048019610290"><a name="p5048019610290"></a><a name="p5048019610290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p2440551510290"><a name="p2440551510290"></a><a name="p2440551510290"></a>Specifies the subtask ID.</p>
</td>
</tr>
<tr id="row3079934617140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p777215910290"><a name="p777215910290"></a><a name="p777215910290"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p2556517210290"><a name="p2556517210290"></a><a name="p2556517210290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p4785561910290"><a name="p4785561910290"></a><a name="p4785561910290"></a>Specify the subtask type.</p>
</td>
</tr>
<tr id="row6307447317140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p5724624610290"><a name="p5724624610290"></a><a name="p5724624610290"></a>begin_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p643434910290"><a name="p643434910290"></a><a name="p643434910290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p6012909110290"><a name="p6012909110290"></a><a name="p6012909110290"></a>Specifies the time when the task started.</p>
</td>
</tr>
<tr id="row2192135517140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p1201928510290"><a name="p1201928510290"></a><a name="p1201928510290"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p3403799810290"><a name="p3403799810290"></a><a name="p3403799810290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p5052973810290"><a name="p5052973810290"></a><a name="p5052973810290"></a>Specifies the time when the task finished.</p>
</td>
</tr>
<tr id="row5463148917140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p6052212310290"><a name="p6052212310290"></a><a name="p6052212310290"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p334495010290"><a name="p334495010290"></a><a name="p334495010290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p2254991410290"><a name="p2254991410290"></a><a name="p2254991410290"></a>Specifies the returned error code when the task execution fails.</p>
<p id="p2391911153711"><a name="p2391911153711"></a><a name="p2391911153711"></a>After the task is executed successfully, the value of this parameter is null.</p>
</td>
</tr>
<tr id="row6572248917140"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p6432481010290"><a name="p6432481010290"></a><a name="p6432481010290"></a>fail_reason</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p4292711110290"><a name="p4292711110290"></a><a name="p4292711110290"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53%" headers="mcps1.2.4.1.3 "><p id="p2113349010290"><a name="p2113349010290"></a><a name="p2113349010290"></a>Specifies the cause of the task execution failure.</p>
<p id="p580920137374"><a name="p580920137374"></a><a name="p580920137374"></a>After the task is executed successfully, the value of this parameter is null.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **entities**  field description

<a name="table2577901102930"></a>
<table><thead align="left"><tr id="row41961594102930"><th class="cellrowborder" valign="top" width="17.64%" id="mcps1.2.4.1.1"><p id="p1819124019365"><a name="p1819124019365"></a><a name="p1819124019365"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.9%" id="mcps1.2.4.1.2"><p id="p31934010363"><a name="p31934010363"></a><a name="p31934010363"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.46%" id="mcps1.2.4.1.3"><p id="p8191240193618"><a name="p8191240193618"></a><a name="p8191240193618"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12623506102930"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p15871098102930"><a name="p15871098102930"></a><a name="p15871098102930"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.4.1.2 "><p id="p10490546102930"><a name="p10490546102930"></a><a name="p10490546102930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.46%" headers="mcps1.2.4.1.3 "><p id="p64306551102930"><a name="p64306551102930"></a><a name="p64306551102930"></a>If the task is an ECS-related operation, the value is <strong id="b195691120185516"><a name="b195691120185516"></a><a name="b195691120185516"></a>server_id</strong>.</p>
</td>
</tr>
<tr id="row41888051102930"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p37488972102930"><a name="p37488972102930"></a><a name="p37488972102930"></a>nic_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.4.1.2 "><p id="p16707926102930"><a name="p16707926102930"></a><a name="p16707926102930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.46%" headers="mcps1.2.4.1.3 "><p id="p33374275102930"><a name="p33374275102930"></a><a name="p33374275102930"></a>If the task is an NIC-related operation, the value is <strong id="b65546242155433"><a name="b65546242155433"></a><a name="b65546242155433"></a>nic_id</strong>.</p>
</td>
</tr>
<tr id="row64971320122011"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p34983202201"><a name="p34983202201"></a><a name="p34983202201"></a>errorcode_message</p>
</td>
<td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.4.1.2 "><p id="p184980206205"><a name="p184980206205"></a><a name="p184980206205"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.46%" headers="mcps1.2.4.1.3 "><p id="p1249812014200"><a name="p1249812014200"></a><a name="p1249812014200"></a>Indicates the cause of a subtask execution failure.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section779115469181"></a>

```
GET https://{endpoint}/v1/{project_id}/jobs/{job_id}
```

## Example Response<a name="section17930437174311"></a>

```
{
    "status": "SUCCESS",
    "entities": {
        "sub_jobs_total": 1,
        "sub_jobs": [
            {
                "status": "SUCCESS",
                "entities": {
                    "server_id": "bae51750-0089-41a1-9b18-5c777978ff6d"
                },
                "job_id": "2c9eb2c5544cbf6101544f0635672b60",
                "job_type": "createSingleServer",
                "begin_time": "2016-04-25T20:04:47.591Z",
                "end_time": "2016-04-25T20:08:21.328Z",
                "error_code": null,
                "fail_reason": null
            }
        ]
    },
    "job_id": "2c9eb2c5544cbf6101544f0602af2b4f",
    "job_type": "createServer",
    "begin_time": "2016-04-25T20:04:34.604Z",
    "end_time": "2016-04-25T20:08:41.593Z",
    "error_code": null,
    "fail_reason": null
}
```

## Returned Values<a name="section6451411163249"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

