# Security Group Configuration Examples<a name="EN-US_TOPIC_0140749075"></a>

## Case 1: BMSs in Different Security Groups Need to Communicate with Each Other Through an Internal Network<a name="section4744164052119"></a>

-   Scenario

    Resources on a BMS in a security group need to be copied to a BMS in another security group. The two BMSs are in the same VPC. Then, you can enable internal network communication between the two BMSs and copy resources.

-   Security group configuration

    In the same VPC, BMSs associated with the same security group can communicate with one another by default, and no additional configuration is required. However, BMSs in different security groups cannot communicate with each other by default. You must add security group rules to enable the BMSs to communicate with each other through an internal network.

    However, BMSs in different security groups cannot communicate with each other by default. You must add security group rules to enable the BMSs to communicate with each other through an internal network.

    <a name="table58694119222"></a>
    <table><thead align="left"><tr id="row1087231120228"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p38731117224"><a name="p38731117224"></a><a name="p38731117224"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p18874111152218"><a name="p18874111152218"></a><a name="p18874111152218"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p198751711112218"><a name="p198751711112218"></a><a name="p198751711112218"></a>Port Range/ICMP Protocol Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p987612111223"><a name="p987612111223"></a><a name="p987612111223"></a>Source</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row108771811102212"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1987841117228"><a name="p1987841117228"></a><a name="p1987841117228"></a>Protocol to be used for internal network communication. Supported values are <strong id="b842352706192848"><a name="b842352706192848"></a><a name="b842352706192848"></a>TCP</strong>, <strong id="b842352706192851"><a name="b842352706192851"></a><a name="b842352706192851"></a>UDP</strong>, <strong id="b842352706192855"><a name="b842352706192855"></a><a name="b842352706192855"></a>ICMP</strong>, and <strong id="b842352706192858"><a name="b842352706192858"></a><a name="b842352706192858"></a>All</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p78795112226"><a name="p78795112226"></a><a name="p78795112226"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p1988081172215"><a name="p1988081172215"></a><a name="p1988081172215"></a>Port number range or ICMP protocol type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p8881141152212"><a name="p8881141152212"></a><a name="p8881141152212"></a>IPv4 address, IPv4 CIDR block, or another security group ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Case 2: Only Specified IP Addresses Can Remotely Access BMSs in a Security Group<a name="section175551446182411"></a>

-   Scenario

    To prevent BMSs from being attacked, you can change the port number for remote login and configure security group rules that allow only specified IP addresses to remotely access the BMSs.

-   Security group configuration

    To allow IP address  **192.168.20.2**  to remotely access Linux BMSs in a security group over the SSH protocol and port 22, you can configure the following security group rule.

    <a name="table939592217292"></a>
    <table><thead align="left"><tr id="row14399112282913"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p640011222298"><a name="p640011222298"></a><a name="p640011222298"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p240119228296"><a name="p240119228296"></a><a name="p240119228296"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p1640292262913"><a name="p1640292262913"></a><a name="p1640292262913"></a>Port Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p144030224297"><a name="p144030224297"></a><a name="p144030224297"></a>Source</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row740482282910"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1740502282911"><a name="p1740502282911"></a><a name="p1740502282911"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p114068223298"><a name="p114068223298"></a><a name="p114068223298"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p20407172272919"><a name="p20407172272919"></a><a name="p20407172272919"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p144081922162913"><a name="p144081922162913"></a><a name="p144081922162913"></a>IPv4 address, IPv4 CIDR block, or another security group ID</p>
    <p id="p1914761211308"><a name="p1914761211308"></a><a name="p1914761211308"></a>For example, 192.168.20.2</p>
    </td>
    </tr>
    </tbody>
    </table>


## Case 3: Remotely Connecting to a Linux BMS Through SSH<a name="section598913913262"></a>

-   Scenario

    To remotely connect to a Linux BMS through SSH, you need to add a security group rule.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The default security group comes with this rule. If you use the default security group, you do not need to configure the rule again.  

-   Security group configuration

    <a name="table1385517143311"></a>
    <table><thead align="left"><tr id="row588161714332"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p16897172333"><a name="p16897172333"></a><a name="p16897172333"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p179081717336"><a name="p179081717336"></a><a name="p179081717336"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p109261743314"><a name="p109261743314"></a><a name="p109261743314"></a>Port Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p119341783314"><a name="p119341783314"></a><a name="p119341783314"></a>Source</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1994141717331"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p199691712336"><a name="p199691712336"></a><a name="p199691712336"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p11971117113318"><a name="p11971117113318"></a><a name="p11971117113318"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p1898117103317"><a name="p1898117103317"></a><a name="p1898117103317"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p129919171330"><a name="p129919171330"></a><a name="p129919171330"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Case 3: Remotely Connecting to a Windows BMS Through RDP<a name="section3923173412303"></a>

-   Scenario

    To remotely connect to a Windows BMS through RDP, you need to add a security group rule.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The default security group comes with this rule. If you use the default security group, you do not need to configure the rule again.  

-   Security group configuration

    <a name="table965119153116"></a>
    <table><thead align="left"><tr id="row365109123116"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p766109193116"><a name="p766109193116"></a><a name="p766109193116"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p13661295317"><a name="p13661295317"></a><a name="p13661295317"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p156611913114"><a name="p156611913114"></a><a name="p156611913114"></a>Port Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p76610953113"><a name="p76610953113"></a><a name="p76610953113"></a>Source</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56609143110"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p36629143110"><a name="p36629143110"></a><a name="p36629143110"></a>RDP (3389)</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p116609143118"><a name="p116609143118"></a><a name="p116609143118"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p8664911310"><a name="p8664911310"></a><a name="p8664911310"></a>3389</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p4661496310"><a name="p4661496310"></a><a name="p4661496310"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Case 5: Pinging a BMS from the Internet<a name="section136661726193213"></a>

-   Scenario

    To ping BMSs from each other to check connectivity, you need to add a security group rule.

-   Security group configuration

    <a name="table16931175453217"></a>
    <table><thead align="left"><tr id="row199311654123217"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p593175443218"><a name="p593175443218"></a><a name="p593175443218"></a>Protocol</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p3931175418326"><a name="p3931175418326"></a><a name="p3931175418326"></a>Direction</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p15931185417321"><a name="p15931185417321"></a><a name="p15931185417321"></a>Port Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p17931654113219"><a name="p17931654113219"></a><a name="p17931654113219"></a>Source</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3931354103218"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p10931205413321"><a name="p10931205413321"></a><a name="p10931205413321"></a>ICMP</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p15931175403219"><a name="p15931175403219"></a><a name="p15931175403219"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p093195483219"><a name="p093195483219"></a><a name="p093195483219"></a>All</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p15931175493216"><a name="p15931175493216"></a><a name="p15931175493216"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


