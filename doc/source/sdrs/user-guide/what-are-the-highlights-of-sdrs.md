# What Are the Highlights of SDRS?<a name="sdrs_06_0430"></a>

SDRS provides the following features:

-   Convenient service recovery

    SDRS provides a management console. You can configure and manage server replication and perform a planned failover or failover.

-   server replication

    You can establish a replication relationship between the production site and the DR site.

-   Replication on demand

    You can replicate servers in an AZ to another AZ as required, thereby reducing the costs and complexity of maintaining another data center.

-   Zero impact on applications

    Applications running on servers can be replicated, and the replication will not have any impact on the applications.

-   High RTO and RPO standard

    For SDRS, recovery time objective \(RTO\) refers to the period from the time when users perform a planned failover or failover at the production site to the time when the servers at the DR site start to run. This period does not include any time for DNS configuration, security group configuration, or customer script execution, and is within 30 minutes.

    SDRS provides continuous and synchronous replication for servers to ensure zero recovery point objective \(RPO\).

-   Crash consistency

    Real-time data synchronization based on storage ensures that data synchronized across two AZs maintains crash consistency. Specifically, the application data across AZs may not be consistent but the disk data across the two AZs remains consistent. 

-   Seamless DR drills

    You can easily perform DR drills without affecting ongoing replication.

-   Flexible failover

    You can perform a planned failover for an expected service interruption to prevent data loss, or perform a failover for unexpected failures to restore services quickly.

-   Efficient network switchover

    SDRS simplifies program resource management during failovers, including reserving IP addresses and MAC addresses, all of which facilitates efficient network switchovers.

-   Excellent performance for the price

    When services are running properly, servers at the DR site are stopped and thereby will not be billed. This greatly reduces the DR TCO.


