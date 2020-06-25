# VPC Connections<a name="overview_0001"></a>

You can use EIPs, load balancers, NAT gateways, VPN connections, and Direct Connect connections to access the Internet if required.

-   Use EIPs to Enable a Small Number of ECSs to Access the Internet

    When only a few ECSs need to access the Internet, you can bind the EIPs to the ECSs. This will provide them with Internet access. You can also dynamically unbind the EIPs from the ECSs and bind them to NAT gateways and load balancers instead, which will also provide Internet access. The process is not complicated. 


-   Use NAT Gateways to Enable a Large Number of ECSs to Access the Internet

    When a large number of ECSs need to access the Internet, the public cloud system provides network address translation \(NAT\) gateways for the ECSs. With NAT gateways, you do not need to assign an EIP to each ECS, which reduces management costs incurred by an excessive number of EIPs. SNAT allows multiple ECSs in the same VPC to share one or more EIPs to access the Internet. SNAT saves money and prevents the EIPs of ECSs from being exposed to the Internet. SNAT supports up to 1 million concurrent connections and 30,000 new connections. 

-   Use ELB to Connect to the Internet If There Are a Large Number of Highly Concurrent Requests

    In high-concurrency scenarios, such as e-commerce, you can use load balancers provided by the ELB service to evenly distribute access traffic across multiple ECSs, allowing a large number of users to concurrently access your business system or application. ELB is deployed in cluster mode and provides fault tolerance for your applications by automatically balancing traffic across multiple availability zones \(AZs\). You can also take advantage of deep integration with Auto Scaling \(AS\), which enables automatic scaling based on service traffic and ensures service stability and reliability.

-   Use VPN or Direct Connect to Extend Your Self-Hosted IDC into the Cloud over the Internet

    For customers with self-hosted IDC equipment rooms, not all businesses of the customers will be migrated to the cloud because the customers want to reuse their legacy devices and require smooth business evolution. Then, you can use VPN or Direct Connect to interconnect your VPC and on-premises IDC. A VPN connection routes traffic through the Internet, which allows you to use a private network with the price of the public network. A Direct Connect connection is a dedicated, private network connection that provides you with more efficient data transmission and more consistent network experience than Internet-based connections.


