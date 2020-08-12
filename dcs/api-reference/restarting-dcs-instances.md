# Restarting DCS Instances<a name="dcs-api-0312018"></a>

## Function<a name="section7884115112419"></a>

This API is used to restart a running DCS instance.

## URI<a name="section135003281596"></a>

PUT /v1.0/\{project\_id\}/instances/status

[Table 1](#table344154216371)  describes the parameter.

**Table  1**  Parameter description

<a name="table344154216371"></a>
<table><thead align="left"><tr id="row44454293719"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p143542153710"><a name="p143542153710"></a><a name="p143542153710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p243942133712"><a name="p243942133712"></a><a name="p243942133712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15431742143710"><a name="p15431742143710"></a><a name="p15431742143710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1843204253716"><a name="p1843204253716"></a><a name="p1843204253716"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54444263714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1144042133712"><a name="p1144042133712"></a><a name="p1144042133712"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p15449424377"><a name="p15449424377"></a><a name="p15449424377"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4441242153712"><a name="p4441242153712"></a><a name="p4441242153712"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14441242143712"><a name="p14441242143712"></a><a name="p14441242143712"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8844175611106"></a>

**Request parameters**

[Table 2](#table103786452372)  describes the request parameters.

**Table  2**  Parameter description

<a name="table103786452372"></a>
<table><thead align="left"><tr id="row1377114516376"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p537711457375"><a name="p537711457375"></a><a name="p537711457375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p1737754583715"><a name="p1737754583715"></a><a name="p1737754583715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p5377345123713"><a name="p5377345123713"></a><a name="p5377345123713"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="p43771145143711"><a name="p43771145143711"></a><a name="p43771145143711"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1437724511376"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p183771145173718"><a name="p183771145173718"></a><a name="p183771145173718"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p537712456375"><a name="p537712456375"></a><a name="p537712456375"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p17377124563715"><a name="p17377124563715"></a><a name="p17377124563715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p13451321125615"><a name="p13451321125615"></a><a name="p13451321125615"></a>Action performed on DCS instances. Value: <strong id="b653782918610"><a name="b653782918610"></a><a name="b653782918610"></a>restart</strong>.</p>
</td>
</tr>
<tr id="row03781645173719"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p11377945183718"><a name="p11377945183718"></a><a name="p11377945183718"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p103774453372"><a name="p103774453372"></a><a name="p103774453372"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p163771745133715"><a name="p163771745133715"></a><a name="p163771745133715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p93774453376"><a name="p93774453376"></a><a name="p93774453376"></a>List of DCS instance IDs.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
PUT https://{dcs_endpoint}/v1.0/{project_id}/instances/status
```

```
{
    "action": "restart",
    "instances": [
        "2e803f66-fbb0-47ad-b6cb-fb87f5bed4ef"
    ]
}
```

## Response<a name="section1526810536111"></a>

**Response parameters**

[Table 3](#table52851943388)  describes the response parameter.

**Table  3**  Parameter description

<a name="table52851943388"></a>
<table><thead align="left"><tr id="row172851641381"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p92851944388"><a name="p92851944388"></a><a name="p92851944388"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p628534163813"><a name="p628534163813"></a><a name="p628534163813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p228511417382"><a name="p228511417382"></a><a name="p228511417382"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1828514413815"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6285184153819"><a name="p6285184153819"></a><a name="p6285184153819"></a>results</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5285154123811"><a name="p5285154123811"></a><a name="p5285154123811"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15285644384"><a name="p15285644384"></a><a name="p15285644384"></a>Indicates the result of instance modification.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  results parameter description

<a name="table2070112173318"></a>
<table><thead align="left"><tr id="row4701171710315"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p107011517838"><a name="p107011517838"></a><a name="p107011517838"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p47012172037"><a name="p47012172037"></a><a name="p47012172037"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16702817236"><a name="p16702817236"></a><a name="p16702817236"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row127025171316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15702101711317"><a name="p15702101711317"></a><a name="p15702101711317"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p157020171730"><a name="p157020171730"></a><a name="p157020171730"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1070213176311"><a name="p1070213176311"></a><a name="p1070213176311"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row1702617833"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10702417734"><a name="p10702417734"></a><a name="p10702417734"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1170214171930"><a name="p1170214171930"></a><a name="p1170214171930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1770221712311"><a name="p1770221712311"></a><a name="p1770221712311"></a>Instance modification result. Options: <strong id="b18540144242919"><a name="b18540144242919"></a><a name="b18540144242919"></a>success</strong> or <strong id="b455518428294"><a name="b455518428294"></a><a name="b455518428294"></a>failed</strong></p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "results": [
        {
            "result": "success",
            "instance": "2e803f66-fbb0-47ad-b6cb-fb87f5bed4ef"
        }
    ]
}
```

## Status Code<a name="section1257075711211"></a>

[Table 5](#table1357115714126)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  5**  Status code

<a name="table1357115714126"></a>
<table><thead align="left"><tr id="row3571145711215"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p17572125771218"><a name="p17572125771218"></a><a name="p17572125771218"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p1572185781216"><a name="p1572185781216"></a><a name="p1572185781216"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row155722572121"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p1757265761210"><a name="p1757265761210"></a><a name="p1757265761210"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p175205075613"><a name="p175205075613"></a><a name="p175205075613"></a>Successfully restarted the DCS instance.</p>
</td>
</tr>
</tbody>
</table>

