# Configuring a Health Check<a name="EN-US_TOPIC_0096561563"></a>

## Function<a name="en-us_topic_0049139665_section48637208"></a>

This API is used to configure a health check for a backend server group to check the status of backend servers. If the health check result is  **OFFLINE**, backend servers are considered unhealthy. You need to check the server configuration.

## URI<a name="en-us_topic_0049139665_section35081689"></a>

POST /v2.0/lbaas/healthmonitors

## Constraints<a name="en-us_topic_0049139665_section47299748"></a>

The security group must allow access from 100.125.0.0/16. Otherwise, the health check cannot be performed.

## Request<a name="en-us_topic_0049139665_section54669653"></a>

**Table  1**  Request parameters

<a name="en-us_topic_0049139665_table470163"></a>
<table><thead align="left"><tr id="en-us_topic_0049139665_row24812117"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049139665_p63624481"><a name="en-us_topic_0049139665_p63624481"></a><a name="en-us_topic_0049139665_p63624481"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.2"><p id="p95643582317"><a name="p95643582317"></a><a name="p95643582317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049139665_p23091719"><a name="en-us_topic_0049139665_p23091719"></a><a name="en-us_topic_0049139665_p23091719"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p18288175017312"><a name="p18288175017312"></a><a name="p18288175017312"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139665_row40067039"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049139665_p24204730"><a name="en-us_topic_0049139665_p24204730"></a><a name="en-us_topic_0049139665_p24204730"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049139665_p14426089"><a name="en-us_topic_0049139665_p14426089"></a><a name="en-us_topic_0049139665_p14426089"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049139665_p27662549"><a name="en-us_topic_0049139665_p27662549"></a><a name="en-us_topic_0049139665_p27662549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049139665_p26073957"><a name="en-us_topic_0049139665_p26073957"></a><a name="en-us_topic_0049139665_p26073957"></a>Specifies the health check. For details, see <a href="#table154092042172813">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **healthmonitor**  parameter description

<a name="table154092042172813"></a>
<table><thead align="left"><tr id="row46491428288"><th class="cellrowborder" valign="top" width="25.132513251325133%" id="mcps1.2.5.1.1"><p id="p964964217283"><a name="p964964217283"></a><a name="p964964217283"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.04100410041004%" id="mcps1.2.5.1.2"><p id="p264916421285"><a name="p264916421285"></a><a name="p264916421285"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.2.5.1.3"><p id="p2649124252811"><a name="p2649124252811"></a><a name="p2649124252811"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.59465946594659%" id="mcps1.2.5.1.4"><p id="p816765003219"><a name="p816765003219"></a><a name="p816765003219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4649154292819"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p064913426281"><a name="p064913426281"></a><a name="p064913426281"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p18649342142815"><a name="p18649342142815"></a><a name="p18649342142815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p564954210280"><a name="p564954210280"></a><a name="p564954210280"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p58501831291"><a name="p58501831291"></a><a name="p58501831291"></a>Specifies the ID of the project where the health check is performed.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p89192325324"><a name="p89192325324"></a><a name="p89192325324"></a>The value must be the same as the value of <strong id="b985465116161"><a name="b985465116161"></a><a name="b985465116161"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row10649742182816"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p2064915426287"><a name="p2064915426287"></a><a name="p2064915426287"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p064934217285"><a name="p064934217285"></a><a name="p064934217285"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p1164994217288"><a name="p1164994217288"></a><a name="p1164994217288"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p18649174212283"><a name="p18649174212283"></a><a name="p18649174212283"></a>Specifies the health check name.</p>
<p id="p11916318557"><a name="p11916318557"></a><a name="p11916318557"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row564910428282"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p19650124216288"><a name="p19650124216288"></a><a name="p19650124216288"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p865044232819"><a name="p865044232819"></a><a name="p865044232819"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p13650104211284"><a name="p13650104211284"></a><a name="p13650104211284"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p4650114222812"><a name="p4650114222812"></a><a name="p4650114222812"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="b12853163810179"><a name="b12853163810179"></a><a name="b12853163810179"></a>1</strong> to <strong id="b14219427175"><a name="b14219427175"></a><a name="b14219427175"></a>50</strong>.</p>
</td>
</tr>
<tr id="row156500428282"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p126504422285"><a name="p126504422285"></a><a name="p126504422285"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p1565054216286"><a name="p1565054216286"></a><a name="p1565054216286"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p83701912163318"><a name="p83701912163318"></a><a name="p83701912163318"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p21016417273"><a name="p21016417273"></a><a name="p21016417273"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="b15925730132419"><a name="b15925730132419"></a><a name="b15925730132419"></a>fail</strong> to <strong id="b2645134112412"><a name="b2645134112412"></a><a name="b2645134112412"></a>success</strong>. The value ranges from <strong id="b4547438132418"><a name="b4547438132418"></a><a name="b4547438132418"></a>1</strong> to <strong id="b12300174120248"><a name="b12300174120248"></a><a name="b12300174120248"></a>10</strong>.</p>
</td>
</tr>
<tr id="row9650184282816"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p18650154292815"><a name="p18650154292815"></a><a name="p18650154292815"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p15650184282813"><a name="p15650184282813"></a><a name="p15650184282813"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p1365015423282"><a name="p1365015423282"></a><a name="p1365015423282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p16501742122819"><a name="p16501742122819"></a><a name="p16501742122819"></a>Specifies the ID of the backend server group.</p>
<p id="p113190164112"><a name="p113190164112"></a><a name="p113190164112"></a>Only one health check can be configured for each backend server group.</p>
</td>
</tr>
<tr id="row865064210286"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p17650124215283"><a name="p17650124215283"></a><a name="p17650124215283"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p1265094216286"><a name="p1265094216286"></a><a name="p1265094216286"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p186502424284"><a name="p186502424284"></a><a name="p186502424284"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p14932133633814"><a name="p14932133633814"></a><a name="p14932133633814"></a>Specifies the administrative status of the health check.</p>
<p id="p737455383817"><a name="p737455383817"></a><a name="p737455383817"></a>The value can be <strong id="b176115149183"><a name="b176115149183"></a><a name="b176115149183"></a>true</strong> or <strong id="b476241415182"><a name="b476241415182"></a><a name="b476241415182"></a>false</strong>. The default value is <strong id="b1821331615185"><a name="b1821331615185"></a><a name="b1821331615185"></a>true</strong>.</p>
<a name="ul118694033910"></a><a name="ul118694033910"></a><ul id="ul118694033910"><li><strong id="b20950183242811"><a name="b20950183242811"></a><a name="b20950183242811"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="b7822194092817"><a name="b7822194092817"></a><a name="b7822194092817"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="row196501742172819"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p186501942192817"><a name="p186501942192817"></a><a name="p186501942192817"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p665074282815"><a name="p665074282815"></a><a name="p665074282815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p465034217288"><a name="p465034217288"></a><a name="p465034217288"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p1784571273912"><a name="p1784571273912"></a><a name="p1784571273912"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="b209591823161815"><a name="b209591823161815"></a><a name="b209591823161815"></a>1</strong> to <strong id="b1096032391812"><a name="b1096032391812"></a><a name="b1096032391812"></a>50</strong>.</p>
<div class="note" id="note187671922193912"><a name="note187671922193912"></a><a name="note187671922193912"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15769322123919"><a name="p15769322123919"></a><a name="p15769322123919"></a>You are advised to set the value less than that of parameter <strong id="b756717380188"><a name="b756717380188"></a><a name="b756717380188"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1465010429289"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p56509421283"><a name="p56509421283"></a><a name="p56509421283"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p166502042192819"><a name="p166502042192819"></a><a name="p166502042192819"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p66504426282"><a name="p66504426282"></a><a name="p66504426282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p1444014213398"><a name="p1444014213398"></a><a name="p1444014213398"></a>Specifies the health check protocol.</p>
<p id="p76509429289"><a name="p76509429289"></a><a name="p76509429289"></a>The value can be <strong id="b650145912188"><a name="b650145912188"></a><a name="b650145912188"></a>TCP</strong>, <strong id="b761518218194"><a name="b761518218194"></a><a name="b761518218194"></a>UDP_CONNECT</strong>, or <strong id="b09362053199"><a name="b09362053199"></a><a name="b09362053199"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row1765014252814"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p165018425282"><a name="p165018425282"></a><a name="p165018425282"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p1765164242812"><a name="p1765164242812"></a><a name="p1765164242812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p17651114262814"><a name="p17651114262814"></a><a name="p17651114262814"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p10119958144115"><a name="p10119958144115"></a><a name="p10119958144115"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="p1165151154216"><a name="p1165151154216"></a><a name="p1165151154216"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="row156511042142817"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p1665119429286"><a name="p1665119429286"></a><a name="p1665119429286"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p565118423287"><a name="p565118423287"></a><a name="p565118423287"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p176516429287"><a name="p176516429287"></a><a name="p176516429287"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p178364704214"><a name="p178364704214"></a><a name="p178364704214"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="p1833549104310"><a name="p1833549104310"></a><a name="p1833549104310"></a>This parameter is valid when the value of <strong id="b2052672201912"><a name="b2052672201912"></a><a name="b2052672201912"></a>type</strong> is set to <strong id="b85288226191"><a name="b85288226191"></a><a name="b85288226191"></a>HTTP</strong>.</p>
<p id="p19194239134314"><a name="p19194239134314"></a><a name="p19194239134314"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="p4782712144317"><a name="p4782712144317"></a><a name="p4782712144317"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="b04251753153515"><a name="b04251753153515"></a><a name="b04251753153515"></a>www.test.com</strong>.</p>
<p id="p193809825516"><a name="p193809825516"></a><a name="p193809825516"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="row1365164232813"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p1065144210289"><a name="p1065144210289"></a><a name="p1065144210289"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p196510429281"><a name="p196510429281"></a><a name="p196510429281"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p1565164232812"><a name="p1565164232812"></a><a name="p1565164232812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p134815784414"><a name="p134815784414"></a><a name="p134815784414"></a>Specifies the HTTP request path for the health check. The default value is <strong id="b842352706112925"><a name="b842352706112925"></a><a name="b842352706112925"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="p2026272014445"><a name="p2026272014445"></a><a name="p2026272014445"></a>This parameter is valid when the value of <strong id="b83216185474"><a name="b83216185474"></a><a name="b83216185474"></a>type</strong> is set to <strong id="b16322518174712"><a name="b16322518174712"></a><a name="b16322518174712"></a>HTTP</strong>.</p>
<p id="p108766337449"><a name="p108766337449"></a><a name="p108766337449"></a>An example value is <strong id="b2050612302214"><a name="b2050612302214"></a><a name="b2050612302214"></a>/test</strong>.</p>
<p id="p538543195510"><a name="p538543195510"></a><a name="p538543195510"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row365154210281"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p12651114217286"><a name="p12651114217286"></a><a name="p12651114217286"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p765112420286"><a name="p765112420286"></a><a name="p765112420286"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p76513422286"><a name="p76513422286"></a><a name="p76513422286"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p57098356"><a name="p57098356"></a><a name="p57098356"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="p44123159"><a name="p44123159"></a><a name="p44123159"></a>A single value, such as 200</p>
<p id="p61564112"><a name="p61564112"></a><a name="p61564112"></a>A list of values, such as 200 and 202</p>
<p id="p17206096"><a name="p17206096"></a><a name="p17206096"></a>A value range, such as 200 to 204</p>
<p id="p20637136"><a name="p20637136"></a><a name="p20637136"></a>This parameter is valid when the value of <strong id="b1478226163617"><a name="b1478226163617"></a><a name="b1478226163617"></a>type</strong> is set to <strong id="b1279182643617"><a name="b1279182643617"></a><a name="b1279182643617"></a>HTTP</strong>.</p>
<p id="p1939437165618"><a name="p1939437165618"></a><a name="p1939437165618"></a>The value contains a maximum of 64 characters.</p>
<div class="note" id="note51516497"><a name="note51516497"></a><a name="note51516497"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p60995292"><a name="p60995292"></a><a name="p60995292"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
<tr id="row116511242152817"><td class="cellrowborder" valign="top" width="25.132513251325133%" headers="mcps1.2.5.1.1 "><p id="p465120420287"><a name="p465120420287"></a><a name="p465120420287"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="10.04100410041004%" headers="mcps1.2.5.1.2 "><p id="p186521042132812"><a name="p186521042132812"></a><a name="p186521042132812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.3 "><p id="p106521542112814"><a name="p106521542112814"></a><a name="p106521542112814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.59465946594659%" headers="mcps1.2.5.1.4 "><p id="p316954715453"><a name="p316954715453"></a><a name="p316954715453"></a>Specifies the HTTP request method. The default value is <strong id="b1583571003114"><a name="b1583571003114"></a><a name="b1583571003114"></a>GET</strong>.</p>
<p id="p21871844204517"><a name="p21871844204517"></a><a name="p21871844204517"></a>The value can be <strong id="b393423343119"><a name="b393423343119"></a><a name="b393423343119"></a>GET</strong>, <strong id="b9365193753110"><a name="b9365193753110"></a><a name="b9365193753110"></a>HEAD</strong>, <strong id="b1136474012312"><a name="b1136474012312"></a><a name="b1136474012312"></a>POST</strong>, <strong id="b19183124916313"><a name="b19183124916313"></a><a name="b19183124916313"></a>PUT</strong>, <strong id="b8869354123118"><a name="b8869354123118"></a><a name="b8869354123118"></a>DELETE</strong>, <strong id="b1237215584317"><a name="b1237215584317"></a><a name="b1237215584317"></a>TRACE</strong>, <strong id="b1931013373216"><a name="b1931013373216"></a><a name="b1931013373216"></a>OPTIONS</strong>, <strong id="b896742910316"><a name="b896742910316"></a><a name="b896742910316"></a>CONNECT</strong>, and <strong id="b189921325153120"><a name="b189921325153120"></a><a name="b189921325153120"></a>PATCH</strong>.</p>
<p id="p658413198402"><a name="p658413198402"></a><a name="p658413198402"></a>This parameter is valid when the value of <strong id="b13164167473"><a name="b13164167473"></a><a name="b13164167473"></a>type</strong> is set to <strong id="b11651862473"><a name="b11651862473"></a><a name="b11651862473"></a>HTTP</strong>.</p>
<p id="p1733791718568"><a name="p1733791718568"></a><a name="p1733791718568"></a>The value contains a maximum of 16 characters.</p>
<div class="note" id="note18114145413811"><a name="note18114145413811"></a><a name="note18114145413811"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p911455418383"><a name="p911455418383"></a><a name="p911455418383"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139665_section22264835"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0049139665_table16106256"></a>
<table><thead align="left"><tr id="en-us_topic_0049139665_row50461073"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139665_p60815108"><a name="en-us_topic_0049139665_p60815108"></a><a name="en-us_topic_0049139665_p60815108"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139665_p27076724"><a name="en-us_topic_0049139665_p27076724"></a><a name="en-us_topic_0049139665_p27076724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139665_p13224809"><a name="en-us_topic_0049139665_p13224809"></a><a name="en-us_topic_0049139665_p13224809"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139665_row64576574"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139665_p63319983"><a name="en-us_topic_0049139665_p63319983"></a><a name="en-us_topic_0049139665_p63319983"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139665_p28645030"><a name="en-us_topic_0049139665_p28645030"></a><a name="en-us_topic_0049139665_p28645030"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139665_p35222847"><a name="en-us_topic_0049139665_p35222847"></a><a name="en-us_topic_0049139665_p35222847"></a>Specifies the health check. For details, see <a href="#table186706722915">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **healthmonitor**  parameter description

<a name="table186706722915"></a>
<table><thead align="left"><tr id="row19929157112914"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p59295713297"><a name="p59295713297"></a><a name="p59295713297"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p79292720293"><a name="p79292720293"></a><a name="p79292720293"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="p1258101218348"><a name="p1258101218348"></a><a name="p1258101218348"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1192911772916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p5929177112912"><a name="p5929177112912"></a><a name="p5929177112912"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p5947132518343"><a name="p5947132518343"></a><a name="p5947132518343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p109296702911"><a name="p109296702911"></a><a name="p109296702911"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="row792915762911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p59290711296"><a name="p59290711296"></a><a name="p59290711296"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1792918772913"><a name="p1792918772913"></a><a name="p1792918772913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p269292715918"><a name="p269292715918"></a><a name="p269292715918"></a>Specifies the ID of the project where the health check is performed.</p>
</td>
</tr>
<tr id="row209291674295"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p692919752912"><a name="p692919752912"></a><a name="p692919752912"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p131123323411"><a name="p131123323411"></a><a name="p131123323411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p199294713299"><a name="p199294713299"></a><a name="p199294713299"></a>Specifies the health check name.</p>
</td>
</tr>
<tr id="row5929279299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p892987162910"><a name="p892987162910"></a><a name="p892987162910"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p792918772915"><a name="p792918772915"></a><a name="p792918772915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p119293720295"><a name="p119293720295"></a><a name="p119293720295"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="b53341117227"><a name="b53341117227"></a><a name="b53341117227"></a>1</strong> to <strong id="b1233617116226"><a name="b1233617116226"></a><a name="b1233617116226"></a>50</strong>.</p>
</td>
</tr>
<tr id="row179291072296"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p15929157192911"><a name="p15929157192911"></a><a name="p15929157192911"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p178711239193411"><a name="p178711239193411"></a><a name="p178711239193411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p189309702917"><a name="p189309702917"></a><a name="p189309702917"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="b8737342112519"><a name="b8737342112519"></a><a name="b8737342112519"></a>fail</strong> to <strong id="b97392422258"><a name="b97392422258"></a><a name="b97392422258"></a>success</strong>. The value ranges from <strong id="b18741134213251"><a name="b18741134213251"></a><a name="b18741134213251"></a>1</strong> to <strong id="b18742842132513"><a name="b18742842132513"></a><a name="b18742842132513"></a>10</strong>.</p>
</td>
</tr>
<tr id="row1193097152917"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p1793016712298"><a name="p1793016712298"></a><a name="p1793016712298"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p893015710294"><a name="p893015710294"></a><a name="p893015710294"></a>Specifies the ID of the backend server group associated with the health check.</p>
</td>
</tr>
<tr id="row2930197182911"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p79301777292"><a name="p79301777292"></a><a name="p79301777292"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p293017715298"><a name="p293017715298"></a><a name="p293017715298"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p88489418492"><a name="p88489418492"></a><a name="p88489418492"></a>Specifies the administrative status of the health check.</p>
<p id="p19848040494"><a name="p19848040494"></a><a name="p19848040494"></a>The value can be <strong id="b13310921202213"><a name="b13310921202213"></a><a name="b13310921202213"></a>true</strong> or <strong id="b131282110226"><a name="b131282110226"></a><a name="b131282110226"></a>false</strong>. The default value is <strong id="b83981522142217"><a name="b83981522142217"></a><a name="b83981522142217"></a>true</strong>.</p>
<a name="ul1848244497"></a><a name="ul1848244497"></a><ul id="ul1848244497"><li><strong id="b1572441093412"><a name="b1572441093412"></a><a name="b1572441093412"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="b157791112193412"><a name="b157791112193412"></a><a name="b157791112193412"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="row09302716299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p19303782913"><a name="p19303782913"></a><a name="p19303782913"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p179315732915"><a name="p179315732915"></a><a name="p179315732915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p37112334494"><a name="p37112334494"></a><a name="p37112334494"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="b1380316275226"><a name="b1380316275226"></a><a name="b1380316275226"></a>1</strong> to <strong id="b1580411278227"><a name="b1580411278227"></a><a name="b1580411278227"></a>50</strong>.</p>
<div class="note" id="note77113384910"><a name="note77113384910"></a><a name="note77113384910"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p57123374911"><a name="p57123374911"></a><a name="p57123374911"></a>You are advised to set the value less than that of parameter <strong id="b10582112915225"><a name="b10582112915225"></a><a name="b10582112915225"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1793116752912"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p6931579296"><a name="p6931579296"></a><a name="p6931579296"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p49311173296"><a name="p49311173296"></a><a name="p49311173296"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p87193317494"><a name="p87193317494"></a><a name="p87193317494"></a>Specifies the health check protocol.</p>
<p id="p5711533184919"><a name="p5711533184919"></a><a name="p5711533184919"></a>The value can be <strong id="b9594432122210"><a name="b9594432122210"></a><a name="b9594432122210"></a>TCP</strong>, <strong id="b19595183219229"><a name="b19595183219229"></a><a name="b19595183219229"></a>UDP_CONNECT</strong>, or <strong id="b14595123282211"><a name="b14595123282211"></a><a name="b14595123282211"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row79313702914"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p29315710299"><a name="p29315710299"></a><a name="p29315710299"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1193119762917"><a name="p1193119762917"></a><a name="p1193119762917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p19915125974920"><a name="p19915125974920"></a><a name="p19915125974920"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="p1891535916496"><a name="p1891535916496"></a><a name="p1891535916496"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="row129325719290"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p4639141253611"><a name="p4639141253611"></a><a name="p4639141253611"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1263931216363"><a name="p1263931216363"></a><a name="p1263931216363"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p30010494"><a name="p30010494"></a><a name="p30010494"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="p1658995"><a name="p1658995"></a><a name="p1658995"></a>A single value, such as 200</p>
<p id="p14930959"><a name="p14930959"></a><a name="p14930959"></a>A list of values, such as 200 and 202</p>
<p id="p160907"><a name="p160907"></a><a name="p160907"></a>A value range, such as 200 to 204</p>
<p id="p1448168"><a name="p1448168"></a><a name="p1448168"></a>This parameter is valid when the value of <strong id="b6389401468"><a name="b6389401468"></a><a name="b6389401468"></a>type</strong> is set to <strong id="b113907012461"><a name="b113907012461"></a><a name="b113907012461"></a>HTTP</strong>.</p>
<p id="p13033520"><a name="p13033520"></a><a name="p13033520"></a>Currently, this parameter is not supported and is fixed at <strong id="b84235270619455"><a name="b84235270619455"></a><a name="b84235270619455"></a>200</strong>.</p>
</td>
</tr>
<tr id="row1993247182913"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p159326713290"><a name="p159326713290"></a><a name="p159326713290"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p179321712912"><a name="p179321712912"></a><a name="p179321712912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p12394754125016"><a name="p12394754125016"></a><a name="p12394754125016"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="p73941354135010"><a name="p73941354135010"></a><a name="p73941354135010"></a>This parameter is valid when the value of <strong id="b55255217488"><a name="b55255217488"></a><a name="b55255217488"></a>type</strong> is set to <strong id="b1752620264817"><a name="b1752620264817"></a><a name="b1752620264817"></a>HTTP</strong>.</p>
<p id="p14394115411501"><a name="p14394115411501"></a><a name="p14394115411501"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="p15394145435010"><a name="p15394145435010"></a><a name="p15394145435010"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="b67911125183711"><a name="b67911125183711"></a><a name="b67911125183711"></a>www.test.com</strong>.</p>
</td>
</tr>
<tr id="row593217719299"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p793277152911"><a name="p793277152911"></a><a name="p793277152911"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1593247182917"><a name="p1593247182917"></a><a name="p1593247182917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p6417986512"><a name="p6417986512"></a><a name="p6417986512"></a>Specifies the HTTP request path for the health check. The default value is <strong id="b1437591082310"><a name="b1437591082310"></a><a name="b1437591082310"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="p64181884511"><a name="p64181884511"></a><a name="p64181884511"></a>This parameter is valid when the value of <strong id="b16827165119475"><a name="b16827165119475"></a><a name="b16827165119475"></a>type</strong> is set to <strong id="b188288512479"><a name="b188288512479"></a><a name="b188288512479"></a>HTTP</strong>.</p>
<p id="p1341818185114"><a name="p1341818185114"></a><a name="p1341818185114"></a>An example value is <strong id="b20236172942318"><a name="b20236172942318"></a><a name="b20236172942318"></a>/test</strong>.</p>
</td>
</tr>
<tr id="row3932167132916"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p793218711296"><a name="p793218711296"></a><a name="p793218711296"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1893212710291"><a name="p1893212710291"></a><a name="p1893212710291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="p48511267514"><a name="p48511267514"></a><a name="p48511267514"></a>Specifies the HTTP request method. The default value is <strong id="b19886729123413"><a name="b19886729123413"></a><a name="b19886729123413"></a>GET</strong>.</p>
<p id="p11851326135110"><a name="p11851326135110"></a><a name="p11851326135110"></a>The value can be <strong id="b205241432133411"><a name="b205241432133411"></a><a name="b205241432133411"></a>GET</strong>, <strong id="b1524432123415"><a name="b1524432123415"></a><a name="b1524432123415"></a>HEAD</strong>, <strong id="b1452533293413"><a name="b1452533293413"></a><a name="b1452533293413"></a>POST</strong>, <strong id="b12525832163420"><a name="b12525832163420"></a><a name="b12525832163420"></a>PUT</strong>, <strong id="b452653210347"><a name="b452653210347"></a><a name="b452653210347"></a>DELETE</strong>, <strong id="b2052773214341"><a name="b2052773214341"></a><a name="b2052773214341"></a>TRACE</strong>, <strong id="b152812324344"><a name="b152812324344"></a><a name="b152812324344"></a>OPTIONS</strong>, <strong id="b75281932203417"><a name="b75281932203417"></a><a name="b75281932203417"></a>CONNECT</strong>, and <strong id="b7529193220347"><a name="b7529193220347"></a><a name="b7529193220347"></a>PATCH</strong>.</p>
<p id="p485142665115"><a name="p485142665115"></a><a name="p485142665115"></a>This parameter is valid when the value of <strong id="b782231144617"><a name="b782231144617"></a><a name="b782231144617"></a>type</strong> is set to <strong id="b178221611124616"><a name="b178221611124616"></a><a name="b178221611124616"></a>HTTP</strong>.</p>
<div class="note" id="note985119267515"><a name="note985119267515"></a><a name="note985119267515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1885112263511"><a name="p1885112263511"></a><a name="p1885112263511"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1510443118364"></a>

-   Example request: Configuring a health check

    ```
    POST https://{Endpoint}/v2.0/lbaas/healthmonitors
    
    {
      "healthmonitor": {
        "admin_state_up": true,
        "pool_id": "bb44bffb-05d9-412c-9d9c-b189d9e14193",
        "domain_name": "www.test.com",
        "delay": 10,
        "max_retries": 10,
       
        "timeout": 10,
        "type": "HTTP"
      }
    }
    ```

-   Example response

    ```
    {
      "healthmonitor": {
        "name": "",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
        "domain_name": "www.test.com",
        "delay": 10,
        "max_retries": 10,
        "expected_codes": "200", 
        
        "http_method": "GET",
        "timeout": 10,
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

