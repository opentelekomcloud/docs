# Processing Failed Jobs<a name="EN-US_TOPIC_0056584609"></a>

This section introduces how to handle a failed job.

## Prerequisites<a name="section69681227125613"></a>

At least one failed job exists.

## Context<a name="section109121418141910"></a>

-   After a backup job fails, a backup whose  **Status**  is  **Error**  is generated, and a message is displayed on the  **Backup Jobs**  tab page of  **Job Status**. Click the question mark  ![](figures/icon-problem.png)  next to the message to view details.
-   After a restoration job fails, a message is displayed on the  **Restoration Jobs**  tab page of  **Job Status**. Click  ![](figures/icon-problem.png)  next to the message to view details.

## Procedure<a name="section2038702641915"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  Click the  **Backups**  tab and then click  ![](figures/icon-failed.jpg)  next to  **Job Status**.
3.  On the  **Backup Jobs**  tab page, view the cause of the failed job.
4.  On the  **Restoration Jobs**  tab page, view the cause of the failed job.
5.  Optional: Click  **Delete**  in the row of the failed job to delete the job. Alternatively, click  **Delete All**  in the upper left corner to delete all failed jobs.

