# Deleting a Software Configuration<a name="EN-US_TOPIC_0084581318"></a>

## Function<a name="en-us_topic_0057973157_section42487485"></a>

This API is used to delete a software configuration.

## URI<a name="en-us_topic_0057973157_section46843046"></a>

DELETE /v1/\{project\_id\}/software\_configs/\{config\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b411761312431"><a name="b411761312431"></a><a name="b411761312431"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b392891614312"><a name="b392891614312"></a><a name="b392891614312"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b18867191724319"><a name="b18867191724319"></a><a name="b18867191724319"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b719620210433"><a name="b719620210433"></a><a name="b719620210433"></a>Description</strong></p>
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

## Request Parameter<a name="en-us_topic_0057973157_section18934233"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973157_section36190376"></a>

This request does not return any content in the response body.

## Request Example<a name="en-us_topic_0057973157_section57277930"></a>

```
DELETE /v1/95d02433133a4c0a87ba6967474a2ad3/software_configs/40p72423093a900a8b7a669768421a6a
```

## Response Example<a name="en-us_topic_0057973157_section45739330"></a>

None

## Return Code<a name="en-us_topic_0057973157_section9000792"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a>Return Code</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973122_p61089452194154"><a name="en-us_topic_0057973122_p61089452194154"></a><a name="en-us_topic_0057973122_p61089452194154"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973122_p49298568194154"><a name="en-us_topic_0057973122_p49298568194154"></a><a name="en-us_topic_0057973122_p49298568194154"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973122_p33761032194154"><a name="en-us_topic_0057973122_p33761032194154"></a><a name="en-us_topic_0057973122_p33761032194154"></a>The RTS service has fulfilled the request by deleting the resource.</p>
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

