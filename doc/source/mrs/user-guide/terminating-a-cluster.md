# Terminating a Cluster<a name="EN-US_TOPIC_0125375265"></a>

If you do not need an MRS cluster after the job execution is complete, you can terminate the MRS cluster. 

## Background<a name="s684a1cdf4e8a4cda90201e9d17bfef02"></a>

If a cluster is terminated before data processing and analysis are completed, data loss may occur. Therefore, exercise caution when terminating a cluster. If MRS cluster deployment fails, the cluster is automatically terminated.

## Procedure<a name="sed29d729c038409ca93295dd1d8d21b1"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  In the navigation tree of the MRS management console, choose  **Clusters \> Active Clusters**.
4.  In the  **Operation** column of the cluster that you want to terminate, click **Terminate**.

    The cluster status changes from  **Running** to **Terminating**. After the cluster is terminated, the cluster status will change to **Terminated** and will be displayed in **Cluster History**.


