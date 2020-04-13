# Functions<a name="EN-US_TOPIC_0143117111"></a>

DMS enables you to use message queues for transmitting messages among application components. With DMS, application components that send messages and components that receive messages do not have to be available at the same time.

## Queue Types and Access Protocols<a name="section0682111517213"></a>

DMS is compatible with native Kafka queues, enabling you to migrate your message services without any modifications.

-   Multiple queue types

    DMS queues include normal, FIFO, and Kafka queues.

    Kafka premium instances are compatible with open-source Kafka  [topics](basic-concepts.md#li538132875613).

-   Multi-protocol access

    DMS queues support access using HTTP RESTful APIs and the Kafka SDK.

    Kafka premium instances support open-source SDKs using the Kafka protocol.


## Queue Features<a name="section22910190216"></a>

DMS queues support dead letters queues, queue sharing and authorization.

-   Dead letter queue

    Messages failed to be processed are sent to a dead letter queue for analysis and separated processing.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This feature is not supported by Kafka queues and Kafka premium instances.  

-   Queue sharing and authorization

    Queues can be shared and authorized between tenants or users created by the same tenant.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This feature is not supported by Kafka premium instances.  


## Message Features<a name="section123610191724"></a>

DMS queues support the following message capabilities:

-   Message filtering

    Consumers can use labels to filter the messages they want to retrieve from the chosen queue.

-   Message tracking

    Messages that have already been retrieved can be retrieved again from the specified time or position.

-   Intentional delivery delay

    Messages can be delivered after a specified delay.

-   Message broadcasting

    The same message can be delivered to all consumers in a consumer group.

-   Message redelivery

    Messages that will not be immediately retrieved can be returned to the original queues. Consumers can retrieve them when they wish.


## High Reliability<a name="section741710251333"></a>

DMS features up to 99.99999999% data reliability and up to 99.95% service availability.

-   Data reliability

    Data replication and synchronous flushing to disks ensure up to 99.99999999% data reliability.

-   Service availability

    Clustered and cross-AZ deployments ensure up to 99.95% service availability.


## High Performance<a name="section1351871942"></a>

DMS supports massive accumulation of messages, auto scaling of queues, and high concurrency.

-   Massive accumulation

    A single queue can hold hundreds of millions of messages without compromising performance.

-   High concurrency

    Queue throughput reaches up to 100,000 concurrent messages per second. Higher concurrency can be achieved simply by adding queues.

-   Low latency

    Message delivery time is accurate to the millisecond.


## Security<a name="section15217118417"></a>

Operations are traceable and messages are encrypted before being stored.

-   Traceability

    DMS interworks with Cloud Trace Service \(CTS\) to record and audit tenant management operations.

-   Message encryption

    Encrypted message storage protects them from unauthorized access.


