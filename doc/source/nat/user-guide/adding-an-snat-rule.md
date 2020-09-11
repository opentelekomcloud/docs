# Adding an SNAT Rule<a name="en-us_topic_0127489529"></a>

## Scenarios<a name="en-us_topic_0127293981_section18103401105119"></a>

After the NAT gateway is created, you need to add SNAT rules. With the SNAT rule, servers in the subnet in a VPC or servers that are connected to a VPC through Direct Connect or VPN can access the Internet by sharing an EIP.

An SNAT rule is configured for one subnet. If there are multiple subnets in a VPC, you can create several SNAT rules to share one or more EIPs.

## **Prerequisites**<a name="en-us_topic_0127293981_section27241609"></a>

-   A NAT gateway has been created.

## Procedure<a name="en-us_topic_0127293981_section43847892"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-3.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the SNAT rule.
5.  On the  **SNAT Rules**  tab, click  **Add SNAT Rule**.

    **Figure  1**  Add SNAT Rule<a name="fig7424951145214"></a>  
    ![](figures/add-snat-rule.png "add-snat-rule")

6.  Specify the parameters as prompted. For details, see  [Table 1](#en-us_topic_0127293981_table4272024117597).

    **Table  1**  Parameter description

    <a name="en-us_topic_0127293981_table4272024117597"></a>
    <table><thead align="left"><tr id="en-us_topic_0127293981_row3248015417597"><th class="cellrowborder" valign="top" width="18.01%" id="mcps1.2.4.1.1"><p id="en-us_topic_0127293981_p1364683317597"><a name="en-us_topic_0127293981_p1364683317597"></a><a name="en-us_topic_0127293981_p1364683317597"></a><strong id="b537195719457"><a name="b537195719457"></a><a name="b537195719457"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.91%" id="mcps1.2.4.1.2"><p id="p18531490225"><a name="p18531490225"></a><a name="p18531490225"></a><strong id="b142434125376"><a name="b142434125376"></a><a name="b142434125376"></a>Condition</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.080000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0127293981_p1643000117597"><a name="en-us_topic_0127293981_p1643000117597"></a><a name="en-us_topic_0127293981_p1643000117597"></a><strong id="b1239112593454"><a name="b1239112593454"></a><a name="b1239112593454"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0127293981_row144002379410"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0127293981_p2400173718417"><a name="en-us_topic_0127293981_p2400173718417"></a><a name="en-us_topic_0127293981_p2400173718417"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.4.1.2 "><p id="p11378191114341"><a name="p11378191114341"></a><a name="p11378191114341"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.080000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p4400123718411"><a name="en-us_topic_0127293981_p4400123718411"></a><a name="en-us_topic_0127293981_p4400123718411"></a>Specifies the scenarios in which the SNAT rule is used.</p>
    <p id="p51852719278"><a name="p51852719278"></a><a name="p51852719278"></a>Select <strong>VPC</strong> when your servers in a VPC need to access the Internet.</p>
    <p id="p21892752716"><a name="p21892752716"></a><a name="p21892752716"></a>Select <strong id="b1585510514918"><a name="b1585510514918"></a><a name="b1585510514918"></a>Direct Connect</strong> when the servers that are connected to a VPC through Direct Connect or VPN in your data center need to access the Internet.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293981_row5681056546"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0127293981_p26815562411"><a name="en-us_topic_0127293981_p26815562411"></a><a name="en-us_topic_0127293981_p26815562411"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.4.1.2 "><p id="p10582494228"><a name="p10582494228"></a><a name="p10582494228"></a>Set this parameter only when you select <strong id="b6861131818378"><a name="b6861131818378"></a><a name="b6861131818378"></a>VPC</strong> for <strong id="b19861161873715"><a name="b19861161873715"></a><a name="b19861161873715"></a>Scenario</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.080000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p206811656248"><a name="en-us_topic_0127293981_p206811656248"></a><a name="en-us_topic_0127293981_p206811656248"></a>Specifies the method used by servers to access the Internet.</p>
    <p id="p12207182812381"><a name="p12207182812381"></a><a name="p12207182812381"></a>Select <strong id="b23886225149"><a name="b23886225149"></a><a name="b23886225149"></a>Subnet</strong> when all servers in a subnet in a VPC need to access the Internet through the SNAT rule.</p>
    <p id="p18916248300"><a name="p18916248300"></a><a name="p18916248300"></a>Select <strong>Custom</strong> when specified servers in a subnet in a VPC need to access the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293981_row3209331417597"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0127293981_p4942162717597"><a name="en-us_topic_0127293981_p4942162717597"></a><a name="en-us_topic_0127293981_p4942162717597"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.4.1.2 "><p id="p360149192215"><a name="p360149192215"></a><a name="p360149192215"></a>Set this parameter when you select <strong id="b599520265423"><a name="b599520265423"></a><a name="b599520265423"></a>VPC</strong> for <strong id="b199672624211"><a name="b199672624211"></a><a name="b199672624211"></a>Scenario</strong>, and <strong id="b14997192634214"><a name="b14997192634214"></a><a name="b14997192634214"></a>Subnet</strong> for <strong id="b89971426144218"><a name="b89971426144218"></a><a name="b89971426144218"></a>Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.080000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p4372884917597"><a name="en-us_topic_0127293981_p4372884917597"></a><a name="en-us_topic_0127293981_p4372884917597"></a>Specifies the subnet in which servers can access the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0127293981_row5801532217597"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.4.1.1 "><p id="p02871145345"><a name="p02871145345"></a><a name="p02871145345"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.4.1.2 "><a name="ul12621049122212"></a><a name="ul12621049122212"></a><ul id="ul12621049122212"><li>Set this parameter when you select <strong id="b206221851211"><a name="b206221851211"></a><a name="b206221851211"></a>VPC</strong> for <strong id="b1831610531512"><a name="b1831610531512"></a><a name="b1831610531512"></a>Scenario</strong>.</li><li>Set this parameter when you select <strong id="b7732516217"><a name="b7732516217"></a><a name="b7732516217"></a>Direct Connect</strong> for <strong id="b825713122212"><a name="b825713122212"></a><a name="b825713122212"></a>Scenario</strong>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="51.080000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p94462428451"><a name="en-us_topic_0127293981_p94462428451"></a><a name="en-us_topic_0127293981_p94462428451"></a>Specifies the public IP address used for accessing the Internet.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b2212415151014"><a name="b2212415151014"></a><a name="b2212415151014"></a>Port Type</strong> set to <strong id="b17213181521014"><a name="b17213181521014"></a><a name="b17213181521014"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    >![](/images/icon-note.gif) **NOTE:**   
    >You can add multiple SNAT rules for a NAT gateway to suite your service requirements.  


