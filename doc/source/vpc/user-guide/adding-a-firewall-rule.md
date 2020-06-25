# Adding a Firewall Rule<a name="en-us_topic_0051746702"></a>

## Scenarios<a name="section66699152161428"></a>

Add an inbound or outbound firewall rule based on your network security requirements.

## Procedure<a name="section25103352161542"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall in the right pane, and click the firewall name to switch to the page showing details of that particular firewall.
6.  On the  **Inbound Rules**  or  **Outbound Rules**  tab, click  **Add Rule**  to add an inbound or outbound rule.

    You can click  **+**  to add more rules.

    **Figure  1**  Add Inbound Rule<a name="fig1525416591394"></a>  
    ![](figures/add-inbound-rule-3.png "add-inbound-rule-3")

    **Table  1**  Parameter description

    <a name="table746894814342"></a>
    <table><thead align="left"><tr id="row245764813417"><th class="cellrowborder" valign="top" width="19.89%" id="mcps1.2.4.1.1"><p id="p14456948183410"><a name="p14456948183410"></a><a name="p14456948183410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.769999999999996%" id="mcps1.2.4.1.2"><p id="p2456154812347"><a name="p2456154812347"></a><a name="p2456154812347"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.34%" id="mcps1.2.4.1.3"><p id="p1645724863410"><a name="p1645724863410"></a><a name="p1645724863410"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row184641148133419"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p6457134819341"><a name="p6457134819341"></a><a name="p6457134819341"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p20487105491017"><a name="p20487105491017"></a><a name="p20487105491017"></a>Specifies the action in the firewall. This parameter is mandatory. You can select a value from the drop-down list. Currently, the value can be <strong id="b67011216115318"><a name="b67011216115318"></a><a name="b67011216115318"></a>Permit</strong> or <strong id="b15652620205314"><a name="b15652620205314"></a><a name="b15652620205314"></a>Deny</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p1446404843410"><a name="p1446404843410"></a><a name="p1446404843410"></a>Permit</p>
    </td>
    </tr>
    <tr id="row0466148153411"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p246464863416"><a name="p246464863416"></a><a name="p246464863416"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p124661748163411"><a name="p124661748163411"></a><a name="p124661748163411"></a>Specifies the protocol supported by the firewall. This parameter is mandatory. You can select a value from the drop-down list. The value can be <strong id="b93582612531"><a name="b93582612531"></a><a name="b93582612531"></a>TCP</strong>, <strong id="b537626155316"><a name="b537626155316"></a><a name="b537626155316"></a>UDP</strong>, <strong id="b198561298545"><a name="b198561298545"></a><a name="b198561298545"></a>All</strong>, or <strong id="b43815260538"><a name="b43815260538"></a><a name="b43815260538"></a>ICMP</strong>. If <strong id="b2381826165313"><a name="b2381826165313"></a><a name="b2381826165313"></a>ICMP</strong> or <strong id="b153992685310"><a name="b153992685310"></a><a name="b153992685310"></a>All</strong> is selected, you do not need to specify port information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p114661548163415"><a name="p114661548163415"></a><a name="p114661548163415"></a>TCP</p>
    </td>
    </tr>
    <tr id="row7466248203412"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p1546611481340"><a name="p1546611481340"></a><a name="p1546611481340"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p1446616487341"><a name="p1446616487341"></a><a name="p1446616487341"></a>Specifies the source IP address that the traffic is allowed from.</p>
    <p id="p144661848153418"><a name="p144661848153418"></a><a name="p144661848153418"></a>The default value is <strong id="b842352706231637"><a name="b842352706231637"></a><a name="b842352706231637"></a>0.0.0.0/0</strong>, which indicates that traffic from all IP addresses is allowed.</p>
    <p id="p64667482345"><a name="p64667482345"></a><a name="p64667482345"></a>For example:</p>
    <p id="p1646613483344"><a name="p1646613483344"></a><a name="p1646613483344"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="p2466154823416"><a name="p2466154823416"></a><a name="p2466154823416"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="p4466194820347"><a name="p4466194820347"></a><a name="p4466194820347"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p12466164823419"><a name="p12466164823419"></a><a name="p12466164823419"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row446624812347"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p846664863418"><a name="p846664863418"></a><a name="p846664863418"></a>Source Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p6466104812345"><a name="p6466104812345"></a><a name="p6466104812345"></a>Specifies the source port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-). For example, <strong id="b51691441981"><a name="b51691441981"></a><a name="b51691441981"></a>1-100</strong>.</p>
    <p id="p124661448153411"><a name="p124661448153411"></a><a name="p124661448153411"></a>You must specify this parameter if <strong>TCP</strong> or <strong>UDP</strong> is selected for <strong>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p6466104818341"><a name="p6466104818341"></a><a name="p6466104818341"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="row346764883414"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p046719484349"><a name="p046719484349"></a><a name="p046719484349"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p046712485344"><a name="p046712485344"></a><a name="p046712485344"></a>Specifies the destination IP address to which the traffic is allowed.</p>
    <p id="p10467174817345"><a name="p10467174817345"></a><a name="p10467174817345"></a>The default value is <strong id="b842352706231637_1"><a name="b842352706231637_1"></a><a name="b842352706231637_1"></a>0.0.0.0/0</strong>, which indicates that traffic to all IP addresses is allowed.</p>
    <p id="p3467104893419"><a name="p3467104893419"></a><a name="p3467104893419"></a>For example:</p>
    <p id="p64671748143413"><a name="p64671748143413"></a><a name="p64671748143413"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="p124671648113415"><a name="p124671648113415"></a><a name="p124671648113415"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="p94671448203411"><a name="p94671448203411"></a><a name="p94671448203411"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p104679481342"><a name="p104679481342"></a><a name="p104679481342"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row646834823419"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p1946720489346"><a name="p1946720489346"></a><a name="p1946720489346"></a>Destination Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p646734819340"><a name="p646734819340"></a><a name="p646734819340"></a>Specifies the destination port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-). For example, <strong id="b15828242172719"><a name="b15828242172719"></a><a name="b15828242172719"></a>1-100</strong>.</p>
    <p id="p124671748153410"><a name="p124671748153410"></a><a name="p124671748153410"></a>You must specify this parameter if <strong>TCP</strong> or <strong>UDP</strong> is selected for <strong>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p346854811345"><a name="p346854811345"></a><a name="p346854811345"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="row2641164215415"><td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p2641134254111"><a name="p2641134254111"></a><a name="p2641134254111"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.769999999999996%" headers="mcps1.2.4.1.2 "><p id="p55384117316"><a name="p55384117316"></a><a name="p55384117316"></a>Provides supplementary information about the firewall rule. This parameter is optional.</p>
    <p id="p185324110315"><a name="p185324110315"></a><a name="p185324110315"></a>The firewall rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.34%" headers="mcps1.2.4.1.3 "><p id="p1364284284110"><a name="p1364284284110"></a><a name="p1364284284110"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    The firewall rule is added. The procedure for adding an outbound rule is the same as that for adding an inbound rule.


