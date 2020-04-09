# How Can I Access an ECS from Another Security Group After an EIP Is Bound to the ECS?<a name="faq_eip_0007"></a>

Each ECS is automatically added to a security group after being created to ensure its security. The security group denies access traffic from the Internet by default. To allow external access to ECSs in the security group, add an inbound rule to the security group.

You can set  **Protocol**  to  **TCP**,  **UDP**,  **ICMP**, or  **All**  as required on the page for creating a security group rule.

-   If the ECS needs to be accessible over the Internet and the IP address used to access the ECS over the Internet has been configured on the ECS, or the ECS does not need to be accessible over the Internet, set  **Source**  to the IP address range containing the IP address that is allowed to access the ECS over the Internet.
-   If the ECS needs to be accessible over the Internet and the IP address used to access the ECS over the Internet has not been configured on the ECS, it is recommended that you retain the default setting  **0.0.0.0/0**  for  **Source**, and then set  **Port Range**  to improve network security.
-   Allocate ECSs that have different Internet access policies to different security groups.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The default source IP address  **0.0.0.0/0**  indicates that all IP addresses can access ECSs in the security group.  


