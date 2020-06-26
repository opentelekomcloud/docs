# Introduction to the Operation Process<a name="EN-US_TOPIC_0125375582"></a>

MRS is easy to use and provides a user-friendly user interface \(UI\). By using computers connected in a cluster, you can run various tasks, and process or store petabytes of data.

After Kerberos authentication is disabled, a typical procedure for using MRS is as follows:

1.  Prepare data.

    Upload the local programs and data files to be computed to Object Storage Service \(OBS\).

2.  Create a cluster.

    Create clusters before you use MRS. The cluster quantity is subject to the Elastic Cloud Server \(ECS\) quantity. Configure basic cluster information to complete cluster creation. You can submit a job at the same time when you create a cluster.

    >![](/images/icon-note.gif) **NOTE:**   
    >When you create a cluster, only one new job can be added. If you need to add more jobs, perform Step  [4](#l0ed995af661d4522a47c26d6cacb63f8).  

3.  Import data.

    After an MRS cluster is successfully created, use the import function of the cluster to import OBS data to HDFS. An MRS cluster can process both OBS data and HDFS data.

4.  <a name="l0ed995af661d4522a47c26d6cacb63f8"></a>Add a job.

    After a cluster is created, you can analyze and process data by adding jobs. Note that MRS provides a platform for executing programs developed by users. You can submit, execute, and monitor such programs by using MRS. After a job is added, the job is in the  **Running**  state by default.

5.  View the execution result.

    The job operation takes a while. After job running is complete, go to the  **Jobs** page, and refresh the job list to view the execution results on the **Jobs**  tab page.

    You cannot execute a successful or failed job, but can add or copy the job. After setting job parameters, you can submit the job again.

6.  Terminate a cluster.

    If you want to terminate a cluster after jobs are complete, click  **Terminate** in **Cluster**. The cluster status changes from **Running** to **Terminating**. After the cluster is terminated, the cluster status will change to **Terminated** and will be displayed in **Cluster History**.


