# Using Spark SQL from Scratch<a name="EN-US_TOPIC_0125375960"></a>

To process structured data, Spark provides Spark SQL, which is similar to SQL.

You can create a table named  **src\_data**, write a data entry in each row of the **src\_data** table, and store data in the **mrs\_20160907** cluster. You can then use SQL statements to query data in the **src\_data** table. Afterward, you can delete the **src\_data**  table.

## Prerequisites<a name="sbc3c67a140b94c4c90dc08ed743a08c1"></a>

You have obtained the AK/SK for writing data from the OBS data source to the Spark SQL table. The method for obtaining the AK/SK is as follows:

1.  Log in to the management console.
2.  Click the username and choose  **My Credential**  from the drop-down list.
3.  Click  **Access Keys**.
4.  Click  **Add Access Key** to switch to the **Add Access Key**  page.
5.  Enter the login password, the verification code received in the email and click **OK**  to download the access key. Keep the access key secure.

## Procedure<a name="see9e426bc69841e481590f8e4fa4db3f"></a>

1.  Prepare data sources for Spark SQL analysis.

    The following is an example of a text file:

    ```
    abcd3ghji
    efgh658ko
    1234jjyu9
    7h8kodfg1
    kk99icxz3
    ```

2.  Upload data to OBS.
    1.  Log in to the OBS management console.
    2.  Click  **Create Bucket** to create a bucket and name it. The name must be unique or else the bucket cannot be created. Here name **sparksql**  will be used as an example.
    3.  In the  **sparksql** bucket, click **Create Folder** to create the **input**  folder.
    4.  Go to the input folder, click  ![](figures/icon_mrs_obsmanu.jpg) to select a local text file, and click **Upload Object**.

3.  Import the text file in OBS to HDFS.
    1.  Log in to the MRS management console. In the navigation tree on the left, choose  **Clusters \> Active Clusters** and click the cluster named **mrs\_20160907**. The **mrs\_20160907** cluster was created in section [Creating a Cluster](creating-a-cluster_quick-start.md).
    2.  Select  **Files** tab page.
    3.  Click  **Create Folder** and create the **userinput**  file folder.
    4.  Go to the  **userinput** file folder, and click **Import Data**.
    5.  Select the OBS and HDFS paths and click  **OK**.

        OBS path:  **s3a://sparksql/input/sparksql-test.txt**

        HDFS path:  **/user/userinput**

4.  Submit the Spark SQL statement.
    1.  On the  **Jobs** tab page, select **Spark SQL**. The Spark SQL job page is displayed.

        Only when the  **mrs\_20160907**  cluster is in the running state can jobs be submitted.

    2.  Enter the Spark SQL statement to create a table.

        When entering Spark SQL statements, ensure that the characters contained are fewer than 10,000.

        The syntax is as follows:

        **CREATE** \[EXTERNAL\] **TABLE** \[IF NOT EXISTS\] _table\_name_ \[\(col\_name data\_type \[COMMENT col\_comment\], ...\)\] \[COMMENT table\_comment\] \[PARTITIONED **BY** \(col\_name data\_type \[COMMENT col\_comment\], ...\)\] \[CLUSTERED **BY** \(col\_name, col\_name, ...\) \[SORTED **BY** \(col\_name \[ASC|DESC\], ...\)\] INTO num\_buckets BUCKETS\] \[ROW FORMAT row\_format\] \[STORED **AS**  file\_format\] \[LOCATION hdfs\_path\];

        You can use either of the following two methods to create a table:

        -   Method 1: Create table  **src\_data**  and write data in every row.

            The data source is stored in the  **/user/userinput** file folder of HDFS: **create external table** _src\_data_**\(line string\) row format delimited fields terminated by '\\\\n' stored as textfile location** '_/user/userinput_'**;**

            The data source is stored in the  **/sparksql/input** file folder of OBS: **create external table** _src\_data_**\(line string\) row format delimited fields terminated by '\\\\n' stored as textfile location** '_s3a://AK:SK@sparksql/input_';

            For the method of obtaining the AK/SK, see the description in  [Prerequisites](#sbc3c67a140b94c4c90dc08ed743a08c1).

        -   Method 2: Create table  **src\_data1** and load data to the **src\_data1**  table in batches.

            **create table** _src\_data1_ **\(line string\) row format delimited fields terminated by ',' ;**

            **load data inpath** '_/user/userinput/sparksql-test.txt_' **into table** _src\_data1_**;**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >When method 2 is used, the data from OBS cannot be loaded to the created tables directly.  

    3.  Enter the Spark SQL statement to query a table.

        The syntax is as follows:

        **SELECT** col\_name **FROM** _table\_name_;

        To query data in the  **src\_data**  table, for example, enter the following statement:

        **select \* from src\_data;**

    4.  Enter the Spark SQL statement to delete a table.

        The syntax is as follows:

        **DROP TABLE** \[IF EXISTS\] _table\_name;_

        For example:

        **drop table src\_data;**

    5.  Click  **Check**  to check whether the statements are correct.
    6.  Click  **Submit**.

        After submitting Spark SQL statements, you can check whether the execution is successful in  **Last Execution Result** and view detailed execution results in **Last Query Result Set**.

5.  Terminate a cluster.

    For details, see  [Terminating a Cluster](terminating-a-cluster.md) in the _User Guide_.


