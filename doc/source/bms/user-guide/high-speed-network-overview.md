# Overview<a name="EN-US_TOPIC_0085714155"></a>

## High-Speed Network<a name="section26319596486"></a>

A high-speed network is an internal network among BMSs and shares the same physical plane with VPC. After you create a high-speed network on the management console, the system will create a dedicated VLAN sub-interface in the BMS OS for network data communication. It uses the 10 Gbit/s port. A high-speed network has only east-west traffic and supports only communication at layer 2 because it does not support layer 3 routing.

## View High-Speed NICs<a name="section18304624184110"></a>

You can view the network interfaces of the high-speed network on the  **NICs**  tab page of the BMS details page. For Linux images, you can also locate the VLAN sub-interface or bond interface in the OS based on the allocated IP address.

Take CentOS 7.4 64-bit as an example. Log in to the OS and view the NIC configuration files  **ifcfg-eth0**,  **ifcfg-eth1**,  **ifcfg-bond0**,  **ifcfg-bond0.3441**,  **ifcfg-bond0.2617**, and  **ifcfg-bond0.2618**  in the  **/etc/sysconfig/network-scripts**  directory. You need to use IP mapping to match the network.

Run the  **ifconfig**  command. The private IP addresses of the two high-speed NICs on the console are 192.168.5.58 and 10.34.247.26. It can be determined that  **ifcfg-bond0.2617**  and  **ifcfg-bond0.2618**  are configuration files of the high-speed NICs.

![](figures/10-6-1-2.png)

The following figures show the NIC and bond configuration information.

![](figures/10-6-1-3.png)

