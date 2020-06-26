# Kafka<a name="EN-US_TOPIC_0125375639"></a>

MRS deploys and hosts Kafka clusters in the cloud based on the open-source Apache Kafka. Kafka is a distributed, partitioned, replicated message publishing and subscription system. It provides features similar to Java Message Service \(JMS\) and has the following enhancements:

-   Message persistency

    Messages are stored in the storage space of clusters in persistence mode and can be used for batch consumption and real-time application programs. Data persistence prevents data loss.

-   High throughput

    High throughput is provided for message publishing and subscription.

-   Reliability

    Message processing methods such as At-Least Once, At-Most Once, and Exactly Once are provided.

-   Distribution

    A distributed system is easy to expand. When new Core nodes are added for capacity expansion, the MRS cluster detects the nodes on which Kafka is installed and adds them to the cluster without interrupting services.


Kafka applies to online and offline message consumption. It is ideal for network service data collection scenarios, such as conventional data collection, website active tracing, data monitoring, and log collection.

For details about Kafka architecture and principles, see  [https://kafka.apache.org/0100/documentation.html](https://kafka.apache.org/0100/documentation.html).

