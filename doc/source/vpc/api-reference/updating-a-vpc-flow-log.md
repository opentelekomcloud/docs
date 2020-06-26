# Updating a VPC Flow Log<a name="vpc_flow_0004"></a>

## Function<a name="section16780111824019"></a>

This API is used to update a VPC flow log.

## URI<a name="section137800183409"></a>

PUT /v1/\{project\_id\}/fl/flow\_logs/\{flowlog\_id\}

[Table 1](#table12780121844016)  describes the parameters.

**Table  1**  Parameter description

<a name="table12780121844016"></a>
<table><thead align="left"><tr id="row78286197403"><th class="cellrowborder" valign="top" width="11.341134113411341%" id="mcps1.2.5.1.1"><p id="p11828219134015"><a name="p11828219134015"></a><a name="p11828219134015"></a><strong id="b1070313552557"><a name="b1070313552557"></a><a name="b1070313552557"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.491649164916492%" id="mcps1.2.5.1.2"><p id="p4828141913406"><a name="p4828141913406"></a><a name="p4828141913406"></a><strong id="b14452155611550"><a name="b14452155611550"></a><a name="b14452155611550"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.08360836083608%" id="mcps1.2.5.1.3"><p id="p582821914404"><a name="p582821914404"></a><a name="p582821914404"></a><strong id="b736475795514"><a name="b736475795514"></a><a name="b736475795514"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.08360836083608%" id="mcps1.2.5.1.4"><p id="p2828201984018"><a name="p2828201984018"></a><a name="p2828201984018"></a><strong id="b151484586552"><a name="b151484586552"></a><a name="b151484586552"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1382891994017"><td class="cellrowborder" valign="top" width="11.341134113411341%" headers="mcps1.2.5.1.1 "><p id="p148282198404"><a name="p148282198404"></a><a name="p148282198404"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.491649164916492%" headers="mcps1.2.5.1.2 "><p id="p17828219104017"><a name="p17828219104017"></a><a name="p17828219104017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.08360836083608%" headers="mcps1.2.5.1.3 "><p id="p118281719104013"><a name="p118281719104013"></a><a name="p118281719104013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.08360836083608%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row5828619154015"><td class="cellrowborder" valign="top" width="11.341134113411341%" headers="mcps1.2.5.1.1 "><p id="p5828819184010"><a name="p5828819184010"></a><a name="p5828819184010"></a>flowlog_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.491649164916492%" headers="mcps1.2.5.1.2 "><p id="p6828219104014"><a name="p6828219104014"></a><a name="p6828219104014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.08360836083608%" headers="mcps1.2.5.1.3 "><p id="p682841915404"><a name="p682841915404"></a><a name="p682841915404"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.08360836083608%" headers="mcps1.2.5.1.4 "><p id="p7828131904011"><a name="p7828131904011"></a><a name="p7828131904011"></a>Specifies the VPC flow log ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2796518114016"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table16811318174019"></a>
    <table><thead align="left"><tr id="row6828819154020"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p14828191944011"><a name="p14828191944011"></a><a name="p14828191944011"></a><strong id="b154110223565"><a name="b154110223565"></a><a name="b154110223565"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p282861917407"><a name="p282861917407"></a><a name="p282861917407"></a><strong id="b1828742315616_1"><a name="b1828742315616_1"></a><a name="b1828742315616_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p11828519204010"><a name="p11828519204010"></a><a name="p11828519204010"></a><strong id="b28091025175615"><a name="b28091025175615"></a><a name="b28091025175615"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1282813194407"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p16828181912405"><a name="p16828181912405"></a><a name="p16828181912405"></a>flow_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p12828919144018"><a name="p12828919144018"></a><a name="p12828919144018"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p382861918408"><a name="p382861918408"></a><a name="p382861918408"></a>Specifies the <strong id="b18370659132814"><a name="b18370659132814"></a><a name="b18370659132814"></a>FlowLog</strong> objects. For details, see <a href="#table13828101864013">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **FlowLog**  field

    <a name="table13828101864013"></a>
    <table><thead align="left"><tr id="row108280194407"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="p1482881944012"><a name="p1482881944012"></a><a name="p1482881944012"></a><strong id="b14180114215561"><a name="b14180114215561"></a><a name="b14180114215561"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p1282815194401"><a name="p1282815194401"></a><a name="p1282815194401"></a><strong id="b1979922018591"><a name="b1979922018591"></a><a name="b1979922018591"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p128281219104013"><a name="p128281219104013"></a><a name="p128281219104013"></a><strong id="b1773482145910"><a name="b1773482145910"></a><a name="b1773482145910"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p108281919174014"><a name="p108281919174014"></a><a name="p108281919174014"></a><strong id="b758822265915"><a name="b758822265915"></a><a name="b758822265915"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row198285199408"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p5828131912409"><a name="p5828131912409"></a><a name="p5828131912409"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p138281119154015"><a name="p138281119154015"></a><a name="p138281119154015"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p08282019114019"><a name="p08282019114019"></a><a name="p08282019114019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><a name="ul29861294319"></a><a name="ul29861294319"></a><ul id="ul29861294319"><li>Specifies the VPC flow log name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row98282194409"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p10828119204019"><a name="p10828119204019"></a><a name="p10828119204019"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p19828131994019"><a name="p19828131994019"></a><a name="p19828131994019"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15828181924013"><a name="p15828181924013"></a><a name="p15828181924013"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><a name="ul74054431539"></a><a name="ul74054431539"></a><ul id="ul74054431539"><li>Provides supplementary information about the VPC flow log.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row12374417171619"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p1960820250163"><a name="p1960820250163"></a><a name="p1960820250163"></a>admin_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4608525131617"><a name="p4608525131617"></a><a name="p4608525131617"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p13608122581620"><a name="p13608122581620"></a><a name="p13608122581620"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p06081825141614"><a name="p06081825141614"></a><a name="p06081825141614"></a>Specifies whether to enable the VPC flow log function.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{Endpoint}/v1/b2782e6708b8475c993e6064bc456bf8/fl/flow_logs/f49f00f1-0f15-470a-a8c5-4e879e461c8d
    
    {
        "flow_log": {
            "name": "flow-log-update",
            "description": "update",
            "admin_state": false
        }
    }
    ```


## Response Message<a name="section4858131834011"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table687451844017"></a>
    <table><thead align="left"><tr id="row1982871904015"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p118281019184012"><a name="p118281019184012"></a><a name="p118281019184012"></a><strong id="b19591146145919"><a name="b19591146145919"></a><a name="b19591146145919"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p1782841917404"><a name="p1782841917404"></a><a name="p1782841917404"></a><strong id="b126148165919"><a name="b126148165919"></a><a name="b126148165919"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p208281419194014"><a name="p208281419194014"></a><a name="p208281419194014"></a><strong id="b787584817592"><a name="b787584817592"></a><a name="b787584817592"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row198281219134011"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p1482810192406"><a name="p1482810192406"></a><a name="p1482810192406"></a>flow_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p182821915404"><a name="p182821915404"></a><a name="p182821915404"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p3828141914015"><a name="p3828141914015"></a><a name="p3828141914015"></a>Specifies the <strong id="b12172121732911"><a name="b12172121732911"></a><a name="b12172121732911"></a>FlowLog</strong> objects. For details, see <a href="#table17299234185110">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **FlowLog**  field

    <a name="table17299234185110"></a>
    <table><thead align="left"><tr id="en-us_topic_0151499961_row1993725815391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0151499961_p293714582397"><a name="en-us_topic_0151499961_p293714582397"></a><a name="en-us_topic_0151499961_p293714582397"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0151499961_p149371458113917"><a name="en-us_topic_0151499961_p149371458113917"></a><a name="en-us_topic_0151499961_p149371458113917"></a><strong id="b1828742315616_3"><a name="b1828742315616_3"></a><a name="b1828742315616_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="en-us_topic_0151499961_p159376583395"><a name="en-us_topic_0151499961_p159376583395"></a><a name="en-us_topic_0151499961_p159376583395"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0151499961_row29378583393"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p1937205819397"><a name="en-us_topic_0151499961_p1937205819397"></a><a name="en-us_topic_0151499961_p1937205819397"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p5937105873915"><a name="en-us_topic_0151499961_p5937105873915"></a><a name="en-us_topic_0151499961_p5937105873915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p29371758183911"><a name="en-us_topic_0151499961_p29371758183911"></a><a name="en-us_topic_0151499961_p29371758183911"></a>Specifies the VPC flow log UUID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row1293725816394"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p20937145883911"><a name="en-us_topic_0151499961_p20937145883911"></a><a name="en-us_topic_0151499961_p20937145883911"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p10937105813391"><a name="en-us_topic_0151499961_p10937105813391"></a><a name="en-us_topic_0151499961_p10937105813391"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p3618473146"><a name="en-us_topic_0151499961_p3618473146"></a><a name="en-us_topic_0151499961_p3618473146"></a>Specifies the VPC flow log name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row6937758193914"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p1793711586397"><a name="en-us_topic_0151499961_p1793711586397"></a><a name="en-us_topic_0151499961_p1793711586397"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p15937135818397"><a name="en-us_topic_0151499961_p15937135818397"></a><a name="en-us_topic_0151499961_p15937135818397"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p165613352211"><a name="p165613352211"></a><a name="p165613352211"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row8937258173912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p593705817390"><a name="en-us_topic_0151499961_p593705817390"></a><a name="en-us_topic_0151499961_p593705817390"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p093712588392"><a name="en-us_topic_0151499961_p093712588392"></a><a name="en-us_topic_0151499961_p093712588392"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p26023187145"><a name="en-us_topic_0151499961_p26023187145"></a><a name="en-us_topic_0151499961_p26023187145"></a>Provides supplementary information about the VPC flow log.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row7937205883910"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p1393795823920"><a name="en-us_topic_0151499961_p1393795823920"></a><a name="en-us_topic_0151499961_p1393795823920"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p10937858133920"><a name="en-us_topic_0151499961_p10937858133920"></a><a name="en-us_topic_0151499961_p10937858133920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p1293717582396"><a name="en-us_topic_0151499961_p1293717582396"></a><a name="en-us_topic_0151499961_p1293717582396"></a>Specifies the type of resource on which to create the VPC flow log.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row189371758133919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p693745853910"><a name="en-us_topic_0151499961_p693745853910"></a><a name="en-us_topic_0151499961_p693745853910"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p1893725843915"><a name="en-us_topic_0151499961_p1893725843915"></a><a name="en-us_topic_0151499961_p1893725843915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p893718589392"><a name="en-us_topic_0151499961_p893718589392"></a><a name="en-us_topic_0151499961_p893718589392"></a>Specifies the unique resource ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row19371458163912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p11937135813399"><a name="en-us_topic_0151499961_p11937135813399"></a><a name="en-us_topic_0151499961_p11937135813399"></a>traffic_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p159371058143918"><a name="en-us_topic_0151499961_p159371058143918"></a><a name="en-us_topic_0151499961_p159371058143918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p49371958143918"><a name="en-us_topic_0151499961_p49371958143918"></a><a name="en-us_topic_0151499961_p49371958143918"></a>Specifies the type of traffic to log.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row1993795813391"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p11937258153912"><a name="en-us_topic_0151499961_p11937258153912"></a><a name="en-us_topic_0151499961_p11937258153912"></a>log_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p1593716589399"><a name="en-us_topic_0151499961_p1593716589399"></a><a name="en-us_topic_0151499961_p1593716589399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p13937458163911"><a name="en-us_topic_0151499961_p13937458163911"></a><a name="en-us_topic_0151499961_p13937458163911"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row69371358193919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p9937105811399"><a name="en-us_topic_0151499961_p9937105811399"></a><a name="en-us_topic_0151499961_p9937105811399"></a>log_topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p3937195853911"><a name="en-us_topic_0151499961_p3937195853911"></a><a name="en-us_topic_0151499961_p3937195853911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p8937105811390"><a name="en-us_topic_0151499961_p8937105811390"></a><a name="en-us_topic_0151499961_p8937105811390"></a>Specifies the log topic ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row149526285714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p1948613611718"><a name="en-us_topic_0151499961_p1948613611718"></a><a name="en-us_topic_0151499961_p1948613611718"></a>admin_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p11486936674"><a name="en-us_topic_0151499961_p11486936674"></a><a name="en-us_topic_0151499961_p11486936674"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p184867361474"><a name="en-us_topic_0151499961_p184867361474"></a><a name="en-us_topic_0151499961_p184867361474"></a>Specifies whether to enable the VPC flow log function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row102334258716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p74861036479"><a name="en-us_topic_0151499961_p74861036479"></a><a name="en-us_topic_0151499961_p74861036479"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p1948613361478"><a name="en-us_topic_0151499961_p1948613361478"></a><a name="en-us_topic_0151499961_p1948613361478"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p1092449185"><a name="en-us_topic_0151499961_p1092449185"></a><a name="en-us_topic_0151499961_p1092449185"></a>Specifies the VPC flow log status.</p>
    <a name="en-us_topic_0151499961_ul12491821389"></a><a name="en-us_topic_0151499961_ul12491821389"></a><ul id="en-us_topic_0151499961_ul12491821389"><li><strong id="b842352706192644"><a name="b842352706192644"></a><a name="b842352706192644"></a>ACTIVE</strong>: Enabled</li><li><strong id="b84235270619274"><a name="b84235270619274"></a><a name="b84235270619274"></a>DOWN</strong>: Disabled</li><li><strong id="b842352706192830"><a name="b842352706192830"></a><a name="b842352706192830"></a>ERROR</strong>: Abnormal fault</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row593715813910"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p6937125803920"><a name="en-us_topic_0151499961_p6937125803920"></a><a name="en-us_topic_0151499961_p6937125803920"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p6937105823914"><a name="en-us_topic_0151499961_p6937105823914"></a><a name="en-us_topic_0151499961_p6937105823914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p1193719586393"><a name="en-us_topic_0151499961_p1193719586393"></a><a name="en-us_topic_0151499961_p1193719586393"></a>Specifies the time when the VPC flow log was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0151499961_row0937358193913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0151499961_p1793713589392"><a name="en-us_topic_0151499961_p1793713589392"></a><a name="en-us_topic_0151499961_p1793713589392"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0151499961_p15937458113912"><a name="en-us_topic_0151499961_p15937458113912"></a><a name="en-us_topic_0151499961_p15937458113912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151499961_p293725893919"><a name="en-us_topic_0151499961_p293725893919"></a><a name="en-us_topic_0151499961_p293725893919"></a>Specifies the time when the VPC flow log was updated.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "flow_log": {
            "id": "f49f00f1-0f15-470a-a8c5-4e879e461c8d",
            "name": " flow-log-update",
            "description": "update",
            "tenant_id": "b2782e6708b8475c993e6064bc456bf8",
            "resource_type": "port",
            "resource_id": "05c4052d-8d14-488f-aa00-19fea5a25fde",
            "traffic_type": "reject",
            "log_group_id": "05c4052d-8d14-488f-aa00-19fea5a25fdd",
            "log_topic_id": "a9d7dee7-37d2-4cba-a208-a016252aaa63",
            "created_at": "2019-01-14T11:03:02",
            "updated_at": "2019-01-14T12:03:02"
            "status": "DOWN",
            "admin_state": false
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

