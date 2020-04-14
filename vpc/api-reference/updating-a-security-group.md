# Updating a Security Group<a name="vpc_sg02_0004"></a>

## Function<a name="section3331610616137"></a>

This API is used to update a security group.

## URI<a name="section1957098316137"></a>

PUT /v2.0/security-groups/\{security\_group\_id\}

## Request Message<a name="section1781687316137"></a>

**Table  1**  Request parameter

<a name="table460557116137"></a>
<table><thead align="left"><tr id="row1322435616137"><th class="cellrowborder" valign="top" width="15.160000000000002%" id="mcps1.2.5.1.1"><p id="p1590492916137"><a name="p1590492916137"></a><a name="p1590492916137"></a><strong id="b1458525917196"><a name="b1458525917196"></a><a name="b1458525917196"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.32%" id="mcps1.2.5.1.2"><p id="p1862451716137"><a name="p1862451716137"></a><a name="p1862451716137"></a><strong id="b2154416203"><a name="b2154416203"></a><a name="b2154416203"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.5.1.3"><p id="p4976459316137"><a name="p4976459316137"></a><a name="p4976459316137"></a><strong id="b11109653101914"><a name="b11109653101914"></a><a name="b11109653101914"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.66%" id="mcps1.2.5.1.4"><p id="p5736665916137"><a name="p5736665916137"></a><a name="p5736665916137"></a><strong id="b24712572019"><a name="b24712572019"></a><a name="b24712572019"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2162479616137"><td class="cellrowborder" valign="top" width="15.160000000000002%" headers="mcps1.2.5.1.1 "><p id="p4116380516137"><a name="p4116380516137"></a><a name="p4116380516137"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.5.1.2 "><p id="p2400419616137"><a name="p2400419616137"></a><a name="p2400419616137"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.5.1.3 "><p id="p2340142616137"><a name="p2340142616137"></a><a name="p2340142616137"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.66%" headers="mcps1.2.5.1.4 "><p id="p4415424716137"><a name="p4415424716137"></a><a name="p4415424716137"></a>Specifies the security group list. For details, see <a href="#table513726041607">Table 2</a>.</p>
<p id="p2337407916137"><a name="p2337407916137"></a><a name="p2337407916137"></a>You must specify at least one attribute when updating a security group.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Security Group**  objects

<a name="table513726041607"></a>
<table><thead align="left"><tr id="row72893461607"><th class="cellrowborder" valign="top" width="23.54%" id="mcps1.2.5.1.1"><p id="p647825491607"><a name="p647825491607"></a><a name="p647825491607"></a><strong id="b3128328122116"><a name="b3128328122116"></a><a name="b3128328122116"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.72%" id="mcps1.2.5.1.2"><p id="p1075015422371"><a name="p1075015422371"></a><a name="p1075015422371"></a><strong id="b157512299213"><a name="b157512299213"></a><a name="b157512299213"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.599999999999998%" id="mcps1.2.5.1.3"><p id="p245230881607"><a name="p245230881607"></a><a name="p245230881607"></a><strong id="b09973011219"><a name="b09973011219"></a><a name="b09973011219"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.14%" id="mcps1.2.5.1.4"><p id="p4542071607"><a name="p4542071607"></a><a name="p4542071607"></a><strong id="b199901030192112"><a name="b199901030192112"></a><a name="b199901030192112"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row356666781607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p270644691607"><a name="p270644691607"></a><a name="p270644691607"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p87501142163712"><a name="p87501142163712"></a><a name="p87501142163712"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p426717071607"><a name="p426717071607"></a><a name="p426717071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p29740751607"><a name="p29740751607"></a><a name="p29740751607"></a>Specifies the security group name.</p>
</td>
</tr>
<tr id="row5261561607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p76095411607"><a name="p76095411607"></a><a name="p76095411607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p11750124243714"><a name="p11750124243714"></a><a name="p11750124243714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p597100051607"><a name="p597100051607"></a><a name="p597100051607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p40269061607"><a name="p40269061607"></a><a name="p40269061607"></a>Provides supplementary information about the security group.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section3049893816137"></a>

**Table  3**  Response parameter

<a name="table821390116137"></a>
<table><thead align="left"><tr id="row2831580216137"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p4903315216137"><a name="p4903315216137"></a><a name="p4903315216137"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p4573700616137"><a name="p4573700616137"></a><a name="p4573700616137"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p6032521316137"><a name="p6032521316137"></a><a name="p6032521316137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1711318416137"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p1178551316137"><a name="p1178551316137"></a><a name="p1178551316137"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p3114620116137"><a name="p3114620116137"></a><a name="p3114620116137"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p5959614316137"><a name="p5959614316137"></a><a name="p5959614316137"></a>Specifies the security group objects. For details, see <a href="#table166682044134519">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Security Group**  objects

<a name="table166682044134519"></a>
<table><thead align="left"><tr id="row146688440458"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p11668744134515"><a name="p11668744134515"></a><a name="p11668744134515"></a><strong id="b1027215342218"><a name="b1027215342218"></a><a name="b1027215342218"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p1668444154513"><a name="p1668444154513"></a><a name="p1668444154513"></a><strong id="b7517203872311"><a name="b7517203872311"></a><a name="b7517203872311"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p186691544154515"><a name="p186691544154515"></a><a name="p186691544154515"></a><strong id="b1533393917231"><a name="b1533393917231"></a><a name="b1533393917231"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row284118681607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p6322881607"><a name="p6322881607"></a><a name="p6322881607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p206339641607"><a name="p206339641607"></a><a name="p206339641607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p538811831607"><a name="p538811831607"></a><a name="p538811831607"></a>Specifies the security group ID.</p>
<p id="p7631141813810"><a name="p7631141813810"></a><a name="p7631141813810"></a>This parameter is not mandatory when you query security groups.</p>
</td>
</tr>
<tr id="row487759591607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p499705331607"><a name="p499705331607"></a><a name="p499705331607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p26621541607"><a name="p26621541607"></a><a name="p26621541607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row0669154474515"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p766954417457"><a name="p766954417457"></a><a name="p766954417457"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p86697446454"><a name="p86697446454"></a><a name="p86697446454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1266984414459"><a name="p1266984414459"></a><a name="p1266984414459"></a>Specifies the security group name.</p>
</td>
</tr>
<tr id="row14669444174515"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1866954418454"><a name="p1866954418454"></a><a name="p1866954418454"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p156691044114516"><a name="p156691044114516"></a><a name="p156691044114516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p156691344114519"><a name="p156691344114519"></a><a name="p156691344114519"></a>Provides supplementary information about the security group.</p>
</td>
</tr>
<tr id="row206696445453"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p17669104411459"><a name="p17669104411459"></a><a name="p17669104411459"></a>security_group_rules</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p263715271607"><a name="p263715271607"></a><a name="p263715271607"></a>Array of <a href="#table655457801607">Security Group Rule</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1466914441454"><a name="p1466914441454"></a><a name="p1466914441454"></a>Specifies the security group rule list. For details, see <a href="#table655457801607">Table 5</a>.</p>
</td>
</tr>
<tr id="row19560720141817"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2044264910305"><a name="p2044264910305"></a><a name="p2044264910305"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row5768162761818"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the security group is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i85011546254"><a name="i85011546254"></a><a name="i85011546254"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row4242824111816"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the security group is updated.</p>
<p id="p28311838161217"><a name="p28311838161217"></a><a name="p28311838161217"></a>Format: <em id="i674435719255"><a name="i674435719255"></a><a name="i674435719255"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  5** **Security Group Rule**  objects

<a name="table655457801607"></a>
<table><thead align="left"><tr id="vpc_sg02_0006_row54478641607"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="vpc_sg02_0006_p389969021607"><a name="vpc_sg02_0006_p389969021607"></a><a name="vpc_sg02_0006_p389969021607"></a><strong id="vpc_sg02_0006_b195868418291"><a name="vpc_sg02_0006_b195868418291"></a><a name="vpc_sg02_0006_b195868418291"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="vpc_sg02_0006_p36789391607"><a name="vpc_sg02_0006_p36789391607"></a><a name="vpc_sg02_0006_p36789391607"></a><strong id="vpc_sg02_0006_b582815515290"><a name="vpc_sg02_0006_b582815515290"></a><a name="vpc_sg02_0006_b582815515290"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="vpc_sg02_0006_p433861031607"><a name="vpc_sg02_0006_p433861031607"></a><a name="vpc_sg02_0006_p433861031607"></a><strong id="vpc_sg02_0006_b198338642916"><a name="vpc_sg02_0006_b198338642916"></a><a name="vpc_sg02_0006_b198338642916"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_sg02_0006_row134774871607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p269083981607"><a name="vpc_sg02_0006_p269083981607"></a><a name="vpc_sg02_0006_p269083981607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p630670281607"><a name="vpc_sg02_0006_p630670281607"></a><a name="vpc_sg02_0006_p630670281607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p334792201607"><a name="vpc_sg02_0006_p334792201607"></a><a name="vpc_sg02_0006_p334792201607"></a>Specifies the security group rule ID.</p>
<p id="vpc_sg02_0006_p529374054010"><a name="vpc_sg02_0006_p529374054010"></a><a name="vpc_sg02_0006_p529374054010"></a>This parameter is not mandatory when you query security group rules.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row250554771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p254411021607"><a name="vpc_sg02_0006_p254411021607"></a><a name="vpc_sg02_0006_p254411021607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p505368621607"><a name="vpc_sg02_0006_p505368621607"></a><a name="vpc_sg02_0006_p505368621607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p480145951607"><a name="vpc_sg02_0006_p480145951607"></a><a name="vpc_sg02_0006_p480145951607"></a>Provides supplementary information about the security group rule.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row569401671607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p115724181607"><a name="vpc_sg02_0006_p115724181607"></a><a name="vpc_sg02_0006_p115724181607"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p615991711607"><a name="vpc_sg02_0006_p615991711607"></a><a name="vpc_sg02_0006_p615991711607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p587796621607"><a name="vpc_sg02_0006_p587796621607"></a><a name="vpc_sg02_0006_p587796621607"></a>Specifies the ID of the belonged security group.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row654332091607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p113008931607"><a name="vpc_sg02_0006_p113008931607"></a><a name="vpc_sg02_0006_p113008931607"></a>remote_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p170542961607"><a name="vpc_sg02_0006_p170542961607"></a><a name="vpc_sg02_0006_p170542961607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p141218971607"><a name="vpc_sg02_0006_p141218971607"></a><a name="vpc_sg02_0006_p141218971607"></a>Specifies the peer ID of the belonged security group.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row9932071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p657989401607"><a name="vpc_sg02_0006_p657989401607"></a><a name="vpc_sg02_0006_p657989401607"></a>direction</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p507988391607"><a name="vpc_sg02_0006_p507988391607"></a><a name="vpc_sg02_0006_p507988391607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p570991491607"><a name="vpc_sg02_0006_p570991491607"></a><a name="vpc_sg02_0006_p570991491607"></a>Specifies the direction of the traffic for which the security group rule takes effect.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row97529031607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p478834691607"><a name="vpc_sg02_0006_p478834691607"></a><a name="vpc_sg02_0006_p478834691607"></a>remote_ip_prefix</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p622759951607"><a name="vpc_sg02_0006_p622759951607"></a><a name="vpc_sg02_0006_p622759951607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p146708701607"><a name="vpc_sg02_0006_p146708701607"></a><a name="vpc_sg02_0006_p146708701607"></a>Specifies the peer IP address segment.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row315033981607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p163656291607"><a name="vpc_sg02_0006_p163656291607"></a><a name="vpc_sg02_0006_p163656291607"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p628340441607"><a name="vpc_sg02_0006_p628340441607"></a><a name="vpc_sg02_0006_p628340441607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p99902671607"><a name="vpc_sg02_0006_p99902671607"></a><a name="vpc_sg02_0006_p99902671607"></a>Specifies the protocol type or the IP protocol number.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row551583771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p97886331607"><a name="vpc_sg02_0006_p97886331607"></a><a name="vpc_sg02_0006_p97886331607"></a>port_range_max</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p343603851607"><a name="vpc_sg02_0006_p343603851607"></a><a name="vpc_sg02_0006_p343603851607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p188144701607"><a name="vpc_sg02_0006_p188144701607"></a><a name="vpc_sg02_0006_p188144701607"></a>Specifies the maximum port number. When ICMP is used, the value is the ICMP code.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row456604071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p630384091607"><a name="vpc_sg02_0006_p630384091607"></a><a name="vpc_sg02_0006_p630384091607"></a>port_range_min</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p337362901607"><a name="vpc_sg02_0006_p337362901607"></a><a name="vpc_sg02_0006_p337362901607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p258562691607"><a name="vpc_sg02_0006_p258562691607"></a><a name="vpc_sg02_0006_p258562691607"></a>Specifies the minimum port number. If the ICMP protocol is used, this parameter indicates the ICMP type.</p>
<p id="vpc_sg02_0006_p5690808615417"><a name="vpc_sg02_0006_p5690808615417"></a><a name="vpc_sg02_0006_p5690808615417"></a>When the TCP or UDP protocol is used, both <strong id="vpc_sg02_0006_b84235270621055"><a name="vpc_sg02_0006_b84235270621055"></a><a name="vpc_sg02_0006_b84235270621055"></a>port_range_max</strong> and <strong id="vpc_sg02_0006_b8423527062112"><a name="vpc_sg02_0006_b8423527062112"></a><a name="vpc_sg02_0006_b8423527062112"></a>port_range_min</strong> must be specified, and the <strong id="vpc_sg02_0006_b43870256421149"><a name="vpc_sg02_0006_b43870256421149"></a><a name="vpc_sg02_0006_b43870256421149"></a>port_range_max</strong> value must be greater than the <strong id="vpc_sg02_0006_b70589128621159"><a name="vpc_sg02_0006_b70589128621159"></a><a name="vpc_sg02_0006_b70589128621159"></a>port_range_min</strong> value.</p>
<p id="vpc_sg02_0006_p4241072615417"><a name="vpc_sg02_0006_p4241072615417"></a><a name="vpc_sg02_0006_p4241072615417"></a>When the ICMP protocol is used, if you specify the ICMP code (<strong id="vpc_sg02_0006_b84235270621317"><a name="vpc_sg02_0006_b84235270621317"></a><a name="vpc_sg02_0006_b84235270621317"></a>port_range_max</strong>), you must also specify the ICMP type (<strong id="vpc_sg02_0006_b84235270621326"><a name="vpc_sg02_0006_b84235270621326"></a><a name="vpc_sg02_0006_b84235270621326"></a>port_range_min</strong>).</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row360773491607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p364292801607"><a name="vpc_sg02_0006_p364292801607"></a><a name="vpc_sg02_0006_p364292801607"></a>ethertype</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p339523071607"><a name="vpc_sg02_0006_p339523071607"></a><a name="vpc_sg02_0006_p339523071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p34728681607"><a name="vpc_sg02_0006_p34728681607"></a><a name="vpc_sg02_0006_p34728681607"></a>Specifies the network type.</p>
<p id="vpc_sg02_0006_p568898621607"><a name="vpc_sg02_0006_p568898621607"></a><a name="vpc_sg02_0006_p568898621607"></a>Only IPv4 is supported.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row532124261607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p593368391607"><a name="vpc_sg02_0006_p593368391607"></a><a name="vpc_sg02_0006_p593368391607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p130282191607"><a name="vpc_sg02_0006_p130282191607"></a><a name="vpc_sg02_0006_p130282191607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p10487112"><a name="vpc_sg02_0006_p10487112"></a><a name="vpc_sg02_0006_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="vpc_sg02_0006_row11992111863317"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p169261732143314"><a name="vpc_sg02_0006_p169261732143314"></a><a name="vpc_sg02_0006_p169261732143314"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p69311132153317"><a name="vpc_sg02_0006_p69311132153317"></a><a name="vpc_sg02_0006_p69311132153317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p13646103310"><a name="vpc_sg02_0006_p13646103310"></a><a name="vpc_sg02_0006_p13646103310"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="vpc_sg02_0006_row10903153923318"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p6634195714335"><a name="vpc_sg02_0006_p6634195714335"></a><a name="vpc_sg02_0006_p6634195714335"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p12638157153319"><a name="vpc_sg02_0006_p12638157153319"></a><a name="vpc_sg02_0006_p12638157153319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p1364635713332"><a name="vpc_sg02_0006_p1364635713332"></a><a name="vpc_sg02_0006_p1364635713332"></a>Specifies the time (UTC) when the security group rule is created.</p>
<p id="vpc_sg02_0006_p65980291419"><a name="vpc_sg02_0006_p65980291419"></a><a name="vpc_sg02_0006_p65980291419"></a>Format: <em id="vpc_sg02_0006_i1034411227245"><a name="vpc_sg02_0006_i1034411227245"></a><a name="vpc_sg02_0006_i1034411227245"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="vpc_sg02_0006_row1797311427338"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p1725445103416"><a name="vpc_sg02_0006_p1725445103416"></a><a name="vpc_sg02_0006_p1725445103416"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p192601514345"><a name="vpc_sg02_0006_p192601514345"></a><a name="vpc_sg02_0006_p192601514345"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p1127018513343"><a name="vpc_sg02_0006_p1127018513343"></a><a name="vpc_sg02_0006_p1127018513343"></a>Specifies the time (UTC) when the security group rule is updated.</p>
<p id="vpc_sg02_0006_p19850105451210"><a name="vpc_sg02_0006_p19850105451210"></a><a name="vpc_sg02_0006_p19850105451210"></a>Format: <em id="vpc_sg02_0006_i1647183316242"><a name="vpc_sg02_0006_i1647183316242"></a><a name="vpc_sg02_0006_i1647183316242"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section2347777416137"></a>

Example request

```
PUT https://{Endpoint}/v2.0/security-groups/d29ae17d-f355-4992-8747-1fb66cc9afd2 
 
{
    "security_group": {
           "name": "sg-test02"
    }
}
```

Example response

```
{
    "security_group": {
        "id": "d29ae17d-f355-4992-8747-1fb66cc9afd2",
        "name": "sg-test02",
        "description": "",
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "security_group_rules": [
            {
                "id": "6332de3e-98fb-4f8c-b44a-fcb8ff09881e",
                "direction": "egress",
                "protocol": null,
                "ethertype": "IPv6",
                "description": null,
                "remote_group_id": null,
                "remote_ip_prefix": null,
                "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
                "port_range_max": null,
                "port_range_min": null,
                "security_group_id": "d29ae17d-f355-4992-8747-1fb66cc9afd2"
            },
            {
                "id": "3f51e52c-0e85-40f7-a137-85927392e436",
                "direction": "egress",
                "protocol": null,
                "ethertype": "IPv4",
                "description": null,
                "remote_group_id": null,
                "remote_ip_prefix": null,
                "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
                "port_range_max": null,
                "port_range_min": null,
                "security_group_id": "d29ae17d-f355-4992-8747-1fb66cc9afd2"
            }
        ],
        "created_at": "2018-09-20T02:15:34",
        "updated_at": "2018-09-20T02:16:31"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

