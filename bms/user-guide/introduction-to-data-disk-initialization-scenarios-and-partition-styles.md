# Introduction to Data Disk Initialization Scenarios and Partition Styles<a name="EN-US_TOPIC_0157011194"></a>

## Scenarios<a name="en-us_topic_0085245975_section3495606093050"></a>

After a disk is attached to a BMS, you need to log in to the BMS to initialize \(format\) the disk before you can use the disk properly.

-   System disk

    A system disk does not need to be initialized because it is automatically created and initialized during the BMS creation. The default disk partition style is master boot record \(MBR\).

-   Data disk

    -   If a data disk is created during the BMS creation, it will be automatically attached to the BMS.
    -   If a data disk is created explicitly, you need to manually attach the data disk to the BMS.

    In both cases, the data disk can only be used after it is initialized. Choose a proper disk partition style based on your service plans.


## Disk Partition Style<a name="en-us_topic_0085245975_section216694193534"></a>

[Table 1](#en-us_topic_0085245975_table2729705994129)  lists the common disk partition styles. For Linux OSs, different disk partition styles require different partitioning tools.

**Table  1**  Disk partition styles

<a name="en-us_topic_0085245975_table2729705994129"></a>
<table><thead align="left"><tr id="en-us_topic_0085245975_row2194811894129"><th class="cellrowborder" valign="top" width="25.187481251874814%" id="mcps1.2.5.1.1"><p id="en-us_topic_0085245975_p2826869894129"><a name="en-us_topic_0085245975_p2826869894129"></a><a name="en-us_topic_0085245975_p2826869894129"></a>Disk Partition Style</p>
</th>
<th class="cellrowborder" valign="top" width="21.617838216178384%" id="mcps1.2.5.1.2"><p id="en-us_topic_0085245975_p806324094129"><a name="en-us_topic_0085245975_p806324094129"></a><a name="en-us_topic_0085245975_p806324094129"></a>Maximum Disk Capacity Supported</p>
</th>
<th class="cellrowborder" valign="top" width="31.576842315768427%" id="mcps1.2.5.1.3"><p id="en-us_topic_0085245975_p4914271494129"><a name="en-us_topic_0085245975_p4914271494129"></a><a name="en-us_topic_0085245975_p4914271494129"></a>Maximum Number of Partitions Supported</p>
</th>
<th class="cellrowborder" valign="top" width="21.617838216178384%" id="mcps1.2.5.1.4"><p id="en-us_topic_0085245975_p2113692194129"><a name="en-us_topic_0085245975_p2113692194129"></a><a name="en-us_topic_0085245975_p2113692194129"></a>Linux Partitioning Tool</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085245975_row5601456494129"><td class="cellrowborder" valign="top" width="25.187481251874814%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085245975_p1205045294213"><a name="en-us_topic_0085245975_p1205045294213"></a><a name="en-us_topic_0085245975_p1205045294213"></a>Master Boot Record (MBR)</p>
</td>
<td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085245975_p2342140694129"><a name="en-us_topic_0085245975_p2342140694129"></a><a name="en-us_topic_0085245975_p2342140694129"></a>2 TB</p>
</td>
<td class="cellrowborder" valign="top" width="31.576842315768427%" headers="mcps1.2.5.1.3 "><a name="en-us_topic_0085245975_ul21060408163037"></a><a name="en-us_topic_0085245975_ul21060408163037"></a><ul id="en-us_topic_0085245975_ul21060408163037"><li>4 primary partitions</li><li>3 primary partitions and 1 extended partition</li></ul>
<p id="en-us_topic_0085245975_p1497092163448"><a name="en-us_topic_0085245975_p1497092163448"></a><a name="en-us_topic_0085245975_p1497092163448"></a>With the MBR partition style, primary partitions and an extended partition can be included, where the extended partition can contain several logical partitions. For example, if 6 partitions need to be created, you can create the partitions in the following two ways:</p>
<a name="en-us_topic_0085245975_ul6972172517474"></a><a name="en-us_topic_0085245975_ul6972172517474"></a><ul id="en-us_topic_0085245975_ul6972172517474"><li>3 primary partitions and 1 extended partition, with the extended partition containing 3 logical partitions</li><li>1 primary partition and 1 extended partition, with the extended partition containing 5 logical partitions</li></ul>
</td>
<td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0085245975_ul1160282695454"></a><a name="en-us_topic_0085245975_ul1160282695454"></a><ul id="en-us_topic_0085245975_ul1160282695454"><li>fdisk</li><li>parted</li></ul>
</td>
</tr>
<tr id="en-us_topic_0085245975_row3114938294129"><td class="cellrowborder" valign="top" width="25.187481251874814%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085245975_p1278766394216"><a name="en-us_topic_0085245975_p1278766394216"></a><a name="en-us_topic_0085245975_p1278766394216"></a>Guid Partition Table (GPT)</p>
</td>
<td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085245975_p2460587094129"><a name="en-us_topic_0085245975_p2460587094129"></a><a name="en-us_topic_0085245975_p2460587094129"></a>18 EB</p>
<p id="en-us_topic_0085245975_p1993019393474"><a name="en-us_topic_0085245975_p1993019393474"></a><a name="en-us_topic_0085245975_p1993019393474"></a>1 EB = 1048576 TB</p>
</td>
<td class="cellrowborder" valign="top" width="31.576842315768427%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085245975_p4691841694129"><a name="en-us_topic_0085245975_p4691841694129"></a><a name="en-us_topic_0085245975_p4691841694129"></a>Unlimited</p>
<p id="en-us_topic_0085245975_p12599114794712"><a name="en-us_topic_0085245975_p12599114794712"></a><a name="en-us_topic_0085245975_p12599114794712"></a>Disk partitions allocated using GPT are not categorized.</p>
</td>
<td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0085245975_p4229536794129"><a name="en-us_topic_0085245975_p4229536794129"></a><a name="en-us_topic_0085245975_p4229536794129"></a>parted</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Currently, an EVS data disk supports up to 32 TB. Therefore, use the GPT partition style if your disk capacity is greater than 2 TB.  
>If you change the disk partition style after the disk has been used, the original data on the disk will be cleared. Therefore, select a proper disk partition style when initializing the disk.  

