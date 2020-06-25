# Overview<a name="rds_02_0010"></a>

This section describes how to create a PostgreSQL DB instance on the management console and connect to the DB instance through an ECS.

If you are using RDS for the first time, see the constraints described in section  [PostgreSQL Constraints](postgresql-constraints.md).

## Process<a name="section153111118126"></a>

[Figure 1](#fig138110377499)  illustrates the process of connecting to a PostgreSQL DB instance through a private network.

**Figure  1**  Connecting to a DB instance through a private network<a name="fig138110377499"></a>  
![](figures/connecting-to-a-db-instance-through-a-private-network-5.png)

-   [Step 1: Create a DB instance.](step-1-create-a-db-instance-(PostgreSQL).md)  Confirm the specifications, storage, network, and database account configurations of the PostgreSQL DB instances based on service requirements.
-   [Step 2: Configure security group rules.](step-2-configure-security-group-rules-(PostgreSQL).md)
    -   If the ECS and RDS DB instance are in the same security group, they can communicate with each other by default. No security group rule needs to be configured. Go to  [Step 3: Connect to a DB Instance Through psql](step-3-connect-to-a-db-instance-through-psql.md).
    -   If the ECS and RDS DB instance are in different security groups, you need to configure security group rules for them, separately.
        -   RDS DB instance: Configure an  **inbound rule**  for the security group with which the RDS DB instance is associated.
        -   ECS: The default security group rule allows all outgoing data packets. In this case, you do not need to configure a security rule for the ECS. If not all outbound traffic is allowed in the security group, you need to configure an  **outbound rule**  for the ECS.


-   [Step 3: Connect to a DB instance through a private network.](step-3-connect-to-a-db-instance-through-psql.md)  You can connect to a DB instance through a common connection or an SSL connection. The  SSL connection encrypts data  and is more secure. The CLI tool psql is used as an example to describe the connection method.

