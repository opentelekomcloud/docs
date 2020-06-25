# Enabling Advanced Disk<a name="EN-US_TOPIC_0122307169"></a>

## Scenarios<a name="section3591191571"></a>

-   Disk functions have been upgraded on the platform. Newly created ECSs can be attached with up to 60 disks. However, an existing ECS can still be attached with a maximum of 24 disks \(40 for certain ECSs\). To allow such ECSs to be attached with up to 60 disks, enable advanced disk.
-   After advanced disk is enabled, you can view the mapping between device names and disks. For details, see  [What Is the Mapping Between Device Names and Disks?](what-is-the-mapping-between-device-names-and-disks.md)

This section describes how to enable advanced disk on an ECS.

## Procedure<a name="section12913133110717"></a>

1.  Log in to management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  Click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **Disks**  tab.
6.  View the current number of disks that can be attached to the ECS and enable advanced disk as prompted.

    The  **Enable Advanced Disk**  dialog box is displayed.

7.  Click  **OK**.
8.  Stop and then start the target ECS.

    This operation allows advanced disk to take effect.

9.  Switch to the page providing details about the ECS again, click the  **Disks**  tab, and check whether the number of disks that can be attached to the ECS has been changed.
    -   If yes, advanced disk has been enabled.
    -   If no, enabling advanced disk failed. In such a case, try again later or contact customer service.


