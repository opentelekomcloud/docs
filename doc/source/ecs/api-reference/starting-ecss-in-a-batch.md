# Starting ECSs in a Batch<a name="EN-US_TOPIC_0020212207"></a>

## Function<a name="section18389930"></a>

This API is used to start ECSs in a batch based on specified ECS IDs. A maximum of 1000 ECSs can be started at a time.

## URI<a name="section31291646"></a>

POST /v1/\{project\_id\}/cloudservers/action

[Table 1](#table58892473)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table58892473"></a>
<table><thead align="left"><tr id="row45596481"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p2327487"><a name="p2327487"></a><a name="p2327487"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p54308798"><a name="p54308798"></a><a name="p54308798"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.86%" id="mcps1.2.4.1.3"><p id="p36936550"><a name="p36936550"></a><a name="p36936550"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39070558"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p10598606"><a name="p10598606"></a><a name="p10598606"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p53180767"><a name="p53180767"></a><a name="p53180767"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section13189358"></a>

**Table  2**  Request parameters

<a name="table66572856"></a>
<table><thead align="left"><tr id="row53954942"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="p8274172"><a name="p8274172"></a><a name="p8274172"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p66228199"><a name="p66228199"></a><a name="p66228199"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p62883878"><a name="p62883878"></a><a name="p62883878"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p60429346"><a name="p60429346"></a><a name="p60429346"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62938818"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p64879470"><a name="p64879470"></a><a name="p64879470"></a>os-start</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p20745743"><a name="p20745743"></a><a name="p20745743"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p2683661"><a name="p2683661"></a><a name="p2683661"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p10232270"><a name="p10232270"></a><a name="p10232270"></a>Specifies the operation to start the ECS. For details, see <a href="#table52132698163051">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **os-start**  field description

<a name="table52132698163051"></a>
<table><thead align="left"><tr id="row58550307163051"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="p22861271209"><a name="p22861271209"></a><a name="p22861271209"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p13286132712018"><a name="p13286132712018"></a><a name="p13286132712018"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p1028616277208"><a name="p1028616277208"></a><a name="p1028616277208"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p16286827182014"><a name="p16286827182014"></a><a name="p16286827182014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63441585163051"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p38494721163051"><a name="p38494721163051"></a><a name="p38494721163051"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p31064669163051"><a name="p31064669163051"></a><a name="p31064669163051"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p33210286163051"><a name="p33210286163051"></a><a name="p33210286163051"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p48899565163125"><a name="p48899565163125"></a><a name="p48899565163125"></a>Specifies ECS IDs. For details, see <a href="#table23507505">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **servers**  field description

<a name="table23507505"></a>
<table><thead align="left"><tr id="row5109846"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="p477877142215"><a name="p477877142215"></a><a name="p477877142215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p1777847162211"><a name="p1777847162211"></a><a name="p1777847162211"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p077816719225"><a name="p077816719225"></a><a name="p077816719225"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p1077816719222"><a name="p1077816719222"></a><a name="p1077816719222"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66578044"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p24112512"><a name="p24112512"></a><a name="p24112512"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p6956456"><a name="p6956456"></a><a name="p6956456"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p26602077"><a name="p26602077"></a><a name="p26602077"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p65561530"><a name="p65561530"></a><a name="p65561530"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section51595365"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section1741103616214"></a>

In the request, the parameters to start ECSs must be sent with field  **os-start**. For details, see the example request.

```
POST https://{endpoint}/v1/{project_id}/cloudservers/action
```

```
{
    "os-start": {
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

## Example Response<a name="section1589616484522"></a>

None

## Returned Values<a name="section17349988"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

