# Obtaining Information About Configuration Parameters<a name="en-us_topic_0034943370"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain information about parameters that can be modified of a specified database version.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/datastores/versions/\{datastore\_version\_id\}/parameters/\{parameter\_name\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.86%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.86%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.86%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the database version ID (<strong id="b842352706195851"><a name="b842352706195851"></a><a name="b842352706195851"></a>dataStores.id</strong> in the response message in <a href="database-version-queries.md">Database Version Queries</a>).</p>
    </td>
    </tr>
    <tr id="row2966082217239"><td class="cellrowborder" valign="top" width="21.86%" headers="mcps1.2.4.1.1 "><p id="p5371637317239"><a name="p5371637317239"></a><a name="p5371637317239"></a>parameter_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p5605898117239"><a name="p5605898117239"></a><a name="p5605898117239"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p4448363017239"><a name="p4448363017239"></a><a name="p4448363017239"></a>Specifies the parameter name.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table34207804"></a>
    <table><thead align="left"><tr id="row41360766"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.2%" id="mcps1.2.4.1.2"><p id="p46853302"><a name="p46853302"></a><a name="p46853302"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.47%" id="mcps1.2.4.1.3"><p id="p37021121"><a name="p37021121"></a><a name="p37021121"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45920800"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p45484399163245"><a name="p45484399163245"></a><a name="p45484399163245"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p60357736163245"><a name="p60357736163245"></a><a name="p60357736163245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p57138453163245"><a name="p57138453163245"></a><a name="p57138453163245"></a>Indicates the parameter name.</p>
    </td>
    </tr>
    <tr id="row49204239"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p26120409"><a name="p26120409"></a><a name="p26120409"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p35378404"><a name="p35378404"></a><a name="p35378404"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p47078488"><a name="p47078488"></a><a name="p47078488"></a>Indicates the minimum value of the parameter. Returned only when <strong id="b842352706153657_1"><a name="b842352706153657_1"></a><a name="b842352706153657_1"></a>type</strong> is <strong id="b84235270615371_1"><a name="b84235270615371_1"></a><a name="b84235270615371_1"></a>integer</strong> or <strong id="b84235270692829"><a name="b84235270692829"></a><a name="b84235270692829"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row21053208"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p27588283"><a name="p27588283"></a><a name="p27588283"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p20058459"><a name="p20058459"></a><a name="p20058459"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p14122463"><a name="p14122463"></a><a name="p14122463"></a>Indicates the maximum value of the parameter. Returned only when <strong id="b842352706153657_3"><a name="b842352706153657_3"></a><a name="b842352706153657_3"></a>type</strong> is <strong id="b84235270615371_3"><a name="b84235270615371_3"></a><a name="b84235270615371_3"></a>integer</strong> or <strong id="b49453009392846"><a name="b49453009392846"></a><a name="b49453009392846"></a>float</strong>.</p>
    </td>
    </tr>
    <tr id="row23955898163837"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p14276497163837"><a name="p14276497163837"></a><a name="p14276497163837"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p15545572163837"><a name="p15545572163837"></a><a name="p15545572163837"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p51231857163837"><a name="p51231857163837"></a><a name="p51231857163837"></a>Indicates whether the instance needs to reboot for the parameter to take effect. The value is <strong id="b842352706105121"><a name="b842352706105121"></a><a name="b842352706105121"></a>true</strong> or <strong id="b842352706105117"><a name="b842352706105117"></a><a name="b842352706105117"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row66492344163847"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p61560188163847"><a name="p61560188163847"></a><a name="p61560188163847"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p20319368163847"><a name="p20319368163847"></a><a name="p20319368163847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p235445291837"><a name="p235445291837"></a><a name="p235445291837"></a>Indicates the parameter type. The value can be <strong id="b84235270620120"><a name="b84235270620120"></a><a name="b84235270620120"></a>integer</strong>, <strong id="b84235270620129"><a name="b84235270620129"></a><a name="b84235270620129"></a>string</strong>, <strong id="b842352706201217"><a name="b842352706201217"></a><a name="b842352706201217"></a>boolean</strong>, <strong id="b842352706201226"><a name="b842352706201226"></a><a name="b842352706201226"></a>float</strong>, or <strong id="b842352706201235"><a name="b842352706201235"></a><a name="b842352706201235"></a>list</strong>.</p>
    </td>
    </tr>
    <tr id="row56101210165444"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p35148844165444"><a name="p35148844165444"></a><a name="p35148844165444"></a>value_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p28484120165444"><a name="p28484120165444"></a><a name="p28484120165444"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p35363391145846"><a name="p35363391145846"></a><a name="p35363391145846"></a>Specifies the parameter value range and enumerated value.</p>
    </td>
    </tr>
    <tr id="row2371826316552"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p1213778316552"><a name="p1213778316552"></a><a name="p1213778316552"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p4363632916552"><a name="p4363632916552"></a><a name="p4363632916552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p4488177616552"><a name="p4488177616552"></a><a name="p4488177616552"></a>Indicates the parameter description.</p>
    </td>
    </tr>
    <tr id="row19561357163847"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p41834487163847"><a name="p41834487163847"></a><a name="p41834487163847"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p33150314163847"><a name="p33150314163847"></a><a name="p33150314163847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.47%" headers="mcps1.2.4.1.3 "><p id="p820893163847"><a name="p820893163847"></a><a name="p820893163847"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "name": "connect_timeout",
        "min": "2",
        "max": "31536000",
        "restart_required": false,
        "type": "integer",
        "value_range": "2-31536000",
        "description": " Number of seconds that the mysqld server waits for a connect packet before responding with "Bad handshake".
        "datastore_version_id": "f8e67741-e767-4137-b394-3fb8a3fafd2f"
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

