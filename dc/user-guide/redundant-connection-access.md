# Redundant Connection Access<a name="EN-US_TOPIC_0128466510"></a>

## Scenarios<a name="section135321112156"></a>

A local data center is connected to a VPC through a connection. To prevent a single connection failure from affecting services, you are advised to create two connections with different access locations. If a connection fails, services are switched to the other connection quickly. Therefore, the communication between the local data center and the VPC is of high quality and high reliability.

**Figure  1**  Redundant connection access<a name="fig1613412318719"></a>  
![](figures/redundant-connection-access.png "redundant-connection-access")

## Operation Flowchart<a name="section184074216541"></a>

You need to create two connections, with one connecting to Biere and the other to Magdeburg. Create a virtual gateway and access the VPC to which the services belong. Create two virtual interfaces and connect them to the same virtual gateway associated with the target VPC.  [Figure 2](#fig159261841102013)  shows how to create a redundant connection.

**Figure  2**  Flowchart for creating a redundant connection<a name="fig159261841102013"></a>  
![](figures/flowchart-for-creating-a-redundant-connection.png "flowchart-for-creating-a-redundant-connection")

## Procedure<a name="section161586309417"></a>

**Creating a Connection**

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and a project.
3.  Under  **Network**, click  **Direct Connect**.
4.  <a name="li1734982310613"></a>In the navigation pane of  **Network Console**, choose  **Direct Connect**  \>  **Connections**.
5.  On the displayed  **Connections**  page, click  **Create Connection**  in the upper right corner to create the first connection.
6.  Follow the prompts to set the following parameters.

    **Table  1**  Connection parameters

    <a name="table27593495173236"></a>
    <table><thead align="left"><tr id="row20729321173236"><th class="cellrowborder" valign="top" width="22.869999999999997%" id="mcps1.2.4.1.1"><p id="p34545082173236"><a name="p34545082173236"></a><a name="p34545082173236"></a><strong id="b11294882173236"><a name="b11294882173236"></a><a name="b11294882173236"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.48%" id="mcps1.2.4.1.2"><p id="p17541007173236"><a name="p17541007173236"></a><a name="p17541007173236"></a><strong id="b46688243173236"><a name="b46688243173236"></a><a name="b46688243173236"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.65%" id="mcps1.2.4.1.3"><p id="p36710115173236"><a name="p36710115173236"></a><a name="p36710115173236"></a><strong id="b11535442173236"><a name="b11535442173236"></a><a name="b11535442173236"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1536018810501"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p12518193510150"><a name="p12518193510150"></a><a name="p12518193510150"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p216615323151"><a name="p216615323151"></a><a name="p216615323151"></a>Specifies the region in which the services will be handled.</p>
    <p id="p0956203916214"><a name="p0956203916214"></a><a name="p0956203916214"></a>If you already selected a region and a project on the management console, you do not need to select the region here.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p3166173219151"><a name="p3166173219151"></a><a name="p3166173219151"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row49534062173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p1353477173236"><a name="p1353477173236"></a><a name="p1353477173236"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p47160706173236"><a name="p47160706173236"></a><a name="p47160706173236"></a>Specifies the connection name.</p>
    <p id="p145461311115919"><a name="p145461311115919"></a><a name="p145461311115919"></a>It can contain 1 to 64 characters.</p>
    <p id="p17341125815818"><a name="p17341125815818"></a><a name="p17341125815818"></a>Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p61920864173236"><a name="p61920864173236"></a><a name="p61920864173236"></a>dc-123</p>
    </td>
    </tr>
    <tr id="row23456554173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p43153374173236"><a name="p43153374173236"></a><a name="p43153374173236"></a>Location</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p0426123951012"><a name="p0426123951012"></a><a name="p0426123951012"></a>Specifies the connection access location.</p>
    <p id="p51861819173236"><a name="p51861819173236"></a><a name="p51861819173236"></a>You can select <strong id="b1588611264550"><a name="b1588611264550"></a><a name="b1588611264550"></a>Biere</strong> or <strong id="b19412112918555"><a name="b19412112918555"></a><a name="b19412112918555"></a>Magdeburg</strong>. The access location of the first connection must be different from that of the second connection.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p40057802173236"><a name="p40057802173236"></a><a name="p40057802173236"></a>Biere</p>
    </td>
    </tr>
    <tr id="row13638511173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p94751753211"><a name="p94751753211"></a><a name="p94751753211"></a>Peering Position</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p1587345416113"><a name="p1587345416113"></a><a name="p1587345416113"></a>Specifies the physical location of the connection. The address is an identifier.</p>
    <p id="p827223318553"><a name="p827223318553"></a><a name="p827223318553"></a>Only letters, digits, underscores (_), and hyphens (-) are allowed.</p>
    <p id="p1927819599112"><a name="p1927819599112"></a><a name="p1927819599112"></a>It can contain 0 to 64 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p126841930191715"><a name="p126841930191715"></a><a name="p126841930191715"></a>"Marderbug-DC01"</p>
    </td>
    </tr>
    <tr id="row22377693173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p49688592173236"><a name="p49688592173236"></a><a name="p49688592173236"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p65352981173236"><a name="p65352981173236"></a><a name="p65352981173236"></a>Specifies the bandwidth size in the unit of Mbit/s.</p>
    <p id="p832742232614"><a name="p832742232614"></a><a name="p832742232614"></a>You can select one of the bandwidths provided on the scroll bar by dragging it. Also, typing a value in the input field is allowed. It is automatically changed to the next allowed value shown on the slider bar.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p59100086173236"><a name="p59100086173236"></a><a name="p59100086173236"></a>100</p>
    </td>
    </tr>
    <tr id="row19093454173236"><td class="cellrowborder" valign="top" width="22.869999999999997%" headers="mcps1.2.4.1.1 "><p id="p0744211838"><a name="p0744211838"></a><a name="p0744211838"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.48%" headers="mcps1.2.4.1.2 "><p id="p5884269173236"><a name="p5884269173236"></a><a name="p5884269173236"></a>Provides supplementary information about the connection.</p>
    <p id="p1470572016597"><a name="p1470572016597"></a><a name="p1470572016597"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.65%" headers="mcps1.2.4.1.3 "><p id="p38575131177"><a name="p38575131177"></a><a name="p38575131177"></a>This is a connection.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  <a name="li111521031181317"></a>Click  **Create Now**, confirm the connection details, and click  **Submit**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Click  **Back to Connection List**  to view the created connections.  
    >-   After clicking  **Submit**, you will be automatically redirected to the connection list after a timeout.  

8.  Repeat step  [4](#li1734982310613)  to step  [7](#li111521031181317)  to create the second connection.

**Creating a Virtual Gateway**

1.  In the navigation pane on the left, choose  **Direct Connect**  \>  **Virtual Gateways**.
2.  In the upper right corner of the  **Virtual Gateways**  page, click  **Create Virtual Gateway**.
3.  Follow the prompts to set the following parameters.

    **Table  2**  Virtual gateway parameters

    <a name="table128947911279"></a>
    <table><thead align="left"><tr id="row1089915918275"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p99001998272"><a name="p99001998272"></a><a name="p99001998272"></a><strong id="b1590149112720"><a name="b1590149112720"></a><a name="b1590149112720"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.2"><p id="p1190212912277"><a name="p1190212912277"></a><a name="p1190212912277"></a><strong id="b1290379112710"><a name="b1290379112710"></a><a name="b1290379112710"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.3"><p id="p690418916274"><a name="p690418916274"></a><a name="p690418916274"></a><strong id="b990559102710"><a name="b990559102710"></a><a name="b990559102710"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29061998270"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p79074992720"><a name="p79074992720"></a><a name="p79074992720"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p490915911278"><a name="p490915911278"></a><a name="p490915911278"></a>Specifies the virtual gateway name.</p>
    <p id="p145122341482"><a name="p145122341482"></a><a name="p145122341482"></a>It can contain 1 to 64 characters.</p>
    <p id="p15542161014314"><a name="p15542161014314"></a><a name="p15542161014314"></a>Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p179107911278"><a name="p179107911278"></a><a name="p179107911278"></a>vgw-123</p>
    </td>
    </tr>
    <tr id="row1891549102716"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p69165912718"><a name="p69165912718"></a><a name="p69165912718"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p1191720972713"><a name="p1191720972713"></a><a name="p1191720972713"></a>Specifies the VPC that you need to access.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p13919696272"><a name="p13919696272"></a><a name="p13919696272"></a>VPC-001</p>
    </td>
    </tr>
    <tr id="row39191392274"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p271441112518"><a name="p271441112518"></a><a name="p271441112518"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p4927075995739"><a name="p4927075995739"></a><a name="p4927075995739"></a>Specifies the CIDR network segment of the VPC to be accessed by the connection.</p>
    <p id="p15921159162718"><a name="p15921159162718"></a><a name="p15921159162718"></a>You can add a maximum of 50 CIDR blocks. Each pair must be unique. Separate every two CIDR blocks with commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p13922179122714"><a name="p13922179122714"></a><a name="p13922179122714"></a>192.168.0.0/16</p>
    </td>
    </tr>
    <tr id="row20923797279"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p17924139182714"><a name="p17924139182714"></a><a name="p17924139182714"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p139261696276"><a name="p139261696276"></a><a name="p139261696276"></a>Provides supplementary information about the virtual gateway.</p>
    <p id="p1184624595912"><a name="p1184624595912"></a><a name="p1184624595912"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p5927294276"><a name="p5927294276"></a><a name="p5927294276"></a>This is a virtual gateway.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

**Creating a Virtual Interface**

1.  <a name="li1022162832914"></a>In the navigation pane on the left, choose  **Direct Connect**  \>  **Virtual Interfaces**.
2.  On the displayed  **Virtual Interfaces**  page, click  **Create Virtual Interface**  in the upper right corner to create the first virtual interface.
3.  Follow the prompts to set the following parameters.

    **Table  3**  Virtual interface parameters

    <a name="table54552924110"></a>
    <table><thead align="left"><tr id="row13422292417"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p94242918414"><a name="p94242918414"></a><a name="p94242918414"></a><strong id="b1942329204113"><a name="b1942329204113"></a><a name="b1942329204113"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.2"><p id="p5422294415"><a name="p5422294415"></a><a name="p5422294415"></a><strong id="b14422029174116"><a name="b14422029174116"></a><a name="b14422029174116"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.3"><p id="p1542182918410"><a name="p1542182918410"></a><a name="p1542182918410"></a><strong id="b1542172918414"><a name="b1542172918414"></a><a name="b1542172918414"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row712103912510"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19505125205119"><a name="p19505125205119"></a><a name="p19505125205119"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p13505452165118"><a name="p13505452165118"></a><a name="p13505452165118"></a>Specifies the region in which the services will be handled.</p>
    <p id="p1650535214513"><a name="p1650535214513"></a><a name="p1650535214513"></a>If you already selected a region and a project on the management console, you do not need to select the region here.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p1551225285120"><a name="p1551225285120"></a><a name="p1551225285120"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row1943142944110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18431229204113"><a name="p18431229204113"></a><a name="p18431229204113"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p134316296412"><a name="p134316296412"></a><a name="p134316296412"></a>Specifies the virtual interface name.</p>
    <p id="p11397624134"><a name="p11397624134"></a><a name="p11397624134"></a>It can contain 1 to 64 characters.</p>
    <p id="p1639982412316"><a name="p1639982412316"></a><a name="p1639982412316"></a>Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p94312293410"><a name="p94312293410"></a><a name="p94312293410"></a>vif-123</p>
    </td>
    </tr>
    <tr id="row943192918410"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p465610545143"><a name="p465610545143"></a><a name="p465610545143"></a>Connection</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p543172914112"><a name="p543172914112"></a><a name="p543172914112"></a>Specifies the connection to be associated.</p>
    <p id="p159711869418"><a name="p159711869418"></a><a name="p159711869418"></a>Select the connection that is connected to Biere or Magdeburg. The access locations of the two connections must be different.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p64312918414"><a name="p64312918414"></a><a name="p64312918414"></a>dc-123</p>
    </td>
    </tr>
    <tr id="row11441729104110"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p6432297419"><a name="p6432297419"></a><a name="p6432297419"></a>Virtual Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p2043929154117"><a name="p2043929154117"></a><a name="p2043929154117"></a>Select the virtual gateway to be associated.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p844152918415"><a name="p844152918415"></a><a name="p844152918415"></a>vgw-123</p>
    </td>
    </tr>
    <tr id="row194419295418"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p14417295413"><a name="p14417295413"></a><a name="p14417295413"></a>VLAN</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p1844129154120"><a name="p1844129154120"></a><a name="p1844129154120"></a>Specifies the virtual interface VLAN ID.</p>
    <p id="p153059362317"><a name="p153059362317"></a><a name="p153059362317"></a>The system automatically allocates a VLAN ID. You do not need to set this parameter.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p1244182914411"><a name="p1244182914411"></a><a name="p1244182914411"></a>30</p>
    </td>
    </tr>
    <tr id="row17505103482518"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p13295151913912"><a name="p13295151913912"></a><a name="p13295151913912"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p1229511191992"><a name="p1229511191992"></a><a name="p1229511191992"></a>Specifies the virtual interface bandwidth in the unit of Mbit/s.</p>
    <p id="p184111483252"><a name="p184111483252"></a><a name="p184111483252"></a>If the selected connection is a hosting connection, the virtual interface exclusively uses the connection bandwidth. That is, the connection bandwidth is the bandwidth of the virtual interface.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p16295619293"><a name="p16295619293"></a><a name="p16295619293"></a>100</p>
    </td>
    </tr>
    <tr id="row64516291414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4441429154110"><a name="p4441429154110"></a><a name="p4441429154110"></a>Remote Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p1244122918413"><a name="p1244122918413"></a><a name="p1244122918413"></a>Specifies the remote subnet and mask. You can enter a maximum of 50 remote subnets. Each pair must be unique. Separate every two remote subnets with commas (,).</p>
    <p id="p14320417153519"><a name="p14320417153519"></a><a name="p14320417153519"></a>The remote subnet of the virtual interface cannot be the same as the VPC CIDR block of the virtual gateway.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p1645429184110"><a name="p1645429184110"></a><a name="p1645429184110"></a>192.168.51.0/24</p>
    </td>
    </tr>
    <tr id="row15452029174112"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p14511292418"><a name="p14511292418"></a><a name="p14511292418"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.2 "><p id="p18458293412"><a name="p18458293412"></a><a name="p18458293412"></a>Provides supplementary information about the virtual interface.</p>
    <p id="p8136182125020"><a name="p8136182125020"></a><a name="p8136182125020"></a>It can contain 0 to 128 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p045152918419"><a name="p045152918419"></a><a name="p045152918419"></a>This is a virtual interface.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  <a name="li13735165074810"></a>Click  **Create Now**.
5.  Repeat step  [1](#li1022162832914)  to step  [4](#li13735165074810)  to create the second virtual interface.

