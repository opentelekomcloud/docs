# Viewing a Queue<a name="EN-US_TOPIC_0128036892"></a>

## Function<a name="section56913064"></a>

This API is used to view a specified queue.

## URI<a name="section42455531"></a>

GET /v1.0/\{project\_id\}/queues/\{queue\_id\}?include\_deadletter=\{include\_deadletter\}

[Table 1](#d0e1298)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e1298"></a>
<table><thead align="left"><tr id="row15337269"><th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.1"><p id="p34359256"><a name="p34359256"></a><a name="p34359256"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p31636323"><a name="p31636323"></a><a name="p31636323"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.3"><p id="p21037001707"><a name="p21037001707"></a><a name="p21037001707"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="51.48514851485149%" id="mcps1.2.5.1.4"><p id="p12405375"><a name="p12405375"></a><a name="p12405375"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row65311315"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.1 "><p id="p55725192"><a name="p55725192"></a><a name="p55725192"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p17446726"><a name="p17446726"></a><a name="p17446726"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.3 "><p id="p450625901707"><a name="p450625901707"></a><a name="p450625901707"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="51.48514851485149%" headers="mcps1.2.5.1.4 "><p id="p3898676"><a name="p3898676"></a><a name="p3898676"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row35088084"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.1 "><p id="p23562574"><a name="p23562574"></a><a name="p23562574"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p29520332"><a name="p29520332"></a><a name="p29520332"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.3 "><p id="p343942871707"><a name="p343942871707"></a><a name="p343942871707"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="51.48514851485149%" headers="mcps1.2.5.1.4 "><p id="p42336695"><a name="p42336695"></a><a name="p42336695"></a>Indicates the ID of the queue to be viewed.</p>
</td>
</tr>
<tr id="row04541414162110"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.1 "><p id="p945520145211"><a name="p945520145211"></a><a name="p945520145211"></a>include_deadletter</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p945551418216"><a name="p945551418216"></a><a name="p945551418216"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.3 "><p id="p10455161415212"><a name="p10455161415212"></a><a name="p10455161415212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="51.48514851485149%" headers="mcps1.2.5.1.4 "><p id="p1492232141413"><a name="p1492232141413"></a><a name="p1492232141413"></a>Indicates whether to list dead letter parameters in the response message.</p>
<p id="p1518912259144"><a name="p1518912259144"></a><a name="p1518912259144"></a>Options:</p>
<a name="ul1675218576164"></a><a name="ul1675218576164"></a><ul id="ul1675218576164"><li><strong id="b208301146267"><a name="b208301146267"></a><a name="b208301146267"></a>true</strong>: Include dead letter messages.</li><li><strong id="b98541715202619"><a name="b98541715202619"></a><a name="b98541715202619"></a>false</strong>: Do not include dead letter messages.</li></ul>
<p id="p7455614172114"><a name="p7455614172114"></a><a name="p7455614172114"></a>The default value is <strong id="b9772162020395"><a name="b9772162020395"></a><a name="b9772162020395"></a>false</strong>.</p>
<p id="p43161318121814"><a name="p43161318121814"></a><a name="p43161318121814"></a>Kafka queues do not support dead letter messages. This parameter is invalid for Kafka queues.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET v1.0/b78a90ae2a134b4b8b2ba30acab4e23a/queues/075ae7da-6ce5-4966-940c-17c19fb5175e?include_deadletter=true
```

## Request<a name="section46555465"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section16346001"></a>

**Response parameters**

[Table 2](#d0e1353)  describes the response parameters.

**Table  2**  Response parameters

<a name="d0e1353"></a>
<table><thead align="left"><tr id="row29858833"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p2646389"><a name="p2646389"></a><a name="p2646389"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p13030950"><a name="p13030950"></a><a name="p13030950"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p48873995"><a name="p48873995"></a><a name="p48873995"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66479500"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p16130451"><a name="p16130451"></a><a name="p16130451"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p31498117"><a name="p31498117"></a><a name="p31498117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1210700"><a name="p1210700"></a><a name="p1210700"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row10896307"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p10185684"><a name="p10185684"></a><a name="p10185684"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p19734077"><a name="p19734077"></a><a name="p19734077"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p54956439"><a name="p54956439"></a><a name="p54956439"></a>Indicates the queue name.</p>
</td>
</tr>
<tr id="row24845910"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p66361692"><a name="p66361692"></a><a name="p66361692"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p6587942"><a name="p6587942"></a><a name="p6587942"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p63861276"><a name="p63861276"></a><a name="p63861276"></a>Indicates the time when a queue is created.</p>
</td>
</tr>
<tr id="row37880580"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p48428136"><a name="p48428136"></a><a name="p48428136"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p30364973"><a name="p30364973"></a><a name="p30364973"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p43643771"><a name="p43643771"></a><a name="p43643771"></a>Indicates the basic information about a queue.</p>
</td>
</tr>
<tr id="row16596213193611"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p572212249363"><a name="p572212249363"></a><a name="p572212249363"></a>queue_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p872212415368"><a name="p872212415368"></a><a name="p872212415368"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p17722162411367"><a name="p17722162411367"></a><a name="p17722162411367"></a>Indicates the queue type.</p>
</td>
</tr>
<tr id="row57249620"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p6707649"><a name="p6707649"></a><a name="p6707649"></a>reservation</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p6448715"><a name="p6448715"></a><a name="p6448715"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p57454101112531"><a name="p57454101112531"></a><a name="p57454101112531"></a>Indicates the retention period (unit: min) of a message in a queue.</p>
</td>
</tr>
<tr id="row3493029"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p14499957"><a name="p14499957"></a><a name="p14499957"></a>max_msg_size_byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p33645886"><a name="p33645886"></a><a name="p33645886"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p40962215"><a name="p40962215"></a><a name="p40962215"></a>Indicates the maximum message size (unit: byte) that is allowed in a queue.</p>
</td>
</tr>
<tr id="row15946978161910"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5073242161916"><a name="p5073242161916"></a><a name="p5073242161916"></a>produced_messages</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p8279492161916"><a name="p8279492161916"></a><a name="p8279492161916"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p66659143161916"><a name="p66659143161916"></a><a name="p66659143161916"></a>Indicates the total number of messages in a queue.</p>
</td>
</tr>
<tr id="row89943117577"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p121121912578"><a name="p121121912578"></a><a name="p121121912578"></a>redrive_policy</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p72117192575"><a name="p72117192575"></a><a name="p72117192575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1456551674120"><a name="p1456551674120"></a><a name="p1456551674120"></a>Indicates whether to enable dead letter messages. This parameter is displayed only when <strong id="b14403345184013"><a name="b14403345184013"></a><a name="b14403345184013"></a>include_deadletter</strong> is set to <strong id="b240324564010"><a name="b240324564010"></a><a name="b240324564010"></a>true</strong>.</p>
<p id="p1426891234116"><a name="p1426891234116"></a><a name="p1426891234116"></a>Options:</p>
<a name="ul1521141935716"></a><a name="ul1521141935716"></a><ul id="ul1521141935716"><li><strong id="b123217467406"><a name="b123217467406"></a><a name="b123217467406"></a>enable</strong></li><li><strong id="b54038487401"><a name="b54038487401"></a><a name="b54038487401"></a>disable</strong></li></ul>
</td>
</tr>
<tr id="row850619178578"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p172114196571"><a name="p172114196571"></a><a name="p172114196571"></a>max_consume_count</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p12211181915715"><a name="p12211181915715"></a><a name="p12211181915715"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1421121945714"><a name="p1421121945714"></a><a name="p1421121945714"></a>Indicates the maximum number of allowed message consumption failures. When a message fails to be consumed after the number of consumption attempts of this message reaches this value, DMS stores this message into the dead letter queue.</p>
<p id="p148142542710"><a name="p148142542710"></a><a name="p148142542710"></a>This parameter is displayed only when <strong id="b1927835624016"><a name="b1927835624016"></a><a name="b1927835624016"></a>include_deadletter</strong> is set to <strong id="b1227845664017"><a name="b1227845664017"></a><a name="b1227845664017"></a>true</strong>. </p>
</td>
</tr>
<tr id="row11309125613916"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1631025617919"><a name="p1631025617919"></a><a name="p1631025617919"></a>group_count</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p431017565912"><a name="p431017565912"></a><a name="p431017565912"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1631025610918"><a name="p1631025610918"></a><a name="p1631025610918"></a>Indicates the number of consumption groups in a queue.</p>
</td>
</tr>
<tr id="row188211471357"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p156498501057"><a name="p156498501057"></a><a name="p156498501057"></a>kafka_topic</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1464985016511"><a name="p1464985016511"></a><a name="p1464985016511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p064910501850"><a name="p064910501850"></a><a name="p064910501850"></a>This parameter is returned only for Kafka queues.</p>
</td>
</tr>
<tr id="row133258864715"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2032610854719"><a name="p2032610854719"></a><a name="p2032610854719"></a>eff_date</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p632611811479"><a name="p632611811479"></a><a name="p632611811479"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p1932620894713"><a name="p1932620894713"></a><a name="p1932620894713"></a>Indicates the time when a queue is created.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "id": "0611d466-a327-4b7b-8034-f84a0f6a6f42",
    "name": "queue-001",
    "description": "This is a FIFO queue.",
    "reservation": 4320,
    "created": 1558691803000,
    "queue_mode": "FIFO",
    "max_msg_size_byte": 524288,
    "produced_messages": 14,
    "eff_date": 1558691803000,
    "group_count": 1
}
```

## Status Code<a name="section12896286"></a>

[Table 3](#d0e1445)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  3**  Status code

<a name="d0e1445"></a>
<table><thead align="left"><tr id="row28263486"><th class="cellrowborder" valign="top" width="24.25%" id="mcps1.2.3.1.1"><p id="p7641038"><a name="p7641038"></a><a name="p7641038"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="75.75%" id="mcps1.2.3.1.2"><p id="p14944322"><a name="p14944322"></a><a name="p14944322"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2530563"><td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.3.1.1 "><p id="p45939957113132"><a name="p45939957113132"></a><a name="p45939957113132"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="75.75%" headers="mcps1.2.3.1.2 "><p id="p30148997113132"><a name="p30148997113132"></a><a name="p30148997113132"></a>The information is obtained successfully.</p>
</td>
</tr>
</tbody>
</table>

