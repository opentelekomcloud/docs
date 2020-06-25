# Can Multiple EIPs Be Bound to an ECS?<a name="EN-US_TOPIC_0018073216"></a>

## Scenarios<a name="section1851945163017"></a>

An ECS can be bound with multiple EIPs, though this configuration is not recommended.

To bind multiple EIPs, you must manually configure routing policies. Exercise caution when you perform this operation.

## Configuration Example<a name="section32091531162222"></a>

[Table 1](#table10449199163243)  lists ECS configurations.

**Table  1**  ECS configurations

<a name="table10449199163243"></a>
<table><thead align="left"><tr id="row8662904163243"><th class="cellrowborder" valign="top" width="25.19%" id="mcps1.2.3.1.1"><p id="p7023835163243"><a name="p7023835163243"></a><a name="p7023835163243"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="74.81%" id="mcps1.2.3.1.2"><p id="p32059771163243"><a name="p32059771163243"></a><a name="p32059771163243"></a>Configuration</p>
</th>
</tr>
</thead>
<tbody><tr id="row20102485163243"><td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.3.1.1 "><p id="p17688570163243"><a name="p17688570163243"></a><a name="p17688570163243"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="74.81%" headers="mcps1.2.3.1.2 "><p id="p23488080163243"><a name="p23488080163243"></a><a name="p23488080163243"></a>ecs_test</p>
</td>
</tr>
<tr id="row10066133163243"><td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.3.1.1 "><p id="p10050422163243"><a name="p10050422163243"></a><a name="p10050422163243"></a>Image</p>
</td>
<td class="cellrowborder" valign="top" width="74.81%" headers="mcps1.2.3.1.2 "><p id="p8777885163243"><a name="p8777885163243"></a><a name="p8777885163243"></a>Red Hat Enterprise Linux 6.5 64bit</p>
</td>
</tr>
<tr id="row11892101163243"><td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.3.1.1 "><p id="p23736109163243"><a name="p23736109163243"></a><a name="p23736109163243"></a>EIP</p>
</td>
<td class="cellrowborder" valign="top" width="74.81%" headers="mcps1.2.3.1.2 "><p id="p43576653163243"><a name="p43576653163243"></a><a name="p43576653163243"></a>2</p>
</td>
</tr>
<tr id="row56645562163243"><td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.3.1.1 "><p id="p24887810163243"><a name="p24887810163243"></a><a name="p24887810163243"></a>Primary NIC</p>
</td>
<td class="cellrowborder" valign="top" width="74.81%" headers="mcps1.2.3.1.2 "><p id="p2646743163243"><a name="p2646743163243"></a><a name="p2646743163243"></a>eth0</p>
</td>
</tr>
<tr id="row23304392163323"><td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.3.1.1 "><p id="p8412943163323"><a name="p8412943163323"></a><a name="p8412943163323"></a>Secondary NIC</p>
</td>
<td class="cellrowborder" valign="top" width="74.81%" headers="mcps1.2.3.1.2 "><p id="p10359815163323"><a name="p10359815163323"></a><a name="p10359815163323"></a>eth1</p>
</td>
</tr>
</tbody>
</table>

**Example 1:**

If you are required to access public network 11.11.11.0/24 through standby NIC  **eth1**, perform the following operations to configure a routing policy:

1.  Log in to the ECS.
2.  Run the following command to configure a routing policy:

    **ip route add 11.11.11.0/24 dev eth1 via 192.168.2.1**

    In the preceding command,  **192.168.2.1**  is the gateway IP address of standby NIC  **eth1**.


**Example 2:**

Based on example 1, if you are required to enable routing for default public network traffic through standby NIC  **eth1**, perform the following operations to configure a routing policy:

1.  Log in to the ECS.
2.  Run the following command to delete the default route:

    **ip route delete default**

3.  Run the following command to configure a new default route:

    **ip route add 0.0.0.0/0 dev eth1 via 192.168.2.1**

    In the preceding command,  **192.168.2.1**  is the gateway IP address of standby NIC  **eth1**.


