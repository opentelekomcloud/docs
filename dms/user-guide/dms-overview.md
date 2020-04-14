# DMS Overview<a name="EN-US_TOPIC_0143117116"></a>

DMS is a fully-managed, high-performance message queuing service that supports normal queues, first-in-first-out \(FIFO\) queues, Kafka queues, and Kafka premium instances. It is compatible with HTTP and TCP, and provides a flexible and reliable asynchronous communication mechanism for distributed applications.

Normal and FIFO queues feature low-latency and high reliability. They support dead letter messages for handling exceptions. In normal queues, partitions ensure higher concurrency.

Kafka queues support high-throughput and high-reliability modes. A Kafka queue is equivalent to a topic. The storage space and network bandwidth resources are allocated by the system, without requiring you to make choices.

Kafka premium instances use physically isolated computing, storage, and bandwidth resources. You can customize partitions and replicas for Kafka topics in the instances, and configure the network bandwidth as required. The instances can be used right out of the box, taking off the deployment and O&M pressure for you so that you can focus on developing your services.

For details about Kafka premium instances and Kafka queues, see  [Comparing Kafka Queues and Kafka Premium Instances](comparing-kafka-queues-and-kafka-premium-instances.md).

[Figure 1](#fig1370624315018)  illustrates the process of creating and retrieving a message.

**Figure  1**  Flowchart for creating and retrieving a message<a name="fig1370624315018"></a>  
![](figures/flowchart-for-creating-and-retrieving-a-message.png "flowchart-for-creating-and-retrieving-a-message")

**Table  1**  Steps for creating and retrieving a message

<a name="table61608233018"></a>
<table><thead align="left"><tr id="row1916014231709"><th class="cellrowborder" valign="top" width="8%" id="mcps1.2.3.1.1"><p id="p41612239013"><a name="p41612239013"></a><a name="p41612239013"></a>Step</p>
</th>
<th class="cellrowborder" valign="top" width="92%" id="mcps1.2.3.1.2"><p id="p141613231609"><a name="p141613231609"></a><a name="p141613231609"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12161223007"><td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.3.1.1 "><p id="p1916112231702"><a name="p1916112231702"></a><a name="p1916112231702"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="92%" headers="mcps1.2.3.1.2 "><p id="p128010208223"><a name="p128010208223"></a><a name="p128010208223"></a>The producer sends message M to a queue.</p>
<p id="p131612231108"><a name="p131612231108"></a><a name="p131612231108"></a>Message M is redundantly distributed in the queue.</p>
</td>
</tr>
<tr id="row1516118236015"><td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.3.1.1 "><p id="p9161162310012"><a name="p9161162310012"></a><a name="p9161162310012"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="92%" headers="mcps1.2.3.1.2 "><p id="p15161122319015"><a name="p15161122319015"></a><a name="p15161122319015"></a>A consumer retrieves message M from the queue.</p>
<p id="p176301136144618"><a name="p176301136144618"></a><a name="p176301136144618"></a>While message M is being retrieved, it remains in the queue. It cannot be retrieved again within 30s since the start of retrieval. If message M fails to be acknowledged within this period, it can be retrieved again.</p>
</td>
</tr>
<tr id="row11161623709"><td class="cellrowborder" valign="top" width="8%" headers="mcps1.2.3.1.1 "><p id="p4161923501"><a name="p4161923501"></a><a name="p4161923501"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="92%" headers="mcps1.2.3.1.2 "><p id="p786220194720"><a name="p786220194720"></a><a name="p786220194720"></a>Once message M is acknowledged, it can no longer be retrieved by consumers from the same consumer group.</p>
<p id="p20756113832712"><a name="p20756113832712"></a><a name="p20756113832712"></a>However, it can still be retrieved by consumers from other consumer groups. It remains in the queue for at least 72 hours (unless the queue is deleted) and will be deleted after this period.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If messages are retrieved using APIs, they must then be acknowledged using the ACK API. If messages are retrieved using the DMS console, they are automatically acknowledged.  

As shown in  [Figure 2](#fig16851144592920), DMS stores messages of a queue on different servers, and each message has multiple replicas, achieving high reliability and availability.

**Figure  2**  Distribution of messages from a queue<a name="fig16851144592920"></a>  
![](figures/distribution-of-messages-from-a-queue.png "distribution-of-messages-from-a-queue")

Message queues have the following characteristics:

-   Ordered message delivery

    Normal queues support higher concurrency, but cannot guarantee that messages are retrieved in the exact sequence as how they are received. If you want to preserve the message sequence, put sequence information in each message, so that messages can be sequenced after they are received.

    FIFO queues support FIFO message delivery and are applicable to scenarios with high sequence requirements.

-   At-least-once delivery

    In rare cases, a server storing message replicas may be unavailable when you request or delete messages. If this happens, the message replicas will not be deleted from that server and may be sent when the connection is restored.

    This is called "at-least-once" delivery. To avoid any adverse impact from processing the same message multiple times, ensure that your application processes messages idempotently.

-   A specified number of messages cannot be obtained at a time when there are only a few messages in a queue.

    When there are only a few messages in a queue, the number of messages retrieved at a time may be less than the message quantity specified in the retrieval request. However, all messages in the queue will eventually be obtained by the consumer after multiple rounds of retrieval.


