# Do DCS Instances Support Cross-VPC Access?<a name="EN-US_TOPIC_0237964754"></a>

Generally, VPCs are isolated from each other and ECSs cannot access DCS instances that belong to a different VPC from these ECSs.

However, by establishing VPC peering connections between VPCs, ECSs can access single-node and master/standby DCS instances across VPCs.

When using VPC peering connections to access DCS instances across VPCs, adhere to the following rules:

<a name="table36808710"></a>
<table><thead align="left"><tr id="row54090270"><th class="cellrowborder" valign="top" width="43.43434343434344%" id="mcps1.1.3.1.1"><p id="p19235715"><a name="p19235715"></a><a name="p19235715"></a>Network Segments of DCS Instances</p>
</th>
<th class="cellrowborder" valign="top" width="56.56565656565656%" id="mcps1.1.3.1.2"><p id="p14589060"><a name="p14589060"></a><a name="p14589060"></a>Network Segments Not Allowed for Clients</p>
</th>
</tr>
</thead>
<tbody><tr id="row40863243"><td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.1.3.1.1 "><p id="p21588349"><a name="p21588349"></a><a name="p21588349"></a>172.16.0.0/12 to 172.16.0.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="56.56565656565656%" headers="mcps1.1.3.1.2 "><p id="p3825860"><a name="p3825860"></a><a name="p3825860"></a>192.168.1.0/24</p>
<p id="p34432747"><a name="p34432747"></a><a name="p34432747"></a>192.168.2.0/24</p>
<p id="p41459272"><a name="p41459272"></a><a name="p41459272"></a>192.168.3.0/24</p>
</td>
</tr>
<tr id="row37589132"><td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.1.3.1.1 "><p id="p24820853"><a name="p24820853"></a><a name="p24820853"></a>192.168.0.0/16 to 192.168.0.0/24</p>
<p id="p22061093"><a name="p22061093"></a><a name="p22061093"></a>10.0.0.0/8 to 10.0.0.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="56.56565656565656%" headers="mcps1.1.3.1.2 "><p id="p42118094"><a name="p42118094"></a><a name="p42118094"></a>172.31.1.0/24</p>
<p id="p43518530"><a name="p43518530"></a><a name="p43518530"></a>172.31.2.0/24</p>
<p id="p56122452"><a name="p56122452"></a><a name="p56122452"></a>172.31.3.0/24</p>
</td>
</tr>
</tbody>
</table>

