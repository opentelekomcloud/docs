# High Security<a name="rds_01_0004"></a>

## Network Isolation<a name="section157471650114110"></a>

RDS uses the Virtual Private Cloud \(VPC\) service and network security groups to isolate your DB instances. VPCs allow you to define IP addresses that are allowed to access RDS. You can run your DB instances in a VPC to improve security. You can configure subnets and security groups to control access to DB instances.

## Access Control<a name="section36087416422"></a>

RDS controls access through the domain/IAM user and security groups. When you create an RDS DB instance, RDS will automatically create an account. You can create an IAM user as required and authorize database objects for the database IAM user for separation of permissions. VPC security groups can have rules that govern both inbound and outbound traffic of DB instances.

## Transmission Encryption<a name="section05340203433"></a>

RDS uses Transport Layer Security \(TLS\) and Secure Sockets Layer \(SSL\) to offer encryption during transmission. You can download the Certificate Authority \(CA\) certificate from the RDS console and upload it when connecting to a database for authentication.

## Storage Encryption<a name="section16846333434"></a>

RDS uses static encryption, tablespace encryption, and homomorphic encryption to encrypt the data to be stored. Encryption keys are managed by Key Management Service \(KMS\).

## Data Deletion<a name="section16781145274310"></a>

When you delete an RDS DB instance, the disks it attaches, object storage space its backups occupy, and all data it stores will be deleted. The deleted data cannot be viewed or restored.

## Anti-DDoS<a name="section861224713"></a>

When you connect to an RDS DB instance through a public network, your DB instance may be in a distributed denial-of-service attack. If the RDS security system detects a DDoS attack, it will enable the anti-DDoS function. If the function cannot defend against the attack or the attack reaches the black hole threshold, black hole processing is triggered to ensure availability of the RDS service.

## Security Protection<a name="section13931102311470"></a>

RDS is protected by multiple layers of firewalls that can ensure data security by defending against various malicious attacks, such as DDoS attacks and SQL injections. You are advised to access RDS through a private network to protect RDS DB instances from DDoS attacks.

