# Accessing OBS Using s3a<a name="EN-US_TOPIC_0221415096"></a>

This section describes how to access OBS from MRS using native S3.

## Using Spark to Access OBS<a name="section23291801617"></a>

-   Use a Spark application to access OBS.

    Before accessing OBS, you need to add  **fs.s3a.access.key**  and  **fs.s3a.secret.key**  to the  **core-site.xml**  configuration file of the Spark client. The default path of the  **core-site.xml**  file is  **/opt/client/Spark/spark/conf/core-site.xml**.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >AK and SK will be displayed as plaintext in the configuration file. Exercise caution when setting AK and SK in the file.   

    ```
    <property>
        <name>fs.s3a.access.key</name>
        <value>ak</value>
    </property>
    <property>
        <name>fs.s3a.secret.key</name>
        <value>sk</value>
    </property>
    ```

    The URL for accessing OBS is as follows, where  **s3a**  is the prefix and  **obs-mrsdemo**  is the bucket name.

    ```
    s3a://obs-mrsdemo/input/NEWS.txt
    ```


-   Access OBS in  **spark-sql**  and  **spark-beeline**.

    If you want to access OBS in  **spark-sql**  and  **spark-beeline**, run the following commands to set the AK and SK:

    ```
    set fs.s3a.access.key=ak;
    set fs.s3a.secret.key=sk;
    ```

    Example:

    ```
    0: jdbc:hive2://ha-cluster/default> set fs.s3a.access.key=xxxxxxxxxxx;
    1 row selected (1.322 seconds)
    0: jdbc:hive2://ha-cluster/default> set fs.s3a.secret.key=xxxxxxxxxxxxxxxxxxxxx;
    1 row selected (0.083 seconds)
    0: jdbc:hive2://ha-cluster/default> create table test(id int) location 's3a://obs-demo-input/table/';
    +---------+--+
    | Result  |
    +---------+--+
    +---------+--+
    No rows selected (1.816 seconds)
    ```


## Using HDFS to Access OBS<a name="section178178171469"></a>

-   Enter AK and SK information in the command line.

    ```
    hadoop fs -Dfs.s3a.access.key=ak -Dfs.s3a.secret.key=sk -ls "s3a://obs-bucket"
    ```

-   Add  **fs.s3a.access.key**  and  **fs.s3a.secret.key**  to the  **core-site.xml**  HDFS client configuration file. The default client path of the  **core-site.xml**  file is  **/opt/client/HDFS/hadoop/etc/hadoop/core-site.xml**.

    ```
    <property>
        <name>fs.s3a.access.key</name>
        <value>ak</value>
    </property>
    <property>
        <name>fs.s3a.secret.key</name>
        <value>sk</value>
    </property>
    ```

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >AK and SK will be displayed as plaintext in the configuration file. Exercise caution when setting AK and SK in the file.   

    After the configuration, you do not need to manually add AK and SK to access OBS.

    ```
     hadoop fs -ls "s3a://obs-bucket"
    ```


## Using Hive to Access OBS<a name="section989576583"></a>

Set the following parameters in hive beeline to access OBS.

```
set fs.s3a.access.key=ak;
set fs.s3a.secret.key=sk;
set metaconf:fs.s3a.access.key=ak;
set metaconf:fs.s3a.secret.key=sk;
```

Example:

```
0: jdbc:hive2://10.10.10.10:10000/> set fs.s3a.access.key=xxxxxxxxxxxxxxxx;
No rows affected (0.015 seconds)
0: jdbc:hive2://10.10.10.10:10000/> set fs.s3a.secret.key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;
No rows affected (0.017 seconds)
0: jdbc:hive2://10.10.10.10:10000/> set metaconf:fs.s3a.access.key=xxxxxxxxxxxxxxxx;
No rows affected (0.019 seconds)
0: jdbc:hive2://10.10.10.10:10000/> set metaconf:fs.s3a.secret.key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;
No rows affected (0.003 seconds)
0: jdbc:hive2://10.10.10.10:10000/> create table aa(id string)location 's3a://obs-demo-input/table/';
No rows affected (1.024 seconds)
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When Hive uses OBS to store data, partition and table storage locations in the same table cannot be stored in different buckets.  
>For example, create a partition table and set its storage location to the folder in OBS bucket 1. In this case, modifying the storage location of the table partition does not take effect. When data is inserted, the storage location of the table is used.  
>1.  Create a partition table and specify the path for storing the table.  
>    ```  
>    create table table_name(id int,name string,company string) partitioned by(dt date) row format delimited fields terminated by ',' stored as textfile location "obs://OBS bucket 1/Folder in the bucket";  
>    ```  
>2.  Modifying the storage location of the table partition to another bucket does not take effect.  
>    ```  
>    alter table table_name partition(dt date) set location "obs://OBS bucket 2/Folder in the bucket";  
>    ```  

## Using Presto to Access OBS<a name="section1842192119379"></a>

1.  On MRS Manager and choose  **Services**  \>  **Presto**  \>  **Service Configuration**.
2.  Set  **Type**  to  **All**.
3.  Search for and configure the following parameters:
    -   Set  **hive.s3.aws-access-key**  to  **ak**.
    -   Set  **hive.s3.aws-secret-key**  to  **sk**.
    -   Set  **hive.s3.endpoint**  to the endpoint of the OBS bucket.

4.  Search for the  **core.site.customized.configs**  parameter and add custom parameters.
    -   Set  **fs.s3a.access.key**  to  **ak**.
    -   Set  **fs.s3a.secret.key**  to  **sk**.

5.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Presto service.
6.  Choose  **Components**  \>  **Hive**  \>  **Service Configuration**.
7.  Set  **Type**  to  **All**.
8.  Search for the  **core.site.customized.configs**  parameter and add custom parameters.
    -   Set  **fs.s3a.access.key**  to  **ak**.
    -   Set  **fs.s3a.secret.key**  to  **sk**.
    -   Set  **fs.s3a.endpoint**  to the endpoint of the OBS bucket.

9.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Hive service.
10. On the Presto client, run the following statement to create a schema and set  **location**  to an OBS path:

    **CREATE SCHEMA hive.demo WITH \(location = 's3a://obs-demo/presto-demo/'\);**

11. Create a table in the schema. The table data is stored in the OBS bucket. The following is an example.

    **CREATE TABLE hive.demo.demo\_table WITH \(format = 'ORC'\) AS SELECT \* FROM tpch.sf1.customer;**


