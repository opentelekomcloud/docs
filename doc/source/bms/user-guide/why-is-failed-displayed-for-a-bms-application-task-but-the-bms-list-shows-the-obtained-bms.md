# Why Is  **Failed**  Displayed for a BMS Application Task But the BMS List Shows the Obtained BMS?<a name="EN-US_TOPIC_0053536915"></a>

## Symptom<a name="section6720837161158"></a>

After I apply for a BMS that requires an EIP on the management console, the BMS application request was successfully processed but binding the EIP failed due to insufficient EIPs. In this case,  **Failed**  was displayed for the task in the  **Task Status**  area. However, the requested BMS was displayed in the BMS list.

## Root Cause<a name="section26118472161749"></a>

-   The BMS list shows the details about obtained BMSs.
-   The  **Task Status**  area shows the processing status of the BMS application task, including statuses of sub-tasks, such as preparing for the BMS resource and binding an EIP. Only when all subtasks have succeeded, the task status becomes  **Succeeded**. Otherwise, the task status is  **Failed**.

If the BMS is successfully provisioned but EIP binding fails,  **Failed**  is displayed for the task. The provisioned BMS is temporarily displayed in the BMS list. After the system rolls back the failed task, the BMS is removed from the list.

