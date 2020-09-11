# Querying ECSs<a name="EN-US_TOPIC_0020212688"></a>

## Function<a name="section56354875"></a>

This API is used to query ECSs.

## URI<a name="section37431827"></a>

GET /v2/\{project\_id\}/servers\{?changes-since,image,flavor,name,status,limit,marker,not-tags,reservation\_id,ip\}

GET /v2.1/\{project\_id\}/servers\{?changes-since,image,flavor,name,status,limit,marker,not-tags,reservation\_id,ip\}

[Table 1](#table5536817)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table5536817"></a>
<table><thead align="left"><tr id="row36554200"><th class="cellrowborder" valign="top" width="16.8%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.64999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12177730"><td class="cellrowborder" valign="top" width="16.8%" headers="mcps1.2.4.1.1 "><p id="p46872098"><a name="p46872098"></a><a name="p46872098"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p38543611"><a name="p38543611"></a><a name="p38543611"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section53661417235"></a>

[Table 2](#table34603472320)  describes the request parameters.

**Table  2**  Request parameters

<a name="table34603472320"></a>
<table><thead align="left"><tr id="row646014417232"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.5.1.1"><p id="p9460749239"><a name="p9460749239"></a><a name="p9460749239"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.45%" id="mcps1.2.5.1.2"><p id="p164601145235"><a name="p164601145235"></a><a name="p164601145235"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.57%" id="mcps1.2.5.1.3"><p id="p1746017414236"><a name="p1746017414236"></a><a name="p1746017414236"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.17%" id="mcps1.2.5.1.4"><p id="p144601748235"><a name="p144601748235"></a><a name="p144601748235"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row134601442317"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p204600417237"><a name="p204600417237"></a><a name="p204600417237"></a>changes-since</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p546017410231"><a name="p546017410231"></a><a name="p546017410231"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p20460945230"><a name="p20460945230"></a><a name="p20460945230"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p19460041231"><a name="p19460041231"></a><a name="p19460041231"></a>Specifies the timestamp of the last ECS status update, which is used to filter out the ECSs with statues updated later than the timestamp. The format must comply with ISO 8601 in the format of CCYY-MM-DDThh:mm:ss+/-hh:mm, for example, 2018-01-17T03:03:32Z.</p>
</td>
</tr>
<tr id="row546084152319"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p194607482315"><a name="p194607482315"></a><a name="p194607482315"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p164606492311"><a name="p164606492311"></a><a name="p164606492311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p10460114112310"><a name="p10460114112310"></a><a name="p10460114112310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p1146019416233"><a name="p1146019416233"></a><a name="p1146019416233"></a>Specifies the image ID.</p>
<p id="p10460540235"><a name="p10460540235"></a><a name="p10460540235"></a>When image is used as a filter criterion, other filter criteria and paging criteria are not supported. If both the image and other filter criteria are specified, the image filter criterion prevails. If the query criteria do not contain the image filter criterion, API functions are not restricted.</p>
</td>
</tr>
<tr id="row646020412239"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p134601742238"><a name="p134601742238"></a><a name="p134601742238"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p1346017472318"><a name="p1346017472318"></a><a name="p1346017472318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p546074132319"><a name="p546074132319"></a><a name="p546074132319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p74607411238"><a name="p74607411238"></a><a name="p74607411238"></a>Specifies the ECS type ID, which is fuzzy matched.</p>
</td>
</tr>
<tr id="row74603419237"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p146012442312"><a name="p146012442312"></a><a name="p146012442312"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p14460184112317"><a name="p14460184112317"></a><a name="p14460184112317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p104600416239"><a name="p104600416239"></a><a name="p104600416239"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p84601048232"><a name="p84601048232"></a><a name="p84601048232"></a>Specifies the ECS name, which is fuzzy matched.</p>
</td>
</tr>
<tr id="row446034182311"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p17460144192313"><a name="p17460144192313"></a><a name="p17460144192313"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p1746019422316"><a name="p1746019422316"></a><a name="p1746019422316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p4460445232"><a name="p4460445232"></a><a name="p4460445232"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p1146084172313"><a name="p1146084172313"></a><a name="p1146084172313"></a>Specifies the ECS status.</p>
<p id="p1146016413234"><a name="p1146016413234"></a><a name="p1146016413234"></a>Options:</p>
<p id="p186329121594"><a name="p186329121594"></a><a name="p186329121594"></a><strong id="b214174715346"><a name="b214174715346"></a><a name="b214174715346"></a>ACTIVE</strong>, <strong id="b490014493341"><a name="b490014493341"></a><a name="b490014493341"></a>BUILD</strong>, <strong id="b8206652153413"><a name="b8206652153413"></a><a name="b8206652153413"></a>ERROR</strong>, <strong id="b137105618342"><a name="b137105618342"></a><a name="b137105618342"></a>HARD_REBOOT</strong>, <strong id="b12124185913347"><a name="b12124185913347"></a><a name="b12124185913347"></a>MIGRATING</strong>, <strong id="b282218463510"><a name="b282218463510"></a><a name="b282218463510"></a>REBOOT</strong>, <strong id="b2036715810351"><a name="b2036715810351"></a><a name="b2036715810351"></a>REBUILD</strong>, <strong id="b416220113357"><a name="b416220113357"></a><a name="b416220113357"></a>RESIZE</strong>, <strong id="b156201614133518"><a name="b156201614133518"></a><a name="b156201614133518"></a>REVERT_RESIZE</strong>, <strong id="b17456161817354"><a name="b17456161817354"></a><a name="b17456161817354"></a>SHUTOFF</strong>, and <strong id="b9409121193517"><a name="b9409121193517"></a><a name="b9409121193517"></a>VERIFY_RESIZE</strong></p>
<p id="p168361158173715"><a name="p168361158173715"></a><a name="p168361158173715"></a>In microversion 2.37, the system will return an empty list for the <strong id="b842352706171434"><a name="b842352706171434"></a><a name="b842352706171434"></a>status</strong> field out of the preceding options. In microversion 2.38 and later, the system will return error 404.</p>
<p id="p278023623513"><a name="p278023623513"></a><a name="p278023623513"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="row1546084152312"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p1546074132313"><a name="p1546074132313"></a><a name="p1546074132313"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p7460154132315"><a name="p7460154132315"></a><a name="p7460154132315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p9460741239"><a name="p9460741239"></a><a name="p9460741239"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p9460147236"><a name="p9460147236"></a><a name="p9460147236"></a>Specifies the upper limit on the number of returned results.</p>
</td>
</tr>
<tr id="row1746044112318"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p34602410233"><a name="p34602410233"></a><a name="p34602410233"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p1946094112310"><a name="p1946094112310"></a><a name="p1946094112310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p14460249231"><a name="p14460249231"></a><a name="p14460249231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p174601046239"><a name="p174601046239"></a><a name="p174601046239"></a>Specifies the marker that points to the ECS ID. The query will start from its next ID.</p>
</td>
</tr>
<tr id="row185002082103"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p04361918181018"><a name="p04361918181018"></a><a name="p04361918181018"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p1643615187104"><a name="p1643615187104"></a><a name="p1643615187104"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p1543617183101"><a name="p1543617183101"></a><a name="p1543617183101"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p147941324101014"><a name="p147941324101014"></a><a name="p147941324101014"></a>Queries ECSs with tags containing the specified value.</p>
</td>
</tr>
<tr id="row1846074192312"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p124601549231"><a name="p124601549231"></a><a name="p124601549231"></a>not-tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p12460174182314"><a name="p12460174182314"></a><a name="p12460174182314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p1460144172313"><a name="p1460144172313"></a><a name="p1460144172313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p497882461442"><a name="p497882461442"></a><a name="p497882461442"></a>Queries ECSs with tags not containing the specified value. The value is the tag key.</p>
<p id="p9642991507"><a name="p9642991507"></a><a name="p9642991507"></a>For details about key rules, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
<div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1745221311560"><a name="p1745221311560"></a><a name="p1745221311560"></a>Tag functions have been upgraded on the public cloud. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
<p id="p213418685710"><a name="p213418685710"></a><a name="p213418685710"></a>For example, an existing tag is <strong id="b84235270610509"><a name="b84235270610509"></a><a name="b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "not-tags=a".</p>
</div></div>
</td>
</tr>
<tr id="row84604419236"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p1346012415236"><a name="p1346012415236"></a><a name="p1346012415236"></a>reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p174607412312"><a name="p174607412312"></a><a name="p174607412312"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p11460164162317"><a name="p11460164162317"></a><a name="p11460164162317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p546010452316"><a name="p546010452316"></a><a name="p546010452316"></a>Specifies the ID returned when ECSs are created in a batch. This parameter is used to query ECSs created in a batch.</p>
</td>
</tr>
<tr id="row117621433502"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p1776243125019"><a name="p1776243125019"></a><a name="p1776243125019"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p0762163105016"><a name="p0762163105016"></a><a name="p0762163105016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p1376214355014"><a name="p1376214355014"></a><a name="p1376214355014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p6597141911013"><a name="p6597141911013"></a><a name="p6597141911013"></a>Sorts query results by ECS attribute. The default sorting order is the reverse order of <strong id="b181551455183619"><a name="b181551455183619"></a><a name="b181551455183619"></a>created_at</strong>.</p>
<p id="p576212355010"><a name="p576212355010"></a><a name="p576212355010"></a>Options: <strong id="b6349137386"><a name="b6349137386"></a><a name="b6349137386"></a>created_at</strong>, <strong id="b184627123813"><a name="b184627123813"></a><a name="b184627123813"></a>availability_zone</strong>, <strong id="b1473221013382"><a name="b1473221013382"></a><a name="b1473221013382"></a>display_name</strong>, <strong id="b6410819193814"><a name="b6410819193814"></a><a name="b6410819193814"></a>host</strong>, <strong id="b1479512343814"><a name="b1479512343814"></a><a name="b1479512343814"></a>instance_type_id</strong>, <strong id="b210818281380"><a name="b210818281380"></a><a name="b210818281380"></a>key_name</strong>, <strong id="b186361931113818"><a name="b186361931113818"></a><a name="b186361931113818"></a>project_id</strong>, <strong id="b21467358386"><a name="b21467358386"></a><a name="b21467358386"></a>user_id</strong>, <strong id="b73751239143818"><a name="b73751239143818"></a><a name="b73751239143818"></a>updated_at</strong>, <strong id="b17626343143813"><a name="b17626343143813"></a><a name="b17626343143813"></a>uuid</strong>, and <strong id="b01591447153810"><a name="b01591447153810"></a><a name="b01591447153810"></a>vm_state</strong></p>
</td>
</tr>
<tr id="row84672413489"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.5.1.1 "><p id="p1646514518158"><a name="p1646514518158"></a><a name="p1646514518158"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.2 "><p id="p1446519457156"><a name="p1446519457156"></a><a name="p1446519457156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.57%" headers="mcps1.2.5.1.3 "><p id="p1846584518155"><a name="p1846584518155"></a><a name="p1846584518155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p546524517153"><a name="p546524517153"></a><a name="p546524517153"></a>Indicates the IPv4 address filtering result.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section12079142"></a>

[Table 3](#table44736746)  describes the response parameters.

**Table  3**  Response parameters

<a name="table44736746"></a>
<table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="18.85%" id="mcps1.2.4.1.1"><p id="p63657004"><a name="p63657004"></a><a name="p63657004"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p35147813"><a name="p35147813"></a><a name="p35147813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.73%" id="mcps1.2.4.1.3"><p id="p28400574"><a name="p28400574"></a><a name="p28400574"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.73%" headers="mcps1.2.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies the ECSs to be queried. For details, see <a href="#table11253402">Table 4</a>.</p>
</td>
</tr>
<tr id="row20821122316810"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.4.1.1 "><p id="p104447017432"><a name="p104447017432"></a><a name="p104447017432"></a>servers_links</p>
</td>
<td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p1749328217432"><a name="p1749328217432"></a><a name="p1749328217432"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.73%" headers="mcps1.2.4.1.3 "><p id="p766970517432"><a name="p766970517432"></a><a name="p766970517432"></a>Specifies the link of the next page in pagination query. For details, see <a href="#table64121649">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **servers**  field description

<a name="table11253402"></a>
<table><thead align="left"><tr id="row10267559"><th class="cellrowborder" valign="top" width="18.790000000000003%" id="mcps1.2.4.1.1"><p id="p151461728122514"><a name="p151461728122514"></a><a name="p151461728122514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.4.1.2"><p id="p3146122815253"><a name="p3146122815253"></a><a name="p3146122815253"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.67%" id="mcps1.2.4.1.3"><p id="p18146728162513"><a name="p18146728162513"></a><a name="p18146728162513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15663"><td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.2.4.1.1 "><p id="p1268752"><a name="p1268752"></a><a name="p1268752"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.4.1.2 "><p id="p2786131"><a name="p2786131"></a><a name="p2786131"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p24350086"><a name="p24350086"></a><a name="p24350086"></a>Specifies the ECS name.</p>
</td>
</tr>
<tr id="row17824184"><td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.2.4.1.1 "><p id="p34472770"><a name="p34472770"></a><a name="p34472770"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.4.1.2 "><p id="p18974148"><a name="p18974148"></a><a name="p18974148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p60510987"><a name="p60510987"></a><a name="p60510987"></a>Specifies an ECS uniquely.</p>
</td>
</tr>
<tr id="row7727977"><td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.2.4.1.1 "><p id="p21986423"><a name="p21986423"></a><a name="p21986423"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.4.1.2 "><p id="p35973707"><a name="p35973707"></a><a name="p35973707"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.67%" headers="mcps1.2.4.1.3 "><p id="p52375797"><a name="p52375797"></a><a name="p52375797"></a>Specifies ECS shortcut links. For details, see <a href="#table64121649">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **servers\_links**  and  **links**  field description

<a name="table64121649"></a>
<table><thead align="left"><tr id="row59320951"><th class="cellrowborder" valign="top" width="18.73%" id="mcps1.2.4.1.1"><p id="p7550144882519"><a name="p7550144882519"></a><a name="p7550144882519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p8566114814254"><a name="p8566114814254"></a><a name="p8566114814254"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.60000000000001%" id="mcps1.2.4.1.3"><p id="p4566124832516"><a name="p4566124832516"></a><a name="p4566124832516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61486274"><td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.2.4.1.1 "><p id="p14332335"><a name="p14332335"></a><a name="p14332335"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p14933841"><a name="p14933841"></a><a name="p14933841"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.4.1.3 "><p id="p1681623"><a name="p1681623"></a><a name="p1681623"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row15134612"><td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.2.4.1.1 "><p id="p17944037"><a name="p17944037"></a><a name="p17944037"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p21885054"><a name="p21885054"></a><a name="p21885054"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.4.1.3 "><p id="p27858965"><a name="p27858965"></a><a name="p27858965"></a>Specifies the shortcut link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section18645171418547"></a>

```
GET https://{endpoint}/v2/{project_id}/servers
GET https://{endpoint}/v2.1/{project_id}/servers
```

## Example Response<a name="section1047337102619"></a>

```
{
    "servers": [
        {
            "id": "616fb98f-46ca-475e-917e-2563e5a8cd19", 
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/616fb98f-46ca-475e-917e-2563e5a8cd19", 
                    "rel": "self"
                }, 
                {
                    "href": "http://openstack.example.com/openstack/servers/616fb98f-46ca-475e-917e-2563e5a8cd19", 
                    "rel": "bookmark"
                }
            ], 
            "name": "new-server-test"
        }
    ]
}
```

## Returned Values<a name="section41603419"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

