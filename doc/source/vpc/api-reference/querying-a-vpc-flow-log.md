# Querying a VPC Flow Log<a name="vpc_flow_0003"></a>

## Function<a name="section16284153465111"></a>

This API is used to query a VPC flow log.

## URI<a name="section1828473425111"></a>

GET /v1/\{project\_id\}/fl/flow\_logs/\{flowlog\_id\}

[Table 1](#table152848346516)  describes the parameters.

**Table  1**  Parameter description

<a name="table152848346516"></a>
<table><thead align="left"><tr id="row540910347514"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p140923405110"><a name="p140923405110"></a><a name="p140923405110"></a><strong id="b8828713185411"><a name="b8828713185411"></a><a name="b8828713185411"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p24091234175119"><a name="p24091234175119"></a><a name="p24091234175119"></a><strong id="b96034145547"><a name="b96034145547"></a><a name="b96034145547"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p94091034205117"><a name="p94091034205117"></a><a name="p94091034205117"></a><strong id="b3510181513543"><a name="b3510181513543"></a><a name="b3510181513543"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p144091344518"><a name="p144091344518"></a><a name="p144091344518"></a><strong id="b02181616195415"><a name="b02181616195415"></a><a name="b02181616195415"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15409143495116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p840923411517"><a name="p840923411517"></a><a name="p840923411517"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p194091934115116"><a name="p194091934115116"></a><a name="p194091934115116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p16409203465120"><a name="p16409203465120"></a><a name="p16409203465120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row17409234195116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p84091634135115"><a name="p84091634135115"></a><a name="p84091634135115"></a>flowlog_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p3409123455117"><a name="p3409123455117"></a><a name="p3409123455117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p3409123418514"><a name="p3409123418514"></a><a name="p3409123418514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p640920345511"><a name="p640920345511"></a><a name="p640920345511"></a>Specifies the VPC flow log ID, which uniquely identifies the VPC flow log.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2284934175115"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/b2782e6708b8475c993e6064bc456bf8/fl/flow_logs/1e10cd9d-742a-4d36-a9fd-aee9784336ff
    ```


## Response Message<a name="section1629919342519"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table9299113405110"></a>
    <table><thead align="left"><tr id="row11409334115117"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p14409103419511"><a name="p14409103419511"></a><a name="p14409103419511"></a><strong id="b1488141212551"><a name="b1488141212551"></a><a name="b1488141212551"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p34093341512"><a name="p34093341512"></a><a name="p34093341512"></a><strong id="b12466413195518"><a name="b12466413195518"></a><a name="b12466413195518"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p240915343512"><a name="p240915343512"></a><a name="p240915343512"></a><strong id="b1333431495510"><a name="b1333431495510"></a><a name="b1333431495510"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row940963413519"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p84095341513"><a name="p84095341513"></a><a name="p84095341513"></a>flow_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p540943475116"><a name="p540943475116"></a><a name="p540943475116"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p34092034125118"><a name="p34092034125118"></a><a name="p34092034125118"></a>Specifies the <strong id="b38591633228"><a name="b38591633228"></a><a name="b38591633228"></a>FlowLog</strong> objects. For details, see <a href="#table17299234185110">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **FlowLog**  field

    <a name="table17299234185110"></a>
    <table><thead align="left"><tr id="en-us_topic_0151499961_row1993725815391"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0151499961_p293714582397"><a name="en-us_topic_0151499961_p293714582397"></a><a name="en-us_topic_0151499961_p293714582397"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0151499961_p149371458113917"><a name="en-us_topic_0151499961_p149371458113917"></a><a name="en-us_topic_0151499961_p149371458113917"></a><strong id="b1679443485"><a name="b1679443485"></a><a name="b1679443485"></a>Type</strong></p>
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
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p117815752110"><a name="p117815752110"></a><a name="p117815752110"></a>Specifies the project ID.</p>
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
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

