# Basic Concepts<a name="nat_pro_0004"></a>

## EIP<a name="section178511752716"></a>

An EIP is an IP address that can be directly accessed over the Internet. A private IP address is an IP address on a local area network \(LAN\) in the public cloud system and cannot be routed through the Internet.

An EIP is a static, public IP address. You can bind an EIP to an ECS in your subnet to enable the ECS in your VPC to communicate with the Internet through a fixed public IP address.

Each EIP can be used by only one ECS at a time.

## SNAT Connections<a name="section157601921152812"></a>

An SNAT connection consists of the source IP address, source port, destination IP address, destination port, and transmission-layer protocol. The source IP address and source port are the EIP and port translated by SNAT to access the destination IP address and port of a public network. With these five elements, a connection can be distinguished as a unique session.

## DNAT Connections<a name="section17561592911"></a>

A DNAT connection enables servers that share the same EIPs in a VPC to provide services accessible from the Internet through the IP address mapping or port mapping.

