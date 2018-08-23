# Creating a Classic Load Balancer<a name="en-us_topic_0015479967"></a>

## Scenarios<a name="section20650420175959"></a>

This section describes how to create a classic load balancer.

## Prepare for Creation<a name="section95639111874"></a>

-   Select the network type of the load balancer.
    -   Public network \(Internet-facing\)

        A public network load balancer provides load balancing services through a public IP address and routes requests from the clients to backend ECSs over the Internet.

    -   Private network \(internal\)

        A private network load balancer provides load balancing services through the private IP address, and routes requests from the clients to backend ECSs in a VPC.

-   Select the protocol.

    <a name="table66244785114429"></a><table><thead align="left"><tr id="row36701900114429"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.5.1.1"><p id="p4473966141520"><a name="p4473966141520"></a><a name="p4473966141520"></a><strong id="b842352706102621"><a name="b842352706102621"></a><a name="b842352706102621"></a>Protocol</strong></p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.5.1.2"><p id="p60499166141520"><a name="p60499166141520"></a><a name="p60499166141520"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" id="mcps1.1.5.1.3"><p id="p18652969141520"><a name="p18652969141520"></a><a name="p18652969141520"></a><strong id="b84235270616379"><a name="b84235270616379"></a><a name="b84235270616379"></a>Application Scenario</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52657811114429"><td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.1 "><p id="p8541510141438"><a name="p8541510141438"></a><a name="p8541510141438"></a>Layer 4</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.1.5.1.1 "><p id="p20330484141012"><a name="p20330484141012"></a><a name="p20330484141012"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.1.5.1.2 "><a name="ul39716962141048"></a><a name="ul39716962141048"></a><ul id="ul39716962141048"><li id="li2168697141048"><a name="li2168697141048"></a><a name="li2168697141048"></a>Source IP address–based sticky sessions</li><li id="li15734882141048"><a name="li15734882141048"></a><a name="li15734882141048"></a>Fast data transfer</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="38.91%" headers="mcps1.1.5.1.3 "><a name="ul2315607141239"></a><a name="ul2315607141239"></a><ul id="ul2315607141239"><li id="li5593824141239"><a name="li5593824141239"></a><a name="li5593824141239"></a>Scenarios that require high reliability and data accuracy, such as file transfer, email sending and receiving, and remote login</li><li id="li59642403141239"><a name="li59642403141239"></a><a name="li59642403141239"></a>Web applications that feature a number of concurrent connections and require high performance</li></ul>
    </td>
    </tr>
    <tr id="row10959143516391"><td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.1 "><p id="p9959153583918"><a name="p9959153583918"></a><a name="p9959153583918"></a>Layer 4</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.1.5.1.1 "><p id="p5270937101819"><a name="p5270937101819"></a><a name="p5270937101819"></a>UDP</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.1.5.1.2 "><a name="ul9365451918"></a><a name="ul9365451918"></a><ul id="ul9365451918"><li id="li153517418198"><a name="li153517418198"></a><a name="li153517418198"></a>Low reliability</li><li id="li93615418197"><a name="li93615418197"></a><a name="li93615418197"></a>Fast data transfer</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="38.91%" headers="mcps1.1.5.1.3 "><p id="p154747282312"><a name="p154747282312"></a><a name="p154747282312"></a>Scenarios that focus on timeliness rather than reliability, such as video chat, game, and real-time financial market information push</p>
    </td>
    </tr>
    <tr id="row0310182312312"><td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.1 "><p id="p1031015238313"><a name="p1031015238313"></a><a name="p1031015238313"></a>Layer 4</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.1.5.1.1 "><p id="p9310132318310"><a name="p9310132318310"></a><a name="p9310132318310"></a>SSL</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.1.5.1.2 "><a name="ul19369121019249"></a><a name="ul19369121019249"></a><ul id="ul19369121019249"><li id="li2369161012246"><a name="li2369161012246"></a><a name="li2369161012246"></a>TCP-based security encryption</li><li id="li15194163042415"><a name="li15194163042415"></a><a name="li15194163042415"></a>High reliability</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="38.91%" headers="mcps1.1.5.1.3 "><p id="p1231015231431"><a name="p1231015231431"></a><a name="p1231015231431"></a>Applications that require encrypted transmission</p>
    </td>
    </tr>
    <tr id="row10296890141711"><td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.1 "><p id="p55450303141740"><a name="p55450303141740"></a><a name="p55450303141740"></a>Layer 7</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.1.5.1.1 "><p id="p3481406314187"><a name="p3481406314187"></a><a name="p3481406314187"></a>HTTP</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.1.5.1.2 "><a name="ul21894483141932"></a><a name="ul21894483141932"></a><ul id="ul21894483141932"><li id="li48229158141932"><a name="li48229158141932"></a><a name="li48229158141932"></a>Cookie-based sticky sessions</li><li id="li10273639141932"><a name="li10273639141932"></a><a name="li10273639141932"></a>X-Forward-For request header</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="38.91%" headers="mcps1.1.5.1.3 "><p id="p55802598141819"><a name="p55802598141819"></a><a name="p55802598141819"></a>Applications in which the data content needs to be identified, such as web applications and mobile games</p>
    </td>
    </tr>
    <tr id="row25590944144339"><td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.1 "><p id="p28991905144339"><a name="p28991905144339"></a><a name="p28991905144339"></a>Layer 7</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.09%" headers="mcps1.1.5.1.1 "><p id="p11410140144345"><a name="p11410140144345"></a><a name="p11410140144345"></a>HTTPS</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.1.5.1.2 "><a name="ul51806117144345"></a><a name="ul51806117144345"></a><ul id="ul51806117144345"><li id="li63601869144345"><a name="li63601869144345"></a><a name="li63601869144345"></a>An extension of HTTP for encrypted data transmission that can prevent unauthorized access</li><li id="li52975091141037"><a name="li52975091141037"></a><a name="li52975091141037"></a>SSL offloading<p id="p2191026817229"><a name="p2191026817229"></a><a name="p2191026817229"></a>Encryption and decryption are performed on the load balancer to reduce the work load of backend ECSs.</p>
    </li><li id="li51477737144345"><a name="li51477737144345"></a><a name="li51477737144345"></a>Multiple encryption protocols and cipher suites</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="38.91%" headers="mcps1.1.5.1.3 "><p id="p8947194144345"><a name="p8947194144345"></a><a name="p8947194144345"></a>Applications that require encrypted transmission</p>
    </td>
    </tr>
    </tbody>
    </table>


## Create a Load Balancer<a name="section25831004181420"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093329999.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance** page, click **Create Classic Load Balancer** and specify the parameters listed in [Table 1](#table806872716142).

    **Table  1**  Load balancer parameters

    <a name="table806872716142"></a><table><thead align="left"><tr id="row4390154016142"><th class="cellrowborder" valign="top" width="22.43%" id="mcps1.2.4.1.1"><p id="p6636386516142"><a name="p6636386516142"></a><a name="p6636386516142"></a><strong id="b6040387516142"><a name="b6040387516142"></a><a name="b6040387516142"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.010000000000005%" id="mcps1.2.4.1.2"><p id="p6087573416142"><a name="p6087573416142"></a><a name="p6087573416142"></a><strong id="b1101069616142"><a name="b1101069616142"></a><a name="b1101069616142"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.3"><p id="p1945115416142"><a name="p1945115416142"></a><a name="p1945115416142"></a><strong id="b4084266016142"><a name="b4084266016142"></a><a name="b4084266016142"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1992116816142"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p300190816142"><a name="p300190816142"></a><a name="p300190816142"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p4182802516142"><a name="p4182802516142"></a><a name="p4182802516142"></a>Specifies the load balancer name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p3262688716142"><a name="p3262688716142"></a><a name="p3262688716142"></a>elb_01</p>
    </td>
    </tr>
    <tr id="row2520652816142"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p2846289316142"><a name="p2846289316142"></a><a name="p2846289316142"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p2379301516142"><a name="p2379301516142"></a><a name="p2379301516142"></a>Specifies the network type of a load balancer. There are two options:</p>
    <a name="ul1281054616142"></a><a name="ul1281054616142"></a><ul id="ul1281054616142"><li id="li271174141254"><a name="li271174141254"></a><a name="li271174141254"></a><strong id="b84235270617328"><a name="b84235270617328"></a><a name="b84235270617328"></a>Public network</strong>: A public network load balancer routes the requests from the clients to backend ECSs over the Internet.</li><li id="li4818605316142"><a name="li4818605316142"></a><a name="li4818605316142"></a><strong id="b842352706111517"><a name="b842352706111517"></a><a name="b842352706111517"></a>Private network</strong>: A private network load balancer routes the requests from the clients to backend ECSs in a VPC.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6594779116142"><a name="p6594779116142"></a><a name="p6594779116142"></a>Private network</p>
    </td>
    </tr>
    <tr id="row5665921016142"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p2599326716142"><a name="p2599326716142"></a><a name="p2599326716142"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p2507984416142"><a name="p2507984416142"></a><a name="p2507984416142"></a>Specifies the VPC where the load balancer works.</p>
    <p id="p2439200716142"><a name="p2439200716142"></a><a name="p2439200716142"></a>You can select an existing VPC or create one.</p>
    <p id="p1820147816142"><a name="p1820147816142"></a><a name="p1820147816142"></a>For more information about VPC, see the <em id="i84235269714525"><a name="i84235269714525"></a><a name="i84235269714525"></a>Virtual Private Cloud User Guide</em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6503360016142"><a name="p6503360016142"></a><a name="p6503360016142"></a>VPC_01</p>
    </td>
    </tr>
    <tr id="row2708947616352"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p4317665116355"><a name="p4317665116355"></a><a name="p4317665116355"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p764788216355"><a name="p764788216355"></a><a name="p764788216355"></a>Specifies the public IP address bound to a public network load balancer. This parameter is available when you select <strong id="b84235270610938"><a name="b84235270610938"></a><a name="b84235270610938"></a>Public network</strong>&nbsp;for&nbsp;<strong id="b84235270610948"><a name="b84235270610948"></a><a name="b84235270610948"></a>Type</strong>. Two options are available for you:</p>
    <a name="ul1935965317046"></a><a name="ul1935965317046"></a><ul id="ul1935965317046"><li id="li2115723817046"><a name="li2115723817046"></a><a name="li2115723817046"></a><strong id="b842352706195854"><a name="b842352706195854"></a><a name="b842352706195854"></a>New EIP</strong>: The system will assign a new EIP to the load balancer.</li><li id="li3150798317046"><a name="li3150798317046"></a><a name="li3150798317046"></a><strong id="b55219283143321"><a name="b55219283143321"></a><a name="b55219283143321"></a>Use existing</strong>: An existing IP address will be used.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p1549873816355"><a name="p1549873816355"></a><a name="p1549873816355"></a>10.154.56.194</p>
    </td>
    </tr>
    <tr id="row6039905116237"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p672055316237"><a name="p672055316237"></a><a name="p672055316237"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p749390916237"><a name="p749390916237"></a><a name="p749390916237"></a>Specifies the subnet where the load balancer works when you select <strong id="b1538662124153121"><a name="b1538662124153121"></a><a name="b1538662124153121"></a>Private network</strong>&nbsp;for&nbsp;<strong id="b842352706123931"><a name="b842352706123931"></a><a name="b842352706123931"></a>Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p302685316237"><a name="p302685316237"></a><a name="p302685316237"></a>N/A</p>
    </td>
    </tr>
    <tr id="row4843149416142"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p3063695216142"><a name="p3063695216142"></a><a name="p3063695216142"></a>Virtual IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p25921021153529"><a name="p25921021153529"></a><a name="p25921021153529"></a>Specifies the virtual IP address (VIP) bound to a private network load balancer. This parameter is available when you select <strong id="b57166080153529"><a name="b57166080153529"></a><a name="b57166080153529"></a>Private network</strong>&nbsp;for&nbsp;<strong id="b44732680153529"><a name="b44732680153529"></a><a name="b44732680153529"></a>Type</strong>. Two options are available:</p>
    <a name="ul902388153548"></a><a name="ul902388153548"></a><ul id="ul902388153548"><li id="li5072023415365"><a name="li5072023415365"></a><a name="li5072023415365"></a><strong id="b61001624153634"><a name="b61001624153634"></a><a name="b61001624153634"></a>Automatically assign</strong>: The system will assign a VIP to the load balancer.</li><li id="li8121495153548"><a name="li8121495153548"></a><a name="li8121495153548"></a><strong id="b20047614153618"><a name="b20047614153618"></a><a name="b20047614153618"></a>Manually specify</strong>: You need to enter an IP address.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6025916616748"><a name="p6025916616748"></a><a name="p6025916616748"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row222653151638"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p661701071638"><a name="p661701071638"></a><a name="p661701071638"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p581784571638"><a name="p581784571638"></a><a name="p581784571638"></a>Specifies the security group of the load balancer. This parameter is available when you select <strong id="b84235270610938_1"><a name="b84235270610938_1"></a><a name="b84235270610938_1"></a>Private network</strong>&nbsp;for&nbsp;<strong id="b84235270610948_1"><a name="b84235270610948_1"></a><a name="b84235270610948_1"></a>Type</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p148346161638"><a name="p148346161638"></a><a name="p148346161638"></a>N/A</p>
    </td>
    </tr>
    <tr id="row20836662151336"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p53312238151336"><a name="p53312238151336"></a><a name="p53312238151336"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p5496486515144"><a name="p5496486515144"></a><a name="p5496486515144"></a>Specifies the public network bandwidth in Mbit/s.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p2296906515144"><a name="p2296906515144"></a><a name="p2296906515144"></a>100 Mbit/s</p>
    </td>
    </tr>
    <tr id="row5804228316142"><td class="cellrowborder" valign="top" width="22.43%" headers="mcps1.2.4.1.1 "><p id="p380446216142"><a name="p380446216142"></a><a name="p380446216142"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.010000000000005%" headers="mcps1.2.4.1.2 "><p id="p3972597716142"><a name="p3972597716142"></a><a name="p3972597716142"></a>Provides supplementary information about the load balancer.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.3 "><p id="p6368757316142"><a name="p6368757316142"></a><a name="p6368757316142"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Create Now**.
6.  After confirming the specifications, click  **Submit**.

## Add a Listener<a name="section39277103194915"></a>

After creating a load balancer, you must add a listener to this load balancer. Perform the following operations to add a listener:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093340396.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  In the  **Listeners** area, click **Add Listener**. In the displayed **Add Listener** dialog box, specify the parameters by referring to [Table 2](#table3947759918410).

    **Table  2**  Listener parameters

    <a name="table3947759918410"></a><table><thead align="left"><tr id="row1918557218410"><th class="cellrowborder" valign="top" width="24.68%" id="mcps1.2.4.1.1"><p id="p25669989184122"><a name="p25669989184122"></a><a name="p25669989184122"></a><strong id="b9225239193651"><a name="b9225239193651"></a><a name="b9225239193651"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.21000000000001%" id="mcps1.2.4.1.2"><p id="p66003208184122"><a name="p66003208184122"></a><a name="p66003208184122"></a><strong id="b9046885193651"><a name="b9046885193651"></a><a name="b9046885193651"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.3"><p id="p44659603184122"><a name="p44659603184122"></a><a name="p44659603184122"></a><strong id="b61709088193651"><a name="b61709088193651"></a><a name="b61709088193651"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3253628418410"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p9051947184122"><a name="p9051947184122"></a><a name="p9051947184122"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p62119074184122"><a name="p62119074184122"></a><a name="p62119074184122"></a>Specifies the listener name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p59487507161644"><a name="p59487507161644"></a><a name="p59487507161644"></a>listener01</p>
    </td>
    </tr>
    <tr id="row66795703161723"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p55255176161725"><a name="p55255176161725"></a><a name="p55255176161725"></a>Frontend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p566915862411"><a name="p566915862411"></a><a name="p566915862411"></a>Specifies the protocol and port the load balancer uses to receive requests from the client and forwards the requests to backend ECSs.</p>
    <p id="p60247126141642"><a name="p60247126141642"></a><a name="p60247126141642"></a>Public network load balancers support the following protocols:</p>
    <a name="ul64785515141838"></a><a name="ul64785515141838"></a><ul id="ul64785515141838"><li id="li29511663141838"><a name="li29511663141838"></a><a name="li29511663141838"></a>HTTP: load balancing at Layer 7</li><li id="li7962232141838"><a name="li7962232141838"></a><a name="li7962232141838"></a>TCP: load balancing at Layer 4</li><li id="li2231402293336"><a name="li2231402293336"></a><a name="li2231402293336"></a>HTTPS: encrypted load balancing at Layer 7</li><li id="li16949496124511"><a name="li16949496124511"></a><a name="li16949496124511"></a>UDP: load balancing at Layer 4</li><li id="li29456178141058"><a name="li29456178141058"></a><a name="li29456178141058"></a>SSL: encrypted layer-4 load balancing</li></ul>
    <p id="p56845019104911"><a name="p56845019104911"></a><a name="p56845019104911"></a>A private network load balancer supports the following protocols:</p>
    <a name="ul59199498104954"></a><a name="ul59199498104954"></a><ul id="ul59199498104954"><li id="li5435049104954"><a name="li5435049104954"></a><a name="li5435049104954"></a>HTTP: load balancing at Layer 7</li><li id="li63033440104954"><a name="li63033440104954"></a><a name="li63033440104954"></a>TCP: load balancing at Layer 4</li><li id="li48915446104954"><a name="li48915446104954"></a><a name="li48915446104954"></a>HTTPS: encrypted load balancing at Layer 7</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p7129598161725"><a name="p7129598161725"></a><a name="p7129598161725"></a>TCP/80</p>
    <p id="p49979242124539"><a name="p49979242124539"></a><a name="p49979242124539"></a>UDP/80</p>
    <p id="p34532864101423"><a name="p34532864101423"></a><a name="p34532864101423"></a>HTTP/80</p>
    <p id="p86058693432"><a name="p86058693432"></a><a name="p86058693432"></a>HTTPS/443</p>
    <p id="p29201162155524"><a name="p29201162155524"></a><a name="p29201162155524"></a>SSL/443</p>
    </td>
    </tr>
    <tr id="row49179263162422"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p39960184162422"><a name="p39960184162422"></a><a name="p39960184162422"></a>Backend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p15549454162422"><a name="p15549454162422"></a><a name="p15549454162422"></a>Specifies the protocol and port used by backend ECSs to receive requests.</p>
    <a name="ul115418117206"></a><a name="ul115418117206"></a><ul id="ul115418117206"><li id="li5709302016525"><a name="li5709302016525"></a><a name="li5709302016525"></a>TCP: layer-4 load balancing. When <strong id="b842352706144454"><a name="b842352706144454"></a><a name="b842352706144454"></a>Frontend Protocol</strong> is set to <strong id="b84235270614451"><a name="b84235270614451"></a><a name="b84235270614451"></a>SSL</strong>, <strong id="b84235270614457"><a name="b84235270614457"></a><a name="b84235270614457"></a>Backend Protocol</strong> is <strong id="b842352706144511"><a name="b842352706144511"></a><a name="b842352706144511"></a>TCP</strong> by default.</li><li id="li47593951124552"><a name="li47593951124552"></a><a name="li47593951124552"></a>UDP: layer-4 load balance service. When <strong id="b842352706144454_1"><a name="b842352706144454_1"></a><a name="b842352706144454_1"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b84235270614451_1"><a name="b84235270614451_1"></a><a name="b84235270614451_1"></a>UDP</strong>,&nbsp;<strong id="b84235270614457_1"><a name="b84235270614457_1"></a><a name="b84235270614457_1"></a>Backend Protocol</strong>&nbsp;is&nbsp;<strong id="b842352706144511_1"><a name="b842352706144511_1"></a><a name="b842352706144511_1"></a>UDP</strong> by default.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p66231138124610"><a name="p66231138124610"></a><a name="p66231138124610"></a>TCP/22</p>
    <p id="p51546298162422"><a name="p51546298162422"></a><a name="p51546298162422"></a>HTTP/80</p>
    </td>
    </tr>
    <tr id="row62337098162422"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p24162975162422"><a name="p24162975162422"></a><a name="p24162975162422"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p11043993162422"><a name="p11043993162422"></a><a name="p11043993162422"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="ul5968188218551"></a><a name="ul5968188218551"></a><ul id="ul5968188218551"><li id="en-us_topic_0118840331_li5131817515586"><a name="en-us_topic_0118840331_li5131817515586"></a><a name="en-us_topic_0118840331_li5131817515586"></a><strong id="en-us_topic_0118840331_b842352706102822"><a name="en-us_topic_0118840331_b842352706102822"></a><a name="en-us_topic_0118840331_b842352706102822"></a>Round robin</strong>: New connection requests are distributed sequentially across all ECSs, so that request workload is evenly shared.</li><li id="en-us_topic_0118840331_li5921039715586"><a name="en-us_topic_0118840331_li5921039715586"></a><a name="en-us_topic_0118840331_li5921039715586"></a><strong id="en-us_topic_0118840331_b842352706103735"><a name="en-us_topic_0118840331_b842352706103735"></a><a name="en-us_topic_0118840331_b842352706103735"></a>Least connections</strong>: New connection requests are forwarded to the ECS processing the least number of connections at that time.</li><li id="en-us_topic_0118840331_li6313152515586"><a name="en-us_topic_0118840331_li6313152515586"></a><a name="en-us_topic_0118840331_li6313152515586"></a><strong id="en-us_topic_0118840331_b84235270616237"><a name="en-us_topic_0118840331_b84235270616237"></a><a name="en-us_topic_0118840331_b84235270616237"></a>Source IP hash</strong>: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.</li></ul>
    <div class="note" id="note449753855814"><a name="note449753855814"></a><a name="note449753855814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12497163811587"><a name="p12497163811587"></a><a name="p12497163811587"></a>As access traffic changes, choose the most appropriate algorithm to improve load balancing.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p22148268162422"><a name="p22148268162422"></a><a name="p22148268162422"></a>Round robin</p>
    </td>
    </tr>
    <tr id="row6077438093536"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p2377775393536"><a name="p2377775393536"></a><a name="p2377775393536"></a>Default Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p4694985993536"><a name="p4694985993536"></a><a name="p4694985993536"></a>Specifies the certificate used by an HTTPS load balancer.</p>
    <p id="p4904405162422"><a name="p4904405162422"></a><a name="p4904405162422"></a>You can select an existing certificate or create one. For how to create a certificate, see <a href="certificate.html">Certificate</a>.</p>
    <p id="p833794293717"><a name="p833794293717"></a><a name="p833794293717"></a>This parameter is available only when <strong id="b842352706105553"><a name="b842352706105553"></a><a name="b842352706105553"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b84235270610569"><a name="b84235270610569"></a><a name="b84235270610569"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p4484222593536"><a name="p4484222593536"></a><a name="p4484222593536"></a>cert-miij/9125267e1b1a4526b346cdfb9b9f856a</p>
    </td>
    </tr>
    <tr id="row7501782152651"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p50902905152739"><a name="p50902905152739"></a><a name="p50902905152739"></a>Enable SNI</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p29494611152739"><a name="p29494611152739"></a><a name="p29494611152739"></a>Specifies whether to enable the Server Name Indication (SNI) function when <strong id="b842352706101914"><a name="b842352706101914"></a><a name="b842352706101914"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b842352706101423"><a name="b842352706101423"></a><a name="b842352706101423"></a>HTTPS</strong>.</p>
    <p id="p64124909152739"><a name="p64124909152739"></a><a name="p64124909152739"></a>SNI is an extension to Transport Layer Security (TLS) when a server uses multiple domain names and certificates. This function allows the client to submit the domain name information while sending an SSL handshake request. Once receiving the request, the load balancer queries the right certificate based on the domain name and returns it to the client. If no certificate is found, the load balancer will issue a default certificate.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p26735145152739"><a name="p26735145152739"></a><a name="p26735145152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row18107119152656"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p28350476152739"><a name="p28350476152739"></a><a name="p28350476152739"></a>SNI Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p14687240152739"><a name="p14687240152739"></a><a name="p14687240152739"></a>Specifies the certificate associated with the domain name when <strong id="b84235270610193"><a name="b84235270610193"></a><a name="b84235270610193"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b991361406101711"><a name="b991361406101711"></a><a name="b991361406101711"></a>HTTPS</strong>.</p>
    <p id="p65076304152739"><a name="p65076304152739"></a><a name="p65076304152739"></a>You can select an existing certificate or create one.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p61767758152739"><a name="p61767758152739"></a><a name="p61767758152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row46636939152656"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p65757227152739"><a name="p65757227152739"></a><a name="p65757227152739"></a>SSL Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p24735162152739"><a name="p24735162152739"></a><a name="p24735162152739"></a>Specifies the encryption protocol used by an HTTPS load balancer. This parameter is used to enable a specified encryption protocol. The following protocols are supported:</p>
    <a name="ul57391130152739"></a><a name="ul57391130152739"></a><ul id="ul57391130152739"><li id="li46758128152739"><a name="li46758128152739"></a><a name="li46758128152739"></a><strong id="b842352706172956"><a name="b842352706172956"></a><a name="b842352706172956"></a>TLSv1.2</strong></li><li id="li18169971152739"><a name="li18169971152739"></a><a name="li18169971152739"></a><strong id="b84235270617303"><a name="b84235270617303"></a><a name="b84235270617303"></a>TLSv1.2 TLSv1.1 TLSv1</strong></li></ul>
    <p id="p29312012152739"><a name="p29312012152739"></a><a name="p29312012152739"></a>This parameter is available only when <strong id="b842352706105553_1"><a name="b842352706105553_1"></a><a name="b842352706105553_1"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b84235270610569_1"><a name="b84235270610569_1"></a><a name="b84235270610569_1"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p27837997152739"><a name="p27837997152739"></a><a name="p27837997152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row52414897152722"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p27023193152739"><a name="p27023193152739"></a><a name="p27023193152739"></a>SSL Cipher</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p41395063152739"><a name="p41395063152739"></a><a name="p41395063152739"></a>Specifies the cipher suite used by an HTTPS load balancer. The following options are available:</p>
    <a name="ul64665817152739"></a><a name="ul64665817152739"></a><ul id="ul64665817152739"><li id="li45121448152739"><a name="li45121448152739"></a><a name="li45121448152739"></a><strong id="b842352706103721"><a name="b842352706103721"></a><a name="b842352706103721"></a>Default Cipher</strong></li><li id="li3439848152739"><a name="li3439848152739"></a><a name="li3439848152739"></a><strong id="b842352706125422"><a name="b842352706125422"></a><a name="b842352706125422"></a>Extended Cipher</strong></li><li id="li30958635152739"><a name="li30958635152739"></a><a name="li30958635152739"></a><strong id="b842352706125429"><a name="b842352706125429"></a><a name="b842352706125429"></a>Strict Cipher</strong></li></ul>
    <p id="p10192267152739"><a name="p10192267152739"></a><a name="p10192267152739"></a>This parameter is available only when <strong id="b842352706105553_2"><a name="b842352706105553_2"></a><a name="b842352706105553_2"></a>Frontend Protocol</strong>&nbsp;is set to&nbsp;<strong id="b84235270610569_2"><a name="b84235270610569_2"></a><a name="b84235270610569_2"></a>HTTPS</strong>.&nbsp;<strong id="b84235270619212"><a name="b84235270619212"></a><a name="b84235270619212"></a>Extended Cipher</strong>&nbsp;is the only available choice when&nbsp;<strong id="b842352706192026"><a name="b842352706192026"></a><a name="b842352706192026"></a>SSL Protocol</strong>&nbsp;is set to&nbsp;<strong id="b842352706192049"><a name="b842352706192049"></a><a name="b842352706192049"></a>TLSv1.2 TLSv1.1 TLSv1</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p48188037152739"><a name="p48188037152739"></a><a name="p48188037152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row38569529152051"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p37941618152117"><a name="p37941618152117"></a><a name="p37941618152117"></a>Sticky Session</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p53372194152117"><a name="p53372194152117"></a><a name="p53372194152117"></a>Specifies whether to enable the sticky session feature.</p>
    <p id="p10587703152117"><a name="p10587703152117"></a><a name="p10587703152117"></a>If the sticky session feature is enabled, all requests from the same client during one session will be sent to the same backend ECS.</p>
    <div class="note" id="note586599751148"><a name="note586599751148"></a><a name="note586599751148"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p581777271148"><a name="p581777271148"></a><a name="p581777271148"></a>This feature is supported only when <strong id="b842352706144645"><a name="b842352706144645"></a><a name="b842352706144645"></a>Load Balancing Algorithm</strong>&nbsp;is set to&nbsp;<strong id="b84235270614472"><a name="b84235270614472"></a><a name="b84235270614472"></a>Round robin</strong>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p52297615152117"><a name="p52297615152117"></a><a name="p52297615152117"></a>N/A</p>
    </td>
    </tr>
    <tr id="row38165688152018"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p7946880152018"><a name="p7946880152018"></a><a name="p7946880152018"></a>Stickiness Duration</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p15559793153157"><a name="p15559793153157"></a><a name="p15559793153157"></a>Specifies the period of time that sticky sessions will be maintained. This parameter is available only when the sticky session feature is enabled. The parameter value ranges from 1 to 1440.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p63006969152018"><a name="p63006969152018"></a><a name="p63006969152018"></a>5 minutes</p>
    </td>
    </tr>
    <tr id="row37894296162422"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p5504344162422"><a name="p5504344162422"></a><a name="p5504344162422"></a>Health Check Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p43198726162422"><a name="p43198726162422"></a><a name="p43198726162422"></a>Specifies the protocol and port used for performing health checks on ECSs.</p>
    <div class="note" id="note9781344114112"><a name="note9781344114112"></a><a name="note9781344114112"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p20923240114112"><a name="p20923240114112"></a><a name="p20923240114112"></a>When UDP is used for health check, the security group rules of backend ECSs must allow access using the ICMP protocol.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p9435957162422"><a name="p9435957162422"></a><a name="p9435957162422"></a>HTTP/80</p>
    </td>
    </tr>
    <tr id="row2064894118410"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p32956516184122"><a name="p32956516184122"></a><a name="p32956516184122"></a>Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p25870774163512"><a name="p25870774163512"></a><a name="p25870774163512"></a>Specifies the maximum amount of time between health checks in the unit of second.</p>
    <p id="p17123758558"><a name="p17123758558"></a><a name="p17123758558"></a>The value ranges from 1 to 50.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p32682136163516"><a name="p32682136163516"></a><a name="p32682136163516"></a>5 seconds</p>
    </td>
    </tr>
    <tr id="row577303118410"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p43486880184122"><a name="p43486880184122"></a><a name="p43486880184122"></a>Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p6084546163512"><a name="p6084546163512"></a><a name="p6084546163512"></a>Specifies the maximum amount of time you need to wait when receiving a response from the health check in the unit of second.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p20753786163516"><a name="p20753786163516"></a><a name="p20753786163516"></a>10 seconds</p>
    </td>
    </tr>
    <tr id="row1853746318410"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p61652718184122"><a name="p61652718184122"></a><a name="p61652718184122"></a>Healthy Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p58496162163512"><a name="p58496162163512"></a><a name="p58496162163512"></a>Specifies the number of consecutive successful health checks necessary for a backend ECS to be considered healthy.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p7746215163516"><a name="p7746215163516"></a><a name="p7746215163516"></a>3</p>
    </td>
    </tr>
    <tr id="row51204614184116"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p53302206184122"><a name="p53302206184122"></a><a name="p53302206184122"></a>Unhealthy Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p37642080163512"><a name="p37642080163512"></a><a name="p37642080163512"></a>Specifies the number of consecutive failed health checks necessary for a backend ECS to be considered unhealthy.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p32899075163516"><a name="p32899075163516"></a><a name="p32899075163516"></a>3</p>
    </td>
    </tr>
    <tr id="row30656460163438"><td class="cellrowborder" valign="top" width="24.68%" headers="mcps1.2.4.1.1 "><p id="p7472684163438"><a name="p7472684163438"></a><a name="p7472684163438"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.4.1.2 "><p id="p1307686163438"><a name="p1307686163438"></a><a name="p1307686163438"></a>Specifies the health check URL. This parameter is available only when <strong id="b705955918174030"><a name="b705955918174030"></a><a name="b705955918174030"></a>Health Check Protocol</strong>&nbsp;is set to&nbsp;<strong id="b372029376113510"><a name="b372029376113510"></a><a name="b372029376113510"></a>HTTP</strong>.</p>
    <div class="note" id="note610554891062"><a name="note610554891062"></a><a name="note610554891062"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p126284931062"><a name="p126284931062"></a><a name="p126284931062"></a>The following special characters can be contained in the URL: -/.%?#&amp;=</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.3 "><p id="p38813732163438"><a name="p38813732163438"></a><a name="p38813732163438"></a>/test.html</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

## Add Backend ECSs<a name="section6956053192937"></a>

You must add running backend ECSs to your listener so that the load balancer can distribute traffic to the ECSs. Perform the following operations to add backend ECSs:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093330017.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  In the  **Listeners** area, locate the row that contains the target listener and click **Add Backend ECS** in the **Operation**  column.
6.  In the displayed  **Add Backend ECS**  dialog box, select the subnet and backend ECSs to be added. You can filter backend ECSs by name or IP address.
7.  Click  **OK**.

## Delete a Load Balancer<a name="section16591966183956"></a>

If you do not need a load balancer any longer, perform the following operations to delete it:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0093340397.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance** page, locate the row that contains the target load balancer, click **More** the **Operation** column, and select **Delete**  from the drop-down list.
5.  In the displayed  **Delete Load Balancer** dialog box, click **OK**.

> ![](public_sys-resources/icon-note.gif) **NOTE:** 

> If the load balancer has listeners associated, delete the listeners first.

## Export Load Balancer Information<a name="section19169366120"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0126233348.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  In the upper right corner of the load balancer list, click  ![](figures/en-us_image_0126233350.png).

