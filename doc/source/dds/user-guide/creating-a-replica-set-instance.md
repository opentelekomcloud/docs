# Creating a Replica Set Instance<a name="dds_02_0012"></a>

## **Scenarios**<a name="section2487181111813"></a>

This section describes how to create a DDS replica set instance on the DDS management console. DDS allows you to tailor your computing resources and storage space to your business needs.

You can use your account to create a maximum of 50 replica set instances in total. To create more replica set instances, click  ![](figures/icon-box.png)  in the upper right corner of the management console. On the  **Service Quota**  page, click  **Increase Quota**  to apply for quotas.

## **Procedure**<a name="s9b4c275aa7904e16a97104c0e01ccdfc"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click  **Create DB Instance**.
3.  On the displayed page, configure parameters about DB instance specifications. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="table44742889144238"></a>
    <table><thead align="left"><tr id="row59029599144238"><th class="cellrowborder" valign="top" width="21.07%" id="mcps1.2.3.1.1"><p id="p56471429144242"><a name="p56471429144242"></a><a name="p56471429144242"></a><strong id="b937447505"><a name="b937447505"></a><a name="b937447505"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.93%" id="mcps1.2.3.1.2"><p id="p10783049144242"><a name="p10783049144242"></a><a name="p10783049144242"></a><strong id="b1968488907"><a name="b1968488907"></a><a name="b1968488907"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row155118279120"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p140103421218"><a name="p140103421218"></a><a name="p140103421218"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p13053412128"><a name="p13053412128"></a><a name="p13053412128"></a>A region where the tenant is located. It can be changed in the upper left corner. For details, see section <a href="regions-and-azs.md">Regions and AZs</a>.</p>
    <div class="note" id="note180234201217"><a name="note180234201217"></a><a name="note180234201217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9033416124"><a name="p9033416124"></a><a name="p9033416124"></a>DB instances in different regions cannot communicate with each other through a private network, and you cannot change the region of a DB instance once it is created. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row16393318102629"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p52790420102629"><a name="p52790420102629"></a><a name="p52790420102629"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p1437847164010"><a name="p1437847164010"></a><a name="p1437847164010"></a>The DB instance name can be 4 to 64 characters long. It must start with a letter and can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p167504101407"><a name="p167504101407"></a><a name="p167504101407"></a>After the DB instance is created, you can change the DB instance name. For details, see section <a href="modifying-the-db-instance-name.md">Modifying the DB Instance Name</a>.</p>
    <p id="p94691413124020"><a name="p94691413124020"></a><a name="p94691413124020"></a></p>
    <p id="p48165638102629"><a name="p48165638102629"></a><a name="p48165638102629"></a></p>
    </td>
    </tr>
    <tr id="row1299919472715"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p1858165811711"><a name="p1858165811711"></a><a name="p1858165811711"></a>Database Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p35812581376"><a name="p35812581376"></a><a name="p35812581376"></a>Community Edition</p>
    </td>
    </tr>
    <tr id="row770112444713"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p55829581273"><a name="p55829581273"></a><a name="p55829581273"></a>DB Instance Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p25822058578"><a name="p25822058578"></a><a name="p25822058578"></a>Select <strong id="b842352706144558"><a name="b842352706144558"></a><a name="b842352706144558"></a>Replica set</strong>.</p>
    <p id="p195829587717"><a name="p195829587717"></a><a name="p195829587717"></a>A replica set consists of the primary node, secondary node, and hidden node. If a primary node goes down or becomes faulty, a secondary node is automatically assigned to the primary role and continues normal operation. If a secondary node is unavailable, a hidden node will take the role of the secondary to ensure high availability.</p>
    </td>
    </tr>
    <tr id="row1024495916243"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p2453532616243"><a name="p2453532616243"></a><a name="p2453532616243"></a>Compatible MongoDB Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><a name="ul13968139192117"></a><a name="ul13968139192117"></a><ul id="ul13968139192117"><li>3.4</li><li>3.2</li></ul>
    </td>
    </tr>
    <tr id="row319181316237"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p1672886816349"><a name="p1672886816349"></a><a name="p1672886816349"></a>Storage Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p1286106916349"><a name="p1286106916349"></a><a name="p1286106916349"></a>WiredTiger</p>
    </td>
    </tr>
    <tr id="row1718594414286"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p689112494285"><a name="p689112494285"></a><a name="p689112494285"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><p id="p38941449182817"><a name="p38941449182817"></a><a name="p38941449182817"></a>A physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through the internal network. For details, see section <a href="regions-and-azs.md">Regions and AZs</a>.</p>
    <p id="p28961549142817"><a name="p28961549142817"></a><a name="p28961549142817"></a>An instance can be deployed in one AZ or three AZs. If three AZs are deployed across three AZs, the primary, secondary, and hidden nodes are deployed in three AZs for high availability.</p>
    </td>
    </tr>
    <tr id="row41307396112018"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.3.1.1 "><p id="p57564751112018"><a name="p57564751112018"></a><a name="p57564751112018"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.93%" headers="mcps1.2.3.1.2 "><a name="ul133881550588"></a><a name="ul133881550588"></a><ul id="ul133881550588"><li><strong id="b842352706102944"><a name="b842352706102944"></a><a name="b842352706102944"></a>Disable</strong>: Disable the encryption function.</li><li><strong id="b84235270610302"><a name="b84235270610302"></a><a name="b84235270610302"></a>Enable</strong>: Enable the encryption function. This feature improves data security but slightly affects read/write performance.<p id="p1950185719127"><a name="p1950185719127"></a><a name="p1950185719127"></a><strong id="b842352706103156"><a name="b842352706103156"></a><a name="b842352706103156"></a>Key Name</strong>: Select or create a private key, which is the tenant key.</p>
    <div class="note" id="note2431518191315"><a name="note2431518191315"></a><a name="note2431518191315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0044018333_ul1362121393110"></a><a name="en-us_topic_0044018333_ul1362121393110"></a><ul id="en-us_topic_0044018333_ul1362121393110"><li>After a DB instance is created, the disk encryption status and the key cannot be changed. Backup data stored on OBS is not encrypted.</li><li>The key cannot be disabled or deleted when being used. Otherwise, the database becomes unavailable.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="en-us_topic_0044018333_i84235269720595"><a name="en-us_topic_0044018333_i84235269720595"></a><a name="en-us_topic_0044018333_i84235269720595"></a>Key Management Service User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Specifications

    <a name="table37562116173420"></a>
    <table><thead align="left"><tr id="row14398999173420"><th class="cellrowborder" valign="top" width="21.14%" id="mcps1.2.3.1.1"><p id="p7826959173420"><a name="p7826959173420"></a><a name="p7826959173420"></a><strong id="b84235270616571"><a name="b84235270616571"></a><a name="b84235270616571"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.86%" id="mcps1.2.3.1.2"><p id="p30003927173420"><a name="p30003927173420"></a><a name="p30003927173420"></a><strong id="b496059865"><a name="b496059865"></a><a name="b496059865"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26958383161127"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.3.1.1 "><p id="p17841537161129"><a name="p17841537161129"></a><a name="p17841537161129"></a>Node Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.86%" headers="mcps1.2.3.1.2 "><p id="p8316353151114"><a name="p8316353151114"></a><a name="p8316353151114"></a>For details about the DB instance specifications, see section <a href="db-instance-specifications.md">DB Instance Specifications</a>. After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-the-cpu-or-memory-of-a-replica-set-db-instance.md">Changing the CPU or Memory of a Replica Set DB Instance</a>.</p>
    </td>
    </tr>
    <tr id="row11977076161542"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.3.1.1 "><p id="p64228766161542"><a name="p64228766161542"></a><a name="p64228766161542"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.86%" headers="mcps1.2.3.1.2 "><p id="p35147592161542"><a name="p35147592161542"></a><a name="p35147592161542"></a>Ultra-high I/O: uses the SSD disk type.</p>
    </td>
    </tr>
    <tr id="row39980177161751"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.3.1.1 "><p id="p48504283161751"><a name="p48504283161751"></a><a name="p48504283161751"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.86%" headers="mcps1.2.3.1.2 "><p id="p36532839161751"><a name="p36532839161751"></a><a name="p36532839161751"></a>Ranges from 10 GB to 2,000 GB. The value must be a multiple of 10.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="table2444757717146"></a>
    <table><thead align="left"><tr id="row3494637717146"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.3.1.1"><p id="p4164999317146"><a name="p4164999317146"></a><a name="p4164999317146"></a><strong id="b842352706101251"><a name="b842352706101251"></a><a name="b842352706101251"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.33%" id="mcps1.2.3.1.2"><p id="p1820627417146"><a name="p1820627417146"></a><a name="p1820627417146"></a><strong id="b137435044"><a name="b137435044"></a><a name="b137435044"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row626686617146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p2466100817216"><a name="p2466100817216"></a><a name="p2466100817216"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p144151228195610"><a name="p144151228195610"></a><a name="p144151228195610"></a>The VPC to which a <span class="keyword" id="keyword253311558518"><a name="keyword253311558518"></a><a name="keyword253311558518"></a>DB instance</span> belongs isolates networks for different services. It allows user to manage and configure internal networks and change network configuration, simplifying network management. You need to create or select the required VPC. For details on how to create a VPC, see section "Creating a VPC" in the <em id="i842352697152613"><a name="i842352697152613"></a><a name="i842352697152613"></a>Virtual Private Cloud User Guide</em>. </p>
    </td>
    </tr>
    <tr id="row1390275717146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p1264740517216"><a name="p1264740517216"></a><a name="p1264740517216"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p1780686617216"><a name="p1780686617216"></a><a name="p1780686617216"></a>A subnet provides dedicated network resources that are logically isolated from other networks, improving network security. After a DB instance is created, you can click the DB instance name and change the private IP address assigned by the subnet to the node on the <strong id="b18139822105614"><a name="b18139822105614"></a><a name="b18139822105614"></a>Basic Information</strong> page.</p>
    <div class="note" id="note4321848124413"><a name="note4321848124413"></a><a name="note4321848124413"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1532211488444"><a name="p1532211488444"></a><a name="p1532211488444"></a>Changing the private IP address of a node will invalidate the previous private IP address. If an EIP is bound to the node, do not unbind the EIP during the change of the private IP address. After the change, the new private IP address is bound to the EIP.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row117043217146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p2919505317216"><a name="p2919505317216"></a><a name="p2919505317216"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p1598907017216"><a name="p1598907017216"></a><a name="p1598907017216"></a>A security group controls access between DDS and other services for security.</p>
    <div class="note" id="note968390917216"><a name="note968390917216"></a><a name="note968390917216"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2004632517216"><a name="p2004632517216"></a><a name="p2004632517216"></a>Ensure that the security group rule you set allows clients to access DB instances. For example, select the TCP protocol with inbound direction, input the default port number <strong id="b72325208594834"><a name="b72325208594834"></a><a name="b72325208594834"></a>8635</strong>, and enter a subnet IP address or select a security group that the DB instance belongs to.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1914874614915"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p1698018495912"><a name="p1698018495912"></a><a name="p1698018495912"></a>SSL</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p2098014493920"><a name="p2098014493920"></a><a name="p2098014493920"></a>Secure Sockets Layer (SSL) certificates set up encrypted connections between clients and servers, preventing data from being tampered with or stolen during transmission.</p>
    <p id="p898054917919"><a name="p898054917919"></a><a name="p898054917919"></a>You can enable SSL to improve data security. After a DB instance is created, you can connect to it in SSL mode. For details, see <a href="connecting-to-a-db-instance-through-a-client(replica-set).md">Connecting to a DB Instance Through a Client</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="table5952588817311"></a>
    <table><thead align="left"><tr id="row5051800017311"><th class="cellrowborder" valign="top" width="20.68%" id="mcps1.2.3.1.1"><p id="p188968917322"><a name="p188968917322"></a><a name="p188968917322"></a><strong id="b842352706104624"><a name="b842352706104624"></a><a name="b842352706104624"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.32000000000001%" id="mcps1.2.3.1.2"><p id="p1884710117322"><a name="p1884710117322"></a><a name="p1884710117322"></a><strong id="b1936729273"><a name="b1936729273"></a><a name="b1936729273"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3306650017311"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.3.1.1 "><p id="p3543244917347"><a name="p3543244917347"></a><a name="p3543244917347"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.32000000000001%" headers="mcps1.2.3.1.2 "><p id="p53475534163330"><a name="p53475534163330"></a><a name="p53475534163330"></a>The default account is <strong id="b842352706104956"><a name="b842352706104956"></a><a name="b842352706104956"></a>rwuser</strong>.</p>
    </td>
    </tr>
    <tr id="row1140943517311"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.3.1.1 "><p id="p6477672517347"><a name="p6477672517347"></a><a name="p6477672517347"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.32000000000001%" headers="mcps1.2.3.1.2 "><p id="p1242340417347"><a name="p1242340417347"></a><a name="p1242340417347"></a>The password is a string of 8 to 32 characters. It must be a combination of uppercase letters, lowercase letters, digits, and special characters. You can also use the following special characters: ~!@#%^*-_=+?</p>
    <p id="p6009326415510"><a name="p6009326415510"></a><a name="p6009326415510"></a>The system cannot save you password. Keep the password secure.</p>
    </td>
    </tr>
    <tr id="row985834117311"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.3.1.1 "><p id="p2259237217347"><a name="p2259237217347"></a><a name="p2259237217347"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.32000000000001%" headers="mcps1.2.3.1.2 "><p id="p1804285317347"><a name="p1804285317347"></a><a name="p1804285317347"></a>The value of this parameter must be the same as the <span class="parmname" id="parmname769647905141841"><a name="parmname769647905141841"></a><a name="parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    <tr id="row1420914884618"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.3.1.1 "><p id="p824433220487"><a name="p824433220487"></a><a name="p824433220487"></a>Replica Set Parameter Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.32000000000001%" headers="mcps1.2.3.1.2 "><p id="p224416324488"><a name="p224416324488"></a><a name="p224416324488"></a>The parameters in the replica set parameter group are applied to replica set instances. After a DB instance is created, you can change the parameter group of the instance. For a parameter group created by users, you can modify the parameters in the parameter group to bring out the best performance.</p>
    <p id="p32441832124814"><a name="p32441832124814"></a><a name="p32441832124814"></a></p>
    <p id="p4245123211487"><a name="p4245123211487"></a><a name="p4245123211487"></a></p>
    <p id="p42451732184819"><a name="p42451732184819"></a><a name="p42451732184819"></a>For details, see <a href="parameter_group.rst">Parameter Group</a>.</p>
    <p id="p224513216489"><a name="p224513216489"></a><a name="p224513216489"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Tag

    <a name="table3731123516113"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row87709361053"><th class="cellrowborder" valign="top" width="20.9%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p1770836856"><a name="en-us_topic_0044018333_p1770836856"></a><a name="en-us_topic_0044018333_p1770836856"></a><strong id="en-us_topic_0044018333_b842352706203916"><a name="en-us_topic_0044018333_b842352706203916"></a><a name="en-us_topic_0044018333_b842352706203916"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.10000000000001%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p4770136655"><a name="en-us_topic_0044018333_p4770136655"></a><a name="en-us_topic_0044018333_p4770136655"></a><strong id="en-us_topic_0044018333_b84235270611143"><a name="en-us_topic_0044018333_b84235270611143"></a><a name="en-us_topic_0044018333_b84235270611143"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044018333_row18770336259"><td class="cellrowborder" valign="top" width="20.9%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p1221015159617"><a name="en-us_topic_0044018333_p1221015159617"></a><a name="en-us_topic_0044018333_p1221015159617"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.10000000000001%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p42130153614"><a name="en-us_topic_0044018333_p42130153614"></a><a name="en-us_topic_0044018333_p42130153614"></a>Tags a DDS DB instance. This configuration is optional. Adding tags to DDS DB instances helps you better identify and manage them. A maximum of 10 tags can be added for a DB instance.</p>
    <p id="en-us_topic_0044018333_p791635119297"><a name="en-us_topic_0044018333_p791635119297"></a><a name="en-us_topic_0044018333_p791635119297"></a>A tag is composed of a key-value pair.</p>
    <a name="en-us_topic_0044018333_ul73781026122214"></a><a name="en-us_topic_0044018333_ul73781026122214"></a><ul id="en-us_topic_0044018333_ul73781026122214"><li>Key: Mandatory if the DB instance is going to be tagged<a name="en-us_topic_0044018333_ul638611265223"></a><a name="en-us_topic_0044018333_ul638611265223"></a><ul id="en-us_topic_0044018333_ul638611265223"><li>For each DB instance, each tag key is unique.</li><li>A tag key consists of a maximum of 36 characters.</li><li>The key can only consist of digits, letters, underscores (_), and hyphens (-).</li></ul>
    </li><li>Value: Optional if the DB instance is going to be tagged<a name="en-us_topic_0044018333_ul1641092614228"></a><a name="en-us_topic_0044018333_ul1641092614228"></a><ul id="en-us_topic_0044018333_ul1641092614228"><li>The value consists of a maximum of 43 characters.</li><li>The value can only consist of digits, letters, underscores (_), and hyphens (-).</li></ul>
    </li></ul>
    <p id="en-us_topic_0044018333_p621481510618"><a name="en-us_topic_0044018333_p621481510618"></a><a name="en-us_topic_0044018333_p621481510618"></a>After a DB instance is created, you can view its tag details on the <strong id="en-us_topic_0044018333_b1468912272147"><a name="en-us_topic_0044018333_b1468912272147"></a><a name="en-us_topic_0044018333_b1468912272147"></a>Tags</strong> tab. In addition, you can add, modify, and delete tags for existing DB instances. For details, see <a href="tag.md">Tag</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >The performance of your DB instance is determined by how you configure it during the creation. The hardware configuration items that can be selected include the class and storage space of the replica set.  

4.  On the displayed page, confirm the DB instance information.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.
    -   If you do not need to modify the specifications, click  **Submit**  to start the instance creation.

5.  After a DDS DB instance is created, you can view and manage it on the  **Instance Management**  page.
    -   When a DB instance is being created, the status displayed in the  **Status**  column is  **Creating**. This process takes about 15 minutes. After the creation is complete, the status changes to  **Available**.
    -   DDS enables the automated backup policy by default. After a DB instance is created, you can modify or disable the automated backup policy. An automated full backup is immediately triggered after the creation of a DB instance.
    -   You can change the database port after the DB instance is created. DDS uses port 8635 by default, which is different from the default port numbers used by databases. To ensure database accessibility, you need to add the required security group rule.


