# Viewing All Consumer Groups of a Specified Queue<a name="EN-US_TOPIC_0128036916"></a>

## Function<a name="section58427690"></a>

This API is used to view all consumer groups of a specified queue. 

## URI<a name="section56087165"></a>

GET /v1.0/\{project\_id\}/queues/\{queue\_id\}/groups?include\_deadletter=\{include\_deadletter\}&include\_messages\_num=\{boolean\}&page\_size=\{page\_size\}&current\_page=\{current\_page\}

[Table 1](#d0e1978)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e1978"></a>
<table><thead align="left"><tr id="row5992637"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p647213801718"><a name="p647213801718"></a><a name="p647213801718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p15257500"><a name="p15257500"></a><a name="p15257500"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27898002"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p45145696"><a name="p45145696"></a><a name="p45145696"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p32922799"><a name="p32922799"></a><a name="p32922799"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p391918691718"><a name="p391918691718"></a><a name="p391918691718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p49501095"><a name="p49501095"></a><a name="p49501095"></a>Indicates the project ID.</p>
</td>
</tr>
<tr id="row42856673"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p48838504"><a name="p48838504"></a><a name="p48838504"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p63604780"><a name="p63604780"></a><a name="p63604780"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p496059171718"><a name="p496059171718"></a><a name="p496059171718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p51713556"><a name="p51713556"></a><a name="p51713556"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row22422372235"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p5242153717236"><a name="p5242153717236"></a><a name="p5242153717236"></a>include_deadletter</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p124243782310"><a name="p124243782310"></a><a name="p124243782310"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p3242143752316"><a name="p3242143752316"></a><a name="p3242143752316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p164021862249"><a name="p164021862249"></a><a name="p164021862249"></a>Indicates whether to list dead letter parameters in the response message. The default value is <strong id="b178495264918"><a name="b178495264918"></a><a name="b178495264918"></a>false</strong>.</p>
</td>
</tr>
<tr id="row1972216192917"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p17221665293"><a name="p17221665293"></a><a name="p17221665293"></a>page_size</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p47221622911"><a name="p47221622911"></a><a name="p47221622911"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p5530796315"><a name="p5530796315"></a><a name="p5530796315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p137227612918"><a name="p137227612918"></a><a name="p137227612918"></a>Indicates the number of consumer groups displayed on each page.</p>
<p id="p16548726113916"><a name="p16548726113916"></a><a name="p16548726113916"></a>If <strong id="b1199011010480"><a name="b1199011010480"></a><a name="b1199011010480"></a>page_size</strong> and <strong id="b17599713134812"><a name="b17599713134812"></a><a name="b17599713134812"></a>current_page</strong> are not set to a valid value at the same time, consumer groups displayed on all pages are queried by default.</p>
</td>
</tr>
<tr id="row13722156192910"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p1272216614292"><a name="p1272216614292"></a><a name="p1272216614292"></a>current_page</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p772216614291"><a name="p772216614291"></a><a name="p772216614291"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p1153212913112"><a name="p1153212913112"></a><a name="p1153212913112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p10722146102916"><a name="p10722146102916"></a><a name="p10722146102916"></a>Indicates the number of a page on which consumer groups are to be queried.</p>
<p id="p115682010124020"><a name="p115682010124020"></a><a name="p115682010124020"></a>If <strong id="b778703524819"><a name="b778703524819"></a><a name="b778703524819"></a>page_size</strong> and <strong id="b878773534819"><a name="b878773534819"></a><a name="b878773534819"></a>current_page</strong> are not set to a valid value at the same time, consumer groups displayed on all pages are queried by default.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
GET v1.0/b78a90ae2a134b4b8b2ba30acab4e23a/queues/075ae7da-6ce5-4966-940c-17c19fb5175e/groups?include_deadletter=true
```

## Request<a name="section35022440"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section46766508"></a>

**Response parameters**

[Table 2](#d0e2089)  and  [Table 3](#table6131701015544)  describe the response parameters.

**Table  2**  Response parameters

<a name="d0e2089"></a>
<table><thead align="left"><tr id="row37189853"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p59588135"><a name="p59588135"></a><a name="p59588135"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p61909621"><a name="p61909621"></a><a name="p61909621"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p48623408"><a name="p48623408"></a><a name="p48623408"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46181951"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p49750539"><a name="p49750539"></a><a name="p49750539"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p3261819"><a name="p3261819"></a><a name="p3261819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p62880759"><a name="p62880759"></a><a name="p62880759"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row29055926"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p4719792"><a name="p4719792"></a><a name="p4719792"></a>queue_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>Indicates the queue name.</p>
</td>
</tr>
<tr id="row63037959"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p5801050"><a name="p5801050"></a><a name="p5801050"></a>groups</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p32885552152316"><a name="p32885552152316"></a><a name="p32885552152316"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p46484021152316"><a name="p46484021152316"></a><a name="p46484021152316"></a>Indicates the consumer group list.</p>
</td>
</tr>
<tr id="row01241210193812"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1126111016388"><a name="p1126111016388"></a><a name="p1126111016388"></a>redrive_policy</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p95526143913"><a name="p95526143913"></a><a name="p95526143913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p11915111335014"><a name="p11915111335014"></a><a name="p11915111335014"></a>Indicates whether to enable dead letter messages. This parameter is displayed only when <strong id="b138354297497"><a name="b138354297497"></a><a name="b138354297497"></a>include_deadletter</strong> is set to <strong id="b2835929164919"><a name="b2835929164919"></a><a name="b2835929164919"></a>true</strong>.</p>
<p id="p118061454184911"><a name="p118061454184911"></a><a name="p118061454184911"></a>Options:</p>
<a name="ul185521014397"></a><a name="ul185521014397"></a><ul id="ul185521014397"><li><strong id="b594419382496"><a name="b594419382496"></a><a name="b594419382496"></a>enable</strong></li><li><strong id="b10335104054917"><a name="b10335104054917"></a><a name="b10335104054917"></a>disable</strong></li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **groups**  parameter description

<a name="table6131701015544"></a>
<table><thead align="left"><tr id="row1414270515544"><th class="cellrowborder" valign="top" width="27.88%" id="mcps1.2.4.1.1"><p id="p470844315544"><a name="p470844315544"></a><a name="p470844315544"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p4583962215544"><a name="p4583962215544"></a><a name="p4583962215544"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.76%" id="mcps1.2.4.1.3"><p id="p2202191415544"><a name="p2202191415544"></a><a name="p2202191415544"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4419434315544"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p2297201515544"><a name="p2297201515544"></a><a name="p2297201515544"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p4879390315544"><a name="p4879390315544"></a><a name="p4879390315544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p5999208015544"><a name="p5999208015544"></a><a name="p5999208015544"></a>Indicates the consumer group ID.</p>
</td>
</tr>
<tr id="row305781215544"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p4635623315544"><a name="p4635623315544"></a><a name="p4635623315544"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p6386737815544"><a name="p6386737815544"></a><a name="p6386737815544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p587512815544"><a name="p587512815544"></a><a name="p587512815544"></a>Indicates the name of a consumer group.</p>
</td>
</tr>
<tr id="row5287615315544"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p5510997215544"><a name="p5510997215544"></a><a name="p5510997215544"></a>produced_messages</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p3472275215544"><a name="p3472275215544"></a><a name="p3472275215544"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p6107952415544"><a name="p6107952415544"></a><a name="p6107952415544"></a>Indicates the total number of messages (not including the messages that have expired and been deleted) in a queue.</p>
</td>
</tr>
<tr id="row1284481115544"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p3379679115544"><a name="p3379679115544"></a><a name="p3379679115544"></a>consumed_messages</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p5318558415544"><a name="p5318558415544"></a><a name="p5318558415544"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p1306505315544"><a name="p1306505315544"></a><a name="p1306505315544"></a>Indicates the total number of messages that are successfully consumed.</p>
</td>
</tr>
<tr id="row5047661915544"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p6207433815544"><a name="p6207433815544"></a><a name="p6207433815544"></a>available_messages</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p6196547315544"><a name="p6196547315544"></a><a name="p6196547315544"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p5314744115544"><a name="p5314744115544"></a><a name="p5314744115544"></a>Indicates the accumulated number of normal messages available to the consumer group.</p>
</td>
</tr>
<tr id="row265512810599"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p1991510439591"><a name="p1991510439591"></a><a name="p1991510439591"></a>produced_deadletters</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p16915164312596"><a name="p16915164312596"></a><a name="p16915164312596"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p17915124335920"><a name="p17915124335920"></a><a name="p17915124335920"></a>Indicates the total number of dead letter messages generated by the consumer group. This parameter is displayed only when <strong id="b174304213529"><a name="b174304213529"></a><a name="b174304213529"></a>include_deadletter</strong> is set to <strong id="b643062145213"><a name="b643062145213"></a><a name="b643062145213"></a>true</strong>. </p>
</td>
</tr>
<tr id="row11747103305914"><td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.1 "><p id="p10915124365912"><a name="p10915124365912"></a><a name="p10915124365912"></a>available_deadletters</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p591614385917"><a name="p591614385917"></a><a name="p591614385917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p091614375914"><a name="p091614375914"></a><a name="p091614375914"></a>Indicates the accumulated number of dead letter messages not consumed in the consumer group. This parameter is displayed only when <strong id="b13758629155212"><a name="b13758629155212"></a><a name="b13758629155212"></a>include_deadletter</strong> is set to <strong id="b075832995219"><a name="b075832995219"></a><a name="b075832995219"></a>true</strong>. </p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "queue_name" : "queue-772289871",
    "groups" : [{
            "name" : "group-1690260950",
            "id" : "g-eb9305bb-5bec-4712-84ab-0a36fbe9c2c0",
            "consumed_messages" : 0,
            "available_messages" : 8,
            "produced_messages" : 10,
        }
    ],
    "redrive_policy" : "enable",
    "queue_id" : "f5b6dd28-08dd-4f0f-866c-2eadf6788163"
}
```

When  **include\_messages\_num**  is set to  **false**:

```
{
    "queue_name" : "queue-586845368",
    "groups" : [{
            "name" : "group-364417183",
            "id" : "g-33d53064-2ab9-4acc-8566-3faa8c8578bf",
            "consumed_messages" : 0,
            "available_messages" : 0,
            "produced_messages" : 0,
        }, {
            "name" : "group-1722391629",
            "id" : "g-876fc3a2-e8c1-4a81-af3e-9ef68e3e46cf",
            "consumed_messages" : 0,
            "available_messages" : 0,
            "produced_messages" : 0,
        }
    ],
    "queue_id" : "e7e6d7f6-c555-470a-b9ee-3175e3408250"
}
```

## Status Code<a name="section18245395"></a>

[Table 4](#d0e2143)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="d0e2143"></a>
<table><thead align="left"><tr id="row46146710"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.3.1.1"><p id="p46896054"><a name="p46896054"></a><a name="p46896054"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="77.25999999999999%" id="mcps1.2.3.1.2"><p id="p40484047"><a name="p40484047"></a><a name="p40484047"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57982344"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.3.1.1 "><p id="p66058249"><a name="p66058249"></a><a name="p66058249"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="77.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p49117947"><a name="p49117947"></a><a name="p49117947"></a>The information is obtained successfully.</p>
</td>
</tr>
</tbody>
</table>

