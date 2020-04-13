# Creating a Private Image from a BMS<a name="EN-US_TOPIC_0084807532"></a>

## Scenarios<a name="section9787459153815"></a>

You can create a private image from a BMS and copy the system disk data of the BMS to the private image. The system disk contains an OS and pre-installed applications for running services.

## Constraints<a name="section036311301271"></a>

-   This operation is supported only when the system disk is an EVS disk.
-   Data disks of a BMS cannot be exported as images.
-   The BMS must be stopped.
-   This operation depends on the bms-network-config and Cloud-Init plug-ins in the BMS image.
    -   If the BMS uses a public image, ensure that the image has the bms-network-config and Cloud-Init plug-ins.
    -   If the BMS uses a private image, check whether bms-network-config and Cloud-Init are installed by following the instructions in  _Bare Metal Server Private Image Creation Guide_.


## Precautions<a name="section443273503917"></a>

-   Delete sensitive data from the BMS before using it to creating a private image to prevent data leak.
-   Delete residual files from the OS. For details, see "Deleting Files" in  _Bare Metal Server Private Image Creation Guide_.
-   During the image creation process, do not change the BMS status. Otherwise, the image will fail to be created.

## Procedure<a name="section183213224212"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Locate the row that contains the target BMS, click  **More**  in the  **Operation**  column, and select  **Stop**  from the drop-down list.

    Only a BMS in stopped state can be used to create a private image.

4.  After the BMS status changes to  **Stopped**, click  **More**  in the  **Operation**  column and select  **Make Image**.

    The page for creating an image is displayed.

5.  Enter the image name, set a tag, and specify the description as needed.

    After the parameters are set, click  **Create Now**.

6.  On the displayed page, confirm the specifications and click  **Submit**.
7.  On the displayed image list page, wait for the image status changes to  **Normal**, which indicates that the image is created successfully.

## Follow-up Operations<a name="section11102012213"></a>

If you want to create BMSs using the private image, see  [Creating a BMS Using a Private Image](creating-a-bms-using-a-private-image.md). On the page for creating BMSs, select the private image you have created.

