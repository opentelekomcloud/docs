# Adding Security Group Rules<a name="EN-US_TOPIC_0053536889"></a>

## Scenarios<a name="section5621376572"></a>

The default security group rule allows all outgoing data packets. BMSs in a security group can access each other without the need to add access rules. After a security group is created, you can create different access rules for the security group to protect the BMSs that are added to this security group.

>![](/images/icon-note.gif) **NOTE:**   
>You can add only one security group when creating a BMS. After the BMS is created, you can modify the security group of each NIC on the BMS details page.  

## Suggestions<a name="section1129171522614"></a>

-   When adding a security group rule for a BMS, grant the minimum permissions possible:
    -   Enable specific ports rather than a port range, for example, port 80.
    -   Be cautious to authorize source address 0.0.0.0/0 \(entire network segment\).

-   You are not advised to use one security group to manage all applications because isolation requirements for different layers vary.
-   Configuring a security group for each BMS is unnecessary. Instead, you can add BMSs with the same security protection requirements to the same security group.
-   Simple security group rules are recommended. For example, if you add a BMS to multiple security groups, the BMS may comply with hundreds of security group rules, and a change to any rule may cause network disconnection for the BMS.

## Procedure<a name="section10722192617297"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.
3.  In the BMS list, click the name of the BMS whose security group rules you want to modify.

    The page showing details of the BMS is displayed.

4.  Click the  **Security Groups**  tab and then  ![](figures/5-3.png)  to view security group rules.
5.  Click the security group ID.

    The system automatically switches to the  **Security Group**  page.

6.  Click  **Manage Rule**  in the  **Operation**  column. On the security group details page, add a rule.

    Value  **Inbound**  indicates that traffic enters the security group, and value  **Outbound**  indicates that traffic leaves the security group.

    **Table  1**  Parameter description

    <a name="table335513383514"></a>
    <table><thead align="left"><tr id="row203581133123514"><th class="cellrowborder" valign="top" width="29.439999999999998%" id="mcps1.2.4.1.1"><p id="p6359123319355"><a name="p6359123319355"></a><a name="p6359123319355"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.459999999999994%" id="mcps1.2.4.1.2"><p id="p03602336359"><a name="p03602336359"></a><a name="p03602336359"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.1%" id="mcps1.2.4.1.3"><p id="p536113334353"><a name="p536113334353"></a><a name="p536113334353"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row73621433103510"><td class="cellrowborder" valign="top" width="29.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p1236312336353"><a name="p1236312336353"></a><a name="p1236312336353"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.2 "><p id="p193631337352"><a name="p193631337352"></a><a name="p193631337352"></a>Specifies the network protocol for which the security group rule takes effect. The value can be <strong id="b84235270613479"><a name="b84235270613479"></a><a name="b84235270613479"></a>TCP</strong>, <strong id="b842352706134713"><a name="b842352706134713"></a><a name="b842352706134713"></a>UDP</strong>, <strong id="b842352706134716"><a name="b842352706134716"></a><a name="b842352706134716"></a>ICMP</strong>, <strong id="b842352706134721"><a name="b842352706134721"></a><a name="b842352706134721"></a>HTTP</strong>, or others.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.1%" headers="mcps1.2.4.1.3 "><p id="p14364833153520"><a name="p14364833153520"></a><a name="p14364833153520"></a>TCP</p>
    </td>
    </tr>
    <tr id="row123671533143517"><td class="cellrowborder" valign="top" width="29.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p8367133123514"><a name="p8367133123514"></a><a name="p8367133123514"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.2 "><p id="p2367153383514"><a name="p2367153383514"></a><a name="p2367153383514"></a>Specifies the port or port range for which the security group rule takes effect. The value ranges from <strong id="b842352706135645"><a name="b842352706135645"></a><a name="b842352706135645"></a>0</strong> to <strong id="b842352706135649"><a name="b842352706135649"></a><a name="b842352706135649"></a>65535</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.1%" headers="mcps1.2.4.1.3 "><p id="p1536873320355"><a name="p1536873320355"></a><a name="p1536873320355"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="row2368183363513"><td class="cellrowborder" valign="top" width="29.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p1036913339351"><a name="p1036913339351"></a><a name="p1036913339351"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.2 "><p id="p108388761418"><a name="p108388761418"></a><a name="p108388761418"></a>Specifies the traffic source (inbound rule). This parameter is required for an inbound rule.</p>
    <p id="p5369143343516"><a name="p5369143343516"></a><a name="p5369143343516"></a>The value can be an IP address or a security group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.1%" headers="mcps1.2.4.1.3 "><p id="p537013313356"><a name="p537013313356"></a><a name="p537013313356"></a>0.0.0.0/0</p>
    <p id="p14371133333513"><a name="p14371133333513"></a><a name="p14371133333513"></a>default</p>
    </td>
    </tr>
    <tr id="row337112338359"><td class="cellrowborder" valign="top" width="29.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p113725338352"><a name="p113725338352"></a><a name="p113725338352"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.2 "><p id="p8389166121417"><a name="p8389166121417"></a><a name="p8389166121417"></a>Specifies the traffic destination (outbound rule). This parameter is required for an outbound rule.</p>
    <p id="p137316337354"><a name="p137316337354"></a><a name="p137316337354"></a>The value can be an IP address or a security group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.1%" headers="mcps1.2.4.1.3 "><p id="p937418336358"><a name="p937418336358"></a><a name="p937418336358"></a>0.0.0.0/0</p>
    <p id="p43759338358"><a name="p43759338358"></a><a name="p43759338358"></a>default</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >The default source IP address  **0.0.0.0/0**  indicates that all IP addresses can access BMSs in the security group.  


