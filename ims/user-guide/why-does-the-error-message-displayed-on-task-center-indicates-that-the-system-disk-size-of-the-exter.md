# Why Does the Error Message Displayed on Task Center Indicates That the System Disk Size of the External Image File Exceeds the Maximum System Disk Size When a VHD Image File Failed to Be Uploaded?<a name="EN-US_TOPIC_0058841396"></a>

If you fail to register an external image file as a private image and the error message displayed on Task Center indicates that the system disk size of the external image file exceeds the maximum system disk size you have configured, possible causes include:

1.  The system disk size you have configured is less than the system disk size of the VM on the original platform. Confirm the system disk size of the image file and register it again.
2.  The VHD image file is generated using  **qemu-img**  or similar tools and the virtual size of the VHD image is inconsistent with that of the original VM. For details, see  [https://bugs.launchpad.net/qemu/+bug/1490611](https://bugs.launchpad.net/qemu/+bug/1490611).

    In this case, run the  **qemu-img info**  command.

    ```
    [xxxx@xxxxx test]$ qemu-img info 2g.vhd
    image: 2g.vhd
    file format: vpc
    virtual size: 2.0G (2147991552 bytes)
    disk size: 8.0K
    cluster_size: 2097152
    ```

    Check whether the virtual size value is an integer in GB. As shown in the preceding command output,  **2147991552 bytes**  \(**2.0004 G**\) is larger than  **2 G**. Therefore, you need to configure a value larger than 2 GB for the system disk size.


