# Overview<a name="EN-US_TOPIC_0127311704"></a>

## User-defined Network<a name="section1231717227563"></a>

BMSs support secondary virtualization. The user-defined network enables communication between the VM network and the VPC, and provides functions similar to the VPC network for VMs. Application scenarios and benefits include:

-   Private clouds such as XenServer, VMware, and Hyper-V can be provisioned using BMSs.
-   VMs or containers provisioned in the private cloud on BMSs can communicate with the Internet.
-   VMs or containers provisioned in the private cloud on BMSs can communicate with each other.
-   Network ACLs can be configured for the subnets of the VMs or containers provisioned in the private cloud on BMSs.
-   VMs or containers provisioned in the private cloud on BMSs can communicate with ECSs in VPCs.
-   The private cloud system based on BMSs and Direct Connect can communicate with the private cloud in the on-premise data center.

## Notes<a name="section973732622210"></a>

-   If you have multiple VPCs, you can only create user-defined networks in one VPC.
-   If each of your BMSs has only one NIC, you cannot create user-defined networks.
-   You must create a BMS with a user-defined VLAN before creating a user-defined network.
-   Security groups cannot be configured for user-defined subnets.

