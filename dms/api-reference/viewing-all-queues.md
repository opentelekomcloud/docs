# Viewing All Queues<a name="EN-US_TOPIC_0128036909"></a>

## Function<a name="section1101770"></a>

This API is used to view all queues.

## URI<a name="section9915935"></a>

GET /v1.0/\{project\_id\}/queues?include\_deadletter=\{include\_deadletter\}

[Table 1](#table47050372)  describes the parameters of this API.

**Table  1**  Parameters

<a name="table47050372"></a>
<table><thead align="left"><tr id="row1301106"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.1"><p id="p38280736"><a name="p38280736"></a><a name="p38280736"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.2"><p id="p13731878"><a name="p13731878"></a><a name="p13731878"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.3"><p id="p62218062165936"><a name="p62218062165936"></a><a name="p62218062165936"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.61%" id="mcps1.2.5.1.4"><p id="p38540333"><a name="p38540333"></a><a name="p38540333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34759260"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.1 "><p id="p64036700"><a name="p64036700"></a><a name="p64036700"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p19590229"><a name="p19590229"></a><a name="p19590229"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p56595689165936"><a name="p56595689165936"></a><a name="p56595689165936"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.2.5.1.4 "><p id="p43304686"><a name="p43304686"></a><a name="p43304686"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="row68695510115"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.1 "><p id="p687013517117"><a name="p687013517117"></a><a name="p687013517117"></a>include_deadletter</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p2870175161118"><a name="p2870175161118"></a><a name="p2870175161118"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p1087010551115"><a name="p1087010551115"></a><a name="p1087010551115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.2.5.1.4 "><p id="p1492232141413"><a name="p1492232141413"></a><a name="p1492232141413"></a>Indicates whether to list dead letter parameters in the response message.</p>
<p id="p1518912259144"><a name="p1518912259144"></a><a name="p1518912259144"></a>Options:</p>
<a name="ul19345104191717"></a><a name="ul19345104191717"></a><ul id="ul19345104191717"><li><strong id="b7734164214264"><a name="b7734164214264"></a><a name="b7734164214264"></a>true</strong>: Include dead letter messages.</li><li><strong id="b11755134372617"><a name="b11755134372617"></a><a name="b11755134372617"></a>false</strong>: Do not include dead letter messages.</li></ul>
<p id="p58706551112"><a name="p58706551112"></a><a name="p58706551112"></a>The default value is <strong id="b12668304318"><a name="b12668304318"></a><a name="b12668304318"></a>false</strong>.</p>
<p id="p1641322642810"><a name="p1641322642810"></a><a name="p1641322642810"></a>Kafka queues do not support dead letter messages. This parameter is invalid for Kafka queues.</p>
</td>
</tr>
<tr id="row49479261277"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.1 "><p id="p8947826132719"><a name="p8947826132719"></a><a name="p8947826132719"></a>include_messages_num</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p1294962622716"><a name="p1294962622716"></a><a name="p1294962622716"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p094922620274"><a name="p094922620274"></a><a name="p094922620274"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.2.5.1.4 "><p id="p8719145115273"><a name="p8719145115273"></a><a name="p8719145115273"></a><strong id="b1790785793114"><a name="b1790785793114"></a><a name="b1790785793114"></a>true</strong>: Return the number of messages in all queues.</p>
<p id="p8949112611273"><a name="p8949112611273"></a><a name="p8949112611273"></a><strong id="b99431593210"><a name="b99431593210"></a><a name="b99431593210"></a>false</strong>: Do not return the number of messages in all queues.</p>
<p id="p76049232818"><a name="p76049232818"></a><a name="p76049232818"></a>The default value is <strong id="b59961093218"><a name="b59961093218"></a><a name="b59961093218"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET v1.0/b78a90ae2a134b4b8b2ba30acab4e23a/queues?&include_deadletter=true
```

## Request<a name="section22134555"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section64993271"></a>

**Response parameters**

[Table 2](#d0e1175)  and  [Table 3](#table43280018111533)  describe the response parameters.

**Table  2**  Response parameters

<a name="d0e1175"></a>
<table><thead align="left"><tr id="row37285554"><th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.4.1.1"><p id="p230999"><a name="p230999"></a><a name="p230999"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p18710936"><a name="p18710936"></a><a name="p18710936"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.64%" id="mcps1.2.4.1.3"><p id="p39190879"><a name="p39190879"></a><a name="p39190879"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20344593"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p37299352"><a name="p37299352"></a><a name="p37299352"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1348700"><a name="p1348700"></a><a name="p1348700"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.64%" headers="mcps1.2.4.1.3 "><p id="p42135876"><a name="p42135876"></a><a name="p42135876"></a>Indicates the total number of queues that belong to the tenant.</p>
</td>
</tr>
<tr id="row43678569"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p48303235"><a name="p48303235"></a><a name="p48303235"></a>queues</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p6479207111926"><a name="p6479207111926"></a><a name="p6479207111926"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.64%" headers="mcps1.2.4.1.3 "><p id="p29474473"><a name="p29474473"></a><a name="p29474473"></a>Indicates the total number of all queue arrays that belong to the tenant.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  queues parameters description

<a name="table43280018111533"></a>
<table><thead align="left"><tr id="row18624228111533"><th class="cellrowborder" valign="top" width="26.75%" id="mcps1.2.4.1.1"><p id="p32167499111533"><a name="p32167499111533"></a><a name="p32167499111533"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p55430618111533"><a name="p55430618111533"></a><a name="p55430618111533"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.830000000000005%" id="mcps1.2.4.1.3"><p id="p60695098111533"><a name="p60695098111533"></a><a name="p60695098111533"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49855097111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p11731095111533"><a name="p11731095111533"></a><a name="p11731095111533"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p10694649111533"><a name="p10694649111533"></a><a name="p10694649111533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p60960264111533"><a name="p60960264111533"></a><a name="p60960264111533"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row11771467111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p13964808111533"><a name="p13964808111533"></a><a name="p13964808111533"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p57407653111533"><a name="p57407653111533"></a><a name="p57407653111533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p19508298111533"><a name="p19508298111533"></a><a name="p19508298111533"></a>Indicates the queue name.</p>
</td>
</tr>
<tr id="row41356960111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p61579429111533"><a name="p61579429111533"></a><a name="p61579429111533"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p21877830111533"><a name="p21877830111533"></a><a name="p21877830111533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p27273837111533"><a name="p27273837111533"></a><a name="p27273837111533"></a>Indicates the time when a queue is created.</p>
</td>
</tr>
<tr id="row44137941111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p18403453111533"><a name="p18403453111533"></a><a name="p18403453111533"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p14284701111533"><a name="p14284701111533"></a><a name="p14284701111533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p16210142111533"><a name="p16210142111533"></a><a name="p16210142111533"></a>Indicates the basic information about a queue.</p>
</td>
</tr>
<tr id="row1186118380342"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p15861153819345"><a name="p15861153819345"></a><a name="p15861153819345"></a>queue_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1386117388341"><a name="p1386117388341"></a><a name="p1386117388341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p1386163811342"><a name="p1386163811342"></a><a name="p1386163811342"></a>Indicates the queue type.</p>
</td>
</tr>
<tr id="row11673554111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p6033831111533"><a name="p6033831111533"></a><a name="p6033831111533"></a>reservation</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p18978288111533"><a name="p18978288111533"></a><a name="p18978288111533"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p60846358111533"><a name="p60846358111533"></a><a name="p60846358111533"></a>Indicates the retention period (unit: min) of a message in a queue.</p>
</td>
</tr>
<tr id="row10746311111533"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p65144834111533"><a name="p65144834111533"></a><a name="p65144834111533"></a>max_msg_size_byte</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p42240206111533"><a name="p42240206111533"></a><a name="p42240206111533"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p66013522111533"><a name="p66013522111533"></a><a name="p66013522111533"></a>Indicates the maximum message size (unit: byte) that is allowed in a queue.</p>
</td>
</tr>
<tr id="row2522487516185"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p2994898516185"><a name="p2994898516185"></a><a name="p2994898516185"></a>produced_messages</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p994872416185"><a name="p994872416185"></a><a name="p994872416185"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p16689568161836"><a name="p16689568161836"></a><a name="p16689568161836"></a>Indicates the total number of messages in a queue.</p>
</td>
</tr>
<tr id="row320318378525"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p15791650175213"><a name="p15791650175213"></a><a name="p15791650175213"></a>redrive_policy</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p157913504520"><a name="p157913504520"></a><a name="p157913504520"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p85671612133611"><a name="p85671612133611"></a><a name="p85671612133611"></a>Indicates whether to enable dead letter messages. This parameter is displayed only when <strong id="b1614113376350"><a name="b1614113376350"></a><a name="b1614113376350"></a>include_deadletter</strong> is set to <strong id="b914183710354"><a name="b914183710354"></a><a name="b914183710354"></a>true</strong>.</p>
<p id="p209421372368"><a name="p209421372368"></a><a name="p209421372368"></a>Options:</p>
<a name="ul199092026205311"></a><a name="ul199092026205311"></a><ul id="ul199092026205311"><li><strong id="b12688154319356"><a name="b12688154319356"></a><a name="b12688154319356"></a>enable</strong></li><li><strong id="b415684773514"><a name="b415684773514"></a><a name="b415684773514"></a>disable</strong></li></ul>
</td>
</tr>
<tr id="row21213419528"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p957910506529"><a name="p957910506529"></a><a name="p957910506529"></a>max_consume_count</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1557985013524"><a name="p1557985013524"></a><a name="p1557985013524"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p19909162675312"><a name="p19909162675312"></a><a name="p19909162675312"></a>Indicates the maximum number of allowed message consumption failures. When a message fails to be consumed after the number of consumption attempts of this message reaches this value, DMS stores this message into the dead letter queue.</p>
<p id="p313032510151"><a name="p313032510151"></a><a name="p313032510151"></a>This parameter is displayed only when <strong id="b17442124913366"><a name="b17442124913366"></a><a name="b17442124913366"></a>include_deadletter</strong> is set to <strong id="b1744284993619"><a name="b1744284993619"></a><a name="b1744284993619"></a>true</strong>. </p>
</td>
</tr>
<tr id="row1953919208713"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p1254012020714"><a name="p1254012020714"></a><a name="p1254012020714"></a>group_count</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1554014201720"><a name="p1554014201720"></a><a name="p1554014201720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p1154032018718"><a name="p1154032018718"></a><a name="p1154032018718"></a>Indicates the number of consumption groups in a queue.</p>
</td>
</tr>
<tr id="row49361114131812"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="p2032610854719"><a name="p2032610854719"></a><a name="p2032610854719"></a>eff_date</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p632611811479"><a name="p632611811479"></a><a name="p632611811479"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p1932620894713"><a name="p1932620894713"></a><a name="p1932620894713"></a>Indicates the time when a queue is created.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "queues" : [{
      "id" : "ef808d2d-58c2-4a36-9e58-d018b2193f80",
      "name" : "aaa_fifo_525",
      "description" : "test_fifo_detail",
      "queue_mode" : "NORMAL",
      "reservation" : 4320,
      "created" : 1495701557000,
      "max_msg_size_byte" : 524288,
      "produced_messages" : 1,
      "redrive_policy" : "enable",
      "max_consume_count" : 3,
      "eff_date": 1495701557000,
      "group_count" : 0
    }, {
      "id" : "bc0ac1ec-a4d6-4490-84cb-9d475f1ec3c5",
      "name" : "aaa_normal_525",
      "description" : "test",
      "queue_mode" : "NORMAL",
      "reservation" : 4320,
      "created" : 1495701490000,
      "max_msg_size_byte" : 524288,
      "produced_messages" : 0,
      "redrive_policy" : "enable",
      "max_consume_count" : 3,
      "eff_date": 1495701490000,
      "group_count" : 0
    }, {
      "id" : "1aaf34d0-7bb0-43be-9b71-f4b719d7ca47",
      "name" : "queue-normal",
      "description" : null,
      "queue_mode" : "NORMAL",
      "reservation" : 4320,
      "created" : 1495447342000,
      "max_msg_size_byte" : 524288,
      "produced_messages" : 2,
      "redrive_policy" : "enable",
      "max_consume_count" : 3,
      "eff_date": 1495447342000,
      "group_count" : 0
    }, {
      "id" : "f685ed59-43f4-4cf9-b609-7f333820d72d",
      "name" : "queue-835807102",
      "description" : "",
      "reservation" : 2160,
      "created" : 1517379348000,
      "queue_mode" : "KAFKA_HA",
      "max_msg_size_byte" : 524288,
      "produced_messages" : 0,
      "eff_date": 1517379348000,
      "group_count" : 0
    }
  ],
  "total" : 4
}
```

## Status Code<a name="section48068532"></a>

[Table 4](#d0e1229)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="d0e1229"></a>
<table><thead align="left"><tr id="row63036484"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.2.3.1.1"><p id="p5681612"><a name="p5681612"></a><a name="p5681612"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="80.83%" id="mcps1.2.3.1.2"><p id="p57557412"><a name="p57557412"></a><a name="p57557412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31638772"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.3.1.1 "><p id="p12603749"><a name="p12603749"></a><a name="p12603749"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="80.83%" headers="mcps1.2.3.1.2 "><p id="p14270750"><a name="p14270750"></a><a name="p14270750"></a>The information is obtained successfully.</p>
</td>
</tr>
</tbody>
</table>

