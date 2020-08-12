# Manually Backing Up a DCS Instance<a name="en-us_topic_0062866098"></a>

## Scenario<a name="section44639112115"></a>

On the DCS console, you can manually back up data in instances.

By default, manually backed up data is permanently retained. If backup data is no longer in use, you can delete it manually.

## Prerequisites<a name="section17463418112"></a>

At least one master/standby or Proxy Cluster DCS instance is in the  **Running**  state.

## Procedure<a name="section144631511812"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache** **Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance you want to manually back up.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backups & Restorations**.
8.  On the  **Backups & Restorations** page, click **Create Backup**.
9.  In the  **Create Backup **dialog box, click **OK**  to start manual backup.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   Information in the  **Description **text box cannot exceed 128 bytes.
    >-   Instance backup takes 10 to 15 minutes. The data added or modified during the backup process will not be backed up.


