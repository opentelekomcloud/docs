# Initializing a Linux Data Disk \(parted\)<a name="EN-US_TOPIC_0085634798"></a>

## Scenarios<a name="en-us_topic_0084935709_section31580524185332"></a>

This topic uses CentOS 7.4 64bit to describe how to initialize a data disk attached to a server running Linux and use parted to partition the data disk.

The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Therefore, use the GPT partition style if your disk capacity is larger than 2 TB. In Linux, if you choose to use the GPT partition style, the fdisk partitioning tool cannot be used. Use the parted partitioning tool instead. For details about disk partition styles, see  [Scenarios and Disk Partitions](scenarios-and-disk-partitions.md).

The method for initializing a disk varies depending on the OS running on the server. This document is used for reference only. For the detailed operations and differences, see the product documents of the corresponding OS.

## Prerequisites<a name="en-us_topic_0084935709_section36737034185332"></a>

-   A data disk has been attached to a server and has not been initialized.
-   You have logged in to the server.
    -   For how to log in to an ECS, see the  _Elastic Cloud Server User Guide_.
    -   For how to log in to a BMS, see the  _Bare Metal Server User Guide_.


## Creating and Mounting a Partition<a name="en-us_topic_0084935709_section36039836195351"></a>

The following example shows you how a new partition can be created on a new data disk that has been attached to a server. The partition will be created using parted, and GPT is used as the partition style. Furthermore, the partition will be formatted using the ext4 file system, mounted on  **/mnt/sdc**, and configured automatic mounting at system start.

1.  Run the following command to query information about the new data disk:

    **lsblk**

    Information similar to the following is displayed:

    ```
    root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  100G  0 disk
    ```

    In the command output, the server contains two disks.  **/dev/vda**  is the system disk, and  **/dev/vdb**  is the new data disk.

2.  Run the following command to enter parted to partition the new data disk:

    **parted** _New data disk_

    In this example, run the following command:

    **parted /dev/vdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# parted /dev/vdb
    GNU Parted 3.1
    Using /dev/vdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) 
    ```

3.  Enter  **p**  and press  **Enter**  to view the current disk partition style.

    Information similar to the following is displayed:

    ```
    (parted) p
    Error: /dev/vdb: unrecognised disk label
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 107GB
    Sector size (logical/physical): 512B/512B
    Partition Table: unknown
    Disk Flags:
    (parted) 
    ```

    In the command output, the  **Partition Table**  value is  **unknown**, indicating that no partition style is set for the new disk.

4.  Run the following command to set the disk partition style:

    **mklabel** _Disk partition style_

    In this example, run the following command to set the partition style to GPT: \(Disk partition styles can be MBR or GPT.\)

    **mklabel gpt**

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Because a data disk currently supports up to 32 TB, use the GPT partition style if your disk capacity is larger than 2 TB.  
    >If you change the disk partition style after the disk has been used, the data on the disk will be cleared. Therefore, select a proper disk partition style when initializing the disk.  

5.  Enter  **p**  and press  **Enter**  to view the disk partition style.

    Information similar to the following is displayed:

    ```
    (parted) mklabel gpt
    (parted) p
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 107GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start  End  Size  File system  Name  Flags
    
    (parted) 
    ```

    In the command output, the  **Partition Table**  value is  **gpt**, indicating that the disk partition style is GPT.

6.  Enter  **unit s**  and press  **Enter**  to set the measurement unit of the disk to sector.
7.  Run the following command and press  **Enter**:

    **mkpart **_Partition name Start sector __End sector_

    In this example, run the following command:

    **mkpart test 2048s 100%**

    In this example, one partition is created for the new data disk. Variable  _2048s_  indicates the disk start sector, and variable  _100%_  indicates the disk end sector. The two values are used for reference only. You can determine the number of partitions and the partition size based on your service requirements.

    Information similar to the following is displayed:

    ```
    (parted) mkpart opt 2048s 100%
    (parted)
    ```

8.  Enter  **p**  and press  **Enter**  to view details about the new partition.

    Information similar to the following is displayed:

    ```
    (parted) p
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 209715200s
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    
    Number  Start  End         Size        File system  Name  Flags
     1      2048s  209713151s  209711104s               test
    
    (parted) 
    ```

9.  Enter  **q**  and press  **Enter**  to exit parted.

    Information similar to the following is displayed:

    ```
    (parted) q
    Information: You may need to update /etc/fstab.
    ```

    You can set automatic disk mounting by updating the  **/etc/fstab**  file. Before updating the file, set the file system format for the partition and mount the partition on the mount point.

10. Run the following command to view the disk partition information:

    **lsblk**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# lsblk
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    vda    253:0    0   40G  0 disk
    └─vda1 253:1    0   40G  0 part /
    vdb    253:16   0  100G  0 disk
    └─vdb1 253:17   0  100G  0 part
    ```

    In the command output,  **/dev/vdb1**  is the partition you created.

11. Run the following command to set the file system format for the new partition:

    **mkfs** **-t** _File system format_ **/dev/vdb1**

    In this example, run the following command to set the  **ext4**  file system for the new partition:

    **mkfs -t ext4 /dev/vdb1**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# mkfs -t ext4 /dev/vdb1
    mke2fs 1.42.9 (28-Dec-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    6553600 inodes, 26213888 blocks
    1310694 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=2174746624
    800 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
            4096000, 7962624, 11239424, 20480000, 23887872
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    The formatting takes a period of time. Observe the system running status and do not exit.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >The partition sizes supported by file systems vary. Therefore, you are advised to choose an appropriate file system based on your service requirements.  

12. Run the following command to create a mount point:

    **mkdir** _Mount point_

    In this example, run the following command to create the  **/mnt/sdc**  mount point:

    **mkdir /mnt/sdc**

13. Run the following command to mount the new partition on the created mount point:

    **mount** _Disk partition_ _Mount point_

    In this example, run the following command to mount the new partition  **/dev/vdb1**  on  **/mnt/sdc**:

    **mount /dev/vdb1 /mnt/sdc**

14. Run the following command to view the mount result:

    **df -TH**

    Information similar to the following is displayed:

    ```
    [root@ecs-test-0001 ~]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/vda1      ext4       43G  1.9G   39G   5% /
    devtmpfs       devtmpfs  2.0G     0  2.0G   0% /dev
    tmpfs          tmpfs     2.0G     0  2.0G   0% /dev/shm
    tmpfs          tmpfs     2.0G  9.0M  2.0G   1% /run
    tmpfs          tmpfs     2.0G     0  2.0G   0% /sys/fs/cgroup
    tmpfs          tmpfs     398M     0  398M   0% /run/user/0
    /dev/vdb1      ext4      106G   63M  101G   1% /mnt/sdc
    ```

    New partition  **/dev/vdb1**  is mounted on  **/mnt/sdc**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the server is restarted, the mounting will become invalid. You can set automatic mounting for partitions at system start by modifying the  **/etc/fstab**  file. For details, see  [Setting Automatic Mounting at System Start](#en-us_topic_0084935709_section15839912195453).  


## Setting Automatic Mounting at System Start<a name="en-us_topic_0084935709_section15839912195453"></a>

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



