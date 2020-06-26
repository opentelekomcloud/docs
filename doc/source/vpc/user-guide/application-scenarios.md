# Application Scenarios<a name="overview_0002"></a>

-   Hosting web applications

    You can host web applications and websites in a VPC and use the VPC as a regular network. You can use EIPs to connect ECSs to the Internet for running web applications deployed on the ECSs. The VPN gateway is used to establish a VPN tunnel between the web applications and the service system on the cloud, ensuring high-speed interconnection between the website and the service system.

-   Hosting services that demand high security

    You can create a VPC and security groups to host multi-tier web applications in different security zones. You can associate web servers and database servers with different security groups and configure different access control rules for security groups. You can launch web servers in a publicly accessible subnet, but run database servers in subnets that are not publicly accessible. This arrangement ensures high security.

-   Extending your corporate network into the cloud

    You can establish a VPN connection between a VPC and a traditional data center to use the ECSs and block storage resources. Applications can be migrated to the cloud and additional web servers can be quickly deployed as needed when there is a spike in demand for computing resources. This way, less money has to be spent on IT and O&M and data is kept safer than in a traditional arrangement. A VPC can span multiple AZs, protecting from single-points-of-failure and ensuring high availability for e-commerce systems.


