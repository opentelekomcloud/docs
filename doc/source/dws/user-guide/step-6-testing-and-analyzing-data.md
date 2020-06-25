# Step 6: Testing and Analyzing Data<a name="dws_01_0016"></a>

## Scenario<a name="section1948053215312"></a>

TPC-DS is the benchmark for testing the performance of decision support. With TPC-DS test data and cases, you can simulate complex scenarios, such as big data set statistics, report generation, online query, and data mining, to better understand functions and performance of database applications.

This section describes how to query sample data and perform the test analysis task.

## Prerequisites<a name="section49533351141031"></a>

-   You have imported the sample data to the cluster database. For details, see section  [Step 5: Importing Sample Data to a Data Warehouse Cluster](step-5-importing-sample-data-to-a-data-warehouse-cluster.md).
-   You have logged in to the ECS and configured the DWS client. For details, see section  [Using the ECS to Connect to a Cluster](step-3-connecting-to-a-cluster.md#section99729517811).

## Procedure<a name="section47500191151445"></a>

1.  In the ECS Linux command window, run the following commands to switch to a specific directory and query the sample data:

    ****cd sample/query\_sql/****

    ****/bin/bash tpcds100x.sh****

2.  Enter the cluster's public network IP address, access port, database name, user who accesses the database, and password of the user.

    -   The default database name is  **postgres**.
    -   Use the administrator username and password configured during cluster creation as the username and password for accessing the database. For details, see section  [Step 2: Creating a Cluster](step-2-creating-a-cluster.md).

    After the query is complete, a directory for storing the query result, such as  **query\_output\_20170914\_072341**, will be generated in the current query directory, for example,  **sample/query\_sql/**.


