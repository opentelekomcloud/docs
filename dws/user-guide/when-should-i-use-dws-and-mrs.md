# When Should I Use DWS and MRS?<a name="dws_03_0010"></a>

MRS is recommended if you want to use big data processing frameworks such as Apache Spark, Hadoop, and HBase, to process and analyze ultra-large data sets through custom code. It allows you to control cluster configurations and software installed in the cluster.

DWS is designed for analysis of different types of data. It aims to pool data from different sources together, such as inventory, finance, and retail system. To ensure consistency and accuracy of enterprises' reports, DWS stores data in a highly structured manner. This structure can directly build the data consistency rule to the database table. Additionally, DWS is highly compatible with standard SQL statements and the syntax of conventional transaction-supported databases.

DWS is preferred when you want to perform complex query of a large amount of structured data with high performance.

