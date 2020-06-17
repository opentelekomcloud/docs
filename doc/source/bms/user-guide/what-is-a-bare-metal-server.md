# What Is a Bare Metal Server?<a name="EN-US_TOPIC_0083745256"></a>

## BMS<a name="section61491597525"></a>

Bare Metal Server \(BMS\) features both the scalability of VMs and high performance of physical servers. It provides dedicated servers on the cloud that offer the computing performance and data security required by core databases, key application systems, high-performance computing \(HPC\), and Big Data. You can apply for and use BMSs on demand.

The BMS self-service feature allows you to apply for a BMS by yourself. To apply for a BMS, you only need to specify the server type, image, required network, and other configurations, then you will obtain your requested BMS within 30 minutes. 

## Product Features<a name="section121621427152512"></a>

BMS has the following features:

-   Flavors

    The cloud platform provides various instances types applicable to different scenarios, including computing-optimized, high-performance computing, GPU-accelerated, and memory-optimized. Different types of instances have different CPUs, memory capacity, storage medium, storage capacity, and NIC quantity.

    For more information about instance configurations, see  [Instance Family](instance-family.md).

-   Storage

    BMSs have local disks with different media, interfaces, and capacities. If your services require data redundancy, you are advised to purchase BMSs with RAID cards.

    BMSs that do not have local disks can be booted from Elastic Volume Service \(EVS\) disks. These BMSs can be provisioned in minutes.

-   Networks

    -   Through a Virtual Private Cloud \(VPC\), BMSs can communicate with Elastic Cloud Servers \(ECSs\), GPU-accelerated Cloud Servers \(GACSs\), and other cloud products. VPC provides a 2 Gbit/s or higher bandwidth.
    -   A high-speed network is an internal network among BMSs and provides high bandwidth for connecting BMSs in the same AZ. It provides a 10 Gbit/s or higher bandwidth.
    -   User-defined VLANs are supported. The QinQ technology is used to isolate user networks and provide additional physical planes and network bandwidth.
    -   The IB network features low latency and high bandwidth, and is applicable to various HPC projects.

    For more information about network configurations, see  [Network](network.md).

-   Images

    Public, private, and shared images are supported.


## Access Methods<a name="section1511192815918"></a>

The public cloud provides a web-based service management system. You can access BMS through the management console or HTTPS-compliant application programming interfaces \(APIs\). These two access methods differ as follows:

-   API

    If you want to integrate BMSs on the cloud platform into a third-party system for secondary development, use an API to access BMSs.

-   Management console

    Use this access method for other operations. 


