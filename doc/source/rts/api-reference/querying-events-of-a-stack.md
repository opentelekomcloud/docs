# Querying Events of a Stack<a name="EN-US_TOPIC_0084581303"></a>

## Function<a name="en-us_topic_0057973139_section51259304"></a>

This API is used to query events of a stack.

## URI<a name="en-us_topic_0057973139_section58680553"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/events

>![](/images/icon-note.gif) **NOTE:**   
>This API supports redirection. During the calling, you can specify only  **stack\_name**  or  **stack\_id**.  

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b8951165216427"><a name="b8951165216427"></a><a name="b8951165216427"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b573285412423"><a name="b573285412423"></a><a name="b573285412423"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b05243551425"><a name="b05243551425"></a><a name="b05243551425"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b8694165914216"><a name="b8694165914216"></a><a name="b8694165914216"></a>Description</strong></p>
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
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973139_section58362934"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973139_section55504358"></a>

<a name="en-us_topic_0057973139_table7572542"></a>
<table><thead align="left"><tr id="en-us_topic_0057973139_row47059925"><th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1441362413433"><a name="b1441362413433"></a><a name="b1441362413433"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.46835316468353%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b1184712764314"><a name="b1184712764314"></a><a name="b1184712764314"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b414773244319"><a name="b414773244319"></a><a name="b414773244319"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.23517648235177%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b389462015447"><a name="b389462015447"></a><a name="b389462015447"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973139_row21093759"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p30872890"><a name="en-us_topic_0057973139_p30872890"></a><a name="en-us_topic_0057973139_p30872890"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p1296515499512"><a name="p1296515499512"></a><a name="p1296515499512"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p17676166"><a name="en-us_topic_0057973139_p17676166"></a><a name="en-us_topic_0057973139_p17676166"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p9211119"><a name="en-us_topic_0057973139_p9211119"></a><a name="en-us_topic_0057973139_p9211119"></a>Specifies the events of a resource.</p>
</td>
</tr>
</tbody>
</table>

**events**  structure information

<a name="en-us_topic_0057973139_table7903197"></a>
<table><thead align="left"><tr id="en-us_topic_0057973139_row1713707"><th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.1"><p id="p10209421195519"><a name="p10209421195519"></a><a name="p10209421195519"></a><strong id="b161954397447"><a name="b161954397447"></a><a name="b161954397447"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.46835316468353%" id="mcps1.1.5.1.2"><p id="p12211112165515"><a name="p12211112165515"></a><a name="p12211112165515"></a><strong id="b7306142882718"><a name="b7306142882718"></a><a name="b7306142882718"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.3"><p id="p12126212556"><a name="p12126212556"></a><a name="p12126212556"></a><strong id="b86011732142717"><a name="b86011732142717"></a><a name="b86011732142717"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.23517648235177%" id="mcps1.1.5.1.4"><p id="p82171321135511"><a name="p82171321135511"></a><a name="p82171321135511"></a><strong id="b4423235162716"><a name="b4423235162716"></a><a name="b4423235162716"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973139_row4374541"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p18793566"><a name="en-us_topic_0057973139_p18793566"></a><a name="en-us_topic_0057973139_p18793566"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p17436313144912"><a name="p17436313144912"></a><a name="p17436313144912"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p45883916"><a name="en-us_topic_0057973139_p45883916"></a><a name="en-us_topic_0057973139_p45883916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p61121949"><a name="en-us_topic_0057973139_p61121949"></a><a name="en-us_topic_0057973139_p61121949"></a>Specifies the resource name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row13226632"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p64724309"><a name="en-us_topic_0057973139_p64724309"></a><a name="en-us_topic_0057973139_p64724309"></a>event_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p1243601374911"><a name="p1243601374911"></a><a name="p1243601374911"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p8177666"><a name="en-us_topic_0057973139_p8177666"></a><a name="en-us_topic_0057973139_p8177666"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p33686045"><a name="en-us_topic_0057973139_p33686045"></a><a name="en-us_topic_0057973139_p33686045"></a>Specifies the time when an event occurs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row34738954"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p62391867"><a name="en-us_topic_0057973139_p62391867"></a><a name="en-us_topic_0057973139_p62391867"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p134363137498"><a name="p134363137498"></a><a name="p134363137498"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p20576498"><a name="en-us_topic_0057973139_p20576498"></a><a name="en-us_topic_0057973139_p20576498"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p46478091"><a name="en-us_topic_0057973139_p46478091"></a><a name="en-us_topic_0057973139_p46478091"></a>Specifies the event URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row15649642"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p59661499"><a name="en-us_topic_0057973139_p59661499"></a><a name="en-us_topic_0057973139_p59661499"></a>logical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p1843613131498"><a name="p1843613131498"></a><a name="p1843613131498"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p743252"><a name="en-us_topic_0057973139_p743252"></a><a name="en-us_topic_0057973139_p743252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p44644225"><a name="en-us_topic_0057973139_p44644225"></a><a name="en-us_topic_0057973139_p44644225"></a>Specifies the logical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row66253707"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p64950021"><a name="en-us_topic_0057973139_p64950021"></a><a name="en-us_topic_0057973139_p64950021"></a>resource_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p144361813114913"><a name="p144361813114913"></a><a name="p144361813114913"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p26460331"><a name="en-us_topic_0057973139_p26460331"></a><a name="en-us_topic_0057973139_p26460331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p62715550"><a name="en-us_topic_0057973139_p62715550"></a><a name="en-us_topic_0057973139_p62715550"></a>Specifies the resource operation reason.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row27569044"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p18500114"><a name="en-us_topic_0057973139_p18500114"></a><a name="en-us_topic_0057973139_p18500114"></a>resource_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p2436161316494"><a name="p2436161316494"></a><a name="p2436161316494"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p22114240"><a name="en-us_topic_0057973139_p22114240"></a><a name="en-us_topic_0057973139_p22114240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p2165197"><a name="en-us_topic_0057973139_p2165197"></a><a name="en-us_topic_0057973139_p2165197"></a>Specifies the resource status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row19486776"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p34925027"><a name="en-us_topic_0057973139_p34925027"></a><a name="en-us_topic_0057973139_p34925027"></a>physical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p174361213104911"><a name="p174361213104911"></a><a name="p174361213104911"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p10354914"><a name="en-us_topic_0057973139_p10354914"></a><a name="en-us_topic_0057973139_p10354914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p24422654"><a name="en-us_topic_0057973139_p24422654"></a><a name="en-us_topic_0057973139_p24422654"></a>Specifies the physical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973139_row18477295"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973139_p20265921"><a name="en-us_topic_0057973139_p20265921"></a><a name="en-us_topic_0057973139_p20265921"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p4436111314918"><a name="p4436111314918"></a><a name="p4436111314918"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973139_p30926891"><a name="en-us_topic_0057973139_p30926891"></a><a name="en-us_topic_0057973139_p30926891"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973139_p41240810"><a name="en-us_topic_0057973139_p41240810"></a><a name="en-us_topic_0057973139_p41240810"></a>Specifies the event ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973139_section29777180"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/events
```

## Response Example<a name="en-us_topic_0057973139_section66668032"></a>

```
{
    "events": [
        {
            "resource_name": "instacne_port",
            "event_time": "2014-01-26T17:21:35Z",
            "links": [
                {
                     "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/instacne_port/events/1302",
                     "rel": "self"
                },
                {
                     "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/instacne_port",
                     "rel": "resource"
                 },
                 {
                     "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                     "rel": "stack"
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

## Return Code<a name="en-us_topic_0057973139_section63141379"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581290_b731785218616"><a name="en-us_topic_0084581290_b731785218616"></a><a name="en-us_topic_0084581290_b731785218616"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"></a>Request was successful.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row18143162895914"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p52068209206"><a name="en-us_topic_0084581290_p52068209206"></a><a name="en-us_topic_0084581290_p52068209206"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p52061120172014"><a name="en-us_topic_0084581290_p52061120172014"></a><a name="en-us_topic_0084581290_p52061120172014"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p620662018205"><a name="en-us_topic_0084581290_p620662018205"></a><a name="en-us_topic_0084581290_p620662018205"></a>The response is about redirection. The response header usually contains a location value that allows you to track the real location of the resource.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
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

