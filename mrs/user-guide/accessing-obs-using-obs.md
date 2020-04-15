# Accessing OBS Using obs<a name="EN-US_TOPIC_0221415097"></a>

In versions later than MRS 1.9.2, OBS can be interconnected with MRS using  **obs://**. Currently, Hadoop, Hive, Spark, HBase, Presto, and Flink are supported.

MRS provides two methods for accessing OBS using the  **obs://**  protocol:

## Using Hadoop to Access OBS<a name="section2114171071418"></a>

-   Add the following content to file  **core-site.xml**  in the HDFS directory \(**$client\_home/ HDFS/hadoop/etc/hadoop**\) on the MRS client:

    ```
    <property>
        <name> fs.obs.access.key</name>
        <value>ak</value>
    </property>
    <property>
        <name> fs.obs.secret.key</name>
        <value>sk</value>
    </property>
    <property>
        <name> fs.obs.endpoint</name>
        <value>obs endpoint</value>
    </property>
    ```

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >AK and SK will be displayed as plaintext in the configuration file. Exercise caution when setting AK and SK in the file.  

    After the configuration is added, you can directly access data on OBS without manually adding the AK/SK and endpoint. For example, run the following command to view the file list of folder  **test\_obs\_orc**  in bucket  **obs-test**:

    ****hadoop fs –ls "obs://obs-test/test\_obs\_orc"****

-   Add AK/SK and endpoint to the command line to access data on OBS.

    ****hadoop fs -Dfs.obs.endpoint=xxx -Dfs.obs.access.key=xx -Dfs.obs.secret.key=xx -ls "obs://obs-test/ test\_obs\_orc"****


## Using Hive to Access OBS<a name="section1164714235144"></a>

1.  On MRS Manager and choose  **Services**  \>  **Hive**  \>  **Service Configuration**.
2.  Set  **Type**  to  **All**.
3.  Search for  **fs.obs.access.key**  and  **fs.obs.secret.key**  and set them to the AK and SK of OBS respectively.
4.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Hive service.
5.  Access the OBS directory in the beeline. For example, run the following command to create a Hive table and specify that data is stored in the  **test\_obs**  directory of bucket  **test-bucket**:

    ****create table test\_obs\(a int, b string\) row format delimited fields terminated by "," stored as textfile location "obs://test-bucket/test\_obs";****


## Using Spark to Access OBS<a name="section19812102810147"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>SparkSQL depends on Hive. Therefore, when configuring OBS on Spark, you need to modify the OBS configuration used in  [Using Hive to Access OBS](#section1164714235144).  

-   spark-beeline and spark-sql

    You can add the following OBS attributes to the shell to access OBS:

    ```
    set fs.obs.endpoint=xxx
    set fs.obs.access.key=xxx
    set fs.obs.secret.key=xxx
    ```

-   spark-beeline

    The spark-beeline can access OBS by configuring service parameters in MRS Manager. The procedure is as follows:

    1.  On MRS Manager and choose  **Services**  \>  **Spark**  \>  **Service Configuration**.
    2.  Set  **Type**  to  **All**.
    3.  Choose  **JDBCServer**  \>  **OBS**, and set values for  **fs.obs.access.key**  and  **fs.obs.secret.key**.
    4.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the HBase service.
    5.  Access OBS in  **spark-beeline**. For example, access the  **obs://obs-demo-input/table/**  directory.

        ****create table test\(id int\) location 'obs://obs-demo-input/table/';****


-   spark-sql and spark-submit

    The spark-sql can also access OBS by modifying the  **core-site.xml**  configuration file.

    The method of modifying the configuration file is the same when you use the spark-sql and spark-submit to submit a task to access OBS.

    Add the following content to  **core-site.xml**  in the Spark configuration folder \(**$client\_home/Spark/spark/conf**\) on the MRS client:

    ```
    <property>
        <name> fs.obs.access.key</name>
        <value>ak</value>
    </property>
    <property>
        <name> fs.obs.secret.key</name>
        <value>sk</value>
    </property>
    <property>
        <name> fs.obs.endpoint</name>
        <value>obs endpoint</value>
    </property>
    ```


## Using HBase to Access OBS<a name="section4462193319149"></a>

1.  On MRS Manager and choose  **Services**  \>  **HBase**, and click  **Stop Service**.
2.  Log in to a Master node. For details, see  [Logging In to a Master Node](logging-in-to-a-master-node.md).
3.  Run the following command to initialize environment variables:

    ****source /opt/client/bigdata\_env****

4.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If the Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    For example,  **kinit hbaseuser**.

5.  Run the following command to delete HDFS/ZooKeeper data from the original HBase:

    ****hbase clean --cleanAll****

6.  On MRS Manager and choose  **Services**  \>  **HBase**  \>  **Service Configuration**.
7.  Set  **Type**  to  **All**.
8.  Set the following parameters for accessing OBS:
    -   fs.obs.access.key
    -   fs.obs.secret.key
    -   Set  **hbase.wal.provider**  to  **filesystem**.
    -   Set  **hbase.rootdir**  to the data storage directory, for example,  **obs://bucket \_name/hbase**.

9.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the HBase service.
10. When HBase is used, the HFile data on HBase is stored on OBS by default, and WAL files are still stored on HDFS.

## Using Presto to Access OBS<a name="section1974614263315"></a>

1.  On MRS Manager and choose  **Services**  \>  **Presto**  \>  **Service Configuration**.
2.  Set  **Type**  to  **All**.
3.  Search for and configure the following parameters:
    -   Set  **fs.obs.access.key**  to  **ak**.
    -   Set  **fs.obs.secret.key**  to  **sk**.

4.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Presto service.
5.  Choose  **Components**  \>  **Hive**  \>  **Service Configuration**.
6.  Set  **Type**  to  **All**.
7.  Search for and configure the following parameters:
    -   Set  **fs.obs.access.key**  to  **ak**.
    -   Set  **fs.obs.secret.key**  to  **sk**.

8.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Hive service.
9.  On the Presto client, run the following statement to create a schema and set  **location**  to an OBS path:

    **CREATE SCHEMA hive.demo WITH \(location = 'obs://obs-demo/presto-demo/'\);**

10. Create a table in the schema. The table data is stored in the OBS bucket. The following is an example.

    **CREATE TABLE hive.demo.demo\_table WITH \(format = 'ORC'\) AS SELECT \* FROM tpch.sf1.customer;**


## Using Flink to Access OBS<a name="section269994210283"></a>

Add the following configuration to the Flink configuration file of the MRS client in  **_Client installation path_/Flink/flink/conf/flink-conf.yaml**:

```
fs.obs.access.key:ak
fs.obs.secret.key: sk  
fs.obs.endpoint: obs endpoint
```

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>AK and SK will be displayed as plaintext in the configuration file. Exercise caution when setting AK and SK in the file.  

After the configuration is added, you can directly access data on OBS without manually adding the AK/SK and endpoint.

