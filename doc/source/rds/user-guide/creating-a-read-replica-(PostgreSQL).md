# Creating a Read Replica<a name="rds_add_read_replica_pg"></a>

## **Scenarios**<a name="s9f95e14048064f63a1d9be0c9f685f07"></a>

Read replicas are used to enhance the read capabilities of primary DB instances and reduce the load on primary DB instances.

After DB instances are created, you can  create read replicas  for them.

>![](/images/icon-note.gif) **NOTE:**   
>A maximum of five read replicas can be created for a primary DB instance.  

## Procedure<a name="s738501c07aa4426eaeea764d9297251d"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  **Create Read Replica**  in the  **Operation**  column.

    Alternatively, click the target DB instance. In the DB instance topology, click  ![](figures/read.png)  under the primary DB instance to create read replicas.

5.  On the displayed page, configure information about the read replica and click  **Create Now**.

    **Table  1**  Basic information

    <a name="table374110104381"></a>
    <table><thead align="left"><tr id="rb89ee2680ad341c88d3dae6ce26e0bbb"><th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.3.1.1"><p id="a8e1ea4dccadf43b3a23421bc1ce2268a"><a name="a8e1ea4dccadf43b3a23421bc1ce2268a"></a><a name="a8e1ea4dccadf43b3a23421bc1ce2268a"></a><strong id="b4163112715511"><a name="b4163112715511"></a><a name="b4163112715511"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="82.33%" id="mcps1.2.3.1.2"><p id="a9fa63d1ff45b4610bf73a3eb62e4ba87"><a name="a9fa63d1ff45b4610bf73a3eb62e4ba87"></a><a name="a9fa63d1ff45b4610bf73a3eb62e4ba87"></a><strong id="b18758144310511"><a name="b18758144310511"></a><a name="b18758144310511"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="re985d3e83e2940f0a844662d774985b3"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="a7f6c93c6dc024e75a7ad763abeeed623"><a name="a7f6c93c6dc024e75a7ad763abeeed623"></a><a name="a7f6c93c6dc024e75a7ad763abeeed623"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="adf7fc0c3b6b34f4a9a4c808ffbc9bc96"><a name="adf7fc0c3b6b34f4a9a4c808ffbc9bc96"></a><a name="adf7fc0c3b6b34f4a9a4c808ffbc9bc96"></a>By default, read replicas are in the same region as the primary DB instance.</p>
    </td>
    </tr>
    <tr id="r09dbcd8e7d9145e290afbbf334c988bd"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="ac7855025749c41a6af6984e088f66e3b"><a name="ac7855025749c41a6af6984e088f66e3b"></a><a name="ac7855025749c41a6af6984e088f66e3b"></a>DB Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="aa4aaba6d2e084151aee6f1772bc7b2bd"><a name="aa4aaba6d2e084151aee6f1772bc7b2bd"></a><a name="aa4aaba6d2e084151aee6f1772bc7b2bd"></a>Must start with a letter and consist of 4 to 64 characters. It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="r9d09bfd516b14798a4888b86d7fed5fa"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="a15abca176028499babd933b839090f5e"><a name="a15abca176028499babd933b839090f5e"></a><a name="a15abca176028499babd933b839090f5e"></a>DB Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="a696cfb29bbb1496797619e0489df6aeb"><a name="a696cfb29bbb1496797619e0489df6aeb"></a><a name="a696cfb29bbb1496797619e0489df6aeb"></a>Same as the DB engine version of the primary DB instance by default and cannot be changed.</p>
    </td>
    </tr>
    <tr id="r216f7256942a42eaa3bd6c7bcbabe851"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="aa85ac38952924c36baa8e440d145831f"><a name="aa85ac38952924c36baa8e440d145831f"></a><a name="aa85ac38952924c36baa8e440d145831f"></a>DB Engine Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0104704897_p611818314226"><a name="en-us_topic_0104704897_p611818314226"></a><a name="en-us_topic_0104704897_p611818314226"></a>Same as the DB engine version of the primary DB instance by default and cannot be changed.</p>
    </td>
    </tr>
    <tr id="r36a71173a2eb4727927e38f116c29a9c"><td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.3.1.1 "><p id="a9633693a57b745308b99fd0f21c81c5e"><a name="a9633693a57b745308b99fd0f21c81c5e"></a><a name="a9633693a57b745308b99fd0f21c81c5e"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="82.33%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0104704897_p114913522132"><a name="en-us_topic_0104704897_p114913522132"></a><a name="en-us_topic_0104704897_p114913522132"></a>RDS allows you to deploy primary DB instances and read replicas in a single AZ or across AZs. You can determine whether the read replica AZ is the same as the primary AZ.<a name="u726b397bae614cd382ea471215ca9a96"></a><a name="u726b397bae614cd382ea471215ca9a96"></a><ul id="u726b397bae614cd382ea471215ca9a96"><li>If they are the same, the read replica and primary DB instance are deployed in the same AZ.</li><li>If they are different, the read replica and primary DB instance are deployed in different AZs to ensure data reliability.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Instance specifications

    <a name="table1347794173811"></a>
    <table><thead align="left"><tr id="reea1444f54b7482fa3815dbe9dbe634f"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="aa1e09dcf216a440b94469aaae6b72510"><a name="aa1e09dcf216a440b94469aaae6b72510"></a><a name="aa1e09dcf216a440b94469aaae6b72510"></a><strong id="b946392919527"><a name="b946392919527"></a><a name="b946392919527"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ab0911e657d3b4abcb1fd222aa87e3624"><a name="ab0911e657d3b4abcb1fd222aa87e3624"></a><a name="ab0911e657d3b4abcb1fd222aa87e3624"></a><strong id="b849873010529"><a name="b849873010529"></a><a name="b849873010529"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r00fdd9f8134240838d06a3321a77c2ce"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a5859384263c14ec894f66ca225c4b2b1"><a name="a5859384263c14ec894f66ca225c4b2b1"></a><a name="a5859384263c14ec894f66ca225c4b2b1"></a>Instance Class</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a6dd1e8437a244c7993a0392e5905ae97"><a name="a6dd1e8437a244c7993a0392e5905ae97"></a><a name="a6dd1e8437a244c7993a0392e5905ae97"></a>Refers to the CPU and memory of a DB instance. Different instance classes refer to different numbers of database connections and maximum IOPS.</p>
    <p id="en-us_topic_0104704897_p781114612508"><a name="en-us_topic_0104704897_p781114612508"></a><a name="en-us_topic_0104704897_p781114612508"></a></p>
    <p id="en-us_topic_0104704897_p5429821515"><a name="en-us_topic_0104704897_p5429821515"></a><a name="en-us_topic_0104704897_p5429821515"></a></p>
    <p id="en-us_topic_0104704897_p12042810516"><a name="en-us_topic_0104704897_p12042810516"></a><a name="en-us_topic_0104704897_p12042810516"></a>For details about instance classes, see section <a href="db-instance-classes.md">DB Instance Classes</a>.</p>
    <p id="en-us_topic_0104704897_p4689621196"><a name="en-us_topic_0104704897_p4689621196"></a><a name="en-us_topic_0104704897_p4689621196"></a></p>
    <p id="en-us_topic_0104704897_p860165515523"><a name="en-us_topic_0104704897_p860165515523"></a><a name="en-us_topic_0104704897_p860165515523"></a></p>
    <p id="en-us_topic_0104704897_p4610514532"><a name="en-us_topic_0104704897_p4610514532"></a><a name="en-us_topic_0104704897_p4610514532"></a></p>
    <p id="en-us_topic_0104704897_p19542517536"><a name="en-us_topic_0104704897_p19542517536"></a><a name="en-us_topic_0104704897_p19542517536"></a>After a DB instance is created, you can change its CPU and memory. For details, see section <a href="changing-a-db-instance-class-29.md">Changing a DB Instance Class</a>.</p>
    <p id="en-us_topic_0104704897_p38285458348"><a name="en-us_topic_0104704897_p38285458348"></a><a name="en-us_topic_0104704897_p38285458348"></a></p>
    </td>
    </tr>
    <tr id="rd48db41ccd0a42aaace73aa321ded210"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a7665201e013c448889b5c690a28838ed"><a name="a7665201e013c448889b5c690a28838ed"></a><a name="a7665201e013c448889b5c690a28838ed"></a>Storage Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a2fa36ff2f41d443d95434fc47d037a38"><a name="a2fa36ff2f41d443d95434fc47d037a38"></a><a name="a2fa36ff2f41d443d95434fc47d037a38"></a>Determines the DB instance read/write speed. The higher the maximum throughput is, the higher the DB instance read/write speed can be.</p>
    <a name="ul1995202413543"></a><a name="ul1995202413543"></a><ul id="ul1995202413543"><li><strong id="b149033118492"><a name="b149033118492"></a><a name="b149033118492"></a>Common I/O</strong>: uses the SATA disk type, with a maximum throughput of 90 MB/s.</li><li><strong id="b182450182111"><a name="b182450182111"></a><a name="b182450182111"></a>Ultra-high I/O</strong>: uses the SSD disk type that supports a maximum throughput of 350 MB/s.</li></ul>
    </td>
    </tr>
    <tr id="rc2c662af50844f29956928f7f7936b37"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a36c5159435ea4e93931bb4045e68b67e"><a name="a36c5159435ea4e93931bb4045e68b67e"></a><a name="a36c5159435ea4e93931bb4045e68b67e"></a>Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0104704897_p253463643920"><a name="en-us_topic_0104704897_p253463643920"></a><a name="en-us_topic_0104704897_p253463643920"></a>Contains the system overhead required for inode, reserved block, and database operation.</p>
    <p id="p9481145015"><a name="p9481145015"></a><a name="p9481145015"></a>By default, storage space of a read replica is the same as that of the primary DB instance.</p>
    </td>
    </tr>
    <tr id="row15865034273"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0104704897_p595744141914"><a name="en-us_topic_0104704897_p595744141914"></a><a name="en-us_topic_0104704897_p595744141914"></a>Disk Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="u2597363a1b7143ff970ab2e4246958f6"></a><a name="u2597363a1b7143ff970ab2e4246958f6"></a><ul id="u2597363a1b7143ff970ab2e4246958f6"><li><strong>Disabled</strong>: indicates the encryption function is disabled.</li><li><strong id="b1214594215126"><a name="b1214594215126"></a><a name="b1214594215126"></a>Enabled</strong>: indicates the encryption function is enabled, improving data security but affecting system performance.<p id="a17a16a1c2ad94e0792279ac47f7fae8e"><a name="a17a16a1c2ad94e0792279ac47f7fae8e"></a><a name="a17a16a1c2ad94e0792279ac47f7fae8e"></a><strong>Key Name</strong>: indicates the tenant key. You can create or select a key.</p>
    <div class="note" id="n84f031fa78db48518e67cda11ff5ea41"><a name="n84f031fa78db48518e67cda11ff5ea41"></a><a name="n84f031fa78db48518e67cda11ff5ea41"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="uc8be307a454d46a08874a85a21814a71"></a><a name="uc8be307a454d46a08874a85a21814a71"></a><ul id="uc8be307a454d46a08874a85a21814a71"><li>Once the disk encryption function is enabled, you cannot disable it or change the key after a DB instance is created. The backup data stored in OBS is not encrypted.</li><li>After an RDS DB instance is created, do not disable or delete the key that is being used. Otherwise, RDS will be unavailable and data cannot be restored.</li><li>For details about how to create a key, see the "Creating a CMK" section in the <em id="i10228957133310"><a name="i10228957133310"></a><a name="i10228957133310"></a>Data Encryption Workshop User Guide</em>.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Network

    <a name="table37304444569"></a>
    <table><thead align="left"><tr id="row1273164417563"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.3.1.1"><p id="p0966175011569"><a name="p0966175011569"></a><a name="p0966175011569"></a><strong id="b273495113"><a name="b273495113"></a><a name="b273495113"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="81.19%" id="mcps1.2.3.1.2"><p id="p2731144465614"><a name="p2731144465614"></a><a name="p2731144465614"></a><strong id="b1066805454"><a name="b1066805454"></a><a name="b1066805454"></a>Description</strong></p>
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

7.  After a read replica has been created, you can view and manage it on the  **Instance Management**  page by clicking  ![](figures/expand.PNG)  on the left of the DB instance to which it belongs.

    Alternatively, click the target DB instance. In the DB instance topology, click the target read replica. You can view and manage it in the displayed pane.


