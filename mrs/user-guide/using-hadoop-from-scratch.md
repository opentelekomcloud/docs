# Using Hadoop from Scratch<a name="EN-US_TOPIC_0125375916"></a>

This section describes how to use Hadoop to submit a wordcount job. Wordcount, a typical Hadoop job, is used to count the words in texts.

## Procedure<a name="s455ff9a6f1bf489f9f62dec880435125"></a>

1.  <a name="l524d34c525384f6b9c4fb83c88ec28e8"></a>Prepare the wordcount program.

    The open source Hadoop example program contains the wordcount program. You can download the Hadoop example program at  [https://dist.apache.org/repos/dist/release/hadoop/common/](https://dist.apache.org/repos/dist/release/hadoop/common/).

    For example, select a Hadoop version  **hadoop-2.7.x**. Download **hadoop-2.7.x.tar.gz**, decompress it, and obtain **hadoop-mapreduce-examples-2.7.x.jar** from the **hadoop-2.7.x\\share\\hadoop\\mapreduce** directory. The **hadoop-mapreduce-examples-2.7.x.jar**  example program contains the wordcount program.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >**hadoop-2.7.x**  indicates the Hadoop version.  

2.  <a name="l1959d41cee6e4ff2b70572897ba1d330"></a>Prepare data files.

    There is no format requirement for data files. Prepare one or more TXT files. The following is an example of a TXT file:

    ```
    qwsdfhoedfrffrofhuncckgktpmhutopmma
    jjpsffjfjorgjgtyiuyjmhombmbogohoyhm
    jhheyeombdhuaqqiquyebchdhmamdhdemmj
    doeyhjwedcrfvtgbmojiyhhqssddddddfkf
    kjhhjkehdeiyrudjhfhfhffooqweopuyyyy
    ```

3.  Upload data to OBS.
    1.  Log in to the OBS console.
    2.  Click  **Create Bucket** to create a bucket and name it. The name must be unique; otherwise the bucket cannot be created. Here name **wordcount**  will be used as an example.
    3.  In the  **wordcount** bucket, click **Create Folder** to create the **program**, **input**, **output**, and **log** folders.
        -   **program**: stores user programs.
        -   **input**: stores user data files.

    4.  Go to the  **program** folder, choose  **Upload Object**, click ![](figures/en-us_image_0125375688.jpg) to select the program package downloaded in [1](#l524d34c525384f6b9c4fb83c88ec28e8), and click **Upload Object**.
    5.  Go to the  **input** folder and upload the data file that is prepared in [2](#l1959d41cee6e4ff2b70572897ba1d330).

4.  Log in to the MRS management console. In the navigation tree on the left, choose  **Clusters \> Active Clusters** and click the cluster named **mrs\_20160907**. The **mrs\_20160907** cluster was created in section [Creating a Cluster](creating-a-cluster_quick-start.md).
5.  Submit a wordcount job.

    On the MRS management console, click the  **Jobs**  tab and click  **Create**. The  **Create Job**  page is displayed, as shown in  [Running a MapReduce Job](running-a-mapreduce-job.md).

    -   In  **Type**, select  **MapReduce**.
    -   In  **Name**, enter  **mr\_01**.
    -   In  **Program Path**, select an OBS path, for example,  **obs://wordcount01/program/hadoop-mapreduce-examples-2.7.x.jar**.
    -   In  **Parameters**, enter the following parameters:  **wordcount obs://wordcount01/input/ obs://wordcount01/output/**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   The OBS bucket name in the  **s3a://wordcount01/input/**  parameter must be replaced with the name of the bucket you create.  
        >-   The OBS bucket name in the  **s3a://wordcount01/output/**  parameter must be replaced with the name of the bucket you create.  For  **output**, enter a directory that does not exist.  

    -   You do not need to set  **Service Parameter**.

    Only when the  **mrs\_20160907**  cluster is in the running state can jobs be submitted.

    A job will be executed immediately after being created successfully.

6.  View the job execution results.
    1.  Go to the  **Jobs** tab page. On the **Jobs**  tab page, check whether the jobs are complete.

        The job operation takes a while. After the jobs are complete, refresh the job list.

        You cannot execute a successful or failed job, but can add or copy the job. After setting job parameters, you can submit the job again.

    2.  Log in to the OBS console. Go to the OBS directory and query job output information.

        In the  **wordcount \> output** directory of OBS, you can query and download the job output files.

7.  Terminate a cluster.

    For details, see  [Terminating a Cluster](terminating-a-cluster.md) in the _User Guide_.


