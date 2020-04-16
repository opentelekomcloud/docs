# Obtaining Information About Configuration Parameters<a name="en-us_topic_0056890258"></a>

## Function<a name="section66864413102314"></a>

This API is used to obtain information about parameters that can be modified of a specified database version.

## URI<a name="section23121848102314"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/datastores/versions/\{datastore\_version\_id\}/parameters/\{parameter\_name\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table39260101102314"></a>
    <table><thead align="left"><tr id="row53407996102314"><th class="cellrowborder" valign="top" width="26.52%" id="mcps1.2.4.1.1"><p id="p31080435102314"><a name="p31080435102314"></a><a name="p31080435102314"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.97%" id="mcps1.2.4.1.2"><p id="p34487335102314"><a name="p34487335102314"></a><a name="p34487335102314"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.51%" id="mcps1.2.4.1.3"><p id="p42010751102314"><a name="p42010751102314"></a><a name="p42010751102314"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47427684102314"><td class="cellrowborder" valign="top" width="26.52%" headers="mcps1.2.4.1.1 "><p id="p16437181102314"><a name="p16437181102314"></a><a name="p16437181102314"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.97%" headers="mcps1.2.4.1.2 "><p id="p56343283102314"><a name="p56343283102314"></a><a name="p56343283102314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.51%" headers="mcps1.2.4.1.3 "><p id="p403181102314"><a name="p403181102314"></a><a name="p403181102314"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row3628631102314"><td class="cellrowborder" valign="top" width="26.52%" headers="mcps1.2.4.1.1 "><p id="p25483699102314"><a name="p25483699102314"></a><a name="p25483699102314"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.97%" headers="mcps1.2.4.1.2 "><p id="p50913735102314"><a name="p50913735102314"></a><a name="p50913735102314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.51%" headers="mcps1.2.4.1.3 "><p id="p30371900102314"><a name="p30371900102314"></a><a name="p30371900102314"></a>Specifies the database version ID (<strong id="b842352706195851"><a name="b842352706195851"></a><a name="b842352706195851"></a>dataStores.id</strong> in the response message in <a href="database-version-queries.md">Database Version Queries</a>).</p>
    </td>
    </tr>
    <tr id="row4911650102314"><td class="cellrowborder" valign="top" width="26.52%" headers="mcps1.2.4.1.1 "><p id="p62299403102314"><a name="p62299403102314"></a><a name="p62299403102314"></a>parameter_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.97%" headers="mcps1.2.4.1.2 "><p id="p13086888102314"><a name="p13086888102314"></a><a name="p13086888102314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.51%" headers="mcps1.2.4.1.3 "><p id="p53405026102314"><a name="p53405026102314"></a><a name="p53405026102314"></a>Specifies the parameter name.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section8775048102314"></a>

None

## Normal Response<a name="section21668289102314"></a>

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
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p36477460102154"><a name="p36477460102154"></a><a name="p36477460102154"></a>List data structure. For details, see <a href="#table29072240102314">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p16958334102154"><a name="p16958334102154"></a><a name="p16958334102154"></a>Indicates all the parameters that can be modified of the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration-parameters field data structure description

    <a name="table29072240102314"></a>
    <table><thead align="left"><tr id="row43813852102314"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p59261153102314"><a name="p59261153102314"></a><a name="p59261153102314"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p35424111102314"><a name="p35424111102314"></a><a name="p35424111102314"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p50780717102314"><a name="p50780717102314"></a><a name="p50780717102314"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19597379102314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43883866102314"><a name="p43883866102314"></a><a name="p43883866102314"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64932249102314"><a name="p64932249102314"></a><a name="p64932249102314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25020841102314"><a name="p25020841102314"></a><a name="p25020841102314"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row14456442104756"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4894496410489"><a name="p4894496410489"></a><a name="p4894496410489"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p511911110489"><a name="p511911110489"></a><a name="p511911110489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1199488410489"><a name="p1199488410489"></a><a name="p1199488410489"></a>Indicates the parameter type, which can be <strong id="b317172548174558"><a name="b317172548174558"></a><a name="b317172548174558"></a>integer</strong>, <strong id="b842352706174612"><a name="b842352706174612"></a><a name="b842352706174612"></a>string</strong>, <strong id="b842352706174617"><a name="b842352706174617"></a><a name="b842352706174617"></a>boolean</strong>, <strong id="b842352706171731"><a name="b842352706171731"></a><a name="b842352706171731"></a>list</strong>, or <strong id="b842352706171734"><a name="b842352706171734"></a><a name="b842352706171734"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row46156155104849"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1667921104856"><a name="p1667921104856"></a><a name="p1667921104856"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p883893104856"><a name="p883893104856"></a><a name="p883893104856"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4486502104856"><a name="p4486502104856"></a><a name="p4486502104856"></a>Indicates the maximum value of the parameter. Returned only when <strong id="b842352706153657_1"><a name="b842352706153657_1"></a><a name="b842352706153657_1"></a>type</strong> is <strong id="b84235270615371_1"><a name="b84235270615371_1"></a><a name="b84235270615371_1"></a>integer</strong> or <strong id="b49453009392846_1"><a name="b49453009392846_1"></a><a name="b49453009392846_1"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row23860983102314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p53691459102314"><a name="p53691459102314"></a><a name="p53691459102314"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p54040883102314"><a name="p54040883102314"></a><a name="p54040883102314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15235375102314"><a name="p15235375102314"></a><a name="p15235375102314"></a>Indicates the minimum value of the parameter. Returned only when <strong id="b842352706153657_3"><a name="b842352706153657_3"></a><a name="b842352706153657_3"></a>type</strong> is <strong id="b84235270615371_3"><a name="b84235270615371_3"></a><a name="b84235270615371_3"></a>integer</strong> or <strong id="b49453009392846_3"><a name="b49453009392846_3"></a><a name="b49453009392846_3"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row120052102314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9724214102314"><a name="p9724214102314"></a><a name="p9724214102314"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49463885102314"><a name="p49463885102314"></a><a name="p49463885102314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47151777102314"><a name="p47151777102314"></a><a name="p47151777102314"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    <tr id="row51576887104918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26569445104925"><a name="p26569445104925"></a><a name="p26569445104925"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4641419104925"><a name="p4641419104925"></a><a name="p4641419104925"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40410695104925"><a name="p40410695104925"></a><a name="p40410695104925"></a>Indicates whether the instance needs to reboot for the parameter to take effect. The value is <strong id="b842352706105121"><a name="b842352706105121"></a><a name="b842352706105121"></a>true</strong> or <strong id="b842352706105117"><a name="b842352706105117"></a><a name="b842352706105117"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
    "configuration-parameters": [
     {
       "name": "connect_timeout",
       "type": "integer",
       "max": "31536000",
       "min": "2",
       "datastore_version_id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61",
       "restart_required": "false"
      }
     ]
    }
    ```


## Abnormal Response<a name="section52760080102314"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

