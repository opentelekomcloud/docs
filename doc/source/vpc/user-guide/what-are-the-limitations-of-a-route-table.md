# What Are the Limitations of a Route Table?<a name="vpc_faq_0064"></a>

-   The ECS providing SNAT can have only one NIC.
-   The ECS providing SNAT must have the  **Unbind IP from MAC**  function enabled.
-   The destination of each route in a route table must be unique. The next hop must be a private IP address or a virtual IP address in the VPC. Otherwise, the route table will not take effect.
-   If a virtual IP address is set to the next hop in a route, EIPs bound with the virtual IP address in the VPC will become invalid.

