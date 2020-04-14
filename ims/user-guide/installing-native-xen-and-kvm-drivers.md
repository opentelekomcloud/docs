# Installing Native Xen and KVM Drivers<a name="EN-US_TOPIC_0086020894"></a>

## Scenarios<a name="section15570104113511"></a>

When optimizing a Linux private image, you need to install  native Xen and KVM drivers  on the ECS.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>If you do not install the Xen driver, the ECS network performance will be poor, and the security group and firewall configured for the ECS will not take effect.  
>If you do not install the KVM driver, NICs of the ECS may not be detected and the ECS cannot communicate with other resources. Therefore, you must install Xen and KVM drivers.  

Edit the configuration file based on the OS version.

-   CentOS, EulerOS

    Take CentOS 7.0 as an example. Modify the  **/etc/dracut.conf**  file. Add the xen-pv and VirtIO drivers to  **add\_drivers**. xen-pv drivers include xen-blkfront and xen-netfront. VirtIO drivers include virtio\_blk, virtio\_scsi, virtio\_net, virtio\_pci, virtio\_ring, and virtio. Separate drive names with spaces. Save and exit the  **/etc/dracut.conf**  file. Run the  **dracut -f**  command to regenerate initrd.

    For details, see  [CentOS, EulerOS](#section57411552112542).

-   Ubuntu and Debian

    Modify the  **/etc/initramfs-tools/modules**  file. Add the xen-pv and VirtIO drivers. xen-pv drivers include xen-blkfront and xen-netfront. VirtIO drivers include virtio\_blk, virtio\_scsi, virtio\_net, virtio\_pci, virtio\_ring, and virtio. Separate drive names with spaces. Save and exit the  **/etc/initramfs-tools/modules**  file. Run the  **update-initramfs -u**  command to regenerate initrd.

    For details, see  [Ubuntu and Debian](#section1865536911274).

-   For SUSE and openSUSE, edit different configuration files based on the OS version.

    -   If the OS version is earlier than SUSE 12 SP1 or OpenSUSE 13, modify the  **/etc/sysconfig/kernel**  file and add xen-pv and VirtIO drivers to  **INITRD\_MODULES=""**. xen-pv drivers include xen\_vnif, xen\_vbd, and xen\_platform\_pci. VirtIO drivers include virtio\_blk, virtio\_scsi, virtio\_net, virtio\_pci, virtio\_ring, and virtio. Separate driver names with spaces. Run the  **mkinitrd**  command to regenerate initrd.
    -   If the OS version is SUSE 12 SP1, modify the  **/etc/dracut.conf**  file and add xen-pv and VirtIO drivers to  **add\_drivers**. xen-pv drivers include xen\_vnif, xen\_vbd, and xen\_platform\_pci. VirtIO drivers include virtio\_blk, virtio\_scsi, virtio\_net, virtio\_pci, virtio\_ring, and virtio. Separate driver names with spaces. Run the  **dracut -f**  command to regenerate initrd.
    -   If the OS version is later than SUSE 12 SP1 or openSUSE 13, modify the  **/etc/dracut.conf**  file and add xen-pv and VirtIO drivers to  **add\_drivers**. xen-pv drivers include xen-blkfront and xen-netfront. VirtIO drivers include virtio\_blk, virtio\_scsi, virtio\_net, virtio\_pci, virtio\_ring, and virtio. Separate drive names with spaces. Save and exit the  **/etc/dracut.conf**  file. Run the  **dracut -f**  command to regenerate initrd.

    For details, see  [SUSE and openSUSE](#section63790002112835).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For SUSE, run the following command to check that xen-kmp \(driver package for xen-pv\) is installed:  
    >**rpm** **-qa** **|grep** **xen-kmp**  
    >The following information is displayed:  
    >```  
    >xen-kmp-default-4.2.2_04_3.0.76_0.11-0.7.5  
    >```  
    >If xen-kmp is not installed, obtain it from the ISO file and install it first.  
    >If you add built-in drivers to the initrd or initramfs file by mistake, the ECS will not be affected.  


## Prerequisites<a name="section19907254112223"></a>

-   ECSs that use native Linux Xen and KVM drivers must have a kernel later than the 2.6.24 version.
-   It is recommended that you disable your antivirus and intrusion detection software. You can enable the software again after Xen and KVM drivers are installed.

## CentOS, EulerOS<a name="section57411552112542"></a>

1.  Run the following command to open the  **/etc/dracut.conf**  file:

    **vi** **/etc/dracut.conf**

2.  Press  **i**  to enter editing mode and add the xen-pv and VirtIO drivers to  **add\_drivers**  \(the format depends on the OS requirements\).

    ```
    [root@CTU10000xxxxx ~]# vi /etc/dracut.conf 
    # additional kernel modules to the default 
    add_drivers+="xen-blkfront xen-netfront virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio" 
    ......
    ```

3.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the change and exits the  **/etc/dracut.conf**  file.
4.  Run the following command to generate initrd again:

    **dracut** **-f** **/boot/initramfs-2.6.32-573.8.1.el6.x86\_64.img**

    If the virtual file system is not the default initramfs, run the  **dracut -f**_Name of the initramfs or initrd file actually used_  command. The actual initramfs or initrd file name can be obtained from the GRUB configuration file, which can be  **/boot/grub/grub.cfg**,  **/boot/gurb2/grub.cfg**, or  **/boot/grub/grub.conf**  depending on the OS.

5.  If the virtual file system is initramfs, run the following commands to check whether native Xen and KVM drivers have been loaded:

    **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **xen**

    **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **virtio**

    If the virtual file system is initrd, run the following commands to check whether native Xen and KVM drivers have been loaded:

    **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **xen**

    **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **virtio**

    If the virtual file system is initramfs, the following information is displayed:

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

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you add built-in drivers to the initrd or initramfs file, the ECS will not be affected. This makes it easy to modify the drivers. However, you cannot check the drivers by running the  **lsinitrd**  command. You can run the following commands to check whether the drivers are built-in ones in the kernel:  
    >**cat** **/boot/config-\`uname -r\`** **|** **grep** **CONFIG\_VIRTIO** **|** **grep** **y**  
    >**cat** **/boot/config-\`uname -r\`** **|** **grep** **CONFIG\_XEN** **|** **grep** **y**  


## Ubuntu and Debian<a name="section1865536911274"></a>

1.  Run the following command to open the  **modules**  file:

    **vi** **/etc/initramfs-tools/modules**

2.  Press  **i**  to enter editing mode and add the xen-pv and VirtIO drivers to the  **/etc/initramfs-tools/modules**  file \(the format depends on the OS requirements\).

    ```
    [root@CTU10000xxxxx ~]#vi /etc/initramfs-tools/modules 
    ......
    # Examples: 
    # 
    # raid1 
    # sd_mOd 
    xen-blkfront
    xen-netfront
    virtio_blk
    virtio_scsi
    virtio_net
    virtio_pci
    virtio_ring
    virtio
    ```

3.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the change and exits the  **/etc/initramfs-tools/modules**  file.
4.  Run the following command to generate initrd again:

    **update-initramfs** **-u**

5.  Run the following commands to check whether native Xen and KVM drivers have been installed:

    **lsinitramfs** **/boot/initrd.img-\`uname** **-r\`** **|grep** **xen**

    **lsinitramfs** **/boot/initrd.img-\`uname** **-r\`** **|grep** **virtio**

    ```
    [root@ CTU10000xxxxx home]# lsinitramfs /boot/initrd.img-`uname -r` |grep xen 
    lib/modules/3.5.0-23-generic/kernel/drivers/net/ethernet/qlogic/netxen 
    lib/modules/3.5.0-23-generic/kernel/drivers/net/ethernet/qlogic/netxen/netxen_nic.ko 
    lib/modules/3.5.0-23-generic/kernel/drivers/net/xen-netback 
    lib/modules/3.5.0-23-generic/kernel/drivers/net/xen-netback/xen-netback.ko 
    lib/modules/3.5.0-23-generic/kernel/drivers/block/xen-blkback 
    lib/modules/3.5.0-23-generic/kernel/drivers/block/xen-blkback/xen-blkback.ko 
     
    [root@ CTU10000xxxxx home]# lsinitramfs /boot/initrd.img-`uname -r` |grep virtio 
    lib/modules/3.5.0-23-generic/kernel/drivers/scsi/virtio_scsi.ko
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you add built-in drivers to the initrd or initramfs file, the ECS will not be affected. This makes it easy to modify the drivers. However, you cannot check the drivers by running the  **lsinitrd**  command. You can run the following commands to check whether the drivers are built-in ones in the kernel:  
    >```  
    >[root@ CTU10000xxxxx home]# cat /boot/config-`uname -r` | grep CONFIG_VIRTIO | grep y  
    >CONFIG_VIRTIO_BLK=y  
    >CONFIG_VIRTIO_NET=y  
    >CONFIG_VIRTIO=y  
    >CONFIG_VIRTIO_RING=y  
    >CONFIG_VIRTIO_PCI=y  
    >CONFIG_VIRTIO_MMIO_CMDLINE_DEVICES=y  
    >[root@ CTU10000xxxxx home]# cat /boot/config-`uname -r` | grep CONFIG_XEN | grep y  
    >CONFIG_XEN_BLKDEV_FRONTEND=y  
    >CONFIG_XEN_NETDEV_FRONTEND=y  
    >```  


## SUSE and openSUSE<a name="section63790002112835"></a>

If the OS version is earlier than SUSE 12 SP1 or OpenSUSE 13, modify the  **/etc/sysconfig/kernel**  file. For details, see  [scenario 1](#en-us_topic_0037352187_li4339952312044).

If the OS version is SUSE 12 SP1, modify the  **/etc/dracut.conf**  file and add xen-pv and VirtIO drivers. For details, see  [scenario 2](#li45512494152649).

If the OS version is later than SUSE 12 SP1 or openSUSE 13, modify the  **/etc/dracut.conf**  file and add xen-pv and VirtIO drivers to  **add\_drivers**. For details, see  [scenario 3](#en-us_topic_0037352187_li57696863113515).

-   <a name="en-us_topic_0037352187_li4339952312044"></a>If the OS version is earlier than SUSE 12 SP1 or openSUSE 13, perform the following steps:

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For SUSE, run the following command to check that xen-kmp \(driver package for xen-pv\) is installed:  
    >**rpm** **-qa** **|grep** **xen-kmp**  
    >The following information is displayed:  
    >```  
    >xen-kmp-default-4.2.2_04_3.0.76_0.11-0.7.5  
    >```  
    >If xen-kmp is not installed, obtain it from the installation ISO and install it first.  

    1.  Run the following command to modify the  **/etc/sysconfig/kernel**  file:

        ****vi**** **etc/sysconfig/kernel**

    2.  Add the xen-pv and VirtIO drivers after  **INITRD\_MODULES=**  \(the format of drivers depends on the OS\).

        ```
        SIA10000xxxxx:~ # vi /etc/sysconfig/kernel 
        # (like drivers for scsi-controllers, for lvm or reiserfs)
        #
        INITRD_MODULES="ata_piix ata_generic xen_vnif xen_vbd xen_platform_pci virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio"
        ```

    3.  Run the  **mkinitrd**  command to generate initrd again:

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the virtual file system is not the default initramfs or initrd, run the  **dracut -f** _Name of the initramfs or initrd file actually used_  command. The name of the initramfs or initrd file used can be obtained from the  **menu.lst**  or  **grub.cfg**  file \(**/boot/grub/menu.lst**,  **/boot/grub/grub.cfg**, or  **/boot/gurb2/grub.cfg**\).  

        The following is an example initrd file of SUSE 11 SP4:

        ```
        default 0
        timeout 10
        gfxmenu (hd0,0)/boot/message
        title sles11sp4_001_[_VMX_]
        root (hd0,0)
        kernel /boot/linux.vmx vga=0x314 splash=silent console=ttyS0,115200n8 console=tty0 net.ifnames=0 NON_PERSISTENT_DEVICE_NAMES=1 showopts
        initrd /boot/initrd.vmx
        title Failsafe_sles11sp4_001_[_VMX_]
        root (hd0,0)
        kernel /boot/linux.vmx vga=0x314 splash=silent ide=nodma apm=off noresume edd=off powersaved=off nohz=off highres=off processsor.max+cstate=1 nomodeset x11failsafe console=ttyS0,115200n8 console=tty0 net.ifnames=0 NON_PERSISTENT_DEVICE_NAMES=1 showopts
        initrd /boot/initrd.vmx
        ```

        **/boot/initrd.vmx**  in the  **initrd**  row is the  **initrd**  file actually used. Run the  **dracut -f /boot/initrd.vmx**  command. If the  **initrd**  file does not contain the  **/boot**  directory, such as  **/initramfs-**_xxx_, run the  **dracut -f /boot/initramfs-**_xxx_  command.

    4.  Run the following commands to check whether the PVOPS module for Xen or VirtIO module for KVM is loaded:

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **xen**

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **virtio**

        ```
        SIA10000xxxxx:~ # lsinitrd /boot/initrd-`uname -r` | grep xen
        -rwxr--r-- 1 root root 42400 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/block/xen-blkfront.ko
        -rwxr--r-- 1 root root 44200 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/net/xen-netfront.ko
        
        SIA10000xxxxx:~ # lsinitrd /boot/initrd-`uname -r` | grep virtio
        -rwxr--r-- 1 root root 19248 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/scsi/virtio_scsi.ko
        -rwxr--r-- 1 root root 23856 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/block/virtio_blk.ko
        drwxr-xr-x 2 root root 0 Jul 12 14:53 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio
        -rwxr--r-- 1 root root 15848 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio_ring.ko
        -rwxr--r-- 1 root root 20008 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio_pci.ko
        -rwxr--r-- 1 root root 12272 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio.ko
        -rwxr--r-- 1 root root 38208 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/net/virtio_net.ko
        ```

    5.  Restart the ECS.
    6.  Modify the  **/boot/grub/menu.lst**  file. Add  **xen\_platform\_pci.dev\_unplug=all**  and modify the root configuration.

        Before the modification:

        ```
        ###Don't change this comment -YaST2 identifier: Original name: linux###
        title SUSE Linux Enterprise Server 11SP4 - 3.0.76-0.11 (default) 
        root (hd0,0) 
        kernel /boot/vmlinuz-3.0.76-0.11-default root=UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130 splash=silentcrashkernel=256M-:128M showopts vga=0x314
        initrd /boot/initrd-3.0.76-0.11-default
        ```

        After the modification:

        ```
        ###Don't change this comment -YaST2 identifier: Original name: linux###
        title SUSE Linux Enterprise Server 11SP4 - 3.0.76-0.11 (default) 
        root (hd0,0) 
        kernel /boot/vmlinuz-3.0.76-0.11-default root=UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130 splash=silentcrashkernel=256M-:128M showopts vga=0x314 xen_platform_pci.dev_unplug=all 
        initrd /boot/initrd-3.0.76-0.11-default
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   Ensure that the root partition is in the UUID format.  
        >-   **xen\_platform\_pci.dev\_unplug=all**  is added to shield the QEMU device.  
        >-   For SUSE 11 SP1 64-bit to SUSE 11 SP4 64-bit, add  **xen\_platform\_pci.dev\_unplug=all**  to the  **menu.lst**  file. For SUSE 12 or later, this function is enabled by default, and you do not need to configure it.  

    7.  Run the following commands to check whether the Xen driver exists in initrd:

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **xen**

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **virtio**

        ```
        SIA10000xxxxx:~ # lsinitrd /boot/initrd-`uname -r` | grep xen
        -rwxr--r-- 1 root root 42400 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/block/xen-blkfront.ko
        -rwxr--r-- 1 root root 44200 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/net/xen-netfront.ko
        
        SIA10000xxxxx:~ # lsinitrd /boot/initrd-`uname -r` | grep virtio
        -rwxr--r-- 1 root root 19248 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/scsi/virtio_scsi.ko
        -rwxr--r-- 1 root root 23856 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/block/virtio_blk.ko
        drwxr-xr-x 2 root root 0 Jul 12 14:53 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio
        -rwxr--r-- 1 root root 15848 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio_ring.ko
        -rwxr--r-- 1 root root 20008 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio_pci.ko
        -rwxr--r-- 1 root root 12272 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/virtio/virtio.ko
        -rwxr--r-- 1 root root 38208 Jun 22 2012 lib/modules/2.6.32-279.el6.x86_64/kernel/drivers/net/virtio_net.ko
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If you add built-in drivers to the initrd or initramfs file, the ECS will not be affected. This makes it easy to modify the drivers. However, you cannot check the drivers by running the  **lsinitrd**  command. You can run the following commands to check whether the drivers are built-in ones in the kernel:  
        >**cat** **/boot/config-\`uname** **-r\`** **|** **grep** **CONFIG\_VIRTIO** **|** **grep** **y**  
        >**cat** **/boot/config-\`uname** **-r\`** **|** **grep** **CONFIG\_XEN** **|** **grep** **y**  


-   <a name="li45512494152649"></a>If the OS version is SUSE 12 SP1, perform the following steps:
    1.  Run the following command to open the  **/etc/dracut.conf**  file:

        **vi** **/etc/dracut.conf**

    2.  Press  **i**  to enter editing mode and add the xen-pv and VirtIO drivers to  **add-drivers**  \(the format depends on the OS requirements\).

        ```
        [root@CTU10000xxxxx ~]# vi /etc/dracut.conf 
        # additional kernel modules to the default
        add_drivers+="ata_piix ata_generic xen_vnif xen_vbd xen_platform_pci virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio"
        ```

    3.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the change and exits the  **/etc/dracut.conf**  file.
    4.  Run the following command to generate initrd again:

        **dracut -f /boot/initramfs-**_File name_

        If the virtual file system is not the default initramfs, run the  **dracut -f** _Name of the initramfs or initrd file actually used_  command. The actual initramfs or initrd file name can be obtained from the GRUB configuration file,  **/boot/grub/grub.cfg**,  **/boot/gurb2/grub.cfg**, or  **/boot/grub/grub.conf**  \(which varies depending on the OS\).

    5.  If the virtual file system is initramfs, run the following commands to check whether native Xen and KVM drivers have been loaded:

        **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **xen**

        **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **virtio**

        If the virtual file system is initrd, run the following commands to check whether native Xen and KVM drivers have been loaded:

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **xen**

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **virtio**


-   <a name="en-us_topic_0037352187_li57696863113515"></a>If the OS version is later than SUSE 12 SP1 or openSUSE 13, perform the following steps:

    Take SUSE Linux Enterprise Server 12 SP2 \(x86\_64\) as an example.

    1.  Run the following command to open the  **/etc/dracut.conf**  file:

        **vi** **/etc/dracut.conf**

    2.  Press  **i**  to enter editing mode and add the xen-pv and VirtIO drivers to  **add\_drivers**  \(the format depends on the OS requirements\).

        ```
        [root@CTU10000xxxxx ~]# vi /etc/dracut.conf 
        # additional kernel modules to the default
        add_drivers+="ata_piix ata_generic xen-blkfront xen-netfront virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio"
        ```

    3.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the change and exits the  **/etc/dracut.conf**  file.
    4.  Run the following command to generate initrd again:

        **dracut -f /boot/initramfs-**_File name_

        If the virtual file system is not the default initramfs, run the  **dracut -f**_Name of the initramfs or initrd file actually used_  command. The actual initramfs or initrd file name can be obtained from the GRUB configuration file, which can be  **/boot/grub/grub.cfg**,  **/boot/gurb2/grub.cfg**, or  **/boot/grub/grub.conf**  depending on the OS.

    5.  If the virtual file system is initramfs, run the following commands to check whether native Xen and KVM drivers have been loaded:

        **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **xen**

        **lsinitrd** **/boot/initramfs-\`uname** **-r\`.img** **|** **grep** **virtio**

        If the virtual file system is initrd, run the following commands to check whether the original Xen and KVM driver modules are successfully loaded:

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **xen**

        **lsinitrd** **/boot/initrd-\`uname** **-r\`** **|** **grep** **virtio**

        If the virtual file system is initrd, the following information is displayed:

        ```
        sluo-ecs-30dc:~ # lsinitrd /boot/initrd-`uname -r` | grep xen
        -rw-r--r-- 1 root root 69575 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/block/xen-blkfront.ko
        -rw-r--r-- 1 root root 53415 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/net/xen-netfront.ko
        drwxr-xr-x 2 root root 0 Sep 28 10:21 lib/modules/4.4.21-69-default/updates/pvdriver/xen-hcall
        -rwxr-xr-x 1 root root 8320 Sep 28 10:21 lib/modules/4.4.21-69-default/updates/pvdriver/xen-hcall/xen-hcall.ko
        
        sluo-ecs-30dc:~ # lsinitrd /boot/initrd-`uname -r` | grep virtio
        -rw-r--r-- 1 root root 29335 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/block/virtio_blk.ko
        -rw-r--r-- 1 root root 57007 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/net/virtio_net.ko
        -rw-r--r-- 1 root root 32415 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/scsi/virtio_scsi.ko
        drwxr-xr-x 2 root root 0 Sep 28 10:21 lib/modules/4.4.21-69-default/kernel/drivers/virtio
        -rw-r--r-- 1 root root 19623 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/virtio/virtio.ko
        -rw-r--r-- 1 root root 38943 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/virtio/virtio_pci.ko
        -rw-r--r-- 1 root root 24431 Oct 26 2016 lib/modules/4.4.21-69-default/kernel/drivers/virtio/virtio_ring.ko
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If you add built-in drivers to the initrd or initramfs file, the ECS will not be affected. This makes it easy to modify the drivers. However, you cannot check the drivers by running the  **lsinitrd**  command. You can run the following commands to check whether the drivers are built-in ones in the kernel:  
        >**cat** **/boot/config-\`uname** **-r\`** **|** **grep** **CONFIG\_VIRTIO** **|** **grep** **y**  
        >**cat** **/boot/config-\`uname** **-r\`** **|** **grep** **CONFIG\_XEN** **|** **grep** **y**  



