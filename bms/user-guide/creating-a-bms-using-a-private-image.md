# Creating a BMS Using a Private Image<a name="EN-US_TOPIC_0140737793"></a>

## Scenarios<a name="section19544752003"></a>

If you want to create a BMS that has the same OS and applications as an existing BMS, you can create a private image using the existing BMS and then create a BMS using the private image. This frees you from repeatedly configuring BMSs and improves efficiency.

## Background<a name="section1774471612495"></a>

You can create a private image using either of the following methods:

-   [Creating a Private Image from a BMS](creating-a-private-image-from-a-bms.md)
-   [Creating a Private Image from an External Image File](creating-a-private-image-from-an-external-image-file.md)

## Procedure<a name="section881117117416"></a>

Create a BMS by following the instructions in  [Creating a BMS](creating-a-bms.md).

Note for setting the parameters:

-   **Region**: Select the region where the private image is located.
-   **Image**: Select  **Private image**  or  **Shared image**  and select the required image from the drop-down list.
-   **Disk**: If the selected flavor supports quick provisioning, you are advised to increase  **System Disk**  by 2 GB or more.

