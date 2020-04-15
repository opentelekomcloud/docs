# Querying Details About ECSs<a name="EN-US_TOPIC_0020212689"></a>

## Function<a name="section33716833"></a>

This API is used to query details about ECSs.

## URI<a name="section35016046"></a>

GET /v2/\{project\_id\}/servers/detail\{?changes-since,image,flavor,name,status,limit,marker,not-tags,reservation\_id,ip\}

GET /v2.1/\{project\_id\}/servers/detail\{?changes-since,image,flavor,name,status,limit,marker,not-tags,reservation\_id,ip\}

[Table 1](#table31251786)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table31251786"></a>
<table><thead align="left"><tr id="row43455040"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41845253"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p34022319"><a name="p34022319"></a><a name="p34022319"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p4344474"><a name="p4344474"></a><a name="p4344474"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section52316204200"></a>

[Table 2](#table49939793)  describes the request parameters.

**Table  2**  Request parameters

<a name="table49939793"></a>
<table><thead align="left"><tr id="row40936054"><th class="cellrowborder" valign="top" width="18.808119188081196%" id="mcps1.2.5.1.1"><p id="p83031738192710"><a name="p83031738192710"></a><a name="p83031738192710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.518248175182485%" id="mcps1.2.5.1.2"><p id="p11776988"><a name="p11776988"></a><a name="p11776988"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.978502149785026%" id="mcps1.2.5.1.3"><p id="p14412003"><a name="p14412003"></a><a name="p14412003"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.695130486951314%" id="mcps1.2.5.1.4"><p id="p37367427"><a name="p37367427"></a><a name="p37367427"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row762524"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p61764512"><a name="p61764512"></a><a name="p61764512"></a>changes-since</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p36869576"><a name="p36869576"></a><a name="p36869576"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p33645693"><a name="p33645693"></a><a name="p33645693"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p32975066"><a name="p32975066"></a><a name="p32975066"></a>Specifies the timestamp of the last ECS status update, which is used to filter out the ECSs with statues updated later than the timestamp. The format must comply with ISO 8601 in the format of CCYY-MM-DDThh:mm:ss+/-hh:mm, for example, 2018-01-17T03:03:32Z.</p>
</td>
</tr>
<tr id="row28340140"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p13849974"><a name="p13849974"></a><a name="p13849974"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p48106092"><a name="p48106092"></a><a name="p48106092"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p4279416"><a name="p4279416"></a><a name="p4279416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p1146019416233"><a name="p1146019416233"></a><a name="p1146019416233"></a>Specifies the image ID.</p>
<p id="p10460540235"><a name="p10460540235"></a><a name="p10460540235"></a>When image is used as a filter criterion, other filter criteria and paging criteria are not supported. If both the image and other filter criteria are specified, the image filter criterion prevails. If the query criteria do not contain the image filter criterion, API functions are not restricted.</p>
</td>
</tr>
<tr id="row25743851"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p4877220"><a name="p4877220"></a><a name="p4877220"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p59510545"><a name="p59510545"></a><a name="p59510545"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p55624859"><a name="p55624859"></a><a name="p55624859"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p16768629"><a name="p16768629"></a><a name="p16768629"></a>Specifies the ECS flavor ID, which is fuzzy matched.</p>
</td>
</tr>
<tr id="row16699940"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p10517875"><a name="p10517875"></a><a name="p10517875"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p46641535"><a name="p46641535"></a><a name="p46641535"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p19867951"><a name="p19867951"></a><a name="p19867951"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p55330634"><a name="p55330634"></a><a name="p55330634"></a>Specifies the ECS name, which is fuzzy matched.</p>
</td>
</tr>
<tr id="row28213660"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p3605162"><a name="p3605162"></a><a name="p3605162"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p23582716"><a name="p23582716"></a><a name="p23582716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p31151867"><a name="p31151867"></a><a name="p31151867"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p26915331"><a name="p26915331"></a><a name="p26915331"></a>Specifies the ECS status.</p>
<p id="p13233363305"><a name="p13233363305"></a><a name="p13233363305"></a>Options:</p>
<p id="p542819271910"><a name="p542819271910"></a><a name="p542819271910"></a><strong id="b136711921172718"><a name="b136711921172718"></a><a name="b136711921172718"></a>ACTIVE</strong>, <strong id="b12672921192719"><a name="b12672921192719"></a><a name="b12672921192719"></a>BUILD</strong>, <strong id="b1867352112272"><a name="b1867352112272"></a><a name="b1867352112272"></a>ERROR</strong>, <strong id="b6674162122710"><a name="b6674162122710"></a><a name="b6674162122710"></a>HARD_REBOOT</strong>, <strong id="b1967522132719"><a name="b1967522132719"></a><a name="b1967522132719"></a>MIGRATING</strong>, <strong id="b176761021122713"><a name="b176761021122713"></a><a name="b176761021122713"></a>REBOOT</strong>, <strong id="b1676221122717"><a name="b1676221122717"></a><a name="b1676221122717"></a>REBUILD</strong>, <strong id="b1167716214277"><a name="b1167716214277"></a><a name="b1167716214277"></a>RESIZE</strong>, <strong id="b06781721172720"><a name="b06781721172720"></a><a name="b06781721172720"></a>REVERT_RESIZE</strong>, <strong id="b36789219272"><a name="b36789219272"></a><a name="b36789219272"></a>SHUTOFF</strong>, and <strong id="b2679112142711"><a name="b2679112142711"></a><a name="b2679112142711"></a>VERIFY_RESIZE</strong></p>
<p id="p168361158173715"><a name="p168361158173715"></a><a name="p168361158173715"></a>In microversion 2.37, the system will return an empty list for the <strong id="b842352706171434"><a name="b842352706171434"></a><a name="b842352706171434"></a>status</strong> field out of the preceding options. In microversion 2.38 and later, the system will return error 404.</p>
<p id="p149623445412"><a name="p149623445412"></a><a name="p149623445412"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row63147504"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p14674162"><a name="p14674162"></a><a name="p14674162"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p47756489"><a name="p47756489"></a><a name="p47756489"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p43070429"><a name="p43070429"></a><a name="p43070429"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p58503618"><a name="p58503618"></a><a name="p58503618"></a>Specifies the upper limit on the number of returned results.</p>
</td>
</tr>
<tr id="row56770522"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p35009555"><a name="p35009555"></a><a name="p35009555"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p17201705"><a name="p17201705"></a><a name="p17201705"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p51160835"><a name="p51160835"></a><a name="p51160835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p50829401"><a name="p50829401"></a><a name="p50829401"></a>Specifies the marker that points to the ECS ID. The query will start from its next ID.</p>
</td>
</tr>
<tr id="row202625131377"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p1077175414512"><a name="p1077175414512"></a><a name="p1077175414512"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p1277165415514"><a name="p1277165415514"></a><a name="p1277165415514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p1277120547517"><a name="p1277120547517"></a><a name="p1277120547517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p144283244132"><a name="p144283244132"></a><a name="p144283244132"></a>Queries ECSs with tags containing the specified value.</p>
</td>
</tr>
<tr id="row3418391114343"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p1743343514343"><a name="p1743343514343"></a><a name="p1743343514343"></a>not-tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p282213114343"><a name="p282213114343"></a><a name="p282213114343"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p2726607214343"><a name="p2726607214343"></a><a name="p2726607214343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p497882461442"><a name="p497882461442"></a><a name="p497882461442"></a>Queries ECSs with tags not containing the specified value. The value is the tag key.</p>
<p id="p9642991507"><a name="p9642991507"></a><a name="p9642991507"></a>For details about key rules, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
<div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020212688_p1745221311560"><a name="en-us_topic_0020212688_p1745221311560"></a><a name="en-us_topic_0020212688_p1745221311560"></a>Tag functions have been upgraded on the public cloud. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
<p id="en-us_topic_0020212688_p213418685710"><a name="en-us_topic_0020212688_p213418685710"></a><a name="en-us_topic_0020212688_p213418685710"></a>For example, an existing tag is <strong id="b84235270610509"><a name="b84235270610509"></a><a name="b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "not-tags=a".</p>
</div></div>
</td>
</tr>
<tr id="row15964135162918"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p151431598259"><a name="p151431598259"></a><a name="p151431598259"></a>reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p11452059192515"><a name="p11452059192515"></a><a name="p11452059192515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p0145165992515"><a name="p0145165992515"></a><a name="p0145165992515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p191452591254"><a name="p191452591254"></a><a name="p191452591254"></a>Specifies the ID returned when ECSs are created in a batch. This parameter is used to query ECSs created in a batch.</p>
</td>
</tr>
<tr id="row2066412186"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p1066412283"><a name="p1066412283"></a><a name="p1066412283"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p15661012780"><a name="p15661012780"></a><a name="p15661012780"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p158210121988"><a name="p158210121988"></a><a name="p158210121988"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p576212355010"><a name="p576212355010"></a><a name="p576212355010"></a>Sorts query results by ECS attribute. The default sorting order is the reverse order of <strong id="b842352706205222"><a name="b842352706205222"></a><a name="b842352706205222"></a>created_at</strong>.</p>
<p id="p1631350906"><a name="p1631350906"></a><a name="p1631350906"></a>Options: <strong id="b197861251143"><a name="b197861251143"></a><a name="b197861251143"></a>created_at</strong>, <strong id="b1278645110414"><a name="b1278645110414"></a><a name="b1278645110414"></a>availability_zone</strong>, <strong id="b207862511348"><a name="b207862511348"></a><a name="b207862511348"></a>display_name</strong>, <strong id="b878713511045"><a name="b878713511045"></a><a name="b878713511045"></a>host</strong>, <strong id="b1778735116411"><a name="b1778735116411"></a><a name="b1778735116411"></a>instance_type_id</strong>, <strong id="b8788175111411"><a name="b8788175111411"></a><a name="b8788175111411"></a>key_name</strong>, <strong id="b147881451747"><a name="b147881451747"></a><a name="b147881451747"></a>project_id</strong>, <strong id="b37888511542"><a name="b37888511542"></a><a name="b37888511542"></a>user_id</strong>, <strong id="b1478812511942"><a name="b1478812511942"></a><a name="b1478812511942"></a>updated_at</strong>, <strong id="b187895511414"><a name="b187895511414"></a><a name="b187895511414"></a>uuid</strong>, and <strong id="b197892051342"><a name="b197892051342"></a><a name="b197892051342"></a>vm_state</strong></p>
</td>
</tr>
<tr id="row1346404515154"><td class="cellrowborder" valign="top" width="18.808119188081196%" headers="mcps1.2.5.1.1 "><p id="p1646514518158"><a name="p1646514518158"></a><a name="p1646514518158"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="17.518248175182485%" headers="mcps1.2.5.1.2 "><p id="p1446519457156"><a name="p1446519457156"></a><a name="p1446519457156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.978502149785026%" headers="mcps1.2.5.1.3 "><p id="p1846584518155"><a name="p1846584518155"></a><a name="p1846584518155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.695130486951314%" headers="mcps1.2.5.1.4 "><p id="p546524517153"><a name="p546524517153"></a><a name="p546524517153"></a>Indicates the IPv4 address filtering result.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section17727455"></a>

[Table 3](#table61256692)  describes the response parameters.

**Table  3**  Response parameters

<a name="table61256692"></a>
<table><thead align="left"><tr id="row16697504"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p151881852192720"><a name="p151881852192720"></a><a name="p151881852192720"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p429128"><a name="p429128"></a><a name="p429128"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.91%" id="mcps1.2.4.1.3"><p id="p34759433"><a name="p34759433"></a><a name="p34759433"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64050727"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p20726409"><a name="p20726409"></a><a name="p20726409"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p23416123"><a name="p23416123"></a><a name="p23416123"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.91%" headers="mcps1.2.4.1.3 "><p id="p24702645"><a name="p24702645"></a><a name="p24702645"></a>Specifies the ECSs to be queried. For details, see <a href="#table1549812072413">Table 4</a>.</p>
</td>
</tr>
<tr id="row5635120017432"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p104447017432"><a name="p104447017432"></a><a name="p104447017432"></a>servers_links</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p1749328217432"><a name="p1749328217432"></a><a name="p1749328217432"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.91%" headers="mcps1.2.4.1.3 "><p id="p766970517432"><a name="p766970517432"></a><a name="p766970517432"></a>Specifies the link of the next page in pagination query. For details, see <a href="#table16539321">Table 7</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **servers**  field description

<a name="table1549812072413"></a>
<table><thead align="left"><tr id="row1548112082413"><th class="cellrowborder" valign="top" width="18.78%" id="mcps1.2.4.1.1"><p id="p17285123172813"><a name="p17285123172813"></a><a name="p17285123172813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p83011731182817"><a name="p83011731182817"></a><a name="p83011731182817"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.8%" id="mcps1.2.4.1.3"><p id="p1230114317281"><a name="p1230114317281"></a><a name="p1230114317281"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1548212052418"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p7482120192416"><a name="p7482120192416"></a><a name="p7482120192416"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p948210207248"><a name="p948210207248"></a><a name="p948210207248"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p34821220112420"><a name="p34821220112420"></a><a name="p34821220112420"></a>Specifies the ECS name.</p>
</td>
</tr>
<tr id="row174821720142411"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p6482320202414"><a name="p6482320202414"></a><a name="p6482320202414"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1348242010244"><a name="p1348242010244"></a><a name="p1348242010244"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p548272092414"><a name="p548272092414"></a><a name="p548272092414"></a>Specifies an ECS uniquely.</p>
</td>
</tr>
<tr id="row19483920182415"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1482520122415"><a name="p1482520122415"></a><a name="p1482520122415"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p11483162010242"><a name="p11483162010242"></a><a name="p11483162010242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p7483620172414"><a name="p7483620172414"></a><a name="p7483620172414"></a>Specifies the ECS status.</p>
<p id="p15483172014245"><a name="p15483172014245"></a><a name="p15483172014245"></a>Options:</p>
<p id="p728611453912"><a name="p728611453912"></a><a name="p728611453912"></a><strong id="b842352706232632"><a name="b842352706232632"></a><a name="b842352706232632"></a>ACTIVE</strong>, <strong id="b842352706232725"><a name="b842352706232725"></a><a name="b842352706232725"></a>BUILD</strong>, <strong id="b842352706232730"><a name="b842352706232730"></a><a name="b842352706232730"></a>DELETED</strong>, <strong id="b842352706232733"><a name="b842352706232733"></a><a name="b842352706232733"></a>ERROR</strong>, <strong id="b842352706232736"><a name="b842352706232736"></a><a name="b842352706232736"></a>HARD_REBOOT</strong>, <strong id="b842352706232740"><a name="b842352706232740"></a><a name="b842352706232740"></a>MIGRATING</strong>, <strong id="b842352706232747"><a name="b842352706232747"></a><a name="b842352706232747"></a>PAUSED</strong>, <strong id="b842352706232751"><a name="b842352706232751"></a><a name="b842352706232751"></a>REBOOT</strong>, <strong id="b842352706232754"><a name="b842352706232754"></a><a name="b842352706232754"></a>REBUILD</strong>, <strong id="b842352706232758"><a name="b842352706232758"></a><a name="b842352706232758"></a>RESIZE</strong>, <strong id="b84235270623282"><a name="b84235270623282"></a><a name="b84235270623282"></a>REVERT_RESIZE</strong>, <strong id="b84235270623285"><a name="b84235270623285"></a><a name="b84235270623285"></a>SHUTOFF</strong>, <strong id="b84235270623289"><a name="b84235270623289"></a><a name="b84235270623289"></a>SHELVED</strong>, <strong id="b842352706232812"><a name="b842352706232812"></a><a name="b842352706232812"></a>SHELVED_OFFLOADED</strong>, <strong id="b842352706232816"><a name="b842352706232816"></a><a name="b842352706232816"></a>SOFT_DELETED</strong>, <strong id="b842352706232819"><a name="b842352706232819"></a><a name="b842352706232819"></a>SUSPENDED</strong>, and <strong id="b842352706232721"><a name="b842352706232721"></a><a name="b842352706232721"></a>VERIFY_RESIZE</strong></p>
<p id="p34821646135413"><a name="p34821646135413"></a><a name="p34821646135413"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row204831920202413"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1148362014246"><a name="p1148362014246"></a><a name="p1148362014246"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p9483112019245"><a name="p9483112019245"></a><a name="p9483112019245"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p9483120172419"><a name="p9483120172419"></a><a name="p9483120172419"></a>Specifies the time when the ECS was created. The time is in the format of "2019-05-22T07:48:53Z".</p>
</td>
</tr>
<tr id="row948452042410"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p12483202082411"><a name="p12483202082411"></a><a name="p12483202082411"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p124849201244"><a name="p124849201244"></a><a name="p124849201244"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p184846209241"><a name="p184846209241"></a><a name="p184846209241"></a>Specifies the time when the ECS was updated last time. The time is in the format of "2019-05-22T07:48:53Z".</p>
</td>
</tr>
<tr id="row1748412052419"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1848482062410"><a name="p1848482062410"></a><a name="p1848482062410"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1484202016247"><a name="p1484202016247"></a><a name="p1484202016247"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p448472092419"><a name="p448472092419"></a><a name="p448472092419"></a>Specifies the ECS flavor.</p>
<p id="p1089830141117"><a name="p1089830141117"></a><a name="p1089830141117"></a>For details, see <a href="#table19588408">Table 5</a>.</p>
</td>
</tr>
<tr id="row4485152072417"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p548452052412"><a name="p548452052412"></a><a name="p548452052412"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p19484620132419"><a name="p19484620132419"></a><a name="p19484620132419"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1485162013249"><a name="p1485162013249"></a><a name="p1485162013249"></a>Specifies the ECS image information. For an ECS created using an image, the image ID and link are returned.</p>
<p id="p1828675713485"><a name="p1828675713485"></a><a name="p1828675713485"></a>For details, see <a href="#table1080891111402">Table 12</a>.</p>
</td>
</tr>
<tr id="row154851208245"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p10485220202414"><a name="p10485220202414"></a><a name="p10485220202414"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p648512014246"><a name="p648512014246"></a><a name="p648512014246"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p10485182017246"><a name="p10485182017246"></a><a name="p10485182017246"></a>Specifies the ID of the tenant to which the ECS belongs. The parameter value is the same as the project ID specified by <strong id="b1920793135115"><a name="b1920793135115"></a><a name="b1920793135115"></a>project_id</strong>.</p>
</td>
</tr>
<tr id="row13486320172411"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p5485122042411"><a name="p5485122042411"></a><a name="p5485122042411"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p11485202072415"><a name="p11485202072415"></a><a name="p11485202072415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1485120202420"><a name="p1485120202420"></a><a name="p1485120202420"></a>Specifies the SSH key name.</p>
</td>
</tr>
<tr id="row1548692072411"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p204861320122415"><a name="p204861320122415"></a><a name="p204861320122415"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1448642072417"><a name="p1448642072417"></a><a name="p1448642072417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1448682020243"><a name="p1448682020243"></a><a name="p1448682020243"></a>Specifies the ID of the user to which an ECS belongs.</p>
</td>
</tr>
<tr id="row748782022420"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p448611202242"><a name="p448611202242"></a><a name="p448611202242"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p848662017248"><a name="p848662017248"></a><a name="p848662017248"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p64871620152419"><a name="p64871620152419"></a><a name="p64871620152419"></a>Specifies the ECS metadata.</p>
</td>
</tr>
<tr id="row448720203246"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p4487122082413"><a name="p4487122082413"></a><a name="p4487122082413"></a>hostId</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p18487620152413"><a name="p18487620152413"></a><a name="p18487620152413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p9487112020247"><a name="p9487112020247"></a><a name="p9487112020247"></a>Specifies the host ID of the ECS.</p>
</td>
</tr>
<tr id="row9488102018244"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p5487182092415"><a name="p5487182092415"></a><a name="p5487182092415"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p104877201246"><a name="p104877201246"></a><a name="p104877201246"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p548802020243"><a name="p548802020243"></a><a name="p548802020243"></a>Specifies the network addresses of an ECS.</p>
<p id="p11732124819142"><a name="p11732124819142"></a><a name="p11732124819142"></a>For details, see <a href="#table3730161">Table 6</a>.</p>
</td>
</tr>
<tr id="row7488142016248"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p148872020247"><a name="p148872020247"></a><a name="p148872020247"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p154882201243"><a name="p154882201243"></a><a name="p154882201243"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1648872013244"><a name="p1648872013244"></a><a name="p1648872013244"></a>Specifies the security groups to which the ECS belongs.</p>
<p id="p14944151210151"><a name="p14944151210151"></a><a name="p14944151210151"></a>For details, see <a href="#table761507165933">Table 10</a>.</p>
</td>
</tr>
<tr id="row15488820152416"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p548811201248"><a name="p548811201248"></a><a name="p548811201248"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p7488620102418"><a name="p7488620102418"></a><a name="p7488620102418"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1488122019249"><a name="p1488122019249"></a><a name="p1488122019249"></a>Specifies ECS shortcut links.</p>
<p id="p1359134614158"><a name="p1359134614158"></a><a name="p1359134614158"></a>For details, see <a href="#table16539321">Table 7</a>.</p>
</td>
</tr>
<tr id="row104894203243"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1448882052415"><a name="p1448882052415"></a><a name="p1448882052415"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p14488820122413"><a name="p14488820122413"></a><a name="p14488820122413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p2048819204245"><a name="p2048819204245"></a><a name="p2048819204245"></a>Specifies the disk configuration mode. This is an extended attribute. This field is valid for the ECS started using an image.</p>
<p id="p13489132012240"><a name="p13489132012240"></a><a name="p13489132012240"></a>Options:</p>
<a name="ul948972012249"></a><a name="ul948972012249"></a><ul id="ul948972012249"><li><strong id="b84235270620172"><a name="b84235270620172"></a><a name="b84235270620172"></a>AUTO</strong>: This API uses a single partition to build an ECS with the target disk size. The API automatically adjusts the file system to adapt to the entire partition.</li><li><strong id="b842352706201852"><a name="b842352706201852"></a><a name="b842352706201852"></a>MANUAL</strong>: This API uses the partitioning scheme in the source image and the file system to build the ECS. If the target disk size is large, the API does not partition the remaining disk space.</li></ul>
</td>
</tr>
<tr id="row17489142082419"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p2489132011245"><a name="p2489132011245"></a><a name="p2489132011245"></a>OS-EXT-AZ:availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p11489320152410"><a name="p11489320152410"></a><a name="p11489320152410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p144898207242"><a name="p144898207242"></a><a name="p144898207242"></a>Specifies the AZ ID. This is an extended attribute.</p>
</td>
</tr>
<tr id="row13490320112416"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p12489162013248"><a name="p12489162013248"></a><a name="p12489162013248"></a>OS-EXT-SRV-ATTR:host</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1749010206242"><a name="p1749010206242"></a><a name="p1749010206242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p20490172020241"><a name="p20490172020241"></a><a name="p20490172020241"></a>Specifies the name of the host on which the ECS is deployed. This is an extended attribute.</p>
</td>
</tr>
<tr id="row44918205242"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p17490162014240"><a name="p17490162014240"></a><a name="p17490162014240"></a>OS-EXT-SRV-ATTR:hypervisor_hostname</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1749015202242"><a name="p1749015202242"></a><a name="p1749015202242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p7490020162410"><a name="p7490020162410"></a><a name="p7490020162410"></a>Specifies the hostname of the hypervisor. This is an extended attribute.</p>
</td>
</tr>
<tr id="row2491420172417"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1949113206248"><a name="p1949113206248"></a><a name="p1949113206248"></a>OS-EXT-SRV-ATTR:instance_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1149192022415"><a name="p1149192022415"></a><a name="p1149192022415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p104919201241"><a name="p104919201241"></a><a name="p104919201241"></a>Specifies the ECS ID. This is an extended attribute.</p>
</td>
</tr>
<tr id="row14492520122419"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p5491142013241"><a name="p5491142013241"></a><a name="p5491142013241"></a>OS-EXT-STS:power_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p9491120132410"><a name="p9491120132410"></a><a name="p9491120132410"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p149116209246"><a name="p149116209246"></a><a name="p149116209246"></a>Specifies the ECS power status. This is an extended attribute.</p>
<p id="p1749162013245"><a name="p1749162013245"></a><a name="p1749162013245"></a>Options: 0, 1, 2, 3, and 4</p>
<a name="ul154921920112413"></a><a name="ul154921920112413"></a><ul id="ul154921920112413"><li><strong id="b84235270617432"><a name="b84235270617432"></a><a name="b84235270617432"></a>0</strong>: pending</li><li><strong id="b842352706174310"><a name="b842352706174310"></a><a name="b842352706174310"></a>1</strong>: running</li><li><strong id="b842352706174319"><a name="b842352706174319"></a><a name="b842352706174319"></a>2</strong>: paused</li><li><strong id="b842352706174326"><a name="b842352706174326"></a><a name="b842352706174326"></a>3</strong>: shutdown</li><li><strong id="b842352706174333"><a name="b842352706174333"></a><a name="b842352706174333"></a>4</strong>: crashed</li></ul>
</td>
</tr>
<tr id="row12492182018247"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p16492142014240"><a name="p16492142014240"></a><a name="p16492142014240"></a>OS-EXT-STS:task_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p12492132082410"><a name="p12492132082410"></a><a name="p12492132082410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p6492120102416"><a name="p6492120102416"></a><a name="p6492120102416"></a>Specifies the ECS task status. This is an extended attribute.</p>
<p id="p13922047162612"><a name="p13922047162612"></a><a name="p13922047162612"></a>For details about options, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row104922209248"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p154927206241"><a name="p154927206241"></a><a name="p154927206241"></a>OS-EXT-STS:vm_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p204926207240"><a name="p204926207240"></a><a name="p204926207240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p14492112013243"><a name="p14492112013243"></a><a name="p14492112013243"></a>Specifies the ECS status. This is an extended attribute.</p>
<p id="p184927203240"><a name="p184927203240"></a><a name="p184927203240"></a>Options:</p>
<p id="p1149222082418"><a name="p1149222082418"></a><a name="p1149222082418"></a><strong id="b842352706145916"><a name="b842352706145916"></a><a name="b842352706145916"></a>ACTIVE</strong>, <strong id="b842352706145922"><a name="b842352706145922"></a><a name="b842352706145922"></a>BUILDING</strong>, <strong id="b842352706145926"><a name="b842352706145926"></a><a name="b842352706145926"></a>STOPPED</strong>, <strong id="b39534363719"><a name="b39534363719"></a><a name="b39534363719"></a>RESIZED</strong>, <strong id="b842352706145932"><a name="b842352706145932"></a><a name="b842352706145932"></a>PAUSED</strong>, <strong id="b842352706145937"><a name="b842352706145937"></a><a name="b842352706145937"></a>SUSPENDED</strong>, <strong id="b842352706145942"><a name="b842352706145942"></a><a name="b842352706145942"></a>RESCUED</strong>, <strong id="b842352706145948"><a name="b842352706145948"></a><a name="b842352706145948"></a>ERROR</strong>, <strong id="b842352706145952"><a name="b842352706145952"></a><a name="b842352706145952"></a>DELETED</strong>, <strong id="b842352706145957"><a name="b842352706145957"></a><a name="b842352706145957"></a>SOFT_DELETED</strong>, <strong id="b8423527061503"><a name="b8423527061503"></a><a name="b8423527061503"></a>SHELVED</strong>, and <strong id="b8423527061508"><a name="b8423527061508"></a><a name="b8423527061508"></a>SHELVED_OFFLOADED</strong></p>
<p id="p824835116542"><a name="p824835116542"></a><a name="p824835116542"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row6492220132410"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p194926206240"><a name="p194926206240"></a><a name="p194926206240"></a>OS-SRV-USG:launched_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p04925208249"><a name="p04925208249"></a><a name="p04925208249"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1649212011249"><a name="p1649212011249"></a><a name="p1649212011249"></a>Specifies the time when the ECS was started. This is an extended attribute. The time is in the format of "2019-05-22T07:48:19.000000".</p>
</td>
</tr>
<tr id="row7493120142419"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p7492202012241"><a name="p7492202012241"></a><a name="p7492202012241"></a>OS-SRV-USG:terminated_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p11492122013248"><a name="p11492122013248"></a><a name="p11492122013248"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p849212201243"><a name="p849212201243"></a><a name="p849212201243"></a>Specifies the time when the ECS was deleted. This is an extended attribute.</p>
<p id="p64281698378"><a name="p64281698378"></a><a name="p64281698378"></a>The time is in the format of "2019-05-22T07:48:19.000000".</p>
</td>
</tr>
<tr id="row1749342013247"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p15493172092417"><a name="p15493172092417"></a><a name="p15493172092417"></a>os-extended-volumes:volumes_attached</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p149302062415"><a name="p149302062415"></a><a name="p149302062415"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p18493102022412"><a name="p18493102022412"></a><a name="p18493102022412"></a>Specifies information about the EVS disks attached to the ECS.</p>
<p id="p382215381616"><a name="p382215381616"></a><a name="p382215381616"></a>For details, see <a href="#table20591095122442">Table 9</a>.</p>
</td>
</tr>
<tr id="row171521018120"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p43095310"><a name="en-us_topic_0057972887_p43095310"></a><a name="en-us_topic_0057972887_p43095310"></a>fault</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p1059226"><a name="en-us_topic_0057972887_p1059226"></a><a name="en-us_topic_0057972887_p1059226"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p37371779"><a name="en-us_topic_0057972887_p37371779"></a><a name="en-us_topic_0057972887_p37371779"></a>Specifies the ECS fault.</p>
<p id="p14777766535"><a name="p14777766535"></a><a name="p14777766535"></a>This parameter is optional. It is returned when an error occurs on an ECS.</p>
<p id="p1688015424530"><a name="p1688015424530"></a><a name="p1688015424530"></a>For details, see <a href="#table1075312230549">Table 11</a>.</p>
</td>
</tr>
<tr id="row510213452422"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p57463526"><a name="en-us_topic_0057972887_p57463526"></a><a name="en-us_topic_0057972887_p57463526"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p24034004"><a name="en-us_topic_0057972887_p24034004"></a><a name="en-us_topic_0057972887_p24034004"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p48379233"><a name="en-us_topic_0057972887_p48379233"></a><a name="en-us_topic_0057972887_p48379233"></a>Specifies the description of the ECS.</p>
<p id="p28201545155518"><a name="p28201545155518"></a><a name="p28201545155518"></a>This field is supported in microversions later than 2.19.</p>
</td>
</tr>
<tr id="row1280618575423"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p58332432"><a name="en-us_topic_0057972887_p58332432"></a><a name="en-us_topic_0057972887_p58332432"></a>host_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p27306569"><a name="en-us_topic_0057972887_p27306569"></a><a name="en-us_topic_0057972887_p27306569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p44841923"><a name="en-us_topic_0057972887_p44841923"></a><a name="en-us_topic_0057972887_p44841923"></a>Specifies the nova-compute status.</p>
<a name="en-us_topic_0057972887_ul924126"></a><a name="en-us_topic_0057972887_ul924126"></a><ul id="en-us_topic_0057972887_ul924126"><li><strong id="b47785605320"><a name="b47785605320"></a><a name="b47785605320"></a>UP</strong>: The nova-compute status is normal.</li><li><strong id="b7237612135314"><a name="b7237612135314"></a><a name="b7237612135314"></a>UNKNOWN</strong>: The nova-compute status is unknown.</li><li><strong id="b123601314115310"><a name="b123601314115310"></a><a name="b123601314115310"></a>DOWN</strong>: the nova-compute status is abnormal.</li><li><strong id="b126104168538"><a name="b126104168538"></a><a name="b126104168538"></a>MAINTENANCE</strong>: The nova-compute is in maintenance state.</li><li><strong id="b84235270618336"><a name="b84235270618336"></a><a name="b84235270618336"></a>Null</strong>: The ECS does not have host information.</li></ul>
<p id="p1359417427544"><a name="p1359417427544"></a><a name="p1359417427544"></a>This field is supported in microversions later than 2.16.</p>
</td>
</tr>
<tr id="row147284114435"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p7131169"><a name="en-us_topic_0057972887_p7131169"></a><a name="en-us_topic_0057972887_p7131169"></a>OS-EXT-SRV-ATTR:hostname</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p40753854"><a name="en-us_topic_0057972887_p40753854"></a><a name="en-us_topic_0057972887_p40753854"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p24324288"><a name="en-us_topic_0057972887_p24324288"></a><a name="en-us_topic_0057972887_p24324288"></a>Specifies the ECS hostname.</p>
<p id="p3479627194317"><a name="p3479627194317"></a><a name="p3479627194317"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row27291011437"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p6779396"><a name="en-us_topic_0057972887_p6779396"></a><a name="en-us_topic_0057972887_p6779396"></a>OS-EXT-SRV-ATTR:reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p12260243"><a name="en-us_topic_0057972887_p12260243"></a><a name="en-us_topic_0057972887_p12260243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p43041107"><a name="en-us_topic_0057972887_p43041107"></a><a name="en-us_topic_0057972887_p43041107"></a>Specifies reserved ECS IDs if ECSs are created in a batch.</p>
<p id="p18137583436"><a name="p18137583436"></a><a name="p18137583436"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row7885664315"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p54550808"><a name="en-us_topic_0057972887_p54550808"></a><a name="en-us_topic_0057972887_p54550808"></a>OS-EXT-SRV-ATTR:launch_index</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p56539341"><a name="en-us_topic_0057972887_p56539341"></a><a name="en-us_topic_0057972887_p56539341"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p43927036"><a name="en-us_topic_0057972887_p43927036"></a><a name="en-us_topic_0057972887_p43927036"></a>Specifies the sequence in which ECSs start if the ECSs are created in a batch.</p>
<p id="p12601191124414"><a name="p12601191124414"></a><a name="p12601191124414"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row1788146104320"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p22853796"><a name="en-us_topic_0057972887_p22853796"></a><a name="en-us_topic_0057972887_p22853796"></a>OS-EXT-SRV-ATTR:kernel_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p39218184"><a name="en-us_topic_0057972887_p39218184"></a><a name="en-us_topic_0057972887_p39218184"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p15126299"><a name="en-us_topic_0057972887_p15126299"></a><a name="en-us_topic_0057972887_p15126299"></a>Specifies the UUID of the kernel image if an AMI image is used. In other scenarios, leave this parameter blank.</p>
<p id="p196273244466"><a name="p196273244466"></a><a name="p196273244466"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row1488769432"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p40968939"><a name="en-us_topic_0057972887_p40968939"></a><a name="en-us_topic_0057972887_p40968939"></a>OS-EXT-SRV-ATTR:ramdisk_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p30149753"><a name="en-us_topic_0057972887_p30149753"></a><a name="en-us_topic_0057972887_p30149753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p42710723"><a name="en-us_topic_0057972887_p42710723"></a><a name="en-us_topic_0057972887_p42710723"></a>Specifies the UUID of the Ramdisk image if an AMI image is used. In other scenarios, leave this parameter blank. This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row11894616433"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p7284856"><a name="en-us_topic_0057972887_p7284856"></a><a name="en-us_topic_0057972887_p7284856"></a>OS-EXT-SRV-ATTR:root_device_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p53202458"><a name="en-us_topic_0057972887_p53202458"></a><a name="en-us_topic_0057972887_p53202458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p28127439"><a name="en-us_topic_0057972887_p28127439"></a><a name="en-us_topic_0057972887_p28127439"></a>Specifies the device name of the ECS system disk.</p>
<p id="p11804132124618"><a name="p11804132124618"></a><a name="p11804132124618"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row1288421013435"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p61864358"><a name="en-us_topic_0057972887_p61864358"></a><a name="en-us_topic_0057972887_p61864358"></a>OS-EXT-SRV-ATTR:user_data</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p44957139"><a name="en-us_topic_0057972887_p44957139"></a><a name="en-us_topic_0057972887_p44957139"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p20334069"><a name="en-us_topic_0057972887_p20334069"></a><a name="en-us_topic_0057972887_p20334069"></a>Specifies the user data configured during ECS creation.</p>
<p id="p1815314834617"><a name="p1815314834617"></a><a name="p1815314834617"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row949312017246"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p749372082418"><a name="p749372082418"></a><a name="p749372082418"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p14493420142420"><a name="p14493420142420"></a><a name="p14493420142420"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p1149310203247"><a name="p1149310203247"></a><a name="p1149310203247"></a>Specifies ECS tags.</p>
<p id="p8849035134415"><a name="p8849035134415"></a><a name="p8849035134415"></a>In microversion 2.26, if the microversion is not used for query, the response does not contain the <strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>tags</strong> field.</p>
<div class="p" id="p7300949059"><a name="p7300949059"></a><a name="p7300949059"></a>Tag functions have been upgraded on the public cloud. After the upgrade, the tag values returned by the system comply with the following rules:<a name="ul871515496611"></a><a name="ul871515496611"></a><ul id="ul871515496611"><li>The key and value of a tag are connected using an equal sign (=), for example, key=value.</li><li>If the value is empty, only the key is returned.</li></ul>
</div>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For more details about upgraded tag functions, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
</td>
</tr>
<tr id="row1264933513916"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1253710242210"><a name="p1253710242210"></a><a name="p1253710242210"></a>locked</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1653720241521"><a name="p1653720241521"></a><a name="p1653720241521"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p18537624422"><a name="p18537624422"></a><a name="p18537624422"></a>Specifies the ECS lock status, which is <strong id="b842352706142719"><a name="b842352706142719"></a><a name="b842352706142719"></a>True</strong> when the ECS is locked and <strong id="b842352706142722"><a name="b842352706142722"></a><a name="b842352706142722"></a>False</strong> when the ECS is unlocked.</p>
<p id="p10742257355"><a name="p10742257355"></a><a name="p10742257355"></a>This field is supported in microversions later than 2.9.</p>
</td>
</tr>
<tr id="row249416203244"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p1149317202246"><a name="p1149317202246"></a><a name="p1149317202246"></a>accessIPv4</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p3493182016241"><a name="p3493182016241"></a><a name="p3493182016241"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p449319209247"><a name="p449319209247"></a><a name="p449319209247"></a>Reserved</p>
</td>
</tr>
<tr id="row1249422052417"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p749492020246"><a name="p749492020246"></a><a name="p749492020246"></a>accessIPv6</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1249442052418"><a name="p1249442052418"></a><a name="p1249442052418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p12494132010248"><a name="p12494132010248"></a><a name="p12494132010248"></a>Reserved</p>
</td>
</tr>
<tr id="row24951820172418"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p19494420102411"><a name="p19494420102411"></a><a name="p19494420102411"></a>config_drive</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p194951720152416"><a name="p194951720152416"></a><a name="p194951720152416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p184951720102410"><a name="p184951720102410"></a><a name="p184951720102410"></a>Reserved</p>
</td>
</tr>
<tr id="row4497132062416"><td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.2.4.1.1 "><p id="p84971020122411"><a name="p84971020122411"></a><a name="p84971020122411"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p11497132082416"><a name="p11497132082416"></a><a name="p11497132082416"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.8%" headers="mcps1.2.4.1.3 "><p id="p6497142015243"><a name="p6497142015243"></a><a name="p6497142015243"></a>Reserved</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **flavor**  field description

<a name="table19588408"></a>
<table><thead align="left"><tr id="row65668512"><th class="cellrowborder" valign="top" width="18.740000000000002%" id="mcps1.2.4.1.1"><p id="p2743203852915"><a name="p2743203852915"></a><a name="p2743203852915"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.29%" id="mcps1.2.4.1.2"><p id="p3743193822918"><a name="p3743193822918"></a><a name="p3743193822918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.97%" id="mcps1.2.4.1.3"><p id="p147431638122913"><a name="p147431638122913"></a><a name="p147431638122913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54114449"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p21194271"><a name="p21194271"></a><a name="p21194271"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p6046963"><a name="p6046963"></a><a name="p6046963"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p20041994"><a name="p20041994"></a><a name="p20041994"></a>Specifies the ECS ID.</p>
<p id="p3257118164112"><a name="p3257118164112"></a><a name="p3257118164112"></a>This field is not supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row46160221"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p47990424"><a name="p47990424"></a><a name="p47990424"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p57492083"><a name="p57492083"></a><a name="p57492083"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p35797372"><a name="p35797372"></a><a name="p35797372"></a>Specifies shortcut links for ECS types. For details, see <a href="#table16539321">Table 7</a>.</p>
<p id="p111161238154113"><a name="p111161238154113"></a><a name="p111161238154113"></a>This field is not supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row1464775313405"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p18647653114019"><a name="p18647653114019"></a><a name="p18647653114019"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p5647153194013"><a name="p5647153194013"></a><a name="p5647153194013"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p594712133917"><a name="p594712133917"></a><a name="p594712133917"></a>Specifies the number of vCPUs in the ECS flavor.</p>
<p id="p7411737161018"><a name="p7411737161018"></a><a name="p7411737161018"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row196001658104015"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p460015587400"><a name="p460015587400"></a><a name="p460015587400"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p1760065884017"><a name="p1760065884017"></a><a name="p1760065884017"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p1760065884013"><a name="p1760065884013"></a><a name="p1760065884013"></a>Specifies the memory size (MB) in the ECS flavor.</p>
<p id="p0979145841010"><a name="p0979145841010"></a><a name="p0979145841010"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row3381294117"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p338192124118"><a name="p338192124118"></a><a name="p338192124118"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p143817234115"><a name="p143817234115"></a><a name="p143817234115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p1381422419"><a name="p1381422419"></a><a name="p1381422419"></a>Specifies the system disk size in the ECS flavor. The value <strong id="b193131334144317"><a name="b193131334144317"></a><a name="b193131334144317"></a>0</strong> indicates that the disk size is not limited.</p>
<p id="p155897161110"><a name="p155897161110"></a><a name="p155897161110"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row135994514117"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p175990512419"><a name="p175990512419"></a><a name="p175990512419"></a>ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p55996517419"><a name="p55996517419"></a><a name="p55996517419"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p1059914514118"><a name="p1059914514118"></a><a name="p1059914514118"></a>Reserved</p>
<p id="p138227319114"><a name="p138227319114"></a><a name="p138227319114"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row563019183421"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p66306183429"><a name="p66306183429"></a><a name="p66306183429"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p863019183421"><a name="p863019183421"></a><a name="p863019183421"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p15630121813429"><a name="p15630121813429"></a><a name="p15630121813429"></a>Reserved</p>
<p id="p568210631113"><a name="p568210631113"></a><a name="p568210631113"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row13365133364216"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p1936516339428"><a name="p1936516339428"></a><a name="p1936516339428"></a>original_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p163651333144219"><a name="p163651333144219"></a><a name="p163651333144219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p2365113374215"><a name="p2365113374215"></a><a name="p2365113374215"></a>Specifies the name of the ECS flavor.</p>
<p id="p47911894115"><a name="p47911894115"></a><a name="p47911894115"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row46311636154213"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p136311336194210"><a name="p136311336194210"></a><a name="p136311336194210"></a>extra_specs</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p563116366423"><a name="p563116366423"></a><a name="p563116366423"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.97%" headers="mcps1.2.4.1.3 "><p id="p963110362428"><a name="p963110362428"></a><a name="p963110362428"></a>Extended flavor field</p>
<p id="p10674132212106"><a name="p10674132212106"></a><a name="p10674132212106"></a>For details, see <a href="data-structure-for-query-details-about-specifications.md">os_extra_specs (flavor) Field Description</a>, which is supported in microversions later than 2.47.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **addresses**  field description

<a name="table3730161"></a>
<table><thead align="left"><tr id="row20014316"><th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.4.1.1"><p id="p8834164002918"><a name="p8834164002918"></a><a name="p8834164002918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.04%" id="mcps1.2.4.1.2"><p id="p6834340112912"><a name="p6834340112912"></a><a name="p6834340112912"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.09%" id="mcps1.2.4.1.3"><p id="p18491640162916"><a name="p18491640162916"></a><a name="p18491640162916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57432766"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.4.1.1 "><p id="p2057412833316"><a name="p2057412833316"></a><a name="p2057412833316"></a>Name of the network where the ECS accesses</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p4439518115623"><a name="p4439518115623"></a><a name="p4439518115623"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.09%" headers="mcps1.2.4.1.3 "><p id="p19891184119819"><a name="p19891184119819"></a><a name="p19891184119819"></a>Specifies the network information of the ECS.</p>
<a name="ul1197110522819"></a><a name="ul1197110522819"></a><ul id="ul1197110522819"><li><strong id="b842352706214237"><a name="b842352706214237"></a><a name="b842352706214237"></a>key</strong> indicates the network name, for example, <strong id="b842352706214248"><a name="b842352706214248"></a><a name="b842352706214248"></a>demo_net</strong>.</li><li><strong id="b84235270621435"><a name="b84235270621435"></a><a name="b84235270621435"></a>value</strong> indicates the detailed network information.</li></ul>
<p id="p204137567134"><a name="p204137567134"></a><a name="p204137567134"></a>For details, see <a href="#table1656029015527">Table 8</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **servers\_links**  and  **links**  field description

<a name="table16539321"></a>
<table><thead align="left"><tr id="row4585366"><th class="cellrowborder" valign="top" width="18.790000000000003%" id="mcps1.2.4.1.1"><p id="p1475445290"><a name="p1475445290"></a><a name="p1475445290"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.2"><p id="p14634442298"><a name="p14634442298"></a><a name="p14634442298"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.05%" id="mcps1.2.4.1.3"><p id="p36312446294"><a name="p36312446294"></a><a name="p36312446294"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14455526"><td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.2.4.1.1 "><p id="p30046962"><a name="p30046962"></a><a name="p30046962"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p39387099"><a name="p39387099"></a><a name="p39387099"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.05%" headers="mcps1.2.4.1.3 "><p id="p36238473"><a name="p36238473"></a><a name="p36238473"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row57710802"><td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.2.4.1.1 "><p id="p44063391"><a name="p44063391"></a><a name="p44063391"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p62035831"><a name="p62035831"></a><a name="p62035831"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.05%" headers="mcps1.2.4.1.3 "><p id="p58846418"><a name="p58846418"></a><a name="p58846418"></a>Specifies the shortcut link.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the network which an ECS accesses

<a name="table1656029015527"></a>
<table><thead align="left"><tr id="row2645284715527"><th class="cellrowborder" valign="top" width="18.759999999999998%" id="mcps1.2.4.1.1"><p id="p99491446132918"><a name="p99491446132918"></a><a name="p99491446132918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.259999999999998%" id="mcps1.2.4.1.2"><p id="p49641746132913"><a name="p49641746132913"></a><a name="p49641746132913"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.98%" id="mcps1.2.4.1.3"><p id="p896474622910"><a name="p896474622910"></a><a name="p896474622910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5009697415527"><td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p3132311415527"><a name="p3132311415527"></a><a name="p3132311415527"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p5414433915527"><a name="p5414433915527"></a><a name="p5414433915527"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.98%" headers="mcps1.2.4.1.3 "><p id="p2361534415527"><a name="p2361534415527"></a><a name="p2361534415527"></a>Specifies the IP address.</p>
</td>
</tr>
<tr id="row1121151015527"><td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p3571711715527"><a name="p3571711715527"></a><a name="p3571711715527"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p740535615527"><a name="p740535615527"></a><a name="p740535615527"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.98%" headers="mcps1.2.4.1.3 "><p id="p6296298815527"><a name="p6296298815527"></a><a name="p6296298815527"></a>Specifies the type of an IP address. The value of this parameter can be <strong id="b84235270614154"><a name="b84235270614154"></a><a name="b84235270614154"></a>4</strong> or <strong id="b842352706141510"><a name="b842352706141510"></a><a name="b842352706141510"></a>6</strong>.</p>
<a name="ul2979598615527"></a><a name="ul2979598615527"></a><ul id="ul2979598615527"><li><strong id="b84235270614151"><a name="b84235270614151"></a><a name="b84235270614151"></a>4</strong>: The type of the IP address is IPv4.</li><li><strong id="b842352706141518"><a name="b842352706141518"></a><a name="b842352706141518"></a>6</strong>: The type of the IP address is IPv6.</li></ul>
</td>
</tr>
<tr id="row3913338616494"><td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p37919028165012"><a name="p37919028165012"></a><a name="p37919028165012"></a>OS-EXT-IPS-MAC:mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p51542402165012"><a name="p51542402165012"></a><a name="p51542402165012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.98%" headers="mcps1.2.4.1.3 "><p id="p14185000165012"><a name="p14185000165012"></a><a name="p14185000165012"></a>Specifies the MAC address. This is an extended attribute.</p>
</td>
</tr>
<tr id="row5993434716495"><td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p6100298165012"><a name="p6100298165012"></a><a name="p6100298165012"></a>OS-EXT-IPS:type</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p24362133165012"><a name="p24362133165012"></a><a name="p24362133165012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.98%" headers="mcps1.2.4.1.3 "><p id="p27175732165012"><a name="p27175732165012"></a><a name="p27175732165012"></a>Specifies the IP address assignment mode. This is an extended attribute.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **os-extended-volumes:volumes\_attached**  field description

<a name="table20591095122442"></a>
<table><thead align="left"><tr id="row46969160122442"><th class="cellrowborder" valign="top" width="18.768123187681233%" id="mcps1.2.4.1.1"><p id="p8475185013292"><a name="p8475185013292"></a><a name="p8475185013292"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.198380161983803%" id="mcps1.2.4.1.2"><p id="p849025062918"><a name="p849025062918"></a><a name="p849025062918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.03349665033497%" id="mcps1.2.4.1.3"><p id="p6490750122918"><a name="p6490750122918"></a><a name="p6490750122918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row22997982122442"><td class="cellrowborder" valign="top" width="18.768123187681233%" headers="mcps1.2.4.1.1 "><p id="p50897247122442"><a name="p50897247122442"></a><a name="p50897247122442"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.198380161983803%" headers="mcps1.2.4.1.2 "><p id="p29036308122442"><a name="p29036308122442"></a><a name="p29036308122442"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.03349665033497%" headers="mcps1.2.4.1.3 "><p id="p3130725122442"><a name="p3130725122442"></a><a name="p3130725122442"></a>Specifies the EVS disk ID.</p>
</td>
</tr>
<tr id="row19927204775210"><td class="cellrowborder" valign="top" width="18.768123187681233%" headers="mcps1.2.4.1.1 "><p id="p9561643144814"><a name="p9561643144814"></a><a name="p9561643144814"></a>delete_on_termination</p>
</td>
<td class="cellrowborder" valign="top" width="16.198380161983803%" headers="mcps1.2.4.1.2 "><p id="p45694310485"><a name="p45694310485"></a><a name="p45694310485"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="65.03349665033497%" headers="mcps1.2.4.1.3 "><p id="p110774385110"><a name="p110774385110"></a><a name="p110774385110"></a>Specifies whether to delete additional disks when deleting the ECS.</p>
<p id="p856184314483"><a name="p856184314483"></a><a name="p856184314483"></a>By default, this parameter is set to <strong id="b6881839145614"><a name="b6881839145614"></a><a name="b6881839145614"></a>False</strong>.</p>
<p id="p18916195017524"><a name="p18916195017524"></a><a name="p18916195017524"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **security\_groups**  field description

<a name="table761507165933"></a>
<table><thead align="left"><tr id="row29958070165933"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="p1550320527296"><a name="p1550320527296"></a><a name="p1550320527296"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.2"><p id="p650355252917"><a name="p650355252917"></a><a name="p650355252917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.53999999999999%" id="mcps1.2.4.1.3"><p id="p14518145202914"><a name="p14518145202914"></a><a name="p14518145202914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29572324165933"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p46548026165933"><a name="p46548026165933"></a><a name="p46548026165933"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.2 "><p id="p12293798165933"><a name="p12293798165933"></a><a name="p12293798165933"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p52012230"><a name="p52012230"></a><a name="p52012230"></a>Specifies the security group name or UUID.</p>
</td>
</tr>
</tbody>
</table>

**Table  11** **fault**  field description

<a name="table1075312230549"></a>
<table><thead align="left"><tr id="row14754182345416"><th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.4.1.1"><p id="p15754172315410"><a name="p15754172315410"></a><a name="p15754172315410"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.97%" id="mcps1.2.4.1.2"><p id="p075415233543"><a name="p075415233543"></a><a name="p075415233543"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.47%" id="mcps1.2.4.1.3"><p id="p175422315410"><a name="p175422315410"></a><a name="p175422315410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row975452395413"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.4.1.1 "><p id="p27541723165410"><a name="p27541723165410"></a><a name="p27541723165410"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p97542231542"><a name="p97542231542"></a><a name="p97542231542"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p17559236540"><a name="p17559236540"></a><a name="p17559236540"></a>Specifies the error code.</p>
</td>
</tr>
<tr id="row11901115718561"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.4.1.1 "><p id="p590117577560"><a name="p590117577560"></a><a name="p590117577560"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p290105719562"><a name="p290105719562"></a><a name="p290105719562"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p1790110571561"><a name="p1790110571561"></a><a name="p1790110571561"></a>Specifies the time when an error occurred.</p>
</td>
</tr>
<tr id="row7674955155611"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.4.1.1 "><p id="p767412557568"><a name="p767412557568"></a><a name="p767412557568"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p2674185516566"><a name="p2674185516566"></a><a name="p2674185516566"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p1267414555563"><a name="p1267414555563"></a><a name="p1267414555563"></a>Describes an error.</p>
</td>
</tr>
<tr id="row2107195385616"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.4.1.1 "><p id="p12108145314564"><a name="p12108145314564"></a><a name="p12108145314564"></a>details</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p13108195335615"><a name="p13108195335615"></a><a name="p13108195335615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p610865345615"><a name="p610865345615"></a><a name="p610865345615"></a>Specifies details about an error. This parameter is optional and is returned only when it is not empty.</p>
</td>
</tr>
</tbody>
</table>

**Table  12** **image**  field description

<a name="table1080891111402"></a>
<table><thead align="left"><tr id="row5852711204015"><th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.1"><p id="p2098102533210"><a name="p2098102533210"></a><a name="p2098102533210"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="29.57%" id="mcps1.2.4.1.2"><p id="p1498192513327"><a name="p1498192513327"></a><a name="p1498192513327"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.5%" id="mcps1.2.4.1.3"><p id="p41141025113214"><a name="p41141025113214"></a><a name="p41141025113214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row149223117400"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p109391611134017"><a name="p109391611134017"></a><a name="p109391611134017"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="29.57%" headers="mcps1.2.4.1.2 "><p id="p7960411104018"><a name="p7960411104018"></a><a name="p7960411104018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.4.1.3 "><p id="p19699157104820"><a name="p19699157104820"></a><a name="p19699157104820"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row119931361483"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p99936664813"><a name="p99936664813"></a><a name="p99936664813"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="29.57%" headers="mcps1.2.4.1.2 "><p id="p5994196144811"><a name="p5994196144811"></a><a name="p5994196144811"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.4.1.3 "><p id="p1399417684820"><a name="p1399417684820"></a><a name="p1399417684820"></a>Specifies shortcut links for ECS images. For details, see <a href="#table16539321">Table 7</a>.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section12362164511549"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/detail
GET https://{endpoint}/v2.1/{project_id}/servers/detail
```

## Example Response<a name="section1630232142117"></a>

```
{
    "servers": [
        {
            "addresses": {
                "68269e6e-4a27-441b-8029-35373ad50bd9": [
                    {
                        "addr": "192.168.0.3", 
                        "version": 4
                    }
                ]
            }, 
            "created": "2012-09-07T16:56:37Z", 
            "flavor": {
                "id": "1", 
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/flavors/1", 
                        "rel": "bookmark"
                    }
                ]
            }, 
            "hostId": "16d193736a5cfdb60c697ca27ad071d6126fa13baeb670fc9d10645e", 
            "id": "05184ba3-00ba-4fbc-b7a2-03b62b884931", 
            "image": "", 
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/05184ba3-00ba-4fbc-b7a2-03b62b884931", 
                    "rel": "self"
                }, 
                {
                    "href": "http://openstack.example.com/openstack/servers/05184ba3-00ba-4fbc-b7a2-03b62b884931", 
                    "rel": "bookmark"
                }
            ], 
            "metadata": {},                         
            "name": "new-server-test", 
            "progress": 0, 
            "status": "ACTIVE", 
            "tenant_id": "openstack", 
            "updated": "2012-09-07T16:56:37Z", 
            "user_id": "fake"
        }
    ]
}
```

## Returned Values<a name="section25329374"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

