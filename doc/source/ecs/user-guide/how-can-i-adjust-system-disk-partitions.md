# How Can I Adjust System Disk Partitions?<a name="EN-US_TOPIC_0076210995"></a>

## Scenarios<a name="section2442470814170"></a>

If the capacity of system disk partitions is inconsistent with the actual system disk capacity after an ECS is created, you can manually adjust the partitions to expand the system disk.

There are two ways to expand a system disk:

-   Take the empty partition as a new partition and attach this partition to a directory in the root partition after formatting it. You can perform the operations in this section.
-   Add the empty partition to the root partition to be expanded. For detailed operations, see the following:
    -   How can I add the empty partition of a system disk to be expanded to the end root partition online?
    -   How can I add the empty partition of a system disk to be expanded to the non-end root partition online?


## Procedure<a name="section2876888014177"></a>

Take an ECS running CentOS 7.3 64bit as an example. The system disk capacity is 60 GB when the ECS is created. However, the capacity of system disk partitions is only 40 GB.

To use the 20 GB capacity, performing the following operations to adjust system disk partitions:

1.  View disk partitions.
    1.  Log in to the ECS.
    2.  Run the following command to switch to user  **root**:

        **sudo su -**

    3.  Run the following command to view details about the ECS disk:

        **fdisk -l**

        In the following command output,  **/dev/xvda**  or  **/dev/vda**  indicates the system disk.

        ![](figures/Viewing-details-about-the-ECS-disk.png)

    4.  Run the following command to view disk partitions:

        **parted -l /dev/xvda**

        ![](figures/Viewing-disk-partitions.jpg)

2.  Create a partition for the expanded system disk capacity.
    1.  Run the following command to switch to the fdisk mode \(taking  **/dev/xvda**  as an example\):

        **fdisk /dev/xvda**

        Information similar to the following is displayed:

        ```
        [root@ecs-8d6c ]# fdisk /dev/xvda
        Welcome to fdisk (util-linux 2.23.2).
        
        Changes will remain in memory only, until you decide to write them.
        Be careful before using the write command.
        
        Command (m for help):
        ```

    2.  Enter  **n**  and press  **Enter**  to create a new partition.

        Because the system disk has two existing partitions, the system automatically creates the third one.

        Information similar to the following is displayed.

        ![](figures/Creating-a-new-partition.png)

    3.  Enter the new partition's start cylinder number and press  **Enter**.

        The start cylinder number must be greater than the end cylinder numbers of existing partitions. In this example, use the default value for the new partition's start cylinder number and press  **Enter**. Information similar to the following is displayed.

        ![](figures/Specifying-the-new-partition-start-cylinder-number.jpg)

    4.  Enter the new partition's end cylinder number and press  **Enter**.

        In this example, use the default value for the new partition's end cylinder number and press  **Enter**. Information similar to the following is displayed.

        ![](figures/Specifying-the-new-partition-end-cylinder-number.jpg)

    5.  Enter  **p**  and press  **Enter**  to view the created partition.

        Information similar to the following is displayed.

        ![](figures/Viewing-the-created-partition.jpg)

    6.  Enter  **w**  and press  **Enter**. The system saves and exits the partition.

        The system automatically writes the partition result into the partition list. Then, the partition is created.

        Information similar to the following is displayed.

        ![](figures/Completing-the-partition-creation.jpg)

    7.  Run the following command to view disk partitions:

        **parted -l /dev/xvda**

        ![](figures/Viewing-disk-partitions-02.jpg)

3.  Run the following command to synchronize the modifications in the partition list with the OS:

    **partprobe**

4.  Configure the type of the new partition file system.
    1.  Run the following command to view the type of the file system:

        **df -TH**

        ![](figures/Viewing-the-file-system-type.png)

    2.  Run the following command to format the partition \(taking the  **ext4**  type as an example\):

        **mkfs -t ext4 /dev/xvda3**

        >![](/images/icon-note.gif) **NOTE:**   
        >Formatting the partition requires a period of time. During this time, observe the system running status and do not exit the system.  

        Information similar to the following is displayed:

        ```
        [root@ecs-86dc ]# mkfs -t ext4 /dev/xvda3
        mke2fs 1.42.9 (28-Dec-2013)
        Filesystem label=
        OS type: Linux
        Block size=4096 (log=2)
        Fragment size=4096 (log=2)
        Stride=0 blocks, Stripe width=0 blocks
        1790544 inodes, 7156992 blocks
        357849 blocks (5.00%) reserved for the super user
        First data block=0
        Maximum filesystem blocks=2155872256
        219 block groups
        32768 blocks per group, 32768 fragments per group
        8176 inodes per group
        Superblock backups stored on blocks:
                32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
                4096000
        
        Allocating group tables: done
        Writing inode tables: done
        Creating journal (32768 blocks): done
        Writing superblocks and filesystem accounting information: done
        ```

5.  Mount the new partition to the target directory.

    If the new partition is mounted to a directory that is not empty, the subdirectories and files in the directory will be hidden. Therefore, you are advised to mount the new partition to an empty directory or a newly created directory. If the new partition must be mounted to a directory that is not empty, move the subdirectories and files in the directory to another directory temporarily. After the partition is mounted, move the subdirectories and files back.

    Take the newly created directory  **/root/new**  as an example.

    1.  Run the following command to create the  **/root/new**  directory:

        **mkdir /root/new**

    2.  Run the following command to mount the new partition to the  **/root/new**  directory:

        **mount /dev/xvda3 /root/new**

        Information similar to the following is displayed:

        ```
        [root@ecs-86dc ]# mount /dev/xvda3 /root/new
        [root@ecs-86dc ]#
        ```

    3.  Run the following command to view the mounted file systems:

        **df -TH**

        Information similar to the following is displayed:

        ![](figures/Viewing-the-mounted-file-systems.jpg)

6.  Determine whether to set automatic mounting upon system startup for the new disk.

    If you do not set automatic mounting upon system startup, you must mount the new partition to the specified directory again after the ECS is restarted.

    -   If automatic mounting is required, go to  [7](#li51885379162851).
    -   If automatic mounting is not required, no further action is required.

7.  <a name="li51885379162851"></a>Set automatic mounting upon system startup for the new disk.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >Do not set automatic mounting upon system startup for unformatted disks, which will cause ECS startup failures.  

    1.  Run the following command to obtain the file system type and UUID:

        **blkid**

        ![](figures/Viewing-the-file-system-type.jpg)

        According to the preceding figure, the UUID of the new partition is 96e5e028-b0fb-4547-a82a-35ace1086c4f.

    2.  Run the following command to open the  **fstab**  file using the vi editor:

        **vi /etc/fstab**

    3.  Press  **i**  to enter editing mode.
    4.  Move the cursor to the end of the file and press  **Enter**. Then add the following information:

        **UUID=96e5e028-b0fb-4547-a82a-35ace1086c4f /root/new ext4 defaults 0 0**

    5.  Press  **Esc**, run the following command, and press  **Enter**. The system saves the configurations and exits the vi editor.

        **:wq**

    >![](/images/icon-note.gif) **NOTE:**   
    >If a new disk for which automatic mounting upon system startup has been set must be detached, you must delete the automatic mounting configuration before detaching the disk. Otherwise, starting the ECS will fail after the disk is detached. To delete the automatic mounting configuration, perform the following operations:  
    >1.  Run the following command to open the  **fstab**  file using the vi editor:  
    >    **vi /etc/fstab**  
    >2.  Press  **i**  to enter editing mode.  
    >3.  Delete the following statement:  
    >    **UUID=96e5e028-b0fb-4547-a82a-35ace1086c4f /root/new ext4 defaults 0 0**  
    >4.  Press  **Esc**, run the following command, and press  **Enter**. The system saves the configurations and exits the vi editor.  
    >    **:wq**  


