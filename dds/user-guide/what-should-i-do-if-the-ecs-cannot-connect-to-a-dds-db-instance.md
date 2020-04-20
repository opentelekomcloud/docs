# What Should I Do If the ECS Cannot Connect to a DDS DB Instance?<a name="dds_faq_0013"></a>

Perform the following steps to identify the problem: The following uses the cluster instance as an example.

1.  Check whether the ECS and DDS DB instance are located in the same VPC.
    -   If they are in the same VPC, go to  [2](#li10923237103639).
    -   If they are in different VPCs, create an ECS in the VPC where the DDS DB instance is located.

2.  <a name="li10923237103639"></a>Check whether a security group has been added to the ECS.
    -   If yes, check whether its configuration rules are suitable. For details, see the security group description in section  [Setting a Security Group](setting-a-security-group(cluster).md). Then, go to  [3](#li2748172710406).
    -   If no security group has been added, go to the VPC console from the ECS details page and click  **Security Groups**  to add a security group.

3.  <a name="li2748172710406"></a>On the ECS, check whether the DDS DB instance address port can be connected.

    ```
    telnet <DB instance address> {8635}
    ```

    -   If the port can be connected, the network is normal. Check the database account and password. For details, see section  [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(cluster).md).
    -   If the port cannot be connected, contact post-sales technical support for troubleshooting.


