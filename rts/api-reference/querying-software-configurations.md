# Querying Software Configurations<a name="EN-US_TOPIC_0085277557"></a>

## Function<a name="en-us_topic_0085081114_section5314816"></a>

This API is used to query the software configurations.

## URI<a name="en-us_topic_0085081114_section47833347"></a>

GET /v1/\{project\_id\}/software\_configs

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b4428113023220"><a name="b4428113023220"></a><a name="b4428113023220"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b1384431133219"><a name="b1384431133219"></a><a name="b1384431133219"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b15218143283211"><a name="b15218143283211"></a><a name="b15218143283211"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b51816333325"><a name="b51816333325"></a><a name="b51816333325"></a>Description</strong></p>
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
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081114_section27846943"></a>

<a name="en-us_topic_0085081114_table2851385316"></a>
<table><thead align="left"><tr id="en-us_topic_0085081114_row711513185311"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b167781640133212"><a name="b167781640133212"></a><a name="b167781640133212"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b7665741103215"><a name="b7665741103215"></a><a name="b7665741103215"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b5638134263212"><a name="b5638134263212"></a><a name="b5638134263212"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b1901104314327"><a name="b1901104314327"></a><a name="b1901104314327"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b177331244153210"><a name="b177331244153210"></a><a name="b177331244153210"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081114_row416813155310"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081114_p81771311533"><a name="en-us_topic_0085081114_p81771311533"></a><a name="en-us_topic_0085081114_p81771311533"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1469622815313"><a name="p1469622815313"></a><a name="p1469622815313"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081114_p318121325314"><a name="en-us_topic_0085081114_p318121325314"></a><a name="en-us_topic_0085081114_p318121325314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081114_p11194136535"><a name="en-us_topic_0085081114_p11194136535"></a><a name="en-us_topic_0085081114_p11194136535"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081114_p020141335320"><a name="en-us_topic_0085081114_p020141335320"></a><a name="en-us_topic_0085081114_p020141335320"></a>Specifies the number of returned software configurations.</p>
</td>
</tr>
<tr id="en-us_topic_0085081114_row1120181355313"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081114_p11215136536"><a name="en-us_topic_0085081114_p11215136536"></a><a name="en-us_topic_0085081114_p11215136536"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p11696172815530"><a name="p11696172815530"></a><a name="p11696172815530"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081114_p17221413115315"><a name="en-us_topic_0085081114_p17221413115315"></a><a name="en-us_topic_0085081114_p17221413115315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081114_p1924313165320"><a name="en-us_topic_0085081114_p1924313165320"></a><a name="en-us_topic_0085081114_p1924313165320"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081114_p825413135312"><a name="en-us_topic_0085081114_p825413135312"></a><a name="en-us_topic_0085081114_p825413135312"></a>Specifies the software configuration from which the next data record starts to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0085081114_section49295902"></a>

<a name="table049473817172"></a>
<table><thead align="left"><tr id="row11494138141711"><th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.1"><p id="p173320367572"><a name="p173320367572"></a><a name="p173320367572"></a><strong id="b17546103093815"><a name="b17546103093815"></a><a name="b17546103093815"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.2"><p id="p335203620575"><a name="p335203620575"></a><a name="p335203620575"></a><strong id="b7456322382"><a name="b7456322382"></a><a name="b7456322382"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.3"><p id="p1037203619576"><a name="p1037203619576"></a><a name="p1037203619576"></a><strong id="b919123373813"><a name="b919123373813"></a><a name="b919123373813"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.18488151184882%" id="mcps1.1.5.1.4"><p id="p114113675711"><a name="p114113675711"></a><a name="p114113675711"></a><strong id="b124210341384"><a name="b124210341384"></a><a name="b124210341384"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1549443813176"><td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081114_p86617813216"><a name="en-us_topic_0085081114_p86617813216"></a><a name="en-us_topic_0085081114_p86617813216"></a>software_configs</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p1391819235614"><a name="p1391819235614"></a><a name="p1391819235614"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081114_p8661283216"><a name="en-us_topic_0085081114_p8661283216"></a><a name="en-us_topic_0085081114_p8661283216"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081114_p76617810215"><a name="en-us_topic_0085081114_p76617810215"></a><a name="en-us_topic_0085081114_p76617810215"></a>Specifies the software configuration objects.</p>
</td>
</tr>
</tbody>
</table>

**software\_configs**  structure information

<a name="en-us_topic_0085081114_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081114_row14014710"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.1"><p id="p157111839115716"><a name="p157111839115716"></a><a name="p157111839115716"></a><strong id="b1790164104011"><a name="b1790164104011"></a><a name="b1790164104011"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.290000000000001%" id="mcps1.1.5.1.2"><p id="p20713113915716"><a name="p20713113915716"></a><a name="p20713113915716"></a><strong id="b720212515409"><a name="b720212515409"></a><a name="b720212515409"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p1071618398570"><a name="p1071618398570"></a><a name="p1071618398570"></a><strong id="b12867694017"><a name="b12867694017"></a><a name="b12867694017"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.59%" id="mcps1.1.5.1.4"><p id="p4719203935710"><a name="p4719203935710"></a><a name="p4719203935710"></a><strong id="b11211794010"><a name="b11211794010"></a><a name="b11211794010"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081114_row20801079"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081114_p12660188322"><a name="en-us_topic_0085081114_p12660188322"></a><a name="en-us_topic_0085081114_p12660188322"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p1516157165620"><a name="p1516157165620"></a><a name="p1516157165620"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081114_p76601981927"><a name="en-us_topic_0085081114_p76601981927"></a><a name="en-us_topic_0085081114_p76601981927"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="p9523204141420"><a name="p9523204141420"></a><a name="p9523204141420"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen165994818143"><a name="screen165994818143"></a><a name="screen165994818143"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081114_row20715858"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081114_p36601981521"><a name="en-us_topic_0085081114_p36601981521"></a><a name="en-us_topic_0085081114_p36601981521"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p1116157195616"><a name="p1116157195616"></a><a name="p1116157195616"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081114_p1566068323"><a name="en-us_topic_0085081114_p1566068323"></a><a name="en-us_topic_0085081114_p1566068323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081114_p166604812220"><a name="en-us_topic_0085081114_p166604812220"></a><a name="en-us_topic_0085081114_p166604812220"></a>Specifies the name of the software configuration group.</p>
</td>
</tr>
<tr id="en-us_topic_0085081114_row26021030"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081114_p66601181021"><a name="en-us_topic_0085081114_p66601181021"></a><a name="en-us_topic_0085081114_p66601181021"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p19165710569"><a name="p19165710569"></a><a name="p19165710569"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081114_p2066058624"><a name="en-us_topic_0085081114_p2066058624"></a><a name="en-us_topic_0085081114_p2066058624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081114_p1066088321"><a name="en-us_topic_0085081114_p1066088321"></a><a name="en-us_topic_0085081114_p1066088321"></a>Specifies the software configuration UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081114_row45386595"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081114_p19660481229"><a name="en-us_topic_0085081114_p19660481229"></a><a name="en-us_topic_0085081114_p19660481229"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p151667105613"><a name="p151667105613"></a><a name="p151667105613"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081114_p96601681328"><a name="en-us_topic_0085081114_p96601681328"></a><a name="en-us_topic_0085081114_p96601681328"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081114_p6661108424"><a name="en-us_topic_0085081114_p6661108424"></a><a name="en-us_topic_0085081114_p6661108424"></a>Specifies the name of the software configuration.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081114_section41009935"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/software_configs
```

## Response Example<a name="en-us_topic_0085081114_section33545101"></a>

```
{
    "software_configs": [
        {
            "group": "script",
            "name": "a-config-we5zpvyu7b5o",
            "creation_time": "2015-01-31T15:12:36Z",
            "id": "ddee7aca-aa32-4335-8265-d436b20db4f1",
        }
    ]
}
```

## Return Code<a name="en-us_topic_0085081114_section33470456"></a>

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

<a name="table1296574815364"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_p129561510144"><a name="en-us_topic_0084581290_p129561510144"></a><a name="en-us_topic_0084581290_p129561510144"></a><strong id="en-us_topic_0084581290_b1552942884813"><a name="en-us_topic_0084581290_b1552942884813"></a><a name="en-us_topic_0084581290_b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_p4959810444"><a name="en-us_topic_0084581290_p4959810444"></a><a name="en-us_topic_0084581290_p4959810444"></a><strong id="en-us_topic_0084581290_b956007905"><a name="en-us_topic_0084581290_b956007905"></a><a name="en-us_topic_0084581290_b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_p9959161020418"><a name="en-us_topic_0084581290_p9959161020418"></a><a name="en-us_topic_0084581290_p9959161020418"></a><strong id="en-us_topic_0084581290_b359171417"><a name="en-us_topic_0084581290_b359171417"></a><a name="en-us_topic_0084581290_b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p896118101840"><a name="en-us_topic_0084581290_p896118101840"></a><a name="en-us_topic_0084581290_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1296211015416"><a name="en-us_topic_0084581290_p1296211015416"></a><a name="en-us_topic_0084581290_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p9963110146"><a name="en-us_topic_0084581290_p9963110146"></a><a name="en-us_topic_0084581290_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p18134027201912"><a name="en-us_topic_0084581290_p18134027201912"></a><a name="en-us_topic_0084581290_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1713419274191"><a name="en-us_topic_0084581290_p1713419274191"></a><a name="en-us_topic_0084581290_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p11134162718196"><a name="en-us_topic_0084581290_p11134162718196"></a><a name="en-us_topic_0084581290_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p125520290312"><a name="en-us_topic_0084581290_p125520290312"></a><a name="en-us_topic_0084581290_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p19789174972712"><a name="en-us_topic_0084581290_p19789174972712"></a><a name="en-us_topic_0084581290_p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p779364918272"><a name="en-us_topic_0084581290_p779364918272"></a><a name="en-us_topic_0084581290_p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p196546319198"><a name="en-us_topic_0084581290_p196546319198"></a><a name="en-us_topic_0084581290_p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

