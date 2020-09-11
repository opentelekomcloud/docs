# Restoring a DCS Instance<a name="EN-US_TOPIC_0237964732"></a>

## Scenario<a name="section17618221"></a>

On the DCS console, you can restore backup data to a chosen DCS instance.

## Prerequisites<a name="section24346266"></a>

-   At least one master/standby DCS instance is in the  **Running**  state.
-   A backup task has been run to back up data in the instance to be restored and the status of the backup task is  **Successful**.

## Procedure<a name="section17789802"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance you want to restore.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backups & Restorations**.
8.  Click  **Restore**  in the same row as the chosen backup task.
9.  In the  **Restore DCS Instance**  dialog box, click  **OK**  to start instance restoration.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Information in the  **Description**  text box cannot exceed 128 bytes.  
    >-   The  **Restoration History**  tab page displays the result of the instance restoration task.  
    >-   Instance restoration takes 5 to 30 minutes.  
    >-   While being restored, DCS instances do not accept data operation requests from clients because existing data is being overwritten by the backup data.  


