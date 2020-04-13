# Best Practices<a name="EN-US_TOPIC_0143117197"></a>

## Recommendations on Creating and Retrieving Messages<a name="section253312468517"></a>

This section describes how to get the most out of DMS.

When using DMS, there are some measures you can take to improve the efficiency of API call and message sending and retrieval. During message sending and retrieval, DMS, producers, and consumers collaborate to ensure service reliability. Best practices for message producers and consumers are as follows:

-   The producer decides whether to re-send the message based on the DMS response.

    Each time the producer sends a message, it waits for an API response to confirm that the message is successfully sent. If an exception occurs when sending the message, the producer will not receive a success response and must decide whether to re-send the message. If a success response is received, it indicates that the message has been stored in DMS.

-   The consumer acknowledges successful message retrieval.

    Messages are stored in DMS in the order that they are created. During message retrieval, the consumer obtains messages stored in DMS in the order that they are stored. After the consumer retrieves the messages, the message retrieval status is recorded as successful or failed. The status is then submitted to DMS. Based on the retrieval status, DMS determines whether to retrieve the next batch of messages or retrieve the messages that failed to be retrieved.

    During this process, the message retrieval status may not be successfully submitted due to an exception. In this case, the corresponding messages will be re-obtained by the consumer in the next message retrieval request.

-   Create different consumer groups to locate faults or debug new services interconnection.

    You can use DMS as a message management system. Reading message content from queues is helpful to fault locating and service debugging. 

    To ensure that other services can continue to process messages in queues, you can create a new consumer group to retrieve and analyze the messages.

-   Send and retrieve messages in batches.

    You are advised to send and retrieve messages in batches. This can help improve the efficiency of sending and retrieving messages, reduce the number of API calls, and minimize service costs.

    During batch message retrieval, the consumer should process the messages and acknowledge message retrievals in the order that the messages are received. If one message fails to be retrieved, the consumer should not process it or subsequent messages in the same batch, because this message and subsequent messages will be re-sent. Only the messages that are correctly processed are acknowledged.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The DMS console allows only one message to be sent at a time.  


## Recommended Parameter Settings for Kafka Clients<a name="section17209041192913"></a>

This section provides recommendations on configuring common parameters for Kafka producers and consumers.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The following parameter setting recommendations are applicable only to Kafka queues and Kafka premium instances and are not applicable to DMS normal or FIFO queues.  

**Table  1**  Producer parameters

<a name="table1323919491438"></a>
<table><thead align="left"><tr id="row024116495310"><th class="cellrowborder" valign="top" width="15.78%" id="mcps1.2.5.1.1"><p id="p92901917413"><a name="p92901917413"></a><a name="p92901917413"></a><strong id="b1920930143313"><a name="b1920930143313"></a><a name="b1920930143313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.459999999999999%" id="mcps1.2.5.1.2"><p id="p1029021448"><a name="p1029021448"></a><a name="p1029021448"></a><strong id="b99547163314"><a name="b99547163314"></a><a name="b99547163314"></a>Default Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.29%" id="mcps1.2.5.1.3"><p id="p142901517413"><a name="p142901517413"></a><a name="p142901517413"></a><strong id="b58381455337"><a name="b58381455337"></a><a name="b58381455337"></a>Recommended Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61.47%" id="mcps1.2.5.1.4"><p id="p18290201244"><a name="p18290201244"></a><a name="p18290201244"></a><strong id="b63831861330"><a name="b63831861330"></a><a name="b63831861330"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1324110492312"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p2515684118"><a name="p2515684118"></a><a name="p2515684118"></a>acks</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p15661412"><a name="p15661412"></a><a name="p15661412"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p1157644113"><a name="p1157644113"></a><a name="p1157644113"></a><strong id="b1053809163318"><a name="b1053809163318"></a><a name="b1053809163318"></a>all</strong> (if high reliability mode is selected)</p>
<p id="p14596134120"><a name="p14596134120"></a><a name="p14596134120"></a><strong id="b58721414183310"><a name="b58721414183310"></a><a name="b58721414183310"></a>1</strong> (if high throughput mode is selected)</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p2518644110"><a name="p2518644110"></a><a name="p2518644110"></a>Indicates the number of acknowledgments the producer requires the server to return before considering a request complete. This controls the durability of records that are sent. The value of this parameter can be any of the following:</p>
<p id="p85961413"><a name="p85961413"></a><a name="p85961413"></a><strong id="b135751316394"><a name="b135751316394"></a><a name="b135751316394"></a>0</strong>: The producer will not wait for any acknowledgment from the server at all. The record will be immediately added to the socket buffer and considered sent. No guarantee can be made that the server has received the record, and the retries configuration will not take effect (as the client generally does not know of any failures). The offset given back for each record will always be set to –1.</p>
<p id="p165860414"><a name="p165860414"></a><a name="p165860414"></a><strong id="b83734357400"><a name="b83734357400"></a><a name="b83734357400"></a>1</strong>: The leader will write the record to its local log but will respond without waiting until receiving full acknowledgement from all followers. If the leader fails immediately after acknowledging the record but before the followers have replicated it, the record will be lost.</p>
<p id="p185168414"><a name="p185168414"></a><a name="p185168414"></a><strong id="b19708172917415"><a name="b19708172917415"></a><a name="b19708172917415"></a>all</strong>: The leader will wait for the full set of replicas to acknowledge the record. This is the strongest available guarantee because the record will not be lost even if there is just one replica that works.</p>
</td>
</tr>
<tr id="row192411349738"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p47126174110"><a name="p47126174110"></a><a name="p47126174110"></a>retries</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p17766134110"><a name="p17766134110"></a><a name="p17766134110"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p1772615419"><a name="p1772615419"></a><a name="p1772615419"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p199551521656"><a name="p199551521656"></a><a name="p199551521656"></a>Number of times that the client resends a message. Setting this parameter to a value greater than zero will cause the client to resend any record that failed to be sent.</p>
<p id="p27186124110"><a name="p27186124110"></a><a name="p27186124110"></a>Note that this retry is no different than if the client resent the record upon receiving the error. Allowing retries will potentially change the ordering of records because if two batches are sent to the same partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first.</p>
</td>
</tr>
<tr id="row82411449935"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p13714617415"><a name="p13714617415"></a><a name="p13714617415"></a>request.timeout.ms</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p157268417"><a name="p157268417"></a><a name="p157268417"></a>30000</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p107176114116"><a name="p107176114116"></a><a name="p107176114116"></a>Set as required.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p51852172917"><a name="p51852172917"></a><a name="p51852172917"></a>Indicates the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses, the client will throw a timeout exception.</p>
<p id="p197264416"><a name="p197264416"></a><a name="p197264416"></a>Setting this parameter to a large value, for example, <strong id="b770655212492"><a name="b770655212492"></a><a name="b770655212492"></a>120000</strong> (120s), can prevent records from failing to be sent in high-concurrency scenarios.</p>
</td>
</tr>
<tr id="row52417498310"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p673624112"><a name="p673624112"></a><a name="p673624112"></a>block.on.buffer.full</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p573654116"><a name="p573654116"></a><a name="p573654116"></a>TRUE</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p1274613414"><a name="p1274613414"></a><a name="p1274613414"></a>TRUE</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p370312258306"><a name="p370312258306"></a><a name="p370312258306"></a>Setting this parameter to <strong id="b5130154145310"><a name="b5130154145310"></a><a name="b5130154145310"></a>TRUE</strong> indicates that when buffer memory is exhausted, the producer must stop receiving new message records or throw an exception.</p>
<p id="p13726154115"><a name="p13726154115"></a><a name="p13726154115"></a>By default, this parameter is set to <strong id="b2232173235315"><a name="b2232173235315"></a><a name="b2232173235315"></a>TRUE</strong>. However, in some cases, non-blocking usage is desired and it is better to throw an exception immediately. Setting this parameter to <strong id="b165517503539"><a name="b165517503539"></a><a name="b165517503539"></a>FALSE</strong> will cause the producer to instead throw "BufferExhaustedException" when buffer memory is exhausted.</p>
</td>
</tr>
<tr id="row18241114912311"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p17717614115"><a name="p17717614115"></a><a name="p17717614115"></a>batch.size</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p7766104113"><a name="p7766104113"></a><a name="p7766104113"></a>16384</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p197186134117"><a name="p197186134117"></a><a name="p197186134117"></a>262144</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p973654111"><a name="p973654111"></a><a name="p973654111"></a>Default maximum number of bytes of messages that can be processed at a time. The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps improve performance of both the client and the server. No attempt will be made to batch records larger than this size.</p>
<p id="p1174684115"><a name="p1174684115"></a><a name="p1174684115"></a>Requests sent to brokers will contain multiple batches, one for each partition with data available to be sent.</p>
<p id="p671568418"><a name="p671568418"></a><a name="p671568418"></a>A smaller batch size will make batching less common and may reduce throughput (a batch size of zero will disable batching entirely). A larger batch size may use more memory as a buffer of the specified batch size will always be allocated in anticipation of additional records.</p>
</td>
</tr>
<tr id="row8241449034"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.2.5.1.1 "><p id="p97176104117"><a name="p97176104117"></a><a name="p97176104117"></a>buffer.memory</p>
</td>
<td class="cellrowborder" valign="top" width="10.459999999999999%" headers="mcps1.2.5.1.2 "><p id="p11746194120"><a name="p11746194120"></a><a name="p11746194120"></a>33554432</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.3 "><p id="p167156134112"><a name="p167156134112"></a><a name="p167156134112"></a>67108864</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.5.1.4 "><p id="p5736134116"><a name="p5736134116"></a><a name="p5736134116"></a>Total bytes of memory the producer can use to buffer records waiting to be sent to the server. If records are sent faster than they can be delivered to the broker, the producer will stop sending records or throw a "block.on.buffer.full" exception.</p>
<p id="p37146194115"><a name="p37146194115"></a><a name="p37146194115"></a>This setting should correspond roughly to the total memory the producer will use, but is not a rigid bound since not all memory the producer uses is used for buffering. Some additional memory will be used for compression (if compression is enabled) as well as for maintaining in-flight requests.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Consumer parameters

<a name="table1440709134014"></a>
<table><thead align="left"><tr id="row1840717954015"><th class="cellrowborder" valign="top" width="14.729999999999999%" id="mcps1.2.5.1.1"><p id="p9407209124010"><a name="p9407209124010"></a><a name="p9407209124010"></a><strong id="b1540709164018"><a name="b1540709164018"></a><a name="b1540709164018"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.86%" id="mcps1.2.5.1.2"><p id="p440759114010"><a name="p440759114010"></a><a name="p440759114010"></a><strong id="b74079994019"><a name="b74079994019"></a><a name="b74079994019"></a>Default Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.42%" id="mcps1.2.5.1.3"><p id="p7407119114014"><a name="p7407119114014"></a><a name="p7407119114014"></a><strong id="b940709184010"><a name="b940709184010"></a><a name="b940709184010"></a>Recommended Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61.99%" id="mcps1.2.5.1.4"><p id="p14071099406"><a name="p14071099406"></a><a name="p14071099406"></a><strong id="b14407139134017"><a name="b14407139134017"></a><a name="b14407139134017"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row84071794405"><td class="cellrowborder" valign="top" width="14.729999999999999%" headers="mcps1.2.5.1.1 "><p id="p55029339546"><a name="p55029339546"></a><a name="p55029339546"></a>auto.commit.enable</p>
</td>
<td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.5.1.2 "><p id="p155021633195419"><a name="p155021633195419"></a><a name="p155021633195419"></a>TRUE</p>
</td>
<td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.5.1.3 "><p id="p5502333165415"><a name="p5502333165415"></a><a name="p5502333165415"></a>FALSE</p>
</td>
<td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.5.1.4 "><p id="p12502633155418"><a name="p12502633155418"></a><a name="p12502633155418"></a>If this parameter is set to <strong id="b4776124065915"><a name="b4776124065915"></a><a name="b4776124065915"></a>TRUE</strong>, the offset of messages already fetched by the consumer will be periodically committed to ZooKeeper. This committed offset will be used when the process fails as the position from which the new consumer will begin.</p>
<p id="p850211335548"><a name="p850211335548"></a><a name="p850211335548"></a>Constraints: If this parameter is set to <strong id="b3574391301"><a name="b3574391301"></a><a name="b3574391301"></a>FALSE</strong>, to avoid message loss, an offset must be committed to ZooKeeper after the messages are successfully consumed.</p>
</td>
</tr>
<tr id="row1940711964018"><td class="cellrowborder" valign="top" width="14.729999999999999%" headers="mcps1.2.5.1.1 "><p id="p950363311540"><a name="p950363311540"></a><a name="p950363311540"></a>auto.offset.reset</p>
</td>
<td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.5.1.2 "><p id="p105031233165413"><a name="p105031233165413"></a><a name="p105031233165413"></a>latest</p>
</td>
<td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.5.1.3 "><p id="p45031833155412"><a name="p45031833155412"></a><a name="p45031833155412"></a>earliest</p>
</td>
<td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.5.1.4 "><p id="p20503203319543"><a name="p20503203319543"></a><a name="p20503203319543"></a>Indicates what to do when there is no initial offset in ZooKeeper or if the current offset has been deleted. Options:</p>
<p id="p1550316334542"><a name="p1550316334542"></a><a name="p1550316334542"></a><strong id="b1310954610"><a name="b1310954610"></a><a name="b1310954610"></a>earliest</strong>: The offset is automatically reset to the smallest offset.</p>
<p id="p750383375412"><a name="p750383375412"></a><a name="p750383375412"></a><strong id="b1762441818"><a name="b1762441818"></a><a name="b1762441818"></a>latest</strong>: The offset is automatically reset to the largest offset.</p>
<p id="p9503163313543"><a name="p9503163313543"></a><a name="p9503163313543"></a><strong id="b147537513110"><a name="b147537513110"></a><a name="b147537513110"></a>none</strong>: The system throws an exception to the consumer if no offset is available.</p>
<p id="p18503533145414"><a name="p18503533145414"></a><a name="p18503533145414"></a><strong id="b330418613112"><a name="b330418613112"></a><a name="b330418613112"></a>anything else</strong>: The system throws an exception to the consumer.</p>
</td>
</tr>
<tr id="row440789154011"><td class="cellrowborder" valign="top" width="14.729999999999999%" headers="mcps1.2.5.1.1 "><p id="p1150383325416"><a name="p1150383325416"></a><a name="p1150383325416"></a>connections.max.idle.ms</p>
</td>
<td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.5.1.2 "><p id="p2503173319543"><a name="p2503173319543"></a><a name="p2503173319543"></a>600000</p>
</td>
<td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.5.1.3 "><p id="p13503433205410"><a name="p13503433205410"></a><a name="p13503433205410"></a>30000</p>
</td>
<td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.5.1.4 "><p id="p1850373325411"><a name="p1850373325411"></a><a name="p1850373325411"></a>Indicates the timeout interval for an idle connection. The server closes the idle connection after this period of time ends. Setting this parameter to 30000 can reduce the server response failures when the network condition is poor.</p>
</td>
</tr>
</tbody>
</table>

