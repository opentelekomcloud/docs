# Creating a DB Instance<a name="en-us_topic_0032347785"></a>

## Function<a name="section4284989"></a>

This API is used to create a single DB instance, primary/standby DB instances, or a read replica.

## URI<a name="section38564907"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.810000000000002%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.449999999999996%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27827961145955"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="p184490251502"><a name="p184490251502"></a><a name="p184490251502"></a>versionId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.4.1.2 "><p id="p179760341502"><a name="p179760341502"></a><a name="p179760341502"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p467726811502"><a name="p467726811502"></a><a name="p467726811502"></a>Specifies the API version. It is case-sensitive and the value is <strong id="b842352706143722"><a name="b842352706143722"></a><a name="b842352706143722"></a>v1</strong>.</p>
    </td>
    </tr>
    <tr id="row3925534"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11539844"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table6209466312442"></a>
    <table><thead align="left"><tr id="row6512234412442"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p4041853012442"><a name="p4041853012442"></a><a name="p4041853012442"></a><strong id="b1333949967"><a name="b1333949967"></a><a name="b1333949967"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5267548812442"><a name="p5267548812442"></a><a name="p5267548812442"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3885613912442"><a name="p3885613912442"></a><a name="p3885613912442"></a><strong id="b999545495"><a name="b999545495"></a><a name="b999545495"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6033953012442"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5566375012442"><a name="p5566375012442"></a><a name="p5566375012442"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5287375317633"><a name="p5287375317633"></a><a name="p5287375317633"></a>Dictionary data structure.</p>
    <p id="p1246986212442"><a name="p1246986212442"></a><a name="p1246986212442"></a>For details on the field description when creating single or primary/standby DB instances, see <a href="#table11236435">Table 3</a>.</p>
    <p id="p590235817628"><a name="p590235817628"></a><a name="p590235817628"></a>For details on the field description when creating a read replica, see <a href="#table228903751753">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48757463124544"><a name="p48757463124544"></a><a name="p48757463124544"></a>Specifies the detailed DB instance information.</p>
    <div class="notice" id="note629684781753"><a name="note629684781753"></a><a name="note629684781753"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p298453971753"><a name="p298453971753"></a><a name="p298453971753"></a>RDS for Microsoft SQL Server does not support creating read replicas.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instance field data structure \(creating single or primary/standby DB instances\)

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="29.520000000000003%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b1117733008"><a name="b1117733008"></a><a name="b1117733008"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b863368061"><a name="b863368061"></a><a name="b863368061"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.060000000000002%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b2023782395"><a name="b2023782395"></a><a name="b2023782395"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b210250754"><a name="b210250754"></a><a name="b210250754"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p23411412333"><a name="p23411412333"></a><a name="p23411412333"></a>Specifies the DB instance name.</p>
    <p id="p463314503337"><a name="p463314503337"></a><a name="p463314503337"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Valid value:</p>
    <p id="p13135136181854"><a name="p13135136181854"></a><a name="p13135136181854"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row56760689"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p19797588"><a name="p19797588"></a><a name="p19797588"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p60100823"><a name="p60100823"></a><a name="p60100823"></a>Dictionary data structure. For details, see <a href="#table64243102">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58520811"><a name="p58520811"></a><a name="p58520811"></a>Specifies the database information.</p>
    </td>
    </tr>
    <tr id="row42565233"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p30516772"><a name="p30516772"></a><a name="p30516772"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p55939488"><a name="p55939488"></a><a name="p55939488"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p34804713"><a name="p34804713"></a><a name="p34804713"></a>Specifies the specification ID (<strong id="b15464132919295"><a name="b15464132919295"></a><a name="b15464132919295"></a>flavors.id</strong> in the response message in section <a href="obtaining-all-db-instance-specifications.md">Obtaining All DB Instance Specifications</a>).</p>
    <p id="p44806966"><a name="p44806966"></a><a name="p44806966"></a>Valid value:</p>
    <p id="p384473214443"><a name="p384473214443"></a><a name="p384473214443"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row49370368"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p39576862"><a name="p39576862"></a><a name="p39576862"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p51609257"><a name="p51609257"></a><a name="p51609257"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>Dictionary data structure. For details, see <a href="#table10656503">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p61513540"><a name="p61513540"></a><a name="p61513540"></a>Specifies the volume information.</p>
    </td>
    </tr>
    <tr id="row16540805"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p64736823"><a name="p64736823"></a><a name="p64736823"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40344576"><a name="p40344576"></a><a name="p40344576"></a>Specifies the region ID.</p>
    <p id="p1978276317427"><a name="p1978276317427"></a><a name="p1978276317427"></a>Valid value:</p>
    <p id="p3825082612023"><a name="p3825082612023"></a><a name="p3825082612023"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row9307971"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>availabilityZone</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p533144"><a name="p533144"></a><a name="p533144"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8297278"><a name="p8297278"></a><a name="p8297278"></a>Specifies the AZ ID.</p>
    <p id="p6574938217430"><a name="p6574938217430"></a><a name="p6574938217430"></a>Valid value:</p>
    <p id="p49296060141410"><a name="p49296060141410"></a><a name="p49296060141410"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row51313205"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p52874399"><a name="p52874399"></a><a name="p52874399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p54967961"><a name="p54967961"></a><a name="p54967961"></a>Specifies the VPC ID. For details about how to obtain this parameter value, see section "Virtual Private Cloud" in the <em id="i842352697165629"><a name="i842352697165629"></a><a name="i842352697165629"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p23219884"><a name="p23219884"></a><a name="p23219884"></a>Valid value:</p>
    <p id="p48962966144451"><a name="p48962966144451"></a><a name="p48962966144451"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row15861880"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p9743886"><a name="p9743886"></a><a name="p9743886"></a>nics</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p42003681"><a name="p42003681"></a><a name="p42003681"></a>Dictionary data structure. For details, see <a href="#table2179128">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19042013"><a name="p19042013"></a><a name="p19042013"></a>Specifies the nics information. For details about how to obtain this parameter value, see section "Subnet" in the <em id="i1727078263"><a name="i1727078263"></a><a name="i1727078263"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row66008059"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>securityGroup</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p42208903"><a name="p42208903"></a><a name="p42208903"></a>Dictionary data structure. For details, see <a href="#table4150710">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p34431157"><a name="p34431157"></a><a name="p34431157"></a>Specifies the security group which the RDS DB instance belongs to.</p>
    <p id="p41444960"><a name="p41444960"></a><a name="p41444960"></a>For details about how to obtain this parameter value, see section "Security Group" in the <em id="i13659676"><a name="i13659676"></a><a name="i13659676"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row31320691125738"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p9447096125742"><a name="p9447096125742"></a><a name="p9447096125742"></a>dbPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p27017325125742"><a name="p27017325125742"></a><a name="p27017325125742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p40919702125742"><a name="p40919702125742"></a><a name="p40919702125742"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19914101012135"><a name="p19914101012135"></a><a name="p19914101012135"></a>Specifies the database port information.</p>
    <a name="ul10438123672912"></a><a name="ul10438123672912"></a><ul id="ul10438123672912"><li>The MySQL database port ranges from 1024 to 65535 (excluding 12017 and 33071, which are occupied by the RDS system and cannot be used).</li><li>The PostgreSQL database port ranges from 2100 to 9500.</li><li>The Microsoft SQL Server database port can be 1433 or ranges from 2100 to 9500, excluding 5355 and 5985.</li></ul>
    <p id="p6601319181417"><a name="p6601319181417"></a><a name="p6601319181417"></a>If this parameter is not set, the default value is as follows:</p>
    <a name="ul1696512278148"></a><a name="ul1696512278148"></a><ul id="ul1696512278148"><li>For MySQL databases, the default value is <strong id="b164181349202913"><a name="b164181349202913"></a><a name="b164181349202913"></a>3306</strong>.</li><li>For PostgreSQL databases, the default value is <strong id="b1632725292912"><a name="b1632725292912"></a><a name="b1632725292912"></a>5432</strong>.</li><li>For Microsoft SQL Server, the default value is <strong id="b139211955182913"><a name="b139211955182913"></a><a name="b139211955182913"></a>1433</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row37460321"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p14387121"><a name="p14387121"></a><a name="p14387121"></a>backupStrategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p24506125"><a name="p24506125"></a><a name="p24506125"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p38839134"><a name="p38839134"></a><a name="p38839134"></a>Dictionary data structure. For details, see <a href="#table49774232">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p60897649"><a name="p60897649"></a><a name="p60897649"></a>Specifies the advanced backup policy.</p>
    </td>
    </tr>
    <tr id="row33762549"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p50411912"><a name="p50411912"></a><a name="p50411912"></a>dbRtPd</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p56833109"><a name="p56833109"></a><a name="p56833109"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p40079106"><a name="p40079106"></a><a name="p40079106"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p25182135"><a name="p25182135"></a><a name="p25182135"></a>Specifies the password for user <strong id="b842352706154754"><a name="b842352706154754"></a><a name="b842352706154754"></a>root</strong> of the database.</p>
    <p id="p26487069"><a name="p26487069"></a><a name="p26487069"></a>Valid value:</p>
    <p id="p12429628144458"><a name="p12429628144458"></a><a name="p12429628144458"></a>The value cannot be empty and should contain 8 to 32 characters, including uppercase and lowercase letters, digits, and the following special characters: ~!@#%^*-_=+?</p>
    </td>
    </tr>
    <tr id="row48829755"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p62896114"><a name="p62896114"></a><a name="p62896114"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p61420436"><a name="p61420436"></a><a name="p61420436"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p8999435"><a name="p8999435"></a><a name="p8999435"></a>Dictionary data structure. For details, see <a href="#table622861661833">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p51028923"><a name="p51028923"></a><a name="p51028923"></a>Specifies the HA configuration parameters, which are used when creating primary/standby DB instances.</p>
    <div class="notice" id="note23027005161934"><a name="note23027005161934"></a><a name="note23027005161934"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p5916456161934"><a name="p5916456161934"></a><a name="p5916456161934"></a>RDS for Microsoft SQL Server does not support creating primary/standby DB instances and this parameter is not involved.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  instance field data structure description \(creating a read replica\)

    <a name="table228903751753"></a>
    <table><thead align="left"><tr id="row70524471753"><th class="cellrowborder" valign="top" width="29.330000000000002%" id="mcps1.2.5.1.1"><p id="p343772981753"><a name="p343772981753"></a><a name="p343772981753"></a><strong id="b446270986"><a name="b446270986"></a><a name="b446270986"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6%" id="mcps1.2.5.1.2"><p id="p330977911753"><a name="p330977911753"></a><a name="p330977911753"></a><strong id="b130169355"><a name="b130169355"></a><a name="b130169355"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.07%" id="mcps1.2.5.1.3"><p id="p636754041753"><a name="p636754041753"></a><a name="p636754041753"></a><strong id="b2139172576"><a name="b2139172576"></a><a name="b2139172576"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p574340811753"><a name="p574340811753"></a><a name="p574340811753"></a><strong id="b1317973372"><a name="b1317973372"></a><a name="b1317973372"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row216489991753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p87385011753"><a name="p87385011753"></a><a name="p87385011753"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p367300201753"><a name="p367300201753"></a><a name="p367300201753"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p223416761753"><a name="p223416761753"></a><a name="p223416761753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p181181003619"><a name="p181181003619"></a><a name="p181181003619"></a>Specifies the DB instance name.</p>
    <p id="p6117105368"><a name="p6117105368"></a><a name="p6117105368"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p467369331753"><a name="p467369331753"></a><a name="p467369331753"></a>Valid value:</p>
    <p id="p24429179182049"><a name="p24429179182049"></a><a name="p24429179182049"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row363844211753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p614570251753"><a name="p614570251753"></a><a name="p614570251753"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p119630961753"><a name="p119630961753"></a><a name="p119630961753"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p294867401753"><a name="p294867401753"></a><a name="p294867401753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p396157731753"><a name="p396157731753"></a><a name="p396157731753"></a>Specifies the specification ID (<strong id="b135018593298"><a name="b135018593298"></a><a name="b135018593298"></a>flavors.id</strong> in the response message in section <a href="obtaining-all-db-instance-specifications.md">Obtaining All DB Instance Specifications</a>).</p>
    <p id="p547610501753"><a name="p547610501753"></a><a name="p547610501753"></a>Valid value:</p>
    <p id="p230874081753"><a name="p230874081753"></a><a name="p230874081753"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row260045131753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p259908001753"><a name="p259908001753"></a><a name="p259908001753"></a>replicaOf</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p248800801753"><a name="p248800801753"></a><a name="p248800801753"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p20206171753"><a name="p20206171753"></a><a name="p20206171753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p294522581753"><a name="p294522581753"></a><a name="p294522581753"></a>Specifies the read replica configuration parameter. It is used to create a read replica of a primary DB instance specified by <strong id="b84235270617137"><a name="b84235270617137"></a><a name="b84235270617137"></a>replicaOf</strong></p>
    <p id="p637437301753"><a name="p637437301753"></a><a name="p637437301753"></a>Valid value:</p>
    <p id="p368226591753"><a name="p368226591753"></a><a name="p368226591753"></a>Only the primary DB instance ID is valid.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  datastore field data structure description

    <a name="table64243102"></a>
    <table><thead align="left"><tr id="row4043462"><th class="cellrowborder" valign="top" width="29.509999999999998%" id="mcps1.2.5.1.1"><p id="p59085005"><a name="p59085005"></a><a name="p59085005"></a><strong id="b561685455"><a name="b561685455"></a><a name="b561685455"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.2"><p id="p21156092"><a name="p21156092"></a><a name="p21156092"></a><strong id="b1601709326"><a name="b1601709326"></a><a name="b1601709326"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.07%" id="mcps1.2.5.1.3"><p id="p35921916"><a name="p35921916"></a><a name="p35921916"></a><strong id="b1579875191"><a name="b1579875191"></a><a name="b1579875191"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p23994101"><a name="p23994101"></a><a name="p23994101"></a><strong id="b275391717"><a name="b275391717"></a><a name="b275391717"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64473998"><td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p55011311"><a name="p55011311"></a><a name="p55011311"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p26731201"><a name="p26731201"></a><a name="p26731201"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p17743659"><a name="p17743659"></a><a name="p17743659"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p49175803141056"><a name="p49175803141056"></a><a name="p49175803141056"></a>Specifies the DB engine. Currently, the following DB engines are supported:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row40466701"><td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p56577386"><a name="p56577386"></a><a name="p56577386"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p19365543"><a name="p19365543"></a><a name="p19365543"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p25105132"><a name="p25105132"></a><a name="p25105132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p20249826"><a name="p20249826"></a><a name="p20249826"></a>Specifies the database version.</p>
    <a name="ul2128855618558"></a><a name="ul2128855618558"></a><ul id="ul2128855618558"><li>MySQL databases support 5.6 and 5.7. Example value: 5.7</li><li>PostgreSQL databases support 9.5, 9.6, 10, and 11. Example value: 9.6</li><li>Microsoft SQL Server databases support 2014 SP2 SE. Example value: 2014_SP2_SE</li></ul>
    <p id="p2139751518103"><a name="p2139751518103"></a><a name="p2139751518103"></a>For details about supported database versions, see section <a href="database-version-queries.md">Database Version Queries</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  volume field data structure description

    <a name="table10656503"></a>
    <table><thead align="left"><tr id="row5847780"><th class="cellrowborder" valign="top" width="29.32%" id="mcps1.2.5.1.1"><p id="p3908185"><a name="p3908185"></a><a name="p3908185"></a><strong id="b78191114"><a name="b78191114"></a><a name="b78191114"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.2"><p id="p48127554"><a name="p48127554"></a><a name="p48127554"></a><strong id="b1637062177"><a name="b1637062177"></a><a name="b1637062177"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.07%" id="mcps1.2.5.1.3"><p id="p6017800"><a name="p6017800"></a><a name="p6017800"></a><strong id="b1804815712"><a name="b1804815712"></a><a name="b1804815712"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p17679762"><a name="p17679762"></a><a name="p17679762"></a><strong id="b1163885549"><a name="b1163885549"></a><a name="b1163885549"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22774600"><td class="cellrowborder" valign="top" width="29.32%" headers="mcps1.2.5.1.1 "><p id="p32803348"><a name="p32803348"></a><a name="p32803348"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p39825499"><a name="p39825499"></a><a name="p39825499"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p4640007"><a name="p4640007"></a><a name="p4640007"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40296320"><a name="p40296320"></a><a name="p40296320"></a>Specifies the volume type.</p>
    <p id="p27122565"><a name="p27122565"></a><a name="p27122565"></a>Its value can be any of the following and is case-sensitive:</p>
    <a name="ul06211247141917"></a><a name="ul06211247141917"></a><ul id="ul06211247141917"><li><strong id="b49281844163118"><a name="b49281844163118"></a><a name="b49281844163118"></a>COMMON</strong>: indicates the SATA type.</li><li><strong id="b175251655173117"><a name="b175251655173117"></a><a name="b175251655173117"></a>ULTRAHIGH</strong>: indicates the SSD type.</li></ul>
    </td>
    </tr>
    <tr id="row42343927"><td class="cellrowborder" valign="top" width="29.32%" headers="mcps1.2.5.1.1 "><p id="p7306053"><a name="p7306053"></a><a name="p7306053"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p54919424"><a name="p54919424"></a><a name="p54919424"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p19288335"><a name="p19288335"></a><a name="p19288335"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p18851291"><a name="p18851291"></a><a name="p18851291"></a>Specifies the volume size.</p>
    <p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>Its value range is from 40 GB to 4000 GB. The value must be a multiple of 10.</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    <div class="note" id="note02685513325"><a name="note02685513325"></a><a name="note02685513325"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p385416153310"><a name="p385416153310"></a><a name="p385416153310"></a>For read replicas, this parameter is invalid. The volume size is the same as that of the primary DB instance by default.</p>
    <p id="p726165518328"><a name="p726165518328"></a><a name="p726165518328"></a></p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  nics field data structure description

    <a name="table2179128"></a>
    <table><thead align="left"><tr id="row28646034"><th class="cellrowborder" valign="top" width="29.09%" id="mcps1.2.5.1.1"><p id="p38627455"><a name="p38627455"></a><a name="p38627455"></a><strong id="b1779892109"><a name="b1779892109"></a><a name="b1779892109"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.98%" id="mcps1.2.5.1.2"><p id="p41816140"><a name="p41816140"></a><a name="p41816140"></a><strong id="b179863744"><a name="b179863744"></a><a name="b179863744"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.93%" id="mcps1.2.5.1.3"><p id="p31664161"><a name="p31664161"></a><a name="p31664161"></a><strong id="b1352251678"><a name="b1352251678"></a><a name="b1352251678"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14660263"><a name="p14660263"></a><a name="p14660263"></a><strong id="b1811461289"><a name="b1811461289"></a><a name="b1811461289"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46630661"><td class="cellrowborder" valign="top" width="29.09%" headers="mcps1.2.5.1.1 "><p id="p18987236"><a name="p18987236"></a><a name="p18987236"></a>subnetId</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.2.5.1.2 "><p id="p61571180"><a name="p61571180"></a><a name="p61571180"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.93%" headers="mcps1.2.5.1.3 "><p id="p21209668"><a name="p21209668"></a><a name="p21209668"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40261524"><a name="p40261524"></a><a name="p40261524"></a>Specifies the network ID of the subnet obtained from VPC.</p>
    <p id="p26809401"><a name="p26809401"></a><a name="p26809401"></a>Valid value:</p>
    <p id="p36848008144522"><a name="p36848008144522"></a><a name="p36848008144522"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  securityGroup field data structure description

    <a name="table4150710"></a>
    <table><thead align="left"><tr id="row37742617"><th class="cellrowborder" valign="top" width="29.13%" id="mcps1.2.5.1.1"><p id="p37253141"><a name="p37253141"></a><a name="p37253141"></a><strong id="b1779777190"><a name="b1779777190"></a><a name="b1779777190"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.2"><p id="p64714441"><a name="p64714441"></a><a name="p64714441"></a><strong id="b1800196941"><a name="b1800196941"></a><a name="b1800196941"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.32%" id="mcps1.2.5.1.3"><p id="p7378398"><a name="p7378398"></a><a name="p7378398"></a><strong id="b511063084"><a name="b511063084"></a><a name="b511063084"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p60779388"><a name="p60779388"></a><a name="p60779388"></a><strong id="b421240097"><a name="b421240097"></a><a name="b421240097"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24183370"><td class="cellrowborder" valign="top" width="29.13%" headers="mcps1.2.5.1.1 "><p id="p12695920"><a name="p12695920"></a><a name="p12695920"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.2 "><p id="p21736599"><a name="p21736599"></a><a name="p21736599"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.2.5.1.3 "><p id="p15834086"><a name="p15834086"></a><a name="p15834086"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7492614"><a name="p7492614"></a><a name="p7492614"></a>Valid value:</p>
    <p id="p48836202144526"><a name="p48836202144526"></a><a name="p48836202144526"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  backupStrategy field data structure description

    <a name="table49774232"></a>
    <table><thead align="left"><tr id="row48589216"><th class="cellrowborder" valign="top" width="29.330000000000002%" id="mcps1.2.5.1.1"><p id="p43412436"><a name="p43412436"></a><a name="p43412436"></a><strong id="b1067534665"><a name="b1067534665"></a><a name="b1067534665"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.16%" id="mcps1.2.5.1.2"><p id="p26746391"><a name="p26746391"></a><a name="p26746391"></a><strong id="b82261719"><a name="b82261719"></a><a name="b82261719"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.51%" id="mcps1.2.5.1.3"><p id="p18974100"><a name="p18974100"></a><a name="p18974100"></a><strong id="b1113332583"><a name="b1113332583"></a><a name="b1113332583"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p60507121"><a name="p60507121"></a><a name="p60507121"></a><strong id="b855664940"><a name="b855664940"></a><a name="b855664940"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13243689"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p66105898"><a name="p66105898"></a><a name="p66105898"></a>startTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.2.5.1.2 "><p id="p52977523"><a name="p52977523"></a><a name="p52977523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.51%" headers="mcps1.2.5.1.3 "><p id="p63321005"><a name="p63321005"></a><a name="p63321005"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40942168155958"><a name="p40942168155958"></a><a name="p40942168155958"></a>Specifies the backup start time that has been set.</p>
    <p id="p57223682"><a name="p57223682"></a><a name="p57223682"></a>Valid value:</p>
    <p id="p29612155144531"><a name="p29612155144531"></a><a name="p29612155144531"></a>The value cannot be empty. It must use the hh:mm:ss format and must be valid. The time is in the UTC format.</p>
    </td>
    </tr>
    <tr id="row41459726"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p2794650"><a name="p2794650"></a><a name="p2794650"></a>keepDays</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.2.5.1.2 "><p id="p25040094"><a name="p25040094"></a><a name="p25040094"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.51%" headers="mcps1.2.5.1.3 "><p id="p14981763"><a name="p14981763"></a><a name="p14981763"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p30482871191015"><a name="p30482871191015"></a><a name="p30482871191015"></a>Specifies the number of days to retain the generated backup files.</p>
    <p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>The value range is from 0 to 732. If this parameter is not specified or set to <strong id="b842352706112318"><a name="b842352706112318"></a><a name="b842352706112318"></a>0</strong>, the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  ha field data structure description

    <a name="table622861661833"></a>
    <table><thead align="left"><tr id="row141379661833"><th class="cellrowborder" valign="top" width="29.7%" id="mcps1.2.5.1.1"><p id="p43246301833"><a name="p43246301833"></a><a name="p43246301833"></a><strong id="b445308850"><a name="b445308850"></a><a name="b445308850"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6%" id="mcps1.2.5.1.2"><p id="p147507341833"><a name="p147507341833"></a><a name="p147507341833"></a><strong id="b799218910"><a name="b799218910"></a><a name="b799218910"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.889999999999997%" id="mcps1.2.5.1.3"><p id="p539587821833"><a name="p539587821833"></a><a name="p539587821833"></a><strong id="b181171029"><a name="b181171029"></a><a name="b181171029"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.81%" id="mcps1.2.5.1.4"><p id="p85852311833"><a name="p85852311833"></a><a name="p85852311833"></a><strong id="b1606593092"><a name="b1606593092"></a><a name="b1606593092"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row243151121833"><td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.5.1.1 "><p id="p233670901833"><a name="p233670901833"></a><a name="p233670901833"></a>enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p136861651833"><a name="p136861651833"></a><a name="p136861651833"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.5.1.3 "><p id="p348375601833"><a name="p348375601833"></a><a name="p348375601833"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.5.1.4 "><p id="p32700831833"><a name="p32700831833"></a><a name="p32700831833"></a>Specifies the HA configuration parameter.</p>
    <p id="p294307511833"><a name="p294307511833"></a><a name="p294307511833"></a>Valid value:</p>
    <p id="p54112632144538"><a name="p54112632144538"></a><a name="p54112632144538"></a>The value is <strong id="b842352706164817"><a name="b842352706164817"></a><a name="b842352706164817"></a>true</strong> or <strong id="b842352706164826"><a name="b842352706164826"></a><a name="b842352706164826"></a>false</strong>. The value <strong id="b842352706164830"><a name="b842352706164830"></a><a name="b842352706164830"></a>true</strong> indicates creating primary/standby DB instances. The value <strong id="b765135452113640"><a name="b765135452113640"></a><a name="b765135452113640"></a>false</strong> indicates creating a single DB instance.</p>
    </td>
    </tr>
    <tr id="row472905471833"><td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.5.1.1 "><p id="p53291281833"><a name="p53291281833"></a><a name="p53291281833"></a>replicationMode</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p290062461833"><a name="p290062461833"></a><a name="p290062461833"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.5.1.3 "><p id="p6957001833"><a name="p6957001833"></a><a name="p6957001833"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.5.1.4 "><p id="p6707901911827"><a name="p6707901911827"></a><a name="p6707901911827"></a>Specifies the replication mode for the standby DB instance.</p>
    <p id="p6684026611827"><a name="p6684026611827"></a><a name="p6684026611827"></a>The value cannot be empty.</p>
    <a name="ul4535249811827"></a><a name="ul4535249811827"></a><ul id="ul4535249811827"><li>For MySQL, the value is <strong id="b842352706165650"><a name="b842352706165650"></a><a name="b842352706165650"></a>async</strong> or <strong id="b842352706165654"><a name="b842352706165654"></a><a name="b842352706165654"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b1658460331"><a name="b1658460331"></a><a name="b1658460331"></a>async</strong> or <strong id="b246566107"><a name="b246566107"></a><a name="b246566107"></a>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong id="b1084866521183314"><a name="b1084866521183314"></a><a name="b1084866521183314"></a>sync</strong>.</li></ul>
    <div class="note" id="note6414722611827"><a name="note6414722611827"></a><a name="note6414722611827"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul4045412711827"></a><a name="ul4045412711827"></a><ul id="ul4045412711827"><li><strong id="b842352706105954"><a name="b842352706105954"></a><a name="b842352706105954"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b842352706164020"><a name="b842352706164020"></a><a name="b842352706164020"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b13384211081105"><a name="b13384211081105"></a><a name="b13384211081105"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    Creating a single DB instance:

    ```
    {
        "instance": {
            "name": "trove-instance-rep2",
            "datastore": {
                "type": "MySQL",
                "version": "5.7"
            },
            "flavorRef": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "region": "eu-de",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "dbPort": 3306,
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            },
            "dbRtPd": "Test@123"
        }
    }
    ```

    Creating primary/standby DB instances:

    ```
    {
        "instance": {
            "name": "trove-instance-ha",
            "datastore": {
                "type": "MySQL",
                "version": "5.7"
            },
            "flavorRef": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "region": "eu-de",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "dbPort": 3306,
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            },
            "dbRtPd": "Test@123",
            "ha": {
                "enable": true,
                "replicationMode": "async"
            }
        }
    }
    ```

    Creating a read replica:

    ```
    {
        "instance": {
            "name": "trove-instance-replica2",
            "flavorRef": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
            "replicaOf": "373af3b8-8f44-44f6-bb90-85f1c32c50d6"
        }
    }
    ```


## Normal Response<a name="section36749739"></a>

-   Parameter description

    **Table  11**  Parameter description

    <a name="table17474517"></a>
    <table><thead align="left"><tr id="row16146366"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="p32787233"><a name="p32787233"></a><a name="p32787233"></a><strong id="b1135864208"><a name="b1135864208"></a><a name="b1135864208"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.15%" id="mcps1.2.4.1.2"><p id="p38520254"><a name="p38520254"></a><a name="p38520254"></a><strong id="b1385659541"><a name="b1385659541"></a><a name="b1385659541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.52%" id="mcps1.2.4.1.3"><p id="p33132859"><a name="p33132859"></a><a name="p33132859"></a><strong id="b2056931038"><a name="b2056931038"></a><a name="b2056931038"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66515904"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p19079158"><a name="p19079158"></a><a name="p19079158"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.15%" headers="mcps1.2.4.1.2 "><p id="p1907972"><a name="p1907972"></a><a name="p1907972"></a>Dictionary data structure. For details, see <a href="#table27245651">Table 12</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.3 "><p id="p48735027"><a name="p48735027"></a><a name="p48735027"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  12**  instance field data structure description

    <a name="table27245651"></a>
    <table><thead align="left"><tr id="row47625437"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p32455223"><a name="p32455223"></a><a name="p32455223"></a><strong id="b1910676470"><a name="b1910676470"></a><a name="b1910676470"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p11627434"><a name="p11627434"></a><a name="p11627434"></a><strong id="b1821282506"><a name="b1821282506"></a><a name="b1821282506"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2298077"><a name="p2298077"></a><a name="p2298077"></a><strong id="b1594643084"><a name="b1594643084"></a><a name="b1594643084"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51926520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45298596"><a name="p45298596"></a><a name="p45298596"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45307656"><a name="p45307656"></a><a name="p45307656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Indicates the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row56907078"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46070597"><a name="p46070597"></a><a name="p46070597"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40730901"><a name="p40730901"></a><a name="p40730901"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10868702"><a name="p10868702"></a><a name="p10868702"></a>Indicates the DB instance status. The value is <span class="parmvalue" id="parmvalue2029132012164130"><a name="parmvalue2029132012164130"></a><a name="parmvalue2029132012164130"></a><b>BUILD</b></span>.</p>
    </td>
    </tr>
    <tr id="row30709455"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4437887"><a name="p4437887"></a><a name="p4437887"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p23924539"><a name="p23924539"></a><a name="p23924539"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58839532"><a name="p58839532"></a><a name="p58839532"></a>Indicates the created DB instance name.</p>
    </td>
    </tr>
    <tr id="row59793748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11455439"><a name="p11455439"></a><a name="p11455439"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55475379"><a name="p55475379"></a><a name="p55475379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64320678"><a name="p64320678"></a><a name="p64320678"></a>Indicates the creation time in the "yyyy-mm-dd Thh:mm:ssZ" format.</p>
    <p id="p6642150175824"><a name="p6642150175824"></a><a name="p6642150175824"></a><strong id="b842352706151812"><a name="b842352706151812"></a><a name="b842352706151812"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706153833"><a name="b842352706153833"></a><a name="b842352706153833"></a>Z</strong> indicates the time zone offset.</p>
    <div class="note" id="note5126817175844"><a name="note5126817175844"></a><a name="note5126817175844"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p46141354175844"><a name="p46141354175844"></a><a name="p46141354175844"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row42592467"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27437792"><a name="p27437792"></a><a name="p27437792"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7868661"><a name="p7868661"></a><a name="p7868661"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33381819"><a name="p33381819"></a><a name="p33381819"></a>Indicates the DB instance connection address. It is a blank string.</p>
    </td>
    </tr>
    <tr id="row32000920"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41937705"><a name="p41937705"></a><a name="p41937705"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41510976"><a name="p41510976"></a><a name="p41510976"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p373123731890"><a name="p373123731890"></a><a name="p373123731890"></a>Indicates the DB instance type, which can be <strong id="b84235270617352"><a name="b84235270617352"></a><a name="b84235270617352"></a>master</strong> or <strong id="b84235270617355"><a name="b84235270617355"></a><a name="b84235270617355"></a>readreplica</strong>.</p>
    </td>
    </tr>
    <tr id="row32924936175949"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27888975175949"><a name="p27888975175949"></a><a name="p27888975175949"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44414535175949"><a name="p44414535175949"></a><a name="p44414535175949"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40807567175949"><a name="p40807567175949"></a><a name="p40807567175949"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row62512728"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30366184"><a name="p30366184"></a><a name="p30366184"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p43741849"><a name="p43741849"></a><a name="p43741849"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53428882"><a name="p53428882"></a><a name="p53428882"></a>Indicates the updated time, which is the same as <strong id="b8423527061176"><a name="b8423527061176"></a><a name="b8423527061176"></a>created</strong>.</p>
    <div class="note" id="note542057061864"><a name="note542057061864"></a><a name="note542057061864"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p180893121864"><a name="p180893121864"></a><a name="p180893121864"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row11097898"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26514531"><a name="p26514531"></a><a name="p26514531"></a>availabilityZone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p193401"><a name="p193401"></a><a name="p193401"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15665491"><a name="p15665491"></a><a name="p15665491"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row785288110273"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p356707210273"><a name="p356707210273"></a><a name="p356707210273"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2049740210273"><a name="p2049740210273"></a><a name="p2049740210273"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4967688510273"><a name="p4967688510273"></a><a name="p4967688510273"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row6771693"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11636265"><a name="p11636265"></a><a name="p11636265"></a>nics</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3013405"><a name="p3013405"></a><a name="p3013405"></a>Dictionary data structure. For details, see <a href="#table41614513165139">Table 13</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p474926017024"><a name="p474926017024"></a><a name="p474926017024"></a>Indicates the nics information.</p>
    </td>
    </tr>
    <tr id="row49289224"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33004241"><a name="p33004241"></a><a name="p33004241"></a>securityGroup</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56097870"><a name="p56097870"></a><a name="p56097870"></a>Dictionary data structure. For details, see <a href="#table255609017350">Table 14</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47633640"><a name="p47633640"></a><a name="p47633640"></a>Indicates the security group information.</p>
    </td>
    </tr>
    <tr id="row26049579"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29641146"><a name="p29641146"></a><a name="p29641146"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52122650"><a name="p52122650"></a><a name="p52122650"></a>Dictionary data structure. For details, see <a href="#table223791861780">Table 15</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61185139"><a name="p61185139"></a><a name="p61185139"></a>Indicates the DB instance specifications.</p>
    </td>
    </tr>
    <tr id="row13795340"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43680716"><a name="p43680716"></a><a name="p43680716"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p48477080"><a name="p48477080"></a><a name="p48477080"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34329433"><a name="p34329433"></a><a name="p34329433"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row9414870143634"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59587820143645"><a name="p59587820143645"></a><a name="p59587820143645"></a>dbPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61884126143645"><a name="p61884126143645"></a><a name="p61884126143645"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46558333143645"><a name="p46558333143645"></a><a name="p46558333143645"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row40529449"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p482489891182"><a name="p482489891182"></a><a name="p482489891182"></a>dataStoreInfo</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p245175991182"><a name="p245175991182"></a><a name="p245175991182"></a>Dictionary data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p573542861182"><a name="p573542861182"></a><a name="p573542861182"></a>Indicates the database information.</p>
    <div class="note" id="note668950831190"><a name="note668950831190"></a><a name="note668950831190"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p651848381190"><a name="p651848381190"></a><a name="p651848381190"></a>The value is <strong id="b842352706141412"><a name="b842352706141412"></a><a name="b842352706141412"></a>null</strong> when the DB instance is being created. After the instance is created, the value is not <strong id="b889385641141721"><a name="b889385641141721"></a><a name="b889385641141721"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row2353067711815"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6520993211819"><a name="p6520993211819"></a><a name="p6520993211819"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4751311611819"><a name="p4751311611819"></a><a name="p4751311611819"></a>Dictionary data structure. For details, see <a href="#table3492062317170">Table 16</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p694709518538"><a name="p694709518538"></a><a name="p694709518538"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    <tr id="row56982912"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p186985881187"><a name="p186985881187"></a><a name="p186985881187"></a>backupStrategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p381906881187"><a name="p381906881187"></a><a name="p381906881187"></a>Dictionary data structure. For details, see <a href="#table18267654155052">Table 18</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64380241187"><a name="p64380241187"></a><a name="p64380241187"></a>Indicates the backup policy.</p>
    </td>
    </tr>
    <tr id="row3430840811031"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5489247911055"><a name="p5489247911055"></a><a name="p5489247911055"></a>slaveId</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1710580811055"><a name="p1710580811055"></a><a name="p1710580811055"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4339317311055"><a name="p4339317311055"></a><a name="p4339317311055"></a>It is returned only when you create primary/standby DB instances.</p>
    </td>
    </tr>
    <tr id="row810597210337"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p32354858103312"><a name="p32354858103312"></a><a name="p32354858103312"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3497827103312"><a name="p3497827103312"></a><a name="p3497827103312"></a>Dictionary data structure. For details, see <a href="#table16318932171721">Table 19</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14888569103312"><a name="p14888569103312"></a><a name="p14888569103312"></a>Indicates the primary/standby DB instance information. It is returned only when you create primary/standby DB instances.</p>
    </td>
    </tr>
    <tr id="row19867487"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p65762630"><a name="p65762630"></a><a name="p65762630"></a>replica_of</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25172842"><a name="p25172842"></a><a name="p25172842"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25734322"><a name="p25734322"></a><a name="p25734322"></a>Same as the request parameter. It is returned only when you create a read replica.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  13**  nics field data structure description

    <a name="table41614513165139"></a>
    <table><thead align="left"><tr id="row61695746165139"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p30976535165713"><a name="p30976535165713"></a><a name="p30976535165713"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p26071408165713"><a name="p26071408165713"></a><a name="p26071408165713"></a><strong id="b1103420156"><a name="b1103420156"></a><a name="b1103420156"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p31409338165713"><a name="p31409338165713"></a><a name="p31409338165713"></a><strong id="b1476048746"><a name="b1476048746"></a><a name="b1476048746"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50187499165139"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38655590165139"><a name="p38655590165139"></a><a name="p38655590165139"></a>subnetId</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44095090165139"><a name="p44095090165139"></a><a name="p44095090165139"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14932534165139"><a name="p14932534165139"></a><a name="p14932534165139"></a>Indicates the network ID of the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  14**  securityGroup field data structure description

    <a name="table255609017350"></a>
    <table><thead align="left"><tr id="row6077622417350"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2392711017350"><a name="p2392711017350"></a><a name="p2392711017350"></a><strong id="b2096455507"><a name="b2096455507"></a><a name="b2096455507"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5904772817350"><a name="p5904772817350"></a><a name="p5904772817350"></a><strong id="b1431903871"><a name="b1431903871"></a><a name="b1431903871"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1813664617350"><a name="p1813664617350"></a><a name="p1813664617350"></a><strong id="b2090291114"><a name="b2090291114"></a><a name="b2090291114"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5978225817350"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1052469717350"><a name="p1052469717350"></a><a name="p1052469717350"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4719414917350"><a name="p4719414917350"></a><a name="p4719414917350"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6462975817350"><a name="p6462975817350"></a><a name="p6462975817350"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  15**  flavor field data structure description

    <a name="table223791861780"></a>
    <table><thead align="left"><tr id="row477223291780"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p403034631780"><a name="p403034631780"></a><a name="p403034631780"></a><strong id="b1543007270"><a name="b1543007270"></a><a name="b1543007270"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p433550451780"><a name="p433550451780"></a><a name="p433550451780"></a><strong id="b819202093"><a name="b819202093"></a><a name="b819202093"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p220977231780"><a name="p220977231780"></a><a name="p220977231780"></a><strong id="b1107720648"><a name="b1107720648"></a><a name="b1107720648"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row450851381780"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p280175531780"><a name="p280175531780"></a><a name="p280175531780"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p548293451780"><a name="p548293451780"></a><a name="p548293451780"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p119919781780"><a name="p119919781780"></a><a name="p119919781780"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  16**  extendparam field data structure description

    <a name="table3492062317170"></a>
    <table><thead align="left"><tr id="row3304075417170"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5905541217170"><a name="p5905541217170"></a><a name="p5905541217170"></a><strong id="b96307093"><a name="b96307093"></a><a name="b96307093"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1875905417170"><a name="p1875905417170"></a><a name="p1875905417170"></a><strong id="b512168666"><a name="b512168666"></a><a name="b512168666"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p4308842517170"><a name="p4308842517170"></a><a name="p4308842517170"></a><strong id="b2141051311"><a name="b2141051311"></a><a name="b2141051311"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50154917170"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4062547217170"><a name="p4062547217170"></a><a name="p4062547217170"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19575195171837"><a name="p19575195171837"></a><a name="p19575195171837"></a>List data structure. For details, see <a href="#table66691786171712">Table 17</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3219143118355"><a name="p3219143118355"></a><a name="p3219143118355"></a>Indicates the returned <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  17**  jobs field data structure description

    <a name="table66691786171712"></a>
    <table><thead align="left"><tr id="row8628012171712"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p27780390171712"><a name="p27780390171712"></a><a name="p27780390171712"></a><strong id="b1965093237"><a name="b1965093237"></a><a name="b1965093237"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p35619108171712"><a name="p35619108171712"></a><a name="p35619108171712"></a><strong id="b747775651"><a name="b747775651"></a><a name="b747775651"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p66575503171712"><a name="p66575503171712"></a><a name="p66575503171712"></a><strong id="b1014433560"><a name="b1014433560"></a><a name="b1014433560"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23906638171712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57389514171712"><a name="p57389514171712"></a><a name="p57389514171712"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66545816171941"><a name="p66545816171941"></a><a name="p66545816171941"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6182355918413"><a name="p6182355918413"></a><a name="p6182355918413"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  18**  backupStrategy field data structure description

    <a name="table18267654155052"></a>
    <table><thead align="left"><tr id="row10891999155052"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p9836690155052"><a name="p9836690155052"></a><a name="p9836690155052"></a><strong id="b1551871547"><a name="b1551871547"></a><a name="b1551871547"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p58574463155052"><a name="p58574463155052"></a><a name="p58574463155052"></a><strong id="b2032987277"><a name="b2032987277"></a><a name="b2032987277"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p46911052155052"><a name="p46911052155052"></a><a name="p46911052155052"></a><strong id="b1934094364"><a name="b1934094364"></a><a name="b1934094364"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41698849155052"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22163623155052"><a name="p22163623155052"></a><a name="p22163623155052"></a>startTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50423045155052"><a name="p50423045155052"></a><a name="p50423045155052"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60186704155531"><a name="p60186704155531"></a><a name="p60186704155531"></a>Indicates the backup start time that has been set. The backup task will be triggered within one hour after the backup start time.</p>
    </td>
    </tr>
    <tr id="row21085930155133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30238783155133"><a name="p30238783155133"></a><a name="p30238783155133"></a><span id="ph36692851155324"><a name="ph36692851155324"></a><a name="ph36692851155324"></a>keepDays</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p33422344155133"><a name="p33422344155133"></a><a name="p33422344155133"></a><span id="ph40947182155522"><a name="ph40947182155522"></a><a name="ph40947182155522"></a>Int</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23098270155542"><a name="p23098270155542"></a><a name="p23098270155542"></a>Indicates the number of days to retain the generated backup files.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  19**  ha field data structure description

    <a name="table16318932171721"></a>
    <table><thead align="left"><tr id="row4195882171721"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p4322179171721"><a name="p4322179171721"></a><a name="p4322179171721"></a><strong id="b1664211329"><a name="b1664211329"></a><a name="b1664211329"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p14552188171721"><a name="p14552188171721"></a><a name="p14552188171721"></a><strong id="b1773223076"><a name="b1773223076"></a><a name="b1773223076"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p37876541171721"><a name="p37876541171721"></a><a name="p37876541171721"></a><strong id="b1937211688"><a name="b1937211688"></a><a name="b1937211688"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48100975171721"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3864889171721"><a name="p3864889171721"></a><a name="p3864889171721"></a>replicationMode</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44620612171721"><a name="p44620612171721"></a><a name="p44620612171721"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57499832171721"><a name="p57499832171721"></a><a name="p57499832171721"></a>Indicates the replication mode for the standby DB instance. Same as the request parameter.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    Creating a single DB instance:

    ```
    {
        "instance": {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "",
            "hostname": "",
            "type": "master",
            "region": "eu-de",
            "updated": "",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "dbPort": 3306,
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dataStoreInfo": null,
            "extendparam": {
                "jobs": [
                    {
                        "id": "ff8080815564ddf5015564f64a560024"
                    }
                ]
            },
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            }
        }
    }
    ```

    Creating primary/standby DB instances:

    ```
    {
        "instance": {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "",
            "hostname": "",
            "type": "master",
            "region": "eu-de",
            "updated": "",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dbPort": 3306,
            "dataStoreInfo": null,
            "extendparam": {
                "jobs": [
                    {
                        "id": "ff8080815564ddf5015564f64a560024"
                    },
                    {
                        "id": "ae3081675564ddf5357564f64a560025"
                    }
                ]
            },
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            },
            "slaveId": "9405d8b8-a87d-4531-bd3a-e504c8434281",
            "ha": {
                "replicationMode": "async"
            }
        }
    }
    ```

    Creating a read replica:

    ```
    {
        "instance": {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "",
            "hostname": "",
            "type": "readreplica",
            "region": "eu-de",
            "updated": "",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dbPort": 3306,
            "dataStoreInfo": null,
            "extendparam": {
                "jobs": [
                    {
                        "id": "ff8080815564ddf5015564f64a560024"
                    }
                ]
            },
            "replica_of": "252f11f1-2912-4c06-be55-1999bde659c5"
        }
    }
    ```


## Abnormal Response<a name="section62312200"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

