# Obtaining Parameters in a Specified Parameter Template<a name="rds_09_0307"></a>

## Function<a name="section5782830193116"></a>

This API is used to obtain parameters of a specified parameter template.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section152364311313"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

## URI<a name="section27821830203110"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/configurations/\{config\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations/463b4b58-d0e8-4e2b-9560-5dea4552fde9

-   Parameter description

    **Table  1**  Parameter description

    <a name="table18782130193120"></a>
    <table><thead align="left"><tr id="row3985193020313"><th class="cellrowborder" valign="top" width="18.68%" id="mcps1.2.4.1.1"><p id="p498543073117"><a name="p498543073117"></a><a name="p498543073117"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.189999999999998%" id="mcps1.2.4.1.2"><p id="p19985203016315"><a name="p19985203016315"></a><a name="p19985203016315"></a><strong id="b4859193419013"><a name="b4859193419013"></a><a name="b4859193419013"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.13%" id="mcps1.2.4.1.3"><p id="p59850301315"><a name="p59850301315"></a><a name="p59850301315"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19985123013319"><td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.4.1.1 "><p id="p198514306315"><a name="p198514306315"></a><a name="p198514306315"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p2098523018318"><a name="p2098523018318"></a><a name="p2098523018318"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.13%" headers="mcps1.2.4.1.3 "><p id="p4985143012313"><a name="p4985143012313"></a><a name="p4985143012313"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p4574330362"><a name="p4574330362"></a><a name="p4574330362"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9985133018318"><td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.4.1.1 "><p id="p15985330173118"><a name="p15985330173118"></a><a name="p15985330173118"></a>config_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p19985530113119"><a name="p19985530113119"></a><a name="p19985530113119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.13%" headers="mcps1.2.4.1.3 "><p id="p12985163015311"><a name="p12985163015311"></a><a name="p12985163015311"></a>Specifies the parameter template ID.</p>
    <p id="p169856302315"><a name="p169856302315"></a><a name="p169856302315"></a>When this parameter is empty (not space), the URL of the parameter template list is obtained. For details, see <a href="obtaining-a-parameter-template-list.md">Obtaining a Parameter Template List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1579853020319"></a>

None

## Response<a name="section47981430203118"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table11813930113110"></a>
    <table><thead align="left"><tr id="row7985143017311"><th class="cellrowborder" valign="top" width="22.992299229922992%" id="mcps1.2.4.1.1"><p id="p6985203063120"><a name="p6985203063120"></a><a name="p6985203063120"></a><strong id="b1474399876"><a name="b1474399876"></a><a name="b1474399876"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.21332133213321%" id="mcps1.2.4.1.2"><p id="p798533073112"><a name="p798533073112"></a><a name="p798533073112"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.79437943794379%" id="mcps1.2.4.1.3"><p id="p1498593083118"><a name="p1498593083118"></a><a name="p1498593083118"></a><strong id="b1131643128"><a name="b1131643128"></a><a name="b1131643128"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2985193019314"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p29859308311"><a name="p29859308311"></a><a name="p29859308311"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p898543003115"><a name="p898543003115"></a><a name="p898543003115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p179856307312"><a name="p179856307312"></a><a name="p179856307312"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row298563013117"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p1098533063111"><a name="p1098533063111"></a><a name="p1098533063111"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p29855306312"><a name="p29855306312"></a><a name="p29855306312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p169851303312"><a name="p169851303312"></a><a name="p169851303312"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row17985103073115"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p12985130103115"><a name="p12985130103115"></a><a name="p12985130103115"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p1398503063118"><a name="p1398503063118"></a><a name="p1398503063118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p398511301312"><a name="p398511301312"></a><a name="p398511301312"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row69855304315"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p9985183033112"><a name="p9985183033112"></a><a name="p9985183033112"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p898583033110"><a name="p898583033110"></a><a name="p898583033110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p798519306319"><a name="p798519306319"></a><a name="p798519306319"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row151123173111"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p911931113119"><a name="p911931113119"></a><a name="p911931113119"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p6143113313"><a name="p6143113313"></a><a name="p6143113313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p13111312314"><a name="p13111312314"></a><a name="p13111312314"></a>Indicates the parameter template description.</p>
    </td>
    </tr>
    <tr id="row1011231173117"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p411131103118"><a name="p411131103118"></a><a name="p411131103118"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p1410316319"><a name="p1410316319"></a><a name="p1410316319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p151331103117"><a name="p151331103117"></a><a name="p151331103117"></a>Indicates the creation time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p5133143114"><a name="p5133143114"></a><a name="p5133143114"></a><strong id="b09222341509"><a name="b09222341509"></a><a name="b09222341509"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b19221034504"><a name="b19221034504"></a><a name="b19221034504"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row1311931103118"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p17163113113"><a name="p17163113113"></a><a name="p17163113113"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p201831203110"><a name="p201831203110"></a><a name="p201831203110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p81103193116"><a name="p81103193116"></a><a name="p81103193116"></a>Indicates the update time in the following format: yyyy-MM-ddTHH:mm:ssZ.</p>
    <p id="p211831173119"><a name="p211831173119"></a><a name="p211831173119"></a><strong id="b1193019341806"><a name="b1193019341806"></a><a name="b1193019341806"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b18930634104"><a name="b18930634104"></a><a name="b18930634104"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row71193183116"><td class="cellrowborder" valign="top" width="22.992299229922992%" headers="mcps1.2.4.1.1 "><p id="p31731193114"><a name="p31731193114"></a><a name="p31731193114"></a>configuration_parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.21332133213321%" headers="mcps1.2.4.1.2 "><p id="p295463213214"><a name="p295463213214"></a><a name="p295463213214"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.4.1.3 "><p id="p14115316313"><a name="p14115316313"></a><a name="p14115316313"></a>Indicates the parameters defined by users based on the default parameter templates.</p>
    <p id="p16101710385"><a name="p16101710385"></a><a name="p16101710385"></a>For details, see <a href="#table082923016312">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration\_parameters field data structure description

    <a name="table082923016312"></a>
    <table><thead align="left"><tr id="row21193111315"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p71203111314"><a name="p71203111314"></a><a name="p71203111314"></a><strong id="b1378187054"><a name="b1378187054"></a><a name="b1378187054"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p16111316315"><a name="p16111316315"></a><a name="p16111316315"></a><strong id="b818260000"><a name="b818260000"></a><a name="b818260000"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p111203123114"><a name="p111203123114"></a><a name="p111203123114"></a><strong id="b1954961654"><a name="b1954961654"></a><a name="b1954961654"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row111143115316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15193113119"><a name="p15193113119"></a><a name="p15193113119"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15133143116"><a name="p15133143116"></a><a name="p15133143116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1911631113116"><a name="p1911631113116"></a><a name="p1911631113116"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row21631123112"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41131113118"><a name="p41131113118"></a><a name="p41131113118"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3143163120"><a name="p3143163120"></a><a name="p3143163120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p101173163114"><a name="p101173163114"></a><a name="p101173163114"></a>Indicates the parameter value.</p>
    </td>
    </tr>
    <tr id="row181103123113"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1611531103116"><a name="p1611531103116"></a><a name="p1611531103116"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1173112316"><a name="p1173112316"></a><a name="p1173112316"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p912312316"><a name="p912312316"></a><a name="p912312316"></a>Indicates whether a restart is required.</p>
    <a name="ul5163173111"></a><a name="ul5163173111"></a><ul id="ul5163173111"><li><strong id="b842352706214352_1"><a name="b842352706214352_1"></a><a name="b842352706214352_1"></a>false</strong> indicates that a restart is not required.</li><li><strong id="b84235270621449_1"><a name="b84235270621449_1"></a><a name="b84235270621449_1"></a>true</strong> indicates that a restart is required.</li></ul>
    </td>
    </tr>
    <tr id="row19143133112"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61123173117"><a name="p61123173117"></a><a name="p61123173117"></a>readonly</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p01173117316"><a name="p01173117316"></a><a name="p01173117316"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p141531103113"><a name="p141531103113"></a><a name="p141531103113"></a>Indicates whether the parameter is read-only.</p>
    <a name="ul17119318311"></a><a name="ul17119318311"></a><ul id="ul17119318311"><li><strong id="b1411252830"><a name="b1411252830"></a><a name="b1411252830"></a>false</strong>: The parameter is not read-only.</li><li><strong id="b10906738997"><a name="b10906738997"></a><a name="b10906738997"></a>true</strong>: The parameter is read-only.</li></ul>
    </td>
    </tr>
    <tr id="row7123117315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1611431113120"><a name="p1611431113120"></a><a name="p1611431113120"></a>value_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p91131133112"><a name="p91131133112"></a><a name="p91131133112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16111312319"><a name="p16111312319"></a><a name="p16111312319"></a>Indicates the parameter value range. For example, the value of <strong id="b842352706163858"><a name="b842352706163858"></a><a name="b842352706163858"></a>integer</strong> is 0–1, and the value of <strong id="b842352706163915"><a name="b842352706163915"></a><a name="b842352706163915"></a>boolean</strong> is <strong id="b842352706163917"><a name="b842352706163917"></a><a name="b842352706163917"></a>true</strong> or <strong id="b842352706163919"><a name="b842352706163919"></a><a name="b842352706163919"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row13173119316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p411231173116"><a name="p411231173116"></a><a name="p411231173116"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41193103117"><a name="p41193103117"></a><a name="p41193103117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4120314313"><a name="p4120314313"></a><a name="p4120314313"></a>Indicates the parameter type, which can be <strong id="b317172548174558"><a name="b317172548174558"></a><a name="b317172548174558"></a>integer</strong>, <strong id="b842352706174612"><a name="b842352706174612"></a><a name="b842352706174612"></a>string</strong>, <strong id="b842352706174617"><a name="b842352706174617"></a><a name="b842352706174617"></a>boolean</strong>, <strong id="b842352706171731"><a name="b842352706171731"></a><a name="b842352706171731"></a>list</strong>, or <strong id="b842352706171734"><a name="b842352706171734"></a><a name="b842352706171734"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row161113143113"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1911312314"><a name="p1911312314"></a><a name="p1911312314"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17110317319"><a name="p17110317319"></a><a name="p17110317319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1215315318"><a name="p1215315318"></a><a name="p1215315318"></a>Indicates the parameter description.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    { 
        "id": "07fc12a8e0e94df7a3fcf53d0b5e1605pr01", 
        "name": "default-mysql-5.6", 
        "datastore_version_name": "5.6", 
        "datastore_name": "mysql", 
        "description": "Default parameter group for mysql 5.6", 
        "created": "2017-05-05T04:40:51+0800", 
        "updated": "2017-05-05T04:40:51+0800", 
        "configuration_parameters": [ 
          { 
            "name": "auto_increment_increment", 
            "value": "1", 
            "restart_required": false, 
            "readonly": true, 
            "value_range": "1-65535", 
            "type": "integer", 
            "description": "auto_increment_increment and auto_increment_offset are intended for use with master-to-master replication, and can be used to control the operation of AUTO_INCREMENT columns." 
          }, 
          { 
            "name": "autocommit", 
            "value": "ON", 
            "restart_required": false, 
            "readonly": true, 
            "value_range": "ON|OFF", 
            "type": "boolean", 
            "description": "The autocommit mode. If set to ON, all changes to a table take effect immediately. If set to OFF, you must use COMMIT to accept a transaction or ROLLBACK to cancel it. " 
          } 
        ] 
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

