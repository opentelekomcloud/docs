# Restoring Data to a New DB Instance<a name="rds_09_0008"></a>

## Function<a name="section117711820496"></a>

This API is used to restore data to a new DB instance \(v3\).

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section191816615431"></a>

-   The DB engine of the original DB instance must be the same as that of the target DB instance. For example, if the original DB instance is running MySQL, the target DB instance must also run MySQL.
-   All DB engine versions of the original and new DB instances must be consistent.
-   The total volume size of the new DB instance must be greater than or equal to that of the original DB instance.
-   Currently, Microsoft SQL Server does not support restoring data to a new DB instance.

## URI<a name="section12081471012"></a>

-   URI format

    POST https://\{_Endpoint_\}/v3/\{project\_id\}/instances

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p1133118381087"><a name="p1133118381087"></a><a name="p1133118381087"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section420839121019"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p23411412333"><a name="p23411412333"></a><a name="p23411412333"></a>Specifies the DB instance name.</p>
    <p id="p463314503337"><a name="p463314503337"></a><a name="p463314503337"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row153106284519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1449010592056"><a name="p1449010592056"></a><a name="p1449010592056"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1249795916511"><a name="p1249795916511"></a><a name="p1249795916511"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p310803110574"><a name="p310803110574"></a><a name="p310803110574"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1851455914518"><a name="p1851455914518"></a><a name="p1851455914518"></a>Specifies the HA configuration parameters, which are used when creating primary/standby DB instances.</p>
    <p id="p5887141310476"><a name="p5887141310476"></a><a name="p5887141310476"></a>For details, see <a href="#table13260175614296">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row933354567"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5334544617"><a name="p5334544617"></a><a name="p5334544617"></a>configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p93315541168"><a name="p93315541168"></a><a name="p93315541168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p173313549619"><a name="p173313549619"></a><a name="p173313549619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p53312541067"><a name="p53312541067"></a><a name="p53312541067"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row59881004135"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3913191019136"><a name="p3913191019136"></a><a name="p3913191019136"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p69131102134"><a name="p69131102134"></a><a name="p69131102134"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p6913210191313"><a name="p6913210191313"></a><a name="p6913210191313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19914101012135"><a name="p19914101012135"></a><a name="p19914101012135"></a>Specifies the database port information.</p>
    <a name="ul164621729141114"></a><a name="ul164621729141114"></a><ul id="ul164621729141114"><li>The MySQL database port ranges from 1024 to 65535 (excluding 12017 and 33071, which are occupied by the RDS system and cannot be used).</li><li>The PostgreSQL database port ranges from 2100 to 9500.</li><li>The Microsoft SQL Server database port is 1433 or ranges from 2100 to 9500 (excluding 5355 and 5985). </li></ul>
    <p id="p1172615390340"><a name="p1172615390340"></a><a name="p1172615390340"></a>If this parameter is not set, the default value is as follows:</p>
    <a name="ul13855195423417"></a><a name="ul13855195423417"></a><ul id="ul13855195423417"><li>For MySQL, the default value is <strong id="rds_01_0002_b1829614472613"><a name="rds_01_0002_b1829614472613"></a><a name="rds_01_0002_b1829614472613"></a>3306</strong>.</li><li>For PostgreSQL, the default value is <strong id="rds_01_0002_b13817121574"><a name="rds_01_0002_b13817121574"></a><a name="rds_01_0002_b13817121574"></a>5432</strong>.</li><li>For Microsoft SQL Server, the default value is <strong id="rds_01_0002_b1633152143014"><a name="rds_01_0002_b1633152143014"></a><a name="rds_01_0002_b1633152143014"></a>1433</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row5642202221319"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p75222324139"><a name="p75222324139"></a><a name="p75222324139"></a>password</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6522163210139"><a name="p6522163210139"></a><a name="p6522163210139"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1352217328132"><a name="p1352217328132"></a><a name="p1352217328132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p252314328139"><a name="p252314328139"></a><a name="p252314328139"></a>Specifies the database password.</p>
    <p id="p26487069"><a name="p26487069"></a><a name="p26487069"></a>Valid value:</p>
    <p id="p12429628144458"><a name="p12429628144458"></a><a name="p12429628144458"></a>The value cannot be empty and should contain 8 to 32 characters, including uppercase and lowercase letters, digits, and the following special characters: ~!@#%^*-_=+?</p>
    <p id="p1441752823615"><a name="p1441752823615"></a><a name="p1441752823615"></a>You are advised to enter a strong password to improve security, preventing security risks such as brute force cracking.</p>
    </td>
    </tr>
    <tr id="row1531134871717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p169876381815"><a name="p169876381815"></a><a name="p169876381815"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9987103141817"><a name="p9987103141817"></a><a name="p9987103141817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p13697181131913"><a name="p13697181131913"></a><a name="p13697181131913"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14803115432218"><a name="p14803115432218"></a><a name="p14803115432218"></a>Specifies the advanced backup policy.</p>
    <p id="p105311421474"><a name="p105311421474"></a><a name="p105311421474"></a>For details, see <a href="#table0863181193416">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row1842179141917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p76971418121913"><a name="p76971418121913"></a><a name="p76971418121913"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p206971718181915"><a name="p206971718181915"></a><a name="p206971718181915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p14699618121914"><a name="p14699618121914"></a><a name="p14699618121914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1669991812194"><a name="p1669991812194"></a><a name="p1669991812194"></a>Specifies the key ID for disk encryption. The default value is empty.</p>
    </td>
    </tr>
    <tr id="row42565233"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>flavor_ref</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p30516772"><a name="p30516772"></a><a name="p30516772"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p55939488"><a name="p55939488"></a><a name="p55939488"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11524913121019"><a name="p11524913121019"></a><a name="p11524913121019"></a>Specifies the specification code. The value cannot be empty.</p>
    <p id="p1778193619122"><a name="p1778193619122"></a><a name="p1778193619122"></a>For details, see <span class="parmname" id="parmname20548731984"><a name="parmname20548731984"></a><a name="parmname20548731984"></a><b>spec_code</b></span> in section <a href="querying-database-specifications.md">Querying Database Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row49370368"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p39576862"><a name="p39576862"></a><a name="p39576862"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p51609257"><a name="p51609257"></a><a name="p51609257"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p61513540"><a name="p61513540"></a><a name="p61513540"></a>Specifies the volume information.</p>
    <p id="p48758754814"><a name="p48758754814"></a><a name="p48758754814"></a>For details, see <a href="#table10656503">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row9307971"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p533144"><a name="p533144"></a><a name="p533144"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8297278"><a name="p8297278"></a><a name="p8297278"></a>Specifies the AZ ID. If the DB instance is not a single instance, you need to specify an AZ for each node of the instance and separate the AZs with commas (,). For details, see the example.</p>
    <p id="p49296060141410"><a name="p49296060141410"></a><a name="p49296060141410"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row51313205"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p52874399"><a name="p52874399"></a><a name="p52874399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7759131604512"><a name="p7759131604512"></a><a name="p7759131604512"></a>Specifies the VPC ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul475921618452"></a><a name="ul475921618452"></a><ul id="ul475921618452"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: See the "Querying VPCs" section in the <em id="rds_01_0002_i842352697165629"><a name="rds_01_0002_i842352697165629"></a><a name="rds_01_0002_i842352697165629"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row15861880"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9743886"><a name="p9743886"></a><a name="p9743886"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42003681"><a name="p42003681"></a><a name="p42003681"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p27596160451"><a name="p27596160451"></a><a name="p27596160451"></a>Specifies the network ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul375971611456"></a><a name="ul375971611456"></a><ul id="ul375971611456"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="rds_01_0002_b4101174416409"><a name="rds_01_0002_b4101174416409"></a><a name="rds_01_0002_b4101174416409"></a>Subnets</strong> page. You can view the network ID on the displayed page.</li><li>Method 2: See the "Querying Subnets" section in the <em id="rds_01_0002_i102188587418"><a name="rds_01_0002_i102188587418"></a><a name="rds_01_0002_i102188587418"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row66008059"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42208903"><a name="p42208903"></a><a name="p42208903"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p157601616114517"><a name="p157601616114517"></a><a name="p157601616114517"></a>Specifies the security group which the RDS DB instance belongs to. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul37601616154512"></a><a name="ul37601616154512"></a><ul id="ul37601616154512"><li>Method 1: Log in to VPC console. Choose <strong id="rds_01_0002_b1913676122"><a name="rds_01_0002_b1913676122"></a><a name="rds_01_0002_b1913676122"></a>Access Control</strong> &gt; <strong id="rds_01_0002_b789502111219"><a name="rds_01_0002_b789502111219"></a><a name="rds_01_0002_b789502111219"></a>Security Groups</strong> in the navigation pane on the left. On the displayed page, click the target security group. You can view the security group ID on the displayed page.</li><li>Method 2: See the "Querying Security Groups" section in the <em id="rds_01_0002_i2369584559"><a name="rds_01_0002_i2369584559"></a><a name="rds_01_0002_i2369584559"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row19723183722710"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p67242370273"><a name="p67242370273"></a><a name="p67242370273"></a>restore_point</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p157241437112719"><a name="p157241437112719"></a><a name="p157241437112719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p2957235135915"><a name="p2957235135915"></a><a name="p2957235135915"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p9724153712271"><a name="p9724153712271"></a><a name="p9724153712271"></a>Specifies the restoration information.</p>
    <p id="p272642434813"><a name="p272642434813"></a><a name="p272642434813"></a>For details, see <a href="#table15343138128">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  ha field data structure description

    <a name="table13260175614296"></a>
    <table><thead align="left"><tr id="row430415632917"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p83131256172915"><a name="p83131256172915"></a><a name="p83131256172915"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1532014560298"><a name="p1532014560298"></a><a name="p1532014560298"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p83297567293"><a name="p83297567293"></a><a name="p83297567293"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p734219563293"><a name="p734219563293"></a><a name="p734219563293"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row173521956122913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p123571256172914"><a name="p123571256172914"></a><a name="p123571256172914"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p336525662915"><a name="p336525662915"></a><a name="p336525662915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p15376756162917"><a name="p15376756162917"></a><a name="p15376756162917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p16181542163018"><a name="p16181542163018"></a><a name="p16181542163018"></a>Specifies the DB instance type. The value is <strong id="b7441203013017"><a name="b7441203013017"></a><a name="b7441203013017"></a>Ha</strong> (primary/standby DB instances) and is case-insensitive.</p>
    </td>
    </tr>
    <tr id="row840515672916"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p92151105323"><a name="p92151105323"></a><a name="p92151105323"></a>replication_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p62151809326"><a name="p62151809326"></a><a name="p62151809326"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1721540173210"><a name="p1721540173210"></a><a name="p1721540173210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p15585263415"><a name="p15585263415"></a><a name="p15585263415"></a>Specifies the replication mode for the standby DB instance.</p>
    <p id="p121155213343"><a name="p121155213343"></a><a name="p121155213343"></a>The value cannot be empty.</p>
    <a name="ul120105263413"></a><a name="ul120105263413"></a><ul id="ul120105263413"><li>For MySQL, the value is <strong>async</strong> or <strong>semisync</strong>.</li><li>For PostgreSQL, the value is <strong>async</strong> or <strong>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong>sync</strong>.</li></ul>
    <div class="note" id="note17075210348"><a name="note17075210348"></a><a name="note17075210348"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul9881252203415"></a><a name="ul9881252203415"></a><ul id="ul9881252203415"><li><strong>async</strong> indicates the asynchronous replication mode.</li><li><strong>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  backup\_strategy field data structure description

    <a name="table0863181193416"></a>
    <table><thead align="left"><tr id="row49079123417"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p491419118346"><a name="p491419118346"></a><a name="p491419118346"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1921131193411"><a name="p1921131193411"></a><a name="p1921131193411"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1293171203411"><a name="p1293171203411"></a><a name="p1293171203411"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p17939718349"><a name="p17939718349"></a><a name="p17939718349"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1094610120345"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1295681153413"><a name="p1295681153413"></a><a name="p1295681153413"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p119619110347"><a name="p119619110347"></a><a name="p119619110347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p5970201183417"><a name="p5970201183417"></a><a name="p5970201183417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p20642173819393"><a name="p20642173819393"></a><a name="p20642173819393"></a>Specifies the backup time window. Automated backups will be triggered during the backup time window.</p>
    <p id="p144363282818"><a name="p144363282818"></a><a name="p144363282818"></a>The value cannot be empty. It must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
    <a name="ul73551635192814"></a><a name="ul73551635192814"></a><ul id="ul73551635192814"><li>The <strong id="b8466258394"><a name="b8466258394"></a><a name="b8466258394"></a>HH</strong> value must be 1 greater than the <strong id="b174669581595"><a name="b174669581595"></a><a name="b174669581595"></a>hh</strong> value.</li><li>The values of <strong id="b13214152101015"><a name="b13214152101015"></a><a name="b13214152101015"></a>mm</strong> and <strong id="b321610214106"><a name="b321610214106"></a><a name="b321610214106"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b1421618251018"><a name="b1421618251018"></a><a name="b1421618251018"></a>00</strong>, <strong id="b1521612261016"><a name="b1521612261016"></a><a name="b1521612261016"></a>15</strong>, <strong id="b72161127109"><a name="b72161127109"></a><a name="b72161127109"></a>30</strong>, or <strong id="b15217102201017"><a name="b15217102201017"></a><a name="b15217102201017"></a>45</strong>.</li></ul>
    <p id="p59342194324"><a name="p59342194324"></a><a name="p59342194324"></a>Example value:</p>
    <a name="ul1210322243217"></a><a name="ul1210322243217"></a><ul id="ul1210322243217"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
    </td>
    </tr>
    <tr id="row1699610173414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p677216342"><a name="p677216342"></a><a name="p677216342"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2171624347"><a name="p2171624347"></a><a name="p2171624347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p125424341"><a name="p125424341"></a><a name="p125424341"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13613273417"><a name="p13613273417"></a><a name="p13613273417"></a>Specifies the retention days for specific backup files.</p>
    <p id="p7391722345"><a name="p7391722345"></a><a name="p7391722345"></a>The value range is from 0 to 732. If this parameter is not specified or set to <strong>0</strong>, the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  volume field data structure description

    <a name="table10656503"></a>
    <table><thead align="left"><tr id="row5847780"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p3908185"><a name="p3908185"></a><a name="p3908185"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p48127554"><a name="p48127554"></a><a name="p48127554"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p6017800"><a name="p6017800"></a><a name="p6017800"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p17679762"><a name="p17679762"></a><a name="p17679762"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22774600"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p32803348"><a name="p32803348"></a><a name="p32803348"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p39825499"><a name="p39825499"></a><a name="p39825499"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4640007"><a name="p4640007"></a><a name="p4640007"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40296320"><a name="p40296320"></a><a name="p40296320"></a>Specifies the volume type.</p>
    <p id="p27122565"><a name="p27122565"></a><a name="p27122565"></a>Its value can be any of the following and is case-sensitive:</p>
    <a name="ul06211247141917"></a><a name="ul06211247141917"></a><ul id="ul06211247141917"><li><strong id="b1783193115308"><a name="b1783193115308"></a><a name="b1783193115308"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b1529815399301"><a name="b1529815399301"></a><a name="b1529815399301"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
    </td>
    </tr>
    <tr id="row42343927"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7306053"><a name="p7306053"></a><a name="p7306053"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p54919424"><a name="p54919424"></a><a name="p54919424"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p19288335"><a name="p19288335"></a><a name="p19288335"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p18851291"><a name="p18851291"></a><a name="p18851291"></a>Specifies the volume size.</p>
    <p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>Its value range is from 40 GB to 4000 GB. The value must be a multiple of 10.</p>
    <p id="p1169318625516"><a name="p1169318625516"></a><a name="p1169318625516"></a></p>
    <div class="notice" id="note18772920133413"><a name="note18772920133413"></a><a name="note18772920133413"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p3772920183420"><a name="p3772920183420"></a><a name="p3772920183420"></a>The volume size of the new DB instance must be greater than or equal to that of the original DB instance.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  restore\_point field data structure description

    <a name="table15343138128"></a>
    <table><thead align="left"><tr id="row53891320125"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p103841361219"><a name="p103841361219"></a><a name="p103841361219"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p14391313121214"><a name="p14391313121214"></a><a name="p14391313121214"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p44051314123"><a name="p44051314123"></a><a name="p44051314123"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p2414137127"><a name="p2414137127"></a><a name="p2414137127"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2421813191218"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13264155191218"><a name="p13264155191218"></a><a name="p13264155191218"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2265855161214"><a name="p2265855161214"></a><a name="p2265855161214"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1626555516125"><a name="p1626555516125"></a><a name="p1626555516125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p02661255101216"><a name="p02661255101216"></a><a name="p02661255101216"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row1853025314318"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1953065318318"><a name="p1953065318318"></a><a name="p1953065318318"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65301153103119"><a name="p65301153103119"></a><a name="p65301153103119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p753012532312"><a name="p753012532312"></a><a name="p753012532312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1530205312316"><a name="p1530205312316"></a><a name="p1530205312316"></a>Specifies the restoration mode. Enumerated values include:</p>
    <a name="ul1286842916197"></a><a name="ul1286842916197"></a><ul id="ul1286842916197"><li><span class="parmvalue" id="parmvalue16942192181913"><a name="parmvalue16942192181913"></a><a name="parmvalue16942192181913"></a><b>backup</b></span>: indicates restoration from backup files. In this mode, <span class="parmname" id="parmname10465636152214"><a name="parmname10465636152214"></a><a name="parmname10465636152214"></a><b>backup_id</b></span> is mandatory when <span class="parmname" id="parmname9885117104719"><a name="parmname9885117104719"></a><a name="parmname9885117104719"></a><b>type</b></span> is not mandatory.</li><li><span class="parmvalue" id="parmvalue2181121091910"><a name="parmvalue2181121091910"></a><a name="parmvalue2181121091910"></a><b>timestamp</b></span>: indicates point-in-time restoration. In this mode, <span class="parmname" id="parmname11407141622319"><a name="parmname11407141622319"></a><a name="parmname11407141622319"></a><b>restore_time</b></span> is mandatory when <span class="parmname" id="parmname431421818472"><a name="parmname431421818472"></a><a name="parmname431421818472"></a><b>type</b></span> is mandatory.</li></ul>
    </td>
    </tr>
    <tr id="row1246181331215"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5479131120"><a name="p5479131120"></a><a name="p5479131120"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p164741341214"><a name="p164741341214"></a><a name="p164741341214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p148131319124"><a name="p148131319124"></a><a name="p148131319124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p104915134120"><a name="p104915134120"></a><a name="p104915134120"></a>Specifies the ID of the backup used to restore data. This parameter must be specified when the backup file is used for restoration.</p>
    <div class="notice" id="note1584469173613"><a name="note1584469173613"></a><a name="note1584469173613"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p88446916368"><a name="p88446916368"></a><a name="p88446916368"></a>When <span class="parmname" id="parmname88681610123613"><a name="parmname88681610123613"></a><a name="parmname88681610123613"></a><b>type</b></span> is not mandatory, <span class="parmname" id="parmname188683106368"><a name="parmname188683106368"></a><a name="parmname188683106368"></a><b>backup_id</b></span> is mandatory.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row13759127103219"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1876020715326"><a name="p1876020715326"></a><a name="p1876020715326"></a>restore_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p167604743213"><a name="p167604743213"></a><a name="p167604743213"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1976018715320"><a name="p1976018715320"></a><a name="p1976018715320"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p147606715321"><a name="p147606715321"></a><a name="p147606715321"></a>Specifies the time point of data restoration in the UNIX timestamp. The unit is millisecond and the time zone is UTC.</p>
    <div class="notice" id="note3321191315376"><a name="note3321191315376"></a><a name="note3321191315376"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p3346913143715"><a name="p3346913143715"></a><a name="p3346913143715"></a>When <strong id="b84235270610114"><a name="b84235270610114"></a><a name="b84235270610114"></a>type</strong> is mandatory, <span class="parmname" id="parmname14103815173711"><a name="parmname14103815173711"></a><a name="parmname14103815173711"></a><b>restore_time</b></span> is mandatory.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    Use backup files for restoration:

    ```
    {
    	"name": "targetInst",
    	"availability_zone": "eu-de-01,eu-de-02",
    	"ha": {
    		"mode": "ha",
    		"replication_mode": "async"
    	},
    	"flavor_ref": "rds.mysql.s1.large",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 40
    	},
    	"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    	"vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    	"subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
    	"security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5",
    	"backup_strategy": {
    		"keep_days": 2,
    		"start_time": "19:00-20:00"
    	},
    	"password": "Demo@12345678",
    	"configuration_id": "52e86e87445847a79bf807ceda213165pr01",
    	"restore_point": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01",
    		"type": "backup",
    		"backup_id": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe"
    	}
    }
    ```

    Use PITR for restoration:

    ```
    {
    	"name": "targetInst",
    	"availability_zone": "eu-de-01,eu-de-02",
    	"ha": {
    		"mode": "ha",
    		"replication_mode": "async"
    	},
    	"flavor_ref": "rds.mysql.s1.large",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 40
    	},
    	"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    	"vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    	"subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
    	"security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5",
    	"backup_strategy": {
    		"keep_days": 2,
    		"start_time": "19:00-20:00"
    	},
    	"password": "Demo@12345678",
    	"configuration_id": "52e86e87445847a79bf807ceda213165pr01",
    	"restore_point": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01",
    		"type": "timestamp",
    		"restore_time": 1532001446987
    	}
    }
    ```


## Response<a name="section1229512143106"></a>

-   Normal response

    **Table  7**  Parameter description

    <a name="table17474517"></a>
    <table><thead align="left"><tr id="row16146366"><th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.1"><p id="p32787233"><a name="p32787233"></a><a name="p32787233"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.29%" id="mcps1.2.4.1.2"><p id="p38520254"><a name="p38520254"></a><a name="p38520254"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p33132859"><a name="p33132859"></a><a name="p33132859"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66515904"><td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.1 "><p id="p19079158"><a name="p19079158"></a><a name="p19079158"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.29%" headers="mcps1.2.4.1.2 "><p id="p1070295810711"><a name="p1070295810711"></a><a name="p1070295810711"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p48735027"><a name="p48735027"></a><a name="p48735027"></a>Indicates the DB instance information.</p>
    <p id="p8266112116531"><a name="p8266112116531"></a><a name="p8266112116531"></a>For details, see <a href="#table175305610274">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row1625804435012"><td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.1 "><p id="p1165525810503"><a name="p1165525810503"></a><a name="p1165525810503"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.29%" headers="mcps1.2.4.1.2 "><p id="p116551958135013"><a name="p116551958135013"></a><a name="p116551958135013"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p16655115865012"><a name="p16655115865012"></a><a name="p16655115865012"></a>Indicates the ID of the DB instance creation task.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  instance description

    <a name="table175305610274"></a>
    <table><thead align="left"><tr id="row4782256142718"><th class="cellrowborder" valign="top" width="33.36333633363336%" id="mcps1.2.4.1.1"><p id="p11791105616272"><a name="p11791105616272"></a><a name="p11791105616272"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.3033303330333%" id="mcps1.2.4.1.2"><p id="p1280910568278"><a name="p1280910568278"></a><a name="p1280910568278"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p081620561276"><a name="p081620561276"></a><a name="p081620561276"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row83685201297"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p109879468293"><a name="p109879468293"></a><a name="p109879468293"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p14953885305"><a name="p14953885305"></a><a name="p14953885305"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1798714612914"><a name="p1798714612914"></a><a name="p1798714612914"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row88231562277"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p383295682710"><a name="p383295682710"></a><a name="p383295682710"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p48498568273"><a name="p48498568273"></a><a name="p48498568273"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13301192910457"><a name="p13301192910457"></a><a name="p13301192910457"></a>Indicates the DB instance name.</p>
    <p id="p143022294458"><a name="p143022294458"></a><a name="p143022294458"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p168621956132710"><a name="p168621956132710"></a><a name="p168621956132710"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1326042683017"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p986116344302"><a name="p986116344302"></a><a name="p986116344302"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p4861203433016"><a name="p4861203433016"></a><a name="p4861203433016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p78617346309"><a name="p78617346309"></a><a name="p78617346309"></a>Indicates the DB instance status. For example, <strong>BUILD</strong> indicates that the DB instance is being created.</p>
    </td>
    </tr>
    <tr id="row1587195662712"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p188761056132717"><a name="p188761056132717"></a><a name="p188761056132717"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p2947134612014"><a name="p2947134612014"></a><a name="p2947134612014"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13907115612720"><a name="p13907115612720"></a><a name="p13907115612720"></a>Indicates the database information.</p>
    <p id="p189026423530"><a name="p189026423530"></a><a name="p189026423530"></a>For details, see <a href="#table766045720277">Table 9</a>.</p>
    </td>
    </tr>
    <tr id="row2091115617278"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p15919756162716"><a name="p15919756162716"></a><a name="p15919756162716"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p89401656112716"><a name="p89401656112716"></a><a name="p89401656112716"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11951155662714"><a name="p11951155662714"></a><a name="p11951155662714"></a>Indicates the HA configuration parameters. This parameter is returned only when primary/standby DB instances are created.</p>
    <p id="p13864195713531"><a name="p13864195713531"></a><a name="p13864195713531"></a>For details, see <a href="#table15899105722713">Table 10</a>.</p>
    </td>
    </tr>
    <tr id="row2095545611272"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p189601356162713"><a name="p189601356162713"></a><a name="p189601356162713"></a>configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p1697725682718"><a name="p1697725682718"></a><a name="p1697725682718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p198515563273"><a name="p198515563273"></a><a name="p198515563273"></a>Indicates the parameter template ID. This parameter is returned only when a custom parameter template is used during DB instance creation.</p>
    </td>
    </tr>
    <tr id="row1299345602718"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p20311571272"><a name="p20311571272"></a><a name="p20311571272"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p1923157132717"><a name="p1923157132717"></a><a name="p1923157132717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1133155782713"><a name="p1133155782713"></a><a name="p1133155782713"></a>Indicates the database port information.</p>
    <a name="ul10361825192619"></a><a name="ul10361825192619"></a><ul id="ul10361825192619"><li>The MySQL database port ranges from 1024 to 65535 (excluding 12017 and 33071, which are occupied by the RDS system and cannot be used).</li><li>The PostgreSQL database port ranges from 2100 to 9500.</li><li>The Microsoft SQL Server database port is 1433 or ranges from 2100 to 9500 (excluding 5355 and 5985). </li></ul>
    <p id="p167691740173814"><a name="p167691740173814"></a><a name="p167691740173814"></a>If this parameter is not set, the default value is as follows:</p>
    <a name="ul47725409381"></a><a name="ul47725409381"></a><ul id="ul47725409381"><li>For MySQL, the default value is <strong id="rds_01_0002_b1829614472613_1"><a name="rds_01_0002_b1829614472613_1"></a><a name="rds_01_0002_b1829614472613_1"></a>3306</strong>.</li><li>For PostgreSQL, the default value is <strong id="rds_01_0002_b13817121574_1"><a name="rds_01_0002_b13817121574_1"></a><a name="rds_01_0002_b13817121574_1"></a>5432</strong>.</li><li>For Microsoft SQL Server, the default value is <strong id="rds_01_0002_b1633152143014_1"><a name="rds_01_0002_b1633152143014_1"></a><a name="rds_01_0002_b1633152143014_1"></a>1433</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row711835715271"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p8127757182713"><a name="p8127757182713"></a><a name="p8127757182713"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p6649451704"><a name="p6649451704"></a><a name="p6649451704"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3151145732716"><a name="p3151145732716"></a><a name="p3151145732716"></a>Indicates the automated backup policy.</p>
    <p id="p1682622910543"><a name="p1682622910543"></a><a name="p1682622910543"></a>For details, see <a href="#table81249589270">Table 11</a>.</p>
    </td>
    </tr>
    <tr id="row1023011571273"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p62375571274"><a name="p62375571274"></a><a name="p62375571274"></a>flavor_ref</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p12250057172719"><a name="p12250057172719"></a><a name="p12250057172719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2146115915716"><a name="p2146115915716"></a><a name="p2146115915716"></a>Indicates the specification ID.</p>
    <p id="p625713579277"><a name="p625713579277"></a><a name="p625713579277"></a>For details, see <span class="parmname" id="parmname44731513133514"><a name="parmname44731513133514"></a><a name="parmname44731513133514"></a><b>spec_code</b></span> in <a href="querying-database-specifications.md#table66531170">Table 3</a> in section <a href="querying-database-specifications.md">Querying Database Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row727255762713"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p22816576279"><a name="p22816576279"></a><a name="p22816576279"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p0476431518"><a name="p0476431518"></a><a name="p0476431518"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16313145722718"><a name="p16313145722718"></a><a name="p16313145722718"></a>Indicates the volume information.</p>
    <p id="p16941154318542"><a name="p16941154318542"></a><a name="p16941154318542"></a>For details, see <a href="#table5324165817272">Table 12</a>.</p>
    </td>
    </tr>
    <tr id="row1331675710271"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p132655742711"><a name="p132655742711"></a><a name="p132655742711"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p83409571274"><a name="p83409571274"></a><a name="p83409571274"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9347357152716"><a name="p9347357152716"></a><a name="p9347357152716"></a>Indicates the region ID.</p>
    </td>
    </tr>
    <tr id="row04101057112715"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p441975772719"><a name="p441975772719"></a><a name="p441975772719"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p7431165752717"><a name="p7431165752717"></a><a name="p7431165752717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p104381557182713"><a name="p104381557182713"></a><a name="p104381557182713"></a>Indicates the AZ ID.</p>
    </td>
    </tr>
    <tr id="row54992572275"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p14507155732716"><a name="p14507155732716"></a><a name="p14507155732716"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p1522205719275"><a name="p1522205719275"></a><a name="p1522205719275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p155952214473"><a name="p155952214473"></a><a name="p155952214473"></a>Indicates the VPC ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul75962214716"></a><a name="ul75962214716"></a><ul id="ul75962214716"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: See the "Querying VPCs" section in the <em id="rds_01_0002_i842352697165629_1"><a name="rds_01_0002_i842352697165629_1"></a><a name="rds_01_0002_i842352697165629_1"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row4544757192710"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p125528573274"><a name="p125528573274"></a><a name="p125528573274"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p20568457112711"><a name="p20568457112711"></a><a name="p20568457112711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15591722114719"><a name="p15591722114719"></a><a name="p15591722114719"></a>Indicates the network ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul12591422114720"></a><a name="ul12591422114720"></a><ul id="ul12591422114720"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="rds_01_0002_b4101174416409_1"><a name="rds_01_0002_b4101174416409_1"></a><a name="rds_01_0002_b4101174416409_1"></a>Subnets</strong> page. You can view the network ID on the displayed page.</li><li>Method 2: See the "Querying Subnets" section in the <em id="rds_01_0002_i102188587418_1"><a name="rds_01_0002_i102188587418_1"></a><a name="rds_01_0002_i102188587418_1"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row158217577276"><td class="cellrowborder" valign="top" width="33.36333633363336%" headers="mcps1.2.4.1.1 "><p id="p7590145715274"><a name="p7590145715274"></a><a name="p7590145715274"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.3033303330333%" headers="mcps1.2.4.1.2 "><p id="p9603205716276"><a name="p9603205716276"></a><a name="p9603205716276"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1659122254713"><a name="p1659122254713"></a><a name="p1659122254713"></a>Indicates the security group which the RDS DB instance belongs to. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul20592221475"></a><a name="ul20592221475"></a><ul id="ul20592221475"><li>Method 1: Log in to VPC console. Choose <strong id="rds_01_0002_b1913676122_1"><a name="rds_01_0002_b1913676122_1"></a><a name="rds_01_0002_b1913676122_1"></a>Access Control</strong> &gt; <strong id="rds_01_0002_b789502111219_1"><a name="rds_01_0002_b789502111219_1"></a><a name="rds_01_0002_b789502111219_1"></a>Security Groups</strong> in the navigation pane on the left. On the displayed page, click the target security group. You can view the security group ID on the displayed page.</li><li>Method 2: See the "Querying Security Groups" section in the <em id="rds_01_0002_i2369584559_1"><a name="rds_01_0002_i2369584559_1"></a><a name="rds_01_0002_i2369584559_1"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  datastore field data structure description

    <a name="table766045720277"></a>
    <table><thead align="left"><tr id="row468335722716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p156891357202720"><a name="p156891357202720"></a><a name="p156891357202720"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p11698205722716"><a name="p11698205722716"></a><a name="p11698205722716"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.3"><p id="p77089577277"><a name="p77089577277"></a><a name="p77089577277"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.4"><p id="p13715557112714"><a name="p13715557112714"></a><a name="p13715557112714"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9723165742714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17321257162715"><a name="p17321257162715"></a><a name="p17321257162715"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18743145762715"><a name="p18743145762715"></a><a name="p18743145762715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.3 "><p id="p17521757192712"><a name="p17521757192712"></a><a name="p17521757192712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.4 "><p id="p26952636163519"><a name="p26952636163519"></a><a name="p26952636163519"></a>Indicates the DB engine. Its value can be any of the following and is case-insensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row37937570272"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10800165713279"><a name="p10800165713279"></a><a name="p10800165713279"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1980825714277"><a name="p1980825714277"></a><a name="p1980825714277"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.3 "><p id="p0819195719271"><a name="p0819195719271"></a><a name="p0819195719271"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.4 "><p id="p1957105533718"><a name="p1957105533718"></a><a name="p1957105533718"></a>Indicates the database version.</p>
    <p id="p71501555377"><a name="p71501555377"></a><a name="p71501555377"></a>For details about supported database versions, see section <a href="database-version-queries.md">Database Version Queries</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  ha field data structure description

    <a name="table15899105722713"></a>
    <table><thead align="left"><tr id="row1393295712715"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p2941125719278"><a name="p2941125719278"></a><a name="p2941125719278"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p149488577271"><a name="p149488577271"></a><a name="p149488577271"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p119521157162710"><a name="p119521157162710"></a><a name="p119521157162710"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p15960175762715"><a name="p15960175762715"></a><a name="p15960175762715"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1965185792714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p179729572279"><a name="p179729572279"></a><a name="p179729572279"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p79807576271"><a name="p79807576271"></a><a name="p79807576271"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p14990257142711"><a name="p14990257142711"></a><a name="p14990257142711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p4997155711270"><a name="p4997155711270"></a><a name="p4997155711270"></a>Indicates the DB instance type. The value is <strong id="b0886131212189"><a name="b0886131212189"></a><a name="b0886131212189"></a>Ha</strong> (primary/standby DB instances).</p>
    </td>
    </tr>
    <tr id="row72115815278"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p29658162714"><a name="p29658162714"></a><a name="p29658162714"></a>replication_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p917358192717"><a name="p917358192717"></a><a name="p917358192717"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1023185852714"><a name="p1023185852714"></a><a name="p1023185852714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p633115816277"><a name="p633115816277"></a><a name="p633115816277"></a>Indicates the replication mode for the standby DB instance.</p>
    <p id="p1837105812718"><a name="p1837105812718"></a><a name="p1837105812718"></a>The value cannot be empty.</p>
    <a name="ul184125872719"></a><a name="ul184125872719"></a><ul id="ul184125872719"><li>For MySQL, the value is <strong>async</strong> or <strong>semisync</strong>.</li><li>For PostgreSQL, the value is <strong>async</strong> or <strong>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong>sync</strong>.</li></ul>
    <div class="note" id="note575155882717"><a name="note575155882717"></a><a name="note575155882717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul593135817276"></a><a name="ul593135817276"></a><ul id="ul593135817276"><li><strong>async</strong> indicates the asynchronous replication mode.</li><li><strong>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11**  backupStrategy field data structure description

    <a name="table81249589270"></a>
    <table><thead align="left"><tr id="row7155105822719"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p151651758112710"><a name="p151651758112710"></a><a name="p151651758112710"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p517485818270"><a name="p517485818270"></a><a name="p517485818270"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p818335813276"><a name="p818335813276"></a><a name="p818335813276"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14192195817274"><a name="p14192195817274"></a><a name="p14192195817274"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1220112589270"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p321175814278"><a name="p321175814278"></a><a name="p321175814278"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p822475872716"><a name="p822475872716"></a><a name="p822475872716"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p16233758102717"><a name="p16233758102717"></a><a name="p16233758102717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p54551583414"><a name="p54551583414"></a><a name="p54551583414"></a>Indicates the backup time window. Automated backups will be triggered during the backup time window.</p>
    <p id="p145868184115"><a name="p145868184115"></a><a name="p145868184115"></a>The value cannot be empty. It must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
    <a name="ul11460108184114"></a><a name="ul11460108184114"></a><ul id="ul11460108184114"><li>The <strong id="b1937213571120"><a name="b1937213571120"></a><a name="b1937213571120"></a>HH</strong> value must be 1 greater than the <strong id="b337225171113"><a name="b337225171113"></a><a name="b337225171113"></a>hh</strong> value.</li><li>The values of <strong id="b4379156131110"><a name="b4379156131110"></a><a name="b4379156131110"></a>mm</strong> and <strong id="b5380669110"><a name="b5380669110"></a><a name="b5380669110"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b43809621116"><a name="b43809621116"></a><a name="b43809621116"></a>00</strong>, <strong id="b1381176101115"><a name="b1381176101115"></a><a name="b1381176101115"></a>15</strong>, <strong id="b1738206171115"><a name="b1738206171115"></a><a name="b1738206171115"></a>30</strong>, or <strong id="b3384136111119"><a name="b3384136111119"></a><a name="b3384136111119"></a>45</strong>.</li></ul>
    <p id="p13473186416"><a name="p13473186416"></a><a name="p13473186416"></a>Example value:</p>
    <a name="ul84762814413"></a><a name="ul84762814413"></a><ul id="ul84762814413"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
    </td>
    </tr>
    <tr id="row162581058122711"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8266145882712"><a name="p8266145882712"></a><a name="p8266145882712"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p11275115813276"><a name="p11275115813276"></a><a name="p11275115813276"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p9286558152710"><a name="p9286558152710"></a><a name="p9286558152710"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p229865817274"><a name="p229865817274"></a><a name="p229865817274"></a>Indicates the retention days for specific backup files.</p>
    <p id="p1230285817274"><a name="p1230285817274"></a><a name="p1230285817274"></a>The value range is from 0 to 732. If this parameter is not specified or set to <strong>0</strong>, the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  12**  volume field data structure description

    <a name="table5324165817272"></a>
    <table><thead align="left"><tr id="row13366558182710"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p43785583277"><a name="p43785583277"></a><a name="p43785583277"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p2039111586274"><a name="p2039111586274"></a><a name="p2039111586274"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p04002058182712"><a name="p04002058182712"></a><a name="p04002058182712"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1841019583272"><a name="p1841019583272"></a><a name="p1841019583272"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1941717585272"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p542455816278"><a name="p542455816278"></a><a name="p542455816278"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18433175812276"><a name="p18433175812276"></a><a name="p18433175812276"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p8441115892715"><a name="p8441115892715"></a><a name="p8441115892715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p144508584276"><a name="p144508584276"></a><a name="p144508584276"></a>Indicates the volume type.</p>
    <p id="p177941130133020"><a name="p177941130133020"></a><a name="p177941130133020"></a>Its value can be any of the following and is case-sensitive:</p>
    <a name="ul97191143171815"></a><a name="ul97191143171815"></a><ul id="ul97191143171815"><li><strong id="b161034143019"><a name="b161034143019"></a><a name="b161034143019"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b1522274453015"><a name="b1522274453015"></a><a name="b1522274453015"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
    </td>
    </tr>
    <tr id="row164658587274"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1247475842718"><a name="p1247475842718"></a><a name="p1247475842718"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p7482105820276"><a name="p7482105820276"></a><a name="p7482105820276"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1549255811272"><a name="p1549255811272"></a><a name="p1549255811272"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7502958132716"><a name="p7502958132716"></a><a name="p7502958132716"></a>Indicates the volume size.</p>
    <p id="p350618584275"><a name="p350618584275"></a><a name="p350618584275"></a>Its value range is from 40 GB to 4000 GB. The value must be a multiple of 10.</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    ```
    {
    	"instance": {
    		"id": "f5ffdd8b1c98434385eb001904209eacin01",
    		"name": "demoname",
    		"status": "BUILD",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.6.41"
    		},
    		"port": "3306",
    		"volume": {
    			"type": "ULTRAHIGH",
    			"size": "40"
    		},
    		"region": "eu-de",
    		"backup_strategy": {
    			"start_time": "02:00-03:00",
    			"keep_days": "7"
    		},
    		"flavor_ref": "rds.mysql.s1.large",
    		"availability_zone": "eu-de-01",
    		"vpc_id": "19e5d45d-70fd-4a91-87e9-b27e71c9891f",
    		"subnet_id": "bd51fb45-2dcb-4296-8783-8623bfe89bb7",
    		"security_group_id": "23fd0cd4-15dc-4d65-bdb3-8844cc291be0"
    	},
    	"job_id": "bf003379-afea-4aa5-aa83-4543542070bc"
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

