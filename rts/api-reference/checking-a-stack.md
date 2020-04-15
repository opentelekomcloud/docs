# Checking a Stack<a name="EN-US_TOPIC_0084581301"></a>

## Function<a name="en-us_topic_0057973137_section22605367"></a>

This API is used to check whether a stack is in the expected status.

## URI<a name="en-us_topic_0057973137_section2121711"></a>

POST /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/actions

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b1250284210349"><a name="b1250284210349"></a><a name="b1250284210349"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b12403164520341"><a name="b12403164520341"></a><a name="b12403164520341"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b205371346143412"><a name="b205371346143412"></a><a name="b205371346143412"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b1183205483412"><a name="b1183205483412"></a><a name="b1183205483412"></a>Description</strong></p>
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

## Request Parameter<a name="en-us_topic_0057973137_section19095402"></a>

<a name="en-us_topic_0057973137_table5975743111756"></a>
<table><thead align="left"><tr id="en-us_topic_0057973137_row48626546111756"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b572971113514"><a name="b572971113514"></a><a name="b572971113514"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b2562161813357"><a name="b2562161813357"></a><a name="b2562161813357"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b11748101916357"><a name="b11748101916357"></a><a name="b11748101916357"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b1419672118358"><a name="b1419672118358"></a><a name="b1419672118358"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b10372926203515"><a name="b10372926203515"></a><a name="b10372926203515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973137_row38131520111756"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973137_p2138749311185"><a name="en-us_topic_0057973137_p2138749311185"></a><a name="en-us_topic_0057973137_p2138749311185"></a>check</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p42427320425"><a name="p42427320425"></a><a name="p42427320425"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973137_p5466538511185"><a name="en-us_topic_0057973137_p5466538511185"></a><a name="en-us_topic_0057973137_p5466538511185"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973137_p6582002811185"><a name="en-us_topic_0057973137_p6582002811185"></a><a name="en-us_topic_0057973137_p6582002811185"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973137_p2982208911185"><a name="en-us_topic_0057973137_p2982208911185"></a><a name="en-us_topic_0057973137_p2982208911185"></a>Checks stack resources.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973137_section37640898"></a>

This operation does not return the response body.

## Request Example<a name="en-us_topic_0057973137_section3223767"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/actions
{
    "check": null
}
```

## Response Example<a name="en-us_topic_0057973137_section29013906"></a>

None

## Return Code<a name="en-us_topic_0057973137_section59798564"></a>

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

<a name="table1389832182115"></a>
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

