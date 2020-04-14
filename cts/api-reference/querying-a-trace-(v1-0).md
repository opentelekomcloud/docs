# Querying a Trace \(v1.0\)<a name="en-us_topic_0168602225"></a>

## Function<a name="section64745266"></a>

This API is used to query records of operations performed on resources in the last seven days.

## URI<a name="section45836489"></a>

GET /v1.0/\{project\_id\}/\{tracker\_name\}/trace\{?trace\_id,service\_type,resource\_type,resource\_id,resource\_name,trace\_name,trace\_rating,user,limit,from,to,next\}

For details about the parameters, see  [Querying a Trace \(v1.0\)](querying-a-trace-(v1-0).md).

**Table  1**  Parameters in the URI

<a name="table4606636"></a>
<table><thead align="left"><tr id="row14981763"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a><strong id="b842352706115119"><a name="b842352706115119"></a><a name="b842352706115119"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.5.1.2"><p id="p47975183"><a name="p47975183"></a><a name="p47975183"></a><strong id="b842352706115121"><a name="b842352706115121"></a><a name="b842352706115121"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p60784581"><a name="p60784581"></a><a name="p60784581"></a><strong id="b842352706115123"><a name="b842352706115123"></a><a name="b842352706115123"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p24604028"><a name="p24604028"></a><a name="p24604028"></a><strong id="b842352706115125"><a name="b842352706115125"></a><a name="b842352706115125"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46769243"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p30212363"><a name="p30212363"></a><a name="p30212363"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p31282356"><a name="p31282356"></a><a name="p31282356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p50842877"><a name="p50842877"></a><a name="p50842877"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24632334"><a name="p24632334"></a><a name="p24632334"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row20364417"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p38905106"><a name="p38905106"></a><a name="p38905106"></a>tracker_name</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p64305920"><a name="p64305920"></a><a name="p64305920"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p41397042"><a name="p41397042"></a><a name="p41397042"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p64826129"><a name="p64826129"></a><a name="p64826129"></a>Specifies the tracker name. Currently, only tracker "system" is available.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section9875225"></a>

-   Parameters

    **Table  2**  Parameters in the request

    <a name="table56410643103525"></a>
    <table><thead align="left"><tr id="row41825310103525"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p32406925103525"><a name="p32406925103525"></a><a name="p32406925103525"></a><strong id="b842352706115130"><a name="b842352706115130"></a><a name="b842352706115130"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p7715257103525"><a name="p7715257103525"></a><a name="p7715257103525"></a><strong id="b2017926937"><a name="b2017926937"></a><a name="b2017926937"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p20956041103525"><a name="p20956041103525"></a><a name="p20956041103525"></a><strong id="b1861722161"><a name="b1861722161"></a><a name="b1861722161"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p19717733103525"><a name="p19717733103525"></a><a name="p19717733103525"></a><strong id="b842352706115136"><a name="b842352706115136"></a><a name="b842352706115136"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53632566103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p49270628103525"><a name="p49270628103525"></a><a name="p49270628103525"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p31497942103525"><a name="p31497942103525"></a><a name="p31497942103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1196533103525"><a name="p1196533103525"></a><a name="p1196533103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p29810344103525"><a name="p29810344103525"></a><a name="p29810344103525"></a>Specifies the type of a service whose traces are to be queried. The value must be the abbreviation of a cloud service that has been interconnected with CTS. It is a word composed of uppercase letters. For the interconnected cloud services, see section "Supported Services" in the <em id="i84235269716030"><a name="i84235269716030"></a><a name="i84235269716030"></a>Cloud Trace Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row18127808153342"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p276965153352"><a name="p276965153352"></a><a name="p276965153352"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22434206153352"><a name="p22434206153352"></a><a name="p22434206153352"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p5231432153352"><a name="p5231432153352"></a><a name="p5231432153352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p21092875153352"><a name="p21092875153352"></a><a name="p21092875153352"></a>Specifies the type of a resource whose traces are to be queried. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter. For the interconnected cloud services, see section "Supported Services" in the <em id="i577693511222"><a name="i577693511222"></a><a name="i577693511222"></a>Cloud Trace Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row66966509103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p55578138103525"><a name="p55578138103525"></a><a name="p55578138103525"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p5535311103525"><a name="p5535311103525"></a><a name="p5535311103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p45707061103525"><a name="p45707061103525"></a><a name="p45707061103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p11284467103525"><a name="p11284467103525"></a><a name="p11284467103525"></a>Specifies the ID of a resource whose traces are to be queried.</p>
    </td>
    </tr>
    <tr id="row34451347103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p39095754103525"><a name="p39095754103525"></a><a name="p39095754103525"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p12639468103525"><a name="p12639468103525"></a><a name="p12639468103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p17164003103525"><a name="p17164003103525"></a><a name="p17164003103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p48107031103525"><a name="p48107031103525"></a><a name="p48107031103525"></a>Specifies the name of a resource whose traces are to be queried.</p>
    </td>
    </tr>
    <tr id="row30310099103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p39198956103525"><a name="p39198956103525"></a><a name="p39198956103525"></a>trace_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p20998902103525"><a name="p20998902103525"></a><a name="p20998902103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p23189529103525"><a name="p23189529103525"></a><a name="p23189529103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p13429115614491"><a name="p13429115614491"></a><a name="p13429115614491"></a>Specifies the operation recorded by this trace. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter.</p>
    </td>
    </tr>
    <tr id="row60841949103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p29250819103525"><a name="p29250819103525"></a><a name="p29250819103525"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p20506175103525"><a name="p20506175103525"></a><a name="p20506175103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p50387446103525"><a name="p50387446103525"></a><a name="p50387446103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p54851346103525"><a name="p54851346103525"></a><a name="p54851346103525"></a>Specifies the number of traces returned in the trace list. The default value is <strong id="b53157894112437"><a name="b53157894112437"></a><a name="b53157894112437"></a>50</strong> and the maximum value is <strong id="b52239541112443"><a name="b52239541112443"></a><a name="b52239541112443"></a>200</strong>.</p>
    </td>
    </tr>
    <tr id="row23900074103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p56857816103525"><a name="p56857816103525"></a><a name="p56857816103525"></a>next</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p42080350103525"><a name="p42080350103525"></a><a name="p42080350103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p53065189103525"><a name="p53065189103525"></a><a name="p53065189103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p4229899610362"><a name="p4229899610362"></a><a name="p4229899610362"></a>Specifies the time of a queried trace (you can query traces earlier than the time). The value can be the parameter <strong id="b842352706103332"><a name="b842352706103332"></a><a name="b842352706103332"></a>marker</strong> value in <a href="#table48500328103927">Table 5</a>.</p>
    <p id="p20652022103033"><a name="p20652022103033"></a><a name="p20652022103033"></a>The time condition <strong id="b2723187112649"><a name="b2723187112649"></a><a name="b2723187112649"></a>next</strong> can be used with another time condition<strong id="b54551593121255"><a name="b54551593121255"></a><a name="b54551593121255"></a> from</strong> and <strong id="b3133181712132"><a name="b3133181712132"></a><a name="b3133181712132"></a>to</strong>.</p>
    <p id="p51650473103033"><a name="p51650473103033"></a><a name="p51650473103033"></a>The final query condition is the intersection of the preceding two conditions.</p>
    </td>
    </tr>
    <tr id="row29817403103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p66399418103525"><a name="p66399418103525"></a><a name="p66399418103525"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9643766103525"><a name="p9643766103525"></a><a name="p9643766103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p42947542103525"><a name="p42947542103525"></a><a name="p42947542103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p56198850103525"><a name="p56198850103525"></a><a name="p56198850103525"></a>Specifies the starting timestamp of the queried trace. The value is in UTC format, accurate to ms, and contains 13 digits. The time spent in selecting this filter is excluded. <strong id="b4486900121235"><a name="b4486900121235"></a><a name="b4486900121235"></a>from</strong> and <strong id="b53531184121242"><a name="b53531184121242"></a><a name="b53531184121242"></a>to</strong> are both used.</p>
    </td>
    </tr>
    <tr id="row36027609103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p32555203103525"><a name="p32555203103525"></a><a name="p32555203103525"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p19725806103525"><a name="p19725806103525"></a><a name="p19725806103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p54286466103525"><a name="p54286466103525"></a><a name="p54286466103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p35127589103525"><a name="p35127589103525"></a><a name="p35127589103525"></a>Specifies the ending timestamp of the queried trace. The value is in UTC format, accurate to ms, and contains 13 digits. The time spent in selecting this filter is excluded. The query criteria <strong id="b65405768121220"><a name="b65405768121220"></a><a name="b65405768121220"></a>to</strong> and <strong id="b6575787612128"><a name="b6575787612128"></a><a name="b6575787612128"></a>from</strong> are both used.</p>
    </td>
    </tr>
    <tr id="row47712853103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p39535893103525"><a name="p39535893103525"></a><a name="p39535893103525"></a>trace_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p48290745103525"><a name="p48290745103525"></a><a name="p48290745103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p19236266103525"><a name="p19236266103525"></a><a name="p19236266103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p2904422814350"><a name="p2904422814350"></a><a name="p2904422814350"></a>Specifies the ID of a trace.</p>
    <p id="p14633679103525"><a name="p14633679103525"></a><a name="p14633679103525"></a>If this parameter is used as a filter, other filters cannot be selected.</p>
    </td>
    </tr>
    <tr id="row64594248103525"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p64751639103525"><a name="p64751639103525"></a><a name="p64751639103525"></a>trace_rating</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10391439103525"><a name="p10391439103525"></a><a name="p10391439103525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p36400215103525"><a name="p36400215103525"></a><a name="p36400215103525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p62736279103525"><a name="p62736279103525"></a><a name="p62736279103525"></a>Specifies the status of a trace. The value can be <strong id="b84235270611014"><a name="b84235270611014"></a><a name="b84235270611014"></a>normal</strong>, <strong id="b84235270611017"><a name="b84235270611017"></a><a name="b84235270611017"></a>warning</strong>, or <strong id="b84235270611021"><a name="b84235270611021"></a><a name="b84235270611021"></a>incident</strong>.</p>
    </td>
    </tr>
    <tr id="row6037854154330"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p27095741154332"><a name="p27095741154332"></a><a name="p27095741154332"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p47271419154332"><a name="p47271419154332"></a><a name="p47271419154332"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p3779770154332"><a name="p3779770154332"></a><a name="p3779770154332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p37725986154332"><a name="p37725986154332"></a><a name="p37725986154332"></a>Specifies a username whose traces are to be queried.</p>
    <div class="note" id="note20149460111234"><a name="note20149460111234"></a><a name="note20149460111234"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p47127417111234"><a name="p47127417111234"></a><a name="p47127417111234"></a>The value may contain uppercase letters.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    GET /v1.0/{project_id}/{tracker_name}/trace?limit=11&to=1479095278000&from=1478490478000&trace_name=createTracker&resource_type=tracker&service_type=CTS
    ```


## Response<a name="section21768161"></a>

-   Parameters

    **Table  3**  Parameters in the response

    <a name="table56607133103757"></a>
    <table><thead align="left"><tr id="row58259530103757"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p21401509103757"><a name="p21401509103757"></a><a name="p21401509103757"></a><strong id="b842352706115143"><a name="b842352706115143"></a><a name="b842352706115143"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p55800681103757"><a name="p55800681103757"></a><a name="p55800681103757"></a><strong id="b842352706115145"><a name="b842352706115145"></a><a name="b842352706115145"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23561276103757"><a name="p23561276103757"></a><a name="p23561276103757"></a><strong id="b842352706115146"><a name="b842352706115146"></a><a name="b842352706115146"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29415241103757"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1546304910475"><a name="p1546304910475"></a><a name="p1546304910475"></a>traces</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11723840103922"><a name="p11723840103922"></a><a name="p11723840103922"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59395281103757"><a name="p59395281103757"></a><a name="p59395281103757"></a>Specifies the trace array in the trace list.</p>
    </td>
    </tr>
    <tr id="row417247010401"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2030576410409"><a name="p2030576410409"></a><a name="p2030576410409"></a>meta_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3415420210409"><a name="p3415420210409"></a><a name="p3415420210409"></a>Structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1502698410409"><a name="p1502698410409"></a><a name="p1502698410409"></a>Specifies the extended field. The value can be <strong id="b842352706111349"><a name="b842352706111349"></a><a name="b842352706111349"></a>count</strong> (number of traces in the response) or <strong id="b842352706111425"><a name="b842352706111425"></a><a name="b842352706111425"></a>marker</strong> (ID of the last trace in the trace list).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Data structure description of the  **traces**  field

    <a name="table55869834103845"></a>
    <table><thead align="left"><tr id="row9404537103845"><th class="cellrowborder" valign="top" width="24.312431243124312%" id="mcps1.2.4.1.1"><p id="p23570009103845"><a name="p23570009103845"></a><a name="p23570009103845"></a><strong id="b84235270611524"><a name="b84235270611524"></a><a name="b84235270611524"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.343634363436344%" id="mcps1.2.4.1.2"><p id="p30122586103845"><a name="p30122586103845"></a><a name="p30122586103845"></a><strong id="b270523588"><a name="b270523588"></a><a name="b270523588"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.34393439343935%" id="mcps1.2.4.1.3"><p id="p24010403103845"><a name="p24010403103845"></a><a name="p24010403103845"></a><strong id="b842352706115156"><a name="b842352706115156"></a><a name="b842352706115156"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65794525103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p27756336103845"><a name="p27756336103845"></a><a name="p27756336103845"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p33670723103845"><a name="p33670723103845"></a><a name="p33670723103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p42974014103845"><a name="p42974014103845"></a><a name="p42974014103845"></a>Specifies the ID of a resource on which operations are performed.</p>
    </td>
    </tr>
    <tr id="row51221810103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p55325982103845"><a name="p55325982103845"></a><a name="p55325982103845"></a>trace_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p52219525103845"><a name="p52219525103845"></a><a name="p52219525103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p1923153103845"><a name="p1923153103845"></a><a name="p1923153103845"></a>Specifies the name of a trace. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter.</p>
    </td>
    </tr>
    <tr id="row17308385103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p59801919103845"><a name="p59801919103845"></a><a name="p59801919103845"></a>trace_rating</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p12117237103845"><a name="p12117237103845"></a><a name="p12117237103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p41972140103845"><a name="p41972140103845"></a><a name="p41972140103845"></a>Specifies the status of a trace. The value can be <strong id="b4511166231122"><a name="b4511166231122"></a><a name="b4511166231122"></a>normal</strong>, <strong id="b14194326761122"><a name="b14194326761122"></a><a name="b14194326761122"></a>warning</strong>, or <strong id="b8148876051122"><a name="b8148876051122"></a><a name="b8148876051122"></a>incident</strong>.</p>
    </td>
    </tr>
    <tr id="row42204943103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p63157226103845"><a name="p63157226103845"></a><a name="p63157226103845"></a>trace_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p15461657103845"><a name="p15461657103845"></a><a name="p15461657103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p44434693103845"><a name="p44434693103845"></a><a name="p44434693103845"></a>Specifies the resource of a trace. The value can be <strong id="b84235270611247"><a name="b84235270611247"></a><a name="b84235270611247"></a>ApiCall</strong>, <strong id="b84235270611251"><a name="b84235270611251"></a><a name="b84235270611251"></a>ConsoleAction</strong>, or <strong id="b84235270611254"><a name="b84235270611254"></a><a name="b84235270611254"></a>SystemAction</strong>.</p>
    </td>
    </tr>
    <tr id="row64367917103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p46418750103845"><a name="p46418750103845"></a><a name="p46418750103845"></a>request</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p1822400103845"><a name="p1822400103845"></a><a name="p1822400103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p13396698103845"><a name="p13396698103845"></a><a name="p13396698103845"></a>Specifies the request of an operation on resources.</p>
    </td>
    </tr>
    <tr id="row53461424103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p35408098103845"><a name="p35408098103845"></a><a name="p35408098103845"></a>response</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p49483713103845"><a name="p49483713103845"></a><a name="p49483713103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p48757812103845"><a name="p48757812103845"></a><a name="p48757812103845"></a>Specifies the response to a user request, that is, the returned information for an operation on resources.</p>
    </td>
    </tr>
    <tr id="row36167129103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p43856326103845"><a name="p43856326103845"></a><a name="p43856326103845"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p62701499103845"><a name="p62701499103845"></a><a name="p62701499103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p45656673103845"><a name="p45656673103845"></a><a name="p45656673103845"></a>Records the response to a user request and specifies the HTTP status code returned by the API recorded in the trace.</p>
    </td>
    </tr>
    <tr id="row8256878103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p64827359103845"><a name="p64827359103845"></a><a name="p64827359103845"></a>api_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p16524758103845"><a name="p16524758103845"></a><a name="p16524758103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p63436984103845"><a name="p63436984103845"></a><a name="p63436984103845"></a>Specifies the version of the API.</p>
    </td>
    </tr>
    <tr id="row34061950103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p7554542103845"><a name="p7554542103845"></a><a name="p7554542103845"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p7938175103845"><a name="p7938175103845"></a><a name="p7938175103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p39012440103845"><a name="p39012440103845"></a><a name="p39012440103845"></a>Specifies the remarks added by other cloud services to a trace.</p>
    </td>
    </tr>
    <tr id="row15567648103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p53019961103845"><a name="p53019961103845"></a><a name="p53019961103845"></a>record_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p66758447103845"><a name="p66758447103845"></a><a name="p66758447103845"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p38725097103845"><a name="p38725097103845"></a><a name="p38725097103845"></a>Specifies the timestamp when a trace is recorded by CTS.</p>
    </td>
    </tr>
    <tr id="row48829470103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p62873031103845"><a name="p62873031103845"></a><a name="p62873031103845"></a>trace_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p59550756103845"><a name="p59550756103845"></a><a name="p59550756103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p58881950103845"><a name="p58881950103845"></a><a name="p58881950103845"></a>Specifies the ID of a trace. The value is the UUID generated by the system.</p>
    </td>
    </tr>
    <tr id="row60175505103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p42377728103845"><a name="p42377728103845"></a><a name="p42377728103845"></a>time</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p10043968103845"><a name="p10043968103845"></a><a name="p10043968103845"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p8255097103845"><a name="p8255097103845"></a><a name="p8255097103845"></a>Specifies the time when a trace occurs.</p>
    </td>
    </tr>
    <tr id="row7187010103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p45276898103845"><a name="p45276898103845"></a><a name="p45276898103845"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p43550094103845"><a name="p43550094103845"></a><a name="p43550094103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p37896751103845"><a name="p37896751103845"></a><a name="p37896751103845"></a>Specifies the user information for which a trace is triggered.</p>
    </td>
    </tr>
    <tr id="row5526447103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p44989082103845"><a name="p44989082103845"></a><a name="p44989082103845"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p20237038103845"><a name="p20237038103845"></a><a name="p20237038103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p331504131803"><a name="p331504131803"></a><a name="p331504131803"></a>Specifies the type of a service whose traces are to be queried. The value must be the abbreviation of a cloud service that has been interconnected with CTS. It is a word composed of uppercase letters.</p>
    </td>
    </tr>
    <tr id="row55959521103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p36427361103845"><a name="p36427361103845"></a><a name="p36427361103845"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p64935109103845"><a name="p64935109103845"></a><a name="p64935109103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p74605161803"><a name="p74605161803"></a><a name="p74605161803"></a>Specifies the type of a resource whose traces are to be queried. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter.</p>
    </td>
    </tr>
    <tr id="row25945638103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p21221940103845"><a name="p21221940103845"></a><a name="p21221940103845"></a>source_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p41255619103845"><a name="p41255619103845"></a><a name="p41255619103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p53370875103845"><a name="p53370875103845"></a><a name="p53370875103845"></a>Specifies the IP address of a user for whom a trace is triggered.</p>
    </td>
    </tr>
    <tr id="row10575829103845"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p51335836103845"><a name="p51335836103845"></a><a name="p51335836103845"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p64562080103845"><a name="p64562080103845"></a><a name="p64562080103845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p62145992103845"><a name="p62145992103845"></a><a name="p62145992103845"></a>Specifies the name of a resource whose traces are to be queried.</p>
    </td>
    </tr>
    <tr id="row6596178210491"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p7510018104911"><a name="p7510018104911"></a><a name="p7510018104911"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p4331721104911"><a name="p4331721104911"></a><a name="p4331721104911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p15325112104911"><a name="p15325112104911"></a><a name="p15325112104911"></a>Specifies the ID of a request.</p>
    </td>
    </tr>
    <tr id="row3759090210491"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p31935806104911"><a name="p31935806104911"></a><a name="p31935806104911"></a>location_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p36663482104911"><a name="p36663482104911"></a><a name="p36663482104911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p16952026104911"><a name="p16952026104911"></a><a name="p16952026104911"></a>Specifies the additional information required for fault locating after a request recording error occurs.</p>
    </td>
    </tr>
    <tr id="row4068348010491"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p9996093104911"><a name="p9996093104911"></a><a name="p9996093104911"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p4377191104911"><a name="p4377191104911"></a><a name="p4377191104911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p19008210104911"><a name="p19008210104911"></a><a name="p19008210104911"></a>This operation involves the endpoint of the page that displays cloud resource details.</p>
    </td>
    </tr>
    <tr id="row5848032510491"><td class="cellrowborder" valign="top" width="24.312431243124312%" headers="mcps1.2.4.1.1 "><p id="p32559574104911"><a name="p32559574104911"></a><a name="p32559574104911"></a>resource_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.2.4.1.2 "><p id="p20079833104911"><a name="p20079833104911"></a><a name="p20079833104911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.34393439343935%" headers="mcps1.2.4.1.3 "><p id="p15853785104911"><a name="p15853785104911"></a><a name="p15853785104911"></a>This operation involves the access link (excluding the endpoint) of the page that displays cloud resource details.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Data structure of the  **meta\_data**  field

    <a name="table48500328103927"></a>
    <table><thead align="left"><tr id="row24886748103927"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2560697103927"><a name="p2560697103927"></a><a name="p2560697103927"></a><strong id="b802546764"><a name="b802546764"></a><a name="b802546764"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p6089886103927"><a name="p6089886103927"></a><a name="p6089886103927"></a><strong id="b393713899"><a name="b393713899"></a><a name="b393713899"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23518772103927"><a name="p23518772103927"></a><a name="p23518772103927"></a><strong id="b842352706115216"><a name="b842352706115216"></a><a name="b842352706115216"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25972386103927"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23388561103927"><a name="p23388561103927"></a><a name="p23388561103927"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15425321103927"><a name="p15425321103927"></a><a name="p15425321103927"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41491473103927"><a name="p41491473103927"></a><a name="p41491473103927"></a>Specifies the trace array in the trace list.</p>
    </td>
    </tr>
    <tr id="row37878938103927"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48295166103927"><a name="p48295166103927"></a><a name="p48295166103927"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19594374103927"><a name="p19594374103927"></a><a name="p19594374103927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43640475103927"><a name="p43640475103927"></a><a name="p43640475103927"></a>Specifies the ID of the last trace in the trace list. The value of this parameter can be used as the <strong id="b842352706112324"><a name="b842352706112324"></a><a name="b842352706112324"></a>next</strong> value. If the value of <strong id="b842352706112352"><a name="b842352706112352"></a><a name="b842352706112352"></a>marker</strong> is <strong id="b84235270611240"><a name="b84235270611240"></a><a name="b84235270611240"></a>null</strong>, all traces have been returned.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "traces" : [ {
        "time" : 1472148708232,
        "user" : "{\"name\":\"xxx\",\"domain\":{\"name\":\"xxx\",\"id\":\"ded649d814464428ba89d04d7955c93e\"},\"assumedBy\":{\"user\":{\"name\":\"bss_bm_admin\",\"id\":\"c5140af45b5d4b399dea8f900f1dcf1b\",\"domain\":{\"name\":\"op_service\",\"id\":\"71ce673175024d0495664e525e52bac0\"}}}}",
        "response" : "{\"code\":\"VPC.0514\",\"message\":\"Update port fail.\"}",
        "code" : 200,
        "service_type" : "VPC",
        "resource_type" : "eip",
        "resource_name" : "192.144.163.1",
        "resource_id" : "d502809d-0d1d-41ce-9690-784282142ccc",
        "trace_name" : "deleteEip",
        "trace_rating" : "warning",
        "trace_type" : "ConsoleAction",
        "api_version" : "2.0",
        "record_time" : 1481066128032,
        "trace_id" : "e001ccb9-bc09-11e6-b00b-4b2a61338db6"
        "request_id" : "a0001c1b9-bctt-2136-c12b-4b2a611116"
        "location_info" : "resource has been deleted"
        "endpoint" : "https://*****/vpc?agencyId=***&region=***&locale=zh-cn#"
        "resource_url" : "/vpc/vpcmanager/vpcs?vpcid=*****"
      }, {
        "time" : 1472148708232,
        "user" : "{\"name\":\"xxx\",\"domain\":{\"name\":\"xxx\",\"id\":\"ded649d814464428ba89d04d7955c93e\"},\"assumedBy\":{\"user\":{\"name\":\"bss_bm_admin\",\"id\":\"c5140af45b5d4b399dea8f900f1dcf1b\",\"domain\":{\"name\":\"op_service\",\"id\":\"71ce673175024d0495664e525e52bac0\"}}}}",
        "response" : "{\"code\":\"VPC.0514\",\"message\":\"Update port fail.\"}",
        "code" : 200,
        "service_type" : "VPC",
        "resource_type" : "eip",
        "resource_name" : "192.144.163.1",
        "resource_id" : "d502809d-0d1d-41ce-9690-784282142ccc",
        "trace_name" : "deleteEip",
        "trace_rating" : "warning",
        "trace_type" : "ConsoleAction",
        "api_version" : "2.0",
        "record_time" : 1481066128032,
        "trace_id" : "e001ccb8-bc09-11e6-b2cc-2640a43cc6e8"
        "request_id" : "a0001c1b9-bctt-2136-c12b-4b2a611116"
        "location_info" : "resource has been deleted"
        "endpoint" : "https://*****/vpc?agencyId=***&region=***&locale=zh-cn#"
        "resource_url" : "/vpc/vpcmanager/vpcs?vpcid=*****"
      } ],
      "meta_data" : {
        "count" : 2,
        "marker" : "e001ccb8-bc09-11e6-b2cc-2640a43cc6e8"
      }
    }
    ```


## Returned Value<a name="section61695723"></a>

-   Normal

    **Table  6**  Return code for successful requests

    <a name="table25056856"></a>
    <table><thead align="left"><tr id="row33223577"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p6755232"><a name="p6755232"></a><a name="p6755232"></a><strong id="b842352706115228"><a name="b842352706115228"></a><a name="b842352706115228"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p10302948"><a name="p10302948"></a><a name="p10302948"></a><strong id="b842352706115231"><a name="b842352706115231"></a><a name="b842352706115231"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29232460"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p19019073"><a name="p19019073"></a><a name="p19019073"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p64149930"><a name="p64149930"></a><a name="p64149930"></a>The request is successful and the query result is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  7**  Return code for failed requests

    <a name="table5762915104223"></a>
    <table><thead align="left"><tr id="row52456994104223"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p21158149104223"><a name="p21158149104223"></a><a name="p21158149104223"></a><strong id="b842352706115236"><a name="b842352706115236"></a><a name="b842352706115236"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p36088488104223"><a name="p36088488104223"></a><a name="p36088488104223"></a><strong id="b842352706115239"><a name="b842352706115239"></a><a name="b842352706115239"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37486387104223"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p16498511104223"><a name="p16498511104223"></a><a name="p16498511104223"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p61311011104223"><a name="p61311011104223"></a><a name="p61311011104223"></a>The query parameters are abnormal.</p>
    </td>
    </tr>
    <tr id="row350748814345"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p3156739914345"><a name="p3156739914345"></a><a name="p3156739914345"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p682253614345"><a name="p682253614345"></a><a name="p682253614345"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row14928194104223"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p2354193614518"><a name="p2354193614518"></a><a name="p2354193614518"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p2784867014518"><a name="p2784867014518"></a><a name="p2784867014518"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row19762237145057"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p3480422114518"><a name="p3480422114518"></a><a name="p3480422114518"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p56961514518"><a name="p56961514518"></a><a name="p56961514518"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row63066207145053"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p8089155145053"><a name="p8089155145053"></a><a name="p8089155145053"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p51241782145053"><a name="p51241782145053"></a><a name="p51241782145053"></a>The requested trace does not exist.</p>
    </td>
    </tr>
    </tbody>
    </table>


