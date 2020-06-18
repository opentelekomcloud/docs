# Creating a Linux LVM Disk Partition for Docker<a name="cce_01_0200"></a>

This section describes how to check whether there are  **available raw disks**  and  **Linux LVM disk partitions**  and how to create  Linux LVM  disk partitions.

## Preparation<a name="section19834182211494"></a>

To improve the system stability, attach a data disk to Docker and use the  direct-lvm  mode.

## Procedure<a name="section18184888105"></a>

1.  <a name="li139011015111020"></a>Check whether available raw disks exist on the current node.
    1.  Log in to the target node as the  **root**  user.
    2.  Check the  raw disk  device.

        **lsblk -l | grep disk**

        If the following information is displayed, the raw disks named  **xvda**  and  **xvdb**  exist on the node.

        ```
        xvda  202:0    0   40G  0 disk
        xvdb  202:16   0  100G  0 disk
        ```

    3.  Check whether the raw disk is in use.

        **lsblk /dev/**_<devicename\>_

        _devicename_  indicates the raw disk name, for example,  **xvda**  and  **xvdb**  in the previous step.

        Run the  **lsblk /dev/xvda**  and  **lsblk /dev/xvdb**  commands. If the following information is displayed,  **xvda**  has been partitioned and used while  **xvdb**  is available. If no raw disk is available, bind an EVS disk to the node. It is advised that the disk space be no less than 80 GB.

        ```
        NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
        xvda    202:0    0   40G  0 disk
        ├─xvda1 202:1    0  100M  0 part /boot
        └─xvda2 202:2    0 39.9G  0 part /
        ```

        ```
        NAME MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
        xvdb 202:16   0  100G  0 disk
        ```

2.  Check whether there are partitions available. Currently, only Linux LVM partitions are supported.
    1.  Log in to the target node as the  **root**  user.
    2.  Check the partition whose system type is Linux LVM.

        **sfdisk -l 2\>\>/dev/null| grep "Linux LVM"**

        If the following information is displayed, two Linux LVM partitions,  **/dev/nvme0n1p1**  and  **/dev/nvme0n1p2**, exist in the system.

        ```
        /dev/nvme0n1p1          1  204800  204800  209715200   8e  Linux LVM
        /dev/nvme0n1p2     204801  409600  204800  209715200   8e  Linux LVM
        ```

    3.  Check whether the partition is in use.

        **lsblk  _<partdevice\>_**

        _<partdevice\>_  is the Linux LVM partition found in the previous step.

        In this example, run the  **lsblk/dev/nvme0n1p1**  and  **lsblk/dev/nvme0n1p2**  commands. If the following information is displayed, partition  **nvme0n1p**  is in use while  **nvme0n1p2**  is available.

        ```
        NAME                       MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
        nvme0n1p1                   259:3    0  200G  0 part
        └─vgpaas-thinpool_tdata   251:8    0  360G  0 lvm
          └─vgpaas-thinpool       251:10   0  360G  0 lvm
        ```

        ```
        NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
        nvme0n1p2 259:1    0  100G  0 part
        ```

        If no AZ is available, perform  [3](#li111391316141612)  to create a partition for the docker.

3.  <a name="li111391316141612"></a>Create a Linux LVM disk partition for the docker.
    1.  Run the following command to create a disk partition.  **devicename**  indicates the available raw disk name, for example,  **xvdb**  in  [1](#li139011015111020).

        **fdisk /dev/_devicename_**

    2.  Enter  **n**  to create a new partition. Enter  **p**  to display the primary partition number. Enter  **4**  to indicate the fourth primary partition.

        **Figure  1**  Creating a partition<a name="fig14533113219112"></a>  
        ![](figures/creating-a-partition.png "creating-a-partition")

    3.  Configure the start and last sectors as follows for example:

        ```
        Start sector (1048578048-4294967295, 1048578048 by default):
        1048578048
        Last sector, +sector or size {K, M, or G} (1048578048-4294967294, 4294967294 by default): +100G
        ```

        This configuration indicates that partition 4 has been set to the Linux type and the size is 100 GiB.

    4.  Enter  **t**  to change the partition system type. Enter the hex code  **8e**  when prompted to change the system type to Linux LVM.

        ```
        Command (enter m to obtain help): t
        Partition ID (ranging from 1 to 4, 4 by default): 4
        Hex code (enter L to list all codes): 8e
        This configuration changes the type of the partition Linux to Linux LVM.
        ```

    5.  Enter  **w**  to save the modification.

        ```
        Command (enter m to obtain help): w
        The partition table has been altered!
        ```

    6.  Run the  **partprobe**  command to refresh the disk partition.


