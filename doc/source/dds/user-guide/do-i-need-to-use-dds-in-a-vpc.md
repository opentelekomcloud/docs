# Do I Need to Use DDS in a VPC?<a name="dds_faq_0022"></a>

A VPC allows you to create virtual network environment in a private and isolated network to control the private IP address range, subnets, route tables, and network gateways. The VPC also allows you to define the virtual network topology and network configuration to make the network similar to the traditional IP network you are operating in the data center.

You may need to use DDS in the VPC in the following cases:

You want to run Internet-oriented web applications and retain the backend server that the public cannot access. To do so, you can create an ECS and a DDS DB instance in the same VPC, allocate a public IP address for the ECS, and deploy a web server on the ECS.

