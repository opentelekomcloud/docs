# Obtaining All DB Instance Specifications<a name="en-us_topic_0032347783"></a>

## Function<a name="section25483595"></a>

This API is used to obtain all instance specifications of a specified database version ID in a specified region.

## URI<a name="section28025763"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/flavors

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.67%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.51%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.82%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.51%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.82%" headers="mcps1.2.4.1.3 "><p id="p11677197163722"><a name="p11677197163722"></a><a name="p11677197163722"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50905282"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table50945089161848"></a>
    <table><thead align="left"><tr id="row57468408161848"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p24429446161848"><a name="p24429446161848"></a><a name="p24429446161848"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.500000000000004%" id="mcps1.2.4.1.2"><p id="p32628076161848"><a name="p32628076161848"></a><a name="p32628076161848"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p25628499161848"><a name="p25628499161848"></a><a name="p25628499161848"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62642530161848"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p40880194161848"><a name="p40880194161848"></a><a name="p40880194161848"></a>dbId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.4.1.2 "><p id="p22961435161848"><a name="p22961435161848"></a><a name="p22961435161848"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p47936916161848"><a name="p47936916161848"></a><a name="p47936916161848"></a>Specifies the database version ID (<strong id="b842352706195346"><a name="b842352706195346"></a><a name="b842352706195346"></a>dataStores.id</strong> in the response message in <a href="database-version-queries.md">Database Version Queries</a>).</p>
    <p id="p57684949161848"><a name="p57684949161848"></a><a name="p57684949161848"></a>Valid value: The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row49402496161848"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p42179265161848"><a name="p42179265161848"></a><a name="p42179265161848"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.4.1.2 "><p id="p61077343161848"><a name="p61077343161848"></a><a name="p61077343161848"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p48317761161848"><a name="p48317761161848"></a><a name="p48317761161848"></a>Specifies the region where the DB instance is deployed.</p>
    <p id="p1715661014187"><a name="p1715661014187"></a><a name="p1715661014187"></a>Valid value:</p>
    <p id="p3825082612023"><a name="p3825082612023"></a><a name="p3825082612023"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    /rds/v1/375d8d8fad1f43039e23d3b6c0f60a19/flavors?dbId=e8a8b8cc-63f8-4fb5-8d4a-24c502317a6&region=eu-de
    ```


## Normal Response<a name="section55494360"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.71%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.18%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2456979"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p64797609"><a name="p64797609"></a><a name="p64797609"></a>flavors</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.2 "><p id="p14114947"><a name="p14114947"></a><a name="p14114947"></a>List data structure. For details, see <a href="#table34207804">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18%" headers="mcps1.2.4.1.3 "><p id="p22140377"><a name="p22140377"></a><a name="p22140377"></a>Indicates the DB instance specifications information list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  flavors field data structure description

    <a name="table34207804"></a>
    <table><thead align="left"><tr id="row41360766"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.52%" id="mcps1.2.4.1.2"><p id="p46853302"><a name="p46853302"></a><a name="p46853302"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.61%" id="mcps1.2.4.1.3"><p id="p37021121"><a name="p37021121"></a><a name="p37021121"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45920800"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p28597308"><a name="p28597308"></a><a name="p28597308"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.2 "><p id="p34680572"><a name="p34680572"></a><a name="p34680572"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.61%" headers="mcps1.2.4.1.3 "><p id="p57662920"><a name="p57662920"></a><a name="p57662920"></a>Indicates the specification ID. Its value is unique.</p>
    </td>
    </tr>
    <tr id="row49204239"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p26120409"><a name="p26120409"></a><a name="p26120409"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.2 "><p id="p35378404"><a name="p35378404"></a><a name="p35378404"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.61%" headers="mcps1.2.4.1.3 "><p id="p47078488"><a name="p47078488"></a><a name="p47078488"></a>Indicates the specification item name.</p>
    </td>
    </tr>
    <tr id="row21053208"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p27588283"><a name="p27588283"></a><a name="p27588283"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.2 "><p id="p20058459"><a name="p20058459"></a><a name="p20058459"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.61%" headers="mcps1.2.4.1.3 "><p id="p14122463"><a name="p14122463"></a><a name="p14122463"></a>Indicates the memory size in megabytes (MB).</p>
    </td>
    </tr>
    <tr id="row5478338319340"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p32176836193428"><a name="p32176836193428"></a><a name="p32176836193428"></a>specCode</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.2 "><p id="p731283419340"><a name="p731283419340"></a><a name="p731283419340"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.61%" headers="mcps1.2.4.1.3 "><p id="p12328599195618"><a name="p12328599195618"></a><a name="p12328599195618"></a>Indicates the resource specification code.</p>
    <p id="p39382216112854"><a name="p39382216112854"></a><a name="p39382216112854"></a>Use <strong id="b842352706171033"><a name="b842352706171033"></a><a name="b842352706171033"></a>rds.mysql.m1.xlarge</strong> as an example.</p>
    <p id="p43848530195618"><a name="p43848530195618"></a><a name="p43848530195618"></a><strong id="b842352706163930"><a name="b842352706163930"></a><a name="b842352706163930"></a>rds</strong> indicates RDS, <strong id="b842352706163952"><a name="b842352706163952"></a><a name="b842352706163952"></a>mysql</strong> indicates the DB engine, and <strong id="b84235270616408"><a name="b84235270616408"></a><a name="b84235270616408"></a>m1.xlarge</strong> indicates the performance specification (large-memory). </p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "flavors": [
            {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
                "name": "OTC_MYHP_LARGE",
                "ram": 4096,
                "specCode": "rds.mysql.c2.large"
            },
            {
                "id": "f7f51f85-cfcd-4409-ae91-b3eae186d0ea",
                "name": "OTC_MYLM_XLARGE",
                "ram": 32768,
                "specCode": "rds.mysql.m1.xlarge"
            }
        ]
    }
    ```


## Abnormal Response<a name="section29687198"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

