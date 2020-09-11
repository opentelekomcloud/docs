# Changing the OS<a name="EN-US_TOPIC_0031523135"></a>

## Scenarios<a name="section44633721195915"></a>

Changing an ECS OS will change the system disk attached to the ECS. After the changing, the system disk ID of the ECS will be changed, and the original system disk will be deleted.

If the OS running on an ECS cannot meet service requirements, change the ECS OS.

The public cloud supports changing between image types \(public images, Marketplace images, private images, and shared images\) and between OSs. You can change your OS to the one of a different image type.

## Constraints<a name="section21723173114530"></a>

-   The EVS disk quota must be greater than 0.
-   H2 ECSs do not support OS change.

## Notes<a name="section34193483165818"></a>

-   After the OS is changed, the original OS is not retained, and the original system disk is deleted.
-   Necessary data has been backed up using either of the following methods. \(Changing the OS clears the data in all partitions of the system disk, including the system partition.\)
-   After the OS is changed, your service running environment must be deployed in the new OS again.
-   After the OS is changed, the ECS will be automatically started.
-   After the OS is changed, the system disk type of the ECS cannot be changed.
-   After the OS is changed, the IP and MAC addresses of the ECS remain unchanged.
-   After the OS is changed, customized configurations, such as DNS and hostname of the original OS will be reset and require reconfiguration.
-   It takes about 10-20 minutes to change the OS. During this process, the ECS is in  **Changing OS**  state.
-   After the OS is changed, the password for logging in to the ECS will be reset. To retrieve the password, perform the following operations:
    -   For a Linux ECS, log in to it using the key and set a new password. For instructions about how to log in to an ECS using a key pair, see  [Login Using an SSH Key](login-using-an-ssh-key.md).
    -   For a Windows ECS, retrieve the password by following the instructions provided in  [Obtaining the Password for Logging In to a Windows ECS](obtaining-the-password-for-logging-in-to-a-windows-ecs.md).


-   The system disk capacity of an ECS with OS changed may change because the system disk capacity specified by the image of the changed OS may be changed.

## Notes on Cross-OS Changing<a name="section1852122261012"></a>

Cross-OS changing indicates that the OS is changed between Windows and Linux.

-   To change Windows to Linux, install an NTFS partition tool, such as NTFS-3G for data reading and writing on the Windows ECS.
-   To change Linux to Windows, install software, such as Ext2Read or Ext2Fsd to identify ext3 or ext4.

    >![](/images/icon-note.gif) **NOTE:**   
    >You are not advised to change Linux to Window on the cloud platform. The reason is as follows: If there are LVM partitions on the Linux ECS, these partitions may fail after the OS is changed to Windows.  


## Prerequisites<a name="section10065433195938"></a>

-   The target ECS is stopped.
-   The target ECS has a system disk attached.
-   Necessary data has been backed up. \(Changing the OS clears the data in all partitions of the system disk, including the system partition.\)
-   If the original ECS uses password authentication while the new ECS uses key pair authentication, ensure that a key pair is available.
-   If a private image is required for changing the ECS OS, create the desired private image by following the instructions provided in  _Image Management Service User Guide_.
    -   If an ECS image is required, make sure that a private image has been created using the ECS.
    -   If a local image file is required, make sure that the image file has been imported to the cloud platform and registered as a private image.
    -   If a private image from another region is required, make sure that the image has been copied.
    -   If a private image from another user account is required, make sure that the image has been shared with you.


## Procedure<a name="section208284422018"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  <a name="en-us_topic_0031523135_en-us_topic_0024911405_li45082966143628"></a>Under  **Computing**, click  **Elastic Cloud Server**.
4.  Select the target ECS and click  **Stop**  in the upper left corner of the ECS list.
5.  Locate the row containing the target ECS. Click  **More**  in the  **Operation**  column and select  **Change OS**.

    The  **Change OS**  page is displayed.

6.  Modify related ECS parameters, such as  **Image Type**  and  **Image**, based on service requirements.

    For more details, see  [Creating an ECS](creating_an_ecs).

7.  \(Optional\) Select a  **License Type**  \(**Use license from the system**  or  **Bring your own license \(BYOL\)**\) if the changed OS running on your ECS is billed. For more details, see  [License Type](license-type.md).

    The following OSs are billed:

    -   SUSE Linux Enterprise Server
    -   Oracle Enterprise Linux
    -   Red Hat Enterprise Linux
    -   Windows Server OS \(BYOL can be used on an ECS that is created on a DeH and runs a Windows Server OS.\)

8.  Configure the login mode.

    If the target ECS uses key pair authentication, you can replace the original key pair.

9.  Click  **OK**.
10. <a name="en-us_topic_0031523135_en-us_topic_0024911405_li45992498111556"></a>On the  **Change ECS OS**  page, confirm the specifications and click  **Submit**.

    After the application is submitted, the ECS status changes to  **Changing OS**. The OS changing has been completed when  **Changing OS**  disappears.

    >![](/images/icon-note.gif) **NOTE:**   
    >A temporary ECS is created during the OS changing process. After the process is complete, this ECS will automatically be deleted.  


## Follow-up Procedure<a name="section6296573110114"></a>

If the OS change is unsuccessful, perform steps  [3](#en-us_topic_0031523135_en-us_topic_0024911405_li45082966143628)  to  [10](#en-us_topic_0031523135_en-us_topic_0024911405_li45992498111556)  again to retry changing the OS again.

If the second OS change attempt is unsuccessful, contact customer service for manual recovery at the backend.

