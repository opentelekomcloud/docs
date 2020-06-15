# Overview<a name="EN-US_TOPIC_0140323157"></a>

## Security Group<a name="section14990143614615"></a>

A security group is a collection of access control rules for ECSs that have the same security protection requirements and that are mutually trusted within a VPC. After a security group is created, you can create various access rules for the security group, these rules will apply to all ECSs added to this security group.

You can also customize a security group or use the default one. The system provides a default security group for you, which permits all outbound traffic and denies inbound traffic. ECSs in a security group are accessible to each other. For details about the default security group, see  [Default Security Group and Rules](default-security-group-and-rules.md).

## Security Group Rules<a name="section1293516499168"></a>

After a security group is created, you can add rules to the security group. A rule applies either to inbound traffic \(ingress\) or outbound traffic \(egress\). After ECSs are added to the security group, they are protected by the rules of that group.

Each security group has default rules. For details, see  [Default Security Group and Rules](default-security-group-and-rules.md). You can also customize security group rules. For details, see  [Configuring Security Group Rules](configuring-security-group-rules.md).

## Security Group Constraints<a name="section1795142593815"></a>

-   By default, you can create up to 100 security groups in your cloud account.
-   By default, each security group can have up to 50 security group rules.
-   By default, an ECS or an ECS extension NIC can be added to a maximum of five security groups.

-   When creating a private network load balancer, you need to select a desired security group. Do not delete the default security group rules or ensure that the following requirements are met:
    -   Outbound rules: only allow data packets to the selected security group or only data packets from the peer load balancer.
    -   Inbound rules: only allow data packets from the selected security group or only data packets from the peer load balancer.


