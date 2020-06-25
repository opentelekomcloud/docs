# How Can I Check the Network Configuration of a Backend ECS?<a name="EN-US_TOPIC_0115500497"></a>

1.  Verify that the security group of the ECS is correctly configured.
    1.  On the ECS details page, view the security group.
    2.  Check whether the security group permits IP addresses in the 100.125.0.0/16 network segment. If no, add inbound rules for this network segment based on the service requirements.

2.  Verify that the network ACL of the subnet will not intercept the traffic.

    When configuring the network ACL, ensure that the subnets for VPC peering connections are available for network communication.


