# Querying ECS Actions by Request ID<a name="EN-US_TOPIC_0065817693"></a>

## Function<a name="en-us_topic_0057973179_section16588975"></a>

This API is used to query a request of an ECS.

## URI<a name="en-us_topic_0057973179_section15083054"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-instance-actions/\{request\_id\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-instance-actions/\{request\_id\}

[Table 1](#en-us_topic_0057973179_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973179_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057973179_row11302482"><th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.560000000000002%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.79%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973179_row49888896"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973179_p14468758"><a name="en-us_topic_0057973179_p14468758"></a><a name="en-us_topic_0057973179_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973179_p31118786"><a name="en-us_topic_0057973179_p31118786"></a><a name="en-us_topic_0057973179_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row613736410235"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973179_p2736446410235"><a name="en-us_topic_0057973179_p2736446410235"></a><a name="en-us_topic_0057973179_p2736446410235"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973179_p192907210235"><a name="en-us_topic_0057973179_p192907210235"></a><a name="en-us_topic_0057973179_p192907210235"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973179_p2203711610235"><a name="en-us_topic_0057973179_p2203711610235"></a><a name="en-us_topic_0057973179_p2203711610235"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row172751639164211"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973179_p1927610391427"><a name="en-us_topic_0057973179_p1927610391427"></a><a name="en-us_topic_0057973179_p1927610391427"></a>request_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.560000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973179_p1727693974213"><a name="en-us_topic_0057973179_p1727693974213"></a><a name="en-us_topic_0057973179_p1727693974213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.79%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973179_p4276839114210"><a name="en-us_topic_0057973179_p4276839114210"></a><a name="en-us_topic_0057973179_p4276839114210"></a>Specifies the request ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973179_section56802184"></a>

None

## Response<a name="en-us_topic_0057973179_section41457614"></a>

[Table 2](#en-us_topic_0057973179_table42003011)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973179_table42003011"></a>
<table><thead align="left"><tr id="en-us_topic_0057973179_row4203326"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973179_p4925089"><a name="en-us_topic_0057973179_p4925089"></a><a name="en-us_topic_0057973179_p4925089"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.599999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973179_p34151611"><a name="en-us_topic_0057973179_p34151611"></a><a name="en-us_topic_0057973179_p34151611"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.6%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973179_p63387966"><a name="en-us_topic_0057973179_p63387966"></a><a name="en-us_topic_0057973179_p63387966"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.46%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973179_p14817088"><a name="en-us_topic_0057973179_p14817088"></a><a name="en-us_topic_0057973179_p14817088"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973179_row59333494"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p41283716"><a name="en-us_topic_0057973179_p41283716"></a><a name="en-us_topic_0057973179_p41283716"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p11092043"><a name="en-us_topic_0057973179_p11092043"></a><a name="en-us_topic_0057973179_p11092043"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p55646739"><a name="en-us_topic_0057973179_p55646739"></a><a name="en-us_topic_0057973179_p55646739"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p26040275"><a name="en-us_topic_0057973179_p26040275"></a><a name="en-us_topic_0057973179_p26040275"></a>Specifies the action name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row33035884"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p58660976"><a name="en-us_topic_0057973179_p58660976"></a><a name="en-us_topic_0057973179_p58660976"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p5331789"><a name="en-us_topic_0057973179_p5331789"></a><a name="en-us_topic_0057973179_p5331789"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p53918616"><a name="en-us_topic_0057973179_p53918616"></a><a name="en-us_topic_0057973179_p53918616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p29221750"><a name="en-us_topic_0057973179_p29221750"></a><a name="en-us_topic_0057973179_p29221750"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row61669162"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p29146205"><a name="en-us_topic_0057973179_p29146205"></a><a name="en-us_topic_0057973179_p29146205"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p35098404"><a name="en-us_topic_0057973179_p35098404"></a><a name="en-us_topic_0057973179_p35098404"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p12032376"><a name="en-us_topic_0057973179_p12032376"></a><a name="en-us_topic_0057973179_p12032376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p24398472"><a name="en-us_topic_0057973179_p24398472"></a><a name="en-us_topic_0057973179_p24398472"></a>Specifies the result status of the action.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row18259663"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p2637755"><a name="en-us_topic_0057973179_p2637755"></a><a name="en-us_topic_0057973179_p2637755"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p59338465"><a name="en-us_topic_0057973179_p59338465"></a><a name="en-us_topic_0057973179_p59338465"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p12331636"><a name="en-us_topic_0057973179_p12331636"></a><a name="en-us_topic_0057973179_p12331636"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p41686379"><a name="en-us_topic_0057973179_p41686379"></a><a name="en-us_topic_0057973179_p41686379"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row39633094"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p56164037"><a name="en-us_topic_0057973179_p56164037"></a><a name="en-us_topic_0057973179_p56164037"></a>request_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p64588638"><a name="en-us_topic_0057973179_p64588638"></a><a name="en-us_topic_0057973179_p64588638"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p52993173"><a name="en-us_topic_0057973179_p52993173"></a><a name="en-us_topic_0057973179_p52993173"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p64297159"><a name="en-us_topic_0057973179_p64297159"></a><a name="en-us_topic_0057973179_p64297159"></a>Specifies the request ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row41803519"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p30641851"><a name="en-us_topic_0057973179_p30641851"></a><a name="en-us_topic_0057973179_p30641851"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p50142074"><a name="en-us_topic_0057973179_p50142074"></a><a name="en-us_topic_0057973179_p50142074"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p66070892"><a name="en-us_topic_0057973179_p66070892"></a><a name="en-us_topic_0057973179_p66070892"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p34976204"><a name="en-us_topic_0057973179_p34976204"></a><a name="en-us_topic_0057973179_p34976204"></a>Specifies the time when the action was started.</p>
</td>
</tr>
<tr id="row419219211572"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="p13192421165713"><a name="p13192421165713"></a><a name="p13192421165713"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="p2019272113571"><a name="p2019272113571"></a><a name="p2019272113571"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="p1419252175710"><a name="p1419252175710"></a><a name="p1419252175710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="p31920211578"><a name="p31920211578"></a><a name="p31920211578"></a>Specifies the user ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row46350387"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p63393830"><a name="en-us_topic_0057973179_p63393830"></a><a name="en-us_topic_0057973179_p63393830"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p53294688"><a name="en-us_topic_0057973179_p53294688"></a><a name="en-us_topic_0057973179_p53294688"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p34626643"><a name="en-us_topic_0057973179_p34626643"></a><a name="en-us_topic_0057973179_p34626643"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p21902453"><a name="en-us_topic_0057973179_p21902453"></a><a name="en-us_topic_0057973179_p21902453"></a>Specifies event information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **events**  parameters

<a name="en-us_topic_0057973179_table12745176"></a>
<table><thead align="left"><tr id="en-us_topic_0057973179_row62655484"><th class="cellrowborder" valign="top" width="18.33%" id="mcps1.2.5.1.1"><p id="p955611101542"><a name="p955611101542"></a><a name="p955611101542"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.5.1.2"><p id="p755691019545"><a name="p755691019545"></a><a name="p755691019545"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.87%" id="mcps1.2.5.1.3"><p id="p1255681015541"><a name="p1255681015541"></a><a name="p1255681015541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.27%" id="mcps1.2.5.1.4"><p id="p1957112100545"><a name="p1957112100545"></a><a name="p1957112100545"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973179_row66711197"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p34897906"><a name="en-us_topic_0057973179_p34897906"></a><a name="en-us_topic_0057973179_p34897906"></a>event</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p56831198"><a name="en-us_topic_0057973179_p56831198"></a><a name="en-us_topic_0057973179_p56831198"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p8158160"><a name="en-us_topic_0057973179_p8158160"></a><a name="en-us_topic_0057973179_p8158160"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p39924292"><a name="en-us_topic_0057973179_p39924292"></a><a name="en-us_topic_0057973179_p39924292"></a>Specifies the action name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row23774312"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p46671110"><a name="en-us_topic_0057973179_p46671110"></a><a name="en-us_topic_0057973179_p46671110"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p58518640"><a name="en-us_topic_0057973179_p58518640"></a><a name="en-us_topic_0057973179_p58518640"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p22263569"><a name="en-us_topic_0057973179_p22263569"></a><a name="en-us_topic_0057973179_p22263569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p42389388"><a name="en-us_topic_0057973179_p42389388"></a><a name="en-us_topic_0057973179_p42389388"></a>Specifies the execution result.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row45960172"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p31786413"><a name="en-us_topic_0057973179_p31786413"></a><a name="en-us_topic_0057973179_p31786413"></a>traceback</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p43418025"><a name="en-us_topic_0057973179_p43418025"></a><a name="en-us_topic_0057973179_p43418025"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p24562655"><a name="en-us_topic_0057973179_p24562655"></a><a name="en-us_topic_0057973179_p24562655"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p27199156"><a name="en-us_topic_0057973179_p27199156"></a><a name="en-us_topic_0057973179_p27199156"></a>Specifies the error message.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row43465817"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p31070312"><a name="en-us_topic_0057973179_p31070312"></a><a name="en-us_topic_0057973179_p31070312"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p42699947"><a name="en-us_topic_0057973179_p42699947"></a><a name="en-us_topic_0057973179_p42699947"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p33667339"><a name="en-us_topic_0057973179_p33667339"></a><a name="en-us_topic_0057973179_p33667339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p36143663"><a name="en-us_topic_0057973179_p36143663"></a><a name="en-us_topic_0057973179_p36143663"></a>Specifies the time when the event was started.</p>
</td>
</tr>
<tr id="en-us_topic_0057973179_row56857514"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973179_p42055936"><a name="en-us_topic_0057973179_p42055936"></a><a name="en-us_topic_0057973179_p42055936"></a>finish_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973179_p44459997"><a name="en-us_topic_0057973179_p44459997"></a><a name="en-us_topic_0057973179_p44459997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973179_p51087662"><a name="en-us_topic_0057973179_p51087662"></a><a name="en-us_topic_0057973179_p51087662"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973179_p44490037"><a name="en-us_topic_0057973179_p44490037"></a><a name="en-us_topic_0057973179_p44490037"></a>Specifies the time when the event was completed.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973179_section37574207"></a>

```
GET https://{endpoint}/v2/89655fe61c4c4a08b9f3e7f9095441b8/servers/e723eb40-f56e-40f9-8c8c-caa517fe06ba/os-instance-actions/req-5a429946-c9cc-45cc-b5bd-68864209e5c
GET https://{endpoint}/v2.1/89655fe61c4c4a08b9f3e7f9095441b8/servers/e723eb40-f56e-40f9-8c8c-caa517fe06ba/os-instance-actions/req-5a429946-c9cc-45cc-b5bd-68864209e5c
```

## Example Response<a name="section18542154625318"></a>

```
{
    "instanceAction": {
        "instance_uuid": "e723eb40-f56e-40f9-8c8c-caa517fe06ba",
        "user_id": "752be40780484291a9cc7ae50fff3e6d",
        "start_time": "2014-12-11T02:17:49.000000",
        "request_id": "req-5a429946-c9cc-45cc-b5bd-68864209e5cc",
        "action": "create",
        "message": null,
        "project_id": "89655fe61c4c4a08b9f3e7f9095441b8",
        "events": [
            {
                "finish_time": "2014-12-11T02:17:58.000000",
                "start_time": "2014-12-11T02:17:50.000000",
                "traceback": null,
                "event": "compute_build_and_run_instance",
                "result": "Success"
            }
        ]
    }
}
```

## Returned Values<a name="en-us_topic_0057973179_section1642564"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

