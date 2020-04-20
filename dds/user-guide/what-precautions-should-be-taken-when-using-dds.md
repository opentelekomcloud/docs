# What Precautions Should Be Taken When Using DDS?<a name="dds_faq_0001"></a>

1.  Failover

    DDS uses multiple mongos, replica sets, and shards to ensure data reliability. When a mongos is faulty, the other mongos takes over services immediately to ensure service continuity. A replica set consists of a primary, a secondary, and a hidden node. When the primary node is faulty, DDS selects the secondary node as the new primary within 30 seconds.

2.  ECSs used for DB instances are invisible to you. Your applications can access the IP addresses and ports corresponding to the database only.
3.  Backup files stored on OBS are invisible to you. They are only visible in the DDS backend management system.
4.  Precautions after applying for DDS:

    After purchasing DDS DB instances, you do not need to perform basic database O&M operations, such as HA and security patches. You need to pay attention to the following:

    1.  Whether the vCPUs, IOPS, and storage space for DDS DB instances are sufficient. If any of them is insufficient, optimize or upgrade the related configuration.
    2.  Whether the performance of DDS DB instances is satisfying, whether a large number of slow query statements exist, whether query statements need to be optimized, and whether any index is redundant or missing.


