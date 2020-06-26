# KafkaManager<a name="EN-US_TOPIC_0221415038"></a>

KafkaManager is a tool for managing Apache Kafka and provides GUI-based metric monitoring and management of Kafka clusters.

KafkaManager supports the following functions:

-   Manage multiple Kafka clusters.
-   Easy inspection of cluster states \(topics, consumers, offsets, partitions, replicas, and nodes\)
-   Run preferred replica election.
-   Generate partition assignments with option to select brokers to use.
-   Run reassignment of partition \(based on generated assignments\).
-   Create a topic with optional topic configurations \(Multiple Kafka cluster versions are supported\).
-   Delete a topic \(only supported on 0.8.2+ and  **delete.topic.enable=true**  is set in broker configuration\).
-   Batch generate partition assignments for multiple topics with option to select brokers to use.
-   Batch run reassignment of partitions for multiple topics.
-   Add partitions to an existing topic.
-   Update configurations for an existing topic.
-   Optionally enable JMX polling for broker-level and topic-level metrics.
-   Optionally filter out consumers that do not have ids/ owner / & offsets/ directories in ZooKeeper. 

