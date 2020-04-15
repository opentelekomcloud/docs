# Using Spark from Scratch<a name="EN-US_TOPIC_0125375446"></a>

This section describes how to use Spark to submit a sparkPi job. SparkPi, a typical Spark job, is used to calculate the value of pi \(π\).

## Procedure<a name="s975d789db3f14bff9ce57a2cfd30992c"></a>

1.  <a name="l16861bd9eed2462b8c8624a720cf5ab5"></a>Prepare the sparkPi program.

    The open source Spark example program contains the sparkPi program. You can download the Spark example program at  [https://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz](https://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz)

    Decompress the Spark example program to obtain the  **spark-examples\_2.11-2.1.0.jar** file in the **spark-2.1.0-bin-hadoop2.7/examples/jars** directory. The **spark-examples\_2.11-2.1.0.jar**  example program contains the sparkPi program.

2.  Upload data to OBS.
    1.  Log in to the OBS console.
    2.  Click  **Create Bucket** to create a bucket and name it. The name must be unique; otherwise the bucket cannot be created. Here name **sparkPi**  will be used as an example.
    3.  In the  **sparkpi** bucket, click **Create Folder** to create the **program**, **output**, and **log** folders.
    4.  Go to the  **program** folder, choose  **Upload Object**, click ![](figures/en-us_image_0125375462.jpg) to select the program package downloaded in [1](#l16861bd9eed2462b8c8624a720cf5ab5), and click **Upload Object**.

3.  Log in to the MRS management console. In the navigation tree on the left, choose  **Clusters \> Active Clusters** and click the cluster named **mrs\_20160907**. The **mrs\_20160907** cluster was created in section [Creating a Cluster](creating-a-cluster_quick-start.md).
4.  Submit a sparkPi job.
    1.  Select  **Jobs**. On the **Jobs** tab page, click **Create** to go to the **Create Job** page. For details, see  [Running a Spark Job](running-a-spark-job.md).

        Only when the  **mrs\_20160907**  cluster is in the running state can jobs be submitted.

        A job will be executed immediately after being created successfully.

5.  View the job execution results.
    1.  Go to the  **Jobs** tab page. On the **Jobs**  tab page, check whether the jobs are complete.

        The job operation takes a while. After the jobs are complete, refresh the job list.

        You cannot execute a successful or failed job, but can add or copy the job. After setting job parameters, you can submit the job again.

    2.  Go to the OBS directory and query job output information.

        In the  **sparkpi \> output**  directory of OBS, you can query and download the job output files.

6.  Terminate a cluster.

    For details, see  [Terminating a Cluster](terminating-a-cluster.md) in the _User Guide_.


