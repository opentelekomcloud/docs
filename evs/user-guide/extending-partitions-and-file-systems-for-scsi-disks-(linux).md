# Extending Partitions and File Systems for SCSI Disks \(Linux\)<a name="evs_01_0018"></a>

## Scenarios<a name="section4385650719406"></a>

After a disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly.

In Linux, you must allocate the additional space to an existing partition or a new partition. This topic uses CentOS 7.4 64bit as the sample OS to describe how to extend an MBR partition of a SCSI data disk. The method for allocating the additional space varies depending on the server OS. This document is used for reference only. For the detailed operations and differences, see the corresponding OS documents.

-   [Creating a New MBR Partition](#section12265143819280)
-   [Extending an Existing MBR Partition](#section31113372194023)

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Performing the expansion operations with caution. Misoperation may lead to data loss or exceptions. Therefore, you are advised to back up the disk data using backups or snapshots before expansion. For details about backups and snapshots, see  [Managing EVS Backup](managing-evs-backup.md)  and  [Creating a Snapshot](creating-a-snapshot.md), respectively.  

## Prerequisites<a name="section19088989195835"></a>

-   You have expanded the disk capacity and attached the disk to a server on the management console. For details, see  [Expanding Capacity for an In-use EVS Disk](expanding-capacity-for-an-in-use-evs-disk.md)  or  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).
-   You have logged in to the server.
    -   For how to log in to an ECS, see the  _Elastic Cloud Server User Guide_.
    -   For how to log in to a BMS, see the  _Bare Metal Server User Guide_.


## Creating a New MBR Partition<a name="section12265143819280"></a>

Originally, data disk  **/dev/sda**  has 50 GB and one partition \(**/dev/sda1**\), and then 50 GB is added to the disk. The following procedure shows you how to create a new MBR partition  **/dev/sda2**  with this 50 GB.

1.  Run the following command to view the disk partition information:

    **fdisk -l**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# fdisk -l
    
    Disk /dev/vda: 42.9 GB, 42949672960 bytes, 83886080 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x000bcb4e
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vda1   *        2048    83886079    41942016   83  Linux
    
    Disk /dev/sda: 107.4 GB, 107374182400 bytes, 209715200 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x915ffe6a
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/sda1            2048   104857599    52427776   83  Linux
    ```

    View the  **/dev/sda**  capacity and check whether the additional space is included.

    -   If the additional space is not included, refresh the capacity according to  [2](#li1311112192367).
    -   If the additional space is included, go to  [3](#li14771329195025).

2.  <a name="li1311112192367"></a>\(Optional\) Run the following command to update the capacity of the SCSI data disk:
    1.  Run the following command to update the disk capacity on the server:

        **echo 1 \> /sys/class/scsi\_device/**_%d:%d:%d:%d_**/device/rescan &**

        In the command,  **%d:%d:%d:%d**  indicates a folder in the  **/sys/class/scsi\_device/**  directory and can be obtained using  **ll /sys/class/scsi\_device/**.

        Information similar to the following is displayed: \(**2:0:0:0**  indicates the folder to be obtained.\)

        ```
        cs-xen-02:/sys/class/scsi_device # ll /sys/class/scsi_device/
        total 0
        lrwxrwxrwx 1 root root 0 Sep 26 11:37 2:0:0:0 -> ../../devices/xen/vscsi-2064/host2/target2:0:0/2:0:0:0/scsi_device/2:0:0:0
        ```

        In this example, run the following command:

        **echo 1 \> /sys/class/scsi\_device/2:0:0:0/device/rescan &**

    2.  After the disk capacity is updated, run the following command to view the disk partition information again:

        **fdisk -l**

        If the additional space is included, go to  [3](#li14771329195025).

3.  <a name="li14771329195025"></a>Run the following command to enter fdisk:

    **fdisk** _Disk_

    In this example, run the following command:

    **fdisk /dev/sda**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# fdisk /dev/sda
    Welcome to fdisk (util-linux 2.23.2).
    
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    
    Command (m for help):
    ```

4.  Enter  **n**  and press  **Enter**  to create a new partition.

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

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the MBR partition style is used, a maximum of 4 primary partitions, or 3 primary partitions and 1 extended partition can be created. The extended partition cannot be used directly and must be divided into logical partitions before use.  
    >Disk partitions created using GPT are not categorized.  

5.  In this example, a primary partition is created. Therefore, enter  **p**  and press  **Enter**  to create a primary partition.

    Information similar to the following is displayed:

    ```
    Select (default p): p
    Partition number (2-4, default 2):
    ```

    **Partition number**  indicates the serial number of the primary partition. Because partition number 1 has been used, the value ranges from  **2**  to  **4**.

6.  Enter the serial number of the primary partition and press  **Enter**. Partition number  **2**  is used in this example. Therefore, enter  **2**  and press  **Enter.**

    Information similar to the following is displayed:

    ```
    Partition number (2-4, default 2): 2
    First sector (104857600-209715199, default 104857600):
    ```

    **First sector**  indicates the start sector. The value ranges from  **104857600**  to  **209715199**, and the default value is  **104857600**.

7.  Enter the new partition's start sector and press  **Enter**. In this example, the default start sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    First sector (104857600-209715199, default 104857600):
    Using default value 104857600
    Last sector, +sectors or +size{K,M,G} (104857600-209715199, default 209715199):
    ```

    **Last sector**  indicates the end sector. The value ranges from  **104857600**  to  **209715199**, and the default value is  **209715199**.

8.  Enter the new partition's end sector and press  **Enter**. In this example, the default end sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    Last sector, +sectors or +size{K,M,G} (104857600-209715199, default 209715199):
    Using default value 209715199
    Partition 2 of type Linux and of size 50 GiB is set
    
    Command (m for help):
    ```

9.  Enter  **p**  and press  **Enter**  to view the new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/sda: 107.4 GB, 107374182400 bytes, 209715200 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x915ffe6a
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/sda1            2048   104857599    52427776   83  Linux
    /dev/sda2       104857600   209715199    52428800   83  Linux
    
    Command (m for help):
    ```

10. Enter  **w**  and press  **Enter**  to write the changes to the partition table.

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

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

11. Run the following command to synchronize the new partition table to the OS:

    **partprobe**

12. Run the following command to set the file system format for the new partition:

    **mkfs -t** _File system_ _Disk partition_

    In this example, run the following command:

    **mkfs -t ext4 /dev/sda2**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The procedure for setting the  **xfs**  file system is the same as that for the  **ext**_\*_  file system. The command for creating the  **xfs**  file system is  **mkfs -t xfs /dev/sda2**.  

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# mkfs -t ext4 /dev/sda2
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

13. \(Optional\) Run the following command to create a mount point:

    Perform this step if you want to mount the partition on a new mount point.

    **mkdir** _Mount point_

    In this example, run the following command to create the  **/mnt/test**  mount point:

    **mkdir** **/mnt/test**

14. Run the following command to mount the new partition:

    **mount** _Disk partition_ _Mount point_

    In this example, run the following command to mount the new partition  **/dev/sda2**  on  **/mnt/test**:

    **mount /dev/sda2 /mnt/test**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

15. Run the following command to view the mount result:

    **df -TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  2.0G   39G   5% /
    devtmpfs       devtmpfs  509M     0  509M   0% /dev
    tmpfs          tmpfs     520M     0  520M   0% /dev/shm
    tmpfs          tmpfs     520M  7.2M  513M   2% /run
    tmpfs          tmpfs     520M     0  520M   0% /sys/fs/cgroup
    tmpfs          tmpfs     104M     0  104M   0% /run/user/0
    /dev/sda1      ext4       53G   55M   50G   1% /mnt/sdc
    /dev/sda2      ext4       53G   55M   50G   1% /mnt/test
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Extending an Existing MBR Partition<a name="section31113372194023"></a>

Originally, SCSI data disk  **/dev/sda**  has 100 GB and two partitions \(**/dev/sda1**  and  **/dev/sda2**, and then 50 GB is added to the disk. The following procedure shows you how to add this 50 GB to the existing MBR partition  **/dev/sda2**.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>During an expansion, the additional space is added to the end of the disk. Therefore, if the disk has multiple partitions, the additional space can only be allocated to the partition at the disk end.  

1.  <a name="li6396237219479"></a>Run the following command to view the disk partition information:

    **fdisk -l**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# fdisk -l
    
    Disk /dev/vda: 42.9 GB, 42949672960 bytes, 83886080 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x000bcb4e
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vda1   *        2048    83886079    41942016   83  Linux
    
    Disk /dev/sda: 161.1 GB, 161061273600 bytes, 314572800 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x915ffe6a
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/sda1            2048   104857599    52427776   83  Linux
    /dev/sda2       104857600   209715199    52428800   83  Linux
    ```

    In the command output, take note of the partition's start and end sectors. In this example,  **/dev/sda2**'s start sector is  **104857600**, and its end sector is  **209715199**.

    View the  **/dev/sda**  capacity and check whether the additional space is included.

    -   If the additional space is not included, refresh the capacity according to  [2](#li11239195417383).
    -   If the additional space is included, take note of the start and end sectors of the target partition and then go to  [3](#li3879043619479). These values will be used in the subsequent operations.

2.  <a name="li11239195417383"></a>\(Optional\) Run the following command to update the capacity of the SCSI data disk:
    1.  Run the following command to update the disk capacity on the server:

        **echo 1 \> /sys/class/scsi\_device/**_%d:%d:%d:%d_**/device/rescan &**

        In the command,  **%d:%d:%d:%d**  indicates a folder in the  **/sys/class/scsi\_device/**  directory and can be obtained using  **ll /sys/class/scsi\_device/**.

        Information similar to the following is displayed: \(**2:0:0:0**  indicates the folder to be obtained.\)

        ```
        cs-xen-02:/sys/class/scsi_device # ll /sys/class/scsi_device/
        total 0
        lrwxrwxrwx 1 root root 0 Sep 26 11:37 2:0:0:0 -> ../../devices/xen/vscsi-2064/host2/target2:0:0/2:0:0:0/scsi_device/2:0:0:0
        ```

        In this example, run the following command:

        **echo 1 \> /sys/class/scsi\_device/2:0:0:0/device/rescan &**

    2.  After the disk capacity is updated, run the following command to view the disk partition information again:

        **fdisk -l**

        If the additional space is included, take note of the start and end sectors of the target partition and then go to  [3](#li3879043619479). These values will be used in the subsequent operations.

3.  <a name="li3879043619479"></a>Run the following command to unmount the partition:

    **umount** _Disk partition_

    In this example, run the following command:

    **umount /dev/sda2**

4.  Run the following command to enter fdisk:

    **fdisk** _Disk_

    In this example, run the following command:

    **fdisk /dev/sda**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# fdisk /dev/sda
    Welcome to fdisk (util-linux 2.23.2).
    
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    
    Command (m for help):
    ```

5.  Run the following command to delete the partition to be extended:
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

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >After deleting the partition, recreate the partition according to the following steps, and data on this disk will not be lost.  


6.  Enter  **n**  and press  **Enter**  to create a new partition.

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

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the MBR partition style is used, a maximum of 4 primary partitions, or 3 primary partitions and 1 extended partition can be created. The extended partition cannot be used directly and must be divided into logical partitions before use.  
    >Disk partitions created using GPT are not categorized.  

7.  Ensure that the entered partition type is the same as the partition had before. In this example, a primary partition is used. Therefore, enter  **p**  and press  **Enter**  to create a primary partition.

    Information similar to the following is displayed:

    ```
    Select (default p): p
    Partition number (2-4, default 2):
    ```

    **Partition number**  indicates the serial number of the primary partition.

8.  Ensure that entered partition number is the same as the partition had before. In this example, partition number  **2**  is used. Therefore, enter  **2**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    Partition number (2-4, default 2): 2
    First sector (104857600-314572799, default 104857600):
    ```

    In the command output,  **First sector**  specifies the start sector.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Data will be lost if the following operations are performed:  
    >-   Select a start sector other than the partition had before.  
    >-   Select an end sector smaller than the partition had before.  

9.  Ensure that the entered start sector is the same as the partition had before. In this example, start sector  **104857600**  is recorded in  [1](#li6396237219479)  or  [2](#li11239195417383). Therefore, enter  **104857600**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    First sector (104857600-314572799, default 104857600):
    Using default value 104857600
    Last sector, +sectors or +size{K,M,G} (104857600-314572799, default 314572799):
    ```

    In the command output,  **Last sector**  specifies the end sector.

10. Ensure that the entered end sector is larger than or equal to the end sector recorded in  [1](#li6396237219479)  or  [2](#li11239195417383). In this example, the recorded end sector is  **209715199**, and the default end sector is used. Therefore, enter  **314572799**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    Last sector, +sectors or +size{K,M,G} (104857600-314572799, default 314572799):
    Using default value 314572799
    Partition 2 of type Linux and of size 100 GiB is set
    
    Command (m for help):
    ```

    The partition is created.

11. Enter  **p**  and press  **Enter**  to view the partition details.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/sda: 161.1 GB, 161061273600 bytes, 314572800 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x915ffe6a
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/sda1            2048   104857599    52427776   83  Linux
    /dev/sda2       104857600   314572799    104857600  83  Linux
    
    Command (m for help):
    ```

12. Enter  **w**  and press  **Enter**  to write the changes to the partition table.

    Information similar to the following is displayed: \(The partition is successfully created.\)

    ```
    Command (m for help): w
    The partition table has been altered!
    
    Calling ioctl() to re-read partition table.
    
    WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
    The kernel still uses the old table. The new table will be used at
    the next reboot or after you run partprobe(8) or kpartx(8)
    Syncing disks.
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

13. Run the following command to synchronize the new partition table to the OS:

    **partprobe**

14. Perform the following operations based on the file system of the disk:
    -   For the  **ext**_\*_  file system
        1.  Run the following command to check the correctness of the file system on the partition:

            **e2fsck -f** _Disk partition_

            In this example, run the following command:

            **e2fsck -f /dev/sda2**

            Information similar to the following is displayed:

            ```
            [root@ecs-scsi ~]# e2fsck -f /dev/sda2
            e2fsck 1.42.9 (28-Dec-2013)
            Pass 1: Checking inodes, blocks, and sizes
            Pass 2: Checking directory structure
            Pass 3: Checking directory connectivity
            Pass 4: Checking reference counts
            Pass 5: Checking group summary information
            /dev/sda2: 11/3276800 files (0.0% non-contiguous), 251790/13107200 blocks
            ```

        2.  Run the following command to extend the file system of the partition:

            **resize2fs** _Disk partition_

            In this example, run the following command:

            **resize2fs /dev/sda2**

            Information similar to the following is displayed:

            ```
            [root@ecs-scsi ~]# resize2fs /dev/sda2
            resize2fs 1.42.9 (28-Dec-2013)
            Resizing the filesystem on /dev/sda2 to 26214400 (4k) blocks.
            The filesystem on /dev/sda2 is now 26214400 blocks long.
            ```

        3.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        4.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/sda2**  on  **/mnt/test**:

            **mount /dev/sda2 /mnt/test**

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  


    -   For the  **xfs**  file system
        1.  \(Optional\) Run the following command to create a mount point:

            Perform this step if you want to mount the partition on a new mount point.

            **mkdir** _Mount point_

            In this example, run the following command to create the  **/mnt/test**  mount point:

            **mkdir** **/mnt/test**

        2.  Run the following command to mount the partition:

            **mount** _Disk partition_ _Mount point_

            In this example, run the following command to mount the partition  **/dev/sda2**  on  **/mnt/test**:

            **mount /dev/sda2 /mnt/test**

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

        3.  Run the following command to extend the file system of the partition:

            **sudo** **xfs\_growfs** _Disk partition_

            In this example, run the following command:

            **sudo** **xfs\_growfs** **/dev/sda2**


15. Run the following command to view the mount result:

    **df -TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-scsi ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  2.0G   39G   5% /
    devtmpfs       devtmpfs  509M     0  509M   0% /dev
    tmpfs          tmpfs     520M     0  520M   0% /dev/shm
    tmpfs          tmpfs     520M  7.2M  513M   2% /run
    tmpfs          tmpfs     520M     0  520M   0% /sys/fs/cgroup
    tmpfs          tmpfs     104M     0  104M   0% /run/user/0
    /dev/sda1      ext4       53G   55M   50G   1% /mnt/sdc
    /dev/sda2      ext4      106G   63M  101G   1% /mnt/test
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#section1107170115310).  


## Setting Automatic Mounting at System Start<a name="section1107170115310"></a>

To automatically mount disk partitions at system start, do not specify partitions, for example  **/dev/vdb1**, in  **/etc/fstab**  because the sequence of cloud devices, and therefore their names may change during the server stop and start. You are advised to use the universally unique identifier \(UUID\) in  **/etc/fstab**  to set automatic mounting at system start.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
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



