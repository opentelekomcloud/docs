# Do Kafka Premium Instances Support Cross-Subnet Access?<a name="EN-US_TOPIC_0151094490"></a>

Yes.

If the client and the instance are in the same VPC, cross-subnet access is supported.

If the client and the instance are in different VPCs, establish a  [VPC peering connection](do-kafka-premium-instances-support-cross-vpc-access.md#EN-US_TOPIC_0151094489).

You can also access an instance through the elastic IP address bound to the instance. For details on how to bind elastic IP addresses to instances, see  [Modifying Instance Parameters](modifying-instance-parameters.md).

