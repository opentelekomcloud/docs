# Accessing the Internet<a name="overview_0002"></a>

To meet your Internet connectivity requirements in different scenarios, the public cloud system provides EIPs, load balancers, NAT gateways, VPN connections, and Direct Connect connections based on the VPC service to help you quickly move your business to the cloud without requiring complex deployment.

## Use EIPs to Enable a Small Number of ECSs to Access the Internet<a name="section1694823517436"></a>

When only a few ECSs need to access the Internet, you can bind the EIPs to the ECSs. Then, the ECSs can connect to the Internet. You can dynamically unbind the EIPs from the ECSs and bind the EIPs to NAT gateways and load balancers to enable them to access the Internet. EIP management is easy. 

## Use NAT Gateways to Enable a Large Number of ECSs to Access the Internet<a name="section14919133775117"></a>

When a large number of ECSs need to access the Internet, the public cloud system provides Network Address Translation \(NAT\) gateways for the ECSs. With NAT gateways, you do not need to assign an EIP to each ECS, which reduces management costs incurred by an excessive number of EIPs. SNAT allows multiple ECSs in the same VPC to share one or more EIPs to access the Internet. The SNAT function reduces management costs and prevents the EIPs of ECSs from being exposed to the Internet. SNAT supports a maximum of 1 million concurrent connections and 30,000 new connections. 

## Use ELB to Connect to the Internet If There Are a Large Number of Highly Concurrent Requests<a name="section14708135910558"></a>

In high-concurrency scenarios, such as e-commerce, you can use load balancers provided by the ELB service to evenly distribute access traffic across multiple ECSs, allowing a large number of users to concurrently access your business system or application. ELB is deployed in cluster mode and provides fault tolerance for your applications by automatically balancing traffic across multiple availability zones \(AZs\). You can also take advantage of deep integration with the Auto Scaling \(AS\) service, which enables automatic scaling based on service traffic and ensures service stability and reliability.

## Use VPN or Direct Connect to Extend Your Self-Hosted IDC into the Cloud over the Internet<a name="section181714415570"></a>

For customers with self-hosted IDC equipment rooms, not all businesses of the customers will be migrated to the cloud because the customers want to reuse their legacy devices and require smooth business evolution. Then, you can use VPN or Direct Connect to interconnect your VPC and on-premises IDC. A VPN connection routes traffic through the Internet, which allows you to use a private network with the price of the public network. A Direct Connect connection is a dedicated, private network connection that provides you with more efficient data transmission and more consistent network experience than Internet-based connections.

