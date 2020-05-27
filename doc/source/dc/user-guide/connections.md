# Connections<a name="en-us_topic_0112674194"></a>

Connections are abstractions of network circuits between locations on the cloud and local data centers. We provide ports only. After creating a connection, you need to contact the carrier to perform offline construction and set up the physical line for you. Connections are dedicated channels for your local data centers to access VPCs on the cloud. Compared with the traditional public network, connections are more stable, reliable, and secure. They provide a maximum transmission rate of 10 Gbit/s.

Connections support redundant configuration. When there are two connections connected from different locations in the same region, they are mutually redundant and work in active/standby mode. If a connection becomes faulty, services are automatically switched to the other, ensuring stable service running. 

