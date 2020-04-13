# Creating and Managing a User-defined Network ACL<a name="EN-US_TOPIC_0161727557"></a>

## Create a User-defined Network ACL<a name="section6127738485"></a>

Each user can create a maximum of 200 user-defined network ACLs by default.

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the  **User-defined Networks**  tab and click  **Create User-defined Network ACL**.
4.  Enter a name and description and click  **OK**.
5.  After the user-defined network ACL is created successfully, it is displayed in the list of user-defined network ACLs.

## Add an Inbound/Outbound Rule<a name="section128685618819"></a>

Add an inbound or outbound rule based on your network security requirements.

1.  On the BMS console, click the  **User-defined Networks**  tab and select  **User-defined Network ACLs**.
2.  Click the name of the target user-defined network ACL.
3.  On the  **Inbound Rules**  or  **Outbound Rules**  tab, click  **Add Rule**  to add an inbound or outbound rule.

    You can click  **+**  to add more rules.

    **Table  1**  Parameter description

    <a name="table53776177585"></a>
    <table><thead align="left"><tr id="row237820178581"><th class="cellrowborder" valign="top" width="18.61186118611861%" id="mcps1.2.4.1.1"><p id="p037821765815"><a name="p037821765815"></a><a name="p037821765815"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.88548854885489%" id="mcps1.2.4.1.2"><p id="p7378131710589"><a name="p7378131710589"></a><a name="p7378131710589"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.502650265026507%" id="mcps1.2.4.1.3"><p id="p18378317155811"><a name="p18378317155811"></a><a name="p18378317155811"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5378141755817"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p9378141711587"><a name="p9378141711587"></a><a name="p9378141711587"></a>Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p153781317195820"><a name="p153781317195820"></a><a name="p153781317195820"></a>Specifies the policy of the user-defined network ACL. This parameter is mandatory. You can select a value from the drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p20378131715582"><a name="p20378131715582"></a><a name="p20378131715582"></a>Permit</p>
    </td>
    </tr>
    <tr id="row113781117155817"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p43781617175815"><a name="p43781617175815"></a><a name="p43781617175815"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p1378161785817"><a name="p1378161785817"></a><a name="p1378161785817"></a>Specifies the protocol supported by the user-defined network ACL. This parameter is mandatory. You can select a value from the drop-down list. Currently, only <strong id="b16640142512192"><a name="b16640142512192"></a><a name="b16640142512192"></a>TCP</strong>, <strong id="b3177133214190"><a name="b3177133214190"></a><a name="b3177133214190"></a>UDP</strong>, <strong id="b311619360197"><a name="b311619360197"></a><a name="b311619360197"></a>ICMP</strong>, and <strong id="b63334101919"><a name="b63334101919"></a><a name="b63334101919"></a>All protocols</strong> are available. If you select <strong id="b374618119203"><a name="b374618119203"></a><a name="b374618119203"></a>ICMP</strong> or <strong id="b27461711182011"><a name="b27461711182011"></a><a name="b27461711182011"></a>All protocols</strong>, port information cannot be specified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p1137851713589"><a name="p1137851713589"></a><a name="p1137851713589"></a>TCP</p>
    </td>
    </tr>
    <tr id="row2037913177582"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p33796174585"><a name="p33796174585"></a><a name="p33796174585"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p73791117165811"><a name="p73791117165811"></a><a name="p73791117165811"></a>Specifies the source IP address from which the traffic is permitted.</p>
    <p id="p18556334549"><a name="p18556334549"></a><a name="p18556334549"></a>The default value is <strong id="b842352706231637"><a name="b842352706231637"></a><a name="b842352706231637"></a>0.0.0.0/0</strong>, which indicates that traffic from all IP addresses is permitted.</p>
    <p id="p1219645618419"><a name="p1219645618419"></a><a name="p1219645618419"></a>The followings are examples:</p>
    <p id="p25741611556"><a name="p25741611556"></a><a name="p25741611556"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="p66883501454"><a name="p66883501454"></a><a name="p66883501454"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="p18163114966"><a name="p18163114966"></a><a name="p18163114966"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p18379617125816"><a name="p18379617125816"></a><a name="p18379617125816"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row937971705818"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p837918178581"><a name="p837918178581"></a><a name="p837918178581"></a>Source Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p8379201712583"><a name="p8379201712583"></a><a name="p8379201712583"></a>Specifies the source port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-), such as <strong id="b1058816183218"><a name="b1058816183218"></a><a name="b1058816183218"></a>1-100</strong>.</p>
    <p id="p2193381275"><a name="p2193381275"></a><a name="p2193381275"></a>You must specify this parameter if <strong id="b564942115216"><a name="b564942115216"></a><a name="b564942115216"></a>TCP</strong> or <strong id="b1165082115217"><a name="b1165082115217"></a><a name="b1165082115217"></a>UDP</strong> is selected for <strong id="b7651162120211"><a name="b7651162120211"></a><a name="b7651162120211"></a>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p19379101712588"><a name="p19379101712588"></a><a name="p19379101712588"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="row737931711588"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p193791017185818"><a name="p193791017185818"></a><a name="p193791017185818"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p937916175584"><a name="p937916175584"></a><a name="p937916175584"></a>Specifies the destination IP address to which the traffic is permitted.</p>
    <p id="p12504122815917"><a name="p12504122815917"></a><a name="p12504122815917"></a>The default value is <strong id="b181491634122"><a name="b181491634122"></a><a name="b181491634122"></a>0.0.0.0/0</strong>, which indicates that traffic from all IP addresses is permitted.</p>
    <p id="p9504162811915"><a name="p9504162811915"></a><a name="p9504162811915"></a>The followings are examples:</p>
    <p id="p13504128394"><a name="p13504128394"></a><a name="p13504128394"></a>xxx.xxx.xxx.xxx/32 (IP address)</p>
    <p id="p85043281491"><a name="p85043281491"></a><a name="p85043281491"></a>xxx.xxx.xxx.0/24 (CIDR block)</p>
    <p id="p75047281491"><a name="p75047281491"></a><a name="p75047281491"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p18379917135812"><a name="p18379917135812"></a><a name="p18379917135812"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row20379171714584"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p10379117195819"><a name="p10379117195819"></a><a name="p10379117195819"></a>Destination Port Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p1166811291122"><a name="p1166811291122"></a><a name="p1166811291122"></a>Specifies the destination port number or port number range. The value ranges from 1 to 65535. For a port number range, enter two port numbers connected by a hyphen (-), such as <strong id="b25574547217"><a name="b25574547217"></a><a name="b25574547217"></a>1-100</strong>.</p>
    <p id="p1766811294124"><a name="p1766811294124"></a><a name="p1766811294124"></a>You must specify this parameter if <strong id="b135951757192118"><a name="b135951757192118"></a><a name="b135951757192118"></a>TCP</strong> or <strong id="b459695710213"><a name="b459695710213"></a><a name="b459695710213"></a>UDP</strong> is selected for <strong id="b175977578214"><a name="b175977578214"></a><a name="b175977578214"></a>Protocol</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p23791117145819"><a name="p23791117145819"></a><a name="p23791117145819"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="row173434529593"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.4.1.1 "><p id="p143437520593"><a name="p143437520593"></a><a name="p143437520593"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.88548854885489%" headers="mcps1.2.4.1.2 "><p id="p23432052145916"><a name="p23432052145916"></a><a name="p23432052145916"></a>Specifies description of the user-defined network ACL rule. This parameter is optional.</p>
    <p id="p1157715115137"><a name="p1157715115137"></a><a name="p1157715115137"></a>The description can contain a maximum of 255 characters and cannot contain angle brackets (&lt;) or (&gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.3 "><p id="p4343652185912"><a name="p4343652185912"></a><a name="p4343652185912"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

## Associate a User-defined Network ACL with a User-defined Subnet<a name="section113777104910"></a>

When you need to associate a user-defined network ACL with a user-defined subnet, go to the user-defined network ACL details page and click the  **User-defined Subnets**  tab. By default, a user-defined network ACL denies all inbound traffic to and outbound traffic from the associated subnet until you add rules.

1.  On the BMS console, click the  **User-defined Networks**  tab and select  **User-defined Network ACLs**.
2.  Click the name of the target user-defined network ACL.
3.  On the  **Associate Subnet**  page, click  **Associate**.
4.  Select the user-defined subnets you want to associate with the user-defined network ACL and click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >User-defined subnets that have already been associated with user-defined network ACLs will not be displayed on the page for you to select. One-click user-defined subnet association and disassociation are not supported. If you want to associate a user-defined subnet that has already been associated with another user-defined network ACL, you must first disassociate the subnet from the original network ACL.  


