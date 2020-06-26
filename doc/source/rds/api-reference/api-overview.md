# API Overview<a name="rds_00_0001"></a>

RDS provides extended APIs and OpenStack-compatible APIs. RDS APIs enable you to use all RDS functions, including creating DB instances, obtaining log information, and backing up and restoring data.

<a name="table1577981717153"></a>
<table><thead align="left"><tr id="row16810121712155"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p924014513320"><a name="p924014513320"></a><a name="p924014513320"></a><strong id="b842352706201211"><a name="b842352706201211"></a><a name="b842352706201211"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.1.4.1.2"><p id="p13834717131516"><a name="p13834717131516"></a><a name="p13834717131516"></a><strong id="b1045314595371"><a name="b1045314595371"></a><a name="b1045314595371"></a>Subtype</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.1.4.1.3"><p id="p3883151714159"><a name="p3883151714159"></a><a name="p3883151714159"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12121816153"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p11240184593319"><a name="p11240184593319"></a><a name="p11240184593319"></a>RDS APIs (v3)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p199557407427"><a name="p199557407427"></a><a name="p199557407427"></a>API Version Queries</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p218111811518"><a name="p218111811518"></a><a name="p218111811518"></a>Obtain API versions, including the API version list and API version information.</p>
</td>
</tr>
<tr id="row1980621151411"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p182401945173314"><a name="p182401945173314"></a><a name="p182401945173314"></a>RDS APIs (v3)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p78251715184011"><a name="p78251715184011"></a><a name="p78251715184011"></a>DB Instance Management</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p178077117141"><a name="p178077117141"></a><a name="p178077117141"></a>Manage DB instances, including creating a DB instance, adjusting instance storage space, rebooting a DB instance, deleting a DB instance, obtaining a DB instance list, and obtaining detailed information of a specified DB instance.</p>
</td>
</tr>
<tr id="row17941818161515"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p824084573314"><a name="p824084573314"></a><a name="p824084573314"></a>RDS APIs (v3)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p6465162615408"><a name="p6465162615408"></a><a name="p6465162615408"></a>Parameter Configuration</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p171171718191511"><a name="p171171718191511"></a><a name="p171171718191511"></a>Configure parameters, including obtaining a parameter list, obtaining configuration parameter information, obtaining default parameters of a DB instance, setting configuration parameters, restoring parameters to their default values, obtaining a parameter template list, and obtaining a parameter template.</p>
</td>
</tr>
<tr id="row1812216184153"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p2024010456336"><a name="p2024010456336"></a><a name="p2024010456336"></a>RDS APIs (v3)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p9609433114010"><a name="p9609433114010"></a><a name="p9609433114010"></a>Backup and Restoration</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p2136171815153"><a name="p2136171815153"></a><a name="p2136171815153"></a>Back up and restore data, including setting an automated backup policy, obtaining an automated backup policy, creating a manual backup, and deleting a manual backup.</p>
</td>
</tr>
<tr id="row124163311348"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p12240144510332"><a name="p12240144510332"></a><a name="p12240144510332"></a>RDS APIs (v3)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p1241911281457"><a name="p1241911281457"></a><a name="p1241911281457"></a>Specified Task Information Queries</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p19417143118418"><a name="p19417143118418"></a><a name="p19417143118418"></a>Obtain information about a specified task in the task center.</p>
</td>
</tr>
<tr id="row3289124610343"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p2290746173419"><a name="p2290746173419"></a><a name="p2290746173419"></a>Native OpenStack API</p>
<p id="p126917523518"><a name="p126917523518"></a><a name="p126917523518"></a></p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p1729011467344"><a name="p1729011467344"></a><a name="p1729011467344"></a>DB Instance Management</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p1774274275817"><a name="p1774274275817"></a><a name="p1774274275817"></a>Manage DB instances, including creating a DB instance, adjusting instance storage space, rebooting a DB instance, deleting a DB instance, obtaining a DB instance list, and obtaining detailed information of a specified DB instance.</p>
</td>
</tr>
<tr id="row76916543513"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p2375135751514"><a name="p2375135751514"></a><a name="p2375135751514"></a>Native OpenStack API</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p1969116516354"><a name="p1969116516354"></a><a name="p1969116516354"></a>Parameter Configuration</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p774834255815"><a name="p774834255815"></a><a name="p774834255815"></a>Configure parameters, including obtaining a parameter list, obtaining default parameters of a DB instance, and creating a parameter template.</p>
</td>
</tr>
<tr id="row11574117113812"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p295142117381"><a name="p295142117381"></a><a name="p295142117381"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p1779092317215"><a name="p1779092317215"></a><a name="p1779092317215"></a>API Version Queries</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p3795223427"><a name="p3795223427"></a><a name="p3795223427"></a>Obtain API versions, including the API version list and API version information.</p>
</td>
</tr>
<tr id="row3275182310319"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p1348116721516"><a name="p1348116721516"></a><a name="p1348116721516"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p527512231833"><a name="p527512231833"></a><a name="p527512231833"></a>Database Version Queries</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p1227562318317"><a name="p1227562318317"></a><a name="p1227562318317"></a>Obtain version information about a specified database type.</p>
</td>
</tr>
<tr id="row9435124114215"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p1122111812152"><a name="p1122111812152"></a><a name="p1122111812152"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p17323524114220"><a name="p17323524114220"></a><a name="p17323524114220"></a>DB Instance Management</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p1532492484211"><a name="p1532492484211"></a><a name="p1532492484211"></a>Manage DB instances, including creating a DB instance, adjusting instance storage space, rebooting a DB instance, deleting a DB instance, obtaining a DB instance list, and obtaining detailed information of a specified DB instance.</p>
</td>
</tr>
<tr id="row13431162413427"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p8269149161516"><a name="p8269149161516"></a><a name="p8269149161516"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p153319245428"><a name="p153319245428"></a><a name="p153319245428"></a>Parameter Configuration</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p103349243424"><a name="p103349243424"></a><a name="p103349243424"></a>Configure parameters, including obtaining a parameter list, obtaining configuration parameter information, obtaining default parameters of a DB instance, setting configuration parameters, restoring parameters to their default values, obtaining a parameter template list, and obtaining a parameter template.</p>
</td>
</tr>
<tr id="row194261124174212"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p18133161041520"><a name="p18133161041520"></a><a name="p18133161041520"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p113391324124215"><a name="p113391324124215"></a><a name="p113391324124215"></a>Backup and Restoration</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p7344112412426"><a name="p7344112412426"></a><a name="p7344112412426"></a>Back up and restore data, including setting an automated backup policy, obtaining an automated backup policy, creating a manual backup, and deleting a manual backup.</p>
</td>
</tr>
<tr id="row1442372417422"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p2448121191520"><a name="p2448121191520"></a><a name="p2448121191520"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p11351152415421"><a name="p11351152415421"></a><a name="p11351152415421"></a>Log Information Queries</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p1735382434216"><a name="p1735382434216"></a><a name="p1735382434216"></a>Obtain log information, including querying database error logs and querying database slow logs.</p>
</td>
</tr>
<tr id="row1541732464214"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p42150126154"><a name="p42150126154"></a><a name="p42150126154"></a>RDS APIs (v1)</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.2 "><p id="p12359424124219"><a name="p12359424124219"></a><a name="p12359424124219"></a>Tag Management</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p4363152454210"><a name="p4363152454210"></a><a name="p4363152454210"></a>Manage tags, including adding a tag, query a tag, and deleting a tag.</p>
</td>
</tr>
</tbody>
</table>

