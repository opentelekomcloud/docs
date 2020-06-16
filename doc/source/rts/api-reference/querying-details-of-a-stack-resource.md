# Querying Details of a Stack Resource<a name="EN-US_TOPIC_0084581295"></a>

## Function<a name="en-us_topic_0057973131_section6707778"></a>

This API is used to query details of a stack resource.

## URI<a name="en-us_topic_0057973131_section60370005"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/resources/\{resource\_name\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b155194548109"><a name="b155194548109"></a><a name="b155194548109"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b436116588102"><a name="b436116588102"></a><a name="b436116588102"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b114135916109"><a name="b114135916109"></a><a name="b114135916109"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b842352706194312"><a name="b842352706194312"></a><a name="b842352706194312"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1581811351277"><a name="p1581811351277"></a><a name="p1581811351277"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row161097438473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p129746567332"><a name="p129746567332"></a><a name="p129746567332"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p127445853413"><a name="p127445853413"></a><a name="p127445853413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p167462087343"><a name="p167462087343"></a><a name="p167462087343"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p2750168173419"><a name="p2750168173419"></a><a name="p2750168173419"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row131851844124918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1859881513364"><a name="p1859881513364"></a><a name="p1859881513364"></a>stack_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p174332483611"><a name="p174332483611"></a><a name="p174332483611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p13461724163619"><a name="p13461724163619"></a><a name="p13461724163619"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p134992463611"><a name="p134992463611"></a><a name="p134992463611"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="row84164613820"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12129567438"><a name="p12129567438"></a><a name="p12129567438"></a>resource_name</p>
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

## Request Parameter<a name="en-us_topic_0057973131_section6459136"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973131_section58132228"></a>

<a name="table254004112510"></a>
<table><thead align="left"><tr id="row20540114112518"><th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b8616124671111"><a name="b8616124671111"></a><a name="b8616124671111"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b10775104911115"><a name="b10775104911115"></a><a name="b10775104911115"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.04809519048095%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b251065421119"><a name="b251065421119"></a><a name="b251065421119"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.42535746425357%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b172235711118"><a name="b172235711118"></a><a name="b172235711118"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10540164132513"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="p2540104122519"><a name="p2540104122519"></a><a name="p2540104122519"></a>resource</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p57361415103015"><a name="p57361415103015"></a><a name="p57361415103015"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="p115402414250"><a name="p115402414250"></a><a name="p115402414250"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p7540154172517"><a name="p7540154172517"></a><a name="p7540154172517"></a>Specifies resource information of the stack.</p>
</td>
</tr>
</tbody>
</table>

**resource**  structure information

<a name="en-us_topic_0057973131_table297159"></a>
<table><thead align="left"><tr id="en-us_topic_0057973131_row15428113"><th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.1"><p id="p277618155544"><a name="p277618155544"></a><a name="p277618155544"></a><strong id="b1725511612125"><a name="b1725511612125"></a><a name="b1725511612125"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.2"><p id="p0778111517547"><a name="p0778111517547"></a><a name="p0778111517547"></a><strong id="b20689172013128"><a name="b20689172013128"></a><a name="b20689172013128"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.04809519048095%" id="mcps1.1.5.1.3"><p id="p1778016153547"><a name="p1778016153547"></a><a name="p1778016153547"></a><strong id="b112252236125"><a name="b112252236125"></a><a name="b112252236125"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.42535746425357%" id="mcps1.1.5.1.4"><p id="p37838151548"><a name="p37838151548"></a><a name="p37838151548"></a><strong id="b189101325171213"><a name="b189101325171213"></a><a name="b189101325171213"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973131_row63505452"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p43667992"><a name="en-us_topic_0057973131_p43667992"></a><a name="en-us_topic_0057973131_p43667992"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p0699104691310"><a name="p0699104691310"></a><a name="p0699104691310"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p47446460"><a name="en-us_topic_0057973131_p47446460"></a><a name="en-us_topic_0057973131_p47446460"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p17958081"><a name="en-us_topic_0057973131_p17958081"></a><a name="en-us_topic_0057973131_p17958081"></a>Specifies the resource name.</p>
</td>
</tr>
<tr id="row44191324132613"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="p3419202412611"><a name="p3419202412611"></a><a name="p3419202412611"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p869964615136"><a name="p869964615136"></a><a name="p869964615136"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="p2420192411261"><a name="p2420192411261"></a><a name="p2420192411261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p1342012243265"><a name="p1342012243265"></a><a name="p1342012243265"></a>Describes the resource.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row27405007"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p5213128"><a name="en-us_topic_0057973131_p5213128"></a><a name="en-us_topic_0057973131_p5213128"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1569964611319"><a name="p1569964611319"></a><a name="p1569964611319"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p19610229"><a name="en-us_topic_0057973131_p19610229"></a><a name="en-us_topic_0057973131_p19610229"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p44924735"><a name="en-us_topic_0057973131_p44924735"></a><a name="en-us_topic_0057973131_p44924735"></a>Specifies the resource URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row1669434"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p1006457"><a name="en-us_topic_0057973131_p1006457"></a><a name="en-us_topic_0057973131_p1006457"></a>logical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p7699124611310"><a name="p7699124611310"></a><a name="p7699124611310"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p14414217"><a name="en-us_topic_0057973131_p14414217"></a><a name="en-us_topic_0057973131_p14414217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p26700946"><a name="en-us_topic_0057973131_p26700946"></a><a name="en-us_topic_0057973131_p26700946"></a>Specifies the logical resource ID.</p>
</td>
</tr>
<tr id="row63564815411"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="p936048344"><a name="p936048344"></a><a name="p936048344"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p33616481749"><a name="p33616481749"></a><a name="p33616481749"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="p1361248545"><a name="p1361248545"></a><a name="p1361248545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p133615481445"><a name="p133615481445"></a><a name="p133615481445"></a>Specifies the time of creating the stack resource.</p>
<p id="p1677318131155"><a name="p1677318131155"></a><a name="p1677318131155"></a>Example: 2019-04-30T02:55:48.869333</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row38981923"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p3419155"><a name="en-us_topic_0057973131_p3419155"></a><a name="en-us_topic_0057973131_p3419155"></a>physical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1469954641312"><a name="p1469954641312"></a><a name="p1469954641312"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p8516111"><a name="en-us_topic_0057973131_p8516111"></a><a name="en-us_topic_0057973131_p8516111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p18716416"><a name="en-us_topic_0057973131_p18716416"></a><a name="en-us_topic_0057973131_p18716416"></a>Specifies the physical resource ID.</p>
</td>
</tr>
<tr id="row7428155310514"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="p1742819536516"><a name="p1742819536516"></a><a name="p1742819536516"></a>attributes</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p174282531259"><a name="p174282531259"></a><a name="p174282531259"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="p1742811531156"><a name="p1742811531156"></a><a name="p1742811531156"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p15428353453"><a name="p15428353453"></a><a name="p15428353453"></a>Includes key-value pairs of the resource attribute.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row34230024"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p21168579"><a name="en-us_topic_0057973131_p21168579"></a><a name="en-us_topic_0057973131_p21168579"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p569911464136"><a name="p569911464136"></a><a name="p569911464136"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p36933351"><a name="en-us_topic_0057973131_p36933351"></a><a name="en-us_topic_0057973131_p36933351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p38811418"><a name="en-us_topic_0057973131_p38811418"></a><a name="en-us_topic_0057973131_p38811418"></a>Specifies the resource type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row13758450"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p40692674"><a name="en-us_topic_0057973131_p40692674"></a><a name="en-us_topic_0057973131_p40692674"></a>resource_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1569924613136"><a name="p1569924613136"></a><a name="p1569924613136"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p7772278"><a name="en-us_topic_0057973131_p7772278"></a><a name="en-us_topic_0057973131_p7772278"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p25574775"><a name="en-us_topic_0057973131_p25574775"></a><a name="en-us_topic_0057973131_p25574775"></a>Specifies the resource status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row28846383"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p54855693"><a name="en-us_topic_0057973131_p54855693"></a><a name="en-us_topic_0057973131_p54855693"></a>resource_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p5699746131316"><a name="p5699746131316"></a><a name="p5699746131316"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p14126188"><a name="en-us_topic_0057973131_p14126188"></a><a name="en-us_topic_0057973131_p14126188"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p3370612"><a name="en-us_topic_0057973131_p3370612"></a><a name="en-us_topic_0057973131_p3370612"></a>Specifies the resource operation reason.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row30335510"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p41257261"><a name="en-us_topic_0057973131_p41257261"></a><a name="en-us_topic_0057973131_p41257261"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p146991046121315"><a name="p146991046121315"></a><a name="p146991046121315"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p53503873"><a name="en-us_topic_0057973131_p53503873"></a><a name="en-us_topic_0057973131_p53503873"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p38846457"><a name="en-us_topic_0057973131_p38846457"></a><a name="en-us_topic_0057973131_p38846457"></a>Specifies the time when the resource was updated.</p>
</td>
</tr>
<tr id="en-us_topic_0057973131_row14073798"><td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973131_p66235888"><a name="en-us_topic_0057973131_p66235888"></a><a name="en-us_topic_0057973131_p66235888"></a>required_by</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p20115102603017"><a name="p20115102603017"></a><a name="p20115102603017"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973131_p63506739"><a name="en-us_topic_0057973131_p63506739"></a><a name="en-us_topic_0057973131_p63506739"></a>List &lt;str&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973131_p43772214"><a name="en-us_topic_0057973131_p43772214"></a><a name="en-us_topic_0057973131_p43772214"></a>Specifies the resource dependency.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973131_section53428011"></a>

```
GET /v1/6e0193034db54600b889f890768a72ea/stacks/stack-0vi3/63a16fbe-717b-417c-a3e5-08fc51544b49/resources/random-group
```

## Response Example<a name="en-us_topic_0057973131_section11090052"></a>

```
{
    "resource": {
        "attributes": {
            "attributes": null,
            "refs": null
        },
        "creation_time": "2019-03-04T06:36:45.455761",
        "description": "",
        "links": [
            {
                "href": "https://orchestration.localdomain.com:8004/v1/6e0193034db54600b889f890768a72ea/stacks/stack-0vi3/63a16fbe-717b-417c-a3e5-08fc51544b49/resources/random-group",
                "rel": "self"
            },
            {
                "href": "https://orchestration.localdomain.com:8004/v1/6e0193034db54600b889f890768a72ea/stacks/stack-0vi3/63a16fbe-717b-417c-a3e5-08fc51544b49",
                "rel": "stack"
            },
            {
                "href": "https://orchestration.localdomain.com:8004/v1/6e0193034db54600b889f890768a72ea/stacks/stack-0vi3-random-group-k7emexipm2k6/2b6d0d58-0a7b-45d7-978f-519d0b1395ce",
                "rel": "nested"
            }
        ],
        "logical_resource_id": "random-group",
        "physical_resource_id": "2b6d0d58-0a7b-45d7-978f-519d0b1395ce",
        "required_by": [],
        "resource_name": "random-group",
        "resource_status": "CREATE_COMPLETE",
        "resource_status_reason": "state changed",
        "resource_type": "OS::Heat::ResourceGroup",
        "updated_time": "2019-03-04T06:36:45.455761"
    }
}
```

## Return Code<a name="en-us_topic_0057973131_section32701610"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
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

