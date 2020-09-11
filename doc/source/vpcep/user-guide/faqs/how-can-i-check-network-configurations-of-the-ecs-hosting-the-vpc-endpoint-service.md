# How Can I Check Network Configurations of the ECS Hosting the VPC Endpoint Service?<a name="en-us_topic_0138838187"></a>

1.  Confirm that the security group of the ECS NIC is correctly configured.
    -   On the ECS details page, view the security group details.
    -   Check whether the security group permits IP addresses in the 198.19.128.0/20 network segment in the inbound direction. If it does not, add inbound rules for this network segment based on service requirements.

2.  Confirm that the firewall for the subnet used by the ECS NIC does not block traffic.

    If you can configure the firewall on the left part of the VPC console, confirm that the subnet of the associated VPC endpoint allows traffic to pass through.

    For details about how to disable the firewall, see  [Enabling or Disabling a Firewall](https://docs.otc.t-systems.com/en-us/usermanual/vpc/vpc_acl_0011.html)  in the  _Virtual Private Cloud User Guide_.


