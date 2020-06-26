# Creating a Read Replica<a name="en-us_topic_add_read_replica"></a>

## **Scenarios**<a name="s9f95e14048064f63a1d9be0c9f685f07"></a>

Read replicas are used to enhance the read capabilities of primary DB instances and reduce the load on primary DB instances.

After DB instances are created, you can  create read replicas  for them.

## Procedure<a name="s738501c07aa4426eaeea764d9297251d"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  **Create Read Replica**  in the  **Operation**  column.

    Alternatively, click the target DB instance. In the DB instance topology, click  ![](figures/read.png)  under the primary DB instance to  create read replicas.

5.  On the displayed page, configure information about the read replica and click  **Create Now**.

    **Table  1**  Basic information

    <a name="table64274465191013"></a>
    <table><thead align="left"><tr id="row10238256191013"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.3.1.1"><p id="p45227061191215"><a name="p45227061191215"></a><a name="p45227061191215"></a><strong id="b84235270618284"><a name="b84235270618284"></a><a name="b84235270618284"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.33%" id="mcps1.2.3.1.2"><p id="p39513321191215"><a name="p39513321191215"></a><a name="p39513321191215"></a><strong id="b842352706212013"><a name="b842352706212013"></a><a name="b842352706212013"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1566273919197"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p6072235519197"><a name="p6072235519197"></a><a name="p6072235519197"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p1956370319197"><a name="p1956370319197"></a><a name="p1956370319197"></a>By default, read replicas are in the same region as the primary DB instance.</p>
    </td>
    </tr>
    <tr id="row15611204134715"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p6818201134720"><a name="p6818201134720"></a><a name="p6818201134720"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p40771789134814"><a name="p40771789134814"></a><a name="p40771789134814"></a>Must start with a letter and consist of 4 to 64 characters. It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row16096253164355"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p4480828164359"><a name="p4480828164359"></a><a name="p4480828164359"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p11852143122115"><a name="p11852143122115"></a><a name="p11852143122115"></a>Same as the DB engine version of the primary DB instance by default and cannot be changed.</p>
    </td>
    </tr>
    <tr id="row56400291164351"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p45320621164359"><a name="p45320621164359"></a><a name="p45320621164359"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="p611818314226"><a name="p611818314226"></a><a name="p611818314226"></a>Same as the DB engine version of the primary DB instance by default and cannot be changed.</p>
    </td>
    </tr>
    <tr id="row986226171118"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="p5363100191215"><a name="p5363100191215"></a><a name="p5363100191215"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><div class="p" id="p114913522132"><a name="p114913522132"></a><a name="p114913522132"></a>RDS allows you to deploy primary DB instances and read replicas in a single AZ or across AZs. You can determine whether the read replica AZ is the same as the primary AZ.<a name="ul17956749161310"></a><a name="ul17956749161310"></a><ul id="ul17956749161310"><li>If they are the same, the read replica and primary DB instance are deployed in the same AZ.</li><li>If they are different, the read replica and primary DB instance are deployed in different AZs to ensure data reliability.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="table5231736819158"></a>
    <table><thead align="left"><tr id="row5678434919158"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p48655908191548"><a name="p48655908191548"></a><a name="p48655908191548"></a><strong id="b1550837902"><a name="b1550837902"></a><a name="b1550837902"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p48814496191548"><a name="p48814496191548"></a><a name="p48814496191548"></a><strong id="b673165747"><a name="b673165747"></a><a name="b673165747"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row440922819158"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p19368524191620"><a name="p19368524191620"></a><a name="p19368524191620"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3612111215507"><a name="p3612111215507"></a><a name="p3612111215507"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="p781114612508"><a name="p781114612508"></a><a name="p781114612508"></a></p>
    <p id="p5429821515"><a name="p5429821515"></a><a name="p5429821515"></a></p>
    <p id="p12042810516"><a name="p12042810516"></a><a name="p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="p4689621196"><a name="p4689621196"></a><a name="p4689621196"></a></p>
    <p id="p860165515523"><a name="p860165515523"></a><a name="p860165515523"></a></p>
    <p id="p4610514532"><a name="p4610514532"></a><a name="p4610514532"></a></p>
    <p id="p19542517536"><a name="p19542517536"></a><a name="p19542517536"></a>After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-a-db-instance-class.md">Changing a DB Instance Class</a>.</p>
    <p id="p38285458348"><a name="p38285458348"></a><a name="p38285458348"></a></p>
    </td>
    </tr>
    <tr id="row373765819158"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3335747191620"><a name="p3335747191620"></a><a name="p3335747191620"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p7776143917411"><a name="p7776143917411"></a><a name="p7776143917411"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="ul45492023191733"></a><a name="ul45492023191733"></a><ul id="ul45492023191733"><li><strong id="b842352706111325"><a name="b842352706111325"></a><a name="b842352706111325"></a>Common I/O</strong>: uses the SATA disk type that supports a maximum throughput of 90 MB/s.</li><li><strong id="b11138162474719"><a name="b11138162474719"></a><a name="b11138162474719"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="row5103267419158"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4000592019158"><a name="p4000592019158"></a><a name="p4000592019158"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1382274394912"><a name="p1382274394912"></a><a name="p1382274394912"></a>Contains the system overhead required for inode, reserved block, and database operation.</p>
    <p id="p29201516144816"><a name="p29201516144816"></a><a name="p29201516144816"></a>By default, storage space of a read replica is the same as that of the primary DB instance.</p>
    </td>
    </tr>
    <tr id="row1594852605117"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p595744141914"><a name="p595744141914"></a><a name="p595744141914"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="ul133881550588"></a><a name="ul133881550588"></a><ul id="ul133881550588"><li><strong id="b842352706111219"><a name="b842352706111219"></a><a name="b842352706111219"></a>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="b842352706111223"><a name="b842352706111223"></a><a name="b842352706111223"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="p1950185719127"><a name="p1950185719127"></a><a name="p1950185719127"></a><strong id="b84235270611136"><a name="b84235270611136"></a><a name="b84235270611136"></a>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="note2431518191315"><a name="note2431518191315"></a><a name="note2431518191315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul36901923165110"></a><a name="ul36901923165110"></a><ul id="ul36901923165110"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS is not encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="i84235269720539"><a name="i84235269720539"></a><a name="i84235269720539"></a>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="table37304444569"></a>
    <table><thead align="left"><tr id="row1273164417563"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.3.1.1"><p id="p0966175011569"><a name="p0966175011569"></a><a name="p0966175011569"></a><strong id="b1839008476"><a name="b1839008476"></a><a name="b1839008476"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="81.19%" id="mcps1.2.3.1.2"><p id="p2731144465614"><a name="p2731144465614"></a><a name="p2731144465614"></a><strong id="b79984453"><a name="b79984453"></a><a name="b79984453"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1073164415564"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.3.1.1 "><p id="p77311441563"><a name="p77311441563"></a><a name="p77311441563"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.19%" headers="mcps1.2.3.1.2 "><p id="p13731104420562"><a name="p13731104420562"></a><a name="p13731104420562"></a>Same as the primary DB instance's VPC.</p>
    </td>
    </tr>
    <tr id="row1173114475611"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.3.1.1 "><p id="p1273115449568"><a name="p1273115449568"></a><a name="p1273115449568"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.19%" headers="mcps1.2.3.1.2 "><p id="p1731174415614"><a name="p1731174415614"></a><a name="p1731174415614"></a>Same as the primary DB instance's subnet. A floating IP address is automatically assigned when you create a read replica. You can also enter an unused floating IP address in the subnet segment. After the read replica is created, you can change the floating IP address.</p>
    </td>
    </tr>
    <tr id="row573117446566"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.3.1.1 "><p id="p573164465611"><a name="p573164465611"></a><a name="p573164465611"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.19%" headers="mcps1.2.3.1.2 "><p id="p18524934105811"><a name="p18524934105811"></a><a name="p18524934105811"></a>Same as the primary DB instance's VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Confirm specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  After a read replica is created, you can view and manage it.

    For details about how to manage read replicas, see  [Managing a Read Replica](managing-a-read-replica.md).

    You can view the detailed progress and result of the task on the  **Task Center**  page. 


