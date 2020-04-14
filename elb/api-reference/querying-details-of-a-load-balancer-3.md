# Querying Details of a Load Balancer<a name="EN-US_TOPIC_0141008271"></a>

## Function<a name="en-us_topic_0096561532_en-us_topic_0049139632_section28798367"></a>

This API is used to query details about a load balancer using its ID.

## URI<a name="en-us_topic_0096561532_en-us_topic_0049139632_section57858711"></a>

GET /v2.0/lbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0096561532_table8859516183710"></a>
<table><thead align="left"><tr id="en-us_topic_0096561532_row1189415166379"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561532_p148945161379"><a name="en-us_topic_0096561532_p148945161379"></a><a name="en-us_topic_0096561532_p148945161379"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561532_p98941716113710"><a name="en-us_topic_0096561532_p98941716113710"></a><a name="en-us_topic_0096561532_p98941716113710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561532_p16894816103712"><a name="en-us_topic_0096561532_p16894816103712"></a><a name="en-us_topic_0096561532_p16894816103712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.396039603960396%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561532_p16894816113718"><a name="en-us_topic_0096561532_p16894816113718"></a><a name="en-us_topic_0096561532_p16894816113718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561532_row1089431611376"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561532_p989461633718"><a name="en-us_topic_0096561532_p989461633718"></a><a name="en-us_topic_0096561532_p989461633718"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561532_p1889491623711"><a name="en-us_topic_0096561532_p1889491623711"></a><a name="en-us_topic_0096561532_p1889491623711"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p1758012345108"><a name="p1758012345108"></a><a name="p1758012345108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561532_p1789471633719"><a name="en-us_topic_0096561532_p1789471633719"></a><a name="en-us_topic_0096561532_p1789471633719"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096561532_section162332597302"></a>

None

## Response<a name="en-us_topic_0096561532_section768911717356"></a>

**Table  2**  Parameter description

<a name="en-us_topic_0096561532_table13388456357"></a>
<table><thead align="left"><tr id="en-us_topic_0096561532_row74113459355"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561532_p1542104583513"><a name="en-us_topic_0096561532_p1542104583513"></a><a name="en-us_topic_0096561532_p1542104583513"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561532_p14431045113513"><a name="en-us_topic_0096561532_p14431045113513"></a><a name="en-us_topic_0096561532_p14431045113513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561532_p2464452354"><a name="en-us_topic_0096561532_p2464452354"></a><a name="en-us_topic_0096561532_p2464452354"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561532_row24634511356"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561532_p64704515357"><a name="en-us_topic_0096561532_p64704515357"></a><a name="en-us_topic_0096561532_p64704515357"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561532_p1648184512359"><a name="en-us_topic_0096561532_p1648184512359"></a><a name="en-us_topic_0096561532_p1648184512359"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561532_p1949145143520"><a name="en-us_topic_0096561532_p1949145143520"></a><a name="en-us_topic_0096561532_p1949145143520"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561532_table1943718352380">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **loadbalancer**  parameter description

<a name="en-us_topic_0096561532_table1943718352380"></a>
<table><thead align="left"><tr id="en-us_topic_0096561532_row6659133533816"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561532_p96591835173819"><a name="en-us_topic_0096561532_p96591835173819"></a><a name="en-us_topic_0096561532_p96591835173819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561532_p17660123513386"><a name="en-us_topic_0096561532_p17660123513386"></a><a name="en-us_topic_0096561532_p17660123513386"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561532_p4660183515387"><a name="en-us_topic_0096561532_p4660183515387"></a><a name="en-us_topic_0096561532_p4660183515387"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561532_row156601235133818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p10415829113311"><a name="en-us_topic_0096561531_p10415829113311"></a><a name="en-us_topic_0096561531_p10415829113311"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p155784252919"><a name="p155784252919"></a><a name="p155784252919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1941513297339"><a name="en-us_topic_0096561531_p1941513297339"></a><a name="en-us_topic_0096561531_p1941513297339"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="row1758616126181"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p20415229113312"><a name="en-us_topic_0096561531_p20415229113312"></a><a name="en-us_topic_0096561531_p20415229113312"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p741592933318"><a name="en-us_topic_0096561531_p741592933318"></a><a name="en-us_topic_0096561531_p741592933318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1341519295331"><a name="en-us_topic_0096561531_p1341519295331"></a><a name="en-us_topic_0096561531_p1341519295331"></a>Specifies the ID of the project where the load balancer is used.</p>
<p id="p77281547155311"><a name="p77281547155311"></a><a name="p77281547155311"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row76601535193815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1041552912332"><a name="en-us_topic_0096561531_p1041552912332"></a><a name="en-us_topic_0096561531_p1041552912332"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p241692918331"><a name="en-us_topic_0096561531_p241692918331"></a><a name="en-us_topic_0096561531_p241692918331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p17416152919332"><a name="en-us_topic_0096561531_p17416152919332"></a><a name="en-us_topic_0096561531_p17416152919332"></a>Specifies the load balancer name.</p>
<p id="p076212535532"><a name="p076212535532"></a><a name="p076212535532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row66605355385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p4416102918335"><a name="en-us_topic_0096561531_p4416102918335"></a><a name="en-us_topic_0096561531_p4416102918335"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p24161129143314"><a name="en-us_topic_0096561531_p24161129143314"></a><a name="en-us_topic_0096561531_p24161129143314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p5416142912334"><a name="en-us_topic_0096561531_p5416142912334"></a><a name="en-us_topic_0096561531_p5416142912334"></a>Provides supplementary information about the load balancer.</p>
<p id="p157105551532"><a name="p157105551532"></a><a name="p157105551532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row1166020352385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1541618299335"><a name="en-us_topic_0096561531_p1541618299335"></a><a name="en-us_topic_0096561531_p1541618299335"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p135272044182910"><a name="p135272044182910"></a><a name="p135272044182910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p4335125124117"><a name="p4335125124117"></a><a name="p4335125124117"></a>Specifies the ID of the subnet where the load balancer works.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row36601435103818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1041622923320"><a name="en-us_topic_0096561531_p1041622923320"></a><a name="en-us_topic_0096561531_p1041622923320"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19102164614291"><a name="p19102164614291"></a><a name="p19102164614291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p173334177415"><a name="p173334177415"></a><a name="p173334177415"></a>Specifies the ID of the port bound to the private IP address of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row1866173519389"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p174164295334"><a name="en-us_topic_0096561531_p174164295334"></a><a name="en-us_topic_0096561531_p174164295334"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p541611290339"><a name="en-us_topic_0096561531_p541611290339"></a><a name="en-us_topic_0096561531_p541611290339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p43391417194120"><a name="p43391417194120"></a><a name="p43391417194120"></a>Specifies the provider of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row6661203510387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1416829143318"><a name="en-us_topic_0096561531_p1416829143318"></a><a name="en-us_topic_0096561531_p1416829143318"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p341672912338"><a name="en-us_topic_0096561531_p341672912338"></a><a name="en-us_topic_0096561531_p341672912338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p64178297334"><a name="en-us_topic_0096561531_p64178297334"></a><a name="en-us_topic_0096561531_p64178297334"></a>Specifies the private IP address of the load balancer.</p>
<p id="p832917316544"><a name="p832917316544"></a><a name="p832917316544"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row16611235163814"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1841715293336"><a name="en-us_topic_0096561531_p1841715293336"></a><a name="en-us_topic_0096561531_p1841715293336"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p10662124818106"><a name="p10662124818106"></a><a name="p10662124818106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p7417112963311"><a name="en-us_topic_0096561531_p7417112963311"></a><a name="en-us_topic_0096561531_p7417112963311"></a>Lists the IDs of listeners added to the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row8661143513384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1441712910330"><a name="en-us_topic_0096561531_p1441712910330"></a><a name="en-us_topic_0096561531_p1441712910330"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p563318509102"><a name="p563318509102"></a><a name="p563318509102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p104171229123313"><a name="en-us_topic_0096561531_p104171229123313"></a><a name="en-us_topic_0096561531_p104171229123313"></a>Lists the IDs of backend server groups associated with the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row566114352387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p727217358477"><a name="p727217358477"></a><a name="p727217358477"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p82761735124717"><a name="p82761735124717"></a><a name="p82761735124717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p9800291619"><a name="p9800291619"></a><a name="p9800291619"></a>Specifies the operating status of the load balancer.</p>
<p id="p75131031164"><a name="p75131031164"></a><a name="p75131031164"></a>The value can be <strong id="b842352706165847"><a name="b842352706165847"></a><a name="b842352706165847"></a>ONLINE</strong>, <strong id="b842352706165850"><a name="b842352706165850"></a><a name="b842352706165850"></a>OFFLINE</strong>, <strong id="b842352706165852"><a name="b842352706165852"></a><a name="b842352706165852"></a>DEGRADED</strong>, <strong id="b842352706165855"><a name="b842352706165855"></a><a name="b842352706165855"></a>DISABLED</strong>, or <strong id="b842352706165859"><a name="b842352706165859"></a><a name="b842352706165859"></a>NO_MONITOR</strong>.</p>
<p id="p58611733561"><a name="p58611733561"></a><a name="p58611733561"></a>This parameter is reserved. The default value is <strong id="b842352706145855"><a name="b842352706145855"></a><a name="b842352706145855"></a>ONLINE</strong>.</p>
<p id="p71718156545"><a name="p71718156545"></a><a name="p71718156545"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row2661123514384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p930113351475"><a name="p930113351475"></a><a name="p930113351475"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p7305153534717"><a name="p7305153534717"></a><a name="p7305153534717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p4255836060"><a name="p4255836060"></a><a name="p4255836060"></a>Specifies the provisioning status of the load balancer.</p>
<p id="p9469138261"><a name="p9469138261"></a><a name="p9469138261"></a>The value can be <strong id="b842352706165943"><a name="b842352706165943"></a><a name="b842352706165943"></a>ACTIVE</strong>, <strong id="b842352706165947"><a name="b842352706165947"></a><a name="b842352706165947"></a>PENDING_CREATE</strong>, or <strong id="b842352706165951"><a name="b842352706165951"></a><a name="b842352706165951"></a>ERROR</strong>.</p>
<p id="p15614144018617"><a name="p15614144018617"></a><a name="p15614144018617"></a>This parameter is reserved. The default value is <strong id="b1402670288"><a name="b1402670288"></a><a name="b1402670288"></a>ACTIVE</strong>.</p>
<p id="p18722348205910"><a name="p18722348205910"></a><a name="p18722348205910"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row16662935103816"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p114181329133314"><a name="en-us_topic_0096561531_p114181329133314"></a><a name="en-us_topic_0096561531_p114181329133314"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p10418172913319"><a name="en-us_topic_0096561531_p10418172913319"></a><a name="en-us_topic_0096561531_p10418172913319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p14847443611"><a name="p14847443611"></a><a name="p14847443611"></a>Specifies the administrative status of the load balancer.</p>
<p id="p114911046864"><a name="p114911046864"></a><a name="p114911046864"></a>This parameter is reserved. The default value is <strong id="b1291373994"><a name="b1291373994"></a><a name="b1291373994"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row866215358384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p74181229133310"><a name="en-us_topic_0096561531_p74181229133310"></a><a name="en-us_topic_0096561531_p74181229133310"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p71551954161018"><a name="p71551954161018"></a><a name="p71551954161018"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p4418112919333"><a name="en-us_topic_0096561531_p4418112919333"></a><a name="en-us_topic_0096561531_p4418112919333"></a>Lists load balancer tags.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row13900164817511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p18781627124910"><a name="en-us_topic_0096561531_p18781627124910"></a><a name="en-us_topic_0096561531_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p18781627204916"><a name="en-us_topic_0096561531_p18781627204916"></a><a name="en-us_topic_0096561531_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p578162719490"><a name="en-us_topic_0096561531_p578162719490"></a><a name="en-us_topic_0096561531_p578162719490"></a>Specifies the time when the load balancer was created.</p>
<p id="p3462240292"><a name="p3462240292"></a><a name="p3462240292"></a>The UTC time is in <em id="i155506367247"><a name="i155506367247"></a><a name="i155506367247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p415795413546"><a name="p415795413546"></a><a name="p415795413546"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561532_row4521952195114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1541843114495"><a name="en-us_topic_0096561531_p1541843114495"></a><a name="en-us_topic_0096561531_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p1810172112506"><a name="en-us_topic_0096561531_p1810172112506"></a><a name="en-us_topic_0096561531_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p341843144919"><a name="en-us_topic_0096561531_p341843144919"></a><a name="en-us_topic_0096561531_p341843144919"></a>Specifies the time when the load balancer was updated.</p>
<p id="p52901417154816"><a name="p52901417154816"></a><a name="p52901417154816"></a>The UTC time is in <em id="i185028407247"><a name="i185028407247"></a><a name="i185028407247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p3844185817544"><a name="p3844185817544"></a><a name="p3844185817544"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1737103643915"></a>

-   Example request: Querying details of a load balancer using its ID

    ```
    GET https://{Endpoint}/v2.0/lbaas/loadbalancers/3d77894d-2ffe-4411-ac0a-0d57689779b8
    ```


-   Example response

    ```
    {
        "loadbalancer": {
            "description": "",
            "admin_state_up": true,
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
      
            "provisioning_status": "ACTIVE",
            "vip_subnet_id": "4f5e8efe-fbbe-405e-b48c-a41202ef697c",
            "listeners": [
                {
                    "id": "09e64049-2ab0-4763-a8c5-f4207875dc3e"
                }
            ],
            "vip_address": "192.168.2.4",
            "vip_port_id": "c7157e7a-036a-42ca-8474-100be22e3727",
            "provider": "vlb",
            "pools": [
                {
                    "id": "b7e53dbd-62ab-4505-a280-5c066078a5c9"
                }
            ],
            "id": "3d77894d-2ffe-4411-ac0a-0d57689779b8",
            "operating_status": "ONLINE",
            "tags": [],
            "name": "lb-2",
            "created_at": "2018-07-25T01:54:13", 
            "updated_at": "2018-07-25T01:54:14"
        }
    }
    ```


## Status Code<a name="en-us_topic_0096561532_en-us_topic_0049139632_section15511864"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

