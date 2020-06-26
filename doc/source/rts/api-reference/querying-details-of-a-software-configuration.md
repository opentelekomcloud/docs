# Querying Details of a Software Configuration<a name="EN-US_TOPIC_0084581317"></a>

## Function<a name="en-us_topic_0057973156_section5314816"></a>

This API is used to query details of a software configuration.

## URI<a name="en-us_topic_0057973156_section47833347"></a>

GET /v1/\{project\_id\}/software\_configs/\{config\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b846223315422"><a name="b846223315422"></a><a name="b846223315422"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b934523417427"><a name="b934523417427"></a><a name="b934523417427"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b056635134218"><a name="b056635134218"></a><a name="b056635134218"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b4880153544213"><a name="b4880153544213"></a><a name="b4880153544213"></a>Description</strong></p>
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
<tr id="row15755181714553"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p88684234559"><a name="p88684234559"></a><a name="p88684234559"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p12870162385512"><a name="p12870162385512"></a><a name="p12870162385512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p2873923165513"><a name="p2873923165513"></a><a name="p2873923165513"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p487552315518"><a name="p487552315518"></a><a name="p487552315518"></a>Specifies the software configuration UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973156_section27846943"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973156_section49295902"></a>

<a name="table464673142115"></a>
<table><thead align="left"><tr id="row1664733112113"><th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1541316114313"><a name="b1541316114313"></a><a name="b1541316114313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b1662711717433"><a name="b1662711717433"></a><a name="b1662711717433"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b14955145614416"><a name="b14955145614416"></a><a name="b14955145614416"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b567258104413"><a name="b567258104413"></a><a name="b567258104413"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1364783192116"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="p19647113152119"><a name="p19647113152119"></a><a name="p19647113152119"></a>software_config</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.2 "><p id="p7979145611599"><a name="p7979145611599"></a><a name="p7979145611599"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="p764719302114"><a name="p764719302114"></a><a name="p764719302114"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p1764733182117"><a name="p1764733182117"></a><a name="p1764733182117"></a>Specifies the software configuration list.</p>
</td>
</tr>
</tbody>
</table>

**software\_config**  structure information

<a name="en-us_topic_0057973156_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0057973156_row14014710"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.1"><p id="p6251753105716"><a name="p6251753105716"></a><a name="p6251753105716"></a><strong id="b10352155034516"><a name="b10352155034516"></a><a name="b10352155034516"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.2"><p id="p52935320570"><a name="p52935320570"></a><a name="p52935320570"></a><strong id="b18673125116459"><a name="b18673125116459"></a><a name="b18673125116459"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p734105317574"><a name="p734105317574"></a><a name="p734105317574"></a><strong id="b14712145217453"><a name="b14712145217453"></a><a name="b14712145217453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.41%" id="mcps1.1.5.1.4"><p id="p204185315578"><a name="p204185315578"></a><a name="p204185315578"></a><strong id="b525835410453"><a name="b525835410453"></a><a name="b525835410453"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973156_row20801079"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p7165868"><a name="en-us_topic_0057973156_p7165868"></a><a name="en-us_topic_0057973156_p7165868"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p017621695812"><a name="p017621695812"></a><a name="p017621695812"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p43564458"><a name="en-us_topic_0057973156_p43564458"></a><a name="en-us_topic_0057973156_p43564458"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p9758302"><a name="en-us_topic_0057973156_p9758302"></a><a name="en-us_topic_0057973156_p9758302"></a>Specifies the software configuration input.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row20715858"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p262928"><a name="en-us_topic_0057973156_p262928"></a><a name="en-us_topic_0057973156_p262928"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p417601616581"><a name="p417601616581"></a><a name="p417601616581"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p21297211"><a name="en-us_topic_0057973156_p21297211"></a><a name="en-us_topic_0057973156_p21297211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p10347766"><a name="en-us_topic_0057973156_p10347766"></a><a name="en-us_topic_0057973156_p10347766"></a>Specifies the name of the software configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row26021030"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p27328647"><a name="en-us_topic_0057973156_p27328647"></a><a name="en-us_topic_0057973156_p27328647"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p1117631620582"><a name="p1117631620582"></a><a name="p1117631620582"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p66136793"><a name="en-us_topic_0057973156_p66136793"></a><a name="en-us_topic_0057973156_p66136793"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p64695278"><a name="en-us_topic_0057973156_p64695278"></a><a name="en-us_topic_0057973156_p64695278"></a>Specifies the software configuration output.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row45386595"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p52435602"><a name="en-us_topic_0057973156_p52435602"></a><a name="en-us_topic_0057973156_p52435602"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p417671620589"><a name="p417671620589"></a><a name="p417671620589"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p19425365"><a name="en-us_topic_0057973156_p19425365"></a><a name="en-us_topic_0057973156_p19425365"></a>Date Time</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p10090937"><a name="en-us_topic_0057973156_p10090937"></a><a name="en-us_topic_0057973156_p10090937"></a>Specifies the time when a configuration is created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row23709572"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p41427194"><a name="en-us_topic_0057973156_p41427194"></a><a name="en-us_topic_0057973156_p41427194"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p0176131655818"><a name="p0176131655818"></a><a name="p0176131655818"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p159560"><a name="en-us_topic_0057973156_p159560"></a><a name="en-us_topic_0057973156_p159560"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p40246671"><a name="en-us_topic_0057973156_p40246671"></a><a name="en-us_topic_0057973156_p40246671"></a>Specifies the name of the software configuration group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row26675721"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p13249808"><a name="en-us_topic_0057973156_p13249808"></a><a name="en-us_topic_0057973156_p13249808"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p017651645816"><a name="p017651645816"></a><a name="p017651645816"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p66601556"><a name="en-us_topic_0057973156_p66601556"></a><a name="en-us_topic_0057973156_p66601556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p26998705"><a name="en-us_topic_0057973156_p26998705"></a><a name="en-us_topic_0057973156_p26998705"></a>Specifies the software configuration code.</p>
</td>
</tr>
<tr id="en-us_topic_0057973156_row41661755"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973156_p19159022"><a name="en-us_topic_0057973156_p19159022"></a><a name="en-us_topic_0057973156_p19159022"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p917651685811"><a name="p917651685811"></a><a name="p917651685811"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973156_p8376929"><a name="en-us_topic_0057973156_p8376929"></a><a name="en-us_topic_0057973156_p8376929"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973156_p65981352"><a name="en-us_topic_0057973156_p65981352"></a><a name="en-us_topic_0057973156_p65981352"></a>Specifies configuration options.</p>
</td>
</tr>
<tr id="row763816221228"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="p263872210224"><a name="p263872210224"></a><a name="p263872210224"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p917612169585"><a name="p917612169585"></a><a name="p917612169585"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="p1638022112213"><a name="p1638022112213"></a><a name="p1638022112213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.41%" headers="mcps1.1.5.1.4 "><p id="p2638322132220"><a name="p2638322132220"></a><a name="p2638322132220"></a>Specifies the software configuration UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973156_section41009935"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/software_configs/40p72423093a900a8b7a669768421a6a
```

## Response Example<a name="en-us_topic_0057973156_section33545101"></a>

```
{
    "software_config": {
        "inputs": [
            {
                "default": null,
                "type": "String",
                "name": "foo",
                "description": null
            },
            {
                "default": null,
                "type": "String",
                "name": "bar",
                "description": null
            }
        ],
        "group": "script",
        "name": "a-config-we5zpvyu7b5o",
        "outputs": [
            {
                "type": "String",
                "name": "result",
                "error_output": false,
                "description": null
            }
        ],
        "creation_time": "2015-01-31T15:12:36Z",
        "id": "ddee7aca-aa32-4335-8265-d436b20db4f1",
        "config": "#!/bin/sh -x\necho \"Writing to /tmp/$bar\"\necho $foo > /tmp/$bar\necho -n \"The file /tmp/$bar contains `cat /tmp/$bar` for server $deploy_server_id during $deploy_action\" > $heat_outputs_path.result\necho \"Written to /tmp/$bar\"\necho \"Output to stderr\" 1>&2",
        "options": null
    }
}
```

## Return Code<a name="en-us_topic_0057973156_section33470456"></a>

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

