# What Should I Do If an ECS Cannot Connect to an RDS DB Instance?<a name="rds_faq_0020"></a>

Perform the following steps to identify the problem:

1.  Check whether the ECS and RDS DB instance are located in the same VPC.
    -   If they are in the same VPC, go to  [2](#l76760374fb794a8d9b961321c13f386d).
    -   If they are in different VPCs, create an ECS in the VPC in which the RDS DB instance is located.

2.  <a name="l76760374fb794a8d9b961321c13f386d"></a>Check whether a security group has been added to the ECS.
    -   If a security group has been added, check whether its configuration rules are suitable.

        For details about RDS for MySQL, see the description of security groups in section  [Step 1: Create a DB Instance](step-1-create-a-db-instance-MySQL.md). Then, go to  [3](#lbdf6c75fe0be4c37879e3354bc192d36).

        For details about RDS for PostgreSQL, see the description of security groups in section  [Step 1: Create a DB Instance](step-1-create-a-db-instance-PostgreSQL.md). Then, go to  [3](#lbdf6c75fe0be4c37879e3354bc192d36).

        For details about RDS for Microsoft SQL Server, see the description of security groups in section  [Step 1: Create a DB Instance](step-1-create-a-db-instance-Microsoft-SQL-Server.md). Then, go to  [3](#lbdf6c75fe0be4c37879e3354bc192d36).

    -   If no security group has been added, go to the VPC console from the ECS details page and click  **Security Groups**  to add a security group.

3.  <a name="lbdf6c75fe0be4c37879e3354bc192d36"></a>Check whether the ECS can connect to the RDS DB instance port.

    The default port of RDS for MySQL is  **3306**.

    The default port of RDS for PostgreSQL is  **5432**.

    The default RDS for Microsoft SQL Server port number is  **1433**.

    ```
    telnet <IP address> {port number}
    ```

    -   If the ECS can connect to the RDS DB instance port, the network between the ECS and the RDS DB instance is normal.
    -   If the ECS cannot connect to the port, contact technical support.


