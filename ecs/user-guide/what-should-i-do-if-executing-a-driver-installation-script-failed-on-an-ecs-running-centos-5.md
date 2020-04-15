# What Should I Do If Executing a Driver Installation Script Failed on an ECS Running CentOS 5?<a name="EN-US_TOPIC_0214940103"></a>

## Scenarios<a name="section1472603014415"></a>

After executing the script for installing the Virtio driver on an ECS running CentOS 5, users cannot determine whether the driver has been successfully installed. This section describes how to check driver installation.

## Procedure<a name="section173923176436"></a>

1.  Log in to the ECS and create a temporary directory  **check**.

    **mkdir /check**

2.  Copy the image file to the current directory.

    **cp /boot/initrd-2.6.18-308.el5.img /check/**

3.  Run the following commands to convert the file format to .gz:

    **cd /check**

    **mv initrd-2.6.18-308.el5.img initrd-2.6.18-308.el5.img.gz**

4.  Decompress the package.

    **gzip –d initrd-2.6.18-308.el5.img.gz**

5.  Check whether the driver has been successfully installed.

    **cpio –t –F initrd-2.6.18-308.el5.img | grep virtio**

    The check process is shown in the following figure.

    **Figure  1**  Checking driver installation<a name="fig203921373466"></a>  
    ![](figures/checking-driver-installation.png "checking-driver-installation")

    If the command output contains  **virtio**,  **virtio\_blk**,  **virtio\_net**, and  **virtio\_pci**, the driver has been successfully installed.

    In the preceding figure, the image is of an early version and has no virtio\_scsi driver installed. As a result, the ECS is not allowed to attach SCSI disks.


