# Querying Details of a Stack<a name="EN-US_TOPIC_0084581290"></a>

## Function<a name="en-us_topic_0057973125_section15571009"></a>

This API is used to query details of a stack.

## URI<a name="en-us_topic_0057973125_section5921358"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}

>![](/images/icon-note.gif) **NOTE:**   
>This API supports redirection. During the calling, you can specify only  **stack\_name**  or  **stack\_id**.  

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b19909141494115"><a name="b19909141494115"></a><a name="b19909141494115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b12216171914418"><a name="b12216171914418"></a><a name="b12216171914418"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b17312182014117"><a name="b17312182014117"></a><a name="b17312182014117"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b561062444111"><a name="b561062444111"></a><a name="b561062444111"></a>Description</strong></p>
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
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973125_section53292223"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973125_section9867967"></a>

<a name="table1160115752114"></a>
<table><thead align="left"><tr id="row96285792113"><th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.1"><p id="p239416162216"><a name="p239416162216"></a><a name="p239416162216"></a><strong id="b756018513412"><a name="b756018513412"></a><a name="b756018513412"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.2"><p id="p65991078374"><a name="p65991078374"></a><a name="p65991078374"></a><strong id="b209351455204112"><a name="b209351455204112"></a><a name="b209351455204112"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.3"><p id="p17396126122218"><a name="p17396126122218"></a><a name="p17396126122218"></a><strong id="b10216959104110"><a name="b10216959104110"></a><a name="b10216959104110"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.18488151184882%" id="mcps1.1.5.1.4"><p id="p114046632218"><a name="p114046632218"></a><a name="p114046632218"></a><strong id="b982411216428"><a name="b982411216428"></a><a name="b982411216428"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5621578214"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p3658190142210"><a name="p3658190142210"></a><a name="p3658190142210"></a>stack</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p359997173719"><a name="p359997173719"></a><a name="p359997173719"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p1066314019225"><a name="p1066314019225"></a><a name="p1066314019225"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p767219012210"><a name="p767219012210"></a><a name="p767219012210"></a>Specifies the stack object.</p>
</td>
</tr>
</tbody>
</table>

**stack**  structure information

<a name="en-us_topic_0057973125_table50168316"></a>
<table><thead align="left"><tr id="en-us_topic_0057973125_row55275058"><th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b4930101110421"><a name="b4930101110421"></a><a name="b4930101110421"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b5444516114217"><a name="b5444516114217"></a><a name="b5444516114217"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b1429531919424"><a name="b1429531919424"></a><a name="b1429531919424"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.18488151184882%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b14244142212429"><a name="b14244142212429"></a><a name="b14244142212429"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row196810364234"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p15167947"><a name="en-us_topic_0057973125_p15167947"></a><a name="en-us_topic_0057973125_p15167947"></a>disable_rollback</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p179419223374"><a name="p179419223374"></a><a name="p179419223374"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p20644201"><a name="en-us_topic_0057973125_p20644201"></a><a name="en-us_topic_0057973125_p20644201"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p20921680"><a name="en-us_topic_0057973125_p20921680"></a><a name="en-us_topic_0057973125_p20921680"></a>Specifies whether to perform a rollback when stack creation fails.</p>
</td>
</tr>
<tr id="row4684104472312"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p57340893"><a name="en-us_topic_0057973125_p57340893"></a><a name="en-us_topic_0057973125_p57340893"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p194192212377"><a name="p194192212377"></a><a name="p194192212377"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p14100779"><a name="en-us_topic_0057973125_p14100779"></a><a name="en-us_topic_0057973125_p14100779"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p39197567"><a name="en-us_topic_0057973125_p39197567"></a><a name="en-us_topic_0057973125_p39197567"></a>Describes the stack.</p>
</td>
</tr>
<tr id="row9976155510519"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p17977195512514"><a name="p17977195512514"></a><a name="p17977195512514"></a>parent</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1197716556514"><a name="p1197716556514"></a><a name="p1197716556514"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p109771455145113"><a name="p109771455145113"></a><a name="p109771455145113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p89771855135118"><a name="p89771855135118"></a><a name="p89771855135118"></a>Specifies the ID of the parent stack if the stack is the nesting type.</p>
</td>
</tr>
<tr id="row134631359185111"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p2463205917519"><a name="p2463205917519"></a><a name="p2463205917519"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1346313594517"><a name="p1346313594517"></a><a name="p1346313594517"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p11463185975118"><a name="p11463185975118"></a><a name="p11463185975118"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p946415597514"><a name="p946415597514"></a><a name="p946415597514"></a>Specifies whether to perform a rollback when stack creation fails.</p>
</td>
</tr>
<tr id="row733725112420"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p18192809"><a name="en-us_topic_0057973125_p18192809"></a><a name="en-us_topic_0057973125_p18192809"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1694172233716"><a name="p1694172233716"></a><a name="p1694172233716"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p64331453"><a name="en-us_topic_0057973125_p64331453"></a><a name="en-us_topic_0057973125_p64331453"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p31020730"><a name="en-us_topic_0057973125_p31020730"></a><a name="en-us_topic_0057973125_p31020730"></a>Specifies parameter information of the stack.</p>
</td>
</tr>
<tr id="row1298101842414"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p3338892"><a name="en-us_topic_0057973125_p3338892"></a><a name="en-us_topic_0057973125_p3338892"></a>stack_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p694722143716"><a name="p694722143716"></a><a name="p694722143716"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p2014806"><a name="en-us_topic_0057973125_p2014806"></a><a name="en-us_topic_0057973125_p2014806"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p65806680"><a name="en-us_topic_0057973125_p65806680"></a><a name="en-us_topic_0057973125_p65806680"></a>Describes the stack operation.</p>
</td>
</tr>
<tr id="row1498201842414"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p55194683"><a name="en-us_topic_0057973125_p55194683"></a><a name="en-us_topic_0057973125_p55194683"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p139472273713"><a name="p139472273713"></a><a name="p139472273713"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p41584316"><a name="en-us_topic_0057973125_p41584316"></a><a name="en-us_topic_0057973125_p41584316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p37170869"><a name="en-us_topic_0057973125_p37170869"></a><a name="en-us_topic_0057973125_p37170869"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row16399104655319"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p13399144625319"><a name="p13399144625319"></a><a name="p13399144625319"></a>stack_user_project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p33995462537"><a name="p33995462537"></a><a name="p33995462537"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p6399114625320"><a name="p6399114625320"></a><a name="p6399114625320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p439944665313"><a name="p439944665313"></a><a name="p439944665313"></a>This is a reserved parameter.</p>
</td>
</tr>
<tr id="row1598251819244"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p10982151812244"><a name="p10982151812244"></a><a name="p10982151812244"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p39492216372"><a name="p39492216372"></a><a name="p39492216372"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p1098291817245"><a name="p1098291817245"></a><a name="p1098291817245"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p169828183245"><a name="p169828183245"></a><a name="p169828183245"></a>Specifies the output stack list.</p>
</td>
</tr>
<tr id="row25417237263"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p3959432"><a name="en-us_topic_0057973125_p3959432"></a><a name="en-us_topic_0057973125_p3959432"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p094622173716"><a name="p094622173716"></a><a name="p094622173716"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p52278570"><a name="en-us_topic_0057973125_p52278570"></a><a name="en-us_topic_0057973125_p52278570"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p6296031"><a name="en-us_topic_0057973125_p6296031"></a><a name="en-us_topic_0057973125_p6296031"></a>Specifies the time when the stack was created.</p>
</td>
</tr>
<tr id="row694173642612"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p53759497"><a name="en-us_topic_0057973125_p53759497"></a><a name="en-us_topic_0057973125_p53759497"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p994172203718"><a name="p994172203718"></a><a name="p994172203718"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p59552004"><a name="en-us_topic_0057973125_p59552004"></a><a name="en-us_topic_0057973125_p59552004"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p12893279"><a name="en-us_topic_0057973125_p12893279"></a><a name="en-us_topic_0057973125_p12893279"></a>Specifies the stack URL list.</p>
</td>
</tr>
<tr id="row14367125817267"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p636745872616"><a name="p636745872616"></a><a name="p636745872616"></a>capabilities</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p5947225376"><a name="p5947225376"></a><a name="p5947225376"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p1736745819268"><a name="p1736745819268"></a><a name="p1736745819268"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p1367175812617"><a name="p1367175812617"></a><a name="p1367175812617"></a>Specifies the list of stack capacities.</p>
</td>
</tr>
<tr id="row112293163271"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p112291316182717"><a name="p112291316182717"></a><a name="p112291316182717"></a>notification_topics</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1848310575387"><a name="p1848310575387"></a><a name="p1848310575387"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p13229111662714"><a name="p13229111662714"></a><a name="p13229111662714"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p9229151662718"><a name="p9229151662718"></a><a name="p9229151662718"></a>Specifies the message notification list of the stack.</p>
</td>
</tr>
<tr id="row522917160279"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p65534095"><a name="en-us_topic_0057973125_p65534095"></a><a name="en-us_topic_0057973125_p65534095"></a>timeout_mins</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p10488175773817"><a name="p10488175773817"></a><a name="p10488175773817"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p6661458"><a name="en-us_topic_0057973125_p6661458"></a><a name="en-us_topic_0057973125_p6661458"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p17956409"><a name="en-us_topic_0057973125_p17956409"></a><a name="en-us_topic_0057973125_p17956409"></a>Specifies the timeout duration.</p>
</td>
</tr>
<tr id="row16229716132718"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p52691811"><a name="en-us_topic_0057973125_p52691811"></a><a name="en-us_topic_0057973125_p52691811"></a>stack_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p7490657183815"><a name="p7490657183815"></a><a name="p7490657183815"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p40178308"><a name="en-us_topic_0057973125_p40178308"></a><a name="en-us_topic_0057973125_p40178308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p6264391"><a name="en-us_topic_0057973125_p6264391"></a><a name="en-us_topic_0057973125_p6264391"></a>Specifies the stack status.</p>
</td>
</tr>
<tr id="row1451911514559"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p15191955555"><a name="p15191955555"></a><a name="p15191955555"></a>stack_owner</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1251995175516"><a name="p1251995175516"></a><a name="p1251995175516"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p4519205125516"><a name="p4519205125516"></a><a name="p4519205125516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p1451915185519"><a name="p1451915185519"></a><a name="p1451915185519"></a>This is a reserved parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0057973125_row23587534"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p26404315"><a name="en-us_topic_0057973125_p26404315"></a><a name="en-us_topic_0057973125_p26404315"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p1449310571389"><a name="p1449310571389"></a><a name="p1449310571389"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p58374766"><a name="en-us_topic_0057973125_p58374766"></a><a name="en-us_topic_0057973125_p58374766"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p6556786"><a name="en-us_topic_0057973125_p6556786"></a><a name="en-us_topic_0057973125_p6556786"></a>Specifies the time when the stack was updated.</p>
</td>
</tr>
<tr id="en-us_topic_0057973125_row37964118"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p31542065"><a name="en-us_topic_0057973125_p31542065"></a><a name="en-us_topic_0057973125_p31542065"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p34961757183813"><a name="p34961757183813"></a><a name="p34961757183813"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p4770510"><a name="en-us_topic_0057973125_p4770510"></a><a name="en-us_topic_0057973125_p4770510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p26587856"><a name="en-us_topic_0057973125_p26587856"></a><a name="en-us_topic_0057973125_p26587856"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973125_row66102371"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973125_p3994012"><a name="en-us_topic_0057973125_p3994012"></a><a name="en-us_topic_0057973125_p3994012"></a>template_description</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.2 "><p id="p649985733814"><a name="p649985733814"></a><a name="p649985733814"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973125_p55079576"><a name="en-us_topic_0057973125_p55079576"></a><a name="en-us_topic_0057973125_p55079576"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973125_p62980318"><a name="en-us_topic_0057973125_p62980318"></a><a name="en-us_topic_0057973125_p62980318"></a>Describes the template.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973125_section21702846"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306
```

## Response Example<a name="en-us_topic_0057973125_section61107894"></a>

```
{
    "stack": {
        "disable_rollback": true,
        "description": "Hello world HOT template that just defines a single compute instance. Contains just base features to verify base HOT support.\n",
        "parent": null,
        "tags": null,
        "parameters": {
            "Network": "3f8713b7-8aea-4b0f-a70b-98d4e1d6251f",
            "OS::stack_name": "HeatStack",
            "ImageId": "68e22196-a4aa-4946-85c3-75f4957e667a",
            "OS::stack_id": "c89c4bb3-96cb-4a55-aafa-076a7939a306",
            "KeyName": "heat-key",
            "OS::project_id": "95d02433133a4c0a87ba6967474a2ad3",
            "InstanceType": "m1.tiny"
        },
        "stack_user_project_id": "95d02433133a4c0a87ba6967474a2ad3",
        "stack_status_reason": "Stack create completed successfully",
        "stack_name": "HeatStack",
        "outputs": [],
        "creation_time": "2014-01-26T17:21:35Z",
        "links": [
            {
                "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                "rel": "self"
             }
        ],
        "capabilities": [],
        "notification_topics": [],
        "timeout_mins": 60,
        "stack_status": "CREATE_COMPLETE",
        "stack_owner": null,
        "updated_time": "2014-01-26T17:21:41Z",
        "id": "c89c4bb3-96cb-4a55-aafa-076a7939a306",
        "template_description": "Hello world HOT template that just defines a single compute instance. Contains just base features to verify base HOT support.\n"
    }
}
```

## Return Code<a name="en-us_topic_0057973125_section13100134"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a><strong id="b731785218616"><a name="b731785218616"></a><a name="b731785218616"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973124_p9904457194351"><a name="en-us_topic_0057973124_p9904457194351"></a><a name="en-us_topic_0057973124_p9904457194351"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973124_p64063566194351"><a name="en-us_topic_0057973124_p64063566194351"></a><a name="en-us_topic_0057973124_p64063566194351"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973124_p21766343194351"><a name="en-us_topic_0057973124_p21766343194351"></a><a name="en-us_topic_0057973124_p21766343194351"></a>Request was successful.</p>
</td>
</tr>
<tr id="row18143162895914"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p52068209206"><a name="p52068209206"></a><a name="p52068209206"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p52061120172014"><a name="p52061120172014"></a><a name="p52061120172014"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p620662018205"><a name="p620662018205"></a><a name="p620662018205"></a>The response is about redirection. The response header usually contains a location value that allows you to track the real location of the resource.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b1552942884813"><a name="b1552942884813"></a><a name="b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b956007905"><a name="b956007905"></a><a name="b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b359171417"><a name="b359171417"></a><a name="b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p896118101840"><a name="p896118101840"></a><a name="p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1296211015416"><a name="p1296211015416"></a><a name="p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p9963110146"><a name="p9963110146"></a><a name="p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p125520290312"><a name="p125520290312"></a><a name="p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19789174972712"><a name="p19789174972712"></a><a name="p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p779364918272"><a name="p779364918272"></a><a name="p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p196546319198"><a name="p196546319198"></a><a name="p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

