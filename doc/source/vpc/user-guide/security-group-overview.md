# Security Group Overview<a name="en-us_topic_0073379079"></a>

## Security Group Basics<a name="section14990143614615"></a>

A security group is a collection of access control rules for ECSs that have the same security protection requirements and are mutually trusted within a VPC. After a security group is created, you can create different access rules for the security group, these rules will apply to any ECS that is added to this security group.

Your account automatically comes with a default security group. The default security group allows all outbound traffic, denies all inbound traffic, and allows all traffic between ECSs in the group. Your ECSs in this security group can communicate with each other already. You do not need to add additional rules. You can directly use the default security group. For details, see  [Default Security Groups and Security Group Rules](default-security-groups-and-security-group-rules.md).

You can also create custom security groups to meet your specific service requirements. For details, see  [Creating a Security Group](creating-a-security-group.md).

## Security Group Rules<a name="section1293516499168"></a>

After a security group is created, you can add rules to the security group. A rule applies either to inbound traffic \(ingress\) or outbound traffic \(egress\). After ECSs are added to the security group, they are protected by the rules of that group.

Each security group has default rules. For details, see  [Table 1](default-security-groups-and-security-group-rules.md#table1580115155277). You can also customize security group rules. For details, see  [Adding a Security Group Rule](adding-a-security-group-rule.md).

## Security Group Constraints<a name="section1795142593815"></a>

-   By default, you can create up to 100 security groups in your cloud account.
-   By default, each security group can have up to 50 security group rules.
-   By default, an ECS or an ECS extension NIC can be added to a maximum of five security groups.

-   When creating a private network load balancer, you need to select a desired security group. Do not delete the default security group rules or ensure that the following requirements are met:
    -   Outbound rules: only allow data packets to the selected security group or only data packets from the peer load balancer.
    -   Inbound rules: only allow data packets from the selected security group or only data packets from the peer load balancer.


