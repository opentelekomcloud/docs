# Configuring Security Group Rules<a name="EN-US_TOPIC_0030878383"></a>

## Scenarios<a name="en-us_topic_0029320966_section35030493215147"></a>

Similar to firewall, a security group is a logical group used to control network access. You can define access rules for a security group to protect the ECSs that are added to this security group.

-   Inbound: Inbound rules allow external network traffic to be sent to the ECSs in the security group.
-   Outbound: Outbound rules allow network traffic from the ECSs in the security group to be sent out of the security group.

For details about the default security group rules, see  _Virtual Private Cloud User Guide_. For details about configuration examples for security group rules, see  [Security Group Configuration Examples](security-group-configuration-examples.md).

## Procedure<a name="en-us_topic_0029320966_section40712064223843"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **Security Groups**  tab and view security group rules.
6.  Click the security group ID.

    The system automatically switches to the  **Security Group**  page.

7.  On the inbound rule tab, click  **Add Rule**. In the displayed dialog box, set required parameters to add an inbound rule.

    You can click  **+**  to add more inbound rules.

    **Figure  1**  Add Inbound Rule<a name="en-us_topic_0118534005_fig3472133015819"></a>  
    ![](figures/add-inbound-rule.png "add-inbound-rule")

    **Table  1**  Inbound rule parameter description

    <a name="en-us_topic_0118534005_table111445216564"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534005_row1811565205613"><th class="cellrowborder" valign="top" width="12.55%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118534005_p51151452125620"><a name="en-us_topic_0118534005_p51151452125620"></a><a name="en-us_topic_0118534005_p51151452125620"></a><strong id="en-us_topic_0118534005_b2131889160"><a name="en-us_topic_0118534005_b2131889160"></a><a name="en-us_topic_0118534005_b2131889160"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.45%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118534005_p5115552175613"><a name="en-us_topic_0118534005_p5115552175613"></a><a name="en-us_topic_0118534005_p5115552175613"></a><strong id="en-us_topic_0118534005_b2109380569"><a name="en-us_topic_0118534005_b2109380569"></a><a name="en-us_topic_0118534005_b2109380569"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118534005_p711565219563"><a name="en-us_topic_0118534005_p711565219563"></a><a name="en-us_topic_0118534005_p711565219563"></a><strong id="en-us_topic_0118534005_b984193573219"><a name="en-us_topic_0118534005_b984193573219"></a><a name="en-us_topic_0118534005_b984193573219"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534005_row9115105219562"><td class="cellrowborder" rowspan="2" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p151157525565"><a name="en-us_topic_0118534005_p151157525565"></a><a name="en-us_topic_0118534005_p151157525565"></a>Protocol &amp; Port</p>
    <p id="en-us_topic_0118534005_p3510193211510"><a name="en-us_topic_0118534005_p3510193211510"></a><a name="en-us_topic_0118534005_p3510193211510"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1711515526562"><a name="en-us_topic_0118534005_p1711515526562"></a><a name="en-us_topic_0118534005_p1711515526562"></a>Specifies the network protocol. Currently, the value can be <strong id="en-us_topic_0118534005_b63642068"><a name="en-us_topic_0118534005_b63642068"></a><a name="en-us_topic_0118534005_b63642068"></a>All</strong>, <strong id="en-us_topic_0118534005_b1275884042"><a name="en-us_topic_0118534005_b1275884042"></a><a name="en-us_topic_0118534005_b1275884042"></a>TCP</strong>, <strong id="en-us_topic_0118534005_b873919964"><a name="en-us_topic_0118534005_b873919964"></a><a name="en-us_topic_0118534005_b873919964"></a>UDP</strong>, <strong id="en-us_topic_0118534005_b1624173192"><a name="en-us_topic_0118534005_b1624173192"></a><a name="en-us_topic_0118534005_b1624173192"></a>ICMP</strong>, <strong id="en-us_topic_0118534005_b104287139"><a name="en-us_topic_0118534005_b104287139"></a><a name="en-us_topic_0118534005_b104287139"></a>GRE</strong>, or others.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p193908441914"><a name="en-us_topic_0118534005_p193908441914"></a><a name="en-us_topic_0118534005_p193908441914"></a>Custom TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row6510532121511"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p4115175245613"><a name="en-us_topic_0118534005_p4115175245613"></a><a name="en-us_topic_0118534005_p4115175245613"></a><strong id="en-us_topic_0118534005_b840131483114"><a name="en-us_topic_0118534005_b840131483114"></a><a name="en-us_topic_0118534005_b840131483114"></a>Port</strong>: specifies the port or port range over which the traffic can reach your ECS. Ports 1 to 65535 are all allowed. </p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1551023251511"><a name="en-us_topic_0118534005_p1551023251511"></a><a name="en-us_topic_0118534005_p1551023251511"></a>22, or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row511615528561"><td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p86899991813"><a name="en-us_topic_0118534005_p86899991813"></a><a name="en-us_topic_0118534005_p86899991813"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p18116175212564"><a name="en-us_topic_0118534005_p18116175212564"></a><a name="en-us_topic_0118534005_p18116175212564"></a><strong id="en-us_topic_0118534005_b18923132315592"><a name="en-us_topic_0118534005_b18923132315592"></a><a name="en-us_topic_0118534005_b18923132315592"></a>Source</strong>: specifies the source of the security group rule. The value can be another security group or a single IP address. For example:</p>
    <a name="en-us_topic_0118534005_ul12116352195619"></a><a name="en-us_topic_0118534005_ul12116352195619"></a><ul id="en-us_topic_0118534005_ul12116352195619"><li>xxx.xxx.xxx.xxx/32 (IPv4 address)</li><li>xxx.xxx.xxx.0/24 (subnet CIDR block)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p611613524569"><a name="en-us_topic_0118534005_p611613524569"></a><a name="en-us_topic_0118534005_p611613524569"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row111615525565"><td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p1711655217565"><a name="en-us_topic_0118534005_p1711655217565"></a><a name="en-us_topic_0118534005_p1711655217565"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1211611525564"><a name="en-us_topic_0118534005_p1211611525564"></a><a name="en-us_topic_0118534005_p1211611525564"></a>Provides supplementary information about the security group rule. This parameter is optional.</p>
    <p id="en-us_topic_0118534005_p6116175225613"><a name="en-us_topic_0118534005_p6116175225613"></a><a name="en-us_topic_0118534005_p6116175225613"></a>The security group rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p3116115216568"><a name="en-us_topic_0118534005_p3116115216568"></a><a name="en-us_topic_0118534005_p3116115216568"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  On the outbound rule tab, click  **Add Rule**. In the displayed dialog box, set required parameters to add an outbound rule.

    You can click  **+**  to add more outbound rules.

    **Figure  2**  Add Outbound Rule<a name="en-us_topic_0118534005_fig172021330144714"></a>  
    ![](figures/add-outbound-rule.png "add-outbound-rule")

    **Table  2**  Outbound rule parameter description

    <a name="en-us_topic_0118534005_table0614192319232"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534005_row19614623202312"><th class="cellrowborder" valign="top" width="12.55%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118534005_p361592319230"><a name="en-us_topic_0118534005_p361592319230"></a><a name="en-us_topic_0118534005_p361592319230"></a><strong id="en-us_topic_0118534005_b1246024759"><a name="en-us_topic_0118534005_b1246024759"></a><a name="en-us_topic_0118534005_b1246024759"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.45%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118534005_p1961514231232"><a name="en-us_topic_0118534005_p1961514231232"></a><a name="en-us_topic_0118534005_p1961514231232"></a><strong id="en-us_topic_0118534005_b392753994"><a name="en-us_topic_0118534005_b392753994"></a><a name="en-us_topic_0118534005_b392753994"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118534005_p1061552372311"><a name="en-us_topic_0118534005_p1061552372311"></a><a name="en-us_topic_0118534005_p1061552372311"></a><strong id="en-us_topic_0118534005_b78071625745"><a name="en-us_topic_0118534005_b78071625745"></a><a name="en-us_topic_0118534005_b78071625745"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534005_row76161523132311"><td class="cellrowborder" rowspan="2" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p1761652313238"><a name="en-us_topic_0118534005_p1761652313238"></a><a name="en-us_topic_0118534005_p1761652313238"></a>Protocol &amp; Port</p>
    <p id="en-us_topic_0118534005_p4616323182310"><a name="en-us_topic_0118534005_p4616323182310"></a><a name="en-us_topic_0118534005_p4616323182310"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1461632352313"><a name="en-us_topic_0118534005_p1461632352313"></a><a name="en-us_topic_0118534005_p1461632352313"></a>Specifies the network protocol. Currently, the value can be <strong id="en-us_topic_0118534005_b202822549"><a name="en-us_topic_0118534005_b202822549"></a><a name="en-us_topic_0118534005_b202822549"></a>All</strong>, <strong id="en-us_topic_0118534005_b2060632122"><a name="en-us_topic_0118534005_b2060632122"></a><a name="en-us_topic_0118534005_b2060632122"></a>TCP</strong>, <strong id="en-us_topic_0118534005_b1478300017"><a name="en-us_topic_0118534005_b1478300017"></a><a name="en-us_topic_0118534005_b1478300017"></a>UDP</strong>, <strong id="en-us_topic_0118534005_b1962364235"><a name="en-us_topic_0118534005_b1962364235"></a><a name="en-us_topic_0118534005_b1962364235"></a>ICMP</strong>, <strong id="en-us_topic_0118534005_b722142174"><a name="en-us_topic_0118534005_b722142174"></a><a name="en-us_topic_0118534005_b722142174"></a>GRE</strong>, or others.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p157082238193"><a name="en-us_topic_0118534005_p157082238193"></a><a name="en-us_topic_0118534005_p157082238193"></a>Custom TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row5616723112313"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p761613239235"><a name="en-us_topic_0118534005_p761613239235"></a><a name="en-us_topic_0118534005_p761613239235"></a><strong id="en-us_topic_0118534005_b1962587115"><a name="en-us_topic_0118534005_b1962587115"></a><a name="en-us_topic_0118534005_b1962587115"></a>Port</strong>: specifies the port or port range over which the traffic can leave your ECS. The value ranges from 1 to 65535. </p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p12616182311235"><a name="en-us_topic_0118534005_p12616182311235"></a><a name="en-us_topic_0118534005_p12616182311235"></a>22, or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row2617112315232"><td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p15617623172315"><a name="en-us_topic_0118534005_p15617623172315"></a><a name="en-us_topic_0118534005_p15617623172315"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p196171823152315"><a name="en-us_topic_0118534005_p196171823152315"></a><a name="en-us_topic_0118534005_p196171823152315"></a><strong id="en-us_topic_0118534005_b4110206531"><a name="en-us_topic_0118534005_b4110206531"></a><a name="en-us_topic_0118534005_b4110206531"></a>Source</strong>: specifies the source of the security group rule. The value can be another security group or a single IP address. For example:</p>
    <a name="en-us_topic_0118534005_ul16177237233"></a><a name="en-us_topic_0118534005_ul16177237233"></a><ul id="en-us_topic_0118534005_ul16177237233"><li>xxx.xxx.xxx.xxx/32 (IPv4 address)</li><li>xxx.xxx.xxx.0/24 (subnet CIDR block)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p4617102352310"><a name="en-us_topic_0118534005_p4617102352310"></a><a name="en-us_topic_0118534005_p4617102352310"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row196181723162317"><td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p2061811237237"><a name="en-us_topic_0118534005_p2061811237237"></a><a name="en-us_topic_0118534005_p2061811237237"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p0618182392312"><a name="en-us_topic_0118534005_p0618182392312"></a><a name="en-us_topic_0118534005_p0618182392312"></a>Provides supplementary information about the security group rule. This parameter is optional.</p>
    <p id="en-us_topic_0118534005_p16618823192317"><a name="en-us_topic_0118534005_p16618823192317"></a><a name="en-us_topic_0118534005_p16618823192317"></a>The security group rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p20618623202311"><a name="en-us_topic_0118534005_p20618623202311"></a><a name="en-us_topic_0118534005_p20618623202311"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **OK**  to complete the security rule configuration.

