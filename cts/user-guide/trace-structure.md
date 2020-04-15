# Trace Structure<a name="en-us_topic_0030598500"></a>

The structure of a trace consists of multiple key fields. For details, see  [Table 1](#table5990537610133).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Formats of some fields displayed on the management console are optimized for easy understanding.  
>-   This section describes the key fields of a trace displayed on the management console.  

**Table  1**  Key fields of traces

<a name="table5990537610133"></a>
<table><thead align="left"><tr id="row1625683610133"><th class="cellrowborder" valign="top" width="22.93%" id="mcps1.2.5.1.1"><p id="p46500856101327"><a name="p46500856101327"></a><a name="p46500856101327"></a><strong id="b842352706185933"><a name="b842352706185933"></a><a name="b842352706185933"></a>Field</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.2"><p id="p57380060101327"><a name="p57380060101327"></a><a name="p57380060101327"></a><strong id="b842352706185943"><a name="b842352706185943"></a><a name="b842352706185943"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.3"><p id="p12377949101327"><a name="p12377949101327"></a><a name="p12377949101327"></a><strong id="b842352706185949"><a name="b842352706185949"></a><a name="b842352706185949"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.98%" id="mcps1.2.5.1.4"><p id="p52511153101327"><a name="p52511153101327"></a><a name="p52511153101327"></a><strong id="b842352706185955"><a name="b842352706185955"></a><a name="b842352706185955"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1139455610133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p11592904101327"><a name="p11592904101327"></a><a name="p11592904101327"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p66393383101327"><a name="p66393383101327"></a><a name="p66393383101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p42020367101327"><a name="p42020367101327"></a><a name="p42020367101327"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p23639477153428"><a name="p23639477153428"></a><a name="p23639477153428"></a>Time when a trace occurred.</p>
<p id="p4071827102556"><a name="p4071827102556"></a><a name="p4071827102556"></a>The value is the local standard time (GMT+local time zone), for example, 12/08/2016 11:24:04 GMT+08:00. This field is transmitted and stored in the form of a timestamp. It is the total number of milliseconds from 00:00:00 on January 1, 1970 (UTC), or 08:00:00 on January 1, 1970 (CST) to the current time.</p>
</td>
</tr>
<tr id="row886636810133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p46466146101327"><a name="p46466146101327"></a><a name="p46466146101327"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p36261921101327"><a name="p36261921101327"></a><a name="p36261921101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p45775395101327"><a name="p45775395101327"></a><a name="p45775395101327"></a>Structure</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p31800255105711"><a name="p31800255105711"></a><a name="p31800255105711"></a>Cloud account used to perform an operation</p>
<p id="p44718377161010"><a name="p44718377161010"></a><a name="p44718377161010"></a>This field is displayed in the <strong id="b84235270616541"><a name="b84235270616541"></a><a name="b84235270616541"></a>Operator</strong> column on the <strong id="b8423527061664"><a name="b8423527061664"></a><a name="b8423527061664"></a>Trace List</strong> page.</p>
<p id="p3194957101327"><a name="p3194957101327"></a><a name="p3194957101327"></a>This field is transmitted and stored in the API in the form of a string.</p>
</td>
</tr>
<tr id="row32393711202213"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p36626726202235"><a name="p36626726202235"></a><a name="p36626726202235"></a>request</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p13974852202235"><a name="p13974852202235"></a><a name="p13974852202235"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p47489789105821"><a name="p47489789105821"></a><a name="p47489789105821"></a>Structure</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p22019939114358"><a name="p22019939114358"></a><a name="p22019939114358"></a>Content requested by an operation</p>
<p id="p59418024141541"><a name="p59418024141541"></a><a name="p59418024141541"></a>This field is transmitted and stored in the API in the form of a string.</p>
</td>
</tr>
<tr id="row25337910202225"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p55934061202247"><a name="p55934061202247"></a><a name="p55934061202247"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p34365079202247"><a name="p34365079202247"></a><a name="p34365079202247"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p32108034202247"><a name="p32108034202247"></a><a name="p32108034202247"></a>Structure</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p2288546411440"><a name="p2288546411440"></a><a name="p2288546411440"></a>Response to the request by an operation</p>
<p id="p50613974202247"><a name="p50613974202247"></a><a name="p50613974202247"></a>This field is transmitted and stored in the API in the form of a string.</p>
</td>
</tr>
<tr id="row3400177210133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p27358325101327"><a name="p27358325101327"></a><a name="p27358325101327"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p47880356101327"><a name="p47880356101327"></a><a name="p47880356101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p61917803101327"><a name="p61917803101327"></a><a name="p61917803101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p62307095101327"><a name="p62307095101327"></a><a name="p62307095101327"></a>Operation source</p>
</td>
</tr>
<tr id="row6113356310133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p5918869101327"><a name="p5918869101327"></a><a name="p5918869101327"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p45740997101327"><a name="p45740997101327"></a><a name="p45740997101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p29041933101327"><a name="p29041933101327"></a><a name="p29041933101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p29691780101327"><a name="p29691780101327"></a><a name="p29691780101327"></a>Resource type</p>
</td>
</tr>
<tr id="row54093169202317"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p40008263202342"><a name="p40008263202342"></a><a name="p40008263202342"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p19443862202342"><a name="p19443862202342"></a><a name="p19443862202342"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p31449014202342"><a name="p31449014202342"></a><a name="p31449014202342"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p64342223202342"><a name="p64342223202342"></a><a name="p64342223202342"></a>Resource name</p>
</td>
</tr>
<tr id="row50964001202322"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p61050661202349"><a name="p61050661202349"></a><a name="p61050661202349"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p46156524202349"><a name="p46156524202349"></a><a name="p46156524202349"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p47690992202349"><a name="p47690992202349"></a><a name="p47690992202349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p37765144202349"><a name="p37765144202349"></a><a name="p37765144202349"></a>Unique resource ID</p>
</td>
</tr>
<tr id="row6471375110133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p8121385101327"><a name="p8121385101327"></a><a name="p8121385101327"></a>source_ip</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p42951013101327"><a name="p42951013101327"></a><a name="p42951013101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p21034936101327"><a name="p21034936101327"></a><a name="p21034936101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p901982293237"><a name="p901982293237"></a><a name="p901982293237"></a>IP address of the user that performs an operation</p>
<p id="p23342406111319"><a name="p23342406111319"></a><a name="p23342406111319"></a>The value of this parameter is empty if the operation is triggered by the system.</p>
</td>
</tr>
<tr id="row797100710133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p39959197101327"><a name="p39959197101327"></a><a name="p39959197101327"></a>trace_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p23757488101327"><a name="p23757488101327"></a><a name="p23757488101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p2331672101327"><a name="p2331672101327"></a><a name="p2331672101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p27020491101327"><a name="p27020491101327"></a><a name="p27020491101327"></a>Operation name</p>
</td>
</tr>
<tr id="row5559914110133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p57889993101327"><a name="p57889993101327"></a><a name="p57889993101327"></a>trace_status</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p30847771101327"><a name="p30847771101327"></a><a name="p30847771101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p56315599101327"><a name="p56315599101327"></a><a name="p56315599101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p956176993250"><a name="p956176993250"></a><a name="p956176993250"></a>Trace level</p>
<p id="p26984706101327"><a name="p26984706101327"></a><a name="p26984706101327"></a>The value can be <strong id="b1687248915371"><a name="b1687248915371"></a><a name="b1687248915371"></a>All trace statuses</strong>, <strong id="b842352706163520"><a name="b842352706163520"></a><a name="b842352706163520"></a>normal</strong>, <strong id="b842352706163524"><a name="b842352706163524"></a><a name="b842352706163524"></a>warning</strong>, or <strong id="b842352706163529"><a name="b842352706163529"></a><a name="b842352706163529"></a>incident</strong>.</p>
</td>
</tr>
<tr id="row2343889910133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p65632398101327"><a name="p65632398101327"></a><a name="p65632398101327"></a>trace_type</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p4288500101327"><a name="p4288500101327"></a><a name="p4288500101327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p21992213101327"><a name="p21992213101327"></a><a name="p21992213101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p2688969418274"><a name="p2688969418274"></a><a name="p2688969418274"></a>Operation type.</p>
<p id="p2527827914544"><a name="p2527827914544"></a><a name="p2527827914544"></a>There are three types of operations:</p>
<a name="ul38353002163137"></a><a name="ul38353002163137"></a><ul id="ul38353002163137"><li>ConsoleAction: operations performed on the management console</li><li>SystemAction: operations triggered by the system</li><li>ApiCall: operations triggered by invoking ApiGateway.</li></ul>
</td>
</tr>
<tr id="row1241397510133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p63842392101327"><a name="p63842392101327"></a><a name="p63842392101327"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p1381752101327"><a name="p1381752101327"></a><a name="p1381752101327"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p23456773101327"><a name="p23456773101327"></a><a name="p23456773101327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p58763902101327"><a name="p58763902101327"></a><a name="p58763902101327"></a>API version of the cloud service on which an operation is performed</p>
</td>
</tr>
<tr id="row4148322210133"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p22030648101327"><a name="p22030648101327"></a><a name="p22030648101327"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p34179318101327"><a name="p34179318101327"></a><a name="p34179318101327"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p54407694115827"><a name="p54407694115827"></a><a name="p54407694115827"></a>Structure</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p58604731101327"><a name="p58604731101327"></a><a name="p58604731101327"></a>Supplementary information</p>
</td>
</tr>
<tr id="row6208394611377"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p32520660113716"><a name="p32520660113716"></a><a name="p32520660113716"></a>record_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p16927771113716"><a name="p16927771113716"></a><a name="p16927771113716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p28972231113716"><a name="p28972231113716"></a><a name="p28972231113716"></a>Number</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p65049408113716"><a name="p65049408113716"></a><a name="p65049408113716"></a>Record time (time stamp) of an operation</p>
</td>
</tr>
<tr id="row819916113712"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p42160859113716"><a name="p42160859113716"></a><a name="p42160859113716"></a>trace_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p59586418113716"><a name="p59586418113716"></a><a name="p59586418113716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p61770545113716"><a name="p61770545113716"></a><a name="p61770545113716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p37358273113716"><a name="p37358273113716"></a><a name="p37358273113716"></a>Unique operation ID</p>
</td>
</tr>
<tr id="row19510966115849"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p3411250115856"><a name="p3411250115856"></a><a name="p3411250115856"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p7875853115856"><a name="p7875853115856"></a><a name="p7875853115856"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p33964369115856"><a name="p33964369115856"></a><a name="p33964369115856"></a>Number</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p66759332115856"><a name="p66759332115856"></a><a name="p66759332115856"></a>Trace HTTP return code, for example, 200 or 400</p>
</td>
</tr>
<tr id="row8891409115849"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p19867569115856"><a name="p19867569115856"></a><a name="p19867569115856"></a>request_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p65769222115856"><a name="p65769222115856"></a><a name="p65769222115856"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p25706743115856"><a name="p25706743115856"></a><a name="p25706743115856"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p1871470115856"><a name="p1871470115856"></a><a name="p1871470115856"></a>Records the ID of the request.</p>
</td>
</tr>
<tr id="row36766385115849"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p47243846115856"><a name="p47243846115856"></a><a name="p47243846115856"></a>location_info</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p1546327115856"><a name="p1546327115856"></a><a name="p1546327115856"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p58143664115856"><a name="p58143664115856"></a><a name="p58143664115856"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p12016378115856"><a name="p12016378115856"></a><a name="p12016378115856"></a>Additional information required for fault locating after a request recording error occurs</p>
</td>
</tr>
<tr id="row57387917115849"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p35787847115856"><a name="p35787847115856"></a><a name="p35787847115856"></a>endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p13134465115856"><a name="p13134465115856"></a><a name="p13134465115856"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p57258727115856"><a name="p57258727115856"></a><a name="p57258727115856"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p7445347115856"><a name="p7445347115856"></a><a name="p7445347115856"></a>Endpoint of the page that displays details of cloud resources involved in this operation</p>
</td>
</tr>
<tr id="row18306788115849"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p10132590115856"><a name="p10132590115856"></a><a name="p10132590115856"></a>resource_url</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p15433436115856"><a name="p15433436115856"></a><a name="p15433436115856"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="p42148770115856"><a name="p42148770115856"></a><a name="p42148770115856"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.98%" headers="mcps1.2.5.1.4 "><p id="p58607209115856"><a name="p58607209115856"></a><a name="p58607209115856"></a>Access link (excluding the endpoint) of the page that displays details of cloud resources involved in this operation</p>
</td>
</tr>
</tbody>
</table>

