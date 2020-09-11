# What Do I Do If No Partition Is Found During the Startup of an ECS Created from an Imported Private Image?<a name="EN-US_TOPIC_0034220644"></a>

## Symptom<a name="section15670444166"></a>

This may be caused by the disk partition ID change after the cross-platform image import. As a result, no partition can be found based on the original disk partition ID in the image. In this case, you need to change the disk partition in the image \(**UUID=**_UUID of the disk partition_\).

## Solution<a name="section04561352374"></a>

The following uses openSUSE 13.2 as an example to describe how to change the partition name.

1.  <a name="li4101085015191"></a>Run the following command to query the disk partition ID:

    **ls -l /dev/disk/by-id/**

    The example command output is as follows.

    ```
    total 0
    lrwxrwxrwx 1 root root 10 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001 -> ../../xvda
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part1 -> ../../xvda1
    lrwxrwxrwx 1 root root 12 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part10 -> ../../xvda10
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part2 -> ../../xvda2
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part5 -> ../../xvda5
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part6 -> ../../xvda6
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part7 -> ../../xvda7
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part8 -> ../../xvda8
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ata-QEMU_HARDDISK_QM00001-part9 -> ../../xvda9
    lrwxrwxrwx 1 root root 10 Jul 22 01:35 ata-QEMU_HARDDISK_QM00005 -> ../../xvde
    lrwxrwxrwx 1 root root 10 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001 -> ../../xvda
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part1 -> ../../xvda1
    lrwxrwxrwx 1 root root 12 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part10 -> ../../xvda10
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part2 -> ../../xvda2
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part5 -> ../../xvda5
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part6 -> ../../xvda6
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part7 -> ../../xvda7
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part8 -> ../../xvda8
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00001-part9 -> ../../xvda9
    lrwxrwxrwx 1 root root 10 Jul 22 01:35 scsi-SATA_QEMU_HARDDISK_QM00005 -> ../../xvde
    ```

    **ata-QEMU\_HARDDISK\_xxx**  and  **scsi-SATA\_QEMU\_HARDDISK\_xxx**  indicate that the disk of the ECS is simulated using Quick EMUlator \(QEMU\). The content at the left of  **-\>**  is the disk partition ID, and that at the right of  **-\>**  is the partition name.

2.  <a name="li37981366152220"></a>Run the following command to query the disk partition UUID:

    **ls -l /dev/disk/by-uuid/**

    The example command output is as follows.

    ```
    total 0
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 45ecd7a0-29da-4402-a017-4564a62308b8 -> ../../xvda5
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 55386c6a-9e32-41d4-af7a-e79596221f51 -> ../../xvda9
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 55f36660-9bac-478c-a701-7ecc5347f789 -> ../../xvda8
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 780f36bc-0ada-4c98-9a8d-44570d65333d -> ../../xvda1
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 b3b7c47f-6a91-45ef-80d6-275b1cc16e19 -> ../../xvda6
    lrwxrwxrwx 1 root root 11 Jul 22 01:35 ea63b55d-3b6e-4dcd-8986-956b72bac3e9 -> ../../xvda7
    lrwxrwxrwx 1 root root 12 Jul 22 01:35 eb3cc645-925e-4bc5-bedf-c2a6f3b65809 -> ../../xvda10
    ```

    The content at the left of  **-\>**  is the disk partition UUID, and that at the right of  **-\>**  is the partition name. Obtain the relationship between the disk partition name, partition ID, and partition UUID.

3.  <a name="li11793524153042"></a>Run the following command to check the partition names in the  **/etc/fstab**  file:

    **vi /etc/fstab**

    The example command output is as follows.

    ```
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part5 / ext3 defaults,errors=panic 1 1
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part1 /boot ext3 defaults,errors=panic 1 2
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part6 /home ext3 nosuid,errors=panic 1 2
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part10 /opt ext3 defaults,errors=panic 1 2
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part7 /tmp ext3 nodev,nosuid,errors=panic 1 2
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part9 /usr ext3 defaults,errors=panic 1 2
    /dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part8 /var ext3 nodev,nosuid,errors=panic 1 2
    sysfs /sys sysfs noauto 0 0
    proc /proc proc defaults 0 0
    usbfs /proc/bus/usb usbfs noauto 0 0
    devpts /dev/pts devpts mode=0620,gid=5 0 0
    /dev/cdrom /media/ udf,iso9660 noexec,noauto,nouser,nodev,nosuid 1 2
    tmpfs /dev/shm tmpfs noexec,nodev,nosuid 0 0
    ```

    The values in the first column are the disk partition IDs.

4.  Press  **i**  to enter editing mode. Change the disk partition ID in the row that contains  **/dev/disk/xxx**  in the  **/etc/fstab**  file in step  [3](#li11793524153042)  to  **UUID=_UUID of the disk partition_**  based on the query results in step  [1](#li4101085015191)  and step  [2](#li37981366152220).

    The modified content is as follows.

    ```
    UUID=45ecd7a0-29da-4402-a017-4564a62308b8 / ext3 defaults,errors=panic 1 1
    UUID=780f36bc-0ada-4c98-9a8d-44570d65333d /boot ext3 defaults,errors=panic 1 2
    UUID=b3b7c47f-6a91-45ef-80d6-275b1cc16e19 /home ext3 nosuid,errors=panic 1 2
    UUID=eb3cc645-925e-4bc5-bedf-c2a6f3b65809 /opt ext3 defaults,errors=panic 1 2
    UUID=ea63b55d-3b6e-4dcd-8986-956b72bac3e9 /tmp ext3 nodev,nosuid,errors=panic 1 2
    UUID=55386c6a-9e32-41d4-af7a-e79596221f51 /usr ext3 defaults,errors=panic 1 2
    UUID=55f36660-9bac-478c-a701-7ecc5347f789 /var ext3 nodev,nosuid,errors=panic 1 2
    sysfs /sys sysfs noauto 0 0
    proc /proc proc defaults 0 0
    usbfs /proc/bus/usb usbfs noauto 0 0
    devpts /dev/pts devpts mode=0620,gid=5 0 0
    /dev/cdrom /media/ udf,iso9660 noexec,noauto,nouser,nodev,nosuid 1 2
    tmpfs /dev/shm tmpfs noexec,nodev,nosuid 0 0
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >Ensure that the UUIDs are correctly modified. Otherwise, the ECS cannot start properly.  

5.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the configuration and exits the vi editor.
6.  <a name="li2638602155053"></a>Check the partition names in the system boot configuration file.

    The system boot configuration files for different OSs vary. Confirm the boot configuration file of the current OS.

    -   Grand Unified Boot Loader \(GRUB\) configuration file
        -   /boot/grub/grub.conf
        -   /boot/grub/menu.lst
        -   /boot/grub/grub.cfg
        -   /boot/grub2/grub.cfg

    -   Syslinux configuration file
        -   /extlinux.conf
        -   /boot/syslinux/extlinux.conf
        -   /boot/extlinux/extlinux.conf
        -   /boot/syslinux/syslinux.cfg
        -   /syslinux/syslinux.cfg
        -   /syslinux.cfg

    The boot file in this example is  **/boot/grub/menu.lst**. Run the following command to check it:

    **vi /boot/grub/menu.lst**

    ```
    default 0
    timeout 3
    title xxx Server OS - xxxxxx
    kernel /boot/vmlinuz-3.0.101-0.47.52-default root=/dev/disk/by-id/scsi-SATA_QEMU_HARDDISK_QM00001-part5 resume= memmap=0x2000000$0x3E000000 nmi_watchdog=2 crashkernel=512M-:256M console=ttyS0,115200 console=tty0 xen_emul_unplug=all
    initrd /boot/initrd-3.0.101-0.47.52-default
    ```

7.  Press  **i**  to enter editing mode and change the partition names in the system boot configuration file.

    Change the disk partition name in the  **/boot/grub/menu.lst**  file in  [6](#li2638602155053)  to  **UUID=_UUID of the disk partition_**  based on the query results in  [1](#li4101085015191)  and  [2](#li37981366152220).

    ```
    default 0
    timeout 3
    title xxx Server OS - xxxxxx
    kernel /boot/vmlinuz-3.0.101-0.47.52-default root=UUID=45ecd7a0-29da-4402-a017-4564a62308b8 resume= memmap=0x2000000$0x3E000000 nmi_watchdog=2 crashkernel=512M-:256M console=ttyS0,115200 console=tty0 xen_emul_unplug=all
    initrd /boot/initrd-3.0.101-0.47.52-default
    ```

8.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the configuration and exits the vi editor.

