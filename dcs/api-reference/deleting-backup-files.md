# Deleting Backup Files<a name="dcs-api-0312024"></a>

## Function<a name="section10680121316113"></a>

This API is used to delete the files backed up by a DCS instance.

## URI<a name="section2310177194512"></a>

DELETE /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups/\{backup\_id\}

[Table 1](#table4154121820350)  describes the parameters.

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
<tr id="row18629154113017"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p169201512193020"><a name="p169201512193020"></a><a name="p169201512193020"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1792101211307"><a name="p1792101211307"></a><a name="p1792101211307"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1692111233017"><a name="p1692111233017"></a><a name="p1692111233017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p17921191213303"><a name="p17921191213303"></a><a name="p17921191213303"></a>ID of the backup record</p>
</td>
</tr>
</tbody>
</table>

Example

```
DELETE https://{dcs_endpoint}/v1.0/885cacf2d49d4bb6931ae668e9c07553/instances/e016385d-b9fa-4bf0-9f38-9379f4a5293f/backups/75509c85-50a6-4525-ad56-a1bb62e84570
```

## Request<a name="section41195764519"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section11426254461"></a>

**Response parameters**

[Table 2](#table5929344419)  describes the response parameters.

**Table  2**  Parameter description

<a name="table5929344419"></a>
<table><thead align="left"><tr id="row1173730448"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16173193104416"><a name="p16173193104416"></a><a name="p16173193104416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p1317316354420"><a name="p1317316354420"></a><a name="p1317316354420"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p111730318446"><a name="p111730318446"></a><a name="p111730318446"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1317316317449"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9174103184416"><a name="p9174103184416"></a><a name="p9174103184416"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p14174113184416"><a name="p14174113184416"></a><a name="p14174113184416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p81742364412"><a name="p81742364412"></a><a name="p81742364412"></a>Result of deleting the backup file</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "message": ""
}
```

## Status Code<a name="section5301161961211"></a>

[Table 3](#table8301101911215)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  3**  Status code

<a name="table8301101911215"></a>
<table><thead align="left"><tr id="row11302101915124"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p73021519101210"><a name="p73021519101210"></a><a name="p73021519101210"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p830281981219"><a name="p830281981219"></a><a name="p830281981219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16302121941211"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p63027192128"><a name="p63027192128"></a><a name="p63027192128"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p1302171916124"><a name="p1302171916124"></a><a name="p1302171916124"></a>Backup file deleted successfully.</p>
</td>
</tr>
</tbody>
</table>

