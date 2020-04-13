# Constraints<a name="en-us_topic_0086739750"></a>

Observe the following constraints when using the NAT Gateway service:

-   Multiple rules for one NAT gateway can reuse the same EIP, but the rules for different NAT gateways must use different EIPs.
-   Each VPC can have only one NAT gateway.
-   Users cannot manually add the default route in a VPC.
-   Only one SNAT rule can be added to a subnet in a VPC.
-   SNAT and DNAT rules cannot share the same EIP.
-   DNAT rules do not support binding an EIP to a virtual IP address.
-   When both the EIP and NAT Gateway services are configured for a server, data will be forwarded through the EIP.
-   The custom CIDR block must be a subset of the VPC subnet CIDR blocks.
-   The custom CIDR block must be a CIDR block of a Direct Connect connection and cannot conflicts with VPC's existing subnet CIDR blocks.

