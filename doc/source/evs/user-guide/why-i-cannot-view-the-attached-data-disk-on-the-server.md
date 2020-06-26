# Why I Cannot View the Attached Data Disk on the Server?<a name="evs_faq_0022"></a>

## Windows data disk<a name="section1894911274212"></a>

**Symptom**: A data disk has been attached to a Windows server on the management console, but the disk cannot be viewed on the server. For example, Volume \(D:\) does not appear in  **This PC**  of a Windows server running Windows Server 2012. Normally, Volume \(D:\) appears, as shown in  [Figure 1](#fig156291639133210).

**Figure  1**  Volume \(D:\) appears<a name="fig156291639133210"></a>  
![](figures/volume-(d-)-appears.png "volume-(d-)-appears")

**Solution**: A new data disk does not have partitions and file systems by default so that they will not appear in  **This PC**. You must manually initialize the disk.

For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

## Linux data disk<a name="section1514019519474"></a>

**Symptom**: A data disk has been attached to a Linux server on the management console, but the disk cannot be viewed on the server. For example, after the  **df -TH**  command is executed to view disk information in a Linux server running CentOS 7.4, only system disk  **/dev/vda1**  is displayed in the command output. Data disk  **/dev/vdb1**  does not appear.

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
```

**Solution**

-   **Method 1**: A new data disk does not have partitions and file systems by default so that they will not appear in the returned disk information. You must manually initialize the disk.

    For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

-   **Method 2**: If the data disk cannot be found after the server is restarted, automatic partition mounting at system start may not be configured. Perform the following steps:
    1.  Run the following command to mount the partition again:

        **mount** _Disk partition_ _Mount point_

        In this example, run the following command:

        **mount /dev/vdb1 /mnt/sdc**

        Perform the following steps to enable automatic partition mounting at system start:

    2.  <a name="li840964143216"></a>Run the following command to query the partition UUID:

        **blkid** _Disk partition_

        In this example, run the following command to query the UUID of the  **/dev/vdb1**  partition:

        **blkid /dev/vdb1**

        Information similar to the following is displayed:

        ```
        [root@ecs-test-0001 ~]# blkid /dev/vdb1
        /dev/vdb1: UUID="0b3040e2-1367-4abb-841d-ddb0b92693df" TYPE="ext4"
        ```

        The UUID of the  **/dev/vdb1**  partition is displayed.

    3.  Run the following command to open the  **fstab**  file using the vi editor:

        **vi /etc/fstab**

        Press  **i**  to enter the editing mode.

    4.  Move the cursor to the end of the file and press  **Enter**. Then, add the following information:

        ```
        UUID=0b3040e2-1367-4abb-841d-ddb0b92693df /mnt/sdc                ext4    defaults        0 2
        ```

        The preceding content is used for reference only. Add the information that is used in the environment. The parameters are described as follows:

        -   The first column indicates the partition UUID obtained in  [2](#li840964143216).
        -   The second column indicates the directory on which the partition is mounted. You can query the mount point using the  **df -TH**  command.
        -   The third column indicates the file system format of the partition. You can query the file system format using the  **df -TH**  command.
        -   The fourth column indicates the partition mount option. Normally, this parameter is set to  **defaults**.
        -   The fifth column indicates the Linux dump backup option.
            -   **0**: not use Linux dump backup. Normally, dump backup is not used, and you can set this parameter to  **0**.
            -   **1**: use Linux dump backup.

        -   The sixth column indicates the fsck option, that is, whether to use fsck to check the attached disk during startup.
            -   **0**: not use fsck.
            -   If the mount point is the root partition \(**/**\), this parameter must be set to  **1**.

                When this parameter is set to  **1**  for the root partition, this parameter for other partitions must start with  **2**  because the system checks the partitions in the ascending order of the values.


    5.  Press  **Esc**, enter  **:wq**, and press  **Enter**.

        The system saves the configurations and exits the vi editor.

        Perform the following operations to verify the automatic mounting function:

        1.  Run the following command to unmount the partition:

            **umount** _Disk partition_

            In this example, run the following command:

            **umount /dev/vdb1**

        2.  Run the following command to reload all the content in the  **/etc/fstab**  file:

            **mount -a**

        3.  Run the following command to query the file system mounting information:

            **mount | grep** _Mount point_

            In this example, run the following command:

            **mount | grep** **/mnt/sdc**

            If information similar to the following is displayed, the automatic mounting function takes effect:

            ```
            root@ecs-test-0001 ~]# mount | grep /mnt/sdc
            /dev/vdb1 on /mnt/sdc type ext4 (rw,relatime,data=ordered)
            ```




