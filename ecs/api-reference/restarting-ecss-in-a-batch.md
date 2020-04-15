# Restarting ECSs in a Batch<a name="EN-US_TOPIC_0020212649"></a>

## Function<a name="section39601516"></a>

This API is used to restart ECSs in a batch based on specified ECS IDs. A maximum of 1000 ECSs can be restarted at a time.

## URI<a name="section20869327"></a>

POST /v1/\{project\_id\}/cloudservers/action

[Table 1](#table33008913)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table33008913"></a>
<table><thead align="left"><tr id="row32701678"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p31590262"><a name="p31590262"></a><a name="p31590262"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p8674443"><a name="p8674443"></a><a name="p8674443"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p31541268"><a name="p31541268"></a><a name="p31541268"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4705914"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p45634724"><a name="p45634724"></a><a name="p45634724"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p5425146"><a name="p5425146"></a><a name="p5425146"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section53606218"></a>

[Table 2](#table54749715)  describes the request parameters.

**Table  2**  Request parameters

<a name="table54749715"></a>
<table><thead align="left"><tr id="row24121565"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p7689721"><a name="p7689721"></a><a name="p7689721"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.2"><p id="p18887690"><a name="p18887690"></a><a name="p18887690"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p53507960"><a name="p53507960"></a><a name="p53507960"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p39177514"><a name="p39177514"></a><a name="p39177514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19262089"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p16725372"><a name="p16725372"></a><a name="p16725372"></a>reboot</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p12577900"><a name="p12577900"></a><a name="p12577900"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p12176960"><a name="p12176960"></a><a name="p12176960"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p18634089"><a name="p18634089"></a><a name="p18634089"></a>Specifies the operation to restart the ECS. For details, see <a href="#table64591731162222">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **reboot**  field description

<a name="table64591731162222"></a>
<table><thead align="left"><tr id="row30453945162222"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p26274222513"><a name="p26274222513"></a><a name="p26274222513"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p4627202192519"><a name="p4627202192519"></a><a name="p4627202192519"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.18%" id="mcps1.2.5.1.3"><p id="p66276219259"><a name="p66276219259"></a><a name="p66276219259"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.5.1.4"><p id="p364202152512"><a name="p364202152512"></a><a name="p364202152512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42922987162336"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p50762568162336"><a name="p50762568162336"></a><a name="p50762568162336"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p18127378162336"><a name="p18127378162336"></a><a name="p18127378162336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.18%" headers="mcps1.2.5.1.3 "><p id="p59031541162336"><a name="p59031541162336"></a><a name="p59031541162336"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.4 "><p id="p16825496162336"><a name="p16825496162336"></a><a name="p16825496162336"></a>Specifies the type of the restart operation.</p>
<a name="ul62344604154036"></a><a name="ul62344604154036"></a><ul id="ul62344604154036"><li><strong>SOFT</strong>: soft restart</li><li><strong id="b5811448105018"><a name="b5811448105018"></a><a name="b5811448105018"></a>HARD</strong>: forcible restart (hard restart)</li></ul>
</td>
</tr>
<tr id="row10461780162222"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p19668200162240"><a name="p19668200162240"></a><a name="p19668200162240"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p49620364162240"><a name="p49620364162240"></a><a name="p49620364162240"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.18%" headers="mcps1.2.5.1.3 "><p id="p59826577162240"><a name="p59826577162240"></a><a name="p59826577162240"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.4 "><p id="p59922456162240"><a name="p59922456162240"></a><a name="p59922456162240"></a>Specifies ECS IDs. For details, see <a href="#table26785545162223">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **servers**  field description

<a name="table26785545162223"></a>
<table><thead align="left"><tr id="row56759147162223"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p1468216622519"><a name="p1468216622519"></a><a name="p1468216622519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.2"><p id="p11682168253"><a name="p11682168253"></a><a name="p11682168253"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.3"><p id="p9682167253"><a name="p9682167253"></a><a name="p9682167253"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.5.1.4"><p id="p20682769256"><a name="p20682769256"></a><a name="p20682769256"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row205574162223"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p16651565162223"><a name="p16651565162223"></a><a name="p16651565162223"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p6599487162223"><a name="p6599487162223"></a><a name="p6599487162223"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.3 "><p id="p64796454162223"><a name="p64796454162223"></a><a name="p64796454162223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.5.1.4 "><p id="p59084190162223"><a name="p59084190162223"></a><a name="p59084190162223"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section12693918"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section366624342413"></a>

In the request, the parameters to restart ECSs must be sent with field  **reboot**. For details, see the example request.

```
POST https://{endpoint}/v1/{project_id}/cloudservers/action
```

```
{
    "reboot": {
        "type":"SOFT",
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

## Example Response<a name="section18237102335311"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

