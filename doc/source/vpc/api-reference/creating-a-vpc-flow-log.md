# Creating a VPC Flow Log<a name="vpc_flow_0001"></a>

## Function<a name="section1349945813399"></a>

This API is used to create a flow log.

A VPC flow log captures information about the traffic going to and from your VPC. You can use flow logs to monitor network traffic, analyze network attacks, and to determine whether security group and firewall rules need to be modified.

VPC flow logs must be used together with the Log Tank Service \(LTS\). You need to create a log group and a log topic in LTS, and then create a VPC flow log.

## URI<a name="section149915853914"></a>

POST /v1/\{project\_id\}/fl/flow\_logs

[Table 1](#table1851575853914)  describes the parameters.

**Table  1**  Parameter description

<a name="table1851575853914"></a>
<table><thead align="left"><tr id="row1993745814390"><th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.1"><p id="p15937165816394"><a name="p15937165816394"></a><a name="p15937165816394"></a><strong id="b148487544110"><a name="b148487544110"></a><a name="b148487544110"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.2.5.1.2"><p id="p4937658183913"><a name="p4937658183913"></a><a name="p4937658183913"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.2.5.1.3"><p id="p11937458183910"><a name="p11937458183910"></a><a name="p11937458183910"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.5.1.4"><p id="p493715883917"><a name="p493715883917"></a><a name="p493715883917"></a><strong id="b1638383415"><a name="b1638383415"></a><a name="b1638383415"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row793795843915"><td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.1 "><p id="p13937658153913"><a name="p13937658153913"></a><a name="p13937658153913"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.2 "><p id="p16937158183920"><a name="p16937158183920"></a><a name="p16937158183920"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.3 "><p id="p893755819399"><a name="p893755819399"></a><a name="p893755819399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section153175823910"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table853105814391"></a>
    <table><thead align="left"><tr id="row89371858113911"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p1893785863911"><a name="p1893785863911"></a><a name="p1893785863911"></a><strong id="b0379530164116"><a name="b0379530164116"></a><a name="b0379530164116"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p6937115819397"><a name="p6937115819397"></a><a name="p6937115819397"></a><strong id="b04561731204119"><a name="b04561731204119"></a><a name="b04561731204119"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p193720580393"><a name="p193720580393"></a><a name="p193720580393"></a><strong id="b163631632194115"><a name="b163631632194115"></a><a name="b163631632194115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row893785811396"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p893725818397"><a name="p893725818397"></a><a name="p893725818397"></a>flow_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p179370582392"><a name="p179370582392"></a><a name="p179370582392"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p159372058193910"><a name="p159372058193910"></a><a name="p159372058193910"></a>Specifies the <strong id="b4840913185011"><a name="b4840913185011"></a><a name="b4840913185011"></a>FlowLog</strong> objects. For details, see <a href="#table656165873916">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **FlowLog**  field

    <a name="table656165873916"></a>
    <table><thead align="left"><tr id="row129371158123910"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="p17937758103914"><a name="p17937758103914"></a><a name="p17937758103914"></a><strong id="b9571724134214"><a name="b9571724134214"></a><a name="b9571724134214"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p169371258113915"><a name="p169371258113915"></a><a name="p169371258113915"></a><strong id="b14210103884214"><a name="b14210103884214"></a><a name="b14210103884214"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p3937558163918"><a name="p3937558163918"></a><a name="p3937558163918"></a><strong id="b12194739174213"><a name="b12194739174213"></a><a name="b12194739174213"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p1693716581396"><a name="p1693716581396"></a><a name="p1693716581396"></a><strong id="b1795114012421"><a name="b1795114012421"></a><a name="b1795114012421"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1293785823916"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p49371458203916"><a name="p49371458203916"></a><a name="p49371458203916"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p293765812392"><a name="p293765812392"></a><a name="p293765812392"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17937185814394"><a name="p17937185814394"></a><a name="p17937185814394"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><a name="ul29861294319"></a><a name="ul29861294319"></a><ul id="ul29861294319"><li>Specifies the VPC flow log name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row693745853920"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p7937195814395"><a name="p7937195814395"></a><a name="p7937195814395"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p149375582393"><a name="p149375582393"></a><a name="p149375582393"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p3937958103917"><a name="p3937958103917"></a><a name="p3937958103917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><a name="ul74054431539"></a><a name="ul74054431539"></a><ul id="ul74054431539"><li>Provides supplementary information about the VPC flow log.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row593795883919"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p1593710582399"><a name="p1593710582399"></a><a name="p1593710582399"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1293715833911"><a name="p1293715833911"></a><a name="p1293715833911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17937458123914"><a name="p17937458123914"></a><a name="p17937458123914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p1393714588394"><a name="p1393714588394"></a><a name="p1393714588394"></a>Specifies the type of resource on which to create the VPC flow log. The value can be <strong id="b842352706112827"><a name="b842352706112827"></a><a name="b842352706112827"></a>Port</strong>, <strong id="b842352706112830"><a name="b842352706112830"></a><a name="b842352706112830"></a>VPC</strong>, and <strong id="b842352706112837"><a name="b842352706112837"></a><a name="b842352706112837"></a>Network</strong>.</p>
    </td>
    </tr>
    <tr id="row2937145893912"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p1937115863912"><a name="p1937115863912"></a><a name="p1937115863912"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p13937145815398"><a name="p13937145815398"></a><a name="p13937145815398"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p2093735811398"><a name="p2093735811398"></a><a name="p2093735811398"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p6937458133920"><a name="p6937458133920"></a><a name="p6937458133920"></a>Specifies the unique resource ID.</p>
    </td>
    </tr>
    <tr id="row393717581395"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p1093735814394"><a name="p1093735814394"></a><a name="p1093735814394"></a>traffic_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p9937135853911"><a name="p9937135853911"></a><a name="p9937135853911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1693745883918"><a name="p1693745883918"></a><a name="p1693745883918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p393735833917"><a name="p393735833917"></a><a name="p393735833917"></a>Specifies the type of traffic to log. The value can be:</p>
    <a name="ul10871656142914"></a><a name="ul10871656142914"></a><ul id="ul10871656142914"><li><strong id="b1142885935314"><a name="b1142885935314"></a><a name="b1142885935314"></a>all</strong>: specifies that both accepted and rejected traffic of the specified resource will be logged.</li><li><strong id="b6510107155413"><a name="b6510107155413"></a><a name="b6510107155413"></a>accept</strong>: specifies that only accepted inbound and outbound traffic of the specified resource will be logged.</li><li><strong id="b1644231585510"><a name="b1644231585510"></a><a name="b1644231585510"></a>reject</strong>: specifies that only rejected inbound and outbound traffic of the specified resource will be logged.</li></ul>
    </td>
    </tr>
    <tr id="row10937358203912"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p159372581393"><a name="p159372581393"></a><a name="p159372581393"></a>log_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p593745863919"><a name="p593745863919"></a><a name="p593745863919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1193795803911"><a name="p1193795803911"></a><a name="p1193795803911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p199371458183912"><a name="p199371458183912"></a><a name="p199371458183912"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    <tr id="row793717586396"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p7937115812398"><a name="p7937115812398"></a><a name="p7937115812398"></a>log_topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p19371558173919"><a name="p19371558173919"></a><a name="p19371558173919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15937258103911"><a name="p15937258103911"></a><a name="p15937258103911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p9937145823911"><a name="p9937145823911"></a><a name="p9937145823911"></a>Specifies the log topic ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1/b2782e6708b8475c993e6064bc456bf8/fl/flow_logs
    
    {
        "flow_log": {
            "name": "flowlog",
            "description": "just a test",
            "resource_type": "port",
            "resource_id": "05c4052d-8d14-488f-aa00-19fea5a25fde",
            "traffic_type": "reject",
            "log_group_id": "05c4052d-8d14-488f-aa00-19fea5a25fdd",
            "log_topic_id": "a9d7dee7-37d2-4cba-a208-a016252aaa63"
        }
    }
    ```


## Response Message<a name="section16608358193917"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table14625205817393"></a>
    <table><thead align="left"><tr id="row11937145810398"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p59374583391"><a name="p59374583391"></a><a name="p59374583391"></a><strong id="b482011482012"><a name="b482011482012"></a><a name="b482011482012"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p3937155873918"><a name="p3937155873918"></a><a name="p3937155873918"></a><strong id="b10803155207"><a name="b10803155207"></a><a name="b10803155207"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p693745883919"><a name="p693745883919"></a><a name="p693745883919"></a><strong id="b338506162015"><a name="b338506162015"></a><a name="b338506162015"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row119371558143915"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p99371758183910"><a name="p99371758183910"></a><a name="p99371758183910"></a>flow_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1193755843911"><a name="p1193755843911"></a><a name="p1193755843911"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p119374580399"><a name="p119374580399"></a><a name="p119374580399"></a>Specifies the <strong id="b615112620232"><a name="b615112620232"></a><a name="b615112620232"></a>FlowLog</strong> objects. For details, see <a href="#table763920584395">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **FlowLog**  field

    <a name="table763920584395"></a>
    <table><thead align="left"><tr id="row1993725815391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p293714582397"><a name="p293714582397"></a><a name="p293714582397"></a><strong id="b1784731242012"><a name="b1784731242012"></a><a name="b1784731242012"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p149371458113917"><a name="p149371458113917"></a><a name="p149371458113917"></a><strong id="b19890101314206"><a name="b19890101314206"></a><a name="b19890101314206"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="p159376583395"><a name="p159376583395"></a><a name="p159376583395"></a><strong id="b9651714122010"><a name="b9651714122010"></a><a name="b9651714122010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29378583393"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1937205819397"><a name="p1937205819397"></a><a name="p1937205819397"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p5937105873915"><a name="p5937105873915"></a><a name="p5937105873915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p29371758183911"><a name="p29371758183911"></a><a name="p29371758183911"></a>Specifies the VPC flow log UUID.</p>
    </td>
    </tr>
    <tr id="row1293725816394"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20937145883911"><a name="p20937145883911"></a><a name="p20937145883911"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p10937105813391"><a name="p10937105813391"></a><a name="p10937105813391"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p3618473146"><a name="p3618473146"></a><a name="p3618473146"></a>Specifies the VPC flow log name.</p>
    </td>
    </tr>
    <tr id="row6937758193914"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1793711586397"><a name="p1793711586397"></a><a name="p1793711586397"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p15937135818397"><a name="p15937135818397"></a><a name="p15937135818397"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p33561446172111"><a name="p33561446172111"></a><a name="p33561446172111"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8937258173912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p593705817390"><a name="p593705817390"></a><a name="p593705817390"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p093712588392"><a name="p093712588392"></a><a name="p093712588392"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p26023187145"><a name="p26023187145"></a><a name="p26023187145"></a>Provides supplementary information about the VPC flow log.</p>
    </td>
    </tr>
    <tr id="row7937205883910"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1393795823920"><a name="p1393795823920"></a><a name="p1393795823920"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p10937858133920"><a name="p10937858133920"></a><a name="p10937858133920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1293717582396"><a name="p1293717582396"></a><a name="p1293717582396"></a>Specifies the type of resource on which to create the VPC flow log.</p>
    </td>
    </tr>
    <tr id="row189371758133919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p693745853910"><a name="p693745853910"></a><a name="p693745853910"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1893725843915"><a name="p1893725843915"></a><a name="p1893725843915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p893718589392"><a name="p893718589392"></a><a name="p893718589392"></a>Specifies the unique resource ID.</p>
    </td>
    </tr>
    <tr id="row19371458163912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11937135813399"><a name="p11937135813399"></a><a name="p11937135813399"></a>traffic_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p159371058143918"><a name="p159371058143918"></a><a name="p159371058143918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p49371958143918"><a name="p49371958143918"></a><a name="p49371958143918"></a>Specifies the type of traffic to log.</p>
    </td>
    </tr>
    <tr id="row1993795813391"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11937258153912"><a name="p11937258153912"></a><a name="p11937258153912"></a>log_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1593716589399"><a name="p1593716589399"></a><a name="p1593716589399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p13937458163911"><a name="p13937458163911"></a><a name="p13937458163911"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    <tr id="row69371358193919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9937105811399"><a name="p9937105811399"></a><a name="p9937105811399"></a>log_topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p3937195853911"><a name="p3937195853911"></a><a name="p3937195853911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p8937105811390"><a name="p8937105811390"></a><a name="p8937105811390"></a>Specifies the log topic ID.</p>
    </td>
    </tr>
    <tr id="row149526285714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1948613611718"><a name="p1948613611718"></a><a name="p1948613611718"></a>admin_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p11486936674"><a name="p11486936674"></a><a name="p11486936674"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p184867361474"><a name="p184867361474"></a><a name="p184867361474"></a>Specifies whether to enable the VPC flow log function.</p>
    </td>
    </tr>
    <tr id="row102334258716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p74861036479"><a name="p74861036479"></a><a name="p74861036479"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p1948613361478"><a name="p1948613361478"></a><a name="p1948613361478"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1092449185"><a name="p1092449185"></a><a name="p1092449185"></a>Specifies the VPC flow log status.</p>
    <a name="ul12491821389"></a><a name="ul12491821389"></a><ul id="ul12491821389"><li><strong id="b842352706192644"><a name="b842352706192644"></a><a name="b842352706192644"></a>ACTIVE</strong>: Enabled</li><li><strong id="b84235270619274"><a name="b84235270619274"></a><a name="b84235270619274"></a>DOWN</strong>: Disabled</li><li><strong id="b842352706192830"><a name="b842352706192830"></a><a name="b842352706192830"></a>ERROR</strong>: Abnormal fault</li></ul>
    </td>
    </tr>
    <tr id="row593715813910"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6937125803920"><a name="p6937125803920"></a><a name="p6937125803920"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p6937105823914"><a name="p6937105823914"></a><a name="p6937105823914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p1193719586393"><a name="p1193719586393"></a><a name="p1193719586393"></a>Specifies the time when the VPC flow log was created.</p>
    </td>
    </tr>
    <tr id="row0937358193913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1793713589392"><a name="p1793713589392"></a><a name="p1793713589392"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p15937458113912"><a name="p15937458113912"></a><a name="p15937458113912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p293725893919"><a name="p293725893919"></a><a name="p293725893919"></a>Specifies the time when the VPC flow log was updated.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "flow_log": {
            "id": "f49f00f1-0f15-470a-a8c5-4e879e461c8d",
            "name": "flowlog",
            "description": "just a test",
            "tenant_id": "b2782e6708b8475c993e6064bc456bf8",
            "resource_type": "port",
            "resource_id": "05c4052d-8d14-488f-aa00-19fea5a25fde",
            "traffic_type": "reject",
            "log_group_id": "05c4052d-8d14-488f-aa00-19fea5a25fdd",
            "log_topic_id": "a9d7dee7-37d2-4cba-a208-a016252aaa63",
            "created_at": "2019-01-14T11:03:02",
            "updated_at": "2019-01-14T11:03:02"
            "admin_state": true,
            "status": "ACTIVE"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

