# Setting a Security Group <a name="dds_02_0013"></a>

## **Scenarios**<a name="en-us_topic_0105284937_section3152058916230"></a>

This section guides you on how to add a security group rule to control access from and to  DDS DB instances  in a security group. This document describes how to set security groups.

## Background Information<a name="en-us_topic_0105284937_section1282916720425"></a>

You can access a DDS DB instance in either of the following ways:

-   Public network
-   Internal network

## Precautions<a name="en-us_topic_0105284937_section14550984204232"></a>

The default security group rule allows all outgoing data packets. ECSs and DDS DB instances can access each other in the same security group. After a security group is created, you can add security group rules to control the access from and to the DDS DB instances in the security group.

By default, a tenant can create a maximum of 500 security group rules. An excessive number of security group rules increases the network latency of the first packet. It is recommended that you add a maximum of 50 rules for each security group.

To access the DDS DB instances in a security group from external resources, create an inbound rule for the security group.

## **Procedure**<a name="en-us_topic_0105284937_section25078651204428"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and project.
3.  Click  **Service List**. Under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Group**  page, click the security group name.
6.  On the  **Inbound Rules**  tab, click  **Add Rule**. In the displayed  **Add Inbound Rule**  dialog box, set required parameters to add inbound rules. On the  **Outbound Rules**  tab, click  **Add Rule**. In the displayed  **Add Outbound Rule**  dialog box, set required parameters to add outbound rules.
7.  Add a security group rule as prompted.

    **Table  1**  Parameter description

    <a name="en-us_topic_0105284937_en-us_topic_0118534005_table532116198213"></a>
    <table><thead align="left"><tr id="en-us_topic_0105284937_en-us_topic_0118534005_row731911191722"><th class="cellrowborder" valign="top" width="13.04%" id="mcps1.2.4.1.1"><p id="en-us_topic_0105284937_en-us_topic_0118534005_p17319119020"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p17319119020"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p17319119020"></a><strong id="b158649370431"><a name="b158649370431"></a><a name="b158649370431"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="68.96%" id="mcps1.2.4.1.2"><p id="en-us_topic_0105284937_en-us_topic_0118534005_p431911191622"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p431911191622"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p431911191622"></a><strong id="b1047363994313"><a name="b1047363994313"></a><a name="b1047363994313"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0105284937_en-us_topic_0118534005_p103191119621"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p103191119621"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p103191119621"></a><strong id="b17051140144319"><a name="b17051140144319"></a><a name="b17051140144319"></a>Value Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0105284937_en-us_topic_0118534005_row8320419723"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0105284937_en-us_topic_0118534005_p1432013199214"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p1432013199214"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p1432013199214"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p432017191726"><a name="en-us_topic_0118534005_p432017191726"></a><a name="en-us_topic_0118534005_p432017191726"></a>Specifies the network protocol. Allows all traffic or supports user-defined protocols, TCP, UDP, ICMP, and SSH.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0105284937_en-us_topic_0118534005_p1332014191216"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p1332014191216"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p1332014191216"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0105284937_row15380125810476"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0105284937_p1538118582479"><a name="en-us_topic_0105284937_p1538118582479"></a><a name="en-us_topic_0105284937_p1538118582479"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0105284937_p1391312104488"><a name="en-us_topic_0105284937_p1391312104488"></a><a name="en-us_topic_0105284937_p1391312104488"></a>Specifies the port allowing the access to ECSs or external devices. </p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0105284937_p1438118583479"><a name="en-us_topic_0105284937_p1438118583479"></a><a name="en-us_topic_0105284937_p1438118583479"></a>8635</p>
    </td>
    </tr>
    <tr id="en-us_topic_0105284937_en-us_topic_0118534005_row1732101910217"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0105284937_en-us_topic_0118534005_p16320131918211"><a name="en-us_topic_0105284937_en-us_topic_0118534005_p16320131918211"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_p16320131918211"></a>Source/Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0105284937_p1953711281854"><a name="en-us_topic_0105284937_p1953711281854"></a><a name="en-us_topic_0105284937_p1953711281854"></a>Specifies the supported IP address and security group.</p>
    <a name="en-us_topic_0105284937_en-us_topic_0118534005_ul474117187016"></a><a name="en-us_topic_0105284937_en-us_topic_0118534005_ul474117187016"></a><ul id="en-us_topic_0105284937_en-us_topic_0118534005_ul474117187016"><li><strong id="b6421166468"><a name="b6421166468"></a><a name="b6421166468"></a>IP address</strong>: indicates that the security group rule takes effect in a specified IP address range.<a name="en-us_topic_0105284937_ul67881445105111"></a><a name="en-us_topic_0105284937_ul67881445105111"></a><ul id="en-us_topic_0105284937_ul67881445105111"><li>xxx.xxx.xxx.xxx/32 (IPv4)</li><li>xxx.xxx.xxx.0/24 (subnet)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </li><li><strong id="b122046167469"><a name="b122046167469"></a><a name="b122046167469"></a>Security group</strong>: indicates that this rule allows all IP addresses of ECSs to access DDS DB instances in the same specified security group.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0105284937_ul209321608538"></a><a name="en-us_topic_0105284937_ul209321608538"></a><ul id="en-us_topic_0105284937_ul209321608538"><li>192.168.10.0/24</li><li>default</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

