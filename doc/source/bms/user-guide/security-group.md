# Security Group<a name="EN-US_TOPIC_0083745264"></a>

## What Is a Security Group?<a name="section5671748165410"></a>

A security group is a virtual firewall that detects status and filters data packets. It is an important network isolation method used to set access control for ECSs, BMSs, load balancers, and database instances.

You can configure security group rules to allow instances in a security group to access the public or private network.

-   A security group is a logical group. You can add BMSs with the same security protection requirements in a region to the same security group.
-   By default, BMSs in a security group can communicate with each other through an internal network, and BMSs in different security groups cannot.
-   You can modify a security group rule at any time, and the modification takes effect immediately.

## Default Security Group<a name="section7270549185510"></a>

When you create a BMS in a region, the system will create a default security group if no security group has been created in the region.

The default security group rule allows all outgoing data packets and controls incoming data packets. BMSs in a security group can access each other without requiring any access rule.

**Figure  1**  Default security group<a name="fig9128164855315"></a>  
![](figures/default-security-group.png "default-security-group")

[Table 1](#table57441530644)  lists the rules for a default security group.

**Table  1**  Default security group rules

<a name="table57441530644"></a>
<table><thead align="left"><tr id="row87461030648"><th class="cellrowborder" valign="top" width="13.639999999999999%" id="mcps1.2.6.1.1"><p id="p974620306420"><a name="p974620306420"></a><a name="p974620306420"></a>Direction</p>
</th>
<th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.6.1.2"><p id="p1474683019414"><a name="p1474683019414"></a><a name="p1474683019414"></a>Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="14.360000000000001%" id="mcps1.2.6.1.3"><p id="p1674620305413"><a name="p1674620305413"></a><a name="p1674620305413"></a>Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.4"><p id="p17461130343"><a name="p17461130343"></a><a name="p17461130343"></a>Source/Destination</p>
</th>
<th class="cellrowborder" valign="top" width="35.47%" id="mcps1.2.6.1.5"><p id="p1474683010413"><a name="p1474683010413"></a><a name="p1474683010413"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row674616301415"><td class="cellrowborder" valign="top" width="13.639999999999999%" headers="mcps1.2.6.1.1 "><p id="p774610301047"><a name="p774610301047"></a><a name="p774610301047"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.6.1.2 "><p id="p674613011415"><a name="p674613011415"></a><a name="p674613011415"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="14.360000000000001%" headers="mcps1.2.6.1.3 "><p id="p0746113016418"><a name="p0746113016418"></a><a name="p0746113016418"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.4 "><p id="p1774612307416"><a name="p1774612307416"></a><a name="p1774612307416"></a>Destination: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.47%" headers="mcps1.2.6.1.5 "><p id="p1074673014417"><a name="p1074673014417"></a><a name="p1074673014417"></a>Allow all outbound traffic.</p>
</td>
</tr>
<tr id="row147461630449"><td class="cellrowborder" valign="top" width="13.639999999999999%" headers="mcps1.2.6.1.1 "><p id="p157464301342"><a name="p157464301342"></a><a name="p157464301342"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.6.1.2 "><p id="p107460302413"><a name="p107460302413"></a><a name="p107460302413"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="14.360000000000001%" headers="mcps1.2.6.1.3 "><p id="p1974610305413"><a name="p1974610305413"></a><a name="p1974610305413"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.4 "><p id="p57461430147"><a name="p57461430147"></a><a name="p57461430147"></a>Source: current security group ID (for example, sg-<em id="i19385142014618"><a name="i19385142014618"></a><a name="i19385142014618"></a>xxxxx</em>)</p>
</td>
<td class="cellrowborder" valign="top" width="35.47%" headers="mcps1.2.6.1.5 "><p id="p207462308411"><a name="p207462308411"></a><a name="p207462308411"></a>Allow inbound traffic from BMSs added to the same security group.</p>
</td>
</tr>
<tr id="row174653015415"><td class="cellrowborder" valign="top" width="13.639999999999999%" headers="mcps1.2.6.1.1 "><p id="p10747330547"><a name="p10747330547"></a><a name="p10747330547"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.6.1.2 "><p id="p87471130740"><a name="p87471130740"></a><a name="p87471130740"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="14.360000000000001%" headers="mcps1.2.6.1.3 "><p id="p1474783018411"><a name="p1474783018411"></a><a name="p1474783018411"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.4 "><p id="p27475302049"><a name="p27475302049"></a><a name="p27475302049"></a>Source: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.47%" headers="mcps1.2.6.1.5 "><p id="p7747103017410"><a name="p7747103017410"></a><a name="p7747103017410"></a>Allows all IP addresses to access Linux BMSs over SSH.</p>
</td>
</tr>
<tr id="row117470305417"><td class="cellrowborder" valign="top" width="13.639999999999999%" headers="mcps1.2.6.1.1 "><p id="p4747113011410"><a name="p4747113011410"></a><a name="p4747113011410"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.6.1.2 "><p id="p1774720308415"><a name="p1774720308415"></a><a name="p1774720308415"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="14.360000000000001%" headers="mcps1.2.6.1.3 "><p id="p107475301546"><a name="p107475301546"></a><a name="p107475301546"></a>3389</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.4 "><p id="p12747163013419"><a name="p12747163013419"></a><a name="p12747163013419"></a>Source: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="35.47%" headers="mcps1.2.6.1.5 "><p id="p1574714301943"><a name="p1574714301943"></a><a name="p1574714301943"></a>Allows all IP addresses to access Linux BMSs over RDP.</p>
</td>
</tr>
</tbody>
</table>

For more information, see  _Virtual Private Cloud User Guide_.

