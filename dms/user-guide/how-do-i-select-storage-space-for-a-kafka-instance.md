# How Do I Select Storage Space for a Kafka Instance?<a name="EN-US_TOPIC_0224083319"></a>

The storage space is the space for storing messages. Storage space configurations for a Kafka instance include the disk type and disk size. Currently supported disk types are ultra-high I/O and high I/O. For details about disks, see  [Disk Types and Disk Performance](https://docs.otc.t-systems.com/en-us/usermanual/evs/en-us_topic_0014580744.html).

Set the storage space configurations as required. They cannot be changed once the instance is created.

For example, if the required disk size to store data for the retention period is 100 GB, the disk capacity must be at least:  **100 GB x Number of replicas + 100 GB \(reserved\)**. In a Kafka cluster, each node uses a 33 GB disk to store logs and ZooKeeper data. Therefore, the actual available storage space is less than the purchased storage space.

The number of replicas \(3 by default\) can be configured when you create a topic.

