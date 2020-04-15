# Storm<a name="EN-US_TOPIC_0125375651"></a>

MRS deploys and hosts Storm clusters in the cloud based on the open-source Apache Storm. Storm is a distributed, reliable, fault-tolerant computing system that processes large-volume streaming data in real time. It is applicable to real-time analysis, continuous computing, and distributed extract, transform, and load \(ETL\). It has the following features:

-   Distributed real-time computing

    In a Storm cluster, each node runs multiple work processes; each work process creates multiple threads; each thread executes multiple tasks; and each task processes data concurrently.

-   Fault tolerance

    During message processing, if a node or a process is faulty, the message processing unit can be redeployed.

-   Reliable messages

    Data processing methods At-Least Once, At-Most Once, and Exactly Once are supported.

-   Flexible topology defining and deployment

    The Flux framework is used to define and deploy service topologies. If the service DAG is changed, users only need to modify YAML domain specific language \(DSL\), but do not need to recompile or package service code.

-   Integration with external components

    Storm supports integration with external components such as Kafka, HDFS, and HBase. This facilitates implementation of services that involve multiple data sources.


For details about Storm architecture and principles, see  [http://storm.apache.org/](http://storm.apache.org/).

