# Creating Other ESXi BMSs<a name="EN-US_TOPIC_0159392259"></a>

1.  Create a BMS. Select a flavor and an image \(see  [Table 3](environment-preparations.md#table5655194511448)\) and configure the VPC subnet to which it connects.
2.  Use the key to log in to the ESXi BMS and change the user  **root**  password.
3.  Add a local datastore to the ESXi host.
4.  Create vSwitch1 for the second and third ESXi hosts, set vmnic2 to uplink, and create vmkernel NICs with IP addresses 11.11.11.102 and 11.11.11.103 on vSwitch1.
5.  Log in to the Windows jump VM and vCenter. Add the ESXi hosts to the vCenter host cluster and DVS through IP addresses 11.11.11.102 and 11.11.11.103.
6.  Migrate the VMkernel NIC and uplink on vSwitch1 to the distributed port group and DVS of dvSwitch-0/hb-mgmt. Configurations of the vSwitch on the second and third ESXi hosts are as follows.

    **Table  1**  vSwitch configurations of the second and third ESXi hosts

    <a name="table87051655144515"></a>
    <table><thead align="left"><tr id="row48173795"><th class="cellrowborder" valign="top" width="30.61%" id="mcps1.2.5.1.1"><p id="p9763311"><a name="p9763311"></a><a name="p9763311"></a>Port Group</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.2"><p id="p3914136"><a name="p3914136"></a><a name="p3914136"></a>vSwitch</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.5.1.3"><p id="p34833164"><a name="p34833164"></a><a name="p34833164"></a>Uplink</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.5.1.4"><p id="p26226671"><a name="p26226671"></a><a name="p26226671"></a>vmkernel NIC</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6065350"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.1 "><p id="p21531379"><a name="p21531379"></a><a name="p21531379"></a>management network</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p66320128"><a name="p66320128"></a><a name="p66320128"></a>vSwitch0</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="p3221269"><a name="p3221269"></a><a name="p3221269"></a>vmnic0</p>
    <p id="p28991427"><a name="p28991427"></a><a name="p28991427"></a>vmnic1</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.5.1.4 "><p id="p66604216"><a name="p66604216"></a><a name="p66604216"></a>vmk0</p>
    </td>
    </tr>
    <tr id="row62567033"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.1 "><p id="p34764952"><a name="p34764952"></a><a name="p34764952"></a>DPortGroup-mgmt</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p64497760"><a name="p64497760"></a><a name="p64497760"></a>dvSwitch-0</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="p56936056"><a name="p56936056"></a><a name="p56936056"></a>vmnic2</p>
    <p id="p42662457"><a name="p42662457"></a><a name="p42662457"></a>vmnic3</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.5.1.4 "><p id="p33107021"><a name="p33107021"></a><a name="p33107021"></a>vmk1</p>
    </td>
    </tr>
    <tr id="row29527737"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.1 "><p id="p42936498"><a name="p42936498"></a><a name="p42936498"></a>DPortGroup-vxlan</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p55304348"><a name="p55304348"></a><a name="p55304348"></a>dvSwitch-1</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="p50467231"><a name="p50467231"></a><a name="p50467231"></a>vmnic4</p>
    <p id="p51551897"><a name="p51551897"></a><a name="p51551897"></a>vmnic5</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.5.1.4 "><p id="p14954099"><a name="p14954099"></a><a name="p14954099"></a>-</p>
    </td>
    </tr>
    <tr id="row369165"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p29902409"><a name="p29902409"></a><a name="p29902409"></a>DPortGroup-edge-internal</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p6176061"><a name="p6176061"></a><a name="p6176061"></a>-</p>
    </td>
    </tr>
    <tr id="row55584556"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.5.1.1 "><p id="p6055208"><a name="p6055208"></a><a name="p6055208"></a>DPortGroup-vsan</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.2 "><p id="p20709873"><a name="p20709873"></a><a name="p20709873"></a>dvSwitch-2</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="p66887022"><a name="p66887022"></a><a name="p66887022"></a>vmnic6</p>
    <p id="p65112292"><a name="p65112292"></a><a name="p65112292"></a>vmnic7</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.5.1.4 "><p id="p39604299"><a name="p39604299"></a><a name="p39604299"></a>vmk2</p>
    </td>
    </tr>
    </tbody>
    </table>


