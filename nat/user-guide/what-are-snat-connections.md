# What Are SNAT Connections?<a name="nat_faq_0002"></a>

An SNAT connection consists of the source IP address, source port, destination IP address, destination port, and transmission-layer protocol. With these five elements, a connection can be distinguished as a unique session. The source IP address and source port are the EIP and port translated by SNAT to access the destination IP address and port of a public network.

SNAT supports three protocols: TCP, UDP, and ICMP. NAT Gateway supports a maximum of 55000 concurrent connections for each destination IP address and port. If any of the destination IP address, port number, and protocol \(TCP/UDP/ICMP\) changes, you can create another 55000 connections. The number of connections you query on an ECS may be different from the actual number of SNAT connections. \(You can run the  **netstat**  command to query the number of connections.\) Assume that an ECS creates 100 connections to a fixed destination every second. 55000 connections will be used up in about 10 minutes without considering the dropped idle connections. As a result, connections cannot be created.

If there is no data packet passing through the SNAT connection for a long time, the connection will be timed out. 

