# Batch Creating or Deleting VPC Tags<a name="vpc_tag_0004"></a>

## Function<a name="section9716105931810"></a>

This API is used to add multiple tags to or delete multiple tags from a VPC at a time.

This API is idempotent.

If there are duplicate keys in the request body when you add tags, an error is reported.

During tag creation, duplicate keys are not allowed. If a key already exists in the database, its value will be overwritten by the new duplicate key.

During tag deletion, if some tags do not exist, the operation is considered to be successful by default. The character set of the tags will not be checked. When you delete tags, the tag structure cannot be missing, and the key cannot be left blank or be an empty string.

## URI<a name="section14718205991814"></a>

POST /v2.0/\{project\_id\}/vpcs/\{vpc\_id\}/tags/action

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b13180940194512"><a name="b13180940194512"></a><a name="b13180940194512"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b14235441154510"><a name="b14235441154510"></a><a name="b14235441154510"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b662694284512"><a name="b662694284512"></a><a name="b662694284512"></a>Description</strong></p>
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
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section972418597185"></a>

Request parameter

**Table  2**  Request parameter

<a name="table2726185911818"></a>
<table><thead align="left"><tr id="row1080816597184"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="p208081359151817"><a name="p208081359151817"></a><a name="p208081359151817"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p9808135941814"><a name="p9808135941814"></a><a name="p9808135941814"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.900990099009901%" id="mcps1.2.5.1.3"><p id="p080805991816"><a name="p080805991816"></a><a name="p080805991816"></a><strong id="b341713560453"><a name="b341713560453"></a><a name="b341713560453"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.415841584158414%" id="mcps1.2.5.1.4"><p id="p680845913189"><a name="p680845913189"></a><a name="p680845913189"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row180885915182"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p148081759191815"><a name="p148081759191815"></a><a name="p148081759191815"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p10424324181820"><a name="p10424324181820"></a><a name="p10424324181820"></a>Array of <a href="#table244913515593">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.5.1.3 "><p id="p6808115981818"><a name="p6808115981818"></a><a name="p6808115981818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.2.5.1.4 "><p id="p180814592186"><a name="p180814592186"></a><a name="p180814592186"></a>Specifies the <strong id="b2031040204619"><a name="b2031040204619"></a><a name="b2031040204619"></a>tag</strong> objects. For details, see <a href="#table244913515593">Table 3</a>.</p>
</td>
</tr>
<tr id="row58082596188"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p128082059141814"><a name="p128082059141814"></a><a name="p128082059141814"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p480816591183"><a name="p480816591183"></a><a name="p480816591183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.5.1.3 "><p id="p1380825915181"><a name="p1380825915181"></a><a name="p1380825915181"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.2.5.1.4 "><p id="p1562014114112"><a name="p1562014114112"></a><a name="p1562014114112"></a>Specifies the operation. Possible values are as follows:</p>
<a name="ul2205152413110"></a><a name="ul2205152413110"></a><ul id="ul2205152413110"><li><strong id="b147195510471"><a name="b147195510471"></a><a name="b147195510471"></a>create</strong></li><li><strong id="b1881017153475"><a name="b1881017153475"></a><a name="b1881017153475"></a>delete</strong></li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  objects

<a name="table244913515593"></a>
<table><thead align="left"><tr id="row345095195914"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p1045012512597"><a name="p1045012512597"></a><a name="p1045012512597"></a><strong id="b831342319470"><a name="b831342319470"></a><a name="b831342319470"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.2"><p id="p124502516594"><a name="p124502516594"></a><a name="p124502516594"></a><strong id="b17113142474710"><a name="b17113142474710"></a><a name="b17113142474710"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.3"><p id="p169809965412"><a name="p169809965412"></a><a name="p169809965412"></a><strong id="b1299110246474"><a name="b1299110246474"></a><a name="b1299110246474"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.699999999999996%" id="mcps1.2.5.1.4"><p id="p1545075105910"><a name="p1545075105910"></a><a name="p1545075105910"></a><strong id="b14242664710"><a name="b14242664710"></a><a name="b14242664710"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="p1183773495120"><a name="p1183773495120"></a><a name="p1183773495120"></a>Yes (when the value of <strong id="b1283710342512"><a name="b1283710342512"></a><a name="b1283710342512"></a>action</strong> is <strong id="b2837173415511"><a name="b2837173415511"></a><a name="b2837173415511"></a>create</strong>) </p>
<p id="p209805915417"><a name="p209805915417"></a><a name="p209805915417"></a>No (when the value of <strong id="b1613095015"><a name="b1613095015"></a><a name="b1613095015"></a>action</strong> is <strong id="b41423411506"><a name="b41423411506"></a><a name="b41423411506"></a>delete</strong>)</p>
</td>
<td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="ul0451105165914"></a><a name="ul0451105165914"></a><ul id="ul0451105165914"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul7895160105919"></a><a name="ul7895160105919"></a><ul id="ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

Request example 1: Creating tags in batches

```
POST https://{Endpoint}/v2.0/{project_id}/vpcs/{vpc_id}/tags/action

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
POST https://{Endpoint}/v2.0/{project_id}/vpcs/{vpc_id}/tags/action

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

## Response Message<a name="section973755901815"></a>

Response parameter

None

Example response

None

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

