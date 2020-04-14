# What Changes Will Be Made to an Image File Used for Registering a Private Image?<a name="EN-US_TOPIC_0032307025"></a>

If you enable automatic configuration when registering a private image using an image file, the system will perform the following operations:

## Linux<a name="section119078190435"></a>

-   Check whether drivers related to the PV driver exist. If yes, delete them.
-   Modify the  **grub**  and  **syslinux**  configuration files to add the OS kernel boot parameters and change the disk partition name \(**UUID=**_UUID of the disk partition_\).
-   Change the names of the disk partitions in the  **/etc/fstab**  file \(**UUID=**_UUID of the disk partition_\).
-   Check whether the  **initrd**  file has the Xen and IDE drivers. If no, load the Xen and IDE drivers.
-   Modify X Window configuration file  **/etc/X11/xorg.conf**  to prevent display failures.
-   Delete services of VMware tools.
-   Record the latest automatic modification made to the image into  **/var/log/rainbow\_modification\_record.log**.
-   Linux OSs automatically copy the built-in VirtIO driver to initrd or initramfs. For details, see  [Formats and OSs Supported for External Image Files](formats-and-oss-supported-for-external-image-files.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>For image files in the following scenarios, this function does not take effect after  **Enable automatic configuration**  is selected:  
>-   Image files whose  **/usr**  directory is an independent partition  
>-   Fedora 29 64-bit and Fedora 30 64-bit image files that use the XFS file system  
>-   Image files that use SUSE 12 SP4 64bit and the ext4 file system  

## Windows<a name="section1126317553435"></a>

-   Restore the IDE driver to enable the system to use the IDE driver for its initial start.
-   Delete the registry keys of the mouse and keyboard and generate the registry keys on the new platform to ensure that the mouse and keyboard are available.
-   Restore the PV driver registry key to rectify the failure to install drivers and Xen driver conflict.
-   Inject the VirtIO driver offline to solve the problem that the system cannot start when UVP VMTools is not installed.
-   Restore DHCP. The system dynamically obtains information such as the IP address based on the DHCP protocol.

