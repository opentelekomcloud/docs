# Converting the Image Format<a name="EN-US_TOPIC_0117262219"></a>

## Scenarios<a name="section131721411811"></a>

The open-source tool  **qemu-img**  is provided for you to convert image file formats.

You can import an image file in VHD, VMDK, QCOW2, RAW, VHDX, QCOW, VDI, QED, ZVHD, or ZVHD2 format to the cloud platform. QCOW2 image files are recommended. If you need to import an image file in other formats, use the qemu-img tool to convert the image format before importing the image file. The image file to be imported must be a single image file. For example, you cannot use a pre-allocated image file which depends on two files:  **xxxx.vmdk**  and  **xxxx-flat.vmdk**. Both files can be imported to the cloud platform only after being converted into common VMDK or QCOW2 files.

The methods of installing qemu-img and converting image file formats may vary depending on the OS.

The  qemu-img  tool can do  conversion between multiple formats, including VHD, VMDK, QCOW2, RAW, VHDX, QCOW, VDI, or QED. You can select the image format as needed.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   ZVHD and ZVHD2 are self-developed image file formats and cannot be identified by qemu-img.  
>-   When you run the command to convert the format of VHD image files, use VPC to replace VHD. Otherwise, qemu-img cannot identify the image format.  
>    For example, to convert a CentOS 6.9 VHD image file into a QCOW2 image file, run the following command:  
>    **qemu-img** **convert** **-p** **-f** **vpc** **-O** **qcow2** **centos6.9.vhd** **centos6.9.qcow2**  

## Windows<a name="section270715818503"></a>

1.  Install qemu-img.
    1.  Download the qemu-img installation package from  [https://qemu.weilnetz.de/w64/](https://qemu.weilnetz.de/w64/).
    2.  Double-click the setup file to install qemu-img in  **D:\\Program Files\\qemu**  \(an example installation path\).

2.  Configure environment variables.
    1.  Choose  **Start**  \>  **Computer**  and right-click  **Properties**.
    2.  Click  **Advanced system settings**.
    3.  In the  **System Properties**  dialog box, click  **Advanced**  \>  **Environment Variables**.
    4.  In the  **Environment Variables**  dialog box, search for  **Path**  in the  **System Variable**  area and click  **Edit**. Add  **D:\\Program Files\\qemu**  to  **Variable Value**. Use a semicolon \(;\) to separate every two variable values.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If  **Path**  does not exist, add it and set its value to  **D:\\Program Files\\qemu**.  

    5.  Click  **OK**.

3.  Verify the installation.

    Choose  **Start**  \>  **Run**, enter  **cmd**, and press  **Enter**. In the  **cmd**  window, enter  **qemu-img** **--help**. If the qemu-img version information is contained in the command output, the installation is successful.

4.  Convert the image format.
    1.  In the  **cmd**  window, run the following commands to switch to  **D:\\Program Files\\qemu**:

        **d:**

        **cd** **D:\\Program** **Files\\qemu**

    1.  Run the following command to convert the image file format from VMDK to QCOW2:

        **qemu-img** **convert** **-p** **-f** **vmdk** **-O** **qcow2** **centos6.9-flat.vmdk** **centos6.9.qcow2**

        The parameters are described as follows:

        -   **-p**  indicates the image conversion progress.
        -   **-f**  indicates the source image format.
        -   The part following  **-O**  \(which must be in upper case\) consists of the required format, source image file, and target image file.

        After the conversion is complete, the target image file is displayed in the directory where the source image file is located.

        The following information is displayed:

        ```
        # qemu-img convert -p -f vmdk -O qcow2 centos6.9-flat.vmdk centos6.9.qcow2
            (100.00/100%)
        ```

    2.  Run the following command to query details about the converted image file in QCOW2 format:

        **qemu-img** **info** **centos6.9.qcow2**

        The following information is displayed:

        ```
        # qemu-img info centos6.9.qcow2
        image: centos6.9.qcow2
        file format: qcow2
        virtual size: 1.0G (1073741824 bytes)
        disk size: 200K
        cluster_size: 65536
        Format specific information:
            compat: 1.1
            lazy refcounts: false
        ```



## Linux<a name="section87611435163413"></a>

1.  Install qemu-img.
    -   For Ubuntu or Debian, run the following command:

        **apt** **install** **qemu-img**

    -   For CentOS, Red Hat, or Oracle, run the following command:

        **yum** **install** **qemu-img**

    -   For SUSE or openSUSE, run the following command:

        **zypper** **install** **qemu-img**

2.  Run the following command to check whether the installation is successful:

    **qemu-img** **-v**

    If the version information and help manual of the qemu-img tool are contained in the command output, the installation is successful. If CentOS 7 is used, the command output is as follows:

    ```
    [root@CentOS7 ~]# qemu-img -v
    qemu-img version 1.5.3, Copyright (c) 2004-2008 Fabrice Bellard
    usage: qemu-img command [command options]
    QEMU disk image utility
    
    Command syntax:
      check [-q] [-f fmt] [--output=ofmt] [-r [leaks | all]] [-T src_cache] filename
      create [-q] [-f fmt] [-o options] filename [size]
      commit [-q] [-f fmt] [-t cache] filename
      compare [-f fmt] [-F fmt] [-T src_cach]
    ```

3.  Convert the image format. For example, perform the following steps to convert a VMDK image file running CentOS 7 to a QCOW2 image file:
    1.  Run the following command to convert the image file format to QCOW2:

        **qemu-img** **convert** **-p** **-f** **vmdk** **-O** **qcow2** **centos6.9-flat.vmdk** **centos6.9.qcow2**

        The parameters are described as follows:

        -   **-p**: indicates the conversion progress.
        -   **-f**  indicates the source image format.
        -   The pat following  **-O**  \(which must be in upper case\) is the converted image format + source image file name + target image file name.

        After the conversion is complete, the target image file is displayed in the directory where the source image file is located.

        The following information is displayed:

        ```
        [root@CentOS7 home]# qemu-img convert -p -f vmdk -O qcow2 centos6.9-flat.vmdk centos6.9.qcow2
            (100.00/100%)
        ```

    2.  Run the following command to query details about the converted image file in QCOW2 format:

        **qemu-img** **info** **centos6.9.qcow2**

        The following information is displayed:

        ```
        [root@CentOS7 home]# qemu-img info centos6.9.qcow2
        image: centos6.9.qcow2
        file format: qcow2
        virtual size: 1.0G (1073741824 bytes)
        disk size: 200K
        cluster_size: 65536
        Format specific information:
            compat: 1.1
            lazy refcounts: false
        ```



## Typical Applications<a name="section134802578420"></a>

A pre-allocated image file depends on two files:  **xxxx.vmdk**  and  **xxxx-flat.vmdk**  and cannot be directly imported to the cloud platform. When you export a pre-allocated image file in VMDK monolithicFlat format from the VMware platform, you must convert its format to common VMDK or QCOW2 before it can be imported to the cloud platform.

The following uses  **centos6.9-64bit-flat.vmdk**  and  **centos6.9-64bit.vmdk**  as an example. Place  **centos6.9-64bit-flat.vmdk**  and  **centos6.9-64bit.vmdk**  in the same directory and use qemu-img to convert the image formats.

1.  Run the following commands to query the image file details:

    **ls** **-lh** **centos6.9-64bit\***

    **qemu-img** **info** **centos6.9-64bit.vmdk**

    The following information is displayed:

    ```
    [root@CentOS7 tmp]# ls -lh centos6.9-64bit*
    -rw-r--r--. 1 root root 10G Jun 13 05:30 centos6.9-64bit-flat.vmdk
    -rw-r--r--. 1 root root 327 Jun 13 05:30 centos6.9-64bit.vmdk
    [root@CentOS7 tmp]# qemu-img info centos6.9-64bit.vmdk
    image: centos6.9-64bit.vmdk
    file format: vmdk
    virtual size: 10G (10737418240 bytes)
    disk size: 4.0K
    Format specific information:
        cid: 3302005459
        parent cid: 4294967295
        create type: monolithicFlat
        extents:
            [0]:
                virtual size: 10737418240
                filename: centos6.9-64bit-flat.vmdk
                format: FLAT
    [root@CentOS7 tmp]# qemu-img info centos6.9-64bit-flat.vmdk
    image: centos6.9-64bit-flat.vmdk
    file format: raw
    virtual size: 10G (10737418240 bytes)
    disk size: 0
    ```

2.  Run the following command to query the configuration of the pre-allocated image file:

    **cat** **centos6.9-64bit.vmdk**

    The following information is displayed:

    ```
    [root@CentOS7 tmp]# cat centos6.9-64bit.vmdk
    # Disk DescriptorFile
    version=1
    CID=c4d09ad3
    parentCID=ffffffff
    createType="monolithicFlat"
     
    # Extent description
    RW 20971520 FLAT "centos6.9-64bit-flat.vmdk" 0
     
    # The Disk Data Base
    #DDB
     
    ddb.virtualHWVersion = "4"
    ddb.geometry.cylinders = "20805"
    ddb.geometry.heads = "16"
    ddb.geometry.sectors = "63"
    ddb.adapterType = "ide"
    ```

3.  Place  **centos6.9-64bit-flat.vmdk**  and  **centos6.9-64bit.vmdk**  in the same directory. Run the following command to convert the image format to QCOW2 using qemu-img:

    ```
    [root@CentOS7 tmp]# qemu-img convert -p -f vmdk -O qcow2 centos6.9-64bit-flat.vmdk centos6.9-64bit.qcow2
        (100.00/100%)
    ```

4.  Run the following command to query details about the converted image file in QCOW2 format:

    **qemu-img** **info** **centos6.9-64bit.qcow2**

    The following information is displayed:

    ```
    [root@CentOS7 tmp]# qemu-img info centos6.9-64bit.qcow2
    image: centos6.9-64bit.qcow2
    file format: qcow2
    virtual size: 10G (10737418240 bytes)
    disk size: 200K
    cluster_size: 65536
    Format specific information:
        compat: 1.1
        lazy refcounts: false
    ```


