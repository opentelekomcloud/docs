# Security Group<a name="vpc_Concepts_0005"></a>

A security group is a collection of access control rules for ECSs that have the same security protection requirements and are mutually trusted within a VPC. After a security group is created, you can create different access rules for the security group, these rules will apply to any ECS that is added to this security group.

Your account automatically comes with a security group by default. The default security group allows all outbound traffic, denies all inbound traffic, and allows all traffic between ECSs in the group. Your ECSs in the security group can communicate with each other by default. There is no need to add rules for this.

