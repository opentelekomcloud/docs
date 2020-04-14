# What Can I Do If VPCs in a VPC Peering Connection Cannot Communicate with Each Other?<a name="vpc_faq_0069"></a>

1.  Check whether a VPC peering connection has been successfully created for the two VPCs. Confirm the IDs of the VPCs in the VPC peering connection.
2.  Check whether routes that point to the CIDR block \(or portion of the CIDR block\) of the other VPC have been configured.
3.  Check whether routes configured for the VPC peering connection are correct. If VPCs in a VPC peering connections have overlapping CIDR blocks, you can only add routes to enable communication between two subnets in the two VPCs.
4.  Check whether the VPCs in the VPC peering connection contain overlapping subnets.
5.  Check whether required security group rules have been configured for the ECSs that need to communicate with each other and whether restriction rules have been added to the iptables or firewall used by the ECSs.
6.  If a message indicating that this route already exists is displayed when you add routes for a VPC peering connection, check whether the route's destination IP addresses of the VPN, Direct Connect, and VPC peering connections already exist.
7.  If the route's destination IP addresses of a VPC peering connection overlap with those of a Direct Connect or VPN connection, the route may be invalid.
8.  If VPCs in a VPC peering connection cannot communicate with each other after all these possible faults have been rectified, contact customer service.

