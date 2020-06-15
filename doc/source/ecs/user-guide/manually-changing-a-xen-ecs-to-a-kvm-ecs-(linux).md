# Manually Changing a Xen ECS to a KVM ECS \(Linux\)<a name="EN-US_TOPIC_0200552469"></a>

## Scenarios<a name="section9265624184119"></a>

Before changing a Xen ECS running Linux to a KVM ECS, install and configure desired drivers.

This section describes how to manually install drivers on a Linux ECS, configure automatic disk attachment, and change Xen to KVM.

For instructions about how to use a script to automatically install drivers, see  [Automatically Changing a Xen ECS to a KVM ECS \(Linux\)](automatically-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md).

>![](/images/icon-note.gif) **NOTE:**   
>-   Xen ECSs include S1, C1, C2, and M1 ECSs.  
>-   To obtain KVM ECSs, see the  **Virtualization Type**  column in  [ECSs](ecs-specifications.md).  
>-   To support both Xen and KVM, Linux ECSs require the xen-pv and Virtio drivers. Before changing a Xen ECS to a KVM ECS, make sure that the Linux ECS has been configured, including installing drivers and configuring automatic disk attachment.  

## Constraints<a name="section32289014501"></a>

-   If a Linux ECS is attached with a logical LVM disk or a RAID disk array consisting of multiple physical disks, the ECS specifications cannot be modified. Otherwise, data may be lost.
-   A Xen ECS with more than 24 VBD disks attached cannot be changed to a KVM ECS.
-   A Xen ECS can be changed to a KVM ECS, but a KVM ECS cannot be changed to a Xen ECS.

## Procedure<a name="section117911026122211"></a>

[Figure 1](#fig1685151934912)  shows the flowchart for manually changing a Xen ECS to a KVM ECS.

**Figure  1**  Flowchart for manually changing a Xen ECS to a KVM ECS<a name="fig1685151934912"></a>  
![](figures/flowchart-for-manually-changing-a-xen-ecs-to-a-kvm-ecs.png "flowchart-for-manually-changing-a-xen-ecs-to-a-kvm-ecs")

**Table  1**  Procedure for manually changing a Xen ECS to a KVM ECS

<a name="table1286142613223"></a>
<table><thead align="left"><tr id="row38601426132214"><th class="cellrowborder" valign="top" width="35.4%" id="mcps1.2.3.1.1"><p id="p10860142632210"><a name="p10860142632210"></a><a name="p10860142632210"></a>Step</p>
</th>
<th class="cellrowborder" valign="top" width="64.60000000000001%" id="mcps1.2.3.1.2"><p id="p4860226192217"><a name="p4860226192217"></a><a name="p4860226192217"></a>Task</p>
</th>
</tr>
</thead>
<tbody><tr id="row12860162652214"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p086062642211"><a name="p086062642211"></a><a name="p086062642211"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p173474421306"><a name="p173474421306"></a><a name="p173474421306"></a><a href="#section125278281411">(Optional) Step 1: Back Up System Disk Data</a></p>
</td>
</tr>
<tr id="row28601626182218"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p5860192632218"><a name="p5860192632218"></a><a name="p5860192632218"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p4860526112216"><a name="p4860526112216"></a><a name="p4860526112216"></a><a href="#section69551357194518">Step 2: Install Drivers</a></p>
</td>
</tr>
<tr id="row138618263229"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p386032662215"><a name="p386032662215"></a><a name="p386032662215"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p4860162642215"><a name="p4860162642215"></a><a name="p4860162642215"></a><a href="#section181471144418">Step 3: Check Whether the ECS Has Been Configured</a></p>
</td>
</tr>
<tr id="row38612269223"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p1686111268228"><a name="p1686111268228"></a><a name="p1686111268228"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p9535155112717"><a name="p9535155112717"></a><a name="p9535155112717"></a><a href="#section1815152131917">Step 4: Modify Specifications</a></p>
</td>
</tr>
<tr id="row11861126192210"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p1086182642219"><a name="p1086182642219"></a><a name="p1086182642219"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p6861326162215"><a name="p6861326162215"></a><a name="p6861326162215"></a><a href="#section2625525131519">(Optional) Step 5: Check Disk Attachment</a></p>
</td>
</tr>
</tbody>
</table>

## \(Optional\) Step 1: Back Up System Disk Data<a name="section125278281411"></a>

Before modifying the specifications, back up the system disk, configure the ECS, and install the driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. If the ECS becomes unavailable, the fault can be rectified by reinstalling the OS, which may cause data loss in your system disk.

For instructions about how to back up the system disk, see "Getting Started \>  [Creating a VBS Backup](https://docs.otc.t-systems.com/en-us/usermanual/vbs/en-us_topic_0015667820.html)" in  _Volume Backup Service User Guide_.

## Step 2: Install Drivers<a name="section69551357194518"></a>

Perform the operations described in this section if your ECS does not support the configuration using a script.

1.  Log in to the ECS.
2.  Uninstall Tools from the ECS.

    For details, see  [Uninstalling the PV Driver from a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0037352186.html).

3.  Change the GRUB disk ID to UUID.

    For details, see  [Changing the Disk Identifier of the GRUB Configuration File to UUID](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0086020895.html).

4.  Change the fstab disk ID to UUID.

    For details, see  [Changing the Disk Identifier of the fstab File to UUID](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0086024961.html).

5.  Install native Xen and KVM drivers.

    For details, see  [Installing Native Xen and KVM Drivers](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0086020894.html).


## Step 3: Check Whether the ECS Has Been Configured<a name="section181471144418"></a>

Perform the following operations to check whether the drivers have been installed and the configuration files have been modified.

>![](/images/icon-notice.gif) **NOTICE:**   
>Before manually configuring an ECS, perform the following operations to check existing ECS configurations.  

1.  Log in to the ECS.
2.  Run the following command to check whether the root partition is in UUID format:

    **cat /boot/grub/grub.cfg**

    -   If yes, the disk ID in the GRUB configuration file has been changed to UUID.
    -   If no, the modification failed. In such a case, change the GRUB disk ID to UUID again.

    ```
    ...menuentry 'Ubuntu Linux, with Linux 3.13.0-24-generic' --class ubuntu --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.13.0-24-generic-advanced-ec51d860-34bf-4374-ad46-a0c3e337fd34' {
    recordfail
    load_video
    gfxmode $linux_gfx_mode
    insmod gzio
    insmod part_msdos
    insmod ext2
    if [ x$feature_platform_search_hint = xy ]; then
    search --no-floppy --fs-uuid --set=root ec51d860-34bf-4374-ad46-a0c3e337fd34
    else
    search --no-floppy --fs-uuid --set=root ec51d860-34bf-4374-ad46-a0c3e337fd34
    fi
    echo 'Loading Linux 3.13.0-24-generic ...'
    linux /boot/vmlinuz-3.13.0-24-generic root=UUID=ec51d860-34bf-4374-ad46-a0c3e337fd34 ro
    echo 'Loading initial ramdisk ...'
    initrd /boot/initrd.img-3.13.0-24-generic
    }
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >The path in which the GRUB configuration file is stored varies depending on the OS. For example, the path can be  **/boot/grub/menu.lst**,  **/boot/grub/grub.cfg**,  **/boot/gurb2/grub.cfg**, or  **/boot/grub/grub.conf**.  

3.  Run the following command to check whether the disk ID in the fstab configuration file is UUID:

    **cat /etc/fstab**

    -   If yes, the disk ID has been changed to UUID.
    -   If no, the modification failed. In such a case, change the fstab disk ID to UUID again.

    ```
    [root@****** ~]# cat /etc/fstab 
    UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130  /       xfs     defaults    0 0
    UUID=2de37c6b-2648-43b4-a4f5-40162154e135  swap    swap    defaults    0 0
    ```

4.  Check whether the native Xen and KVM drivers have been installed.

    -   If the boot virtual file system is initramfs, run the following commands:

        **lsinitrd /boot/initramfs-\`uname -r\`.img | grep xen**

        **lsinitrd /boot/initramfs-\`uname -r\`.img | grep virtio**

    -   If the boot virtual file system is initrd, run the following commands:

        **lsinitrd /boot/initrd-\`uname -r\` | grep xen**

        **lsinitrd /boot/initrd-\`uname -r\` | grep virtio**

    If the names of the native Xen and KVM drivers are displayed in the command output, the drivers have been installed.

    ```
    [root@CTU10000xxxxx home]# lsinitrd /boot/initramfs-`uname -r`.img | grep xen 
    -rwxr--r--   1 root     root        54888 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/block/xen-blkfront.ko 
    -rwxr--r--   1 root     root        45664 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/net/xen-netfront.ko 
     
    [root@CTU10000xxxxx home]# lsinitrd /boot/initramfs-`uname -r`.img | grep virtio 
    -rwxr--r--   1 root     root        23448 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/block/virtio_blk.ko 
    -rwxr--r--   1 root     root        50704 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/net/virtio_net.ko 
    -rwxr--r--   1 root     root        28424 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/scsi/virtio_scsi.ko 
    drwxr-xr-x   2 root     root            0 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/virtio 
    -rwxr--r--   1 root     root        14544 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/virtio/virtio.ko 
    -rwxr--r--   1 root     root        21040 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/virtio/virtio_pci.ko 
    -rwxr--r--   1 root     root        18016 Jul 16 17:53 lib/modules/2.6.32-573.8.1.el6.x86_64/kernel/drivers/virtio/virtio_ring.ko
    ```


>![](/images/icon-notice.gif) **NOTICE:**   
>Make sure that the ECS has been configured successfully. Otherwise, the ECS will be unavailable after the modification is performed.  

## Step 4: Modify Specifications<a name="section1815152131917"></a>

1.  Log in to management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, view the status of the target ECS.

    If the ECS is not in  **Stopped**  state, click  **More**  in the  **Operation**  column and select  **Stop**.

5.  Click  **More**  in the  **Operation**  column and select  **Modify Specifications**.

    The  **Modify ECS Specifications**  page is displayed.

6.  Select the new ECS type, vCPUs, and memory as prompted.
7.  \(Optional\) Set  **DeH**.

    If the ECS is created on a DeH, the system allows you to change the DeH.

    To do so, select the target DeH from the drop-down list. If no DeH is available in the drop-down list, remaining DeH resources are insufficient and cannot be used to create the ECS with specifications modified.

8.  Select the check box to confirm the ECS configuration.
9.  Click  **OK**.

## \(Optional\) Step 5: Check Disk Attachment<a name="section2625525131519"></a>

After a Xen ECS is changed to a KVM ECS, disk attachment may fail. Therefore, check disk attachment after specifications modification. If disks are properly attached, the specifications modification is successful.

-   Linux

    For details, see  [What Should I Do If the Disk of a Linux ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-disk-of-a-linux-ecs-becomes-offline-after-the-ecs-specifications-are-modifie.md)


## Follow-up Procedure<a name="section7460163511720"></a>

If the ECS with specifications modified is displayed in the ECS list but its OS cannot be started after the ECS is remotely logged in, reinstall the ECS OS to rectify this fault. For details, see  [Reinstalling the OS](reinstalling-the-os.md).

