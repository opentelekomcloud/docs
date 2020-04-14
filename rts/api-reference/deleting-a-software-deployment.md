# Deleting a Software Deployment<a name="EN-US_TOPIC_0085277562"></a>

## Function<a name="en-us_topic_0085081139_section5314816"></a>

This API is used to delete a software deployment.

## URI<a name="en-us_topic_0085081139_section47833347"></a>

DELETE /v1/\{project\_id\}/software\_deployments/\{deployment\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b9410181420182"><a name="b9410181420182"></a><a name="b9410181420182"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b15580201514188"><a name="b15580201514188"></a><a name="b15580201514188"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b14365111615182"><a name="b14365111615182"></a><a name="b14365111615182"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b8235717191811"><a name="b8235717191811"></a><a name="b8235717191811"></a>Description</strong></p>
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
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1874564042214"><a name="p1874564042214"></a><a name="p1874564042214"></a>deployment_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p17747124020225"><a name="p17747124020225"></a><a name="p17747124020225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p157491540122216"><a name="p157491540122216"></a><a name="p157491540122216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p197517404224"><a name="p197517404224"></a><a name="p197517404224"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081139_section27846943"></a>

N/A

## Response Parameter<a name="en-us_topic_0085081139_section49295902"></a>

This request does not return any content in the response body.

## Request Example<a name="en-us_topic_0085081139_section41009935"></a>

```
DELETE /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments/80p72409093a9005bb7a6698c85a1b61
```

## Response Example<a name="en-us_topic_0085081139_section33545101"></a>

None

## Return Code<a name="en-us_topic_0085081139_section33470456"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0084581318_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581318_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581318_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581318_en-us_topic_0057973117_p13413377194057"></a>Return Code</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581318_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581318_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581318_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581318_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581318_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581318_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581318_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581318_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581318_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581318_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581318_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581318_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581318_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581318_en-us_topic_0057973122_p61089452194154"><a name="en-us_topic_0084581318_en-us_topic_0057973122_p61089452194154"></a><a name="en-us_topic_0084581318_en-us_topic_0057973122_p61089452194154"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581318_en-us_topic_0057973122_p49298568194154"><a name="en-us_topic_0084581318_en-us_topic_0057973122_p49298568194154"></a><a name="en-us_topic_0084581318_en-us_topic_0057973122_p49298568194154"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581318_en-us_topic_0057973122_p33761032194154"><a name="en-us_topic_0084581318_en-us_topic_0057973122_p33761032194154"></a><a name="en-us_topic_0084581318_en-us_topic_0057973122_p33761032194154"></a>The RTS service has fulfilled the request by deleting the resource.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table3304326164315"></a>
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

