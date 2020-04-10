# Virtual Private Network<a name="en-us_topic_0035391393"></a>

A Virtual Private Network \(VPN\) establishes an encrypted, Internet-based communications tunnel between a user and a Virtual Private Cloud \(VPC\). With VPN, you can connect to a VPC and access service resources in it.

By default, ECSs in a VPC cannot communicate with your data center or private network. To enable communication between them, use a VPN.

A VPN consists of a VPN gateway and one or more VPN connections. A VPN gateway provides an Internet egress for a VPC and works together with the remote gateway in the local data center. A VPN connection uses the Internet-based encryption technology to connect the VPN gateway and the remote gateway to enable communication between the local data center and VPC. The VPN connection allows you to quickly build secure hybrid cloud environment.  [Figure 1](#fig681916843511)  shows the VPN networking.

**Figure  1**  VPN networking<a name="fig681916843511"></a>  
![](figures/vpn-networking.png "vpn-networking")

