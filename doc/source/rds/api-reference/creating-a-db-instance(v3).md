# Creating a DB Instance<a name="rds_01_0002"></a>

## Function<a name="section4284989"></a>

This API is used to create a single RDS DB instance, primary/standby DB instances, or a read replica.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section38564907"></a>

-   URI format

    POST https://\{_Endpoint_\}/v3/\{project\_id\}/instances

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong id="b13612184114314"><a name="b13612184114314"></a><a name="b13612184114314"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong id="b7976204244310"><a name="b7976204244310"></a><a name="b7976204244310"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong id="b874064312434"><a name="b874064312434"></a><a name="b874064312434"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p131433595402"><a name="p131433595402"></a><a name="p131433595402"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11539844"></a>

**Table  2**  Parameter description \(creating single and primary/standby DB instances\)

<a name="table11236435"></a>
<table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b193256496458"><a name="b193256496458"></a><a name="b193256496458"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.65346534653465%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b299655164516"><a name="b299655164516"></a><a name="b299655164516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b1103195634512"><a name="b1103195634512"></a><a name="b1103195634512"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.683168316831683%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b45319574450"><a name="b45319574450"></a><a name="b45319574450"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p23411412333"><a name="p23411412333"></a><a name="p23411412333"></a>Specifies the DB instance name.</p>
<p id="p51611184"><a name="p51611184"></a><a name="p51611184"></a>DB instances of the same type can have same names under the same tenant.</p>
<p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-sensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row56760689"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p19797588"><a name="p19797588"></a><a name="p19797588"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="a9a9492e05cb648e885d1e747a339d04d"><a name="a9a9492e05cb648e885d1e747a339d04d"></a><a name="a9a9492e05cb648e885d1e747a339d04d"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p58520811"><a name="p58520811"></a><a name="p58520811"></a>Specifies the database information.</p>
<p id="p6426115842318"><a name="p6426115842318"></a><a name="p6426115842318"></a>For details, see <a href="#table64243102">Table 4</a>.</p>
</td>
</tr>
<tr id="row153106284519"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1449010592056"><a name="p1449010592056"></a><a name="p1449010592056"></a>ha</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p1249795916511"><a name="p1249795916511"></a><a name="p1249795916511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p44233713193"><a name="p44233713193"></a><a name="p44233713193"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p1851455914518"><a name="p1851455914518"></a><a name="p1851455914518"></a>Specifies the HA configuration parameters, which are used when creating primary/standby DB instances.</p>
<p id="p116241910162412"><a name="p116241910162412"></a><a name="p116241910162412"></a>For details, see <a href="#table13260175614296">Table 5</a>.</p>
</td>
</tr>
<tr id="row933354567"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p5334544617"><a name="p5334544617"></a><a name="p5334544617"></a>configuration_id</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p93315541168"><a name="p93315541168"></a><a name="p93315541168"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p173313549619"><a name="p173313549619"></a><a name="p173313549619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p53312541067"><a name="p53312541067"></a><a name="p53312541067"></a>Specifies the parameter template ID.</p>
<p id="p91885306228"><a name="p91885306228"></a><a name="p91885306228"></a>For details, see <span class="parmname" id="parmname11831112133013"><a name="parmname11831112133013"></a><a name="parmname11831112133013"></a><b>id</b></span> in <a href="obtaining-a-parameter-template-list.md#table1324110018258">Table 3</a> in section <a href="obtaining-a-parameter-template-list.md">Obtaining a Parameter Template List</a>.</p>
</td>
</tr>
<tr id="row59881004135"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p3913191019136"><a name="p3913191019136"></a><a name="p3913191019136"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p69131102134"><a name="p69131102134"></a><a name="p69131102134"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p6913210191313"><a name="p6913210191313"></a><a name="p6913210191313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p19914101012135"><a name="p19914101012135"></a><a name="p19914101012135"></a>Specifies the database port information.</p>
<a name="ul10438123672912"></a><a name="ul10438123672912"></a><ul id="ul10438123672912"><li>The MySQL database port ranges from 1024 to 65535 (excluding 12017 and 33071, which are occupied by the RDS system and cannot be used).</li><li>The PostgreSQL database port ranges from 2100 to 9500.</li><li>The Microsoft SQL Server database port is 1433 or ranges from 2100 to 9500 (excluding 5355 and 5985). </li></ul>
<p id="p6601319181417"><a name="p6601319181417"></a><a name="p6601319181417"></a>If this parameter is not set, the default value is as follows:</p>
<a name="ul1696512278148"></a><a name="ul1696512278148"></a><ul id="ul1696512278148"><li>For MySQL, the default value is <strong id="b1829614472613"><a name="b1829614472613"></a><a name="b1829614472613"></a>3306</strong>.</li><li>For PostgreSQL, the default value is <strong id="b13817121574"><a name="b13817121574"></a><a name="b13817121574"></a>5432</strong>.</li><li>For Microsoft SQL Server, the default value is <strong id="b1633152143014"><a name="b1633152143014"></a><a name="b1633152143014"></a>1433</strong>.</li></ul>
</td>
</tr>
<tr id="row5642202221319"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p75222324139"><a name="p75222324139"></a><a name="p75222324139"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p6522163210139"><a name="p6522163210139"></a><a name="p6522163210139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p1352217328132"><a name="p1352217328132"></a><a name="p1352217328132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p252314328139"><a name="p252314328139"></a><a name="p252314328139"></a>Specifies the database password.</p>
<p id="p26487069"><a name="p26487069"></a><a name="p26487069"></a>Valid value:</p>
<p id="p482217533347"><a name="p482217533347"></a><a name="p482217533347"></a>The value cannot be empty and should contain 8 to 32 characters, including uppercase and lowercase letters, digits, and the following special characters: ~!@#%^*-_=+?</p>
<p id="p12429628144458"><a name="p12429628144458"></a><a name="p12429628144458"></a>You are advised to enter a strong password to improve security, preventing security risks such as brute force cracking.</p>
</td>
</tr>
<tr id="row1531134871717"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p169876381815"><a name="p169876381815"></a><a name="p169876381815"></a>backup_strategy</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p9987103141817"><a name="p9987103141817"></a><a name="p9987103141817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p13697181131913"><a name="p13697181131913"></a><a name="p13697181131913"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p14803115432218"><a name="p14803115432218"></a><a name="p14803115432218"></a>Specifies the advanced backup policy.</p>
<p id="p16503153252414"><a name="p16503153252414"></a><a name="p16503153252414"></a>For details, see <a href="#table0863181193416">Table 6</a>.</p>
</td>
</tr>
<tr id="row1842179141917"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p76971418121913"><a name="p76971418121913"></a><a name="p76971418121913"></a>disk_encryption_id</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p206971718181915"><a name="p206971718181915"></a><a name="p206971718181915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p14699618121914"><a name="p14699618121914"></a><a name="p14699618121914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p1669991812194"><a name="p1669991812194"></a><a name="p1669991812194"></a>Specifies the key ID for disk encryption. The default value is empty.</p>
</td>
</tr>
<tr id="row42565233"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>flavor_ref</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p30516772"><a name="p30516772"></a><a name="p30516772"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p55939488"><a name="p55939488"></a><a name="p55939488"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p11524913121019"><a name="p11524913121019"></a><a name="p11524913121019"></a>Specifies the specification code. The value cannot be empty.</p>
<p id="p1778193619122"><a name="p1778193619122"></a><a name="p1778193619122"></a>For details, see <span class="parmname" id="parmname6175172718302"><a name="parmname6175172718302"></a><a name="parmname6175172718302"></a><b>spec_code</b></span> in <a href="querying-database-specifications.md#table66531170">Table 3</a> in section <a href="querying-database-specifications.md">Querying Database Specifications</a>.</p>
</td>
</tr>
<tr id="row49370368"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p39576862"><a name="p39576862"></a><a name="p39576862"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p51609257"><a name="p51609257"></a><a name="p51609257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p1811431418199"><a name="p1811431418199"></a><a name="p1811431418199"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p61513540"><a name="p61513540"></a><a name="p61513540"></a>Specifies the volume information.</p>
<p id="p12360550192412"><a name="p12360550192412"></a><a name="p12360550192412"></a>For details, see <a href="#table10656503">Table 7</a>.</p>
</td>
</tr>
<tr id="row16540805"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p64736823"><a name="p64736823"></a><a name="p64736823"></a>region</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p40344576"><a name="p40344576"></a><a name="p40344576"></a>Specifies the region ID.</p>
<p id="p3825082612023"><a name="p3825082612023"></a><a name="p3825082612023"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="row9307971"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p533144"><a name="p533144"></a><a name="p533144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p8297278"><a name="p8297278"></a><a name="p8297278"></a>Specifies the AZ ID. If the DB instance is not a single instance, you need to specify an AZ for each node of the instance and separate the AZs with commas (,). For details, see the example.</p>
<p id="p49296060141410"><a name="p49296060141410"></a><a name="p49296060141410"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="row51313205"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p52874399"><a name="p52874399"></a><a name="p52874399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p1593595153419"><a name="p1593595153419"></a><a name="p1593595153419"></a>Specifies the VPC ID. To obtain this parameter value, use either of the following methods:</p>
<a name="ul250415512347"></a><a name="ul250415512347"></a><ul id="ul250415512347"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: See the "Querying VPCs" section in the <em id="i842352697165629"><a name="i842352697165629"></a><a name="i842352697165629"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row15861880"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p9743886"><a name="p9743886"></a><a name="p9743886"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p42003681"><a name="p42003681"></a><a name="p42003681"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p512371711393"><a name="p512371711393"></a><a name="p512371711393"></a>Specifies the network ID. To obtain this parameter value, use either of the following methods:</p>
<a name="ul9152102763919"></a><a name="ul9152102763919"></a><ul id="ul9152102763919"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="b4101174416409"><a name="b4101174416409"></a><a name="b4101174416409"></a>Subnets</strong> page. You can view the network ID on the displayed page.</li><li>Method 2: See the "Querying Subnets" section in the <em id="i102188587418"><a name="i102188587418"></a><a name="i102188587418"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row66008059"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p42208903"><a name="p42208903"></a><a name="p42208903"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p193681417164213"><a name="p193681417164213"></a><a name="p193681417164213"></a>Specifies the security group which the RDS DB instance belongs to. To obtain this parameter value, use either of the following methods:</p>
<a name="ul16404122194211"></a><a name="ul16404122194211"></a><ul id="ul16404122194211"><li>Method 1: Log in to VPC console. Choose <strong id="b1913676122"><a name="b1913676122"></a><a name="b1913676122"></a>Access Control</strong> &gt; <strong id="b789502111219"><a name="b789502111219"></a><a name="b789502111219"></a>Security Groups</strong> in the navigation pane on the left. On the displayed page, click the target security group. You can view the security group ID on the displayed page.</li><li>Method 2: See the "Querying Security Groups" section in the <em id="i2369584559"><a name="i2369584559"></a><a name="i2369584559"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row8447315691"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p12016301915"><a name="p12016301915"></a><a name="p12016301915"></a>charge_info</p>
</td>
<td class="cellrowborder" valign="top" width="34.65346534653465%" headers="mcps1.2.5.1.2 "><p id="p18093019918"><a name="p18093019918"></a><a name="p18093019918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p1813161911919"><a name="p1813161911919"></a><a name="p1813161911919"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.2.5.1.4 "><p id="p180153019913"><a name="p180153019913"></a><a name="p180153019913"></a>Specifies the billing information, which is pay-per-use. By default, pay-per-use is used.</p>
<p id="p195191056102519"><a name="p195191056102519"></a><a name="p195191056102519"></a>For details, see <a href="#table992615211258">Table 8</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description \(creating read replicas. This API does not support creating read replicas for yearly/monthly Microsoft SQL Server DB instances.\)

<a name="table16591198151210"></a>
<table><thead align="left"><tr id="row1663514861214"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p18645086122"><a name="p18645086122"></a><a name="p18645086122"></a><strong id="b132301532184914"><a name="b132301532184914"></a><a name="b132301532184914"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.5.1.2"><p id="p206550811210"><a name="p206550811210"></a><a name="p206550811210"></a><strong id="b4232143444910"><a name="b4232143444910"></a><a name="b4232143444910"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p2665684124"><a name="p2665684124"></a><a name="p2665684124"></a><strong id="b351811352492"><a name="b351811352492"></a><a name="b351811352492"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.64356435643564%" id="mcps1.2.5.1.4"><p id="p1967819813127"><a name="p1967819813127"></a><a name="p1967819813127"></a><strong id="b455383664913"><a name="b455383664913"></a><a name="b455383664913"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1169268141212"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p18702148111210"><a name="p18702148111210"></a><a name="p18702148111210"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p9711087123"><a name="p9711087123"></a><a name="p9711087123"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p127211481129"><a name="p127211481129"></a><a name="p127211481129"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p20251134153419"><a name="p20251134153419"></a><a name="p20251134153419"></a>Specifies the DB instance name.</p>
<p id="p17253344340"><a name="p17253344340"></a><a name="p17253344340"></a>The DB instance name of the same type must be unique for the same tenant.</p>
<p id="p9739986124"><a name="p9739986124"></a><a name="p9739986124"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-sensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row179663811216"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1297510801214"><a name="p1297510801214"></a><a name="p1297510801214"></a>replica_of_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p4984168121215"><a name="p4984168121215"></a><a name="p4984168121215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p1727498128"><a name="p1727498128"></a><a name="p1727498128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p1136159181211"><a name="p1136159181211"></a><a name="p1136159181211"></a>Specifies the DB instance ID, which is used to create a read replica.</p>
<p id="p48851020185819"><a name="p48851020185819"></a><a name="p48851020185819"></a>For details, see <span class="parmname" id="parmname242413171108"><a name="parmname242413171108"></a><a name="parmname242413171108"></a><b>id</b></span> in <a href="querying-details-about-db-instances.md#table2058713718267">Table 3</a> in section <a href="querying-details-about-db-instances.md">Querying Details About DB Instances</a>.</p>
</td>
</tr>
<tr id="row1713809131212"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p101485981219"><a name="p101485981219"></a><a name="p101485981219"></a>disk_encryption_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p615549111212"><a name="p615549111212"></a><a name="p615549111212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p151661892126"><a name="p151661892126"></a><a name="p151661892126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p1918039171210"><a name="p1918039171210"></a><a name="p1918039171210"></a>Specifies the key ID for disk encryption. The default value is empty.</p>
</td>
</tr>
<tr id="row219811901216"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p920529201219"><a name="p920529201219"></a><a name="p920529201219"></a>flavor_ref</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p4214192128"><a name="p4214192128"></a><a name="p4214192128"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p17227199201212"><a name="p17227199201212"></a><a name="p17227199201212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p5402027141614"><a name="p5402027141614"></a><a name="p5402027141614"></a>Specifies the specification code. The value cannot be empty.</p>
<p id="p1645132714167"><a name="p1645132714167"></a><a name="p1645132714167"></a>For details, see <span class="parmname" id="parmname228712136432"><a name="parmname228712136432"></a><a name="parmname228712136432"></a><b>spec_code</b></span> in <a href="querying-database-specifications.md#table66531170">Table 3</a> in section <a href="querying-database-specifications.md">Querying Database Specifications</a>.</p>
</td>
</tr>
<tr id="row1325015961210"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p132588914128"><a name="p132588914128"></a><a name="p132588914128"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p5266498128"><a name="p5266498128"></a><a name="p5266498128"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p4982172211916"><a name="p4982172211916"></a><a name="p4982172211916"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p92926915126"><a name="p92926915126"></a><a name="p92926915126"></a>Specifies the volume information.</p>
<p id="p1253782122620"><a name="p1253782122620"></a><a name="p1253782122620"></a>For details, see <a href="#table10656503">Table 7</a>.</p>
</td>
</tr>
<tr id="row152988911120"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p6307990122"><a name="p6307990122"></a><a name="p6307990122"></a>region</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p33171895128"><a name="p33171895128"></a><a name="p33171895128"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p93263961213"><a name="p93263961213"></a><a name="p93263961213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p1833589161210"><a name="p1833589161210"></a><a name="p1833589161210"></a>Specifies the region ID. Currently, read replicas can be created only in the same region as that of the primary DB instance.</p>
<p id="p1034210971218"><a name="p1034210971218"></a><a name="p1034210971218"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="row154028915126"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1141010961213"><a name="p1141010961213"></a><a name="p1141010961213"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p3420291128"><a name="p3420291128"></a><a name="p3420291128"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p1742813913128"><a name="p1742813913128"></a><a name="p1742813913128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p743712961216"><a name="p743712961216"></a><a name="p743712961216"></a>Specifies the AZ ID.</p>
<p id="p04480991212"><a name="p04480991212"></a><a name="p04480991212"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="row77777191106"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p13402152714108"><a name="p13402152714108"></a><a name="p13402152714108"></a>charge_info</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="p134021276106"><a name="p134021276106"></a><a name="p134021276106"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p44771426201913"><a name="p44771426201913"></a><a name="p44771426201913"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.5.1.4 "><p id="p19402192710107"><a name="p19402192710107"></a><a name="p19402192710107"></a>Specifies the billing information, which is pay-per-use. By default, pay-per-use is used.</p>
<p id="p545918325262"><a name="p545918325262"></a><a name="p545918325262"></a>For details, see <a href="#table992615211258">Table 8</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  datastore field data structure description

<a name="table64243102"></a>
<table><thead align="left"><tr id="row4043462"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.2.5.1.1"><p id="p59085005"><a name="p59085005"></a><a name="p59085005"></a><strong id="b7454018185715"><a name="b7454018185715"></a><a name="b7454018185715"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.21%" id="mcps1.2.5.1.2"><p id="p21156092"><a name="p21156092"></a><a name="p21156092"></a><strong id="b127117321005"><a name="b127117321005"></a><a name="b127117321005"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.5.1.3"><p id="p35921916"><a name="p35921916"></a><a name="p35921916"></a><strong id="b139516339019"><a name="b139516339019"></a><a name="b139516339019"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.049999999999997%" id="mcps1.2.5.1.4"><p id="p23994101"><a name="p23994101"></a><a name="p23994101"></a><strong id="b8978123412012"><a name="b8978123412012"></a><a name="b8978123412012"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64473998"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.1 "><p id="p55011311"><a name="p55011311"></a><a name="p55011311"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.5.1.2 "><p id="p26731201"><a name="p26731201"></a><a name="p26731201"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.5.1.3 "><p id="p17743659"><a name="p17743659"></a><a name="p17743659"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.049999999999997%" headers="mcps1.2.5.1.4 "><p id="p49175803141056"><a name="p49175803141056"></a><a name="p49175803141056"></a>Specifies the DB engine. Value:</p>
<a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
</td>
</tr>
<tr id="row40466701"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.2.5.1.1 "><p id="p56577386"><a name="p56577386"></a><a name="p56577386"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.5.1.2 "><p id="p19365543"><a name="p19365543"></a><a name="p19365543"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.5.1.3 "><p id="p25105132"><a name="p25105132"></a><a name="p25105132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.049999999999997%" headers="mcps1.2.5.1.4 "><p id="p20249826"><a name="p20249826"></a><a name="p20249826"></a>Specifies the database version.</p>
<a name="ul2128855618558"></a><a name="ul2128855618558"></a><ul id="ul2128855618558"><li>MySQL databases support 5.6 and 5.7. Example value: 5.7 </li><li>PostgreSQL databases support 9.5, 9.6, 10, and 11. Example value: 9.6</li><li>Microsoft SQL Server databases only support 2014 SE, 2016 SE, and 2016 EE. Example value: 2014_SE</li></ul>
<p id="p2139751518103"><a name="p2139751518103"></a><a name="p2139751518103"></a>For details about supported database versions, see section <a href="querying-version-information-about-a-db-engine.md">Querying Version Information About a DB Engine</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  ha field data structure description

<a name="table13260175614296"></a>
<table><thead align="left"><tr id="row430415632917"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p83131256172915"><a name="p83131256172915"></a><a name="p83131256172915"></a><strong id="b335119141821"><a name="b335119141821"></a><a name="b335119141821"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.5.1.2"><p id="p1532014560298"><a name="p1532014560298"></a><a name="p1532014560298"></a><strong id="b157567152024"><a name="b157567152024"></a><a name="b157567152024"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p83297567293"><a name="p83297567293"></a><a name="p83297567293"></a><strong id="b07661616521"><a name="b07661616521"></a><a name="b07661616521"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.5.1.4"><p id="p734219563293"><a name="p734219563293"></a><a name="p734219563293"></a><strong id="b192774181121"><a name="b192774181121"></a><a name="b192774181121"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row173521956122913"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p123571256172914"><a name="p123571256172914"></a><a name="p123571256172914"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p336525662915"><a name="p336525662915"></a><a name="p336525662915"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p15376756162917"><a name="p15376756162917"></a><a name="p15376756162917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p16181542163018"><a name="p16181542163018"></a><a name="p16181542163018"></a>Specifies the DB instance type. The value is <strong id="b42701951145715"><a name="b42701951145715"></a><a name="b42701951145715"></a>Ha</strong> (primary/standby DB instances) and is case-insensitive.</p>
</td>
</tr>
<tr id="row840515672916"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p92151105323"><a name="p92151105323"></a><a name="p92151105323"></a>replication_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p62151809326"><a name="p62151809326"></a><a name="p62151809326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1721540173210"><a name="p1721540173210"></a><a name="p1721540173210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p15585263415"><a name="p15585263415"></a><a name="p15585263415"></a>Specifies the replication mode for the standby DB instance.</p>
<p id="p121155213343"><a name="p121155213343"></a><a name="p121155213343"></a>Value:</p>
<a name="ul120105263413"></a><a name="ul120105263413"></a><ul id="ul120105263413"><li>For MySQL, the value is <strong id="b842352706165650_1"><a name="b842352706165650_1"></a><a name="b842352706165650_1"></a>async</strong> or <strong id="b842352706165654_1"><a name="b842352706165654_1"></a><a name="b842352706165654_1"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b842352706165650_5"><a name="b842352706165650_5"></a><a name="b842352706165650_5"></a>async</strong> or <strong id="b842352706165654_5"><a name="b842352706165654_5"></a><a name="b842352706165654_5"></a>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong id="b1084866521183314"><a name="b1084866521183314"></a><a name="b1084866521183314"></a>sync</strong>.</li></ul>
<div class="note" id="note17075210348"><a name="note17075210348"></a><a name="note17075210348"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul9881252203415"></a><a name="ul9881252203415"></a><ul id="ul9881252203415"><li><strong id="b842352706105954"><a name="b842352706105954"></a><a name="b842352706105954"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b842352706164020"><a name="b842352706164020"></a><a name="b842352706164020"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b13384211081105"><a name="b13384211081105"></a><a name="b13384211081105"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  6**  backupStrategy field data structure description

<a name="table0863181193416"></a>
<table><thead align="left"><tr id="row49079123417"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p491419118346"><a name="p491419118346"></a><a name="p491419118346"></a><strong id="b1519442321112"><a name="b1519442321112"></a><a name="b1519442321112"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.5.1.2"><p id="p1921131193411"><a name="p1921131193411"></a><a name="p1921131193411"></a><strong id="b89021624111113"><a name="b89021624111113"></a><a name="b89021624111113"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p1293171203411"><a name="p1293171203411"></a><a name="p1293171203411"></a><strong id="b1010742615116"><a name="b1010742615116"></a><a name="b1010742615116"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.5.1.4"><p id="p17939718349"><a name="p17939718349"></a><a name="p17939718349"></a><strong id="b3857828121111"><a name="b3857828121111"></a><a name="b3857828121111"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1094610120345"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1295681153413"><a name="p1295681153413"></a><a name="p1295681153413"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="p119619110347"><a name="p119619110347"></a><a name="p119619110347"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p5970201183417"><a name="p5970201183417"></a><a name="p5970201183417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p8983181183415"><a name="p8983181183415"></a><a name="p8983181183415"></a>Specifies the backup time window. Automated backups will be triggered during the backup time window.</p>
<p id="p144363282818"><a name="p144363282818"></a><a name="p144363282818"></a>The value cannot be empty. It must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
<a name="ul73551635192814"></a><a name="ul73551635192814"></a><ul id="ul73551635192814"><li>The <strong id="b5530258153011"><a name="b5530258153011"></a><a name="b5530258153011"></a>HH</strong> value must be 1 greater than the <strong id="b2053210587304"><a name="b2053210587304"></a><a name="b2053210587304"></a>hh</strong> value.</li><li>The values of <strong id="b980810043118"><a name="b980810043118"></a><a name="b980810043118"></a>mm</strong> and <strong id="b48083010310"><a name="b48083010310"></a><a name="b48083010310"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b780814063112"><a name="b780814063112"></a><a name="b780814063112"></a>00</strong>, <strong id="b1580890143110"><a name="b1580890143110"></a><a name="b1580890143110"></a>15</strong>, <strong id="b2809180133112"><a name="b2809180133112"></a><a name="b2809180133112"></a>30</strong>, or <strong id="b1780918016317"><a name="b1780918016317"></a><a name="b1780918016317"></a>45</strong>.</li></ul>
<p id="p59342194324"><a name="p59342194324"></a><a name="p59342194324"></a>Example value:</p>
<a name="ul1210322243217"></a><a name="ul1210322243217"></a><ul id="ul1210322243217"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
</td>
</tr>
<tr id="row1699610173414"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p677216342"><a name="p677216342"></a><a name="p677216342"></a>keep_days</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="p2171624347"><a name="p2171624347"></a><a name="p2171624347"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p125424341"><a name="p125424341"></a><a name="p125424341"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p13613273417"><a name="p13613273417"></a><a name="p13613273417"></a>Specifies the retention days for specific backup files.</p>
<p id="p7391722345"><a name="p7391722345"></a><a name="p7391722345"></a>The value range is from 0 to 732. If this parameter is not specified or set to <strong id="b842352706112318"><a name="b842352706112318"></a><a name="b842352706112318"></a>0</strong>, the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
<div class="notice" id="note861516536349"><a name="note861516536349"></a><a name="note861516536349"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1558917683213"><a name="p1558917683213"></a><a name="p1558917683213"></a>Primary/standby DB instances of Microsoft SQL Server do not support disabling the automated backup policy.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  7**  volume field data structure description

<a name="table10656503"></a>
<table><thead align="left"><tr id="row5847780"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p3908185"><a name="p3908185"></a><a name="p3908185"></a><strong id="b856633513152"><a name="b856633513152"></a><a name="b856633513152"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.5.1.2"><p id="p48127554"><a name="p48127554"></a><a name="p48127554"></a><strong id="b20635173612152"><a name="b20635173612152"></a><a name="b20635173612152"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p6017800"><a name="p6017800"></a><a name="p6017800"></a><strong id="b1280583810151"><a name="b1280583810151"></a><a name="b1280583810151"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.5.1.4"><p id="p17679762"><a name="p17679762"></a><a name="p17679762"></a><strong id="b10752439191511"><a name="b10752439191511"></a><a name="b10752439191511"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22774600"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p32803348"><a name="p32803348"></a><a name="p32803348"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p39825499"><a name="p39825499"></a><a name="p39825499"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p4640007"><a name="p4640007"></a><a name="p4640007"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p40296320"><a name="p40296320"></a><a name="p40296320"></a>Specifies the volume type.</p>
<p id="p27122565"><a name="p27122565"></a><a name="p27122565"></a>Its value can be any of the following and is case-sensitive:</p>
<a name="ul7711857141311"></a><a name="ul7711857141311"></a><ul id="ul7711857141311"><li><strong id="b175811447151011"><a name="b175811447151011"></a><a name="b175811447151011"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b4248410143119"><a name="b4248410143119"></a><a name="b4248410143119"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
</td>
</tr>
<tr id="row42343927"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p7306053"><a name="p7306053"></a><a name="p7306053"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.2 "><p id="p54919424"><a name="p54919424"></a><a name="p54919424"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p19288335"><a name="p19288335"></a><a name="p19288335"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.5.1.4 "><p id="p18851291"><a name="p18851291"></a><a name="p18851291"></a>Specifies the volume size.</p>
<p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>Its value must be a multiple of 10 and the value range is from 40 GB to 4000 GB.</p>
<div class="note" id="note02685513325"><a name="note02685513325"></a><a name="note02685513325"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p385416153310"><a name="p385416153310"></a><a name="p385416153310"></a>For read replicas, this parameter is invalid. The volume size is the same as that of the primary DB instance by default.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  8**  chargeInfo field data structure description

<a name="table992615211258"></a>
<table><thead align="left"><tr id="row139830521259"><th class="cellrowborder" valign="top" width="19.491949194919492%" id="mcps1.2.5.1.1"><p id="p18997135202515"><a name="p18997135202515"></a><a name="p18997135202515"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.67256725672567%" id="mcps1.2.5.1.2"><p id="p4995352514"><a name="p4995352514"></a><a name="p4995352514"></a><strong id="b916371947"><a name="b916371947"></a><a name="b916371947"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.13201320132013%" id="mcps1.2.5.1.3"><p id="p7219531251"><a name="p7219531251"></a><a name="p7219531251"></a><strong id="b221124618"><a name="b221124618"></a><a name="b221124618"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.703470347034695%" id="mcps1.2.5.1.4"><p id="p143485310253"><a name="p143485310253"></a><a name="p143485310253"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row44865311257"><td class="cellrowborder" valign="top" width="19.491949194919492%" headers="mcps1.2.5.1.1 "><p id="p147051450112610"><a name="p147051450112610"></a><a name="p147051450112610"></a>charge_mode</p>
</td>
<td class="cellrowborder" valign="top" width="25.67256725672567%" headers="mcps1.2.5.1.2 "><p id="p170519503263"><a name="p170519503263"></a><a name="p170519503263"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.13201320132013%" headers="mcps1.2.5.1.3 "><p id="p3705750182610"><a name="p3705750182610"></a><a name="p3705750182610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.703470347034695%" headers="mcps1.2.5.1.4 "><p id="p13419304384"><a name="p13419304384"></a><a name="p13419304384"></a>Specifies the billing mode.</p>
<p id="p134812510201"><a name="p134812510201"></a><a name="p134812510201"></a>The value <strong id="b950011618311"><a name="b950011618311"></a><a name="b950011618311"></a>postPaid</strong> indicates the pay-per-use billing mode.</p>
</td>
</tr>
</tbody>
</table>

-   Request example

    Creating a single DB instance:

    ```
    {
    	"name": "rds-instance-rep2",
    	"datastore": {
    		"type": "MySQL",
    		"version": "5.6"
    	},
    	"flavor_ref": "rds.mysql.s1.large",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 100
    	},
    	"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    	"region": "eu-de",
    	"availability_zone": "eu-de-01",
    	"vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    	"subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
    	"security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5",
    	"port": 8635,
    	"backup_strategy": {
    		"start_time": "08:15-09:15",
    		"keep_days": 12
    	},
    	"charge_info": {
    		"charge_mode": "postPaid"
    	},
    	"password": "Test@12345678",
    	"configuration_id": "452408-ef4b-44c5-94be-305145fg"
    }
    ```

    Creating primary/standby DB instances:

    ```
    {
    	"name": "rds-instance-rep2",
    	"datastore": {
    		"type": "MySQL",
    		"version": "5.6"
    	},
    	"ha": {
    		"mode": "ha",
    		"replication_mode": "semisync"
    	},
    	"flavor_ref": "rds.mysql.s1.large.ha",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 100
    	},
    	"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    	"region": "eu-de",
    	"availability_zone": "eu-de-01,eu-de-02",
    	"vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    	"subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
    	"security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5",
    	"port": 8635,
    	"backup_strategy": {
    		"start_time": "08:15-09:15",
    		"keep_days": 12
    	},
    	"charge_info": {
    		"charge_mode": "postPaid"
    	},
    	"password": "Test@12345678",
    	"configuration_id": "452408-ef4b-44c5-94be-305145fg"
    }
    ```

    Creating a read replica:

    ```
    {
    	"name": "rds-instance-rep2",
    	"replica_of_id": "afdsad-fds-fdsagin01",
    	"flavor_ref": "rds.mysql.s1.large.rr",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 100
    	},
    	"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    	"region": "eu-de",
    	"availability_zone": "eu-de-01"
    }
    ```


## Response<a name="section36749739"></a>

-   Normal response

    **Table  9**  Parameter description

    <a name="table17474517"></a>
    <table><thead align="left"><tr id="row16146366"><th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.1"><p id="p32787233"><a name="p32787233"></a><a name="p32787233"></a><strong id="b1923318131915"><a name="b1923318131915"></a><a name="b1923318131915"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.29%" id="mcps1.2.4.1.2"><p id="p38520254"><a name="p38520254"></a><a name="p38520254"></a><strong id="b224313917193"><a name="b224313917193"></a><a name="b224313917193"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p33132859"><a name="p33132859"></a><a name="p33132859"></a><strong id="b2187181012195"><a name="b2187181012195"></a><a name="b2187181012195"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66515904"><td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.1 "><p id="p19079158"><a name="p19079158"></a><a name="p19079158"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.29%" headers="mcps1.2.4.1.2 "><p id="p148451042014"><a name="p148451042014"></a><a name="p148451042014"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p48735027"><a name="p48735027"></a><a name="p48735027"></a>Indicates the DB instance information.</p>
    <p id="p31211412488"><a name="p31211412488"></a><a name="p31211412488"></a>For details, see <a href="#table175305610274">Table 10</a>.</p>
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

    **Table  10**  instance field data structure description

    <a name="table175305610274"></a>
    <table><thead align="left"><tr id="row4782256142718"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p11791105616272"><a name="p11791105616272"></a><a name="p11791105616272"></a><strong id="b3479182912209"><a name="b3479182912209"></a><a name="b3479182912209"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1280910568278"><a name="p1280910568278"></a><a name="p1280910568278"></a><strong id="b19212231152015"><a name="b19212231152015"></a><a name="b19212231152015"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p081620561276"><a name="p081620561276"></a><a name="p081620561276"></a><strong id="b141701329208"><a name="b141701329208"></a><a name="b141701329208"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row83685201297"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p109879468293"><a name="p109879468293"></a><a name="p109879468293"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14953885305"><a name="p14953885305"></a><a name="p14953885305"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1798714612914"><a name="p1798714612914"></a><a name="p1798714612914"></a>Indicates the DB instance ID.</p>
    <div class="note" id="note10609835155910"><a name="note10609835155910"></a><a name="note10609835155910"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1661116354596"><a name="p1661116354596"></a><a name="p1661116354596"></a>The v3 DB instance ID is incompatible with the v1 DB instance ID.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row88231562277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p383295682710"><a name="p383295682710"></a><a name="p383295682710"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p48498568273"><a name="p48498568273"></a><a name="p48498568273"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1785918563276"><a name="p1785918563276"></a><a name="p1785918563276"></a>Indicates the DB instance name. Indicates the DB instance name. DB instances of the same type can have same names under the same tenant.</p>
    <p id="p168621956132710"><a name="p168621956132710"></a><a name="p168621956132710"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1326042683017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p986116344302"><a name="p986116344302"></a><a name="p986116344302"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4861203433016"><a name="p4861203433016"></a><a name="p4861203433016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p78617346309"><a name="p78617346309"></a><a name="p78617346309"></a>Indicates the DB instance status. For example, <strong id="b9548194552618"><a name="b9548194552618"></a><a name="b9548194552618"></a>BUILD</strong> indicates that the DB instance is being created.</p>
    </td>
    </tr>
    <tr id="row1587195662712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p188761056132717"><a name="p188761056132717"></a><a name="p188761056132717"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1420620152206"><a name="p1420620152206"></a><a name="p1420620152206"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13907115612720"><a name="p13907115612720"></a><a name="p13907115612720"></a>Indicates the database information.</p>
    <p id="p3202172191616"><a name="p3202172191616"></a><a name="p3202172191616"></a>For details, see <a href="#table766045720277">Table 11</a>.</p>
    </td>
    </tr>
    <tr id="row2091115617278"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15919756162716"><a name="p15919756162716"></a><a name="p15919756162716"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5393917192016"><a name="p5393917192016"></a><a name="p5393917192016"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11951155662714"><a name="p11951155662714"></a><a name="p11951155662714"></a>Indicates the HA configuration parameters. This parameter is returned only when primary/standby DB instances are created.</p>
    <p id="p175371517131617"><a name="p175371517131617"></a><a name="p175371517131617"></a>For details, see <a href="#table15899105722713">Table 12</a>.</p>
    </td>
    </tr>
    <tr id="row2095545611272"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p189601356162713"><a name="p189601356162713"></a><a name="p189601356162713"></a>configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1697725682718"><a name="p1697725682718"></a><a name="p1697725682718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p198515563273"><a name="p198515563273"></a><a name="p198515563273"></a>Indicates the parameter template ID. This parameter is returned only when a custom parameter template is used during DB instance creation.</p>
    </td>
    </tr>
    <tr id="row1299345602718"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20311571272"><a name="p20311571272"></a><a name="p20311571272"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1923157132717"><a name="p1923157132717"></a><a name="p1923157132717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1133155782713"><a name="p1133155782713"></a><a name="p1133155782713"></a>Indicates the database port, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row711835715271"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8127757182713"><a name="p8127757182713"></a><a name="p8127757182713"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p112581220112016"><a name="p112581220112016"></a><a name="p112581220112016"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3151145732716"><a name="p3151145732716"></a><a name="p3151145732716"></a>Indicates the automated backup policy.</p>
    <p id="p1727510419167"><a name="p1727510419167"></a><a name="p1727510419167"></a>For details, see <a href="#table81249589270">Table 13</a>.</p>
    </td>
    </tr>
    <tr id="row11961857142710"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p420435702717"><a name="p420435702717"></a><a name="p420435702717"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2219205782710"><a name="p2219205782710"></a><a name="p2219205782710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p12644165011499"><a name="p12644165011499"></a><a name="p12644165011499"></a>Indicates the key ID for disk encryption. By default, this parameter is empty and is returned only when it is specified during the DB instance creation.</p>
    </td>
    </tr>
    <tr id="row1023011571273"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62375571274"><a name="p62375571274"></a><a name="p62375571274"></a>flavor_ref</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12250057172719"><a name="p12250057172719"></a><a name="p12250057172719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p236414121179"><a name="p236414121179"></a><a name="p236414121179"></a>Indicates the specification code. The value cannot be empty.</p>
    <p id="p7368101291717"><a name="p7368101291717"></a><a name="p7368101291717"></a>For details, see <span class="parmname" id="parmname33904329319"><a name="parmname33904329319"></a><a name="parmname33904329319"></a><b>spec_code</b></span> in <a href="querying-database-specifications.md#table66531170">Table 3</a> in section <a href="querying-database-specifications.md">Querying Database Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row727255762713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22816576279"><a name="p22816576279"></a><a name="p22816576279"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1127219238200"><a name="p1127219238200"></a><a name="p1127219238200"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16313145722718"><a name="p16313145722718"></a><a name="p16313145722718"></a>Indicates the volume information.</p>
    <p id="p9926555171610"><a name="p9926555171610"></a><a name="p9926555171610"></a>For details, see <a href="#table5324165817272">Table 14</a>.</p>
    </td>
    </tr>
    <tr id="row1331675710271"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p132655742711"><a name="p132655742711"></a><a name="p132655742711"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p83409571274"><a name="p83409571274"></a><a name="p83409571274"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9347357152716"><a name="p9347357152716"></a><a name="p9347357152716"></a>Indicates the region ID.</p>
    </td>
    </tr>
    <tr id="row04101057112715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p441975772719"><a name="p441975772719"></a><a name="p441975772719"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7431165752717"><a name="p7431165752717"></a><a name="p7431165752717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p104381557182713"><a name="p104381557182713"></a><a name="p104381557182713"></a>Indicates the AZ ID.</p>
    </td>
    </tr>
    <tr id="row54992572275"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14507155732716"><a name="p14507155732716"></a><a name="p14507155732716"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1522205719275"><a name="p1522205719275"></a><a name="p1522205719275"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7759131604512"><a name="p7759131604512"></a><a name="p7759131604512"></a>Indicates the VPC ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul475921618452"></a><a name="ul475921618452"></a><ul id="ul475921618452"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: See the "Querying VPCs" section in the <em id="rds_01_0002_i842352697165629"><a name="rds_01_0002_i842352697165629"></a><a name="rds_01_0002_i842352697165629"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row4544757192710"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p125528573274"><a name="p125528573274"></a><a name="p125528573274"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20568457112711"><a name="p20568457112711"></a><a name="p20568457112711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27596160451"><a name="p27596160451"></a><a name="p27596160451"></a>Indicates the network ID. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul375971611456"></a><a name="ul375971611456"></a><ul id="ul375971611456"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="rds_01_0002_b4101174416409"><a name="rds_01_0002_b4101174416409"></a><a name="rds_01_0002_b4101174416409"></a>Subnets</strong> page. You can view the network ID on the displayed page.</li><li>Method 2: See the "Querying Subnets" section in the <em id="rds_01_0002_i102188587418"><a name="rds_01_0002_i102188587418"></a><a name="rds_01_0002_i102188587418"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row158217577276"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7590145715274"><a name="p7590145715274"></a><a name="p7590145715274"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9603205716276"><a name="p9603205716276"></a><a name="p9603205716276"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p157601616114517"><a name="p157601616114517"></a><a name="p157601616114517"></a>Indicates the security group which the RDS DB instance belongs to. To obtain this parameter value, use either of the following methods:</p>
    <a name="ul37601616154512"></a><a name="ul37601616154512"></a><ul id="ul37601616154512"><li>Method 1: Log in to VPC console. Choose <strong id="rds_01_0002_b1913676122"><a name="rds_01_0002_b1913676122"></a><a name="rds_01_0002_b1913676122"></a>Access Control</strong> &gt; <strong id="rds_01_0002_b789502111219"><a name="rds_01_0002_b789502111219"></a><a name="rds_01_0002_b789502111219"></a>Security Groups</strong> in the navigation pane on the left. On the displayed page, click the target security group. You can view the security group ID on the displayed page.</li><li>Method 2: See the "Querying Security Groups" section in the <em id="rds_01_0002_i2369584559"><a name="rds_01_0002_i2369584559"></a><a name="rds_01_0002_i2369584559"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row0196133117331"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p020245918349"><a name="p020245918349"></a><a name="p020245918349"></a>charge_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16860202662013"><a name="p16860202662013"></a><a name="p16860202662013"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p132021959163412"><a name="p132021959163412"></a><a name="p132021959163412"></a>Indicates the billing information, which is pay-per-use.</p>
    <p id="p1755410518172"><a name="p1755410518172"></a><a name="p1755410518172"></a>For details, see <a href="#table207147873611">Table 15</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11**  datastore field data structure description

    <a name="table766045720277"></a>
    <table><thead align="left"><tr id="row468335722716"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.2.4.1.1"><p id="p156891357202720"><a name="p156891357202720"></a><a name="p156891357202720"></a><strong id="b1981643284612"><a name="b1981643284612"></a><a name="b1981643284612"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.3%" id="mcps1.2.4.1.2"><p id="p77089577277"><a name="p77089577277"></a><a name="p77089577277"></a><strong id="b1639043514465"><a name="b1639043514465"></a><a name="b1639043514465"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.53%" id="mcps1.2.4.1.3"><p id="p13715557112714"><a name="p13715557112714"></a><a name="p13715557112714"></a><strong id="b272823624615"><a name="b272823624615"></a><a name="b272823624615"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9723165742714"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.4.1.1 "><p id="p17321257162715"><a name="p17321257162715"></a><a name="p17321257162715"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.4.1.2 "><p id="p17521757192712"><a name="p17521757192712"></a><a name="p17521757192712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.53%" headers="mcps1.2.4.1.3 "><p id="p1734174217233"><a name="p1734174217233"></a><a name="p1734174217233"></a>Indicates the DB engine. Value:</p>
    <a name="ul137341742112314"></a><a name="ul137341742112314"></a><ul id="ul137341742112314"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row37937570272"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.4.1.1 "><p id="p10800165713279"><a name="p10800165713279"></a><a name="p10800165713279"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.4.1.2 "><p id="p0819195719271"><a name="p0819195719271"></a><a name="p0819195719271"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.53%" headers="mcps1.2.4.1.3 "><p id="p1957105533718"><a name="p1957105533718"></a><a name="p1957105533718"></a>Indicates the database version.</p>
    <p id="p71501555377"><a name="p71501555377"></a><a name="p71501555377"></a>For details about supported database versions, see section <a href="database-version-queries.md">Database Version Queries</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  12**  ha field data structure description

    <a name="table15899105722713"></a>
    <table><thead align="left"><tr id="row1393295712715"><th class="cellrowborder" valign="top" width="19.31%" id="mcps1.2.4.1.1"><p id="p2941125719278"><a name="p2941125719278"></a><a name="p2941125719278"></a><strong id="b2060931019487"><a name="b2060931019487"></a><a name="b2060931019487"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.229999999999997%" id="mcps1.2.4.1.2"><p id="p119521157162710"><a name="p119521157162710"></a><a name="p119521157162710"></a><strong id="b1595731515483"><a name="b1595731515483"></a><a name="b1595731515483"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.459999999999994%" id="mcps1.2.4.1.3"><p id="p15960175762715"><a name="p15960175762715"></a><a name="p15960175762715"></a><strong id="b153161217104811"><a name="b153161217104811"></a><a name="b153161217104811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1965185792714"><td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.1 "><p id="p179729572279"><a name="p179729572279"></a><a name="p179729572279"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.229999999999997%" headers="mcps1.2.4.1.2 "><p id="p14990257142711"><a name="p14990257142711"></a><a name="p14990257142711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p4997155711270"><a name="p4997155711270"></a><a name="p4997155711270"></a>Indicates the DB instance type. The value is <strong id="b1731261515142"><a name="b1731261515142"></a><a name="b1731261515142"></a>Ha</strong> (primary/standby DB instances).</p>
    </td>
    </tr>
    <tr id="row72115815278"><td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.1 "><p id="p29658162714"><a name="p29658162714"></a><a name="p29658162714"></a>replication_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.229999999999997%" headers="mcps1.2.4.1.2 "><p id="p1023185852714"><a name="p1023185852714"></a><a name="p1023185852714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p633115816277"><a name="p633115816277"></a><a name="p633115816277"></a>Indicates the replication mode for the standby DB instance. This parameter is valid when the <strong id="b16915165181410"><a name="b16915165181410"></a><a name="b16915165181410"></a>mode</strong> is <strong id="b791675181411"><a name="b791675181411"></a><a name="b791675181411"></a>Ha</strong>.</p>
    <p id="p1837105812718"><a name="p1837105812718"></a><a name="p1837105812718"></a>Value:</p>
    <a name="ul184125872719"></a><a name="ul184125872719"></a><ul id="ul184125872719"><li>For MySQL, the value is <strong id="b61924266493"><a name="b61924266493"></a><a name="b61924266493"></a>async</strong> or <strong id="b819332654913"><a name="b819332654913"></a><a name="b819332654913"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b1676132994915"><a name="b1676132994915"></a><a name="b1676132994915"></a>async</strong> or <strong id="b17623290494"><a name="b17623290494"></a><a name="b17623290494"></a>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong id="b72418327496"><a name="b72418327496"></a><a name="b72418327496"></a>sync</strong>.</li></ul>
    <div class="note" id="note575155882717"><a name="note575155882717"></a><a name="note575155882717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul593135817276"></a><a name="ul593135817276"></a><ul id="ul593135817276"><li><strong id="b209335194918"><a name="b209335194918"></a><a name="b209335194918"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b6463816497"><a name="b6463816497"></a><a name="b6463816497"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b4648540124911"><a name="b4648540124911"></a><a name="b4648540124911"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  13**  backupStrategy field data structure description

    <a name="table81249589270"></a>
    <table><thead align="left"><tr id="row7155105822719"><th class="cellrowborder" valign="top" width="20.810000000000002%" id="mcps1.2.4.1.1"><p id="p151651758112710"><a name="p151651758112710"></a><a name="p151651758112710"></a><strong id="b1317048124917"><a name="b1317048124917"></a><a name="b1317048124917"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.21%" id="mcps1.2.4.1.2"><p id="p818335813276"><a name="p818335813276"></a><a name="p818335813276"></a><strong id="b1658905013490"><a name="b1658905013490"></a><a name="b1658905013490"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.980000000000004%" id="mcps1.2.4.1.3"><p id="p14192195817274"><a name="p14192195817274"></a><a name="p14192195817274"></a><strong id="b58027515491"><a name="b58027515491"></a><a name="b58027515491"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1220112589270"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p321175814278"><a name="p321175814278"></a><a name="p321175814278"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p16233758102717"><a name="p16233758102717"></a><a name="p16233758102717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p9542823183517"><a name="p9542823183517"></a><a name="p9542823183517"></a>Specifies the backup time window. Automated backups will be triggered during the backup time window.</p>
    <p id="p122470773718"><a name="p122470773718"></a><a name="p122470773718"></a>The value cannot be empty. It must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
    <a name="ul152511713710"></a><a name="ul152511713710"></a><ul id="ul152511713710"><li>The <strong id="b47116919575"><a name="b47116919575"></a><a name="b47116919575"></a>HH</strong> value must be 1 greater than the <strong id="b147210975710"><a name="b147210975710"></a><a name="b147210975710"></a>hh</strong> value.</li><li>The values of <strong id="b4517171220573"><a name="b4517171220573"></a><a name="b4517171220573"></a>mm</strong> and <strong id="b751912121579"><a name="b751912121579"></a><a name="b751912121579"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b65191612185719"><a name="b65191612185719"></a><a name="b65191612185719"></a>00</strong>, <strong id="b1252117129570"><a name="b1252117129570"></a><a name="b1252117129570"></a>15</strong>, <strong id="b652313123574"><a name="b652313123574"></a><a name="b652313123574"></a>30</strong>, or <strong id="b15241112195713"><a name="b15241112195713"></a><a name="b15241112195713"></a>45</strong>.</li></ul>
    <p id="p18280157153716"><a name="p18280157153716"></a><a name="p18280157153716"></a>Example value:</p>
    <a name="ul132861073374"></a><a name="ul132861073374"></a><ul id="ul132861073374"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
    <p id="p17846943163516"><a name="p17846943163516"></a><a name="p17846943163516"></a>If <span class="parmname" id="parmname87264315208"><a name="parmname87264315208"></a><a name="parmname87264315208"></a><b>backup_strategy</b></span> in the request body is empty, <span class="parmvalue" id="parmvalue167315432201"><a name="parmvalue167315432201"></a><a name="parmvalue167315432201"></a><b>02:00-03:00</b></span> is returned for <span class="parmname" id="parmname57384320206"><a name="parmname57384320206"></a><a name="parmname57384320206"></a><b>start_time</b></span> by default.</p>
    </td>
    </tr>
    <tr id="row162581058122711"><td class="cellrowborder" valign="top" width="20.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p8266145882712"><a name="p8266145882712"></a><a name="p8266145882712"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p9286558152710"><a name="p9286558152710"></a><a name="p9286558152710"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p229865817274"><a name="p229865817274"></a><a name="p229865817274"></a>Indicates the retention days for specific backup files.</p>
    <p id="p1230285817274"><a name="p1230285817274"></a><a name="p1230285817274"></a>The value range is from 0 to 732. If this parameter is not specified or set to <strong id="b154931332175017"><a name="b154931332175017"></a><a name="b154931332175017"></a>0</strong>, the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    <p id="p13596123011365"><a name="p13596123011365"></a><a name="p13596123011365"></a>If <span class="parmname" id="parmname135371651182016"><a name="parmname135371651182016"></a><a name="parmname135371651182016"></a><b>backup_strategy</b></span> in the request body is empty, <span class="parmvalue" id="parmvalue1153895192014"><a name="parmvalue1153895192014"></a><a name="parmvalue1153895192014"></a><b>7</b></span> is returned for <span class="parmname" id="parmname165381351172018"><a name="parmname165381351172018"></a><a name="parmname165381351172018"></a><b>keep_days</b></span> by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  14**  volume field data structure description

    <a name="table5324165817272"></a>
    <table><thead align="left"><tr id="row13366558182710"><th class="cellrowborder" valign="top" width="20.87%" id="mcps1.2.4.1.1"><p id="p43785583277"><a name="p43785583277"></a><a name="p43785583277"></a><strong id="b89163418503"><a name="b89163418503"></a><a name="b89163418503"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.2"><p id="p04002058182712"><a name="p04002058182712"></a><a name="p04002058182712"></a><strong id="b588819452509"><a name="b588819452509"></a><a name="b588819452509"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.75%" id="mcps1.2.4.1.3"><p id="p1841019583272"><a name="p1841019583272"></a><a name="p1841019583272"></a><strong id="b99501546155010"><a name="b99501546155010"></a><a name="b99501546155010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1941717585272"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.4.1.1 "><p id="p542455816278"><a name="p542455816278"></a><a name="p542455816278"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="p8441115892715"><a name="p8441115892715"></a><a name="p8441115892715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.75%" headers="mcps1.2.4.1.3 "><p id="p144508584276"><a name="p144508584276"></a><a name="p144508584276"></a>Indicates the volume type.</p>
    <p id="p788415113303"><a name="p788415113303"></a><a name="p788415113303"></a>Its value can be any of the following and is case-sensitive:</p>
    <a name="ul97191143171815"></a><a name="ul97191143171815"></a><ul id="ul97191143171815"><li><strong id="b719833457"><a name="b719833457"></a><a name="b719833457"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b1442253005"><a name="b1442253005"></a><a name="b1442253005"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
    </td>
    </tr>
    <tr id="row164658587274"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.4.1.1 "><p id="p1247475842718"><a name="p1247475842718"></a><a name="p1247475842718"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.2 "><p id="p1549255811272"><a name="p1549255811272"></a><a name="p1549255811272"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.75%" headers="mcps1.2.4.1.3 "><p id="p7502958132716"><a name="p7502958132716"></a><a name="p7502958132716"></a>Indicates the volume size.</p>
    <p id="p251014588279"><a name="p251014588279"></a><a name="p251014588279"></a>Its value range is from 40 GB to 4000 GB. The value must be a multiple of 10.</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  15**  chargeInfo field data structure description

    <a name="table207147873611"></a>
    <table><thead align="left"><tr id="row1577020823612"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.2.4.1.1"><p id="p178613803619"><a name="p178613803619"></a><a name="p178613803619"></a><strong id="b92145966"><a name="b92145966"></a><a name="b92145966"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.82%" id="mcps1.2.4.1.2"><p id="p281617863613"><a name="p281617863613"></a><a name="p281617863613"></a><strong id="b1642553666"><a name="b1642553666"></a><a name="b1642553666"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.459999999999994%" id="mcps1.2.4.1.3"><p id="p98254810367"><a name="p98254810367"></a><a name="p98254810367"></a><strong id="b229526089"><a name="b229526089"></a><a name="b229526089"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row188358873611"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.2.4.1.1 "><p id="p2611995378"><a name="p2611995378"></a><a name="p2611995378"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.82%" headers="mcps1.2.4.1.2 "><p id="p1161892377"><a name="p1161892377"></a><a name="p1161892377"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p1161169163719"><a name="p1161169163719"></a><a name="p1161169163719"></a>Indicates the billing information, which is pay-per-use.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    Creating a single DB instance:

    ```
    {
    	"instance": {
    		"id": "dsfae23fsfdsae3435in01",
    		"name": "trove-instance-rep2",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.6"
    		},
    		"flavor_ref": "rds.mysql.s1.large",
    		"volume": {
    			"type": "ULTRAHIGH",
    			"size": 100
    		},
    		"disk_encryption_id": "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
    		"region": "eu-de",
    		"availability_zone": "eu-de-01",
    		"vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    		"subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
    		"security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5",
    		"port": "8635",
    		"backup_strategy": {
    			"start_time": "08:15-09:15",
    			"keep_days": 3
    		},
    		"configuration_id": "452408-44c5-94be-305145fg",
    		"charge_info": {
    			"charge_mode": "postPaid"
    		}
    	},
    	"job_id": "dff1d289-4d03-4942-8b9f-463ea07c000d"
    }
    ```

    Creating primary/standby DB instances:

    ```
    {
      "instance":{ 
               "id": "dsfae23fsfdsae3435in01",
               "name": "trove-instance-rep2", 
               "datastore": { 
                 "type": "MySQL", 
                 "version": "5.6" 
                }, 
               "ha": {
                 "mode": "ha",
                 "replication_mode": "semisync"
               },
               "flavor_ref": "rds.mysql.s1.large.ha",
               "volume": { 
                   "type": "ULTRAHIGH", 
                   "size": 100 
                 },
               "disk_encryption_id":  "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
               "region": "eu-de",
               "availability_zone": "eu-de-01,en-de-02",
               "vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce", 
               "subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
               "security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5", 
               "port": "8635", 
               "backup_strategy": { 
                 "start_time": "08:15-09:15", 
                 "keep_days": 3 
                }, 
               "configuration_id": "452408-44c5-94be-305145fg",
               "charge_info": {
                       "charge_mode": "postPaid"
                                   },
             },
      "job_id": "dff1d289-4d03-4942-8b9f-463ea07c000d" 
    }
    ```

    Creating a read replica:

    ```
    {
      "instance":{ 
                "id": "dsfae23fsfdsae3435in01",
                "name": "trove-instance-rep2", 
                "flavor_ref": "rds.mysql.s1.large.rr",
                 "volume": { 
                   "type": "ULTRAHIGH", 
                   "size": 100 
                 },
               "disk_encryption_id":  "2gfdsh-844a-4023-a776-fc5c5fb71fb4",
               "region": "eu-de",
               "availability_zone": "eu-de-01",
               "vpc_id": "490a4a08-ef4b-44c5-94be-3051ef9e4fce", 
               "subnet_id": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f",
               "security_group_id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5", 
               "port": "8635", 
               "configuration_id": "452408-44c5-94be-305145fg"
             },
     "job_id": "dff1d289-4d03-4942-8b9f-463ea07c000d"  
    
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

