# \(Optional\) Step 4: Add an SNAT Rule<a name="nat_qs_0017"></a>

## Scenarios<a name="section18103401105119"></a>

After a NAT gateway is created, you can add SNAT rules for it. With SNAT rules, servers that are connected to a VPC through a direct connection can access the Internet by using a shared EIP.

An SNAT rule is configured for one CIDR block. If the Direct Connect connection of your side has multiple CIDR blocks, you can create several SNAT rules to make multiple servers share more EIPs.

## Prerequisites<a name="section27241609"></a>

A NAT gateway has been created.

## Procedure<a name="section43847892"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click the name of the NAT gateway for which you want to add the SNAT rule.
5.  On the  **SNAT Rules**  tab, click  **Add SNAT Rule**.

    **Figure  1**  Add SNAT Rule<a name="fig1386671012585"></a>  
    ![](figures/add-snat-rule-1.png "add-snat-rule-1")

6.  Specify the parameters as prompted. For details, see  [Table 1](#table4272024117597).

    **Table  1**  Parameter description

    <a name="table4272024117597"></a>
    <table><thead align="left"><tr id="row3248015417597"><th class="cellrowborder" valign="top" width="34.36%" id="mcps1.2.3.1.1"><p id="p1364683317597"><a name="p1364683317597"></a><a name="p1364683317597"></a><strong id="b16362172412415"><a name="b16362172412415"></a><a name="b16362172412415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.64%" id="mcps1.2.3.1.2"><p id="p1643000117597"><a name="p1643000117597"></a><a name="p1643000117597"></a><strong id="b13311726172418"><a name="b13311726172418"></a><a name="b13311726172418"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row144002379410"><td class="cellrowborder" valign="top" width="34.36%" headers="mcps1.2.3.1.1 "><p id="p2400173718417"><a name="p2400173718417"></a><a name="p2400173718417"></a>Scenario</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.64%" headers="mcps1.2.3.1.2 "><p id="p4320122201011"><a name="p4320122201011"></a><a name="p4320122201011"></a>Select <strong id="b59414103915"><a name="b59414103915"></a><a name="b59414103915"></a>Direct Connect</strong> when servers in your data center need to access the Internet.</p>
    <p id="p555513762014"><a name="p555513762014"></a><a name="p555513762014"></a>The servers in your data center that are connected to a VPC through Direct Connect or VPN can provide services for the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="row3209331417597"><td class="cellrowborder" valign="top" width="34.36%" headers="mcps1.2.3.1.1 "><p id="p1360713214112"><a name="p1360713214112"></a><a name="p1360713214112"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.64%" headers="mcps1.2.3.1.2 "><p id="p182455013518"><a name="p182455013518"></a><a name="p182455013518"></a>Specifies a CIDR block. Local servers whose IP address in this CIDR block can access the Internet through the SNAT rule.</p>
    </td>
    </tr>
    <tr id="row5801532217597"><td class="cellrowborder" valign="top" width="34.36%" headers="mcps1.2.3.1.1 "><p id="p162061317597"><a name="p162061317597"></a><a name="p162061317597"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.64%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0127293981_p94462428451"><a name="en-us_topic_0127293981_p94462428451"></a><a name="en-us_topic_0127293981_p94462428451"></a>Specifies the public IP address used for accessing the Internet.</p>
    <p id="en-us_topic_0127293981_p578114194614"><a name="en-us_topic_0127293981_p578114194614"></a><a name="en-us_topic_0127293981_p578114194614"></a>You can only select an EIP that has not been bound, has been bound to a DNAT rule with <strong id="b123425222077"><a name="b123425222077"></a><a name="b123425222077"></a>Port Type</strong> set to <strong id="b534318229713"><a name="b534318229713"></a><a name="b534318229713"></a>Specific port</strong> of the current NAT gateway, or has been bound to an SNAT rule of the current NAT gateway.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.
8.  View details in the SNAT rule list. If  **Status**  is  **Running**, the rule has been added successfully.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can add multiple SNAT rules for a NAT gateway to suite your service requirements.  


