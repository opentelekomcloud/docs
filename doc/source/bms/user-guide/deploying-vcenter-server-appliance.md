# Deploying vCenter Server Appliance<a name="EN-US_TOPIC_0159392258"></a>

1.  Deploy vCenter Server Appliance on the ESXi host. For details, see section "Deploying the vCenter Server Appliance and Platform Services Controller Appliance" in  [vSphere Installation and Setup](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.install.doc/GUID-F06BA415-66D8-42CD-9151-701BBBCE8D65.html).
2.  Some example configurations are as follows:
    1.  When importing the OVA file during the first installation phase, set a static IP address 11.11.11.3 for vCenter Server Appliance, and set the subnet mask to 255.255.255.0, default gateway to 11.11.11.1, and DNS to 11.11.11.6.
    2.  In phase 2, set the username and password of the new vCenter Single Sign-on domain. Assume that the username is  **administrator**, domain name is  **vsphere.local**, and site name is  **photon-machine**.

        ![](figures/4-4.png)

3.  Log in to vCenter Web Client and create a data center and a cluster.
4.  On the vCenter Web Client, create three distributed virtual switches \(DVSs\), create one or more distributed port groups on each DVS, and configure VLAN IDs for the distributed port groups based on DPortGroup-mgmt, DPortGroup-vxlan, DPortGroup-edge-internal, and DPortGroup-vsan.  [Table 1](#table47011255194512)  lists the DVSs and distributed port groups.

    **Table  1**  Configuration information

    <a name="table47011255194512"></a>
    <table><thead align="left"><tr id="row50855279"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p25636935"><a name="p25636935"></a><a name="p25636935"></a>DVS</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p33061902"><a name="p33061902"></a><a name="p33061902"></a>Distributed Port Group</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p10044987"><a name="p10044987"></a><a name="p10044987"></a>VLAN ID</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7929439"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38304827"><a name="p38304827"></a><a name="p38304827"></a>dvSwitch-0</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15683279"><a name="p15683279"></a><a name="p15683279"></a>DPortGroup-mgmt</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62386116"><a name="p62386116"></a><a name="p62386116"></a>0</p>
    </td>
    </tr>
    <tr id="row24604138"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46778195"><a name="p46778195"></a><a name="p46778195"></a>dvSwitch-1</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30937456"><a name="p30937456"></a><a name="p30937456"></a>DPortGroup-vxlan</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22906026"><a name="p22906026"></a><a name="p22906026"></a>200</p>
    </td>
    </tr>
    <tr id="row4827645"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p55494956"><a name="p55494956"></a><a name="p55494956"></a>dvSwitch-1</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65906476"><a name="p65906476"></a><a name="p65906476"></a>DPortGroup-edge-internal</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36824357"><a name="p36824357"></a><a name="p36824357"></a>300</p>
    </td>
    </tr>
    <tr id="row62983758"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1410734"><a name="p1410734"></a><a name="p1410734"></a>dvSwitch-2</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p47160602"><a name="p47160602"></a><a name="p47160602"></a>DPortGroup-vsan</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61912443"><a name="p61912443"></a><a name="p61912443"></a>400</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Create the VMkernel NIC on the hb-vsan port group. Select  **Virtual SAN traffic**  for the port attribute and configure the IP address based on  [Table 3](environment-preparations.md#table5655194511448).

    Migrate the VMkernel NIC and uplink on vSwitch1 to the distributed port group and DVS of dpg-hb-mgmt.

6.  Add the first ESXi host to vCenter through IP address 11.11.11.101.

    Configure a distributed switch and migrate the vmknic, DNS/NTP, vCenter, and jump VM to the switch. For details, see section  [Setting Up Networking with vSphere Distributed Switches](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-375B45C7-684C-4C51-BA3C-70E48DFABF04.html).

7.  Add the ESXi host to the DVSs dvSwitch-1 and dvSwitch-2. Use uplinks vmnic4/vmnic5 and vmnic6/vmnic7 in active/standby mode.
8.  Add the ESXi host to the distributed switch dvSwitch-0 using the uplink vmnic3.
9.  Migrate the VMkernel NIC vmk1 to the distributed port group dpg-hb-mgmt.
10. Connect the DNS/NTP on the ESXi host and the vNIC of the vCenter VM to the distributed port group dpg-hb-mgmt.
11. Migrate the Windows jump VM on the ESXi host and connect the vNIC that connects to vSwitch1/hb-mgmt to the port group dpg-hb-mgmt on dvSwitch0.
12. Add vmnic2 to dvSwitch-0 and delete the vSwitch1 VM.

    Configurations of the vSwitch on the first ESXi host are as follows.

    **Table  2**  vSwitch configuration \(first ESXi host\)

    <a name="table19703055134513"></a>
    <table><thead align="left"><tr id="row14294113"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p16972520"><a name="p16972520"></a><a name="p16972520"></a>Port Group</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p24936720"><a name="p24936720"></a><a name="p24936720"></a>vSwitch</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p59475977"><a name="p59475977"></a><a name="p59475977"></a>Uplink</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p5661318"><a name="p5661318"></a><a name="p5661318"></a>vlan ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p33460290"><a name="p33460290"></a><a name="p33460290"></a>vmkernel NIC</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32033984"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p44615908"><a name="p44615908"></a><a name="p44615908"></a>management network</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p57118825"><a name="p57118825"></a><a name="p57118825"></a>vSwitch0</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p63222135"><a name="p63222135"></a><a name="p63222135"></a>vmnic0</p>
    <p id="p32128304"><a name="p32128304"></a><a name="p32128304"></a>vmnic1</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p52255837"><a name="p52255837"></a><a name="p52255837"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p4864423"><a name="p4864423"></a><a name="p4864423"></a>vmk0</p>
    </td>
    </tr>
    <tr id="row43779810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p56503713"><a name="p56503713"></a><a name="p56503713"></a>hb-mgmt</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p13398065"><a name="p13398065"></a><a name="p13398065"></a>dvSwitch-0</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p11501498"><a name="p11501498"></a><a name="p11501498"></a>vmnic2</p>
    <p id="p36404619"><a name="p36404619"></a><a name="p36404619"></a>vmnic3</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p63092987"><a name="p63092987"></a><a name="p63092987"></a>0</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p10258295"><a name="p10258295"></a><a name="p10258295"></a>vmk1</p>
    </td>
    </tr>
    <tr id="row25215798"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p29213744"><a name="p29213744"></a><a name="p29213744"></a>DPortGroup -vxlan</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p17503083"><a name="p17503083"></a><a name="p17503083"></a>dvSwitch-1</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p8463631"><a name="p8463631"></a><a name="p8463631"></a>vmnic4</p>
    <p id="p9063815"><a name="p9063815"></a><a name="p9063815"></a>vmnic5</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p63080410"><a name="p63080410"></a><a name="p63080410"></a>100</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p9239594"><a name="p9239594"></a><a name="p9239594"></a>-</p>
    </td>
    </tr>
    <tr id="row16047484"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p24777809"><a name="p24777809"></a><a name="p24777809"></a>hb-edge-internal</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p60845527"><a name="p60845527"></a><a name="p60845527"></a>300</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p29540661"><a name="p29540661"></a><a name="p29540661"></a>-</p>
    </td>
    </tr>
    <tr id="row64539365"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p60306108"><a name="p60306108"></a><a name="p60306108"></a>DPortGroup -vsan</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p52956542"><a name="p52956542"></a><a name="p52956542"></a>dvSwitch-2</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p61621525"><a name="p61621525"></a><a name="p61621525"></a>vmnic6</p>
    <p id="p17722820"><a name="p17722820"></a><a name="p17722820"></a>vmnic7</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p26262325"><a name="p26262325"></a><a name="p26262325"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p46873582"><a name="p46873582"></a><a name="p46873582"></a>vmk2</p>
    </td>
    </tr>
    </tbody>
    </table>


