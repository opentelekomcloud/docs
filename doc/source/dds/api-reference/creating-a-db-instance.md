# Creating a DB Instance<a name="dds_api_0020"></a>

## Function<a name="section4284989"></a>

This API is used to create cluster and replica set instances.

## URI<a name="section38564907"></a>

-   URI format

    POST /v3/\{project\_id\}/instances

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.810000000000002%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.449999999999996%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b2889154219311"><a name="b2889154219311"></a><a name="b2889154219311"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="section11539844"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="29.520000000000003%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b842352706102346_5_1"><a name="b842352706102346_5_1"></a><a name="b842352706102346_5_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.060000000000002%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b842352706164541_3_1"><a name="b842352706164541_3_1"></a><a name="b842352706164541_3_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p829918354016"><a name="p829918354016"></a><a name="p829918354016"></a><strong id="b452214511319"><a name="b452214511319"></a><a name="b452214511319"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p51611184"><a name="p51611184"></a><a name="p51611184"></a>Specifies the DB instance name. The DB instance name of the same DB engine is unique for the same tenant.</p>
    <p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>The value must be 4 to 64 characters in length and start with a letter (from A to Z or from a to z). It is case-sensitive and can contain only letters, digits (from 0 to 9), hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row56760689"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p19797588"><a name="p19797588"></a><a name="p19797588"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p585814343514"><a name="p585814343514"></a><a name="p585814343514"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58520811"><a name="p58520811"></a><a name="p58520811"></a>Specifies the database information. For more information, see <a href="#table228903751753">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row16540805"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p64736823"><a name="p64736823"></a><a name="p64736823"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p40344576"><a name="p40344576"></a><a name="p40344576"></a>Specifies the region ID.</p>
    <p id="p3825082612023"><a name="p3825082612023"></a><a name="p3825082612023"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row9307971"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p533144"><a name="p533144"></a><a name="p533144"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p122956256251"><a name="p122956256251"></a><a name="p122956256251"></a>Specifies the AZ ID.</p>
    <p id="p49296060141410"><a name="p49296060141410"></a><a name="p49296060141410"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row51313205"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p52874399"><a name="p52874399"></a><a name="p52874399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p54967961"><a name="p54967961"></a><a name="p54967961"></a>Specifies the VPC ID. For details about how to obtain this parameter value, see section "Virtual Private Cloud" in the <em id="i842352697165629_1"><a name="i842352697165629_1"></a><a name="i842352697165629_1"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p23219884"><a name="p23219884"></a><a name="p23219884"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row15861880"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p9743886"><a name="p9743886"></a><a name="p9743886"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p13242114155510"><a name="p13242114155510"></a><a name="p13242114155510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19042013"><a name="p19042013"></a><a name="p19042013"></a>Specifies the subnet ID. For details about how to obtain this parameter value, see section "Subnet" in the <em id="i842352697165629_3"><a name="i842352697165629_3"></a><a name="i842352697165629_3"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row66008059"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p1376611710555"><a name="p1376611710555"></a><a name="p1376611710555"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p2098817965512"><a name="p2098817965512"></a><a name="p2098817965512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p34431157"><a name="p34431157"></a><a name="p34431157"></a>Specifies the ID of the security group where a specified DB instance belongs to.</p>
    <p id="p41444960"><a name="p41444960"></a><a name="p41444960"></a>For details about how to obtain this parameter value, see section "Security Group" in the <em id="i842352697165629_5"><a name="i842352697165629_5"></a><a name="i842352697165629_5"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row159113725612"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p164189456567"><a name="p164189456567"></a><a name="p164189456567"></a>password</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p34185452568"><a name="p34185452568"></a><a name="p34185452568"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p1041814515560"><a name="p1041814515560"></a><a name="p1041814515560"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14418145185610"><a name="p14418145185610"></a><a name="p14418145185610"></a>Specifies the database password.</p>
    <p id="p26487069"><a name="p26487069"></a><a name="p26487069"></a>The value must be 8 to 32 characters in length and contain uppercase letters (A to Z), lowercase letters (a to z), digits (0 to 9), and special characters, such as ~!@#%^*-_=+?</p>
    <p id="p12429628144458"><a name="p12429628144458"></a><a name="p12429628144458"></a>You are advised to enter a strong password to improve security, preventing security risks such as brute force cracking.</p>
    </td>
    </tr>
    <tr id="row166071201577"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p16918122175716"><a name="p16918122175716"></a><a name="p16918122175716"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p39184275719"><a name="p39184275719"></a><a name="p39184275719"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p09181214570"><a name="p09181214570"></a><a name="p09181214570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p091822175717"><a name="p091822175717"></a><a name="p091822175717"></a>Specifies the key ID used for disk encryption. The string must comply with UUID regular expression rules. </p>
    <p id="p59182025571"><a name="p59182025571"></a><a name="p59182025571"></a>If this parameter is not transferred, disk encryption is not performed.</p>
    </td>
    </tr>
    <tr id="row33762549"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p7287161811578"><a name="p7287161811578"></a><a name="p7287161811578"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p72872184576"><a name="p72872184576"></a><a name="p72872184576"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p132871018165719"><a name="p132871018165719"></a><a name="p132871018165719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p142871818175710"><a name="p142871818175710"></a><a name="p142871818175710"></a>Specifies the instance type. Cluster and replica set instances are supported.</p>
    <p id="p1228716183574"><a name="p1228716183574"></a><a name="p1228716183574"></a>Valid value:</p>
    <a name="ul358318483493"></a><a name="ul358318483493"></a><ul id="ul358318483493"><li>Sharding</li><li>ReplicaSet</li></ul>
    </td>
    </tr>
    <tr id="row48829755"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p11644203014577"><a name="p11644203014577"></a><a name="p11644203014577"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p2644230135711"><a name="p2644230135711"></a><a name="p2644230135711"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p57556557376"><a name="p57556557376"></a><a name="p57556557376"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p15644130115717"><a name="p15644130115717"></a><a name="p15644130115717"></a>Specifies the instance specifications. For more information, see <a href="#table94791241013">Table 4</a>.</p>
    <p id="p5644133025714"><a name="p5644133025714"></a><a name="p5644133025714"></a>For details about how to obtain the value, see the response values of <strong id="b1738412109577"><a name="b1738412109577"></a><a name="b1738412109577"></a>flavor</strong> in <a href="querying-all-db-instance-specifications.md">Querying All DB Instance Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row1289615471281"><td class="cellrowborder" valign="top" width="29.520000000000003%" headers="mcps1.2.5.1.1 "><p id="p2758135918812"><a name="p2758135918812"></a><a name="p2758135918812"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.2 "><p id="p97671759782"><a name="p97671759782"></a><a name="p97671759782"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.060000000000002%" headers="mcps1.2.5.1.3 "><p id="p1350774773916"><a name="p1350774773916"></a><a name="p1350774773916"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1793175919811"><a name="p1793175919811"></a><a name="p1793175919811"></a>Specifies the advanced backup policy. For more information, see <a href="#table15990419397">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  datastore field data structure description

    <a name="table228903751753"></a>
    <table><thead align="left"><tr id="row70524471753"><th class="cellrowborder" valign="top" width="29.330000000000002%" id="mcps1.2.5.1.1"><p id="p343772981753"><a name="p343772981753"></a><a name="p343772981753"></a><strong id="b842352706102328_9"><a name="b842352706102328_9"></a><a name="b842352706102328_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6%" id="mcps1.2.5.1.2"><p id="p330977911753"><a name="p330977911753"></a><a name="p330977911753"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.07%" id="mcps1.2.5.1.3"><p id="p636754041753"><a name="p636754041753"></a><a name="p636754041753"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p574120414014"><a name="p574120414014"></a><a name="p574120414014"></a><strong id="b348844611312"><a name="b348844611312"></a><a name="b348844611312"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row216489991753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p1521482415580"><a name="p1521482415580"></a><a name="p1521482415580"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p42146248583"><a name="p42146248583"></a><a name="p42146248583"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p13214192410581"><a name="p13214192410581"></a><a name="p13214192410581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10214162414580"><a name="p10214162414580"></a><a name="p10214162414580"></a></p>
    <p id="p5562520192718"><a name="p5562520192718"></a><a name="p5562520192718"></a>Specifies the database type. DDS Community Edition is supported. The value is <strong id="b22814210211"><a name="b22814210211"></a><a name="b22814210211"></a>DDS-Community</strong>.</p>
    </td>
    </tr>
    <tr id="row363844211753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p42144246586"><a name="p42144246586"></a><a name="p42144246586"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p162141624165815"><a name="p162141624165815"></a><a name="p162141624165815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p172142024165814"><a name="p172142024165814"></a><a name="p172142024165814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p112141824105817"><a name="p112141824105817"></a><a name="p112141824105817"></a></p>
    <p id="p68674213317"><a name="p68674213317"></a><a name="p68674213317"></a>Indicates the database version. Versions 3.2 and 3.4 are supported. The value is <strong id="b1412194516457"><a name="b1412194516457"></a><a name="b1412194516457"></a>3.2</strong> or <strong id="b448118482454"><a name="b448118482454"></a><a name="b448118482454"></a>3.4</strong>.</p>
    </td>
    </tr>
    <tr id="row260045131753"><td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.5.1.1 "><p id="p152141624175815"><a name="p152141624175815"></a><a name="p152141624175815"></a>storage_engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.2.5.1.2 "><p id="p102145249581"><a name="p102145249581"></a><a name="p102145249581"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.07%" headers="mcps1.2.5.1.3 "><p id="p1521452419586"><a name="p1521452419586"></a><a name="p1521452419586"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1072024123815"><a name="p1072024123815"></a><a name="p1072024123815"></a>Specifies the storage engine. Currently, DDS supports the WiredTiger storage engine. The value is <strong id="b13522163233219"><a name="b13522163233219"></a><a name="b13522163233219"></a>wiredTiger</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  flavor field data structure description

    <a name="table94791241013"></a>
    <table><thead align="left"><tr id="row14800249118"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1662124515111"><a name="p1662124515111"></a><a name="p1662124515111"></a><strong id="b430235112379"><a name="b430235112379"></a><a name="b430235112379"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p11670144519110"><a name="p11670144519110"></a><a name="p11670144519110"></a><strong id="b842352706102346_5_3"><a name="b842352706102346_5_3"></a><a name="b842352706102346_5_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.3"><p id="p15675134514110"><a name="p15675134514110"></a><a name="p15675134514110"></a><strong id="b842352706164541_3_3"><a name="b842352706164541_3_3"></a><a name="b842352706164541_3_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p203621746403"><a name="p203621746403"></a><a name="p203621746403"></a><strong id="b19951343164218"><a name="b19951343164218"></a><a name="b19951343164218"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2480924512"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p18116152911"><a name="p18116152911"></a><a name="p18116152911"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p11161852317"><a name="p11161852317"></a><a name="p11161852317"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p121164521715"><a name="p121164521715"></a><a name="p121164521715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p21161452619"><a name="p21161452619"></a><a name="p21161452619"></a>Specifies the node type.</p>
    <p id="p369141413331"><a name="p369141413331"></a><a name="p369141413331"></a>Valid value:</p>
    <a name="ul121232613404"></a><a name="ul121232613404"></a><ul id="ul121232613404"><li>For a cluster instance, the value can be <strong id="b10928484446"><a name="b10928484446"></a><a name="b10928484446"></a>mongos</strong>, <strong id="b15983455144410"><a name="b15983455144410"></a><a name="b15983455144410"></a>shard</strong>, or <strong id="b14732155814414"><a name="b14732155814414"></a><a name="b14732155814414"></a>config</strong>.</li><li>For a replica set instance, the value is <strong id="b1496317331458"><a name="b1496317331458"></a><a name="b1496317331458"></a>replica</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row194801524017"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p17946205216"><a name="p17946205216"></a><a name="p17946205216"></a>num</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p179461801727"><a name="p179461801727"></a><a name="p179461801727"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p1994615016215"><a name="p1994615016215"></a><a name="p1994615016215"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p11946207210"><a name="p11946207210"></a><a name="p11946207210"></a>Specifies node quantity.</p>
    <p id="p1946140122"><a name="p1946140122"></a><a name="p1946140122"></a>Valid value:</p>
    <a name="ul16946160926"></a><a name="ul16946160926"></a><ul id="ul16946160926"><li>mongos: The value ranges from 2 to 12.</li><li>shard: The value ranges from 2 to 12.</li><li>config: The value is <strong id="b1318012185488"><a name="b1318012185488"></a><a name="b1318012185488"></a>1</strong>.</li><li>replica: The value is <strong id="b1833473110367"><a name="b1833473110367"></a><a name="b1833473110367"></a>1</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row5161165517286"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p131613551280"><a name="p131613551280"></a><a name="p131613551280"></a>storage</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1532310162817"><a name="p1532310162817"></a><a name="p1532310162817"></a>This parameter is mandatory for all nodes except mongos. This parameter is invalid for the mongos nodes.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p3589184744118"><a name="p3589184744118"></a><a name="p3589184744118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p2887384610"><a name="p2887384610"></a><a name="p2887384610"></a>Specifies the disk type.</p>
    <p id="p15929549113710"><a name="p15929549113710"></a><a name="p15929549113710"></a>Valid value: ULTRAHIGH, which indicates the type SSD.</p>
    <p id="p1495131511210"><a name="p1495131511210"></a><a name="p1495131511210"></a>This parameter is valid for the shard and config nodes of a cluster instance and for replica set instances. This parameter is invalid for mongos nodes. Therefore, you do not need to specify the storage space for mongos nodes.</p>
    </td>
    </tr>
    <tr id="row84801524316"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p12619121114318"><a name="p12619121114318"></a><a name="p12619121114318"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1615821120194"><a name="p1615821120194"></a><a name="p1615821120194"></a>This parameter is mandatory for all nodes except mongos. This parameter is invalid for the mongos nodes.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p661913115318"><a name="p661913115318"></a><a name="p661913115318"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p13619151112319"><a name="p13619151112319"></a><a name="p13619151112319"></a>Specifies the disk size.</p>
    <p id="p16619211039"><a name="p16619211039"></a><a name="p16619211039"></a>The value must be a multiple of 10. The unit is GB.</p>
    <a name="ul116195116311"></a><a name="ul116195116311"></a><ul id="ul116195116311"><li>For a cluster instance, the storage space of a shard node can be 10 to 1000 GB, and the config storage space is 20 GB. This parameter is invalid for mongos nodes. Therefore, you do not need to specify the storage space for mongos nodes.</li><li>For a replica set instance, the value ranges from 10 to 2000.</li></ul>
    </td>
    </tr>
    <tr id="row13588338389"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1877334110385"><a name="p1877334110385"></a><a name="p1877334110385"></a>spec_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p77801941143817"><a name="p77801941143817"></a><a name="p77801941143817"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.3 "><p id="p13788124173814"><a name="p13788124173814"></a><a name="p13788124173814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p2079864173819"><a name="p2079864173819"></a><a name="p2079864173819"></a>Specifies the resource specification code. For details about how to obtain the value, see the response values of <strong id="b15409175112507"><a name="b15409175112507"></a><a name="b15409175112507"></a>spec_code</strong> in <a href="querying-all-db-instance-specifications.md">Querying All DB Instance Specifications</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  backup\_strategy field data structure description

    <a name="table15990419397"></a>
    <table><thead align="left"><tr id="row13463201495"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p258122019911"><a name="p258122019911"></a><a name="p258122019911"></a><strong id="b3515421175117"><a name="b3515421175117"></a><a name="b3515421175117"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p47172016918"><a name="p47172016918"></a><a name="p47172016918"></a><strong id="b842352706102346_5_7"><a name="b842352706102346_5_7"></a><a name="b842352706102346_5_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p19887204920"><a name="p19887204920"></a><a name="p19887204920"></a><strong id="b842352706164541_3_7"><a name="b842352706164541_3_7"></a><a name="b842352706164541_3_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39%" id="mcps1.2.5.1.4"><p id="p542012552010"><a name="p542012552010"></a><a name="p542012552010"></a><strong id="b87114521838"><a name="b87114521838"></a><a name="b87114521838"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12114172014914"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1912612020911"><a name="p1912612020911"></a><a name="p1912612020911"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p81383201395"><a name="p81383201395"></a><a name="p81383201395"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p13150162018916"><a name="p13150162018916"></a><a name="p13150162018916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="p8983181183415"><a name="p8983181183415"></a><a name="p8983181183415"></a>Specifies the backup time window. Automated backups will be triggered during the backup time window.</p>
    <p id="p144363282818"><a name="p144363282818"></a><a name="p144363282818"></a>The value cannot be empty. It must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
    <a name="ul73551635192814"></a><a name="ul73551635192814"></a><ul id="ul73551635192814"><li>The <strong id="b8466258394"><a name="b8466258394"></a><a name="b8466258394"></a>HH</strong> value must be 1 greater than the <strong id="b174669581595"><a name="b174669581595"></a><a name="b174669581595"></a>hh</strong> value.</li><li>The values of <strong id="b13214152101015"><a name="b13214152101015"></a><a name="b13214152101015"></a>mm</strong> and <strong id="b321610214106"><a name="b321610214106"></a><a name="b321610214106"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b1421618251018"><a name="b1421618251018"></a><a name="b1421618251018"></a>00</strong>, <strong id="b1521612261016"><a name="b1521612261016"></a><a name="b1521612261016"></a>15</strong>, <strong id="b72161127109"><a name="b72161127109"></a><a name="b72161127109"></a>30</strong>, or <strong id="b15217102201017"><a name="b15217102201017"></a><a name="b15217102201017"></a>45</strong>.</li></ul>
    <p id="p59342194324"><a name="p59342194324"></a><a name="p59342194324"></a>Example value:</p>
    <a name="ul1210322243217"></a><a name="ul1210322243217"></a><ul id="ul1210322243217"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
    </td>
    </tr>
    <tr id="row111950203915"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p10206620196"><a name="p10206620196"></a><a name="p10206620196"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p421932012920"><a name="p421932012920"></a><a name="p421932012920"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p111662049164812"><a name="p111662049164812"></a><a name="p111662049164812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="p19255132017913"><a name="p19255132017913"></a><a name="p19255132017913"></a>Specifies the number of days to retain the generated backup files.</p>
    <p id="p1627115206911"><a name="p1627115206911"></a><a name="p1627115206911"></a>The value range is from 0 to 732.</p>
    <a name="ul20536122725718"></a><a name="ul20536122725718"></a><ul id="ul20536122725718"><li>If this parameter is set to <strong id="b842352706112318"><a name="b842352706112318"></a><a name="b842352706112318"></a>0</strong>, the automated backup policy is not set.</li><li>If this parameter is not transferred, the automated backup policy is enabled by default. Backup files are stored for seven days by default.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


>![](/images/icon-note.gif) **NOTE:**   
>The values of  **region**  and  **availability\_zone**  are used as examples.  

-   Request header

    ```
    POST https://DDS endpoint/v3/{project_id}/instances.
    ```

-   Example request

    Create a cluster instance.

    ```
    {
      "name": "test-cluster-01",
      "datastore": {
        "type": "DDS-Community",
        "version": "3.4",
        "storage_engine": "wiredTiger"
      },
      "region": "aaa",
      "availability_zone": "bbb",
      "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
      "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
      "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
      "password": "Test@123",
      "mode": "Sharding",
      "flavor": [
        {
          "type": "mongos",
          "num": 2,
          "spec_code": "dds.mongodb.s2.medium.4.mongos"
        },
        {
          "type": "shard",
          "num": 2,
          "storage": "ULTRAHIGH",
          "size": 20,
          "spec_code": "dds.mongodb.s2.medium.4.shard"
        },
        {
          "type": "config",
          "num": 1,
          "storage": "ULTRAHIGH",
          "size": 20,
          "spec_code": "dds.mongodb.s2.large.2.config"
        }
      ],
      "backup_strategy": {
        "start_time": "08:15-09:15",
        "keep_days": "8"
      }
    }
    ```

    Create a replica set instance.

    ```
    {
      "name": "test-replicaset",
      "datastore": {
        "type": "DDS-Community",
        "version": "3.4",
        "storage_engine": "wiredTiger"
      },
      "region": "aaa",
      "availability_zone": "bbb",
      "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
      "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
      "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
      "password": "Test@123",
      "mode": "ReplicaSet",
      "flavor": [
        {
          "type": "replica",
          "num": 1,
          "storage": "ULTRAHIGH",
          "size": 30,
          "spec_code": "dds.mongodb.s2.medium.4.repset"
        }
      ],
      "backup_strategy": {
        "start_time": "08:15-09:15",
        "keep_days": "8"
      }
    }
    ```


## Responses<a name="section36749739"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table27245651"></a>
    <table><thead align="left"><tr id="row47625437"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p32455223"><a name="p32455223"></a><a name="p32455223"></a><strong id="b842352706102328_25"><a name="b842352706102328_25"></a><a name="b842352706102328_25"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p11627434"><a name="p11627434"></a><a name="p11627434"></a><strong id="b842352706164541_21"><a name="b842352706164541_21"></a><a name="b842352706164541_21"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p152381041511"><a name="p152381041511"></a><a name="p152381041511"></a><strong id="b46627531333"><a name="b46627531333"></a><a name="b46627531333"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51926520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45298596"><a name="p45298596"></a><a name="p45298596"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45307656"><a name="p45307656"></a><a name="p45307656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46041549"><a name="p46041549"></a><a name="p46041549"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row20114173217101"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p942262101114"><a name="p942262101114"></a><a name="p942262101114"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1543113251117"><a name="p1543113251117"></a><a name="p1543113251117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15439202191111"><a name="p15439202191111"></a><a name="p15439202191111"></a>Same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row1187910274115"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p891540131119"><a name="p891540131119"></a><a name="p891540131119"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p323001118407"><a name="p323001118407"></a><a name="p323001118407"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33020407110"><a name="p33020407110"></a><a name="p33020407110"></a>Indicates the database information, which is the same as the request parameter. For more information, see <a href="#table228903751753">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row59793748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1770211716105"><a name="p1770211716105"></a><a name="p1770211716105"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1870215741016"><a name="p1870215741016"></a><a name="p1870215741016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p157021731012"><a name="p157021731012"></a><a name="p157021731012"></a>Indicates the creation time in the following format: yyyy-mm-dd hh:mm:ss.</p>
    </td>
    </tr>
    <tr id="row591219314127"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16849171341212"><a name="p16849171341212"></a><a name="p16849171341212"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p138561913181214"><a name="p138561913181214"></a><a name="p138561913181214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15866113151219"><a name="p15866113151219"></a><a name="p15866113151219"></a>Indicates the DB instance status. The value is <span class="parmvalue" id="parmvalue5337746114210"><a name="parmvalue5337746114210"></a><a name="parmvalue5337746114210"></a><b>creating</b></span>.</p>
    </td>
    </tr>
    <tr id="row32924936175949"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1535621031120"><a name="p1535621031120"></a><a name="p1535621031120"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3356151013114"><a name="p3356151013114"></a><a name="p3356151013114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p159871637193619"><a name="p159871637193619"></a><a name="p159871637193619"></a>Indicates the region ID, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row11097898"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1535618104112"><a name="p1535618104112"></a><a name="p1535618104112"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p235661031119"><a name="p235661031119"></a><a name="p235661031119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2356181081116"><a name="p2356181081116"></a><a name="p2356181081116"></a>Indicates the AZ ID, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row785288110273"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p135661012113"><a name="p135661012113"></a><a name="p135661012113"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53561210161117"><a name="p53561210161117"></a><a name="p53561210161117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2356201012113"><a name="p2356201012113"></a><a name="p2356201012113"></a>Indicates the VPC ID, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row6771693"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12356161015111"><a name="p12356161015111"></a><a name="p12356161015111"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p73561910111114"><a name="p73561910111114"></a><a name="p73561910111114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6356111081115"><a name="p6356111081115"></a><a name="p6356111081115"></a>Indicates the subnet ID, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row49289224"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1435661071112"><a name="p1435661071112"></a><a name="p1435661071112"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p113568101117"><a name="p113568101117"></a><a name="p113568101117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8356910131112"><a name="p8356910131112"></a><a name="p8356910131112"></a>Indicates the ID of the security group to which the instance belongs, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row118272047171218"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19867514132"><a name="p19867514132"></a><a name="p19867514132"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p78782010132"><a name="p78782010132"></a><a name="p78782010132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p68850151312"><a name="p68850151312"></a><a name="p68850151312"></a>Indicates the ID of the disk encryption key, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row9414870143634"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p393916271115"><a name="p393916271115"></a><a name="p393916271115"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p293912771120"><a name="p293912771120"></a><a name="p293912771120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1193910279117"><a name="p1193910279117"></a><a name="p1193910279117"></a>Indicates the instance type, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row40529449"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1871214715112"><a name="p1871214715112"></a><a name="p1871214715112"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p824425424013"><a name="p824425424013"></a><a name="p824425424013"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18491173333816"><a name="p18491173333816"></a><a name="p18491173333816"></a>Indicates the instance specification, which is the same as the request parameter. For more information, see <a href="#table94791241013">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row430511298132"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p848854719136"><a name="p848854719136"></a><a name="p848854719136"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7935239134111"><a name="p7935239134111"></a><a name="p7935239134111"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4509154751315"><a name="p4509154751315"></a><a name="p4509154751315"></a>Indicates the advanced backup policy, which is the same as the request parameter. For more information, see <a href="#table15990419397">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row2353067711815"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16141310121213"><a name="p16141310121213"></a><a name="p16141310121213"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1714161011120"><a name="p1714161011120"></a><a name="p1714161011120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10141141019125"><a name="p10141141019125"></a><a name="p10141141019125"></a>Indicates the ID of the workflow for creating a DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>


>![](/images/icon-note.gif) **NOTE:**   
>The values of  **region**  and  **availability\_zone**  are used as examples.  

-   Response example

    Cluster instance:

    ```
    { 
        "id": "39b6a1a278844ac48119d86512e0000bin02",
        "name": "test-cluster-01",
        "datastore": {
            "type": "DDS-Community",
            "version": "3.4",
            "storage_engine": "wiredTiger"
        },
        "created": "2019-01-16 09:34:36",
        "status": "creating",
        "region": "aaa",
        "availability_zone": "bbb",
        "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
        "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
        "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
        "disk_encryption_id": "",
        "mode": "Sharding",
        "flavor": [
            {
                "type": "mongos",
                "num": 2,
                "spec_code": "dds.mongodb.s2.medium.4.mongos"
            },
            {
                "type": "shard",
                "num": 2,
                "spec_code": "dds.mongodb.s2.medium.4.shard",
                "size": 20
            },
            {
                "type": "config",
                "num": 1,
                "spec_code": "dds.mongodb.s2.large.2.config",
                "size": 20
            }
        ],
        "backup_strategy": {
            "start_time": "08:15-09:15",
            "keep_days": "8"
        },
        "job_id": "c010abd0-48cf-4fa8-8cbc-090f093eaa2f"
    }
    ```

    Replica set instance:

    ```
    {
        "id": "46dfadfd2b674585a430217f23606cd7in02",
        "name": "test-replicaset",
        "datastore": {
            "type": "DDS-Community",
            "version": "3.4",
            "storage_engine": "wiredTiger"
        },
        "created": "2019-01-16 09:33:08",
        "status": "creating",
        "region": "aaa",
        "availability_zone": "bbb",
        "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
        "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
        "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
        "disk_encryption_id": "",
        "mode": "ReplicaSet",
        "flavor": [
            {
                "type": "replica",
                "num": 1,
                "spec_code": "dds.mongodb.s2.medium.4.repset",
                "size": 30
            }
        ],
        "backup_strategy": {
            "start_time": "08:15-09:15",
            "keep_days": "7"
        },
        "job_id": "2408417d-fd4b-40ae-bec6-e09ce594eb5f"
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

