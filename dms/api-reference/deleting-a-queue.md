# Deleting a Queue<a name="EN-US_TOPIC_0128036925"></a>

## Function<a name="section66716254"></a>

This API is used to delete a specified queue. 

## URI<a name="section63575380"></a>

DELETE /v1.0/\{project\_id\}/queues/\{queue\_id\}

[Table 1](#d0e1514)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e1514"></a>
<table><thead align="left"><tr id="row5595356"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p50570707"><a name="p50570707"></a><a name="p50570707"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p2586631"><a name="p2586631"></a><a name="p2586631"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p4113828617026"><a name="p4113828617026"></a><a name="p4113828617026"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p8190559"><a name="p8190559"></a><a name="p8190559"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59455556"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p51170717"><a name="p51170717"></a><a name="p51170717"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p51187411"><a name="p51187411"></a><a name="p51187411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p6355303217026"><a name="p6355303217026"></a><a name="p6355303217026"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p52539597"><a name="p52539597"></a><a name="p52539597"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row3094327"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p49313939"><a name="p49313939"></a><a name="p49313939"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p35006119"><a name="p35006119"></a><a name="p35006119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p2504447617026"><a name="p2504447617026"></a><a name="p2504447617026"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p16923420"><a name="p16923420"></a><a name="p16923420"></a>Indicates the ID of the queue to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section35307513"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section49332166"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section41336317"></a>

[Table 2](#d0e1675)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  2**  Status code

<a name="d0e1675"></a>
<table><thead align="left"><tr id="row24171358"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p11722994"><a name="p11722994"></a><a name="p11722994"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p10038421"><a name="p10038421"></a><a name="p10038421"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7805810"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p28290863"><a name="p28290863"></a><a name="p28290863"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p9858548"><a name="p9858548"></a><a name="p9858548"></a>The queue is deleted successfully.</p>
</td>
</tr>
</tbody>
</table>

