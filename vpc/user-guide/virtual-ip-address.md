# Virtual IP Address<a name="vpc_Concepts_0012"></a>

A virtual IP address \(VIP\) is an IP address that is not allocated to an actual ECS NIC. An ECS can have both private and virtual IP addresses, and you can access the ECS through either one. A virtual IP address has the same network access capabilities as a private IP address, including layer 2 and layer 3 communication in VPCs, access between VPCs using peering connections, as well as Internet access through EIPs, VPN connections, and Direct Connect connections.

Multiple ECSs deployed in active/standby mode can be bound to the same virtual IP address. The virtual IP address can then be bound to an EIP. When someone accesses that EIP from the Internet, since the virtual IP address has made it possible to link active/standby mode copies of ECSs, those ECSs are highly fault tolerant.

## Networking<a name="section766193134213"></a>

Virtual IP addresses are used for high availability as they make active/standby ECS switchover possible. If the active ECS becomes faulty and cannot provide services, the virtual IP address is dynamically switched to the standby ECS and services continue uninterrupted. ECSs can be configured for HA or as load balancing clusters.

-   **Networking mode 1**: HA

    If you want to improve service availability and avoid single points of failure, you can deploy ECSs in the active/standby mode or one active and multiple standby mode. In this arrangement, the ECSs all use the same virtual IP address. If the active ECS becomes faulty, a standby ECS takes over services from the active ECS and services continue uninterrupted.

    **Figure  1**  Networking diagram of the HA mode<a name="en-us_topic_0206027322_fig127741244152518"></a>  
    ![](figures/networking-diagram-of-the-ha-mode.png "networking-diagram-of-the-ha-mode")

    -   In this configuration, two ECSs in a subnet are bound to a single virtual IP address.
    -   Keepalived is then used to configure the two ECSs to work in the active/standby mode. Follow industry standards for configuring Keepalived. The details are not included here.

-   **Networking mode 2**: HA load balancing cluster

    If you want to build a high-availability load balancing cluster, use Keepalived and configure LVS nodes as direct routers.

    **Figure  2**  HA load balancing cluster<a name="en-us_topic_0206027322_fig10769151182615"></a>  
    ![](figures/ha-load-balancing-cluster.png "ha-load-balancing-cluster")

    -   Bind two ECSs to the same virtual IP address.
    -   Configure the two ECSs as LVS nodes working as direct routers and use Keepalived to configure the nodes in the active/standby mode. The two ECSs will evenly forward requests to different backend servers.
    -   Configure another two ECSs as backend servers.
    -   Disable the source/destination check for the two servers.

    Follow industry standards for configuring Keepalived. The details are not included here.


## Application Scenarios<a name="section43011914174217"></a>

-   Using an EIP to access a virtual IP address

    If your application has high availability requirements and needs to provide services through the Internet, it is recommended that you bind an EIP to a virtual IP address.

-   Using a VPN, Direct Connect, or peering connection to access a virtual IP address

    To ensure high availability and access to the Internet, use a VPN for security and Direct Connect for a stable connection. The VPC peering connection is needed so that the VPCs in the same region can communicate with each other.


