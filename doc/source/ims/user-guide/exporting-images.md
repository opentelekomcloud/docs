# Exporting Images<a name="EN-US_TOPIC_0034011241"></a>

## Scenarios<a name="section524694217214"></a>

You can export private images to specified storage devices and use the private images on other platforms.

You can export private images to OBS buckets in specified format and then download images to specified storage devices from the buckets.

Images exported in different formats may vary in size.

## Constraints<a name="section12716918161831"></a>

-   Images can only be exported to standard OBS buckets.
-   You can export private images in the  **Normal**  or  **Normal \(Uninitialized\)**  status.
-   You cannot export Windows or SUSE public images or private images created from these public images.
-   Full-ECS images cannot be exported.
-   You can only export images smaller than 128 GB.
-   You can export images only in the format of VMDK, VHD, QCOW2, or ZVHD.
-   You cannot export images created using CSBS backups.
-   If a market image is used to create an ECS and then the ECS is used to create a private image, this private image cannot be exported.

## Prerequisites<a name="section38081590162757"></a>

You have an OBS bucket.

For details about OBS operations, see  _Object Storage Service User Guide_.

## Procedure<a name="section51496588162929"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed. 

3.  Locate the row that contains the image to be exported, click  **More**  in the  **Operation**  column and select  **Export**.
4.  In the displayed  **Export Image**  dialog box, set the following parameters:
    -   **Format**: Select one from  **qcow2**,  **vmdk**,  **vhd**, and  **zvhd**  as you need.
    -   **Name**: Enter a name that is easy to identify.
    -   **Storage Path**: Click  ![](figures/image-8.png)  to expand the bucket list and select an OBS bucket for storing the exported image.

5.  Click  **OK**.

    You can view the image export progress above the private image list. After the image is successfully exported, you can download the image from the OBS bucket on the OBS console or OBS Browser.


