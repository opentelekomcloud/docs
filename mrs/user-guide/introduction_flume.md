# Introduction<a name="EN-US_TOPIC_0125375571"></a>

## Process<a name="s37097284a2a3481082de105ab2a6f40e"></a>

The process for collecting logs using Flume is as follows:

1.  Install the Flume client.
2.  Configure the Flume server and client parameters.
3.  Collect and query logs using the Flume client.
4.  Stop and uninstall the Flume client.

## Flume Client<a name="s3d61c39943394733ac83a5ace60a8db6"></a>

A Flume client consists of the source, channel, and sink. The source sends the data to the channel, and then the sink transmits the data from the channel to the external device.

**Table  1**  Module description

<a name="tbabfdc7cc86e4a41816ca02a8b4c50be"></a>
<table><thead align="left"><tr id="en-us_topic_0066459129_row5952094"><th class="cellrowborder" valign="top" width="12.35%" id="mcps1.2.3.1.1"><p id="en-us_topic_0066459129_p12357643"><a name="en-us_topic_0066459129_p12357643"></a><a name="en-us_topic_0066459129_p12357643"></a><strong id="abfd4d2df86dc488ebed4ff1ec8861813"><a name="abfd4d2df86dc488ebed4ff1ec8861813"></a><a name="abfd4d2df86dc488ebed4ff1ec8861813"></a>Module</strong></p>
</th>
<th class="cellrowborder" valign="top" width="87.64999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0066459129_p16134234"><a name="en-us_topic_0066459129_p16134234"></a><a name="en-us_topic_0066459129_p16134234"></a><strong id="en-us_topic_0066459129_b10990381"><a name="en-us_topic_0066459129_b10990381"></a><a name="en-us_topic_0066459129_b10990381"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0066459129_row17805683"><td class="cellrowborder" valign="top" width="12.35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0066459129_p32974225"><a name="en-us_topic_0066459129_p32974225"></a><a name="en-us_topic_0066459129_p32974225"></a>Source</p>
</td>
<td class="cellrowborder" valign="top" width="87.64999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0066459129_p53666608"><a name="en-us_topic_0066459129_p53666608"></a><a name="en-us_topic_0066459129_p53666608"></a>A source receives or generates data and sends the data to one&nbsp;or&nbsp;more channels. Sources can work in either data-driven or polling mode.</p>
<p id="en-us_topic_0066459129_p13237432"><a name="en-us_topic_0066459129_p13237432"></a><a name="en-us_topic_0066459129_p13237432"></a>Typical sources include:</p>
<a name="en-us_topic_0066459129_ul52028024"></a><a name="en-us_topic_0066459129_ul52028024"></a><ul id="en-us_topic_0066459129_ul52028024"><li>Syslog and Netcat, which are integrated in the system to receive data</li><li>Exec and SEQ that generate event data automatically</li><li>Avro that is used for communication between agents</li></ul>
<p id="aa0ff7ec8cc9647c8a75ba5b771ba9052"><a name="aa0ff7ec8cc9647c8a75ba5b771ba9052"></a><a name="aa0ff7ec8cc9647c8a75ba5b771ba9052"></a>A source must be associated with at least one channel.</p>
</td>
</tr>
<tr id="en-us_topic_0066459129_row26121765"><td class="cellrowborder" valign="top" width="12.35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0066459129_p35488221"><a name="en-us_topic_0066459129_p35488221"></a><a name="en-us_topic_0066459129_p35488221"></a>Channel</p>
</td>
<td class="cellrowborder" valign="top" width="87.64999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0066459129_p55973666"><a name="en-us_topic_0066459129_p55973666"></a><a name="en-us_topic_0066459129_p55973666"></a>A channel is used to buffer data between a source and a sink. After the sink transmits the data to the next channel or the destination, the cache is deleted automatically.</p>
<p id="en-us_topic_0066459129_p34000948"><a name="en-us_topic_0066459129_p34000948"></a><a name="en-us_topic_0066459129_p34000948"></a>The persistency of the channels varies with the channel types:</p>
<a name="en-us_topic_0066459129_ul37573083"></a><a name="en-us_topic_0066459129_ul37573083"></a><ul id="en-us_topic_0066459129_ul37573083"><li>Memory channel: no persistency</li><li>File channel: persistency implemented based on write-ahead logging (WAL)</li><li>JDBC channel: persistency implemented based on the embedded database</li></ul>
<p id="en-us_topic_0066459129_p26143179"><a name="en-us_topic_0066459129_p26143179"></a><a name="en-us_topic_0066459129_p26143179"></a>Channels support the transaction feature to ensure simple sequential operations. A channel can work with sources and sinks of any quantity.</p>
</td>
</tr>
<tr id="en-us_topic_0066459129_row33962021"><td class="cellrowborder" valign="top" width="12.35%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0066459129_p66569185"><a name="en-us_topic_0066459129_p66569185"></a><a name="en-us_topic_0066459129_p66569185"></a>Sink</p>
</td>
<td class="cellrowborder" valign="top" width="87.64999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0066459129_p23394901"><a name="en-us_topic_0066459129_p23394901"></a><a name="en-us_topic_0066459129_p23394901"></a>A sink transmits data to the next hop or destination. After the transmission is complete, it deletes the data from the channel.</p>
<p id="en-us_topic_0066459129_p9227524"><a name="en-us_topic_0066459129_p9227524"></a><a name="en-us_topic_0066459129_p9227524"></a>Typical sinks include:</p>
<a name="en-us_topic_0066459129_ul15938858"></a><a name="en-us_topic_0066459129_ul15938858"></a><ul id="en-us_topic_0066459129_ul15938858"><li>HDFS and Kafka that store data to the destination</li><li>Null sink that automatically consumes the data</li><li>Avro that is used for communication between agents</li></ul>
<p id="en-us_topic_0066459129_p19242262"><a name="en-us_topic_0066459129_p19242262"></a><a name="en-us_topic_0066459129_p19242262"></a>A sink must be associated with at least one channel.</p>
</td>
</tr>
</tbody>
</table>

A Flume client can have multiple sources, channels, and sinks. A source can send data to multiple channels, and then multiple sinks send the data out of the client.

Multiple Flume clients can be cascaded. That is, a sink can send data to the source of another client.

## Supplementary Information<a name="s0e65d9f51a9f4b949e151abe09ab5899"></a>

1.  What are the reliability measures of Flume?
    -   The transaction mechanism is implemented between sources and channels, and between channels and sinks.
    -   The sink processor supports failover and load balancing.

        The following is an example of the load balancing configuration:

        ```
        server.sinkgroups=g1
        server.sinkgroups.g1.sinks=k1 k2
        server.sinkgroups.g1.processor.type=load_balance
        server.sinkgroups.g1.processor.backoff=true
        server.sinkgroups.g1.processor.selector=random
        ```



1.  What are the precautions for the aggregation and cascading of multiple Flume clients?
    -   Use the Avro or Thrift protocol for cascading.
    -   When the aggregation end contains multiple nodes, evenly distribute the clients to these nodes. Do not connect all the clients to a single node.


