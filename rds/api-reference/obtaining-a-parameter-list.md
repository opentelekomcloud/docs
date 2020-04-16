# Obtaining a Parameter List<a name="en-us_topic_0034943369"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain all the parameters that can be modified of the current database version.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/datastores/versions/\{datastore\_version\_id\}/parameters

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.439999999999998%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p48030001163437"><a name="p48030001163437"></a><a name="p48030001163437"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the database version ID (<strong id="b842352706195851"><a name="b842352706195851"></a><a name="b842352706195851"></a>dataStores.id</strong> in the response message in <a href="database-version-queries.md">Database Version Queries</a>).</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.26%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2456979"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>configuration-parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.26%" headers="mcps1.2.4.1.2 "><p id="p14114947"><a name="p14114947"></a><a name="p14114947"></a>List data structure. For details, see <a href="#table34207804">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p22140377"><a name="p22140377"></a><a name="p22140377"></a>Indicates all the parameters that can be modified of the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration-parameters field data structure description

    <a name="table34207804"></a>
    <table><thead align="left"><tr id="row41360766"><th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.4.1.1"><p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.2"><p id="p46853302"><a name="p46853302"></a><a name="p46853302"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p37021121"><a name="p37021121"></a><a name="p37021121"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45920800"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p45484399163245"><a name="p45484399163245"></a><a name="p45484399163245"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p60357736163245"><a name="p60357736163245"></a><a name="p60357736163245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p57138453163245"><a name="p57138453163245"></a><a name="p57138453163245"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row49204239"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p26120409"><a name="p26120409"></a><a name="p26120409"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p35378404"><a name="p35378404"></a><a name="p35378404"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p47078488"><a name="p47078488"></a><a name="p47078488"></a>Indicates the minimum value. Returned only when <strong id="b842352706153531"><a name="b842352706153531"></a><a name="b842352706153531"></a>type</strong> is <strong id="b842352706153537"><a name="b842352706153537"></a><a name="b842352706153537"></a>integer</strong> or <strong id="b84235270692552"><a name="b84235270692552"></a><a name="b84235270692552"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row21053208"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p27588283"><a name="p27588283"></a><a name="p27588283"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p20058459"><a name="p20058459"></a><a name="p20058459"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p14122463"><a name="p14122463"></a><a name="p14122463"></a>Indicates the maximum value. Returned only when <strong id="b842352706153556"><a name="b842352706153556"></a><a name="b842352706153556"></a>type</strong> is <strong id="b842352706153319"><a name="b842352706153319"></a><a name="b842352706153319"></a>integer</strong> or <strong id="b119659312492627"><a name="b119659312492627"></a><a name="b119659312492627"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row66492344163847"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p61560188163847"><a name="p61560188163847"></a><a name="p61560188163847"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p20319368163847"><a name="p20319368163847"></a><a name="p20319368163847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p35256079163847"><a name="p35256079163847"></a><a name="p35256079163847"></a>Indicates the parameter type. The value can be <strong id="b84235270620120"><a name="b84235270620120"></a><a name="b84235270620120"></a>integer</strong>, <strong id="b84235270620129"><a name="b84235270620129"></a><a name="b84235270620129"></a>string</strong>, <strong id="b842352706201217"><a name="b842352706201217"></a><a name="b842352706201217"></a>boolean</strong>, <strong id="b842352706201226"><a name="b842352706201226"></a><a name="b842352706201226"></a>float</strong>, or <strong id="b842352706201235"><a name="b842352706201235"></a><a name="b842352706201235"></a>list</strong>.</p>
    </td>
    </tr>
    <tr id="row18311707165752"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p7200466165951"><a name="p7200466165951"></a><a name="p7200466165951"></a>value_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p14648596165951"><a name="p14648596165951"></a><a name="p14648596165951"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p45685652165951"><a name="p45685652165951"></a><a name="p45685652165951"></a>Specifies the parameter value range and enumerated value.</p>
    </td>
    </tr>
    <tr id="row24783327165741"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p18844278165951"><a name="p18844278165951"></a><a name="p18844278165951"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p47270407165951"><a name="p47270407165951"></a><a name="p47270407165951"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p3697753165951"><a name="p3697753165951"></a><a name="p3697753165951"></a>Indicates the parameter description.</p>
    </td>
    </tr>
    <tr id="row3494747312729"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p6084539712735"><a name="p6084539712735"></a><a name="p6084539712735"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p2953011612735"><a name="p2953011612735"></a><a name="p2953011612735"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p4312922012735"><a name="p4312922012735"></a><a name="p4312922012735"></a>Indicates whether the instance needs to reboot for the parameter to take effect. The value is <strong id="b842352706105121"><a name="b842352706105121"></a><a name="b842352706105121"></a>true</strong> or <strong id="b842352706105117"><a name="b842352706105117"></a><a name="b842352706105117"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row19561357163847"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p41834487163847"><a name="p41834487163847"></a><a name="p41834487163847"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p33150314163847"><a name="p33150314163847"></a><a name="p33150314163847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p820893163847"><a name="p820893163847"></a><a name="p820893163847"></a>Indicates the database version ID.</p>
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
        "value_range" : "ON|OFF",
        "description" : "The autocommit mode. If set to ON, all changes to a table take effect immediately. If set to OFF, you must use COMMIT to accept a transaction or ROLLBACK to cancel it. ",
        "restart_required" : false,
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
      }, {
        "name" : "auto_increment_increment",
        "min" : "1",
        "max" : "65535",
        "type" : "integer",
        "value_range": "1-65535",
        "description" : "auto_increment_increment and auto_increment_offset are intended for use with master-to-master replication, and can be used to control the operation of AUTO_INCREMENT columns.",
        "restart_required" : false,
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
      }, {
        "name" : "auto_increment_offset",
        "min" : "1",
        "max" : "65535",
        "type" : "integer",
        "value_range": "1-65535",
        "description" : "auto_increment_increment and auto_increment_offset are intended for use with master-to-master replication, and can be used to control the operation of AUTO_INCREMENT columns. ",
        "restart_required" : false,
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
      }, {
        "name" : "back_log",
        "min" : "1",
        "max" : "65535",
        "type" : "integer",
        "value_range": "1-65535",
        "description" : "The number of outstanding connection requests MySQL can have. This comes into play when the main MySQL thread gets very many connection requests in a very short time. It then takes some time (although very little) for the main thread to check the connection and start a new thread. The back_log value indicates how many requests can be stacked during this short time before MySQL momentarily stops answering new requests. The default value depends on system architecture.",
        "restart_required" : true,
        "datastore_version_id" : "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
        }
      ]
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

