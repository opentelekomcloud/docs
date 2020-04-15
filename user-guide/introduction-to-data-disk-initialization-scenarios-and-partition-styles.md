# Introduction to Data Disk Initialization Scenarios and Partition Styles<a name="evs_01_0038"></a>

## Scenarios<a name="section3495606093050"></a>

After a disk is attached to a server, you need to log in to the server to initialize the disk, that is, format the disk. You must initialize a disk before accessing it.

-   System disk

    A system disk does not require manual initialization because it is automatically created and initialized upon server creation. The default disk partition style is master boot record \(MBR\).

-   Data disk

    -   If a data disk is created along with a server, it will be automatically attached to the server.
    -   If a data disk is created separately, you need to manually attach it to a server.

    In both cases, you must initialize the data disk before using it. Choose a proper disk partition style base on your service plan.


## Constraints<a name="section9329185781310"></a>

Disks created from backups or snapshots do not need to be initialized. Otherwise, data on the disks may be lost.

## Disk Partition Styles<a name="section216694193534"></a>

[Table 1](#table2729705994129)  lists the common disk partition styles. In Linux, different disk partition styles require different partitioning tools.

**Table  1**  Disk partition styles

<a name="table2729705994129"></a>
<table><thead align="left"><tr id="row2194811894129"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p2826869894129"><a name="p2826869894129"></a><a name="p2826869894129"></a>Disk Partition Style</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p806324094129"><a name="p806324094129"></a><a name="p806324094129"></a>Maximum Disk Capacity Supported</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.5.1.3"><p id="p4914271494129"><a name="p4914271494129"></a><a name="p4914271494129"></a>Maximum Number of Partitions Supported</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.4"><p id="p2113692194129"><a name="p2113692194129"></a><a name="p2113692194129"></a>Linux Partitioning Tool</p>
</th>
</tr>
</thead>
<tbody><tr id="row5601456494129"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1205045294213"><a name="p1205045294213"></a><a name="p1205045294213"></a>Master Boot Record (MBR)</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2342140694129"><a name="p2342140694129"></a><a name="p2342140694129"></a>2 TB</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.3 "><a name="ul21060408163037"></a><a name="ul21060408163037"></a><ul id="ul21060408163037"><li>4 primary partitions</li><li>3 primary partitions and 1 extended partition</li></ul>
<div class="p" id="p723613328428"><a name="p723613328428"></a><a name="p723613328428"></a>With MBR, one may create several primary partitions and an extended partition. An extended partition must be divided into several logical partitions before use. For example, if 6 partitions need to be created, you can create the partitions in the following two ways:<a name="ul6972172517474"></a><a name="ul6972172517474"></a><ul id="ul6972172517474"><li>3 primary partitions and 1 extended partition, with the extended partition divided into 3 logical partitions</li><li>1 primary partition and 1 extended partition, with the extended partition divided into 5 logical partitions</li></ul>
</div>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.4 "><a name="ul1160282695454"></a><a name="ul1160282695454"></a><ul id="ul1160282695454"><li>fdisk</li><li>parted</li></ul>
</td>
</tr>
<tr id="row3114938294129"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1278766394216"><a name="p1278766394216"></a><a name="p1278766394216"></a>Guid Partition Table (GPT)</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2460587094129"><a name="p2460587094129"></a><a name="p2460587094129"></a>18 EB</p>
<p id="p1993019393474"><a name="p1993019393474"></a><a name="p1993019393474"></a>1 EB = 1048576 TB</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.3 "><p id="p4691841694129"><a name="p4691841694129"></a><a name="p4691841694129"></a>Unlimited</p>
<p id="p12599114794712"><a name="p12599114794712"></a><a name="p12599114794712"></a>Disk partitions created using GPT are not categorized.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.4 "><p id="p4229536794129"><a name="p4229536794129"></a><a name="p4229536794129"></a>parted</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Because a data disk currently supports up to 32 TB, use the GPT partition style if your disk capacity is larger than 2 TB.  
>If you change the disk partition style after the disk has been used, the data on the disk will be cleared. Therefore, select a proper disk partition style when initializing the disk.  

