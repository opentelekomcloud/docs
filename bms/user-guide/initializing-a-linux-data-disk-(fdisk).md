# Initializing a Linux Data Disk \(fdisk\)<a name="EN-US_TOPIC_0083737009"></a>

## Scenarios<a name="en-us_topic_0044524669_section31580524185332"></a>

This section uses CentOS 7.0 64-bit as an example.

The maximum disk capacity supported by MBR is 2 TB, and that supported by GPT is 18 EB. Therefore, use the GPT partition style if your disk capacity is greater than 2 TB. In Linux OSs, if the GPT partition style is used, the fdisk partitioning tool cannot be used. The parted partitioning tool must be used. For details about disk partition styles, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

The method for initializing a disk varies depending on the OSs running on the BMS. This document is for reference only. For detailed operations and differences, see the product documents of the OSs running on the corresponding BMSs.

## Prerequisites<a name="en-us_topic_0044524669_section117091356845"></a>

-   You have logged in to the BMS.
-   A data disk has been attached to the BMS and has not been initialized.

## Create Partitions and Attach a Disk<a name="en-us_topic_0044524669_section36039836195351"></a>

The following example shows you how to use fdisk to create a primary partition on a data disk that has been attached to the BMS. The default partitioning style is MBR and the default file system format is  **ext4**. Mount the file system to  **/mnt/sdc**, and configure automatic mounting upon system start.

1.  Run the following command to query information about the added data disk:

    **fdisk** **-l**

    Information similar to the following is displayed:

    ```
    [root@bms-b656 test]# fdisk -l
    
    Disk /dev/sda: 42.9 GB, 42949672960 bytes, 83886080 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x000cc4ad
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/xvda1   *        2048     2050047     1024000   83  Linux
    /dev/xvda2         2050048    22530047    10240000   83  Linux
    /dev/xvda3        22530048    24578047     1024000   83  Linux
    /dev/xvda4        24578048    83886079    29654016    5  Extended
    /dev/xvda5        24580096    26628095     1024000   82  Linux swap / Solaris
    
    Disk /dev/sdb: 10.7 GB, 10737418240 bytes, 20971520 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    ```

    The command output shows that the BMS has two disks, system disk  **/dev/sda**  and data disk  **/dev/sdb**.

2.  Run the following command to use fdisk to perform the partitioning operations for the added data disk:

    **fdisk** _Newly added data disk_

    For example, run the following command to use fdisk to perform the partitioning operations for the  **/dev/sdb**  data disk:

    **fdisk** **/dev/sdb**

    Information similar to the following is displayed:

    ```
    [root@ecs-b656 test]# fdisk /dev/sdb
    Welcome to fdisk (util-linux 2.23.2).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    Device does not contain a recognized partition table
    Building a new DOS disklabel with disk identifier 0xb00005bd.
    Command (m for help): 
    ```

3.  Enter  **n**  and press  **Enter**  to create a new partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): n
    Partition type:
       p   primary (0 primary, 0 extended, 4 free)
       e   extended
    ```

    There are two types of disk partitions:

    -   Choosing  **p**  creates a primary partition.
    -   Choosing  **e**  creates an extended partition.

4.  Recreate the partition with the same partition type as before. In this example a primary partition is used. Therefore, enter  **p**  and press  **Enter**  to create a primary partition.

    Information similar to the following is displayed:

    ```
    Select (default p): p
    Partition number (1-4, default 1):
    ```

    **Partition number**  indicates the serial number of the primary partition. The value can be  **1**  to  **4**.

5.  Enter the same partition number as the partition had before and press  **Enter**. Primary partition number  **1**  is used in this example.

    Information similar to the following is displayed:

    ```
    Partition number (1-4, default 1): 1
    First sector (2048-20971519, default 2048):
    ```

    **First sector**  indicates the start cylinder number. The value can be  **2048**  to  **20971519**, and the default value is  **2048**.

6.  Ensure that you enter the same first cylinder as the partition had before. In this example, we previously noted down  **2048**, so we type in  **2048**  here and press  **Enter**.

    Information similar to the following is displayed:

    ```
    First sector (2048-20971519, default 2048):
    Using default value 2048
    Last sector, +sectors or +size{K,M,G} (2048-20971519, default 20971519):
    ```

    **Last sector**  indicates the end cylinder number. The value can be  **2048**  to  **20971519**, and the default value is  **20971519**.

7.  In this example, select the default end cylinder number  **20971519**  and press  **Enter**.

    Information similar to the following is displayed:

    ```
    Last sector, +sectors or +size{K,M,G} (2048-20971519, default 20971519):
    Using default value 20971519
    Partition 1 of type Linux and of size 10 GiB is set
    Command (m for help):
    ```

    A primary partition has been created for a 10-GB data disk.

8.  Enter  **p**  and press  **Enter**  to view the details about the created partition.

    Information similar to the following is displayed:

    ```
    Command (m for help): p
    
    Disk /dev/sdb: 10.7 GB, 10737418240 bytes, 20971520 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0xb00005bd
    
       Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048    20971519    10484736   83  Linux
    
    Command (m for help): 
    ```

    Details about the  **/dev/sdb1**  partition are displayed.

9.  Enter  **w**  and press  **Enter**  to write the partition result into the partition table.

    Information similar to the following is displayed:

    ```
    Command (m for help): w
    The partition table has been altered!
    
    Calling ioctl() to re-read partition table.
    Syncing disks.
    ```

    The partition is successfully created.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In case that you want to discard the changes made before, you can exit fdisk by entering  **q**.  

10. Run the following command to synchronize the new partition table to the OS: 

    **partprobe**

11. Run the following command to set the format for the file system of the newly created partition:

    **mkfs** **-t** _File system format_ **/dev/sdb1**

    For example, run the following command to set the  **ext4**  file system for the  **/dev/xvdb1**  partition:

    **mkfs** **-t** **ext4** **/dev/sdb1**

    Information similar to the following is displayed:

    ```
    [root@bms-b656 test]# mkfs -t ext4 /dev/sdb1
    mke2fs 1.42.9 (28-Dec-2013)
    Filesystem label=
    OS type: Linux
    Block size=4096 (log=2)
    Fragment size=4096 (log=2)
    Stride=0 blocks, Stripe width=0 blocks
    655360 inodes, 2621184 blocks
    131059 blocks (5.00%) reserved for the super user
    First data block=0
    Maximum filesystem blocks=2151677952
    80 block groups
    32768 blocks per group, 32768 fragments per group
    8192 inodes per group
    Superblock backups stored on blocks:
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    The formatting takes a period of time. Observe the system running status, and do not exit.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >The partition sizes supported by file systems vary. Therefore, you are advised to choose an appropriate file system based on your service requirements.  

12. <a name="en-us_topic_0044524669_li1758111811323"></a>Run the following command to create a mount point:

    **mkdir** _Mount point_

    For example, run the following command to create the  **/mnt/sdc**  mount point:

    **mkdir** **/mnt/sdc**

13. Run the following command to mount the new partition on the mount point created in  [12](#en-us_topic_0044524669_li1758111811323):

    **mount** **/dev/sdb1** _Mount point_

    For example, run the following command to mount the newly created partition on  **/mnt/sdc**:

    **mount** **/dev/sdb1** **/mnt/sdc**

14. Run the following command to view the mount result:

    **df** **-TH**

    Information similar to the following is displayed:

    ```
    [root@bms-b656 test]# df -TH
    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/xvda2     xfs        11G  7.4G  3.2G  71% /
    devtmpfs       devtmpfs  4.1G     0  4.1G   0% /dev
    tmpfs          tmpfs     4.1G   82k  4.1G   1% /dev/shm
    tmpfs          tmpfs     4.1G  9.2M  4.1G   1% /run
    tmpfs          tmpfs     4.1G     0  4.1G   0% /sys/fs/cgroup
    /dev/sda3     xfs       1.1G   39M  1.1G   4% /home
    /dev/sda1     xfs       1.1G  131M  915M  13% /boot
    /dev/sdb1     ext4       11G   38M  9.9G   1% /mnt/sdc
    ```

    The newly created  **/dev/sdb1**  is mounted on  **/mnt/sdc**.


## Set Automatic Disk Attachment Upon BMS Start<a name="en-us_topic_0044524669_section15839912195453"></a>

To automatically attach a disk when a BMS starts, you should not specify its partition, for example  **/dev/sdb1**, in  **/etc/fstab**. This is because the sequence of cloud devices may change during the server start or stop process, for example, from  **/dev/sdb**  to  **/dev/sdc**. You are advised to use the universally unique identifier \(UUID\) in  **/etc/fstab**  to automatically attach a disk at system start.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The universally unique identifier \(UUID\) is the unique character string for disk partitions in a Linux system.  

1.  Run the following command to query the partition UUID:

    **blkid** _Disk partition_

    For example, run the following command to query the UUID of  **/dev/sdb1**:

    **blkid** **/dev/sdb1**

    Information similar to the following is displayed:

    ```
    [root@bms-b656 test]# blkid /dev/sdb1
    /dev/sdb1: UUID="1851e23f-1c57-40ab-86bb-5fc5fc606ffa" TYPE="ext4"
    ```

    The UUID of  **/dev/sdb1**  is displayed.

2.  Run the following command to open the  **fstab**  file using the vi editor:

    **vi** **/etc/fstab**

3.  Press  **i**  to enter the editing mode.
4.  Move the cursor to the end of the file and press  **Enter**. Then add the following information:

    ```
    UUID=1851e23f-1c57-40ab-86bb-5fc5fc606ffa /mnt/sdc      ext4 defaults     0   2
    ```

5.  Press  **Esc**, enter  **:wq**, and press  **Enter**.

    The system saves the configurations and exits the vi editor.


