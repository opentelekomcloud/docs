# Deleting a Single DCS Instance<a name="dcs-api-0312008"></a>

## Function<a name="section17272736165320"></a>

This API is used to delete a specified DCS instance to free up all resources occupied by the DCS instance.

## URI<a name="section2310177194512"></a>

DELETE /v1.0/\{project\_id\}/instances/\{instance\_id\}

[Table 1](#table4154121820350)  describes the parameter.

**Table  1**  Parameter description

<a name="table4154121820350"></a>
<table><thead align="left"><tr id="row17153191817358"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p993885712414"><a name="p993885712414"></a><a name="p993885712414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p215314189354"><a name="p215314189354"></a><a name="p215314189354"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1715320185352"><a name="p1715320185352"></a><a name="p1715320185352"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p215351873519"><a name="p215351873519"></a><a name="p215351873519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61531718163510"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p51531218183514"><a name="p51531218183514"></a><a name="p51531218183514"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p115311813514"><a name="p115311813514"></a><a name="p115311813514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p815391853510"><a name="p815391853510"></a><a name="p815391853510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1153818143518"><a name="p1153818143518"></a><a name="p1153818143518"></a>Project ID</p>
</td>
</tr>
<tr id="row111541118183517"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p161532018113520"><a name="p161532018113520"></a><a name="p161532018113520"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p015314181351"><a name="p015314181351"></a><a name="p015314181351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11153318123518"><a name="p11153318123518"></a><a name="p11153318123518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41533186358"><a name="p41533186358"></a><a name="p41533186358"></a>DCS instance ID</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section41195764519"></a>

**Request parameters**

None.

**Example request**

Request URL:

```
DELETE https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}
```

## Response<a name="section11426254461"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section5301161961211"></a>

[Table 2](#table8301101911215)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  2**  Status code

<a name="table8301101911215"></a>
<table><thead align="left"><tr id="row11302101915124"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p73021519101210"><a name="p73021519101210"></a><a name="p73021519101210"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p830281981219"><a name="p830281981219"></a><a name="p830281981219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16302121941211"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p63027192128"><a name="p63027192128"></a><a name="p63027192128"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p1302171916124"><a name="p1302171916124"></a><a name="p1302171916124"></a>DCS instances deleted successfully.</p>
</td>
</tr>
</tbody>
</table>

