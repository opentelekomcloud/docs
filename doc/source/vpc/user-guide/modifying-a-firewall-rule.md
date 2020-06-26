# Modifying a Firewall Rule<a name="vpc_acl_0005"></a>

## Scenarios<a name="section66699152161428"></a>

Modify an inbound or outbound firewall rule based on your network security requirements.

## Procedure<a name="section25103352161542"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall in the right pane, and click the firewall name to switch to the page showing details of that particular firewall.
6.  On the  **Inbound Rules**  or  **Outbound Rules**  tab, locate the target rule and click  **Modify**  in the  **Operation**  column. In the displayed dialog box, configure parameters as prompted.  [Table 1](#table59686157164549)  lists the parameters to be configured.

    **Figure  1**  Modify Rule<a name="fig4739105024618"></a>  
    ![](figures/modify-rule.png "modify-rule")

    **Table  1**  Parameter description

    <a name="table59686157164549"></a>
    <table><thead align="left"><tr id="en-us_topic_0051746702_row245764813417"><th class="cellrowborder" valign="top" width="19.89%" id="mcps1.2.4.1.1"><p id="en-us_topic_0051746702_p14456948183410"><a name="en-us_topic_0051746702_p14456948183410"></a><a name="en-us_topic_0051746702_p14456948183410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.769999999999996%" id="mcps1.2.4.1.2"><p id="en-us_topic_0051746702_p2456154812347"><a name="en-us_topic_0051746702_p2456154812347"></a><a name="en-us_topic_0051746702_p2456154812347"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.34%" id="mcps1.2.4.1.3"><p id="en-us_topic_0051746702_p1645724863410"><a name="en-us_topic_0051746702_p1645724863410"></a><a name="en-us_topic_0051746702_p1645724863410"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0051746702_row184641148133419"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p6457134819341"><a name="en-us_topic_0051746702_p6457134819341"></a><a name="en-us_topic_0051746702_p6457134819341"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p20487105491017"><a name="en-us_topic_0051746702_p20487105491017"></a><a name="en-us_topic_0051746702_p20487105491017"></a>Specifies the action in the firewall. This parameter is mandatory. You can select a value from the drop-down list. Currently, the value can be <strong id="en-us_topic_0051746702_b67011216115318"><a name="en-us_topic_0051746702_b67011216115318"></a><a name="en-us_topic_0051746702_b67011216115318"></a>Permit</strong> or <strong id="en-us_topic_0051746702_b15652620205314"><a name="en-us_topic_0051746702_b15652620205314"></a><a name="en-us_topic_0051746702_b15652620205314"></a>Deny</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p1446404843410"><a name="en-us_topic_0051746702_p1446404843410"></a><a name="en-us_topic_0051746702_p1446404843410"></a>Permit</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row0466148153411"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p246464863416"><a name="en-us_topic_0051746702_p246464863416"></a><a name="en-us_topic_0051746702_p246464863416"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p124661748163411"><a name="en-us_topic_0051746702_p124661748163411"></a><a name="en-us_topic_0051746702_p124661748163411"></a>Specifies the protocol supported by the firewall. This parameter is mandatory. You can select a value from the drop-down list. The value can be <strong id="en-us_topic_0051746702_b93582612531"><a name="en-us_topic_0051746702_b93582612531"></a><a name="en-us_topic_0051746702_b93582612531"></a>TCP</strong>, <strong id="en-us_topic_0051746702_b537626155316"><a name="en-us_topic_0051746702_b537626155316"></a><a name="en-us_topic_0051746702_b537626155316"></a>UDP</strong>, <strong id="en-us_topic_0051746702_b198561298545"><a name="en-us_topic_0051746702_b198561298545"></a><a name="en-us_topic_0051746702_b198561298545"></a>All</strong>, or <strong id="en-us_topic_0051746702_b43815260538"><a name="en-us_topic_0051746702_b43815260538"></a><a name="en-us_topic_0051746702_b43815260538"></a>ICMP</strong>. If <strong id="en-us_topic_0051746702_b2381826165313"><a name="en-us_topic_0051746702_b2381826165313"></a><a name="en-us_topic_0051746702_b2381826165313"></a>ICMP</strong> or <strong id="en-us_topic_0051746702_b153992685310"><a name="en-us_topic_0051746702_b153992685310"></a><a name="en-us_topic_0051746702_b153992685310"></a>All</strong> is selected, you do not need to specify port information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p114661548163415"><a name="en-us_topic_0051746702_p114661548163415"></a><a name="en-us_topic_0051746702_p114661548163415"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row7466248203412"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p1546611481340"><a name="en-us_topic_0051746702_p1546611481340"></a><a name="en-us_topic_0051746702_p1546611481340"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p1446616487341"><a name="en-us_topic_0051746702_p1446616487341"></a><a name="en-us_topic_0051746702_p1446616487341"></a>Specifies the source IP address that the traffic is allowed from.</p>
    <p id="en-us_topic_0051746702_p144661848153418"><a name="en-us_topic_0051746702_p144661848153418"></a><a name="en-us_topic_0051746702_p144661848153418"></a>The default value is <strong id="en-us_topic_0051746702_b842352706231637"><a name="en-us_topic_0051746702_b842352706231637"></a><a name="en-us_topic_0051746702_b842352706231637"></a>0.0.0.0/0</strong>, which indicates that traffic from all IP addresses is allowed.</p>
    <p id="en-us_topic_0051746702_p64667482345"><a name="en-us_topic_0051746702_p64667482345"></a><a name="en-us_topic_0051746702_p64667482345"></a>For example:</p>
    <p id="en-us_topic_0051746702_p1646613483344"><a name="en-us_topic_0051746702_p1646613483344"></a><a name="en-us_topic_0051746702_p1646613483344"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="en-us_topic_0051746702_p2466154823416"><a name="en-us_topic_0051746702_p2466154823416"></a><a name="en-us_topic_0051746702_p2466154823416"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="en-us_topic_0051746702_p4466194820347"><a name="en-us_topic_0051746702_p4466194820347"></a><a name="en-us_topic_0051746702_p4466194820347"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p12466164823419"><a name="en-us_topic_0051746702_p12466164823419"></a><a name="en-us_topic_0051746702_p12466164823419"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row446624812347"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p846664863418"><a name="en-us_topic_0051746702_p846664863418"></a><a name="en-us_topic_0051746702_p846664863418"></a>Source Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p6466104812345"><a name="en-us_topic_0051746702_p6466104812345"></a><a name="en-us_topic_0051746702_p6466104812345"></a>Specifies the source port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-). For example, <strong id="en-us_topic_0051746702_b51691441981"><a name="en-us_topic_0051746702_b51691441981"></a><a name="en-us_topic_0051746702_b51691441981"></a>1-100</strong>.</p>
    <p id="en-us_topic_0051746702_p124661448153411"><a name="en-us_topic_0051746702_p124661448153411"></a><a name="en-us_topic_0051746702_p124661448153411"></a>You must specify this parameter if <strong>TCP</strong> or <strong>UDP</strong> is selected for <strong>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p6466104818341"><a name="en-us_topic_0051746702_p6466104818341"></a><a name="en-us_topic_0051746702_p6466104818341"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row346764883414"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p046719484349"><a name="en-us_topic_0051746702_p046719484349"></a><a name="en-us_topic_0051746702_p046719484349"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p046712485344"><a name="en-us_topic_0051746702_p046712485344"></a><a name="en-us_topic_0051746702_p046712485344"></a>Specifies the destination IP address to which the traffic is allowed.</p>
    <p id="en-us_topic_0051746702_p10467174817345"><a name="en-us_topic_0051746702_p10467174817345"></a><a name="en-us_topic_0051746702_p10467174817345"></a>The default value is <strong id="en-us_topic_0051746702_b842352706231637_1"><a name="en-us_topic_0051746702_b842352706231637_1"></a><a name="en-us_topic_0051746702_b842352706231637_1"></a>0.0.0.0/0</strong>, which indicates that traffic to all IP addresses is allowed.</p>
    <p id="en-us_topic_0051746702_p3467104893419"><a name="en-us_topic_0051746702_p3467104893419"></a><a name="en-us_topic_0051746702_p3467104893419"></a>For example:</p>
    <p id="en-us_topic_0051746702_p64671748143413"><a name="en-us_topic_0051746702_p64671748143413"></a><a name="en-us_topic_0051746702_p64671748143413"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="en-us_topic_0051746702_p124671648113415"><a name="en-us_topic_0051746702_p124671648113415"></a><a name="en-us_topic_0051746702_p124671648113415"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="en-us_topic_0051746702_p94671448203411"><a name="en-us_topic_0051746702_p94671448203411"></a><a name="en-us_topic_0051746702_p94671448203411"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p104679481342"><a name="en-us_topic_0051746702_p104679481342"></a><a name="en-us_topic_0051746702_p104679481342"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row646834823419"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p1946720489346"><a name="en-us_topic_0051746702_p1946720489346"></a><a name="en-us_topic_0051746702_p1946720489346"></a>Destination Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p646734819340"><a name="en-us_topic_0051746702_p646734819340"></a><a name="en-us_topic_0051746702_p646734819340"></a>Specifies the destination port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-). For example, <strong id="en-us_topic_0051746702_b15828242172719"><a name="en-us_topic_0051746702_b15828242172719"></a><a name="en-us_topic_0051746702_b15828242172719"></a>1-100</strong>.</p>
    <p id="en-us_topic_0051746702_p124671748153410"><a name="en-us_topic_0051746702_p124671748153410"></a><a name="en-us_topic_0051746702_p124671748153410"></a>You must specify this parameter if <strong>TCP</strong> or <strong>UDP</strong> is selected for <strong>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p346854811345"><a name="en-us_topic_0051746702_p346854811345"></a><a name="en-us_topic_0051746702_p346854811345"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051746702_row2641164215415"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0051746702_p2641134254111"><a name="en-us_topic_0051746702_p2641134254111"></a><a name="en-us_topic_0051746702_p2641134254111"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0051746702_p55384117316"><a name="en-us_topic_0051746702_p55384117316"></a><a name="en-us_topic_0051746702_p55384117316"></a>Provides supplementary information about the firewall rule. This parameter is optional.</p>
    <p id="en-us_topic_0051746702_p185324110315"><a name="en-us_topic_0051746702_p185324110315"></a><a name="en-us_topic_0051746702_p185324110315"></a>The firewall rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0051746702_p1364284284110"><a name="en-us_topic_0051746702_p1364284284110"></a><a name="en-us_topic_0051746702_p1364284284110"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    The firewall rule is modified. The procedure for modifying an outbound firewall rule is the same as that for modifying an inbound rule.


