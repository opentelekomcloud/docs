# Configuring Message Notification<a name="EN-US_TOPIC_0125375245"></a>

You can connect MRS to SMN to provide basic SMS notification and email notification functions in specific scenarios.

## Scenario<a name="section4424935411854"></a>

On the MRS management console, you can enable or disable the notification service on the  **Alarms**  tab page of the cluster details page. The functions in the following scenarios can be implemented only after the required cluster function is enabled:

-   After a user subscribes to the notification service, the MRS management plane notifies the user of success or failure of cluster expansion, shrinking, termination, and auto scaling by email or SMS message.
-   The management plane checks alarms about the MRS cluster and sends a notification to the user's tenants if the alarm is critical and affects service use.
-   If either of the operations such as deletion, shutdown, specifications modification, restart, and OS update is performed on an ECS in a cluster, the MRS cluster malfunctions. The management plane notifies a user when detecting that the VM of the user is in either of the preceding states.

## Procedure<a name="section2769747914132"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/wwx437827-中软基础平台部-datasight-image-bbfbe22f-2a2d-4e1b-8f10-a7782fd1d3ed-35.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Alarms**  tab page.
5.  Choose  **Notification Rules**  \>  **Add Notification Rule**. The  **Add Notification Rule**  page is displayed.
6.  Set the notification rule parameters.

    **Table  1**  Notification rule parameters

    <a name="table16966367519"></a>
    <table><thead align="left"><tr id="row156941836135115"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p13694133625120"><a name="p13694133625120"></a><a name="p13694133625120"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p269413364512"><a name="p269413364512"></a><a name="p269413364512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46951636175110"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p16951836145117"><a name="p16951836145117"></a><a name="p16951836145117"></a>Rule Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1469573612516"><a name="p1469573612516"></a><a name="p1469573612516"></a>Notification rule name specified by a user. Only digits, letters, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row8695123635117"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p12695336145112"><a name="p12695336145112"></a><a name="p12695336145112"></a>Message Notification</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul11695183615117"></a><a name="ul11695183615117"></a><ul id="ul11695183615117"><li>If you enable this function, the system sends notifications to subscribers based on the notification rule.</li><li>If you disable this function, the rule does not take effect, that is, notifications are not sent to subscribers.</li></ul>
    </td>
    </tr>
    <tr id="row12695236135113"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1669563645114"><a name="p1669563645114"></a><a name="p1669563645114"></a>Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p769583616511"><a name="p769583616511"></a><a name="p769583616511"></a>Select an existing topic or click <strong id="b36951236145112"><a name="b36951236145112"></a><a name="b36951236145112"></a>Create Topic</strong> to create a topic.</p>
    </td>
    </tr>
    <tr id="row369583618519"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p6695173610516"><a name="p6695173610516"></a><a name="p6695173610516"></a>Notification Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1169593685110"><a name="p1169593685110"></a><a name="p1169593685110"></a>Select the type of the notification to be subscribed to.</p>
    <a name="ul469533614517"></a><a name="ul469533614517"></a><ul id="ul469533614517"><li>Alarm</li><li>Event</li></ul>
    </td>
    </tr>
    <tr id="row26961368518"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1569583616511"><a name="p1569583616511"></a><a name="p1569583616511"></a>Subscription Items</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p116961336155119"><a name="p116961336155119"></a><a name="p116961336155119"></a>Select the items to be subscribed to. You can select all or some items as required.</p>
    <a name="ul13696153635114"></a><a name="ul13696153635114"></a><ul id="ul13696153635114"><li>Critical</li><li>Major</li><li>Minor</li><li>Suggestion</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click OK.

