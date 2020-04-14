# Deleting an Instance<a name="EN-US_TOPIC_0128036935"></a>

## Function<a name="section790717910293"></a>

This API is used to delete an instance to release all the resources occupied by it.

## URI<a name="section26585449267"></a>

URI format: DELETE /v1.0/\{project\_id\}/instances/\{instance\_id\}

[Table 1](#table3660444102619)  describes the parameters.

**Table  1**  Parameter description

<a name="table3660444102619"></a>
<table><thead align="left"><tr id="row1272594492615"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1172504452615"><a name="p1172504452615"></a><a name="p1172504452615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p10725164402619"><a name="p10725164402619"></a><a name="p10725164402619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p10725174422615"><a name="p10725174422615"></a><a name="p10725174422615"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p16725114416265"><a name="p16725114416265"></a><a name="p16725114416265"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15725744182619"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p472534452619"><a name="p472534452619"></a><a name="p472534452619"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1272544412262"><a name="p1272544412262"></a><a name="p1272544412262"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p117259441266"><a name="p117259441266"></a><a name="p117259441266"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p4725344112618"><a name="p4725344112618"></a><a name="p4725344112618"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row1725194482619"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1172554419268"><a name="p1172554419268"></a><a name="p1172554419268"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p17251844122618"><a name="p17251844122618"></a><a name="p17251844122618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p107251442262"><a name="p107251442262"></a><a name="p107251442262"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1772534422613"><a name="p1772534422613"></a><a name="p1772534422613"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8669134414263"></a>

Request

None.

**Example request**

None.

## Response<a name="section14669134411268"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section186704445268"></a>

[Table 2](#table1467214432612)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  2**  Status code

<a name="table1467214432612"></a>
<table><thead align="left"><tr id="row4725344202613"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p0725844142612"><a name="p0725844142612"></a><a name="p0725844142612"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p8725134442613"><a name="p8725134442613"></a><a name="p8725134442613"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row07251445263"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p15725244152611"><a name="p15725244152611"></a><a name="p15725244152611"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p4725164420266"><a name="p4725164420266"></a><a name="p4725164420266"></a>The instance is deleted successfully.</p>
</td>
</tr>
</tbody>
</table>

