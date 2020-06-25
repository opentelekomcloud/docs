# Read/Write Splitting<a name="rds_01_0012"></a>

Both primary DB instances and read replicas of RDS MySQL and PostgreSQL databases have independent connection addresses. A maximum of five read replicas can be created for each primary MySQL or PostgreSQL DB instance. For details about how to create a read replica, see  [Creating a Read Replica](creating-a-read-replica.md)  and  [Managing a Read Replica](managing-a-read-replica.md).

To improve the system processing capability, you do not need to change applications. You only need to create read replicas.

