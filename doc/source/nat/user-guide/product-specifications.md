# Product Specifications<a name="en-us_topic_0086739763"></a>

The specification refers to the maximum number of SNAT connections supported by a NAT gateway.

An SNAT connection consists of the source IP address, source port, destination IP address, destination port, and transmission-layer protocol. The source IP address and source port are the EIP and port translated by SNAT to access the destination IP address and port of a public network. With these five elements, a connection can be distinguished as a unique session.

The data throughput of a NAT gateway is determined by the sum of EIP bandwidths of its DNAT rules. For example, a NAT gateway has two DNAT rules. If the bandwidth of the EIP bound to one rule is 10 Mbit/s and that bound to the other is 5 Mbit/s, the throughput of the NAT gateway is 15 Mbit/s.

When creating a NAT gateway, select the proper type based on your requirements.  [Table 1](#table39923257151849)  lists the NAT gateway specifications.

**Table  1**  NAT Gateway type

<a name="table39923257151849"></a>
<table><thead align="left"><tr id="row26507130151849"><th class="cellrowborder" valign="top" width="45%" id="mcps1.2.3.1.1"><p id="p10919583151849"><a name="p10919583151849"></a><a name="p10919583151849"></a><strong id="b49779767"><a name="b49779767"></a><a name="b49779767"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.3.1.2"><p id="p38230083151849"><a name="p38230083151849"></a><a name="p38230083151849"></a><strong id="b842352706135953"><a name="b842352706135953"></a><a name="b842352706135953"></a>Maximum Number of SNAT Connections</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row32100542151849"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="p66702817151849"><a name="p66702817151849"></a><a name="p66702817151849"></a>Small</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="p34219059151849"><a name="p34219059151849"></a><a name="p34219059151849"></a>10,000</p>
</td>
</tr>
<tr id="row12752392151849"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="p20469426151849"><a name="p20469426151849"></a><a name="p20469426151849"></a>Medium</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="p47410811151849"><a name="p47410811151849"></a><a name="p47410811151849"></a>50,000</p>
</td>
</tr>
<tr id="row56885558151849"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="p47662666151849"><a name="p47662666151849"></a><a name="p47662666151849"></a>Large</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="p35470708151849"><a name="p35470708151849"></a><a name="p35470708151849"></a>200,000</p>
</td>
</tr>
<tr id="row44794007151849"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="p42207974151849"><a name="p42207974151849"></a><a name="p42207974151849"></a>Extra-large</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="p63402763151849"><a name="p63402763151849"></a><a name="p63402763151849"></a>1,000,000</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   If the requests exceed the maximum allowed connections of your NAT gateway, your services will be adversely affected. To avoid this situation, you are advised to create alarm rules for the SNAT connection in Cloud Eye.  
>-   The DNAT rule has no relationship with the NAT gateway specifications. A maximum of 200 DNAT rules can be added to a NAT gateway. The number of SNAT rules is irrelevant to the NAT gateway specifications.  

