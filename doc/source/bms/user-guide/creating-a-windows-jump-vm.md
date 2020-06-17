# Creating a Windows Jump VM<a name="EN-US_TOPIC_0159392256"></a>

Create a jump VM that connects to the hb-mgmt network and VPC. Configure VMware components manually or enable automatic configuration.

1.  Create a Windows VM as a jump server and connect the VM to the hb-mgmt network.
    1.  On the  **vSwitch**  page, click  **Add Standard vSwitch**. In the displayed dialog box, enter  **vSwitch1**for  **vSwitch Name**  and add uplinks  **vmnic2**  and  **vmnic3**.
    2.  Click  **Add Port Group**. In the displayed dialog box, select  **vSwitch1**  for  **vSwitch**, add port group  **hb-mgmt**, and set  **VLAN ID**  to  **0**.
    3.  Create a VM and configure a network adapter to connect the VM to the  **hb-mgmt**  port group.
    4.  Start the VM and install Windows on the VM. After the installation is complete, configure IP address 11.11.11.2 for the VM.
    5.  Use the remote desktop to log in to the Windows jump VM and enable the remote desktop service \(set the gateway address to 11.11.11.1 and disable the firewall of the jump VM\).
    6.  Upload the downloaded software such as the vCenter ISO and NSX-manager ovf templates to the jump VM.

2.  On the  **VMkernel NIC**  page, click  **Add VMkernel NIC**. In the displayed dialog box, select  **vSwitch1**  for  **vSwitch**, create  **VMkernel**  port group and NIC, and set  **VLAN ID**  to  **0**  and  **Address**  to  **11.11.11.101**.

    The configurations of vSwitch and port groups on the ESXi host are as follows.

    **Table  1**  vSwitch and port group configurations

    <a name="table77251121236"></a>
    <table><thead align="left"><tr id="row127243211133"><th class="cellrowborder" valign="top" width="22.68%" id="mcps1.2.5.1.1"><p id="p127241821131"><a name="p127241821131"></a><a name="p127241821131"></a>Port Group</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.68%" id="mcps1.2.5.1.2"><p id="p1872413211631"><a name="p1872413211631"></a><a name="p1872413211631"></a>vSwitch</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.68%" id="mcps1.2.5.1.3"><p id="p1472413214316"><a name="p1472413214316"></a><a name="p1472413214316"></a>Uplink</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.5.1.4"><p id="p87249214318"><a name="p87249214318"></a><a name="p87249214318"></a>VMkernel NIC</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row97251121439"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.5.1.1 "><p id="p167243212318"><a name="p167243212318"></a><a name="p167243212318"></a>management network</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.5.1.2 "><p id="p13724821539"><a name="p13724821539"></a><a name="p13724821539"></a>vSwitch0</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.5.1.3 "><p id="p572442112315"><a name="p572442112315"></a><a name="p572442112315"></a>vmnic0/vmnic1</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.5.1.4 "><p id="p127258219314"><a name="p127258219314"></a><a name="p127258219314"></a>vmk0</p>
    </td>
    </tr>
    <tr id="row187254211036"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.2.5.1.1 "><p id="p1872572116311"><a name="p1872572116311"></a><a name="p1872572116311"></a>hb-mgmt</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="22.68%" headers="mcps1.2.5.1.2 "><p id="p1872517218320"><a name="p1872517218320"></a><a name="p1872517218320"></a>vSwitch1</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="22.68%" headers="mcps1.2.5.1.3 "><p id="p17251421430"><a name="p17251421430"></a><a name="p17251421430"></a>vmnic2</p>
    <p id="p12725142116316"><a name="p12725142116316"></a><a name="p12725142116316"></a>vmnic3</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.5.1.4 "><p id="p1972522120320"><a name="p1972522120320"></a><a name="p1972522120320"></a>-</p>
    </td>
    </tr>
    <tr id="row1725122118320"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5725621436"><a name="p5725621436"></a><a name="p5725621436"></a>vmk-hb-mgmt</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p772516211633"><a name="p772516211633"></a><a name="p772516211633"></a>vmk1</p>
    </td>
    </tr>
    </tbody>
    </table>


