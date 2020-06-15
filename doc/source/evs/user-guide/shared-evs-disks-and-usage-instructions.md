# Shared EVS Disks and Usage Instructions<a name="en-us_topic_0032860759"></a>

## What Are Shared EVS Disks<a name="section14853146154645"></a>

Shared EVS disks are block storage devices that support concurrent read/write operations and can be attached to multiple servers. Shared EVS disks feature multiple attachments, high-concurrency, high-performance, and high-reliability. They are usually used for enterprise key applications that require cluster deployment. Multiple servers can access the same shared EVS disk at the same time.

A shared EVS disk can be attached to a maximum of 16 servers. But if you simply attach a shared disk to multiple servers, files cannot be shared between the servers and data on the disk may be overwritten. You must deploy a shared file system or a cluster management system, such as Windows MSCS, Veritas VCS or CFS, to implement file sharing.

**Figure  1**  Application scenario of shared EVS disks<a name="fig186617301262"></a>  
![](figures/application-scenario-of-shared-evs-disks.png "application-scenario-of-shared-evs-disks")

## Usage Precautions<a name="section20091124154758"></a>

Most common clusters, such as Windows MSCS and Veritas VCS and CFS, require SCSI reservations. Therefore, you are advised to use shared SCSI EVS disks for clusters. If a SCSI EVS disk is attached to a Xen ECS for use, you must install the driver. For details, see  [Device Types and Usage Instructions](device-types-and-usage-instructions.md).

You can create shared VBD disks or shared SCSI disks. It is recommended that you attach the shared disk to the ECSs in the same ECS group to improve service reliability.

-   Shared VBD EVS disks: The device type of a newly created shared EVS disk is VBD by default. Such disks can be used as virtual block storage devices, but do not support SCSI reservations. If SCSI reservations are required for your applications, create shared SCSI EVS disks.
-   Shared SCSI EVS disks: These EVS disks support SCSI reservations.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >-   To improve data security, you are advised to use SCSI reservations together with the anti-affinity policy of an ECS group. That said, ensure that shared SCSI EVS disks are only attached to ECSs in the same anti-affinity ECS group.  
    >-   If an ECS does not belong to any anti-affinity ECS group, you are advised not to attach shared SCSI EVS disks to this ECS. Otherwise, SCSI reservations may not work properly, which may put your data at risk.  

    Concepts of the anti-affinity ECS group and SCSI reservations:

    -   The anti-affinity policy of an ECS group allows ECSs to be created on different physical servers to improve service reliability.

        For details about ECS groups, see  **Managing ECS Groups**  in the  _Elastic Cloud Server User Guide_.

    -   The SCSI reservation mechanism uses a SCSI reservation command to perform SCSI reservation operations. If an ECS sends such a command to an EVS disk, the disk is displayed as locked to other ECSs, preventing the data damage that may be caused by simultaneous read/write operations to the disk from multiple ECSs.
    -   ECS groups and SCSI reservations have the following relationship: A SCSI reservation on a single EVS disk cannot differentiate multiple ECSs on the same physical host. For that reason, if multiple ECSs that use the same shared EVS disk are running on the same physical host, SCSI reservations will not work properly. Therefore, you are advised to use SCSI reservations only on ECSs that are in the same ECS group, thus having a working anti-affinity policy. 


## Advantages<a name="section14238006154818"></a>

-   Multiple attachments: A shared EVS disk can be attached to a maximum of 16 servers.
-   High-performance: When multiple servers concurrently access a shared ultra-high I/O EVS disk, random read/write IOPS can reach up to 160,000.
-   High-reliability: Shared EVS disks support both manual and automatic backup, delivering highly reliable data storage.
-   Wide application scenarios: Shared EVS disks can be used for Linux RHCS clusters where only VBD EVS disks are needed. Whereas, they can also be used for Windows MSCS and Veritas VCS clusters that require SCSI reservations.

## Specifications and Performance<a name="section42854539155015"></a>

The key metrics of EVS disk performance include read/write I/O latency, IOPS, and throughput.

-   IOPS: Number of read/write operations performed by an EVS disk per second
-   Throughput: Amount of data successfully transmitted by an EVS disk per second, that is, the amount of data read from and written into an EVS disk
-   Read/write I/O latency: Minimum interval between two consecutive read/write operations of an EVS disk

**Table  1**  EVS disk performance data

<a name="table34437110213531"></a>
<table><thead align="left"><tr id="row5595843213531"><th class="cellrowborder" valign="top" width="19.998000199980005%" id="mcps1.2.7.1.1"><p id="p11059827213531"><a name="p11059827213531"></a><a name="p11059827213531"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.998500149985%" id="mcps1.2.7.1.2"><p id="p23430785213531"><a name="p23430785213531"></a><a name="p23430785213531"></a>Common I/O</p>
</th>
<th class="cellrowborder" valign="top" width="14.4985501449855%" id="mcps1.2.7.1.3"><p id="p18845436213531"><a name="p18845436213531"></a><a name="p18845436213531"></a>High I/O</p>
</th>
<th class="cellrowborder" valign="top" width="15.24847515248475%" id="mcps1.2.7.1.4"><p id="p50085323213531"><a name="p50085323213531"></a><a name="p50085323213531"></a>Ultra-high I/O</p>
</th>
<th class="cellrowborder" valign="top" width="18.258174182581744%" id="mcps1.2.7.1.5"><p id="p30379351213531"><a name="p30379351213531"></a><a name="p30379351213531"></a>High I/O (Performance optimized I)</p>
</th>
<th class="cellrowborder" valign="top" width="16.998300169983%" id="mcps1.2.7.1.6"><p id="p44808327213531"><a name="p44808327213531"></a><a name="p44808327213531"></a>Ultra-high I/O (Latency optimized)</p>
</th>
</tr>
</thead>
<tbody><tr id="row47459901213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p50610164213531"><a name="p50610164213531"></a><a name="p50610164213531"></a>IOPS per GB/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p5782658213531"><a name="p5782658213531"></a><a name="p5782658213531"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p65742164213531"><a name="p65742164213531"></a><a name="p65742164213531"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p10309230213531"><a name="p10309230213531"></a><a name="p10309230213531"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p29741339213531"><a name="p29741339213531"></a><a name="p29741339213531"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p60238248213531"><a name="p60238248213531"></a><a name="p60238248213531"></a>50</p>
</td>
</tr>
<tr id="row53970869213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p24485931213531"><a name="p24485931213531"></a><a name="p24485931213531"></a>Min. IOPS/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p37203360213531"><a name="p37203360213531"></a><a name="p37203360213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p60682161213531"><a name="p60682161213531"></a><a name="p60682161213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p16308040213531"><a name="p16308040213531"></a><a name="p16308040213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p45882826213531"><a name="p45882826213531"></a><a name="p45882826213531"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p25521441213531"><a name="p25521441213531"></a><a name="p25521441213531"></a>100</p>
</td>
</tr>
<tr id="row28446705213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p15975777213531"><a name="p15975777213531"></a><a name="p15975777213531"></a>Max. IOPS/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p18969562213531"><a name="p18969562213531"></a><a name="p18969562213531"></a>1,000</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p60139588213531"><a name="p60139588213531"></a><a name="p60139588213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p39468487213531"><a name="p39468487213531"></a><a name="p39468487213531"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p42830858213531"><a name="p42830858213531"></a><a name="p42830858213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p46747445213531"><a name="p46747445213531"></a><a name="p46747445213531"></a>30,000</p>
</td>
</tr>
<tr id="row56734862213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p54693757213531"><a name="p54693757213531"></a><a name="p54693757213531"></a>IOPS Burst Limit/EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p1009300213531"><a name="p1009300213531"></a><a name="p1009300213531"></a>1,000</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p14644496213531"><a name="p14644496213531"></a><a name="p14644496213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p45353561213531"><a name="p45353561213531"></a><a name="p45353561213531"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p49759830213531"><a name="p49759830213531"></a><a name="p49759830213531"></a>3,000</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p4014448213531"><a name="p4014448213531"></a><a name="p4014448213531"></a>15,000</p>
</td>
</tr>
<tr id="row60726385213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p40851714213531"><a name="p40851714213531"></a><a name="p40851714213531"></a>Max. Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p20654562213531"><a name="p20654562213531"></a><a name="p20654562213531"></a>40 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p62406843213531"><a name="p62406843213531"></a><a name="p62406843213531"></a>120 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p21789492213531"><a name="p21789492213531"></a><a name="p21789492213531"></a>320 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p20118389213531"><a name="p20118389213531"></a><a name="p20118389213531"></a>550 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p18976807213531"><a name="p18976807213531"></a><a name="p18976807213531"></a>1 GB/s</p>
</td>
</tr>
<tr id="row28952840213531"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.7.1.1 "><p id="p9666559213531"><a name="p9666559213531"></a><a name="p9666559213531"></a>Read/write I/O latency</p>
<div class="note" id="note157542404113"><a name="note157542404113"></a><a name="note157542404113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5754840101115"><a name="p5754840101115"></a><a name="p5754840101115"></a>This parameter specifies the single-queue access latencies of EVS disks.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="14.998500149985%" headers="mcps1.2.7.1.2 "><p id="p44793825213531"><a name="p44793825213531"></a><a name="p44793825213531"></a>10 ms to 15 ms</p>
</td>
<td class="cellrowborder" valign="top" width="14.4985501449855%" headers="mcps1.2.7.1.3 "><p id="p4421232213531"><a name="p4421232213531"></a><a name="p4421232213531"></a>6 ms to 10 ms</p>
</td>
<td class="cellrowborder" valign="top" width="15.24847515248475%" headers="mcps1.2.7.1.4 "><p id="p22575507213531"><a name="p22575507213531"></a><a name="p22575507213531"></a>1 ms to 3 ms</p>
</td>
<td class="cellrowborder" valign="top" width="18.258174182581744%" headers="mcps1.2.7.1.5 "><p id="p16676787213531"><a name="p16676787213531"></a><a name="p16676787213531"></a>6 ms to 10 ms</p>
</td>
<td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.7.1.6 "><p id="p8642487213531"><a name="p8642487213531"></a><a name="p8642487213531"></a>1 ms</p>
</td>
</tr>
<tr id="row148918911819"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p56066191782"><a name="p56066191782"></a><a name="p56066191782"></a>Number of <span id="text997610190"><a name="text997610190"></a><a name="text997610190"></a>servers</span> that can be attached to</p>
</td>
<td class="cellrowborder" colspan="5" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p56209191786"><a name="p56209191786"></a><a name="p56209191786"></a>A shared EVS disk can be attached to a maximum of 16 <span id="text289881421"><a name="text289881421"></a><a name="text289881421"></a>servers</span>.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   To test the performance of a shared disk, the following requirements must be met:  
>    -   The shared disk must be attached to multiple servers \(ECSs or BMSs\).  
>    -   If the shared disk is attached to multiple ECSs, these ECSs must belong to the same anti-affinity ECS group.  
>        If these ECSs fail to meet the anti-affinity requirement, the optimal performance of the shared disk cannot be achieved.  

## Data Sharing Principle and Common Usage Mistakes<a name="section23510620221927"></a>

A shared EVS disk is essentially the disk that can be attached to multiple servers for use, which is similar to a physical disk in that the disk can be attached to multiple physical servers, and each server can read data from and write data into any space on the disk. If the data read/write rules, such as the read/write sequence and meaning, between these servers are not defined, data read/write interference between servers or other unpredictable errors may occur.

Though shared EVS disks are block storage devices that provide shared access for servers, shared EVS disks do not have the cluster management capability. Therefore, you need to deploy a cluster system to manage shared EVS disks. Common cluster management systems include Windows MSCS, Linux RHCS, Veritas VCS, and Veritas CFS.

If shared EVS disks are not managed by a cluster system, the following issues may occur:

-   Data inconsistency caused by read/write conflicts

    When a shared EVS disk is attached to two servers \(server A and server B\), server A cannot recognize the disk spaces allocated to server B, vice versa. That said, a disk space allocated to server A may be already used by server B. In this case, repeated disk space allocation occurs, which leads to data errors.

    For example, a shared EVS disk has been formatted into the ext3 file system and attached to server A and server B. Server A has written metadata into the file system in space R and space G. Then server B has written metadata into space E and space G. In this case, the data written into space G by server A will be replaced. When the metadata in space G is read, an error will occur.

-   Data inconsistency caused by data caching

    When a shared EVS disk is attached to two servers \(server A and server B\), the application on server A has read the data in space R and space G, then cached the data. At that time, other processes and threads on server A would then read this data directly from the cache. At the same time, if the application on server B has modified the data in space R and space G, the application on server A cannot detect this data change and still reads this data from the cache. As a result, the user cannot view the modified data on server A.

    For example, a shared EVS disk has been formatted into the ext3 file system and attached to server A and server B. Both servers have cached the metadata in the file system. Then server A has created a new file \(file F\) on the shared disk, but server B cannot detect this modification and still reads data from its cached data. As a result, the user cannot view file F on server B.


Before you attach a shared EVS disk to multiple servers, the disk device type needs to be determined. The device type can be either VBD or SCSI. Shared SCSI EVS disks support SCSI reservations. Before using SCSI reservations, you need to install a driver in the server OS and ensure that the OS image is included in the compatibility list.

For details about the usages of shared EVS disks, see  [Managing a Shared EVS Disk](managing-a-shared-evs-disk.md).

>![](/images/icon-notice.gif) **NOTICE:**   
>If you simply attach a shared EVS disk to multiple servers, files cannot be shared between the servers as shared EVS disks do not have the cluster capability. Therefore, build a shared file system or deploy a cluster management system if you need to share files between servers.   

