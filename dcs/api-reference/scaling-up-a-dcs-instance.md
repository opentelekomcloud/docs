# Scaling Up a DCS Instance<a name="dcs-api-0312010"></a>

## Function<a name="section1119991614542"></a>

This API is used to scale up a DCS Redis instance in the  **Running**  state.

## URI<a name="section2310177194512"></a>

POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/extend

[Table 1](#table4154121820350)  describes the parameters.

**Table  1**  Parameter description

<a name="table4154121820350"></a>
<table><thead align="left"><tr id="row17153191817358"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p993885712414"><a name="p993885712414"></a><a name="p993885712414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p215314189354"><a name="p215314189354"></a><a name="p215314189354"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p1715320185352"><a name="p1715320185352"></a><a name="p1715320185352"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.2.5.1.4"><p id="p215351873519"><a name="p215351873519"></a><a name="p215351873519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61531718163510"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p51531218183514"><a name="p51531218183514"></a><a name="p51531218183514"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p115311813514"><a name="p115311813514"></a><a name="p115311813514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p815391853510"><a name="p815391853510"></a><a name="p815391853510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="p1153818143518"><a name="p1153818143518"></a><a name="p1153818143518"></a>Project ID.</p>
</td>
</tr>
<tr id="row1358873516587"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1137117202451"><a name="p1137117202451"></a><a name="p1137117202451"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p193715205458"><a name="p193715205458"></a><a name="p193715205458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p637142014512"><a name="p637142014512"></a><a name="p637142014512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="p53711207459"><a name="p53711207459"></a><a name="p53711207459"></a>Instance ID</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section41195764519"></a>

**Request parameters**

[Table 2](#table166993107405)  describes the request parameters.

**Table  2**  Parameter description

<a name="table166993107405"></a>
<table><thead align="left"><tr id="row7700310174015"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p770012105401"><a name="p770012105401"></a><a name="p770012105401"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p5700201018409"><a name="p5700201018409"></a><a name="p5700201018409"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p0700210154019"><a name="p0700210154019"></a><a name="p0700210154019"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="p9700610174018"><a name="p9700610174018"></a><a name="p9700610174018"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13700121010407"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p38321751124510"><a name="p38321751124510"></a><a name="p38321751124510"></a>new_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p198321551134517"><a name="p198321551134517"></a><a name="p198321551134517"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p38321751104511"><a name="p38321751104511"></a><a name="p38321751104511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p08324511459"><a name="p08324511459"></a><a name="p08324511459"></a>New specification (memory space) of the DCS instance. The new specification to which the DCS instance will be scaled up must be greater than the current specification. Unit: GB.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
POST https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/extend
```

```
{
   "new_capacity": 4
}
```

## Response<a name="section11426254461"></a>

**Response parameters**

None.

**Example response**

None.

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
<tbody><tr id="row182271411314"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p168231014739"><a name="p168231014739"></a><a name="p168231014739"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p38237146312"><a name="p38237146312"></a><a name="p38237146312"></a>DCS instance scaled up successfully.</p>
</td>
</tr>
</tbody>
</table>

