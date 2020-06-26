# Differences Between Security Groups and Firewalls<a name="en-us_topic_0052003963"></a>

You can configure security groups and firewalls to increase the security of ECSs in your VPC.

-   Security groups protect ECSs.
-   Firewalls protect subnets.

For details, see  [Figure 1](#fig9582182315479).

**Figure  1**  Security groups and firewalls<a name="fig9582182315479"></a>  
![](figures/security-groups-and-firewalls.png "security-groups-and-firewalls")

[Table 1](#table53053071174845)  describes the differences between security groups and firewalls.

**Table  1**  Differences between security groups and firewalls

<a name="table53053071174845"></a>
<table><thead align="left"><tr id="row63488302174845"><th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.2.4.1.1"><p id="p16252192132814"><a name="p16252192132814"></a><a name="p16252192132814"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="39.77%" id="mcps1.2.4.1.2"><p id="p44965011174845"><a name="p44965011174845"></a><a name="p44965011174845"></a>Security Group</p>
</th>
<th class="cellrowborder" valign="top" width="45.76%" id="mcps1.2.4.1.3"><p id="p18287275174845"><a name="p18287275174845"></a><a name="p18287275174845"></a>Firewall</p>
</th>
</tr>
</thead>
<tbody><tr id="row30367752174845"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.4.1.1 "><p id="p425252102818"><a name="p425252102818"></a><a name="p425252102818"></a>Targets</p>
</td>
<td class="cellrowborder" valign="top" width="39.77%" headers="mcps1.2.4.1.2 "><p id="p43868882174845"><a name="p43868882174845"></a><a name="p43868882174845"></a>Operates at the ECS level.</p>
</td>
<td class="cellrowborder" valign="top" width="45.76%" headers="mcps1.2.4.1.3 "><p id="p63718581174845"><a name="p63718581174845"></a><a name="p63718581174845"></a>Operates at the subnet level.</p>
</td>
</tr>
<tr id="row36596319174845"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.4.1.1 "><p id="p9252182132813"><a name="p9252182132813"></a><a name="p9252182132813"></a>Rules</p>
</td>
<td class="cellrowborder" valign="top" width="39.77%" headers="mcps1.2.4.1.2 "><p id="p11511833174845"><a name="p11511833174845"></a><a name="p11511833174845"></a>Only supports <strong id="b84235270616192"><a name="b84235270616192"></a><a name="b84235270616192"></a>Allow</strong> rules.</p>
</td>
<td class="cellrowborder" valign="top" width="45.76%" headers="mcps1.2.4.1.3 "><p id="p60043263174845"><a name="p60043263174845"></a><a name="p60043263174845"></a>Supports <strong id="b661010993"><a name="b661010993"></a><a name="b661010993"></a>Allow</strong> and <strong id="b842352706141521"><a name="b842352706141521"></a><a name="b842352706141521"></a>Deny</strong> rules.</p>
</td>
</tr>
<tr id="row3518463174845"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.4.1.1 "><p id="p3252321102813"><a name="p3252321102813"></a><a name="p3252321102813"></a>Priority</p>
</td>
<td class="cellrowborder" valign="top" width="39.77%" headers="mcps1.2.4.1.2 "><p id="p16560083174845"><a name="p16560083174845"></a><a name="p16560083174845"></a>If security group rules conflict, the overlapping elements of these rules take effect.</p>
</td>
<td class="cellrowborder" valign="top" width="45.76%" headers="mcps1.2.4.1.3 "><p id="p66298376174845"><a name="p66298376174845"></a><a name="p66298376174845"></a>If firewall rules conflict, the rule with the highest priority takes effect.</p>
</td>
</tr>
<tr id="row59814478174845"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.4.1.1 "><p id="p14252172117284"><a name="p14252172117284"></a><a name="p14252172117284"></a>Usage</p>
</td>
<td class="cellrowborder" valign="top" width="39.77%" headers="mcps1.2.4.1.2 "><p id="p13134583174845"><a name="p13134583174845"></a><a name="p13134583174845"></a>Automatically applies to ECSs in the security group that is selected during ECS creation. You must select a security group when creating ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="45.76%" headers="mcps1.2.4.1.3 "><p id="p57268308174845"><a name="p57268308174845"></a><a name="p57268308174845"></a>Applies to all ECSs in the subnets associated with the firewall. Selecting a firewall is not allowed during subnet creation. You must create a firewall, associate subnets with it, add inbound and outbound network rules, and enable firewall. The firewall then takes effect for the associated subnets and ECSs in the subnets.</p>
</td>
</tr>
<tr id="row3289418310534"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.4.1.1 "><p id="p82520212284"><a name="p82520212284"></a><a name="p82520212284"></a>Packets</p>
</td>
<td class="cellrowborder" valign="top" width="39.77%" headers="mcps1.2.4.1.2 "><p id="p4718316010534"><a name="p4718316010534"></a><a name="p4718316010534"></a>Only packet filtering based on the 3-tuple (protocol, port, and peer IP address) is supported.</p>
</td>
<td class="cellrowborder" valign="top" width="45.76%" headers="mcps1.2.4.1.3 "><p id="p6373958110534"><a name="p6373958110534"></a><a name="p6373958110534"></a>Only packet filtering based on the 5-tuple (protocol, source port, destination port, source IP address, and destination IP address) is supported.</p>
</td>
</tr>
</tbody>
</table>

