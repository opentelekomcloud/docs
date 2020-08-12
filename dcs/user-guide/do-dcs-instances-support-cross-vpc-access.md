# Do DCS Instances Support Cross-VPC Access?<a name="en-us_topic_0100698850"></a>

Generally, VPCs are isolated from each other and ECSs cannot access DCS instances that belong to a different VPC from these ECSs.

However, by establishing VPC peering connections between VPCs, ECSs can access DCS instances across VPCs.

When using VPC peering connections to access DCS instances across VPCs, adhere to the following rules:

**Table  1**  Client CIDR block constraints

<a name="table16102153132716"></a>
<table><thead align="left"><tr id="row81023536275"><th class="cellrowborder" valign="top" width="43%" id="mcps1.2.3.1.1"><p id="p16376715152816"><a name="p16376715152816"></a><a name="p16376715152816"></a><strong id="b51151340163113"><a name="b51151340163113"></a><a name="b51151340163113"></a>CIDR Blocks of DCS Instances</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.3.1.2"><p id="p1737681517287"><a name="p1737681517287"></a><a name="p1737681517287"></a><strong id="b212513403317"><a name="b212513403317"></a><a name="b212513403317"></a>CIDR Blocks Not Allowed for Clients</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row710318536271"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.3.1.1 "><p id="p0208172311289"><a name="p0208172311289"></a><a name="p0208172311289"></a>172.16.0.0/12 to 172.16.0.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.3.1.2 "><p id="p11208623132810"><a name="p11208623132810"></a><a name="p11208623132810"></a>192.168.1.0/24</p>
<p id="p3208623142816"><a name="p3208623142816"></a><a name="p3208623142816"></a>192.168.2.0/24</p>
<p id="p1120832362817"><a name="p1120832362817"></a><a name="p1120832362817"></a>192.168.3.0/24</p>
</td>
</tr>
<tr id="row11103155311272"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.3.1.1 "><p id="p14209162322815"><a name="p14209162322815"></a><a name="p14209162322815"></a>192.168.0.0/16 to 192.168.0.0/24</p>
<p id="p020915233281"><a name="p020915233281"></a><a name="p020915233281"></a>10.0.0.0/8 to 10.0.0.0/24</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.3.1.2 "><p id="p1220913236284"><a name="p1220913236284"></a><a name="p1220913236284"></a>172.31.1.0/24</p>
<p id="p420902302811"><a name="p420902302811"></a><a name="p420902302811"></a>172.31.2.0/24</p>
<p id="p3209122314280"><a name="p3209122314280"></a><a name="p3209122314280"></a>172.31.3.0/24</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>-   The right column lists the CIDR blocks used by the subnets of the resource tenant. The clients cannot use these subnets.
>-   For more information about creating and using VPC peering connections, see the  _Virtual Private Cloud User Guide_.

