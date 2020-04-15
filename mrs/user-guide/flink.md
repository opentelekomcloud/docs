# Flink<a name="EN-US_TOPIC_0221415040"></a>

Flink is a unified computing framework that supports both batch processing and stream processing. It provides a stream data processing engine that supports data distribution and parallel computing. 

Flink provides high-concurrency pipeline data processing, millisecond-level latency, and high reliability, making it extremely suitable for low-latency data processing. 

**The entire Flink system consists of three parts**:

-   Client

    Flink client is used to submit jobs \(streaming jobs\) to Flink.


-   TaskManager

    TaskManager is a service execution node of Flink. It executes specific tasks. A Flink system can have multiple TaskManagers. These TaskManagers are equivalent to each other. 


-   JobManager

    JobManager is a management node of Flink. It manages all TaskManagers and schedules tasks submitted by users to specific TaskManagers. In high-availability \(HA\) mode, multiple JobManagers are deployed. Among these JobManagers, one is selected as the active JobManager, and the others are standby. 


**Flink provides the following features**: 

-   Low latency

    Millisecond-level processing capability


-   Exactly Once

    Asynchronous snapshot mechanism, ensuring that all data is processed only once


-   HA

    Active/standby JobManagers, preventing single points of failure \(SPOFs\)


-   Scale-out

    Manual scale-out supported by TaskManagers


For details about Flink, visit  [https://flink.apache.org/](https://flink.apache.org/).

