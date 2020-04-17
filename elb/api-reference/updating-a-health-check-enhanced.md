# Updating a Health Check<a name="EN-US_TOPIC_0096561564"></a>

## Function<a name="en-us_topic_0049139666_section37518984"></a>

This API is used to update a health check.

## URI<a name="en-us_topic_0049139666_section2126544"></a>

PUT /v2.0/lbaas/healthmonitors/\{healthmonitor\_id\}

**Table  1**  Parameter description

<a name="table71865297294"></a>
<table><thead align="left"><tr id="row102351629152911"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1523562962910"><a name="p1523562962910"></a><a name="p1523562962910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p17235329152919"><a name="p17235329152919"></a><a name="p17235329152919"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p16235112912920"><a name="p16235112912920"></a><a name="p16235112912920"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p32351829182910"><a name="p32351829182910"></a><a name="p32351829182910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row923562992910"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p22359291297"><a name="p22359291297"></a><a name="p22359291297"></a>healthmonitor_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p8993121115284"><a name="p8993121115284"></a><a name="p8993121115284"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p10235929142916"><a name="p10235929142916"></a><a name="p10235929142916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p14235152962911"><a name="p14235152962911"></a><a name="p14235152962911"></a>Specifies the health check ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139666_section19138897"></a>

If  **provisioning\_status**  of the load balancer for which the health check is configured is not  **ACTIVE**, the health check cannot be updated.

## Request<a name="en-us_topic_0049139666_section60721476"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0049139666_table12185309"></a>
<table><thead align="left"><tr id="en-us_topic_0049139666_row58571242"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139666_p46650162"><a name="en-us_topic_0049139666_p46650162"></a><a name="en-us_topic_0049139666_p46650162"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="en-us_topic_0049139666_p55297360"><a name="en-us_topic_0049139666_p55297360"></a><a name="en-us_topic_0049139666_p55297360"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p4611184915286"><a name="p4611184915286"></a><a name="p4611184915286"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0049139666_p49901174"><a name="en-us_topic_0049139666_p49901174"></a><a name="en-us_topic_0049139666_p49901174"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139666_row15463264"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139666_p44564854"><a name="en-us_topic_0049139666_p44564854"></a><a name="en-us_topic_0049139666_p44564854"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049139666_p63801673"><a name="en-us_topic_0049139666_p63801673"></a><a name="en-us_topic_0049139666_p63801673"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p15610449192818"><a name="p15610449192818"></a><a name="p15610449192818"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139666_p553045"><a name="en-us_topic_0049139666_p553045"></a><a name="en-us_topic_0049139666_p553045"></a>Specifies the health check. For details, see <a href="#table61361617301">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **healthmonitor**  parameter description

<a name="table61361617301"></a>
<table><thead align="left"><tr id="row830011619301"><th class="cellrowborder" valign="top" width="21.0978902109789%" id="mcps1.2.5.1.1"><p id="p230017616303"><a name="p230017616303"></a><a name="p230017616303"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.978602139786023%" id="mcps1.2.5.1.2"><p id="p1030036103019"><a name="p1030036103019"></a><a name="p1030036103019"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.428457154284573%" id="mcps1.2.5.1.3"><p id="p2300156163014"><a name="p2300156163014"></a><a name="p2300156163014"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.495050494950505%" id="mcps1.2.5.1.4"><p id="p53001762308"><a name="p53001762308"></a><a name="p53001762308"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11300465300"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p1300186153017"><a name="p1300186153017"></a><a name="p1300186153017"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p6300666305"><a name="p6300666305"></a><a name="p6300666305"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p103001062301"><a name="p103001062301"></a><a name="p103001062301"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p20300156103020"><a name="p20300156103020"></a><a name="p20300156103020"></a>Specifies the health check name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row15300666308"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p230036193012"><a name="p230036193012"></a><a name="p230036193012"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p230086123012"><a name="p230086123012"></a><a name="p230086123012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p230018633015"><a name="p230018633015"></a><a name="p230018633015"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p20300164309"><a name="p20300164309"></a><a name="p20300164309"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="b1221515449466"><a name="b1221515449466"></a><a name="b1221515449466"></a>1</strong> to <strong id="b162165448462"><a name="b162165448462"></a><a name="b162165448462"></a>50</strong>.</p>
</td>
</tr>
<tr id="row12300964305"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p1430046103010"><a name="p1430046103010"></a><a name="p1430046103010"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p183001664309"><a name="p183001664309"></a><a name="p183001664309"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p12300146123016"><a name="p12300146123016"></a><a name="p12300146123016"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p1991219919349"><a name="p1991219919349"></a><a name="p1991219919349"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="b1314983522918"><a name="b1314983522918"></a><a name="b1314983522918"></a>fail</strong> to <strong id="b21504355292"><a name="b21504355292"></a><a name="b21504355292"></a>success</strong>. The value ranges from <strong id="b8150735172919"><a name="b8150735172919"></a><a name="b8150735172919"></a>1</strong> to <strong id="b51501335102919"><a name="b51501335102919"></a><a name="b51501335102919"></a>10</strong>.</p>
</td>
</tr>
<tr id="row193001569303"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p930056103015"><a name="p930056103015"></a><a name="p930056103015"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p1530014614307"><a name="p1530014614307"></a><a name="p1530014614307"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p193001361301"><a name="p193001361301"></a><a name="p193001361301"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p14932133633814"><a name="p14932133633814"></a><a name="p14932133633814"></a>Specifies the administrative status of the health check.</p>
<p id="p737455383817"><a name="p737455383817"></a><a name="p737455383817"></a>The value can be <strong id="b1898184911466"><a name="b1898184911466"></a><a name="b1898184911466"></a>true</strong> or <strong id="b2899549154612"><a name="b2899549154612"></a><a name="b2899549154612"></a>false</strong>. The default value is <strong id="b19931145094615"><a name="b19931145094615"></a><a name="b19931145094615"></a>true</strong>.</p>
<a name="ul118694033910"></a><a name="ul118694033910"></a><ul id="ul118694033910"><li><strong id="b17292752124613"><a name="b17292752124613"></a><a name="b17292752124613"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="b9760155364617"><a name="b9760155364617"></a><a name="b9760155364617"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="row143001867306"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p230012613302"><a name="p230012613302"></a><a name="p230012613302"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p14300864308"><a name="p14300864308"></a><a name="p14300864308"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p1230012663011"><a name="p1230012663011"></a><a name="p1230012663011"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p1784571273912"><a name="p1784571273912"></a><a name="p1784571273912"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="b5889175510463"><a name="b5889175510463"></a><a name="b5889175510463"></a>1</strong> to <strong id="b1089065504612"><a name="b1089065504612"></a><a name="b1089065504612"></a>50</strong>.</p>
<div class="note" id="note187671922193912"><a name="note187671922193912"></a><a name="note187671922193912"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15769322123919"><a name="p15769322123919"></a><a name="p15769322123919"></a>You are advised to set the value less than that of parameter <strong id="b550025713461"><a name="b550025713461"></a><a name="b550025713461"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1550918371128"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p56509421283"><a name="p56509421283"></a><a name="p56509421283"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p166502042192819"><a name="p166502042192819"></a><a name="p166502042192819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p66504426282"><a name="p66504426282"></a><a name="p66504426282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p1444014213398"><a name="p1444014213398"></a><a name="p1444014213398"></a>Specifies the health check protocol.</p>
<p id="p76509429289"><a name="p76509429289"></a><a name="p76509429289"></a>The value can be <strong id="b10505154220313"><a name="b10505154220313"></a><a name="b10505154220313"></a>TCP</strong>, <strong id="b175066422319"><a name="b175066422319"></a><a name="b175066422319"></a>UDP_CONNECT</strong>, or <strong id="b1750715420314"><a name="b1750715420314"></a><a name="b1750715420314"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row143005613016"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p730212653017"><a name="p730212653017"></a><a name="p730212653017"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p113021665303"><a name="p113021665303"></a><a name="p113021665303"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p330210663010"><a name="p330210663010"></a><a name="p330210663010"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p10119958144115"><a name="p10119958144115"></a><a name="p10119958144115"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="p1165151154216"><a name="p1165151154216"></a><a name="p1165151154216"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="row123024610308"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p103022062309"><a name="p103022062309"></a><a name="p103022062309"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p230214610307"><a name="p230214610307"></a><a name="p230214610307"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p930210616307"><a name="p930210616307"></a><a name="p930210616307"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p11981302"><a name="p11981302"></a><a name="p11981302"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="p40722856"><a name="p40722856"></a><a name="p40722856"></a>A single value, such as 200</p>
<p id="p30961386"><a name="p30961386"></a><a name="p30961386"></a>A list of values, such as 200 and 202</p>
<p id="p10217021"><a name="p10217021"></a><a name="p10217021"></a>A value range, such as 200 to 204</p>
<p id="p24844331"><a name="p24844331"></a><a name="p24844331"></a>This parameter is valid when the value of <strong id="b13262749193115"><a name="b13262749193115"></a><a name="b13262749193115"></a>type</strong> is set to <strong id="b18263249153114"><a name="b18263249153114"></a><a name="b18263249153114"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row83021869302"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p10302176133017"><a name="p10302176133017"></a><a name="p10302176133017"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p33027614305"><a name="p33027614305"></a><a name="p33027614305"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p1030210610304"><a name="p1030210610304"></a><a name="p1030210610304"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p178364704214"><a name="p178364704214"></a><a name="p178364704214"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="p1833549104310"><a name="p1833549104310"></a><a name="p1833549104310"></a>This parameter is valid when the value of <strong id="b637812864719"><a name="b637812864719"></a><a name="b637812864719"></a>type</strong> is set to <strong id="b637917819471"><a name="b637917819471"></a><a name="b637917819471"></a>HTTP</strong>.</p>
<p id="p19194239134314"><a name="p19194239134314"></a><a name="p19194239134314"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="p4782712144317"><a name="p4782712144317"></a><a name="p4782712144317"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="b886773413332"><a name="b886773413332"></a><a name="b886773413332"></a>www.test.com</strong>.</p>
<p id="p8589189165912"><a name="p8589189165912"></a><a name="p8589189165912"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="row93023623016"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p130216123011"><a name="p130216123011"></a><a name="p130216123011"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p630213613301"><a name="p630213613301"></a><a name="p630213613301"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p18302206123010"><a name="p18302206123010"></a><a name="p18302206123010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p134815784414"><a name="p134815784414"></a><a name="p134815784414"></a>Specifies the HTTP request path for the health check. The default value is <strong id="b1134110189478"><a name="b1134110189478"></a><a name="b1134110189478"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="p2026272014445"><a name="p2026272014445"></a><a name="p2026272014445"></a>This parameter is valid when the value of <strong id="b1835952074716"><a name="b1835952074716"></a><a name="b1835952074716"></a>type</strong> is set to <strong id="b236032014479"><a name="b236032014479"></a><a name="b236032014479"></a>HTTP</strong>.</p>
<p id="p108766337449"><a name="p108766337449"></a><a name="p108766337449"></a>An example value is <strong id="b1721942116471"><a name="b1721942116471"></a><a name="b1721942116471"></a>/test</strong>.</p>
<p id="p0951133145917"><a name="p0951133145917"></a><a name="p0951133145917"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1030211683018"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.2.5.1.1 "><p id="p23021862301"><a name="p23021862301"></a><a name="p23021862301"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="13.978602139786023%" headers="mcps1.2.5.1.2 "><p id="p53021660309"><a name="p53021660309"></a><a name="p53021660309"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.2.5.1.3 "><p id="p14302146113011"><a name="p14302146113011"></a><a name="p14302146113011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.495050494950505%" headers="mcps1.2.5.1.4 "><p id="p316954715453"><a name="p316954715453"></a><a name="p316954715453"></a>Specifies the HTTP request method. The default value is <strong id="b9159722104717"><a name="b9159722104717"></a><a name="b9159722104717"></a>GET</strong>.</p>
<p id="p21871844204517"><a name="p21871844204517"></a><a name="p21871844204517"></a>The value can be <strong id="b3533202310479"><a name="b3533202310479"></a><a name="b3533202310479"></a>GET</strong>, <strong id="b75341623154713"><a name="b75341623154713"></a><a name="b75341623154713"></a>HEAD</strong>, <strong id="b653412239475"><a name="b653412239475"></a><a name="b653412239475"></a>POST</strong>, <strong id="b8535132344713"><a name="b8535132344713"></a><a name="b8535132344713"></a>PUT</strong>, <strong id="b135361223154716"><a name="b135361223154716"></a><a name="b135361223154716"></a>DELETE</strong>, <strong id="b45361723154719"><a name="b45361723154719"></a><a name="b45361723154719"></a>TRACE</strong>, <strong id="b153716231476"><a name="b153716231476"></a><a name="b153716231476"></a>OPTIONS</strong>, <strong id="b353712314715"><a name="b353712314715"></a><a name="b353712314715"></a>CONNECT</strong>, and <strong id="b195387236470"><a name="b195387236470"></a><a name="b195387236470"></a>PATCH</strong>.</p>
<p id="p658413198402"><a name="p658413198402"></a><a name="p658413198402"></a>This parameter is valid when the value of <strong id="b181225254473"><a name="b181225254473"></a><a name="b181225254473"></a>type</strong> is set to <strong id="b3123525134714"><a name="b3123525134714"></a><a name="b3123525134714"></a>HTTP</strong>.</p>
<p id="p14820113585918"><a name="p14820113585918"></a><a name="p14820113585918"></a>The value contains a maximum of 16 characters.</p>
<div class="note" id="note18114145413811"><a name="note18114145413811"></a><a name="note18114145413811"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p911455418383"><a name="p911455418383"></a><a name="p911455418383"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139666_section9622376"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0049139666_table44796718"></a>
<table><thead align="left"><tr id="en-us_topic_0049139666_row27530415"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139666_p15371167"><a name="en-us_topic_0049139666_p15371167"></a><a name="en-us_topic_0049139666_p15371167"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139666_p37105032"><a name="en-us_topic_0049139666_p37105032"></a><a name="en-us_topic_0049139666_p37105032"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p7801153163319"><a name="p7801153163319"></a><a name="p7801153163319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139666_row990244"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139666_p13100926"><a name="en-us_topic_0049139666_p13100926"></a><a name="en-us_topic_0049139666_p13100926"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139666_p54542105"><a name="en-us_topic_0049139666_p54542105"></a><a name="en-us_topic_0049139666_p54542105"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139666_p26292272"><a name="en-us_topic_0049139666_p26292272"></a><a name="en-us_topic_0049139666_p26292272"></a>Specifies the health check. For details, see <a href="#table25969311303">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **healthmonitor**  parameter description

<a name="table25969311303"></a>
<table><thead align="left"><tr id="en-us_topic_0096561563_row19929157112914"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561563_p59295713297"><a name="en-us_topic_0096561563_p59295713297"></a><a name="en-us_topic_0096561563_p59295713297"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561563_p79292720293"><a name="en-us_topic_0096561563_p79292720293"></a><a name="en-us_topic_0096561563_p79292720293"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561563_p1258101218348"><a name="en-us_topic_0096561563_p1258101218348"></a><a name="en-us_topic_0096561563_p1258101218348"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561563_row1192911772916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p5929177112912"><a name="en-us_topic_0096561563_p5929177112912"></a><a name="en-us_topic_0096561563_p5929177112912"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p5947132518343"><a name="en-us_topic_0096561563_p5947132518343"></a><a name="en-us_topic_0096561563_p5947132518343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p109296702911"><a name="en-us_topic_0096561563_p109296702911"></a><a name="en-us_topic_0096561563_p109296702911"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row792915762911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p59290711296"><a name="en-us_topic_0096561563_p59290711296"></a><a name="en-us_topic_0096561563_p59290711296"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1792918772913"><a name="en-us_topic_0096561563_p1792918772913"></a><a name="en-us_topic_0096561563_p1792918772913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p269292715918"><a name="en-us_topic_0096561563_p269292715918"></a><a name="en-us_topic_0096561563_p269292715918"></a>Specifies the ID of the project where the health check is performed.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row209291674295"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p692919752912"><a name="en-us_topic_0096561563_p692919752912"></a><a name="en-us_topic_0096561563_p692919752912"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p131123323411"><a name="en-us_topic_0096561563_p131123323411"></a><a name="en-us_topic_0096561563_p131123323411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p199294713299"><a name="en-us_topic_0096561563_p199294713299"></a><a name="en-us_topic_0096561563_p199294713299"></a>Specifies the health check name.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row5929279299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p892987162910"><a name="en-us_topic_0096561563_p892987162910"></a><a name="en-us_topic_0096561563_p892987162910"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p792918772915"><a name="en-us_topic_0096561563_p792918772915"></a><a name="en-us_topic_0096561563_p792918772915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p119293720295"><a name="en-us_topic_0096561563_p119293720295"></a><a name="en-us_topic_0096561563_p119293720295"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="en-us_topic_0096561563_b53341117227"><a name="en-us_topic_0096561563_b53341117227"></a><a name="en-us_topic_0096561563_b53341117227"></a>1</strong> to <strong id="en-us_topic_0096561563_b1233617116226"><a name="en-us_topic_0096561563_b1233617116226"></a><a name="en-us_topic_0096561563_b1233617116226"></a>50</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row179291072296"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p15929157192911"><a name="en-us_topic_0096561563_p15929157192911"></a><a name="en-us_topic_0096561563_p15929157192911"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p178711239193411"><a name="en-us_topic_0096561563_p178711239193411"></a><a name="en-us_topic_0096561563_p178711239193411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p189309702917"><a name="en-us_topic_0096561563_p189309702917"></a><a name="en-us_topic_0096561563_p189309702917"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="en-us_topic_0096561563_b8737342112519"><a name="en-us_topic_0096561563_b8737342112519"></a><a name="en-us_topic_0096561563_b8737342112519"></a>fail</strong> to <strong id="en-us_topic_0096561563_b97392422258"><a name="en-us_topic_0096561563_b97392422258"></a><a name="en-us_topic_0096561563_b97392422258"></a>success</strong>. The value ranges from <strong id="en-us_topic_0096561563_b18741134213251"><a name="en-us_topic_0096561563_b18741134213251"></a><a name="en-us_topic_0096561563_b18741134213251"></a>1</strong> to <strong id="en-us_topic_0096561563_b18742842132513"><a name="en-us_topic_0096561563_b18742842132513"></a><a name="en-us_topic_0096561563_b18742842132513"></a>10</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1193097152917"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p1793016712298"><a name="en-us_topic_0096561563_p1793016712298"></a><a name="en-us_topic_0096561563_p1793016712298"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561563_en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p893015710294"><a name="en-us_topic_0096561563_p893015710294"></a><a name="en-us_topic_0096561563_p893015710294"></a>Specifies the ID of the backend server group associated with the health check.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row2930197182911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p79301777292"><a name="en-us_topic_0096561563_p79301777292"></a><a name="en-us_topic_0096561563_p79301777292"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p293017715298"><a name="en-us_topic_0096561563_p293017715298"></a><a name="en-us_topic_0096561563_p293017715298"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p88489418492"><a name="en-us_topic_0096561563_p88489418492"></a><a name="en-us_topic_0096561563_p88489418492"></a>Specifies the administrative status of the health check.</p>
<p id="en-us_topic_0096561563_p19848040494"><a name="en-us_topic_0096561563_p19848040494"></a><a name="en-us_topic_0096561563_p19848040494"></a>The value can be <strong id="en-us_topic_0096561563_b13310921202213"><a name="en-us_topic_0096561563_b13310921202213"></a><a name="en-us_topic_0096561563_b13310921202213"></a>true</strong> or <strong id="en-us_topic_0096561563_b131282110226"><a name="en-us_topic_0096561563_b131282110226"></a><a name="en-us_topic_0096561563_b131282110226"></a>false</strong>. The default value is <strong id="en-us_topic_0096561563_b83981522142217"><a name="en-us_topic_0096561563_b83981522142217"></a><a name="en-us_topic_0096561563_b83981522142217"></a>true</strong>.</p>
<a name="en-us_topic_0096561563_ul1848244497"></a><a name="en-us_topic_0096561563_ul1848244497"></a><ul id="en-us_topic_0096561563_ul1848244497"><li><strong id="en-us_topic_0096561563_b1572441093412"><a name="en-us_topic_0096561563_b1572441093412"></a><a name="en-us_topic_0096561563_b1572441093412"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="en-us_topic_0096561563_b157791112193412"><a name="en-us_topic_0096561563_b157791112193412"></a><a name="en-us_topic_0096561563_b157791112193412"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561563_row09302716299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p19303782913"><a name="en-us_topic_0096561563_p19303782913"></a><a name="en-us_topic_0096561563_p19303782913"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p179315732915"><a name="en-us_topic_0096561563_p179315732915"></a><a name="en-us_topic_0096561563_p179315732915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p37112334494"><a name="en-us_topic_0096561563_p37112334494"></a><a name="en-us_topic_0096561563_p37112334494"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="en-us_topic_0096561563_b1380316275226"><a name="en-us_topic_0096561563_b1380316275226"></a><a name="en-us_topic_0096561563_b1380316275226"></a>1</strong> to <strong id="en-us_topic_0096561563_b1580411278227"><a name="en-us_topic_0096561563_b1580411278227"></a><a name="en-us_topic_0096561563_b1580411278227"></a>50</strong>.</p>
<div class="note" id="en-us_topic_0096561563_note77113384910"><a name="en-us_topic_0096561563_note77113384910"></a><a name="en-us_topic_0096561563_note77113384910"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561563_p57123374911"><a name="en-us_topic_0096561563_p57123374911"></a><a name="en-us_topic_0096561563_p57123374911"></a>You are advised to set the value less than that of parameter <strong id="en-us_topic_0096561563_b10582112915225"><a name="en-us_topic_0096561563_b10582112915225"></a><a name="en-us_topic_0096561563_b10582112915225"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1793116752912"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p6931579296"><a name="en-us_topic_0096561563_p6931579296"></a><a name="en-us_topic_0096561563_p6931579296"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p49311173296"><a name="en-us_topic_0096561563_p49311173296"></a><a name="en-us_topic_0096561563_p49311173296"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p87193317494"><a name="en-us_topic_0096561563_p87193317494"></a><a name="en-us_topic_0096561563_p87193317494"></a>Specifies the health check protocol.</p>
<p id="en-us_topic_0096561563_p5711533184919"><a name="en-us_topic_0096561563_p5711533184919"></a><a name="en-us_topic_0096561563_p5711533184919"></a>The value can be <strong id="en-us_topic_0096561563_b9594432122210"><a name="en-us_topic_0096561563_b9594432122210"></a><a name="en-us_topic_0096561563_b9594432122210"></a>TCP</strong>, <strong id="en-us_topic_0096561563_b19595183219229"><a name="en-us_topic_0096561563_b19595183219229"></a><a name="en-us_topic_0096561563_b19595183219229"></a>UDP_CONNECT</strong>, or <strong id="en-us_topic_0096561563_b14595123282211"><a name="en-us_topic_0096561563_b14595123282211"></a><a name="en-us_topic_0096561563_b14595123282211"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row79313702914"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p29315710299"><a name="en-us_topic_0096561563_p29315710299"></a><a name="en-us_topic_0096561563_p29315710299"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1193119762917"><a name="en-us_topic_0096561563_p1193119762917"></a><a name="en-us_topic_0096561563_p1193119762917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p19915125974920"><a name="en-us_topic_0096561563_p19915125974920"></a><a name="en-us_topic_0096561563_p19915125974920"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="en-us_topic_0096561563_p1891535916496"><a name="en-us_topic_0096561563_p1891535916496"></a><a name="en-us_topic_0096561563_p1891535916496"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row129325719290"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p4639141253611"><a name="en-us_topic_0096561563_p4639141253611"></a><a name="en-us_topic_0096561563_p4639141253611"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1263931216363"><a name="en-us_topic_0096561563_p1263931216363"></a><a name="en-us_topic_0096561563_p1263931216363"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p30010494"><a name="en-us_topic_0096561563_p30010494"></a><a name="en-us_topic_0096561563_p30010494"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="en-us_topic_0096561563_p1658995"><a name="en-us_topic_0096561563_p1658995"></a><a name="en-us_topic_0096561563_p1658995"></a>A single value, such as 200</p>
<p id="en-us_topic_0096561563_p14930959"><a name="en-us_topic_0096561563_p14930959"></a><a name="en-us_topic_0096561563_p14930959"></a>A list of values, such as 200 and 202</p>
<p id="en-us_topic_0096561563_p160907"><a name="en-us_topic_0096561563_p160907"></a><a name="en-us_topic_0096561563_p160907"></a>A value range, such as 200 to 204</p>
<p id="en-us_topic_0096561563_p1448168"><a name="en-us_topic_0096561563_p1448168"></a><a name="en-us_topic_0096561563_p1448168"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b6389401468"><a name="en-us_topic_0096561563_b6389401468"></a><a name="en-us_topic_0096561563_b6389401468"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b113907012461"><a name="en-us_topic_0096561563_b113907012461"></a><a name="en-us_topic_0096561563_b113907012461"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p13033520"><a name="en-us_topic_0096561563_p13033520"></a><a name="en-us_topic_0096561563_p13033520"></a>Currently, this parameter is not supported and is fixed at <strong id="en-us_topic_0096561563_b84235270619455"><a name="en-us_topic_0096561563_b84235270619455"></a><a name="en-us_topic_0096561563_b84235270619455"></a>200</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row1993247182913"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p159326713290"><a name="en-us_topic_0096561563_p159326713290"></a><a name="en-us_topic_0096561563_p159326713290"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p179321712912"><a name="en-us_topic_0096561563_p179321712912"></a><a name="en-us_topic_0096561563_p179321712912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p12394754125016"><a name="en-us_topic_0096561563_p12394754125016"></a><a name="en-us_topic_0096561563_p12394754125016"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="en-us_topic_0096561563_p73941354135010"><a name="en-us_topic_0096561563_p73941354135010"></a><a name="en-us_topic_0096561563_p73941354135010"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b55255217488"><a name="en-us_topic_0096561563_b55255217488"></a><a name="en-us_topic_0096561563_b55255217488"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b1752620264817"><a name="en-us_topic_0096561563_b1752620264817"></a><a name="en-us_topic_0096561563_b1752620264817"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p14394115411501"><a name="en-us_topic_0096561563_p14394115411501"></a><a name="en-us_topic_0096561563_p14394115411501"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="en-us_topic_0096561563_p15394145435010"><a name="en-us_topic_0096561563_p15394145435010"></a><a name="en-us_topic_0096561563_p15394145435010"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="en-us_topic_0096561563_b67911125183711"><a name="en-us_topic_0096561563_b67911125183711"></a><a name="en-us_topic_0096561563_b67911125183711"></a>www.test.com</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row593217719299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p793277152911"><a name="en-us_topic_0096561563_p793277152911"></a><a name="en-us_topic_0096561563_p793277152911"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1593247182917"><a name="en-us_topic_0096561563_p1593247182917"></a><a name="en-us_topic_0096561563_p1593247182917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p6417986512"><a name="en-us_topic_0096561563_p6417986512"></a><a name="en-us_topic_0096561563_p6417986512"></a>Specifies the HTTP request path for the health check. The default value is <strong id="en-us_topic_0096561563_b1437591082310"><a name="en-us_topic_0096561563_b1437591082310"></a><a name="en-us_topic_0096561563_b1437591082310"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="en-us_topic_0096561563_p64181884511"><a name="en-us_topic_0096561563_p64181884511"></a><a name="en-us_topic_0096561563_p64181884511"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b16827165119475"><a name="en-us_topic_0096561563_b16827165119475"></a><a name="en-us_topic_0096561563_b16827165119475"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b188288512479"><a name="en-us_topic_0096561563_b188288512479"></a><a name="en-us_topic_0096561563_b188288512479"></a>HTTP</strong>.</p>
<p id="en-us_topic_0096561563_p1341818185114"><a name="en-us_topic_0096561563_p1341818185114"></a><a name="en-us_topic_0096561563_p1341818185114"></a>An example value is <strong id="en-us_topic_0096561563_b20236172942318"><a name="en-us_topic_0096561563_b20236172942318"></a><a name="en-us_topic_0096561563_b20236172942318"></a>/test</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561563_row3932167132916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561563_p793218711296"><a name="en-us_topic_0096561563_p793218711296"></a><a name="en-us_topic_0096561563_p793218711296"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561563_p1893212710291"><a name="en-us_topic_0096561563_p1893212710291"></a><a name="en-us_topic_0096561563_p1893212710291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561563_p48511267514"><a name="en-us_topic_0096561563_p48511267514"></a><a name="en-us_topic_0096561563_p48511267514"></a>Specifies the HTTP request method. The default value is <strong id="en-us_topic_0096561563_b19886729123413"><a name="en-us_topic_0096561563_b19886729123413"></a><a name="en-us_topic_0096561563_b19886729123413"></a>GET</strong>.</p>
<p id="en-us_topic_0096561563_p11851326135110"><a name="en-us_topic_0096561563_p11851326135110"></a><a name="en-us_topic_0096561563_p11851326135110"></a>The value can be <strong id="en-us_topic_0096561563_b205241432133411"><a name="en-us_topic_0096561563_b205241432133411"></a><a name="en-us_topic_0096561563_b205241432133411"></a>GET</strong>, <strong id="en-us_topic_0096561563_b1524432123415"><a name="en-us_topic_0096561563_b1524432123415"></a><a name="en-us_topic_0096561563_b1524432123415"></a>HEAD</strong>, <strong id="en-us_topic_0096561563_b1452533293413"><a name="en-us_topic_0096561563_b1452533293413"></a><a name="en-us_topic_0096561563_b1452533293413"></a>POST</strong>, <strong id="en-us_topic_0096561563_b12525832163420"><a name="en-us_topic_0096561563_b12525832163420"></a><a name="en-us_topic_0096561563_b12525832163420"></a>PUT</strong>, <strong id="en-us_topic_0096561563_b452653210347"><a name="en-us_topic_0096561563_b452653210347"></a><a name="en-us_topic_0096561563_b452653210347"></a>DELETE</strong>, <strong id="en-us_topic_0096561563_b2052773214341"><a name="en-us_topic_0096561563_b2052773214341"></a><a name="en-us_topic_0096561563_b2052773214341"></a>TRACE</strong>, <strong id="en-us_topic_0096561563_b152812324344"><a name="en-us_topic_0096561563_b152812324344"></a><a name="en-us_topic_0096561563_b152812324344"></a>OPTIONS</strong>, <strong id="en-us_topic_0096561563_b75281932203417"><a name="en-us_topic_0096561563_b75281932203417"></a><a name="en-us_topic_0096561563_b75281932203417"></a>CONNECT</strong>, and <strong id="en-us_topic_0096561563_b7529193220347"><a name="en-us_topic_0096561563_b7529193220347"></a><a name="en-us_topic_0096561563_b7529193220347"></a>PATCH</strong>.</p>
<p id="en-us_topic_0096561563_p485142665115"><a name="en-us_topic_0096561563_p485142665115"></a><a name="en-us_topic_0096561563_p485142665115"></a>This parameter is valid when the value of <strong id="en-us_topic_0096561563_b782231144617"><a name="en-us_topic_0096561563_b782231144617"></a><a name="en-us_topic_0096561563_b782231144617"></a>type</strong> is set to <strong id="en-us_topic_0096561563_b178221611124616"><a name="en-us_topic_0096561563_b178221611124616"></a><a name="en-us_topic_0096561563_b178221611124616"></a>HTTP</strong>.</p>
<div class="note" id="en-us_topic_0096561563_note985119267515"><a name="en-us_topic_0096561563_note985119267515"></a><a name="en-us_topic_0096561563_note985119267515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0096561563_p1885112263511"><a name="en-us_topic_0096561563_p1885112263511"></a><a name="en-us_topic_0096561563_p1885112263511"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1133411497515"></a>

-   Example request: Updating a health check

    ```
    PUT https://{Endpoint}/v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412
    
    {
      "healthmonitor": {
        "delay": 15,
        "name": "health-xx",
        "timeout": 12
       }
    }
    ```

-   Example response

    ```
    {
      "healthmonitor": {
        "name": "health-xx",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
        "domain_name": null,
        "delay": 15,
        "expected_codes": "200",
        "max_retries": 10,
        
        "http_method": "GET",
        "timeout": 12,
        "pools": [
          {
            "id": "bb44bffb-05d9-412c-9d9c-b189d9e14193"
          }
        ],
        "url_path": "/",
        "type": "HTTP",
        "id": "2dca3867-98c5-4cde-8f2c-b89ae6bd7e36",
        "monitor_port": 112
      }
    }
    ```


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

