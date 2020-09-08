# How Do I Select a Network Model When Creating a CCE Cluster? What Are the Differences Between These Models?<a name="cce_faq_00162"></a>

CCE uses high-performance container network add-ons, which support the tunnel network and the VPC network models.

>![](/images/icon-caution.gif) **CAUTION:** 
>After a cluster is created, the network model cannot be changed. Exercise caution when selecting a network model.

-   **Tunnel network**: The container network is an overlay tunnel network on top of a VPC network and uses the VXLAN technology. This network model is applicable when there is no high requirements on performance. VXLAN encapsulates Ethernet packets as UDP packets for tunnel transmission. Though at some cost of performance, the tunnel encapsulation enables higher interoperability and compatibility with advanced features \(such as network policy-based isolation\), meeting the requirements of most applications.

    **Figure  1**  Container tunnel network<a name="en-us_topic_0242566245_fig119421248102318"></a>  
    ![](figures/container-tunnel-network.png "container-tunnel-network")

-   **VPC network**: The container network uses VPC routing to integrate with the underlying network. This network model is applicable to performance-intensive scenarios. The maximum number of nodes allowed in a cluster depends on the route quota in a VPC network. Each node is assigned a CIDR block of a fixed size. VPC networks are free from tunnel encapsulation overhead and outperform container tunnel networks. In addition, as VPC routing includes routes to node IP addresses and container network segment, container pods in the cluster can be directly accessed from outside the cluster.

    **Figure  2**  VPC network<a name="en-us_topic_0242566245_fig105374614243"></a>  
    ![](figures/vpc-network.png "vpc-network")


The following table lists the differences between the network models.

**Table  1**  Network comparison

<a name="en-us_topic_0242566245_table715802210336"></a>
<table><thead align="left"><tr id="en-us_topic_0242566245_row015822213316"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="en-us_topic_0242566245_p1715813225335"><a name="en-us_topic_0242566245_p1715813225335"></a><a name="en-us_topic_0242566245_p1715813225335"></a><strong id="en-us_topic_0242566245_b7212104043613"><a name="en-us_topic_0242566245_b7212104043613"></a><a name="en-us_topic_0242566245_b7212104043613"></a>Dimension</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.69%" id="mcps1.2.4.1.2"><p id="en-us_topic_0242566245_p1015919220339"><a name="en-us_topic_0242566245_p1015919220339"></a><a name="en-us_topic_0242566245_p1015919220339"></a><strong id="en-us_topic_0242566245_b29012400369"><a name="en-us_topic_0242566245_b29012400369"></a><a name="en-us_topic_0242566245_b29012400369"></a>Tunnel Network</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.86%" id="mcps1.2.4.1.3"><p id="en-us_topic_0242566245_p5158192253312"><a name="en-us_topic_0242566245_p5158192253312"></a><a name="en-us_topic_0242566245_p5158192253312"></a><strong id="en-us_topic_0242566245_b15481184218360"><a name="en-us_topic_0242566245_b15481184218360"></a><a name="en-us_topic_0242566245_b15481184218360"></a>VPC Network</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0242566245_row3364165414382"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p7365105418387"><a name="en-us_topic_0242566245_p7365105418387"></a><a name="en-us_topic_0242566245_p7365105418387"></a>Core components</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p205912419393"><a name="en-us_topic_0242566245_p205912419393"></a><a name="en-us_topic_0242566245_p205912419393"></a>OVS</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p1759117483919"><a name="en-us_topic_0242566245_p1759117483919"></a><a name="en-us_topic_0242566245_p1759117483919"></a>IPVlan</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row9184022123919"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p939214336391"><a name="en-us_topic_0242566245_p939214336391"></a><a name="en-us_topic_0242566245_p939214336391"></a>Applicable clusters</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p183921533143919"><a name="en-us_topic_0242566245_p183921533143919"></a><a name="en-us_topic_0242566245_p183921533143919"></a>Hybrid cluster</p>
<p id="en-us_topic_0242566245_p7392123313914"><a name="en-us_topic_0242566245_p7392123313914"></a><a name="en-us_topic_0242566245_p7392123313914"></a>VM cluster</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p139214338397"><a name="en-us_topic_0242566245_p139214338397"></a><a name="en-us_topic_0242566245_p139214338397"></a>Hybrid cluster</p>
<p id="en-us_topic_0242566245_p53924334399"><a name="en-us_topic_0242566245_p53924334399"></a><a name="en-us_topic_0242566245_p53924334399"></a>VM cluster</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row18748936104718"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p104711451154714"><a name="en-us_topic_0242566245_p104711451154714"></a><a name="en-us_topic_0242566245_p104711451154714"></a>Support for network policies</p>
<p id="en-us_topic_0242566245_p6471751134717"><a name="en-us_topic_0242566245_p6471751134717"></a><a name="en-us_topic_0242566245_p6471751134717"></a>(networkpolicy)</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p20471351124715"><a name="en-us_topic_0242566245_p20471351124715"></a><a name="en-us_topic_0242566245_p20471351124715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p1047145111471"><a name="en-us_topic_0242566245_p1047145111471"></a><a name="en-us_topic_0242566245_p1047145111471"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row26521844204715"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p134711351184716"><a name="en-us_topic_0242566245_p134711351184716"></a><a name="en-us_topic_0242566245_p134711351184716"></a>Support for ENI</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p74715518471"><a name="en-us_topic_0242566245_p74715518471"></a><a name="en-us_topic_0242566245_p74715518471"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p20471115114714"><a name="en-us_topic_0242566245_p20471115114714"></a><a name="en-us_topic_0242566245_p20471115114714"></a>Yes. The container network is deeply integrated with the VPC network, and ENI is used for pods to communicate.</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row96181615010"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p1726882465017"><a name="en-us_topic_0242566245_p1726882465017"></a><a name="en-us_topic_0242566245_p1726882465017"></a>IP address management</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p82691024125018"><a name="en-us_topic_0242566245_p82691024125018"></a><a name="en-us_topic_0242566245_p82691024125018"></a>IP addresses can be migrated.</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0242566245_ul1259224495118"></a><a name="en-us_topic_0242566245_ul1259224495118"></a><ul id="en-us_topic_0242566245_ul1259224495118"><li>Each node is allocated with a small subnet.</li><li>A static route is added on the VPC router with the next hop set to the node IP address.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0242566245_row1661816105018"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p10269102415509"><a name="en-us_topic_0242566245_p10269102415509"></a><a name="en-us_topic_0242566245_p10269102415509"></a>Network performance</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p526982419507"><a name="en-us_topic_0242566245_p526982419507"></a><a name="en-us_topic_0242566245_p526982419507"></a>Performance loss due to VXLAN tunnel encapsulation</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0242566245_ul4143192791019"></a><a name="en-us_topic_0242566245_ul4143192791019"></a><ul id="en-us_topic_0242566245_ul4143192791019"><li>No performance loss as no tunnel encapsulation is required; performance comparable to bare metal networks</li><li>Data forwarded across nodes through the VPC router</li></ul>
</td>
</tr>
<tr id="en-us_topic_0242566245_row262191685013"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p142691524115014"><a name="en-us_topic_0242566245_p142691524115014"></a><a name="en-us_topic_0242566245_p142691524115014"></a>Network scale</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p72692024105016"><a name="en-us_topic_0242566245_p72692024105016"></a><a name="en-us_topic_0242566245_p72692024105016"></a>1,000 nodes</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p184026307513"><a name="en-us_topic_0242566245_p184026307513"></a><a name="en-us_topic_0242566245_p184026307513"></a>Limited by the VPC route table.</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row265119104479"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p1826920247509"><a name="en-us_topic_0242566245_p1826920247509"></a><a name="en-us_topic_0242566245_p1826920247509"></a>External dependency</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566245_p32691424195014"><a name="en-us_topic_0242566245_p32691424195014"></a><a name="en-us_topic_0242566245_p32691424195014"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566245_p204029302517"><a name="en-us_topic_0242566245_p204029302517"></a><a name="en-us_topic_0242566245_p204029302517"></a>Static route table of the VPC router</p>
</td>
</tr>
<tr id="en-us_topic_0242566245_row14400144693816"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566245_p1926972465013"><a name="en-us_topic_0242566245_p1926972465013"></a><a name="en-us_topic_0242566245_p1926972465013"></a>Application scenarios</p>
</td>
<td class="cellrowborder" valign="top" width="36.69%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0242566245_ul619513457509"></a><a name="en-us_topic_0242566245_ul619513457509"></a><ul id="en-us_topic_0242566245_ul619513457509"><li>Common container service scenarios</li><li>Scenarios that do not have high requirements on network latency and bandwidth</li></ul>
</td>
<td class="cellrowborder" valign="top" width="40.86%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0242566245_ul1659212532511"></a><a name="en-us_topic_0242566245_ul1659212532511"></a><ul id="en-us_topic_0242566245_ul1659212532511"><li>Scenarios that have high requirements on network latency and bandwidth</li><li>Containers can communicate with VMs using a microservice registration framework, such as Dubbo and CSE.</li></ul>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-notice.gif) **NOTICE:** 
>1.  The actual cluster scale is limited by the quota of custom routes of the VPC. Therefore, estimate the number of required nodes before creating a VPC.
>2.  By default, the VPC network model supports direct communication between containers and hosts in the same VPC. If a peering connection policy is configured between the VPC and another VPC, the containers can directly communicate with hosts on the peer VPC. In addition, in hybrid networking scenarios such as cloud private line and VPN, communication between containers and hosts on the peer end can also be achieved with proper planning.

