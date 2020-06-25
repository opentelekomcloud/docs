# Creating a Queue<a name="EN-US_TOPIC_0128036860"></a>

## Function<a name="section27263117"></a>

By default, a maximum of 30 queues can be created for a project.

>![](/images/icon-note.gif) **NOTE:**   
>When a queue is created, it takes one to three seconds to initialize the queue. Therefore, if operations such as message production, message consumption, queue details query, consumer group creation, and queue deletion are performed immediately after a queue is created, the operations may fail. You are advised to perform these operations three seconds after creating the queue.  

## URI<a name="section44041463"></a>

POST /v1.0/\{project\_id\}/queues

[Table 1](#table39601516)  describes the parameter of this API.

**Table  1**  Parameter

<a name="table39601516"></a>
<table><thead align="left"><tr id="row48948360"><th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.1"><p id="p5394248"><a name="p5394248"></a><a name="p5394248"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.5.1.2"><p id="p34280961"><a name="p34280961"></a><a name="p34280961"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="22.56%" id="mcps1.2.5.1.3"><p id="p18033224165911"><a name="p18033224165911"></a><a name="p18033224165911"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="38.72%" id="mcps1.2.5.1.4"><p id="p25294426"><a name="p25294426"></a><a name="p25294426"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35582587"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.1 "><p id="p63617293"><a name="p63617293"></a><a name="p63617293"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.2 "><p id="p52727095"><a name="p52727095"></a><a name="p52727095"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.5.1.3 "><p id="p3057905165911"><a name="p3057905165911"></a><a name="p3057905165911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.72%" headers="mcps1.2.5.1.4 "><p id="p43036322"><a name="p43036322"></a><a name="p43036322"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section60828848"></a>

**Request parameters**

[Table 2](#d0e878)  describes the parameters.

**Table  2**  Request parameters

<a name="d0e878"></a>
<table><thead align="left"><tr id="row44853923"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p9289124"><a name="p9289124"></a><a name="p9289124"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p14221611"><a name="p14221611"></a><a name="p14221611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p11099805"><a name="p11099805"></a><a name="p11099805"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="p26669028"><a name="p26669028"></a><a name="p26669028"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12707688"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p22689808"><a name="p22689808"></a><a name="p22689808"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p25935173"><a name="p25935173"></a><a name="p25935173"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p20374254"><a name="p20374254"></a><a name="p20374254"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p39701876"><a name="p39701876"></a><a name="p39701876"></a>Indicates the unique name of a queue.</p>
<p id="p4496890016927"><a name="p4496890016927"></a><a name="p4496890016927"></a>The value is a string of 1 to 64 characters that contain letters, digits, hyphens (-), and underscores (_).</p>
<p id="p61735358"><a name="p61735358"></a><a name="p61735358"></a>The name cannot be modified once specified.</p>
</td>
</tr>
<tr id="row19439658134613"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1244055812467"><a name="p1244055812467"></a><a name="p1244055812467"></a>queue_mode</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p54401758204614"><a name="p54401758204614"></a><a name="p54401758204614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p114401858164617"><a name="p114401858164617"></a><a name="p114401858164617"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p0110116142420"><a name="p0110116142420"></a><a name="p0110116142420"></a>Indicates the queue type.</p>
<p id="p11896203502"><a name="p11896203502"></a><a name="p11896203502"></a>Options:</p>
<a name="ul144681030155011"></a><a name="ul144681030155011"></a><ul id="ul144681030155011"><li><strong id="b425512285169"><a name="b425512285169"></a><a name="b425512285169"></a>NORMAL</strong>: Standard queue, which supports high concurrency performance but cannot guarantee that messages are retrieved in the exact sequence as how they are received.</li><li><strong id="b89441827182010"><a name="b89441827182010"></a><a name="b89441827182010"></a>FIFO</strong>: First-in-first-out (FIFO) queue, which guarantees that messages are retrieved in the exact sequence as how they are received.</li><li><strong id="b77647472213"><a name="b77647472213"></a><a name="b77647472213"></a>KAFKA_HA</strong>: High-reliability Kafka queue. All message replicas are flushed to a disk synchronously, ensuring message reliability.</li><li><strong id="b1930249162211"><a name="b1930249162211"></a><a name="b1930249162211"></a>KAFKA_HT</strong>: High-throughput Kafka queue. All message replicas are flushed to a disk asynchronously, ensuring high performance.</li></ul>
<p id="p11333422519"><a name="p11333422519"></a><a name="p11333422519"></a>The default value is <strong id="b1158361715239"><a name="b1158361715239"></a><a name="b1158361715239"></a>NORMAL</strong>.</p>
</td>
</tr>
<tr id="row18747312"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p42137308"><a name="p42137308"></a><a name="p42137308"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p57678784"><a name="p57678784"></a><a name="p57678784"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p41469957"><a name="p41469957"></a><a name="p41469957"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p3623379"><a name="p3623379"></a><a name="p3623379"></a>Indicates the basic information about a queue.</p>
<p id="p29436884172957"><a name="p29436884172957"></a><a name="p29436884172957"></a>The value is a string of a maximum of 160 characters and cannot contain the angle brackets (&lt;&gt;).</p>
</td>
</tr>
<tr id="row156297194612"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p28911624134616"><a name="p28911624134616"></a><a name="p28911624134616"></a>redrive_policy</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p2891424174614"><a name="p2891424174614"></a><a name="p2891424174614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1789172484619"><a name="p1789172484619"></a><a name="p1789172484619"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p9853135543212"><a name="p9853135543212"></a><a name="p9853135543212"></a>This parameter is valid only when queue_mode is set to <strong id="b163181556152319"><a name="b163181556152319"></a><a name="b163181556152319"></a>NORMAL</strong> or <strong id="b14552195810234"><a name="b14552195810234"></a><a name="b14552195810234"></a>FIFO</strong>.</p>
<p id="p13507530144719"><a name="p13507530144719"></a><a name="p13507530144719"></a>This parameter specifies whether to enable dead letter messages. Dead letter messages are messages that cannot be normally consumed.</p>
<p id="p450710307473"><a name="p450710307473"></a><a name="p450710307473"></a>When a message fails to be consumed after the number of consumption attempts of this message reaches this value, DMS stores this message into the dead letter queue. This message will be retained in the deal letter queue for 72 hours. During this period, consumers can consume the dead letter message.</p>
<p id="p4507630124719"><a name="p4507630124719"></a><a name="p4507630124719"></a>Dead letter messages can be consumed only by the consumer group that generated these dead letter messages.</p>
<p id="p450714305477"><a name="p450714305477"></a><a name="p450714305477"></a>Dead letter messages of a FIFO queue are stored and consumed based on the FIFO sequence.</p>
<p id="p136001918497"><a name="p136001918497"></a><a name="p136001918497"></a>Options:</p>
<a name="ul1558923144913"></a><a name="ul1558923144913"></a><ul id="ul1558923144913"><li><strong id="b1625115309257"><a name="b1625115309257"></a><a name="b1625115309257"></a>enable</strong></li><li><strong id="b53320327255"><a name="b53320327255"></a><a name="b53320327255"></a>disable</strong></li></ul>
<p id="p77210820599"><a name="p77210820599"></a><a name="p77210820599"></a>The default value is <strong id="b993916326254"><a name="b993916326254"></a><a name="b993916326254"></a>disable</strong>.</p>
</td>
</tr>
<tr id="row12433014184617"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p4891824194610"><a name="p4891824194610"></a><a name="p4891824194610"></a>max_consume_count</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p98912024204615"><a name="p98912024204615"></a><a name="p98912024204615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1589152434611"><a name="p1589152434611"></a><a name="p1589152434611"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p111151651312"><a name="p111151651312"></a><a name="p111151651312"></a>This parameter is mandatory only when <strong id="b12158173952518"><a name="b12158173952518"></a><a name="b12158173952518"></a>redrive_policy</strong> is set to <strong id="b415812391254"><a name="b415812391254"></a><a name="b415812391254"></a>enable</strong>.</p>
<p id="p18346144854811"><a name="p18346144854811"></a><a name="p18346144854811"></a>Indicates the maximum number of allowed message consumption failures. When a message fails to be consumed after the number of consumption attempts of this message reaches this value, DMS stores this message into the dead letter queue.</p>
<p id="p1034684844819"><a name="p1034684844819"></a><a name="p1034684844819"></a>Value range: 1–100.</p>
</td>
</tr>
<tr id="row1453322163518"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p543112593510"><a name="p543112593510"></a><a name="p543112593510"></a>retention_hours</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p7431257350"><a name="p7431257350"></a><a name="p7431257350"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p5436252355"><a name="p5436252355"></a><a name="p5436252355"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p1570102312367"><a name="p1570102312367"></a><a name="p1570102312367"></a>Indicates the hours of storing messages in the Kafka queue.</p>
<p id="p27012238366"><a name="p27012238366"></a><a name="p27012238366"></a>This parameter is valid only when <strong id="b77481422619"><a name="b77481422619"></a><a name="b77481422619"></a>queue_mode</strong> is set to <strong id="b974121462617"><a name="b974121462617"></a><a name="b974121462617"></a>KAFKA_HA</strong> or <strong id="b10741914132611"><a name="b10741914132611"></a><a name="b10741914132611"></a>KAFKA_HT</strong>.</p>
<p id="p67042383617"><a name="p67042383617"></a><a name="p67042383617"></a>Value range: 1–72.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

Creating a FIFO queue:

```
{
  "name" : "queue-001",
  "description" : "This is a FIFO queue.",
  "queue_mode" : "FIFO",
  "redrive_policy" : "enable",
  "max_consume_count" : 3
}
```

Creating a Kafka queue:

```
{
  "name" : "queue-002",
  "description" : "This is a Kafka queue.",
  "queue_mode" : "KAFKA_HA",
  "retention_hours" : 36
}
```

## Response<a name="section10588721"></a>

**Response parameters**

[Table 3](#d0e950)  describes the response parameters.

**Table  3**  Response parameters

<a name="d0e950"></a>
<table><thead align="left"><tr id="row54890288"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p16928338"><a name="p16928338"></a><a name="p16928338"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.2"><p id="p29018124"><a name="p29018124"></a><a name="p29018124"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.4.1.3"><p id="p1657863"><a name="p1657863"></a><a name="p1657863"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row69227"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p5607390"><a name="p5607390"></a><a name="p5607390"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.2 "><p id="p51545483"><a name="p51545483"></a><a name="p51545483"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.3 "><p id="p14434584"><a name="p14434584"></a><a name="p14434584"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row62802394"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p53829147"><a name="p53829147"></a><a name="p53829147"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.2 "><p id="p65193616"><a name="p65193616"></a><a name="p65193616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.3 "><p id="p46191521"><a name="p46191521"></a><a name="p46191521"></a>Indicates the name of a queue.</p>
</td>
</tr>
<tr id="row14657447830"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p116574471838"><a name="p116574471838"></a><a name="p116574471838"></a>kafka_topic</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.2 "><p id="p1165716472318"><a name="p1165716472318"></a><a name="p1165716472318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.3 "><p id="p9866448184619"><a name="p9866448184619"></a><a name="p9866448184619"></a>This parameter is returned only for Kafka queues.</p>
<p id="p168109183485"><a name="p168109183485"></a><a name="p168109183485"></a>Indicates the Kafka topic ID when Kafka SDK is used.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

Creating a FIFO queue:

```
{
    "id": "9bf46390-38a2-462d-b392-4d5b2d519c55", 
    "name": "queue_001"
}
```

Creating a Kafka queue:

```
{
  "id" : "3ec7a4a2-541b-430a-9c2b-77fa4b64ed8",
  "name" : "queue_002",
  "kafka_topic" : "k-fdc60cfe407a4b2a96a498efda55c785-3ec7a4a2-541b-430a-9c2b-77fa4b64ed8"
}
```

## Status Code<a name="section28189627"></a>

[Table 4](#d0e1002)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="d0e1002"></a>
<table><thead align="left"><tr id="row21704116"><th class="cellrowborder" valign="top" width="18.23%" id="mcps1.2.3.1.1"><p id="p13202999"><a name="p13202999"></a><a name="p13202999"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="81.77%" id="mcps1.2.3.1.2"><p id="p62809978"><a name="p62809978"></a><a name="p62809978"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54443429"><td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.3.1.1 "><p id="p47841633"><a name="p47841633"></a><a name="p47841633"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="81.77%" headers="mcps1.2.3.1.2 "><p id="p49967061"><a name="p49967061"></a><a name="p49967061"></a>The queue is created successfully.</p>
</td>
</tr>
</tbody>
</table>

