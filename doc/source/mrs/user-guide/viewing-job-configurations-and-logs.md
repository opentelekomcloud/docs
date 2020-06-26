# Viewing Job Configurations and Logs<a name="EN-US_TOPIC_0125375972"></a>

This section describes how to view job configurations and logs.

## Background<a name="section1147871411155"></a>

-   You can view configurations of all jobs.
-   You can only view logs of running jobs.

    Because logs of Spark SQL and DistCp jobs are not in the background, you cannot view logs of running Spark SQL and DistCp jobs.


## Procedure<a name="section66086406112044"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Jobs**.
5.  In the  **Operation** column corresponding to the selected job, click **View**.

    In the  **View Details**  window that is displayed, configuration of the selected job is displayed.

6.  Select a MapReduce job, and click  **View Log** in the **Operation**  column corresponding to the selected job.

    In the page that is displayed, log information of the selected job is displayed.

    The MapReduce job is only an example. You can view log information about MapReduce, Spark, Spark Script, and Hive Script jobs regardless of their status.

    Each tenant can submit 10 jobs and query 10 logs concurrently.


