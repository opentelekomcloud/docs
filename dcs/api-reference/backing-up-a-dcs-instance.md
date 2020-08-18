# Backing Up a DCS Instance<a name="dcs-api-0312020"></a>

## Function<a name="section1525575419919"></a>

This API is used to back up a specified DCS instance.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>Only master/standby and cluster DCS instances can be backed up and restored, while single-node instances cannot.

## URI<a name="section10627123311133"></a>

POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups

[Table 1](#table1899262913382)  describes the parameters.

**Table  1**  Parameter description

<a name="table1899262913382"></a>
<table><thead align="left"><tr id="row1599115293389"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15991152913819"><a name="p15991152913819"></a><a name="p15991152913819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p129916298387"><a name="p129916298387"></a><a name="p129916298387"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p13991142913384"><a name="p13991142913384"></a><a name="p13991142913384"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1991329193814"><a name="p1991329193814"></a><a name="p1991329193814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11992929163813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p159911329153817"><a name="p159911329153817"></a><a name="p159911329153817"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18992192943819"><a name="p18992192943819"></a><a name="p18992192943819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p9992172933814"><a name="p9992172933814"></a><a name="p9992172933814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p20992829103811"><a name="p20992829103811"></a><a name="p20992829103811"></a>Project ID.</p>
</td>
</tr>
<tr id="row17992929193810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1899282919384"><a name="p1899282919384"></a><a name="p1899282919384"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p15992229153810"><a name="p15992229153810"></a><a name="p15992229153810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p199921129133818"><a name="p199921129133818"></a><a name="p199921129133818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p199212910384"><a name="p199212910384"></a><a name="p199212910384"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17412144620133"></a>

**Request parameters**

[Table 2](#table153111335113816)  describes the request parameters.

**Table  2**  Parameter description

<a name="table153111335113816"></a>
<table><thead align="left"><tr id="row73117359383"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p1031043517387"><a name="p1031043517387"></a><a name="p1031043517387"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.2"><p id="p19310113593814"><a name="p19310113593814"></a><a name="p19310113593814"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.2.5.1.3"><p id="p93101035183813"><a name="p93101035183813"></a><a name="p93101035183813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.2.5.1.4"><p id="p173101235153817"><a name="p173101235153817"></a><a name="p173101235153817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1631133513386"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p287019311111"><a name="p287019311111"></a><a name="p287019311111"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.2 "><p id="p1387014311215"><a name="p1387014311215"></a><a name="p1387014311215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.3 "><p id="p287033113111"><a name="p287033113111"></a><a name="p287033113111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p1587016314112"><a name="p1587016314112"></a><a name="p1587016314112"></a>Description of DCS instance backup.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
POST https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/backups
```

```
{
    "remark": "Backup instances"
}
```

## Response<a name="section1417213312142"></a>

**Response parameters**

[Table 3](#table1861319576383)  describes the response parameter.

**Table  3**  Parameter description

<a name="table1861319576383"></a>
<table><thead align="left"><tr id="row1961225712388"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p136126577389"><a name="p136126577389"></a><a name="p136126577389"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p76121757113816"><a name="p76121757113816"></a><a name="p76121757113816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p26121157123820"><a name="p26121157123820"></a><a name="p26121157123820"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row166121557203812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1461218271754"><a name="p1461218271754"></a><a name="p1461218271754"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p6612727959"><a name="p6612727959"></a><a name="p6612727959"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p19612327552"><a name="p19612327552"></a><a name="p19612327552"></a>ID of the backup record</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "backup_id": "548ceeff-2cbb-47ab-9a1c-7b085a8c08d7"
}
```

## Status Code<a name="section4860101417132"></a>

[Table 4](#table486141410130)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table486141410130"></a>
<table><thead align="left"><tr id="row18616141139"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1986191418133"><a name="p1986191418133"></a><a name="p1986191418133"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p18861111415138"><a name="p18861111415138"></a><a name="p18861111415138"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row786131451312"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p6861114181311"><a name="p6861114181311"></a><a name="p6861114181311"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p48619143136"><a name="p48619143136"></a><a name="p48619143136"></a>Specified DCS instance backed up successfully.</p>
</td>
</tr>
</tbody>
</table>

