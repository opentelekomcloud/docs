# Task Management<a name="obs_03_0435"></a>

OBS Browser supports the management of upload, download, deletion, and restoration tasks. You can suspend, cancel, or delete tasks using the task management function.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the number of displayed items exceeds 200,000, the system will save the first 100,000 items of tasks that are created earlier to the  **history**  directory in the decompression path of OBS Browser. These items are saved in the  **historyDBData**\[_time stamp_\]**.csv**  files, for example,  **historyDBData20170426T063744.csv**.  

## Procedure<a name="s2e1e8418d7a844de8abe7b9e6c926f07"></a>

1.  Log in to OBS Browser.
2.  In the upper right corner on the page, click  ![](figures/icon-task-management.png).
3.  You can select a task type from the drop-down list box in the upper right corner to query the running tasks.
4.  **Optional**: Select a running task and click  ![](figures/icon-stop.png)  to suspend the task. For a paused task, you can click  ![](figures/icon-start.png)  to continue the task.
5.  **Optional**: Select a running task and click  ![](figures/icon-delete-1.png)  to delete the task.
6.  **Optional**: If the task fails, select the failed task, move the pointer over  ![](figures/icon-info.png)  to view the failure cause, and click  ![](figures/icon-start.png)  to run the task again.
7.  **Optional**: You can select multiple tasks and click  **Run All**,  **Suspend All**, or  **Cancel All**  above the list.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   For tasks in the  **Restoring**  status, the  **Run All**  and  **Suspend All**  buttons do not take effect.  
    >-   The  **Cancel All**  button does not take effect on tasks that are in the  **Restoring**  status, but will delete tasks that fail to be restored.  

8.  **Optional**: Click the  **Completed**  button on the top of the page to view completed tasks. Click  ![](figures/icon-delete-1.png)  next to a finished task to delete the task record.

