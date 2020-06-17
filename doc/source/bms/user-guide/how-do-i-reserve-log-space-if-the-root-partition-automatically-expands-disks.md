# How Do I Reserve Log Space If the Root Partition Automatically Expands Disks?<a name="EN-US_TOPIC_0151841135"></a>

## Scenarios<a name="section68586510396"></a>

In the scenario where the root partition automatically expands disks, the initial root partition may occupy all space of the system disk. This section describes how to reserve log space.

## Procedure<a name="section19619191573914"></a>

1.  Run the  **lsblk**  command. The following command output indicates that the initial root partition has occupied all space of the system disk.

    ![](figures/7.png)

2.  Run the following command to create a directory for storing logs:

    **mkdir log**

    ![](figures/8.png)

3.  Run the following command to create a 200 GB image file for storing logs.

    **dd if=/dev/zero of=disk.img bs=1M count=200000**

    ![](figures/9-15.png)

4.  Run the following commands to virtualize the generated file into a block device and format it:

    **losetup /dev/loop0 disk.img**

    **mkfs.ext4 /dev/loop0**

    ![](figures/10.png)

5.  Run the following command to mount the image file to the log directory:

    **mount disk.img log**

    ![](figures/11-16.png)

6.  Create a file in the log directory.

    ![](figures/12.png)

7.  Run the following command to add the mount command to  **/etc/rc.local**:

    **mount /root/disk.img /root/log**

    ![](figures/13.png)

8.  Run the following command to restart the OS:

    **reboot**

    ![](figures/14.png)

9.  Run the  **lsblk**  command. The command output indicates that the image file has been mounted.

    ![](figures/15-17.png)


