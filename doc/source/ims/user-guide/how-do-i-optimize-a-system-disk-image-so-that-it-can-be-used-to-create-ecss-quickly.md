# How Do I Optimize a System Disk Image So That It Can Be Used to Create ECSs Quickly?<a name="EN-US_TOPIC_0187108863"></a>

## Scenarios<a name="section92175116555"></a>

If a system disk image supports fast ECS creation, the time required for creating ECSs from it can be greatly reduced. Existing system disk images may not support this function. You are advised to optimize the images using the image replication function.

If image A cannot be used to quickly create ECSs, you can replicate it to generate image copy\_A, which can be used to quickly create ECSs.

## Constraints<a name="section29241710114211"></a>

Full-ECS images cannot be optimized using this method.

## Check Whether an Image Supports Fast ECS Creation<a name="section4115164295317"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.
3.  Click the  **Private Images**  tab to display the image list.
4.  Click the name of the target image.
5.  On the displayed image details page, check the value of  **Fast ECS Creation**.

## Optimize an Image<a name="section039835262019"></a>

1.  Locate the target system disk image, click  **More**  in the  **Operation**  column, and select  **Replicate**  from the drop-down list.

    The  **Replicate Image**  dialog box is displayed.

2.  Set parameters based on  [Replicating Images](replicating-images.md).
3.  After the image is successfully replicated, the generated image can be used to quickly create ECSs.

