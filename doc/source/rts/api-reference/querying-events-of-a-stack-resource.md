# Querying Events of a Stack Resource<a name="EN-US_TOPIC_0084581305"></a>

## Function<a name="en-us_topic_0057973142_section9336199"></a>

This API is used to query events of a stack resource.

## URI<a name="en-us_topic_0057973142_section16916929"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/resources/\{resource\_name\}/events

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b865719012339"><a name="b865719012339"></a><a name="b865719012339"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b19433152203318"><a name="b19433152203318"></a><a name="b19433152203318"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b935919319335"><a name="b935919319335"></a><a name="b935919319335"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b145520917335"><a name="b145520917335"></a><a name="b145520917335"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row161097438473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10658144911017"><a name="p10658144911017"></a><a name="p10658144911017"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1166014498107"><a name="p1166014498107"></a><a name="p1166014498107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p666214493103"><a name="p666214493103"></a><a name="p666214493103"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p76631349181010"><a name="p76631349181010"></a><a name="p76631349181010"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row131851844124918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p146651349161017"><a name="p146651349161017"></a><a name="p146651349161017"></a>stack_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1666614912100"><a name="p1666614912100"></a><a name="p1666614912100"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p106671249191011"><a name="p106671249191011"></a><a name="p106671249191011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p6668124912103"><a name="p6668124912103"></a><a name="p6668124912103"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="row04307962213"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12129567438"><a name="p12129567438"></a><a name="p12129567438"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1146461564314"><a name="p1146461564314"></a><a name="p1146461564314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p184668153435"><a name="p184668153435"></a><a name="p184668153435"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8469181518439"><a name="p8469181518439"></a><a name="p8469181518439"></a>Specifies the name of the resource in the stack.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973142_section18034640"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973142_section28094036"></a>

<a name="en-us_topic_0057973142_table19596697"></a>
<table><thead align="left"><tr id="en-us_topic_0057973142_row50957800"><th class="cellrowborder" valign="top" width="16.27837216278372%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b673734683310"><a name="b673734683310"></a><a name="b673734683310"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.11848815118488%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b1066410498333"><a name="b1066410498333"></a><a name="b1066410498333"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.27837216278372%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b19533135011339"><a name="b19533135011339"></a><a name="b19533135011339"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.32476752324767%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b0812115316339"><a name="b0812115316339"></a><a name="b0812115316339"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973142_row48089434"><td class="cellrowborder" valign="top" width="16.27837216278372%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p2930044"><a name="en-us_topic_0057973142_p2930044"></a><a name="en-us_topic_0057973142_p2930044"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="15.11848815118488%" headers="mcps1.1.5.1.2 "><p id="p1713651475811"><a name="p1713651475811"></a><a name="p1713651475811"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.27837216278372%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p36007027"><a name="en-us_topic_0057973142_p36007027"></a><a name="en-us_topic_0057973142_p36007027"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="52.32476752324767%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p18908415"><a name="en-us_topic_0057973142_p18908415"></a><a name="en-us_topic_0057973142_p18908415"></a>Specifies the events of a resource.</p>
</td>
</tr>
</tbody>
</table>

**events**  structure information

<a name="en-us_topic_0057973142_table55186660"></a>
<table><thead align="left"><tr id="en-us_topic_0057973142_row11951831"><th class="cellrowborder" valign="top" width="16.471647164716472%" id="mcps1.1.5.1.1"><p id="p74171140185520"><a name="p74171140185520"></a><a name="p74171140185520"></a><strong id="b11649103416"><a name="b11649103416"></a><a name="b11649103416"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.2"><p id="p8420174014552"><a name="p8420174014552"></a><a name="p8420174014552"></a><strong id="b176074113411"><a name="b176074113411"></a><a name="b176074113411"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.471647164716472%" id="mcps1.1.5.1.3"><p id="p1423184015515"><a name="p1423184015515"></a><a name="p1423184015515"></a><strong id="b1443414743411"><a name="b1443414743411"></a><a name="b1443414743411"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.76517651765175%" id="mcps1.1.5.1.4"><p id="p104321240175517"><a name="p104321240175517"></a><a name="p104321240175517"></a><strong id="b1877018912347"><a name="b1877018912347"></a><a name="b1877018912347"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973142_row6835688"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p16819822"><a name="en-us_topic_0057973142_p16819822"></a><a name="en-us_topic_0057973142_p16819822"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p1282910278567"><a name="p1282910278567"></a><a name="p1282910278567"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p20228341"><a name="en-us_topic_0057973142_p20228341"></a><a name="en-us_topic_0057973142_p20228341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p43923748"><a name="en-us_topic_0057973142_p43923748"></a><a name="en-us_topic_0057973142_p43923748"></a>Specifies the resource name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row59769418"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p9484678"><a name="en-us_topic_0057973142_p9484678"></a><a name="en-us_topic_0057973142_p9484678"></a>event_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p16829112715569"><a name="p16829112715569"></a><a name="p16829112715569"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p30061414"><a name="en-us_topic_0057973142_p30061414"></a><a name="en-us_topic_0057973142_p30061414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p67095859"><a name="en-us_topic_0057973142_p67095859"></a><a name="en-us_topic_0057973142_p67095859"></a>Specifies the time when an event occurs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row66991827"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p57628926"><a name="en-us_topic_0057973142_p57628926"></a><a name="en-us_topic_0057973142_p57628926"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p1582942715613"><a name="p1582942715613"></a><a name="p1582942715613"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p37431442"><a name="en-us_topic_0057973142_p37431442"></a><a name="en-us_topic_0057973142_p37431442"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p36357906"><a name="en-us_topic_0057973142_p36357906"></a><a name="en-us_topic_0057973142_p36357906"></a>Specifies the event URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row58785701"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p64021321"><a name="en-us_topic_0057973142_p64021321"></a><a name="en-us_topic_0057973142_p64021321"></a>logical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p10829192719564"><a name="p10829192719564"></a><a name="p10829192719564"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p18344506"><a name="en-us_topic_0057973142_p18344506"></a><a name="en-us_topic_0057973142_p18344506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p32111136"><a name="en-us_topic_0057973142_p32111136"></a><a name="en-us_topic_0057973142_p32111136"></a>Specifies the logical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row20564775"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p55134111"><a name="en-us_topic_0057973142_p55134111"></a><a name="en-us_topic_0057973142_p55134111"></a>resource_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p4829927175615"><a name="p4829927175615"></a><a name="p4829927175615"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p36677991"><a name="en-us_topic_0057973142_p36677991"></a><a name="en-us_topic_0057973142_p36677991"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p59022856"><a name="en-us_topic_0057973142_p59022856"></a><a name="en-us_topic_0057973142_p59022856"></a>Specifies the resource operation reason.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row61443660"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p10880577"><a name="en-us_topic_0057973142_p10880577"></a><a name="en-us_topic_0057973142_p10880577"></a>resource_status</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p13829192715563"><a name="p13829192715563"></a><a name="p13829192715563"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p8911530"><a name="en-us_topic_0057973142_p8911530"></a><a name="en-us_topic_0057973142_p8911530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p16730874"><a name="en-us_topic_0057973142_p16730874"></a><a name="en-us_topic_0057973142_p16730874"></a>Specifies the resource status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row16360140"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p50102968"><a name="en-us_topic_0057973142_p50102968"></a><a name="en-us_topic_0057973142_p50102968"></a>physical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p148297276563"><a name="p148297276563"></a><a name="p148297276563"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p31808604"><a name="en-us_topic_0057973142_p31808604"></a><a name="en-us_topic_0057973142_p31808604"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p54798319"><a name="en-us_topic_0057973142_p54798319"></a><a name="en-us_topic_0057973142_p54798319"></a>Specifies the physical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row23422824"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p18200597"><a name="en-us_topic_0057973142_p18200597"></a><a name="en-us_topic_0057973142_p18200597"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p982922719562"><a name="p982922719562"></a><a name="p982922719562"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p64962271"><a name="en-us_topic_0057973142_p64962271"></a><a name="en-us_topic_0057973142_p64962271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p9067240"><a name="en-us_topic_0057973142_p9067240"></a><a name="en-us_topic_0057973142_p9067240"></a>Specifies the event ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973142_section51519734"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/my_instance/events
```

## Response Example<a name="en-us_topic_0057973142_section61024423"></a>

```
{
    "events": [
        {
            "resource_name": "my_instance",
            "event_time": "2014-01-26T17:21:35Z",
            "links": [
                {
                    "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/my_instance/events/1304",
                    "rel": "self"
                }
            ],
            "logical_resource_id": "instacne_port",
            "resource_status_reason": "state changed",
            "resource_status": "CREATE_IN_PROGRESS",
            "physical_resource_id": null,
            "id": "1302"
        }
    ]
}
```

## Return Code<a name="en-us_topic_0057973142_section12348896"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table8571828153012"></a>
<table><thead align="left"><tr id="en-us_topic_0084581294_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581294_p129561510144"><a name="en-us_topic_0084581294_p129561510144"></a><a name="en-us_topic_0084581294_p129561510144"></a><strong id="en-us_topic_0084581294_b1235759101013"><a name="en-us_topic_0084581294_b1235759101013"></a><a name="en-us_topic_0084581294_b1235759101013"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581294_p4959810444"><a name="en-us_topic_0084581294_p4959810444"></a><a name="en-us_topic_0084581294_p4959810444"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581294_p9959161020418"><a name="en-us_topic_0084581294_p9959161020418"></a><a name="en-us_topic_0084581294_p9959161020418"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581294_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p896118101840"><a name="en-us_topic_0084581294_p896118101840"></a><a name="en-us_topic_0084581294_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1296211015416"><a name="en-us_topic_0084581294_p1296211015416"></a><a name="en-us_topic_0084581294_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p9963110146"><a name="en-us_topic_0084581294_p9963110146"></a><a name="en-us_topic_0084581294_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p18134027201912"><a name="en-us_topic_0084581294_p18134027201912"></a><a name="en-us_topic_0084581294_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1713419274191"><a name="en-us_topic_0084581294_p1713419274191"></a><a name="en-us_topic_0084581294_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p11134162718196"><a name="en-us_topic_0084581294_p11134162718196"></a><a name="en-us_topic_0084581294_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p125520290312"><a name="en-us_topic_0084581294_p125520290312"></a><a name="en-us_topic_0084581294_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
</tbody>
</table>

