# Updating VPC Information<a name="EN-US_TOPIC_0020090626"></a>

## Function<a name="section8079634"></a>

This interface is used to update information about a VPC.

## URI<a name="section5607849"></a>

-   PUT /v1/\{tenant\_id\}/vpcs/\{vpc\_id\}
-   Parameter description

    <a name="table27380479"></a><table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p62013962"><a name="p62013962"></a><a name="p62013962"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50470647"></a>

-   Parameter description

    <a name="table4060745715545"></a><table><thead align="left"><tr id="row1619435515545"><th class="cellrowborder" valign="top" width="11.459999999999999%" id="mcps1.1.5.1.1"><p id="p3667439915545"><a name="p3667439915545"></a><a name="p3667439915545"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.93%" id="mcps1.1.5.1.2"><p id="p1783637615545"><a name="p1783637615545"></a><a name="p1783637615545"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.93%" id="mcps1.1.5.1.3"><p id="p3546035715545"><a name="p3546035715545"></a><a name="p3546035715545"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.68%" id="mcps1.1.5.1.4"><p id="p5371668715545"><a name="p5371668715545"></a><a name="p5371668715545"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5608438115545"><td class="cellrowborder" valign="top" width="11.459999999999999%" headers="mcps1.1.5.1.1 "><p id="p4654101615545"><a name="p4654101615545"></a><a name="p4654101615545"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.1.5.1.2 "><p id="p1172592715545"><a name="p1172592715545"></a><a name="p1172592715545"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.1.5.1.3 "><p id="p1027601915545"><a name="p1027601915545"></a><a name="p1027601915545"></a><em id="i2537530715545"><a name="i2537530715545"></a><a name="i2537530715545"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="45.68%" headers="mcps1.1.5.1.4 "><p id="p4213394815545"><a name="p4213394815545"></a><a name="p4213394815545"></a>VPC object, which must contain <strong id="b842352706192811"><a name="b842352706192811"></a><a name="b842352706192811"></a>name</strong>&nbsp;or&nbsp;<strong id="b842352706192817"><a name="b842352706192817"></a><a name="b842352706192817"></a>cidr</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **vpc**  fields

    <a name="table34290771"></a><table><thead align="left"><tr id="row42952388"><th class="cellrowborder" valign="top" width="14.66%" id="mcps1.1.5.1.1"><p id="p56591389"><a name="p56591389"></a><a name="p56591389"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16%" id="mcps1.1.5.1.2"><p id="p20499795"><a name="p20499795"></a><a name="p20499795"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.849999999999998%" id="mcps1.1.5.1.3"><p id="p17479484174639"><a name="p17479484174639"></a><a name="p17479484174639"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.33%" id="mcps1.1.5.1.4"><p id="p49870669"><a name="p49870669"></a><a name="p49870669"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12992371"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.1.5.1.1 "><p id="p45749167"><a name="p45749167"></a><a name="p45749167"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.2 "><p id="p14695014"><a name="p14695014"></a><a name="p14695014"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.1.5.1.3 "><p id="p6552131174639"><a name="p6552131174639"></a><a name="p6552131174639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.1.5.1.4 "><p id="p49445506"><a name="p49445506"></a><a name="p49445506"></a>Specifies the VPC name.</p>
    <p id="p45663083"><a name="p45663083"></a><a name="p45663083"></a>The name must be unique for a tenant.</p>
    <p id="p8314568"><a name="p8314568"></a><a name="p8314568"></a>The value is a string of no more than 64 characters and can contain digits, letters, underscores (_), hyphens (-), and periods (.).</p>
    <p id="p61048968191314"><a name="p61048968191314"></a><a name="p61048968191314"></a>If <strong id="b842352706192947"><a name="b842352706192947"></a><a name="b842352706192947"></a>name</strong>&nbsp;is not specified,&nbsp;<strong id="b842352706192955"><a name="b842352706192955"></a><a name="b842352706192955"></a>cidr</strong> must be specified.</p>
    </td>
    </tr>
    <tr id="row7722248"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.1.5.1.1 "><p id="p21522370"><a name="p21522370"></a><a name="p21522370"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.2 "><p id="p65590400"><a name="p65590400"></a><a name="p65590400"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.1.5.1.3 "><p id="p60960565174639"><a name="p60960565174639"></a><a name="p60960565174639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.1.5.1.4 "><p id="p54772939121428"><a name="p54772939121428"></a><a name="p54772939121428"></a>Specifies the available subnets in the VPC.</p>
    <p id="p66807544121428"><a name="p66807544121428"></a><a name="p66807544121428"></a>The value must be in CIDR format, for example, <strong>192.168.0.0/16</strong>.</p>
    <p id="p64396986121428"><a name="p64396986121428"></a><a name="p64396986121428"></a>The value ranges from <strong>10.0.0.0/8</strong>&nbsp;to&nbsp;<strong>10.255.255.240/28</strong>,&nbsp;<strong>172.16.0.0/12</strong>&nbsp;to&nbsp;<strong>172.31.255.240/28</strong>, or&nbsp;<strong>192.168.0.0/16</strong>&nbsp;to&nbsp;<strong>192.168.255.240/28</strong>.</p>
    <p id="p57917797191340"><a name="p57917797191340"></a><a name="p57917797191340"></a>If <strong id="b842352706192947_1"><a name="b842352706192947_1"></a><a name="b842352706192947_1"></a>cidr</strong>&nbsp;is not specified,&nbsp;<strong id="b842352706192955_1"><a name="b842352706192955_1"></a><a name="b842352706192955_1"></a>name</strong> must be specified.</p>
    </td>
    </tr>
    <tr id="row14946201923916"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.1.5.1.1 "><p id="p41373254402"><a name="p41373254402"></a><a name="p41373254402"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.2 "><p id="p2036962673916"><a name="p2036962673916"></a><a name="p2036962673916"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.1.5.1.3 "><p id="p18137202516409"><a name="p18137202516409"></a><a name="p18137202516409"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.33%" headers="mcps1.1.5.1.4 "><p id="p51371325174011"><a name="p51371325174011"></a><a name="p51371325174011"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong>&nbsp;indicates that the function is enabled, and the value&nbsp;<strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
    "vpc":
        {
        "name": "vpc1",
        "cidr": "192.168.0.0/16"
        "enable_shared_snat": true
        }
    }
    ```


## Response<a name="section51582645"></a>

-   Parameter description

    <a name="table163236181565"></a><table><thead align="left"><tr id="row361709001565"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p441618021565"><a name="p441618021565"></a><a name="p441618021565"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.1.4.1.2"><p id="p366208391565"><a name="p366208391565"></a><a name="p366208391565"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.93%" id="mcps1.1.4.1.3"><p id="p134980151565"><a name="p134980151565"></a><a name="p134980151565"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row195974151565"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p438867591565"><a name="p438867591565"></a><a name="p438867591565"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.4.1.2 "><p id="p440032491565"><a name="p440032491565"></a><a name="p440032491565"></a><em id="i2537530715545_1"><a name="i2537530715545_1"></a><a name="i2537530715545_1"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.93%" headers="mcps1.1.4.1.3 "><p id="p3322021565"><a name="p3322021565"></a><a name="p3322021565"></a>Specifies the VPC objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **vpc**  fields

    <a name="table22527411"></a><table><thead align="left"><tr id="row37318421"><th class="cellrowborder" valign="top" width="17.59175917591759%" id="mcps1.1.4.1.1"><p id="p2893298"><a name="p2893298"></a><a name="p2893298"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.822182218221823%" id="mcps1.1.4.1.2"><p id="p32078086174724"><a name="p32078086174724"></a><a name="p32078086174724"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.58605860586058%" id="mcps1.1.4.1.3"><p id="p58230900"><a name="p58230900"></a><a name="p58230900"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19082474"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p2176568"><a name="p2176568"></a><a name="p2176568"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p48188187174724"><a name="p48188187174724"></a><a name="p48188187174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p53389951"><a name="p53389951"></a><a name="p53389951"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row10747513"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p65242240"><a name="p65242240"></a><a name="p65242240"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p10929060174724"><a name="p10929060174724"></a><a name="p10929060174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p47359816174719"><a name="p47359816174719"></a><a name="p47359816174719"></a>Specifies the VPC name.</p>
    </td>
    </tr>
    <tr id="row37632913"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p28367147"><a name="p28367147"></a><a name="p28367147"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p12838666174724"><a name="p12838666174724"></a><a name="p12838666174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p31350350174719"><a name="p31350350174719"></a><a name="p31350350174719"></a>Specifies the range of available subnets in the VPC.</p>
    </td>
    </tr>
    <tr id="row14466778"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p30958352"><a name="p30958352"></a><a name="p30958352"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p33298996174724"><a name="p33298996174724"></a><a name="p33298996174724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p37391642174719"><a name="p37391642174719"></a><a name="p37391642174719"></a>Specifies the status of the VPC.</p>
    <p id="p12308246174719"><a name="p12308246174719"></a><a name="p12308246174719"></a>The value can be <strong>CREATING</strong>,&nbsp;<strong>OK</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>PENDING_UPDATE</strong>,&nbsp;<strong>PENDING_DELETE</strong>, or&nbsp;<strong>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row6192167813568"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p4960003413568"><a name="p4960003413568"></a><a name="p4960003413568"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p1494185813568"><a name="p1494185813568"></a><a name="p1494185813568"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p26256563192136"><a name="p26256563192136"></a><a name="p26256563192136"></a>Specifies the route information.</p>
    <p id="p42971876202757"><a name="p42971876202757"></a><a name="p42971876202757"></a>For details, see descriptions of <strong>route</strong> fields.</p>
    </td>
    </tr>
    <tr id="row197011819164016"><td class="cellrowborder" valign="top" width="17.59175917591759%" headers="mcps1.1.4.1.1 "><p id="p2819122014403"><a name="p2819122014403"></a><a name="p2819122014403"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.822182218221823%" headers="mcps1.1.4.1.2 "><p id="p19821620144010"><a name="p19821620144010"></a><a name="p19821620144010"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.58605860586058%" headers="mcps1.1.4.1.3 "><p id="p2082432034020"><a name="p2082432034020"></a><a name="p2082432034020"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178_1"><a name="b84235270612178_1"></a><a name="b84235270612178_1"></a>true</strong>&nbsp;indicates that the function is enabled, and the value&nbsp;<strong id="b84235270614243_1"><a name="b84235270614243_1"></a><a name="b84235270614243_1"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **route**  fields

    <a name="table3576833291556"></a><table><thead align="left"><tr id="row921218691556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p798956991556"><a name="p798956991556"></a><a name="p798956991556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.38%" id="mcps1.1.4.1.2"><p id="p754435891556"><a name="p754435891556"></a><a name="p754435891556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.28%" id="mcps1.1.4.1.3"><p id="p711326791556"><a name="p711326791556"></a><a name="p711326791556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3930377391556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p2948903591556"><a name="p2948903591556"></a><a name="p2948903591556"></a>destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p270722191556"><a name="p270722191556"></a><a name="p270722191556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p2740730591556"><a name="p2740730591556"></a><a name="p2740730591556"></a>Specifies the destination network segment of a route.</p>
    <p id="p2436469411021"><a name="p2436469411021"></a><a name="p2436469411021"></a>The value must be in the CIDR format. Currently, only the value <strong id="b842352706144646"><a name="b842352706144646"></a><a name="b842352706144646"></a>0.0.0.0/0</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p5632574211054"><a name="p5632574211054"></a><a name="p5632574211054"></a>Specifies the next hop of a route.</p>
    <p id="p2794258711440"><a name="p2794258711440"></a><a name="p2794258711440"></a>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</p>
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
            "cidr": "192.168.0.0/16",
            "status": "OK",
            "routes": null,
            "enable_shared_snat": true
        }
    }
    ```


## Returned Value<a name="section61590629"></a>

-   Normal

    200

-   Abnormal

    <a name="table1944505495123"></a><table><thead align="left"><tr id="row4547095595123"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p5926870895123"><a name="p5926870895123"></a><a name="p5926870895123"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p3603600595123"><a name="p3603600595123"></a><a name="p3603600595123"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3323528795123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p770371395123"><a name="p770371395123"></a><a name="p770371395123"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2002103695123"><a name="p2002103695123"></a><a name="p2002103695123"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row4597160195123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3271222495123"><a name="p3271222495123"></a><a name="p3271222495123"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3244448395123"><a name="p3244448395123"></a><a name="p3244448395123"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2356489695123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2970841395123"><a name="p2970841395123"></a><a name="p2970841395123"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5757123495123"><a name="p5757123495123"></a><a name="p5757123495123"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4837906495123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2639007795123"><a name="p2639007795123"></a><a name="p2639007795123"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5722147095123"><a name="p5722147095123"></a><a name="p5722147095123"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row4523118995123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3984772595123"><a name="p3984772595123"></a><a name="p3984772595123"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p644027795123"><a name="p644027795123"></a><a name="p644027795123"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row5796249495123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6445046695123"><a name="p6445046695123"></a><a name="p6445046695123"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5310525895123"><a name="p5310525895123"></a><a name="p5310525895123"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row818527995123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5902789795123"><a name="p5902789795123"></a><a name="p5902789795123"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1653038095123"><a name="p1653038095123"></a><a name="p1653038095123"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1455569495123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3816053695123"><a name="p3816053695123"></a><a name="p3816053695123"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p399569495123"><a name="p399569495123"></a><a name="p399569495123"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row3596125495123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2718045895123"><a name="p2718045895123"></a><a name="p2718045895123"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5413351995123"><a name="p5413351995123"></a><a name="p5413351995123"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1743962995123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p332387895123"><a name="p332387895123"></a><a name="p332387895123"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p79870795123"><a name="p79870795123"></a><a name="p79870795123"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row718836995123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4538701695123"><a name="p4538701695123"></a><a name="p4538701695123"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5246967195123"><a name="p5246967195123"></a><a name="p5246967195123"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row246499895123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6544712595123"><a name="p6544712595123"></a><a name="p6544712595123"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6672576195123"><a name="p6672576195123"></a><a name="p6672576195123"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row6366093795123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5626223495123"><a name="p5626223495123"></a><a name="p5626223495123"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6094710095123"><a name="p6094710095123"></a><a name="p6094710095123"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row1165299095123"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p436817295123"><a name="p436817295123"></a><a name="p436817295123"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1827766295123"><a name="p1827766295123"></a><a name="p1827766295123"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

