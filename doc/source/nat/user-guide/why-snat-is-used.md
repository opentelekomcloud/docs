# Why SNAT Is Used?<a name="nat_faq_001"></a>

Besides requiring services provided by the system, some ECSs also need to access the Internet to obtain information or download software. However, assigning a public IP address to each ECS consumes already-limited IPv4 addresses, incurs additional costs, and may increase the attack surface for a virtual environment. Therefore, enabling multiple ECSs to share one public IP address is a preferable and more feasible method. This can be done using SNAT.

