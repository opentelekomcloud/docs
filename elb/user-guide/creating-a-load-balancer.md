# Creating a Load Balancer<a name="EN-US_TOPIC_0166333711"></a>

## Prerequisites<a name="section12884538197"></a>

You have prepared everything required for creating a load balancer. For details, see  [Preparing for Creation](preparing-for-creation.md).

Load balancers receive requests from clients and route them to backend servers, which answer to these requests over the private network.

## Create a Classic Load Balancer<a name="section3645846124218"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Create Classic Load Balancer**. On the displayed page, specify the parameters by referring to  [Table 1](#table806872716142).

    **Table  1**  Parameters for creating a classic load balancer

    <a name="table806872716142"></a>
    <table><thead align="left"><tr id="row4390154016142"><th class="cellrowborder" valign="top" width="25.44%" id="mcps1.2.4.1.1"><p id="p6636386516142"><a name="p6636386516142"></a><a name="p6636386516142"></a><strong id="b202252391210"><a name="b202252391210"></a><a name="b202252391210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.2"><p id="p6087573416142"><a name="p6087573416142"></a><a name="p6087573416142"></a><strong id="b11471440911"><a name="b11471440911"></a><a name="b11471440911"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.3"><p id="p1945115416142"><a name="p1945115416142"></a><a name="p1945115416142"></a><strong id="b125912416114"><a name="b125912416114"></a><a name="b125912416114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1992116816142"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p300190816142"><a name="p300190816142"></a><a name="p300190816142"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p4182802516142"><a name="p4182802516142"></a><a name="p4182802516142"></a>Specifies the load balancer name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p3262688716142"><a name="p3262688716142"></a><a name="p3262688716142"></a>elb_01</p>
    </td>
    </tr>
    <tr id="row2520652816142"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p2846289316142"><a name="p2846289316142"></a><a name="p2846289316142"></a>Network Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p2379301516142"><a name="p2379301516142"></a><a name="p2379301516142"></a>Specifies the network type of a load balancer. There are two options:</p>
    <a name="ul1281054616142"></a><a name="ul1281054616142"></a><ul id="ul1281054616142"><li><strong id="b84235270617328"><a name="b84235270617328"></a><a name="b84235270617328"></a>Public network</strong>: A public network load balancer routes requests from the clients to backend servers over the Internet.</li><li><strong id="b842352706111517"><a name="b842352706111517"></a><a name="b842352706111517"></a>Private network</strong>: A private network load balancer routes requests from the clients to backend servers in a VPC.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6594779116142"><a name="p6594779116142"></a><a name="p6594779116142"></a>Private network</p>
    </td>
    </tr>
    <tr id="row5665921016142"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p2599326716142"><a name="p2599326716142"></a><a name="p2599326716142"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p2507984416142"><a name="p2507984416142"></a><a name="p2507984416142"></a>Specifies the VPC where the load balancer works.</p>
    <p id="p2439200716142"><a name="p2439200716142"></a><a name="p2439200716142"></a>You can select an existing VPC or create one.</p>
    <p id="p15101746113715"><a name="p15101746113715"></a><a name="p15101746113715"></a>For more information about VPC, see the <em id="i84235269714525"><a name="i84235269714525"></a><a name="i84235269714525"></a>Virtual Private Cloud User Guide</em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6503360016142"><a name="p6503360016142"></a><a name="p6503360016142"></a>VPC_01</p>
    </td>
    </tr>
    <tr id="row2708947616352"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p4317665116355"><a name="p4317665116355"></a><a name="p4317665116355"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p764788216355"><a name="p764788216355"></a><a name="p764788216355"></a>Specifies the public IP address bound to a load balancer. This parameter is available when you select <strong id="b1631495515613"><a name="b1631495515613"></a><a name="b1631495515613"></a>Public network</strong> for <strong id="b1031595512618"><a name="b1031595512618"></a><a name="b1031595512618"></a>Network Type</strong>. You can use an existing EIP or apply for a new one.</p>
    <a name="ul1935965317046"></a><a name="ul1935965317046"></a><ul id="ul1935965317046"><li><strong id="b842352706195854"><a name="b842352706195854"></a><a name="b842352706195854"></a>New EIP</strong>: The system will assign a new EIP to the load balancer.</li><li><strong id="b55219283143321"><a name="b55219283143321"></a><a name="b55219283143321"></a>Use existing</strong>: An existing IP address will be used. You need to select an EIP from the drop-down list.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p1549873816355"><a name="p1549873816355"></a><a name="p1549873816355"></a>10.154.56.194</p>
    </td>
    </tr>
    <tr id="row6039905116237"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p672055316237"><a name="p672055316237"></a><a name="p672055316237"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p749390916237"><a name="p749390916237"></a><a name="p749390916237"></a>Specifies the subnet where the load balancer works when you select <strong id="b1076112417912"><a name="b1076112417912"></a><a name="b1076112417912"></a>Private network</strong> for <strong id="b1776219417920"><a name="b1776219417920"></a><a name="b1776219417920"></a>Network Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p302685316237"><a name="p302685316237"></a><a name="p302685316237"></a>N/A</p>
    </td>
    </tr>
    <tr id="row4843149416142"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p3063695216142"><a name="p3063695216142"></a><a name="p3063695216142"></a>Virtual IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p6567407116142"><a name="p6567407116142"></a><a name="p6567407116142"></a>Specifies the virtual IP address that will be bound to a load balancer. This parameter is required when you select <strong id="b2997843111120"><a name="b2997843111120"></a><a name="b2997843111120"></a>Private network</strong> for <strong id="b7998144321112"><a name="b7998144321112"></a><a name="b7998144321112"></a>Network Type</strong>. You can select <strong id="b48361645171118"><a name="b48361645171118"></a><a name="b48361645171118"></a>Automatically assign</strong> or <strong id="b983612459118"><a name="b983612459118"></a><a name="b983612459118"></a>Manually specify</strong>. You need to enter an IP address when you select <strong id="b842352706154816"><a name="b842352706154816"></a><a name="b842352706154816"></a>Manually specify</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6025916616748"><a name="p6025916616748"></a><a name="p6025916616748"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row222653151638"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p661701071638"><a name="p661701071638"></a><a name="p661701071638"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p581784571638"><a name="p581784571638"></a><a name="p581784571638"></a>Specifies the security group of the load balancer. This parameter is available when you select <strong id="b28522502118"><a name="b28522502118"></a><a name="b28522502118"></a>Private network</strong> for <strong id="b1785255013114"><a name="b1785255013114"></a><a name="b1785255013114"></a>Network Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p148346161638"><a name="p148346161638"></a><a name="p148346161638"></a>N/A</p>
    </td>
    </tr>
    <tr id="row20836662151336"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p53312238151336"><a name="p53312238151336"></a><a name="p53312238151336"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p5496486515144"><a name="p5496486515144"></a><a name="p5496486515144"></a>Specifies the public network bandwidth in the unit of Mbit/s.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p2296906515144"><a name="p2296906515144"></a><a name="p2296906515144"></a>100 Mbit/s</p>
    </td>
    </tr>
    <tr id="row5804228316142"><td class="cellrowborder" valign="top" width="25.44%" headers="mcps1.2.4.1.1 "><p id="p380446216142"><a name="p380446216142"></a><a name="p380446216142"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p3972597716142"><a name="p3972597716142"></a><a name="p3972597716142"></a>Provides supplementary information about the load balancer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6368757316142"><a name="p6368757316142"></a><a name="p6368757316142"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Next**.
6.  After confirming the configuration, click  **Submit**.

## Create an Enhanced Load Balancer<a name="section19343262431"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click  **Create Enhanced Load Balancer**  in the  **Operation**  column. Set the parameters by referring to  [Table 2](#table1312515231668).

    **Table  2**  Parameters for creating an enhanced load balancer

    <a name="table1312515231668"></a>
    <table><thead align="left"><tr id="row5117123161"><th class="cellrowborder" valign="top" width="24.36%" id="mcps1.2.4.1.1"><p id="p1117823768"><a name="p1117823768"></a><a name="p1117823768"></a><strong id="b152701410151511"><a name="b152701410151511"></a><a name="b152701410151511"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.71%" id="mcps1.2.4.1.2"><p id="p311712236611"><a name="p311712236611"></a><a name="p311712236611"></a><strong id="b1389131141513"><a name="b1389131141513"></a><a name="b1389131141513"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.93%" id="mcps1.2.4.1.3"><p id="p9117192312618"><a name="p9117192312618"></a><a name="p9117192312618"></a><strong id="b84235270617719"><a name="b84235270617719"></a><a name="b84235270617719"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row161204232619"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p41179231464"><a name="p41179231464"></a><a name="p41179231464"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p1911720230618"><a name="p1911720230618"></a><a name="p1911720230618"></a>Resources in different regions cannot communicate with each other over internal networks. For lower network latency and faster access to resources, select the nearest region.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p1912082312615"><a name="p1912082312615"></a><a name="p1912082312615"></a>N/A</p>
    </td>
    </tr>
    <tr id="row2120523962"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p131203233612"><a name="p131203233612"></a><a name="p131203233612"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p412010231864"><a name="p412010231864"></a><a name="p412010231864"></a>Specifies the VPC where the load balancer works.</p>
    <p id="p912017235612"><a name="p912017235612"></a><a name="p912017235612"></a>You can select an existing VPC or create one.</p>
    <p id="p16120223061"><a name="p16120223061"></a><a name="p16120223061"></a>For more information about VPC, see the <em id="i1548834481517"><a name="i1548834481517"></a><a name="i1548834481517"></a>Virtual Private Cloud User Guide</em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p51206233618"><a name="p51206233618"></a><a name="p51206233618"></a>N/A</p>
    </td>
    </tr>
    <tr id="row161213231462"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p151201323169"><a name="p151201323169"></a><a name="p151201323169"></a>Network Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p111201623364"><a name="p111201623364"></a><a name="p111201623364"></a>Specifies the network type of a load balancer. There are two options:</p>
    <a name="ul9121423867"></a><a name="ul9121423867"></a><ul id="ul9121423867"><li><strong id="b640712220152"><a name="b640712220152"></a><a name="b640712220152"></a>Public network</strong>: A public network load balancer routes requests from the clients to backend servers over the Internet.</li><li><strong id="b940193120156"><a name="b940193120156"></a><a name="b940193120156"></a>Private network</strong>: A private network load balancer routes requests from the clients to backend servers in a VPC.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p13121723161"><a name="p13121723161"></a><a name="p13121723161"></a>Private network</p>
    </td>
    </tr>
    <tr id="row19121723266"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p2121172315614"><a name="p2121172315614"></a><a name="p2121172315614"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p2012112231161"><a name="p2012112231161"></a><a name="p2012112231161"></a>Specifies the subnet that the load balancer belongs to.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p71218238620"><a name="p71218238620"></a><a name="p71218238620"></a>N/A</p>
    </td>
    </tr>
    <tr id="row712113233611"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p101211223569"><a name="p101211223569"></a><a name="p101211223569"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p01211623863"><a name="p01211623863"></a><a name="p01211623863"></a>Specifies the IP address bound to the load balancer. You can select <strong id="b84235270615249"><a name="b84235270615249"></a><a name="b84235270615249"></a>Automatically assign</strong> or <strong id="b84235270615254"><a name="b84235270615254"></a><a name="b84235270615254"></a>Manually specify</strong>. If you select <strong id="b61315038315318"><a name="b61315038315318"></a><a name="b61315038315318"></a>Manually specify</strong>, enter an IP address.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p1112122315610"><a name="p1112122315610"></a><a name="p1112122315610"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row1112282318619"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p1612117231566"><a name="p1612117231566"></a><a name="p1612117231566"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p91211023964"><a name="p91211023964"></a><a name="p91211023964"></a>Specifies the public IP address bound to the load balancer for receiving and forwarding requests over the Internet.</p>
    <p id="p1812120231665"><a name="p1812120231665"></a><a name="p1812120231665"></a>You can use an existing EIP or apply for a new one.</p>
    <p id="p1412112231464"><a name="p1412112231464"></a><a name="p1412112231464"></a>The following options are available:</p>
    <a name="ul51229232063"></a><a name="ul51229232063"></a><ul id="ul51229232063"><li><strong id="b84235270615639"><a name="b84235270615639"></a><a name="b84235270615639"></a>Not required</strong>: No EIP will be bound to the load balancer. Therefore, the load balancer cannot receive requests from clients over the Internet.</li><li><strong id="b16427828112014"><a name="b16427828112014"></a><a name="b16427828112014"></a>New EIP</strong>: The system will automatically assign an EIP.</li><li><strong id="b134597530208"><a name="b134597530208"></a><a name="b134597530208"></a>Use existing</strong>: To use an existing EIP, select one from the drop-down list.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p1412214231768"><a name="p1412214231768"></a><a name="p1412214231768"></a>New EIP</p>
    </td>
    </tr>
    <tr id="row41242233612"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p812314231366"><a name="p812314231366"></a><a name="p812314231366"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p8123182316611"><a name="p8123182316611"></a><a name="p8123182316611"></a>Specifies the bandwidth when a new EIP is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p11123142315610"><a name="p11123142315610"></a><a name="p11123142315610"></a>10 Mbit/s</p>
    </td>
    </tr>
    <tr id="row112414233619"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p16124723664"><a name="p16124723664"></a><a name="p16124723664"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p912410232614"><a name="p912410232614"></a><a name="p912410232614"></a>Specifies the load balancer name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p712402315614"><a name="p712402315614"></a><a name="p712402315614"></a>elb-yss0</p>
    </td>
    </tr>
    <tr id="row21242231616"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p6124112317617"><a name="p6124112317617"></a><a name="p6124112317617"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p171243231969"><a name="p171243231969"></a><a name="p171243231969"></a>Provides supplementary information about the load balancer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><p id="p1412414231067"><a name="p1412414231067"></a><a name="p1412414231067"></a>N/A</p>
    </td>
    </tr>
    <tr id="row312482318617"><td class="cellrowborder" valign="top" width="24.36%" headers="mcps1.2.4.1.1 "><p id="p101247235619"><a name="p101247235619"></a><a name="p101247235619"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.71%" headers="mcps1.2.4.1.2 "><p id="p31246231611"><a name="p31246231611"></a><a name="p31246231611"></a>Identifies load balancers so that they can be easily categorized and quickly searched. A tag consists of a tag key and a tag value. That is, you can distinguish cloud resources from two dimensions. The tag key marks a tag, and the tag value specifies specific tag content.</p>
    <p id="p1112415237614"><a name="p1112415237614"></a><a name="p1112415237614"></a>For details about the naming specifications, see <a href="#table212772311610">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.93%" headers="mcps1.2.4.1.3 "><a name="ul1912417231364"></a><a name="ul1912417231364"></a><ul id="ul1912417231364"><li>Key: elb_key1</li><li>Value: elb-01</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Naming rules of load balancer tags

    <a name="table212772311610"></a>
    <table><thead align="left"><tr id="row912512231661"><th class="cellrowborder" valign="top" width="10%" id="mcps1.2.4.1.1"><p id="p1712513231067"><a name="p1712513231067"></a><a name="p1712513231067"></a><strong id="b151692530564"><a name="b151692530564"></a><a name="b151692530564"></a>Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="73%" id="mcps1.2.4.1.2"><p id="p31257234610"><a name="p31257234610"></a><a name="p31257234610"></a><strong id="b1550711563561"><a name="b1550711563561"></a><a name="b1550711563561"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.3"><p id="p512519231167"><a name="p512519231167"></a><a name="p512519231167"></a><strong id="b1932625918563"><a name="b1932625918563"></a><a name="b1932625918563"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row131261423867"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.4.1.1 "><p id="p131251323260"><a name="p131251323260"></a><a name="p131251323260"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.2 "><a name="ul712618231865"></a><a name="ul712618231865"></a><ul id="ul712618231865"><li>Cannot be empty.</li><li>Must be unique for the same load balancer.</li><li>Consists of at most 36 characters.</li><li>Cannot contain asterisks (*), angle brackets (&lt; and &gt;), backslashes (\), equal signs (=), commas (,), vertical bars (|), or slashes (/).</li><li>Can contain only the following character types:<a name="ul812612318614"></a><a name="ul812612318614"></a><ul id="ul812612318614"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="p11126182313620"><a name="p11126182313620"></a><a name="p11126182313620"></a>elb_key1</p>
    </td>
    </tr>
    <tr id="row5126132314618"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.4.1.1 "><p id="p1612613236616"><a name="p1612613236616"></a><a name="p1612613236616"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.2 "><a name="ul2126192311620"></a><a name="ul2126192311620"></a><ul id="ul2126192311620"><li>Can contain a maximum of 43 characters.</li><li>Cannot contain asterisks (*), angle brackets (&lt; and &gt;), backslashes (\), equal signs (=), commas (,), vertical bars (|), or slashes (/).</li><li>Can contain only the following character types:<a name="ul1126122319611"></a><a name="ul1126122319611"></a><ul id="ul1126122319611"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="p412612235611"><a name="p412612235611"></a><a name="p412612235611"></a>elb-01</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Create Now**.
6.  Confirm the configuration and click  **Submit**.

