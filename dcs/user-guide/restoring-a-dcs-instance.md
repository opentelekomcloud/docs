# Restoring a DCS Instance<a name="en-us_topic_0062866099"></a>

## Scenario<a name="section187115171110"></a>

On the DCS console, you can restore backup data to a chosen DCS instance.

## Prerequisites<a name="section271111717112"></a>

-   At least one master/standby or Proxy Cluster DCS instance is in the  **Running**  state.
-   A backup task has been run to back up data in the instance to be restored and the status of the backup task is  **Successful**.

## Procedure<a name="section0711121717114"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache** **Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance you want to restore.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backups & Restorations**.
8.  Click  **Restore**  in the same row as the chosen backup task.
9.  Click **Yes**  to start instance restoration.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   Information in the  **Description**  text box cannot exceed 128 bytes.
    >-   The  **Restoration History**  tab page displays the result of the instance restoration task.
    >-   Instance restoration takes 5 to 30 minutes.
    >-   While being restored, DCS instances do not accept data operation requests from clients because existing data is being overwritten by the backup data.


