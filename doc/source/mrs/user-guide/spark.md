# Spark<a name="EN-US_TOPIC_0125375187"></a>

Spark is a distributed and parallel data processing framework. MRS deploys and hosts Apache Spark clusters in the cloud.

Fault-tolerant Spark is a distributed computing framework based on memory, which ensures that data can be quickly restored and recalculated. It is more efficient than MapReduce in terms of iterative data computing.

In the Hadoop ecosystem, Spark and Hadoop are seamlessly interconnected. By using HDFS for data storage and Yarn for resource management and scheduling, users can switch from MapReduce to Spark quickly.

Spark applies to the following scenarios:

-   Data processing and ETL \(extract, transform, and load\)
-   Machine learning
-   Interactive analysis
-   Iterative computing and data reuse. Users benefit more from Spark when they perform operations frequently and the volume of the required data is large.
-   On-demand capacity expansion. This is due to Spark's ease-of-use and low cost in the cloud.

For details about Spark architecture and principles, see  [http://spark.apache.org/docs/2.1.0/quick-start.html](http://spark.apache.org/docs/2.1.0/quick-start.html).

