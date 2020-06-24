# Manually Backing Up a DCS Instance<a name="EN-US_TOPIC_0237964731"></a>

## Scenario<a name="section62417850"></a>

On the DCS console, you can manually back up data in instances.

By default, manually backed up data is permanently retained. If backup data is no longer in use, you can delete it manually.

## Prerequisites<a name="section24889743"></a>

At least one master/standby DCS instance is in the  **Running**  state.

## Procedure<a name="section22681099"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance you want to manually back up.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backups & Restorations**.
8.  On the  **Backups & Restorations**  page, click  **Create Backup**.
9.  In the  **Create Backup**  dialog box, click  **OK**  to start manual backup.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Information in the  **Description**  text box cannot exceed 128 bytes.  
    >-   Instance backup takes 10 to 15 minutes. The data added or modified during the backup process will not be backed up.  


