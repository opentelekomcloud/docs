# Querying Details of a Stack Resource Event<a name="EN-US_TOPIC_0084581306"></a>

## Function<a name="en-us_topic_0057973143_section21526787"></a>

This API is used to query details of a stack resource event.

## URI<a name="en-us_topic_0057973143_section59523362"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/resources/\{resource\_name\}/events/\{event\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b15586132913611"><a name="b15586132913611"></a><a name="b15586132913611"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b32794328367"><a name="b32794328367"></a><a name="b32794328367"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b31913333361"><a name="b31913333361"></a><a name="b31913333361"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b322615365365"><a name="b322615365365"></a><a name="b322615365365"></a>Description</strong></p>
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
<tr id="row04307962213"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1514822615235"><a name="p1514822615235"></a><a name="p1514822615235"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p13151102611233"><a name="p13151102611233"></a><a name="p13151102611233"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p115382612311"><a name="p115382612311"></a><a name="p115382612311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1615542615236"><a name="p1615542615236"></a><a name="p1615542615236"></a>Specifies the name of the resource in the stack.</p>
</td>
</tr>
<tr id="row185441474233"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1899845810236"><a name="p1899845810236"></a><a name="p1899845810236"></a>event_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p140135992319"><a name="p140135992319"></a><a name="p140135992319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p52759122315"><a name="p52759122315"></a><a name="p52759122315"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p9519592232"><a name="p9519592232"></a><a name="p9519592232"></a>Specifies the UUID of the event related to the resource in the stack.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973143_section65948211"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973143_section56662993"></a>

<a name="en-us_topic_0057973142_table19596697"></a>
<table><thead align="left"><tr id="en-us_topic_0057973142_row50957800"><th class="cellrowborder" valign="top" width="15.11848815118488%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.27837216278372%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b13593172810375"><a name="b13593172810375"></a><a name="b13593172810375"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.27837216278372%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b135553223716"><a name="b135553223716"></a><a name="b135553223716"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.32476752324767%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b1849916344371"><a name="b1849916344371"></a><a name="b1849916344371"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973142_row48089434"><td class="cellrowborder" valign="top" width="15.11848815118488%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p2930044"><a name="en-us_topic_0057973142_p2930044"></a><a name="en-us_topic_0057973142_p2930044"></a>event</p>
</td>
<td class="cellrowborder" valign="top" width="16.27837216278372%" headers="mcps1.1.5.1.2 "><p id="p83828525112"><a name="p83828525112"></a><a name="p83828525112"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.27837216278372%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p36007027"><a name="en-us_topic_0057973142_p36007027"></a><a name="en-us_topic_0057973142_p36007027"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.32476752324767%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p18908415"><a name="en-us_topic_0057973142_p18908415"></a><a name="en-us_topic_0057973142_p18908415"></a>Specifies a resource event.</p>
</td>
</tr>
</tbody>
</table>

**event**  structure information

<a name="en-us_topic_0057973142_table55186660"></a>
<table><thead align="left"><tr id="en-us_topic_0057973142_row11951831"><th class="cellrowborder" valign="top" width="16.471647164716472%" id="mcps1.1.5.1.1"><p id="p161475355513"><a name="p161475355513"></a><a name="p161475355513"></a><strong id="b749383031"><a name="b749383031"></a><a name="b749383031"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.2"><p id="p1615155325519"><a name="p1615155325519"></a><a name="p1615155325519"></a><strong id="b1883610525377"><a name="b1883610525377"></a><a name="b1883610525377"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.3"><p id="p1018353135520"><a name="p1018353135520"></a><a name="p1018353135520"></a><strong id="b86225517378"><a name="b86225517378"></a><a name="b86225517378"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.945294529452944%" id="mcps1.1.5.1.4"><p id="p19231853175519"><a name="p19231853175519"></a><a name="p19231853175519"></a><strong id="b328919572371"><a name="b328919572371"></a><a name="b328919572371"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973142_row6835688"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p9484678"><a name="en-us_topic_0057973142_p9484678"></a><a name="en-us_topic_0057973142_p9484678"></a>event_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p99581284106"><a name="p99581284106"></a><a name="p99581284106"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p30061414"><a name="en-us_topic_0057973142_p30061414"></a><a name="en-us_topic_0057973142_p30061414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p43923748"><a name="en-us_topic_0057973142_p43923748"></a><a name="en-us_topic_0057973142_p43923748"></a>Specifies the time when an event occurs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row59769418"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="p3135202075411"><a name="p3135202075411"></a><a name="p3135202075411"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p69583815109"><a name="p69583815109"></a><a name="p69583815109"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="p7133102005414"><a name="p7133102005414"></a><a name="p7133102005414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p67095859"><a name="en-us_topic_0057973142_p67095859"></a><a name="en-us_topic_0057973142_p67095859"></a>Specifies the UUID of the event object.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row66991827"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p57628926"><a name="en-us_topic_0057973142_p57628926"></a><a name="en-us_topic_0057973142_p57628926"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p995815891013"><a name="p995815891013"></a><a name="p995815891013"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p37431442"><a name="en-us_topic_0057973142_p37431442"></a><a name="en-us_topic_0057973142_p37431442"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="p866816504301"><a name="p866816504301"></a><a name="p866816504301"></a>Specifies the event URL list. Each URL is a JSON object with one <strong id="b72198263505"><a name="b72198263505"></a><a name="b72198263505"></a>href</strong> keyword for identifying the URL and one <strong id="b15368113213501"><a name="b15368113213501"></a><a name="b15368113213501"></a>rel</strong> keyword indicating the event relationship. Multiple URLs may be returned.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row58785701"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p64021321"><a name="en-us_topic_0057973142_p64021321"></a><a name="en-us_topic_0057973142_p64021321"></a>logical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p795814819109"><a name="p795814819109"></a><a name="p795814819109"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p18344506"><a name="en-us_topic_0057973142_p18344506"></a><a name="en-us_topic_0057973142_p18344506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p32111136"><a name="en-us_topic_0057973142_p32111136"></a><a name="en-us_topic_0057973142_p32111136"></a>Specifies the logical stack resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row20564775"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="p18612813544"><a name="p18612813544"></a><a name="p18612813544"></a>physical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p795820810104"><a name="p795820810104"></a><a name="p795820810104"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="p156121117543"><a name="p156121117543"></a><a name="p156121117543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p59022856"><a name="en-us_topic_0057973142_p59022856"></a><a name="en-us_topic_0057973142_p59022856"></a>Specifies the physical stack resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row61443660"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p16819822"><a name="en-us_topic_0057973142_p16819822"></a><a name="en-us_topic_0057973142_p16819822"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p59588871013"><a name="p59588871013"></a><a name="p59588871013"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p20228341"><a name="en-us_topic_0057973142_p20228341"></a><a name="en-us_topic_0057973142_p20228341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p16730874"><a name="en-us_topic_0057973142_p16730874"></a><a name="en-us_topic_0057973142_p16730874"></a>Specifies the resource name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row16360140"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="p198381422102318"><a name="p198381422102318"></a><a name="p198381422102318"></a>resource_properties</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p59581388103"><a name="p59581388103"></a><a name="p59581388103"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="p17838112212234"><a name="p17838112212234"></a><a name="p17838112212234"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p54798319"><a name="en-us_topic_0057973142_p54798319"></a><a name="en-us_topic_0057973142_p54798319"></a>Specifies the mapping between resource attributes and events.</p>
</td>
</tr>
<tr id="en-us_topic_0057973142_row23422824"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p55134111"><a name="en-us_topic_0057973142_p55134111"></a><a name="en-us_topic_0057973142_p55134111"></a>resource_status</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p095820811016"><a name="p095820811016"></a><a name="p095820811016"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p36677991"><a name="en-us_topic_0057973142_p36677991"></a><a name="en-us_topic_0057973142_p36677991"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973142_p9067240"><a name="en-us_topic_0057973142_p9067240"></a><a name="en-us_topic_0057973142_p9067240"></a>Specifies the resource status.</p>
</td>
</tr>
<tr id="row123401016286"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p10880577"><a name="en-us_topic_0057973142_p10880577"></a><a name="en-us_topic_0057973142_p10880577"></a>resource_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p11958198161018"><a name="p11958198161018"></a><a name="p11958198161018"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p8911530"><a name="en-us_topic_0057973142_p8911530"></a><a name="en-us_topic_0057973142_p8911530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="p734017116283"><a name="p734017116283"></a><a name="p734017116283"></a>Specifies the cause causing the current stack resource status.</p>
</td>
</tr>
<tr id="row9340161172813"><td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973142_p18200597"><a name="en-us_topic_0057973142_p18200597"></a><a name="en-us_topic_0057973142_p18200597"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p2095812891013"><a name="p2095812891013"></a><a name="p2095812891013"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973142_p64962271"><a name="en-us_topic_0057973142_p64962271"></a><a name="en-us_topic_0057973142_p64962271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="p234014182819"><a name="p234014182819"></a><a name="p234014182819"></a>Specifies the resource type name.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973143_section40204892"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/random_str/events/1313
```

## Response Example<a name="en-us_topic_0057973143_section26299709"></a>

```
{
    "event": { 
        "event_time": "2014-02-18T18:23:27Z",
        "id": "485",
        "links": [
            {
                "href":  "http://x.x.x.x:8004/v1/8443bcd779f3435e86e1cbf73d98a89c/stacks/heat168714801/e6d10493-8d85-46cb-bf3c-e5572f255ef5/resources/random_str/events/1313",
                "rel": "self"
            },
            { 
                "href":  "http://x.x.x.x:8004/v1/8443bcd779f3435e86e1cbf73d98a89c/stacks/heat168714801/e6d10493-8d85-46cb-bf3c-e5572f255ef5/resources/random_str",
                "rel": "resource"
            },
            { 
                "href":  "http://x.x.x.x:8004/v1/8443bcd779f3435e86e1cbf73d98a89c/stacks/heat168714801/e6d10493-8d85-46cb-bf3c-e5572f255ef5",
                "rel": "stack"
            }
        ],
        "logical_resource_id": "random_key_name",
        "physical_resource_id": null,
        "resource_name": "random_key_name",
        "resource_properties": {
            "character_classes": null,
            "character_sequences": null,
            "length": 8,
            "salt": null,
            "sequence": null
        },
        "resource_status": "CREATE_IN_PROGRESS",
        "resource_status_reason": "state changed",
        "resource_type": "OS::Heat::RandomString"
    }
}
```

## Return Code<a name="en-us_topic_0057973143_section35370789"></a>

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

<a name="table19512103414"></a>
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

