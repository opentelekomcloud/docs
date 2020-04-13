# SNAT<a name="vpc_Concepts_0004"></a>

In addition to services provided by the system, some ECSs need to access the Internet to obtain information or download software. You can bind EIPs to virtual NICs \(ports\) of ECSs to enable the ECSs to access the Internet. However, assigning a public IP address to each ECS consumes already-limited IPv4 addresses, incurs additional costs, and may increase the attack surface for a virtual environment. Therefore, SNAT is introduced to enable multiple ECSs to share one public IP address.

On a public cloud, a public IP address can be assigned to an ECS that serves as the SNAT router or gateway for other ECSs from the same subnet or VPC.

For details about how to configure SNAT, see  [Configuring an SNAT Server](configuring-an-snat-server.md).

