# SNAT<a name="en-us_topic_0051191229"></a>

Besides requiring services provided by the system, some ECSs also need to access the Internet to obtain information or download software. The public cloud system allows users to bind EIPs \(public IP addresses\) to virtual NICs \(ports\) of ECSs to enable the ECSs to access the Internet. However, assigning a public IP address to each ECS consumes already-limited IPv4 addresses, incurs additional costs, and may increase the attack surface for a virtual environment. Therefore, enabling multiple ECSs to share one public IP address is a preferable and feasible method. This can be done using SNAT.

The public cloud system supports SNAT. A public IP address is assigned to an ECS that serves as the SNAT router or gateway for other ECSs from the same subnet or VPC.

For details about how to configure SNAT, see section  [Configuring an SNAT Server](configuring-an-snat-server.md).

