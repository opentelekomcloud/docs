# Application Scenarios<a name="overview_0001"></a>

-   Hosting universal web applications

    You can host web applications and websites in a VPC and use the VPC as a common network. You can use EIPs to connect ECSs to the Internet for running web applications deployed on the ECSs. The VPN gateway is used to establish a VPN channel between the web applications and the service system on the cloud, ensuring high-speed interconnection between the website and the service system.

-   Hosting security-demanding services

    You can create a VPC and security groups to host multi-tier web applications in different security zones. you can associate web servers and database servers with different security groups and configure different access control rules for security groups. You can launch web servers in a publicly accessible subnet and database servers in non-publically accessible subnets to ensure high security and meet requirements of security-demanding scenarios.

-   Extending your corporate network into the cloud

    You can connect a VPC to your private cloud using a VPN connection. With a VPN connection between the VPC and your traditional data center, you can easily use the ECSs and block storage resources. Applications can be migrated to the cloud and additional web servers can be deployed to increase the computing capacity on a network. In this way, a hybrid cloud is built, which reduces IT O&M costs and protects enterprise core data from being leaked. A VPC can span multiple AZs, thereby ensuring high availability of e-commerce systems.


