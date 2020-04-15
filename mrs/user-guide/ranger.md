# Ranger<a name="EN-US_TOPIC_0228885947"></a>

Apache Ranger offers a centralized security framework and supports fine grained authorization and auditing. It manages fine grained access control over Hadoop and related components, such as HDFS, Hive, HBase, Kafka, and Storm. You can use the front-end web UI console provided by Ranger to configure policies to control users' access to these components.

**The entire Ranger system consists of three parts**:

-   Ranger Admin

    Provides a web UI for users to manage the entire Ranger.

-   Ranger UserSync

    Synchronizes Unix OS users or LADP users to Ranger for unified management.

-   Ranger Plugin

    Provides plug-ins for each component to control the access permissions of each component.


