# Querying Software Deployments<a name="EN-US_TOPIC_0085277559"></a>

## Function<a name="en-us_topic_0085081136_section5314816"></a>

This API is used to query software deployments.

## URI<a name="en-us_topic_0085081136_section47833347"></a>

GET /v1/\{project\_id\}/software\_deployments

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b2084954819916"><a name="b2084954819916"></a><a name="b2084954819916"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b198672491591"><a name="b198672491591"></a><a name="b198672491591"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b4758850391"><a name="b4758850391"></a><a name="b4758850391"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b176874512094"><a name="b176874512094"></a><a name="b176874512094"></a>Description</strong></p>
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

## Request Parameter<a name="en-us_topic_0085081136_section27846943"></a>

<a name="en-us_topic_0085081136_table2851385316"></a>
<table><thead align="left"><tr id="en-us_topic_0085081136_row711513185311"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b529115571499"><a name="b529115571499"></a><a name="b529115571499"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b37701758793"><a name="b37701758793"></a><a name="b37701758793"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b1489119592092"><a name="b1489119592092"></a><a name="b1489119592092"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b186524013100"><a name="b186524013100"></a><a name="b186524013100"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b0699181181020"><a name="b0699181181020"></a><a name="b0699181181020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081136_row416813155310"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081136_p8395163391017"><a name="en-us_topic_0085081136_p8395163391017"></a><a name="en-us_topic_0085081136_p8395163391017"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p149392551015"><a name="p149392551015"></a><a name="p149392551015"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081136_p0395103311019"><a name="en-us_topic_0085081136_p0395103311019"></a><a name="en-us_topic_0085081136_p0395103311019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081136_p4395233121016"><a name="en-us_topic_0085081136_p4395233121016"></a><a name="en-us_topic_0085081136_p4395233121016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081136_p63954336109"><a name="en-us_topic_0085081136_p63954336109"></a><a name="en-us_topic_0085081136_p63954336109"></a>Specifies the target server ID.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0085081136_section49295902"></a>

<a name="table1231113618280"></a>
<table><thead align="left"><tr id="row1831214652811"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p13771749115820"><a name="p13771749115820"></a><a name="p13771749115820"></a><strong id="b275811621013"><a name="b275811621013"></a><a name="b275811621013"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.950000000000001%" id="mcps1.1.5.1.2"><p id="p2380104912583"><a name="p2380104912583"></a><a name="p2380104912583"></a><strong id="b126912813104"><a name="b126912813104"></a><a name="b126912813104"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.3"><p id="p53831549195817"><a name="p53831549195817"></a><a name="p53831549195817"></a><strong id="b1317818917107"><a name="b1317818917107"></a><a name="b1317818917107"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.33%" id="mcps1.1.5.1.4"><p id="p4387184911585"><a name="p4387184911585"></a><a name="p4387184911585"></a><strong id="b1624581071020"><a name="b1624581071020"></a><a name="b1624581071020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row193121165288"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p33129618284"><a name="p33129618284"></a><a name="p33129618284"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p1296132961010"><a name="p1296132961010"></a><a name="p1296132961010"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="p16312769280"><a name="p16312769280"></a><a name="p16312769280"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="p2031336112814"><a name="p2031336112814"></a><a name="p2031336112814"></a>Specifies the software deployment resource object.</p>
</td>
</tr>
</tbody>
</table>

**software\_deployments**  structure information

<a name="en-us_topic_0085081136_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081136_row14014710"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p16625145215582"><a name="p16625145215582"></a><a name="p16625145215582"></a><strong id="b17184616151014"><a name="b17184616151014"></a><a name="b17184616151014"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.950000000000001%" id="mcps1.1.5.1.2"><p id="p262895265820"><a name="p262895265820"></a><a name="p262895265820"></a><strong id="b2230121711106"><a name="b2230121711106"></a><a name="b2230121711106"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.3"><p id="p463015210585"><a name="p463015210585"></a><a name="p463015210585"></a><strong id="b112331818111012"><a name="b112331818111012"></a><a name="b112331818111012"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.33%" id="mcps1.1.5.1.4"><p id="p1863355219582"><a name="p1863355219582"></a><a name="p1863355219582"></a><strong id="b4174819131013"><a name="b4174819131013"></a><a name="b4174819131013"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081136_row20801079"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p15887171181112"><a name="en-us_topic_0085081136_p15887171181112"></a><a name="en-us_topic_0085081136_p15887171181112"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p1165152711816"><a name="p1165152711816"></a><a name="p1165152711816"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p1887171151115"><a name="en-us_topic_0085081136_p1887171151115"></a><a name="en-us_topic_0085081136_p1887171151115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p588731111111"><a name="en-us_topic_0085081136_p588731111111"></a><a name="en-us_topic_0085081136_p588731111111"></a>Specifies the stack action that triggers this software deployment resource.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row20715858"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p19887318118"><a name="en-us_topic_0085081136_p19887318118"></a><a name="en-us_topic_0085081136_p19887318118"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p10651327386"><a name="p10651327386"></a><a name="p10651327386"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p2088871101110"><a name="en-us_topic_0085081136_p2088871101110"></a><a name="en-us_topic_0085081136_p2088871101110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p1388821161113"><a name="en-us_topic_0085081136_p1388821161113"></a><a name="en-us_topic_0085081136_p1388821161113"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row26021030"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p1788811141113"><a name="en-us_topic_0085081136_p1788811141113"></a><a name="en-us_topic_0085081136_p1788811141113"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p11651527181"><a name="p11651527181"></a><a name="p11651527181"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p588851181111"><a name="en-us_topic_0085081136_p588851181111"></a><a name="en-us_topic_0085081136_p588851181111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="p593065912411"><a name="p593065912411"></a><a name="p593065912411"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen1698184112517"><a name="screen1698184112517"></a><a name="screen1698184112517"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081136_row45386595"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p788821191114"><a name="en-us_topic_0085081136_p788821191114"></a><a name="en-us_topic_0085081136_p788821191114"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p56517271281"><a name="p56517271281"></a><a name="p56517271281"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p68883120118"><a name="en-us_topic_0085081136_p68883120118"></a><a name="en-us_topic_0085081136_p68883120118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p1688831101115"><a name="en-us_topic_0085081136_p1688831101115"></a><a name="en-us_topic_0085081136_p1688831101115"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row23709572"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p688817114117"><a name="en-us_topic_0085081136_p688817114117"></a><a name="en-us_topic_0085081136_p688817114117"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p13654271382"><a name="p13654271382"></a><a name="p13654271382"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p19888514112"><a name="en-us_topic_0085081136_p19888514112"></a><a name="en-us_topic_0085081136_p19888514112"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p1888161181117"><a name="en-us_topic_0085081136_p1888161181117"></a><a name="en-us_topic_0085081136_p1888161181117"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row1676488279"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p388881141112"><a name="en-us_topic_0085081136_p388881141112"></a><a name="en-us_topic_0085081136_p388881141112"></a>output_values</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p8651427080"><a name="p8651427080"></a><a name="p8651427080"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p688811121111"><a name="en-us_topic_0085081136_p688811121111"></a><a name="en-us_topic_0085081136_p688811121111"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p988891101113"><a name="en-us_topic_0085081136_p988891101113"></a><a name="en-us_topic_0085081136_p988891101113"></a>Specifies output data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row876414818717"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p888817181112"><a name="en-us_topic_0085081136_p888817181112"></a><a name="en-us_topic_0085081136_p888817181112"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p146542716812"><a name="p146542716812"></a><a name="p146542716812"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p14888314118"><a name="en-us_topic_0085081136_p14888314118"></a><a name="en-us_topic_0085081136_p14888314118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p198882111120"><a name="en-us_topic_0085081136_p198882111120"></a><a name="en-us_topic_0085081136_p198882111120"></a>Specifies the server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row576428579"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p15888719114"><a name="en-us_topic_0085081136_p15888719114"></a><a name="en-us_topic_0085081136_p15888719114"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p46510271782"><a name="p46510271782"></a><a name="p46510271782"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p188894115117"><a name="en-us_topic_0085081136_p188894115117"></a><a name="en-us_topic_0085081136_p188894115117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p1788921131115"><a name="en-us_topic_0085081136_p1788921131115"></a><a name="en-us_topic_0085081136_p1788921131115"></a>Specifies the current status of software deployments. Valid values include <strong id="b164383353107"><a name="b164383353107"></a><a name="b164383353107"></a>COMPLETE</strong>, <strong id="b543933514106"><a name="b543933514106"></a><a name="b543933514106"></a>IN_PROGRESS</strong>, and <strong id="b15439143591016"><a name="b15439143591016"></a><a name="b15439143591016"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row17648812714"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p1088917121111"><a name="en-us_topic_0085081136_p1088917121111"></a><a name="en-us_topic_0085081136_p1088917121111"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p16651327689"><a name="p16651327689"></a><a name="p16651327689"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p28891215111"><a name="en-us_topic_0085081136_p28891215111"></a><a name="en-us_topic_0085081136_p28891215111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081136_p158891315114"><a name="en-us_topic_0085081136_p158891315114"></a><a name="en-us_topic_0085081136_p158891315114"></a>Specifies the cause of the software deployment resource status.</p>
</td>
</tr>
<tr id="en-us_topic_0085081136_row196812121172"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081136_p1488951101111"><a name="en-us_topic_0085081136_p1488951101111"></a><a name="en-us_topic_0085081136_p1488951101111"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p2658271381"><a name="p2658271381"></a><a name="p2658271381"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081136_p138891015111"><a name="en-us_topic_0085081136_p138891015111"></a><a name="en-us_topic_0085081136_p138891015111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.5.1.4 "><p id="p746492251"><a name="p746492251"></a><a name="p746492251"></a>Specifies the update time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen118313192514"><a name="screen118313192514"></a><a name="screen118313192514"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081136_section41009935"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments
```

## Response Example<a name="en-us_topic_0085081136_section33545101"></a>

```
{
    "software_deployments": [
        {
            "status": "COMPLETE",
            "server_id": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
            "config_id": "8da95794-2ad9-4979-8ae5-739ce314c5cd",
            "output_values": {
                "deploy_stdout": "Writing to /tmp/barmy\nWritten to /tmp/barmy\n",
                "deploy_stderr": "+ echo Writing to /tmp/barmy\n+ echo fu\n+ cat /tmp/barmy\n+ echo -n The file /tmp/barmy contains fu for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE\n+ echo Written to /tmp/barmy\n+ echo Output to stderr\nOutput to stderr\n",
                "deploy_status_code": 0,
                "result": "The file /tmp/barmy contains fu for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE"
            },
            "input_values": null,
            "action": "CREATE",
            "status_reason": "Outputs received",
            "id": "ef422fa5-719a-419e-a10c-72e3a367b0b8",
            "creation_time": "2015-01-31T15:12:36Z",
            "updated_time": "2015-01-31T15:18:21Z"
        }
    ]
}
```

## Return Code<a name="en-us_topic_0085081136_section33470456"></a>

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

