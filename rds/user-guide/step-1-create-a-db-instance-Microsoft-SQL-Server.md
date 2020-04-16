# Step 1: Create a DB Instance<a name="rds_03_0012"></a>

## **Scenarios**<a name="en-us_topic_0053089697_sbcaab6a7fb3345dea860ce4eef037052"></a>

You can create DB instances using the RDS console or APIs. For details about how to create DB instances using APIs, see the "Creating a DB Instance" section in the  _Relational Database Service API Reference_. This section describes how to  create a DB instance  on the RDS console.

The DB instance class and storage space you need depends on your processing power and memory requirements.

## Procedure<a name="en-us_topic_0053089697_s079b76f81e474df9a2c7acbc17dffd61"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click  **Create DB Instance**.
5.  On the displayed page, configure information about your DB instance. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="en-us_topic_0053089697_table96132401149"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row06139409140"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p0613174016148"><a name="en-us_topic_0053089697_p0613174016148"></a><a name="en-us_topic_0053089697_p0613174016148"></a><strong id="en-us_topic_0053089697_b84235270618284"><a name="en-us_topic_0053089697_b84235270618284"></a><a name="en-us_topic_0053089697_b84235270618284"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p1061364061416"><a name="en-us_topic_0053089697_p1061364061416"></a><a name="en-us_topic_0053089697_p1061364061416"></a><strong id="en-us_topic_0053089697_b842352706212013"><a name="en-us_topic_0053089697_b842352706212013"></a><a name="en-us_topic_0053089697_b842352706212013"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row06131640161411"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p12613164012146"><a name="en-us_topic_0053089697_p12613164012146"></a><a name="en-us_topic_0053089697_p12613164012146"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p32572714488"><a name="en-us_topic_0053089697_p32572714488"></a><a name="en-us_topic_0053089697_p32572714488"></a>A region where the tenant is located. It can be changed in the upper left corner of the page.</p>
    <div class="note" id="en-us_topic_0053089697_note12403733192620"><a name="en-us_topic_0053089697_note12403733192620"></a><a name="en-us_topic_0053089697_note12403733192620"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0053089697_p1740443312265"><a name="en-us_topic_0053089697_p1740443312265"></a><a name="en-us_topic_0053089697_p1740443312265"></a>Products in different regions cannot communicate with each other through a private network and you cannot change the region of a DB instance after creating the instance. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row1761304011141"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1761314405141"><a name="en-us_topic_0053089697_p1761314405141"></a><a name="en-us_topic_0053089697_p1761314405141"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p95081131748"><a name="en-us_topic_0053089697_p95081131748"></a><a name="en-us_topic_0053089697_p95081131748"></a>Must start with a letter and consist of 4 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row861314409141"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p261314020144"><a name="en-us_topic_0053089697_p261314020144"></a><a name="en-us_topic_0053089697_p261314020144"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p1961314012142"><a name="en-us_topic_0053089697_p1961314012142"></a><a name="en-us_topic_0053089697_p1961314012142"></a>Set to <strong id="en-us_topic_0053089697_b842352706111154"><a name="en-us_topic_0053089697_b842352706111154"></a><a name="en-us_topic_0053089697_b842352706111154"></a>Microsoft SQL Server</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row12613340191412"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1361344012148"><a name="en-us_topic_0053089697_p1361344012148"></a><a name="en-us_topic_0053089697_p1361344012148"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p1742111458236"><a name="en-us_topic_0053089697_p1742111458236"></a><a name="en-us_topic_0053089697_p1742111458236"></a></p>
    <p id="en-us_topic_0053089697_p110755122311"><a name="en-us_topic_0053089697_p110755122311"></a><a name="en-us_topic_0053089697_p110755122311"></a></p>
    <p id="en-us_topic_0053089697_p1225416012240"><a name="en-us_topic_0053089697_p1225416012240"></a><a name="en-us_topic_0053089697_p1225416012240"></a>For details, see section <a href="db-engines-and-versions.md">DB Engines and Versions</a>.</p>
    <p id="en-us_topic_0053089697_p0613184016142"><a name="en-us_topic_0053089697_p0613184016142"></a><a name="en-us_topic_0053089697_p0613184016142"></a></p>
    <p id="en-us_topic_0053089697_p1755071811589"><a name="en-us_topic_0053089697_p1755071811589"></a><a name="en-us_topic_0053089697_p1755071811589"></a>Different DB engine versions are supported in different regions.</p>
    <p id="en-us_topic_0053089697_p320863915612"><a name="en-us_topic_0053089697_p320863915612"></a><a name="en-us_topic_0053089697_p320863915612"></a>If you use a Microsoft SQL Server database, select a proper DB engine version based on service requirements. You are advised to select the latest available version because it is more stable, reliable, and secure.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row20613174014140"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p16131040141416"><a name="en-us_topic_0053089697_p16131040141416"></a><a name="en-us_topic_0053089697_p16131040141416"></a>DB Instance Type and AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0053089697_ul15613144081413"></a><a name="en-us_topic_0053089697_ul15613144081413"></a><ul id="en-us_topic_0053089697_ul15613144081413"><li><strong id="en-us_topic_0053089697_b1690174485015"><a name="en-us_topic_0053089697_b1690174485015"></a><a name="en-us_topic_0053089697_b1690174485015"></a>Primary/Standby</strong>: uses the HA architecture with a primary DB instance and a synchronous standby DB instance. It is suitable for production databases of large- and medium-sized enterprises in Internet, Internet of Things (IoT), retail e-commerce sales, logistics, gaming, and other sectors. The standby DB instance improves instance reliability and is invisible to you after being created.<p id="en-us_topic_0053089697_p919182912162"><a name="en-us_topic_0053089697_p919182912162"></a><a name="en-us_topic_0053089697_p919182912162"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network. </p>
    <p id="en-us_topic_0053089697_p7283142831614"><a name="en-us_topic_0053089697_p7283142831614"></a><a name="en-us_topic_0053089697_p7283142831614"></a>RDS supports deploying primary and standby DB instances in an AZ or across AZs. You can determine whether the standby AZ is the same as the primary AZ.</p>
    <a name="en-us_topic_0053089697_ul13283228181616"></a><a name="en-us_topic_0053089697_ul13283228181616"></a><ul id="en-us_topic_0053089697_ul13283228181616"><li>If they are the same (default setting), the primary and standby DB instances are deployed in the same AZ.</li><li>If they are different, the primary and standby DB instances are deployed in different AZs to ensure failover support and high availability.</li></ul>
    </li><li><strong id="en-us_topic_0053089697_b20217205215020"><a name="en-us_topic_0053089697_b20217205215020"></a><a name="en-us_topic_0053089697_b20217205215020"></a>Single</strong>: uses the single-node architecture, which is more cost-effective than mainstream primary/standby DB instances. It is suitable for developing and testing of microsites, and small- and medium-sized enterprises, or for learning about RDS.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row3613184051411"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p461334001414"><a name="en-us_topic_0053089697_p461334001414"></a><a name="en-us_topic_0053089697_p461334001414"></a>Time Zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p161314071418"><a name="en-us_topic_0053089697_p161314071418"></a><a name="en-us_topic_0053089697_p161314071418"></a>You need to select a time zone for your DB instance according to the longitude and latitude of the region hosting your DB instance. Can be specified only when you create a DB instance and cannot be modified after the DB instance is created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row1260593375214"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1760515335520"><a name="en-us_topic_0053089697_p1760515335520"></a><a name="en-us_topic_0053089697_p1760515335520"></a>Server Collation</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p157171127193116"><a name="en-us_topic_0053089697_p157171127193116"></a><a name="en-us_topic_0053089697_p157171127193116"></a>Defines a collation of a database or table column, or a collation cast operation when applied to character string expression. It acts as the default collation for the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="en-us_topic_0053089697_table2630240101411"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row1163034012144"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p106301040161410"><a name="en-us_topic_0053089697_p106301040161410"></a><a name="en-us_topic_0053089697_p106301040161410"></a><strong id="en-us_topic_0053089697_b57812301143154"><a name="en-us_topic_0053089697_b57812301143154"></a><a name="en-us_topic_0053089697_b57812301143154"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.25999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p063014011145"><a name="en-us_topic_0053089697_p063014011145"></a><a name="en-us_topic_0053089697_p063014011145"></a><strong id="en-us_topic_0053089697_b20033708143154"><a name="en-us_topic_0053089697_b20033708143154"></a><a name="en-us_topic_0053089697_b20033708143154"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row36301740151412"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p8630134031416"><a name="en-us_topic_0053089697_p8630134031416"></a><a name="en-us_topic_0053089697_p8630134031416"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p3612111215507"><a name="en-us_topic_0053089697_p3612111215507"></a><a name="en-us_topic_0053089697_p3612111215507"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="en-us_topic_0053089697_p781114612508"><a name="en-us_topic_0053089697_p781114612508"></a><a name="en-us_topic_0053089697_p781114612508"></a></p>
    <p id="en-us_topic_0053089697_p5429821515"><a name="en-us_topic_0053089697_p5429821515"></a><a name="en-us_topic_0053089697_p5429821515"></a></p>
    <p id="en-us_topic_0053089697_p12042810516"><a name="en-us_topic_0053089697_p12042810516"></a><a name="en-us_topic_0053089697_p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="en-us_topic_0053089697_p4689621196"><a name="en-us_topic_0053089697_p4689621196"></a><a name="en-us_topic_0053089697_p4689621196"></a></p>
    <p id="en-us_topic_0053089697_p860165515523"><a name="en-us_topic_0053089697_p860165515523"></a><a name="en-us_topic_0053089697_p860165515523"></a></p>
    <p id="en-us_topic_0053089697_p4610514532"><a name="en-us_topic_0053089697_p4610514532"></a><a name="en-us_topic_0053089697_p4610514532"></a></p>
    <p id="en-us_topic_0053089697_p19542517536"><a name="en-us_topic_0053089697_p19542517536"></a><a name="en-us_topic_0053089697_p19542517536"></a>After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-a-db-instance-class-86.md">Changing a DB Instance Class</a>.</p>
    <p id="en-us_topic_0053089697_p38285458348"><a name="en-us_topic_0053089697_p38285458348"></a><a name="en-us_topic_0053089697_p38285458348"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row1363024014143"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p963074010141"><a name="en-us_topic_0053089697_p963074010141"></a><a name="en-us_topic_0053089697_p963074010141"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p15371533939"><a name="en-us_topic_0053089697_p15371533939"></a><a name="en-us_topic_0053089697_p15371533939"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="en-us_topic_0053089697_ul45492023191733"></a><a name="en-us_topic_0053089697_ul45492023191733"></a><ul id="en-us_topic_0053089697_ul45492023191733"><li><strong id="en-us_topic_0053089697_b26451717161712"><a name="en-us_topic_0053089697_b26451717161712"></a><a name="en-us_topic_0053089697_b26451717161712"></a>Common I/O</strong>: uses the SATA disk type, with a maximum throughput of 90 MB/s.</li><li><strong id="en-us_topic_0053089697_b18729521101718"><a name="en-us_topic_0053089697_b18729521101718"></a><a name="en-us_topic_0053089697_b18729521101718"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row363084061415"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p126303409148"><a name="en-us_topic_0053089697_p126303409148"></a><a name="en-us_topic_0053089697_p126303409148"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p177851720184018"><a name="en-us_topic_0053089697_p177851720184018"></a><a name="en-us_topic_0053089697_p177851720184018"></a>Contains the system overhead required for inode, reserved block, and database operation. Can range in size from 40 GB to 4000 GB and can be scaled up only by a multiple of 10 GB.</p>
    <p id="en-us_topic_0053089697_p4990256102610"><a name="en-us_topic_0053089697_p4990256102610"></a><a name="en-us_topic_0053089697_p4990256102610"></a></p>
    <p id="en-us_topic_0053089697_p5999151032711"><a name="en-us_topic_0053089697_p5999151032711"></a><a name="en-us_topic_0053089697_p5999151032711"></a></p>
    <p id="en-us_topic_0053089697_p13797182010276"><a name="en-us_topic_0053089697_p13797182010276"></a><a name="en-us_topic_0053089697_p13797182010276"></a>After a DB instance is created, you can scale up its storage space. For details, see section <a href="scaling-up-storage-space.md">Scaling Up Storage Space</a>.</p>
    <p id="en-us_topic_0053089697_p1182820454348"><a name="en-us_topic_0053089697_p1182820454348"></a><a name="en-us_topic_0053089697_p1182820454348"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row121651133419"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p438435219119"><a name="en-us_topic_0053089697_p438435219119"></a><a name="en-us_topic_0053089697_p438435219119"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0053089697_ul33847521015"></a><a name="en-us_topic_0053089697_ul33847521015"></a><ul id="en-us_topic_0053089697_ul33847521015"><li><strong id="en-us_topic_0053089697_b842352706111219"><a name="en-us_topic_0053089697_b842352706111219"></a><a name="en-us_topic_0053089697_b842352706111219"></a>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="en-us_topic_0053089697_b842352706111223"><a name="en-us_topic_0053089697_b842352706111223"></a><a name="en-us_topic_0053089697_b842352706111223"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="en-us_topic_0053089697_p2038417521118"><a name="en-us_topic_0053089697_p2038417521118"></a><a name="en-us_topic_0053089697_p2038417521118"></a><strong id="en-us_topic_0053089697_b84235270611136"><a name="en-us_topic_0053089697_b84235270611136"></a><a name="en-us_topic_0053089697_b84235270611136"></a>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="en-us_topic_0053089697_note133841352710"><a name="en-us_topic_0053089697_note133841352710"></a><a name="en-us_topic_0053089697_note133841352710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0053089697_ul11400145211112"></a><a name="en-us_topic_0053089697_ul11400145211112"></a><ul id="en-us_topic_0053089697_ul11400145211112"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS is not encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="en-us_topic_0053089697_table166305407148"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row19630740121415"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p17630184015144"><a name="en-us_topic_0053089697_p17630184015144"></a><a name="en-us_topic_0053089697_p17630184015144"></a><strong id="en-us_topic_0053089697_b42647982143154"><a name="en-us_topic_0053089697_b42647982143154"></a><a name="en-us_topic_0053089697_b42647982143154"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.95%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p11630340121413"><a name="en-us_topic_0053089697_p11630340121413"></a><a name="en-us_topic_0053089697_p11630340121413"></a><strong id="en-us_topic_0053089697_b813434055"><a name="en-us_topic_0053089697_b813434055"></a><a name="en-us_topic_0053089697_b813434055"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row16630194014144"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p146304401141"><a name="en-us_topic_0053089697_p146304401141"></a><a name="en-us_topic_0053089697_p146304401141"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p11630124051412"><a name="en-us_topic_0053089697_p11630124051412"></a><a name="en-us_topic_0053089697_p11630124051412"></a>A dedicated virtual network in which your RDS DB instances are located. Isolates networks for different services. You can select an existing VPC or create a VPC. For details on how to create a VPC, see the "Creating a VPC" section in the <em id="en-us_topic_0053089697_i842352697152613"><a name="en-us_topic_0053089697_i842352697152613"></a><a name="en-us_topic_0053089697_i842352697152613"></a>Virtual Private Cloud User Guide</em>.</p>
    <p id="en-us_topic_0053089697_p146301640131412"><a name="en-us_topic_0053089697_p146301640131412"></a><a name="en-us_topic_0053089697_p146301640131412"></a>If no VPC is available, RDS allocates a VPC to you by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row126301940121413"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p196301409148"><a name="en-us_topic_0053089697_p196301409148"></a><a name="en-us_topic_0053089697_p196301409148"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p15630144011417"><a name="en-us_topic_0053089697_p15630144011417"></a><a name="en-us_topic_0053089697_p15630144011417"></a>Improves network security by providing dedicated network resources that are logically isolated from other networks. Subnets take effect only within an AZ. The Dynamic Host Configuration Protocol (DHCP) function must be enabled by default for subnets in which you plan to create RDS DB instances and cannot be disabled.</p>
    <p id="en-us_topic_0053089697_p118281445193416"><a name="en-us_topic_0053089697_p118281445193416"></a><a name="en-us_topic_0053089697_p118281445193416"></a>A floating IP address is automatically assigned when you create a DB instance. You can also enter an unused floating IP address in the subnet segment. After the DB instance is created, the floating IP address cannot be changed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row12630240181414"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p4630134041410"><a name="en-us_topic_0053089697_p4630134041410"></a><a name="en-us_topic_0053089697_p4630134041410"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p1263084010145"><a name="en-us_topic_0053089697_p1263084010145"></a><a name="en-us_topic_0053089697_p1263084010145"></a>Enhances security by controlling access to RDS from other services. You need to add rules to a security group that enable you to connect to your DB instance.</p>
    <p id="en-us_topic_0053089697_p3630640101415"><a name="en-us_topic_0053089697_p3630640101415"></a><a name="en-us_topic_0053089697_p3630640101415"></a>If no security group is available, RDS allocates a security group to you by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="en-us_topic_0053089697_table14630840201412"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row16630140141419"><th class="cellrowborder" valign="top" width="20.87%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p1963011403149"><a name="en-us_topic_0053089697_p1963011403149"></a><a name="en-us_topic_0053089697_p1963011403149"></a><strong id="en-us_topic_0053089697_b33406385143154"><a name="en-us_topic_0053089697_b33406385143154"></a><a name="en-us_topic_0053089697_b33406385143154"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.13%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p4630140181412"><a name="en-us_topic_0053089697_p4630140181412"></a><a name="en-us_topic_0053089697_p4630140181412"></a><strong id="en-us_topic_0053089697_b64102973143154"><a name="en-us_topic_0053089697_b64102973143154"></a><a name="en-us_topic_0053089697_b64102973143154"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row863034017141"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1063016407143"><a name="en-us_topic_0053089697_p1063016407143"></a><a name="en-us_topic_0053089697_p1063016407143"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p106301440171418"><a name="en-us_topic_0053089697_p106301440171418"></a><a name="en-us_topic_0053089697_p106301440171418"></a>The default login name for the database is <strong id="en-us_topic_0053089697_b842352706184259"><a name="en-us_topic_0053089697_b842352706184259"></a><a name="en-us_topic_0053089697_b842352706184259"></a>rdsuser</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row1663024001410"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p8630114019145"><a name="en-us_topic_0053089697_p8630114019145"></a><a name="en-us_topic_0053089697_p8630114019145"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p6630040151420"><a name="en-us_topic_0053089697_p6630040151420"></a><a name="en-us_topic_0053089697_p6630040151420"></a>Must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters (~!@#%^*-_+?,). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="en-us_topic_0053089697_p36301740171419"><a name="en-us_topic_0053089697_p36301740171419"></a><a name="en-us_topic_0053089697_p36301740171419"></a>Keep this password secure. The system cannot retrieve it.</p>
    <p id="en-us_topic_0053089697_p432375214012"><a name="en-us_topic_0053089697_p432375214012"></a><a name="en-us_topic_0053089697_p432375214012"></a></p>
    <p id="en-us_topic_0053089697_p136346617119"><a name="en-us_topic_0053089697_p136346617119"></a><a name="en-us_topic_0053089697_p136346617119"></a>After a DB instance is created, you can reset this password. For details, see section <a href="resetting-the-administrator-password-97.md">Resetting the Administrator Password</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row963064018148"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1863010407141"><a name="en-us_topic_0053089697_p1863010407141"></a><a name="en-us_topic_0053089697_p1863010407141"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p126301640121411"><a name="en-us_topic_0053089697_p126301640121411"></a><a name="en-us_topic_0053089697_p126301640121411"></a>Must be the same as <span class="parmname" id="en-us_topic_0053089697_parmname769647905141841"><a name="en-us_topic_0053089697_parmname769647905141841"></a><a name="en-us_topic_0053089697_parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row156111228045"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p18676102012444"><a name="en-us_topic_0053089697_p18676102012444"></a><a name="en-us_topic_0053089697_p18676102012444"></a>Parameter Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p863014019144"><a name="en-us_topic_0053089697_p863014019144"></a><a name="en-us_topic_0053089697_p863014019144"></a>Contains engine configuration values that can be applied to one or more DB instances. If you intend to create primary/standby DB instances, they use the same parameter template. You can modify instance parameters as required after the DB instance is created.</p>
    <div class="notice" id="en-us_topic_0053089697_note365219366379"><a name="en-us_topic_0053089697_note365219366379"></a><a name="en-us_topic_0053089697_note365219366379"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="en-us_topic_0053089697_p916211653412"><a name="en-us_topic_0053089697_p916211653412"></a><a name="en-us_topic_0053089697_p916211653412"></a>If you use a custom parameter template when creating a DB instance, the specification-related parameter <span class="parmname" id="en-us_topic_0053089697_parmname11713749193416"><a name="en-us_topic_0053089697_parmname11713749193416"></a><a name="en-us_topic_0053089697_parmname11713749193416"></a><b>max server memory (MB)</b></span> in the custom template is not delivered. Instead, the default value is used.</p>
    </div></div>
    <p id="en-us_topic_0053089697_p147431598590"><a name="en-us_topic_0053089697_p147431598590"></a><a name="en-us_topic_0053089697_p147431598590"></a></p>
    <p id="en-us_topic_0053089697_p1581213215597"><a name="en-us_topic_0053089697_p1581213215597"></a><a name="en-us_topic_0053089697_p1581213215597"></a></p>
    <p id="en-us_topic_0053089697_p757011330597"><a name="en-us_topic_0053089697_p757011330597"></a><a name="en-us_topic_0053089697_p757011330597"></a>You can modify the instance parameters as required after the DB instance is created. For details see section <a href="modifying-parameters-in-a-parameter-template-110.md">Modifying Parameters in a Parameter Template</a>.</p>
    <p id="en-us_topic_0053089697_p1282884515344"><a name="en-us_topic_0053089697_p1282884515344"></a><a name="en-us_topic_0053089697_p1282884515344"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  AD domain

    <a name="en-us_topic_0053089697_table17700153119104"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row570014317103"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p353002414554"><a name="en-us_topic_0053089697_p353002414554"></a><a name="en-us_topic_0053089697_p353002414554"></a><strong id="en-us_topic_0053089697_b1305617683"><a name="en-us_topic_0053089697_b1305617683"></a><a name="en-us_topic_0053089697_b1305617683"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p9530172418558"><a name="en-us_topic_0053089697_p9530172418558"></a><a name="en-us_topic_0053089697_p9530172418558"></a><strong id="en-us_topic_0053089697_b1202766412"><a name="en-us_topic_0053089697_b1202766412"></a><a name="en-us_topic_0053089697_b1202766412"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row67007318105"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p13530152415554"><a name="en-us_topic_0053089697_p13530152415554"></a><a name="en-us_topic_0053089697_p13530152415554"></a>AD Domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p1654755884213"><a name="en-us_topic_0053089697_p1654755884213"></a><a name="en-us_topic_0053089697_p1654755884213"></a>Allows an Active Directory user to authenticate with Microsoft SQL Server DB instances.</p>
    <p id="en-us_topic_0053089697_p203472461465"><a name="en-us_topic_0053089697_p203472461465"></a><a name="en-us_topic_0053089697_p203472461465"></a>Active Directory, which is short for AD, is a directory service on Windows Standard Server, Windows Enterprise Server, and Windows Datacenter Server. Active Directory stores information about objects on the network and makes this information easy for administrators and users to find and use. Active Directory uses a structured data store as the basis for a logical, hierarchical organization of directory information.</p>
    <div class="notice" id="en-us_topic_0053089697_note64581401166"><a name="en-us_topic_0053089697_note64581401166"></a><a name="en-us_topic_0053089697_note64581401166"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="en-us_topic_0053089697_ol78790168171"></a><a name="en-us_topic_0053089697_ol78790168171"></a><ol id="en-us_topic_0053089697_ol78790168171"><li>When you configure an AD domain information during the DB instance creation, do not configure or disable Group Policy Object (GPO) for your domain controller server. Otherwise, the DB instance creation will fail.</li><li>If GPO is required, you need to create an ECS and set up a new domain controller server with GPO disabled. Then, establish trust between your domain controller server and the new domain controller server. For details, contact customer service.</li></ol>
    </div></div>
    <a name="en-us_topic_0053089697_ul249302602517"></a><a name="en-us_topic_0053089697_ul249302602517"></a><ul id="en-us_topic_0053089697_ul249302602517"><li><strong id="en-us_topic_0053089697_b84235270611146"><a name="en-us_topic_0053089697_b84235270611146"></a><a name="en-us_topic_0053089697_b84235270611146"></a>Skip</strong>: This option is selected by default.</li><li><strong id="en-us_topic_0053089697_b588141336"><a name="en-us_topic_0053089697_b588141336"></a><a name="en-us_topic_0053089697_b588141336"></a>Configure</strong>: To configure the AD domain, you must first prepare a domain controller on an ECS or on-premises database. Then, configure the directory address, domain name, directory administrator, and directory administrator password as required.</li></ul>
    <div class="note" id="en-us_topic_0053089697_note25015506369"><a name="en-us_topic_0053089697_note25015506369"></a><a name="en-us_topic_0053089697_note25015506369"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0053089697_p135015093614"><a name="en-us_topic_0053089697_p135015093614"></a><a name="en-us_topic_0053089697_p135015093614"></a>If a Microsoft SQL Server single DB instance is configured with the AD domain, it cannot be changed to primary/standby DB instances.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row570043161020"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1253012419555"><a name="en-us_topic_0053089697_p1253012419555"></a><a name="en-us_topic_0053089697_p1253012419555"></a>Directory Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p135079514431"><a name="en-us_topic_0053089697_p135079514431"></a><a name="en-us_topic_0053089697_p135079514431"></a>Enter the private IP address of the ECS that supports the AD domain.</p>
    <p id="en-us_topic_0053089697_p1201640182516"><a name="en-us_topic_0053089697_p1201640182516"></a><a name="en-us_topic_0053089697_p1201640182516"></a>For example: 192.168.x.x.</p>
    <div class="note" id="en-us_topic_0053089697_note317205818312"><a name="en-us_topic_0053089697_note317205818312"></a><a name="en-us_topic_0053089697_note317205818312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0053089697_p1617214589316"><a name="en-us_topic_0053089697_p1617214589316"></a><a name="en-us_topic_0053089697_p1617214589316"></a>The ECS must be in the same subnet as the DB instance.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row8700631121015"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p18462733105818"><a name="en-us_topic_0053089697_p18462733105818"></a><a name="en-us_topic_0053089697_p18462733105818"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p05182429436"><a name="en-us_topic_0053089697_p05182429436"></a><a name="en-us_topic_0053089697_p05182429436"></a>A fully qualified domain name, such as luna@newrds.com, must:</p>
    <a name="en-us_topic_0053089697_ol1017819516413"></a><a name="en-us_topic_0053089697_ol1017819516413"></a><ol id="en-us_topic_0053089697_ol1017819516413"><li>Be the same as the ECS domain name.</li><li>Be no more than 48 characters long.</li><li>Only include letters, digits, dots (.), and hyphens (-).</li><li>Include a valid top-level domain name which is more than 2 characters long and contains only dots (.) and letters.</li></ol>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row6700103115102"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p9530112412554"><a name="en-us_topic_0053089697_p9530112412554"></a><a name="en-us_topic_0053089697_p9530112412554"></a>Directory Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p32316429583"><a name="en-us_topic_0053089697_p32316429583"></a><a name="en-us_topic_0053089697_p32316429583"></a>You are advised to enter the domain administrator username.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0053089697_row20700183115103"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1553092435512"><a name="en-us_topic_0053089697_p1553092435512"></a><a name="en-us_topic_0053089697_p1553092435512"></a>Directory Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p22811651192920"><a name="en-us_topic_0053089697_p22811651192920"></a><a name="en-us_topic_0053089697_p22811651192920"></a>Indicates the password of the directory administrator.</p>
    <p id="en-us_topic_0053089697_p121331037121419"><a name="en-us_topic_0053089697_p121331037121419"></a><a name="en-us_topic_0053089697_p121331037121419"></a>Must consist of 8 to 32 characters and must be a combination of uppercase letters, lowercase letters, digits, and at least one of the following special characters: ~!@#%^*-_=+? Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="en-us_topic_0053089697_p10149123751418"><a name="en-us_topic_0053089697_p10149123751418"></a><a name="en-us_topic_0053089697_p10149123751418"></a>Keep this password secure. The system cannot retrieve it.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Tags

    <a name="en-us_topic_0053089697_table05011128132310"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row250292812318"><th class="cellrowborder" valign="top" width="24.349999999999998%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p852913210175"><a name="en-us_topic_0053089697_p852913210175"></a><a name="en-us_topic_0053089697_p852913210175"></a><strong id="en-us_topic_0053089697_b1089235155"><a name="en-us_topic_0053089697_b1089235155"></a><a name="en-us_topic_0053089697_b1089235155"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.64999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p175291021161717"><a name="en-us_topic_0053089697_p175291021161717"></a><a name="en-us_topic_0053089697_p175291021161717"></a><strong id="en-us_topic_0053089697_b1287816460"><a name="en-us_topic_0053089697_b1287816460"></a><a name="en-us_topic_0053089697_b1287816460"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row13502102812310"><td class="cellrowborder" valign="top" width="24.349999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p7529202171713"><a name="en-us_topic_0053089697_p7529202171713"></a><a name="en-us_topic_0053089697_p7529202171713"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.64999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p141127570267"><a name="en-us_topic_0053089697_p141127570267"></a><a name="en-us_topic_0053089697_p141127570267"></a>Tags an RDS DB instance. This configuration is optional. Adding tags to RDS DB instances helps you better identify and manage the DB instances. A maximum of 20 tags can be added for each DB instance.</p>
    <p id="en-us_topic_0053089697_p83821399268"><a name="en-us_topic_0053089697_p83821399268"></a><a name="en-us_topic_0053089697_p83821399268"></a>After a DB instance is created, you can view its tag details on the <strong id="en-us_topic_0053089697_b362324625716"><a name="en-us_topic_0053089697_b362324625716"></a><a name="en-us_topic_0053089697_b362324625716"></a>Tags</strong> tab. For details, see section <a href="managing-tags-95.md">Managing Tags</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  Batch creation

    <a name="en-us_topic_0053089697_table2303143712383"></a>
    <table><thead align="left"><tr id="en-us_topic_0053089697_row630515379381"><th class="cellrowborder" valign="top" width="23.74%" id="mcps1.2.3.1.1"><p id="en-us_topic_0053089697_p131195564383"><a name="en-us_topic_0053089697_p131195564383"></a><a name="en-us_topic_0053089697_p131195564383"></a><strong id="en-us_topic_0053089697_b182817584576"><a name="en-us_topic_0053089697_b182817584576"></a><a name="en-us_topic_0053089697_b182817584576"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76.25999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0053089697_p4119155610385"><a name="en-us_topic_0053089697_p4119155610385"></a><a name="en-us_topic_0053089697_p4119155610385"></a><strong id="en-us_topic_0053089697_b1694285817575"><a name="en-us_topic_0053089697_b1694285817575"></a><a name="en-us_topic_0053089697_b1694285817575"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0053089697_row130593718387"><td class="cellrowborder" valign="top" width="23.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0053089697_p1730583743810"><a name="en-us_topic_0053089697_p1730583743810"></a><a name="en-us_topic_0053089697_p1730583743810"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0053089697_p930543712381"><a name="en-us_topic_0053089697_p930543712381"></a><a name="en-us_topic_0053089697_p930543712381"></a>RDS supports DB instance creation in batches. If you choose to create primary/standby DB instances and set <strong id="en-us_topic_0053089697_b38073135813"><a name="en-us_topic_0053089697_b38073135813"></a><a name="en-us_topic_0053089697_b38073135813"></a>Quantity</strong> to <strong id="en-us_topic_0053089697_b68081716582"><a name="en-us_topic_0053089697_b68081716582"></a><a name="en-us_topic_0053089697_b68081716582"></a>1</strong>, a primary DB instance and a standby DB instance will be created synchronously.</p>
    <p id="en-us_topic_0053089697_p71561045152219"><a name="en-us_topic_0053089697_p71561045152219"></a><a name="en-us_topic_0053089697_p71561045152219"></a>If you create multiple DB instances at a time, they will be named with four digits appended to the DB instance name. For example, if you enter <strong id="en-us_topic_0053089697_b32981525102211"><a name="en-us_topic_0053089697_b32981525102211"></a><a name="en-us_topic_0053089697_b32981525102211"></a>instance</strong>, the first instance will be named as instance-0001, the second as instance-0002, and so on.</p>
    </td>
    </tr>
    </tbody>
    </table>

    After the configuration, click  **Price Calculator**  to view the RDS configuration fee.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The performance of your DB instance depends on its configurations. Hardware configuration items include the instance specifications, storage type, and storage space.  

6.  Confirm the specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  To view and manage the DB instance, go to the  **Instance Management**  page.
    -   During the creation process, the DB instance status is  **Creating**.
    -   To refresh the DB instance list, click  ![](figures/refresh.png)  in the upper right corner of the list. When the creation process is complete, the instance status will change to  **Available**.
    -   The automated backup policy is enabled by default. An automated full backup is immediately triggered after a DB instance is created.
    -   The default database port number is  **1433**. After a DB instance is created, you can change its port number.

        For details, see section  [Changing the Database Port](changing-the-database-port-(Microsoft-SQL-Server).md).



