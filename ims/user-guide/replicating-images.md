# Replicating Images<a name="EN-US_TOPIC_0049177180"></a>

## Scenarios<a name="section813670151747"></a>

You can convert encrypted and unencrypted images into each other or enable some advanced features \(such as fast ECS creation from an image\) using the image replication function. You may need to  replicate an image  in the following scenarios:

-   Replicate an encrypted image to an unencrypted one.

    Encrypted images cannot be shared with other tenants or published as a Marketplace image. If you want to publish or share an encrypted image, you can replicate it to an unencrypted one.

-   Replicate an encrypted image to an encrypted one.

    Keys for encrypting the images cannot be changed. If you want to change the key of an encrypted image, you can replicate this image to a new one and encrypt the new image using an encryption key.

-   Replicate an unencrypted image to an encrypted one.

    If you want to store an unencrypted image in an encrypted way, you can replicate this image as a new one and encrypt the new image using a key.

-   Optimize a system disk image so that it can be used to quickly create ECSs.

    If a system disk image supports fast ECS creation, the time required for creating ECSs from it can be greatly reduced. Existing system disk images may not support this function. You can optimize the images using the image replication function. If image A cannot be used to quickly create ECSs, you can replicate it to generate image copy\_A, which can be used to quickly create ECSs.


## Constraints<a name="section9136389151747"></a>

You can replicate private images in  **Normal**  or  **Normal \(Uninitialized\)**  state.

Full-ECS images cannot be replicated.

## Prerequisites<a name="section30553689151747"></a>

The image to be replicated is in  **Normal**  or  **Normal \(Uninitialized\)**  state.

## Procedure<a name="section33501422151747"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  Locate the row that contains the image to be replicated, click  **More**  in the  **Operation**  column, and select  **Replicate**.
4.  In the displayed  **Replicate Image**  dialog box, set the following parameters:
    -   **Name**: Enter a name that is easy to identify.
    -   **Description**: Enter the description of the image. This parameter is optional.
    -   **Encryption**: If you want to encrypt the image or change a key, select  **KMS encryption**  and select the key you want to use from the drop-down list.

5.  Click  **OK**.

    On the  **Private Images**  page, view the replication progress. If the status of the new image becomes  **Normal**, the image replication is successful.


