# What Are the Limitations of VPC Peering?<a name="vpc_faq_0068"></a>

-   VPC peering connections created between VPCs that have overlapping subnet CIDR blocks may not take effect.
-   You cannot have more than one VPC peering connection between the same two VPCs at the same time.
-   You cannot create a VPC peering connection between VPCs in different regions.
-   You cannot use the EIPs in a VPC of a VPC peering connection to access resources in the other VPC. For example, VPC A is peered with VPC B, VPC B has EIPs that can be used to access the Internet, you cannot use EIPs in VPC B to access the Internet from VPC A.
-   To request a VPC peering connection with a VPC of another tenant, the peer tenant must accept the request to activate the connection. If you request a VPC peering connection with a VPC of your own, the system automatically accepts the request to activate the connection.
-   After a VPC peering connection is established, the local and peer tenants must add routes in the local and peer VPCs to enable communication between the two VPCs.
-   VPC A is peered with both VPC B and VPC C. If VPC B and VPC C have overlapping CIDR blocks, routes with the same destinations cannot be added in VPC A.
-   To ensure security, do not accept VPC peering connections from unknown tenants.
-   Either owner of a VPC in a peering connection can delete the VPC peering connection at any time. If a VPC peering connection is deleted by one of its owners, all information about this connection will be automatically deleted immediately, including routes added for the VPC peering connection.
-   Currently, the route table of a VPC takes effect for all subnets in the VPC. You cannot add a route table dedicated for a specific subnet. The route preference is as follows: direct route \> VPC peering connection route \> custom route.
-   If two VPCs in a VPC peering connection have overlapping CIDR blocks, the peering connection can only enable communication between two subnets in the two VPCs. If subnets in the two VPCs of a VPC peering connection have overlapping CIDR blocks, the peering connection will not take effect. When creating a VPC peering connection, ensure that the VPCs involved do not contain overlapping subnets.
-   You cannot delete a VPC for which VPC peering connection routes have been configured.

