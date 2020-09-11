# Stopping ECSs in a Batch<a name="EN-US_TOPIC_0020212651"></a>

## Function<a name="section14270750"></a>

This API is used to stop ECSs in a batch based on the specified ECS ID list. A maximum of 1000 ECSs can be stopped at a time.

## URI<a name="section61327894"></a>

POST /v1/\{project\_id\}/cloudservers/action

[Table 1](#table66418347)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table66418347"></a>
<table><thead align="left"><tr id="row49507636"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p50695543"><a name="p50695543"></a><a name="p50695543"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p12698356"><a name="p12698356"></a><a name="p12698356"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p21933905"><a name="p21933905"></a><a name="p21933905"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31815862"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p26948044"><a name="p26948044"></a><a name="p26948044"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p35307962"><a name="p35307962"></a><a name="p35307962"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15080136"></a>

**Table  2**  Request parameters

<a name="table12156768"></a>
<table><thead align="left"><tr id="row44143566"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p18859061"><a name="p18859061"></a><a name="p18859061"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p51188993"><a name="p51188993"></a><a name="p51188993"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p52667802"><a name="p52667802"></a><a name="p52667802"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p38233575"><a name="p38233575"></a><a name="p38233575"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9911889"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p64665535"><a name="p64665535"></a><a name="p64665535"></a>os-stop</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p3416986"><a name="p3416986"></a><a name="p3416986"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p8340425"><a name="p8340425"></a><a name="p8340425"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p40372317"><a name="p40372317"></a><a name="p40372317"></a>Specifies the operation to stop the ECS. For details, see <a href="#table51053190162024">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **os-stop**  field description

<a name="table51053190162024"></a>
<table><thead align="left"><tr id="row27328423162024"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p6705171622715"><a name="p6705171622715"></a><a name="p6705171622715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p14705171632717"><a name="p14705171632717"></a><a name="p14705171632717"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p17705151615277"><a name="p17705151615277"></a><a name="p17705151615277"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p570511161274"><a name="p570511161274"></a><a name="p570511161274"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21953637162024"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p33414178162024"><a name="p33414178162024"></a><a name="p33414178162024"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p22193916162024"><a name="p22193916162024"></a><a name="p22193916162024"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p52876762162024"><a name="p52876762162024"></a><a name="p52876762162024"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p26671950162024"><a name="p26671950162024"></a><a name="p26671950162024"></a>Specifies ECS IDs. For details, see <a href="#table48932206">Table 4</a>.</p>
</td>
</tr>
<tr id="row8227700141926"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p62463948141926"><a name="p62463948141926"></a><a name="p62463948141926"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p26415004141926"><a name="p26415004141926"></a><a name="p26415004141926"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p59240589141926"><a name="p59240589141926"></a><a name="p59240589141926"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p33758406141926"><a name="p33758406141926"></a><a name="p33758406141926"></a>Specifies an ECS stop type. The default value is <strong id="b84235270612825"><a name="b84235270612825"></a><a name="b84235270612825"></a>SOFT</strong>.</p>
<p id="p28853449141951"><a name="p28853449141951"></a><a name="p28853449141951"></a><strong id="b84235270617736"><a name="b84235270617736"></a><a name="b84235270617736"></a>SOFT</strong>: normal ECS stop (default)</p>
<p id="p18774459142010"><a name="p18774459142010"></a><a name="p18774459142010"></a><strong id="b8423527061788"><a name="b8423527061788"></a><a name="b8423527061788"></a>HARD</strong>: forcible ECS stop</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **servers**  field description

<a name="table48932206"></a>
<table><thead align="left"><tr id="row2750866"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p1530882182711"><a name="p1530882182711"></a><a name="p1530882182711"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p1930815213276"><a name="p1930815213276"></a><a name="p1930815213276"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p1230815218276"><a name="p1230815218276"></a><a name="p1230815218276"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p3308132152717"><a name="p3308132152717"></a><a name="p3308132152717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46555465"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p12896286"><a name="p12896286"></a><a name="p12896286"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p37966223"><a name="p37966223"></a><a name="p37966223"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p55365254"><a name="p55365254"></a><a name="p55365254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p28842926"><a name="p28842926"></a><a name="p28842926"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1503503"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section78042033102712"></a>

In the request parameters, the request for stopping the ECS must be issued with field  **os-stop**, as shown in the example request.

```
POST https://{endpoint}/v1/{project_id}/cloudservers/action
```

```
{
    "os-stop": {
        "type":"HARD",
        "servers": [
            {
                "id": "616fb98f-46ca-475e-917e-2563e5a8cd19"
            },
            {
                "id": "726fb98f-46ca-475e-917e-2563e5a8cd20"
            }

        ]
    }
}
```

## Example Response<a name="section14343105213539"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

