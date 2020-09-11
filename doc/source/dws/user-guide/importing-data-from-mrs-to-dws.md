# Importing Data from MRS to DWS<a name="en-us_topic_0065840553"></a>

## Importing Data from MRS to a Data Warehouse Cluster<a name="section34418118183527"></a>

MRS is a big data cluster running based on the open source Hadoop ecosystem. It provides the industry's latest cutting-edge storage and analysis capabilities of massive volumes of data, satisfying even the most demanding of your data storage and processing requirements. For details, see the  _MapReduce Service User Guide_.

You can use Hive/Spark \(analysis cluster of MRS\) to store massive volumes of service data. Hive/Spark data files are stored in HDFS. On DWS, you can connect a data warehouse cluster to an MRS cluster, read data from HDFS files, and write the data to DWS when the clusters are on the same network.

## Import Process<a name="section4774472184623"></a>

Perform the following operations to import data from MRS to a data warehouse cluster:

1.  In the data warehouse cluster, create an MRS data source connection according to section  [Creating an MRS Data Source Connection](creating-an-mrs-data-source-connection.md).

    >![](/images/icon-note.gif) **NOTE:**   
    >A connection is also called a  **foreign server**  in databases. Only one connection can exist between a data warehouse cluster and an MRS cluster, but you can connect to multiple MRS clusters through a data warehouse cluster.  

2.  Create an HDFS foreign table for querying data from the MRS cluster over interfaces of a foreign server.

    For details, see section  **Data Import \> Importing Data from MRS to a Cluster**  in the  _Data Warehouse Service Database Developer Guide_.


