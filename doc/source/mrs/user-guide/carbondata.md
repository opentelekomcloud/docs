# CarbonData<a name="EN-US_TOPIC_0125375190"></a>

CarbonData is a new Apache Hadoop file format. It adopts the advanced column-oriented storage, index, compression, and encoding technologies and stores data in HDFS to improve computing efficiency. It helps accelerate the PB-level data query and is applicable to quicker interactive queries. CarbonData is also a high-performance analysis engine that integrates data sources with Spark. Users can execute Spark SQL statements to query and analyze data.

CarbonData has the following features:

-   SQL

    CarbonData is compatible with Spark SQL and supports SQL query operations performed on Spark SQL.

-   Simple definition of table data sets

    CarbonData supports defining and creating data sets by using user-friendly Data Definition Language \(DDL\) statements. CarbonData DDL is flexible and easy to use, and can define complex tables.

-   Convenient data management

    CarbonData provides various data management functions for data loading and maintenance. It can load historical data and incrementally load new data. The loaded data can be deleted according to the loading time and specific data loading operations can be canceled.

-   Quick query response

    CarbonData features high-performance query. It uses dedicated data formats and applies multiple index technologies, global dictionary code, and multiple push-down optimizations. The query speed is 10 times that of Spark SQL.

-   Efficient data compression

    CarbonData compresses data by combining the lightweight and heavyweight compression algorithms. This saves 60% to 80% data storage spaces and the hardware storage cost.


For details about CarbonData architecture and principles, see  [http://carbondata.apache.org/](http://carbondata.apache.org/).

