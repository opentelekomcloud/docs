# Creating Encrypted Images<a name="EN-US_TOPIC_0046588155"></a>

You can create an encrypted image using an encrypted ECS or an external image file.

-   Create an  encrypted image  using an encrypted ECS.

    When you use an encrypted ECS system disk to create a private image, the created private image is also encrypted. The key used for encrypting the image is the one used for creating the system disk. For details, see  [Creating a System Disk Image from a Windows ECS](creating-a-system-disk-image-from-a-windows-ecs.md)  and  [Creating a System Disk Image from a Linux ECS](creating-a-system-disk-image-from-a-linux-ecs.md).

-   Create an encrypted image using an external image file.

    When you use an external image file that has been uploaded to an OBS bucket to create a private image, you can select KMS encryption and the key when registering the image to encrypt the image. For details, see  [Creating a Windows System Disk Image from an External Image File](creating-a-windows-system-disk-image-from-an-external-image-file.md)  and  [Creating a Linux System Disk Image from an External Image File](creating-a-linux-system-disk-image-from-an-external-image-file.md).


