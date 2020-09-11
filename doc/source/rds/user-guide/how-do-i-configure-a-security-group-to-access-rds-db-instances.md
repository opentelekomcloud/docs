# How Do I Configure a Security Group to Access RDS DB Instances?<a name="rds_faq_0054"></a>

-   When you attempt to connect to a DB instance through a private network, check whether the ECS and RDS DB instance are in the same security group.
    -   If the ECS and RDS DB instance are in the same security group, they can communicate with each other by default. No security group rule needs to be configured.
    -   If the ECS and DamengDB instance are in different security groups, you need to configure security group rules for them, separately.
        -   RDS DB instance: Configure an  **inbound rule**  for the security group with which the DB instance is associated.
        -   ECS: The default security group rule allows all outgoing data packets. In this case, you do not need to configure a security rule for the ECS. If not all outbound traffic is allowed in the security group, you need to configure an  **outbound rule**  for the ECS.


-   When you attempt to connect to a DB instance through an EIP, you need to configure an  **inbound rule**  for the security group associated with the DB instance.

