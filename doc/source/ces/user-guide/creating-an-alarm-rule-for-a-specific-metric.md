# Creating an Alarm Rule for a Specific Metric<a name="EN-US_TOPIC_0084572282"></a>

Cloud Eye enables you to create alarm rules for a metric of one or multiple cloud services, making it convenient for you to monitor the metric of your resources.

## Adding a Custom Alarm Rule<a name="section62658995171654"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Management & Deployment**, select  **Cloud Eye**.
4.  Choose  **Alarm Management**  \>  **Alarm Rules**  and click  **Create Alarm Rule**.
5.  In the  **Create Alarm Rule**  dialog box, follow the prompts to set the parameters.
    1.  Select an object and configure parameters listed in  [Table 1](#table35986202162751). Click  **Next**.

        **Table  1**  Parameter description

        <a name="table35986202162751"></a>
        <table><thead align="left"><tr id="row7480685162751"><th class="cellrowborder" valign="top" width="24.9%" id="mcps1.2.3.1.1"><p id="p2221744016285"><a name="p2221744016285"></a><a name="p2221744016285"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="75.1%" id="mcps1.2.3.1.2"><p id="p5478221016285"><a name="p5478221016285"></a><a name="p5478221016285"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row37125236162751"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p54354165162751"><a name="p54354165162751"></a><a name="p54354165162751"></a>Resource Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p31697306162858"><a name="p31697306162858"></a><a name="p31697306162858"></a>Specifies the name of the service for which the alarm rule is configured.</p>
        <p id="p1732911297334"><a name="p1732911297334"></a><a name="p1732911297334"></a>Example value: <strong id="b097443354214"><a name="b097443354214"></a><a name="b097443354214"></a>Elastic Cloud Server</strong></p>
        </td>
        </tr>
        <tr id="row10616740162751"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p54649575162751"><a name="p54649575162751"></a><a name="p54649575162751"></a>Dimension</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p28042977162858"><a name="p28042977162858"></a><a name="p28042977162858"></a>Specifies the metric dimension of the selected cloud resource.</p>
        <p id="p12143164853319"><a name="p12143164853319"></a><a name="p12143164853319"></a>Example value: <strong id="b2731114022213"><a name="b2731114022213"></a><a name="b2731114022213"></a>ECS</strong></p>
        </td>
        </tr>
        <tr id="row53988257162836"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p10972710162836"><a name="p10972710162836"></a><a name="p10972710162836"></a>Monitored Object</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p65673712162858"><a name="p65673712162858"></a><a name="p65673712162858"></a>Specifies the resource for which the alarm rule is set. You can specify one or more resources.</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  In the  **Select Metric**  step, select  **Create manually**  and configure parameters based on  [Table 2](#table4534051437).

        **Table  2**  Parameter description

        <a name="table4534051437"></a>
        <table><thead align="left"><tr id="row3530951333"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p1530851938"><a name="p1530851938"></a><a name="p1530851938"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="59.46%" id="mcps1.2.4.1.2"><p id="p1530551132"><a name="p1530551132"></a><a name="p1530551132"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="23.94%" id="mcps1.2.4.1.3"><p id="p1453016511319"><a name="p1453016511319"></a><a name="p1453016511319"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row45306511317"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p115301254316"><a name="p115301254316"></a><a name="p115301254316"></a>Method</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p145301056319"><a name="p145301056319"></a><a name="p145301056319"></a>Specifies the means by which you create the alarm rule.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p105301251131"><a name="p105301251131"></a><a name="p105301251131"></a>Create manually</p>
        </td>
        </tr>
        <tr id="row45317514311"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p125302519314"><a name="p125302519314"></a><a name="p125302519314"></a>Metric</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p12531457319"><a name="p12531457319"></a><a name="p12531457319"></a>For example:</p>
        <a name="ul1753119519317"></a><a name="ul1753119519317"></a><ul id="ul1753119519317"><li>CPU Usage<p id="p3531759318"><a name="p3531759318"></a><a name="p3531759318"></a>Indicates the CPU usage of the monitored object. The unit is percent.</p>
        </li></ul>
        <a name="ul1531145138"></a><a name="ul1531145138"></a><ul id="ul1531145138"><li>Memory Usage<p id="p9531155635"><a name="p9531155635"></a><a name="p9531155635"></a>Indicates the percentage of memory currently in use. The unit is percent.</p>
        </li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p7531105036"><a name="p7531105036"></a><a name="p7531105036"></a>CPU Usage</p>
        </td>
        </tr>
        <tr id="row137702043153419"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p9435204373719"><a name="p9435204373719"></a><a name="p9435204373719"></a>Alarm Policy</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p2043584343715"><a name="p2043584343715"></a><a name="p2043584343715"></a>Specifies the policy that triggers an alarm.</p>
        <p id="p043712111488"><a name="p043712111488"></a><a name="p043712111488"></a>For example, an alarm is triggered if the metric average data is 80% or more for three consecutive periods of 5 minutes.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p54357432379"><a name="p54357432379"></a><a name="p54357432379"></a>N/A</p>
        </td>
        </tr>
        <tr id="row125695754311"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p1195420845111"><a name="p1195420845111"></a><a name="p1195420845111"></a>Alarm Severity</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p17956884516"><a name="p17956884516"></a><a name="p17956884516"></a>Specifies the severity of the alarm. Valid values are <strong id="b842352706182313"><a name="b842352706182313"></a><a name="b842352706182313"></a>Critical</strong>, <strong id="b842352706182316"><a name="b842352706182316"></a><a name="b842352706182316"></a>Major</strong>, <strong id="b842352706182320"><a name="b842352706182320"></a><a name="b842352706182320"></a>Minor</strong>, and <strong id="b842352706182324"><a name="b842352706182324"></a><a name="b842352706182324"></a>Informational</strong>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p8956389517"><a name="p8956389517"></a><a name="p8956389517"></a>Major</p>
        </td>
        </tr>
        <tr id="row14533185337"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p05331451736"><a name="p05331451736"></a><a name="p05331451736"></a>Alarm Notification</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p25331957319"><a name="p25331957319"></a><a name="p25331957319"></a>Specifies whether to notify users when alarms are triggered. Notifications can be sent by emails, text messages, or HTTP/HTTPS requests sent to the servers.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p10533353313"><a name="p10533353313"></a><a name="p10533353313"></a>Enable</p>
        </td>
        </tr>
        <tr id="row115341653311"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p65331051036"><a name="p65331051036"></a><a name="p65331051036"></a>Topic</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p195331052311"><a name="p195331052311"></a><a name="p195331052311"></a>Specifies the name of the topic to which the alarm notification is sent.</p>
        <p id="p45331951433"><a name="p45331951433"></a><a name="p45331951433"></a>If you enable this function, you need to select a topic. If no desirable topics are available, you need to create one first, whereupon the SMN service is invoked. For details about how to create a topic, see the <em id="i93185645019156"><a name="i93185645019156"></a><a name="i93185645019156"></a>Simple Message Notification User Guide</em>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p5534552312"><a name="p5534552312"></a><a name="p5534552312"></a>N/A</p>
        </td>
        </tr>
        <tr id="row17534558319"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p1953418515316"><a name="p1953418515316"></a><a name="p1953418515316"></a>Trigger Condition</p>
        </td>
        <td class="cellrowborder" valign="top" width="59.46%" headers="mcps1.2.4.1.2 "><p id="p353475732"><a name="p353475732"></a><a name="p353475732"></a>Specifies the condition for triggering the alarm. You can select <strong id="b842352706181020"><a name="b842352706181020"></a><a name="b842352706181020"></a>Generated alarm</strong>, <strong id="b842352706181028"><a name="b842352706181028"></a><a name="b842352706181028"></a>Cleared alarm</strong>, or both.</p>
        </td>
        <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.4.1.3 "><p id="p1534455310"><a name="p1534455310"></a><a name="p1534455310"></a>N/A</p>
        </td>
        </tr>
        </tbody>
        </table>

    3.  In the  **Specify Rule Name**  step, set the parameters as prompted. Click  **Finish**.

        **Table  3**  Parameter description

        <a name="table7623731163957"></a>
        <table><thead align="left"><tr id="row1169056163957"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.3.1.1"><p id="p57791071164012"><a name="p57791071164012"></a><a name="p57791071164012"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="75.51%" id="mcps1.2.3.1.2"><p id="p50565187164012"><a name="p50565187164012"></a><a name="p50565187164012"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row36013392163957"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.3.1.1 "><p id="p61370602164020"><a name="p61370602164020"></a><a name="p61370602164020"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.51%" headers="mcps1.2.3.1.2 "><p id="p4962871164020"><a name="p4962871164020"></a><a name="p4962871164020"></a>Specifies the alarm rule name. The system generates a name randomly but you can change it.</p>
        <p id="p245581843716"><a name="p245581843716"></a><a name="p245581843716"></a>Example value: <strong id="b0804441112214"><a name="b0804441112214"></a><a name="b0804441112214"></a>alarm-b6al</strong></p>
        </td>
        </tr>
        <tr id="row2717654163957"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.3.1.1 "><p id="p55312011164020"><a name="p55312011164020"></a><a name="p55312011164020"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.51%" headers="mcps1.2.3.1.2 "><p id="p51087931164020"><a name="p51087931164020"></a><a name="p51087931164020"></a>(Optional) Provides supplementary information about the alarm rule.</p>
        </td>
        </tr>
        </tbody>
        </table>



