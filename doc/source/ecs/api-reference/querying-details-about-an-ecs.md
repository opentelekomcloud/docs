# Querying Details About an ECS<a name="EN-US_TOPIC_0020212690"></a>

## Function<a name="section11242227"></a>

This API is used to query details about an ECS based on the ECS ID.

## URI<a name="section34071180"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table32475667"></a>
<table><thead align="left"><tr id="row44937496"><th class="cellrowborder" valign="top" width="20.36%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.1%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1664874"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="p637140"><a name="p637140"></a><a name="p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.1%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row41565035"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="p11324657"><a name="p11324657"></a><a name="p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p44882061"><a name="p44882061"></a><a name="p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.1%" headers="mcps1.2.4.1.3 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section38205169"></a>

None

## Response<a name="section8302201"></a>

[Table 2](#table44736746)  describes the response parameters.

**Table  2**  Response parameters

<a name="table44736746"></a>
<table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="20.79%" id="mcps1.2.4.1.1"><p id="p63657004"><a name="p63657004"></a><a name="p63657004"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.2.4.1.2"><p id="p35147813"><a name="p35147813"></a><a name="p35147813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.38%" id="mcps1.2.4.1.3"><p id="p28400574"><a name="p28400574"></a><a name="p28400574"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.38%" headers="mcps1.2.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies ECS information. For details, see <a href="#table26210179">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **server**  field description

<a name="table26210179"></a>
<table><thead align="left"><tr id="row30559396"><th class="cellrowborder" valign="top" width="20.932093209320936%" id="mcps1.2.4.1.1"><p id="p59391972"><a name="p59391972"></a><a name="p59391972"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.79167916791679%" id="mcps1.2.4.1.2"><p id="p36664945"><a name="p36664945"></a><a name="p36664945"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.27622762276228%" id="mcps1.2.4.1.3"><p id="p17070607"><a name="p17070607"></a><a name="p17070607"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19417740"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p29333120"><a name="p29333120"></a><a name="p29333120"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p53487552"><a name="p53487552"></a><a name="p53487552"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p37524445"><a name="p37524445"></a><a name="p37524445"></a>Specifies the ECS name.</p>
</td>
</tr>
<tr id="row2175687"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p42012952"><a name="p42012952"></a><a name="p42012952"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p30874046"><a name="p30874046"></a><a name="p30874046"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p17769829"><a name="p17769829"></a><a name="p17769829"></a>Specifies an ECS uniquely.</p>
</td>
</tr>
<tr id="row25710733"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p2194613"><a name="p2194613"></a><a name="p2194613"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p37560342"><a name="p37560342"></a><a name="p37560342"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p22488863"><a name="p22488863"></a><a name="p22488863"></a>Specifies the ECS status.</p>
<p id="p17952198145121"><a name="p17952198145121"></a><a name="p17952198145121"></a>Options:</p>
<p id="p53652898145152"><a name="p53652898145152"></a><a name="p53652898145152"></a><strong id="b842352706232632"><a name="b842352706232632"></a><a name="b842352706232632"></a>ACTIVE</strong>, <strong id="b842352706232725"><a name="b842352706232725"></a><a name="b842352706232725"></a>BUILD</strong>, <strong id="b842352706232730"><a name="b842352706232730"></a><a name="b842352706232730"></a>DELETED</strong>, <strong id="b842352706232733"><a name="b842352706232733"></a><a name="b842352706232733"></a>ERROR</strong>, <strong id="b842352706232736"><a name="b842352706232736"></a><a name="b842352706232736"></a>HARD_REBOOT</strong>, <strong id="b842352706232740"><a name="b842352706232740"></a><a name="b842352706232740"></a>MIGRATING</strong>, <strong id="b842352706232747"><a name="b842352706232747"></a><a name="b842352706232747"></a>PAUSED</strong>, <strong id="b842352706232751"><a name="b842352706232751"></a><a name="b842352706232751"></a>REBOOT</strong>, <strong id="b842352706232754"><a name="b842352706232754"></a><a name="b842352706232754"></a>REBUILD</strong>, <strong id="b842352706232758"><a name="b842352706232758"></a><a name="b842352706232758"></a>RESIZE</strong>, <strong id="b84235270623282"><a name="b84235270623282"></a><a name="b84235270623282"></a>REVERT_RESIZE</strong>, <strong id="b84235270623285"><a name="b84235270623285"></a><a name="b84235270623285"></a>SHUTOFF</strong>, <strong id="b84235270623289"><a name="b84235270623289"></a><a name="b84235270623289"></a>SHELVED</strong>, <strong id="b842352706232812"><a name="b842352706232812"></a><a name="b842352706232812"></a>SHELVED_OFFLOADED</strong>, <strong id="b842352706232816"><a name="b842352706232816"></a><a name="b842352706232816"></a>SOFT_DELETED</strong>, <strong id="b842352706232819"><a name="b842352706232819"></a><a name="b842352706232819"></a>SUSPENDED</strong>, and <strong id="b842352706232721"><a name="b842352706232721"></a><a name="b842352706232721"></a>VERIFY_RESIZE</strong></p>
<p id="p5103192105518"><a name="p5103192105518"></a><a name="p5103192105518"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row1073183"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p19818984"><a name="p19818984"></a><a name="p19818984"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p42487544"><a name="p42487544"></a><a name="p42487544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p18939022"><a name="p18939022"></a><a name="p18939022"></a>Specifies the time when the ECS was created. The time is in the format of "2019-05-22T07:48:19Z".</p>
</td>
</tr>
<tr id="row36233478"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p49230602"><a name="p49230602"></a><a name="p49230602"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p7022941"><a name="p7022941"></a><a name="p7022941"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p31987323"><a name="p31987323"></a><a name="p31987323"></a>Specifies the time when the ECS was updated last time. The time is in the format of "2019-05-22T07:48:19Z".</p>
</td>
</tr>
<tr id="row19450451"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p31982717"><a name="p31982717"></a><a name="p31982717"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p56299846"><a name="p56299846"></a><a name="p56299846"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p39071968"><a name="p39071968"></a><a name="p39071968"></a>Specifies ECS flavors. For details, see <a href="#table29241163">Table 4</a>.</p>
</td>
</tr>
<tr id="row16103393"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p29306417"><a name="p29306417"></a><a name="p29306417"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p12507614"><a name="p12507614"></a><a name="p12507614"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p58354673"><a name="p58354673"></a><a name="p58354673"></a>Specifies the ECS image information. For an ECS created using an image, the image ID and link are returned.</p>
<p id="p5571104842212"><a name="p5571104842212"></a><a name="p5571104842212"></a>For details, see <a href="#table1080891111402">Table 5</a>.</p>
</td>
</tr>
<tr id="row55430014"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p60646173"><a name="p60646173"></a><a name="p60646173"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p11089280"><a name="p11089280"></a><a name="p11089280"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p25816468"><a name="p25816468"></a><a name="p25816468"></a>Specifies the ID of the tenant to which the ECS belongs. The parameter value is the same as the project ID specified by <strong id="b221521211599"><a name="b221521211599"></a><a name="b221521211599"></a>project_id</strong>.</p>
</td>
</tr>
<tr id="row289486817056"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p4349571017124"><a name="p4349571017124"></a><a name="p4349571017124"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p3349163017124"><a name="p3349163017124"></a><a name="p3349163017124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p2846749017124"><a name="p2846749017124"></a><a name="p2846749017124"></a>Specifies the SSH key name.</p>
</td>
</tr>
<tr id="row31021623"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p29723549"><a name="p29723549"></a><a name="p29723549"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p64958874"><a name="p64958874"></a><a name="p64958874"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p27177474"><a name="p27177474"></a><a name="p27177474"></a>Specifies the ID of the user to which an ECS belongs.</p>
</td>
</tr>
<tr id="row43270676"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p15263883"><a name="p15263883"></a><a name="p15263883"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p19916823"><a name="p19916823"></a><a name="p19916823"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p23849822"><a name="p23849822"></a><a name="p23849822"></a>Specifies the ECS metadata.</p>
</td>
</tr>
<tr id="row13321813"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p5325067"><a name="p5325067"></a><a name="p5325067"></a>hostId</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p41156139"><a name="p41156139"></a><a name="p41156139"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p45312999"><a name="p45312999"></a><a name="p45312999"></a>Specifies the host ID of the ECS.</p>
</td>
</tr>
<tr id="row5163807"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p15615252"><a name="p15615252"></a><a name="p15615252"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p43546944"><a name="p43546944"></a><a name="p43546944"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p3229562"><a name="p3229562"></a><a name="p3229562"></a>Specifies the network addresses of an ECS. For details, see <a href="#table36337966">Table 6</a>.</p>
</td>
</tr>
<tr id="row2817586217053"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p2741526417147"><a name="p2741526417147"></a><a name="p2741526417147"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p604393417147"><a name="p604393417147"></a><a name="p604393417147"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p4395185217147"><a name="p4395185217147"></a><a name="p4395185217147"></a>Specifies the security groups to which the ECS belongs. For details, see <a href="#table2053207517233">Table 10</a>.</p>
</td>
</tr>
<tr id="row29066061"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p5540732"><a name="p5540732"></a><a name="p5540732"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p46852469"><a name="p46852469"></a><a name="p46852469"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p64147070"><a name="p64147070"></a><a name="p64147070"></a>Specifies shortcut links for ECS markers. For details, see <a href="#table35230296">Table 7</a>.</p>
</td>
</tr>
<tr id="row5544204718389"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p749372082418"><a name="p749372082418"></a><a name="p749372082418"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p14493420142420"><a name="p14493420142420"></a><a name="p14493420142420"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p1620274611333"><a name="p1620274611333"></a><a name="p1620274611333"></a>Specifies ECS tags.</p>
<p id="p1149310203247"><a name="p1149310203247"></a><a name="p1149310203247"></a>In microversion 2.26, if the microversion is not used for query, the response does not contain the <strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>tags</strong> field.</p>
<div class="p" id="p7300949059"><a name="p7300949059"></a><a name="p7300949059"></a>Tag functions have been upgraded on the public cloud. After the upgrade, the tag values returned by the system comply with the following rules:<a name="en-us_topic_0020212689_ul871515496611"></a><a name="en-us_topic_0020212689_ul871515496611"></a><ul id="en-us_topic_0020212689_ul871515496611"><li>The key and value of a tag are connected using an equal sign (=), for example, key=value.</li><li>If the value is empty, only the key is returned.</li></ul>
</div>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For more details about upgraded tag functions, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
</td>
</tr>
<tr id="row65689897121119"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p19281432121119"><a name="p19281432121119"></a><a name="p19281432121119"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p18292184121119"><a name="p18292184121119"></a><a name="p18292184121119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p5271953121119"><a name="p5271953121119"></a><a name="p5271953121119"></a>Specifies the disk configuration mode. This is an extended attribute. This field is valid for the ECS started using an image.</p>
<p id="p978417418171"><a name="p978417418171"></a><a name="p978417418171"></a>Options:</p>
<a name="ul5356518715165"></a><a name="ul5356518715165"></a><ul id="ul5356518715165"><li><strong id="b5814747015165"><a name="b5814747015165"></a><a name="b5814747015165"></a>AUTO</strong>: This API uses a single partition to build an ECS with the target disk size. The API automatically adjusts the file system to adapt to the entire partition.</li></ul>
<a name="ul42058244151611"></a><a name="ul42058244151611"></a><ul id="ul42058244151611"><li><strong id="b64325461151611"><a name="b64325461151611"></a><a name="b64325461151611"></a>MANUAL</strong>: This API uses the partitioning scheme in the source image and the file system to build the ECS. If the target disk size is large, the API does not partition the remaining disk space.</li></ul>
</td>
</tr>
<tr id="row26985914121125"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p38375386121125"><a name="p38375386121125"></a><a name="p38375386121125"></a>OS-EXT-AZ:availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p21398534121125"><a name="p21398534121125"></a><a name="p21398534121125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p55559719121125"><a name="p55559719121125"></a><a name="p55559719121125"></a>Specifies the AZ ID. This is an extended attribute.</p>
</td>
</tr>
<tr id="row8927030121127"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p52000861121127"><a name="p52000861121127"></a><a name="p52000861121127"></a>OS-EXT-SRV-ATTR:host</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p51320175121127"><a name="p51320175121127"></a><a name="p51320175121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p63293526121127"><a name="p63293526121127"></a><a name="p63293526121127"></a>Specifies the name of the host on which the ECS is deployed. This is an extended attribute.</p>
</td>
</tr>
<tr id="row15809615121127"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p5510414121127"><a name="p5510414121127"></a><a name="p5510414121127"></a>OS-EXT-SRV-ATTR:hypervisor_hostname</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p43690378121127"><a name="p43690378121127"></a><a name="p43690378121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p49259690121127"><a name="p49259690121127"></a><a name="p49259690121127"></a>Specifies the hostname of the hypervisor. This is an extended attribute.</p>
</td>
</tr>
<tr id="row20844277121128"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p10664873121128"><a name="p10664873121128"></a><a name="p10664873121128"></a>OS-EXT-SRV-ATTR:instance_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p58548414121128"><a name="p58548414121128"></a><a name="p58548414121128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p44801116121128"><a name="p44801116121128"></a><a name="p44801116121128"></a>Specifies the ECS alias. This is an extended attribute.</p>
</td>
</tr>
<tr id="row66679123121128"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p32299911121128"><a name="p32299911121128"></a><a name="p32299911121128"></a>OS-EXT-STS:power_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p66155999121128"><a name="p66155999121128"></a><a name="p66155999121128"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p57035716121128"><a name="p57035716121128"></a><a name="p57035716121128"></a>Specifies the ECS power status. This is an extended attribute.</p>
<p id="p2689123602310"><a name="p2689123602310"></a><a name="p2689123602310"></a>Options: 0, 1, 2, 3, and 4</p>
<a name="ul934453312193"></a><a name="ul934453312193"></a><ul id="ul934453312193"><li><strong id="b842352706204759"><a name="b842352706204759"></a><a name="b842352706204759"></a>0</strong>: pending</li><li><strong id="b84235270620489"><a name="b84235270620489"></a><a name="b84235270620489"></a>1</strong>: running</li><li><strong id="b842352706204817"><a name="b842352706204817"></a><a name="b842352706204817"></a>2</strong>: paused</li><li><strong id="b842352706204825"><a name="b842352706204825"></a><a name="b842352706204825"></a>3</strong>: shutdown</li><li><strong id="b842352706204833"><a name="b842352706204833"></a><a name="b842352706204833"></a>4</strong>: crashed</li></ul>
</td>
</tr>
<tr id="row19260742121226"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p16616235121226"><a name="p16616235121226"></a><a name="p16616235121226"></a>OS-EXT-STS:task_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p3737772121226"><a name="p3737772121226"></a><a name="p3737772121226"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p34324147121226"><a name="p34324147121226"></a><a name="p34324147121226"></a>Specifies the ECS task status. This is an extended attribute.</p>
<p id="p13922047162612"><a name="p13922047162612"></a><a name="p13922047162612"></a>For details about options, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row11298969121227"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p42801278121227"><a name="p42801278121227"></a><a name="p42801278121227"></a>OS-EXT-STS:vm_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p44351508121227"><a name="p44351508121227"></a><a name="p44351508121227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p9331154012376"><a name="p9331154012376"></a><a name="p9331154012376"></a>Specifies the ECS status. This is an extended attribute.</p>
<p id="p35702402121227"><a name="p35702402121227"></a><a name="p35702402121227"></a>Options:</p>
<p id="p15276846381"><a name="p15276846381"></a><a name="p15276846381"></a><strong id="b842352706202631"><a name="b842352706202631"></a><a name="b842352706202631"></a>ACTIVE</strong>, <strong id="b842352706202636"><a name="b842352706202636"></a><a name="b842352706202636"></a>BUILDING</strong>, <strong id="b842352706202641"><a name="b842352706202641"></a><a name="b842352706202641"></a>STOPPED</strong>, <strong id="b842352706202645"><a name="b842352706202645"></a><a name="b842352706202645"></a>RESIZED</strong>, <strong id="b842352706202649"><a name="b842352706202649"></a><a name="b842352706202649"></a>PAUSED</strong>, <strong id="b842352706202654"><a name="b842352706202654"></a><a name="b842352706202654"></a>SUSPENDED</strong>, <strong id="b842352706202658"><a name="b842352706202658"></a><a name="b842352706202658"></a>RESCUED</strong>, <strong id="b84235270620273"><a name="b84235270620273"></a><a name="b84235270620273"></a>ERROR</strong>, <strong id="b84235270620278"><a name="b84235270620278"></a><a name="b84235270620278"></a>DELETED</strong>, <strong id="b842352706202716"><a name="b842352706202716"></a><a name="b842352706202716"></a>SOFT_DELETED</strong>, <strong id="b842352706202721"><a name="b842352706202721"></a><a name="b842352706202721"></a>SHELVED</strong>, <strong id="b842352706202726"><a name="b842352706202726"></a><a name="b842352706202726"></a>SHELVED_OFFLOADED</strong></p>
<p id="p69818711559"><a name="p69818711559"></a><a name="p69818711559"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row59870257121227"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p17652642121227"><a name="p17652642121227"></a><a name="p17652642121227"></a>OS-SRV-USG:launched_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p20577863121227"><a name="p20577863121227"></a><a name="p20577863121227"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p56194184121227"><a name="p56194184121227"></a><a name="p56194184121227"></a>Specifies the time when the ECS was started. This is an extended attribute. The time is in the format of "2019-05-22T07:48:19.000000".</p>
</td>
</tr>
<tr id="row58808453121228"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p65864237121228"><a name="p65864237121228"></a><a name="p65864237121228"></a>OS-SRV-USG:terminated_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p33402957121228"><a name="p33402957121228"></a><a name="p33402957121228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p21285006121228"><a name="p21285006121228"></a><a name="p21285006121228"></a>Specifies the time when the ECS was deleted. This is an extended attribute. The time is in the format of "2019-05-22T07:48:19.000000".</p>
</td>
</tr>
<tr id="row22845263122110"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p29403502122828"><a name="p29403502122828"></a><a name="p29403502122828"></a>os-extended-volumes:volumes_attached</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p32873451122828"><a name="p32873451122828"></a><a name="p32873451122828"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p6881526122828"><a name="p6881526122828"></a><a name="p6881526122828"></a>Specifies the EVS disks attached to an ECS. For details, see <a href="#table10024873122234">Table 9</a>.</p>
</td>
</tr>
<tr id="row161046711504"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p43095310"><a name="en-us_topic_0057972887_p43095310"></a><a name="en-us_topic_0057972887_p43095310"></a>fault</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p1059226"><a name="en-us_topic_0057972887_p1059226"></a><a name="en-us_topic_0057972887_p1059226"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p37371779"><a name="en-us_topic_0057972887_p37371779"></a><a name="en-us_topic_0057972887_p37371779"></a>Specifies the ECS fault.</p>
<p id="p14777766535"><a name="p14777766535"></a><a name="p14777766535"></a>This parameter is optional. It is returned when an error occurs on an ECS.</p>
<p id="p1688015424530"><a name="p1688015424530"></a><a name="p1688015424530"></a>For details, see <a href="#table1075312230549">Table 11</a>.</p>
</td>
</tr>
<tr id="row107959146481"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p57463526"><a name="en-us_topic_0057972887_p57463526"></a><a name="en-us_topic_0057972887_p57463526"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p24034004"><a name="en-us_topic_0057972887_p24034004"></a><a name="en-us_topic_0057972887_p24034004"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p48379233"><a name="en-us_topic_0057972887_p48379233"></a><a name="en-us_topic_0057972887_p48379233"></a>Specifies the description of the ECS.</p>
<p id="p28201545155518"><a name="p28201545155518"></a><a name="p28201545155518"></a>This field is supported in microversions later than 2.19.</p>
</td>
</tr>
<tr id="row456252015488"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p58332432"><a name="en-us_topic_0057972887_p58332432"></a><a name="en-us_topic_0057972887_p58332432"></a>host_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p27306569"><a name="en-us_topic_0057972887_p27306569"></a><a name="en-us_topic_0057972887_p27306569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p44841923"><a name="en-us_topic_0057972887_p44841923"></a><a name="en-us_topic_0057972887_p44841923"></a>Specifies the nova-compute status.</p>
<a name="en-us_topic_0057972887_ul924126"></a><a name="en-us_topic_0057972887_ul924126"></a><ul id="en-us_topic_0057972887_ul924126"><li><strong id="b1713315404590"><a name="b1713315404590"></a><a name="b1713315404590"></a>UP</strong>: The nova-compute status is normal.</li><li><strong id="b169254310593"><a name="b169254310593"></a><a name="b169254310593"></a>UNKNOWN</strong>: The nova-compute status is unknown.</li><li><strong id="b459919447590"><a name="b459919447590"></a><a name="b459919447590"></a>DOWN</strong>: the nova-compute status is abnormal.</li><li><strong id="b654321717572"><a name="b654321717572"></a><a name="b654321717572"></a>MAINTENANCE</strong>: The nova-compute is in maintenance state.</li><li><strong id="b1297948185920"><a name="b1297948185920"></a><a name="b1297948185920"></a>Null</strong>: The ECS does not have host information.</li></ul>
<p id="p9178121814561"><a name="p9178121814561"></a><a name="p9178121814561"></a>This field is supported in microversions later than 2.16.</p>
</td>
</tr>
<tr id="row1043718233485"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p7131169"><a name="en-us_topic_0057972887_p7131169"></a><a name="en-us_topic_0057972887_p7131169"></a>OS-EXT-SRV-ATTR:hostname</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p40753854"><a name="en-us_topic_0057972887_p40753854"></a><a name="en-us_topic_0057972887_p40753854"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p24324288"><a name="en-us_topic_0057972887_p24324288"></a><a name="en-us_topic_0057972887_p24324288"></a>Specifies the ECS hostname.</p>
<p id="p3479627194317"><a name="p3479627194317"></a><a name="p3479627194317"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row1843752316486"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p6779396"><a name="en-us_topic_0057972887_p6779396"></a><a name="en-us_topic_0057972887_p6779396"></a>OS-EXT-SRV-ATTR:reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p12260243"><a name="en-us_topic_0057972887_p12260243"></a><a name="en-us_topic_0057972887_p12260243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p43041107"><a name="en-us_topic_0057972887_p43041107"></a><a name="en-us_topic_0057972887_p43041107"></a>Specifies reserved ECS IDs if ECSs are created in a batch.</p>
<p id="p18137583436"><a name="p18137583436"></a><a name="p18137583436"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row12424182718489"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p54550808"><a name="en-us_topic_0057972887_p54550808"></a><a name="en-us_topic_0057972887_p54550808"></a>OS-EXT-SRV-ATTR:launch_index</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p56539341"><a name="en-us_topic_0057972887_p56539341"></a><a name="en-us_topic_0057972887_p56539341"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p43927036"><a name="en-us_topic_0057972887_p43927036"></a><a name="en-us_topic_0057972887_p43927036"></a>Specifies the sequence in which ECSs start if the ECSs are created in a batch.</p>
<p id="p12601191124414"><a name="p12601191124414"></a><a name="p12601191124414"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row14424927204815"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p22853796"><a name="en-us_topic_0057972887_p22853796"></a><a name="en-us_topic_0057972887_p22853796"></a>OS-EXT-SRV-ATTR:kernel_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p39218184"><a name="en-us_topic_0057972887_p39218184"></a><a name="en-us_topic_0057972887_p39218184"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p15126299"><a name="en-us_topic_0057972887_p15126299"></a><a name="en-us_topic_0057972887_p15126299"></a>Specifies the UUID of the kernel image if an AMI image is used. In other scenarios, leave this parameter blank.</p>
<p id="p196273244466"><a name="p196273244466"></a><a name="p196273244466"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row1842472711482"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p40968939"><a name="en-us_topic_0057972887_p40968939"></a><a name="en-us_topic_0057972887_p40968939"></a>OS-EXT-SRV-ATTR:ramdisk_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p30149753"><a name="en-us_topic_0057972887_p30149753"></a><a name="en-us_topic_0057972887_p30149753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p11808112215493"><a name="p11808112215493"></a><a name="p11808112215493"></a>Specifies the UUID of the Ramdisk image if an AMI image is used. In other scenarios, leave this parameter blank.</p>
<p id="en-us_topic_0057972887_p42710723"><a name="en-us_topic_0057972887_p42710723"></a><a name="en-us_topic_0057972887_p42710723"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row5425122710481"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p7284856"><a name="en-us_topic_0057972887_p7284856"></a><a name="en-us_topic_0057972887_p7284856"></a>OS-EXT-SRV-ATTR:root_device_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p53202458"><a name="en-us_topic_0057972887_p53202458"></a><a name="en-us_topic_0057972887_p53202458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p28127439"><a name="en-us_topic_0057972887_p28127439"></a><a name="en-us_topic_0057972887_p28127439"></a>Specifies the device name of the ECS system disk.</p>
<p id="p11804132124618"><a name="p11804132124618"></a><a name="p11804132124618"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row11445163194818"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p61864358"><a name="en-us_topic_0057972887_p61864358"></a><a name="en-us_topic_0057972887_p61864358"></a>OS-EXT-SRV-ATTR:user_data</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p44957139"><a name="en-us_topic_0057972887_p44957139"></a><a name="en-us_topic_0057972887_p44957139"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p20334069"><a name="en-us_topic_0057972887_p20334069"></a><a name="en-us_topic_0057972887_p20334069"></a>Specifies the user data configured during ECS creation.</p>
<p id="p1815314834617"><a name="p1815314834617"></a><a name="p1815314834617"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
<tr id="row8537324827"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p1253710242210"><a name="p1253710242210"></a><a name="p1253710242210"></a>locked</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p1653720241521"><a name="p1653720241521"></a><a name="p1653720241521"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p18537624422"><a name="p18537624422"></a><a name="p18537624422"></a>Specifies the ECS lock status, which is <strong id="b842352706142719"><a name="b842352706142719"></a><a name="b842352706142719"></a>True</strong> when the ECS is locked and <strong id="b842352706142722"><a name="b842352706142722"></a><a name="b842352706142722"></a>False</strong> when the ECS is unlocked.</p>
<p id="p13993454402"><a name="p13993454402"></a><a name="p13993454402"></a>This field is supported in microversions later than 2.9.</p>
</td>
</tr>
<tr id="row4211297017037"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p4431131717046"><a name="p4431131717046"></a><a name="p4431131717046"></a>accessIPv4</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p3244692017046"><a name="p3244692017046"></a><a name="p3244692017046"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p1095487217046"><a name="p1095487217046"></a><a name="p1095487217046"></a>Reserved</p>
</td>
</tr>
<tr id="row5854487717038"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p14705517046"><a name="p14705517046"></a><a name="p14705517046"></a>accessIPv6</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p1191150917046"><a name="p1191150917046"></a><a name="p1191150917046"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p2530817917046"><a name="p2530817917046"></a><a name="p2530817917046"></a>Reserved</p>
</td>
</tr>
<tr id="row3362467117038"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p6183447417046"><a name="p6183447417046"></a><a name="p6183447417046"></a>config_drive</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p4253646017046"><a name="p4253646017046"></a><a name="p4253646017046"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p2290125117046"><a name="p2290125117046"></a><a name="p2290125117046"></a>Reserved</p>
</td>
</tr>
<tr id="row6528865417041"><td class="cellrowborder" valign="top" width="20.932093209320936%" headers="mcps1.2.4.1.1 "><p id="p6381535217046"><a name="p6381535217046"></a><a name="p6381535217046"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="16.79167916791679%" headers="mcps1.2.4.1.2 "><p id="p166104217046"><a name="p166104217046"></a><a name="p166104217046"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.27622762276228%" headers="mcps1.2.4.1.3 "><p id="p32670417046"><a name="p32670417046"></a><a name="p32670417046"></a>Reserved</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavor**  field description

<a name="table29241163"></a>
<table><thead align="left"><tr id="row10599309"><th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.4.1.1"><p id="p08351422143212"><a name="p08351422143212"></a><a name="p08351422143212"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.4.1.2"><p id="p158351922123214"><a name="p158351922123214"></a><a name="p158351922123214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.6%" id="mcps1.2.4.1.3"><p id="p8835192210324"><a name="p8835192210324"></a><a name="p8835192210324"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1202807"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p30318520"><a name="p30318520"></a><a name="p30318520"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p9142577"><a name="p9142577"></a><a name="p9142577"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p2351288"><a name="p2351288"></a><a name="p2351288"></a>Specifies the ECS ID.</p>
<p id="p5578010620"><a name="p5578010620"></a><a name="p5578010620"></a>This field is not supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row21161599"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p36367968"><a name="p36367968"></a><a name="p36367968"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p38229923"><a name="p38229923"></a><a name="p38229923"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p19435912"><a name="p19435912"></a><a name="p19435912"></a>Specifies the shortcut links of the ECS type markers.</p>
<p id="p580410263265"><a name="p580410263265"></a><a name="p580410263265"></a>For details, see <a href="#table35230296">Table 7</a>.</p>
<p id="p1923951718615"><a name="p1923951718615"></a><a name="p1923951718615"></a>This field is not supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row11601145721619"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p18647653114019"><a name="p18647653114019"></a><a name="p18647653114019"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p5647153194013"><a name="p5647153194013"></a><a name="p5647153194013"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p594712133917"><a name="p594712133917"></a><a name="p594712133917"></a>Specifies the number of vCPUs in the ECS flavor.</p>
<p id="p7411737161018"><a name="p7411737161018"></a><a name="p7411737161018"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row146331125171"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p460015587400"><a name="p460015587400"></a><a name="p460015587400"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p1760065884017"><a name="p1760065884017"></a><a name="p1760065884017"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p1760065884013"><a name="p1760065884013"></a><a name="p1760065884013"></a>Specifies the memory size (MB) in the ECS flavor.</p>
<p id="p0979145841010"><a name="p0979145841010"></a><a name="p0979145841010"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row663372141712"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p338192124118"><a name="p338192124118"></a><a name="p338192124118"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p143817234115"><a name="p143817234115"></a><a name="p143817234115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p1381422419"><a name="p1381422419"></a><a name="p1381422419"></a>Specifies the system disk size in the ECS flavor. The value <strong id="b26095715528"><a name="b26095715528"></a><a name="b26095715528"></a>0</strong> indicates that the disk size is not limited.</p>
<p id="p155897161110"><a name="p155897161110"></a><a name="p155897161110"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row14477413101710"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p175990512419"><a name="p175990512419"></a><a name="p175990512419"></a>ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p55996517419"><a name="p55996517419"></a><a name="p55996517419"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p1059914514118"><a name="p1059914514118"></a><a name="p1059914514118"></a>Reserved</p>
<p id="p138227319114"><a name="p138227319114"></a><a name="p138227319114"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row184771134175"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p66306183429"><a name="p66306183429"></a><a name="p66306183429"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p863019183421"><a name="p863019183421"></a><a name="p863019183421"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p15630121813429"><a name="p15630121813429"></a><a name="p15630121813429"></a>Reserved</p>
<p id="p568210631113"><a name="p568210631113"></a><a name="p568210631113"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row154771813181718"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p1936516339428"><a name="p1936516339428"></a><a name="p1936516339428"></a>original_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p163651333144219"><a name="p163651333144219"></a><a name="p163651333144219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p2365113374215"><a name="p2365113374215"></a><a name="p2365113374215"></a>Specifies the name of the ECS flavor.</p>
<p id="p47911894115"><a name="p47911894115"></a><a name="p47911894115"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
<tr id="row62747810179"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.4.1.1 "><p id="p136311336194210"><a name="p136311336194210"></a><a name="p136311336194210"></a>extra_specs</p>
</td>
<td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.2 "><p id="p563116366423"><a name="p563116366423"></a><a name="p563116366423"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.6%" headers="mcps1.2.4.1.3 "><p id="p10674132212106"><a name="p10674132212106"></a><a name="p10674132212106"></a>Indicates an extended flavor field. For details, see <a href="data-structure-for-query-details-about-specifications.md">os_extra_specs (flavor) Field Description</a>.</p>
<p id="p68221938111119"><a name="p68221938111119"></a><a name="p68221938111119"></a>This field is supported in microversions later than 2.47.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **image**  field description

<a name="table1080891111402"></a>
<table><thead align="left"><tr id="row5852711204015"><th class="cellrowborder" valign="top" width="20.18%" id="mcps1.2.4.1.1"><p id="p2098102533210"><a name="p2098102533210"></a><a name="p2098102533210"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p1498192513327"><a name="p1498192513327"></a><a name="p1498192513327"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.660000000000004%" id="mcps1.2.4.1.3"><p id="p41141025113214"><a name="p41141025113214"></a><a name="p41141025113214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row149223117400"><td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.2.4.1.1 "><p id="p109391611134017"><a name="p109391611134017"></a><a name="p109391611134017"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p7960411104018"><a name="p7960411104018"></a><a name="p7960411104018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.660000000000004%" headers="mcps1.2.4.1.3 "><p id="p19699157104820"><a name="p19699157104820"></a><a name="p19699157104820"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row119931361483"><td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.2.4.1.1 "><p id="p99936664813"><a name="p99936664813"></a><a name="p99936664813"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p5994196144811"><a name="p5994196144811"></a><a name="p5994196144811"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.660000000000004%" headers="mcps1.2.4.1.3 "><p id="p1399417684820"><a name="p1399417684820"></a><a name="p1399417684820"></a>Specifies shortcut links for ECS images. For details, see <a href="#table35230296">Table 7</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **addresses**  field description

<a name="table36337966"></a>
<table><thead align="left"><tr id="row66136932"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p8152204019329"><a name="p8152204019329"></a><a name="p8152204019329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p1515294016327"><a name="p1515294016327"></a><a name="p1515294016327"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.660000000000004%" id="mcps1.2.4.1.3"><p id="p1515284010326"><a name="p1515284010326"></a><a name="p1515284010326"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66161841"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p2057412833316"><a name="p2057412833316"></a><a name="p2057412833316"></a>Name of the network where the ECS accesses</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p4439518115623"><a name="p4439518115623"></a><a name="p4439518115623"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.660000000000004%" headers="mcps1.2.4.1.3 "><p id="p1534202613277"><a name="p1534202613277"></a><a name="p1534202613277"></a>Specifies the network information of the ECS.</p>
<a name="ul1556425242710"></a><a name="ul1556425242710"></a><ul id="ul1556425242710"><li><strong id="b842352706214237"><a name="b842352706214237"></a><a name="b842352706214237"></a>key</strong> indicates the network name, for example, <strong id="b842352706214248"><a name="b842352706214248"></a><a name="b842352706214248"></a>demo_net</strong>.</li><li><strong id="b84235270621435"><a name="b84235270621435"></a><a name="b84235270621435"></a>value</strong> indicates the detailed network information.</li></ul>
<p id="p8364776268"><a name="p8364776268"></a><a name="p8364776268"></a>For details, see <a href="#table1972725101724">Table 8</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **links**  field description

<a name="table35230296"></a>
<table><thead align="left"><tr id="row22264835"><th class="cellrowborder" valign="top" width="19.8%" id="mcps1.2.4.1.1"><p id="p112383444325"><a name="p112383444325"></a><a name="p112383444325"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p14238944103219"><a name="p14238944103219"></a><a name="p14238944103219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.660000000000004%" id="mcps1.2.4.1.3"><p id="p1023811445320"><a name="p1023811445320"></a><a name="p1023811445320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35493489"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.4.1.1 "><p id="p56400342"><a name="p56400342"></a><a name="p56400342"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p4372186"><a name="p4372186"></a><a name="p4372186"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.660000000000004%" headers="mcps1.2.4.1.3 "><p id="p18602825"><a name="p18602825"></a><a name="p18602825"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row33207705"><td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.2.4.1.1 "><p id="p5469547"><a name="p5469547"></a><a name="p5469547"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p49569014"><a name="p49569014"></a><a name="p49569014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.660000000000004%" headers="mcps1.2.4.1.3 "><p id="p55667198"><a name="p55667198"></a><a name="p55667198"></a>Provides the corresponding shortcut link.</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Data structure of the network which an ECS accesses

<a name="table1972725101724"></a>
<table><thead align="left"><tr id="row12506860101724"><th class="cellrowborder" valign="top" width="19.759999999999998%" id="mcps1.2.4.1.1"><p id="p1370316476325"><a name="p1370316476325"></a><a name="p1370316476325"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.7%" id="mcps1.2.4.1.2"><p id="p370334723212"><a name="p370334723212"></a><a name="p370334723212"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.53999999999999%" id="mcps1.2.4.1.3"><p id="p0703347163220"><a name="p0703347163220"></a><a name="p0703347163220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12641738101724"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p65254077101750"><a name="p65254077101750"></a><a name="p65254077101750"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p51088888101750"><a name="p51088888101750"></a><a name="p51088888101750"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p44559239101750"><a name="p44559239101750"></a><a name="p44559239101750"></a>Specifies the IP address.</p>
</td>
</tr>
<tr id="row21763795101724"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p2995307101750"><a name="p2995307101750"></a><a name="p2995307101750"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p41293276101750"><a name="p41293276101750"></a><a name="p41293276101750"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p32665092151024"><a name="p32665092151024"></a><a name="p32665092151024"></a>Specifies the type of an IP address. The value of this parameter can be <strong id="b84235270614154"><a name="b84235270614154"></a><a name="b84235270614154"></a>4</strong> or <strong id="b842352706141510"><a name="b842352706141510"></a><a name="b842352706141510"></a>6</strong>.</p>
<a name="ul25550372151024"></a><a name="ul25550372151024"></a><ul id="ul25550372151024"><li><strong id="b84235270614151"><a name="b84235270614151"></a><a name="b84235270614151"></a>4</strong>: The type of the IP address is IPv4.</li><li><strong id="b842352706141518"><a name="b842352706141518"></a><a name="b842352706141518"></a>6</strong>: The type of the IP address is IPv6.</li></ul>
</td>
</tr>
<tr id="row5677238512196"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p3516049812196"><a name="p3516049812196"></a><a name="p3516049812196"></a>OS-EXT-IPS-MAC:mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p2942812812196"><a name="p2942812812196"></a><a name="p2942812812196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p3486817812196"><a name="p3486817812196"></a><a name="p3486817812196"></a>Specifies the MAC address. This is an extended attribute.</p>
</td>
</tr>
<tr id="row211654712196"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p3722265012196"><a name="p3722265012196"></a><a name="p3722265012196"></a>OS-EXT-IPS:type</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p6224463612196"><a name="p6224463612196"></a><a name="p6224463612196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p865077112196"><a name="p865077112196"></a><a name="p865077112196"></a>Specifies the IP address assignment mode. This is an extended attribute.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **os-extended-volumes:volumes\_attached**  field description

<a name="table10024873122234"></a>
<table><thead align="left"><tr id="row57520332122234"><th class="cellrowborder" valign="top" width="19.759999999999998%" id="mcps1.2.4.1.1"><p id="p141714507323"><a name="p141714507323"></a><a name="p141714507323"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.7%" id="mcps1.2.4.1.2"><p id="p1433115012326"><a name="p1433115012326"></a><a name="p1433115012326"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.53999999999999%" id="mcps1.2.4.1.3"><p id="p1043345063214"><a name="p1043345063214"></a><a name="p1043345063214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36412167122234"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p63704378122234"><a name="p63704378122234"></a><a name="p63704378122234"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p59781031122234"><a name="p59781031122234"></a><a name="p59781031122234"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p10425332122234"><a name="p10425332122234"></a><a name="p10425332122234"></a>Specifies the EVS disk ID.</p>
</td>
</tr>
<tr id="row156174394818"><td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.4.1.1 "><p id="p9561643144814"><a name="p9561643144814"></a><a name="p9561643144814"></a>delete_on_termination</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.2 "><p id="p45694310485"><a name="p45694310485"></a><a name="p45694310485"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="62.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p110774385110"><a name="p110774385110"></a><a name="p110774385110"></a>Specifies whether to delete additional disks when deleting the ECS.</p>
<p id="p856184314483"><a name="p856184314483"></a><a name="p856184314483"></a>By default, this parameter is set to <strong id="b197481074219"><a name="b197481074219"></a><a name="b197481074219"></a>False</strong>.</p>
<p id="p1169334275311"><a name="p1169334275311"></a><a name="p1169334275311"></a>This field is supported in microversions later than 2.3.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **security\_groups**  field description

<a name="table2053207517233"></a>
<table><thead align="left"><tr id="row2114422117233"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p894305273218"><a name="p894305273218"></a><a name="p894305273218"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p139591452193215"><a name="p139591452193215"></a><a name="p139591452193215"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.97999999999999%" id="mcps1.2.4.1.3"><p id="p695912521323"><a name="p695912521323"></a><a name="p695912521323"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5784450417233"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p5489327917233"><a name="p5489327917233"></a><a name="p5489327917233"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p1717057717233"><a name="p1717057717233"></a><a name="p1717057717233"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p52012230"><a name="p52012230"></a><a name="p52012230"></a>Specifies the security group name or UUID.</p>
</td>
</tr>
</tbody>
</table>

**Table  11** **fault**  field description

<a name="table1075312230549"></a>
<table><thead align="left"><tr id="row14754182345416"><th class="cellrowborder" valign="top" width="16.68%" id="mcps1.2.4.1.1"><p id="p15754172315410"><a name="p15754172315410"></a><a name="p15754172315410"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.4.1.2"><p id="p075415233543"><a name="p075415233543"></a><a name="p075415233543"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.91%" id="mcps1.2.4.1.3"><p id="p175422315410"><a name="p175422315410"></a><a name="p175422315410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row975452395413"><td class="cellrowborder" valign="top" width="16.68%" headers="mcps1.2.4.1.1 "><p id="p27541723165410"><a name="p27541723165410"></a><a name="p27541723165410"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.2 "><p id="p97542231542"><a name="p97542231542"></a><a name="p97542231542"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.91%" headers="mcps1.2.4.1.3 "><p id="p17559236540"><a name="p17559236540"></a><a name="p17559236540"></a>Specifies the error code.</p>
</td>
</tr>
<tr id="row11901115718561"><td class="cellrowborder" valign="top" width="16.68%" headers="mcps1.2.4.1.1 "><p id="p590117577560"><a name="p590117577560"></a><a name="p590117577560"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.2 "><p id="p290105719562"><a name="p290105719562"></a><a name="p290105719562"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.91%" headers="mcps1.2.4.1.3 "><p id="p1790110571561"><a name="p1790110571561"></a><a name="p1790110571561"></a>Specifies the time when an error occurred.</p>
</td>
</tr>
<tr id="row7674955155611"><td class="cellrowborder" valign="top" width="16.68%" headers="mcps1.2.4.1.1 "><p id="p767412557568"><a name="p767412557568"></a><a name="p767412557568"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.2 "><p id="p2674185516566"><a name="p2674185516566"></a><a name="p2674185516566"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.91%" headers="mcps1.2.4.1.3 "><p id="p1267414555563"><a name="p1267414555563"></a><a name="p1267414555563"></a>Describes an error.</p>
</td>
</tr>
<tr id="row2107195385616"><td class="cellrowborder" valign="top" width="16.68%" headers="mcps1.2.4.1.1 "><p id="p12108145314564"><a name="p12108145314564"></a><a name="p12108145314564"></a>details</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.2 "><p id="p13108195335615"><a name="p13108195335615"></a><a name="p13108195335615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.91%" headers="mcps1.2.4.1.3 "><p id="p610865345615"><a name="p610865345615"></a><a name="p610865345615"></a>Specifies details about an error. This parameter is optional and is returned only when it is not empty.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section17256720205514"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}
```

## Example Response<a name="section827141312330"></a>

```
{
    "server": {
        "addresses": {
            "68269e6e-4a27-441b-8029-35373ad50bd9": [
                {
                    "addr": "192.168.0.3", 
                    "version": 4,
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:1b:35:78",
                    "OS-EXT-IPS:type": "fixed"
                }
            ]
        }, 
        "created": "2012-08-20T21:11:09Z", 
        "flavor": {
            "id": "1", 
            "links": [
                {
                    "href": "http://openstack.example.com/openstack/flavors/1", 
                    "rel": "bookmark"
                }
            ]
        }, 
        "hostId": "65201c14a29663e06d0748e561207d998b343e1d164bfa0aafa9c45d", 
        "id": "893c7791-f1df-4c3d-8383-3caae9656c62", 
        "image": "", 
        "links": [
            {
                "href": "http://openstack.example.com/v2/openstack/servers/893c7791-f1df-4c3d-8383-3caae9656c62", 
                "rel": "self"
            }, 
            {
                "href": "http://openstack.example.com/openstack/servers/893c7791-f1df-4c3d-8383-3caae9656c62", 
                "rel": "bookmark"
            }
        ], 
        "metadata": {},
        "name": "new-server-test", 
        "progress": 0, 
        "status": "ACTIVE", 
        "tenant_id": "openstack", 
        "updated": "2012-08-20T21:11:09Z", 
        "user_id": "fake"
    }
}
```

## Returned Values<a name="section7610951"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

