# Regions and AZs<a name="en-us_topic_0070904402"></a>

A region is a geographic area in which resources used by DDS are located.

Each region comprises one or more AZs and is completely isolated from other regions. AZs within the same region can communicate with one another through an internal network, while those in different regions cannot communicate with one another through an internal network.

Public cloud data centers are deployed worldwide. DDS applies to different regions. Provisioning DDS to specific regions can better meet user requirements. For example, applications can be designed to better meet specific user requirements or comply with local laws and other demands.

Each region contains many AZs where power and networks are physically isolated. AZs in the same region can communicate with each other over an intranet. Each AZ provides cost-effective and low-latency network connections that are unaffected by faults in other AZs. As a result, provisioning DDS in separate AZs protects your applications against local faults that occur in a single location. DDS supports the deployment of a replica set instance across three AZs. It means that the primary, secondary, and hidden nodes are deployed in three AZs for disaster recovery.

