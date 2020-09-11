# Configuring SMN-Enabled Event Notification<a name="en-us_topic_0066088963"></a>

This topic describes how to configure an SMN-enabled event notification rule on OBS Console.

## Background Information<a name="section72855457345"></a>

For details, see  [SMN-Enabled Event Notification](smn-enabled-event-notification.md).

## Procedure<a name="section4422459618019"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the  **Basic Configurations**  area, click the  **Event Notification**  label. The  **Event Notification**  page is displayed.

    Alternatively, you can choose  **Basic Configurations**  \>  **Event Notification**  in the navigation pane on the left.

3.  Click  **Create**. The  **Create Event Notification**  dialog box is displayed. See  [Figure 1](#fig17847723015)  for details.

    **Figure  1**  Creating an event notification rule<a name="fig17847723015"></a>  
    ![](figures/creating-an-event-notification-rule.png "creating-an-event-notification-rule")

4.  Configure parameters.  [Table 1](#aobs_console_0039_mmccppss_table01)  describes the parameters.

    **Table  1**  Event notification parameters

    <a name="aobs_console_0039_mmccppss_table01"></a>
    <table><thead align="left"><tr id="row2055942"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.3.1.1"><p id="p32313598"><a name="p32313598"></a><a name="p32313598"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="66%" id="mcps1.2.3.1.2"><p id="p155758"><a name="p155758"></a><a name="p155758"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12616447"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p15299288"><a name="p15299288"></a><a name="p15299288"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p31282850"><a name="p31282850"></a><a name="p31282850"></a>Name of the event. If the event name is left blank, the system will automatically generate a unique ID as the event name.</p>
    </td>
    </tr>
    <tr id="row13110201"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p55293359"><a name="p55293359"></a><a name="p55293359"></a>Events</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p49577065"><a name="p49577065"></a><a name="p49577065"></a>Various types of events. Currently, OBS supports event notification for the following event types:</p>
    <a name="ul43540403"></a><a name="ul43540403"></a><ul id="ul43540403"><li><strong id="b1048514225810"><a name="b1048514225810"></a><a name="b1048514225810"></a>ObjectCreated</strong>: Indicates all kinds of object creation operations, including PUT, POST, and COPY of objects, as well as the merging of parts.</li><li><strong id="b161475022395327"><a name="b161475022395327"></a><a name="b161475022395327"></a>Put</strong>: Uploads an object using the PUT method.</li><li><strong id="b63719940162134"><a name="b63719940162134"></a><a name="b63719940162134"></a>Post</strong>: Uploads an object using the POST method.</li><li><strong id="b1614216482110"><a name="b1614216482110"></a><a name="b1614216482110"></a>Copy</strong>: Uploads an object using the COPY method.</li><li><strong id="b157561432376"><a name="b157561432376"></a><a name="b157561432376"></a>CompleteMultipartUpload</strong>: Merges parts of multipart tasks.</li><li><strong id="b1247145233716"><a name="b1247145233716"></a><a name="b1247145233716"></a>ObjectRemoved</strong>: Deletes an object.</li><li><strong id="b102321594591"><a name="b102321594591"></a><a name="b102321594591"></a>Delete</strong>: Deletes an object with a specified version ID.</li><li><strong id="b146469154595"><a name="b146469154595"></a><a name="b146469154595"></a>DeleteMarkerCreated</strong>: Deletes an object without specifying a version ID.</li></ul>
    <p id="p64865822"><a name="p64865822"></a><a name="p64865822"></a>Multiple event types are applicable to the same object. For example, if you have selected <strong id="b2091313193599"><a name="b2091313193599"></a><a name="b2091313193599"></a>Put</strong>, <strong id="b1691461905913"><a name="b1691461905913"></a><a name="b1691461905913"></a>Copy</strong>, and <strong id="b1591591955916"><a name="b1591591955916"></a><a name="b1591591955916"></a>Delete</strong> in an event notification rule, a notification message will be sent to you when the specified object is uploaded to, copied to, or deleted from the bucket. <strong id="b10982172711591"><a name="b10982172711591"></a><a name="b10982172711591"></a>ObjectCreated</strong> contains <strong id="b9983132755917"><a name="b9983132755917"></a><a name="b9983132755917"></a>Put</strong>, <strong id="b15984827185911"><a name="b15984827185911"></a><a name="b15984827185911"></a>Post</strong>, <strong id="b11984927175910"><a name="b11984927175910"></a><a name="b11984927175910"></a>Copy</strong>, and <strong id="b79851127195916"><a name="b79851127195916"></a><a name="b79851127195916"></a>CompleteMultipartUpload</strong>. If you select <strong id="b9986132712595"><a name="b9986132712595"></a><a name="b9986132712595"></a>ObjectCreated</strong>, the others are automatically selected and cannot be deselected. Similarly, if you select <strong id="b918816366592"><a name="b918816366592"></a><a name="b918816366592"></a>ObjectRemoved</strong>, <strong id="b818911360595"><a name="b818911360595"></a><a name="b818911360595"></a>Delete</strong> and <strong id="b91901136185910"><a name="b91901136185910"></a><a name="b91901136185910"></a>DeleteMarkerCreated</strong> are automatically selected and cannot be deselected.</p>
    </td>
    </tr>
    <tr id="row47353991"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p10468038"><a name="p10468038"></a><a name="p10468038"></a>Prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p42604738"><a name="p42604738"></a><a name="p42604738"></a>Object name prefix. The event notification rule applies to objects that have the same name prefix.</p>
    <div class="note" id="note13847653113412"><a name="note13847653113412"></a><a name="note13847653113412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p138481553193416"><a name="p138481553193416"></a><a name="p138481553193416"></a>If neither the <strong id="b11129141033217"><a name="b11129141033217"></a><a name="b11129141033217"></a>Prefix</strong> nor the <strong id="b3429101412321"><a name="b3429101412321"></a><a name="b3429101412321"></a>Suffix</strong> is configured, the event notification rule applies to all objects in the bucket.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row16547757"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p65299951"><a name="p65299951"></a><a name="p65299951"></a>Suffix</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p54804702"><a name="p54804702"></a><a name="p54804702"></a>Object name suffix. The event notification rule applies to objects that have the same name suffix.</p>
    <div class="note" id="note64263792115"><a name="note64263792115"></a><a name="note64263792115"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul75801343183518"></a><a name="ul75801343183518"></a><ul id="ul75801343183518"><li>A folder path ends with a slash (/). Therefore, if you want to configure the event notification for operations on folders and you need to filter folders by suffix, the suffix must also end with a slash (/).</li><li>If neither the <strong id="b14649194213219"><a name="b14649194213219"></a><a name="b14649194213219"></a>Prefix</strong> nor the <strong id="b16651104273212"><a name="b16651104273212"></a><a name="b16651104273212"></a>Suffix</strong> is configured, the event notification rule applies to all objects in the bucket.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row16019620144324"><td class="cellrowborder" rowspan="2" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p28106203"><a name="p28106203"></a><a name="p28106203"></a>SMN Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p28828893173745"><a name="p28828893173745"></a><a name="p28828893173745"></a>Project: The project that contains the SMN topic you want to select.</p>
    <p id="p66230298175226"><a name="p66230298175226"></a><a name="p66230298175226"></a>Projects are used to manage and classify cloud resources, including SMN topics. Each project contains different SMN topics. Select a project first and then a topic.</p>
    </td>
    </tr>
    <tr id="row13603062"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><div class="p" id="p62009948"><a name="p62009948"></a><a name="p62009948"></a>Topic: specifies the SMN topic that authorizes OBS to publish messages. You can create such topics on the SMN management console.<div class="note" id="note21218627"><a name="note21218627"></a><a name="note21218627"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul290173585413"></a><a name="ul290173585413"></a><ul id="ul290173585413"><li class="NotesTextinTable">Once SMN topics are selected for pushing OBS event notifications, do not delete them or cancel their authorizations to OBS.</li><li class="NotesTextinTable">If the topics are deleted or their authorizations to OBS are canceled, the following conditions may occur:<p class="NotesTextinTable" id="p162521921105510"><a name="p162521921105510"></a><a name="p162521921105510"></a>a. The subscriber of the topic cannot receive messages.</p>
    <p class="NotesTextinTable" id="p198921517175511"><a name="p198921517175511"></a><a name="p198921517175511"></a>b. Event notifications associated with unavailable topics are automatically cleared.</p>
    </li><li>For details, see sections "Creating a Topic", "Adding a Subscription to the Topic", and "Configuring a Topic Policy" in the <em id="i028282204217"><a name="i028282204217"></a><a name="i028282204217"></a>Simple Message Notification User Guide</em>.</li></ul>
    </div></div>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.

## Related Operations<a name="section183921920123113"></a>

You can click  **Edit**  under the  **Operation**  column of an event notification rule, to edit the notification rule. Also you can click  **Delete**  to delete it.

If you want to delete more than one event notification rules at a time, select them and click  **Delete**  above the list.

