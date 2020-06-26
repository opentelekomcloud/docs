# Firewall Overview<a name="acl_0001"></a>

A firewall is an optional layer of security for your subnets. You associate one or more subnets with a firewall. The firewall can help control traffic in and out of the subnets.

[Figure 1](#fig9582182315479)  shows how a firewall works.

**Figure  1**  Security groups and firewalls<a name="fig9582182315479"></a>  
![](figures/security-groups-and-firewalls.png "security-groups-and-firewalls")

Similar to security groups, firewalls control access to the network. They add an additional layer of defense to your VPC. Security groups only have the "allow" rules, but firewalls have both "allow" and "deny" rules. You can use firewalls together with security groups to implement access control that is both comprehensive and fine-grained.

[Differences Between Security Groups and Firewalls](differences-between-security-groups-and-firewalls.md)  summarizes the basic differences between security groups and firewalls.

## Firewall Basics<a name="section1952742625114"></a>

-   Your VPC does not come with a default firewall, but you can create one and associate it with a subnet if required. By default, each firewall denies all inbound traffic to and outbound traffic from the associated subnet until you add rules.
-   You can associate a firewall with multiple subnets. However, a subnet can only be associated with one firewall at a time.
-   Each newly created firewall is in the  **Inactive**  state until you associate subnets with it.

## Default Firewall Rules<a name="section99541345213"></a>

By default, each firewall has preset rules that allow the following packets:

-   Packets whose source and destination are in the same subnet
-   Broadcast packets with the destination 255.255.255.255/32, which is used to configure host startup information.
-   Multicast packets with the destination 224.0.0.0/24, which is used by routing protocols.
-   Metadata packets with the destination 169.254.169.254/32 and TCP port number 80, which is used to obtain metadata.
-   Packets from CIDR blocks that are reserved for public services \(for example, packets with the destination 100.125.0.0/16\)
-   A firewall denies all traffic in and out of a subnet excepting the preceding ones.  [Table 1](#table1034601475112)  shows the default firewall rules. The default rules cannot be modified or deleted.

    **Table  1**  Default firewall rules

    <a name="table1034601475112"></a>
    <table><thead align="left"><tr id="row1267171445118"><th class="cellrowborder" valign="top" width="11.918808119188078%" id="mcps1.2.8.1.1"><p id="p4671214185116"><a name="p4671214185116"></a><a name="p4671214185116"></a><strong id="b12656727141516"><a name="b12656727141516"></a><a name="b12656727141516"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="6.05939406059394%" id="mcps1.2.8.1.2"><p id="p46711614195111"><a name="p46711614195111"></a><a name="p46711614195111"></a>Priority</p>
    </th>
    <th class="cellrowborder" valign="top" width="7.0892910708929096%" id="mcps1.2.8.1.3"><p id="p186711114105115"><a name="p186711114105115"></a><a name="p186711114105115"></a><strong id="b16601851131517"><a name="b16601851131517"></a><a name="b16601851131517"></a>Action</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.25917408259174%" id="mcps1.2.8.1.4"><p id="p86711114195114"><a name="p86711114195114"></a><a name="p86711114195114"></a><strong id="b14117145217158"><a name="b14117145217158"></a><a name="b14117145217158"></a>Protocol</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.198580141985797%" id="mcps1.2.8.1.5"><p id="p12671101405114"><a name="p12671101405114"></a><a name="p12671101405114"></a><strong id="b42971979165"><a name="b42971979165"></a><a name="b42971979165"></a>Source</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.568743125687428%" id="mcps1.2.8.1.6"><p id="p2671814165117"><a name="p2671814165117"></a><a name="p2671814165117"></a><strong id="b32151116131617"><a name="b32151116131617"></a><a name="b32151116131617"></a>Destination</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.90600939906009%" id="mcps1.2.8.1.7"><p id="p136711114195118"><a name="p136711114195118"></a><a name="p136711114195118"></a><strong id="b84235270694155"><a name="b84235270694155"></a><a name="b84235270694155"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row167117147516"><td class="cellrowborder" valign="top" width="11.918808119188078%" headers="mcps1.2.8.1.1 "><p id="p14671214175113"><a name="p14671214175113"></a><a name="p14671214175113"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="6.05939406059394%" headers="mcps1.2.8.1.2 "><p id="p467181413516"><a name="p467181413516"></a><a name="p467181413516"></a>*</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.0892910708929096%" headers="mcps1.2.8.1.3 "><p id="p767141475110"><a name="p767141475110"></a><a name="p767141475110"></a>Deny</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25917408259174%" headers="mcps1.2.8.1.4 "><p id="p12671161413512"><a name="p12671161413512"></a><a name="p12671161413512"></a>All</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.198580141985797%" headers="mcps1.2.8.1.5 "><p id="p1967117148511"><a name="p1967117148511"></a><a name="p1967117148511"></a>0.0.0.0/0</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.568743125687428%" headers="mcps1.2.8.1.6 "><p id="p10671101425118"><a name="p10671101425118"></a><a name="p10671101425118"></a>0.0.0.0/0</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.90600939906009%" headers="mcps1.2.8.1.7 "><p id="p967101418517"><a name="p967101418517"></a><a name="p967101418517"></a>Denies all inbound traffic.</p>
    </td>
    </tr>
    <tr id="row11671414155113"><td class="cellrowborder" valign="top" width="11.918808119188078%" headers="mcps1.2.8.1.1 "><p id="p1567121445119"><a name="p1567121445119"></a><a name="p1567121445119"></a>Outbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="6.05939406059394%" headers="mcps1.2.8.1.2 "><p id="p2671161475110"><a name="p2671161475110"></a><a name="p2671161475110"></a>*</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.0892910708929096%" headers="mcps1.2.8.1.3 "><p id="p18671181425114"><a name="p18671181425114"></a><a name="p18671181425114"></a>Deny</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25917408259174%" headers="mcps1.2.8.1.4 "><p id="p667111455114"><a name="p667111455114"></a><a name="p667111455114"></a>All</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.198580141985797%" headers="mcps1.2.8.1.5 "><p id="p3671114195119"><a name="p3671114195119"></a><a name="p3671114195119"></a>0.0.0.0/0</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.568743125687428%" headers="mcps1.2.8.1.6 "><p id="p06711814205118"><a name="p06711814205118"></a><a name="p06711814205118"></a>0.0.0.0/0</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.90600939906009%" headers="mcps1.2.8.1.7 "><p id="p17671814105114"><a name="p17671814105114"></a><a name="p17671814105114"></a>Denies all outbound traffic.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Rule Priorities<a name="section74125695419"></a>

-   Each firewall rule has a priority value where a smaller value corresponds to a higher priority. Any time two rules conflict, the one with the higher priority is the one that get applied. The rule whose priority value is an asterisk \(\*\) has the lowest priority.
-   If multiple firewall rules conflict, the rule with the highest priority takes effect. If you need a rule to take effect before or after a specific rule, you can insert that rule before or after the specific rule.

## Application Scenarios<a name="section1864416226298"></a>

-   If the application layer needs to provide services for users, traffic must be allowed to reach the application layer from all IP addresses. However, you also need to prevent illegal access from malicious users.

    Solution: You can add firewall rules to deny access from suspect IP addresses.

-   How can I isolate ports with identified vulnerabilities? For example, how do I isolate port 445 that can be exploited by WannaCry worm?

    Solution: You can add firewall rules to deny access traffic from specific port and protocol, for example, TCP port 445.

-   No defense is required for the east-west traffic between subnets, but access control is required for north-south traffic.

    Solution: You can add firewall rules to protect north-south traffic.

-   For frequently accessed applications, a security rule sequence may need to be adjusted to improve performance.

    Solution: A firewall allows you to adjust the rule sequence so that frequently used rules are applied before other rules.


## Firewall Configuration Procedure<a name="section14396131910515"></a>

[Figure 2](#fig1643183218163)  shows the procedure for configuring a firewall.

**Figure  2**  Firewall configuration procedure<a name="fig1643183218163"></a>  
![](figures/firewall-configuration-procedure.png "firewall-configuration-procedure")

1.  Create a firewall by following the steps described in  [Creating a Firewall](creating-a-firewall.md).
2.  Add firewall rules by following the steps described in  [Adding a Firewall Rule](adding-a-firewall-rule.md).
3.  Associate subnets with the firewall by following the steps described in  [Associating Subnets with a Firewall](associating-subnets-with-a-firewall.md). After subnets are associated with the firewall, the subnets will be protected by the configured firewall rules.

