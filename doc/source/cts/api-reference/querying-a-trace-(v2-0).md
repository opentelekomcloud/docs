# Querying a Trace \(v2.0\)<a name="en-us_topic_0168602252"></a>

## Function<a name="section27109618165546"></a>

This API is used to query records of operations on resources during the last seven days. Compared with v1.0, the request parameter  **trace\_rating**  is changed to  **trace\_status**, and the type of response parameters  **user**,  **request**, and  **resource**  is changed to  **Structure**.

## URI<a name="section32905997165546"></a>

GET /v2.0/\{project\_id\}/\{tracker\_name\}/trace\{?trace\_id,service\_type,resource\_type,resource\_id,resource\_name,trace\_name,trace\_status,user,limit,from,to,next\}

For details about the parameters, see  [Table1 Parameters in the URI](querying-a-trace-(v2-0).md).

**Table  1**  Parameters in the URI

<a name="table32743527165546"></a>
<table><thead align="left"><tr id="row60169999165546"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p41931785165546"><a name="p41931785165546"></a><a name="p41931785165546"></a><strong id="b842352706115119"><a name="b842352706115119"></a><a name="b842352706115119"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p41031452165546"><a name="p41031452165546"></a><a name="p41031452165546"></a><strong id="b842352706115121"><a name="b842352706115121"></a><a name="b842352706115121"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p35213295165546"><a name="p35213295165546"></a><a name="p35213295165546"></a><strong id="b842352706115123"><a name="b842352706115123"></a><a name="b842352706115123"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p33704618165546"><a name="p33704618165546"></a><a name="p33704618165546"></a><strong id="b842352706115259"><a name="b842352706115259"></a><a name="b842352706115259"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row45719542165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p12295418165546"><a name="p12295418165546"></a><a name="p12295418165546"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p56404831165546"><a name="p56404831165546"></a><a name="p56404831165546"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p5388621165546"><a name="p5388621165546"></a><a name="p5388621165546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p33825131165546"><a name="p33825131165546"></a><a name="p33825131165546"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row35990723165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p29567469165546"><a name="p29567469165546"></a><a name="p29567469165546"></a>tracker_name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p46154779165546"><a name="p46154779165546"></a><a name="p46154779165546"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p47549622165546"><a name="p47549622165546"></a><a name="p47549622165546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p26314149165546"><a name="p26314149165546"></a><a name="p26314149165546"></a>Specifies the tracker name. Currently, only tracker "system" is available.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section51071313165546"></a>

-   Parameters

    **Table  2**  Parameters in the request

    <a name="table4326653165546"></a>
    <table><thead align="left"><tr id="row24894309165546"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p3173112165546"><a name="p3173112165546"></a><a name="p3173112165546"></a><strong id="b1318976144"><a name="b1318976144"></a><a name="b1318976144"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p55695557165546"><a name="p55695557165546"></a><a name="p55695557165546"></a><strong id="b965256198"><a name="b965256198"></a><a name="b965256198"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p15046258165546"><a name="p15046258165546"></a><a name="p15046258165546"></a><strong id="b1186757630"><a name="b1186757630"></a><a name="b1186757630"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p10787367165546"><a name="p10787367165546"></a><a name="p10787367165546"></a><strong id="b1204008219"><a name="b1204008219"></a><a name="b1204008219"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1361549165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p43176651165546"><a name="p43176651165546"></a><a name="p43176651165546"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p7647882165546"><a name="p7647882165546"></a><a name="p7647882165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p15498738165546"><a name="p15498738165546"></a><a name="p15498738165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p2667048518032"><a name="p2667048518032"></a><a name="p2667048518032"></a>Specifies the type of a service whose traces are to be queried. The value must be the abbreviation of a cloud service that has been interconnected with CTS. It is a word composed of uppercase letters.</p>
    <p id="p51908309105111"><a name="p51908309105111"></a><a name="p51908309105111"></a>For the interconnected cloud services, see section "Supported Services" in the <em id="i84235269716030"><a name="i84235269716030"></a><a name="i84235269716030"></a>Cloud Trace Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row24291067165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p21419439165546"><a name="p21419439165546"></a><a name="p21419439165546"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p57252999165546"><a name="p57252999165546"></a><a name="p57252999165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p6981356165546"><a name="p6981356165546"></a><a name="p6981356165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p4832241718032"><a name="p4832241718032"></a><a name="p4832241718032"></a>Specifies the type of a resource whose traces are to be queried. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter. For the interconnected cloud services, see section "Supported Services" in the <em id="i19851040113010"><a name="i19851040113010"></a><a name="i19851040113010"></a>Cloud Trace Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row56243953165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p59466324165546"><a name="p59466324165546"></a><a name="p59466324165546"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p52042911165546"><a name="p52042911165546"></a><a name="p52042911165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p54726267165546"><a name="p54726267165546"></a><a name="p54726267165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p3642639165546"><a name="p3642639165546"></a><a name="p3642639165546"></a>Specifies the ID of a resource whose traces are to be queried.</p>
    </td>
    </tr>
    <tr id="row32783758165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p38238762165546"><a name="p38238762165546"></a><a name="p38238762165546"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p10332051165546"><a name="p10332051165546"></a><a name="p10332051165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p31589808165546"><a name="p31589808165546"></a><a name="p31589808165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p8637674165546"><a name="p8637674165546"></a><a name="p8637674165546"></a>Specifies the name of a resource whose traces are to be queried.</p>
    <div class="note" id="note14394599111437"><a name="note14394599111437"></a><a name="note14394599111437"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p62442531111437"><a name="p62442531111437"></a><a name="p62442531111437"></a>The value may contain uppercase letters.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row10630205165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p55740268165546"><a name="p55740268165546"></a><a name="p55740268165546"></a>trace_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p18667884165546"><a name="p18667884165546"></a><a name="p18667884165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p35703653165546"><a name="p35703653165546"></a><a name="p35703653165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p6314750165546"><a name="p6314750165546"></a><a name="p6314750165546"></a>Specifies the operation recorded by this trace.</p>
    <div class="note" id="note42907983111452"><a name="note42907983111452"></a><a name="note42907983111452"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p50627527111452"><a name="p50627527111452"></a><a name="p50627527111452"></a>The value may contain uppercase letters.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row56832750165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p40050010165546"><a name="p40050010165546"></a><a name="p40050010165546"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p22825403165546"><a name="p22825403165546"></a><a name="p22825403165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p36918393165546"><a name="p36918393165546"></a><a name="p36918393165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p37599867165546"><a name="p37599867165546"></a><a name="p37599867165546"></a>Specifies the number of traces returned in the trace list. The default value is <strong id="b13055005113140"><a name="b13055005113140"></a><a name="b13055005113140"></a>50</strong> and the maximum value is <strong id="b1906933113145"><a name="b1906933113145"></a><a name="b1906933113145"></a>200</strong>.</p>
    </td>
    </tr>
    <tr id="row2854490165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p29887101165546"><a name="p29887101165546"></a><a name="p29887101165546"></a>next</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p4936154165546"><a name="p4936154165546"></a><a name="p4936154165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p64284183165546"><a name="p64284183165546"></a><a name="p64284183165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p54490452103033"><a name="p54490452103033"></a><a name="p54490452103033"></a>Specifies the time of a queried trace (you can query traces earlier than the time). The value can be the parameter <strong id="b842352706103332"><a name="b842352706103332"></a><a name="b842352706103332"></a>marker</strong> value in <a href="#table28997784165546">Table 5</a>.</p>
    <p id="p20652022103033"><a name="p20652022103033"></a><a name="p20652022103033"></a>The time condition <strong id="b32627209121556"><a name="b32627209121556"></a><a name="b32627209121556"></a>next</strong> can be used with another time condition <strong id="b5533162012162"><a name="b5533162012162"></a><a name="b5533162012162"></a>from</strong> and <strong id="b26809740121619"><a name="b26809740121619"></a><a name="b26809740121619"></a>to</strong>.</p>
    <p id="p51650473103033"><a name="p51650473103033"></a><a name="p51650473103033"></a>The final query condition is the intersection of the preceding two conditions.</p>
    </td>
    </tr>
    <tr id="row21182530165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p38063335165546"><a name="p38063335165546"></a><a name="p38063335165546"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p63231272165546"><a name="p63231272165546"></a><a name="p63231272165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p21459439165546"><a name="p21459439165546"></a><a name="p21459439165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p60492961165546"><a name="p60492961165546"></a><a name="p60492961165546"></a>Specifies the starting timestamp of the queried trace. The value is in UTC format, accurate to ms, and contains 13 digits. The time spent in selecting this filter is excluded. <strong id="b698899671105531"><a name="b698899671105531"></a><a name="b698899671105531"></a>from</strong> and <strong id="b438122548105531"><a name="b438122548105531"></a><a name="b438122548105531"></a>to</strong> are both used.</p>
    </td>
    </tr>
    <tr id="row7565743165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p8845423165546"><a name="p8845423165546"></a><a name="p8845423165546"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p45390672165546"><a name="p45390672165546"></a><a name="p45390672165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p52765817165546"><a name="p52765817165546"></a><a name="p52765817165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p46172819165546"><a name="p46172819165546"></a><a name="p46172819165546"></a>Specifies the ending timestamp of the queried trace. The value is in UTC format, accurate to ms, and contains 13 digits. The time spent in selecting this filter is excluded. <strong id="b61987530113234"><a name="b61987530113234"></a><a name="b61987530113234"></a>from</strong> and <strong id="b28253901113239"><a name="b28253901113239"></a><a name="b28253901113239"></a>to</strong> are both used.</p>
    </td>
    </tr>
    <tr id="row12902194165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p38444792165546"><a name="p38444792165546"></a><a name="p38444792165546"></a>trace_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p27020418165546"><a name="p27020418165546"></a><a name="p27020418165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p41170232165546"><a name="p41170232165546"></a><a name="p41170232165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p46454532165546"><a name="p46454532165546"></a><a name="p46454532165546"></a>Specifies the ID of a trace.</p>
    <p id="p15437604165546"><a name="p15437604165546"></a><a name="p15437604165546"></a>If this parameter is used as a filter, other filters cannot be selected.</p>
    </td>
    </tr>
    <tr id="row4720715165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p46833655165546"><a name="p46833655165546"></a><a name="p46833655165546"></a>trace_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p35429744165546"><a name="p35429744165546"></a><a name="p35429744165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p51237021165546"><a name="p51237021165546"></a><a name="p51237021165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p56558055165546"><a name="p56558055165546"></a><a name="p56558055165546"></a>Specifies the status of a trace. The value can be <strong id="b4511166231122"><a name="b4511166231122"></a><a name="b4511166231122"></a>normal</strong>, <strong id="b14194326761122"><a name="b14194326761122"></a><a name="b14194326761122"></a>warning</strong>, or <strong id="b8148876051122"><a name="b8148876051122"></a><a name="b8148876051122"></a>incident</strong>.</p>
    </td>
    </tr>
    <tr id="row39260450165546"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p25979873165546"><a name="p25979873165546"></a><a name="p25979873165546"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p23994993165546"><a name="p23994993165546"></a><a name="p23994993165546"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p64546298165546"><a name="p64546298165546"></a><a name="p64546298165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p60867619165546"><a name="p60867619165546"></a><a name="p60867619165546"></a>Specifies a username whose traces are to be queried.</p>
    <div class="note" id="note90750111518"><a name="note90750111518"></a><a name="note90750111518"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p816750111518"><a name="p816750111518"></a><a name="p816750111518"></a>The value may contain uppercase letters.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    GET 
    /v2.0/{project_id}/{tracker_name}/trace?limit=11&to=1479095278000&from=1478490478000&trace_name=createTracker&resource_type=tracker&service_type=CTS
    ```


## Response<a name="section22606120165546"></a>

-   Parameters

    **Table  3**  Parameters in the response

    <a name="table8170248165546"></a>
    <table><thead align="left"><tr id="row61682794165546"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p30250398165546"><a name="p30250398165546"></a><a name="p30250398165546"></a><strong id="b630699742"><a name="b630699742"></a><a name="b630699742"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p34363167165546"><a name="p34363167165546"></a><a name="p34363167165546"></a><strong id="b1873433443"><a name="b1873433443"></a><a name="b1873433443"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p31953108165546"><a name="p31953108165546"></a><a name="p31953108165546"></a><strong id="b1678799229"><a name="b1678799229"></a><a name="b1678799229"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38064933165546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p63360764165546"><a name="p63360764165546"></a><a name="p63360764165546"></a>traces</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p31948222165546"><a name="p31948222165546"></a><a name="p31948222165546"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p37669205165546"><a name="p37669205165546"></a><a name="p37669205165546"></a>Specifies the trace array in the trace list.</p>
    </td>
    </tr>
    <tr id="row59964039104211"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p23393412104219"><a name="p23393412104219"></a><a name="p23393412104219"></a>meta_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p15818213104219"><a name="p15818213104219"></a><a name="p15818213104219"></a>Structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p6206842104219"><a name="p6206842104219"></a><a name="p6206842104219"></a>Specifies the extended field. The value can be <strong id="b842352706111349"><a name="b842352706111349"></a><a name="b842352706111349"></a>count</strong> (number of traces in the response) or <strong id="b842352706111425"><a name="b842352706111425"></a><a name="b842352706111425"></a>marker</strong> (ID of the last trace in the trace list).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Data structure of the  **traces**  field

    <a name="table52822305165546"></a>
    <table><thead align="left"><tr id="row32694645165546"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.4.1.1"><p id="p31020559165546"><a name="p31020559165546"></a><a name="p31020559165546"></a><strong id="b84235270611524"><a name="b84235270611524"></a><a name="b84235270611524"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.060000000000002%" id="mcps1.2.4.1.2"><p id="p29637333165546"><a name="p29637333165546"></a><a name="p29637333165546"></a><strong id="b736988524"><a name="b736988524"></a><a name="b736988524"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.2%" id="mcps1.2.4.1.3"><p id="p51813809165546"><a name="p51813809165546"></a><a name="p51813809165546"></a><strong id="b1629227491"><a name="b1629227491"></a><a name="b1629227491"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36168968165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p44005316165546"><a name="p44005316165546"></a><a name="p44005316165546"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p7660877165546"><a name="p7660877165546"></a><a name="p7660877165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p16551306165546"><a name="p16551306165546"></a><a name="p16551306165546"></a>Specifies the ID of a resource on which operations are performed.</p>
    </td>
    </tr>
    <tr id="row14744032165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p53415943165546"><a name="p53415943165546"></a><a name="p53415943165546"></a>trace_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p31724118165546"><a name="p31724118165546"></a><a name="p31724118165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p66412540103525"><a name="p66412540103525"></a><a name="p66412540103525"></a>Specifies the name of a trace. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter.</p>
    </td>
    </tr>
    <tr id="row41433388165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p661256165546"><a name="p661256165546"></a><a name="p661256165546"></a>trace_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p53561736165546"><a name="p53561736165546"></a><a name="p53561736165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p43533332165546"><a name="p43533332165546"></a><a name="p43533332165546"></a>Specifies the status of a trace. The value can be <strong id="b800828488"><a name="b800828488"></a><a name="b800828488"></a>normal</strong>, <strong id="b1499375875"><a name="b1499375875"></a><a name="b1499375875"></a>warning</strong>, or <strong id="b259490898"><a name="b259490898"></a><a name="b259490898"></a>incident</strong>.</p>
    </td>
    </tr>
    <tr id="row56255675165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p60415813165546"><a name="p60415813165546"></a><a name="p60415813165546"></a>trace_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p61842704165546"><a name="p61842704165546"></a><a name="p61842704165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p43203140165546"><a name="p43203140165546"></a><a name="p43203140165546"></a>Specifies the resource of a trace. The value can be <strong id="b84235270611247"><a name="b84235270611247"></a><a name="b84235270611247"></a>ApiCall</strong>, <strong id="b84235270611251"><a name="b84235270611251"></a><a name="b84235270611251"></a>ConsoleAction</strong>, or <strong id="b84235270611254"><a name="b84235270611254"></a><a name="b84235270611254"></a>SystemAction</strong>.</p>
    </td>
    </tr>
    <tr id="row53283940165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p21031879165546"><a name="p21031879165546"></a><a name="p21031879165546"></a>request</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p25860647165546"><a name="p25860647165546"></a><a name="p25860647165546"></a>Structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p14337643165546"><a name="p14337643165546"></a><a name="p14337643165546"></a>Specifies the request of an operation on resources.</p>
    </td>
    </tr>
    <tr id="row61929926165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p50268124165546"><a name="p50268124165546"></a><a name="p50268124165546"></a>response</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p45186250165546"><a name="p45186250165546"></a><a name="p45186250165546"></a>Structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p36207673165546"><a name="p36207673165546"></a><a name="p36207673165546"></a>Specifies the response to a user request, that is, the returned information for an operation on resources.</p>
    </td>
    </tr>
    <tr id="row57433609165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p21610715165546"><a name="p21610715165546"></a><a name="p21610715165546"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p5637506165546"><a name="p5637506165546"></a><a name="p5637506165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p53984870165546"><a name="p53984870165546"></a><a name="p53984870165546"></a>Specifies the HTTP status code returned by the associated interface and records the response to a user request.</p>
    </td>
    </tr>
    <tr id="row16101786165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p29176291165546"><a name="p29176291165546"></a><a name="p29176291165546"></a>api_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p14469405165546"><a name="p14469405165546"></a><a name="p14469405165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p31171184165546"><a name="p31171184165546"></a><a name="p31171184165546"></a>Specifies the version of the API.</p>
    </td>
    </tr>
    <tr id="row12105202165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p40997276165546"><a name="p40997276165546"></a><a name="p40997276165546"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p32445042165546"><a name="p32445042165546"></a><a name="p32445042165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p10802782165546"><a name="p10802782165546"></a><a name="p10802782165546"></a>Specifies the remarks added by other cloud services to a trace.</p>
    </td>
    </tr>
    <tr id="row30116174165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p23491059165546"><a name="p23491059165546"></a><a name="p23491059165546"></a>record_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p23727649165546"><a name="p23727649165546"></a><a name="p23727649165546"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p42891391165546"><a name="p42891391165546"></a><a name="p42891391165546"></a>Specifies the timestamp when a trace is recorded by CTS.</p>
    </td>
    </tr>
    <tr id="row50584187165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p3678500165546"><a name="p3678500165546"></a><a name="p3678500165546"></a>trace_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p29523053165546"><a name="p29523053165546"></a><a name="p29523053165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p42557054165546"><a name="p42557054165546"></a><a name="p42557054165546"></a>Specifies the ID of a trace. The value is the UUID generated by the system.</p>
    </td>
    </tr>
    <tr id="row47469169165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p19797506165546"><a name="p19797506165546"></a><a name="p19797506165546"></a>time</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p60094192165546"><a name="p60094192165546"></a><a name="p60094192165546"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p35791394165546"><a name="p35791394165546"></a><a name="p35791394165546"></a>Specifies the time when a trace is received.</p>
    </td>
    </tr>
    <tr id="row53687097165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p53687564165546"><a name="p53687564165546"></a><a name="p53687564165546"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p53725465165546"><a name="p53725465165546"></a><a name="p53725465165546"></a>Structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p56795398165546"><a name="p56795398165546"></a><a name="p56795398165546"></a>Specifies the user information for which a trace is triggered.</p>
    </td>
    </tr>
    <tr id="row41396536165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p64785113165546"><a name="p64785113165546"></a><a name="p64785113165546"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p13102766165546"><a name="p13102766165546"></a><a name="p13102766165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p5074752718058"><a name="p5074752718058"></a><a name="p5074752718058"></a>Specifies the type of a service whose traces are to be queried. The value must be the abbreviation of a cloud service that has been interconnected with CTS. It is a word composed of uppercase letters.</p>
    </td>
    </tr>
    <tr id="row22457886165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p7149510165546"><a name="p7149510165546"></a><a name="p7149510165546"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p42239422165546"><a name="p42239422165546"></a><a name="p42239422165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p1796340518058"><a name="p1796340518058"></a><a name="p1796340518058"></a>Specifies the type of a resource whose traces are to be queried. The value is a string of 1 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), and periods (.). In addition, it must start with a letter.</p>
    </td>
    </tr>
    <tr id="row56679075165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p27602363165546"><a name="p27602363165546"></a><a name="p27602363165546"></a>source_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p21198944165546"><a name="p21198944165546"></a><a name="p21198944165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p39392889165546"><a name="p39392889165546"></a><a name="p39392889165546"></a>Specifies the IP address of a user for whom a trace is triggered.</p>
    </td>
    </tr>
    <tr id="row18991685165546"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p61931496165546"><a name="p61931496165546"></a><a name="p61931496165546"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p50395251165546"><a name="p50395251165546"></a><a name="p50395251165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p55483535165546"><a name="p55483535165546"></a><a name="p55483535165546"></a>Specifies the name of a resource whose traces are to be queried.</p>
    </td>
    </tr>
    <tr id="row4585385310527"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p8436414105215"><a name="p8436414105215"></a><a name="p8436414105215"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p12260895105215"><a name="p12260895105215"></a><a name="p12260895105215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p53608433105215"><a name="p53608433105215"></a><a name="p53608433105215"></a>Record the ID of the request.</p>
    </td>
    </tr>
    <tr id="row5438862310527"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p23189049105215"><a name="p23189049105215"></a><a name="p23189049105215"></a>location_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p66373691105215"><a name="p66373691105215"></a><a name="p66373691105215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p7559914105215"><a name="p7559914105215"></a><a name="p7559914105215"></a>Specifies the additional information required for fault locating after a request recording error occurs.</p>
    </td>
    </tr>
    <tr id="row3851496810527"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p8250778105215"><a name="p8250778105215"></a><a name="p8250778105215"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p64333271105215"><a name="p64333271105215"></a><a name="p64333271105215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p43612444105215"><a name="p43612444105215"></a><a name="p43612444105215"></a>This operation involves the endpoint of the page that displays cloud resource details.</p>
    </td>
    </tr>
    <tr id="row1120313510527"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p50979495105215"><a name="p50979495105215"></a><a name="p50979495105215"></a>resource_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p35698408105215"><a name="p35698408105215"></a><a name="p35698408105215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.2%" headers="mcps1.2.4.1.3 "><p id="p5889967105215"><a name="p5889967105215"></a><a name="p5889967105215"></a>This operation involves the access link (excluding the endpoint) of the page that displays cloud resource details.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Data structure description of the  **meta\_data**  field

    <a name="table28997784165546"></a>
    <table><thead align="left"><tr id="row641162165546"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p51934161165546"><a name="p51934161165546"></a><a name="p51934161165546"></a><strong id="b489815982"><a name="b489815982"></a><a name="b489815982"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p45917504165546"><a name="p45917504165546"></a><a name="p45917504165546"></a><strong id="b1637486048"><a name="b1637486048"></a><a name="b1637486048"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p28330368165546"><a name="p28330368165546"></a><a name="p28330368165546"></a><strong id="b2014356007"><a name="b2014356007"></a><a name="b2014356007"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13058489165546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p51104658165546"><a name="p51104658165546"></a><a name="p51104658165546"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p45836595165546"><a name="p45836595165546"></a><a name="p45836595165546"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p21776709165546"><a name="p21776709165546"></a><a name="p21776709165546"></a>Specifies the number of traces returned in the trace list.</p>
    </td>
    </tr>
    <tr id="row61772655165546"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p37529197165546"><a name="p37529197165546"></a><a name="p37529197165546"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p19966127165546"><a name="p19966127165546"></a><a name="p19966127165546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p6643614165546"><a name="p6643614165546"></a><a name="p6643614165546"></a>Specifies the ID of the last trace in the trace list. The value of this parameter can be used as the <strong id="b842352706112324"><a name="b842352706112324"></a><a name="b842352706112324"></a>next</strong> value. If the value of <strong id="b842352706112352"><a name="b842352706112352"></a><a name="b842352706112352"></a>marker</strong> is <strong id="b84235270611240"><a name="b84235270611240"></a><a name="b84235270611240"></a>null</strong>, all traces have been returned.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
      "traces" : [ { 
        "time" : 1472148708232, 
        "user" : {"name":"xxx","id":"a2e899190fcd444084a68fc0ac2sc1e9","domain":{"name":"xxx","id":"05b2598d69bc4a209f9ac5eeeb1f91ad"}}, 
        "response" : {"code":"VPC.0514","message":"Update port fail."}, 
        "code" : 200, 
        "service_type" : "VPC", 
        "resource_type" : "eip", 
        "resource_name" : "192.144.163.1", 
        "resource_id" : "d502809d-0d1d-41ce-9690-784282142ccc", 
        "trace_name" : "deleteEip", 
        "trace_status " : "warning", 
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
        "user" : {"name":"xxx","id":"a2e899190fcd444084a68fc0ac2sc1e9","domain":{"name":"xxx","id":"05b2598d69bc4a209f9ac5eeeb1f91ad"}}, 
    "request": {"servers":[{"id":"3045f042-9a7c-436d-a944-ff76ceb7b477"}],"delete_volume":false,"delete_publicip":false},
        "response" : {"code":"VPC.0514","message":"Update port fail."}, 
        "code" : 200, 
        "service_type" : "VPC", 
        "resource_type" : "eip", 
        "resource_name" : "192.144.163.1", 
        "resource_id" : "d502809d-0d1d-41ce-9690-784282142ccc", 
        "trace_name" : "deleteEip", 
        "trace_status" : "warning", 
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


## Returned Value<a name="section24657413165546"></a>

-   Normal

    **Table  6**  Return code for successful requests

    <a name="table44927131165546"></a>
    <table><thead align="left"><tr id="row21668667165546"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p10331587165546"><a name="p10331587165546"></a><a name="p10331587165546"></a><strong id="b8423527069424"><a name="b8423527069424"></a><a name="b8423527069424"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p31552195165546"><a name="p31552195165546"></a><a name="p31552195165546"></a><strong id="b623689803"><a name="b623689803"></a><a name="b623689803"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5591012165546"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p50218829165546"><a name="p50218829165546"></a><a name="p50218829165546"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p41193383165546"><a name="p41193383165546"></a><a name="p41193383165546"></a>The request is successful and the query result is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    **Table  7**  Return code for failed requests

    <a name="table22395981165546"></a>
    <table><thead align="left"><tr id="row13016504165546"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p47703871165546"><a name="p47703871165546"></a><a name="p47703871165546"></a><strong id="b762307605"><a name="b762307605"></a><a name="b762307605"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p38808363165546"><a name="p38808363165546"></a><a name="p38808363165546"></a><strong id="b1287413589"><a name="b1287413589"></a><a name="b1287413589"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56469732165546"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p10645585165546"><a name="p10645585165546"></a><a name="p10645585165546"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p56986075165546"><a name="p56986075165546"></a><a name="p56986075165546"></a>The query parameters are abnormal.</p>
    </td>
    </tr>
    <tr id="row12766140143550"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p47786399143550"><a name="p47786399143550"></a><a name="p47786399143550"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p45493102143550"><a name="p45493102143550"></a><a name="p45493102143550"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row43112630165546"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p2462133165546"><a name="p2462133165546"></a><a name="p2462133165546"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p65215109165546"><a name="p65215109165546"></a><a name="p65215109165546"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row50065075165546"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p28739263165546"><a name="p28739263165546"></a><a name="p28739263165546"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p46178927165546"><a name="p46178927165546"></a><a name="p46178927165546"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row12957160165546"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p42897034165546"><a name="p42897034165546"></a><a name="p42897034165546"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p52107716165546"><a name="p52107716165546"></a><a name="p52107716165546"></a>The requested trace does not exist.</p>
    </td>
    </tr>
    </tbody>
    </table>


