# Querying VPC Flow Logs<a name="vpc_flow_0002"></a>

## Function<a name="section638721504117"></a>

This API is used to query all VPC flow logs of the tenant submitting the request. The VPC flow logs are filtered based on the filtering condition.

## URI<a name="section1838713156413"></a>

GET /v1/\{project\_id\}/fl/flow\_logs

Example:

```
GET https://{Endpoint}/v1/b2782e6708b8475c993e6064bc456bf8/fl/flow_logs?name=flowlog
```

[Table 1](#table238711153416)  describes the parameters.

**Table  1**  Parameter description

<a name="table238711153416"></a>
<table><thead align="left"><tr id="row14669101554118"><th class="cellrowborder" valign="top" width="32.993299329932995%" id="mcps1.2.5.1.1"><p id="p166911154415"><a name="p166911154415"></a><a name="p166911154415"></a><strong id="b1912452434917"><a name="b1912452434917"></a><a name="b1912452434917"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.431443144314432%" id="mcps1.2.5.1.2"><p id="p18669101519419"><a name="p18669101519419"></a><a name="p18669101519419"></a><strong id="b28922248495"><a name="b28922248495"></a><a name="b28922248495"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.46154615461546%" id="mcps1.2.5.1.3"><p id="p26694151414"><a name="p26694151414"></a><a name="p26694151414"></a><strong id="b516511278495"><a name="b516511278495"></a><a name="b516511278495"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.11371137113711%" id="mcps1.2.5.1.4"><p id="p176841515164110"><a name="p176841515164110"></a><a name="p176841515164110"></a><strong id="b155321728194918"><a name="b155321728194918"></a><a name="b155321728194918"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4684415134110"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1168471519417"><a name="p1168471519417"></a><a name="p1168471519417"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p15684715104120"><a name="p15684715104120"></a><a name="p15684715104120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p17684121514416"><a name="p17684121514416"></a><a name="p17684121514416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row20684415194112"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p15684815104119"><a name="p15684815104119"></a><a name="p15684815104119"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p176846156418"><a name="p176846156418"></a><a name="p176846156418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p196847155410"><a name="p196847155410"></a><a name="p196847155410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p6684715154116"><a name="p6684715154116"></a><a name="p6684715154116"></a>Specifies the VPC flow log UUID.</p>
</td>
</tr>
<tr id="row468461544117"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p8684121518411"><a name="p8684121518411"></a><a name="p8684121518411"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p868411153419"><a name="p868411153419"></a><a name="p868411153419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p268441514413"><a name="p268441514413"></a><a name="p268441514413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><a name="ul16841015174115"></a><a name="ul16841015174115"></a><ul id="ul16841015174115"><li>Specifies the VPC flow log name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
</td>
</tr>
<tr id="row1368431515411"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1668491518416"><a name="p1668491518416"></a><a name="p1668491518416"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p18684161519419"><a name="p18684161519419"></a><a name="p18684161519419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p1968419159414"><a name="p1968419159414"></a><a name="p1968419159414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p1468471534118"><a name="p1468471534118"></a><a name="p1468471534118"></a>Specifies the type of resource on which to create the VPC flow log.</p>
</td>
</tr>
<tr id="row11684121574118"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p968411564111"><a name="p968411564111"></a><a name="p968411564111"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p66847153416"><a name="p66847153416"></a><a name="p66847153416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p1368431518417"><a name="p1368431518417"></a><a name="p1368431518417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p268471594117"><a name="p268471594117"></a><a name="p268471594117"></a>Specifies the unique resource ID.</p>
</td>
</tr>
<tr id="row1568431515411"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p146841715144111"><a name="p146841715144111"></a><a name="p146841715144111"></a>traffic_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p8684111518413"><a name="p8684111518413"></a><a name="p8684111518413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p15684171513416"><a name="p15684171513416"></a><a name="p15684171513416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p96846151412"><a name="p96846151412"></a><a name="p96846151412"></a>Specifies the type of traffic to log.</p>
</td>
</tr>
<tr id="row368416157412"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1968451514411"><a name="p1968451514411"></a><a name="p1968451514411"></a>log_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p7684015114118"><a name="p7684015114118"></a><a name="p7684015114118"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p4684115144113"><a name="p4684115144113"></a><a name="p4684115144113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p6684715144111"><a name="p6684715144111"></a><a name="p6684715144111"></a>Specifies the log group ID.</p>
</td>
</tr>
<tr id="row166842015104110"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p19684171534116"><a name="p19684171534116"></a><a name="p19684171534116"></a>log_topic_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p1684191516418"><a name="p1684191516418"></a><a name="p1684191516418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p1568411564116"><a name="p1568411564116"></a><a name="p1568411564116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p186841152412"><a name="p186841152412"></a><a name="p186841152412"></a>Specifies the log topic ID.</p>
</td>
</tr>
<tr id="row121318184513"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1613216181558"><a name="p1613216181558"></a><a name="p1613216181558"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p43114521558"><a name="p43114521558"></a><a name="p43114521558"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p10311125217516"><a name="p10311125217516"></a><a name="p10311125217516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p12311152556"><a name="p12311152556"></a><a name="p12311152556"></a>Specifies the VPC flow log status.</p>
<a name="ul12491821389"></a><a name="ul12491821389"></a><ul id="ul12491821389"><li><strong id="b842352706192644"><a name="b842352706192644"></a><a name="b842352706192644"></a>ACTIVE</strong>: Enabled</li><li><strong id="b84235270619274"><a name="b84235270619274"></a><a name="b84235270619274"></a>DOWN</strong>: Disabled</li><li><strong id="b842352706192830"><a name="b842352706192830"></a><a name="b842352706192830"></a>ERROR</strong>: Abnormal fault</li></ul>
</td>
</tr>
<tr id="row9684201574115"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1768418154410"><a name="p1768418154410"></a><a name="p1768418154410"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p16684715144119"><a name="p16684715144119"></a><a name="p16684715144119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p116841415164112"><a name="p116841415164112"></a><a name="p116841415164112"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><a name="ul186842015164114"></a><a name="ul186842015164114"></a><ul id="ul186842015164114"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li></ul>
</td>
</tr>
<tr id="row3684171513419"><td class="cellrowborder" valign="top" width="32.993299329932995%" headers="mcps1.2.5.1.1 "><p id="p1684161564111"><a name="p1684161564111"></a><a name="p1684161564111"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.431443144314432%" headers="mcps1.2.5.1.2 "><p id="p26841315104116"><a name="p26841315104116"></a><a name="p26841315104116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.3 "><p id="p1968481564115"><a name="p1968481564115"></a><a name="p1968481564115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.2.5.1.4 "><p id="p10684171554120"><a name="p10684171554120"></a><a name="p10684171554120"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section15450181516413"></a>

-   Request parameter

    None


-   Example request

    None


## Response Message<a name="section18465111518417"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table1346521554119"></a>
    <table><thead align="left"><tr id="row4684115164112"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p136841215114112"><a name="p136841215114112"></a><a name="p136841215114112"></a><strong id="b167561740165013"><a name="b167561740165013"></a><a name="b167561740165013"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p11684181510415"><a name="p11684181510415"></a><a name="p11684181510415"></a><strong id="b145886415502"><a name="b145886415502"></a><a name="b145886415502"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p16847153414"><a name="p16847153414"></a><a name="p16847153414"></a><strong id="b941164245018"><a name="b941164245018"></a><a name="b941164245018"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9684215134119"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p3684121513412"><a name="p3684121513412"></a><a name="p3684121513412"></a>flow_logs</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p13684101534119"><a name="p13684101534119"></a><a name="p13684101534119"></a>Array of <a href="#table34811015184118">FlowLog</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p668481574120"><a name="p668481574120"></a><a name="p668481574120"></a>Specifies the <strong id="b1287253319279"><a name="b1287253319279"></a><a name="b1287253319279"></a>FlowLog</strong> object list. For details, see <a href="#table34811015184118">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **FlowLog**  field

    <a name="table34811015184118"></a>
    <table><thead align="left"><tr id="en-us_topic_0151499961_row1993725815391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0151499961_p293714582397"><a name="en-us_topic_0151499961_p293714582397"></a><a name="en-us_topic_0151499961_p293714582397"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0151499961_p149371458113917"><a name="en-us_topic_0151499961_p149371458113917"></a><a name="en-us_topic_0151499961_p149371458113917"></a><strong id="b2131245496"><a name="b2131245496"></a><a name="b2131245496"></a>Type</strong></p>
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
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p19640125119213"><a name="p19640125119213"></a><a name="p19640125119213"></a>Specifies the project ID.</p>
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
    <a name="en-us_topic_0151499961_ul12491821389"></a><a name="en-us_topic_0151499961_ul12491821389"></a><ul id="en-us_topic_0151499961_ul12491821389"><li><strong id="b967657751"><a name="b967657751"></a><a name="b967657751"></a>ACTIVE</strong>: Enabled</li><li><strong id="b560397809"><a name="b560397809"></a><a name="b560397809"></a>DOWN</strong>: Disabled</li><li><strong id="b681897732"><a name="b681897732"></a><a name="b681897732"></a>ERROR</strong>: Abnormal fault</li></ul>
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
        "flow_logs": [
            {
                "id": "35868d55-443e-4d5c-90a4-ac618dc45c1a",
                "name": "flow",
                "description": "just a test",
                "tenant_id": "b2782e6708b8475c993e6064bc456bf8",
                "resource_type": "port",
                "resource_id": "05c4052d-8d14-488f-aa00-19fea5a25fde",
                "traffic_type": "reject",
                "log_group_id": "05c4052d-8d14-488f-aa00-19fea5a25fff",
                "log_topic_id": "a9d7dee7-37d2-4cba-a208-a016252aaa63",
                "created_at": "2019-01-14T11:03:02",
                "updated_at": "2019-01-14T11:03:02"
                "status": "ACTIVE",
                "admin_state": true
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

