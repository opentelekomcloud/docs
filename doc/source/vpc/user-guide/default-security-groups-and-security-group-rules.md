# Default Security Groups and Security Group Rules<a name="SecurityGroup_0003"></a>

Your account automatically comes with a security group by default. The default security group allows all outbound traffic, denies all inbound traffic, and allows all traffic between ECSs in the group. Your ECSs in the security group can communicate with each other by default. There is no need to add rules for this.

[Figure 1](#fig997718156161)  shows the default security group.

**Figure  1**  Default security group<a name="fig997718156161"></a>  
![](figures/default-security-group.png "default-security-group")

[Table 1](#table1580115155277)  describes the default rules for a default security group.

**Table  1**  Default security group rules

<a name="table1580115155277"></a>
<table><thead align="left"><tr id="row15801415182713"><th class="cellrowborder" valign="top" width="14.26%" id="mcps1.2.6.1.1"><p id="p15802141552711"><a name="p15802141552711"></a><a name="p15802141552711"></a><strong id="b842352706194648"><a name="b842352706194648"></a><a name="b842352706194648"></a>Direction</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.459999999999999%" id="mcps1.2.6.1.2"><p id="p11802131517270"><a name="p11802131517270"></a><a name="p11802131517270"></a><strong id="b842352706194658"><a name="b842352706194658"></a><a name="b842352706194658"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.6.1.3"><p id="p2415644494621"><a name="p2415644494621"></a><a name="p2415644494621"></a><strong id="b842352706194415"><a name="b842352706194415"></a><a name="b842352706194415"></a>Port/Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.1%" id="mcps1.2.6.1.4"><p id="p5726142910428"><a name="p5726142910428"></a><a name="p5726142910428"></a><strong id="b842352706204628"><a name="b842352706204628"></a><a name="b842352706204628"></a>Source/Destination</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.470000000000002%" id="mcps1.2.6.1.5"><p id="p103721737152919"><a name="p103721737152919"></a><a name="p103721737152919"></a><strong id="b84235270694155"><a name="b84235270694155"></a><a name="b84235270694155"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1280251562712"><td class="cellrowborder" valign="top" width="14.26%" headers="mcps1.2.6.1.1 "><p id="p680211519274"><a name="p680211519274"></a><a name="p680211519274"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.6.1.2 "><p id="p380271516271"><a name="p380271516271"></a><a name="p380271516271"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.6.1.3 "><p id="p16955313314"><a name="p16955313314"></a><a name="p16955313314"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.2.6.1.4 "><p id="p780201519279"><a name="p780201519279"></a><a name="p780201519279"></a>Destination: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="29.470000000000002%" headers="mcps1.2.6.1.5 "><p id="p237233720296"><a name="p237233720296"></a><a name="p237233720296"></a>Allow all outbound traffic.</p>
</td>
</tr>
<tr id="row1980261512714"><td class="cellrowborder" valign="top" width="14.26%" headers="mcps1.2.6.1.1 "><p id="p1931115561307"><a name="p1931115561307"></a><a name="p1931115561307"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.6.1.2 "><p id="p180281512274"><a name="p180281512274"></a><a name="p180281512274"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.6.1.3 "><p id="p141995510319"><a name="p141995510319"></a><a name="p141995510319"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.2.6.1.4 "><p id="p3802181552715"><a name="p3802181552715"></a><a name="p3802181552715"></a>Source: ID of the current security group (for example, sg-<em id="i2138146127154428"><a name="i2138146127154428"></a><a name="i2138146127154428"></a>xxxxx</em>)</p>
</td>
<td class="cellrowborder" valign="top" width="29.470000000000002%" headers="mcps1.2.6.1.5 "><p id="p14372153702916"><a name="p14372153702916"></a><a name="p14372153702916"></a>Allow communication among ECSs within the security group and deny all inbound traffic (incoming data packets).</p>
</td>
</tr>
</tbody>
</table>

