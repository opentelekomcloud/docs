# Partition and File System Extension Preparations \(Linux\)<a name="evs_01_0035"></a>

Before extending the disk partition and file system, you must check the disk partition style and file system format, and then select the appropriate operation accordingly.

1.  To view the disk partition style, see the following methods:
    -   [Method 1: Check Partition Style and File System Format](#section45741613172812)
    -   [Method 2: Check Partition Style and File System Format](#section7627683297)

2.  To select the appropriate operation, see  [Disk Partition and File System Extension Scenarios](#section1136918160143).

## Method 1: Check Partition Style and File System Format<a name="section45741613172812"></a>

1.  <a name="li4640174163019"></a>Run the following command to view all the disks attached to the server:

    **lsblk**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  150G  0 disk
    └─vdb1 253:17   0  100G  0 part /mnt/sdc
    ```

    In this example, data disk  **/dev/vdb**  already has partition  **/dev/vdb1**  before capacity expansion, and the additional 50 GB added has not been allocated yet. Therefore,  **/dev/vdb**  has 150 GB, and  **/dev/vdb1**  has 100 GB.

2.  Run the following command to view the current disk partition style:

    **fdisk -l**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# fdisk -l
    
    Disk /dev/vda: 42.9 GB, 42949672960 bytes, 83886080 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x000bcb4e
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vda1   *        2048    83886079    41942016   83  Linux
    
    Disk /dev/vdb: 161.1 GB, 161061273600 bytes, 314572800 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x38717fc1
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vdb1            2048   209715199   104856576   83  Linux
    ```

    The value in the  **System**  column indicates the disk partition style. Value  **Linux**  indicates the MBR partition style. Value  **GPT**  indicates the GPT partition style.

    -   If the disk partitions displayed are inconsistent with those obtained in  [1](#li4640174163019), the partition that is not displayed uses the GPT partition style and has unallocated space. In this case, you cannot query all the partition information using the  **fdisk -l**  command. Go to  [Method 2: Check Partition Style and File System Format](#section7627683297).
    -   If the disk partitions displayed are consistent with those obtained in  [1](#li4640174163019), continue with the following operations.

3.  Run the following command to view the partition's file system format:

    **blkid** _Disk partition_

    In this example, run the following command:

    **blkid /dev/vdb1**

    In the command output, the  **TYPE**  value is  **ext4**, indicating that  **/dev/vdb1**'s file system format is  **ext4**.

4.  Run the following command to view the file system status:

    ext\*:  **e2fsck -n** _Disk partition_

    xfs:  **xfs\_repair -n** _Disk partition_

    In this example, the ext4 file system is used. Therefore, run the following command:

    **e2fsck -n /dev/vdb1**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# e2fsck -n /dev/vdb1
    e2fsck 1.42.9 (28-Dec-2013)
    Warning!  /dev/vdb1 is mounted.
    Warning: skipping journal recovery because doing a read-only filesystem check.
    /dev/vdb1: clean, 11/6553600 files, 459544/26214144 blocks
    ```

    If the file system status is  **clean**, the file system status is normal. Otherwise, rectify the faulty and then perform the capacity expansion.


## Method 2: Check Partition Style and File System Format<a name="section7627683297"></a>

1.  Run the following command to view all the disks attached to the server:

    **lsblk**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  150G  0 disk
    └─vdb1 253:17   0  100G  0 part /mnt/sdc
    ```

    In this example, data disk  **/dev/vdb**  already has partition  **/dev/vdb1**  before capacity expansion, and the additional 50 GB added has not been allocated yet. Therefore,  **/dev/vdb**  has 150 GB, and  **/dev/vdb1**  has 100 GB.

2.  Run the following command and enter  **p**  to view the disk partition style:

    **parted** _Disk_

    For example, run the following command to view  **/dev/vdb**'s partition style:

    **parted /dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# parted /dev/vdb
    GNU Parted 3.1
    Using /dev/vdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) p
    Error: The backup GPT table is not at the end of the disk, as it should be.  This might mean that another operating system believes the
    disk is smaller.  Fix, by moving the backup to the end (and removing the old backup)?
    Fix/Ignore/Cancel? Fix
    Warning: Not all of the space available to /dev/vdb appears to be used, you can fix the GPT to use all of the space (an extra 104857600
    blocks) or continue with the current setting?
    Fix/Ignore? Fix
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 161GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start   End    Size   File system  Name  Flags
     1      1049kB  107GB  107GB  ext4         test
    
    (parted) 
    ```

    In the command output, parameter  **Partition Table**  indicates the disk partition style. Value  **msdos**  indicates the MBR partition style, and value  **gpt**  indicates the GPT partition style.

    -   If the following error information is displayed, enter  **Fix**.

        ```
        Error: The backup GPT table is not at the end of the disk, as it should be.  This might mean that another operating system believes the
        disk is smaller.  Fix, by moving the backup to the end (and removing the old backup)?
        ```

        The GPT partition table information is stored at the start of the disk. To reduce the risk of damages, a backup of the information is saved at the end of the disk. When you expand the disk capacity, the end of the disk changes accordingly. In this case, enter  **Fix**  to move the backup file of the information to new disk end.

    -   If the following warning information is displayed, enter  **Fix**.

        ```
        Warning: Not all of the space available to /dev/vdb appears to be used, you can fix the GPT to use all of the space (an extra 104857600
        blocks) or continue with the current setting?
        Fix/Ignore? Fix
        ```

        Enter  **Fix**  as prompted. The system automatically sets the GPT partition style for the additional space.

3.  Enter  **q**  and press  **Enter**  to exit parted.

## Disk Partition and File System Extension Scenarios<a name="section1136918160143"></a>

**Table  1**  Disk partition and file system extension scenarios

<a name="table378248191411"></a>
<table><thead align="left"><tr id="row127801589149"><th class="cellrowborder" valign="top" width="10%" id="mcps1.2.6.1.1"><p id="p67805813143"><a name="p67805813143"></a><a name="p67805813143"></a>Disk</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.2"><p id="p197801817146"><a name="p197801817146"></a><a name="p197801817146"></a>Scenario</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.6.1.3"><p id="p07801289143"><a name="p07801289143"></a><a name="p07801289143"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.4"><p id="p1278058171417"><a name="p1278058171417"></a><a name="p1278058171417"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.6.1.5"><p id="p15780148151415"><a name="p15780148151415"></a><a name="p15780148151415"></a>Constraints</p>
</th>
</tr>
</thead>
<tbody><tr id="row83901751558"><td class="cellrowborder" rowspan="2" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p1390053558"><a name="p1390053558"></a><a name="p1390053558"></a>System disk</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="p86391164554"><a name="p86391164554"></a><a name="p86391164554"></a>Create a new MBR partition with the additional space.</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p9322120105510"><a name="p9322120105510"></a><a name="p9322120105510"></a><a href="extending-partitions-and-file-systems-for-system-disks-(linux).md#section9194153012119">Creating a New MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p730114243555"><a name="p730114243555"></a><a name="p730114243555"></a><a href="#li4674330102614">Services are not interrupted.</a></p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="36%" headers="mcps1.2.6.1.5 "><p id="p1058715298558"><a name="p1058715298558"></a><a name="p1058715298558"></a>An EVS system disk supports up to 1 TB (1024 GB). You can expand the capacity of a system disk to up to 1 TB.</p>
</td>
</tr>
<tr id="row5723127155520"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p563914165557"><a name="p563914165557"></a><a name="p563914165557"></a>Allocate the additional space to an existing MBR partition.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p16322220145511"><a name="p16322220145511"></a><a name="p16322220145511"></a><a href="extending-partitions-and-file-systems-for-system-disks-(linux).md#section143412109355">Extending an Existing MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8302142415518"><a name="p8302142415518"></a><a name="p8302142415518"></a><a href="#li132901912815">Whether services are interrupted is determined by the Linux kernel version.</a></p>
</td>
</tr>
<tr id="row1378110851412"><td class="cellrowborder" rowspan="4" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p13780384149"><a name="p13780384149"></a><a name="p13780384149"></a>Data disk</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.2 "><p id="p17807811417"><a name="p17807811417"></a><a name="p17807811417"></a>Create a new MBR partition with the additional space.</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1378058181415"><a name="p1378058181415"></a><a name="p1378058181415"></a><a href="extending-partitions-and-file-systems-for-data-disks-(linux).md#section20200028194016">Creating a New MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p278018141414"><a name="p278018141414"></a><a name="p278018141414"></a><a href="#li8782887145">Services are not interrupted.</a></p>
</td>
<td class="cellrowborder" rowspan="6" valign="top" width="36%" headers="mcps1.2.6.1.5 "><div class="p" id="p28915510213"><a name="p28915510213"></a><a name="p28915510213"></a>An EVS data disk supports up to 32 TB (32768 GB).<a name="ul899913613126"></a><a name="ul899913613126"></a><ul id="ul899913613126"><li>With MBR, the disk space exceeding 2 TB cannot be allocated and used, because the maximum disk capacity supported by MBR is 2 TB (2048 GB).<p id="p10243143610134"><a name="p10243143610134"></a><a name="p10243143610134"></a>In this case, if you want to expand the disk capacity to over 2 TB, change the partition style from MBR to GPT. Ensure that the disk data has been backed up before changing the partition style because services will be interrupted and data on the disk will be cleared during this change.</p>
</li></ul>
<a name="ul155151221015"></a><a name="ul155151221015"></a><ul id="ul155151221015"><li>With GPT, you can expand the capacity of a data disk to up to 32 TB.</li></ul>
</div>
</td>
</tr>
<tr id="row878119815141"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1378111851411"><a name="p1378111851411"></a><a name="p1378111851411"></a>Allocate the additional space to an existing MBR partition.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p67819814143"><a name="p67819814143"></a><a name="p67819814143"></a><a href="extending-partitions-and-file-systems-for-data-disks-(linux).md#section31113372194023">Extending an Existing MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p47818811414"><a name="p47818811414"></a><a name="p47818811414"></a><a href="#li069375552612">Services are interrupted.</a></p>
</td>
</tr>
<tr id="row278118171419"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p197816819146"><a name="p197816819146"></a><a name="p197816819146"></a>Create a new GPT partition with the additional space.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5781583147"><a name="p5781583147"></a><a name="p5781583147"></a><a href="extending-partitions-and-file-systems-for-data-disks-(linux).md#section15940163415487">Creating a New GPT Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p778128121410"><a name="p778128121410"></a><a name="p778128121410"></a><a href="#li8782887145">Services are not interrupted.</a></p>
</td>
</tr>
<tr id="row1678119810147"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p97811082149"><a name="p97811082149"></a><a name="p97811082149"></a>Allocate the additional space to an existing GPT partition.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p17819819145"><a name="p17819819145"></a><a name="p17819819145"></a><a href="extending-partitions-and-file-systems-for-data-disks-(linux).md#section13346184710300">Extending an Existing GPT Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p197811284148"><a name="p197811284148"></a><a name="p197811284148"></a><a href="#li069375552612">Services are interrupted.</a></p>
</td>
</tr>
<tr id="row515711531178"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="p1115814536170"><a name="p1115814536170"></a><a name="p1115814536170"></a>SCSI data disk</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p577312181820"><a name="p577312181820"></a><a name="p577312181820"></a>Create a new MBR partition with the additional space.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p19158185371717"><a name="p19158185371717"></a><a name="p19158185371717"></a><a href="extending-partitions-and-file-systems-for-scsi-disks-(linux).md#section12265143819280">Creating a New MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p20616228183"><a name="p20616228183"></a><a name="p20616228183"></a><a href="#li8782887145">Services are not interrupted.</a></p>
</td>
</tr>
<tr id="row544165520175"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p15771126185"><a name="p15771126185"></a><a name="p15771126185"></a>Allocate the additional space to an existing MBR partition.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p17442115501718"><a name="p17442115501718"></a><a name="p17442115501718"></a><a href="extending-partitions-and-file-systems-for-scsi-disks-(linux).md#section31113372194023">Extending an Existing MBR Partition</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p19714223187"><a name="p19714223187"></a><a name="p19714223187"></a><a href="#li069375552612">Services are interrupted.</a></p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>For a system disk:  
>-   <a name="li4674330102614"></a>If the additional space is used to create a new partition, existing partitions will not be affected, and services will not be interrupted.  
>-   <a name="li132901912815"></a>If the additional space is allocated to an existing partition, whether services are interrupted or not is determined by the Linux kernel version. When the kernel version is too early, the partition and file system extension takes effect only after a reboot. In this case, services will be interrupted. Otherwise, a reboot is not required, and services will not be interrupted.  
>For a data disk:  
>-   <a name="li8782887145"></a>If the additional space is used to create a new partition, existing partitions will not be affected, and services will not be interrupted. In scenarios where you want to expand data disks without interrupting services, create new partitions with the additional space.  
>-   <a name="li069375552612"></a>If the additional space is allocated to an existing partition, data on the disk will not be cleared but you must unmount the partition. In this case, services will be affected.  

