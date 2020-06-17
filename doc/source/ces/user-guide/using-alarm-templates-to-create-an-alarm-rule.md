# Using Alarm Templates to Create an Alarm Rule<a name="EN-US_TOPIC_0084572213"></a>

Cloud Eye enables you to use alarm templates to create alarm rules, making it easy and convenient to add or modify alarm rules for resources or cloud services, especially for a large number of resources and cloud services.

This topic describes how to use a default alarm template to create an alarm rule for a cloud service resource.

## Creating Alarm Rules<a name="section62658995171654"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Management & Deployment**, select  **Cloud Eye**.
4.  In the navigation pane on the left, choose  **Alarm Management**  \>  **Alarm Rules**.
5.  Click  **Create Alarm Rule**  in the upper right corner.
6.  In the  **Create Alarm Rule**  dialog box, follow the prompts to set the parameters.
    1.  Select an object and configure other parameters listed in  [Table 1](#table2902443185911). Click  **Next**.

        **Table  1**  Parameters

        <a name="table2902443185911"></a>
        <table><thead align="left"><tr id="row59044436596"><th class="cellrowborder" valign="top" width="24.9%" id="mcps1.2.3.1.1"><p id="p990410439599"><a name="p990410439599"></a><a name="p990410439599"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="75.1%" id="mcps1.2.3.1.2"><p id="p290534320597"><a name="p290534320597"></a><a name="p290534320597"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row139086431592"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p15908204318599"><a name="p15908204318599"></a><a name="p15908204318599"></a>Resource Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p1790884310590"><a name="p1790884310590"></a><a name="p1790884310590"></a>Specifies the name of the service for which the alarm rule is configured.</p>
        </td>
        </tr>
        <tr id="row491164325912"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p2912243175913"><a name="p2912243175913"></a><a name="p2912243175913"></a>Dimension</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p9912343125912"><a name="p9912343125912"></a><a name="p9912343125912"></a>Specifies the metric dimension of the selected cloud resource.</p>
        </td>
        </tr>
        <tr id="row2912164313591"><td class="cellrowborder" valign="top" width="24.9%" headers="mcps1.2.3.1.1 "><p id="p18701139155613"><a name="p18701139155613"></a><a name="p18701139155613"></a>Monitored Object</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.1%" headers="mcps1.2.3.1.2 "><p id="p14913124312596"><a name="p14913124312596"></a><a name="p14913124312596"></a>Specifies the resource for which the alarm rule is set. You can specify one or more resources.</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  In the  **Select Metric**  step, select  **Use template**  and configure parameters based on  [Table 2](#table17310615145610).

        **Table  2**  Parameters

        <a name="table17310615145610"></a>
        <table><thead align="left"><tr id="row1830881513561"><th class="cellrowborder" valign="top" width="25.369999999999997%" id="mcps1.2.3.1.1"><p id="p73081015165615"><a name="p73081015165615"></a><a name="p73081015165615"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="74.63%" id="mcps1.2.3.1.2"><p id="p20308171535615"><a name="p20308171535615"></a><a name="p20308171535615"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row143081615195619"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.3.1.1 "><p id="p830815150569"><a name="p830815150569"></a><a name="p830815150569"></a>Method</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.63%" headers="mcps1.2.3.1.2 "><p id="p15308915105616"><a name="p15308915105616"></a><a name="p15308915105616"></a>Specifies the means by which you create the alarm rule.</p>
        </td>
        </tr>
        <tr id="row230841525618"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.3.1.1 "><p id="p1830891516561"><a name="p1830891516561"></a><a name="p1830891516561"></a>Template</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.63%" headers="mcps1.2.3.1.2 "><p id="p12308111535617"><a name="p12308111535617"></a><a name="p12308111535617"></a>Specifies the template to be used.</p>
        </td>
        </tr>
        <tr id="row19309615185617"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.3.1.1 "><p id="p530981585610"><a name="p530981585610"></a><a name="p530981585610"></a>Alarm Notification</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.63%" headers="mcps1.2.3.1.2 "><p id="p14309415155617"><a name="p14309415155617"></a><a name="p14309415155617"></a>Specifies whether to notify users when alarms are triggered. Notifications can be sent by emails or text messages, or HTTP/HTTPS requests sent to the servers.</p>
        </td>
        </tr>
        <tr id="row831016155567"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.3.1.1 "><p id="p12310121585614"><a name="p12310121585614"></a><a name="p12310121585614"></a>Topic</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.63%" headers="mcps1.2.3.1.2 "><p id="p23101815125618"><a name="p23101815125618"></a><a name="p23101815125618"></a>Specifies the name of the topic to which the alarm notification is sent.</p>
        <p id="p163101115105615"><a name="p163101115105615"></a><a name="p163101115105615"></a>If you enable this function, you need to select a topic. If no desirable topics are available, you need to create one first, whereupon the SMN service is invoked. For details about how to create a topic, see the <em id="i296877741"><a name="i296877741"></a><a name="i296877741"></a>Simple Message Notification User Guide</em>.</p>
        </td>
        </tr>
        <tr id="row531041519563"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.3.1.1 "><p id="p1231014155561"><a name="p1231014155561"></a><a name="p1231014155561"></a>Trigger Condition</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.63%" headers="mcps1.2.3.1.2 "><p id="p1531071512564"><a name="p1531071512564"></a><a name="p1531071512564"></a>Specifies the condition for triggering the alarm. You can select <strong id="b842352706181020"><a name="b842352706181020"></a><a name="b842352706181020"></a>Generated alarm</strong>, <strong id="b842352706181028"><a name="b842352706181028"></a><a name="b842352706181028"></a>Cleared alarm</strong>, or both.</p>
        </td>
        </tr>
        </tbody>
        </table>

    3.  In the  **Specify Rule Name**  step, set the parameters as prompted. After the configuration is complete, click  **Finish**.

        **Table  3**  Parameters

        <a name="table10391431667"></a>
        <table><thead align="left"><tr id="row133921438611"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.3.1.1"><p id="p0393231567"><a name="p0393231567"></a><a name="p0393231567"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="75.51%" id="mcps1.2.3.1.2"><p id="p1393631469"><a name="p1393631469"></a><a name="p1393631469"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row3396331612"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.3.1.1 "><p id="p63961231563"><a name="p63961231563"></a><a name="p63961231563"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.51%" headers="mcps1.2.3.1.2 "><p id="p839633762"><a name="p839633762"></a><a name="p839633762"></a>Specifies the alarm rule name. The system generates a name randomly but you can change it.</p>
        <p id="p1786174103520"><a name="p1786174103520"></a><a name="p1786174103520"></a>Example value: <strong id="b158472055192612"><a name="b158472055192612"></a><a name="b158472055192612"></a>alarm-b6al</strong></p>
        </td>
        </tr>
        <tr id="row1739693467"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.3.1.1 "><p id="p6396938611"><a name="p6396938611"></a><a name="p6396938611"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="75.51%" headers="mcps1.2.3.1.2 "><p id="p1739653463"><a name="p1739653463"></a><a name="p1739653463"></a>(Optional) Provides supplementary information about the alarm rule.</p>
        </td>
        </tr>
        </tbody>
        </table>



After the alarm rule is created, if the metric data reaches the specified threshold, Cloud Eye immediately informs you that an exception has occurred.

