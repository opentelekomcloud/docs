# Step 1: Create a DB Instance<a name="en-us_topic_0046585384"></a>

## **Scenarios**<a name="section3881006517148"></a>

You can create DB instances using the RDS console or APIs. For details about how to  create DB instances  using APIs, see the "Creating a DB Instance" section in the  _Relational Database Service API Reference_. This section describes how to  create a DB instance  on the RDS console.

RDS allows you to tailor your computing resources and storage space to your business needs.

## Procedure<a name="sddcec3dbbccd43178a23424d29482e1a"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click  **Create DB Instance**.
5.  On the displayed page, configure information about your DB instance. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="table17676102015448"></a>
    <table><thead align="left"><tr id="row196591120114414"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p1765922011445"><a name="p1765922011445"></a><a name="p1765922011445"></a><strong id="b84235270618284_1"><a name="b84235270618284_1"></a><a name="b84235270618284_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p3659102019443"><a name="p3659102019443"></a><a name="p3659102019443"></a><strong id="b842352706212013_1"><a name="b842352706212013_1"></a><a name="b842352706212013_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13659192074416"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p136595209441"><a name="p136595209441"></a><a name="p136595209441"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p15971451194710"><a name="p15971451194710"></a><a name="p15971451194710"></a>A region where the tenant is located. It can be changed in the upper left corner of the page.</p>
    <div class="note" id="note19961614265"><a name="note19961614265"></a><a name="note19961614265"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1999615642620"><a name="p1999615642620"></a><a name="p1999615642620"></a>Products in different regions cannot communicate with each other through a private network and you cannot change the region of a DB instance after creating the instance. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1367612024415"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p365952016449"><a name="p365952016449"></a><a name="p365952016449"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p34931419132919"><a name="p34931419132919"></a><a name="p34931419132919"></a>Must start with a letter and consist of 4 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row14676112084411"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p6676162019441"><a name="p6676162019441"></a><a name="p6676162019441"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p567611206445"><a name="p567611206445"></a><a name="p567611206445"></a>Set to <strong id="b84235270611955"><a name="b84235270611955"></a><a name="b84235270611955"></a>PostgreSQL</strong>.</p>
    </td>
    </tr>
    <tr id="row667672017449"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p10676102074415"><a name="p10676102074415"></a><a name="p10676102074415"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p545215541125"><a name="p545215541125"></a><a name="p545215541125"></a></p>
    <p id="p1961756101213"><a name="p1961756101213"></a><a name="p1961756101213"></a></p>
    <p id="p145823010132"><a name="p145823010132"></a><a name="p145823010132"></a>For details, see section <a href="db-engines-and-versions.md">DB Engines and Versions</a>.</p>
    <p id="p116761220154415"><a name="p116761220154415"></a><a name="p116761220154415"></a></p>
    <p id="p192551714184510"><a name="p192551714184510"></a><a name="p192551714184510"></a>Different DB engine versions are supported in different regions.</p>
    <p id="p687715327516"><a name="p687715327516"></a><a name="p687715327516"></a>If you use a PostgreSQL database, select a proper DB engine version based on service requirements. You are advised to select the latest available version because it is more stable, reliable, and secure.</p>
    </td>
    </tr>
    <tr id="row17676220104418"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p13676192011449"><a name="p13676192011449"></a><a name="p13676192011449"></a>DB Instance Type and AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="ul7676820184413"></a><a name="ul7676820184413"></a><ul id="ul7676820184413"><li><strong id="b177591121144916"><a name="b177591121144916"></a><a name="b177591121144916"></a>Primary/Standby</strong>: uses the HA architecture with a primary DB instance and a synchronous standby DB instance. It is suitable for production databases of large- and medium-sized enterprises in Internet, Internet of Things (IoT), retail e-commerce sales, logistics, gaming, and other sectors. The standby DB instance improves instance reliability and is invisible to you after being created.<p id="p3659122084410"><a name="p3659122084410"></a><a name="p3659122084410"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network. </p>
    <p id="p14411939141316"><a name="p14411939141316"></a><a name="p14411939141316"></a>RDS supports deploying primary and standby DB instances in an AZ or across AZs. You can determine whether the standby AZ is the same as the primary AZ.</p>
    <a name="ul1241210399138"></a><a name="ul1241210399138"></a><ul id="ul1241210399138"><li>If they are the same (default setting), the primary and standby DB instances are deployed in the same AZ.</li><li>If they are different, the primary and standby DB instances are deployed in different AZs to ensure failover support and high availability.</li></ul>
    </li><li><strong id="b29771729114913"><a name="b29771729114913"></a><a name="b29771729114913"></a>Single</strong>: uses the single-node architecture, which is more cost-effective than mainstream primary/standby DB instances. It is suitable for developing and testing of microsites, and small- and medium-sized enterprises, or for learning about RDS.</li></ul>
    </td>
    </tr>
    <tr id="row1675018111332"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p188281545173410"><a name="p188281545173410"></a><a name="p188281545173410"></a>Time Zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1682834520347"><a name="p1682834520347"></a><a name="p1682834520347"></a>You need to select a time zone for your DB instance according to the longitude and latitude of the region hosting your DB instance. Can be selected during DB instance creation and can be changed after the DB instance is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="table17676620144413"></a>
    <table><thead align="left"><tr id="row06763201449"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p19676112013449"><a name="p19676112013449"></a><a name="p19676112013449"></a><strong id="b28465709112351"><a name="b28465709112351"></a><a name="b28465709112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p66761120154418"><a name="p66761120154418"></a><a name="p66761120154418"></a><strong id="b9357258112351"><a name="b9357258112351"></a><a name="b9357258112351"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row186761520134411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1676182013443"><a name="p1676182013443"></a><a name="p1676182013443"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3612111215507"><a name="p3612111215507"></a><a name="p3612111215507"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="p781114612508"><a name="p781114612508"></a><a name="p781114612508"></a></p>
    <p id="p5429821515"><a name="p5429821515"></a><a name="p5429821515"></a></p>
    <p id="p12042810516"><a name="p12042810516"></a><a name="p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="p4689621196"><a name="p4689621196"></a><a name="p4689621196"></a></p>
    <p id="p860165515523"><a name="p860165515523"></a><a name="p860165515523"></a></p>
    <p id="p4610514532"><a name="p4610514532"></a><a name="p4610514532"></a></p>
    <p id="p19542517536"><a name="p19542517536"></a><a name="p19542517536"></a>After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-a-db-instance-class-(PostgreSQL).md">Changing a DB Instance Class</a>.</p>
    <p id="p38285458348"><a name="p38285458348"></a><a name="p38285458348"></a></p>
    </td>
    </tr>
    <tr id="row116761020134412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p96761020194411"><a name="p96761020194411"></a><a name="p96761020194411"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p799718574114"><a name="p799718574114"></a><a name="p799718574114"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="ul17230161564119"></a><a name="ul17230161564119"></a><ul id="ul17230161564119"><li><strong id="b1499317517538"><a name="b1499317517538"></a><a name="b1499317517538"></a>Common I/O</strong>: uses the SATA disk type, with a maximum throughput of 90 MB/s.</li><li><strong id="b175932011548"><a name="b175932011548"></a><a name="b175932011548"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="row1467616204445"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p176763206449"><a name="p176763206449"></a><a name="p176763206449"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p12950023171218"><a name="p12950023171218"></a><a name="p12950023171218"></a>Contains the system overhead required for inode, reserved block, and database operation. Can range in size from 40 GB to 4000 GB and can be scaled up only by a multiple of 10 GB.</p>
    <p id="p4990256102610"><a name="p4990256102610"></a><a name="p4990256102610"></a></p>
    <p id="p5999151032711"><a name="p5999151032711"></a><a name="p5999151032711"></a></p>
    <p id="p13797182010276"><a name="p13797182010276"></a><a name="p13797182010276"></a>After a DB instance is created, you can scale up its storage space. For details, see section <a href="scaling-up-storage-space.md">Scaling Up Storage Space</a>.</p>
    <p id="p1182820454348"><a name="p1182820454348"></a><a name="p1182820454348"></a></p>
    </td>
    </tr>
    <tr id="row3377101065014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p119341314506"><a name="p119341314506"></a><a name="p119341314506"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="ul141961813185014"></a><a name="ul141961813185014"></a><ul id="ul141961813185014"><li><strong id="b84235270611657"><a name="b84235270611657"></a><a name="b84235270611657"></a>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="b8423527061172"><a name="b8423527061172"></a><a name="b8423527061172"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="p19208161316507"><a name="p19208161316507"></a><a name="p19208161316507"></a><strong id="b8423527061176"><a name="b8423527061176"></a><a name="b8423527061176"></a>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="note72081013185015"><a name="note72081013185015"></a><a name="note72081013185015"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul221110134509"></a><a name="ul221110134509"></a><ul id="ul221110134509"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS is not encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="i84235269720539"><a name="i84235269720539"></a><a name="i84235269720539"></a>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="table1567602014410"></a>
    <table><thead align="left"><tr id="row9676172019444"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.3.1.1"><p id="p1267632012446"><a name="p1267632012446"></a><a name="p1267632012446"></a><strong id="b10991376112351"><a name="b10991376112351"></a><a name="b10991376112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.95%" id="mcps1.2.3.1.2"><p id="p76761320184410"><a name="p76761320184410"></a><a name="p76761320184410"></a><strong id="b842352706212013_5"><a name="b842352706212013_5"></a><a name="b842352706212013_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6676122014412"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p1567612074417"><a name="p1567612074417"></a><a name="p1567612074417"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p567672084416"><a name="p567672084416"></a><a name="p567672084416"></a>A dedicated virtual network in which your RDS DB instances are located. Isolates networks for different services. You can select an existing VPC or create a VPC. For details on how to create a VPC, see the "Creating a VPC" section in the <em id="i842352697152613"><a name="i842352697152613"></a><a name="i842352697152613"></a>Virtual Private Cloud User Guide</em>.</p>
    <p id="p146764206449"><a name="p146764206449"></a><a name="p146764206449"></a>If no VPC is available, RDS allocates a VPC to you by default.</p>
    </td>
    </tr>
    <tr id="row196763203449"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p9676152015447"><a name="p9676152015447"></a><a name="p9676152015447"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p16676102064418"><a name="p16676102064418"></a><a name="p16676102064418"></a>Improves network security by providing dedicated network resources that are logically isolated from other networks. Subnets take effect only within an AZ. The Dynamic Host Configuration Protocol (DHCP) function must be enabled by default for subnets in which you plan to create RDS DB instances and cannot be disabled.</p>
    <p id="p118281445193416"><a name="p118281445193416"></a><a name="p118281445193416"></a>A floating IP address is automatically assigned when you create a DB instance. You can also enter an unused floating IP address in the subnet segment. After the DB instance is created, you can change the floating IP address.</p>
    </td>
    </tr>
    <tr id="row167622084411"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p967652018443"><a name="p967652018443"></a><a name="p967652018443"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p2676420194417"><a name="p2676420194417"></a><a name="p2676420194417"></a>Controls the access that traffic has in and out of a DB instance. By default, the security group associated with the DB instance is authorized.</p>
    <p id="p106761320154412"><a name="p106761320154412"></a><a name="p106761320154412"></a>Enhances security by controlling access to RDS from other services. You need to add rules to a security group that enable you to connect to your DB instance.</p>
    <p id="p867616204441"><a name="p867616204441"></a><a name="p867616204441"></a>If no security group is available, RDS allocates a security group to you by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="table2067602034417"></a>
    <table><thead align="left"><tr id="row867602015445"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.3.1.1"><p id="p0676172094416"><a name="p0676172094416"></a><a name="p0676172094416"></a><strong id="b62569647112351"><a name="b62569647112351"></a><a name="b62569647112351"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.14%" id="mcps1.2.3.1.2"><p id="p1767692064412"><a name="p1767692064412"></a><a name="p1767692064412"></a><strong id="b61301106112351"><a name="b61301106112351"></a><a name="b61301106112351"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46766201446"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="p196761220104417"><a name="p196761220104417"></a><a name="p196761220104417"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="p867632012441"><a name="p867632012441"></a><a name="p867632012441"></a>The default login name for the database is <strong id="b842352706184259"><a name="b842352706184259"></a><a name="b842352706184259"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="row1267602012448"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="p3676620104415"><a name="p3676620104415"></a><a name="p3676620104415"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="p46761720194415"><a name="p46761720194415"></a><a name="p46761720194415"></a>Must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters (~!@#%^*-_+?,). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="p76765206446"><a name="p76765206446"></a><a name="p76765206446"></a>Keep this password secure. The system cannot retrieve it.</p>
    <p id="p432375214012"><a name="p432375214012"></a><a name="p432375214012"></a></p>
    <p id="p136346617119"><a name="p136346617119"></a><a name="p136346617119"></a>After a DB instance is created, you can reset this password. For details, see section <a href="resetting-the-administrator-password-39.md">Resetting the Administrator Password</a>.</p>
    </td>
    </tr>
    <tr id="row106762020204410"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="p16676320124415"><a name="p16676320124415"></a><a name="p16676320124415"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="p19676620144414"><a name="p19676620144414"></a><a name="p19676620144414"></a>Must be the same as <span class="parmname" id="parmname769647905141841"><a name="parmname769647905141841"></a><a name="parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    <tr id="row91491594316"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="p9676320204413"><a name="p9676320204413"></a><a name="p9676320204413"></a>Parameter Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="p18676102012444"><a name="p18676102012444"></a><a name="p18676102012444"></a>Contains engine configuration values that can be applied to one or more DB instances. If you intend to create primary/standby DB instances, they use the same parameter template. You can modify instance parameters as required after the DB instance is created.</p>
    <div class="notice" id="note365219366379"><a name="note365219366379"></a><a name="note365219366379"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p965293617376"><a name="p965293617376"></a><a name="p965293617376"></a>If you use a custom parameter template when creating a DB instance, the specification-related parameters in the custom template are not delivered. Instead, the default values are used.</p>
    <a name="ul827715317325"></a><a name="ul827715317325"></a><ul id="ul827715317325"><li><span class="parmname" id="parmname1427512817352"><a name="parmname1427512817352"></a><a name="parmname1427512817352"></a><b>maintenance_work_mem</b></span></li><li><span class="parmname" id="parmname17967163018354"><a name="parmname17967163018354"></a><a name="parmname17967163018354"></a><b>shared_buffers</b></span></li><li><span class="parmname" id="parmname9556933163518"><a name="parmname9556933163518"></a><a name="parmname9556933163518"></a><b>max_connections</b></span></li><li><span class="parmname" id="parmname1313523713512"><a name="parmname1313523713512"></a><a name="parmname1313523713512"></a><b>effective_cache_size</b></span></li></ul>
    </div></div>
    <p id="p147431598590"><a name="p147431598590"></a><a name="p147431598590"></a></p>
    <p id="p1581213215597"><a name="p1581213215597"></a><a name="p1581213215597"></a></p>
    <p id="p757011330597"><a name="p757011330597"></a><a name="p757011330597"></a>You can modify the instance parameters as required after the DB instance is created. For details see section <a href="modifying-parameters-in-a-parameter-template-52.md">Modifying Parameters in a Parameter Template</a>.</p>
    <p id="p1282884515344"><a name="p1282884515344"></a><a name="p1282884515344"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Tags

    <a name="table555184732217"></a>
    <table><thead align="left"><tr id="row105624782217"><th class="cellrowborder" valign="top" width="24.66%" id="mcps1.2.3.1.1"><p id="p852913210175"><a name="p852913210175"></a><a name="p852913210175"></a><strong id="b6455113171816"><a name="b6455113171816"></a><a name="b6455113171816"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.33999999999999%" id="mcps1.2.3.1.2"><p id="p175291021161717"><a name="p175291021161717"></a><a name="p175291021161717"></a><strong id="b778201581819"><a name="b778201581819"></a><a name="b778201581819"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55620472221"><td class="cellrowborder" valign="top" width="24.66%" headers="mcps1.2.3.1.1 "><p id="p7529202171713"><a name="p7529202171713"></a><a name="p7529202171713"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.33999999999999%" headers="mcps1.2.3.1.2 "><p id="p141127570267"><a name="p141127570267"></a><a name="p141127570267"></a>Tags an RDS DB instance. This configuration is optional. Adding tags to RDS DB instances helps you better identify and manage the DB instances. A maximum of 20 tags can be added for each DB instance.</p>
    <p id="p83821399268"><a name="p83821399268"></a><a name="p83821399268"></a>After a DB instance is created, you can view its tag details on the <strong id="b144102691817"><a name="b144102691817"></a><a name="b144102691817"></a>Tags</strong> tab. For details, see section <a href="managing-tags-(PostgreSQL).md">Managing Tags</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Batch creation

    <a name="table2303143712383"></a>
    <table><thead align="left"><tr id="row630515379381"><th class="cellrowborder" valign="top" width="23.74%" id="mcps1.2.3.1.1"><p id="p131195564383"><a name="p131195564383"></a><a name="p131195564383"></a><strong id="b6929153535713"><a name="b6929153535713"></a><a name="b6929153535713"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76.25999999999999%" id="mcps1.2.3.1.2"><p id="p4119155610385"><a name="p4119155610385"></a><a name="p4119155610385"></a><strong id="b621838185716"><a name="b621838185716"></a><a name="b621838185716"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row130593718387"><td class="cellrowborder" valign="top" width="23.74%" headers="mcps1.2.3.1.1 "><p id="p1730583743810"><a name="p1730583743810"></a><a name="p1730583743810"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p66611721195715"><a name="p66611721195715"></a><a name="p66611721195715"></a>RDS supports DB instance creation in batches. If you choose to create primary/standby DB instances and set <strong id="b38073135813"><a name="b38073135813"></a><a name="b38073135813"></a>Quantity</strong> to <strong id="b68081716582"><a name="b68081716582"></a><a name="b68081716582"></a>1</strong>, a primary DB instance and a standby DB instance will be created synchronously.</p>
    <p id="p0880182916576"><a name="p0880182916576"></a><a name="p0880182916576"></a>If you create multiple DB instances at a time, they will be named with four digits appended to the DB instance name. For example, if you enter <strong id="b1035516513911"><a name="b1035516513911"></a><a name="b1035516513911"></a>instance</strong>, the first instance will be named as instance-0001, the second as instance-0002, and so on.</p>
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



