# Overview<a name="qsg_0002"></a>

If your ECSs need to access the Internet \(for example, the ECSs functioning as the service nodes for deploying a website\), you can follow the procedure shown in  [Figure 1](#en-us_topic_0118499056_fe457c1ec47c84d6fa3b87210d5b284eb)  to bind EIPs to the ECSs.

**Figure  1**  Configuring the network<a name="en-us_topic_0118499056_fe457c1ec47c84d6fa3b87210d5b284eb"></a>  
![](figures/configuring-the-network.png "configuring-the-network")

[Table 1](#en-us_topic_0118499056_t5143cea7d59f4c31b1c56ab35e86f71f)  describes the different tasks in the procedure for configuring the network.

**Table  1**  Configuration process description

<a name="en-us_topic_0118499056_t5143cea7d59f4c31b1c56ab35e86f71f"></a>
<table><thead align="left"><tr id="en-us_topic_0118499056_rd46fbe417c1a4d4196d4ae976649caa7"><th class="cellrowborder" valign="top" width="38.53%" id="mcps1.2.3.1.1"><p id="en-us_topic_0118499056_aa20c8817f67b40d3ba27b78629516d3f"><a name="en-us_topic_0118499056_aa20c8817f67b40d3ba27b78629516d3f"></a><a name="en-us_topic_0118499056_aa20c8817f67b40d3ba27b78629516d3f"></a>Task</p>
</th>
<th class="cellrowborder" valign="top" width="61.47%" id="mcps1.2.3.1.2"><p id="en-us_topic_0118499056_a0eea81e5c6a947d5915bafe07f886ac8"><a name="en-us_topic_0118499056_a0eea81e5c6a947d5915bafe07f886ac8"></a><a name="en-us_topic_0118499056_a0eea81e5c6a947d5915bafe07f886ac8"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0118499056_rf8fbae6a398f4e658e2c6ad68527ef96"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0118499056_aa349144332da440893bf0db301c34664"><a name="en-us_topic_0118499056_aa349144332da440893bf0db301c34664"></a><a name="en-us_topic_0118499056_aa349144332da440893bf0db301c34664"></a>Create a VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0118499056_abba0097b4ec3474cad85f4b948a9b7a9"><a name="en-us_topic_0118499056_abba0097b4ec3474cad85f4b948a9b7a9"></a><a name="en-us_topic_0118499056_abba0097b4ec3474cad85f4b948a9b7a9"></a>This task is mandatory.</p>
<p id="en-us_topic_0118499056_a597e557ba50f49e88bda01564ff87856"><a name="en-us_topic_0118499056_a597e557ba50f49e88bda01564ff87856"></a><a name="en-us_topic_0118499056_a597e557ba50f49e88bda01564ff87856"></a>You must configure required parameters to create a VPC. The created VPC comes with a default subnet you specified.</p>
<p id="en-us_topic_0118499056_af7d0dddd13744702a347bb7c2e03980a"><a name="en-us_topic_0118499056_af7d0dddd13744702a347bb7c2e03980a"></a><a name="en-us_topic_0118499056_af7d0dddd13744702a347bb7c2e03980a"></a>After the VPC is created, you can create other required network resources in the VPC based on your service requirements.</p>
</td>
</tr>
<tr id="en-us_topic_0118499056_rfa3546e7a13e43fa87b2259e5b952714"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0118499056_a6ee2e9edbf2a4a9c93b4dcaffdb3e8b2"><a name="en-us_topic_0118499056_a6ee2e9edbf2a4a9c93b4dcaffdb3e8b2"></a><a name="en-us_topic_0118499056_a6ee2e9edbf2a4a9c93b4dcaffdb3e8b2"></a>Create another subnet for the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0118499056_a47cd6268a7164960a92b63757bd0b1a3"><a name="en-us_topic_0118499056_a47cd6268a7164960a92b63757bd0b1a3"></a><a name="en-us_topic_0118499056_a47cd6268a7164960a92b63757bd0b1a3"></a>This task is optional.</p>
<p id="en-us_topic_0118499056_a7bef7c1795b4407f8a56a5f6f1e860cb"><a name="en-us_topic_0118499056_a7bef7c1795b4407f8a56a5f6f1e860cb"></a><a name="en-us_topic_0118499056_a7bef7c1795b4407f8a56a5f6f1e860cb"></a>If the default subnet cannot meet your requirements, you can create one.</p>
<p id="en-us_topic_0118499056_ad8cd630dc83c4a7ba9d022fdb3fdd175"><a name="en-us_topic_0118499056_ad8cd630dc83c4a7ba9d022fdb3fdd175"></a><a name="en-us_topic_0118499056_ad8cd630dc83c4a7ba9d022fdb3fdd175"></a>The new subnet is used to assign IP addresses to NICs added to the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0118499056_r570769dc55e84514a7b4217d6a543930"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0118499056_acbb18772996c44fcab4e46dfcdd0dca0"><a name="en-us_topic_0118499056_acbb18772996c44fcab4e46dfcdd0dca0"></a><a name="en-us_topic_0118499056_acbb18772996c44fcab4e46dfcdd0dca0"></a>Assign an EIP and bind it to an ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0118499056_a03804715572c499a8a869ad68fa0305e"><a name="en-us_topic_0118499056_a03804715572c499a8a869ad68fa0305e"></a><a name="en-us_topic_0118499056_a03804715572c499a8a869ad68fa0305e"></a>This task is mandatory.</p>
<p id="en-us_topic_0118499056_a575b5f3fe254423ca89924fa8061b398"><a name="en-us_topic_0118499056_a575b5f3fe254423ca89924fa8061b398"></a><a name="en-us_topic_0118499056_a575b5f3fe254423ca89924fa8061b398"></a>You can assign an EIP and bind it to an ECS so that the ECS can access the Internet.</p>
</td>
</tr>
<tr id="en-us_topic_0118499056_r06afc77d8ba84443a76bdfc23a58a1f5"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0118499056_a6c372f1677c2471c911944ac62db73a6"><a name="en-us_topic_0118499056_a6c372f1677c2471c911944ac62db73a6"></a><a name="en-us_topic_0118499056_a6c372f1677c2471c911944ac62db73a6"></a>Create a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0118499056_ac13a8ad697774a8ba46bbac1947099c2"><a name="en-us_topic_0118499056_ac13a8ad697774a8ba46bbac1947099c2"></a><a name="en-us_topic_0118499056_ac13a8ad697774a8ba46bbac1947099c2"></a>This task is mandatory.</p>
<p id="en-us_topic_0118499056_aa426a5288a00433baa21e6b3f1fcb1e3"><a name="en-us_topic_0118499056_aa426a5288a00433baa21e6b3f1fcb1e3"></a><a name="en-us_topic_0118499056_aa426a5288a00433baa21e6b3f1fcb1e3"></a>You can create a security group and add ECSs in the VPC to the security group to improve ECS access security.</p>
<p id="en-us_topic_0118499056_a898dd82e685844b2bb3d09c12183e878"><a name="en-us_topic_0118499056_a898dd82e685844b2bb3d09c12183e878"></a><a name="en-us_topic_0118499056_a898dd82e685844b2bb3d09c12183e878"></a>After a security group is created, it has a default rule, which allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule meets your service requirements, you do not need to add rules to the security group.</p>
</td>
</tr>
<tr id="en-us_topic_0118499056_ra03bfe4215784be6ae0234c29961410b"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0118499056_a341ecd75565440b598f9ab7c9b6b9e1b"><a name="en-us_topic_0118499056_a341ecd75565440b598f9ab7c9b6b9e1b"></a><a name="en-us_topic_0118499056_a341ecd75565440b598f9ab7c9b6b9e1b"></a>Add a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0118499056_aa73e2da8a7bd4c2f8966de571f359e41"><a name="en-us_topic_0118499056_aa73e2da8a7bd4c2f8966de571f359e41"></a><a name="en-us_topic_0118499056_aa73e2da8a7bd4c2f8966de571f359e41"></a>This task is optional.</p>
<p id="en-us_topic_0118499056_a45a897f64ea544e3aad7cf250d35cdd0"><a name="en-us_topic_0118499056_a45a897f64ea544e3aad7cf250d35cdd0"></a><a name="en-us_topic_0118499056_a45a897f64ea544e3aad7cf250d35cdd0"></a>After a security group is created, it has a default rule, which allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule does not meet your service requirements, you can add a security group rule.</p>
</td>
</tr>
</tbody>
</table>

