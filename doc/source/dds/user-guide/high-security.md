# High Security<a name="dds_01_0008"></a>

## Network Isolation<a name="section157471650114110"></a>

DDS uses Virtual Private Clouds \(VPCs\) and network security groups to isolate your DB instances. VPCs allow you to configure IP address ranges that are allowed  access to DDS. You can run your DB instances in a VPC to improve security. To further enhance database security, you can configure subnets and security groups to control access to DB instances.

## Access Control<a name="section36087416422"></a>

VPC security groups can have rules that govern both inbound and outbound traffic of DB instances.

## Transmission Encryption<a name="section05340203433"></a>

DDS uses Secure Sockets Layer \(SSL\) to encrypt transmitted data. You can download a certificate authority \(CA\) from the DDS console and upload it for authentication when connecting to a database.

## Security Protection<a name="section13931102311470"></a>

DDS provides a multi-layer network protection against various malicious attacks. The protection system consists of VPCs, subnets, security groups, DDoS protection, and SSL.

-   VPC is used to isolate tenants and control access to databases.
-   The SSL connection ensures data security and integrity.
-   Security group rules restrict traffic to specific IP addresses and ports, securing connections between DDS and other services.

## Performance Monitoring<a name="section1305495014142"></a>

DDS monitors instance performance, reducing O&M activities by as much as 60%. It provides real-time monitoring information about CPU utilization, disk usage, IOPS, and number of active connections, allowing you to check instance status at any time.

In asynchronous disk scenarios, DDS provides excellent plugin performance and process memory databases. It also provides the secondary index function to meet dynamic query requirements.

