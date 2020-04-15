# Getting Started with CarbonData<a name="EN-US_TOPIC_0125375478"></a>

This section describes the procedure of using Spark CarbonData. All tasks are based on the Spark-beeline environment. The following tasks are included:

1.  Connect to Spark.

    Before performing any operation on CarbonData, users must connect CarbonData to Spark.

2.  Create a CarbonData table.

    After CarbonData connects to Spark, users must create a CarbonData table to load and query data.

3.  Load data to the CarbonData table.

    Users load data from CSV files in HDFS to the CarbonData table.

4.  Query data in CarbonData.

    After data is loaded to the CarbonData table, users can run query commands such as  **groupby** and **where**.


## Prerequisites<a name="sc03e7daa77f34361912e319fb7b9cad1"></a>

The client has been updated.

## Procedure<a name="sa2350943a81b4731a8196b75f8ac0747"></a>

1.  Connect CarbonData to Spark.
    1.  Log in to the node where the client is installed.

        For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Client Management](client-management.md).

    2.  Switch the user and configure environment variables.

        **sudo su - omm**

        **source /opt/client/bigdata\_env**

    3.  If Kerberos authentication is enabled, run the following command to authenticate the user. If Kerberos authentication is disabled, skip this step.

        **kinit** _**Spark username**_

        The user must be added to the  **hive**  group.

    4.  Run the following command to connect to the Spark environment.

        **spark-beeline**

2.  Create a CarbonData table.

    Run the following command to create a CarbonData table, which is used to load and query data.

    **CREATE TABLE x1 \(imei string, deviceInformationId int, mac string, productdate timestamp, updatetime timestamp, gamePointId double, contractNumber double\)**

    **STORED BY 'org.apache.carbondata.format'**

    **TBLPROPERTIES \('DICTIONARY\_EXCLUDE'='mac','DICTIONARY\_INCLUDE'='deviceInformationId'\);**

    Command result:

    ```
    +---------+--+
    | result  |
    +---------+--+
    +---------+--+
    No rows selected (1.551 seconds)
    ```

3.  Load data from CSV files to the CarbonData table.

    Currently, only CSV files are supported. The CSV column names specified in the  **LOAD**  command must be the same and in the same sequence as the column names in the CarbonData table. The data formats and number of data columns in the CSV files must also be the same as those in the CarbonData table.

    The CSV files must be stored on HDFS. Users can upload the files to OBS and import them from OBS to HDFS on the  **Files** page of the MRS management console. If Kerberos authentication is enabled, prepare the CSV files in the work environment and import them to HDFS using open-source HDFS commands. In addition, assign the Spark user with the read and execute permissions of the files on HDFS.

    For example, the  **data.csv** file is saved in the **tmp**  directory of HDFS and has the following contents:

    ```
    x123,111,dd,2017-04-20 08:51:27,2017-04-20 07:56:51,2222,33333
    ```

    The command for loading data from the file is as follows:

    **LOAD DATA inpath 'hdfs://hacluster/tmp/data.csv' into table x1 options\('DELIMITER'=',','QUOTECHAR'='"','FILEHEADER'='imei, deviceinformationid,mac,productdate,updatetime,gamepointid,contractnumber'\);**

    Command result:

    ```
    +---------+--+
    | Result  |
    +---------+--+
    +---------+--+
    No rows selected (3.039 seconds)
    ```

4.  Query data in the CarbonData table.

    -   **Obtaining the number of records**

        Run the following command to obtain the number of records in the CarbonData table:

        **select count\(\*\) from x1;**

    -   **Querying with the groupby condition**

        Run the following command to obtain the  **deviceinformationid**  records without repetition in the CarbonData table:

        **select deviceinformationid,count \(distinct deviceinformationid\) from x1 group by deviceinformationid;**

    -   **Querying with the where condition**

        Run the following command to obtain specific  **deviceinformationid**  records:

        **select \* from x1 where deviceinformationid='111';**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the query result has Chinese or other non-English characters, the columns in the query result may not be aligned. This is because characters of different languages occupy different widths.  

5.  Run the following command to exit the Spark environment.

    **!quit**


