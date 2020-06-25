# Step 1: Create a DB Instance<a name="rds_02_0020"></a>

## **Scenarios**<a name="en-us_topic_0046585384_section3881006517148"></a>

You can create DB instances using the RDS console or APIs. For details about how to  create DB instances  using APIs, see the "Creating a DB Instance" section in the  _Relational Database Service API Reference_. This section describes how to  create a DB instance  on the RDS console.

RDS allows you to tailor your computing resources and storage space to your business needs.

## Procedure<a name="en-us_topic_0046585384_sddcec3dbbccd43178a23424d29482e1a"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click  **Create DB Instance**.
5.  On the displayed page, configure information about your DB instance. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="en-us_topic_0046585384_table17676102015448"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row196591120114414"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p1765922011445"><a name="en-us_topic_0046585384_p1765922011445"></a><a name="en-us_topic_0046585384_p1765922011445"></a><strong id="en-us_topic_0046585384_b84235270618284_1"><a name="en-us_topic_0046585384_b84235270618284_1"></a><a name="en-us_topic_0046585384_b84235270618284_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p3659102019443"><a name="en-us_topic_0046585384_p3659102019443"></a><a name="en-us_topic_0046585384_p3659102019443"></a><strong id="en-us_topic_0046585384_b842352706212013_1"><a name="en-us_topic_0046585384_b842352706212013_1"></a><a name="en-us_topic_0046585384_b842352706212013_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row13659192074416"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p136595209441"><a name="en-us_topic_0046585384_p136595209441"></a><a name="en-us_topic_0046585384_p136595209441"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p15971451194710"><a name="en-us_topic_0046585384_p15971451194710"></a><a name="en-us_topic_0046585384_p15971451194710"></a>A region where the tenant is located. It can be changed in the upper left corner of the page.</p>
    <div class="note" id="en-us_topic_0046585384_note19961614265"><a name="en-us_topic_0046585384_note19961614265"></a><a name="en-us_topic_0046585384_note19961614265"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0046585384_p1999615642620"><a name="en-us_topic_0046585384_p1999615642620"></a><a name="en-us_topic_0046585384_p1999615642620"></a>Products in different regions cannot communicate with each other through a private network and you cannot change the region of a DB instance after creating the instance. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row1367612024415"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p365952016449"><a name="en-us_topic_0046585384_p365952016449"></a><a name="en-us_topic_0046585384_p365952016449"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p34931419132919"><a name="en-us_topic_0046585384_p34931419132919"></a><a name="en-us_topic_0046585384_p34931419132919"></a>Must start with a letter and consist of 4 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row14676112084411"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p6676162019441"><a name="en-us_topic_0046585384_p6676162019441"></a><a name="en-us_topic_0046585384_p6676162019441"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p567611206445"><a name="en-us_topic_0046585384_p567611206445"></a><a name="en-us_topic_0046585384_p567611206445"></a>Set to <strong id="en-us_topic_0046585384_b84235270611955"><a name="en-us_topic_0046585384_b84235270611955"></a><a name="en-us_topic_0046585384_b84235270611955"></a>PostgreSQL</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row667672017449"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p10676102074415"><a name="en-us_topic_0046585384_p10676102074415"></a><a name="en-us_topic_0046585384_p10676102074415"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p545215541125"><a name="en-us_topic_0046585384_p545215541125"></a><a name="en-us_topic_0046585384_p545215541125"></a></p>
    <p id="en-us_topic_0046585384_p1961756101213"><a name="en-us_topic_0046585384_p1961756101213"></a><a name="en-us_topic_0046585384_p1961756101213"></a></p>
    <p id="en-us_topic_0046585384_p145823010132"><a name="en-us_topic_0046585384_p145823010132"></a><a name="en-us_topic_0046585384_p145823010132"></a>For details, see section <a href="db-engines-and-versions.md">DB Engines and Versions</a>.</p>
    <p id="en-us_topic_0046585384_p116761220154415"><a name="en-us_topic_0046585384_p116761220154415"></a><a name="en-us_topic_0046585384_p116761220154415"></a></p>
    <p id="en-us_topic_0046585384_p192551714184510"><a name="en-us_topic_0046585384_p192551714184510"></a><a name="en-us_topic_0046585384_p192551714184510"></a>Different DB engine versions are supported in different regions.</p>
    <p id="en-us_topic_0046585384_p687715327516"><a name="en-us_topic_0046585384_p687715327516"></a><a name="en-us_topic_0046585384_p687715327516"></a>If you use a PostgreSQL database, select a proper DB engine version based on service requirements. You are advised to select the latest available version because it is more stable, reliable, and secure.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row17676220104418"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p13676192011449"><a name="en-us_topic_0046585384_p13676192011449"></a><a name="en-us_topic_0046585384_p13676192011449"></a>DB Instance Type and AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0046585384_ul7676820184413"></a><a name="en-us_topic_0046585384_ul7676820184413"></a><ul id="en-us_topic_0046585384_ul7676820184413"><li><strong id="en-us_topic_0046585384_b177591121144916"><a name="en-us_topic_0046585384_b177591121144916"></a><a name="en-us_topic_0046585384_b177591121144916"></a>Primary/Standby</strong>: uses the HA architecture with a primary DB instance and a synchronous standby DB instance. It is suitable for production databases of large- and medium-sized enterprises in Internet, Internet of Things (IoT), retail e-commerce sales, logistics, gaming, and other sectors. The standby DB instance improves instance reliability and is invisible to you after being created.<p id="en-us_topic_0046585384_p3659122084410"><a name="en-us_topic_0046585384_p3659122084410"></a><a name="en-us_topic_0046585384_p3659122084410"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network. </p>
    <p id="en-us_topic_0046585384_p14411939141316"><a name="en-us_topic_0046585384_p14411939141316"></a><a name="en-us_topic_0046585384_p14411939141316"></a>RDS supports deploying primary and standby DB instances in an AZ or across AZs. You can determine whether the standby AZ is the same as the primary AZ.</p>
    <a name="en-us_topic_0046585384_ul1241210399138"></a><a name="en-us_topic_0046585384_ul1241210399138"></a><ul id="en-us_topic_0046585384_ul1241210399138"><li>If they are the same (default setting), the primary and standby DB instances are deployed in the same AZ.</li><li>If they are different, the primary and standby DB instances are deployed in different AZs to ensure failover support and high availability.</li></ul>
    </li><li><strong id="en-us_topic_0046585384_b29771729114913"><a name="en-us_topic_0046585384_b29771729114913"></a><a name="en-us_topic_0046585384_b29771729114913"></a>Single</strong>: uses the single-node architecture, which is more cost-effective than mainstream primary/standby DB instances. It is suitable for developing and testing of microsites, and small- and medium-sized enterprises, or for learning about RDS.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row1675018111332"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p188281545173410"><a name="en-us_topic_0046585384_p188281545173410"></a><a name="en-us_topic_0046585384_p188281545173410"></a>Time Zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p1682834520347"><a name="en-us_topic_0046585384_p1682834520347"></a><a name="en-us_topic_0046585384_p1682834520347"></a>You need to select a time zone for your DB instance according to the longitude and latitude of the region hosting your DB instance. Can be selected during DB instance creation and can be changed after the DB instance is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="en-us_topic_0046585384_table17676620144413"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row06763201449"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p19676112013449"><a name="en-us_topic_0046585384_p19676112013449"></a><a name="en-us_topic_0046585384_p19676112013449"></a><strong id="en-us_topic_0046585384_b28465709112351"><a name="en-us_topic_0046585384_b28465709112351"></a><a name="en-us_topic_0046585384_b28465709112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p66761120154418"><a name="en-us_topic_0046585384_p66761120154418"></a><a name="en-us_topic_0046585384_p66761120154418"></a><strong id="en-us_topic_0046585384_b9357258112351"><a name="en-us_topic_0046585384_b9357258112351"></a><a name="en-us_topic_0046585384_b9357258112351"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row186761520134411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p1676182013443"><a name="en-us_topic_0046585384_p1676182013443"></a><a name="en-us_topic_0046585384_p1676182013443"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p3612111215507"><a name="en-us_topic_0046585384_p3612111215507"></a><a name="en-us_topic_0046585384_p3612111215507"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="en-us_topic_0046585384_p781114612508"><a name="en-us_topic_0046585384_p781114612508"></a><a name="en-us_topic_0046585384_p781114612508"></a></p>
    <p id="en-us_topic_0046585384_p5429821515"><a name="en-us_topic_0046585384_p5429821515"></a><a name="en-us_topic_0046585384_p5429821515"></a></p>
    <p id="en-us_topic_0046585384_p12042810516"><a name="en-us_topic_0046585384_p12042810516"></a><a name="en-us_topic_0046585384_p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="en-us_topic_0046585384_p4689621196"><a name="en-us_topic_0046585384_p4689621196"></a><a name="en-us_topic_0046585384_p4689621196"></a></p>
    <p id="en-us_topic_0046585384_p860165515523"><a name="en-us_topic_0046585384_p860165515523"></a><a name="en-us_topic_0046585384_p860165515523"></a></p>
    <p id="en-us_topic_0046585384_p4610514532"><a name="en-us_topic_0046585384_p4610514532"></a><a name="en-us_topic_0046585384_p4610514532"></a></p>
    <p id="en-us_topic_0046585384_p19542517536"><a name="en-us_topic_0046585384_p19542517536"></a><a name="en-us_topic_0046585384_p19542517536"></a>After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-a-db-instance-class-29.md">Changing a DB Instance Class</a>.</p>
    <p id="en-us_topic_0046585384_p38285458348"><a name="en-us_topic_0046585384_p38285458348"></a><a name="en-us_topic_0046585384_p38285458348"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row116761020134412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p96761020194411"><a name="en-us_topic_0046585384_p96761020194411"></a><a name="en-us_topic_0046585384_p96761020194411"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p799718574114"><a name="en-us_topic_0046585384_p799718574114"></a><a name="en-us_topic_0046585384_p799718574114"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="en-us_topic_0046585384_ul17230161564119"></a><a name="en-us_topic_0046585384_ul17230161564119"></a><ul id="en-us_topic_0046585384_ul17230161564119"><li><strong id="en-us_topic_0046585384_b1499317517538"><a name="en-us_topic_0046585384_b1499317517538"></a><a name="en-us_topic_0046585384_b1499317517538"></a>Common I/O</strong>: uses the SATA disk type, with a maximum throughput of 90 MB/s.</li><li><strong id="en-us_topic_0046585384_b175932011548"><a name="en-us_topic_0046585384_b175932011548"></a><a name="en-us_topic_0046585384_b175932011548"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row1467616204445"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p176763206449"><a name="en-us_topic_0046585384_p176763206449"></a><a name="en-us_topic_0046585384_p176763206449"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p12950023171218"><a name="en-us_topic_0046585384_p12950023171218"></a><a name="en-us_topic_0046585384_p12950023171218"></a>Contains the system overhead required for inode, reserved block, and database operation. Can range in size from 40 GB to 4000 GB and can be scaled up only by a multiple of 10 GB.</p>
    <p id="en-us_topic_0046585384_p4990256102610"><a name="en-us_topic_0046585384_p4990256102610"></a><a name="en-us_topic_0046585384_p4990256102610"></a></p>
    <p id="en-us_topic_0046585384_p5999151032711"><a name="en-us_topic_0046585384_p5999151032711"></a><a name="en-us_topic_0046585384_p5999151032711"></a></p>
    <p id="en-us_topic_0046585384_p13797182010276"><a name="en-us_topic_0046585384_p13797182010276"></a><a name="en-us_topic_0046585384_p13797182010276"></a>After a DB instance is created, you can scale up its storage space. For details, see section <a href="scaling-up-storage-space.md">Scaling Up Storage Space</a>.</p>
    <p id="en-us_topic_0046585384_p1182820454348"><a name="en-us_topic_0046585384_p1182820454348"></a><a name="en-us_topic_0046585384_p1182820454348"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row3377101065014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p119341314506"><a name="en-us_topic_0046585384_p119341314506"></a><a name="en-us_topic_0046585384_p119341314506"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0046585384_ul141961813185014"></a><a name="en-us_topic_0046585384_ul141961813185014"></a><ul id="en-us_topic_0046585384_ul141961813185014"><li><strong id="en-us_topic_0046585384_b84235270611657"><a name="en-us_topic_0046585384_b84235270611657"></a><a name="en-us_topic_0046585384_b84235270611657"></a>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="en-us_topic_0046585384_b8423527061172"><a name="en-us_topic_0046585384_b8423527061172"></a><a name="en-us_topic_0046585384_b8423527061172"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="en-us_topic_0046585384_p19208161316507"><a name="en-us_topic_0046585384_p19208161316507"></a><a name="en-us_topic_0046585384_p19208161316507"></a><strong id="en-us_topic_0046585384_b8423527061176"><a name="en-us_topic_0046585384_b8423527061176"></a><a name="en-us_topic_0046585384_b8423527061176"></a>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="en-us_topic_0046585384_note72081013185015"><a name="en-us_topic_0046585384_note72081013185015"></a><a name="en-us_topic_0046585384_note72081013185015"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0046585384_ul221110134509"></a><a name="en-us_topic_0046585384_ul221110134509"></a><ul id="en-us_topic_0046585384_ul221110134509"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS is not encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="en-us_topic_0046585384_i84235269720539"><a name="en-us_topic_0046585384_i84235269720539"></a><a name="en-us_topic_0046585384_i84235269720539"></a>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="en-us_topic_0046585384_table1567602014410"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row9676172019444"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p1267632012446"><a name="en-us_topic_0046585384_p1267632012446"></a><a name="en-us_topic_0046585384_p1267632012446"></a><strong id="en-us_topic_0046585384_b10991376112351"><a name="en-us_topic_0046585384_b10991376112351"></a><a name="en-us_topic_0046585384_b10991376112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.95%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p76761320184410"><a name="en-us_topic_0046585384_p76761320184410"></a><a name="en-us_topic_0046585384_p76761320184410"></a><strong id="en-us_topic_0046585384_b842352706212013_5"><a name="en-us_topic_0046585384_b842352706212013_5"></a><a name="en-us_topic_0046585384_b842352706212013_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row6676122014412"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p1567612074417"><a name="en-us_topic_0046585384_p1567612074417"></a><a name="en-us_topic_0046585384_p1567612074417"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p567672084416"><a name="en-us_topic_0046585384_p567672084416"></a><a name="en-us_topic_0046585384_p567672084416"></a>A dedicated virtual network in which your RDS DB instances are located. Isolates networks for different services. You can select an existing VPC or create a VPC. For details on how to create a VPC, see the "Creating a VPC" section in the <em id="en-us_topic_0046585384_i842352697152613"><a name="en-us_topic_0046585384_i842352697152613"></a><a name="en-us_topic_0046585384_i842352697152613"></a>Virtual Private Cloud User Guide</em>.</p>
    <p id="en-us_topic_0046585384_p146764206449"><a name="en-us_topic_0046585384_p146764206449"></a><a name="en-us_topic_0046585384_p146764206449"></a>If no VPC is available, RDS allocates a VPC to you by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row196763203449"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p9676152015447"><a name="en-us_topic_0046585384_p9676152015447"></a><a name="en-us_topic_0046585384_p9676152015447"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p16676102064418"><a name="en-us_topic_0046585384_p16676102064418"></a><a name="en-us_topic_0046585384_p16676102064418"></a>Improves network security by providing dedicated network resources that are logically isolated from other networks. Subnets take effect only within an AZ. The Dynamic Host Configuration Protocol (DHCP) function must be enabled by default for subnets in which you plan to create RDS DB instances and cannot be disabled.</p>
    <p id="en-us_topic_0046585384_p118281445193416"><a name="en-us_topic_0046585384_p118281445193416"></a><a name="en-us_topic_0046585384_p118281445193416"></a>A floating IP address is automatically assigned when you create a DB instance. You can also enter an unused floating IP address in the subnet segment. After the DB instance is created, you can change the floating IP address.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row167622084411"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p967652018443"><a name="en-us_topic_0046585384_p967652018443"></a><a name="en-us_topic_0046585384_p967652018443"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p2676420194417"><a name="en-us_topic_0046585384_p2676420194417"></a><a name="en-us_topic_0046585384_p2676420194417"></a>Controls the access that traffic has in and out of a DB instance. By default, the security group associated with the DB instance is authorized.</p>
    <p id="en-us_topic_0046585384_p106761320154412"><a name="en-us_topic_0046585384_p106761320154412"></a><a name="en-us_topic_0046585384_p106761320154412"></a>Enhances security by controlling access to RDS from other services. You need to add rules to a security group that enable you to connect to your DB instance.</p>
    <p id="en-us_topic_0046585384_p867616204441"><a name="en-us_topic_0046585384_p867616204441"></a><a name="en-us_topic_0046585384_p867616204441"></a>If no security group is available, RDS allocates a security group to you by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="en-us_topic_0046585384_table2067602034417"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row867602015445"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p0676172094416"><a name="en-us_topic_0046585384_p0676172094416"></a><a name="en-us_topic_0046585384_p0676172094416"></a><strong id="en-us_topic_0046585384_b62569647112351"><a name="en-us_topic_0046585384_b62569647112351"></a><a name="en-us_topic_0046585384_b62569647112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.14%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p1767692064412"><a name="en-us_topic_0046585384_p1767692064412"></a><a name="en-us_topic_0046585384_p1767692064412"></a><strong id="en-us_topic_0046585384_b61301106112351"><a name="en-us_topic_0046585384_b61301106112351"></a><a name="en-us_topic_0046585384_b61301106112351"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row46766201446"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p196761220104417"><a name="en-us_topic_0046585384_p196761220104417"></a><a name="en-us_topic_0046585384_p196761220104417"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p867632012441"><a name="en-us_topic_0046585384_p867632012441"></a><a name="en-us_topic_0046585384_p867632012441"></a>The default login name for the database is <strong id="en-us_topic_0046585384_b842352706184259"><a name="en-us_topic_0046585384_b842352706184259"></a><a name="en-us_topic_0046585384_b842352706184259"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row1267602012448"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p3676620104415"><a name="en-us_topic_0046585384_p3676620104415"></a><a name="en-us_topic_0046585384_p3676620104415"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p46761720194415"><a name="en-us_topic_0046585384_p46761720194415"></a><a name="en-us_topic_0046585384_p46761720194415"></a>Must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters (~!@#%^*-_+?,). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="en-us_topic_0046585384_p76765206446"><a name="en-us_topic_0046585384_p76765206446"></a><a name="en-us_topic_0046585384_p76765206446"></a>Keep this password secure. The system cannot retrieve it.</p>
    <p id="en-us_topic_0046585384_p432375214012"><a name="en-us_topic_0046585384_p432375214012"></a><a name="en-us_topic_0046585384_p432375214012"></a></p>
    <p id="en-us_topic_0046585384_p136346617119"><a name="en-us_topic_0046585384_p136346617119"></a><a name="en-us_topic_0046585384_p136346617119"></a>After a DB instance is created, you can reset this password. For details, see section <a href="resetting-the-administrator-password-39.md">Resetting the Administrator Password</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row106762020204410"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p16676320124415"><a name="en-us_topic_0046585384_p16676320124415"></a><a name="en-us_topic_0046585384_p16676320124415"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p19676620144414"><a name="en-us_topic_0046585384_p19676620144414"></a><a name="en-us_topic_0046585384_p19676620144414"></a>Must be the same as <span class="parmname" id="en-us_topic_0046585384_parmname769647905141841"><a name="en-us_topic_0046585384_parmname769647905141841"></a><a name="en-us_topic_0046585384_parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0046585384_row91491594316"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p9676320204413"><a name="en-us_topic_0046585384_p9676320204413"></a><a name="en-us_topic_0046585384_p9676320204413"></a>Parameter Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p18676102012444"><a name="en-us_topic_0046585384_p18676102012444"></a><a name="en-us_topic_0046585384_p18676102012444"></a>Contains engine configuration values that can be applied to one or more DB instances. If you intend to create primary/standby DB instances, they use the same parameter template. You can modify instance parameters as required after the DB instance is created.</p>
    <div class="notice" id="en-us_topic_0046585384_note365219366379"><a name="en-us_topic_0046585384_note365219366379"></a><a name="en-us_topic_0046585384_note365219366379"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="en-us_topic_0046585384_p965293617376"><a name="en-us_topic_0046585384_p965293617376"></a><a name="en-us_topic_0046585384_p965293617376"></a>If you use a custom parameter template when creating a DB instance, the specification-related parameters in the custom template are not delivered. Instead, the default values are used.</p>
    <a name="en-us_topic_0046585384_ul827715317325"></a><a name="en-us_topic_0046585384_ul827715317325"></a><ul id="en-us_topic_0046585384_ul827715317325"><li><span class="parmname" id="en-us_topic_0046585384_parmname1427512817352"><a name="en-us_topic_0046585384_parmname1427512817352"></a><a name="en-us_topic_0046585384_parmname1427512817352"></a><b>maintenance_work_mem</b></span></li><li><span class="parmname" id="en-us_topic_0046585384_parmname17967163018354"><a name="en-us_topic_0046585384_parmname17967163018354"></a><a name="en-us_topic_0046585384_parmname17967163018354"></a><b>shared_buffers</b></span></li><li><span class="parmname" id="en-us_topic_0046585384_parmname9556933163518"><a name="en-us_topic_0046585384_parmname9556933163518"></a><a name="en-us_topic_0046585384_parmname9556933163518"></a><b>max_connections</b></span></li><li><span class="parmname" id="en-us_topic_0046585384_parmname1313523713512"><a name="en-us_topic_0046585384_parmname1313523713512"></a><a name="en-us_topic_0046585384_parmname1313523713512"></a><b>effective_cache_size</b></span></li></ul>
    </div></div>
    <p id="en-us_topic_0046585384_p147431598590"><a name="en-us_topic_0046585384_p147431598590"></a><a name="en-us_topic_0046585384_p147431598590"></a></p>
    <p id="en-us_topic_0046585384_p1581213215597"><a name="en-us_topic_0046585384_p1581213215597"></a><a name="en-us_topic_0046585384_p1581213215597"></a></p>
    <p id="en-us_topic_0046585384_p757011330597"><a name="en-us_topic_0046585384_p757011330597"></a><a name="en-us_topic_0046585384_p757011330597"></a>You can modify the instance parameters as required after the DB instance is created. For details see section <a href="modifying-parameters-in-a-parameter-template-52.md">Modifying Parameters in a Parameter Template</a>.</p>
    <p id="en-us_topic_0046585384_p1282884515344"><a name="en-us_topic_0046585384_p1282884515344"></a><a name="en-us_topic_0046585384_p1282884515344"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Tags

    <a name="en-us_topic_0046585384_table555184732217"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row105624782217"><th class="cellrowborder" valign="top" width="24.66%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p852913210175"><a name="en-us_topic_0046585384_p852913210175"></a><a name="en-us_topic_0046585384_p852913210175"></a><strong id="en-us_topic_0046585384_b6455113171816"><a name="en-us_topic_0046585384_b6455113171816"></a><a name="en-us_topic_0046585384_b6455113171816"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.33999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p175291021161717"><a name="en-us_topic_0046585384_p175291021161717"></a><a name="en-us_topic_0046585384_p175291021161717"></a><strong id="en-us_topic_0046585384_b778201581819"><a name="en-us_topic_0046585384_b778201581819"></a><a name="en-us_topic_0046585384_b778201581819"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row55620472221"><td class="cellrowborder" valign="top" width="24.66%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p7529202171713"><a name="en-us_topic_0046585384_p7529202171713"></a><a name="en-us_topic_0046585384_p7529202171713"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.33999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p141127570267"><a name="en-us_topic_0046585384_p141127570267"></a><a name="en-us_topic_0046585384_p141127570267"></a>Tags an RDS DB instance. This configuration is optional. Adding tags to RDS DB instances helps you better identify and manage the DB instances. A maximum of 20 tags can be added for each DB instance.</p>
    <p id="en-us_topic_0046585384_p83821399268"><a name="en-us_topic_0046585384_p83821399268"></a><a name="en-us_topic_0046585384_p83821399268"></a>After a DB instance is created, you can view its tag details on the <strong id="en-us_topic_0046585384_b144102691817"><a name="en-us_topic_0046585384_b144102691817"></a><a name="en-us_topic_0046585384_b144102691817"></a>Tags</strong> tab. For details, see section <a href="managing-tags-37.md">Managing Tags</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Batch creation

    <a name="en-us_topic_0046585384_table2303143712383"></a>
    <table><thead align="left"><tr id="en-us_topic_0046585384_row630515379381"><th class="cellrowborder" valign="top" width="23.74%" id="mcps1.2.3.1.1"><p id="en-us_topic_0046585384_p131195564383"><a name="en-us_topic_0046585384_p131195564383"></a><a name="en-us_topic_0046585384_p131195564383"></a><strong id="en-us_topic_0046585384_b6929153535713"><a name="en-us_topic_0046585384_b6929153535713"></a><a name="en-us_topic_0046585384_b6929153535713"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76.25999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0046585384_p4119155610385"><a name="en-us_topic_0046585384_p4119155610385"></a><a name="en-us_topic_0046585384_p4119155610385"></a><strong id="en-us_topic_0046585384_b621838185716"><a name="en-us_topic_0046585384_b621838185716"></a><a name="en-us_topic_0046585384_b621838185716"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0046585384_row130593718387"><td class="cellrowborder" valign="top" width="23.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0046585384_p1730583743810"><a name="en-us_topic_0046585384_p1730583743810"></a><a name="en-us_topic_0046585384_p1730583743810"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0046585384_p66611721195715"><a name="en-us_topic_0046585384_p66611721195715"></a><a name="en-us_topic_0046585384_p66611721195715"></a>RDS supports DB instance creation in batches. If you choose to create primary/standby DB instances and set <strong id="en-us_topic_0046585384_b38073135813"><a name="en-us_topic_0046585384_b38073135813"></a><a name="en-us_topic_0046585384_b38073135813"></a>Quantity</strong> to <strong id="en-us_topic_0046585384_b68081716582"><a name="en-us_topic_0046585384_b68081716582"></a><a name="en-us_topic_0046585384_b68081716582"></a>1</strong>, a primary DB instance and a standby DB instance will be created synchronously.</p>
    <p id="en-us_topic_0046585384_p0880182916576"><a name="en-us_topic_0046585384_p0880182916576"></a><a name="en-us_topic_0046585384_p0880182916576"></a>If you create multiple DB instances at a time, they will be named with four digits appended to the DB instance name. For example, if you enter <strong id="en-us_topic_0046585384_b1035516513911"><a name="en-us_topic_0046585384_b1035516513911"></a><a name="en-us_topic_0046585384_b1035516513911"></a>instance</strong>, the first instance will be named as instance-0001, the second as instance-0002, and so on.</p>
    </td>
    </tr>
    </tbody>
    </table>

    After the configuration, click  **Price Calculator**  to view the RDS configuration fee.

    >![](/images/icon-note.gif) **NOTE:**   
    >The performance of your DB instance depends on its configurations. Hardware configuration items include the instance specifications, storage type, and storage space.  

6.  Confirm the specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  To view and manage the DB instance, go to the  **Instance Management**  page.
    -   During the creation process, the DB instance status is  **Creating**.
    -   To refresh the DB instance list, click  ![](figures/refresh.png)  in the upper right corner of the list. When the creation process is complete, the instance status will change to  **Available**.
    -   The automated backup policy is enabled by default. An automated full backup is immediately triggered after a DB instance is created.
    -   The default database port is  **5432**. After a DB instance is created, you can change the database port.

        For details, see section  [Changing the Database Port](changing-the-database-port-(PostgreSQL).md).



