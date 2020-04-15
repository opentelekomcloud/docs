# Modifying a Backup Task<a name="EN-US_TOPIC_0125375805"></a>

## Scenario<a name="section4592770114628"></a>

Modify the parameters of a created backup task on MRS Manager to meet changing service requirements. The parameters of recovery tasks can be viewed but not modified.

## Impact on the System<a name="section17743278114648"></a>

After a backup task is modified, the new parameters take effect when the task is executed next time.

## Prerequisites<a name="section1999999114656"></a>

-   A backup task has been created.
-   A new backup task policy has been planned based on the actual situation.

## Procedure<a name="section739059411472"></a>

1.  On MRS Manager, choose  **System**  \>  **Back Up Data**.
2.  In the task list, locate a specified task, and click  **Configure** in the **Operation**  column to go to the configuration modification page.
3.  On the page that is displayed, modify the following parameters:

    -   **Start Time**
    -   **Period**
    -   **Target Path**
    -   **Max. Number of Backup Copies**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >After the  **Target Path**  parameter of a backup task is modified, this task will be performed as a full backup task for the first time by default.  

4.  Click  **OK**  to save the settings.

