## SNAT

Some ECSs not only require services provided by the system but also need to access the Internet to obtain information or download software. The public cloud system allows users to bind EIPs to virtual NICs (ports) of ECSs to enable the ECSs to access the Internet. However, assigning a public IP address to each required ECS consumes scarce IPv4 addresses, incurs additional costs, and may increase the attack surface against a virtual environment. Therefore, enabling multiple ECSs to share one public IP address is a preferable and feasible method. This can be done by source network address translation (SNAT).

The public cloud system supports the SNAT function. A public IP address is assigned to an ECS that serves as the SNAT router or gateway for other ECSs from the same subnet or VPC.

For details about how to configure the SNAT function, see section <a href="Configuring the SNAT Server.md">Configuring the SNAT Server</a>.