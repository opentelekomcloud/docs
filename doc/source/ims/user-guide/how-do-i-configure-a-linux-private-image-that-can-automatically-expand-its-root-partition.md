# How Do I Configure a Linux Private Image That Can Automatically Expand Its Root Partition?<a name="EN-US_TOPIC_0076880304"></a>

## Constraints<a name="section38936340165553"></a>

-   An image whose root partition file system is xfs cannot automatically expand its partitions.
-   An image that has the LVM partition cannot automatically expand its partitions.
-   Images whose file system is ext3 or ext4 are recommended.

    >![](/images/icon-note.gif) **NOTE:**   
    >After OS partitions of old versions are expanded, the OS must be restarted to update the file system.  


## Installation of growpart on Different OSs<a name="section9252000155656"></a>

To enable private images to automatically expand the root partition, install growpart.

**Table  1**  growpart installation packages for different OSs

<a name="table6390260216055"></a>
<table><thead align="left"><tr id="row2229091416055"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p973129916055"><a name="p973129916055"></a><a name="p973129916055"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p5003772716055"><a name="p5003772716055"></a><a name="p5003772716055"></a>Tool Package</p>
</th>
</tr>
</thead>
<tbody><tr id="row4768636616055"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3739042416055"><a name="p3739042416055"></a><a name="p3739042416055"></a>Debian/Ubuntu</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p872552316055"><a name="p872552316055"></a><a name="p872552316055"></a>cloud-init, cloud-utils, and cloud-initramfs-growroot</p>
</td>
</tr>
<tr id="row1142084816055"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5267351916055"><a name="p5267351916055"></a><a name="p5267351916055"></a>Fedora/CentOS</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3869664216055"><a name="p3869664216055"></a><a name="p3869664216055"></a>cloud-init, cloud-utils, and cloud-utils-growpart</p>
</td>
</tr>
<tr id="row1272546316055"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2412957216055"><a name="p2412957216055"></a><a name="p2412957216055"></a>SUSE/OpenSUSE</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p833829716055"><a name="p833829716055"></a><a name="p833829716055"></a>cloud-init and growpart</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For Debian 9, use method 1 to install growpart. If the installation fails, use method 2 to install growpart.  
>**Method 1**:  
>Run the following command to install growpart:  
>**apt-get install -y -f cloud-init cloud-utils cloud-initramfs-growroot**  
>**Method 2**:  
>If method 1 fails, it may be because the installation source of Debian 9.0.0 is faulty. Therefore, you need to download dependency packages  **cloud-utils**  and  **cloud-initramfs-growroot**  and install them.  
>1.  Run the following command to download the dependent packages:  
>    **wget  _Package download path_**  
>    You can obtain the dependent packages from the following paths:  
>    [http://ftp.br.debian.org/debian/pool/main/c/cloud-utils/cloud-utils\_0.29-1\_all.deb](http://ftp.br.debian.org/debian/pool/main/c/cloud-utils/cloud-utils_0.29-1_all.deb)  
>    [http://ftp.br.debian.org/debian/pool/main/c/cloud-initramfs-tools/cloud-initramfs-growroot\_0.18.debian5\_all.deb](http://ftp.br.debian.org/debian/pool/main/c/cloud-initramfs-tools/cloud-initramfs-growroot_0.18.debian5_all.deb)  
>2.  Run the following command to rectify the dependent packages:  
>    **apt --fix-broken install**  
>3.  Run the following command to install the dependent packages:  
>    **dpkg -i **_cloud-utils__ package path_** **_cloud-initramfs-growroot__ package path_  
>    An example command is  **dpkg -i /root/cloud-utils\_0.29-1\_all.deb /root/cloud-initramfs-growroot\_0.18.debian5\_all.deb**.  
>For other Debian versions, run the following command to install dependent packages:  
>**apt-get update;apt-get install cloud-utils cloud-initramfs-growroot**  

## Procedure<a name="section4041293916641"></a>

Take the following as two examples of image disk partitioning:

If the root partition is the last partition, see  [Root partition at the last](#li38782413161354).

If the root partition is not the last partition, see  [Root partition not at the last](#li17770807112053).

>![](/images/icon-note.gif) **NOTE:**   
>If the  **parted**  command fails, ensure that the  **parted**  tool has been installed on the OS. Perform the following operations to install the tool:  
>-   For CentOS, run the following command:  
>    **yum install parted**  
>-   For Debian, run the following command:  
>    **apt-get install parted**  

-   <a name="li38782413161354"></a>Root partition at the last \(**/dev/xvda1: swap**  and  **/dev/xvda2: root**\)

    For example, if the system disk size of CentOS 6.5 64-bit is 40 GB, perform the following operations to configure a Linux private image that can automatically expand its root partition:

    1.  Run the following command to query the partitions of  **/dev/xvda**:

        **parted -l /dev/xvda**

        As shown in the command output, the root partition is the second partition and is 38.7 GB.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.7GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        
        Number Start End Size Type File system Flags
        1 1049kB 4296MB 4295MB primary linux-swap(v1)
        2 4296MB 42.9GB 38.7GB primary ext4 boot
        ```

    2.  Install growpart to ensure that the image can automatically expand its root partition.

        Run the following command to install growpart:

        **yum install_ _cloud-\***

        >![](/images/icon-note.gif) **NOTE:**   
        >growpart may be contained in the  **cloud-utils-growpart/cloud-utils/cloud-initramfs-tools/cloud-init**  package. You can run the preceding command directly and then run the  **growpart**  command to check whether growpart has been installed successfully.  

    3.  Run the following command to obtain the file system type and UUID:

        **blkid**

        The command output is as follows:

        ```
        /dev/xvda1: UUID="25ec3bdb-ba24-4561-bcdc-802edf42b85f" TYPE="swap" 
        /dev/xvda2: UUID="1a1ce4de-e56a-4e1f-864d-31b7d9dfb547" TYPE="ext4" 
        ```

    4.  Stop the ECS and use it to create a private image.

        ```
        [root@sluo-ecs-e6dc-resizefs ~]# poweroff 
        Connection closed by foreign host.
        Disconnected from remote host at 11:08:54.
        Type `help´ to learn how to use Xshell prompt.
        ```

    5.  Use the created image to provision an ECS with a 50 GB system disk. Log in to the ECS and run the following command to query the expanded partitions:

        **parted -l /dev/xvda**

        As shown in the command output, the root partition has been expanded automatically.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 53.7GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        
        NumberStartEndSizeTypeFile systemFlags
        1 1049kB 4296MB 4295MB primary linux-swap(v1)
        2 4296MB 53.7GB 49.4GB primary ext4 boot
        ```

    6.  Run the following command to check whether disks are attached to the VM successfully:

        **df -Th**

        The command output is as follows:

        ```
        Filesystem     Type      Size    Used   Avail Use%  Mounted on
        /dev/xvda2     ext4      49.4G    2.6G  46.8G  4%   /dev/shm
        tmpfs          tmpfs     4295M    0     4295M  0%   / 
        ```


-   <a name="li17770807112053"></a>Root partition not at the last \(for example,  **/dev/xvda1: root**  and  **/dev/xvda2: swap**\)

    For example, if the system disk size of CentOS 7.3 64-bit is 40 GB, perform the following operations to configure a Linux private image that can automatically expand its root partition:

    1.  Run the following command to query the partitions of  **/dev/xvda**:

        **parted -l /dev/xvda**

        As shown in the command output, the root partition is the first partition and is 40.9 GB. The swap partition is the second partition.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.9GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End     Size    Type     File system     Flags
        1      1049kB  41.0GB  40.9GB  primary  ext4            boot
        2      41.0GB  42.9GB  2000MB  primary  linux-swap(v1)
        ```

    2.  Run the following command to check the configuration of the  **/etc/fstab**  file:

        **tail -n 3 /etc/fstab**

        As shown in the command output, UUIDs of the two partitions are displayed.

        ```
        #
        UUID=7c4fce5d-f8f7-4ed6-8463-f2bd22d0ddea /                       ext4    defaults        1 1
        UUID=5de3cf2c-30c6-4fb2-9e63-830439d4e674 swap                    swap    defaults        0 0
        ```

    3.  Run the following command to open the  **/etc/fstab**  file and press  **i**  to enter editing mode:

        **vi /etc/fstab**

    4.  Delete the swap partition configuration, press  **Esc**  to exit editing mode, and run the following command to save the configuration:

        **wq!**

    5.  Run the following command to check whether the configuration has been modified:

        **tail -n 3 /etc/fstab**

        As shown in the command output, only the UUID of the root partition is displayed.

        ```
        UUID=7c4fce5d-f8f7-4ed6-8463-f2bd22d0ddea /                       ext4    defaults        1 1
        ```

    6.  Run the following command to stop the swap device:

        **swapoff -a**

    7.  Run the following command to query the partitions of  **/dev/xvda**:

        **parted /dev/xvda**

        The command output is as follows:

        ```
        [root@test-0912 bin]# parted /dev/xvda
        GNU Parted 3.1
        Using /dev/xvda
        Welcome to GNU Parted! Type 'help' to view a list of commands.
        (parted) 
        ```

    8.  Run the following command to query the disk partitions:

        **p**

        The command output is as follows:

        ```
        (parted) p                                                     
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.9GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End     Size    Type     File system     Flags
         1      1049kB  4296MB  4295MB  primary  linux-swap(v1)
         2      4296MB  42.9GB  38.7GB  primary  xfs             boot
        (parted) 
        ```

    9.  Run the following command to delete the second partition:

        **rm 2**

        The command output is as follows:

        ```
        (parted) rm 2
        (parted)
        ```

    10. Run the following command to query the disk partitions:

        **p**

        The command output is as follows:

        ```
        (parted) p                                                               
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.9GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End     Size    Type     File system  Flags
        1      1049kB  41.0GB  40.9GB  primary  ext4         boot
        ```

    11. Type  **quit**.
    12. Run the following command to query the partitions of  **/dev/xvda**:

        **parted -l /dev/xvda**

        As shown in the command output, the swap partition is deleted.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.9GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End     Size    Type     File system  Flags
        1      1049kB  41.0GB  40.9GB  primary  ext4         boot
        ```

    13. Install growpart to ensure that the image can automatically expand its root partition.

        Run the following command to install growpart:

        **yum install_ _cloud-\***

        >![](/images/icon-note.gif) **NOTE:**   
        >growpart may be contained in the  **cloud-utils-growpart/cloud-utils/cloud-initramfs-tools/cloud-init**  package. You can run the preceding command directly and then run the  **growpart**  command to check whether growpart has been installed successfully.  

    14. Run the following command to expand the swap partition of the  **/dev/xvda**  disk to the first partition to which the root partition belongs:

        **growpart /dev/xvda 1**

        The following information is displayed:

        ```
        CHANGED: partition=1 start=2048 old: size=79978496 end=79980544 new: size=83873317,end=83875365
        ```

    15. Run the following command to query the partitions of  **/dev/xvda**:

        **parted -l /dev/xvda**

        As shown in the command output, the expanded root partition is 107 GB.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 42.9GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End     Size    Type     File system  Flags
        1      1049kB  42.9GB  42.9GB  primary  ext4         boot
        ```

    16. Run the following command to obtain the file system type and UUID:

        **blkid**

        The following information is displayed:

        ```
        /dev/xvda1: UUID="7c4fce5d-f8f7-4ed6-8463-f2bd22d0ddea" TYPE="ext4" 
        ```

    17. Stop the ECS and use it to create a private image.

        ```
        [root@sluo-ecs-e6dc-resizefs ~]# poweroff 
        Connection closed by foreign host.
        Disconnected from remote host at 11:08:54.
        Type `help´ to learn how to use Xshell prompt.
        ```

    18. Use the created image to provision an ECS with a 100 GB system disk. Log in to the ECS and run the following command to query the partitions of  **/dev/xvda**:

        **parted -l /dev/xvda**

        As shown in the command output, the root partition has been expanded automatically.

        ```
        Model: Xen Virtual Block Device (xvd)
        Disk /dev/xvda: 107GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags: 
        
        Number  Start   End    Size   Type     File system  Flags
         1      1049kB  107GB  107GB  primary  ext4         boot
        
        ```

        >![](/images/icon-note.gif) **NOTE:**   
        >The value of  **Size**  is the size of the expanded root partition.  



