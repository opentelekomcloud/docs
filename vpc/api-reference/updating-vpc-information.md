# Updating VPC Information<a name="vpc_api01_0004"></a>

## Function<a name="section8079634"></a>

This API is used to update information about a VPC.

## URI<a name="section5607849"></a>

PUT /v1/\{project\_id\}/vpcs/\{vpc\_id\}

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section50470647"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table4060745715545"></a>
    <table><thead align="left"><tr id="row1619435515545"><th class="cellrowborder" valign="top" width="11.459999999999999%" id="mcps1.2.5.1.1"><p id="p3667439915545"><a name="p3667439915545"></a><a name="p3667439915545"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.93%" id="mcps1.2.5.1.2"><p id="p1783637615545"><a name="p1783637615545"></a><a name="p1783637615545"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.93%" id="mcps1.2.5.1.3"><p id="p3546035715545"><a name="p3546035715545"></a><a name="p3546035715545"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.68%" id="mcps1.2.5.1.4"><p id="p5371668715545"><a name="p5371668715545"></a><a name="p5371668715545"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5608438115545"><td class="cellrowborder" valign="top" width="11.459999999999999%" headers="mcps1.2.5.1.1 "><p id="p4654101615545"><a name="p4654101615545"></a><a name="p4654101615545"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.2.5.1.2 "><p id="p1172592715545"><a name="p1172592715545"></a><a name="p1172592715545"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.3 "><p id="p1027601915545"><a name="p1027601915545"></a><a name="p1027601915545"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.68%" headers="mcps1.2.5.1.4 "><p id="p4213394815545"><a name="p4213394815545"></a><a name="p4213394815545"></a><a href="#table34290771">Specifies the VPC objects.</a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  VPC objects

    <a name="table34290771"></a>
    <table><thead align="left"><tr id="row42952388"><th class="cellrowborder" valign="top" width="14.66%" id="mcps1.2.5.1.1"><p id="p56591389"><a name="p56591389"></a><a name="p56591389"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.2"><p id="p20499795"><a name="p20499795"></a><a name="p20499795"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.849999999999998%" id="mcps1.2.5.1.3"><p id="p17479484174639"><a name="p17479484174639"></a><a name="p17479484174639"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.33%" id="mcps1.2.5.1.4"><p id="p49870669"><a name="p49870669"></a><a name="p49870669"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12992371"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p45749167"><a name="p45749167"></a><a name="p45749167"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.2 "><p id="p14695014"><a name="p14695014"></a><a name="p14695014"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.3 "><p id="p6552131174639"><a name="p6552131174639"></a><a name="p6552131174639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.2.5.1.4 "><a name="ul0576257538"></a><a name="ul0576257538"></a><ul id="ul0576257538"><li>Specifies the VPC name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>Each VPC name of a tenant must be unique if the VPC name is not left blank.</li></ul>
    </td>
    </tr>
    <tr id="row12304154151511"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p211618568154"><a name="p211618568154"></a><a name="p211618568154"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.2 "><p id="p1211635651520"><a name="p1211635651520"></a><a name="p1211635651520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.3 "><p id="p18116165611152"><a name="p18116165611152"></a><a name="p18116165611152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.2.5.1.4 "><a name="ul5116195661518"></a><a name="ul5116195661518"></a><ul id="ul5116195661518"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row7722248"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p21522370"><a name="p21522370"></a><a name="p21522370"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.2 "><p id="p65590400"><a name="p65590400"></a><a name="p65590400"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.3 "><p id="p60960565174639"><a name="p60960565174639"></a><a name="p60960565174639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.2.5.1.4 "><a name="ul161253336536"></a><a name="ul161253336536"></a><ul id="ul161253336536"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul53161626155413"></a><a name="ul53161626155413"></a><ul id="ul53161626155413"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b3560145617710"><a name="b3560145617710"></a><a name="b3560145617710"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b082517582076"><a name="b082517582076"></a><a name="b082517582076"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row14946201923916"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p41373254402"><a name="p41373254402"></a><a name="p41373254402"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.2 "><p id="p2036962673916"><a name="p2036962673916"></a><a name="p2036962673916"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.3 "><p id="p18137202516409"><a name="p18137202516409"></a><a name="p18137202516409"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.2.5.1.4 "><p id="p51371325174011"><a name="p51371325174011"></a><a name="p51371325174011"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong> indicates that the function is enabled, and the value <strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{Endpoint}/v1/{project_id}/vpcs/99d9d709-8478-4b46-9f3f-2206b1023fd3
    
    {
        "vpc": {
            "name": "vpc1",
            "description": "test1",
            "cidr": "192.168.0.0/16",
            "enable_shared_snat": true
        }
    }
    ```


## Response Message<a name="section51582645"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table163236181565"></a>
    <table><thead align="left"><tr id="row361709001565"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p441618021565"><a name="p441618021565"></a><a name="p441618021565"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.2.4.1.2"><p id="p366208391565"><a name="p366208391565"></a><a name="p366208391565"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.93%" id="mcps1.2.4.1.3"><p id="p134980151565"><a name="p134980151565"></a><a name="p134980151565"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row195974151565"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p438867591565"><a name="p438867591565"></a><a name="p438867591565"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.4.1.2 "><p id="p440032491565"><a name="p440032491565"></a><a name="p440032491565"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.93%" headers="mcps1.2.4.1.3 "><p id="p3322021565"><a name="p3322021565"></a><a name="p3322021565"></a><a href="#table22527411">Specifies the VPC objects.</a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  VPC objects

    <a name="table22527411"></a>
    <table><thead align="left"><tr id="row37318421"><th class="cellrowborder" valign="top" width="17.59175917591759%" id="mcps1.2.4.1.1"><p id="p2893298"><a name="p2893298"></a><a name="p2893298"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.822182218221823%" id="mcps1.2.4.1.2"><p id="p32078086174724"><a name="p32078086174724"></a><a name="p32078086174724"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.58605860586058%" id="mcps1.2.4.1.3"><p id="p58230900"><a name="p58230900"></a><a name="p58230900"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19082474"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p2176568"><a name="p2176568"></a><a name="p2176568"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p48188187174724"><a name="p48188187174724"></a><a name="p48188187174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><p id="p53389951"><a name="p53389951"></a><a name="p53389951"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row10747513"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p65242240"><a name="p65242240"></a><a name="p65242240"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p10929060174724"><a name="p10929060174724"></a><a name="p10929060174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><p id="p47359816174719"><a name="p47359816174719"></a><a name="p47359816174719"></a>Specifies the VPC name.</p>
    </td>
    </tr>
    <tr id="row15698184911617"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p174335514162"><a name="p174335514162"></a><a name="p174335514162"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p743345115166"><a name="p743345115166"></a><a name="p743345115166"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><a name="ul6433175110169"></a><a name="ul6433175110169"></a><ul id="ul6433175110169"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row37632913"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p28367147"><a name="p28367147"></a><a name="p28367147"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p12838666174724"><a name="p12838666174724"></a><a name="p12838666174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><a name="ul10389173917465"></a><a name="ul10389173917465"></a><ul id="ul10389173917465"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul9987194121820"></a><a name="ul9987194121820"></a><ul id="ul9987194121820"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b32921160817"><a name="b32921160817"></a><a name="b32921160817"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b13607171818814"><a name="b13607171818814"></a><a name="b13607171818814"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row14466778"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p30958352"><a name="p30958352"></a><a name="p30958352"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p33298996174724"><a name="p33298996174724"></a><a name="p33298996174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><a name="ul74552213513"></a><a name="ul74552213513"></a><ul id="ul74552213513"><li>Specifies the VPC status.</li><li>Possible values are as follows:<a name="ul5890854165417"></a><a name="ul5890854165417"></a><ul id="ul5890854165417"><li><strong id="b3219648483"><a name="b3219648483"></a><a name="b3219648483"></a>CREATING</strong>: The VPC is being created.</li><li><strong id="b32161149686"><a name="b32161149686"></a><a name="b32161149686"></a>OK</strong>: The VPC is created successfully.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row6192167813568"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p4960003413568"><a name="p4960003413568"></a><a name="p4960003413568"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p1494185813568"><a name="p1494185813568"></a><a name="p1494185813568"></a>Array of <a href="#table3576833291556">route</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><a name="ul1021319485513"></a><a name="ul1021319485513"></a><ul id="ul1021319485513"><li>Specifies the route information.</li><li>For details, see the description of the <a href="#table3576833291556">route objects</a>.</li></ul>
    </td>
    </tr>
    <tr id="row197011819164016"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.2.4.1.1 "><p id="p2819122014403"><a name="p2819122014403"></a><a name="p2819122014403"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.2.4.1.2 "><p id="p19821620144010"><a name="p19821620144010"></a><a name="p19821620144010"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.2.4.1.3 "><p id="p2082432034020"><a name="p2082432034020"></a><a name="p2082432034020"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b1328911050"><a name="b1328911050"></a><a name="b1328911050"></a>true</strong> indicates that the function is enabled, and the value <strong id="b1061928441"><a name="b1061928441"></a><a name="b1061928441"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **route**  objects

    <a name="table3576833291556"></a>
    <table><thead align="left"><tr id="row921218691556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p798956991556"><a name="p798956991556"></a><a name="p798956991556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.38%" id="mcps1.2.4.1.2"><p id="p754435891556"><a name="p754435891556"></a><a name="p754435891556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.28%" id="mcps1.2.4.1.3"><p id="p711326791556"><a name="p711326791556"></a><a name="p711326791556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3930377391556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p2948903591556"><a name="p2948903591556"></a><a name="p2948903591556"></a>destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p270722191556"><a name="p270722191556"></a><a name="p270722191556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul18181132710558"></a><a name="ul18181132710558"></a><ul id="ul18181132710558"><li>Specifies the destination network segment of a route.</li><li>The value must be in the CIDR format. Currently, only the value <strong>0.0.0.0/0</strong> is supported.</li></ul>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul17731193025515"></a><a name="ul17731193025515"></a><ul id="ul17731193025515"><li>Specifies the next hop of a route.</li><li>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "vpc": {
            "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
            "name": "vpc1",
            "description": "test1",
            "cidr": "192.168.0.0/16",
            "status": "OK",
            
            "routes": [],
            "enable_shared_snat": true
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

