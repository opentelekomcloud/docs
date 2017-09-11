## VPC Functions and Application Scenarios
### Functions

A VPC provides the following functions:

-   **Private network customization**

	You can customize private subnets in your VPC and deploy applications and other services in the subnets accordingly.

-   **Flexible security policy configuration**

	You can use security groups to divide ECSs in a VPC into different security zones and then configure different access control rules for each security zone.

	An inbound security group rule enables external access to ECSs in a security group, and an outbound security group rule enables ECSs in a security group to access external networks. If a security group has no access rules after an ECS is added to the security group, the communication between the ECS and the external network is blocked. The default inbound rule enables an ECS to be accessed by other ECSs in the same security group, and the default outbound rule enables ECSs in the security group to access external networks. The security group function cannot resolve the problems caused by network faults or incorrect network configuration. For example, when two ECSs cannot communicate with each other due to the network configuration, they still cannot communicate with each other even if you configure a security group rule to allow the communication between them.

-   **EIP binding**

	You can assign an independent EIP in your VPC. The EIP can be bound to or unbound from an ECS as required. The binding and unbinding operations take effect immediately after the operations are performed.

-   **VPN access**

	By default, ECSs in a VPC cannot communicate with your physical data center or private network. To enable communication between them, you can enable the VPN function.

	A VPN connects your data center or private network to a VPC, enabling you to migrate your applications to the cloud.
### Application Scenarios

-   Host universal web applications

	You can host web applications and websites in a VPC and use the VPC as a common network. You can also create a subnet in the VPC, add ECSs to the subnet, and then assign EIPs to the ECSs to enable the ECSs to communicate with the Internet for running web applications on the ECSs. The VPN gateway is used to establish a VPN channel between the web applications and the service system in the cloud, ensuring high-speed interconnection between the website and the service system.

-   Host security-demanding services

	You can place multi-tier web applications into different security groups, and configure access control rules for each security group as required. In a VPC, you can add the web servers and database servers to different security groups. The subnet to which the web servers belong allows access from the Internet, but the subnet to which the databases belong allows only internal access. This method ensures database server security, meeting high security requirements.

-   Extend your corporate network into the cloud

	You can connect a VPC to your private cloud using a VPN. With the VPN between the VPC and your traditional data center, you can easily use the ECSs and block storage resources. Applications can be migrated to the cloud and additional web servers can be created to increase the computing capacity on a network. In this way, a hybrid cloud is built, which reduces IT O&M costs and protects enterprise core data from being leaked. VPCs can be created across AZs, thereby ensuring high availability of e-commerce systems.
