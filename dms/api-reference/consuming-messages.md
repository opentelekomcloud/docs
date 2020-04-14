# Consuming Messages<a name="EN-US_TOPIC_0128036926"></a>

## Function<a name="section7322556"></a>

This API is used to consume messages in a specified queue. Multiple messages can be consumed at a time. The load of messages consumed each time cannot exceed 512 KB.

When there are only a few messages in a queue, the number of messages actually consumed at a time may be less than the message quantity specified in the consumption request. However, all messages in the queue will be eventually obtained by the message consumer after multiple rounds of consumption. If the queue is empty, no message will be returned to the consumer.

## URI<a name="section65903005"></a>

GET /v1.0/\{project\_id\}/queues/\{queue\_id\}/groups/\{consumer\_group\_id\}/messages?max\_msgs=\{max\_msgs\}&time\_wait=\{time\_wait\}&ack\_wait=\{ack\_wait\}

[Table 1](#d0e2446)  describes the parameters of this API. 

**Table  1**  Parameters

<a name="d0e2446"></a>
<table><thead align="left"><tr id="row57297510"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.6.1.1"><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.6.1.2"><p id="p24646311165331"><a name="p24646311165331"></a><a name="p24646311165331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.6.1.3"><p id="p52215961"><a name="p52215961"></a><a name="p52215961"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.6.1.4"><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.2.6.1.5"><p id="p11854244165326"><a name="p11854244165326"></a><a name="p11854244165326"></a>Value Range</p>
</th>
</tr>
</thead>
<tbody><tr id="row65280430"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p53223490"><a name="p53223490"></a><a name="p53223490"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p39198951165331"><a name="p39198951165331"></a><a name="p39198951165331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p16135397"><a name="p16135397"></a><a name="p16135397"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p31898818"><a name="p31898818"></a><a name="p31898818"></a>Indicates the ID of a project.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p20669698165326"><a name="p20669698165326"></a><a name="p20669698165326"></a>N/A</p>
</td>
</tr>
<tr id="row18653909"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p34571641"><a name="p34571641"></a><a name="p34571641"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p54768228165331"><a name="p54768228165331"></a><a name="p54768228165331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p48839530"><a name="p48839530"></a><a name="p48839530"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p63687823"><a name="p63687823"></a><a name="p63687823"></a>Indicates the queue ID.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p63632845165326"><a name="p63632845165326"></a><a name="p63632845165326"></a>N/A</p>
</td>
</tr>
<tr id="row4444242816423"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p16267667113324"><a name="p16267667113324"></a><a name="p16267667113324"></a>consumer_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p42612627113324"><a name="p42612627113324"></a><a name="p42612627113324"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p29070772113324"><a name="p29070772113324"></a><a name="p29070772113324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p5922333113324"><a name="p5922333113324"></a><a name="p5922333113324"></a>Indicates the consumer group ID. Obtain the consumer group ID from the response message in <a href="viewing-all-consumer-groups-of-a-specified-queue.md">Viewing All Consumer Groups of a Specified Queue</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p9946999113324"><a name="p9946999113324"></a><a name="p9946999113324"></a>N/A</p>
</td>
</tr>
<tr id="row44326086164211"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p4228174316555"><a name="p4228174316555"></a><a name="p4228174316555"></a>max_msgs</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p226919016555"><a name="p226919016555"></a><a name="p226919016555"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p4958666416555"><a name="p4958666416555"></a><a name="p4958666416555"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p5709686316555"><a name="p5709686316555"></a><a name="p5709686316555"></a>Indicates the number of consumable messages that can be obtained per time.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p51481630174626"><a name="p51481630174626"></a><a name="p51481630174626"></a>Value range: 1–10.</p>
<p id="p156811159414"><a name="p156811159414"></a><a name="p156811159414"></a>Default Value: <strong id="b8101532412"><a name="b8101532412"></a><a name="b8101532412"></a>10</strong>.</p>
</td>
</tr>
<tr id="row38149710187"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p1155910472219"><a name="p1155910472219"></a><a name="p1155910472219"></a>time_wait</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p1955910452213"><a name="p1955910452213"></a><a name="p1955910452213"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p45591148226"><a name="p45591148226"></a><a name="p45591148226"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p455911492213"><a name="p455911492213"></a><a name="p455911492213"></a>Indicates the amount of time that the API call can wait for a message to arrive in the empty queue before returning an empty response.</p>
<p id="p0969165015424"><a name="p0969165015424"></a><a name="p0969165015424"></a>If a message is available during the wait period, the call will return the message consumption result immediately.</p>
<p id="p1856295294213"><a name="p1856295294213"></a><a name="p1856295294213"></a>If no message is available until the wait period expires, the call will return an empty response after the wait period expires.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p15591049224"><a name="p15591049224"></a><a name="p15591049224"></a>Value range: 1 to 60 seconds.</p>
<p id="p1755964102219"><a name="p1755964102219"></a><a name="p1755964102219"></a>Default value: <strong id="b11406297439"><a name="b11406297439"></a><a name="b11406297439"></a>3s</strong>.</p>
<p id="p1455994162215"><a name="p1455994162215"></a><a name="p1455994162215"></a>The default wait period is 3 seconds even if the API request does not carry the <strong id="b1993515074418"><a name="b1993515074418"></a><a name="b1993515074418"></a>time_wait</strong> parameter or the <strong id="b1235784164416"><a name="b1235784164416"></a><a name="b1235784164416"></a>time_wait</strong> parameter in the API request is left unspecified.</p>
</td>
</tr>
<tr id="row1252954811512"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.6.1.1 "><p id="p1353194817512"><a name="p1353194817512"></a><a name="p1353194817512"></a>ack_wait</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.2 "><p id="p553164812511"><a name="p553164812511"></a><a name="p553164812511"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.6.1.3 "><p id="p953118481950"><a name="p953118481950"></a><a name="p953118481950"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.6.1.4 "><p id="p1144613521859"><a name="p1144613521859"></a><a name="p1144613521859"></a>Indicates the timeout duration that the API call can wait for message consumption acknowledgement. The client needs to submit the message consumption acknowledgement within the specified time. If the message consumption is not acknowledged within this period of time, the system displays a message, indicating that message consumption acknowledgement has timed out or the handler is invalid. In this case, the system determines that the message fails to be consumed by default.</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.6.1.5 "><p id="p16531348858"><a name="p16531348858"></a><a name="p16531348858"></a>Value range: 15 to 300 seconds.</p>
<p id="p11734163412710"><a name="p11734163412710"></a><a name="p11734163412710"></a>Default value: <strong id="b0881172414458"><a name="b0881172414458"></a><a name="b0881172414458"></a>30s</strong>.</p>
<p id="p151106812"><a name="p151106812"></a><a name="p151106812"></a>If this parameter is left unspecified or empty, the default value <strong id="b1420062824515"><a name="b1420062824515"></a><a name="b1420062824515"></a>30s</strong> is used. </p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET v1.0/b78a90ae2a134b4b8b2ba30acab4e23a/queues/075ae7da-6ce5-4966-940c-17c19fb5175e/groups/g-5ec247fd-d4a2-4d4f-9876-e4ff3280c461/messages?max_msgs=10&ack_wait=30
```

## Request<a name="section56256135"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section36543171"></a>

**Response parameters**

[Table 2](#d0e2557)  and  [Table 3](#table11221821161432)  describe the response parameters.

**Table  2**  Response parameters

<a name="d0e2557"></a>
<table><thead align="left"><tr id="row26059286"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.1"><p id="p30427456"><a name="p30427456"></a><a name="p30427456"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.12%" id="mcps1.2.4.1.2"><p id="p48704899"><a name="p48704899"></a><a name="p48704899"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.199999999999996%" id="mcps1.2.4.1.3"><p id="p52782726"><a name="p52782726"></a><a name="p52782726"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47542385"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.2 "><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a>JSON object</p>
</td>
<td class="cellrowborder" valign="top" width="57.199999999999996%" headers="mcps1.2.4.1.3 "><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a>Indicates the message content.</p>
</td>
</tr>
<tr id="row44803986114625"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p7539317114635"><a name="p7539317114635"></a><a name="p7539317114635"></a>handler</p>
</td>
<td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.2 "><p id="p6704956114635"><a name="p6704956114635"></a><a name="p6704956114635"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.199999999999996%" headers="mcps1.2.4.1.3 "><p id="p6230592114635"><a name="p6230592114635"></a><a name="p6230592114635"></a>Indicates the message handler.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  message parameter description

<a name="table11221821161432"></a>
<table><thead align="left"><tr id="row23543717161432"><th class="cellrowborder" valign="top" width="21.12%" id="mcps1.2.4.1.1"><p id="p27992888161432"><a name="p27992888161432"></a><a name="p27992888161432"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.62%" id="mcps1.2.4.1.2"><p id="p52831493161432"><a name="p52831493161432"></a><a name="p52831493161432"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.26%" id="mcps1.2.4.1.3"><p id="p51492530161432"><a name="p51492530161432"></a><a name="p51492530161432"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45649083161432"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.1 "><p id="p6588213161432"><a name="p6588213161432"></a><a name="p6588213161432"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.2 "><p id="p63883227161432"><a name="p63883227161432"></a><a name="p63883227161432"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="56.26%" headers="mcps1.2.4.1.3 "><p id="p7158935161432"><a name="p7158935161432"></a><a name="p7158935161432"></a>Indicates the message body.</p>
</td>
</tr>
<tr id="row13504496161432"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.1 "><p id="p29095533183133"><a name="p29095533183133"></a><a name="p29095533183133"></a>attributes</p>
</td>
<td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.2 "><p id="p19302504161432"><a name="p19302504161432"></a><a name="p19302504161432"></a>JSON object</p>
</td>
<td class="cellrowborder" valign="top" width="56.26%" headers="mcps1.2.4.1.3 "><p id="p19998995161432"><a name="p19998995161432"></a><a name="p19998995161432"></a>Indicates the list of attributes.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
[{
  "message" : {
   "body" : {
    "foo" : "123="
   },
   "attributes": {
       "attribute1": "value1",
       "attribute2": "value2"
        }
  }, 
  "handler" : "eyJjZyI6Im15X2pzb25fZ3JvdXAiLCJjaSI6InJlc3QtY29uc3VtZXItYzNlNThiNjEtYzA0NC00NGJkLTkxM2ItZDgzNjljNmJhYTQxIiwiY291bnQiOjAsIm9mZnNldCI6MCwicCI6MCwidCI6InRlc3QyIn0="
 }, {
  "message" : {
   "body" : {
    "foo" : "123="
   },
   "attributes": {
       "attribute1": "value1",
       "attribute2": "value2"
        }
  },  
  "handler" : "eyJjZyI6Im15X2pzb25fZ3JvdXAiLCJjaSI6InJlc3QtY29uc3VtZXItYzNlNThiNjEtYzA0NC00NGJkLTkxM2ItZDgzNjljNmJhYTQxIiwiY291bnQiOjAsIm9mZnNldCI6MSwicCI6MCwidCI6InRlc3QyIn0="
 }
]
```

## Status Code<a name="section60453091"></a>

[Table 4](#d0e2611)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="d0e2611"></a>
<table><thead align="left"><tr id="row25779254"><th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.3.1.1"><p id="p7744859"><a name="p7744859"></a><a name="p7744859"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="80.45%" id="mcps1.2.3.1.2"><p id="p23353865"><a name="p23353865"></a><a name="p23353865"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12614887"><td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.3.1.1 "><p id="p15172893"><a name="p15172893"></a><a name="p15172893"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="80.45%" headers="mcps1.2.3.1.2 "><p id="p21044820"><a name="p21044820"></a><a name="p21044820"></a>The information is obtained successfully.</p>
</td>
</tr>
</tbody>
</table>

