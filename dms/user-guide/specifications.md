# Specifications<a name="EN-US_TOPIC_0201838023"></a>

## Kafka Queue Specifications<a name="en-us_topic_0159429488_section1616216232008"></a>

The network, storage, and computing resources of Kafka queues are managed by DMS. The resources allocated to each queue should be capable of meeting the concurrency and storage requirements of most services. If you have higher concurrency requirements, submit a service ticket for technical support.

To occupy isolated network, storage, and computing resources, use Kafka premium instances instead.

## Kafka Premium Instance Specifications<a name="en-us_topic_0159429488_section21958537463"></a>

Kafka premium instances are compatible with open-source Kafka 2.3.1. The instance specifications are classified based on bandwidth, including 100 MB/s, 300 MB/s, 600 MB/s, and 1,200 MB/s.

**Table  1**  TPS and maximum number of partitions supported by different instance specifications

<a name="en-us_topic_0159429488_table78751014154818"></a>
<table><thead align="left"><tr id="en-us_topic_0159429488_row887661474817"><th class="cellrowborder" valign="top" width="16.91169116911691%" id="mcps1.2.6.1.1"><p id="en-us_topic_0159429488_p187611474813"><a name="en-us_topic_0159429488_p187611474813"></a><a name="en-us_topic_0159429488_p187611474813"></a>Bandwidth</p>
</th>
<th class="cellrowborder" valign="top" width="19.79197919791979%" id="mcps1.2.6.1.2"><p id="en-us_topic_0159429488_p087601415481"><a name="en-us_topic_0159429488_p087601415481"></a><a name="en-us_topic_0159429488_p087601415481"></a>I/O Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.54235423542354%" id="mcps1.2.6.1.3"><p id="en-us_topic_0159429488_p7876121417484"><a name="en-us_topic_0159429488_p7876121417484"></a><a name="en-us_topic_0159429488_p7876121417484"></a>TPS (High-Throughput)</p>
</th>
<th class="cellrowborder" valign="top" width="21.53215321532153%" id="mcps1.2.6.1.4"><p id="en-us_topic_0159429488_p2876514144817"><a name="en-us_topic_0159429488_p2876514144817"></a><a name="en-us_topic_0159429488_p2876514144817"></a>TPS (Synchronous Replication)</p>
</th>
<th class="cellrowborder" valign="top" width="18.22182218221822%" id="mcps1.2.6.1.5"><p id="en-us_topic_0159429488_p473420062316"><a name="en-us_topic_0159429488_p473420062316"></a><a name="en-us_topic_0159429488_p473420062316"></a>Maximum Partitions</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0159429488_row14876161419486"><td class="cellrowborder" rowspan="2" valign="top" width="16.91169116911691%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p887611420481"><a name="en-us_topic_0159429488_p887611420481"></a><a name="en-us_topic_0159429488_p887611420481"></a>100 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="19.79197919791979%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p587641494812"><a name="en-us_topic_0159429488_p587641494812"></a><a name="en-us_topic_0159429488_p587641494812"></a>High I/O</p>
</td>
<td class="cellrowborder" valign="top" width="23.54235423542354%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p6876191454812"><a name="en-us_topic_0159429488_p6876191454812"></a><a name="en-us_topic_0159429488_p6876191454812"></a>100,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.53215321532153%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p13876214144813"><a name="en-us_topic_0159429488_p13876214144813"></a><a name="en-us_topic_0159429488_p13876214144813"></a>60,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.22182218221822%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0159429488_p1973490132315"><a name="en-us_topic_0159429488_p1973490132315"></a><a name="en-us_topic_0159429488_p1973490132315"></a>300</p>
</td>
</tr>
<tr id="en-us_topic_0159429488_row987671494818"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p14877191414814"><a name="en-us_topic_0159429488_p14877191414814"></a><a name="en-us_topic_0159429488_p14877191414814"></a>Ultra-high I/O</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p38771414124820"><a name="en-us_topic_0159429488_p38771414124820"></a><a name="en-us_topic_0159429488_p38771414124820"></a>100,000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p1787711464810"><a name="en-us_topic_0159429488_p1787711464810"></a><a name="en-us_topic_0159429488_p1787711464810"></a>80,000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p177341503239"><a name="en-us_topic_0159429488_p177341503239"></a><a name="en-us_topic_0159429488_p177341503239"></a>300</p>
</td>
</tr>
<tr id="en-us_topic_0159429488_row1987731414488"><td class="cellrowborder" rowspan="2" valign="top" width="16.91169116911691%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p158771145486"><a name="en-us_topic_0159429488_p158771145486"></a><a name="en-us_topic_0159429488_p158771145486"></a>300 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="19.79197919791979%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p81946616198"><a name="en-us_topic_0159429488_p81946616198"></a><a name="en-us_topic_0159429488_p81946616198"></a>High I/O</p>
</td>
<td class="cellrowborder" valign="top" width="23.54235423542354%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p1219412617194"><a name="en-us_topic_0159429488_p1219412617194"></a><a name="en-us_topic_0159429488_p1219412617194"></a>300,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.53215321532153%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p19194186201918"><a name="en-us_topic_0159429488_p19194186201918"></a><a name="en-us_topic_0159429488_p19194186201918"></a>150,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.22182218221822%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0159429488_p19734170132314"><a name="en-us_topic_0159429488_p19734170132314"></a><a name="en-us_topic_0159429488_p19734170132314"></a>900</p>
</td>
</tr>
<tr id="en-us_topic_0159429488_row1987711149481"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p919618691910"><a name="en-us_topic_0159429488_p919618691910"></a><a name="en-us_topic_0159429488_p919618691910"></a>Ultra-high I/O</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p8196186121912"><a name="en-us_topic_0159429488_p8196186121912"></a><a name="en-us_topic_0159429488_p8196186121912"></a>300,000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p141960610191"><a name="en-us_topic_0159429488_p141960610191"></a><a name="en-us_topic_0159429488_p141960610191"></a>200,000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p373400192312"><a name="en-us_topic_0159429488_p373400192312"></a><a name="en-us_topic_0159429488_p373400192312"></a>900</p>
</td>
</tr>
<tr id="en-us_topic_0159429488_row10877414124815"><td class="cellrowborder" valign="top" width="16.91169116911691%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p19877111424819"><a name="en-us_topic_0159429488_p19877111424819"></a><a name="en-us_topic_0159429488_p19877111424819"></a>600 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="19.79197919791979%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p6887132015"><a name="en-us_topic_0159429488_p6887132015"></a><a name="en-us_topic_0159429488_p6887132015"></a>Ultra-high I/O</p>
</td>
<td class="cellrowborder" valign="top" width="23.54235423542354%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p1088181172014"><a name="en-us_topic_0159429488_p1088181172014"></a><a name="en-us_topic_0159429488_p1088181172014"></a>600,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.53215321532153%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p1088417205"><a name="en-us_topic_0159429488_p1088417205"></a><a name="en-us_topic_0159429488_p1088417205"></a>300,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.22182218221822%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0159429488_p1973450182313"><a name="en-us_topic_0159429488_p1973450182313"></a><a name="en-us_topic_0159429488_p1973450182313"></a>1,800</p>
</td>
</tr>
<tr id="en-us_topic_0159429488_row1020392861910"><td class="cellrowborder" valign="top" width="16.91169116911691%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0159429488_p1320352841912"><a name="en-us_topic_0159429488_p1320352841912"></a><a name="en-us_topic_0159429488_p1320352841912"></a>1,200 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="19.79197919791979%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0159429488_p1841726206"><a name="en-us_topic_0159429488_p1841726206"></a><a name="en-us_topic_0159429488_p1841726206"></a>Ultra-high I/O</p>
</td>
<td class="cellrowborder" valign="top" width="23.54235423542354%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0159429488_p6842252018"><a name="en-us_topic_0159429488_p6842252018"></a><a name="en-us_topic_0159429488_p6842252018"></a>1.2 million</p>
</td>
<td class="cellrowborder" valign="top" width="21.53215321532153%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0159429488_p98420232017"><a name="en-us_topic_0159429488_p98420232017"></a><a name="en-us_topic_0159429488_p98420232017"></a>400,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.22182218221822%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0159429488_p187342062312"><a name="en-us_topic_0159429488_p187342062312"></a><a name="en-us_topic_0159429488_p187342062312"></a>1,800</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>For Kafka instances, the number of transactions per second \(TPS\) is the maximum number of messages that can be written per second. The preceding TPS is calculated with each message being 1 KB.  

## Specifying Bandwidth for Kafka Premium Instances<a name="en-us_topic_0159429488_section57651849164311"></a>

The bandwidth of a Kafka instance refers to the maximum read or write bandwidth. You are advised to select a bandwidth 30% higher than what is required.

-   100 MB/s

    Recommended for up to 3,000 client connections, 60 consumer groups, and 70 MB/s of service traffic.

-   300 MB/s

    Recommended for up to 10,000 client connections, 300 consumer groups, and 210 MB/s of service traffic.

-   600 MB/s

    Recommended for up to 20,000 client connections, 600 consumer groups, and 420 MB/s of service traffic.

-   1,200 MB/s

    Recommended for up to 20,000 client connections, 600 consumer groups, and 840 MB/s of service traffic.


## Specifying Storage Space for Kafka Premium Instances<a name="en-us_topic_0159429488_section2792821194417"></a>

Kafka premium instances support storage with 1 to 3 replicas. The storage space is the space consumed by all replicas. When creating an instance, specify its storage space based on the expected service message size and the number of replicas.

For example, if the estimated message size is 100 GB, the disk capacity must be at least: 100 GB x Number of replicas + 100 GB \(reserved\).

