# Obtaining a Parameter Template List<a name="rds_09_0301"></a>

## Function<a name="section81771062513"></a>

This API is used to obtain the parameter template list, including default parameter templates of all databases and those created by users.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section152364311313"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

## URI<a name="section017719022520"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{_project\_id_\}/configurations

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations

-   Parameter description

    **Table  1**  Parameter description

    <a name="table181941109258"></a>
    <table><thead align="left"><tr id="row849117017252"><th class="cellrowborder" valign="top" width="21.41%" id="mcps1.2.4.1.1"><p id="p54918042519"><a name="p54918042519"></a><a name="p54918042519"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.03%" id="mcps1.2.4.1.2"><p id="p34917019250"><a name="p34917019250"></a><a name="p34917019250"></a><strong id="b768912191038"><a name="b768912191038"></a><a name="b768912191038"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.559999999999995%" id="mcps1.2.4.1.3"><p id="p194916016259"><a name="p194916016259"></a><a name="p194916016259"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16491304255"><td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.2.4.1.1 "><p id="p949116015257"><a name="p949116015257"></a><a name="p949116015257"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.03%" headers="mcps1.2.4.1.2 "><p id="p949110162516"><a name="p949110162516"></a><a name="p949110162516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p149114012257"><a name="p149114012257"></a><a name="p149114012257"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p125591943105712"><a name="p125591943105712"></a><a name="p125591943105712"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section12251402259"></a>

None

## Response<a name="section52256012514"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table3225120142519"></a>
    <table><thead align="left"><tr id="row114911709259"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p74911403256"><a name="p74911403256"></a><a name="p74911403256"></a><strong id="b1427920811"><a name="b1427920811"></a><a name="b1427920811"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p5491110182515"><a name="p5491110182515"></a><a name="p5491110182515"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p164913016250"><a name="p164913016250"></a><a name="p164913016250"></a><strong id="b987321903"><a name="b987321903"></a><a name="b987321903"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13491305254"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p204917011259"><a name="p204917011259"></a><a name="p204917011259"></a>configurations</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p449110202513"><a name="p449110202513"></a><a name="p449110202513"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p449110182519"><a name="p449110182519"></a><a name="p449110182519"></a>Indicates the parameter template list.</p>
    <p id="p11880165913273"><a name="p11880165913273"></a><a name="p11880165913273"></a>For details, see <a href="#table1324110018258">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configurations field data structure description

    <a name="table1324110018258"></a>
    <table><thead align="left"><tr id="row124916013259"><th class="cellrowborder" valign="top" width="17.64%" id="mcps1.2.4.1.1"><p id="p64916052515"><a name="p64916052515"></a><a name="p64916052515"></a><strong id="b1429650437"><a name="b1429650437"></a><a name="b1429650437"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.669999999999998%" id="mcps1.2.4.1.2"><p id="p349170142515"><a name="p349170142515"></a><a name="p349170142515"></a><strong id="b2133935348"><a name="b2133935348"></a><a name="b2133935348"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.69%" id="mcps1.2.4.1.3"><p id="p94914092513"><a name="p94914092513"></a><a name="p94914092513"></a><strong id="b2145610042"><a name="b2145610042"></a><a name="b2145610042"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row94919018254"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p849112018256"><a name="p849112018256"></a><a name="p849112018256"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p104911706251"><a name="p104911706251"></a><a name="p104911706251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p34911304253"><a name="p34911304253"></a><a name="p34911304253"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row1549170182513"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p44910052510"><a name="p44910052510"></a><a name="p44910052510"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p749110017252"><a name="p749110017252"></a><a name="p749110017252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p144914015258"><a name="p144914015258"></a><a name="p144914015258"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row1749110019252"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p154912092512"><a name="p154912092512"></a><a name="p154912092512"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p849116016259"><a name="p849116016259"></a><a name="p849116016259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p1649115072512"><a name="p1649115072512"></a><a name="p1649115072512"></a>Indicates the parameter template description.</p>
    </td>
    </tr>
    <tr id="row1849119013256"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p24917022510"><a name="p24917022510"></a><a name="p24917022510"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p154361721193019"><a name="p154361721193019"></a><a name="p154361721193019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p549114022515"><a name="p549114022515"></a><a name="p549114022515"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row94917032517"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p1949118062513"><a name="p1949118062513"></a><a name="p1949118062513"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1629515220307"><a name="p1629515220307"></a><a name="p1629515220307"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p164911809250"><a name="p164911809250"></a><a name="p164911809250"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row849118015255"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p5491120122513"><a name="p5491120122513"></a><a name="p5491120122513"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1449113010256"><a name="p1449113010256"></a><a name="p1449113010256"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p249113012510"><a name="p249113012510"></a><a name="p249113012510"></a>Indicates the creation time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p6491190182519"><a name="p6491190182519"></a><a name="p6491190182519"></a><strong id="b108538191735"><a name="b108538191735"></a><a name="b108538191735"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b2853121914311"><a name="b2853121914311"></a><a name="b2853121914311"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row10491702259"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p1149115032510"><a name="p1149115032510"></a><a name="p1149115032510"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1749110142518"><a name="p1749110142518"></a><a name="p1749110142518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p1249180122519"><a name="p1249180122519"></a><a name="p1249180122519"></a>Indicates the update time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p0491502251"><a name="p0491502251"></a><a name="p0491502251"></a><strong id="b58747196319"><a name="b58747196319"></a><a name="b58747196319"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b118745191330"><a name="b118745191330"></a><a name="b118745191330"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row3491102258"><td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.1 "><p id="p74911022518"><a name="p74911022518"></a><a name="p74911022518"></a>user_defined</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p44913062511"><a name="p44913062511"></a><a name="p44913062511"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.69%" headers="mcps1.2.4.1.3 "><p id="p1149116052514"><a name="p1149116052514"></a><a name="p1149116052514"></a>Specifies whether the parameter template is created by users.</p>
    <a name="ul1649170142510"></a><a name="ul1649170142510"></a><ul id="ul1649170142510"><li><strong id="b842352706171054"><a name="b842352706171054"></a><a name="b842352706171054"></a>false</strong>: The parameter template is a default parameter template.</li><li><strong id="b235592260171138"><a name="b235592260171138"></a><a name="b235592260171138"></a>true</strong>: The parameter template is a custom template.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"configurations": [{
    			"id": "887ea0d1bb0843c49e8d8e5a09a95652pr01",
    			"name": "configuration_test",
    			"description": "configuration_test",
    			"datastore_version_name": "5.6",
    			"datastore_name": "mysql",
    			"created": "2019-05-15T11:53:34+0000",
    			"updated": "2019-05-15T11:53:34+0000",
    			"user_defined": true
    		},
    		{
    			"id": "3bc1e9cc0d34404b9225ed7a58fb284epr01",
    			"name": "Default-MySQL-5.7",
    			"description": "Default parameter group for MySQL 5.7",
    			"datastore_version_name": "5.7",
    			"datastore_name": "mysql",
    			"created": "2019-05-27T03:38:51+0000",
    			"updated": "2019-05-27T03:38:51+0000",
    			"user_defined": false
    		}
    	]
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

