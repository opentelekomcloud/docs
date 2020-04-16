# Setting a Security Group<a name="dds_02_0005"></a>

## Scenarios<a name="section3152058916230"></a>

This section guides you on how to add a security group rule to control access from and to  DDS DB instances  in a security group.

## Background Information<a name="section1282916720425"></a>

You can access a DDS DB instance in either of the following ways:

-   Public network
-   Internal network

## Precautions<a name="section14550984204232"></a>

The default security group rule allows all outgoing data packets. ECSs and DDS DB instances can access each other in the same security group. After a security group is created, you can add security group rules to control the access from and to the DDS DB instances in the security group.

By default, a tenant can create a maximum of 500 security group rules. An excessive number of security group rules increases the network latency of the first packet. It is recommended that you add a maximum of 50 rules for each security group.

To access the DDS DB instances in a security group from external resources, create an inbound rule for the security group.

## **Procedure**<a name="section25078651204428"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0225630996.png)  in the upper left corner and select a region and project.
3.  Click  **Service List**. Under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Group**  page, click the security group name.
6.  On the  **Inbound Rules**  tab, click  **Add Rule**. In the displayed  **Add Inbound Rule**  dialog box, set required parameters to add inbound rules. On the  **Outbound Rules**  tab, click  **Add Rule**. In the displayed  **Add Outbound Rule**  dialog box, set required parameters to add outbound rules.
7.  Add a security group rule as prompted.

    **Table  1**  Field description

    <a name="en-us_topic_0118534005_table532116198213"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534005_row731911191722"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118534005_p17319119020"><a name="en-us_topic_0118534005_p17319119020"></a><a name="en-us_topic_0118534005_p17319119020"></a><strong id="b6507101123818"><a name="b6507101123818"></a><a name="b6507101123818"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118534005_p431911191622"><a name="en-us_topic_0118534005_p431911191622"></a><a name="en-us_topic_0118534005_p431911191622"></a><strong id="b1979812213380"><a name="b1979812213380"></a><a name="b1979812213380"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118534005_p103191119621"><a name="en-us_topic_0118534005_p103191119621"></a><a name="en-us_topic_0118534005_p103191119621"></a><strong id="b84235270617550"><a name="b84235270617550"></a><a name="b84235270617550"></a>Value Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534005_row8320419723"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p1432013199214"><a name="en-us_topic_0118534005_p1432013199214"></a><a name="en-us_topic_0118534005_p1432013199214"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p432017191726"><a name="en-us_topic_0118534005_p432017191726"></a><a name="en-us_topic_0118534005_p432017191726"></a>Specifies the network protocol. Allows all traffic or supports user-defined protocols, TCP, UDP, ICMP, and SSH.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p1332014191216"><a name="en-us_topic_0118534005_p1332014191216"></a><a name="en-us_topic_0118534005_p1332014191216"></a>TCP</p>
    </td>
    </tr>
    <tr id="row15380125810476"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1538118582479"><a name="p1538118582479"></a><a name="p1538118582479"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.2 "><p id="p1391312104488"><a name="p1391312104488"></a><a name="p1391312104488"></a>Specifies the port allowing the access to ECSs or external devices. </p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p1438118583479"><a name="p1438118583479"></a><a name="p1438118583479"></a>8635</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row1732101910217"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p16320131918211"><a name="en-us_topic_0118534005_p16320131918211"></a><a name="en-us_topic_0118534005_p16320131918211"></a>Source/Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.2 "><p id="p1953711281854"><a name="p1953711281854"></a><a name="p1953711281854"></a>Specifies the supported IP address and security group.</p>
    <a name="en-us_topic_0118534005_ul474117187016"></a><a name="en-us_topic_0118534005_ul474117187016"></a><ul id="en-us_topic_0118534005_ul474117187016"><li><strong id="b812614895114"><a name="b812614895114"></a><a name="b812614895114"></a>IP address</strong>: indicates that the security group rule takes effect in a specified IP address range.<a name="ul67881445105111"></a><a name="ul67881445105111"></a><ul id="ul67881445105111"><li>xxx.xxx.xxx.xxx/32 (IPv4)</li><li>xxx.xxx.xxx.0/24 (subnet)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </li><li><strong id="b71025536519"><a name="b71025536519"></a><a name="b71025536519"></a>Security group</strong>: indicates that this rule allows all IP addresses of ECSs to access DDS DB instances in the same specified security group.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><a name="ul209321608538"></a><a name="ul209321608538"></a><ul id="ul209321608538"><li>192.168.10.0/24</li><li>default</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

