# Restrictions<a name="EN-US_TOPIC_0159392335"></a>

-   The MAC address of the primary ESX NIC cannot be changed. If you change it, network connection of the primary ESX NIC will be interrupted.
-   To enable the VMware VM to communicate with other VMs or BMSs in the VPC, ensure that the VMware VM IP address is different from the IP CIDR of the VPC.
-   The host for provisioning ESXi images cannot have EVS disks.
-   When forming a NIC group of the QinQ high-speed network, you cannot use ToR for configuration, such as etherchannel and LACP.

