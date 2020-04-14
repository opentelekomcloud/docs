# Modifying a Subnet<a name="vpc_vpc_0001"></a>

## Scenarios<a name="s81d197a61ece470aa5393f50fa131bf6"></a>

Change the subnet name, NTP server address, and DNS server address.

## Procedure<a name="sedd7d89d31ad414698b7418d9a9cbd6f"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC for which a subnet is to be modified and click the VPC name.
6.  In the subnet list, locate the target subnet and click  **Modify**. Modify the parameters as prompted.

    **Figure  1**  Modify Subnet<a name="fig6212173213319"></a>  
    ![](figures/modify-subnet.png "modify-subnet")

    **Table  1**  Parameter description

    <a name="t1358556fe53340eb82fa8c754581b79d"></a>
    <table><thead align="left"><tr id="r9fa5b742a4a3411f8c03962647a54613"><th class="cellrowborder" valign="top" width="32.22%" id="mcps1.2.4.1.1"><p id="a8dc96d68aa234b9493333915ccbe0f6d"><a name="a8dc96d68aa234b9493333915ccbe0f6d"></a><a name="a8dc96d68aa234b9493333915ccbe0f6d"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.1%" id="mcps1.2.4.1.2"><p id="a72187a613d4e4200b43f8f187713722f"><a name="a72187a613d4e4200b43f8f187713722f"></a><a name="a72187a613d4e4200b43f8f187713722f"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.68%" id="mcps1.2.4.1.3"><p id="a75e440e19d704953b2f9c4ec237001dc"><a name="a75e440e19d704953b2f9c4ec237001dc"></a><a name="a75e440e19d704953b2f9c4ec237001dc"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r4b7733c08f1b44efa71c70084ae18ba2"><td class="cellrowborder" valign="top" width="32.22%" headers="mcps1.2.4.1.1 "><p id="a8d06ad8e6b3147fa803fbce3f40c8dff"><a name="a8d06ad8e6b3147fa803fbce3f40c8dff"></a><a name="a8d06ad8e6b3147fa803fbce3f40c8dff"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.1%" headers="mcps1.2.4.1.2 "><p id="a1122b5a9ae354f90a3c59181681ce331"><a name="a1122b5a9ae354f90a3c59181681ce331"></a><a name="a1122b5a9ae354f90a3c59181681ce331"></a>Specifies the subnet name.</p>
    <p id="p24201817123619"><a name="p24201817123619"></a><a name="p24201817123619"></a>The VPC flow log name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.3 "><p id="a02044c412e894f908b0e3ec406fda14c"><a name="a02044c412e894f908b0e3ec406fda14c"></a><a name="a02044c412e894f908b0e3ec406fda14c"></a>Subnet</p>
    </td>
    </tr>
    <tr id="row08664184148"><td class="cellrowborder" valign="top" width="32.22%" headers="mcps1.2.4.1.1 "><p id="p88661918201415"><a name="p88661918201415"></a><a name="p88661918201415"></a>DNS Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.1%" headers="mcps1.2.4.1.2 "><p id="p15436112194319"><a name="p15436112194319"></a><a name="p15436112194319"></a>By default, two DNS server addresses are configured. You can change them as required. A maximum of five DNS server addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.3 "><p id="p108271634171219"><a name="p108271634171219"></a><a name="p108271634171219"></a>100.125.x.x</p>
    </td>
    </tr>
    <tr id="row653864310412"><td class="cellrowborder" valign="top" width="32.22%" headers="mcps1.2.4.1.1 "><p id="p1984172312520"><a name="p1984172312520"></a><a name="p1984172312520"></a>NTP Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.1%" headers="mcps1.2.4.1.2 "><p id="p927533664219"><a name="p927533664219"></a><a name="p927533664219"></a>Specifies the IP address of the NTP server. This parameter is optional.</p>
    <p id="p195514432428"><a name="p195514432428"></a><a name="p195514432428"></a>You can configure the NTP server IP addresses to be added to the subnet as required. The IP addresses are added in addition to the default NTP server addresses. If this parameter is left empty, no IP address of the NTP server is added.</p>
    <p id="p7667123710153"><a name="p7667123710153"></a><a name="p7667123710153"></a>A maximum of four IP addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    <div class="note" id="note42882459322"><a name="note42882459322"></a><a name="note42882459322"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0118498970_ul75071540174811"></a><a name="en-us_topic_0118498970_ul75071540174811"></a><ul id="en-us_topic_0118498970_ul75071540174811"><li>If you add or change the NTP server addresses of a subnet, you need to renew the DHCP lease for or restart all the ECSs in the subnet to make the change take effect immediately.</li><li>If the NTP server addresses have been cleared out, restarting the ECSs will not help. You must renew the DHCP lease for all ECSs to make the change take effect immediately.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.3 "><p id="p484723192518"><a name="p484723192518"></a><a name="p484723192518"></a>192.168.2.1</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

