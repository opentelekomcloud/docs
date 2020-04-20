# Obtaining Specified DB Instance Specifications<a name="en-us_topic_0032347784"></a>

## Function<a name="section36902586"></a>

This API is used to obtain DB instance specifications of a specified specification ID.

## URI<a name="section63687823"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/flavors/\{flavorId\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table6918001"></a>
    <table><thead align="left"><tr id="row17531178"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p10739296"><a name="p10739296"></a><a name="p10739296"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.2"><p id="p64576684"><a name="p64576684"></a><a name="p64576684"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.24999999999999%" id="mcps1.2.4.1.3"><p id="p63328883"><a name="p63328883"></a><a name="p63328883"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29365919"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p29829272"><a name="p29829272"></a><a name="p29829272"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p251973"><a name="p251973"></a><a name="p251973"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p20409871"><a name="p20409871"></a><a name="p20409871"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row49471114"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p47737289"><a name="p47737289"></a><a name="p47737289"></a>flavorId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p41515225"><a name="p41515225"></a><a name="p41515225"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p7290082"><a name="p7290082"></a><a name="p7290082"></a>Specifies the specification ID compliant with the UUID format.</p>
    <p id="p51126387153724"><a name="p51126387153724"></a><a name="p51126387153724"></a>For details about how to obtain this parameter value, see <strong id="b842352706195521"><a name="b842352706195521"></a><a name="b842352706195521"></a>flavors.id</strong> in the response message in <a href="obtaining-all-db-instance-specifications.md">Obtaining All DB Instance Specifications</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36319496"></a>

None

## Normal Response<a name="section58440016"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table30427456"></a>
    <table><thead align="left"><tr id="row47542385"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.1"><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.689999999999998%" id="mcps1.2.4.1.2"><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10023380"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p6587426"><a name="p6587426"></a><a name="p6587426"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.689999999999998%" headers="mcps1.2.4.1.2 "><p id="p63819464"><a name="p63819464"></a><a name="p63819464"></a>List data structure. For details, see <a href="#table64140254">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p17946858"><a name="p17946858"></a><a name="p17946858"></a>Indicates the DB instance specifications information list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  flavor field data structure description

    <a name="table64140254"></a>
    <table><thead align="left"><tr id="row21591473"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p4078883"><a name="p4078883"></a><a name="p4078883"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.2"><p id="p61954093"><a name="p61954093"></a><a name="p61954093"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.43%" id="mcps1.2.4.1.3"><p id="p52225656"><a name="p52225656"></a><a name="p52225656"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2419756"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p61782511"><a name="p61782511"></a><a name="p61782511"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p38327532"><a name="p38327532"></a><a name="p38327532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p17522377"><a name="p17522377"></a><a name="p17522377"></a>Indicates the specification ID. Its value is unique.</p>
    </td>
    </tr>
    <tr id="row23483667"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p23128868"><a name="p23128868"></a><a name="p23128868"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p61498985"><a name="p61498985"></a><a name="p61498985"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p15361866"><a name="p15361866"></a><a name="p15361866"></a>Indicates the specification item name.</p>
    </td>
    </tr>
    <tr id="row4039073"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p58729529"><a name="p58729529"></a><a name="p58729529"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p59471393"><a name="p59471393"></a><a name="p59471393"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p52453505"><a name="p52453505"></a><a name="p52453505"></a>Indicates the memory size in megabytes (MB).</p>
    </td>
    </tr>
    <tr id="row51398059195617"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p6098035195618"><a name="p6098035195618"></a><a name="p6098035195618"></a>specCode</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p24178835195618"><a name="p24178835195618"></a><a name="p24178835195618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p12328599195618"><a name="p12328599195618"></a><a name="p12328599195618"></a>Indicates the resource specifications code.</p>
    <p id="p39382216112854"><a name="p39382216112854"></a><a name="p39382216112854"></a>Use <strong id="b842352706171033"><a name="b842352706171033"></a><a name="b842352706171033"></a>rds.mysql.m1.xlarge</strong> as an example.</p>
    <p id="p43848530195618"><a name="p43848530195618"></a><a name="p43848530195618"></a><strong id="b842352706163930"><a name="b842352706163930"></a><a name="b842352706163930"></a>rds</strong> indicates RDS, <strong id="b842352706163952"><a name="b842352706163952"></a><a name="b842352706163952"></a>mysql</strong> indicates the DB engine, and <strong id="b84235270616408"><a name="b84235270616408"></a><a name="b84235270616408"></a>m1.xlarge</strong> indicates the performance specification (large-memory). </p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "flavor": {
            "id": "f7f51f85-cfcd-4409-ae91-b3eae186d0ea",
            "name": "OTC_MYLM_XLARGE",
            "ram": 32768,
            "specCode": "rds.mysql.m1.xlarge"
        }
    }
    ```


## Abnormal Response<a name="section56198103"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

