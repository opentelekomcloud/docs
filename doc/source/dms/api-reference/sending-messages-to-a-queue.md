# Sending Messages to a Queue<a name="EN-US_TOPIC_0128036914"></a>

## Function<a name="section55852871"></a>

This API is used to send messages to a queue. Multiple messages can be sent at a time. The following requirements must be met:

-   A maximum of 10 messages can be sent at a time.
-   The aggregated size of messages sent at a time cannot exceed 512 KB.
-   In Kafka queues, messages are retained for 1 to 72 hours, depending on what you choose when creating a queue. In the other queues, messages are retained for at least 72 hours and will be deleted after expiry.

## URI<a name="section32913796"></a>

POST /v1.0/\{project\_id\}/queues/\{queue\_id\}/messages

[Table 1](#d0e2212)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e2212"></a>
<table><thead align="left"><tr id="row46703582"><th class="cellrowborder" valign="top" width="18.98%" id="mcps1.2.5.1.1"><p id="p24893793"><a name="p24893793"></a><a name="p24893793"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.5.1.2"><p id="p3131361"><a name="p3131361"></a><a name="p3131361"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p3649247217133"><a name="p3649247217133"></a><a name="p3649247217133"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44.37%" id="mcps1.2.5.1.4"><p id="p52313669"><a name="p52313669"></a><a name="p52313669"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9548790"><td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.2.5.1.1 "><p id="p35254491"><a name="p35254491"></a><a name="p35254491"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.2 "><p id="p37041500"><a name="p37041500"></a><a name="p37041500"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p4979573517133"><a name="p4979573517133"></a><a name="p4979573517133"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.5.1.4 "><p id="p47571555"><a name="p47571555"></a><a name="p47571555"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="row25490811"><td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.2.5.1.1 "><p id="p51489795"><a name="p51489795"></a><a name="p51489795"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.2 "><p id="p22895614155355"><a name="p22895614155355"></a><a name="p22895614155355"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p6230429017133"><a name="p6230429017133"></a><a name="p6230429017133"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.5.1.4 "><p id="p65633828"><a name="p65633828"></a><a name="p65633828"></a>Indicates the queue ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section204561591114"></a>

**Request parameters**

[Table 2](#table74562591114)  and  [Table 3](#table945725914117)  list the parameter description.

**Table  2**  Request parameters

<a name="table74562591114"></a>
<table><thead align="left"><tr id="row1045695919110"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p144561959711"><a name="p144561959711"></a><a name="p144561959711"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.2"><p id="p1345615918117"><a name="p1345615918117"></a><a name="p1345615918117"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.3"><p id="p74571559417"><a name="p74571559417"></a><a name="p74571559417"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.61%" id="mcps1.2.5.1.4"><p id="p4457165918111"><a name="p4457165918111"></a><a name="p4457165918111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20457205910118"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p1045715591017"><a name="p1045715591017"></a><a name="p1045715591017"></a>messages</p>
</td>
<td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.2 "><p id="p945716596120"><a name="p945716596120"></a><a name="p945716596120"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p54570591217"><a name="p54570591217"></a><a name="p54570591217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.2.5.1.4 "><p id="p54576591710"><a name="p54576591710"></a><a name="p54576591710"></a>Indicates the message list.</p>
</td>
</tr>
<tr id="row14885144917563"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p10886104935612"><a name="p10886104935612"></a><a name="p10886104935612"></a>returnId</p>
</td>
<td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.2 "><p id="p12887154965618"><a name="p12887154965618"></a><a name="p12887154965618"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p2887249145619"><a name="p2887249145619"></a><a name="p2887249145619"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.2.5.1.4 "><p id="p1887164915613"><a name="p1887164915613"></a><a name="p1887164915613"></a>Indicates whether to return a message ID after a message is sent successfully. The default value is <strong id="b11299215175714"><a name="b11299215175714"></a><a name="b11299215175714"></a>false</strong>. A message ID is returned only if the value is set to <strong id="b134561619105720"><a name="b134561619105720"></a><a name="b134561619105720"></a>true</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  messages parameter description

<a name="table945725914117"></a>
<table><thead align="left"><tr id="row84578591213"><th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.2.5.1.1"><p id="p12457115918111"><a name="p12457115918111"></a><a name="p12457115918111"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p84572591413"><a name="p84572591413"></a><a name="p84572591413"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.3"><p id="p145713592116"><a name="p145713592116"></a><a name="p145713592116"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.19%" id="mcps1.2.5.1.4"><p id="p845815591314"><a name="p845815591314"></a><a name="p845815591314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4458459514"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.5.1.1 "><p id="p04588591515"><a name="p04588591515"></a><a name="p04588591515"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p845815915112"><a name="p845815915112"></a><a name="p845815915112"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.3 "><p id="p11458659318"><a name="p11458659318"></a><a name="p11458659318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.5.1.4 "><p id="p10458185919118"><a name="p10458185919118"></a><a name="p10458185919118"></a>Indicates the message body.</p>
</td>
</tr>
<tr id="row114581659616"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.5.1.1 "><p id="p15458759311"><a name="p15458759311"></a><a name="p15458759311"></a>attributes</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p174586591111"><a name="p174586591111"></a><a name="p174586591111"></a>JSON object</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.3 "><p id="p1245811597112"><a name="p1245811597112"></a><a name="p1245811597112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.5.1.4 "><p id="p54583594112"><a name="p54583594112"></a><a name="p54583594112"></a>Indicates the list of attributes, including attribute names and values. This parameter is displayed only for standard queues and not for Kafka queues.</p>
<p id="p124581459912"><a name="p124581459912"></a><a name="p124581459912"></a>The attribute name must be unique for a message. </p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
    "messages" : [{
            "body" : "TEST11",
            "attributes" : {
                "attribute1" : "value1",
                "attribute2" : "value2"
            },
        }, {
            "body" : {
                "foo" : "test02"
            },
            "attributes" : {
                "attribute1" : "value1",
                "attribute2" : "value2"
            },
                    }
    ]
}
```

## Response<a name="section48771786"></a>

**Response parameters**

[Table 4](#d0e2557)  and  [Table 5](#table176130447818)  describe the response parameters.

**Table  4**  Response parameters

<a name="d0e2557"></a>
<table><thead align="left"><tr id="row26059286"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p30427456"><a name="p30427456"></a><a name="p30427456"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p48704899"><a name="p48704899"></a><a name="p48704899"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="p52782726"><a name="p52782726"></a><a name="p52782726"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47542385"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a>Indicates the message list.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  messages response parameter

<a name="table176130447818"></a>
<table><thead align="left"><tr id="row1062220441589"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p1962414445813"><a name="p1962414445813"></a><a name="p1962414445813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p16267441983"><a name="p16267441983"></a><a name="p16267441983"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.4.1.3"><p id="p1262914414813"><a name="p1262914414813"></a><a name="p1262914414813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row063216447810"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p16331544284"><a name="p16331544284"></a><a name="p16331544284"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p6635194415816"><a name="p6635194415816"></a><a name="p6635194415816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p8637124412811"><a name="p8637124412811"></a><a name="p8637124412811"></a>Indicates the error information.</p>
</td>
</tr>
<tr id="row583415014816"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p5835750781"><a name="p5835750781"></a><a name="p5835750781"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p4836650685"><a name="p4836650685"></a><a name="p4836650685"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p4836950784"><a name="p4836950784"></a><a name="p4836950784"></a>Indicates the error code (if any).</p>
</td>
</tr>
<tr id="row133968545811"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p839795420819"><a name="p839795420819"></a><a name="p839795420819"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1339720541184"><a name="p1339720541184"></a><a name="p1339720541184"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p193971154585"><a name="p193971154585"></a><a name="p193971154585"></a>Indicates the message sending status.</p>
<p id="p4939163611145"><a name="p4939163611145"></a><a name="p4939163611145"></a><strong id="b3914142720370"><a name="b3914142720370"></a><a name="b3914142720370"></a>0</strong>: Messages are successfully sent.</p>
<p id="p3260043171412"><a name="p3260043171412"></a><a name="p3260043171412"></a><strong id="b176813516372"><a name="b176813516372"></a><a name="b176813516372"></a>1</strong>: Messages failed to be sent. The <strong id="b9377854103719"><a name="b9377854103719"></a><a name="b9377854103719"></a>error</strong> and <strong id="b1069015803719"><a name="b1069015803719"></a><a name="b1069015803719"></a>error_code</strong> parameters indicate the cause of failure.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "messages" : [{
      "error" : null,
      "error_code" : null,
      "state" : 0
    }, {
      "error_code" : null,
      "state" : 0,
      "error" : null
    }
  ]
}
```

## Status Code<a name="section36292894"></a>

[Table 6](#d0e2377)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  6**  Status code

<a name="d0e2377"></a>
<table><thead align="left"><tr id="row34207804"><th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.3.1.1"><p id="p19368760"><a name="p19368760"></a><a name="p19368760"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="81.39%" id="mcps1.2.3.1.2"><p id="p25365761"><a name="p25365761"></a><a name="p25365761"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41360766"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.3.1.1 "><p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="81.39%" headers="mcps1.2.3.1.2 "><p id="p46853302"><a name="p46853302"></a><a name="p46853302"></a>Messages are sent successfully.</p>
</td>
</tr>
</tbody>
</table>

