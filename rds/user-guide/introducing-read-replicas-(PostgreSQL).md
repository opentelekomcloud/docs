# Introducing Read Replicas<a name="rds_pg_11_0002"></a>

## **Introduction**<a name="section4110332420355"></a>

RDS for PostgreSQL supports  read replicas.

If few write requests but many read requests must be sent to the database, a single DB instance may be unable to handle the read pressure. In this case, operations may be affected. To expand the DB instance read ability to offload read pressure on the database, you can create one or more read replicas in a region. These read replicas can process a large number of read requests and increase application throughput. You need to separately configure connection addresses of the primary DB instance and each read replica on your applications so that all read requests can be sent to read replicas and write requests to the primary DB instance.

A read replica uses the architecture of a single physical node \(without a slave node\). Changes to the primary DB instance are also automatically synchronized to all associated read replicas through the native replication function of PostgreSQL. The synchronization is not affected by network latency. Read replicas and the primary DB instance must be in the same region but can be in different AZs.

## Functions<a name="section439150632066"></a>

-   Specifications of read replicas can be different from those of the primary DB instance, and can be changed at any time to facilitate flexible scaling.
-   You do not need to maintain accounts or databases. Both of them are synchronized from the primary DB instance.
-   Read replicas support system performance monitoring.

    RDS provides up to 20 monitoring metrics, including storage space, IOPS, number of database connections, CPU usage, and network traffic. You can view these metrics to determine the load of DB instances.


## Constraints<a name="section20475080201355"></a>

-   A maximum of five read replicas can be created for a primary DB instance.
-   Read replicas do not support backup settings or temporary backups.
-   Read replicas do not support the creation of temporary DB instances from backup files or point-in-time recovery, and do not support overwriting of DB instances from backup files.
-   Data cannot be migrated to read replicas.
-   Read replicas do not support database creation and deletion.
-   Read replicas do not support account creation. You can create accounts only on primary DB instances.

