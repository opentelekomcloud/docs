# Obtaining a Parameter List<a name="en-us_topic_0056890257"></a>

## Function<a name="section6944811102154"></a>

This API is used to obtain all the parameters that can be modified of the current database version.

## URI<a name="section29602910102154"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/datastores/versions/\{datastore\_version\_id\}/parameters

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table30967278102154"></a>
    <table><thead align="left"><tr id="row27696912102154"><th class="cellrowborder" valign="top" width="25.759999999999998%" id="mcps1.2.4.1.1"><p id="p28857385102154"><a name="p28857385102154"></a><a name="p28857385102154"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.97%" id="mcps1.2.4.1.2"><p id="p55746847102154"><a name="p55746847102154"></a><a name="p55746847102154"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.269999999999996%" id="mcps1.2.4.1.3"><p id="p19200729102154"><a name="p19200729102154"></a><a name="p19200729102154"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11755199102154"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p12647099102154"><a name="p12647099102154"></a><a name="p12647099102154"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.97%" headers="mcps1.2.4.1.2 "><p id="p17782066102154"><a name="p17782066102154"></a><a name="p17782066102154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p31061262102154"><a name="p31061262102154"></a><a name="p31061262102154"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row11115910102154"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p27973492102154"><a name="p27973492102154"></a><a name="p27973492102154"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.97%" headers="mcps1.2.4.1.2 "><p id="p51260346102154"><a name="p51260346102154"></a><a name="p51260346102154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p58447361102154"><a name="p58447361102154"></a><a name="p58447361102154"></a>Specifies the database version ID (<strong id="b842352706195851"><a name="b842352706195851"></a><a name="b842352706195851"></a>dataStores.id</strong> in the response message in <a href="database-version-queries.md">Database Version Queries</a>).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section1633976102154"></a>

None

## Normal Response<a name="section50318295102154"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table29836925102154"></a>
    <table><thead align="left"><tr id="row8341487102154"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p4571867102154"><a name="p4571867102154"></a><a name="p4571867102154"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p34776980102154"><a name="p34776980102154"></a><a name="p34776980102154"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p65472001102154"><a name="p65472001102154"></a><a name="p65472001102154"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1631883102154"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p65073689102154"><a name="p65073689102154"></a><a name="p65073689102154"></a>configuration-parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p36477460102154"><a name="p36477460102154"></a><a name="p36477460102154"></a>List data structure. For details, see <a href="#table31447783102154">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p16958334102154"><a name="p16958334102154"></a><a name="p16958334102154"></a>Indicates all the parameters that can be modified of the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration-parameters field data structure description

    <a name="table31447783102154"></a>
    <table><thead align="left"><tr id="row57162906102154"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p66792684102154"><a name="p66792684102154"></a><a name="p66792684102154"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p41498347102154"><a name="p41498347102154"></a><a name="p41498347102154"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5922942102154"><a name="p5922942102154"></a><a name="p5922942102154"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9996302102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4394114102154"><a name="p4394114102154"></a><a name="p4394114102154"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20378947102154"><a name="p20378947102154"></a><a name="p20378947102154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40081976102154"><a name="p40081976102154"></a><a name="p40081976102154"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row25193465102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27404824102154"><a name="p27404824102154"></a><a name="p27404824102154"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5198304102154"><a name="p5198304102154"></a><a name="p5198304102154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18409464102154"><a name="p18409464102154"></a><a name="p18409464102154"></a>Indicates the minimum value. Returned only when <strong id="b842352706153531"><a name="b842352706153531"></a><a name="b842352706153531"></a>type</strong> is <strong id="b842352706153537"><a name="b842352706153537"></a><a name="b842352706153537"></a>integer</strong> or <strong id="b84235270692552"><a name="b84235270692552"></a><a name="b84235270692552"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row31467449102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p65835469102154"><a name="p65835469102154"></a><a name="p65835469102154"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31072773102154"><a name="p31072773102154"></a><a name="p31072773102154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33866698102154"><a name="p33866698102154"></a><a name="p33866698102154"></a>Indicates the maximum value. Returned only when <strong id="b842352706153556"><a name="b842352706153556"></a><a name="b842352706153556"></a>type</strong> is <strong id="b842352706153319"><a name="b842352706153319"></a><a name="b842352706153319"></a>integer</strong> or <strong id="b119659312492627"><a name="b119659312492627"></a><a name="b119659312492627"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row36364828102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59869983102154"><a name="p59869983102154"></a><a name="p59869983102154"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17630434102154"><a name="p17630434102154"></a><a name="p17630434102154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18779021102154"><a name="p18779021102154"></a><a name="p18779021102154"></a>Indicates the parameter type, which can be <strong id="b317172548174558"><a name="b317172548174558"></a><a name="b317172548174558"></a>integer</strong>, <strong id="b842352706174612"><a name="b842352706174612"></a><a name="b842352706174612"></a>string</strong>, <strong id="b842352706174617"><a name="b842352706174617"></a><a name="b842352706174617"></a>boolean</strong>, <strong id="b842352706171731"><a name="b842352706171731"></a><a name="b842352706171731"></a>list</strong>, or <strong id="b842352706171734"><a name="b842352706171734"></a><a name="b842352706171734"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row34793465102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66807317102154"><a name="p66807317102154"></a><a name="p66807317102154"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42683564102154"><a name="p42683564102154"></a><a name="p42683564102154"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34816680102154"><a name="p34816680102154"></a><a name="p34816680102154"></a>Indicates whether the instance needs to reboot for the parameter to take effect. The value is <strong id="b842352706105121"><a name="b842352706105121"></a><a name="b842352706105121"></a>true</strong> or <strong id="b842352706105117"><a name="b842352706105117"></a><a name="b842352706105117"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row44914672102154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14209790102154"><a name="p14209790102154"></a><a name="p14209790102154"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10142308102154"><a name="p10142308102154"></a><a name="p10142308102154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16220619102154"><a name="p16220619102154"></a><a name="p16220619102154"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    { 
      "configuration-parameters" : [ { 
        "name" : "autocommit", 
        "type" : "boolean", 
        "restart_required" : false, 
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61" 
      }, { 
        "name" : "auto_increment_increment", 
        "min" : "1", 
        "max" : "65535", 
        "type" : "integer", 
        "restart_required" : false, 
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61" 
      }, { 
        "name" : "auto_increment_offset", 
        "min" : "1", 
        "max" : "65535", 
        "type" : "integer", 
        "restart_required" : false, 
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61" 
      }, { 
        "name" : "back_log", 
        "min" : "1", 
        "max" : "65535", 
        "type" : "integer", 
        "restart_required" : true, 
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61" 
        } ] 
    }
    ```


## Abnormal Response<a name="section33647504102154"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

