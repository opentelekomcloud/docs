# Previewing a Stack<a name="EN-US_TOPIC_0084581287"></a>

## Function<a name="en-us_topic_0057973122_section3630399"></a>

This API is used to preview a stack.

## URI<a name="en-us_topic_0057973122_section32673592"></a>

POST /v1/\{project\_id\}/stacks/preview

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p623302764616"><a name="p623302764616"></a><a name="p623302764616"></a><strong id="b149517142109"><a name="b149517142109"></a><a name="b149517142109"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p92386277468"><a name="p92386277468"></a><a name="p92386277468"></a><strong id="b081718593102"><a name="b081718593102"></a><a name="b081718593102"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p72423275465"><a name="p72423275465"></a><a name="p72423275465"></a><strong id="b1892330141114"><a name="b1892330141114"></a><a name="b1892330141114"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p624719271465"><a name="p624719271465"></a><a name="p624719271465"></a><strong id="b175012619115"><a name="b175012619115"></a><a name="b175012619115"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p625562794612"><a name="p625562794612"></a><a name="p625562794612"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1126062744618"><a name="p1126062744618"></a><a name="p1126062744618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1726662744617"><a name="p1726662744617"></a><a name="p1726662744617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1727018275468"><a name="p1727018275468"></a><a name="p1727018275468"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973122_section25626875"></a>

<a name="en-us_topic_0057973122_table4943390911314"></a>
<table><thead align="left"><tr id="en-us_topic_0057973122_row6551718411314"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.1"><p id="p17493122142817"><a name="p17493122142817"></a><a name="p17493122142817"></a><strong id="b116161931114"><a name="b116161931114"></a><a name="b116161931114"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.2"><p id="p1887419221879"><a name="p1887419221879"></a><a name="p1887419221879"></a><strong id="b1812522214115"><a name="b1812522214115"></a><a name="b1812522214115"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.3"><p id="p16493922112813"><a name="p16493922112813"></a><a name="p16493922112813"></a><strong id="b053142521111"><a name="b053142521111"></a><a name="b053142521111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.4"><p id="p94935225284"><a name="p94935225284"></a><a name="p94935225284"></a><strong id="b193871726101119"><a name="b193871726101119"></a><a name="b193871726101119"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.1.6.1.5"><p id="p1549342213284"><a name="p1549342213284"></a><a name="p1549342213284"></a><strong id="b13857203381110"><a name="b13857203381110"></a><a name="b13857203381110"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973122_row4356524411314"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973122_p687852811322"><a name="en-us_topic_0057973122_p687852811322"></a><a name="en-us_topic_0057973122_p687852811322"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p394012418417"><a name="p394012418417"></a><a name="p394012418417"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973122_p2028992511322"><a name="en-us_topic_0057973122_p2028992511322"></a><a name="en-us_topic_0057973122_p2028992511322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973122_p3287125111322"><a name="en-us_topic_0057973122_p3287125111322"></a><a name="en-us_topic_0057973122_p3287125111322"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973122_p4532564911322"><a name="en-us_topic_0057973122_p4532564911322"></a><a name="en-us_topic_0057973122_p4532564911322"></a>Specifies the stack name.</p>
<a name="ul45291469124"></a><a name="ul45291469124"></a><ul id="ul45291469124"><li>The value can contain only uppercase letters, lowercase letters, digits, hyphens (-), periods (.), and underscores (_).</li><li>The value must start with an uppercase letter or a lowercase letter.</li><li>The value can contain 1 to 255 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057973122_row4669483711314"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973122_p2483709111322"><a name="en-us_topic_0057973122_p2483709111322"></a><a name="en-us_topic_0057973122_p2483709111322"></a>template_url</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p10940122417415"><a name="p10940122417415"></a><a name="p10940122417415"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973122_p6564734511322"><a name="en-us_topic_0057973122_p6564734511322"></a><a name="en-us_topic_0057973122_p6564734511322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973122_p1583473211322"><a name="en-us_topic_0057973122_p1583473211322"></a><a name="en-us_topic_0057973122_p1583473211322"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973122_p754489111322"><a name="en-us_topic_0057973122_p754489111322"></a><a name="en-us_topic_0057973122_p754489111322"></a>Specifies the template URL. You cannot select a template using the URL temporarily.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row1869491611314"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973122_p6440780711322"><a name="en-us_topic_0057973122_p6440780711322"></a><a name="en-us_topic_0057973122_p6440780711322"></a>template</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1294002418418"><a name="p1294002418418"></a><a name="p1294002418418"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973122_p4964984011322"><a name="en-us_topic_0057973122_p4964984011322"></a><a name="en-us_topic_0057973122_p4964984011322"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973122_p6221409811322"><a name="en-us_topic_0057973122_p6221409811322"></a><a name="en-us_topic_0057973122_p6221409811322"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973122_p617716411322"><a name="en-us_topic_0057973122_p617716411322"></a><a name="en-us_topic_0057973122_p617716411322"></a>Specifies the template. The template content must use the YAML syntax.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row1496430011314"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973122_p685920411322"><a name="en-us_topic_0057973122_p685920411322"></a><a name="en-us_topic_0057973122_p685920411322"></a>files</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p10940024194112"><a name="p10940024194112"></a><a name="p10940024194112"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973122_p1872467511322"><a name="en-us_topic_0057973122_p1872467511322"></a><a name="en-us_topic_0057973122_p1872467511322"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973122_p4030370211322"><a name="en-us_topic_0057973122_p4030370211322"></a><a name="en-us_topic_0057973122_p4030370211322"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973122_p4337443811322"><a name="en-us_topic_0057973122_p4337443811322"></a><a name="en-us_topic_0057973122_p4337443811322"></a>Specifies the files referenced in the environment.</p>
</td>
</tr>
<tr id="row41337528138"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="p9135852121320"><a name="p9135852121320"></a><a name="p9135852121320"></a>disable_rollback</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1494052418415"><a name="p1494052418415"></a><a name="p1494052418415"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="p913513527134"><a name="p913513527134"></a><a name="p913513527134"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="p1213525281317"><a name="p1213525281317"></a><a name="p1213525281317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="p613515528137"><a name="p613515528137"></a><a name="p613515528137"></a>Specifies whether to perform a rollback when stack creation fails.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row4805106011314"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973122_p1169054111322"><a name="en-us_topic_0057973122_p1169054111322"></a><a name="en-us_topic_0057973122_p1169054111322"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p59406241419"><a name="p59406241419"></a><a name="p59406241419"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973122_p740977911322"><a name="en-us_topic_0057973122_p740977911322"></a><a name="en-us_topic_0057973122_p740977911322"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973122_p6332123311322"><a name="en-us_topic_0057973122_p6332123311322"></a><a name="en-us_topic_0057973122_p6332123311322"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973122_p2874628811322"><a name="en-us_topic_0057973122_p2874628811322"></a><a name="en-us_topic_0057973122_p2874628811322"></a>Specifies parameter information of the stack.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973122_section29315290"></a>

<a name="table1160115752114"></a>
<table><thead align="left"><tr id="row96285792113"><th class="cellrowborder" valign="top" width="18.39%" id="mcps1.1.5.1.1"><p id="p10737181684115"><a name="p10737181684115"></a><a name="p10737181684115"></a><strong id="b1451020319192"><a name="b1451020319192"></a><a name="b1451020319192"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.940000000000001%" id="mcps1.1.5.1.2"><p id="p10741101619416"><a name="p10741101619416"></a><a name="p10741101619416"></a><strong id="b43001562196"><a name="b43001562196"></a><a name="b43001562196"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.09%" id="mcps1.1.5.1.3"><p id="p0746191610413"><a name="p0746191610413"></a><a name="p0746191610413"></a><strong id="b43362916191"><a name="b43362916191"></a><a name="b43362916191"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.580000000000005%" id="mcps1.1.5.1.4"><p id="p0754716144111"><a name="p0754716144111"></a><a name="p0754716144111"></a><strong id="b2131212171912"><a name="b2131212171912"></a><a name="b2131212171912"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5621578214"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.5.1.1 "><p id="p3658190142210"><a name="p3658190142210"></a><a name="p3658190142210"></a>stack</p>
</td>
<td class="cellrowborder" valign="top" width="14.940000000000001%" headers="mcps1.1.5.1.2 "><p id="p83331638134518"><a name="p83331638134518"></a><a name="p83331638134518"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09%" headers="mcps1.1.5.1.3 "><p id="p1066314019225"><a name="p1066314019225"></a><a name="p1066314019225"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50.580000000000005%" headers="mcps1.1.5.1.4 "><p id="p767219012210"><a name="p767219012210"></a><a name="p767219012210"></a>Specifies the stack object.</p>
</td>
</tr>
</tbody>
</table>

**stack**  structure information

<a name="en-us_topic_0057973122_table21028423"></a>
<table><thead align="left"><tr id="en-us_topic_0057973122_row27762594"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p19538715104414"><a name="p19538715104414"></a><a name="p19538715104414"></a><strong id="b13931222199"><a name="b13931222199"></a><a name="b13931222199"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p054301516441"><a name="p054301516441"></a><a name="p054301516441"></a><strong id="b4410162711918"><a name="b4410162711918"></a><a name="b4410162711918"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.3"><p id="p15546515194419"><a name="p15546515194419"></a><a name="p15546515194419"></a><strong id="b1235813017199"><a name="b1235813017199"></a><a name="b1235813017199"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p4555201504411"><a name="p4555201504411"></a><a name="p4555201504411"></a><strong id="b101661733181920"><a name="b101661733181920"></a><a name="b101661733181920"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973122_row17639389"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p19504393"><a name="en-us_topic_0057973122_p19504393"></a><a name="en-us_topic_0057973122_p19504393"></a>parent</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p5472113518428"><a name="p5472113518428"></a><a name="p5472113518428"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p36351961"><a name="en-us_topic_0057973122_p36351961"></a><a name="en-us_topic_0057973122_p36351961"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p314502"><a name="en-us_topic_0057973122_p314502"></a><a name="en-us_topic_0057973122_p314502"></a>Specifies the UUID of the parent stack (for a nested stack).</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row2830526"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p27946073"><a name="en-us_topic_0057973122_p27946073"></a><a name="en-us_topic_0057973122_p27946073"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p16472735114214"><a name="p16472735114214"></a><a name="p16472735114214"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p49039453"><a name="en-us_topic_0057973122_p49039453"></a><a name="en-us_topic_0057973122_p49039453"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p27957437"><a name="en-us_topic_0057973122_p27957437"></a><a name="en-us_topic_0057973122_p27957437"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row50290344"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p46986044"><a name="en-us_topic_0057973122_p46986044"></a><a name="en-us_topic_0057973122_p46986044"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1947243574218"><a name="p1947243574218"></a><a name="p1947243574218"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p47773213"><a name="en-us_topic_0057973122_p47773213"></a><a name="en-us_topic_0057973122_p47773213"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p41656035"><a name="en-us_topic_0057973122_p41656035"></a><a name="en-us_topic_0057973122_p41656035"></a>Specifies the stack URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row39360002"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p34043626"><a name="en-us_topic_0057973122_p34043626"></a><a name="en-us_topic_0057973122_p34043626"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p16472103518428"><a name="p16472103518428"></a><a name="p16472103518428"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p6070306"><a name="en-us_topic_0057973122_p6070306"></a><a name="en-us_topic_0057973122_p6070306"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p31722659"><a name="en-us_topic_0057973122_p31722659"></a><a name="en-us_topic_0057973122_p31722659"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row17068479"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p40369572"><a name="en-us_topic_0057973122_p40369572"></a><a name="en-us_topic_0057973122_p40369572"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1047253517422"><a name="p1047253517422"></a><a name="p1047253517422"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p48709885"><a name="en-us_topic_0057973122_p48709885"></a><a name="en-us_topic_0057973122_p48709885"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p13148205"><a name="en-us_topic_0057973122_p13148205"></a><a name="en-us_topic_0057973122_p13148205"></a>Describes the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row51224983"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p55582963"><a name="en-us_topic_0057973122_p55582963"></a><a name="en-us_topic_0057973122_p55582963"></a>template_description</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p8218145217447"><a name="p8218145217447"></a><a name="p8218145217447"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p5926151"><a name="en-us_topic_0057973122_p5926151"></a><a name="en-us_topic_0057973122_p5926151"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p25450106"><a name="en-us_topic_0057973122_p25450106"></a><a name="en-us_topic_0057973122_p25450106"></a>Describes the template defined by the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row27724363"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p31080936"><a name="en-us_topic_0057973122_p31080936"></a><a name="en-us_topic_0057973122_p31080936"></a>timeout_mins</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1322675284419"><a name="p1322675284419"></a><a name="p1322675284419"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p34527906"><a name="en-us_topic_0057973122_p34527906"></a><a name="en-us_topic_0057973122_p34527906"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p45177739"><a name="en-us_topic_0057973122_p45177739"></a><a name="en-us_topic_0057973122_p45177739"></a>Specifies the timeout duration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row3946468"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p51228509"><a name="en-us_topic_0057973122_p51228509"></a><a name="en-us_topic_0057973122_p51228509"></a>disable_rollback</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1923114527447"><a name="p1923114527447"></a><a name="p1923114527447"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p55868534"><a name="en-us_topic_0057973122_p55868534"></a><a name="en-us_topic_0057973122_p55868534"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p4836521"><a name="en-us_topic_0057973122_p4836521"></a><a name="en-us_topic_0057973122_p4836521"></a>Specifies whether to perform a rollback when stack creation fails.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row43528691"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p36163121"><a name="en-us_topic_0057973122_p36163121"></a><a name="en-us_topic_0057973122_p36163121"></a>capabilities</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1923655274418"><a name="p1923655274418"></a><a name="p1923655274418"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p43531699"><a name="en-us_topic_0057973122_p43531699"></a><a name="en-us_topic_0057973122_p43531699"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p63265957"><a name="en-us_topic_0057973122_p63265957"></a><a name="en-us_topic_0057973122_p63265957"></a>Specifies the list of stack capacities.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row32522706"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p17093519"><a name="en-us_topic_0057973122_p17093519"></a><a name="en-us_topic_0057973122_p17093519"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p11242652114411"><a name="p11242652114411"></a><a name="p11242652114411"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p42397780"><a name="en-us_topic_0057973122_p42397780"></a><a name="en-us_topic_0057973122_p42397780"></a>Date Time</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p5597720"><a name="en-us_topic_0057973122_p5597720"></a><a name="en-us_topic_0057973122_p5597720"></a>Specifies the time when the stack was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row50379488"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p54206759"><a name="en-us_topic_0057973122_p54206759"></a><a name="en-us_topic_0057973122_p54206759"></a>notification_topics</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p12761056154417"><a name="p12761056154417"></a><a name="p12761056154417"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p28671321"><a name="en-us_topic_0057973122_p28671321"></a><a name="en-us_topic_0057973122_p28671321"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p6395812"><a name="en-us_topic_0057973122_p6395812"></a><a name="en-us_topic_0057973122_p6395812"></a>Specifies the message notification list of the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row57562312"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p32035697"><a name="en-us_topic_0057973122_p32035697"></a><a name="en-us_topic_0057973122_p32035697"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p881156134419"><a name="p881156134419"></a><a name="p881156134419"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p44754699"><a name="en-us_topic_0057973122_p44754699"></a><a name="en-us_topic_0057973122_p44754699"></a>Date Time</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p34305585"><a name="en-us_topic_0057973122_p34305585"></a><a name="en-us_topic_0057973122_p34305585"></a>Specifies the last time when the stack was updated.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row40314810"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p44274160"><a name="en-us_topic_0057973122_p44274160"></a><a name="en-us_topic_0057973122_p44274160"></a>stack_owner</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p12861056114414"><a name="p12861056114414"></a><a name="p12861056114414"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p29437244"><a name="en-us_topic_0057973122_p29437244"></a><a name="en-us_topic_0057973122_p29437244"></a>Sting</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p65556783"><a name="en-us_topic_0057973122_p65556783"></a><a name="en-us_topic_0057973122_p65556783"></a>Specifies the name of the stack owner.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row53140143"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p9384301"><a name="en-us_topic_0057973122_p9384301"></a><a name="en-us_topic_0057973122_p9384301"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p792175674414"><a name="p792175674414"></a><a name="p792175674414"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p21930883"><a name="en-us_topic_0057973122_p21930883"></a><a name="en-us_topic_0057973122_p21930883"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p7122137"><a name="en-us_topic_0057973122_p7122137"></a><a name="en-us_topic_0057973122_p7122137"></a>Specifies parameters defined by the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973122_row64099240"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973122_p24655927"><a name="en-us_topic_0057973122_p24655927"></a><a name="en-us_topic_0057973122_p24655927"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p119745618445"><a name="p119745618445"></a><a name="p119745618445"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973122_p50973059"><a name="en-us_topic_0057973122_p50973059"></a><a name="en-us_topic_0057973122_p50973059"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973122_p30770799"><a name="en-us_topic_0057973122_p30770799"></a><a name="en-us_topic_0057973122_p30770799"></a>Specifies the stack resource list.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973122_section62511020"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/preview
{
    "files": {},
    "disable_rollback": true,
    "parameters": {
        "flavor": "m1.heat"
    },
    "stack_name": "teststack",
    "template": {
        "heat_template_version": "2013-05-23",
        "description": "Simple template to test heat commands",
        "parameters": {
            "flavor": {
                "default": "m1.tiny",
                "type": "string"
            }
        },
        "resources": {
            "hello_world": {
                "type": "OS::Nova::Server",
                "properties": {
                    "key_name": "heat_key",
                    "flavor": {
                        "get_param": "flavor"
                    },
                    "image": "40be8d1a-3eb9-40de-8abd-43237517384f",
                    "user_data": "#!/bin/bash -xv\necho \"hello world\" &gt; /root/hello-world.txt\n"
                }
            }
        }
    },
    "timeout_mins": 60
}
```

## Response Example<a name="en-us_topic_0057973122_section25728276"></a>

```
{
    "stack": {
        "capabilities": [],
        "creation_time": "2015-01-31T15:12:36Z",
        "description": "HOT template for Nova Server resource.\n",
        "disable_rollback": true,
        "id": "None",
        "links": [
            {
                "href": "http://x.x.x.x:8004/v1/6e18cc2bdbeb48a5basad2dc499f6804/stacks/test_stack/None",
                "rel": "self"
            }
        ],
        "notification_topics": [],
        "parameters": {
            "OS::project_id": "6e18cc2bdbeb48a5basad2dc499f6804",
            "OS::stack_id": "None",
            "OS::stack_name": "teststack",
            "admin_user": "cloud-user",
            "flavor": "m1.small",
            "image": "F20-cfg",
            "key_name": "heat_key",
            "server_name": "MyServer"
        },
        "parent": null,
        "resources": [
            {
                "attributes": {},
                "description": "",
                "metadata": {},
                "physical_resource_id": "",
                "properties": {
                    "description": "Ping and SSH",
                    "name": "the_sg",
                    "rules": [
                        {
                            "direction": "ingress",
                            "ethertype": "IPv4",
                            "port_range_max": null,
                            "port_range_min": null,
                            "protocol": "icmp",
                            "remote_group_id": null,
                            "remote_ip_prefix": null,
                            "remote_mode": "remote_ip_prefix"
                        },
                        {
                            "direction": "ingress",
                            "ethertype": "IPv4",
                            "port_range_max": 65535,
                            "port_range_min": 1,
                            "protocol": "tcp",
                            "remote_group_id": null,
                            "remote_ip_prefix": null,
                            "remote_mode": "remote_ip_prefix"
                        },
                        {
                            "direction": "ingress",
                            "ethertype": "IPv4",
                            "port_range_max": 65535,
                            "port_range_min": 1,
                            "protocol": "udp",
                            "remote_group_id": null,
                            "remote_ip_prefix": null,
                            "remote_mode": "remote_ip_prefix"
                        }
                    ]
                },
                "required_by": [
                    "server1"
                ],
                "resource_action": "INIT",
                "resource_identity": {
                    "path": "/resources/the_sg_res",
                    "stack_id": "None",
                    "stack_name": "teststack",
                    "tenant": "6e18cc2bdbeb48a5b3cad2dc499f6804"
                },
                "resource_name": "the_sg_res",
                "resource_status": "COMPLETE",
                "resource_status_reason": "",
                "resource_type": "OS::Neutron::SecurityGroup",
                "stack_identity": {
                    "path": "",
                    "stack_id": "None",
                    "stack_name": "teststack",
                    "tenant": "6e18cc2bdbeb48a5b3cad2dc499f6804"
                },
                "stack_name": "teststack",
                "updated_time": "2015-01-31T15:12:36Z"
            },
            {
                "attributes": {
                    "accessIPv4": "",
                    "accessIPv6": "",
                    "addresses": "",
                    "console_urls": "",
                    "first_address": "",
                    "instance_name": "",
                    "name": "MyServer",
                    "networks": "",
                    "show": ""
                },
                "description": "",
                "metadata": {},
                "physical_resource_id": "",
                "properties": {
                    "admin_pass": null,
                    "admin_user": "cloud-user",
                    "availability_zone": null,
                    "block_device_mapping": null,
                    "config_drive": null,
                    "diskConfig": null,
                    "flavor": "m1.small",
                    "flavor_update_policy": "RESIZE",
                    "image": "F20-cfg",
                    "image_update_policy": "REPLACE",
                    "key_name": "heat_key",
                    "metadata": {
                        "ha_stack": "None"
                    },
                    "name": "MyServer",
                    "networks": [
                        {
                            "fixed_ip": null,
                            "network": "private",
                            "port": null,
                            "uuid": null
                        }
                    ],
                    "personality": {},
                    "reservation_id": null,
                    "scheduler_hints": null,
                    "security_groups": [
                        "None"
                    ],
                    "software_config_transport": "POLL_SERVER_CFN",
                    "user_data": "",
                    "user_data_format": "HEAT_CFNTOOLS"
                },
                "required_by": [],
                "resource_action": "INIT",
                "resource_identity": {
                    "path": "/resources/hello_world",
                    "stack_id": "None",
                    "stack_name": "teststack",
                    "tenant": "6e18cc2bdbeb48a3433cad2dc499sdf32234"
                },
                "resource_name": "hello_world",
                "resource_status": "COMPLETE",
                "resource_status_reason": "",
                "resource_type": "OS::Nova::Server",
                "stack_identity": {
                    "path": "",
                    "stack_id": "None",
                    "stack_name": "teststack",
                    "tenant": "6e18cc2bdbeb48a3433cad2dc499sdf32234"
                },
                "stack_name": "teststack",
                "updated_time": "2015-01-31T15:12:36Z"
            }
        ],
        "stack_name": "test_stack",
        "stack_owner": "admin",
        "template_description": "HOT template for Nova Server resource.\n",
        "timeout_mins": null,
        "updated_time": null
    }
}
```

## Return Code<a name="en-us_topic_0057973122_section30227898"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a><strong id="b2876940264"><a name="b2876940264"></a><a name="b2876940264"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0057973117_p8637307194057"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0057973117_p28533244194057"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0057973117_p29491459194057"></a>The resource has been created and is ready for use.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b14562155022311"><a name="b14562155022311"></a><a name="b14562155022311"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b372233500"><a name="b372233500"></a><a name="b372233500"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b1892635879"><a name="b1892635879"></a><a name="b1892635879"></a>Description</strong></p>
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
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p156541031121913"><a name="p156541031121913"></a><a name="p156541031121913"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p12654183112194"><a name="p12654183112194"></a><a name="p12654183112194"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1253585513244"><a name="p1253585513244"></a><a name="p1253585513244"></a>The request could not be processed due to a conflict.</p>
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

