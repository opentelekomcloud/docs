# What Do I Do If a Subnet Cannot Be Deleted Because It Is Being Used by Other Resources?<a name="vpc_faq_0075"></a>

The VPC service allows you to create private, isolated virtual networks. In a VPC, you can manage private IP address ranges, subnets, route tables, and network gateways. ECSs, BMSs, databases, and some other applications use secure networks created in VPCs.

Subnets in a VPC cannot be deleted if the subnets are used by the following resources:

-   ECS
-   BMS
-   CCE cluster
-   RDS instance
-   Workspace
-   MRS cluster
-   DCS instance
-   Elastic load balancer
-   VPN
-   Private IP address
-   Custom route
-   NAT gateway

Check whether the subnet is used by the preceding resources. If yes, delete all resources in the subnet and delete the subnet. 

