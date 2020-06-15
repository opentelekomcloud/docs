# Creating a Data Disk Image from an External Image File<a name="EN-US_TOPIC_0084064672"></a>

## Scenarios<a name="section167191841145711"></a>

A  data disk image  contains only your service data. You can use an  external image file  to create a data disk image.

You can also use a data disk image to create EVS disks and migrate your service data to the cloud.

## Constraints<a name="section438627819352"></a>

-   The OS type of the data disk image must be defined, and it can either Windows or Linux.
-   The data disk has about 40 GB to 2048 GB of storage space.
-   When uploading the external image file, you must select an OBS bucket with standard storage.

## Prerequisites<a name="section5577833119352"></a>

You have uploaded an image file to the OBS bucket.

You can import an image file in VHD, VMDK, QCOW2, RAW, VHDX, QCOW, VDI, QED, ZVHD, or ZVHD2 format to the cloud platform. QCOW2 image files are recommended. If you need to import an image file in other formats, use the qemu-img tool to convert the image format before importing the image file. The image file to be imported must be a single image file. For example, you cannot use a pre-allocated image file which depends on two files:  **xxxx.vmdk**  and  **xxxx-flat.vmdk**. Both files can be imported to the cloud platform only after being converted into common VMDK or QCOW2 files.

For details about image file format conversion, see  [Converting the Image Format](converting-the-image-format.md).

## Procedure<a name="section17888236123013"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  In the upper right corner, click  **Create Image**.
4.  In the  **Image Type and Source**  area, select  **Data disk image**  for  **Type**.
5.  Select  **Image File**  for  **Source**. Select the bucket storing the image file from the list and then select the image file.

    **Figure  1**  Creating a data disk image<a name="fig4234441141414"></a>  
    ![](figures/creating-a-data-disk-image-0.png "creating-a-data-disk-image-0")

6.  To register the image file using the Fast Create function, select  **Enable Fast Create**.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Currently, this function supports only image files in ZVHD2 or RAW format.  
    >-   For how to convert image file formats and generate bitmap files, see  [Quickly Importing an Image File](quickly_importing_an_image_file).  

    After you decide to use this function, you need to confirm whether image file is ready for creation.

    -   For ZVHD2 image files: Ensure that the image file format is ZVHD2.
    -   For Raw image files, bitmap files have been uploaded together with the image files.

    If image files are ready, select  **Image File Preparation**.

7.  In the  **Image Information**  area, select an OS type.
8.  Enter the data disk size. Ensure that the entered size is no less than the data disk size in the image file.
9.  Enter the image name and also the description as needed.
10. \(Optional\) If you want to encrypt the image, select  **KMS encryption**  and select the key to be used from the key list.

    When you use an external image file that has been uploaded to your OBS bucket to create a data disk image, you can enable KMS encryption and a key to encrypt the image.

11. Click  **Create Now**.
12. Confirm the parameters and click  **Submit**.

## Follow-up Operations<a name="section14131852173714"></a>

If you want to use the created data disk image to create an EVS disk and attach it to an ECS, you can perform either of the following operations:

-   Locate the row that contains the created data disk image and click  **Apply for Data Disk**  to create one or multiple data disks. Then attach the data disks to an ECS.
-   On the page for creating ECSs, click  **Create Disk from Data Disk Image**  and select the data disk image.

    >![](/images/icon-note.gif) **NOTE:**   
    >A data disk image can be used to create a data disk only once.   


