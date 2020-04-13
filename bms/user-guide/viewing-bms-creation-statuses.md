# Viewing BMS Creation Statuses<a name="EN-US_TOPIC_0053536924"></a>

## **Scenarios**<a name="section49701611171023"></a>

After clicking  **Submit**  to request a BMS, you can query the task status in the  **Task Status**  area. A task involves several sub-tasks, such as creating a BMS resource, binding an EIP, and attaching an EVS disk.

The task status may be either  **Creating**  or  **Failed**:

-   **Processing**: The system is processing the task.
-   **Failed**: The system has failed to process the task. The system rolls back the failed task and displays an error code, for example,  **\(BMS.3033\) Failed to create system disk**.

This section describes how to query BMS application processing status and the information displayed in the  **Task Status**  area.

## **Procedure**<a name="section40936232171845"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  **Task Status**  is displayed on the right of common operations, such as  **Start**,  **Stop**,  **Restart**, and  **Delete**. After you apply for a BMS, the  **Task Status**  area will show the task processing status.

    **Figure  1**  BMS application status<a name="fig15281205162813"></a>  
    ![](figures/bms-application-status.png "bms-application-status")

4.  Click the number displayed in the  **Task Status**  area to view details about the BMS application processing status. The tasks in  **Processing**  and  **Failed**  statuses are displayed.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If  **Failed**  is displayed for a task in the  **Task Status**  area, but the BMS list contains the BMS, handle this issue by following the instructions in  [Why Is Failed Displayed for a BMS Application Task But the BMS List Shows the Obtained BMS?](why-is-failed-displayed-for-a-bms-application-task-but-the-bms-list-shows-the-obtained-bms.md).  


