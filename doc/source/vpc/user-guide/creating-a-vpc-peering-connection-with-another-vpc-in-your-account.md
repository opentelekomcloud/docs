# Creating a VPC Peering Connection with Another VPC in Your Account<a name="en-us_topic_0046655037"></a>

## Scenarios<a name="s15a6c19babf0488eba98096754d78b91"></a>

To create a VPC peering connection, first create a request to peer with another VPC. You can request a VPC peering connection with another VPC in your account, but the two VPCs must be in the same region. The system automatically accepts the request.

## Prerequisites<a name="section2622867121261"></a>

Two VPCs in the same region have been created.

## Creating a VPC Peering Connection<a name="section143383585438"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **VPC Peering**.
5.  In the right pane displayed, click  **Create VPC Peering Connection**.
6.  Configure parameters as prompted. You must select  **My account**  for  **Account**.  [Table 1](#table1215761020244)  lists the parameters to be configured.

    **Figure  1**  Create VPC Peering Connection<a name="fig51552010112410"></a>  
    ![](figures/create-vpc-peering-connection.png "create-vpc-peering-connection")

    **Table  1**  Parameter description

    <a name="table1215761020244"></a>
    <table><thead align="left"><tr id="row0156161072415"><th class="cellrowborder" valign="top" width="22.38223822382238%" id="mcps1.2.4.1.1"><p id="p915541019242"><a name="p915541019242"></a><a name="p915541019242"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.884388438843885%" id="mcps1.2.4.1.2"><p id="p1315515103244"><a name="p1315515103244"></a><a name="p1315515103244"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.73337333733373%" id="mcps1.2.4.1.3"><p id="p315671013242"><a name="p315671013242"></a><a name="p315671013242"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1115691072416"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p1156161072419"><a name="p1156161072419"></a><a name="p1156161072419"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p215615107243"><a name="p215615107243"></a><a name="p215615107243"></a>Specifies the name of the VPC peering connection.</p>
    <p id="p21567102249"><a name="p21567102249"></a><a name="p21567102249"></a>The name contains a maximum of 64 characters, which consist of letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p11156181013240"><a name="p11156181013240"></a><a name="p11156181013240"></a>peering-001</p>
    </td>
    </tr>
    <tr id="row141561910182419"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p11156121018242"><a name="p11156121018242"></a><a name="p11156121018242"></a>Local VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p1715615101242"><a name="p1715615101242"></a><a name="p1715615101242"></a>Specifies the local VPC. You can select one from the drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p161561107240"><a name="p161561107240"></a><a name="p161561107240"></a>vpc_002</p>
    </td>
    </tr>
    <tr id="row10156141092419"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p1615611072410"><a name="p1615611072410"></a><a name="p1615611072410"></a>Local VPC CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p1115691011249"><a name="p1115691011249"></a><a name="p1115691011249"></a>Specifies the CIDR block for the local VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p1815631042413"><a name="p1815631042413"></a><a name="p1815631042413"></a>192.168.10.0/24</p>
    </td>
    </tr>
    <tr id="row1015616108249"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p9156410182413"><a name="p9156410182413"></a><a name="p9156410182413"></a>Account</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p1415610102246"><a name="p1415610102246"></a><a name="p1415610102246"></a>Specifies the account to which the VPC to peer with belongs.</p>
    <a name="ul1815617101249"></a><a name="ul1815617101249"></a><ul id="ul1815617101249"><li><strong id="b8557122464410"><a name="b8557122464410"></a><a name="b8557122464410"></a>My account</strong>: The VPC peering connection will be created between two VPCs, in the same region, in your account.</li><li><strong id="b1881217261456"><a name="b1881217261456"></a><a name="b1881217261456"></a>Another account</strong>: The VPC peering connection will be created between your VPC and a VPC in another account, in the same region.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p31568105241"><a name="p31568105241"></a><a name="p31568105241"></a>My account</p>
    </td>
    </tr>
    <tr id="row4157151017243"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p915611062416"><a name="p915611062416"></a><a name="p915611062416"></a>Peer Project</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p615681052410"><a name="p615681052410"></a><a name="p615681052410"></a>Specifies the peer project name. The project name of the current project is used by default. </p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p18157210142410"><a name="p18157210142410"></a><a name="p18157210142410"></a>aaa</p>
    </td>
    </tr>
    <tr id="row101571310132410"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p61575109245"><a name="p61575109245"></a><a name="p61575109245"></a>Peer VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p81571310112418"><a name="p81571310112418"></a><a name="p81571310112418"></a>Specifies the peer VPC. You can select one from the drop-down list if the VPC peering connection is created between two VPCs in your own account.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p17157161010245"><a name="p17157161010245"></a><a name="p17157161010245"></a>vpc_fab1</p>
    </td>
    </tr>
    <tr id="row161571610102416"><td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.1 "><p id="p6157121062415"><a name="p6157121062415"></a><a name="p6157121062415"></a>Peer VPC CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.884388438843885%" headers="mcps1.2.4.1.2 "><p id="p1015791062420"><a name="p1015791062420"></a><a name="p1015791062420"></a>Specifies the CIDR block for the peer VPC.</p>
    <p id="p5157310192413"><a name="p5157310192413"></a><a name="p5157310192413"></a>The local and peer VPCs cannot have matching or overlapping CIDR blocks. Otherwise, the routes added for the VPC peering connection may not take effect.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.4.1.3 "><p id="p215771012417"><a name="p215771012417"></a><a name="p215771012417"></a>192.168.2.0/24</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

## Adding Routes for a VPC Peering Connection <a name="section22722059952"></a>

If you request a VPC peering connection with another VPC in your own account, the system automatically accepts the request. To enable communication between the two VPCs, you need to add local and peer routes for the VPC peering connection.

1.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
2.  In the navigation pane on the left, click  **VPC Peering**.
3.  Locate the target VPC peering connection in the connection list.

    **Figure  2**  VPC peering connection list<a name="fig1461994645319"></a>  
    ![](figures/vpc-peering-connection-list.png "vpc-peering-connection-list")

4.  Click the name of the VPC peering connection to switch to the page showing details about the connection.
5.  On the displayed page, click the  **Local Routes**  tab.
6.  In the displayed  **Local Routes**  area, click  **Add Local Route**. In the displayed dialog box, add a local route.  [Table 2](#table1626072032518)  lists the parameters to be configured.

    **Figure  3**  Add Local Route<a name="fig125922020257"></a>  
    ![](figures/add-local-route.png "add-local-route")

    **Table  2**  Route parameter description

    <a name="table1626072032518"></a>
    <table><thead align="left"><tr id="row1260520192515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p192601220202510"><a name="p192601220202510"></a><a name="p192601220202510"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p16260202012252"><a name="p16260202012252"></a><a name="p16260202012252"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p142601420172518"><a name="p142601420172518"></a><a name="p142601420172518"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row92601620142520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2026032017259"><a name="p2026032017259"></a><a name="p2026032017259"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1226011201251"><a name="p1226011201251"></a><a name="p1226011201251"></a>Specifies the destination address. Set it to the peer VPC or subnet CIDR block. </p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3260172012258"><a name="p3260172012258"></a><a name="p3260172012258"></a>192.168.2.0/24</p>
    </td>
    </tr>
    <tr id="row19260102012518"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p126012092511"><a name="p126012092511"></a><a name="p126012092511"></a>Next Hop</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4260220142514"><a name="p4260220142514"></a><a name="p4260220142514"></a>Specifies the next hop address. The default value is the VPC peering connection ID. Keep the default value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1260112010256"><a name="p1260112010256"></a><a name="p1260112010256"></a>d1a7863b-9d5e-4d27-8eaf-ab14d2a9148b</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**  to switch to the page showing the VPC peering connection details.
8.  On the displayed page, click the  **Peer Routes**  tab.
9.  In the displayed  **Peer Routes**  area, click  **Add Peer Route**  and add a route.
10. Click  **OK**  to add the route.

After a VPC peering connection is created, the two VPCs can communicate with each other through private IP addresses. You can run the  **ping**  command to check whether the two VPCs can communicate with each other. 

If two VPCs cannot communicate with each other, check the configuration by following the instructions provided in  [What Can I Do If VPCs in a VPC Peering Connection Cannot Communicate with Each Other?](what-can-i-do-if-vpcs-in-a-vpc-peering-connection-cannot-communicate-with-each-other.md).

