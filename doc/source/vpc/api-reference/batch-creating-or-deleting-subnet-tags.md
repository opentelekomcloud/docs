# Batch Creating or Deleting Subnet Tags<a name="subnet_tag_0004"></a>

## Function<a name="section13122151902216"></a>

This API is used to add multiple tags to or delete multiple tags from a subnet at a time.

This API is idempotent.

If there are duplicate keys in the request body when you add tags, an error is reported.

During tag creation, duplicate keys are not allowed. If a key already exists in the database, its value will be overwritten by the new duplicate key.

During tag deletion, if some tags do not exist, the operation is considered to be successful by default. The character set of the tags will not be checked. When you delete tags, the tag structure cannot be missing, and the key cannot be left blank or be an empty string.

## URI<a name="section1712271922215"></a>

POST /v2.0/\{project\_id\}/subnets/\{subnet\_id\}/tags/action

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b18594327366"><a name="b18594327366"></a><a name="b18594327366"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b154206287611"><a name="b154206287611"></a><a name="b154206287611"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b7604184017611"><a name="b7604184017611"></a><a name="b7604184017611"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section3126219162217"></a>

Request parameter

**Table  2**  Request parameter

<a name="table6126151902213"></a>
<table><thead align="left"><tr id="row1618916198227"><th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.1"><p id="p1418961982213"><a name="p1418961982213"></a><a name="p1418961982213"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.262626262626267%" id="mcps1.2.5.1.2"><p id="p818981920229"><a name="p818981920229"></a><a name="p818981920229"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="6.0606060606060606%" id="mcps1.2.5.1.3"><p id="p418918193229"><a name="p418918193229"></a><a name="p418918193229"></a><strong id="b4521261078"><a name="b4521261078"></a><a name="b4521261078"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.57575757575757%" id="mcps1.2.5.1.4"><p id="p21899199220"><a name="p21899199220"></a><a name="p21899199220"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11891119102210"><td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.1 "><p id="p41891619132211"><a name="p41891619132211"></a><a name="p41891619132211"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.5.1.2 "><p id="p5189719172218"><a name="p5189719172218"></a><a name="p5189719172218"></a>Array of <a href="#table244913515593">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="6.0606060606060606%" headers="mcps1.2.5.1.3 "><p id="p51893195226"><a name="p51893195226"></a><a name="p51893195226"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.5.1.4 "><p id="p81894192221"><a name="p81894192221"></a><a name="p81894192221"></a>Specifies the <strong id="b6686179878"><a name="b6686179878"></a><a name="b6686179878"></a>tag</strong> object list. For details, see <a href="#table244913515593">Table 3</a>.</p>
</td>
</tr>
<tr id="row17189161942213"><td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.1 "><p id="p141894199225"><a name="p141894199225"></a><a name="p141894199225"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.2.5.1.2 "><p id="p10189181982214"><a name="p10189181982214"></a><a name="p10189181982214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="6.0606060606060606%" headers="mcps1.2.5.1.3 "><p id="p918915199228"><a name="p918915199228"></a><a name="p918915199228"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.5.1.4 "><p id="p1562014114112"><a name="p1562014114112"></a><a name="p1562014114112"></a>Specifies the operation. Possible values are as follows:</p>
<a name="ul2205152413110"></a><a name="ul2205152413110"></a><ul id="ul2205152413110"><li><strong id="b1674214217710"><a name="b1674214217710"></a><a name="b1674214217710"></a>create</strong></li><li><strong id="b88582221717"><a name="b88582221717"></a><a name="b88582221717"></a>delete</strong></li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  objects

<a name="table244913515593"></a>
<table><thead align="left"><tr id="row345095195914"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p1045012512597"><a name="p1045012512597"></a><a name="p1045012512597"></a><strong id="b1660412415710"><a name="b1660412415710"></a><a name="b1660412415710"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.2"><p id="p124502516594"><a name="p124502516594"></a><a name="p124502516594"></a><strong id="b109572025779"><a name="b109572025779"></a><a name="b109572025779"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.3"><p id="p169809965412"><a name="p169809965412"></a><a name="p169809965412"></a><strong id="b872122614719"><a name="b872122614719"></a><a name="b872122614719"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.699999999999996%" id="mcps1.2.5.1.4"><p id="p1545075105910"><a name="p1545075105910"></a><a name="p1545075105910"></a><strong id="b1445818272715"><a name="b1445818272715"></a><a name="b1445818272715"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row84502515598"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p154506595915"><a name="p154506595915"></a><a name="p154506595915"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p14501518591"><a name="p14501518591"></a><a name="p14501518591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="p298018911544"><a name="p298018911544"></a><a name="p298018911544"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="ul9450135125915"></a><a name="ul9450135125915"></a><ul id="ul9450135125915"><li>Specifies the tag key.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul9450453597"></a><a name="ul9450453597"></a><ul id="ul9450453597"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a VPC must be unique.</li></ul>
</td>
</tr>
<tr id="row845145185917"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p12451185185910"><a name="p12451185185910"></a><a name="p12451185185910"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p104515514598"><a name="p104515514598"></a><a name="p104515514598"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="p1032014523815"><a name="p1032014523815"></a><a name="p1032014523815"></a>Yes (when the value of <strong id="b432010521810"><a name="b432010521810"></a><a name="b432010521810"></a>action</strong> is <strong id="b132011524811"><a name="b132011524811"></a><a name="b132011524811"></a>create</strong>) </p>
<p id="p209805915417"><a name="p209805915417"></a><a name="p209805915417"></a>No (when the value of <strong id="b6215742170"><a name="b6215742170"></a><a name="b6215742170"></a>action</strong> is <strong id="b92186420720"><a name="b92186420720"></a><a name="b92186420720"></a>delete</strong>)</p>
</td>
<td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="ul0451105165914"></a><a name="ul0451105165914"></a><ul id="ul0451105165914"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul7895160105919"></a><a name="ul7895160105919"></a><ul id="ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

Request example 1: Creating tags in batches

```
POST https://{Endpoint}/v2.0/{project_id}/subnets/{subnet_id}/tags/action

{
    "action": "create",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key2",
            "value": "value3"
        }
    ]
}
```

Request example 2: Deleting tags in batches

```
POST https://{Endpoint}/v2.0/{project_id}/subnets/{subnet_id}/tags/action

{
    "action": "delete",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key2",
            "value": "value3"
        }
    ]
}
```

## Response Message<a name="section1713651914221"></a>

Response parameter

None

Example response

None

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

