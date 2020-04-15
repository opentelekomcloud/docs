# Creating an Image<a name="EN-US_TOPIC_0101604508"></a>

## Scenarios<a name="section87874817127"></a>

You can use an existing ECS to create a system disk image, data disk image, and full-ECS image.

-   System disk image: contains an OS and application software for running services. You can use a system disk image to create ECSs and migrate your services to the cloud.
-   Data disk image: contains only service data. You can create a data disk image from an ECS data disk. You can also use a data disk image to create EVS disks and migrate your service data to the cloud.
-   Full-ECS image: contains the data of an ECS, including the data on the data disks attached to the ECS. A full-ECS image can be used to rapidly create ECSs with service data.

If you plan to use a private image to change the OS, ensure that the private image is available. For instructions about how to create a private image, see  _Image Management Service User Guide_.

## Procedure<a name="section1685231310443"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  Locate the row that contains the ECS, click  **More**  in the  **Operation**  column, and select  **Create Image**.
5.  Configure image information as prompted.
    -   **Source**:  **ECS**
    -   **ECS**: Retain default settings.
    -   **Name**: Customize your image name.

6.  Click  **Submit**.

