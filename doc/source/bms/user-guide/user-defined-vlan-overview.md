# Overview<a name="EN-US_TOPIC_0085714156"></a>

## User-defined VLAN<a name="section5963929102410"></a>

You can use the Ethernet NICs \(10GE defined in BMS specifications\) not used by the system to configure a user-defined VLAN. The QinQ technology is used to isolate networks and provide additional physical planes and bandwidths. You can allocate VLAN subnets to isolate traffic in various scenarios including SAP HANA and VMware. User-defined VLAN NICs are in pairs. You can configure NIC bonding to achieve high availability. User-defined VLANs in different AZs cannot communicate.

Ethernet NICs not used by the system by default do not have configuration files and are in  **down**  state during the system startup. You can run  **ifconfig** **-a**  to view the NIC name and run  **ifconfig** _eth2_ **up**  to configure the NIC. The configuration method varies depending on the OS.

For example, on a Linux BMS, eth0 and eth1 are automatically bonded in a VPC network, and eth2 and eth3 are used in a user-defined VLAN. You can send packets with any VLAN tags through the two network interfaces. If you want to allocate a VLAN, configure eth2 and eth3 bonding and create the target VLAN network interface on the bond device. The method is similar to that of creating a bond device and a VLAN sub-interface in a VPC.

>![](/images/icon-note.gif) **NOTE:**   
>In a user-defined VLAN, ports can be bonded or not, and they can only be bonded in active/standby mode.  
>For more information about NIC bond, visit  [https://www.kernel.org/doc/Documentation/networking/bonding.txt](https://www.kernel.org/doc/Documentation/networking/bonding.txt).  

For details about how to configure a user-defined VLAN for BMSs running different OSs, see sections  [Configuring a User-defined VLAN \(SUSE Linux Enterprise Server 12\)](configuring-a-user-defined-vlan-(suse-linux-enterprise-server-12).md)  to  [Configuring a User-defined VLAN \(Windows Server\)](configuring-a-user-defined-vlan-(windows-server).md).

## View User-defined VLANs<a name="section125275095016"></a>

User-defined VLANs are presented to you through the BMS specifications shown in  [Figure 1](#fig465385574917).

**Figure  1**  BMS specifications<a name="fig465385574917"></a>  
![](figures/bms-specifications.png "bms-specifications")

A BMS created using this flavor provides one two-port 10GE NIC for connecting to the VPC as well as one two-port 10GE extension NIC for a high-speed interconnection between BMSs. You can configure VLANs on the extension NIC as needed.

