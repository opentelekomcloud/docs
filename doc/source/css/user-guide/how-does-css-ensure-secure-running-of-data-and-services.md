# How Does CSS Ensure Secure Running of Data and Services?<a name="css_02_0006"></a>

CSS ensures secure running of data and services from the following aspects:

-   Network isolation

    The entire network is divided into two planes: service plane and management plane. The two planes are deployed and isolated physically to ensure the security of the service and management networks.

    -   Service plane: refers to the network plane of the cluster. It provides service channels for users and delivers data definition, index, and search capabilities. 
    -   Management plane: refers to the management console. It is used to manage CSS.

-   Host security

    CSS provides the following security measures:

    -   The VPC security group ensures the security of hosts in a VPC.
    -   Using the network access control list \(ACL\), you can permit or deny the network traffic entering and exiting the subnets. 
    -   Internal security infrastructure \(including the network firewall, intrusion detection system, and protection system\) can monitor all network traffic that enters or exits the VPC through the IPsec VPN. 

-   Data security

    In CSS, the multi-replica mechanism is used to ensure user data security.


