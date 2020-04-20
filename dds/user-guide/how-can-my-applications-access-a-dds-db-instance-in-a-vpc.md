# How Can My Applications Access a DDS DB Instance in a VPC?<a name="dds_faq_0016"></a>

Ensure that the ECS where in which your applications are located is in the same VPC and subnet as the DDS DB instance. If the ECS and the DDS DB instance are in different subnets or VPCs, modify the VPC route table and network access control list \(ACL\) to ensure the ECS can access the DDS DB instance.

