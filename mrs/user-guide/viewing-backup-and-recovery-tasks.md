# Viewing Backup and Recovery Tasks<a name="EN-US_TOPIC_0125376039"></a>

## Scenario<a name="section728550114837"></a>

On MRS Manager, view created backup and recovery tasks and check their running status.

## Procedure<a name="section59209364114855"></a>

1.  On MRS Manager, click  **System**.
2.  Click  **Back Up Data** or **Restore Data**.
3.  In the task list, obtain the previous task execution result in the  **Task Progress**  column. Green indicates that the task is executed successfully, and red indicates that the execution fails.
4.  In the  **Operation** column of a specified task in the task list, choose **More \> View History**  to view the task execution records.

    In the displayed window, click  **View** in the **View Details**  column of a specified record to display log information about the execution.


## Related Tasks<a name="section4491308111495"></a>

-   Modifying a backup task

    See  [Modifying a Backup Task](modifying-a-backup-task.md).

-   Viewing a recovery task

    In the task list, locate a specified task and click  **View task** in the **Operation**  column to view a recovery task. The parameters of recovery tasks can only be viewed but not modified.

-   Executing a backup or recovery task

    In the task list, locate a specified task and click  **More**  \>  **Run** or **Start** in the **Operation**  column to start a backup or recovery task that is ready or fails to be executed. Executed recovery tasks cannot be repeatedly executed.

-   Stopping a backup task

    In the task list, locate a specified task and click  **More**  \>  **Stop** in the **Operation**  column to stop a backup task that is running.

-   Deleting a backup or recovery task

    In the task list, locate a specified task and click  **More**  \>  **Delete** in the **Operation**  column to delete a backup or recovery task. Backup data will be reserved by default after a task is deleted.

-   Suspending a backup task

    In the task list, locate a specified task and click  **More**  \>  **Suspend** in the **Operation** column to suspend a backup task. Only periodic backup tasks can be suspended. Suspended backup tasks are no longer executed automatically. When you suspend a backup task that is being executed, the task execution stops. If you want to cancel the suspension status of a task, click **More**  \>  **Resume**.


