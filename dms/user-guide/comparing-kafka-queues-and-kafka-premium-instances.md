# Comparing Kafka Queues and Kafka Premium Instances<a name="EN-US_TOPIC_0201838022"></a>

Both Kafka premium instances and Kafka queues are compatible with Apache Kafka. However, they differ in the following aspects.

## Open-Source Compatibility<a name="en-us_topic_0165154748_section5294188102115"></a>

-   Kafka queues:

    Kafka 0.10.2.1

-   Kafka premium instances:

    Kafka 2.3.1

    With each version upgrade, Apache Kafka introduces new features, improves APIs, and updates producer and consumer configuration files. To check whether your application features and APIs are compatible with your Kafka clients, see the  [upgrade notes on the official Apache Kafka website](http://kafka.apache.org/documentation.html#upgrade_1_1_0).


## Purchase<a name="en-us_topic_0165154748_section1474825617911"></a>

-   Kafka queues:

    A Kafka queue is created on the DMS console. You do not need to configure the storage space or the bandwidth because these resources are allocated by the system.

-   Kafka premium instances:

    A Kafka premium instance is created on the DMS console. Before creating a Kafka premium instance, determine the required bandwidth and storage space based on your service expectations. You also need to prepare a VPC and security group for the instance.

    After the instance has been created, you must create  [topics](basic-concepts.md#li538132875613)  in the instance and configure the number of partitions and replicas for the topics.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >After a Kafka instance is created, the storage space can be expanded, but the network bandwidth cannot be expanded.  


## Usage<a name="en-us_topic_0165154748_section832916361779"></a>

-   Kafka queues:

    Kafka queues are compatible with Kafka APIs. DMS provides SDKs in Java, Python, Lua, C, and Go languages. For details, see the "DMS Kafka Developer Guide" chapter in the  _Developer Guide_.

-   Kafka premium instances:

    Kafka premium instances are fully compatible with open-source Kafka. You can access Kafka premium instances and topics using  [open-source Kafka clients](https://cwiki.apache.org/confluence/display/KAFKA/Clients). If SASL access is enabled, you must use the  [SSL certificate](https://obs.eu-de.otc.t-systems.com/dms-demo/cert.zip)  downloaded from the DMS console.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For more information about Kafka SASL, see the  [documentation on the Kafka official website](http://kafka.apache.org/documentation/#security_sasl).  


## Performance<a name="en-us_topic_0165154748_section1370713361109"></a>

-   Kafka queues:

    There are two queue modes: high-throughput and high-reliability. In the high-throughput mode, messages are flushed to disk asynchronously, ensuring high concurrency.

-   Kafka premium instances:

    Compute, bandwidth, and storage resources are physically isolated for each instance. Determine the required bandwidth and storage space when creating an instance. For storage space, you can choose  **Ultra-high I/O**, which indicates that messages are stored on SSDs.


## Other Differences<a name="en-us_topic_0165154748_section1628705914274"></a>

You can customize the number of partitions and replicas for a Kafka premium instance. Each topic can have 1 to 20 partitions and 1 to 3 replicas.

By default, a Kafka queue has three partitions and three replicas. If this does not meet your requirements, submit a service ticket.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Divide a topic into a certain number of partitions so that messages can be evenly distributed to partitions, enabling load balancing and horizontal scalability. Different consumers can retrieve messages from one or more partitions, improving message processing performance.  
>With more replicas come higher reliability. However, synchronizing messages between replicas consumes bandwidth and offsets compute performance.  

