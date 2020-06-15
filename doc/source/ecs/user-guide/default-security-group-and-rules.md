# Default Security Group and Rules<a name="EN-US_TOPIC_0140323154"></a>

Your account automatically comes with a security group by default. The default security group allows all outbound traffic, denies all inbound traffic, and allows all traffic between ECSs in the group. Your ECSs in the security group can communicate with each other by default. There is no need to add rules for this.

[Figure 1](#fig11890174421819)  shows the default security group.

**Figure  1**  Default security group<a name="fig11890174421819"></a>  
![](figures/default-security-group.png "default-security-group")

[Table 1](#table1580115155277)  describes default security group rules.

**Table  1**  Default security group rules

<a name="table1580115155277"></a>
<table><thead align="left"><tr id="en-us_topic_0118534003_row15801415182713"><th class="cellrowborder" valign="top" width="14.26%" id="mcps1.2.6.1.1"><p id="en-us_topic_0118534003_p15802141552711"><a name="en-us_topic_0118534003_p15802141552711"></a><a name="en-us_topic_0118534003_p15802141552711"></a><strong id="en-us_topic_0118534003_b842352706194648"><a name="en-us_topic_0118534003_b842352706194648"></a><a name="en-us_topic_0118534003_b842352706194648"></a>Direction</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.459999999999999%" id="mcps1.2.6.1.2"><p id="en-us_topic_0118534003_p11802131517270"><a name="en-us_topic_0118534003_p11802131517270"></a><a name="en-us_topic_0118534003_p11802131517270"></a><strong id="en-us_topic_0118534003_b842352706194658"><a name="en-us_topic_0118534003_b842352706194658"></a><a name="en-us_topic_0118534003_b842352706194658"></a>Protocol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.71%" id="mcps1.2.6.1.3"><p id="en-us_topic_0118534003_p2415644494621"><a name="en-us_topic_0118534003_p2415644494621"></a><a name="en-us_topic_0118534003_p2415644494621"></a><strong id="en-us_topic_0118534003_b842352706194415"><a name="en-us_topic_0118534003_b842352706194415"></a><a name="en-us_topic_0118534003_b842352706194415"></a>Port/Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.1%" id="mcps1.2.6.1.4"><p id="en-us_topic_0118534003_p5726142910428"><a name="en-us_topic_0118534003_p5726142910428"></a><a name="en-us_topic_0118534003_p5726142910428"></a><strong id="en-us_topic_0118534003_b842352706204628"><a name="en-us_topic_0118534003_b842352706204628"></a><a name="en-us_topic_0118534003_b842352706204628"></a>Source/Destination</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.470000000000002%" id="mcps1.2.6.1.5"><p id="en-us_topic_0118534003_p103721737152919"><a name="en-us_topic_0118534003_p103721737152919"></a><a name="en-us_topic_0118534003_p103721737152919"></a><strong id="en-us_topic_0118534003_b84235270694155"><a name="en-us_topic_0118534003_b84235270694155"></a><a name="en-us_topic_0118534003_b84235270694155"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0118534003_row1280251562712"><td class="cellrowborder" valign="top" width="14.26%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0118534003_p680211519274"><a name="en-us_topic_0118534003_p680211519274"></a><a name="en-us_topic_0118534003_p680211519274"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0118534003_p380271516271"><a name="en-us_topic_0118534003_p380271516271"></a><a name="en-us_topic_0118534003_p380271516271"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0118534003_p16955313314"><a name="en-us_topic_0118534003_p16955313314"></a><a name="en-us_topic_0118534003_p16955313314"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0118534003_p780201519279"><a name="en-us_topic_0118534003_p780201519279"></a><a name="en-us_topic_0118534003_p780201519279"></a>Destination: 0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="29.470000000000002%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0118534003_p237233720296"><a name="en-us_topic_0118534003_p237233720296"></a><a name="en-us_topic_0118534003_p237233720296"></a>Allow all outbound traffic.</p>
</td>
</tr>
<tr id="en-us_topic_0118534003_row1980261512714"><td class="cellrowborder" valign="top" width="14.26%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0118534003_p1931115561307"><a name="en-us_topic_0118534003_p1931115561307"></a><a name="en-us_topic_0118534003_p1931115561307"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0118534003_p180281512274"><a name="en-us_topic_0118534003_p180281512274"></a><a name="en-us_topic_0118534003_p180281512274"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0118534003_p141995510319"><a name="en-us_topic_0118534003_p141995510319"></a><a name="en-us_topic_0118534003_p141995510319"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0118534003_p3802181552715"><a name="en-us_topic_0118534003_p3802181552715"></a><a name="en-us_topic_0118534003_p3802181552715"></a>Source: ID of the current security group (for example, sg-<em id="en-us_topic_0118534003_i2138146127154428"><a name="en-us_topic_0118534003_i2138146127154428"></a><a name="en-us_topic_0118534003_i2138146127154428"></a>xxxxx</em>)</p>
</td>
<td class="cellrowborder" valign="top" width="29.470000000000002%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0118534003_p14372153702916"><a name="en-us_topic_0118534003_p14372153702916"></a><a name="en-us_topic_0118534003_p14372153702916"></a>Allow communication among ECSs within the security group and deny all inbound traffic (incoming data packets).</p>
</td>
</tr>
</tbody>
</table>

