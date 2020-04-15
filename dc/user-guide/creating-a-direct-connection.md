# Creating a Direct Connection<a name="EN-US_TOPIC_0085241899"></a>

## Scenarios<a name="section46753508488"></a>

Apply for a direct connection in the self-service mode to enable ECSs in your VPC to communicate with your data center or private network.

To request a direct connection, you need to create a connection, a virtual gateway, and a virtual interface.

In case the created single connection is faulty, you are recommended to create two connections to connect to different access locations. For details, see  [Redundant Connection Access](redundant-connection-access.md).

## Procedure<a name="section767665016484"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and a project.
3.  Under  **Network**, click  **Direct Connect**.
4.  In the navigation pane on the left of  **Network Console**, under  **Direct Connect**, choose  **Direct Connect**  \>  **Connections**.
5.  In the upper right corner of the  **Connections**  page, click  **Create Connection**.
6.  Follow the prompts to set the parameters.

    **Figure  1**  Create Connection<a name="fig1458719183201"></a>  
    ![](figures/create-connection.png "create-connection")

    **Table  1**  Connection parameters

    <a name="table27593495173236"></a>
    <table><thead align="left"><tr id="row20729321173236"><th class="cellrowborder" valign="top" width="22.869999999999997%" id="mcps1.2.4.1.1"><p id="p34545082173236"><a name="p34545082173236"></a><a name="p34545082173236"></a><strong id="b11294882173236"><a name="b11294882173236"></a><a name="b11294882173236"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.83%" id="mcps1.2.4.1.2"><p id="p17541007173236"><a name="p17541007173236"></a><a name="p17541007173236"></a><strong id="b46688243173236"><a name="b46688243173236"></a><a name="b46688243173236"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.3%" id="mcps1.2.4.1.3"><p id="p36710115173236"><a name="p36710115173236"></a><a name="p36710115173236"></a><strong id="b11535442173236"><a name="b11535442173236"></a><a name="b11535442173236"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12166232201514"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p12518193510150"><a name="p12518193510150"></a><a name="p12518193510150"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p216615323151"><a name="p216615323151"></a><a name="p216615323151"></a>Specifies the region in which the services will be handled.</p>
    <p id="p0956203916214"><a name="p0956203916214"></a><a name="p0956203916214"></a>If you already selected a region and a project on the management console, you do not need to select the region here.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p3166173219151"><a name="p3166173219151"></a><a name="p3166173219151"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row49534062173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p1353477173236"><a name="p1353477173236"></a><a name="p1353477173236"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p47160706173236"><a name="p47160706173236"></a><a name="p47160706173236"></a>Specifies the connection name.</p>
    <a name="ul24541438114618"></a><a name="ul24541438114618"></a><ul id="ul24541438114618"><li>It can contain 1 to 64 characters.</li><li>Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p61920864173236"><a name="p61920864173236"></a><a name="p61920864173236"></a>dc-123</p>
    </td>
    </tr>
    <tr id="row23456554173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p43153374173236"><a name="p43153374173236"></a><a name="p43153374173236"></a>Location</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p51861819173236"><a name="p51861819173236"></a><a name="p51861819173236"></a>Specifies the connection access location.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p40057802173236"><a name="p40057802173236"></a><a name="p40057802173236"></a>Biere</p>
    </td>
    </tr>
    <tr id="row13638511173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p94751753211"><a name="p94751753211"></a><a name="p94751753211"></a>Peering Position</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p1587345416113"><a name="p1587345416113"></a><a name="p1587345416113"></a>Specifies the physical location of the connection. The address is an identifier.</p>
    <a name="ul185801447194618"></a><a name="ul185801447194618"></a><ul id="ul185801447194618"><li>Only letters, digits, underscores (_), and hyphens (-) are allowed.</li><li>It can contain 0 to 64 characters.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p126841930191715"><a name="p126841930191715"></a><a name="p126841930191715"></a>Marderbug-DC01</p>
    </td>
    </tr>
    <tr id="row22377693173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p49688592173236"><a name="p49688592173236"></a><a name="p49688592173236"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p65352981173236"><a name="p65352981173236"></a><a name="p65352981173236"></a>Specifies the bandwidth size in the unit of Mbit/s.</p>
    <a name="ul1453982420460"></a><a name="ul1453982420460"></a><ul id="ul1453982420460"><li>You can select one of the bandwidths provided on the scroll bar by dragging it. Also, typing a value in the input field is allowed. It is automatically changed to the next allowed value shown on the slider bar.</li><li>The value ranges from 10 Mbit/s to 1000 Mbit/s.<p id="p1237135211518"><a name="p1237135211518"></a><a name="p1237135211518"></a>Possible values are as follows:</p>
    <p id="p575205414817"><a name="p575205414817"></a><a name="p575205414817"></a><strong id="b147662115517"><a name="b147662115517"></a><a name="b147662115517"></a>10</strong>, <strong id="b12794182614513"><a name="b12794182614513"></a><a name="b12794182614513"></a>50</strong>, <strong id="b14901192917510"><a name="b14901192917510"></a><a name="b14901192917510"></a>100</strong>, <strong id="b7229033355"><a name="b7229033355"></a><a name="b7229033355"></a>150</strong>, <strong id="b743013365511"><a name="b743013365511"></a><a name="b743013365511"></a>200</strong>, <strong id="b15319391952"><a name="b15319391952"></a><a name="b15319391952"></a>300</strong>, <strong id="b15713124319510"><a name="b15713124319510"></a><a name="b15713124319510"></a>400</strong>, <strong id="b1222911488513"><a name="b1222911488513"></a><a name="b1222911488513"></a>500</strong>, <strong id="b287816511551"><a name="b287816511551"></a><a name="b287816511551"></a>600</strong>, and <strong id="b082685420511"><a name="b082685420511"></a><a name="b082685420511"></a>1000</strong></p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p59100086173236"><a name="p59100086173236"></a><a name="p59100086173236"></a>100</p>
    </td>
    </tr>
    <tr id="row19093454173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p0744211838"><a name="p0744211838"></a><a name="p0744211838"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.83%" headers="mcps1.2.4.1.2 "><p id="p5884269173236"><a name="p5884269173236"></a><a name="p5884269173236"></a>Provides supplementary information about the connection.</p>
    <p id="p1470572016597"><a name="p1470572016597"></a><a name="p1470572016597"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.4.1.3 "><p id="p38575131177"><a name="p38575131177"></a><a name="p38575131177"></a>This is a connection.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **Create Now**.
8.  Check the connection details and click  **Submit**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Click  **Back to Connection List**  to view the created connections.  
    >-   After clicking  **Submit**, you will be automatically redirected to the connection list after a timeout.  

9.  In the navigation pane on the left, choose  **Direct Connect**  \>  **Virtual Gateways**.
10. In the upper right corner of the  **Virtual Gateways**  page, click  **Create Virtual Gateway**.
11. Follow the prompts to set the parameters.

    **Figure  2**  Create Virtual Gateway<a name="fig1256744491814"></a>  
    ![](figures/create-virtual-gateway.png "create-virtual-gateway")

    **Table  2**  Virtual gateway parameters

    <a name="table128947911279"></a>
    <table><thead align="left"><tr id="row1089915918275"><th class="cellrowborder" valign="top" width="20.560000000000002%" id="mcps1.2.4.1.1"><p id="p99001998272"><a name="p99001998272"></a><a name="p99001998272"></a><strong id="b1590149112720"><a name="b1590149112720"></a><a name="b1590149112720"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.97%" id="mcps1.2.4.1.2"><p id="p1190212912277"><a name="p1190212912277"></a><a name="p1190212912277"></a><strong id="b1290379112710"><a name="b1290379112710"></a><a name="b1290379112710"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.470000000000002%" id="mcps1.2.4.1.3"><p id="p690418916274"><a name="p690418916274"></a><a name="p690418916274"></a><strong id="b990559102710"><a name="b990559102710"></a><a name="b990559102710"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29061998270"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p79074992720"><a name="p79074992720"></a><a name="p79074992720"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.97%" headers="mcps1.2.4.1.2 "><p id="p490915911278"><a name="p490915911278"></a><a name="p490915911278"></a>Specifies the virtual gateway name.</p>
    <p id="p145122341482"><a name="p145122341482"></a><a name="p145122341482"></a>It can contain 1 to 64 characters.</p>
    <p id="p15542161014314"><a name="p15542161014314"></a><a name="p15542161014314"></a>Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.470000000000002%" headers="mcps1.2.4.1.3 "><p id="p179107911278"><a name="p179107911278"></a><a name="p179107911278"></a>vgw-123</p>
    </td>
    </tr>
    <tr id="row1891549102716"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p21073315466"><a name="p21073315466"></a><a name="p21073315466"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.97%" headers="mcps1.2.4.1.2 "><p id="p1191720972713"><a name="p1191720972713"></a><a name="p1191720972713"></a>Specifies the VPC where the virtual gateway resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.470000000000002%" headers="mcps1.2.4.1.3 "><p id="p13919696272"><a name="p13919696272"></a><a name="p13919696272"></a>VPC-001</p>
    </td>
    </tr>
    <tr id="row39191392274"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p4954513124619"><a name="p4954513124619"></a><a name="p4954513124619"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.97%" headers="mcps1.2.4.1.2 "><p id="p4927075995739"><a name="p4927075995739"></a><a name="p4927075995739"></a>Specifies the CIDR network segment of the VPC to be accessed by the direct connection.</p>
    <p id="p15921159162718"><a name="p15921159162718"></a><a name="p15921159162718"></a>You can add a maximum of 50 CIDR blocks. Each pair must be unique. Separate every two CIDR blocks with commas (,).</p>
    <p id="p932313289531"><a name="p932313289531"></a><a name="p932313289531"></a>A direct connection can access multiple VPCs. For details, see <a href="using-a-direct-connection-to-access-multiple-vpcs.md">Using a Direct Connection to Access Multiple VPCs</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.470000000000002%" headers="mcps1.2.4.1.3 "><p id="p13922179122714"><a name="p13922179122714"></a><a name="p13922179122714"></a>192.168.0.0/16</p>
    </td>
    </tr>
    <tr id="row20923797279"><td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.4.1.1 "><p id="p17924139182714"><a name="p17924139182714"></a><a name="p17924139182714"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.97%" headers="mcps1.2.4.1.2 "><p id="p139261696276"><a name="p139261696276"></a><a name="p139261696276"></a>Provides supplementary information about the virtual gateway.</p>
    <p id="p1184624595912"><a name="p1184624595912"></a><a name="p1184624595912"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.470000000000002%" headers="mcps1.2.4.1.3 "><p id="p5927294276"><a name="p5927294276"></a><a name="p5927294276"></a>This is a virtual gateway.</p>
    </td>
    </tr>
    </tbody>
    </table>

12. Click  **OK**.
13. In the navigation pane on the left, choose  **Direct Connect**  \>  **Virtual Interfaces**.
14. In the upper right corner of the  **Virtual Interfaces**  page, click  **Create Virtual Interface**.
15. Follow the prompts to set the parameters.

    **Figure  3**  Create Virtual Interface<a name="fig1674715216343"></a>  
    ![](figures/create-virtual-interface.png "create-virtual-interface")

    **Table  3**  Virtual interface parameters

    <a name="table54552924110"></a>
    <table><thead align="left"><tr id="row13422292417"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p94242918414"><a name="p94242918414"></a><a name="p94242918414"></a><strong id="b888875052618"><a name="b888875052618"></a><a name="b888875052618"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.230000000000004%" id="mcps1.2.4.1.2"><p id="p5422294415"><a name="p5422294415"></a><a name="p5422294415"></a><strong id="b2144328602"><a name="b2144328602"></a><a name="b2144328602"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.77%" id="mcps1.2.4.1.3"><p id="p1542182918410"><a name="p1542182918410"></a><a name="p1542182918410"></a><strong id="b1942109972"><a name="b1942109972"></a><a name="b1942109972"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1979213710268"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1279210717264"><a name="p1279210717264"></a><a name="p1279210717264"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p186332314269"><a name="p186332314269"></a><a name="p186332314269"></a>Specifies the region in which the services will be handled.</p>
    <p id="p1186317238265"><a name="p1186317238265"></a><a name="p1186317238265"></a>If you already selected a region and a project on the management console, you do not need to select the region here.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p1987052313264"><a name="p1987052313264"></a><a name="p1987052313264"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row1943142944110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18431229204113"><a name="p18431229204113"></a><a name="p18431229204113"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p134316296412"><a name="p134316296412"></a><a name="p134316296412"></a>Specifies the virtual interface name.</p>
    <p id="p11397624134"><a name="p11397624134"></a><a name="p11397624134"></a>It can contain 1 to 64 characters.</p>
    <p id="p1639982412316"><a name="p1639982412316"></a><a name="p1639982412316"></a>Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p94312293410"><a name="p94312293410"></a><a name="p94312293410"></a>vif-123</p>
    </td>
    </tr>
    <tr id="row943192918410"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p465610545143"><a name="p465610545143"></a><a name="p465610545143"></a>Connection</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p543172914112"><a name="p543172914112"></a><a name="p543172914112"></a>Specifies the connection to be associated.</p>
    <p id="p159711869418"><a name="p159711869418"></a><a name="p159711869418"></a>A connection can be associated with only one virtual interface. Only connections that are not bound to other interfaces are available in the list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p64312918414"><a name="p64312918414"></a><a name="p64312918414"></a>dc-123</p>
    </td>
    </tr>
    <tr id="row11441729104110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p6432297419"><a name="p6432297419"></a><a name="p6432297419"></a>Virtual Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p2043929154117"><a name="p2043929154117"></a><a name="p2043929154117"></a>Select the virtual gateway to be associated.</p>
    <p id="p11957147153218"><a name="p11957147153218"></a><a name="p11957147153218"></a>You can select a virtual gateway that has virtual interfaces bound. However, the connection associated with the virtual interfaces that have been bound to the virtual gateway needs to be at different locations.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p844152918415"><a name="p844152918415"></a><a name="p844152918415"></a>vgw-123</p>
    </td>
    </tr>
    <tr id="row194419295418"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p14417295413"><a name="p14417295413"></a><a name="p14417295413"></a>VLAN</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p1844129154120"><a name="p1844129154120"></a><a name="p1844129154120"></a>Specifies the virtual interface VLAN ID.</p>
    <p id="p153059362317"><a name="p153059362317"></a><a name="p153059362317"></a>The system automatically allocates a VLAN ID. You do not need to set this parameter.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p1244182914411"><a name="p1244182914411"></a><a name="p1244182914411"></a>30</p>
    </td>
    </tr>
    <tr id="row1729520195912"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p13295151913912"><a name="p13295151913912"></a><a name="p13295151913912"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p1229511191992"><a name="p1229511191992"></a><a name="p1229511191992"></a>Specifies the virtual interface bandwidth in the unit of Mbit/s.</p>
    <p id="p184111483252"><a name="p184111483252"></a><a name="p184111483252"></a>If the selected connection is a hosting connection, the virtual interface exclusively uses the connection bandwidth. That is, the connection bandwidth is the bandwidth of the virtual interface.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p16295619293"><a name="p16295619293"></a><a name="p16295619293"></a>100</p>
    </td>
    </tr>
    <tr id="row64516291414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4441429154110"><a name="p4441429154110"></a><a name="p4441429154110"></a>Remote Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p1244122918413"><a name="p1244122918413"></a><a name="p1244122918413"></a>Specifies the remote subnet and mask. You can enter a maximum of 50 remote subnets. Each pair must be unique. Separate every two remote subnets with commas (,).</p>
    <p id="p14320417153519"><a name="p14320417153519"></a><a name="p14320417153519"></a>The remote subnet of the virtual interface cannot be the same as the VPC CIDR block of the virtual gateway.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p1645429184110"><a name="p1645429184110"></a><a name="p1645429184110"></a>192.168.51.0/24</p>
    </td>
    </tr>
    <tr id="row15452029174112"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p14511292418"><a name="p14511292418"></a><a name="p14511292418"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.230000000000004%" headers="mcps1.2.4.1.2 "><p id="p18458293412"><a name="p18458293412"></a><a name="p18458293412"></a>Provides supplementary information about the virtual interface.</p>
    <p id="p8136182125020"><a name="p8136182125020"></a><a name="p8136182125020"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.4.1.3 "><p id="p045152918419"><a name="p045152918419"></a><a name="p045152918419"></a>This is a virtual interface.</p>
    </td>
    </tr>
    </tbody>
    </table>

16. Click  **Create Now**.

