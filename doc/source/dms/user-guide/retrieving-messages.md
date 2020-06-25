# Retrieving Messages<a name="EN-US_TOPIC_0143117133"></a>

## Scenario<a name="en-us_topic_0033854554-chtext"></a>

Messages can be retrieved from a queue.

## Prerequisites<a name="section49347015"></a>

A queue has been created. The queue has at least one consumer group and at least one message.

>![](/images/icon-note.gif) **NOTE:**   
>Messages are retained in a queue for at least 72 hours and are deleted after expiry. You can specify the retention period of messages in Kafka queues. The value range is 1 to 72 hours.  

## Procedure<a name="section41469957"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose  **Queue Manager**.
5.  Open the  **Retrieve Message**  dialog box using either of the methods:
    -   Method 1

        In the queue list, choose  **More **\>  **Retrieve Message**  in the same row as the queue from which messages will be retrieved.

    -   Method 2
        1.  Click the name of the queue from which messages will be retrieved.
        2.  Click the  **Consumer Groups**  tab.
        3.  In the consumer group list, click  **Retrieve Message**  in the same row as the consumer group who will retrieve messages from the chosen queue.

6.  Specify parameters as shown in  [Table 1](#table29045431203121).

    **Table  1**  Parameter description

    <a name="table29045431203121"></a>
    <table><thead align="left"><tr id="row21820003203121"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p22589805203121"><a name="p22589805203121"></a><a name="p22589805203121"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p17834936203121"><a name="p17834936203121"></a><a name="p17834936203121"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35343724203121"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p44269359203121"><a name="p44269359203121"></a><a name="p44269359203121"></a>Consumer Group Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p29048364203121"><a name="p29048364203121"></a><a name="p29048364203121"></a>Name of a consumer group.</p>
    <p id="p247128142710"><a name="p247128142710"></a><a name="p247128142710"></a>If you open the <strong id="b9137584172823"><a name="b9137584172823"></a><a name="b9137584172823"></a>Retrieve Message</strong> dialog box by choosing <strong id="b34852014172838"><a name="b34852014172838"></a><a name="b34852014172838"></a>More </strong>&gt; <strong id="b4440847172838"><a name="b4440847172838"></a><a name="b4440847172838"></a>Retrieve Message</strong> in the queue list, the <strong id="b47700380173151"><a name="b47700380173151"></a><a name="b47700380173151"></a>Consumer Group Name</strong> parameter is by default set to the name of the first consumer group in the chosen queue.</p>
    <p id="p35289222818"><a name="p35289222818"></a><a name="p35289222818"></a>If you open the <strong id="b36828069172950"><a name="b36828069172950"></a><a name="b36828069172950"></a>Retrieve Message</strong> dialog box by clicking <strong id="b52929970173018"><a name="b52929970173018"></a><a name="b52929970173018"></a>Retrieve Message</strong> in the consumer group list, the <strong id="b25737397173212"><a name="b25737397173212"></a><a name="b25737397173212"></a>Consumer Group Name</strong> parameter is by default set to the name of the chosen consumer group.</p>
    </td>
    </tr>
    <tr id="row37165444203121"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p57610994203121"><a name="p57610994203121"></a><a name="p57610994203121"></a>Queue Polling Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p324516456277"><a name="p324516456277"></a><a name="p324516456277"></a>Interval at which DMS polls the queue for messages.</p>
    <p id="p35978977203121"><a name="p35978977203121"></a><a name="p35978977203121"></a>The value can be: <strong id="b15638021123816"><a name="b15638021123816"></a><a name="b15638021123816"></a>3s</strong>, <strong id="b9435216163817"><a name="b9435216163817"></a><a name="b9435216163817"></a>5s</strong>, <strong id="b89681713193812"><a name="b89681713193812"></a><a name="b89681713193812"></a>10s</strong>, or <strong id="b11327121133812"><a name="b11327121133812"></a><a name="b11327121133812"></a>30s</strong>.</p>
    <p id="p977725918274"><a name="p977725918274"></a><a name="p977725918274"></a>Default value: <strong id="b1680264233019"><a name="b1680264233019"></a><a name="b1680264233019"></a>3s</strong> </p>
    </td>
    </tr>
    <tr id="row38904437716"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p208912437714"><a name="p208912437714"></a><a name="p208912437714"></a>Message Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p389114431273"><a name="p389114431273"></a><a name="p389114431273"></a>Type of messages to be retrieved.</p>
    <p id="p3840132110107"><a name="p3840132110107"></a><a name="p3840132110107"></a>Options:</p>
    <a name="ul1912039141016"></a><a name="ul1912039141016"></a><ul id="ul1912039141016"><li><strong id="b960123317235"><a name="b960123317235"></a><a name="b960123317235"></a>Normal</strong><p id="p4140527185217"><a name="p4140527185217"></a><a name="p4140527185217"></a>Only normal messages are retrieved from the chosen queue.</p>
    </li><li><strong id="b3876718917237"><a name="b3876718917237"></a><a name="b3876718917237"></a>Dead letter</strong><p id="p358753095217"><a name="p358753095217"></a><a name="p358753095217"></a>Only dead letter messages generated for the chosen consumer group are retrieved from the chosen queue.</p>
    </li></ul>
    <p id="p16822153643114"><a name="p16822153643114"></a><a name="p16822153643114"></a>Default value: <strong id="b1220483215293"><a name="b1220483215293"></a><a name="b1220483215293"></a>Normal</strong></p>
    <div class="note" id="note5197105913520"><a name="note5197105913520"></a><a name="note5197105913520"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p151993591954"><a name="p151993591954"></a><a name="p151993591954"></a>If the dead letter queue function is disabled in <a href="creating-a-queue.md">Creating a Queue</a>, only normal messages are retrieved.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row494912134512"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p65306191650"><a name="p65306191650"></a><a name="p65306191650"></a>Max. Message Count</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p3533419555"><a name="p3533419555"></a><a name="p3533419555"></a>Maximum number of messages to be retrieved in a single polling cycle.</p>
    <p id="p14533819254"><a name="p14533819254"></a><a name="p14533819254"></a>The value can be <strong id="b12262340312"><a name="b12262340312"></a><a name="b12262340312"></a>5</strong> or <strong id="b5261347314"><a name="b5261347314"></a><a name="b5261347314"></a>10</strong>.</p>
    <p id="p05339196519"><a name="p05339196519"></a><a name="p05339196519"></a>Default value: <strong id="b12834164233116"><a name="b12834164233116"></a><a name="b12834164233116"></a>5</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

    After you click the  **Start **button, the console polls the queue at regular intervals for 5 minutes, even if there are messages in the queue. After 5 minutes, the polling stops automatically. To stop polling before then, click  **Stop**  and the polling will stop after the current cycle of polling completes.

    If you close the  **Retrieve Message**  dialog box or change the  **Consumer Group Name**,  **Max. Message Count**, or  **Queue Polling Interval**  while messages are being retrieved, the message retrieval will stop after the current cycle of polling completes.

    Retrieved messages are displayed in the list. To view details such as the message body, message size, ID, attribute count, and attributes, click  **More Details**  in the same row as the chosen message. Message retrieval will not be interrupted when you are viewing details.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Messages can be retrieved only once by each consumer group. Data about messages retrieved by the current consumer group is lost after the  **Retrieve Message**  dialog box is closed or another consumer group is selected to retrieve messages. However, the messages can still be retrieved by other consumer groups.  
    >-   Messages from one queue are stored in different partitions to enable simultaneous retrieval of multiple messages by one consumer group. Each retrieval request can target messages in only one partition, preventing cross-partition management and access from adversely impacting performance. If the message queue contains only a few messages and messages are distributed over partitions, the number of messages in a single partition may be less than the number of messages you specified to be retrieved in a single polling cycle. This means that each polling cycle will return fewer messages than expected. However, all messages in the queue will be retrieved after multiple cycles.  

    **Table  2**  Parameters in the Messages Retrieved list

    <a name="table537217131332"></a>
    <table><thead align="left"><tr id="row163730130335"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p0373813193317"><a name="p0373813193317"></a><a name="p0373813193317"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p7373313123315"><a name="p7373313123315"></a><a name="p7373313123315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1537321318330"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4373191343310"><a name="p4373191343310"></a><a name="p4373191343310"></a>Message Body (Condensed)</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1937311343310"><a name="p1937311343310"></a><a name="p1937311343310"></a>Content of the message body.</p>
    <p id="p5315135317472"><a name="p5315135317472"></a><a name="p5315135317472"></a>Content of messages in Kafka queues is encoded with Base64.</p>
    </td>
    </tr>
    <tr id="row183731813103317"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p9373161315334"><a name="p9373161315334"></a><a name="p9373161315334"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p237313133339"><a name="p237313133339"></a><a name="p237313133339"></a>Handler of the message.</p>
    </td>
    </tr>
    <tr id="row1837381333315"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p15373171333316"><a name="p15373171333316"></a><a name="p15373171333316"></a>Body Size</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1937320137336"><a name="p1937320137336"></a><a name="p1937320137336"></a>Size of the message body.</p>
    </td>
    </tr>
    <tr id="row5373151314339"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p737311310338"><a name="p737311310338"></a><a name="p737311310338"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p81014224293"><a name="p81014224293"></a><a name="p81014224293"></a>Clicking <strong id="b43661112202335"><a name="b43661112202335"></a><a name="b43661112202335"></a>More Details</strong> in the <strong id="b59428318202435"><a name="b59428318202435"></a><a name="b59428318202435"></a>Operation</strong> column displays the complete message body, complete message ID, and complete message attributes of the message retrieved.</p>
    <p id="p426020335409"><a name="p426020335409"></a><a name="p426020335409"></a>The <strong id="b46411302202650"><a name="b46411302202650"></a><a name="b46411302202650"></a>Operation</strong> column is not displayed if the message is retrieved from a Kafka queue.</p>
    </td>
    </tr>
    </tbody>
    </table>


