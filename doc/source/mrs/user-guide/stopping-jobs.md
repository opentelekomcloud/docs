# Stopping Jobs<a name="EN-US_TOPIC_0125375200"></a>

This section describes how to stop running MRS jobs.

## Background<a name="section40236377113738"></a>

Spark SQL jobs  cannot be stopped. After a job is stopped, its status changes to **Terminated**, and it cannot be executed again.

## Procedure<a name="section8927127113755"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Jobs**.
5.  Select a running job and choose  **More \> Stop** in the **Operation**  column corresponding to the selected job.

    The job status changes from  **Running** to **Terminated**.

    >![](/images/icon-note.gif) **NOTE:**   
    >When you submit a job on the  **Spark SQL** page, you can click **Cancel**  to stop the job.  


