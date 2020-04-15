# What Is the Relationship Between Hive and Other Components?<a name="EN-US_TOPIC_0125375277"></a>

-   Relationship between Hive and HDFS

    Hive is the subproject of Apache Hadoop. Hive uses HDFS as the file storage system. Hive parses and processes structured data, and HDFS provides highly reliable underlying storage support for Hive. All data files in the Hive database are stored in HDFS, and all data operations on Hive are also performed using HDFS APIs.

-   Relationship between Hive and MapReduce

    Hive data computing depends on MapReduce. MapReduce is a subproject of Apache Hadoop. It is a parallel computing framework based on HDFS. During data analysis, Hive translates HiveQL statements submitted by users into MapReduce jobs and submits the jobs to MapReduce for execution.

-   Relationship between Hive and DBService

    MetaStore \(metadata service\) of Hive processes the structure and attribute information about Hive databases, tables, and partitions. The information needs to be stored in a relational database and is maintained and processed by MetaStore. In MRS, the relational database is maintained by the DBService component.

-   Relationship between Hive and Spark

    Hive data computing can be implemented on Spark. Spark is an Apache project. It is a distributed computing framework based on memory. During data analysis, Hive translates HiveQL statements submitted by users into Spark jobs and submits the jobs to Spark for execution.


