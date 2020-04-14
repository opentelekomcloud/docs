# Quickly Importing an Image File \(Linux\)<a name="EN-US_TOPIC_0133773660"></a>

## Scenarios<a name="section12126161523313"></a>

This section describes how to quickly import an image file in Linux. You are advised to use an EulerOS ECS on the cloud platform for converting image formats and generating bitmap files.

In Linux, you are advised to use  **qemu-img-hw**  in the fast import tool to convert image formats.

## Prerequisites<a name="section1892165619595"></a>

-   The image file has been optimized. For details, see  [Optimization Process](optimization-process-(windows).md)  or  [Optimization Process](optimization-process-(linux).md). In addition, ensure that the image file meets the requirements in  [Table 1](preparing-an-image-file-(windows).md#table85212269215)  or  [Table 1](preparing-an-image-file-(linux).md#table85212269215).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Select the reference content based on the OS type in the image file.  

-   You have created an ECS running EulerOS on the management console and bound an EIP to the ECS.
-   An OBS bucket has been created on the management console.

## Procedure<a name="section745217198110"></a>

1.  Upload the image file to the ECS.
    -   If the local host runs a Linux OS, run the  **scp**  command.

        For example, to upload  **image01.qcow2**  to the  **/usr/**  directory on the ECS, run the following command:

        **scp** **/var/image01.qcow2** **root@**_xxx.xxx.xx.xxx_**:/usr/**

        _xxx.xxx.xx.xxx_  indicates the EIP bound to the ECS.

    -   If the local host runs a Windows OS, use a file transfer tool, such as WinSCP, to upload the image file to the ECS.

2.  Obtain the fast import tool package, upload it to the ECS, and then decompress the package.

    Obtain the fast import tool from the following link in the table.

    **Table  1**  Fast import tool package

    <a name="table69651049112418"></a>
    <table><thead align="left"><tr id="row996618490249"><th class="cellrowborder" valign="top" width="26.840000000000003%" id="mcps1.2.3.1.1"><p id="p117482592122"><a name="p117482592122"></a><a name="p117482592122"></a>Tool Package</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.16%" id="mcps1.2.3.1.2"><p id="p774995919129"><a name="p774995919129"></a><a name="p774995919129"></a>How to Obtain</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1596614496243"><td class="cellrowborder" valign="top" width="26.840000000000003%" headers="mcps1.2.3.1.1 "><p id="p892264334719"><a name="p892264334719"></a><a name="p892264334719"></a>quick-import-tools</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.16%" headers="mcps1.2.3.1.2 "><p id="p3750175910127"><a name="p3750175910127"></a><a name="p3750175910127"></a><a href="https://obs-20181128.ims.obs.eu-de.otc.t-systems.com/DT-image-convert-tools.zip" target="_blank" rel="noopener noreferrer">https://obs-20181128.ims.obs.eu-de.otc.t-systems.com/DT-image-convert-tools.zip</a></p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Use the fast import tool to convert the image format.
    1.  Go to the directory where  **qemu-img-hw**  is stored, for example,  **/usr/quick-import-tools/qemu-img-hw**.

        **cd** **/usr/quick-import-tools/qemu-img-hw**

    2.  Run the following command to change file permissions:

        **chmod** **+x** **qemu-img-hw**

    3.  Run the  **qemu-img-hw**  command to convert the image file to the ZVHD2 \(recommended\) or RAW format.

        The command format of  **qemu-img-hw**  is as follows:

        **./qemu-img-hw convert -p -O** _Target image format_ _Source image file_ _Target image file_

        For example, run the following command to convert an  **image01.qcow2**  file to an  **image01.zvhd2**  file:

        **./qemu-img-hw** **convert** **-p** **-O** **zvhd2** **image01.qcow2** **image01.zvhd2**

        -   If the image file is converted to the ZVHD2 format, go to  [5](#li12136151722).
        -   If the image file is converted to the RAW format, use  **CreateMF.jar**  in the tool package to generate a bitmap file. Go to  [4](#li1683153619217).

4.  <a name="li1683153619217"></a>Use the fast import tool to generate a bitmap file.
    1.  Ensure that JDK has been installed on the ECS.

        Run the following command to check whether JDK is installed:

        **source** **/etc/profile**

        **java** **-version**

        If the Java version is displayed, JDK has been installed.

    2.  Run the following command to enter the directory where  **CreateMF.jar**  is stored:

        **cd** **/usr/quick-import-tools/createMF**

    3.  Run the following command to generate a bitmap file:

        **java -jar CreateMF.jar** _/Original RAW file path /Generated .mf file path_

        Example:

        **java** **-jar** **CreateMF.jar** **image01.raw** **image01.mf**

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >The generated bitmap file must have the same name as the RAW image file. For example, if the image file name is  **image01.raw**, the generated bitmap name is  **image01.mf**.  


5.  <a name="li12136151722"></a>Use  **s3cmd**  to upload files to the OBS bucket.
    1.  Install  **s3cmd**.

        If  **s3cmd**  has been installed, skip this step.

        1.  Run the following command to install setuptools:

            **yum** **install** **python-setuptools**

        2.  Run the following command to install wget:

            **yum** **install** **wget**

        3.  Run the following commands to obtain the  **s75pxd**  software package:

            **wget** **https://github.com/s3tools/s3cmd/archive/master.zip**

            **mv** **master.zip** **s3cmd-master.zip**

        4.  Run the following commands to install  **s3cmd**:

            **unzip** **s3cmd-master.zip**

            **cd** **s3cmd-master**

            **python** **setup.py** **install**

    2.  Configure  **s3cmd**.

        Run the following command to configure  **s3cmd**:

        ```
        s3cmd --configure
        Access Key: Enter the AK.
        Secret Key: Enter the SK.
        Default Region: Enter the region where the bucket is located.
        S3 Endpoint: Refer to the OBS endpoint.
        DNS-style bucket+hostname:port template for accessing a bucket: Enter a server address with a bucket name, for example, mybucket.obs.myclouds.com.
        Encryption password: Press Enter.
        Path to GPG program: Press Enter.
        Use HTTPS protocol: Specifies whether to use HTTPS. The value can be Yes or No.
        HTTP Proxy server name: Specifies the proxy address used to connect the cloud from an external network. (If you do not need connect to the cloud, press Enter.)
        HTTP Proxy server port: Specifies the proxy port used to connect to the cloud from an external network (If you do not need connect to the cloud, press Enter.)
        Test access with supplied credentials? y
        (If Success. Your access key and secret key worked fine :-) is displayed, the connection is successful.)
        Save settings? y (Specifies whether to save the configuration. If y is entered, the configuration will be saved.)
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >The configuration is stored in the  **/root/.s3cfg**  directory. If you want to modify the configuration, run the  **s3cmd --configure**  command again or directly edit the  **.s3cfg**  file by running the  **vi .s3cfg**  command.  

    3.  Run the  **s3cmd**  command to upload the ZVHD2 image file to the OBS bucket, or upload the RAW image file and its bitmap file to the OBS bucket.

        **s3cmd** **put** _image01.zvhd2_ **s3://**_mybucket_**/**

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >The .mf file must be in the same OBS bucket as the RAW image file.  


6.  Register a private image.

    You can register a private image using the converted ZVHD2 or RAW file on the console or using an API.

    Method 1: Create a private image on the console.

    1.  Log in to the management console.
    2.  Under  **Computing**, click  **Image Management Service**.

        The IMS console is displayed.

    3.  In the upper right corner, click  **Create Image**.
    4.  In the  **Image Type and Source**  area, select  System disk image  or  **Data disk image**  for  **Type**.
    5.  Select  **Image File**  for  **Source**. Select the bucket storing the ZVHD2 or RAW image file and then select the image file. If the image file is in the RAW format, you also need to select its bitmap file.
    6.  Select  **Enable Fast Create**, ensure that the image file has been optimized, and select the sentence following  **Image File Preparation**.

        **Figure  1**  Importing an image file quickly<a name="fig91021219113612"></a>  
        ![](figures/importing-an-image-file-quickly.png "importing-an-image-file-quickly")

    7.  Set parameters as prompted.

        For details about the parameters, see  [Registering an External Image File as a Private Image](registering-an-external-image-file-as-a-private-image-(windows).md)  and  [Registering an External Image File as a Private Image](registering-an-external-image-file-as-a-private-image-(linux).md).

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >-   The OS must be the same as that in the image file.  
        >-   The size of the system disk must be greater than the size in the image file.  
        >    You can use the  **qemu-img-hw**  tool to query for the image file size.  
        >    **qemu-img-hw** **info** _test.zvhd2_  


    Method 2: Create a private image using an API.

    You can use the POST /v2/cloudimages/quickimport/action API to quickly import an image file.

    For details about how to call this API, see "Creating an Image from an Image File Using the Fast Image Creation Function" in  _Image Management Service API Reference_.


## Appendix 1: Common qemu-img-hw Commands<a name="section962713814611"></a>

-   Image file format conversion:  **qemu-img-hw convert -p -O** _Target image format_ _Source image file_ _Target image file_

    The parameters are described as follows:

    **-p**: indicates the conversion progress.

    The part following  **-O**  \(which must be in upper case\) consists of the target image format, source image file, and target image file.

    For example, run the following command to convert a QCOW2 image file to a ZVHD2 file:

    **qemu-img-hw** **convert** **-p** **-O** **zvhd2** **test.qcow2** **test.zvhd2**

-   Querying image file information:  **qemu-img-hw info** _Source image file_

    An example command is  **qemu-img-hw info test.zvhd2**.

-   Viewing help information:  **qemu-img-hw –help**

## Appendix 2: Common Errors During qemu-img-hw Running<a name="section168872043899"></a>

-   Symptom:

    The following information is displayed when you run the  **qemu-img-hw**  command:

    ```
    ./qemu-img-hw: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by ./qemu-img-hw)
    ```

    Solution:

    Run the  **strings /lib64/libc.so.6 | grep glibc**  command to check the glibc version. If the version is too early, install the latest version. Run the following commands in sequence:

    **wget** **http://ftp.gnu.org/gnu/glibc/glibc-2.15.tar.gz**

    **wget** **http://ftp.gnu.org/gnu/glibc/glibc-ports-2.15.tar.gz**

    **tar** **-xvf** **glibc-2.15.tar.gz**

    **tar** **-xvf** **glibc-ports-2.15.tar.gz**

    **mv** **glibc-ports-2.15** **glibc-2.15/ports**

    **mkdir** **glibc-build-2.15**

    **cd** **glibc-build-2.15**

    **../glibc-2.15/configure** **--prefix=/usr** **--disable-profile** **--enable-add-ons** **--with-headers=/usr/include** **--with-binutils=/usr/bin**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If  **configure: error: no acceptable C compiler found in $PATH**  is displayed, run the  **yum -y install gcc**  command.  

    **make**

    **make** **install**

-   Symptom:

    The following information is displayed when you run the  **qemu-img-hw**  command:

    ```
    ./qemu-img-hw: error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory
    ```

    Solution: Run the  **yum install libaio**  command.


