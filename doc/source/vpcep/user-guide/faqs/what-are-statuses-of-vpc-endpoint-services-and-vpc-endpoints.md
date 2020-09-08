# What Are Statuses of VPC Endpoint Services and VPC Endpoints?<a name="vpcep_04_0005"></a>

[Table 1](#table740435852615)  describes statuses of a VPC endpoint service and their meanings.

**Table  1**  Statuses of a VPC endpoint service

<a name="table740435852615"></a>
<table><thead align="left"><tr id="row154047580269"><th class="cellrowborder" valign="top" width="17.14%" id="mcps1.2.3.1.1"><p id="p14404145852613"><a name="p14404145852613"></a><a name="p14404145852613"></a><strong id="b258754865213"><a name="b258754865213"></a><a name="b258754865213"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="82.86%" id="mcps1.2.3.1.2"><p id="p12404165852618"><a name="p12404165852618"></a><a name="p12404165852618"></a><strong id="b14167155015526"><a name="b14167155015526"></a><a name="b14167155015526"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1340465892617"><td class="cellrowborder" valign="top" width="17.14%" headers="mcps1.2.3.1.1 "><p id="p64047585266"><a name="p64047585266"></a><a name="p64047585266"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="82.86%" headers="mcps1.2.3.1.2 "><p id="p640405813268"><a name="p640405813268"></a><a name="p640405813268"></a>Indicates that the VPC endpoint service is being created.</p>
</td>
</tr>
<tr id="row1040512589265"><td class="cellrowborder" valign="top" width="17.14%" headers="mcps1.2.3.1.1 "><p id="p9405658152614"><a name="p9405658152614"></a><a name="p9405658152614"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="82.86%" headers="mcps1.2.3.1.2 "><p id="p10128174711292"><a name="p10128174711292"></a><a name="p10128174711292"></a>Indicates that the VPC endpoint service is created and can accept a VPC endpoint.</p>
</td>
</tr>
<tr id="row24051558112619"><td class="cellrowborder" valign="top" width="17.14%" headers="mcps1.2.3.1.1 "><p id="p1740555814264"><a name="p1740555814264"></a><a name="p1740555814264"></a>Failed</p>
</td>
<td class="cellrowborder" valign="top" width="82.86%" headers="mcps1.2.3.1.2 "><p id="p1840535812619"><a name="p1840535812619"></a><a name="p1840535812619"></a>Indicates that the VPC endpoint service fails to be created.</p>
</td>
</tr>
<tr id="row10405155872617"><td class="cellrowborder" valign="top" width="17.14%" headers="mcps1.2.3.1.1 "><p id="p1740525810261"><a name="p1740525810261"></a><a name="p1740525810261"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="82.86%" headers="mcps1.2.3.1.2 "><p id="p1340575812620"><a name="p1340575812620"></a><a name="p1340575812620"></a>Indicates that the VPC endpoint service is being deleted.</p>
</td>
</tr>
<tr id="row10405195892612"><td class="cellrowborder" valign="top" width="17.14%" headers="mcps1.2.3.1.1 "><p id="p14405185822619"><a name="p14405185822619"></a><a name="p14405185822619"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" width="82.86%" headers="mcps1.2.3.1.2 "><p id="p14059580261"><a name="p14059580261"></a><a name="p14059580261"></a>Indicates that the VPC endpoint service has been deleted.</p>
</td>
</tr>
</tbody>
</table>

[Table 2](#table134332505311)  describes statuses of a VPC endpoint and their meanings.

**Table  2**  Statuses of a VPC endpoint

<a name="table134332505311"></a>
<table><thead align="left"><tr id="row4431925115314"><th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.2.3.1.1"><p id="p44392515534"><a name="p44392515534"></a><a name="p44392515534"></a><strong id="b79821817195118"><a name="b79821817195118"></a><a name="b79821817195118"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70.73%" id="mcps1.2.3.1.2"><p id="p9438252537"><a name="p9438252537"></a><a name="p9438252537"></a><strong id="b1695515219514"><a name="b1695515219514"></a><a name="b1695515219514"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3430259533"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p944132595315"><a name="p944132595315"></a><a name="p944132595315"></a>Pending acceptance</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p12527185319364"><a name="p12527185319364"></a><a name="p12527185319364"></a>Indicates that the VPC endpoint is pending acceptance of the owner of the associated VPC endpoint service.</p>
</td>
</tr>
<tr id="row84442535310"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p744925145312"><a name="p744925145312"></a><a name="p744925145312"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p174422513537"><a name="p174422513537"></a><a name="p174422513537"></a>Indicates that the VPC endpoint is connecting to the associated VPC endpoint service.</p>
</td>
</tr>
<tr id="row20311114918569"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p1831214975619"><a name="p1831214975619"></a><a name="p1831214975619"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p1231274914563"><a name="p1231274914563"></a><a name="p1231274914563"></a>Indicates that the VPC endpoint is accepted by the associated VPC endpoint service.</p>
</td>
</tr>
<tr id="row57091857105614"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p15709105720568"><a name="p15709105720568"></a><a name="p15709105720568"></a>Rejected</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p1170915713560"><a name="p1170915713560"></a><a name="p1170915713560"></a>Indicates that the VPC endpoint is rejected by the associated VPC endpoint service.</p>
</td>
</tr>
<tr id="row17795510572"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p17918515573"><a name="p17918515573"></a><a name="p17918515573"></a>Failed</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p107917565713"><a name="p107917565713"></a><a name="p107917565713"></a>Indicates that the VPC endpoint fails to connect to the associated VPC endpoint service.</p>
</td>
</tr>
<tr id="row1440512175714"><td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.2.3.1.1 "><p id="p5402126574"><a name="p5402126574"></a><a name="p5402126574"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="70.73%" headers="mcps1.2.3.1.2 "><p id="p1240181255719"><a name="p1240181255719"></a><a name="p1240181255719"></a>Indicates that the VPC endpoint is being deleted.</p>
</td>
</tr>
</tbody>
</table>

