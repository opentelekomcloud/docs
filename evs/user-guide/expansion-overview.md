# Expansion Overview<a name="evs_01_0006"></a>

## What Is Capacity Expansion?<a name="section1493121695811"></a>

If the capacity of an existing disk is insufficient, you can expand the disk capacity to increase the storage space.

Both system disks and data disks can be expanded. Currently, disk capacities can be expanded only. Capacity reduction is not supported.

## How to Expand the Disk Capacity?<a name="section173511542246"></a>

A capacity expansion operation includes the following steps:

1.  [Expand the disk capacity on the management console.](#section87622024418)
2.  [Log in to the server and extend the disk partition and file system.](#section487311389414)

**Figure  1**  Capacity expansion procedure<a name="fig76833489137"></a>  
![](figures/capacity-expansion-procedure.png "capacity-expansion-procedure")

## Expand the Disk Capacity on the Management Console<a name="section87622024418"></a>

Choose a proper expansion method based on the disk status. 

-   If the disk status is  **In-use**, the disk has been attached to a server. Check whether your disk can be expanded in the  **In-use**  state. For details, see  [Constraints](expanding-capacity-for-an-in-use-evs-disk.md#section158147122515).
    -   If yes, expand the disk capacity according to  [Expanding Capacity for an In-use EVS Disk](expanding-capacity-for-an-in-use-evs-disk.md).
    -   If no, detach the disk. Then, expand the capacity according to  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).

-   If the disk status is  **Available**, the disk is not attached to any server and can be expanded directly. For details, see  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).

## Log In to the Server and Extend the Disk Partition and File System<a name="section487311389414"></a>

After the disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly. You must log in to the server and extend the disk partition and file system. For details, see  [Table 1](#table458383431811).

**Table  1**  Extending the disk partition and file system

<a name="table458383431811"></a>
<table><thead align="left"><tr id="row3584153411812"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p17584123417187"><a name="p17584123417187"></a><a name="p17584123417187"></a>Capacity After Expansion</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p1858419349186"><a name="p1858419349186"></a><a name="p1858419349186"></a>Extend Disk Partition and File System</p>
</th>
</tr>
</thead>
<tbody><tr id="row15584133410181"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p20584234101814"><a name="p20584234101814"></a><a name="p20584234101814"></a>Disk capacity ≤2 TB</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul1792564894112"></a><a name="ul1792564894112"></a><ul id="ul1792564894112"><li>Windows: <a href="extending-disk-partitions-and-file-systems-(windows).md">Extending Disk Partitions and File Systems (Windows)</a></li><li>Linux: <a href="partition-and-file-system-extension-preparations-(linux).md">Partition and File System Extension Preparations (Linux)</a></li></ul>
</td>
</tr>
<tr id="row35841834121815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p185841834141811"><a name="p185841834141811"></a><a name="p185841834141811"></a>Disk capacity &gt;2 TB</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><a name="ul15171154910427"></a><a name="ul15171154910427"></a><ul id="ul15171154910427"><li>GPT partition style: <a href="extending-disk-partitions-and-file-systems-(windows).md">Extending Disk Partitions and File Systems (Windows)</a> or <a href="partition-and-file-system-extension-preparations-(linux).md">Partition and File System Extension Preparations (Linux)</a></li><li>MBR partition style: Not supported<p id="p7650194892910"><a name="p7650194892910"></a><a name="p7650194892910"></a>The maximum disk capacity that MBR supports is 2 TB, and the disk space exceeding 2 TB cannot be used. If your disk uses MBR and you need to expand the disk capacity to over 2 TB, change the partition style from MBR to GPT. Ensure that the disk data has been backed up before changing the partition style because services will be interrupted and data on the disk will be cleared during this change.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Related Operations<a name="section387117383196"></a>

For more expansion FAQs, see  [Disk Capacity Expansion FAQs](disk-capacity-expansion-faqs.md).

