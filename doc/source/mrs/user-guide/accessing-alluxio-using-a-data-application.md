# Accessing Alluxio Using a Data Application<a name="EN-US_TOPIC_0228886231"></a>

The port number used for accessing the Alluxio file system is 19998, and the access address is  **alluxio://<Master node IP address of Alluxio\>:19998/<PATH\>**. This section uses examples to describe how to access the Alluxio file system using data applications \(Spark, Hive, Hadoop MapReduce, and Presto\).

## Using Alluxio as the Input and Output of a Spark Application<a name="section450673117125"></a>

1.  Log in to the Master node in a cluster as user  **root**  using the password set during cluster creation.
2.  Run the following command to configure environment variables:

    **source /opt/client/bigdata\_env**

3.  If Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    Example:  **kinit admin**

4.  Prepare an input file and copy local data to the Alluxio file system.

    For example, prepare the input file  **test\_input.txt**  in the local  **/home**  directory, and run the following command to save the  **test\_input.txt**  file to Alluxio:

    **alluxio fs copyFromLocal /home/test\_input.txt /input**

5.  Run the following commands to start  **spark-shell**:

    **spark-shell**

6.  Run the following command in  **spark-shell**  \(replace  **<Master node IP address of Alluxio\>**  with the actual IP address\):

    **val s = sc.textFile\("alluxio://<Master node IP address of Alluxio\>:19998/input"\)**

    **val double = s.map\(line =\> line + line\)**

    **double.saveAsTextFile\("alluxio://<Master node IP address of Alluxio\>:19998/output"\)**

7.  Run the  **alluxio fs ls /**  command to check whether the output directory  **/output**  containing double content of the input file exists in the root directory of Alluxio.

## Creating a Hive Table on Alluxio<a name="section7925727121811"></a>

1.  Log in to the Master node in a cluster as user  **root**  using the password set during cluster creation.
2.  Run the following command to configure environment variables:

    **source /opt/client/bigdata\_env**

3.  If Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    Example:  **kinit admin**

4.  Prepare an input file. For example, prepare the  **hive\_load.txt**  input file in the local  **/home**  directory. The file content is as follows:

    ```
    1, Alice, company A
    2, Bob, company B
    ```

5.  Run the following command to import the  **hive\_load.txt**  file to Alluxio:

    **alluxio fs copyFromLocal /home/hive\_load.txt /hive\_input**

6.  Run the following command to start the Hive beeline:

    **beeline**

7.  Run the following command \(replace  **<Master node IP address of Alluxio\>**  with the actual IP address\) in the beeline to create a table based on the input file in Alluxio:

    **\>CREATE TABLE u\_user\(id INT, name STRING, company STRING\) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';**

    **\>LOAD DATA INPATH 'alluxio://<Master node IP address of Alluxio\>:19998/hive\_input'  INTO TABLE u\_user;**

8.  Run the following command to view the created table:

    **select \* from u\_user;**


## Running Hadoop Wordcount in Alluxio<a name="section12420127102313"></a>

1.  Log in to the Master node in a cluster as user  **root**  using the password set during cluster creation.
2.  Run the following command to configure environment variables:

    **source /opt/client/bigdata\_env**

3.  If Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    Example:  **kinit admin**

4.  Prepare an input file and copy local data to the Alluxio file system.

    For example, prepare the input file  **test\_input.txt**  in the local  **/home**  directory, and run the following command to save the  **test\_input.txt**  file to Alluxio:

    **alluxio fs copyFromLocal /home/test\_input.txt /input**

5.  Run the wordcount job using  **yarn jar**. \(Replace  **<Master node IP address of Alluxio\>**,  **<Hadoop version\>**, and  **<MRS cluster version\>**  with the actual values.\)

    **yarn jar /opt/share/hadoop-mapreduce-examples-<Hadoop version\>-mrs-<MRS cluster version\>/hadoop-mapreduce-examples-<Hadoop version\>-mrs-<MRS cluster version\>.jar wordcount alluxio://<Master node IP address of Alluxio\>:19998/input alluxio://<Master node IP address of Alluxio\>:19998/output**

6.  Run the  **alluxio fs ls /**  command to check whether the output directory  **/output**  containing the wordcount result exists in the root directory of Alluxio.

## Using Presto to Query Tables in Alluxio<a name="section494714103266"></a>

1.  Log in to the Master node in a cluster as user  **root**  using the password set during cluster creation.
2.  Run the following command to configure environment variables:

    **source /opt/client/bigdata\_env**

3.  If Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    Example:  **kinit admin**

4.  Start the Hive beeline to create a table in Alluxio. \(Replace  **<Master node IP address of Alluxio\>**  with the actual IP address.\)

    **beeline**

    **\>CREATE TABLE u\_user \(id int, name string, company string\) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION 'alluxio://<Master node IP address of Alluxio\>:19998/u\_user';**

    **\>insert into u\_user values\(1,'Alice','Company A'\),\(2, 'Bob', 'Company B'\);**

5.  Start the Presto client. For details, see  [1](using-a-client-to-execute-query-statements.md#li9368161132311)  to  [7](using-a-client-to-execute-query-statements.md#li15202527183812)  in  [Using a Client to Execute Query Statements](using-a-client-to-execute-query-statements.md).
6.  On the Presto client, run the  **select \* from hive.default.u\_user;**  statement to query the table created in Alluxio:

    **Figure  1**  Using Presto to query the table created in Alluxio<a name="fig129013018357"></a>  
    ![](figures/using-presto-to-query-the-table-created-in-alluxio.png "using-presto-to-query-the-table-created-in-alluxio")


