# Creating a Queue<a name="EN-US_TOPIC_0143117118"></a>

## Scenario<a name="section66578044"></a>

The first task in using DMS is to create one or more queues.

## Procedure<a name="section24112512"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose  **Queue Manager**.
5.  Click  **Create Queue**. 

    The remaining number of queues that can be created is displayed above the  **Delete**  button. By default, a maximum of 5 queues can be created under a project. To create more than the default number of queues, contact customer service to increase your quota.

6.  Specify parameters listed in  [Table 1](#table173317324270).

    **Table  1**  Parameter description

    <a name="table173317324270"></a>
    <table><thead align="left"><tr id="row4331832122719"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p10332432162714"><a name="p10332432162714"></a><a name="p10332432162714"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p193329321278"><a name="p193329321278"></a><a name="p193329321278"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63323328277"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p10332332122718"><a name="p10332332122718"></a><a name="p10332332122718"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p6332133213274"><a name="p6332133213274"></a><a name="p6332133213274"></a>Unique name of a queue.</p>
    <p id="p53328326279"><a name="p53328326279"></a><a name="p53328326279"></a>When you create a queue, a default queue name is generated, which you can change if required. A queue name is 1 to 64 characters long. Only letters, digits, underscores (_), and hyphens (-) are allowed.</p>
    <p id="p153321332162713"><a name="p153321332162713"></a><a name="p153321332162713"></a>The queue name cannot be modified after creation of the queue.</p>
    </td>
    </tr>
    <tr id="row1133223215278"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1133215329272"><a name="p1133215329272"></a><a name="p1133215329272"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p733293219275"><a name="p733293219275"></a><a name="p733293219275"></a><strong id="b1454518178317"><a name="b1454518178317"></a><a name="b1454518178317"></a>Standard queue</strong> or <strong id="b15466172316"><a name="b15466172316"></a><a name="b15466172316"></a>Kafka queue</strong></p>
    </td>
    </tr>
    <tr id="row73321032112719"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p133327328276"><a name="p133327328276"></a><a name="p133327328276"></a>Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><div class="p" id="p1733293292716"><a name="p1733293292716"></a><a name="p1733293292716"></a>When the queue type is standard, the queue mode can be:<a name="ul1733213326279"></a><a name="ul1733213326279"></a><ul id="ul1733213326279"><li><strong id="b16284142494316"><a name="b16284142494316"></a><a name="b16284142494316"></a>Normal</strong>: Messages may be retrieved out of sequence, but the concurrency is higher.</li><li><strong id="b143420346323"><a name="b143420346323"></a><a name="b143420346323"></a>FIFO</strong>: Messages are retrieved in the order they were sent.</li></ul>
    </div>
    <div class="p" id="p14333103232712"><a name="p14333103232712"></a><a name="p14333103232712"></a>When the queue type is Kafka, the queue mode can be:<a name="ul1633393214271"></a><a name="ul1633393214271"></a><ul id="ul1633393214271"><li><strong id="b1845195810527"><a name="b1845195810527"></a><a name="b1845195810527"></a>High throughput</strong>: All message replicas are flushed to disk asynchronously. Select this mode when high message delivery performance is required.</li><li><strong id="b19307035320"><a name="b19307035320"></a><a name="b19307035320"></a>High reliability</strong>: All message replicas are flushed to disk synchronously. Select this mode when high message delivery reliability is required.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row2033383217278"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p133353219273"><a name="p133353219273"></a><a name="p133353219273"></a>Dead Letter Queue</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p133339326273"><a name="p133339326273"></a><a name="p133339326273"></a>This parameter is displayed only if the <strong id="b629199263"><a name="b629199263"></a><a name="b629199263"></a>Queue Type</strong> is set to <strong id="b1969463081"><a name="b1969463081"></a><a name="b1969463081"></a>Standard queue</strong>.</p>
    <p id="p123334321277"><a name="p123334321277"></a><a name="p123334321277"></a>An indicator of whether to enable dead letter queue, which accommodates messages that cannot be correctly retrieved.</p>
    <p id="p433373220270"><a name="p433373220270"></a><a name="p433373220270"></a>If a message fails to be retrieved for a preset number of times, it will be sent to the dead letter queue and retained for 72 hours. You can then retrieve the message from the dead letter queue.</p>
    <p id="p103331732172716"><a name="p103331732172716"></a><a name="p103331732172716"></a>Messages in the dead letter queue are specific to individual consumer groups, and consumer groups cannot retrieve each other's dead letter messages.</p>
    <p id="p11333832172717"><a name="p11333832172717"></a><a name="p11333832172717"></a>Dead letter messages from FIFO queues are sent to the dead letter queue in the FIFO order.</p>
    <p id="p15333832162716"><a name="p15333832162716"></a><a name="p15333832162716"></a>By default, <strong id="b2009313650"><a name="b2009313650"></a><a name="b2009313650"></a>Dead Letter Queue</strong> is disabled.</p>
    </td>
    </tr>
    <tr id="row19333133272719"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p73331232152715"><a name="p73331232152715"></a><a name="p73331232152715"></a>Message Retention Period (h)</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p19333153222719"><a name="p19333153222719"></a><a name="p19333153222719"></a>This parameter is displayed only if the <strong id="b152761624173718"><a name="b152761624173718"></a><a name="b152761624173718"></a>Queue Type</strong> is set to <strong id="b927662483720"><a name="b927662483720"></a><a name="b927662483720"></a>Kafka queue</strong>.</p>
    <p id="p5333193282710"><a name="p5333193282710"></a><a name="p5333193282710"></a>The number of hours for which messages will be preserved in a Kafka queue. Messages older than that period will be deleted. Deleted messages are not retrievable to consumer groups.</p>
    <p id="p113331832112717"><a name="p113331832112717"></a><a name="p113331832112717"></a>Value range: integers from 1 to 72</p>
    <p id="p1433343219276"><a name="p1433343219276"></a><a name="p1433343219276"></a>Default value: <strong id="b264693441"><a name="b264693441"></a><a name="b264693441"></a>72</strong></p>
    </td>
    </tr>
    <tr id="row033317329279"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p12333132112713"><a name="p12333132112713"></a><a name="p12333132112713"></a>Maximum Retrievals</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p33341332182719"><a name="p33341332182719"></a><a name="p33341332182719"></a>This parameter is displayed only if <strong id="b710557834"><a name="b710557834"></a><a name="b710557834"></a>Dead Letter Queue</strong> is enabled.</p>
    <p id="p123341132102711"><a name="p123341132102711"></a><a name="p123341132102711"></a>The maximum number of times a message can be retrieved before it is sent to the dead letter queue.</p>
    <p id="p93341932142718"><a name="p93341932142718"></a><a name="p93341932142718"></a>Value range: 1 to 100</p>
    <p id="p8334332122717"><a name="p8334332122717"></a><a name="p8334332122717"></a>Default value: <strong id="b858421681"><a name="b858421681"></a><a name="b858421681"></a>3</strong></p>
    </td>
    </tr>
    <tr id="row193341432182712"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p16334103282717"><a name="p16334103282717"></a><a name="p16334103282717"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1633463232713"><a name="p1633463232713"></a><a name="p1633463232713"></a>Tags of a queue, which are used to identify the queue. You can classify queues by tag and search for a specific queue based on its tags.</p>
    <a name="ul173341832122712"></a><a name="ul173341832122712"></a><ul id="ul173341832122712"><li>Tags of the same queue cannot have the same key.</li><li>You can customize tags or use tags predefined by TMS.</li><li>You can add a maximum of 10 tag keys to a queue.</li></ul>
    </td>
    </tr>
    <tr id="row1633418324274"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p333433211279"><a name="p333433211279"></a><a name="p333433211279"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p3335103210274"><a name="p3335103210274"></a><a name="p3335103210274"></a>The description is 0 to 160 characters long and cannot contain angle brackets (&lt; and &gt;).</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    After the queue is created, you can click the name of a queue to view queue details.


