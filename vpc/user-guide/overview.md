# Overview<a name="en-us_topic_0030969441"></a>

If your ECSs do not need to access the Internet or need to access the Internet using a specified IP address with limited bandwidth on default network segment 100.64.0.0/11, for example, the ECSs functioning as the database nodes or server nodes for deploying a website, you can follow the procedure shown in [Figure 1](#fd87108563a6848bba1a0f0295fef3515)  to configure a VPC for the ECSs.

**Figure  1**  Configuring the network<a name="fd87108563a6848bba1a0f0295fef3515"></a>
![](figures/configuring-the-network.png "Configuring the network")

[Table 1](#t1b39acc5d1d449eabbea2aab68bfab25)  describes the different tasks in the procedure for configuring the network.

**Table  1**  Configuration process description

<a name="t1b39acc5d1d449eabbea2aab68bfab25"></a><table><thead align="left"><tr id="r60edadb596314703ac46c7069ce33cfd"><th class="cellrowborder" valign="top" width="38.53%" id="mcps1.2.3.1.1"><p id="a1c262edbb41f41109ed3af0f9f9acd2b"><a name="a1c262edbb41f41109ed3af0f9f9acd2b"></a><a name="a1c262edbb41f41109ed3af0f9f9acd2b"></a>Task</p>
</th>
<th class="cellrowborder" valign="top" width="61.47%" id="mcps1.2.3.1.2"><p id="a014ebb6e4d9649829818d57e6f41c4a9"><a name="a014ebb6e4d9649829818d57e6f41c4a9"></a><a name="a014ebb6e4d9649829818d57e6f41c4a9"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r8b45006c1579411c82d8dcbc6292ea2c"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="a53854b9771bf4562a1197a10fb659e14"><a name="a53854b9771bf4562a1197a10fb659e14"></a><a name="a53854b9771bf4562a1197a10fb659e14"></a>Create a VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="a41c5390044454dd589fc3bddbb7339a9"><a name="a41c5390044454dd589fc3bddbb7339a9"></a><a name="a41c5390044454dd589fc3bddbb7339a9"></a>This task is mandatory.</p>
<p id="ab02ba533334540bfa75e1a8d20625d65"><a name="ab02ba533334540bfa75e1a8d20625d65"></a><a name="ab02ba533334540bfa75e1a8d20625d65"></a>You must configure required parameters to create a VPC. The created VPC comes with a default subnet you specified.</p>
<p id="a818db46b90e44120815cfa8144c35c08"><a name="a818db46b90e44120815cfa8144c35c08"></a><a name="a818db46b90e44120815cfa8144c35c08"></a>After the VPC is created, you can create other required network resources in the VPC based on your service requirements.</p>
</td>
</tr>
<tr id="r348b6d2fc2bc48c2aba92daf85f980f9"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="ac72ef170b0504cc7871f7a875ce934c1"><a name="ac72ef170b0504cc7871f7a875ce934c1"></a><a name="ac72ef170b0504cc7871f7a875ce934c1"></a>Create another subnet for the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="a01d9857fac044d97b501d8c3a83d80b9"><a name="a01d9857fac044d97b501d8c3a83d80b9"></a><a name="a01d9857fac044d97b501d8c3a83d80b9"></a>This task is optional.</p>
<p id="a7bef7c1795b4407f8a56a5f6f1e860cb"><a name="a7bef7c1795b4407f8a56a5f6f1e860cb"></a><a name="a7bef7c1795b4407f8a56a5f6f1e860cb"></a>If you need another subnet in addition to the default one, you can create a subnet in the VPC.</p>
<p id="a1f560b983e2742c38feb0d4f2a752669"><a name="a1f560b983e2742c38feb0d4f2a752669"></a><a name="a1f560b983e2742c38feb0d4f2a752669"></a>The new subnet is used to assign IP addresses to NICs added to the ECS.</p>
</td>
</tr>
<tr id="r34972bb690334883b229040e79833a74"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="a4ccc9086f94c42f39a6e61276e74354c"><a name="a4ccc9086f94c42f39a6e61276e74354c"></a><a name="a4ccc9086f94c42f39a6e61276e74354c"></a>Create a security group.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="a2a5e4b146180467884a76dc60e6f9174"><a name="a2a5e4b146180467884a76dc60e6f9174"></a><a name="a2a5e4b146180467884a76dc60e6f9174"></a>This task is mandatory.</p>
<p id="a14710d49a76c4dc0a94576bffc5e06a5"><a name="a14710d49a76c4dc0a94576bffc5e06a5"></a><a name="a14710d49a76c4dc0a94576bffc5e06a5"></a>You can create a security group and add ECS&nbsp;in the VPC to the security group to improve&nbsp;ECS access security.</p>
<p id="a4a071bd88ba44d5eb30715f42001f885"><a name="a4a071bd88ba44d5eb30715f42001f885"></a><a name="a4a071bd88ba44d5eb30715f42001f885"></a>After a security group is created, it has a default rule, which allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule meets your service requirements, you do not need to add rules to the security group.</p>
</td>
</tr>
<tr id="r2df0384cb2454eeca0ff868997a4ffc3"><td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.3.1.1 "><p id="afba502afa35e4df29757334fbb1d70c3"><a name="afba502afa35e4df29757334fbb1d70c3"></a><a name="afba502afa35e4df29757334fbb1d70c3"></a>Add a security group rule.</p>
</td>
<td class="cellrowborder" valign="top" width="61.47%" headers="mcps1.2.3.1.2 "><p id="a837ce5ee939c4e53a53170e7aafab5c1"><a name="a837ce5ee939c4e53a53170e7aafab5c1"></a><a name="a837ce5ee939c4e53a53170e7aafab5c1"></a>This task is optional.</p>
<p id="a3897c2aae61e41d3af1889a4ddff8d34"><a name="a3897c2aae61e41d3af1889a4ddff8d34"></a><a name="a3897c2aae61e41d3af1889a4ddff8d34"></a>After a security group is created, it has a default rule, which allows all outgoing data packets. ECSs in a security group can access each other without the need to add rules. If the default rule does not meet your service requirements, you can add a security group rule.</p>
</td>
</tr>
</tbody>
</table>

