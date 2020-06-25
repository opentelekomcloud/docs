# Disk Types and Disk Performance<a name="en-us_topic_0014580744"></a>

EVS disk types are classified based on the disk I/O performance. EVS disk types differ in performance and price. Choose the disk type based on your requirements. The details are described as follows:

## Application Scenarios<a name="section44708501163538"></a>

-   Common I/O: EVS disks of this type deliver a maximum of 1,000 IOPS. This disk type is suitable for application scenarios that require large capacity, a medium read/write speed, and fewer transactions, such as enterprise office applications and small-scale testing.
-   High I/O: EVS disks of this type deliver a maximum of 3,000 IOPS and a minimum of 6 ms read/write latency. This disk type is designed to meet the needs of mainstream high-performance, high-reliability application scenarios, such as enterprise applications, large-scale development and testing, and web server logs.
-   Ultra-high I/O: EVS disks of this type deliver a maximum of 20,000 IOPS and a minimum of 1 ms read/write latency. This disk type is excellent for ultra-high I/O, ultra-high bandwidth, and read/write-intensive application scenarios, such as distributed file systems in HPC scenarios or NoSQL/RDS in I/O-intensive scenarios.
-   High I/O \(Performance optimized I\): EVS disks of this type deliver a maximum of 550 MB/s throughput, which is higher than high I/O EVS disks. They are cost-effective and provide higher performance, optimizing both IOPS and bandwidth. Such disks are particularly suitable for hybrid load scenarios consisting of online analytical processing \(OLAP\) and online transaction processing \(OLTP\) or consisting of large and small HPC files.
-   Ultra-high I/O \(Latency optimized\): EVS disks of this type deliver a maximum of 1 GB/s throughput and a minimum of 1 ms read/write latency. They can be used for enterprise key services, such as SAP HANA.

    >![](/images/icon-note.gif) **NOTE:**   
    >Currently, high I/O \(performance optimized I\) and ultra-high I/O \(latency optimized\) EVS disks can be attached to SAP HANA ECSs or HL1 ECSs only.  


## EVS Disk Performance<a name="section60833190213531"></a>

The key metrics of EVS disk performance include read/write I/O latency, IOPS, and throughput.

-   IOPS: Number of read/write operations performed by an EVS disk per second
-   Throughput: Amount of data successfully transmitted by an EVS disk per second, that is, the amount of data read from and written into an EVS disk
-   Read/write I/O latency: Minimum interval between two consecutive read/write operations of an EVS disk

**Table  1**  EVS disk performance data

<a name="table34437110213531"></a>
<table><thead align="left"><tr id="row5595843213531"><th class="cellrowborder" valign="top" width="19.740000000000002%" id="mcps1.2.7.1.1"><p id="p11059827213531"><a name="p11059827213531"></a><a name="p11059827213531"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.840000000000003%" id="mcps1.2.7.1.2"><p id="p23430785213531"><a name="p23430785213531"></a><a name="p23430785213531"></a>Common I/O</p>
</th>
<th class="cellrowborder" valign="top" width="13.150000000000004%" id="mcps1.2.7.1.3"><p id="p18845436213531"><a name="p18845436213531"></a><a name="p18845436213531"></a>High I/O</p>
</th>
<th class="cellrowborder" valign="top" width="15.230000000000002%" id="mcps1.2.7.1.4"><p id="p50085323213531"><a name="p50085323213531"></a><a name="p50085323213531"></a>Ultra-high I/O</p>
</th>
<th class="cellrowborder" valign="top" width="19.180000000000003%" id="mcps1.2.7.1.5"><p id="p30379351213531"><a name="p30379351213531"></a><a name="p30379351213531"></a>High I/O (Performance optimized I)</p>
</th>
<th class="cellrowborder" valign="top" width="17.860000000000003%" id="mcps1.2.7.1.6"><p id="p44808327213531"><a name="p44808327213531"></a><a name="p44808327213531"></a>Ultra-high I/O (Latency optimized)</p>
</th>
</tr>
</thead>
<tbody><tr id="row47459901213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p50610164213531"><a name="p50610164213531"></a><a name="p50610164213531"></a>IOPS per GB/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p5782658213531"><a name="p5782658213531"></a><a name="p5782658213531"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p65742164213531"><a name="p65742164213531"></a><a name="p65742164213531"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p10309230213531"><a name="p10309230213531"></a><a name="p10309230213531"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p29741339213531"><a name="p29741339213531"></a><a name="p29741339213531"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p60238248213531"><a name="p60238248213531"></a><a name="p60238248213531"></a>50</p>
</td>
</tr>
<tr id="row53970869213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p24485931213531"><a name="p24485931213531"></a><a name="p24485931213531"></a>Min. IOPS/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p37203360213531"><a name="p37203360213531"></a><a name="p37203360213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p60682161213531"><a name="p60682161213531"></a><a name="p60682161213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p16308040213531"><a name="p16308040213531"></a><a name="p16308040213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p45882826213531"><a name="p45882826213531"></a><a name="p45882826213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p25521441213531"><a name="p25521441213531"></a><a name="p25521441213531"></a>100</p>
</td>
</tr>
<tr id="row28446705213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p15975777213531"><a name="p15975777213531"></a><a name="p15975777213531"></a>Max. IOPS/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p18969562213531"><a name="p18969562213531"></a><a name="p18969562213531"></a>1,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p60139588213531"><a name="p60139588213531"></a><a name="p60139588213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p39468487213531"><a name="p39468487213531"></a><a name="p39468487213531"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p42830858213531"><a name="p42830858213531"></a><a name="p42830858213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p46747445213531"><a name="p46747445213531"></a><a name="p46747445213531"></a>30,000</p>
</td>
</tr>
<tr id="row56734862213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p54693757213531"><a name="p54693757213531"></a><a name="p54693757213531"></a>IOPS Burst Limit/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p1009300213531"><a name="p1009300213531"></a><a name="p1009300213531"></a>1,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p14644496213531"><a name="p14644496213531"></a><a name="p14644496213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p45353561213531"><a name="p45353561213531"></a><a name="p45353561213531"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p49759830213531"><a name="p49759830213531"></a><a name="p49759830213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p4014448213531"><a name="p4014448213531"></a><a name="p4014448213531"></a>15,000</p>
</td>
</tr>
<tr id="row60726385213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p40851714213531"><a name="p40851714213531"></a><a name="p40851714213531"></a>Max. Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p20654562213531"><a name="p20654562213531"></a><a name="p20654562213531"></a>40 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p62406843213531"><a name="p62406843213531"></a><a name="p62406843213531"></a>120 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p21789492213531"><a name="p21789492213531"></a><a name="p21789492213531"></a>320 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p20118389213531"><a name="p20118389213531"></a><a name="p20118389213531"></a>550 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p18976807213531"><a name="p18976807213531"></a><a name="p18976807213531"></a>1 GB/s</p>
</td>
</tr>
<tr id="row28952840213531"><td class="cellrowborder" valign="top" width="19.740000000000002%" headers="mcps1.2.7.1.1 "><p id="p9666559213531"><a name="p9666559213531"></a><a name="p9666559213531"></a>Read/write I/O latency</p>
<div class="note" id="note157542404113"><a name="note157542404113"></a><a name="note157542404113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5754840101115"><a name="p5754840101115"></a><a name="p5754840101115"></a>This parameter specifies the single-queue access latencies of EVS disks.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="14.840000000000003%" headers="mcps1.2.7.1.2 "><p id="p44793825213531"><a name="p44793825213531"></a><a name="p44793825213531"></a>10 ms to 15 ms</p>
</td>
<td class="cellrowborder" valign="top" width="13.150000000000004%" headers="mcps1.2.7.1.3 "><p id="p4421232213531"><a name="p4421232213531"></a><a name="p4421232213531"></a>6 ms to 10 ms</p>
</td>
<td class="cellrowborder" valign="top" width="15.230000000000002%" headers="mcps1.2.7.1.4 "><p id="p22575507213531"><a name="p22575507213531"></a><a name="p22575507213531"></a>1 ms to 3 ms</p>
</td>
<td class="cellrowborder" valign="top" width="19.180000000000003%" headers="mcps1.2.7.1.5 "><p id="p16676787213531"><a name="p16676787213531"></a><a name="p16676787213531"></a>6 ms to 10 ms</p>
</td>
<td class="cellrowborder" valign="top" width="17.860000000000003%" headers="mcps1.2.7.1.6 "><p id="p8642487213531"><a name="p8642487213531"></a><a name="p8642487213531"></a>1 ms</p>
</td>
</tr>
</tbody>
</table>

