# IPsec VPN<a name="en-us_topic_0160974607"></a>

The Internet Protocol Security \(IPsec\) VPN is an encrypted tunneling technology that uses encrypted security services to establish confidential and secure communication tunnels between different networks.

In  [Figure 1](#fig489417475262), a VPC has two subnets: 192.168.1.0/24 and 192.168.2.0/24. On your router deployed in your physical data center, you also have two subnets: 192.168.3.0/24 and 192.168.4.0/24. You can use VPN to enable subnets in your VPC to communicate with those in your data center.

**Figure  1**  IPsec VPN<a name="fig489417475262"></a>  
![](figures/ipsec-vpn.png "ipsec-vpn")

Currently, the site-to-site VPN and hub-spoke VPN are supported. You need to set up VPNs in both your data center and the VPC to establish the VPN connection.

Ensure that the VPN in your VPC and that in your data center use the same Internet Key Exchange \(IKE\) and IPsec policy configurations. Before creating a VPN, familiarize yourself with the protocols described in  [Table 1](#en-us_topic_0030969429_en-us_topic_0030119097_table19214078112957)  and ensure that your device meets the requirements and configuration constraints of the involved protocols.

**Table  1**  Involved protocols

<a name="en-us_topic_0030969429_en-us_topic_0030119097_table19214078112957"></a>
<table><thead align="left"><tr id="en-us_topic_0030969429_en-us_topic_0030119097_row55236938112957"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0030969429_en-us_topic_0030119097_p45007011112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p45007011112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p45007011112957"></a><strong id="b842352706184931"><a name="b842352706184931"></a><a name="b842352706184931"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.980000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0030969429_en-us_topic_0030119097_p21689244112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p21689244112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p21689244112957"></a><strong>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.86%" id="mcps1.2.4.1.3"><p id="en-us_topic_0030969429_en-us_topic_0030119097_p11998301112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p11998301112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p11998301112957"></a><strong id="b84235270617755"><a name="b84235270617755"></a><a name="b84235270617755"></a>Constraint</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0030969429_en-us_topic_0030119097_row32338319112957"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969429_en-us_topic_0030119097_p2158169112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p2158169112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p2158169112957"></a>RFC 2409</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969429_en-us_topic_0030119097_p40594020112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p40594020112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p40594020112957"></a>Defines the IKE protocol, which negotiates and verifies key information to safeguard VPNs.</p>
</td>
<td class="cellrowborder" valign="top" width="34.86%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0030969429_en-us_topic_0030119097_ul66890200112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_ul66890200112957"></a><ul id="en-us_topic_0030969429_en-us_topic_0030119097_ul66890200112957"><li>Use the pre-shared key (PSK) to reach an IKE peer agreement.</li><li>Use the main mode for negotiation.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0030969429_en-us_topic_0030119097_row41920571112957"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969429_en-us_topic_0030119097_p40123099112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p40123099112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p40123099112957"></a>RFC 4301</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969429_en-us_topic_0030119097_p28745567112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p28745567112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p28745567112957"></a>Defines the IPsec architecture, the security services that IPsec offers, and the collaboration between components.</p>
</td>
<td class="cellrowborder" valign="top" width="34.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969429_en-us_topic_0030119097_p46689584112957"><a name="en-us_topic_0030969429_en-us_topic_0030119097_p46689584112957"></a><a name="en-us_topic_0030969429_en-us_topic_0030119097_p46689584112957"></a>Use the IPsec tunnel to set up a VPN connection.</p>
</td>
</tr>
</tbody>
</table>

