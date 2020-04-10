# Creating a Linux ECS from an Image<a name="EN-US_TOPIC_0030713197"></a>

## Scenarios<a name="section17191143145412"></a>

After registering an external image file as a private image on the cloud platform, you can use the image to create ECSs or reinstall or change the OSs of existing ECSs. This section describes how to create an ECS from an image.

## Procedure<a name="section328511235510"></a>

You can create an ECS by referring to  [Creating an ECS from an Image](creating-an-ecs-from-an-image.md).

Note the following when setting the parameters:

-   **Region**: Select the region where the private image is located.
-   **Flavor**: Select a flavor based on the OS type of the image and the OS versions described in  [OSs Supported by Different Types of ECSs](oss-supported-by-different-types-of-ecss.md).
-   **Image**: Select  **Private image**  and then the created image from the drop-down list.

