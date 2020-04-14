# Querying a Topic in a Kafka Instance<a name="EN-US_TOPIC_0128036881"></a>

## Function<a name="section281017251256"></a>

This API is available for only Kafka instances.

This API is used to query details about a topic in a Kafka instance.

## URI<a name="section153934371214"></a>

URI format: GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/topics

[Table 1](#table163952313129)  describes the parameter.

**Table  1**  Parameter description

<a name="table163952313129"></a>
<table><thead align="left"><tr id="row2493193181217"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p249343171215"><a name="p249343171215"></a><a name="p249343171215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p1549383101214"><a name="p1549383101214"></a><a name="p1549383101214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p1249323141214"><a name="p1249323141214"></a><a name="p1249323141214"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p44932341212"><a name="p44932341212"></a><a name="p44932341212"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2493031124"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p8493153191215"><a name="p8493153191215"></a><a name="p8493153191215"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p18493103191215"><a name="p18493103191215"></a><a name="p18493103191215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p11493634127"><a name="p11493634127"></a><a name="p11493634127"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p114938311210"><a name="p114938311210"></a><a name="p114938311210"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row74931936127"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p049393171212"><a name="p049393171212"></a><a name="p049393171212"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1849319381212"><a name="p1849319381212"></a><a name="p1849319381212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p94938319125"><a name="p94938319125"></a><a name="p94938319125"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p1949316301217"><a name="p1949316301217"></a><a name="p1949316301217"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section540483191220"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section1740614351212"></a>

**Response parameters**

[Table 2](#table2407333125)  describes the parameter.

**Table  2**  Parameter description

<a name="table2407333125"></a>
<table><thead align="left"><tr id="row20493934122"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p16493437123"><a name="p16493437123"></a><a name="p16493437123"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p1849315317125"><a name="p1849315317125"></a><a name="p1849315317125"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p114931631122"><a name="p114931631122"></a><a name="p114931631122"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row349318361214"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p149316320122"><a name="p149316320122"></a><a name="p149316320122"></a>topics</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1949514321211"><a name="p1949514321211"></a><a name="p1949514321211"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p144951938128"><a name="p144951938128"></a><a name="p144951938128"></a>Indicates the list of topics.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description

<a name="table721516381617"></a>
<table><thead align="left"><tr id="row521819351615"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1421916319160"><a name="p1421916319160"></a><a name="p1421916319160"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p19220193181611"><a name="p19220193181611"></a><a name="p19220193181611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p42211734161"><a name="p42211734161"></a><a name="p42211734161"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row182259318164"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p82278351616"><a name="p82278351616"></a><a name="p82278351616"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p7227153111619"><a name="p7227153111619"></a><a name="p7227153111619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p52277361617"><a name="p52277361617"></a><a name="p52277361617"></a>Indicates the topic name.</p>
</td>
</tr>
<tr id="row13996111183611"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p723243121615"><a name="p723243121615"></a><a name="p723243121615"></a>replication</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p52321939169"><a name="p52321939169"></a><a name="p52321939169"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p52349310161"><a name="p52349310161"></a><a name="p52349310161"></a>Indicates the number of replicas, which is configured to ensure data reliability.</p>
</td>
</tr>
<tr id="row622718313161"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p132281318163"><a name="p132281318163"></a><a name="p132281318163"></a>partition</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p92304331618"><a name="p92304331618"></a><a name="p92304331618"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1023023101615"><a name="p1023023101615"></a><a name="p1023023101615"></a>Indicates the number of topic partitions, which is used to set the number of concurrently consumed messages.</p>
</td>
</tr>
<tr id="row102302321617"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1423419319167"><a name="p1423419319167"></a><a name="p1423419319167"></a>retention_time</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1023616315167"><a name="p1023616315167"></a><a name="p1023616315167"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1923619351613"><a name="p1923619351613"></a><a name="p1923619351613"></a>Indicates the retention period of a message.</p>
</td>
</tr>
<tr id="row1994501616482"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p126894217446"><a name="p126894217446"></a><a name="p126894217446"></a>sync_replication</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p12681342184417"><a name="p12681342184417"></a><a name="p12681342184417"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p62689423441"><a name="p62689423441"></a><a name="p62689423441"></a>Indicates whether to enable synchronous replication. After this function is enabled, the <strong id="b67657501264"><a name="b67657501264"></a><a name="b67657501264"></a>acks</strong> parameter on the producer client must be set to <strong id="b5765155092617"><a name="b5765155092617"></a><a name="b5765155092617"></a>–1</strong>. Otherwise, this parameter does not take effect.</p>
<p id="p192687429448"><a name="p192687429448"></a><a name="p192687429448"></a>By default, synchronous replication is disabled.</p>
</td>
</tr>
<tr id="row62340310167"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1123719314161"><a name="p1123719314161"></a><a name="p1123719314161"></a>sync_message_flush</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p3237235167"><a name="p3237235167"></a><a name="p3237235167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1923911315167"><a name="p1923911315167"></a><a name="p1923911315167"></a>Indicates whether to enable synchronous flushing. Synchronous flushing compromises performance.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "topics" : [{
      "id" : "haha",
      "replication" : 3,
      "partition" : 3,
      "retention_time" : 10,
      "sync_message_flush" : true,
      "sync_replication" : true
    }, {
      "id" : "xixi",
      "replication" : 3,
      "partition" : 3,
      "retention_time" : 10,
      "sync_message_flush" : true,
      "sync_replication" : true
    }
  ]
}
```

## Status Code<a name="section17430153151212"></a>

[Table 4](#table64308351212)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="table64308351212"></a>
<table><thead align="left"><tr id="row204961735122"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p3496133121"><a name="p3496133121"></a><a name="p3496133121"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p0496103161220"><a name="p0496103161220"></a><a name="p0496103161220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row949618381217"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p849618371213"><a name="p849618371213"></a><a name="p849618371213"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p24961391213"><a name="p24961391213"></a><a name="p24961391213"></a>The information is queried successfully.</p>
</td>
</tr>
</tbody>
</table>

