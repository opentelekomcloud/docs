# Restoring Data to a New DB Instance<a name="en-us_topic_0037147509"></a>

## Function<a name="section4850156117316"></a>

This API is used to restore data to a new DB instance.

## Constraints<a name="section76661720122713"></a>

Currently, Microsoft SQL Server is not supported.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.12%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.46%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.42%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.42%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table6209466312442"></a>
    <table><thead align="left"><tr id="row6512234412442"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p4041853012442"><a name="p4041853012442"></a><a name="p4041853012442"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5267548812442"><a name="p5267548812442"></a><a name="p5267548812442"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3885613912442"><a name="p3885613912442"></a><a name="p3885613912442"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6033953012442"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5566375012442"><a name="p5566375012442"></a><a name="p5566375012442"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1246986212442"><a name="p1246986212442"></a><a name="p1246986212442"></a>Dictionary data structure. For details, see <a href="#table3901776810752">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48757463124544"><a name="p48757463124544"></a><a name="p48757463124544"></a>Specifies new DB instance details.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instance field data structure description

    <a name="table3901776810752"></a>
    <table><thead align="left"><tr id="row3810763010752"><th class="cellrowborder" valign="top" width="20.87%" id="mcps1.2.5.1.1"><p id="p6681916210752"><a name="p6681916210752"></a><a name="p6681916210752"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.69%" id="mcps1.2.5.1.2"><p id="p4364306710752"><a name="p4364306710752"></a><a name="p4364306710752"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.3"><p id="p4542757710752"><a name="p4542757710752"></a><a name="p4542757710752"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.08%" id="mcps1.2.5.1.4"><p id="p5575513110752"><a name="p5575513110752"></a><a name="p5575513110752"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1987178610752"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.1 "><p id="p6611082910752"><a name="p6611082910752"></a><a name="p6611082910752"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p5337694110752"><a name="p5337694110752"></a><a name="p5337694110752"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p2856494510752"><a name="p2856494510752"></a><a name="p2856494510752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.4 "><p id="p23411412333"><a name="p23411412333"></a><a name="p23411412333"></a>Specifies the DB instance name.</p>
    <p id="p463314503337"><a name="p463314503337"></a><a name="p463314503337"></a>The DB instance name of the same type must be unique for the same tenant.</p>
    <p id="p2009736210752"><a name="p2009736210752"></a><a name="p2009736210752"></a>Valid value:</p>
    <p id="p59489767182234"><a name="p59489767182234"></a><a name="p59489767182234"></a>The value must be 4 to 64 characters in length and start with a letter. It is case-insensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1445976910752"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.1 "><p id="p3039067510752"><a name="p3039067510752"></a><a name="p3039067510752"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p4572563810752"><a name="p4572563810752"></a><a name="p4572563810752"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p1278917710752"><a name="p1278917710752"></a><a name="p1278917710752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.4 "><p id="p34804713"><a name="p34804713"></a><a name="p34804713"></a>Specifies the specification ID (<strong id="b8423527062011"><a name="b8423527062011"></a><a name="b8423527062011"></a>flavors.id</strong> in the response message in section <a href="obtaining-all-db-instance-specifications.md">Obtaining All DB Instance Specifications</a>).</p>
    <p id="p6228690410752"><a name="p6228690410752"></a><a name="p6228690410752"></a>Valid value:</p>
    <p id="p2371123210752"><a name="p2371123210752"></a><a name="p2371123210752"></a>The value cannot be empty. The string length and whether the string complying with UUID regular expression rules are verified.</p>
    </td>
    </tr>
    <tr id="row1207450010752"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.1 "><p id="p3851041110752"><a name="p3851041110752"></a><a name="p3851041110752"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p3233560710752"><a name="p3233560710752"></a><a name="p3233560710752"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p193854410752"><a name="p193854410752"></a><a name="p193854410752"></a>Dictionary data structure. For details, see <a href="#table5177446510752">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.4 "><p id="p3521559110752"><a name="p3521559110752"></a><a name="p3521559110752"></a>Specifies the volume information.</p>
    <p id="p4850486610752"><a name="p4850486610752"></a><a name="p4850486610752"></a>This parameter is mandatory for the creation of a single or primary/standby DB instances.</p>
    </td>
    </tr>
    <tr id="row5592339910752"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.1 "><p id="p3350147910752"><a name="p3350147910752"></a><a name="p3350147910752"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p2926525910752"><a name="p2926525910752"></a><a name="p2926525910752"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p2167577210752"><a name="p2167577210752"></a><a name="p2167577210752"></a>Dictionary data structure. For details, see <a href="#table4694349710752">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.4 "><p id="p1105769810752"><a name="p1105769810752"></a><a name="p1105769810752"></a>Specifies the HA configuration parameter. It is mandatory for the primary/standby DB instance creation.</p>
    </td>
    </tr>
    <tr id="row6230336510164"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.1 "><p id="p21756125101656"><a name="p21756125101656"></a><a name="p21756125101656"></a>restorePoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p17415701101656"><a name="p17415701101656"></a><a name="p17415701101656"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p1385690101656"><a name="p1385690101656"></a><a name="p1385690101656"></a>Dictionary data structure. For details, see <a href="#table40926645101321">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.2.5.1.4 "><p id="p17922162101656"><a name="p17922162101656"></a><a name="p17922162101656"></a>Specifies the configuration parameter for restoring data to a new DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  volume field data structure description

    <a name="table5177446510752"></a>
    <table><thead align="left"><tr id="row2755836110752"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.1"><p id="p1763473410752"><a name="p1763473410752"></a><a name="p1763473410752"></a><strong id="b842352706102328_9"><a name="b842352706102328_9"></a><a name="b842352706102328_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.189999999999998%" id="mcps1.2.5.1.2"><p id="p1912732710752"><a name="p1912732710752"></a><a name="p1912732710752"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p580968610752"><a name="p580968610752"></a><a name="p580968610752"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.71%" id="mcps1.2.5.1.4"><p id="p82252010752"><a name="p82252010752"></a><a name="p82252010752"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row462410410752"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.1 "><p id="p3900811510752"><a name="p3900811510752"></a><a name="p3900811510752"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.5.1.2 "><p id="p554075110752"><a name="p554075110752"></a><a name="p554075110752"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p4614768310752"><a name="p4614768310752"></a><a name="p4614768310752"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.71%" headers="mcps1.2.5.1.4 "><p id="p2625079716439"><a name="p2625079716439"></a><a name="p2625079716439"></a>Specifies the volume size.</p>
    <p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>Its value range is from 40 GB to 4000 GB. The value must be a multiple of 10.</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    <div class="notice" id="note18772920133413"><a name="note18772920133413"></a><a name="note18772920133413"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p3772920183420"><a name="p3772920183420"></a><a name="p3772920183420"></a>The volume size of the new DB instance must be greater than or equal to that of the original DB instance.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  ha field data structure description

    <a name="table4694349710752"></a>
    <table><thead align="left"><tr id="rc4bff549a2b741c485959f1fd3311a97"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0032347785_p43246301833"><a name="en-us_topic_0032347785_p43246301833"></a><a name="en-us_topic_0032347785_p43246301833"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.560000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0032347785_p147507341833"><a name="en-us_topic_0032347785_p147507341833"></a><a name="en-us_topic_0032347785_p147507341833"></a><strong id="b842352706102346_9"><a name="b842352706102346_9"></a><a name="b842352706102346_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.18%" id="mcps1.2.5.1.3"><p id="en-us_topic_0032347785_p539587821833"><a name="en-us_topic_0032347785_p539587821833"></a><a name="en-us_topic_0032347785_p539587821833"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.519999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0032347785_p85852311833"><a name="en-us_topic_0032347785_p85852311833"></a><a name="en-us_topic_0032347785_p85852311833"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf08895c14d8241feaacbfb9b5e2420f6"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032347785_p233670901833"><a name="en-us_topic_0032347785_p233670901833"></a><a name="en-us_topic_0032347785_p233670901833"></a>enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.560000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032347785_p136861651833"><a name="en-us_topic_0032347785_p136861651833"></a><a name="en-us_topic_0032347785_p136861651833"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032347785_p348375601833"><a name="en-us_topic_0032347785_p348375601833"></a><a name="en-us_topic_0032347785_p348375601833"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0032347785_p32700831833"><a name="en-us_topic_0032347785_p32700831833"></a><a name="en-us_topic_0032347785_p32700831833"></a>Specifies the HA configuration parameter.</p>
    <p id="en-us_topic_0032347785_p294307511833"><a name="en-us_topic_0032347785_p294307511833"></a><a name="en-us_topic_0032347785_p294307511833"></a>Valid value:</p>
    <p id="ad58d18133f9145018439d81844fb0b43"><a name="ad58d18133f9145018439d81844fb0b43"></a><a name="ad58d18133f9145018439d81844fb0b43"></a>The value is <strong id="b842352706164817"><a name="b842352706164817"></a><a name="b842352706164817"></a>true</strong> or <strong id="b842352706164826"><a name="b842352706164826"></a><a name="b842352706164826"></a>false</strong>. The value <strong id="b842352706164830"><a name="b842352706164830"></a><a name="b842352706164830"></a>true</strong> indicates creating primary/standby DB instances. The value <strong id="b765135452113640"><a name="b765135452113640"></a><a name="b765135452113640"></a>false</strong> indicates creating a single DB instance.</p>
    </td>
    </tr>
    <tr id="re15acb153a31487ea9db5e0bb5ee0ee9"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032347785_p53291281833"><a name="en-us_topic_0032347785_p53291281833"></a><a name="en-us_topic_0032347785_p53291281833"></a>replicationMode</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.560000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032347785_p290062461833"><a name="en-us_topic_0032347785_p290062461833"></a><a name="en-us_topic_0032347785_p290062461833"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032347785_p6957001833"><a name="en-us_topic_0032347785_p6957001833"></a><a name="en-us_topic_0032347785_p6957001833"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.2.5.1.4 "><p id="aeea4666de16a4bad9fa955cf2f4a4ef6"><a name="aeea4666de16a4bad9fa955cf2f4a4ef6"></a><a name="aeea4666de16a4bad9fa955cf2f4a4ef6"></a>Specifies the replication mode for the standby DB instance.</p>
    <p id="ac4b923b802374d699e305263adadfa09"><a name="ac4b923b802374d699e305263adadfa09"></a><a name="ac4b923b802374d699e305263adadfa09"></a>The value cannot be empty.</p>
    <a name="ud6ac9139b5eb40b7a172c5b2bd63ecf2"></a><a name="ud6ac9139b5eb40b7a172c5b2bd63ecf2"></a><ul id="ud6ac9139b5eb40b7a172c5b2bd63ecf2"><li>For MySQL, the value is <strong id="b842352706165650_1"><a name="b842352706165650_1"></a><a name="b842352706165650_1"></a>async</strong> or <strong id="b842352706165654_1"><a name="b842352706165654_1"></a><a name="b842352706165654_1"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b842352706165650_5"><a name="b842352706165650_5"></a><a name="b842352706165650_5"></a>async</strong> or <strong id="b842352706165654_5"><a name="b842352706165654_5"></a><a name="b842352706165654_5"></a>sync</strong>.</li></ul>
    <div class="note" id="nf64beccbbfa1482882c78e5ab29e4b27"><a name="nf64beccbbfa1482882c78e5ab29e4b27"></a><a name="nf64beccbbfa1482882c78e5ab29e4b27"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ufd28b5f637624fb2a46dc916919c3217"></a><a name="ufd28b5f637624fb2a46dc916919c3217"></a><ul id="ufd28b5f637624fb2a46dc916919c3217"><li><strong id="b842352706105954"><a name="b842352706105954"></a><a name="b842352706105954"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b842352706164020"><a name="b842352706164020"></a><a name="b842352706164020"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b13384211081105"><a name="b13384211081105"></a><a name="b13384211081105"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  restorePoint field data structure description

    <a name="table40926645101321"></a>
    <table><thead align="left"><tr id="row24600537101321"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.5.1.1"><p id="p46486469101321"><a name="p46486469101321"></a><a name="p46486469101321"></a><strong id="b842352706102328_11"><a name="b842352706102328_11"></a><a name="b842352706102328_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.69%" id="mcps1.2.5.1.2"><p id="p7307605101321"><a name="p7307605101321"></a><a name="p7307605101321"></a><strong id="b842352706102346_11"><a name="b842352706102346_11"></a><a name="b842352706102346_11"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.5.1.3"><p id="p55045105101321"><a name="p55045105101321"></a><a name="p55045105101321"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.5.1.4"><p id="p29468546101321"><a name="p29468546101321"></a><a name="p29468546101321"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38142064101321"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p2499490101321"><a name="p2499490101321"></a><a name="p2499490101321"></a>backupRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p1132161101321"><a name="p1132161101321"></a><a name="p1132161101321"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p24596212101321"><a name="p24596212101321"></a><a name="p24596212101321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.4 "><p id="p52323761101345"><a name="p52323761101345"></a><a name="p52323761101345"></a>Specifies the full backup file.</p>
    </td>
    </tr>
    <tr id="row11722875101321"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p50964136101355"><a name="p50964136101355"></a><a name="p50964136101355"></a>restoreTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p7029151101321"><a name="p7029151101321"></a><a name="p7029151101321"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p6126029210142"><a name="p6126029210142"></a><a name="p6126029210142"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.4 "><p id="p6066633101411"><a name="p6066633101411"></a><a name="p6066633101411"></a>Specifies the time point the DB instance is restored to. At least one of the <strong id="b84235270611824"><a name="b84235270611824"></a><a name="b84235270611824"></a>backupRef</strong> and <strong id="b84235270611827"><a name="b84235270611827"></a><a name="b84235270611827"></a>restoreTime</strong> parameters should be specified. If both parameters are specified, the DB instance is restored using the full backup file.</p>
    </td>
    </tr>
    <tr id="row64797343101420"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p2273989101428"><a name="p2273989101428"></a><a name="p2273989101428"></a>sourceInstanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p8099656101435"><a name="p8099656101435"></a><a name="p8099656101435"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p52092398101435"><a name="p52092398101435"></a><a name="p52092398101435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.4 "><p id="p26764629101441"><a name="p26764629101441"></a><a name="p26764629101441"></a>Specifies the source DB instance ID.</p>
    <p id="p161813239552"><a name="p161813239552"></a><a name="p161813239552"></a>If <span class="parmname" id="parmname96045294552"><a name="parmname96045294552"></a><a name="parmname96045294552"></a><b>backupRef</b></span> is not specified and <span class="parmname" id="parmname97751735105517"><a name="parmname97751735105517"></a><a name="parmname97751735105517"></a><b>restoreTime</b></span> is specified, the <strong id="b290483814375"><a name="b290483814375"></a><a name="b290483814375"></a>sourceInstanceId</strong> parameter is mandatory.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
        "instance": {
            "name": "trove-newinstance",
            "flavorRef": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
            "volume": {
                "size": 100
            },
            "restorePoint":{
               "backupRef": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe",
               "sourceInstanceId": "0bc7300c-dc63-45d4-aa3b-d85bf577baac"
            }
        }
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  7**  Parameter description

    <a name="table17474517"></a>
    <table><thead align="left"><tr id="row16146366"><th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.1"><p id="p32787233"><a name="p32787233"></a><a name="p32787233"></a><strong id="b842352706102328_13"><a name="b842352706102328_13"></a><a name="b842352706102328_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.29%" id="mcps1.2.4.1.2"><p id="p38520254"><a name="p38520254"></a><a name="p38520254"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p33132859"><a name="p33132859"></a><a name="p33132859"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66515904"><td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.1 "><p id="p19079158"><a name="p19079158"></a><a name="p19079158"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.29%" headers="mcps1.2.4.1.2 "><p id="p1907972"><a name="p1907972"></a><a name="p1907972"></a>Dictionary data structure. For details, see <a href="#table27245651">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p48735027"><a name="p48735027"></a><a name="p48735027"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  instance field data structure description

    <a name="table27245651"></a>
    <table><thead align="left"><tr id="row47625437"><th class="cellrowborder" valign="top" width="26.94269426942694%" id="mcps1.2.4.1.1"><p id="p32455223"><a name="p32455223"></a><a name="p32455223"></a><strong id="b842352706102328_15"><a name="b842352706102328_15"></a><a name="b842352706102328_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.72397239723972%" id="mcps1.2.4.1.2"><p id="p11627434"><a name="p11627434"></a><a name="p11627434"></a><strong id="b842352706164541_13"><a name="b842352706164541_13"></a><a name="b842352706164541_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2298077"><a name="p2298077"></a><a name="p2298077"></a><strong id="b842352706163417_17"><a name="b842352706163417_17"></a><a name="b842352706163417_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51926520"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p45298596"><a name="p45298596"></a><a name="p45298596"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p45307656"><a name="p45307656"></a><a name="p45307656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Indicates the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row56907078"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p46070597"><a name="p46070597"></a><a name="p46070597"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p40730901"><a name="p40730901"></a><a name="p40730901"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10868702"><a name="p10868702"></a><a name="p10868702"></a>Indicates the DB instance status. The value is <span class="parmvalue" id="parmvalue5337746114210"><a name="parmvalue5337746114210"></a><a name="parmvalue5337746114210"></a><b>BUILD</b></span>.</p>
    </td>
    </tr>
    <tr id="row30709455"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p4437887"><a name="p4437887"></a><a name="p4437887"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p23924539"><a name="p23924539"></a><a name="p23924539"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58839532"><a name="p58839532"></a><a name="p58839532"></a>Indicates the provisioned DB instance information.</p>
    </td>
    </tr>
    <tr id="row59793748"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p11455439"><a name="p11455439"></a><a name="p11455439"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p55475379"><a name="p55475379"></a><a name="p55475379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64320678"><a name="p64320678"></a><a name="p64320678"></a>Indicates the creation time. It is a blank string.</p>
    </td>
    </tr>
    <tr id="row42592467"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p27437792"><a name="p27437792"></a><a name="p27437792"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p7868661"><a name="p7868661"></a><a name="p7868661"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33381819"><a name="p33381819"></a><a name="p33381819"></a>Indicates the DB instance connection address. It is a blank string.</p>
    </td>
    </tr>
    <tr id="row32000920"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p41937705"><a name="p41937705"></a><a name="p41937705"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p41510976"><a name="p41510976"></a><a name="p41510976"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6945858"><a name="p6945858"></a><a name="p6945858"></a>Indicates the DB instance type.</p>
    </td>
    </tr>
    <tr id="row22664988153914"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p23924701153914"><a name="p23924701153914"></a><a name="p23924701153914"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p58852623153914"><a name="p58852623153914"></a><a name="p58852623153914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2333145153914"><a name="p2333145153914"></a><a name="p2333145153914"></a>Indicates the region ID.</p>
    </td>
    </tr>
    <tr id="row62512728"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p30366184"><a name="p30366184"></a><a name="p30366184"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p43741849"><a name="p43741849"></a><a name="p43741849"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53428882"><a name="p53428882"></a><a name="p53428882"></a>Indicates the empty string.</p>
    </td>
    </tr>
    <tr id="row11097898"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p26514531"><a name="p26514531"></a><a name="p26514531"></a>availabilityZone</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p193401"><a name="p193401"></a><a name="p193401"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66626642215817"><a name="p66626642215817"></a><a name="p66626642215817"></a>Indicates the AZ ID, which is the same as that of the specified DB instance.</p>
    </td>
    </tr>
    <tr id="row31649748174657"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p13492815174657"><a name="p13492815174657"></a><a name="p13492815174657"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p19176243174657"><a name="p19176243174657"></a><a name="p19176243174657"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2950522174751"><a name="p2950522174751"></a><a name="p2950522174751"></a>Indicates the VPC ID, which is the same as that of the specified DB instance.</p>
    </td>
    </tr>
    <tr id="row6771693"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p11636265"><a name="p11636265"></a><a name="p11636265"></a>nics</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p61638963215928"><a name="p61638963215928"></a><a name="p61638963215928"></a>Dictionary data structure. For details, see <a href="#table2179128">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15224149215928"><a name="p15224149215928"></a><a name="p15224149215928"></a>Indicates the nics information, which is the same as that of the specified DB instance.</p>
    </td>
    </tr>
    <tr id="row49289224"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p33004241"><a name="p33004241"></a><a name="p33004241"></a>securityGroup</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p56097870"><a name="p56097870"></a><a name="p56097870"></a>Dictionary data structure. For details, see <a href="#table14331939154828">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47633640"><a name="p47633640"></a><a name="p47633640"></a>Indicates the security group that the specified DB instance belongs to.</p>
    </td>
    </tr>
    <tr id="row26049579"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p29641146"><a name="p29641146"></a><a name="p29641146"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p52122650"><a name="p52122650"></a><a name="p52122650"></a>Dictionary data structure. For details, see <a href="#table3902718715528">Table 11</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42884477155036"><a name="p42884477155036"></a><a name="p42884477155036"></a>Indicates the specification ID, which is the same as that of the specified DB instance.</p>
    </td>
    </tr>
    <tr id="row13795340"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p43680716"><a name="p43680716"></a><a name="p43680716"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p48477080"><a name="p48477080"></a><a name="p48477080"></a>Dictionary data structure. For details, see <a href="#table3983437622329">Table 12</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34329433"><a name="p34329433"></a><a name="p34329433"></a>Indicates the volume information.</p>
    </td>
    </tr>
    <tr id="row60201629154321"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p44493790154321"><a name="p44493790154321"></a><a name="p44493790154321"></a>dataStoreInfo</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p14540660161250"><a name="p14540660161250"></a><a name="p14540660161250"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p201185154321"><a name="p201185154321"></a><a name="p201185154321"></a>Its value is <strong id="b84235270611614"><a name="b84235270611614"></a><a name="b84235270611614"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="row44422854114347"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p13622028114543"><a name="p13622028114543"></a><a name="p13622028114543"></a>dbPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p13779188114426"><a name="p13779188114426"></a><a name="p13779188114426"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26648574114459"><a name="p26648574114459"></a><a name="p26648574114459"></a>Indicates the database port number.</p>
    </td>
    </tr>
    <tr id="row30282311"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p36948161"><a name="p36948161"></a><a name="p36948161"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p40011092"><a name="p40011092"></a><a name="p40011092"></a>Dictionary data structure. For details, see <a href="#table52869820">Table 13</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19672999"><a name="p19672999"></a><a name="p19672999"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    <tr id="row4534970015542"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p5330303215542"><a name="p5330303215542"></a><a name="p5330303215542"></a>backupStrategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p2257829815542"><a name="p2257829815542"></a><a name="p2257829815542"></a>Dictionary data structure. For details, see <a href="#table49774232">Table 15</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2695485315542"><a name="p2695485315542"></a><a name="p2695485315542"></a>Indicates the backup policy information, which is the same as that of the specified DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  nics field data structure description

    <a name="table2179128"></a>
    <table><thead align="left"><tr id="row28646034"><th class="cellrowborder" valign="top" width="26.752675267526755%" id="mcps1.2.4.1.1"><p id="p38627455"><a name="p38627455"></a><a name="p38627455"></a><strong id="b842352706102328_17"><a name="b842352706102328_17"></a><a name="b842352706102328_17"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.91399139913992%" id="mcps1.2.4.1.2"><p id="p31664161"><a name="p31664161"></a><a name="p31664161"></a><strong id="b842352706164541_15"><a name="b842352706164541_15"></a><a name="b842352706164541_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14660263"><a name="p14660263"></a><a name="p14660263"></a><strong id="b842352706163417_19"><a name="b842352706163417_19"></a><a name="b842352706163417_19"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46630661"><td class="cellrowborder" valign="top" width="26.752675267526755%" headers="mcps1.2.4.1.1 "><p id="p18987236"><a name="p18987236"></a><a name="p18987236"></a>subnetId</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.91399139913992%" headers="mcps1.2.4.1.2 "><p id="p21209668"><a name="p21209668"></a><a name="p21209668"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40261524"><a name="p40261524"></a><a name="p40261524"></a>Indicates the network ID of the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  securityGroup field data structure description

    <a name="table14331939154828"></a>
    <table><thead align="left"><tr id="row1816327154828"><th class="cellrowborder" valign="top" width="27.32%" id="mcps1.2.4.1.1"><p id="p12904759154828"><a name="p12904759154828"></a><a name="p12904759154828"></a><strong id="b842352706102328_19"><a name="b842352706102328_19"></a><a name="b842352706102328_19"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.35%" id="mcps1.2.4.1.2"><p id="p43847332154828"><a name="p43847332154828"></a><a name="p43847332154828"></a><strong id="b842352706164541_17"><a name="b842352706164541_17"></a><a name="b842352706164541_17"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p61973042154828"><a name="p61973042154828"></a><a name="p61973042154828"></a><strong id="b842352706163417_21"><a name="b842352706163417_21"></a><a name="b842352706163417_21"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53760516154828"><td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.1 "><p id="p59634563154828"><a name="p59634563154828"></a><a name="p59634563154828"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.35%" headers="mcps1.2.4.1.2 "><p id="p17693606154828"><a name="p17693606154828"></a><a name="p17693606154828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p13737069154828"><a name="p13737069154828"></a><a name="p13737069154828"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11**  flavor field data structure description

    <a name="table3902718715528"></a>
    <table><thead align="left"><tr id="row2745207115528"><th class="cellrowborder" valign="top" width="26.94269426942694%" id="mcps1.2.4.1.1"><p id="p902525915528"><a name="p902525915528"></a><a name="p902525915528"></a><strong id="b842352706102328_21"><a name="b842352706102328_21"></a><a name="b842352706102328_21"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.72397239723972%" id="mcps1.2.4.1.2"><p id="p2470892915528"><a name="p2470892915528"></a><a name="p2470892915528"></a><strong id="b842352706164541_19"><a name="b842352706164541_19"></a><a name="b842352706164541_19"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5526621015528"><a name="p5526621015528"></a><a name="p5526621015528"></a><strong id="b842352706163417_23"><a name="b842352706163417_23"></a><a name="b842352706163417_23"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4737805715528"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p1241737115528"><a name="p1241737115528"></a><a name="p1241737115528"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.72397239723972%" headers="mcps1.2.4.1.2 "><p id="p21475815528"><a name="p21475815528"></a><a name="p21475815528"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p65797846155234"><a name="p65797846155234"></a><a name="p65797846155234"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  12**  volume field data structure description

    <a name="table3983437622329"></a>
    <table><thead align="left"><tr id="row5626807322329"><th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.1"><p id="p6142006622329"><a name="p6142006622329"></a><a name="p6142006622329"></a><strong id="b842352706102328_23"><a name="b842352706102328_23"></a><a name="b842352706102328_23"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.6%" id="mcps1.2.4.1.2"><p id="p5543963122329"><a name="p5543963122329"></a><a name="p5543963122329"></a><strong id="b842352706164541_21"><a name="b842352706164541_21"></a><a name="b842352706164541_21"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p6142510622329"><a name="p6142510622329"></a><a name="p6142510622329"></a><strong id="b842352706163417_25"><a name="b842352706163417_25"></a><a name="b842352706163417_25"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row937766122329"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="p2139308122329"><a name="p2139308122329"></a><a name="p2139308122329"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.6%" headers="mcps1.2.4.1.2 "><p id="p3537280222329"><a name="p3537280222329"></a><a name="p3537280222329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p4662473622329"><a name="p4662473622329"></a><a name="p4662473622329"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row3234748622329"><td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="p290072822329"><a name="p290072822329"></a><a name="p290072822329"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.6%" headers="mcps1.2.4.1.2 "><p id="p3987036922329"><a name="p3987036922329"></a><a name="p3987036922329"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p827443222329"><a name="p827443222329"></a><a name="p827443222329"></a>Indicates the volume size.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  13**  extendparam field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b842352706102328_25"><a name="b842352706102328_25"></a><a name="b842352706102328_25"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.73%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b842352706164541_23"><a name="b842352706164541_23"></a><a name="b842352706164541_23"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b842352706163417_27"><a name="b842352706163417_27"></a><a name="b842352706163417_27"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8307988"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p1858451"><a name="p1858451"></a><a name="p1858451"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.73%" headers="mcps1.2.4.1.2 "><p id="p16316838"><a name="p16316838"></a><a name="p16316838"></a>List data structure. For details, see <a href="#table32267243">Table 14</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p16706408"><a name="p16706408"></a><a name="p16706408"></a>Indicates the returned <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  14**  jobs field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="27.88278827882788%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b842352706102328_27"><a name="b842352706102328_27"></a><a name="b842352706102328_27"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.78387838783878%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b842352706164541_25"><a name="b842352706164541_25"></a><a name="b842352706164541_25"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b842352706163417_29"><a name="b842352706163417_29"></a><a name="b842352706163417_29"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="27.88278827882788%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.78387838783878%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48259009"><a name="p48259009"></a><a name="p48259009"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  15**  backupStrategy field data structure description

    <a name="table49774232"></a>
    <table><thead align="left"><tr id="row48589216"><th class="cellrowborder" valign="top" width="28.63286328632863%" id="mcps1.2.4.1.1"><p id="p43412436"><a name="p43412436"></a><a name="p43412436"></a><strong id="b842352706102328_29"><a name="b842352706102328_29"></a><a name="b842352706102328_29"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.033803380338036%" id="mcps1.2.4.1.2"><p id="p18974100"><a name="p18974100"></a><a name="p18974100"></a><strong id="b842352706164541_27"><a name="b842352706164541_27"></a><a name="b842352706164541_27"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p60507121"><a name="p60507121"></a><a name="p60507121"></a><strong id="b842352706163417_31"><a name="b842352706163417_31"></a><a name="b842352706163417_31"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13243689"><td class="cellrowborder" valign="top" width="28.63286328632863%" headers="mcps1.2.4.1.1 "><p id="p66105898"><a name="p66105898"></a><a name="p66105898"></a>startTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p63321005"><a name="p63321005"></a><a name="p63321005"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28727808"><a name="p28727808"></a><a name="p28727808"></a>Indicates the backup start time that has been set. The backup task will be triggered within one hour after the backup start time.</p>
    <p id="p2273717816053"><a name="p2273717816053"></a><a name="p2273717816053"></a>The time is in the UTC format.</p>
    </td>
    </tr>
    <tr id="row41459726"><td class="cellrowborder" valign="top" width="28.63286328632863%" headers="mcps1.2.4.1.1 "><p id="p2794650"><a name="p2794650"></a><a name="p2794650"></a>keepDays</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.033803380338036%" headers="mcps1.2.4.1.2 "><p id="p14981763"><a name="p14981763"></a><a name="p14981763"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55740763191711"><a name="p55740763191711"></a><a name="p55740763191711"></a>Indicates the number of days to retain the generated backup files.</p>
    <p id="p31904819191711"><a name="p31904819191711"></a><a name="p31904819191711"></a>The value range is from 0 to 732. If this parameter is <strong id="b842352706112422"><a name="b842352706112422"></a><a name="b842352706112422"></a>0</strong>, the automated backup policy is not set. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "instance": {
            "id": "9fbe7995-9851-47ea-b7af-6037104a1dd5",
            "status": "BUILD",
            "name": "rds-f1d61",
            "created": "",
            "hostname": "",
            "type": "master",
            "region": "eu-de",
            "updated": "",
            "availabilityZone": "eu-de-01",
            "vpc": "2d6d6053-6dd1-46d7-99b4-02c62686a628",
            "nics": {
                "subnetId": "a2c3a6e3-5204-4f53-aa4c-bc3d22c98176"
            },
            "securityGroup": {
                "id": "8c3f8730-f63b-48d4-a183-d0c8a091db8c"
            },
            "flavor": {
                "id": "0d922098-553c-4124-80df-e627a1d41a0d"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dataStoreInfo": null,
            "dbPort": 3306,
            "extendparam": {
                "jobs": [
                    {
                        "id": "ff80808156fd9aee0156fe1fef4a294f"
                    }
                ]
            },
            "backupStrategy": {
                "startTime": "22:00:00",
                "keepDays": 2
            }
        }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

