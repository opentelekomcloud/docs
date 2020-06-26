# Overview<a name="EN-US_TOPIC_0133773658"></a>

If the size of an external image file is greater than 128 GB, you can import the image file through fast import. Only the RAW and ZVHD2 formats support fast import. The image file size cannot exceed 1 TB.

## Import Solution<a name="section6244171371013"></a>

Select a proper import solution based on the image file format.

-   If the file format is ZVHD2, the import solution is as follows: Optimize the image file \> Upload the image file to the OBS bucket \> Register the image file on the cloud platform.
-   If the file format is RAW, the import solution is as follows: Optimize the image file \> Generate a bitmap file for the image file \> Upload the image file and bitmap file to the OBS bucket \> Register the image file on the cloud platform.
-   If the file is not in the ZVHD2 or RAW format, import the file in either of the following ways:
    -   Optimize the image file \> Convert the image file format to ZVHD2 \> Upload the image file to the OBS bucket \> Register the image file on the cloud platform
    -   Optimize the image file \> Convert the image file format to RAW and generate a bitmap file for the image file \> Upload the image file and bitmap file to the OBS bucket \> Register the image file on the cloud platform


>![](/images/icon-note.gif) **NOTE:**   
>-   Fast import is used to import large files. The import of large files depends on the lazy loading feature. The ZVHD2 format supports this feature but the RAW does not. The import of RAW files depends on a bitmap file. Therefore, you need to upload a bitmap file together with the RAW file.  
>-   For details about how to optimize an image file, see  [Optimization Process](optimization-process-(windows).md)  or  [Optimization Process](optimization-process-(linux).md)  depending on the OS type of the image file.  

## Import Process<a name="section1336119141146"></a>

The following describes how to import an external image file in a format other than ZVHD2 or RAW.

You can use  **qemu-img-hw**  in the fast import tool or use the open-source tool  **qemu-img**  to convert the image format.  **qemu-img-hw**  is used only in Linux. This document provides guidance for importing external image files in both Linux and Windows.

>![](/images/icon-note.gif) **NOTE:**   
>The fast import tool consists of  **qemu-img-hw**  \(for converting image formats\) and  **CreateMF.jar**  \(for generating bitmap files\).  

-   Linux

    You are advised to use an EulerOS ECS on the cloud platform.  [Figure 1](#fig1082719127448)  shows the import process.

    **Figure  1**  Import process \(Linux\)<a name="fig1082719127448"></a>  
    ![](figures/import-process-(linux).png "import-process-(linux)")

    For details, see  [Quickly Importing an Image File \(Linux\)](quickly-importing-an-image-file-(linux).md).

-   Windows

    You are advised to use a local PC running Windows.  [Figure 2](#fig0232738181819)  shows the import process.

    >![](/images/icon-note.gif) **NOTE:**   
    >**qemu-img**  cannot convert image files to the ZVHD2 format. Therefore, you need to convert the image files to the RAW format and then use  **CreateMF.jar**  to generate bitmap files.  

    **Figure  2**  Import process \(Windows\)<a name="fig0232738181819"></a>  
    ![](figures/import-process-(windows).png "import-process-(windows)")

    For details, see  [Quickly Importing an Image File \(Windows\)](quickly-importing-an-image-file-(windows).md).


