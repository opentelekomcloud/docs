# Creating a DB Instance<a name="en-us_topic_0056889804"></a>

## Function<a name="section4284989"></a>

This API is used to create a single RDS DB instance or a read replica.

## URI<a name="section38564907"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.46000000000001%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.46000000000001%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section5589818810531"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table6209466312442"></a>
    <table><thead align="left"><tr id="row6512234412442"><th class="cellrowborder" valign="top" width="21.307869213078693%" id="mcps1.2.4.1.1"><p id="p4041853012442"><a name="p4041853012442"></a><a name="p4041853012442"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.44715528447155%" id="mcps1.2.4.1.2"><p id="p5267548812442"><a name="p5267548812442"></a><a name="p5267548812442"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.24497550244975%" id="mcps1.2.4.1.3"><p id="p3885613912442"><a name="p3885613912442"></a><a name="p3885613912442"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6033953012442"><td class="cellrowborder" valign="top" width="21.307869213078693%" headers="mcps1.2.4.1.1 "><p id="p5566375012442"><a name="p5566375012442"></a><a name="p5566375012442"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.44715528447155%" headers="mcps1.2.4.1.2 "><p id="p5287375317633"><a name="p5287375317633"></a><a name="p5287375317633"></a>Dictionary data structure.</p>
    <p id="p1246986212442"><a name="p1246986212442"></a><a name="p1246986212442"></a>For details on the field description when creating a single DB instance, see <a href="#table11236435">Table 3</a>.</p>
    <p id="p590235817628"><a name="p590235817628"></a><a name="p590235817628"></a>For details on the field description when creating a read replica, see <a href="#table32692621183156">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24497550244975%" headers="mcps1.2.4.1.3 "><p id="p48757463124544"><a name="p48757463124544"></a><a name="p48757463124544"></a>Specifies the detailed DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instance field data structure \(creating a single DB instance\)

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.119999999999997%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.89%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61715939182217"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p31636595182226"><a name="p31636595182226"></a><a name="p31636595182226"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p12427415182226"><a name="p12427415182226"></a><a name="p12427415182226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p67096522182226"><a name="p67096522182226"></a><a name="p67096522182226"></a>Dictionary data structure. For details, see <a href="#table1282893518295">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58112242182226"><a name="p58112242182226"></a><a name="p58112242182226"></a>Specifies the database information.</p>
    </td>
    </tr>
    <tr id="row60827539"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p23411412333"><a name="p23411412333"></a><a name="p23411412333"></a>Specifies the DB instance name.</p>
    <p id="p463314503337"><a name="p463314503337"></a><a name="p463314503337"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Valid value:</p>
    <p id="p49586916144357"><a name="p49586916144357"></a><a name="p49586916144357"></a>The value must be 4 to 64 characters in length and start with a letter. It can contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row42565233"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p30516772"><a name="p30516772"></a><a name="p30516772"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p55939488"><a name="p55939488"></a><a name="p55939488"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p34804713"><a name="p34804713"></a><a name="p34804713"></a>Specifies the specification ID (<span class="parmname" id="parmname1056617516452"><a name="parmname1056617516452"></a><a name="parmname1056617516452"></a><b>str_id</b></span> in the response message in <a href="obtaining-all-db-instance-specifications-18.md#table5932144310813">Table 3</a> in section <a href="obtaining-all-db-instance-specifications-18.md">Obtaining All DB Instance Specifications</a>).</p>
    <p id="p44806966"><a name="p44806966"></a><a name="p44806966"></a>Valid value:</p>
    <p id="p384473214443"><a name="p384473214443"></a><a name="p384473214443"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row10911119122552"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p37921377122726"><a name="p37921377122726"></a><a name="p37921377122726"></a>users</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p51732731122726"><a name="p51732731122726"></a><a name="p51732731122726"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p29601710122726"><a name="p29601710122726"></a><a name="p29601710122726"></a>List data structure. For details, see <a href="#table52086869182956">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37701418122726"><a name="p37701418122726"></a><a name="p37701418122726"></a>Specifies the user information.</p>
    <p id="p3768444122726"><a name="p3768444122726"></a><a name="p3768444122726"></a>It must contain the administrator username (for mysql and postgres, the administrator username is <strong id="b842352706192849"><a name="b842352706192849"></a><a name="b842352706192849"></a>root</strong>) and the administrator password.</p>
    </td>
    </tr>
    <tr id="row10212442122810"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p38533284122814"><a name="p38533284122814"></a><a name="p38533284122814"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p34188317122814"><a name="p34188317122814"></a><a name="p34188317122814"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p17790262122814"><a name="p17790262122814"></a><a name="p17790262122814"></a>Dictionary data structure. For details, see <a href="#table812499818308">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p17090258122814"><a name="p17090258122814"></a><a name="p17090258122814"></a>Specifies the volume information.</p>
    </td>
    </tr>
    <tr id="row38255771182316"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p7458408182320"><a name="p7458408182320"></a><a name="p7458408182320"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p151300182320"><a name="p151300182320"></a><a name="p151300182320"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p12255300182320"><a name="p12255300182320"></a><a name="p12255300182320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8634903182320"><a name="p8634903182320"></a><a name="p8634903182320"></a>Specifies the configuration parameter set used for initializing the database. For details about how to obtain this parameter value, see <strong id="b842352706195521"><a name="b842352706195521"></a><a name="b842352706195521"></a>configurations.id</strong> in the response message in section <a href="obtaining-a-parameter-template-list-23.md">Obtaining a Parameter Template List</a>.</p>
    <p id="p10605265182320"><a name="p10605265182320"></a><a name="p10605265182320"></a>Valid value: The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row15044115182424"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p18168441182430"><a name="p18168441182430"></a><a name="p18168441182430"></a>databases</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p62357587182430"><a name="p62357587182430"></a><a name="p62357587182430"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p17799769182430"><a name="p17799769182430"></a><a name="p17799769182430"></a>List data structure. For details, see <a href="#table10656503">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24021533182430"><a name="p24021533182430"></a><a name="p24021533182430"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    <tr id="row14119184171355"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p52247814171716"><a name="p52247814171716"></a><a name="p52247814171716"></a>modules</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p4214542171716"><a name="p4214542171716"></a><a name="p4214542171716"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p5833635171716"><a name="p5833635171716"></a><a name="p5833635171716"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24861712171716"><a name="p24861712171716"></a><a name="p24861712171716"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    <tr id="row5231214612292"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p636523122911"><a name="p636523122911"></a><a name="p636523122911"></a>nics</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p51558387122911"><a name="p51558387122911"></a><a name="p51558387122911"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p15479795122911"><a name="p15479795122911"></a><a name="p15479795122911"></a>Array. For details, see <a href="#table2179128">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10481848122911"><a name="p10481848122911"></a><a name="p10481848122911"></a>Specifies the nics information. For details about how to obtain this parameter value, see section "Subnet" in the <em id="i842352697165629"><a name="i842352697165629"></a><a name="i842352697165629"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p27227773122911"><a name="p27227773122911"></a><a name="p27227773122911"></a>If this parameter is not specified, RDS will query the VPC, subnet, and security group of the tenant. By default, the first query result is the parameter value.</p>
    </td>
    </tr>
    <tr id="row9307971"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p533144"><a name="p533144"></a><a name="p533144"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8297278"><a name="p8297278"></a><a name="p8297278"></a>Specifies the AZ ID.</p>
    <p id="p6574938217430"><a name="p6574938217430"></a><a name="p6574938217430"></a>Valid value:</p>
    <p id="p3825082612023"><a name="p3825082612023"></a><a name="p3825082612023"></a>For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row53995777123132"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p31441858123142"><a name="p31441858123142"></a><a name="p31441858123142"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p63762573123142"><a name="p63762573123142"></a><a name="p63762573123142"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p64494764123142"><a name="p64494764123142"></a><a name="p64494764123142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p56693384123142"><a name="p56693384123142"></a><a name="p56693384123142"></a>Specifies the VPC ID. For details about how to obtain this parameter value, see section "Virtual Private Cloud" in the <em id="i899345101"><a name="i899345101"></a><a name="i899345101"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p40478408123142"><a name="p40478408123142"></a><a name="p40478408123142"></a>Valid value:</p>
    <p id="p28761352123142"><a name="p28761352123142"></a><a name="p28761352123142"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row37460321"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p884523171817"><a name="p884523171817"></a><a name="p884523171817"></a>restorePoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p4537551171817"><a name="p4537551171817"></a><a name="p4537551171817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p31997314171817"><a name="p31997314171817"></a><a name="p31997314171817"></a>Dictionary data structure. For details, see <a href="#table41613092172617">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41645679171817"><a name="p41645679171817"></a><a name="p41645679171817"></a>Specifies the configuration parameter for restoring data to a new DB instance.</p>
    <p id="p39266794171817"><a name="p39266794171817"></a><a name="p39266794171817"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    <tr id="row33762549"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p31027925171837"><a name="p31027925171837"></a><a name="p31027925171837"></a>cluster_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p30233960171837"><a name="p30233960171837"></a><a name="p30233960171837"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.5.1.3 "><p id="p33031733171837"><a name="p33031733171837"></a><a name="p33031733171837"></a>Dictionary data structure. For details, see <a href="#table19785388173024">Table 11</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58324706171837"><a name="p58324706171837"></a><a name="p58324706171837"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  instance field data structure description \(creating a read replica\)

    <a name="table32692621183156"></a>
    <table><thead align="left"><tr id="row47515064183156"><th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.1"><p id="p23514980183156"><a name="p23514980183156"></a><a name="p23514980183156"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.2"><p id="p25665224183156"><a name="p25665224183156"></a><a name="p25665224183156"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.08%" id="mcps1.2.5.1.3"><p id="p65617293183156"><a name="p65617293183156"></a><a name="p65617293183156"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p13400539183156"><a name="p13400539183156"></a><a name="p13400539183156"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11701849183156"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p8325679183156"><a name="p8325679183156"></a><a name="p8325679183156"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p3291398183156"><a name="p3291398183156"></a><a name="p3291398183156"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p65276677183156"><a name="p65276677183156"></a><a name="p65276677183156"></a>Dictionary data structure. For details, see <a href="#table1282893518295">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p6513539183156"><a name="p6513539183156"></a><a name="p6513539183156"></a>Specifies the database information. Its value must be the same as the primary DB instance.</p>
    </td>
    </tr>
    <tr id="row58621854183156"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p50749703183156"><a name="p50749703183156"></a><a name="p50749703183156"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p17085240183156"><a name="p17085240183156"></a><a name="p17085240183156"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p41727194183156"><a name="p41727194183156"></a><a name="p41727194183156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p2040583212443"><a name="p2040583212443"></a><a name="p2040583212443"></a>Specifies the DB instance name.</p>
    <p id="p15405332124419"><a name="p15405332124419"></a><a name="p15405332124419"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p18809274183156"><a name="p18809274183156"></a><a name="p18809274183156"></a>Valid value:</p>
    <p id="p35065743183156"><a name="p35065743183156"></a><a name="p35065743183156"></a>The value must be 4 to 64 characters in length and start with a letter. It can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row47156236183156"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p61558795183156"><a name="p61558795183156"></a><a name="p61558795183156"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p20206494183156"><a name="p20206494183156"></a><a name="p20206494183156"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p26113326183156"><a name="p26113326183156"></a><a name="p26113326183156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p34804642183156"><a name="p34804642183156"></a><a name="p34804642183156"></a>Specifies the specification ID (<span class="parmname" id="parmname1751651919427"><a name="parmname1751651919427"></a><a name="parmname1751651919427"></a><b>str_id</b></span> in the response message in <a href="obtaining-all-db-instance-specifications-18.md#table5932144310813">Table 3</a> in section <a href="obtaining-all-db-instance-specifications-18.md">Obtaining All DB Instance Specifications</a>).</p>
    <p id="p603747183156"><a name="p603747183156"></a><a name="p603747183156"></a>Valid value:</p>
    <p id="p5433723183156"><a name="p5433723183156"></a><a name="p5433723183156"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row328001112117"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p1664755712120"><a name="p1664755712120"></a><a name="p1664755712120"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p627490612120"><a name="p627490612120"></a><a name="p627490612120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p3850540012120"><a name="p3850540012120"></a><a name="p3850540012120"></a>Dictionary data structure. For details, see <a href="#table812499818308">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1893157412120"><a name="p1893157412120"></a><a name="p1893157412120"></a>Specifies the volume information. The volume information must be the same as that of the primary DB instance.</p>
    </td>
    </tr>
    <tr id="row61351644161119"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p23260218161128"><a name="p23260218161128"></a><a name="p23260218161128"></a>slave_of</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p5029466161128"><a name="p5029466161128"></a><a name="p5029466161128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p4733574161128"><a name="p4733574161128"></a><a name="p4733574161128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10161974161148"><a name="p10161974161148"></a><a name="p10161974161148"></a>Specifies the read replica configuration parameter. It is used to create a read replica of a primary DB instance specified by <strong id="b84235270617137_1"><a name="b84235270617137_1"></a><a name="b84235270617137_1"></a>slave_of</strong>.</p>
    <p id="p47875239161128"><a name="p47875239161128"></a><a name="p47875239161128"></a>Valid value: The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified. Only the primary DB instance ID is valid.</p>
    </td>
    </tr>
    <tr id="row60704404161359"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p45660683161412"><a name="p45660683161412"></a><a name="p45660683161412"></a>replica_of</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p7527855161412"><a name="p7527855161412"></a><a name="p7527855161412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p5776482161412"><a name="p5776482161412"></a><a name="p5776482161412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p64063826161443"><a name="p64063826161443"></a><a name="p64063826161443"></a>Specifies the read replica configuration parameter. It is used to create a read replica of a primary DB instance specified by <strong id="b84235270617137_3"><a name="b84235270617137_3"></a><a name="b84235270617137_3"></a>replica_of</strong>.</p>
    <p id="p65241935161412"><a name="p65241935161412"></a><a name="p65241935161412"></a>Valid value: The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified. Only the primary DB instance ID is valid.</p>
    <p id="p50306506161412"><a name="p50306506161412"></a><a name="p50306506161412"></a>If both <strong id="b842352706203428"><a name="b842352706203428"></a><a name="b842352706203428"></a>slave_of</strong> and <strong id="b842352706203431"><a name="b842352706203431"></a><a name="b842352706203431"></a>replica_of</strong> exist, use <strong id="b686831585203452"><a name="b686831585203452"></a><a name="b686831585203452"></a>replica_of</strong> first.</p>
    </td>
    </tr>
    <tr id="row50975269161930"><td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.1 "><p id="p24652695161945"><a name="p24652695161945"></a><a name="p24652695161945"></a>replica_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p50711289161945"><a name="p50711289161945"></a><a name="p50711289161945"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.3 "><p id="p13973768161945"><a name="p13973768161945"></a><a name="p13973768161945"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58133419161945"><a name="p58133419161945"></a><a name="p58133419161945"></a>Specifies the number of read replicas.</p>
    <p id="p53438728161945"><a name="p53438728161945"></a><a name="p53438728161945"></a>Currently, creating multiple read replicas at a time is not supported.</p>
    <p id="p2356597816205"><a name="p2356597816205"></a><a name="p2356597816205"></a>Valid value: <strong id="b842352706113942"><a name="b842352706113942"></a><a name="b842352706113942"></a>1</strong> or not contained in the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  datastore field data structure description

    <a name="table1282893518295"></a>
    <table><thead align="left"><tr id="row1297240218295"><th class="cellrowborder" valign="top" width="22.052205220522055%" id="mcps1.2.5.1.1"><p id="p4413161718295"><a name="p4413161718295"></a><a name="p4413161718295"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p1789121318295"><a name="p1789121318295"></a><a name="p1789121318295"></a><strong id="b842352706102346_9"><a name="b842352706102346_9"></a><a name="b842352706102346_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.14331433143314%" id="mcps1.2.5.1.3"><p id="p3990210918295"><a name="p3990210918295"></a><a name="p3990210918295"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.002500250025%" id="mcps1.2.5.1.4"><p id="p1084536918295"><a name="p1084536918295"></a><a name="p1084536918295"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row605972218295"><td class="cellrowborder" valign="top" width="22.052205220522055%" headers="mcps1.2.5.1.1 "><p id="p2107551218295"><a name="p2107551218295"></a><a name="p2107551218295"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p2939492218295"><a name="p2939492218295"></a><a name="p2939492218295"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.14331433143314%" headers="mcps1.2.5.1.3 "><p id="p3217850518295"><a name="p3217850518295"></a><a name="p3217850518295"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.5.1.4 "><p id="p5632210818295"><a name="p5632210818295"></a><a name="p5632210818295"></a>Specifies the DB engine.</p>
    <p id="p3713692918295"><a name="p3713692918295"></a><a name="p3713692918295"></a>Currently, the DB engines MySQL and PostgreSQL are supported.</p>
    </td>
    </tr>
    <tr id="row6579690818295"><td class="cellrowborder" valign="top" width="22.052205220522055%" headers="mcps1.2.5.1.1 "><p id="p2794931218295"><a name="p2794931218295"></a><a name="p2794931218295"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p4930179318295"><a name="p4930179318295"></a><a name="p4930179318295"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.14331433143314%" headers="mcps1.2.5.1.3 "><p id="p3402226218295"><a name="p3402226218295"></a><a name="p3402226218295"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.002500250025%" headers="mcps1.2.5.1.4 "><p id="p433981518295"><a name="p433981518295"></a><a name="p433981518295"></a>Specifies the database version.</p>
    <a name="ul2128855618558"></a><a name="ul2128855618558"></a><ul id="ul2128855618558"><li>MySQL databases support 5.6 and 5.7. Example value: MySQL-5.7</li><li>PostgreSQL databases support 9.5, 9.6, 10, and 11. Example value: PostgreSQL-9.6</li></ul>
    <p id="p2139751518103"><a name="p2139751518103"></a><a name="p2139751518103"></a>For details about supported database versions, see section <a href="database-version-queries.md">Database Version Queries</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  users field data structure description

    <a name="table52086869182956"></a>
    <table><thead align="left"><tr id="row35321281182956"><th class="cellrowborder" valign="top" width="21.73%" id="mcps1.2.5.1.1"><p id="p42451536182956"><a name="p42451536182956"></a><a name="p42451536182956"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.36%" id="mcps1.2.5.1.2"><p id="p16022387182956"><a name="p16022387182956"></a><a name="p16022387182956"></a><strong id="b842352706102346_11"><a name="b842352706102346_11"></a><a name="b842352706102346_11"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.910000000000004%" id="mcps1.2.5.1.3"><p id="p22744979182956"><a name="p22744979182956"></a><a name="p22744979182956"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p30403991182956"><a name="p30403991182956"></a><a name="p30403991182956"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46804200182956"><td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.5.1.1 "><p id="p33043821182956"><a name="p33043821182956"></a><a name="p33043821182956"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.5.1.2 "><p id="p59303822182956"><a name="p59303822182956"></a><a name="p59303822182956"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.910000000000004%" headers="mcps1.2.5.1.3 "><p id="p38880309182956"><a name="p38880309182956"></a><a name="p38880309182956"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p62297287182956"><a name="p62297287182956"></a><a name="p62297287182956"></a>Specifies the database username. Currently, the database username for mysql and postgres is <strong id="b842352706213032"><a name="b842352706213032"></a><a name="b842352706213032"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="row23804677182956"><td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.5.1.1 "><p id="p49130661182956"><a name="p49130661182956"></a><a name="p49130661182956"></a>password</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.5.1.2 "><p id="p20160614182956"><a name="p20160614182956"></a><a name="p20160614182956"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.910000000000004%" headers="mcps1.2.5.1.3 "><p id="p22397039182956"><a name="p22397039182956"></a><a name="p22397039182956"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p2220905182956"><a name="p2220905182956"></a><a name="p2220905182956"></a>Specifies the password of the database user.</p>
    <p id="p4185084616327"><a name="p4185084616327"></a><a name="p4185084616327"></a>The value cannot be empty and should contain 8 to 32 characters, including uppercase and lowercase letters, digits, and the following special characters: ~!@#%^*-_=+?</p>
    </td>
    </tr>
    <tr id="row19988152182956"><td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.5.1.1 "><p id="p8427614182956"><a name="p8427614182956"></a><a name="p8427614182956"></a>databases</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.5.1.2 "><p id="p11548104182956"><a name="p11548104182956"></a><a name="p11548104182956"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.910000000000004%" headers="mcps1.2.5.1.3 "><p id="p62981214182956"><a name="p62981214182956"></a><a name="p62981214182956"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1204746182956"><a name="p1204746182956"></a><a name="p1204746182956"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  volume field data structure description

    <a name="table812499818308"></a>
    <table><thead align="left"><tr id="row1209876418308"><th class="cellrowborder" valign="top" width="21.529999999999998%" id="mcps1.2.5.1.1"><p id="p4047583118308"><a name="p4047583118308"></a><a name="p4047583118308"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.77%" id="mcps1.2.5.1.2"><p id="p5731685418308"><a name="p5731685418308"></a><a name="p5731685418308"></a><strong id="b842352706102346_13"><a name="b842352706102346_13"></a><a name="b842352706102346_13"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.99%" id="mcps1.2.5.1.3"><p id="p1215358618308"><a name="p1215358618308"></a><a name="p1215358618308"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.709999999999997%" id="mcps1.2.5.1.4"><p id="p4491637018308"><a name="p4491637018308"></a><a name="p4491637018308"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1434732618308"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.5.1.1 "><p id="p12805632123442"><a name="p12805632123442"></a><a name="p12805632123442"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.5.1.2 "><p id="p30623235123442"><a name="p30623235123442"></a><a name="p30623235123442"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.99%" headers="mcps1.2.5.1.3 "><p id="p64563008123442"><a name="p64563008123442"></a><a name="p64563008123442"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.2.5.1.4 "><p id="p8172010105044"><a name="p8172010105044"></a><a name="p8172010105044"></a>Specifies the volume type.</p>
    <p id="p62221149123442"><a name="p62221149123442"></a><a name="p62221149123442"></a>Its value can be any of the following and is case-sensitive:</p>
    <a name="ul06211247141917"></a><a name="ul06211247141917"></a><ul id="ul06211247141917"><li><strong id="b1033916119322"><a name="b1033916119322"></a><a name="b1033916119322"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b182031914183213"><a name="b182031914183213"></a><a name="b182031914183213"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
    <div class="note" id="note23119431123442"><a name="note23119431123442"></a><a name="note23119431123442"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6748290123442"><a name="p6748290123442"></a><a name="p6748290123442"></a>In the Trove API, this parameter is optional in the request. If this parameter is not contained in the request, its value is <strong id="b842352706214824"><a name="b842352706214824"></a><a name="b842352706214824"></a>COMMON</strong> by default. If this parameter is specified, the volume type must be set to a value supported by the old API.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1030080118308"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.5.1.1 "><p id="p20556829123442"><a name="p20556829123442"></a><a name="p20556829123442"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.2.5.1.2 "><p id="p54490430123442"><a name="p54490430123442"></a><a name="p54490430123442"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.99%" headers="mcps1.2.5.1.3 "><p id="p51648741123442"><a name="p51648741123442"></a><a name="p51648741123442"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.2.5.1.4 "><p id="p22798455123442"><a name="p22798455123442"></a><a name="p22798455123442"></a>Specifies the volume size in gigabytes (GB).</p>
    <p id="p35443891"><a name="p35443891"></a><a name="p35443891"></a>Its value must be a multiple of 10 and the value range is from 40 GB to 4000 GB.</p>
    <div class="note" id="note6488766393554"><a name="note6488766393554"></a><a name="note6488766393554"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4711805793554"><a name="p4711805793554"></a><a name="p4711805793554"></a>If the size is a decimal value, the system will round it down.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  databases field data structure description \(not supported currently\)

    <a name="table10656503"></a>
    <table><thead align="left"><tr id="row5847780"><th class="cellrowborder" valign="top" width="21.43214321432143%" id="mcps1.2.5.1.1"><p id="p3908185"><a name="p3908185"></a><a name="p3908185"></a><strong id="b84235270691445_17"><a name="b84235270691445_17"></a><a name="b84235270691445_17"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.122112211221122%" id="mcps1.2.5.1.2"><p id="p48127554"><a name="p48127554"></a><a name="p48127554"></a><strong id="b842352706102346_15"><a name="b842352706102346_15"></a><a name="b842352706102346_15"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.87328732873287%" id="mcps1.2.5.1.3"><p id="p6017800"><a name="p6017800"></a><a name="p6017800"></a><strong id="b842352706164541_13"><a name="b842352706164541_13"></a><a name="b842352706164541_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.57245724572457%" id="mcps1.2.5.1.4"><p id="p17679762"><a name="p17679762"></a><a name="p17679762"></a><strong id="b842352706163417_17"><a name="b842352706163417_17"></a><a name="b842352706163417_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32061346123339"><td class="cellrowborder" valign="top" width="21.43214321432143%" headers="mcps1.2.5.1.1 "><p id="p53202695123419"><a name="p53202695123419"></a><a name="p53202695123419"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.122112211221122%" headers="mcps1.2.5.1.2 "><p id="p14451011123419"><a name="p14451011123419"></a><a name="p14451011123419"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87328732873287%" headers="mcps1.2.5.1.3 "><p id="p29681268123419"><a name="p29681268123419"></a><a name="p29681268123419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.57245724572457%" headers="mcps1.2.5.1.4 "><p id="p55372546123419"><a name="p55372546123419"></a><a name="p55372546123419"></a>Specifies the database name.</p>
    </td>
    </tr>
    <tr id="row63134513123348"><td class="cellrowborder" valign="top" width="21.43214321432143%" headers="mcps1.2.5.1.1 "><p id="p34159227123419"><a name="p34159227123419"></a><a name="p34159227123419"></a>collate</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.122112211221122%" headers="mcps1.2.5.1.2 "><p id="p15433966123419"><a name="p15433966123419"></a><a name="p15433966123419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87328732873287%" headers="mcps1.2.5.1.3 "><p id="p42191771123419"><a name="p42191771123419"></a><a name="p42191771123419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.57245724572457%" headers="mcps1.2.5.1.4 "><p id="p62090280123419"><a name="p62090280123419"></a><a name="p62090280123419"></a>Specifies the database code.</p>
    </td>
    </tr>
    <tr id="row33943398123344"><td class="cellrowborder" valign="top" width="21.43214321432143%" headers="mcps1.2.5.1.1 "><p id="p32439979123419"><a name="p32439979123419"></a><a name="p32439979123419"></a>characterSet</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.122112211221122%" headers="mcps1.2.5.1.2 "><p id="p10392608123419"><a name="p10392608123419"></a><a name="p10392608123419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.87328732873287%" headers="mcps1.2.5.1.3 "><p id="p36494897123419"><a name="p36494897123419"></a><a name="p36494897123419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.57245724572457%" headers="mcps1.2.5.1.4 "><p id="p3296712123419"><a name="p3296712123419"></a><a name="p3296712123419"></a>Specifies the database code.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  nics field data structure description

    <a name="table2179128"></a>
    <table><thead align="left"><tr id="row28646034"><th class="cellrowborder" valign="top" width="21.567843215678433%" id="mcps1.2.5.1.1"><p id="p38627455"><a name="p38627455"></a><a name="p38627455"></a><strong id="b84235270691445_19"><a name="b84235270691445_19"></a><a name="b84235270691445_19"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.997900209979%" id="mcps1.2.5.1.2"><p id="p41816140"><a name="p41816140"></a><a name="p41816140"></a><strong id="b842352706102346_17"><a name="b842352706102346_17"></a><a name="b842352706102346_17"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.71672832716728%" id="mcps1.2.5.1.3"><p id="p31664161"><a name="p31664161"></a><a name="p31664161"></a><strong id="b842352706164541_15"><a name="b842352706164541_15"></a><a name="b842352706164541_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.717528247175284%" id="mcps1.2.5.1.4"><p id="p14660263"><a name="p14660263"></a><a name="p14660263"></a><strong id="b842352706163417_19"><a name="b842352706163417_19"></a><a name="b842352706163417_19"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46630661"><td class="cellrowborder" valign="top" width="21.567843215678433%" headers="mcps1.2.5.1.1 "><p id="p18987236"><a name="p18987236"></a><a name="p18987236"></a>net-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.997900209979%" headers="mcps1.2.5.1.2 "><p id="p61571180"><a name="p61571180"></a><a name="p61571180"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.71672832716728%" headers="mcps1.2.5.1.3 "><p id="p21209668"><a name="p21209668"></a><a name="p21209668"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.4 "><p id="p40261524"><a name="p40261524"></a><a name="p40261524"></a>Specifies the subnet ID obtained from the VPC.</p>
    <p id="p26809401"><a name="p26809401"></a><a name="p26809401"></a>Valid value:</p>
    <p id="p36848008144522"><a name="p36848008144522"></a><a name="p36848008144522"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    <div class="note" id="note9968994627"><a name="note9968994627"></a><a name="note9968994627"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1887520394633"><a name="p1887520394633"></a><a name="p1887520394633"></a>RDS will query the VPC associated with the specified net-id, associate the VPC with the DB instance, and query the security group based on the VPC. Then, RDS sets the queried security group.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row58535722173058"><td class="cellrowborder" valign="top" width="21.567843215678433%" headers="mcps1.2.5.1.1 "><p id="p43773055173058"><a name="p43773055173058"></a><a name="p43773055173058"></a>securityGroupId</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.997900209979%" headers="mcps1.2.5.1.2 "><p id="p55956552173058"><a name="p55956552173058"></a><a name="p55956552173058"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.71672832716728%" headers="mcps1.2.5.1.3 "><p id="p36186862173058"><a name="p36186862173058"></a><a name="p36186862173058"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.4 "><p id="p7492614"><a name="p7492614"></a><a name="p7492614"></a>Valid value:</p>
    <p id="p48836202144526"><a name="p48836202144526"></a><a name="p48836202144526"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  restorePoint field data structure description \(not supported currently\)

    <a name="table41613092172617"></a>
    <table><thead align="left"><tr id="row46529820172617"><th class="cellrowborder" valign="top" width="21.18788121187881%" id="mcps1.2.5.1.1"><p id="p10819075172617"><a name="p10819075172617"></a><a name="p10819075172617"></a><strong id="b84235270691445_21"><a name="b84235270691445_21"></a><a name="b84235270691445_21"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.987901209879013%" id="mcps1.2.5.1.2"><p id="p3929874172617"><a name="p3929874172617"></a><a name="p3929874172617"></a><strong id="b842352706102346_19"><a name="b842352706102346_19"></a><a name="b842352706102346_19"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.966703329667034%" id="mcps1.2.5.1.3"><p id="p49884402172617"><a name="p49884402172617"></a><a name="p49884402172617"></a><strong id="b842352706164541_17"><a name="b842352706164541_17"></a><a name="b842352706164541_17"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.857514248575143%" id="mcps1.2.5.1.4"><p id="p14104779172617"><a name="p14104779172617"></a><a name="p14104779172617"></a><strong id="b842352706163417_21"><a name="b842352706163417_21"></a><a name="b842352706163417_21"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1636420172617"><td class="cellrowborder" valign="top" width="21.18788121187881%" headers="mcps1.2.5.1.1 "><p id="p64294291172645"><a name="p64294291172645"></a><a name="p64294291172645"></a>backupRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.987901209879013%" headers="mcps1.2.5.1.2 "><p id="p40455065172645"><a name="p40455065172645"></a><a name="p40455065172645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.966703329667034%" headers="mcps1.2.5.1.3 "><p id="p55634869172645"><a name="p55634869172645"></a><a name="p55634869172645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.857514248575143%" headers="mcps1.2.5.1.4 "><p id="p28507117181526"><a name="p28507117181526"></a><a name="p28507117181526"></a>Specifies the full backup file.</p>
    <p id="p47906700181526"><a name="p47906700181526"></a><a name="p47906700181526"></a>Valid value: The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11**  cluster\_config field data structure description \(not supported currently\)

    <a name="table19785388173024"></a>
    <table><thead align="left"><tr id="row5181095173024"><th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.1"><p id="p17015590173024"><a name="p17015590173024"></a><a name="p17015590173024"></a><strong id="b84235270691445_23"><a name="b84235270691445_23"></a><a name="b84235270691445_23"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.97%" id="mcps1.2.5.1.2"><p id="p36085582173024"><a name="p36085582173024"></a><a name="p36085582173024"></a><strong id="b842352706102346_21"><a name="b842352706102346_21"></a><a name="b842352706102346_21"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.98%" id="mcps1.2.5.1.3"><p id="p37251014173024"><a name="p37251014173024"></a><a name="p37251014173024"></a><strong id="b842352706164541_19"><a name="b842352706164541_19"></a><a name="b842352706164541_19"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p64542134173024"><a name="p64542134173024"></a><a name="p64542134173024"></a><strong id="b842352706163417_23"><a name="b842352706163417_23"></a><a name="b842352706163417_23"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60530375173024"><td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.1 "><p id="p49801394173034"><a name="p49801394173034"></a><a name="p49801394173034"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.2.5.1.2 "><p id="p7381147173034"><a name="p7381147173034"></a><a name="p7381147173034"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.98%" headers="mcps1.2.5.1.3 "><p id="p61002040173034"><a name="p61002040173034"></a><a name="p61002040173034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p42218226173034"><a name="p42218226173034"></a><a name="p42218226173034"></a>Specifies the cluster ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    Creating a single DB instance:

    ```
    {
        "instance": {
            "datastore": {
                           "type": "MySQL",
                           "version": "MySQL-5.7"
                         },
            "name": "json-rack-instance",
            "flavorRef": "123",
            "users": [
                        {                      
                          "name": "root",
                          "password": "Demo@12345678"
                        }
                     ],
            "volume": {
                        "size": 100
                      },
            "configuration" : "ft26458f-d9f8-4cab-8fe1-cb8704fbo9bp",
            "nics":[
                    {
                     "net-id": "3226458f-d9f8-4cab-8fe1-cb8704fb9fb8",
                     "securityGroupId":"fpo6458f-d9f8-4cab-8fe1-cb8704fb9fb8"
                     }
                   ],
            "availability_zone": "az1pod1",
            "vpc":"98ik458f-d9f8-4cab-8fe1-cb8704fb9fbb"
           }
     }
    ```

    Creating a read replica:

    ```
    {
        "instance": {
            "datastore": {
                "type": "MySQL",
                "version": "MySQL-5.7"
            },
            "name": "json-rack-instance",
            "flavorRef": "123",
            "volume": {
                "size": 100
            },
            "replica_of": "123",
            "replica_count":1
        }
    }
    ```


## Normal Response<a name="section5037157118037"></a>

-   Parameter description

    **Table  12**  Parameter description

    <a name="table2105473618141"></a>
    <table><thead align="left"><tr id="row5305535918141"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p251680918141"><a name="p251680918141"></a><a name="p251680918141"></a><strong id="b84235270691445_25"><a name="b84235270691445_25"></a><a name="b84235270691445_25"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p400813618141"><a name="p400813618141"></a><a name="p400813618141"></a><strong id="b842352706164541_21"><a name="b842352706164541_21"></a><a name="b842352706164541_21"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5622356318141"><a name="p5622356318141"></a><a name="p5622356318141"></a><strong id="b842352706163417_25"><a name="b842352706163417_25"></a><a name="b842352706163417_25"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5781479218141"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2163967018239"><a name="p2163967018239"></a><a name="p2163967018239"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40959010173633"><a name="p40959010173633"></a><a name="p40959010173633"></a>Dictionary data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4895508618141"><a name="p4895508618141"></a><a name="p4895508618141"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  13**  instance field data structure description

    <a name="table6489863618329"></a>
    <table><thead align="left"><tr id="row95141018329"><th class="cellrowborder" valign="top" width="33.26332633263326%" id="mcps1.2.4.1.1"><p id="p995534618329"><a name="p995534618329"></a><a name="p995534618329"></a><strong id="b84235270691445_27"><a name="b84235270691445_27"></a><a name="b84235270691445_27"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.463346334633464%" id="mcps1.2.4.1.2"><p id="p969003718329"><a name="p969003718329"></a><a name="p969003718329"></a><strong id="b842352706164541_23"><a name="b842352706164541_23"></a><a name="b842352706164541_23"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.273327332733274%" id="mcps1.2.4.1.3"><p id="p1760649318329"><a name="p1760649318329"></a><a name="p1760649318329"></a><strong id="b842352706163417_27"><a name="b842352706163417_27"></a><a name="b842352706163417_27"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row123342018329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p3279822718329"><a name="p3279822718329"></a><a name="p3279822718329"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p3941069318329"><a name="p3941069318329"></a><a name="p3941069318329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p3814958018329"><a name="p3814958018329"></a><a name="p3814958018329"></a>Indicates the DB instance status.</p>
    </td>
    </tr>
    <tr id="row780190718329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p63328718105459"><a name="p63328718105459"></a><a name="p63328718105459"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p5899380105421"><a name="p5899380105421"></a><a name="p5899380105421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p19605484105421"><a name="p19605484105421"></a><a name="p19605484105421"></a>Indicates the DB instance updated time.</p>
    </td>
    </tr>
    <tr id="row6287432618329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p5965564418329"><a name="p5965564418329"></a><a name="p5965564418329"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p26896618329"><a name="p26896618329"></a><a name="p26896618329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p2548492105536"><a name="p2548492105536"></a><a name="p2548492105536"></a>Instances the DB instance name. When a single DB instance is created, its name is automatically added with the suffix "_node0", for example, rds-test-openstack_node0.</p>
    </td>
    </tr>
    <tr id="row6185869218329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p4449815218329"><a name="p4449815218329"></a><a name="p4449815218329"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p4758058918329"><a name="p4758058918329"></a><a name="p4758058918329"></a>List data structure. For details, see <a href="#table35796249181358">Table 14</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p2882252318329"><a name="p2882252318329"></a><a name="p2882252318329"></a>Indicates the DB instance information link.</p>
    </td>
    </tr>
    <tr id="row44609613105555"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p979978810560"><a name="p979978810560"></a><a name="p979978810560"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p5558537010560"><a name="p5558537010560"></a><a name="p5558537010560"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p612116110560"><a name="p612116110560"></a><a name="p612116110560"></a>Indicates the DB instance creation time.</p>
    </td>
    </tr>
    <tr id="row58075968105615"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p6532990105615"><a name="p6532990105615"></a><a name="p6532990105615"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p59410156105615"><a name="p59410156105615"></a><a name="p59410156105615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p47493298105615"><a name="p47493298105615"></a><a name="p47493298105615"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row5807611618329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p654496118329"><a name="p654496118329"></a><a name="p654496118329"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p6037985118329"><a name="p6037985118329"></a><a name="p6037985118329"></a>Dictionary data structure. For details, see <a href="#table5589436418437">Table 15</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p5892975318329"><a name="p5892975318329"></a><a name="p5892975318329"></a>Indicates the DB instance volume information.</p>
    </td>
    </tr>
    <tr id="row6060573318329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p1011736518329"><a name="p1011736518329"></a><a name="p1011736518329"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p1420025418329"><a name="p1420025418329"></a><a name="p1420025418329"></a>Dictionary data structure. For details, see <a href="#table4806207618447">Table 16</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p936989518329"><a name="p936989518329"></a><a name="p936989518329"></a>Indicates the DB instance specifications.</p>
    </td>
    </tr>
    <tr id="row1722019118329"><td class="cellrowborder" valign="top" width="33.26332633263326%" headers="mcps1.2.4.1.1 "><p id="p5265820318329"><a name="p5265820318329"></a><a name="p5265820318329"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.463346334633464%" headers="mcps1.2.4.1.2 "><p id="p3745607618329"><a name="p3745607618329"></a><a name="p3745607618329"></a>Dictionary data structure. For details, see <a href="#table629209691859">Table 17</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.273327332733274%" headers="mcps1.2.4.1.3 "><p id="p1404335418329"><a name="p1404335418329"></a><a name="p1404335418329"></a>Indicates the DB engine information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  14**  links field data structure description

    <a name="table35796249181358"></a>
    <table><thead align="left"><tr id="row43394390181358"><th class="cellrowborder" valign="top" width="33.19%" id="mcps1.2.4.1.1"><p id="p25284664181358"><a name="p25284664181358"></a><a name="p25284664181358"></a><strong id="b84235270691445_29"><a name="b84235270691445_29"></a><a name="b84235270691445_29"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.550000000000004%" id="mcps1.2.4.1.2"><p id="p34791919181358"><a name="p34791919181358"></a><a name="p34791919181358"></a><strong id="b842352706164541_25"><a name="b842352706164541_25"></a><a name="b842352706164541_25"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.26%" id="mcps1.2.4.1.3"><p id="p66682083181358"><a name="p66682083181358"></a><a name="p66682083181358"></a><strong id="b842352706163417_29"><a name="b842352706163417_29"></a><a name="b842352706163417_29"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32539643181358"><td class="cellrowborder" valign="top" width="33.19%" headers="mcps1.2.4.1.1 "><p id="p18465440181358"><a name="p18465440181358"></a><a name="p18465440181358"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.550000000000004%" headers="mcps1.2.4.1.2 "><p id="p19305657181358"><a name="p19305657181358"></a><a name="p19305657181358"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.26%" headers="mcps1.2.4.1.3 "><p id="p20254383181358"><a name="p20254383181358"></a><a name="p20254383181358"></a>Indicates the link address. Its value is <strong id="b842352706155319"><a name="b842352706155319"></a><a name="b842352706155319"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row48071720181358"><td class="cellrowborder" valign="top" width="33.19%" headers="mcps1.2.4.1.1 "><p id="p1495219181358"><a name="p1495219181358"></a><a name="p1495219181358"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.550000000000004%" headers="mcps1.2.4.1.2 "><p id="p54003919181358"><a name="p54003919181358"></a><a name="p54003919181358"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.26%" headers="mcps1.2.4.1.3 "><p id="p12241315181358"><a name="p12241315181358"></a><a name="p12241315181358"></a>Its value is <strong id="b842352706221326"><a name="b842352706221326"></a><a name="b842352706221326"></a>self</strong> or <strong id="b842352706221332"><a name="b842352706221332"></a><a name="b842352706221332"></a>bookmark</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  15**  volume field data structure description

    <a name="table5589436418437"></a>
    <table><thead align="left"><tr id="row2634996818437"><th class="cellrowborder" valign="top" width="33.339999999999996%" id="mcps1.2.4.1.1"><p id="p5397265318437"><a name="p5397265318437"></a><a name="p5397265318437"></a><strong id="b84235270691445_31"><a name="b84235270691445_31"></a><a name="b84235270691445_31"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.26%" id="mcps1.2.4.1.2"><p id="p2026992818437"><a name="p2026992818437"></a><a name="p2026992818437"></a><strong id="b842352706164541_27"><a name="b842352706164541_27"></a><a name="b842352706164541_27"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.4%" id="mcps1.2.4.1.3"><p id="p1282747818437"><a name="p1282747818437"></a><a name="p1282747818437"></a><strong id="b842352706163417_31"><a name="b842352706163417_31"></a><a name="b842352706163417_31"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3239283718437"><td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.1 "><p id="p657417318437"><a name="p657417318437"></a><a name="p657417318437"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.26%" headers="mcps1.2.4.1.2 "><p id="p6274598918437"><a name="p6274598918437"></a><a name="p6274598918437"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.4%" headers="mcps1.2.4.1.3 "><p id="p4926032518437"><a name="p4926032518437"></a><a name="p4926032518437"></a>Indicates the volume size in GB.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  16**  flavor field data structure description

    <a name="table4806207618447"></a>
    <table><thead align="left"><tr id="row5436532118447"><th class="cellrowborder" valign="top" width="30.06699330066993%" id="mcps1.2.4.1.1"><p id="p4151484318447"><a name="p4151484318447"></a><a name="p4151484318447"></a><strong id="b84235270691445_33"><a name="b84235270691445_33"></a><a name="b84235270691445_33"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.96650334966503%" id="mcps1.2.4.1.2"><p id="p6533224918447"><a name="p6533224918447"></a><a name="p6533224918447"></a><strong id="b842352706164541_29"><a name="b842352706164541_29"></a><a name="b842352706164541_29"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.96650334966503%" id="mcps1.2.4.1.3"><p id="p4702539018447"><a name="p4702539018447"></a><a name="p4702539018447"></a><strong id="b842352706163417_33"><a name="b842352706163417_33"></a><a name="b842352706163417_33"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5096025918447"><td class="cellrowborder" valign="top" width="30.06699330066993%" headers="mcps1.2.4.1.1 "><p id="p3414030018447"><a name="p3414030018447"></a><a name="p3414030018447"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.2 "><p id="p1390091418447"><a name="p1390091418447"></a><a name="p1390091418447"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.3 "><p id="p5223222018447"><a name="p5223222018447"></a><a name="p5223222018447"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    <tr id="row32793418447"><td class="cellrowborder" valign="top" width="30.06699330066993%" headers="mcps1.2.4.1.1 "><p id="p2656269818447"><a name="p2656269818447"></a><a name="p2656269818447"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.2 "><p id="p409492618447"><a name="p409492618447"></a><a name="p409492618447"></a>List data structure. For details, see <a href="#table35796249181358">Table 14</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.3 "><p id="p6325361918447"><a name="p6325361918447"></a><a name="p6325361918447"></a>Indicates the DB instance specification link.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  17**  datastore field data structure description

    <a name="table629209691859"></a>
    <table><thead align="left"><tr id="row465266741859"><th class="cellrowborder" valign="top" width="30.06699330066993%" id="mcps1.2.4.1.1"><p id="p105642511859"><a name="p105642511859"></a><a name="p105642511859"></a><strong id="b84235270691445_35"><a name="b84235270691445_35"></a><a name="b84235270691445_35"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.96650334966503%" id="mcps1.2.4.1.2"><p id="p509291561859"><a name="p509291561859"></a><a name="p509291561859"></a><strong id="b842352706164541_31"><a name="b842352706164541_31"></a><a name="b842352706164541_31"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.96650334966503%" id="mcps1.2.4.1.3"><p id="p161532751859"><a name="p161532751859"></a><a name="p161532751859"></a><strong id="b842352706163417_35"><a name="b842352706163417_35"></a><a name="b842352706163417_35"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row333468701859"><td class="cellrowborder" valign="top" width="30.06699330066993%" headers="mcps1.2.4.1.1 "><p id="p167419541859"><a name="p167419541859"></a><a name="p167419541859"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.2 "><p id="p139210301859"><a name="p139210301859"></a><a name="p139210301859"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.3 "><p id="p538616751859"><a name="p538616751859"></a><a name="p538616751859"></a>Indicates the DB engine.</p>
    </td>
    </tr>
    <tr id="row149930331859"><td class="cellrowborder" valign="top" width="30.06699330066993%" headers="mcps1.2.4.1.1 "><p id="p64761941859"><a name="p64761941859"></a><a name="p64761941859"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.2 "><p id="p548097111859"><a name="p548097111859"></a><a name="p548097111859"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.4.1.3 "><p id="p104016251859"><a name="p104016251859"></a><a name="p104016251859"></a>Indicates the database version, such as MySQL-5.6.33.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "instance": {
        "status": "BUILD",
        "updated": "2017-05-06T05:55:03",
        "name": "creat-trove-instance-28-MySQL-1-1",
        "links": [
          {
            "href": "",
            "rel": "self"
          },
          {
            "href": "",
            "rel": "bookmark"
          }
        ],
        "created": "2017-05-06T05:55:03",
        "id": "c90c1234-f687-462a-a6bd-cec35919c096",
        "volume": {
          "size": 100
        },
        "flavor": {
          "id": "99001234-dfc2-4418-b224-fea05d358ce3",
          "links": [
            {
              "href": "",
              "rel": "self"
            },
            {
              "href": "",
              "rel": "bookmark"
            }
          ]
        },
        "datastore": {
          "type": "MySQL",
          "version": "MySQL-5.7"
        }
      }
    }
    ```


## Abnormal Response<a name="section1604544818856"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

