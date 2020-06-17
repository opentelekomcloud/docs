# Step 2: Configure Security Group Rules<a name="rds_02_0004"></a>

## **Scenarios**<a name="sf45ae489721044578fc3fd08405287ca"></a>

A  security group  is a collection of access control rules for ECSs and RDS DB instances that have the same security protection requirements and are mutually trusted in a VPC.

This section describes how to create a security group to enable specific IP addresses and ports to access RDS.

Check whether the ECS and RDS DB instance are in the same security group.

-   If the ECS and RDS DB instance are in the same security group, they can communicate with each other by default. No security group rule needs to be configured. Go to  [Step 3: Connect to a DB Instance Through a Private Network](step-3-connect-to-a-db-instance-through-a-private-network.md).
-   If the ECS and RDS DB instance are in different security groups, you need to configure security group rules for them, separately.
    -   RDS DB instance: Configure an  **inbound rule**  for the security group with which the RDS DB instance is associated.
    -   ECS: The default security group rule allows all outgoing data packets. In this case, you do not need to configure a security rule for the ECS. If not all outbound traffic is allowed in the security group, you need to configure an  **outbound rule**  for the ECS.


## Precautions<a name="s993d56a9d4e041c2a6546bacf61b28de"></a>

The default security group rule allows all outgoing data packets. ECSs and RDS DB instances can access each other if they are deployed in the same security group. After a security group is created, you can configure security group rules to control access from and to the DB instances in the security group.

-   By default, you can create a maximum of 500 security group rules.
-   Too many security group rules will increase the first packet latency. You are advised to create a maximum of 50 rules for each security group.
-   To access an RDS DB instance from resources outside the security group, you need to configure an  **inbound rule**  for the security group associated with the RDS DB instance.

>![](/images/icon-note.gif) **NOTE:**   
>If you use  **0.0.0.0/0**, you enable all IP addresses to access RDS DB instances in the security group.  

## Procedure<a name="s1180e3b90880473c9b18090acab38155"></a>

1.  Log in to the management console.
2.  Under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
4.  On the  **Security Groups**  page, locate the target security group and click  **Manage Rule**  in the  **Operation**  column.
5.  On the displayed page, click  **Add Rule**.
6.  In the displayed dialog box, set required parameters to add an inbound rule.
7.  Click  **OK**.

