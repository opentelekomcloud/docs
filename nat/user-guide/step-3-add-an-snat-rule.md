# Step 3: Add an SNAT Rule<a name="nat_qs_0004"></a>

## Scenarios<a name="section18103401105119"></a>

After the NAT gateway is created, you need to add SNAT rules. With an SNAT rule, your servers in a specified subnet can access the Internet by sharing the same EIP.

An SNAT rule is configured for one subnet or CIDR block. If there are multiple subnets or CIDR blocks in a VPC, you can create several SNAT rules to make multiple servers share more EIPs.

## **Prerequisites**<a name="section27241609"></a>

A NAT gateway has been created.

## Procedure<a name="section43847892"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the SNAT rule.
5.  On the  **SNAT Rules**  tab, click  **Add SNAT Rule**.

    **Figure  1**  Add SNAT Rule<a name="fig68741230114612"></a>  
    ![](figures/add-snat-rule.png "add-snat-rule")

6.  Set the parameters as prompted.  [Table 1](#table1966804261617)  describes the parameters.

    **Table  1**  Parameter description

    <a name="table1966804261617"></a>
    <table><thead align="left"><tr id="row17666124215168"><th class="cellrowborder" valign="top" width="16.06%" id="mcps1.2.4.1.1"><p id="p4666542201617"><a name="p4666542201617"></a><a name="p4666542201617"></a><strong id="b9372723144"><a name="b9372723144"></a><a name="b9372723144"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.529999999999998%" id="mcps1.2.4.1.2"><p id="p7378141183413"><a name="p7378141183413"></a><a name="p7378141183413"></a><strong id="b1387373883812"><a name="b1387373883812"></a><a name="b1387373883812"></a>Condition</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.410000000000004%" id="mcps1.2.4.1.3"><p id="p96661242171612"><a name="p96661242171612"></a><a name="p96661242171612"></a><strong id="b37983896144751"><a name="b37983896144751"></a><a name="b37983896144751"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row136661642201612"><td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.2.4.1.1 "><p id="p2666104217168"><a name="p2666104217168"></a><a name="p2666104217168"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p11378191114341"><a name="p11378191114341"></a><a name="p11378191114341"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.410000000000004%" headers="mcps1.2.4.1.3 "><p id="p41648253424"><a name="p41648253424"></a><a name="p41648253424"></a>Select <strong id="b200172584111"><a name="b200172584111"></a><a name="b200172584111"></a>VPC</strong> when your servers use the SNAT rule to access the Internet.</p>
    <p id="p816412534216"><a name="p816412534216"></a><a name="p816412534216"></a>This scenario involves servers in a VPC.</p>
    </td>
    </tr>
    <tr id="row16667842141618"><td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.2.4.1.1 "><p id="p3667154218162"><a name="p3667154218162"></a><a name="p3667154218162"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p437871115341"><a name="p437871115341"></a><a name="p437871115341"></a>Set this parameter only when you select <strong id="b1484925165412"><a name="b1484925165412"></a><a name="b1484925165412"></a>VPC</strong> for <strong id="b1784911525410"><a name="b1784911525410"></a><a name="b1784911525410"></a>Scenario</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.410000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p206811656248"><a name="en-us_topic_0127293981_p206811656248"></a><a name="en-us_topic_0127293981_p206811656248"></a>Specifies the method used by servers to access the Internet.</p>
    <p id="p04171762394"><a name="p04171762394"></a><a name="p04171762394"></a>Select <strong id="b422718237417"><a name="b422718237417"></a><a name="b422718237417"></a>Subnet</strong> when all servers in a subnet in a VPC need to access the Internet through the SNAT rule.</p>
    <p id="p12207182812381"><a name="p12207182812381"></a><a name="p12207182812381"></a>Select <strong id="b927672112512"><a name="b927672112512"></a><a name="b927672112512"></a>Custom</strong> when specified servers in a subnet in a VPC need to access the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="row1966711421161"><td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.2.4.1.1 "><p id="p206671421164"><a name="p206671421164"></a><a name="p206671421164"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p4378181113345"><a name="p4378181113345"></a><a name="p4378181113345"></a>Set this parameter when you select <strong id="b1957353411513"><a name="b1957353411513"></a><a name="b1957353411513"></a>VPC</strong> for <strong id="b757483418516"><a name="b757483418516"></a><a name="b757483418516"></a>Scenario</strong>, and <strong id="b2057417341955"><a name="b2057417341955"></a><a name="b2057417341955"></a>Subnet</strong> for <strong id="b18575234558"><a name="b18575234558"></a><a name="b18575234558"></a>Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.410000000000004%" headers="mcps1.2.4.1.3 "><p id="p360149192215"><a name="p360149192215"></a><a name="p360149192215"></a>Specifies the subnet in which servers can access the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="row2668542131619"><td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.2.4.1.1 "><p id="p16667942191611"><a name="p16667942191611"></a><a name="p16667942191611"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p18609184214014"><a name="p18609184214014"></a><a name="p18609184214014"></a>Set this parameter when you select <strong id="b1636714863918"><a name="b1636714863918"></a><a name="b1636714863918"></a>VPC</strong> for <strong id="b15203195143919"><a name="b15203195143919"></a><a name="b15203195143919"></a>Scenario</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.410000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0127293981_p94462428451"><a name="en-us_topic_0127293981_p94462428451"></a><a name="en-us_topic_0127293981_p94462428451"></a>Specifies the public IP address used for accessing the Internet.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b201941321181914"><a name="b201941321181914"></a><a name="b201941321181914"></a>Port Type</strong> set to <strong id="b13195142118198"><a name="b13195142118198"></a><a name="b13195142118198"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can add multiple SNAT rules for a NAT gateway to suite your service requirements.  


