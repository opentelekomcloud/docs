# Creating a Parameter Template<a name="rds_09_0302"></a>

## Function<a name="section182013364336"></a>

This API is used to create a parameter template and configure the name, description, DB engine, and parameter values in the parameter template.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section380114515317"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

-   The name of the created parameter template cannot be the same as that of the default or an existing parameter template.

## URI<a name="section3208362333"></a>

-   URI format

    POST https://\{_Endpoint_\}/v3/\{project\_id\}/configurations

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations

-   Parameter description

    **Table  1**  Parameter description

    <a name="table123563611337"></a>
    <table><thead align="left"><tr id="row113016363338"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p1230173613313"><a name="p1230173613313"></a><a name="p1230173613313"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.919999999999998%" id="mcps1.2.4.1.2"><p id="p230113364338"><a name="p230113364338"></a><a name="p230113364338"></a><strong id="b20690418533"><a name="b20690418533"></a><a name="b20690418533"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.870000000000005%" id="mcps1.2.4.1.3"><p id="p3301133619335"><a name="p3301133619335"></a><a name="p3301133619335"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row163012364332"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p6301163610337"><a name="p6301163610337"></a><a name="p6301163610337"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.919999999999998%" headers="mcps1.2.4.1.2 "><p id="p1330103618332"><a name="p1330103618332"></a><a name="p1330103618332"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.870000000000005%" headers="mcps1.2.4.1.3 "><p id="p4301163619338"><a name="p4301163619338"></a><a name="p4301163619338"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p3894155517518"><a name="p3894155517518"></a><a name="p3894155517518"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section351133623316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table17511836203310"></a>
    <table><thead align="left"><tr id="row7301103663317"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.1"><p id="p1930143633311"><a name="p1930143633311"></a><a name="p1930143633311"></a><strong id="b1885350880"><a name="b1885350880"></a><a name="b1885350880"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.57%" id="mcps1.2.5.1.2"><p id="p1301123673313"><a name="p1301123673313"></a><a name="p1301123673313"></a><strong id="b8743118831"><a name="b8743118831"></a><a name="b8743118831"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.72%" id="mcps1.2.5.1.3"><p id="p4301183613311"><a name="p4301183613311"></a><a name="p4301183613311"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.29%" id="mcps1.2.5.1.4"><p id="p1230183610335"><a name="p1230183610335"></a><a name="p1230183610335"></a><strong id="b1569990359"><a name="b1569990359"></a><a name="b1569990359"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17301143623312"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p8301173613330"><a name="p8301173613330"></a><a name="p8301173613330"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.57%" headers="mcps1.2.5.1.2 "><p id="p1030153617336"><a name="p1030153617336"></a><a name="p1030153617336"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.5.1.3 "><p id="p730103603311"><a name="p730103603311"></a><a name="p730103603311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.2.5.1.4 "><p id="p93011036133314"><a name="p93011036133314"></a><a name="p93011036133314"></a>Specifies the parameter template name. It contains a maximum of 64 characters and can contain only uppercase letters, lowercase letters, digits, hyphens (-), underscores (_), and periods (.).</p>
    </td>
    </tr>
    <tr id="row15301536113314"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p430115362338"><a name="p430115362338"></a><a name="p430115362338"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.57%" headers="mcps1.2.5.1.2 "><p id="p12301336113310"><a name="p12301336113310"></a><a name="p12301336113310"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.5.1.3 "><p id="p16301113663320"><a name="p16301113663320"></a><a name="p16301113663320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.2.5.1.4 "><p id="p14301143673311"><a name="p14301143673311"></a><a name="p14301143673311"></a>Specifies the parameter template description. It contains a maximum of 256 characters and cannot contain the following special characters: &gt;!&lt;"&amp;'= Its value is left blank by default.</p>
    </td>
    </tr>
    <tr id="row6301143613312"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p1530113362338"><a name="p1530113362338"></a><a name="p1530113362338"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.57%" headers="mcps1.2.5.1.2 "><p id="p930115361330"><a name="p930115361330"></a><a name="p930115361330"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.5.1.3 "><p id="p6301203614332"><a name="p6301203614332"></a><a name="p6301203614332"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.2.5.1.4 "><p id="p230183617332"><a name="p230183617332"></a><a name="p230183617332"></a>Specifies the parameter values defined by users based on the default parameter template. By default, the parameter values cannot be changed.</p>
    <p id="p145463318285"><a name="p145463318285"></a><a name="p145463318285"></a>For details, see <a href="#table766183663313">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row730183613339"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p530153673318"><a name="p530153673318"></a><a name="p530153673318"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.57%" headers="mcps1.2.5.1.2 "><p id="p153011036183311"><a name="p153011036183311"></a><a name="p153011036183311"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.5.1.3 "><p id="p15081927144517"><a name="p15081927144517"></a><a name="p15081927144517"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.2.5.1.4 "><p id="p123018362336"><a name="p123018362336"></a><a name="p123018362336"></a>Specifies the database object.</p>
    <p id="p1643815425284"><a name="p1643815425284"></a><a name="p1643815425284"></a>For details, see <a href="#table1266173643311">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  values field data structure description

    <a name="table766183663313"></a>
    <table><thead align="left"><tr id="row1430153614339"><th class="cellrowborder" valign="top" width="18.54185418541854%" id="mcps1.2.5.1.1"><p id="p113011936153317"><a name="p113011936153317"></a><a name="p113011936153317"></a><strong id="b1479878228"><a name="b1479878228"></a><a name="b1479878228"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.36233623362336%" id="mcps1.2.5.1.2"><p id="p113012361337"><a name="p113012361337"></a><a name="p113012361337"></a><strong id="b1859191817318"><a name="b1859191817318"></a><a name="b1859191817318"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.681668166816678%" id="mcps1.2.5.1.3"><p id="p530153613332"><a name="p530153613332"></a><a name="p530153613332"></a><strong id="b1825297063"><a name="b1825297063"></a><a name="b1825297063"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.5.1.4"><p id="p9301133643319"><a name="p9301133643319"></a><a name="p9301133643319"></a><strong id="b630539102"><a name="b630539102"></a><a name="b630539102"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row930193615337"><td class="cellrowborder" valign="top" width="18.54185418541854%" headers="mcps1.2.5.1.1 "><p id="p18301336113314"><a name="p18301336113314"></a><a name="p18301336113314"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.36233623362336%" headers="mcps1.2.5.1.2 "><p id="p15301163603319"><a name="p15301163603319"></a><a name="p15301163603319"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.681668166816678%" headers="mcps1.2.5.1.3 "><p id="p83011736193315"><a name="p83011736193315"></a><a name="p83011736193315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p1330112362336"><a name="p1330112362336"></a><a name="p1330112362336"></a>Specifies the parameter name. For example, in <strong id="b3367863672350"><a name="b3367863672350"></a><a name="b3367863672350"></a>"max_connections": "10"</strong>, the key is <strong id="b7337336272350"><a name="b7337336272350"></a><a name="b7337336272350"></a>max_connections</strong>. If <strong id="b84235270617255"><a name="b84235270617255"></a><a name="b84235270617255"></a>key</strong> is left blank, the parameter <strong id="b84235270617238"><a name="b84235270617238"></a><a name="b84235270617238"></a>value</strong> cannot be changed. If <strong id="b84235270617332"><a name="b84235270617332"></a><a name="b84235270617332"></a>key</strong> is not empty, the parameter <strong id="b84235270617341"><a name="b84235270617341"></a><a name="b84235270617341"></a>value</strong> cannot be empty, either.</p>
    </td>
    </tr>
    <tr id="row530119367339"><td class="cellrowborder" valign="top" width="18.54185418541854%" headers="mcps1.2.5.1.1 "><p id="p930117365330"><a name="p930117365330"></a><a name="p930117365330"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.36233623362336%" headers="mcps1.2.5.1.2 "><p id="p9301203616333"><a name="p9301203616333"></a><a name="p9301203616333"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.681668166816678%" headers="mcps1.2.5.1.3 "><p id="p530115365333"><a name="p530115365333"></a><a name="p530115365333"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p6301136153319"><a name="p6301136153319"></a><a name="p6301136153319"></a>Specifies the parameter value. For example, in <strong id="b12548790223511"><a name="b12548790223511"></a><a name="b12548790223511"></a>"max_connections": "10"</strong>, the value is <strong id="b144027762523511"><a name="b144027762523511"></a><a name="b144027762523511"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  datastore field data structure description

    <a name="table1266173643311"></a>
    <table><thead align="left"><tr id="row3301336193311"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.5.1.1"><p id="p1630183610339"><a name="p1630183610339"></a><a name="p1630183610339"></a><strong id="b754201691"><a name="b754201691"></a><a name="b754201691"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.5.1.2"><p id="p3301113653318"><a name="p3301113653318"></a><a name="p3301113653318"></a><strong id="b1593214181431"><a name="b1593214181431"></a><a name="b1593214181431"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.5.1.3"><p id="p1330133613334"><a name="p1330133613334"></a><a name="p1330133613334"></a><strong id="b1223697379"><a name="b1223697379"></a><a name="b1223697379"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.06%" id="mcps1.2.5.1.4"><p id="p1730133612333"><a name="p1730133612333"></a><a name="p1730133612333"></a><strong id="b1680521174"><a name="b1680521174"></a><a name="b1680521174"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row73014364337"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p2030115366339"><a name="p2030115366339"></a><a name="p2030115366339"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.5.1.2 "><p id="p113011436133311"><a name="p113011436133311"></a><a name="p113011436133311"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.5.1.3 "><p id="p203015366338"><a name="p203015366338"></a><a name="p203015366338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.06%" headers="mcps1.2.5.1.4 "><p id="p73014367334"><a name="p73014367334"></a><a name="p73014367334"></a>Specifies the DB engine. Its value can be any of the following and is case-insensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row103011436113312"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p1330117364336"><a name="p1330117364336"></a><a name="p1330117364336"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.5.1.2 "><p id="p14301736143320"><a name="p14301736143320"></a><a name="p14301736143320"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.5.1.3 "><p id="p16301336183317"><a name="p16301336183317"></a><a name="p16301336183317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.06%" headers="mcps1.2.5.1.4 "><div class="p" id="p230113683317"><a name="p230113683317"></a><a name="p230113683317"></a>Specifies the database version. For details, see <a href="#section380114515317">Constraints</a>. Example values:<a name="ul5781159126"></a><a name="ul5781159126"></a><ul id="ul5781159126"><li>MySQL: <strong id="b133491640135510"><a name="b133491640135510"></a><a name="b133491640135510"></a>5.7</strong></li><li>PostgreSQL: <strong id="b181110177562"><a name="b181110177562"></a><a name="b181110177562"></a>9.5</strong></li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
    	"name": "configuration_test",
    	"description": "configuration_test",
    	"values": {
    		"max_connections": "10",
    		"autocommit": "OFF"
    	},
    	"datastore": {
    		"type": "mysql",
    		"version": "5.6"
    	}
    }
    ```


## Response<a name="section169863617335"></a>

-   Normal response

    **Table  5**  Parameter description

    <a name="table1098153612338"></a>
    <table><thead align="left"><tr id="row13301123683314"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p193016363334"><a name="p193016363334"></a><a name="p193016363334"></a><strong id="b1451353403"><a name="b1451353403"></a><a name="b1451353403"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p113011236173313"><a name="p113011236173313"></a><a name="p113011236173313"></a><strong id="b1971680184"><a name="b1971680184"></a><a name="b1971680184"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p1130123603314"><a name="p1130123603314"></a><a name="p1130123603314"></a><strong id="b1564305697"><a name="b1564305697"></a><a name="b1564305697"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13301173623311"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p630112365335"><a name="p630112365335"></a><a name="p630112365335"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p91660415456"><a name="p91660415456"></a><a name="p91660415456"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p1830113615334"><a name="p1830113615334"></a><a name="p1830113615334"></a>Indicates the parameter template information.</p>
    <p id="p1847203118295"><a name="p1847203118295"></a><a name="p1847203118295"></a>For details, see <a href="#table1113193619337">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  configuration field data structure description

    <a name="table1113193619337"></a>
    <table><thead align="left"><tr id="row730173611331"><th class="cellrowborder" valign="top" width="24.93%" id="mcps1.2.4.1.1"><p id="p18301203614333"><a name="p18301203614333"></a><a name="p18301203614333"></a><strong id="b1716734955"><a name="b1716734955"></a><a name="b1716734955"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.06%" id="mcps1.2.4.1.2"><p id="p133016363335"><a name="p133016363335"></a><a name="p133016363335"></a><strong id="b781617305"><a name="b781617305"></a><a name="b781617305"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.01%" id="mcps1.2.4.1.3"><p id="p1330153663313"><a name="p1330153663313"></a><a name="p1330153663313"></a><strong id="b1427628121"><a name="b1427628121"></a><a name="b1427628121"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5301143663318"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p93019363335"><a name="p93019363335"></a><a name="p93019363335"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p93011336193312"><a name="p93011336193312"></a><a name="p93011336193312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p1130113369339"><a name="p1130113369339"></a><a name="p1130113369339"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row12301143693311"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p18301153693319"><a name="p18301153693319"></a><a name="p18301153693319"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p4301936123312"><a name="p4301936123312"></a><a name="p4301936123312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p83010363335"><a name="p83010363335"></a><a name="p83010363335"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row113011436133310"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p9301636133310"><a name="p9301636133310"></a><a name="p9301636133310"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p1301236193316"><a name="p1301236193316"></a><a name="p1301236193316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p8301836123310"><a name="p8301836123310"></a><a name="p8301836123310"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row8301636113311"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p1130193683312"><a name="p1130193683312"></a><a name="p1130193683312"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p19301163613314"><a name="p19301163613314"></a><a name="p19301163613314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p13011136133317"><a name="p13011136133317"></a><a name="p13011136133317"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row13301123653318"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p18301336173320"><a name="p18301336173320"></a><a name="p18301336173320"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p5301163619337"><a name="p5301163619337"></a><a name="p5301163619337"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p1030118366339"><a name="p1030118366339"></a><a name="p1030118366339"></a>Indicates the parameter template description.</p>
    </td>
    </tr>
    <tr id="row113012361333"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p20301113613317"><a name="p20301113613317"></a><a name="p20301113613317"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p10301336143320"><a name="p10301336143320"></a><a name="p10301336143320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p1830119360330"><a name="p1830119360330"></a><a name="p1830119360330"></a>Indicates the creation time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p930118363333"><a name="p930118363333"></a><a name="p930118363333"></a><strong id="b122399191738"><a name="b122399191738"></a><a name="b122399191738"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b72391219232"><a name="b72391219232"></a><a name="b72391219232"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row430123603317"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.4.1.1 "><p id="p13301236103319"><a name="p13301236103319"></a><a name="p13301236103319"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.06%" headers="mcps1.2.4.1.2 "><p id="p19301236123320"><a name="p19301236123320"></a><a name="p19301236123320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.01%" headers="mcps1.2.4.1.3 "><p id="p1301133613332"><a name="p1301133613332"></a><a name="p1301133613332"></a>Indicates the update time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p93019368337"><a name="p93019368337"></a><a name="p93019368337"></a><strong id="b1526111914312"><a name="b1526111914312"></a><a name="b1526111914312"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b2261151911316"><a name="b2261151911316"></a><a name="b2261151911316"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"configuration": {
    		"id": "463b4b58-d0e8-4e2b-9560-5dea4552fde9",
    		"name": "configuration_test",
    		"datastore_version_name": "5.6",
    		"datastore_name": "mysql",
    		"description": "configuration_test",
    		"created": "2017-04-09T08:27:56+0800",
    		"updated": "2017-04-09T08:27:56+0800"
    	}
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

