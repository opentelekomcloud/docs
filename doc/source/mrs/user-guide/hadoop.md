# Hadoop<a name="EN-US_TOPIC_0125376141"></a>

MRS deploys and hosts Apache Hadoop clusters in the cloud to provide services featuring high availability and enhanced reliability for big data processing and analysis.

Hadoop is a distributed system architecture that consists of HDFS, MapReduce, and Yarn. The following describes the functions of each component:

-   HDFS:

    HDFS provides high-throughput data access and is applicable to the processing of large data sets. MRS cluster data is stored in HDFS.

-   MapReduce:

    As a programming model that simplifies parallel computing, MapReduce gets its name from two key operations: Map and Reduce. Map divides one task into multiple tasks, and Reduce summarizes their processing results and produces the final analysis result. MRS clusters allow users to submit self-developed MapReduce programs, execute the programs, and obtain the results.

-   Yarn:

    As the resource management system of Hadoop, Yarn manages and schedules resources for applications. MRS uses Yarn to schedule and manage cluster resources.


For details about Hadoop architecture and principles, see  [http://hadoop.apache.org/docs/stable/index.html](http://hadoop.apache.org/docs/stable/index.html).

