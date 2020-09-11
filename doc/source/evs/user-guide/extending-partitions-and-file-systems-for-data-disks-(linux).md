# Extending Partitions and File Systems for Data Disks \(Linux\)<a name="evs_01_0109"></a>

## Scenarios<a name="section4385650719406"></a>

After a disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly.

In Linux, you must allocate the additional space to an existing partition or a new partition. This topic uses CentOS 7.4 64bit as the sample OS to describe how to extend an MBR or GPT partition. The method for allocating the additional space varies depending on the server OS. This document is used for reference only. For the detailed operations and differences, see the corresponding OS documents.

-   [Creating a New MBR Partition](#section20200028194016)
-   [Extending an Existing MBR Partition](#section31113372194023)
-   [Creating a New GPT Partition](#section15940163415487)
-   [Extending an Existing GPT Partition](#section13346184710300)

>![](/images/icon-notice.gif) **NOTICE:**   
>Performing the expansion operations with caution. Misoperation may lead to data loss or exceptions. Therefore, you are advised to back up the disk data using backups or snapshots before expansion. For details about backups and snapshots, see  [Managing EVS Backup](managing-evs-backup.md)  and  [Creating a Snapshot](creating-a-snapshot.md), respectively.  

## Prerequisites<a name="section19088989195835"></a>

-   You have expanded the disk capacity and attached the disk to a server on the management console. For details, see  [Expanding Capacity for an In-use EVS Disk](expanding-capacity-for-an-in-use-evs-disk.md)  or  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).
-   You have logged in to the server.
    -   For how to log in to an ECS, see the  _Elastic Cloud Server User Guide_.
    -   For how to log in to a BMS, see the  _Bare Metal Server User Guide_.


## Creating a New MBR Partition<a name="section20200028194016"></a>

Originally, data disk  **/dev/vdb**  has 100 GB and one partition \(**/dev/vdb1**\), and then 50 GB is added to the disk. The following procedure shows you how to create a new MBR partition  **/dev/vdb2**  with this 50 GB.

1.  Run the following command to view the disk partition information:

    **fdisk** **-l**

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

2.  Run the following command to enter fdisk:

    **fdisk** _Disk_

    In this example, run the following command:

    **fdisk** **/dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# fdisk /dev/vdb
    Welcome to fdisk (util-linux 2.23.2).
    
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    
    Command (m for help): 
    ```

3.  Enter  **n**  and press  **Enter**  to create a new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): n
    Partition type:
       p   primary (1 primary, 0 extended, 3 free)
       e   extended
    Select (default p):
    ```

    There are two types of disk partitions:

    -   Choosing  **p**  creates a primary partition.
    -   Choosing  **e**  creates an extended partition.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the MBR partition style is used, a maximum of 4 primary partitions, or 3 primary partitions and 1 extended partition can be created. The extended partition cannot be used directly and must be divided into logical partitions before use.  
    >Disk partitions created using GPT are not categorized.  

4.  In this example, a primary partition is created. Therefore, enter  **p**  and press  **Enter**  to create a primary partition.

    Information similar to the following is displayed:

    ```
    Select (default p): p
    Partition number (2-4, default 2):
    ```

    **Partition number**  indicates the serial number of the primary partition. Because partition number 1 has been used, the value ranges from  **2**  to  **4**.

5.  Enter the serial number of the primary partition and press  **Enter**. Partition number  **2**  is used in this example. Therefore, enter  **2**  and press  **Enter.**

    Information similar to the following is displayed:

    ```
    Partition number (2-4, default 2): 2
    First sector (209715200-314572799, default 209715200):
    ```

    **First sector**  indicates the start sector. The value ranges from  **209715200**  to  **314572799**, and the default value is  **209715200**.

6.  Enter the new partition's start sector and press  **Enter**. In this example, the default start sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    First sector (209715200-314572799, default 209715200):
    Using default value 209715200
    Last sector, +sectors or +size{K,M,G} (209715200-314572799, default 314572799):
    ```

    **Last sector**  indicates the end sector. The value ranges from  **209715200**  to  **314572799**, and the default value is  **314572799**.

7.  Enter the new partition's end sector and press  **Enter**. In this example, the default end sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    Last sector, +sectors or +size{K,M,G} (209715200-314572799, default 314572799):
    Using default value 314572799
    Partition 2 of type Linux and of size 50 GiB is set
    
    Command (m for help): 
    ```

8.  Enter  **p**  and press  **Enter**  to view the new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/vdb: 161.1 GB, 161061273600 bytes, 314572800 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x38717fc1
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vdb1            2048   209715199   104856576   83  Linux
    /dev/vdb2       209715200   314572799    52428800   83  Linux
    
    Command (m for help): 
    ```

9.  Enter  **w**  and press  **Enter**  to write the changes to the partition table.

    Information similar to the following is displayed:

    ```
    Command (m for help): w
    The partition table has been altered!
    
    Calling ioctl() to re-read partition table.
    
    WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
    The kernel still uses the old table. The new table will be used at
    the next reboot or after you run partprobe(8) or kpartx(8)
    Syncing disks.
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

10. Run the following command to synchronize the new partition table to the OS:

    **partprobe**

11. Run the following command to set the file system format for the new partition:

    **mkfs** **-t** _File system_ _Disk partition_

    In this example, run the following command:

    **mkfs** **-t** **ext4** **/dev/vdb2**

    >![](/images/icon-note.gif) **NOTE:**   
    >The procedure for setting the  **xfs**  file system is the same as that for the  **ext**_\*_  file system. The command for creating the  **xfs**  file system is  **mkfs** **-t** **xfs** **/dev/vdb2**.  

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# mkfs -t ext4 /dev/vdb2
    mke2fs 1.42.9 (28-Dec-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    3276800 inodes, 13107200 blocks
    655360 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=2162163712
    400 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
            4096000, 7962624, 11239424
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    The formatting takes a while, and you need to observe the system running status. Once  **done**  is displayed in the command output, the formatting is complete.

12. \(Optional\) Run the following command to create a mount point:

    Perform this step if you want to mount the partition on a new mount point.

    **mkdir** _Mount point_

    In this example, run the following command to create the  **/mnt/test**  mount point:

    **mkdir** **/mnt/test**

13. Run the following command to mount the new partition:

    **mount** _Disk partition_ _Mount point_

    In this example, run the following command to mount the new partition  **/dev/vdb2**  on  **/mnt/test**:

    **mount** **/dev/vdb2** **/mnt/test**

    >![](/images/icon-note.gif) **NOTE:**   
    >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

14. Run the following command to view the mount result:

    **df** **-TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  1.9G   39G   5% /
    devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
    tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
    tmpfs          tmpfs     2.0G  9.1M  2.0G   1% /run
    tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs          tmpfs     398M     0  398M   0% /run/user/0
    /dev/vdb1      ext4      106G   63M  101G   1% /mnt/sdc
    /dev/vdb2      ext4       53G   55M   50G   1% /mnt/test
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Extending an Existing MBR Partition<a name="section31113372194023"></a>

Originally, data disk  **/dev/vdb**  has 150 GB and two partitions \(**/dev/vdb1**  and  **/dev/vdb2**, and then 80 GB is added to the disk. The following procedure shows you how to add this 80 GB to the existing MBR partition  **/dev/vdb2**.

>![](/images/icon-notice.gif) **NOTICE:**   
>During an expansion, the additional space is added to the end of the disk. Therefore, if the disk has multiple partitions, the additional space can only be allocated to the partition at the disk end.  

1.  <a name="li6396237219479"></a>Run the following command to view the disk partition information:

    **fdisk** **-l**

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
    
    Disk /dev/vdb: 247.0 GB, 246960619520 bytes, 482344960 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x38717fc1
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vdb1            2048   209715199   104856576   83  Linux
    /dev/vdb2       209715200   314572799    52428800   83  Linux
    ```

    In the command output, take note of the partition's start and end sectors. In this example,  **/dev/vdb2**'s start sector is  **209715200**, and its end sector is  **314572799**.

    View the  **/dev/vdb**  capacity and check whether the additional space is included.

    -   If the additional space is not included, refresh the capacity according to  [Extending Partitions and File Systems for SCSI Disks \(Linux\)](extending-partitions-and-file-systems-for-scsi-disks-(linux).md).
    -   If the additional space is included, take note of the start and end sectors of the target partition and then go to  [2](#li3879043619479). These values will be used in the subsequent operations.

2.  <a name="li3879043619479"></a>Run the following command to unmount the partition:

    **umount** _Disk partition_

    In this example, run the following command:

    **umount** **/dev/vdb2**

3.  Run the following command to enter fdisk:

    **fdisk** _Disk_

    In this example, run the following command:

    **fdisk** **/dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# fdisk /dev/vdb
    Welcome to fdisk (util-linux 2.23.2).
    
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    
    Command (m for help): 
    ```

4.  Run the following command to delete the partition to be extended:
    1.  Enter  **d**  and press  **Enter**  to delete the partition.

        Information similar to the following is displayed:

        ```
        Command (m for help): d
        Partition number (1,2, default 2):
        ```

    2.  Enter the partition number and press  **Enter**  to delete the partition. In this example, enter  **2**.

        Information similar to the following is displayed:

        ```
        Partition number (1,2, default 2): 2
        Partition 2 is deleted
        
        Command (m for help): 
        ```

        >![](/images/icon-note.gif) **NOTE:**   
        >After deleting the partition, recreate the partition according to the following steps, and data on this disk will not be lost.  


5.  Enter  **n**  and press  **Enter**  to create a new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): n
    Partition type:
       p   primary (1 primary, 0 extended, 3 free)
       e   extended
    Select (default p):
    ```

    There are two types of disk partitions:

    -   Choosing  **p**  creates a primary partition.
    -   Choosing  **e**  creates an extended partition.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the MBR partition style is used, a maximum of 4 primary partitions, or 3 primary partitions and 1 extended partition can be created. The extended partition cannot be used directly and must be divided into logical partitions before use.  
    >Disk partitions created using GPT are not categorized.  

6.  Ensure that the entered partition type is the same as the partition had before. In this example, a primary partition is used. Therefore, enter  **p**  and press  **Enter**  to create a primary partition.

    Information similar to the following is displayed:

    ```
    Select (default p): p
    Partition number (2-4, default 2): 
    ```

    **Partition number**  indicates the serial number of the primary partition.

7.  Ensure that entered partition number is the same as the partition had before. In this example, partition number  **2**  is used. Therefore, enter  **2**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    Partition number (2-4, default 2): 2
    First sector (209715200-482344959, default 209715200):
    ```

    In the command output,  **First sector**  specifies the start sector.

    >![](/images/icon-note.gif) **NOTE:**   
    >Data will be lost if the following operations are performed:  
    >-   Select a start sector other than the partition had before.  
    >-   Select an end sector smaller than the partition had before.  

8.  Ensure that the entered start sector is the same as the partition had before. In this example, start sector  **209715200**  is recorded in  [1](#li6396237219479). Therefore, enter  **209715200**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    First sector (209715200-482344959, default 209715200):
    Using default value 209715200
    Last sector, +sectors or +size{K,M,G} (209715200-482344959, default 482344959):
    ```

    In the command output,  **Last sector**  specifies the end sector.

9.  Ensure that the entered end sector is larger than or equal to the end sector recorded in  [1](#li6396237219479). In this example, the recorded end sector is  **314572799**, and the default end sector is used. Therefore, enter  **482344959**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    Using default value 209715200
    Last sector, +sectors or +size{K,M,G} (209715200-482344959, default 482344959):
    Using default value 482344959
    Partition 2 of type Linux and of size 130 GiB is set
    
    Command (m for help): 
    ```

    The partition is created.

10. Enter  **p**  and press  **Enter**  to view the partition details.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/vdb: 247.0 GB, 246960619520 bytes, 482344960 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x38717fc1
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vdb1            2048   209715199   104856576   83  Linux
    /dev/vdb2       209715200   482344959   136314880   83  Linux
    
    Command (m for help):
    ```

11. Enter  **w**  and press  **Enter**  to write the changes to the partition table.

    Information similar to the following is displayed:

    ```
    Command (m for help): w
    The partition table has been altered!
    
    Calling ioctl() to re-read partition table.
    
    WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
    The kernel still uses the old table. The new table will be used at
    the next reboot or after you run partprobe(8) or kpartx(8)
    Syncing disks.
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

12. Run the following command to synchronize the new partition table to the OS:

    **partprobe**

13. Perform the following operations based on the file system of the disk:
    -   For the  **ext**_\*_  file system
        1.  Run the following command to check the correctness of the file system on the partition:

            **e2fsck** **-f** _Disk partition_

            In this example, run the following command:

            **e2fsck** **-f** **/dev/vdb2**

            Information similar to the following is displayed:

            ```
            [root@ecs-test-0001 ~]# e2fsck -f /dev/vdb2
            e2fsck 1.42.9 (28-Dec-2013)
            Pass 1: Checking inodes, blocks, and sizes
            Pass 2: Checking directory structure
            Pass 3: Checking directory connectivity
            Pass 4: Checking reference counts
            Pass 5: Checking group summary information
            /dev/vdb2: 11/3276800 files (0.0% non-contiguous), 251790/13107200 blocks
            ```

        2.  Run the following command to extend the file system of the partition:

            **resize2fs** _Disk partition_

            In this example, run the following command:

            **resize2fs** **/dev/vdb2**

            Information similar to the following is displayed:

            ```
            [root@ecs-test-0001 ~]# resize2fs /dev/vdb2
            resize2fs 1.42.9 (28-Dec-2013)
            Resizing the filesystem on /dev/vdb2 to 34078720 (4k) blocks.
            The filesystem on /dev/vdb2 is now 34078720 blocks long.
            ```

        3.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        4.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/vdb2**  on  **/mnt/test**:

            **mount** **/dev/vdb2** **/mnt/test**

            >![](/images/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  


    -   For the  **xfs**  file system
        1.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        2.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/vdb2**  on  **/mnt/test**:

            **mount** **/dev/vdb2** **/mnt/test**

            >![](/images/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

        3.  Run the following command to extend the file system of the partition:

            **sudo** **xfs\_growfs** _Disk partition_

            In this example, run the following command:

            **sudo** **xfs\_growfs** **/dev/vdb2**


14. Run the following command to view the mount result:

    **df** **-TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  1.9G   39G   5% /
    devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
    tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
    tmpfs          tmpfs     2.0G  9.1M  2.0G   1% /run
    tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs          tmpfs     398M     0  398M   0% /run/user/0
    /dev/vdb1      ext4      106G   63M  101G   1% /mnt/sdc
    /dev/vdb2      ext4      138G   63M  131G   1% /mnt/test
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Creating a New GPT Partition<a name="section15940163415487"></a>

Originally, data disk  **/dev/vdb**  has 100 GB and one partition \(**/dev/vdb1**\), and then 50 GB is added to the disk. The following procedure shows you how to create a new GPT partition  **/dev/vdb2**  with this 50 GB.

1.  Run the following command to view the disk partition information:

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

2.  <a name="li131751636184912"></a>Run the following command to enter parted:

    **parted** _Disk_

    In this example, run the following command:

    **parted** **/dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# parted /dev/vdb
    GNU Parted 3.1
    Using /dev/vdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) 
    ```

3.  Enter  **unit s**  and press  **Enter**  to set the measurement unit of the disk to sector.
4.  <a name="li317653664918"></a>Enter  **p**  and press  **Enter**  to view the current disk partition style.

    Information similar to the following is displayed:

    ```
    (parted) unit s
    (parted) p
    Error: The backup GPT table is not at the end of the disk, as it should be.  This might mean that another operating system believes the
    disk is smaller.  Fix, by moving the backup to the end (and removing the old backup)?
    Fix/Ignore/Cancel? Fix
    Warning: Not all of the space available to /dev/vdb appears to be used, you can fix the GPT to use all of the space (an extra 104857600
    blocks) or continue with the current setting?
    Fix/Ignore? Fix
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 314572800s
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start  End         Size        File system  Name  Flags
     1      2048s  209713151s  209711104s  ext4         test
    
    (parted)
    ```

    In the command output, take note of the partition's end sector. In this example, the end sector of the  **/dev/vdb1**  partition is  **209713151s**.

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

5.  Run the following command and press  **Enter**:

    **mkpart** _Partition name Start sector_ _End sector_

    In this example, run the following command:

    **mkpart** **data** **209713152s** **100%**

    In this example, the additional space is used to create a new partition. In  [4](#li317653664918), the end sector of partition  **dev/vdb1**  is  **209713151s**. Therefore, the start sector of the new partition  **dev/vdb2**  is set to  **209713152s**  and the end sector  **100%**. This start and end sectors are for reference only. You can plan the number of partitions and partition size based on service requirements.

    Information similar to the following is displayed:

    ```
    (parted) mkpart data 209713152s 100%
    (parted) 
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >The maximum sector can be obtained in either of the following ways:  
    >-   Query the disk's maximum end sector. For details, see  [2](#li131751636184912)  to  [4](#li317653664918).  
    >-   Enter  **-1s**  or  **100%**, and the value displayed is the maximum end sector.  

6.  Enter  **p**  and press  **Enter**  to view the new partition.

    Information similar to the following is displayed:

    ```
    (parted) p
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 314572800s
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start       End         Size        File system  Name  Flags
     1      2048s       209713151s  209711104s  ext4         test
     2      209713152s  314570751s  104857600s               data
    
    (parted) 
    ```

7.  Enter  **q**  and press  **Enter**  to exit parted.

    Information similar to the following is displayed:

    ```
    (parted) q
    Information: You may need to update /etc/fstab.
    ```

    You can set automatic disk mounting by updating the  **/etc/fstab**  file. Before updating the file, set the file system format for the partition and mount the partition on the mount point.

8.  Run the following command to set the file system format for the new partition:

    **mkfs** **-t** _File system_ _Disk partition_

    In this example, run the following command:

    **mkfs** **-t** **ext4** **/dev/vdb2**

    >![](/images/icon-note.gif) **NOTE:**   
    >The procedure for setting the  **xfs**  file system is the same as that for the  **ext3**  or  **ext4**  file system. The command for creating the  **xfs**  file system is  **mkfs** **-t** **xfs** **/dev/vdb2**.  

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# mkfs -t ext4 /dev/vdb2
    mke2fs 1.42.9 (28-Dec-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    3276800 inodes, 13107200 blocks
    655360 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=2162163712
    400 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
            4096000, 7962624, 11239424
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    The formatting takes a while, and you need to observe the system running status. Once  **done**  is displayed in the command output, the formatting is complete.

9.  \(Optional\) Run the following command to create a mount point:

    Perform this step if you want to mount the partition on a new mount point.

    **mkdir** _Mount point_

    In this example, run the following command to create the  **/mnt/test**  mount point:

    **mkdir** **/mnt/test**

10. Run the following command to mount the partition:

    **mount** _Disk partition_ _Mount point_

    In this example, run the following command to mount the partition  **/dev/vdb2**  on  **/mnt/test**:

    **mount** **/dev/vdb2** **/mnt/test**

    >![](/images/icon-note.gif) **NOTE:**   
    >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

11. Run the following command to view the mount result:

    **df** **-TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  1.9G   39G   5% /
    devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
    tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
    tmpfs          tmpfs     2.0G  9.1M  2.0G   1% /run
    tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs          tmpfs     398M     0  398M   0% /run/user/0
    /dev/vdb1      ext4      106G   63M  101G   1% /mnt/sdc
    /dev/vdb2      ext4       53G   55M   50G   1% /mnt/test
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Extending an Existing GPT Partition<a name="section13346184710300"></a>

Originally, data disk  **/dev/vdb**  has 150 GB and two partitions \(**/dev/vdb1**  and  **/dev/vdb2**, and then 80 GB is added to the disk. The following procedure shows you how to add this 80 GB to the existing GPT partition  **/dev/vdb2**.

>![](/images/icon-notice.gif) **NOTICE:**   
>During an expansion, the additional space is added to the end of the disk. Therefore, if the disk has multiple partitions, the additional space can only be allocated to the partition at the disk end.  

1.  Run the following command to view the disk partition information:

    **lsblk**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  230G  0 disk
    ├─vdb1 253:17   0  100G  0 part /mnt/sdc
    └─vdb2 253:18   0   50G  0 part /mnt/test
    ```

    View the  **/dev/vdb**  capacity and check whether the additional space is included.

    -   If the additional space is not included, refresh the capacity according to  [Extending Partitions and File Systems for SCSI Disks \(Linux\)](extending-partitions-and-file-systems-for-scsi-disks-(linux).md).
    -   If the additional space is included, go to  [2](#li3879043619479).

2.  Run the following command to unmount the partition:

    **umount** _Disk partition_

    In this example, run the following command:

    **umount** **/dev/vdb2**

3.  Run the following command to view the unmount result:

    **lsblk**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  230G  0 disk
    ├─vdb1 253:17   0  100G  0 part /mnt/sdc
    └─vdb2 253:18   0   50G  0 part
    ```

4.  Run the following command to enter parted:

    **parted** _Disk_

    In this example, run the following command:

    **parted** **/dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# parted /dev/vdb
    GNU Parted 3.1
    Using /dev/vdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted)
    ```

5.  Enter  **unit s**  and press  **Enter**  to set the measurement unit of the disk to sector.
6.  <a name="li17966161521416"></a>Enter  **p**  and press  **Enter**  to view the current disk partition style.

    Information similar to the following is displayed:

    ```
    (parted) unit s
    (parted) p
    Error: The backup GPT table is not at the end of the disk, as it should be.  This might mean that another operating system believes the
    disk is smaller.  Fix, by moving the backup to the end (and removing the old backup)?
    Fix/Ignore/Cancel? Fix
    Warning: Not all of the space available to /dev/vdb appears to be used, you can fix the GPT to use all of the space (an extra 167772160
    blocks) or continue with the current setting?
    Fix/Ignore? Fix
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 482344960s
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start       End         Size        File system  Name  Flags
     1      2048s       209713151s  209711104s  ext4         test
     2      209713152s  314570751s  104857600s  ext4         data
    
    (parted)
    ```

    Take note of the start and end sectors of the  **/dev/vdb2**  partition. These values will be used during the partition recreation. In this example, the partition's start sector is  **209713152s**, and its end sector is  **314570751s**.

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

7.  Enter  **rm**  and the partition number, and then press  **Enter**. In this example, partition number  **2**  is used.

    Information similar to the following is displayed:

    ```
    (parted) rm
    Partition number? 2
    (parted)
    ```

8.  Run the following command to recreate the partition and press  **Enter**:

    **mkpart** _Partition name Start sector_ _End sector_

    In this example, run the following command:

    **mkpart data 209713152s 100%**

    -   Ensure that the entered start sector is the same as the partition had before. In this example, start sector  **209713152s**  is recorded in  [6](#li17966161521416). Therefore, enter  **209713152s**.
    -   Ensure that the entered end sector is smaller than the partition had before. In this example, the end sector recorded in  [6](#li17966161521416)  is  **314570751s**, and all the additional space needs to be allocated to  **dev/vdb2**. Therefore, enter  **100%**.

    Information similar to the following is displayed:

    ```
    (parted) mkpart data 209713152s 100%
    (parted)
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >Data will be lost if the following operations are performed:  
    >-   Select a start sector other than the partition had before.  
    >-   Select an end sector smaller than the partition had before.  

9.  Enter  **p**  and press  **Enter**  to view the partition information.

    Information similar to the following is displayed:

    ```
    (parted) p
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 482344960s
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start       End         Size        File system  Name  Flags
     1      2048s       209713151s  209711104s  ext4         test
     2      209713152s  482342911s  272629760s  ext4         data
    
    (parted) 
    ```

10. Enter  **q**  and press  **Enter**  to exit parted.

    Information similar to the following is displayed:

    ```
    (parted) q
    Information: You may need to update /etc/fstab.
    ```

    You can set automatic disk mounting by updating the  **/etc/fstab**  file. Before updating the file, set the file system format for the partition and mount the partition on the mount point.

11. Perform the following operations based on the file system of the disk:
    -   For the  **ext**_\*_  file system
        1.  Run the following command to check the correctness of the file system on the partition:

            **e2fsck** **-f** _Disk partition_

            In this example, run the following command:

            **e2fsck** **-f** **/dev/vdb2**

            Information similar to the following is displayed:

            ```
            [root@ecs-test-0001 ~]# e2fsck -f /dev/vdb2
            e2fsck 1.42.9 (28-Dec-2013)
            Pass 1: Checking inodes, blocks, and sizes
            Pass 2: Checking directory structure
            Pass 3: Checking directory connectivity
            Pass 4: Checking reference counts
            Pass 5: Checking group summary information
            /dev/vdb2: 11/3276800 files (0.0% non-contiguous), 251790/13107200 blocks
            ```

        2.  Run the following command to extend the file system of the partition:

            **resize2fs** _Disk partition_

            In this example, run the following command:

            **resize2fs** **/dev/vdb2**

            Information similar to the following is displayed:

            ```
            [root@ecs-test-0001 ~]# resize2fs /dev/vdb2
            resize2fs 1.42.9 (28-Dec-2013)
            Resizing the filesystem on /dev/vdb2 to 34078720 (4k) blocks.
            The filesystem on /dev/vdb2 is now 34078720 blocks long.
            ```

        3.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        4.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/vdb2**  on  **/mnt/test**:

            **mount** **/dev/vdb2** **/mnt/test**

            >![](/images/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  


    -   For the  **xfs**  file system
        1.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        2.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/vdb2**  on  **/mnt/test**:

            **mount** **/dev/vdb2** **/mnt/test**

            >![](/images/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

        3.  Run the following command to extend the file system of the partition:

            **sudo** **xfs\_growfs** _Disk partition_

            In this example, run the following command:

            **sudo** **xfs\_growfs** **/dev/vdb2**


12. Run the following command to view the mount result:

    **df -TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  1.9G   39G   5% /
    devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
    tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
    tmpfs          tmpfs     2.0G  9.1M  2.0G   1% /run
    tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs          tmpfs     398M     0  398M   0% /run/user/0
    /dev/vdb1      ext4      106G   63M  101G   1% /mnt/sdc
    /dev/vdb2      ext4      138G   63M  131G   1% /mnt/test
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Setting Automatic Mounting at System Start<a name="section1107170115310"></a>

To automatically mount disk partitions at system start, do not specify partitions, for example  **/dev/vdb1**, in  **/etc/fstab**  because the sequence of cloud devices, and therefore their names may change during the server stop and start. You are advised to use the universally unique identifier \(UUID\) in  **/etc/fstab**  to set automatic mounting at system start.

>![](/images/icon-note.gif) **NOTE:**   
>UUID is the unique character string for disk partitions in a Linux system.  

1.  Run the following command to query the partition UUID:

    **blkid** _Disk partition_

    In this example, run the following command to query the UUID of the  **/dev/vdb1**  partition:

    **blkid /dev/vdb1**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# blkid /dev/vdb1
    /dev/vdb1: UUID="0b3040e2-1367-4abb-841d-ddb0b92693df" TYPE="ext4"
    ```

    The UUID of the  **/dev/vdb1**  partition is displayed.

2.  Run the following command to open the  **fstab**  file using the vi editor:

    **vi /etc/fstab**

3.  Press  **i**  to enter the editing mode.
4.  Move the cursor to the end of the file and press  **Enter**. Then, add the following information:

    ```
    UUID=0b3040e2-1367-4abb-841d-ddb0b92693df /mnt/sdc                ext4    defaults        0 2
    ```

5.  Press  **Esc**, enter  **:wq**, and press  **Enter**.

    The system saves the configurations and exits the vi editor.

6.  Perform the following operations to verify the automatic mounting function:
    1.  Run the following command to unmount the partition:

        **umount** _Disk partition_

        In this example, run the following command:

        **umount /dev/vdb1**

    2.  Run the following command to reload all the content in the  **/etc/fstab**  file:

        **mount -a**

    3.  Run the following command to query the file system mounting information:

        **mount** **|** **grep** _Mount point_

        In this example, run the following command:

        **mount** **|** **grep** **/mnt/sdc**

        If information similar to the following is displayed, the automatic mounting function takes effect:

        ```
        root@ecs-test-0001 ~]# mount | grep /mnt/sdc
        /dev/vdb1 on /mnt/sdc type ext4 (rw,relatime,data=ordered)
        ```



