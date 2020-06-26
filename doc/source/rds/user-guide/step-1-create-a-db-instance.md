# Step 1: Create a DB Instance<a name="en-us_topic_0046585334"></a>

## **Scenarios**<a name="section3881006517148"></a>

This section describes how to create a DB instance on the management console.

The DB instance class and storage space you need depends on your processing power and memory requirements.

## Procedure<a name="sa49e76d034cc442ab719cd1f42a02558"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click  **Create DB Instance**.
5.  On the displayed page, configure information about your DB instance. Then, click  **Create Now**.

    **Table  1**  Basic information

    <a name="table2225129135419"></a>
    <table><thead align="left"><tr id="row82251935412"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.3.1.1"><p id="p142251694540"><a name="p142251694540"></a><a name="p142251694540"></a><strong id="b84235270618284_1"><a name="b84235270618284_1"></a><a name="b84235270618284_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.33%" id="mcps1.2.3.1.2"><p id="p1322516915549"><a name="p1322516915549"></a><a name="p1322516915549"></a><strong id="b842352706212013_1"><a name="b842352706212013_1"></a><a name="b842352706212013_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row622516920543"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p82251193549"><a name="p82251193549"></a><a name="p82251193549"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p134556434485"><a name="p134556434485"></a><a name="p134556434485"></a>A region where the tenant is located. It can be changed in the upper left corner of the page.</p>
    <div class="note" id="note1191592913255"><a name="note1191592913255"></a><a name="note1191592913255"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p791682952516"><a name="p791682952516"></a><a name="p791682952516"></a>Products in different regions cannot communicate with each other through a private network and you cannot change the region of a DB instance after creating the instance. Therefore, exercise caution when selecting a region.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1722517910546"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p1722511913546"><a name="p1722511913546"></a><a name="p1722511913546"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p181596279382"><a name="p181596279382"></a><a name="p181596279382"></a>Must start with a letter and consist of 4 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row8225697547"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p1422515955416"><a name="p1422515955416"></a><a name="p1422515955416"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p1922515917542"><a name="p1922515917542"></a><a name="p1922515917542"></a>Set to <strong id="b84235270611622"><a name="b84235270611622"></a><a name="b84235270611622"></a>MySQL</strong>.</p>
    </td>
    </tr>
    <tr id="row62256995419"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p322516920542"><a name="p322516920542"></a><a name="p322516920542"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p22259918542"><a name="p22259918542"></a><a name="p22259918542"></a></p>
    <p id="p222519918543"><a name="p222519918543"></a><a name="p222519918543"></a></p>
    <p id="p1454734014442"><a name="p1454734014442"></a><a name="p1454734014442"></a>For details, see <a href="db-engines-and-versions.md">DB Engines and Versions</a>.</p>
    <p id="p1222512911542"><a name="p1222512911542"></a><a name="p1222512911542"></a>Different DB engine versions are supported in different regions.</p>
    <p id="p1322579205418"><a name="p1322579205418"></a><a name="p1322579205418"></a>If you use a MySQL database, select a proper DB engine version based on service requirements. You are advised to select the latest available version because it is more stable, reliable, and secure.</p>
    </td>
    </tr>
    <tr id="row17225298543"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p62251493546"><a name="p62251493546"></a><a name="p62251493546"></a>DB Instance Type and AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><a name="ul142258910549"></a><a name="ul142258910549"></a><ul id="ul142258910549"><li><strong id="b162633297234"><a name="b162633297234"></a><a name="b162633297234"></a>Primary/Standby</strong>: uses the HA architecture with a primary DB instance and a synchronous standby DB instance. It is suitable for production databases of large- and medium-sized enterprises in Internet, Internet of Things (IoT), retail e-commerce sales, logistics, gaming, and other sectors. The standby DB instance improves instance reliability and is invisible to you after being created.<p id="p32258914549"><a name="p32258914549"></a><a name="p32258914549"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network. </p>
    <p id="p8225139165419"><a name="p8225139165419"></a><a name="p8225139165419"></a>RDS allows you to deploy primary and standby DB instances in an AZ or across AZs. You can determine whether the standby AZ is the same as the primary AZ.</p>
    <a name="ul18225139185411"></a><a name="ul18225139185411"></a><ul id="ul18225139185411"><li>If they are the same (default setting), the primary and standby DB instances are deployed in the same AZ.</li><li>If they are different, the primary and standby DB instances are deployed in different AZs to ensure failover support and high availability.</li></ul>
    </li><li><strong id="b1014418272268"><a name="b1014418272268"></a><a name="b1014418272268"></a>Single</strong>: uses the single-node architecture, which is more cost-effective than mainstream primary/standby DB instances. It is suitable for developing and testing of microsites, and small- and medium-sized enterprises, or for learning about RDS.</li></ul>
    </td>
    </tr>
    <tr id="row1522599175410"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p112255955412"><a name="p112255955412"></a><a name="p112255955412"></a>Time Zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p1122529195410"><a name="p1122529195410"></a><a name="p1122529195410"></a>You need to select a time zone for your DB instance according to the longitude and latitude of the region hosting your DB instance. The time zone can be selected during the DB instance creation and changed after the instance is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="table13240997543"></a>
    <table><thead align="left"><tr id="row2225890545"><th class="cellrowborder" valign="top" width="19.98%" id="mcps1.2.3.1.1"><p id="p132257916546"><a name="p132257916546"></a><a name="p132257916546"></a><strong id="b84235270618284_3"><a name="b84235270618284_3"></a><a name="b84235270618284_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.02%" id="mcps1.2.3.1.2"><p id="p112251899547"><a name="p112251899547"></a><a name="p112251899547"></a><strong id="b842352706212013_3"><a name="b842352706212013_3"></a><a name="b842352706212013_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15225999544"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p3225169185417"><a name="p3225169185417"></a><a name="p3225169185417"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p32253910544"><a name="p32253910544"></a><a name="p32253910544"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="p6225199205417"><a name="p6225199205417"></a><a name="p6225199205417"></a></p>
    <p id="p182251396548"><a name="p182251396548"></a><a name="p182251396548"></a></p>
    <p id="p32256913542"><a name="p32256913542"></a><a name="p32256913542"></a></p>
    <p id="p2022518955412"><a name="p2022518955412"></a><a name="p2022518955412"></a></p>
    <p id="p12042810516"><a name="p12042810516"></a><a name="p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="p19542517536"><a name="p19542517536"></a><a name="p19542517536"></a>After a DB instance is created, you can change its instance class. For details, see section <a href="changing-a-db-instance-class.md">Changing a DB Instance Class</a>.</p>
    </td>
    </tr>
    <tr id="row8240994542"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p1124049125419"><a name="p1124049125419"></a><a name="p1124049125419"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p16240139125418"><a name="p16240139125418"></a><a name="p16240139125418"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="ul14828144553416"></a><a name="ul14828144553416"></a><ul id="ul14828144553416"><li><strong id="b1452912323810"><a name="b1452912323810"></a><a name="b1452912323810"></a>Common I/O</strong>: uses the SATA disk type, with a maximum throughput of 90 MB/s.</li><li><strong id="b842352706111332"><a name="b842352706111332"></a><a name="b842352706111332"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="row2240794541"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p192402091545"><a name="p192402091545"></a><a name="p192402091545"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p1724017955414"><a name="p1724017955414"></a><a name="p1724017955414"></a>Contains the system overhead required for inode, reserved block, and database operation. Storage space can range in size from 40 GB to 4000 GB and can be scaled up only by a multiple of 10 GB. </p>
    <p id="p9240139155415"><a name="p9240139155415"></a><a name="p9240139155415"></a></p>
    <p id="p1824012935420"><a name="p1824012935420"></a><a name="p1824012935420"></a></p>
    <p id="p13797182010276"><a name="p13797182010276"></a><a name="p13797182010276"></a>After a DB instance is created, you can scale up its storage space. For details, see section <a href="scaling-up-storage-space.md">Scaling Up Storage Space</a>.</p>
    </td>
    </tr>
    <tr id="row15240109205415"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p1624014905414"><a name="p1624014905414"></a><a name="p1624014905414"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><a name="ul02406995419"></a><a name="ul02406995419"></a><ul id="ul02406995419"><li><strong id="b84235270611657"><a name="b84235270611657"></a><a name="b84235270611657"></a>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="b8423527061172"><a name="b8423527061172"></a><a name="b8423527061172"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="p122404995419"><a name="p122404995419"></a><a name="p122404995419"></a><strong id="b8423527061176"><a name="b8423527061176"></a><a name="b8423527061176"></a>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="note52401494544"><a name="note52401494544"></a><a name="note52401494544"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul624013985411"></a><a name="ul624013985411"></a><ul id="ul624013985411"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS will not be encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="i4950102715563"><a name="i4950102715563"></a><a name="i4950102715563"></a>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="table42406975413"></a>
    <table><thead align="left"><tr id="row42407919548"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.3.1.1"><p id="p11240189205418"><a name="p11240189205418"></a><a name="p11240189205418"></a><strong id="b84235270618284_7"><a name="b84235270618284_7"></a><a name="b84235270618284_7"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="78.95%" id="mcps1.2.3.1.2"><p id="p324014918549"><a name="p324014918549"></a><a name="p324014918549"></a><strong id="b842352706212013_7"><a name="b842352706212013_7"></a><a name="b842352706212013_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row224039205415"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p1724018911549"><a name="p1724018911549"></a><a name="p1724018911549"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p1124011975415"><a name="p1124011975415"></a><a name="p1124011975415"></a>A dedicated virtual network in which your RDS DB instances are located. Isolates networks for different services. You can select an existing VPC or create a VPC. For details on how to create a VPC, see the "Creating a VPC" section in the <em id="i842352697152613"><a name="i842352697152613"></a><a name="i842352697152613"></a>Virtual Private Cloud User Guide</em>.</p>
    <p id="p3240796540"><a name="p3240796540"></a><a name="p3240796540"></a>If no VPC is available, RDS allocates a VPC to you by default.</p>
    </td>
    </tr>
    <tr id="row124012915413"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p102402945412"><a name="p102402945412"></a><a name="p102402945412"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p22408919547"><a name="p22408919547"></a><a name="p22408919547"></a>Improves network security by providing dedicated network resources that are logically isolated from other networks. Subnets take effect only within an AZ. The Dynamic Host Configuration Protocol (DHCP) function must be enabled by default for subnets in which you plan to create RDS DB instances and cannot be disabled.</p>
    <p id="p2240209185413"><a name="p2240209185413"></a><a name="p2240209185413"></a>A floating IP address is automatically assigned when you create a DB instance. You can also enter an unused floating IP address in the subnet segment. After the DB instance is created, you can change the floating IP address.</p>
    </td>
    </tr>
    <tr id="row122405915418"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.3.1.1 "><p id="p724016917546"><a name="p724016917546"></a><a name="p724016917546"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.95%" headers="mcps1.2.3.1.2 "><p id="p162402915543"><a name="p162402915543"></a><a name="p162402915543"></a>Enhances security by controlling access to RDS from other services. You need to add rules to a security group that enable you to connect to your DB instance.</p>
    <p id="p224029195419"><a name="p224029195419"></a><a name="p224029195419"></a>If no security group is available or has been created, RDS allocates a security group to you by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Database configuration

    <a name="table13240209195412"></a>
    <table><thead align="left"><tr id="row1424011975415"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p1524016975416"><a name="p1524016975416"></a><a name="p1524016975416"></a><strong id="b84235270618284_9"><a name="b84235270618284_9"></a><a name="b84235270618284_9"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p72404919543"><a name="p72404919543"></a><a name="p72404919543"></a><strong id="b84235270618288"><a name="b84235270618288"></a><a name="b84235270618288"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1924089105419"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p024020916544"><a name="p024020916544"></a><a name="p024020916544"></a>Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p192402920541"><a name="p192402920541"></a><a name="p192402920541"></a>The default login name for the database is <strong id="b842352706184259"><a name="b842352706184259"></a><a name="b842352706184259"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="row10240119115418"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p11240399542"><a name="p11240399542"></a><a name="p11240399542"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p7240129205418"><a name="p7240129205418"></a><a name="p7240129205418"></a>Must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters (~!@#%^*-_+?,). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.</p>
    <p id="p172408985415"><a name="p172408985415"></a><a name="p172408985415"></a>Keep this password secure. The system cannot retrieve it.</p>
    <p id="p624089165419"><a name="p624089165419"></a><a name="p624089165419"></a></p>
    <p id="p136346617119"><a name="p136346617119"></a><a name="p136346617119"></a>After a DB instance is created, you can reset this password. For details, see section <a href="resetting-the-administrator-password.md">Resetting the Administrator Password</a>.</p>
    </td>
    </tr>
    <tr id="row1924015915547"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p124012911542"><a name="p124012911542"></a><a name="p124012911542"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p19240179175411"><a name="p19240179175411"></a><a name="p19240179175411"></a>Must be the same as <span class="parmname" id="parmname769647905141841"><a name="parmname769647905141841"></a><a name="parmname769647905141841"></a><b>Administrator Password</b></span>.</p>
    </td>
    </tr>
    <tr id="row724017912543"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p92404915419"><a name="p92404915419"></a><a name="p92404915419"></a>Parameter Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p1324089125419"><a name="p1324089125419"></a><a name="p1324089125419"></a>Contains engine configuration values that can be applied to one or more DB instances. If you intend to create primary/standby DB instances, they use the same parameter template. You can modify the instance parameters as required after the DB instance is created.</p>
    <div class="notice" id="note365219366379"><a name="note365219366379"></a><a name="note365219366379"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p965293617376"><a name="p965293617376"></a><a name="p965293617376"></a>If you use a custom parameter template when creating a DB instance, the specification-related parameters in the custom template are not delivered. Instead, the default values are used.</p>
    <a name="ul1696522792620"></a><a name="ul1696522792620"></a><ul id="ul1696522792620"><li><span class="parmname" id="parmname20138115253516"><a name="parmname20138115253516"></a><a name="parmname20138115253516"></a><b>back_log</b></span></li><li><span class="parmname" id="parmname25352551356"><a name="parmname25352551356"></a><a name="parmname25352551356"></a><b>innodb_io_capacity_max</b></span></li><li><span class="parmname" id="parmname14661357143516"><a name="parmname14661357143516"></a><a name="parmname14661357143516"></a><b>max_connections</b></span></li><li><span class="parmname" id="parmname6765659143517"><a name="parmname6765659143517"></a><a name="parmname6765659143517"></a><b>innodb_io_capacity</b></span></li><li><span class="parmname" id="parmname96529120369"><a name="parmname96529120369"></a><a name="parmname96529120369"></a><b>innodb_buffer_pool_size</b></span></li><li><span class="parmname" id="parmname168811338367"><a name="parmname168811338367"></a><a name="parmname168811338367"></a><b>innodb_buffer_pool_instances</b></span></li></ul>
    </div></div>
    <p id="p1224019915415"><a name="p1224019915415"></a><a name="p1224019915415"></a></p>
    <p id="p102401090542"><a name="p102401090542"></a><a name="p102401090542"></a></p>
    <p id="p757011330597"><a name="p757011330597"></a><a name="p757011330597"></a>You can modify the instance parameters as required after the DB instance is created. For details, see section <a href="modifying-parameters-in-a-parameter-template.md">Modifying Parameters in a Parameter Template</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Tags

    <a name="table1362213221313"></a>
    <table><thead align="left"><tr id="row15623123291318"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p852913210175"><a name="p852913210175"></a><a name="p852913210175"></a><strong id="b482011591496"><a name="b482011591496"></a><a name="b482011591496"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p175291021161717"><a name="p175291021161717"></a><a name="p175291021161717"></a><strong id="b874415115018"><a name="b874415115018"></a><a name="b874415115018"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row562313221311"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p7529202171713"><a name="p7529202171713"></a><a name="p7529202171713"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p141127570267"><a name="p141127570267"></a><a name="p141127570267"></a>Tags an RDS DB instance. This configuration is optional. Adding tags to RDS DB instances helps you better identify and manage the DB instances. A maximum of 20 tags can be added for each DB instance.</p>
    <p id="p83821399268"><a name="p83821399268"></a><a name="p83821399268"></a>After a DB instance is created, you can click it and view its details on the <strong id="b362324625716"><a name="b362324625716"></a><a name="b362324625716"></a>Tags</strong> page. For details, see section <a href="managing-tags.md">Managing Tags</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Batch creation

    <a name="table2303143712383"></a>
    <table><thead align="left"><tr id="row630515379381"><th class="cellrowborder" valign="top" width="23.74%" id="mcps1.2.3.1.1"><p id="p131195564383"><a name="p131195564383"></a><a name="p131195564383"></a><strong id="b84235270618284_1_1"><a name="b84235270618284_1_1"></a><a name="b84235270618284_1_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76.25999999999999%" id="mcps1.2.3.1.2"><p id="p4119155610385"><a name="p4119155610385"></a><a name="p4119155610385"></a><strong id="b581495475611"><a name="b581495475611"></a><a name="b581495475611"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row130593718387"><td class="cellrowborder" valign="top" width="23.74%" headers="mcps1.2.3.1.1 "><p id="p1730583743810"><a name="p1730583743810"></a><a name="p1730583743810"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p930543712381"><a name="p930543712381"></a><a name="p930543712381"></a>RDS supports DB instance creation in batches. If you choose to create primary/standby DB instances and set <strong id="b196891458165619"><a name="b196891458165619"></a><a name="b196891458165619"></a>Quantity</strong> to <strong id="b176895581560"><a name="b176895581560"></a><a name="b176895581560"></a>1</strong>, a primary DB instance and a standby DB instance will be created synchronously.</p>
    <p id="p74561272211"><a name="p74561272211"></a><a name="p74561272211"></a>If you create multiple DB instances at a time, they will be named with four digits appended to the DB instance name. For example, if you enter <strong id="b4318125891719"><a name="b4318125891719"></a><a name="b4318125891719"></a>instance</strong>, the first instance will be named as instance-0001, the second as instance-0002, and so on.</p>
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
    -   During the creation process, the DB instance status is  **Creating**. You can view the detailed progress and result of the task on the  **Task Center**  page. To refresh the DB instance list, click  ![](figures/refresh.png)  in the upper right corner of the list. When the creation process is complete, the instance status will change to  **Available**.
    -   The automated backup policy is enabled by default. After the DB instance is created, you can modify the automated backup policy. An automated full backup is immediately triggered after a DB instance is created.
    -   The default database port is  **3306**. After a DB instance is created, you can change its port.

        For details, see section  [Changing the Database Port](changing-the-database-port.md).



