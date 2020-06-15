# Creating a Cluster Instance<a name="dds_02_0008"></a>

## **Scenarios**<a name="en-us_topic_0044018333_section2487181111813"></a>

This section describes how to create a DDS cluster instance of Community Edition on the DDS management console. DDS allows you to tailor your computing resources and storage space to your business needs.

You can use your account to create a maximum of 10 cluster instances. To create more cluster instances, click  ![](figures/icon-box.png)  in the upper right corner of the management console. On the  **Service Quota**  page, click  **Increase Quota**  to apply for quotas.

## **Procedure**<a name="en-us_topic_0044018333_s9b4c275aa7904e16a97104c0e01ccdfc"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click  **Create DB Instance**.
3.  On the displayed page, configure parameters about DB instance specifications. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="en-us_topic_0044018333_table44742889144238"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row59029599144238"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p56471429144242"><a name="en-us_topic_0044018333_p56471429144242"></a><a name="en-us_topic_0044018333_p56471429144242"></a><strong id="en-us_topic_0044018333_b842352706203916"><a name="en-us_topic_0044018333_b842352706203916"></a><a name="en-us_topic_0044018333_b842352706203916"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.95%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p10783049144242"><a name="en-us_topic_0044018333_p10783049144242"></a><a name="en-us_topic_0044018333_p10783049144242"></a><strong id="en-us_topic_0044018333_b84235270611143"><a name="en-us_topic_0044018333_b84235270611143"></a><a name="en-us_topic_0044018333_b84235270611143"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044018333_row171091022720"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p10437142392713"><a name="en-us_topic_0044018333_p10437142392713"></a><a name="en-us_topic_0044018333_p10437142392713"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p544112231276"><a name="en-us_topic_0044018333_p544112231276"></a><a name="en-us_topic_0044018333_p544112231276"></a>A region where the tenant is located. It can be changed in the upper left corner. For details, see section <a href="regions-and-azs.md">Regions and AZs</a>.</p>
    <div class="note" id="en-us_topic_0044018333_note1644622312714"><a name="en-us_topic_0044018333_note1644622312714"></a><a name="en-us_topic_0044018333_note1644622312714"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0044018333_p44521230278"><a name="en-us_topic_0044018333_p44521230278"></a><a name="en-us_topic_0044018333_p44521230278"></a>DB instances in different regions cannot communicate with each other through a private network, and you cannot change the region of a DB instance once it is created. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row806550594126"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p4932615094126"><a name="en-us_topic_0044018333_p4932615094126"></a><a name="en-us_topic_0044018333_p4932615094126"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p6999412127"><a name="en-us_topic_0044018333_p6999412127"></a><a name="en-us_topic_0044018333_p6999412127"></a>The DB instance name can be 4 to 64 characters long. It must start with a letter and can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
    <p id="en-us_topic_0044018333_p5238108111215"><a name="en-us_topic_0044018333_p5238108111215"></a><a name="en-us_topic_0044018333_p5238108111215"></a>After the DB instance is created, you can change the DB instance name. For details, see section <a href="modifying-the-db-instance-name.md">Modifying the DB Instance Name</a>.</p>
    <p id="en-us_topic_0044018333_p598401171217"><a name="en-us_topic_0044018333_p598401171217"></a><a name="en-us_topic_0044018333_p598401171217"></a></p>
    <p id="en-us_topic_0044018333_p3599522894126"><a name="en-us_topic_0044018333_p3599522894126"></a><a name="en-us_topic_0044018333_p3599522894126"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1921417431412"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p15134121641411"><a name="en-us_topic_0044018333_p15134121641411"></a><a name="en-us_topic_0044018333_p15134121641411"></a>Database Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p61351416131417"><a name="en-us_topic_0044018333_p61351416131417"></a><a name="en-us_topic_0044018333_p61351416131417"></a>Community Edition</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1013512731419"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p151351316101415"><a name="en-us_topic_0044018333_p151351316101415"></a><a name="en-us_topic_0044018333_p151351316101415"></a>DB Instance Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p0135181618149"><a name="en-us_topic_0044018333_p0135181618149"></a><a name="en-us_topic_0044018333_p0135181618149"></a>Select <strong id="en-us_topic_0044018333_b842352706152955"><a name="en-us_topic_0044018333_b842352706152955"></a><a name="en-us_topic_0044018333_b842352706152955"></a>Cluster</strong>.</p>
    <p id="en-us_topic_0044018333_p11135716181417"><a name="en-us_topic_0044018333_p11135716181417"></a><a name="en-us_topic_0044018333_p11135716181417"></a>A cluster instance includes three types of nodes: mongos, shard, and config. shard and config use the three-node replica set architecture to ensure high availability.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1024495916243"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p2453532616243"><a name="en-us_topic_0044018333_p2453532616243"></a><a name="en-us_topic_0044018333_p2453532616243"></a>Compatible MongoDB Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0044018333_ul13968139192117"></a><a name="en-us_topic_0044018333_ul13968139192117"></a><ul id="en-us_topic_0044018333_ul13968139192117"><li>3.4</li><li>3.2</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row319181316237"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p1672886816349"><a name="en-us_topic_0044018333_p1672886816349"></a><a name="en-us_topic_0044018333_p1672886816349"></a>Storage Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1286106916349"><a name="en-us_topic_0044018333_p1286106916349"></a><a name="en-us_topic_0044018333_p1286106916349"></a>WiredTiger</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row9142051182617"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p440150182715"><a name="en-us_topic_0044018333_p440150182715"></a><a name="en-us_topic_0044018333_p440150182715"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p3478012711"><a name="en-us_topic_0044018333_p3478012711"></a><a name="en-us_topic_0044018333_p3478012711"></a>A physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through the internal network. For details, see section <a href="regions-and-azs.md">Regions and AZs</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row48121472104319"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p5525166104319"><a name="en-us_topic_0044018333_p5525166104319"></a><a name="en-us_topic_0044018333_p5525166104319"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0044018333_ul133881550588"></a><a name="en-us_topic_0044018333_ul133881550588"></a><ul id="en-us_topic_0044018333_ul133881550588"><li><strong id="en-us_topic_0044018333_b842352706102944"><a name="en-us_topic_0044018333_b842352706102944"></a><a name="en-us_topic_0044018333_b842352706102944"></a>Disable</strong>: Disable the encryption function.</li><li><strong id="en-us_topic_0044018333_b6660771592"><a name="en-us_topic_0044018333_b6660771592"></a><a name="en-us_topic_0044018333_b6660771592"></a>Enable</strong>: Enable the encryption function. This feature improves data security but slightly affects read/write performance.<p id="en-us_topic_0044018333_p1950185719127"><a name="en-us_topic_0044018333_p1950185719127"></a><a name="en-us_topic_0044018333_p1950185719127"></a><strong id="en-us_topic_0044018333_b842352706103156"><a name="en-us_topic_0044018333_b842352706103156"></a><a name="en-us_topic_0044018333_b842352706103156"></a>Key Name</strong>: Select or create a private key, which is the tenant key.</p>
    <div class="note" id="en-us_topic_0044018333_note2431518191315"><a name="en-us_topic_0044018333_note2431518191315"></a><a name="en-us_topic_0044018333_note2431518191315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0044018333_ul1362121393110"></a><a name="en-us_topic_0044018333_ul1362121393110"></a><ul id="en-us_topic_0044018333_ul1362121393110"><li>After a DB instance is created, the disk encryption status and the key cannot be changed. Backup data stored on OBS is not encrypted.</li><li>The key cannot be disabled or deleted when being used. Otherwise, the database becomes unavailable.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="en-us_topic_0044018333_i84235269720595"><a name="en-us_topic_0044018333_i84235269720595"></a><a name="en-us_topic_0044018333_i84235269720595"></a>Key Management Service User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Specifications

    <a name="en-us_topic_0044018333_table37562116173420"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row14398999173420"><th class="cellrowborder" valign="top" width="26.029999999999998%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p7826959173420"><a name="en-us_topic_0044018333_p7826959173420"></a><a name="en-us_topic_0044018333_p7826959173420"></a><strong id="en-us_topic_0044018333_b84235270616571"><a name="en-us_topic_0044018333_b84235270616571"></a><a name="en-us_topic_0044018333_b84235270616571"></a>Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="73.97%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p30003927173420"><a name="en-us_topic_0044018333_p30003927173420"></a><a name="en-us_topic_0044018333_p30003927173420"></a><strong id="en-us_topic_0044018333_b84235270611143_1"><a name="en-us_topic_0044018333_b84235270611143_1"></a><a name="en-us_topic_0044018333_b84235270611143_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044018333_row26958383161127"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p17841537161129"><a name="en-us_topic_0044018333_p17841537161129"></a><a name="en-us_topic_0044018333_p17841537161129"></a>mongos class</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p8316353151114"><a name="en-us_topic_0044018333_p8316353151114"></a><a name="en-us_topic_0044018333_p8316353151114"></a>For details about the mongos CPU and memory, see section <a href="db-instance-specifications.md">DB Instance Specifications</a>. After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-the-cpu-or-memory-of-a-cluster-db-instance.md">Changing the CPU or Memory of a Cluster DB Instance</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row66640864173420"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p44330033173420"><a name="en-us_topic_0044018333_p44330033173420"></a><a name="en-us_topic_0044018333_p44330033173420"></a>mongos quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1202224316210"><a name="en-us_topic_0044018333_p1202224316210"></a><a name="en-us_topic_0044018333_p1202224316210"></a>The value ranges from 2 to 12. After a DB instance is created, you can add nodes. For details, see section <a href="adding-cluster-instance-nodes.md">Adding Cluster Instance Nodes</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row4199175144117"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p1019925110415"><a name="en-us_topic_0044018333_p1019925110415"></a><a name="en-us_topic_0044018333_p1019925110415"></a>mongos parameter group</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p683830114214"><a name="en-us_topic_0044018333_p683830114214"></a><a name="en-us_topic_0044018333_p683830114214"></a>Parameters in a mongos parameter group can be applied to mongos nodes. After a DB instance is created, you can change the parameter group of a node. For a parameter group created by users, you can modify the parameters in the parameter group to bring out the best performance.</p>
    <p id="en-us_topic_0044018333_p3859309423"><a name="en-us_topic_0044018333_p3859309423"></a><a name="en-us_topic_0044018333_p3859309423"></a></p>
    <p id="en-us_topic_0044018333_p159333074217"><a name="en-us_topic_0044018333_p159333074217"></a><a name="en-us_topic_0044018333_p159333074217"></a></p>
    <p id="en-us_topic_0044018333_p109814306422"><a name="en-us_topic_0044018333_p109814306422"></a><a name="en-us_topic_0044018333_p109814306422"></a>For details, see <a href="parameter_group.rst">Parameter Group</a>.</p>
    <p id="en-us_topic_0044018333_p51021730164220"><a name="en-us_topic_0044018333_p51021730164220"></a><a name="en-us_topic_0044018333_p51021730164220"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row64196077161527"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p2623062161145"><a name="en-us_topic_0044018333_p2623062161145"></a><a name="en-us_topic_0044018333_p2623062161145"></a>shard class</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p124791914161416"><a name="en-us_topic_0044018333_p124791914161416"></a><a name="en-us_topic_0044018333_p124791914161416"></a>For details about the shard CPU and memory, see section <a href="db-instance-specifications.md">DB Instance Specifications</a>. After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-the-cpu-or-memory-of-a-cluster-db-instance.md">Changing the CPU or Memory of a Cluster DB Instance</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row11977076161542"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p64228766161542"><a name="en-us_topic_0044018333_p64228766161542"></a><a name="en-us_topic_0044018333_p64228766161542"></a>shard storage type</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p35147592161542"><a name="en-us_topic_0044018333_p35147592161542"></a><a name="en-us_topic_0044018333_p35147592161542"></a>Ultra-high I/O: uses the SSD disk type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row39980177161751"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p48504283161751"><a name="en-us_topic_0044018333_p48504283161751"></a><a name="en-us_topic_0044018333_p48504283161751"></a>shard storage space</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p36532839161751"><a name="en-us_topic_0044018333_p36532839161751"></a><a name="en-us_topic_0044018333_p36532839161751"></a>The value ranges from 10 GB to 1,000 GB and must be a multiple of 10. After a DB instance is created, you can scale up its storage space. For details, see section <a href="scaling-up-storage-space.md">Scaling Up Storage Space</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row23608369161415"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p66216679161417"><a name="en-us_topic_0044018333_p66216679161417"></a><a name="en-us_topic_0044018333_p66216679161417"></a>shard quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p61950772161417"><a name="en-us_topic_0044018333_p61950772161417"></a><a name="en-us_topic_0044018333_p61950772161417"></a>shard stores user data but cannot be accessed directly by you.</p>
    <p id="en-us_topic_0044018333_p20686038161417"><a name="en-us_topic_0044018333_p20686038161417"></a><a name="en-us_topic_0044018333_p20686038161417"></a>The value ranges from 2 to 12. After a DB instance is created, you can add nodes. For details, see section <a href="adding-cluster-instance-nodes.md">Adding Cluster Instance Nodes</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row6818135531813"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p0255959111818"><a name="en-us_topic_0044018333_p0255959111818"></a><a name="en-us_topic_0044018333_p0255959111818"></a>shard parameter group</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p172599594184"><a name="en-us_topic_0044018333_p172599594184"></a><a name="en-us_topic_0044018333_p172599594184"></a>Parameters in a shard parameter group can be applied to shard nodes. After a DB instance is created, you can change the parameter group of a node. For a parameter group created by users, you can modify the parameters in the parameter group to bring out the best performance.</p>
    <p id="en-us_topic_0044018333_p2026212598185"><a name="en-us_topic_0044018333_p2026212598185"></a><a name="en-us_topic_0044018333_p2026212598185"></a></p>
    <p id="en-us_topic_0044018333_p227125961813"><a name="en-us_topic_0044018333_p227125961813"></a><a name="en-us_topic_0044018333_p227125961813"></a></p>
    <p id="en-us_topic_0044018333_p13276135915186"><a name="en-us_topic_0044018333_p13276135915186"></a><a name="en-us_topic_0044018333_p13276135915186"></a>For details, see <a href="parameter_group.rst">Parameter Group</a>.</p>
    <p id="en-us_topic_0044018333_p1028245991812"><a name="en-us_topic_0044018333_p1028245991812"></a><a name="en-us_topic_0044018333_p1028245991812"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row18505060112437"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p37776127112446"><a name="en-us_topic_0044018333_p37776127112446"></a><a name="en-us_topic_0044018333_p37776127112446"></a>config class</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p26784243112437"><a name="en-us_topic_0044018333_p26784243112437"></a><a name="en-us_topic_0044018333_p26784243112437"></a>config stores DB instance configurations but cannot be accessed directly by you. For details, see <a href="db-instance-specifications.md">DB Instance Specifications</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row9232087161643"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p29687954161835"><a name="en-us_topic_0044018333_p29687954161835"></a><a name="en-us_topic_0044018333_p29687954161835"></a>config storage type</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1734412385571"><a name="en-us_topic_0044018333_p1734412385571"></a><a name="en-us_topic_0044018333_p1734412385571"></a>Ultra-high I/O: uses the SSD disk type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row60968540161639"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p33124823161835"><a name="en-us_topic_0044018333_p33124823161835"></a><a name="en-us_topic_0044018333_p33124823161835"></a>config storage space</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p15977346161639"><a name="en-us_topic_0044018333_p15977346161639"></a><a name="en-us_topic_0044018333_p15977346161639"></a>The storage space is 20 GB and cannot be scaled up.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row983324921914"><td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p486620545196"><a name="en-us_topic_0044018333_p486620545196"></a><a name="en-us_topic_0044018333_p486620545196"></a>config parameter group</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.97%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1187015542193"><a name="en-us_topic_0044018333_p1187015542193"></a><a name="en-us_topic_0044018333_p1187015542193"></a>Parameters in a config parameter group can be applied to config nodes. After a DB instance is created, you can change the parameter group of a node. For a parameter group created by users, you can modify the parameters in the parameter group to bring out the best performance.</p>
    <p id="en-us_topic_0044018333_p10872135441912"><a name="en-us_topic_0044018333_p10872135441912"></a><a name="en-us_topic_0044018333_p10872135441912"></a></p>
    <p id="en-us_topic_0044018333_p1887812548192"><a name="en-us_topic_0044018333_p1887812548192"></a><a name="en-us_topic_0044018333_p1887812548192"></a></p>
    <p id="en-us_topic_0044018333_p18883165491918"><a name="en-us_topic_0044018333_p18883165491918"></a><a name="en-us_topic_0044018333_p18883165491918"></a>For details, see <a href="parameter_group.rst">Parameter Group</a>.</p>
    <p id="en-us_topic_0044018333_p588765441911"><a name="en-us_topic_0044018333_p588765441911"></a><a name="en-us_topic_0044018333_p588765441911"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="en-us_topic_0044018333_table2444757717146"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row3494637717146"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p4164999317146"><a name="en-us_topic_0044018333_p4164999317146"></a><a name="en-us_topic_0044018333_p4164999317146"></a><strong id="en-us_topic_0044018333_b842352706101251"><a name="en-us_topic_0044018333_b842352706101251"></a><a name="en-us_topic_0044018333_b842352706101251"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.33%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p1820627417146"><a name="en-us_topic_0044018333_p1820627417146"></a><a name="en-us_topic_0044018333_p1820627417146"></a><strong id="en-us_topic_0044018333_b84235270611143_2"><a name="en-us_topic_0044018333_b84235270611143_2"></a><a name="en-us_topic_0044018333_b84235270611143_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044018333_row626686617146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p2466100817216"><a name="en-us_topic_0044018333_p2466100817216"></a><a name="en-us_topic_0044018333_p2466100817216"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p144151228195610"><a name="en-us_topic_0044018333_p144151228195610"></a><a name="en-us_topic_0044018333_p144151228195610"></a>The VPC to which a <span class="keyword" id="en-us_topic_0044018333_keyword1851815295115"><a name="en-us_topic_0044018333_keyword1851815295115"></a><a name="en-us_topic_0044018333_keyword1851815295115"></a>DB instance</span> belongs isolates networks for different services. It allows user to manage and configure internal networks and change network configuration, simplifying network management. You need to create or select the required VPC. For details on how to create a VPC, see section "Creating a VPC" in the <em id="en-us_topic_0044018333_i842352697152613"><a name="en-us_topic_0044018333_i842352697152613"></a><a name="en-us_topic_0044018333_i842352697152613"></a>Virtual Private Cloud User Guide</em>. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1390275717146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p1264740517216"><a name="en-us_topic_0044018333_p1264740517216"></a><a name="en-us_topic_0044018333_p1264740517216"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1780686617216"><a name="en-us_topic_0044018333_p1780686617216"></a><a name="en-us_topic_0044018333_p1780686617216"></a>A subnet provides dedicated network resources that are logically isolated from other networks, improving network security. After a DB instance is created, you can click the DB instance name and change the private IP address assigned by the subnet to the mongos node on the <strong id="en-us_topic_0044018333_b1889912119222"><a name="en-us_topic_0044018333_b1889912119222"></a><a name="en-us_topic_0044018333_b1889912119222"></a>Basic Information</strong> page.</p>
    <div class="note" id="en-us_topic_0044018333_note4321848124413"><a name="en-us_topic_0044018333_note4321848124413"></a><a name="en-us_topic_0044018333_note4321848124413"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0044018333_p1532211488444"><a name="en-us_topic_0044018333_p1532211488444"></a><a name="en-us_topic_0044018333_p1532211488444"></a>Changing the private IP address of a node will invalidate the previous private IP address. If an EIP is bound to the node, do not unbind the EIP during the change of the private IP address. After the change, the new private IP address is bound to the EIP.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row117043217146"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p2919505317216"><a name="en-us_topic_0044018333_p2919505317216"></a><a name="en-us_topic_0044018333_p2919505317216"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1598907017216"><a name="en-us_topic_0044018333_p1598907017216"></a><a name="en-us_topic_0044018333_p1598907017216"></a>A security group controls access between DDS and other services for security.</p>
    <div class="note" id="en-us_topic_0044018333_note968390917216"><a name="en-us_topic_0044018333_note968390917216"></a><a name="en-us_topic_0044018333_note968390917216"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0044018333_p2004632517216"><a name="en-us_topic_0044018333_p2004632517216"></a><a name="en-us_topic_0044018333_p2004632517216"></a>Ensure that the security group rule you set allows clients to access DB instances. For example, select the TCP protocol with inbound direction, input the default port number <strong id="en-us_topic_0044018333_b106365045794850"><a name="en-us_topic_0044018333_b106365045794850"></a><a name="en-us_topic_0044018333_b106365045794850"></a>8635</strong>, and enter a subnet IP address or select a security group that the DB instance belongs to.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1265332016155"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p252472921519"><a name="en-us_topic_0044018333_p252472921519"></a><a name="en-us_topic_0044018333_p252472921519"></a>SSL</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p125241297153"><a name="en-us_topic_0044018333_p125241297153"></a><a name="en-us_topic_0044018333_p125241297153"></a>Secure Sockets Layer (SSL) certificates set up encrypted connections between clients and servers, preventing data from being tampered with or stolen during transmission.</p>
    <p id="en-us_topic_0044018333_p12524529151515"><a name="en-us_topic_0044018333_p12524529151515"></a><a name="en-us_topic_0044018333_p12524529151515"></a>You can enable SSL to improve data security. After a DB instance is created, you can connect to it in SSL mode. For details, see <a href="connecting-to-a-db-instance-through-a-client(cluster).md">Connecting to a DB Instance Through a Client</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="en-us_topic_0044018333_table5952588817311"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row5051800017311"><th class="cellrowborder" valign="top" width="20.31%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p188968917322"><a name="en-us_topic_0044018333_p188968917322"></a><a name="en-us_topic_0044018333_p188968917322"></a><strong id="en-us_topic_0044018333_b842352706104624"><a name="en-us_topic_0044018333_b842352706104624"></a><a name="en-us_topic_0044018333_b842352706104624"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.69000000000001%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p1884710117322"><a name="en-us_topic_0044018333_p1884710117322"></a><a name="en-us_topic_0044018333_p1884710117322"></a><strong id="en-us_topic_0044018333_b84235270611143_3"><a name="en-us_topic_0044018333_b84235270611143_3"></a><a name="en-us_topic_0044018333_b84235270611143_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044018333_row3306650017311"><td class="cellrowborder" valign="top" width="20.31%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p3543244917347"><a name="en-us_topic_0044018333_p3543244917347"></a><a name="en-us_topic_0044018333_p3543244917347"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.69000000000001%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p53475534163330"><a name="en-us_topic_0044018333_p53475534163330"></a><a name="en-us_topic_0044018333_p53475534163330"></a>The default account is <strong id="en-us_topic_0044018333_b842352706104956"><a name="en-us_topic_0044018333_b842352706104956"></a><a name="en-us_topic_0044018333_b842352706104956"></a>rwuser</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row1140943517311"><td class="cellrowborder" valign="top" width="20.31%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p6477672517347"><a name="en-us_topic_0044018333_p6477672517347"></a><a name="en-us_topic_0044018333_p6477672517347"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.69000000000001%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1242340417347"><a name="en-us_topic_0044018333_p1242340417347"></a><a name="en-us_topic_0044018333_p1242340417347"></a>The password is a string of 8 to 32 characters. It must be a combination of uppercase letters, lowercase letters, digits, and special characters. You can also use the following special characters: ~!@#%^*-_=+?</p>
    <p id="en-us_topic_0044018333_p31488386155011"><a name="en-us_topic_0044018333_p31488386155011"></a><a name="en-us_topic_0044018333_p31488386155011"></a>The system cannot save you password. Keep the password secure.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044018333_row985834117311"><td class="cellrowborder" valign="top" width="20.31%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0044018333_p2259237217347"><a name="en-us_topic_0044018333_p2259237217347"></a><a name="en-us_topic_0044018333_p2259237217347"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.69000000000001%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0044018333_p1804285317347"><a name="en-us_topic_0044018333_p1804285317347"></a><a name="en-us_topic_0044018333_p1804285317347"></a>The value of this parameter must be the same as the <span class="parmname" id="en-us_topic_0044018333_parmname769647905141841"><a name="en-us_topic_0044018333_parmname769647905141841"></a><a name="en-us_topic_0044018333_parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Tag

    <a name="en-us_topic_0044018333_table167699362520"></a>
    <table><thead align="left"><tr id="en-us_topic_0044018333_row87709361053"><th class="cellrowborder" valign="top" width="20.9%" id="mcps1.2.3.1.1"><p id="en-us_topic_0044018333_p1770836856"><a name="en-us_topic_0044018333_p1770836856"></a><a name="en-us_topic_0044018333_p1770836856"></a><strong id="en-us_topic_0044018333_b842352706203916_1"><a name="en-us_topic_0044018333_b842352706203916_1"></a><a name="en-us_topic_0044018333_b842352706203916_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.10000000000001%" id="mcps1.2.3.1.2"><p id="en-us_topic_0044018333_p4770136655"><a name="en-us_topic_0044018333_p4770136655"></a><a name="en-us_topic_0044018333_p4770136655"></a><strong id="en-us_topic_0044018333_b84235270611143_4"><a name="en-us_topic_0044018333_b84235270611143_4"></a><a name="en-us_topic_0044018333_b84235270611143_4"></a>Description</strong></p>
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
    >DB instance performance is determined by the configurations you set during its creation, including the node class and storage space.  

4.  On the displayed page, confirm the DB instance information.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.
    -   If you do not need to modify the specifications, click  **Submit**  to start the instance creation.

5.  After a DDS DB instance is created, you can view and manage it on the  **Instance Management**  page.
    -   When a DB instance is being created, the status displayed in the  **Status**  column is  **Creating**. This process takes about 15 minutes. After the creation is complete, the status changes to  **Available**.
    -   DDS enables the automated backup policy by default. After a DB instance is created, you can modify or disable the automated backup policy. An automated full backup is immediately triggered after the creation of a DB instance.
    -   You can change the database port after the DB instance is created. DDS uses port 8635 by default, which is different from the default port numbers used by databases. To ensure database accessibility, you need to add the required security group rule.


