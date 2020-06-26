# Extending Partitions and File Systems for System Disks \(Linux\)<a name="evs_01_0072"></a>

## Scenarios<a name="section4385650719406"></a>

After a disk has been expanded on the management console, only the disk storage capacity is enlarged, but its additional space cannot be used directly.

In Linux, you must allocate the additional space to an existing partition or a new partition.

This topic uses CentOS 7.4 64bit and CentOS 6.5 64bit as the sample OSs to describe how to extend the disk partition using growpart and fdisk. The method for allocating the additional space varies depending on the server OS. This document is used for reference only. For the detailed operations and differences, see the corresponding OS documents.

-   [Extending an Existing MBR Partition](#section143412109355)
-   [Creating a New MBR Partition](#section9194153012119)

>![](/images/icon-notice.gif) **NOTICE:**   
>Performing the expansion operations with caution. Misoperation may lead to data loss or exceptions. Therefore, you are advised to back up the disk data using backups or snapshots before expansion. For details about backups and snapshots, see  [Managing EVS Backup](managing-evs-backup.md)  and  [Creating a Snapshot](creating-a-snapshot.md), respectively.  

## Prerequisites<a name="section51503350171737"></a>

-   You have expanded the system disk capacity and attached the disk to a server on the management console. For details, see  [Expanding Capacity for an In-use EVS Disk](expanding-capacity-for-an-in-use-evs-disk.md)  or  [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md).
-   You have logged in to the server.
    -   For how to log in to an ECS, see the  _Elastic Cloud Server User Guide_.
    -   For how to log in to a BMS, see the  _Bare Metal Server User Guide_.


## Extending an Existing MBR Partition<a name="section143412109355"></a>

1.  \(Optional\) Run the following command to install the growpart tool:

    **yum install cloud-utils-growpart**

    >![](/images/icon-note.gif) **NOTE:**   
    >You can run the  **growpart**  command to check whether the growpart tool has been installed. If the command output displays the tool usage instructions, the tool has been installed and you do not need to install it separately.  

2.  Run the following command to query the Linux kernel version:

    **uname -a**

    Then, perform corresponding operations depending on whether the Linux kernel version is later than 3.6.0.

    -   View the CentOS 7.4 64bit kernel version. Information similar to the following is displayed:

        ```
        Linux ecs-test-0001 3.10.0-957.5.1.el7.x86_64 #1 SMP Fri Feb 1 14:54:57 UTC 2019 x86_64 x86_64 
        ```

        The kernel version is 3.10.0, which is later than 3.6.0. In this case, a server reboot is not required after the disk partition and file system extension. For details, see  [3](#li18237184811315).

    -   View the CentOS 6.5 64bit kernel version. Information similar to the following is displayed:

        ```
        Linux ecs-test-0002 2.6.32-754.10.1.el6.x86_64 #1 SMP Tue Jan 15 17:07:28 UTC 2019 x86_64
        ```

        The kernel version is 2.6.32, which is earlier than 3.6.0. In this case, the disk partition and file system extension takes effect only after a server reboot. For details, see  [4](#li3275153719124).

3.  <a name="li18237184811315"></a>Perform the following steps to extend the disk partition and file system:

    In this example, CentOS 7.4 64bit is used as the sample OS. Because its kernel version is later than 3.6.0, a server reboot is not required.

    1.  Run the following command to view the total capacity of the  **/dev/vda**  system disk:

        **fdisk -l**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# fdisk -l
        
        Disk /dev/vda: 107.4 GB, 107374182400 bytes, 209715200 sectors
        Units = sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disk label type: dos
        Disk identifier: 0x000bcb4e
        
           Device Boot      Start         End      Blocks   Id  System
        /dev/vda1   *        2048    83886079    41942016   83  Linux
        ```

    2.  Run the following command to view the capacity of the  **/dev/vda1**  partition:

        **df -TH**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# df -TH
        Filesystem     Type      Size  Used Avail Use% Mounted on
        /dev/vda1      ext4       43G  2.0G   39G   5% /
        devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
        tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
        tmpfs          tmpfs     2.0G  9.0M  2.0G   1% /run
        tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
        tmpfs          tmpfs     398M     0  398M   0% /run/user/0
        ```

    3.  Run the following command to extend the partition using growpart:

        **growpart** _System disk Partition number_

        In this example, run the following command:

        **growpart /dev/vda 1**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# growpart /dev/vda 1
        CHANGED: partition=1 start=2048 old: size=83884032 end=83886080 new: size=209713119,end=209715167
        ```

    4.  Run the following command to extend the file system of the partition:

        **resize2fs** _Disk partition_

        In this example, run the following command:

        **resize2fs /dev/vda1**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# resize2fs /dev/vda1
        resize2fs 1.42.9 (28-Dec-2013)
        Filesystem at /dev/vda1 is mounted on /; on-line resizing required
        old_desc_blocks = 5, new_desc_blocks = 13
        The filesystem on /dev/vda1 is now 26214139 blocks long.
        ```

    5.  Run the following command to view the new capacity of the  **/dev/vda1**  partition:

        **df -TH**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# df -TH
        Filesystem     Type      Size  Used Avail Use% Mounted on
        /dev/vda1      ext4      106G  2.0G   99G   2% /
        devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
        tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
        tmpfs          tmpfs     2.0G  9.0M  2.0G   1% /run
        tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
        tmpfs          tmpfs     398M     0  398M   0% /run/user/0
        ```

4.  <a name="li3275153719124"></a>Perform the following steps to extend the disk partition and file system:

    In this example, CentOS 6.5 64bit is used as the sample OS. Because its kernel version is earlier than 3.6.0, a server reboot is required.

    1.  Run the following command to install the dracut-modules-growroot tool:

        **yum install cloud-utils-growpart**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# yum install cloud-utils-growpart
        Loaded plugins: fastestmirror, security
        Setting up Install Process
        Determining fastest mirrors
        ...
        Package cloud-utils-growpart-0.27-10.el6.x86_64 already installed and latest version
        Nothing to do
        ```

    2.  Run the following command to regenerate the initramfs file:

        **dracut -f**

    3.  Run the following command to view the total capacity of the  **/dev/vda**  system disk:

        **fdisk -l**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# fdisk -l
        
        Disk /dev/vda: 107.4 GB, 107374182400 bytes
        255 heads, 63 sectors/track, 13054 cylinders
        Units = cylinders of 16065 * 512 = 8225280 bytes
        Sector size (logical/physical): 512 bytes / 512 bytes
        I/O size (minimum/optimal): 512 bytes / 512 bytes
        Disk identifier: 0x0004e0be
        
           Device Boot      Start         End      Blocks   Id  System
        /dev/vda1   *           1        5222    41942016   83  Linux
        ```

    4.  Run the following command to view the capacity of the  **/dev/vda1**  partition:

        **df -TH**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# df -TH
        Filesystem     Type   Size  Used Avail Use% Mounted on
        /dev/vda1      ext4    43G  1.7G   39G   5% /
        tmpfs          tmpfs  2.1G     0  2.1G   0% /dev/shm
        ```

    5.  Run the following command to extend the partition using growpart:

        **growpart** _System disk Partition number_

        In this example, run the following command:

        **growpart /dev/vda 1**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# growpart /dev/vda 1
        CHANGED: partition=1 start=2048 old: size=83884032 end=83886080 new: size=209710462,end=209712510
        ```

    6.  Run the following command to restart the server:

        **reboot**

        After the server is restarted, reconnect to the server and perform the following steps.

    7.  Run the following command to extend the file system of the partition:

        **resize2fs** _Disk partition_

        In this example, run the following command:

        **resize2fs** **/dev/vda1**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# resize2fs /dev/vda1
        resize2fs 1.41.12 (17-May-2010)
        The filesystem is already 26213807 blocks long.  Nothing to do!
        ```

    8.  Run the following command to view the new capacity of the  **/dev/vda1**  partition:

        **df -TH**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0002 ~]# df -TH
        Filesystem     Type   Size  Used Avail Use% Mounted on
        /dev/vda1      ext4   106G  1.7G   99G   2% /
        tmpfs          tmpfs  2.1G     0  2.1G   0% /dev/shm
        ```



## Creating a New MBR Partition<a name="section9194153012119"></a>

Originally, system disk  **/dev/vda**  has 40 GB and one partition \(**/dev/vda1**\), and then 40 GB is added to the disk. The following procedure shows you how to create a new MBR partition  **/dev/vda2**  with this 40 GB.

1.  Run the following command to view the disk partition information:

    **fdisk -l**

    Information similar to the following is displayed:

    ```
    [root@ecs-2220 ~]# fdisk -l
    
    Disk /dev/vda: 85.9 GB, 85899345920 bytes, 167772160 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x0008d18f
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vda1   *        2048    83886079    41942016   83  Linux
    ```

    In the command output, the capacity of the  **dev/vda**  system disk is 80 GB, in which the in-use  **dev/vda1**  partition takes 40 GB and the additional 40 GB has not been allocated.

2.  Run the following command to enter fdisk:

    **fdisk /dev/vda**

    Information similar to the following is displayed:

    ```
    [root@ecs-2220 ~]# fdisk /dev/vda
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

5.  Partition number  **2**  is used in this example. Therefore, enter  **2**  and press  **Enter.**

    Information similar to the following is displayed:

    ```
    Partition number (2-4, default 2): 2
    First sector (83886080-167772159, default 83886080):
    ```

6.  Enter the new partition's start sector and press  **Enter**. In this example, the default start sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    First sector (83886080-167772159, default 83886080):
    Using default value 83886080
    Last sector, +sectors or +size{K,M,G} (83886080-167772159,default 167772159):
    ```

7.  Enter the new partition's end sector and press  **Enter**. In this example, the default end sector is used.

    The system displays the start and end sectors of the partition's available space. You can customize the value within this range or use the default value. The start sector must be smaller than the partition's end sector.

    Information similar to the following is displayed:

    ```
    Last sector, +sectors or +size{K,M,G} (83886080-167772159,
    default 167772159):
    Using default value 167772159
    Partition 2 of type Linux and of size 40 GiB is set
    
    Command (m for help): 
    ```

8.  Enter  **p**  and press  **Enter**  to view the new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/vda: 85.9 GB, 85899345920 bytes, 167772160 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x0008d18f
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/vda1   *        2048    83886079    41942016   83  Linux
    /dev/vda2        83886080   167772159    41943040   83  Linux
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

    The partition is created.

    >![](/images/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

10. Run the following command to synchronize the new partition table to the OS:

    **partprobe**

11. Run the following command to set the file system format for the new partition:

    \(The ext4 file system is used in this example.\)

    **mkfs -t ext4 /dev/vda2**

    >![](/images/icon-note.gif) **NOTE:**   
    >The procedure for setting the  **xfs**  file system is the same as that for the  **ext3**  or  **ext4**  file system. The command for creating the  **xfs**  file system is  **mkfs -t xfs /dev/vda2**.  

    Information similar to the following is displayed:

    ```
    [root@ecs-2220 ~]# mkfs -t ext4 /dev/vda2
    mke2fs 1.42.9 (28-Dec-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    2621440 inodes, 10485760 blocks
    524288 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=2157969408
    320 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
            4096000, 7962624
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    The formatting takes a while, and you need to observe the system running status. Once  **done**  is displayed in the command output, the formatting is complete.

12. \(Optional\) Run the following command to create a mount point:

    Perform this step if you want to mount the partition on a new mount point.

    **mkdir** _Mount point_

    In this example, run the following command to create the  **/opt**  mount point:

    **mkdir /opt**

13. Run the following command to mount the new partition:

    **mount** _Disk partition_ _Mount point_

    In this example, run the following command to mount the new partition  **/dev/vda2**  on  **/opt**:

    **mount /dev/vda2 /opt**

    >![](/images/icon-note.gif) **NOTE:**   
    >If the new partition is mounted on a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition on an empty directory or a new directory. If the new partition must be mounted on a directory that is not empty, move the subdirectories and files in this directory to another directory temporarily. After the partition is successfully mounted, move the subdirectories and files back.  

14. Run the following command to view the mount result:

    **df -TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-2220 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  2.0G   39G   5% /
    devtmpfs       devtmpfs  509M     0  509M   0% /dev
    tmpfs          tmpfs     520M     0  520M   0% /dev/shm
    tmpfs          tmpfs     520M  7.2M  513M   2% /run
    tmpfs          tmpfs     520M     0  520M   0% /sys/fs/cgroup
    tmpfs          tmpfs     104M     0  104M   0% /run/user/0
    /dev/vda2      ext4       43G   51M   40G   1% /opt
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



