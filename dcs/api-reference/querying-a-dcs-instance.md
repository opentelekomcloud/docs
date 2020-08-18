# Querying a DCS Instance<a name="dcs-api-0312005"></a>

## Function<a name="section159181355213"></a>

This API is used to query the details about a specified DCS instance.

## URI<a name="section1522918159341"></a>

GET /v1.0/\{project\_id\}/instances/\{instance\_id\}

[Table 1](#table374812348341)  describes the parameters.

**Table  1**  Parameter description

<a name="table374812348341"></a>
<table><thead align="left"><tr id="row474713417340"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p6747173433414"><a name="p6747173433414"></a><a name="p6747173433414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p274718343343"><a name="p274718343343"></a><a name="p274718343343"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p19747183419347"><a name="p19747183419347"></a><a name="p19747183419347"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1674783493418"><a name="p1674783493418"></a><a name="p1674783493418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27471534143414"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p147471934113411"><a name="p147471934113411"></a><a name="p147471934113411"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p074763423420"><a name="p074763423420"></a><a name="p074763423420"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p67471934133414"><a name="p67471934133414"></a><a name="p67471934133414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p9747934143417"><a name="p9747934143417"></a><a name="p9747934143417"></a>For details on how to obtain the value of this parameter, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row97485345347"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6747734133415"><a name="p6747734133415"></a><a name="p6747734133415"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2074783418343"><a name="p2074783418343"></a><a name="p2074783418343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p37471234153412"><a name="p37471234153412"></a><a name="p37471234153412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p97482340341"><a name="p97482340341"></a><a name="p97482340341"></a>ID of the instance to be queried</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section229211578341"></a>

**Request parameters**

None.

**Example request**

Request URL:

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}
```

## Response<a name="section9961121793517"></a>

**Response parameters**

[Table 2](#table1257921310816)  describes the response parameters.

**Table  2**  Parameter description

<a name="table1257921310816"></a>
<table><thead align="left"><tr id="row1257912134819"><th class="cellrowborder" valign="top" width="22.484848484848484%" id="mcps1.2.4.1.1"><p id="p145791113689"><a name="p145791113689"></a><a name="p145791113689"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.080808080808083%" id="mcps1.2.4.1.2"><p id="p95791013283"><a name="p95791013283"></a><a name="p95791013283"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.43434343434344%" id="mcps1.2.4.1.3"><p id="p105797137811"><a name="p105797137811"></a><a name="p105797137811"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row454214964417"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p96664013456"><a name="p96664013456"></a><a name="p96664013456"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1866616064514"><a name="p1866616064514"></a><a name="p1866616064514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p146661905459"><a name="p146661905459"></a><a name="p146661905459"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row16661191012456"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p31401820194511"><a name="p31401820194511"></a><a name="p31401820194511"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p14140120144512"><a name="p14140120144512"></a><a name="p14140120144512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p2140720144511"><a name="p2140720144511"></a><a name="p2140720144511"></a>DCS instance engine.</p>
</td>
</tr>
<tr id="row515034414458"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p4738115815451"><a name="p4738115815451"></a><a name="p4738115815451"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p2083117322329"><a name="p2083117322329"></a><a name="p2083117322329"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p1973914586454"><a name="p1973914586454"></a><a name="p1973914586454"></a>DCS instance cache capacity. Unit: GB.</p>
</td>
</tr>
<tr id="row1319329466"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1492572218460"><a name="p1492572218460"></a><a name="p1492572218460"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p492517223465"><a name="p492517223465"></a><a name="p492517223465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p489187165218"><a name="p489187165218"></a><a name="p489187165218"></a>IP address for connecting to the DCS instance For a cluster instance, multiple IP addresses are returned and separated by commas (,). For example, 192.168.0.1,192.168.0.2.</p>
</td>
</tr>
<tr id="row12545654103410"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p18925182216466"><a name="p18925182216466"></a><a name="p18925182216466"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p20925522184612"><a name="p20925522184612"></a><a name="p20925522184612"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p17925522144612"><a name="p17925522144612"></a><a name="p17925522144612"></a>Port number of the cache node.</p>
</td>
</tr>
<tr id="row11545854183410"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p105235444610"><a name="p105235444610"></a><a name="p105235444610"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p8521754104614"><a name="p8521754104614"></a><a name="p8521754104614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p7521754164619"><a name="p7521754164619"></a><a name="p7521754164619"></a>Cache instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row1960517295472"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p16216144064712"><a name="p16216144064712"></a><a name="p16216144064712"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p121634094714"><a name="p121634094714"></a><a name="p121634094714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p221612408473"><a name="p221612408473"></a><a name="p221612408473"></a>Brief description of the DCS instance.</p>
</td>
</tr>
<tr id="row20965121211366"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p3583191317818"><a name="p3583191317818"></a><a name="p3583191317818"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p35844135810"><a name="p35844135810"></a><a name="p35844135810"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p43202563142827"><a name="p43202563142827"></a><a name="p43202563142827"></a>Total memory size.</p>
<p id="p56041229105916"><a name="p56041229105916"></a><a name="p56041229105916"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row59651212143618"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1258418132082"><a name="p1258418132082"></a><a name="p1258418132082"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p2584613482"><a name="p2584613482"></a><a name="p2584613482"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p64428528142829"><a name="p64428528142829"></a><a name="p64428528142829"></a>Size of the used memory.</p>
<p id="p19605229135918"><a name="p19605229135918"></a><a name="p19605229135918"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row2057920131686"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p757915131680"><a name="p757915131680"></a><a name="p757915131680"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p165796132817"><a name="p165796132817"></a><a name="p165796132817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p2057913134814"><a name="p2057913134814"></a><a name="p2057913134814"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row357971310814"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1945118112497"><a name="p1945118112497"></a><a name="p1945118112497"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p19451191111493"><a name="p19451191111493"></a><a name="p19451191111493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p154521311174912"><a name="p154521311174912"></a><a name="p154521311174912"></a>Resource specifications.</p>
<a name="ul15897813419"></a><a name="ul15897813419"></a><ul id="ul15897813419"><li><strong id="b3157833622"><a name="b3157833622"></a><a name="b3157833622"></a>dcs.single_node</strong>: indicates a DCS instance in single-node mode.</li><li><strong id="b13392536624"><a name="b13392536624"></a><a name="b13392536624"></a>dcs.master_standby</strong>: indicates a DCS instance in master/standby mode.</li><li><strong id="b71349391523"><a name="b71349391523"></a><a name="b71349391523"></a>dcs.cluster</strong>: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row135804131482"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p3953113011492"><a name="p3953113011492"></a><a name="p3953113011492"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p149531930194915"><a name="p149531930194915"></a><a name="p149531930194915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p1695333094918"><a name="p1695333094918"></a><a name="p1695333094918"></a>Cache engine version.</p>
</td>
</tr>
<tr id="row19580101316810"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1895313303498"><a name="p1895313303498"></a><a name="p1895313303498"></a>internal_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1595373054910"><a name="p1595373054910"></a><a name="p1595373054910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p10954183034917"><a name="p10954183034917"></a><a name="p10954183034917"></a>Internal DCS version.</p>
</td>
</tr>
<tr id="row165801713282"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p69547300496"><a name="p69547300496"></a><a name="p69547300496"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p17954173012494"><a name="p17954173012494"></a><a name="p17954173012494"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p39546309494"><a name="p39546309494"></a><a name="p39546309494"></a>Billing mode. <strong id="b1693649608141417"><a name="b1693649608141417"></a><a name="b1693649608141417"></a>0</strong>: pay-per-use.</p>
</td>
</tr>
<tr id="row2058020131089"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p152971744104917"><a name="p152971744104917"></a><a name="p152971744104917"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1129874410491"><a name="p1129874410491"></a><a name="p1129874410491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p629894418498"><a name="p629894418498"></a><a name="p629894418498"></a>VPC ID.</p>
</td>
</tr>
<tr id="row1758171317816"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p172982440497"><a name="p172982440497"></a><a name="p172982440497"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p229864413499"><a name="p229864413499"></a><a name="p229864413499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p19299344184918"><a name="p19299344184918"></a><a name="p19299344184918"></a>VPC name.</p>
</td>
</tr>
<tr id="row88105517491"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1549357195017"><a name="p1549357195017"></a><a name="p1549357195017"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p949414713501"><a name="p949414713501"></a><a name="p949414713501"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p5420602914282"><a name="p5420602914282"></a><a name="p5420602914282"></a>Time at which the DCS instance is created.</p>
<p id="p46051629195914"><a name="p46051629195914"></a><a name="p46051629195914"></a>For example, 2017-03-31<strong id="b84850841164"><a name="b84850841164"></a><a name="b84850841164"></a>T</strong>12:24:46.297<strong id="b92569001164"><a name="b92569001164"></a><a name="b92569001164"></a>Z</strong>.</p>
</td>
</tr>
<tr id="row557215250506"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p879125715508"><a name="p879125715508"></a><a name="p879125715508"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1379105735016"><a name="p1379105735016"></a><a name="p1379105735016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p37271648142755"><a name="p37271648142755"></a><a name="p37271648142755"></a>Error code returned when the DCS instance fails to be created or is in abnormal status.</p>
<p id="p1605182919594"><a name="p1605182919594"></a><a name="p1605182919594"></a>For details about error codes, see <a href="#table691509456">Table 3</a>.</p>
</td>
</tr>
<tr id="row327374913711"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p45920101386"><a name="p45920101386"></a><a name="p45920101386"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p115913108389"><a name="p115913108389"></a><a name="p115913108389"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p35931013389"><a name="p35931013389"></a><a name="p35931013389"></a>User ID.</p>
</td>
</tr>
<tr id="row32741349183713"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p612717160389"><a name="p612717160389"></a><a name="p612717160389"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p191275169385"><a name="p191275169385"></a><a name="p191275169385"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p1412731683814"><a name="p1412731683814"></a><a name="p1412731683814"></a>Username.</p>
</td>
</tr>
<tr id="row67495272384"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p13545101053910"><a name="p13545101053910"></a><a name="p13545101053910"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p354520108395"><a name="p354520108395"></a><a name="p354520108395"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p28444466142849"><a name="p28444466142849"></a><a name="p28444466142849"></a>Time at which the maintenance time window starts.</p>
<p id="p4605182945911"><a name="p4605182945911"></a><a name="p4605182945911"></a>Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row107502272383"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p654621033913"><a name="p654621033913"></a><a name="p654621033913"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p125461810203910"><a name="p125461810203910"></a><a name="p125461810203910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p66913287142854"><a name="p66913287142854"></a><a name="p66913287142854"></a>Time at which the maintenance time window ends.</p>
<p id="p760542917593"><a name="p760542917593"></a><a name="p760542917593"></a>Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row2123192024114"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p4583181319816"><a name="p4583181319816"></a><a name="p4583181319816"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1583161314820"><a name="p1583161314820"></a><a name="p1583161314820"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p11583161312820"><a name="p11583161312820"></a><a name="p11583161312820"></a>AZ where a cache node resides. The value of this parameter in the response contains an AZ ID.</p>
</td>
</tr>
<tr id="row312317204414"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p205821013680"><a name="p205821013680"></a><a name="p205821013680"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p135827139811"><a name="p135827139811"></a><a name="p135827139811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p358212136818"><a name="p358212136818"></a><a name="p358212136818"></a>Subnet ID.</p>
</td>
</tr>
<tr id="row1912472014414"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p2582913185"><a name="p2582913185"></a><a name="p2582913185"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p185823135811"><a name="p185823135811"></a><a name="p185823135811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p35821513888"><a name="p35821513888"></a><a name="p35821513888"></a>Security group ID.</p>
</td>
</tr>
<tr id="row1612492064110"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p694551810489"><a name="p694551810489"></a><a name="p694551810489"></a>backend_addrs</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p199451518134816"><a name="p199451518134816"></a><a name="p199451518134816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p15945201816484"><a name="p15945201816484"></a><a name="p15945201816484"></a>Backend address of a cluster instance.</p>
</td>
</tr>
<tr id="row135816131388"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p958121319811"><a name="p958121319811"></a><a name="p958121319811"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p358111310810"><a name="p358111310810"></a><a name="p358111310810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p1758114130820"><a name="p1758114130820"></a><a name="p1758114130820"></a>Product ID.</p>
</td>
</tr>
<tr id="row55821713384"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p11582151310813"><a name="p11582151310813"></a><a name="p11582151310813"></a>security_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p25821513486"><a name="p25821513486"></a><a name="p25821513486"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p1458214131886"><a name="p1458214131886"></a><a name="p1458214131886"></a>Security group name.</p>
</td>
</tr>
<tr id="row1758218135812"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p165829131586"><a name="p165829131586"></a><a name="p165829131586"></a>subnet_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p458215131587"><a name="p458215131587"></a><a name="p458215131587"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p175823131280"><a name="p175823131280"></a><a name="p175823131280"></a>Subnet name.</p>
</td>
</tr>
<tr id="row206871758182115"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p170935112019"><a name="p170935112019"></a><a name="p170935112019"></a>subnet_cidr</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1070915513017"><a name="p1070915513017"></a><a name="p1070915513017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p37106513011"><a name="p37106513011"></a><a name="p37106513011"></a>Subnet segment.</p>
</td>
</tr>
<tr id="row11582513288"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p1189611221388"><a name="p1189611221388"></a><a name="p1189611221388"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p6896102212381"><a name="p6896102212381"></a><a name="p6896102212381"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p16896162233813"><a name="p16896162233813"></a><a name="p16896162233813"></a>Order ID.</p>
</td>
</tr>
<tr id="row1374145316544"><td class="cellrowborder" valign="top" width="22.484848484848484%" headers="mcps1.2.4.1.1 "><p id="p10126119554"><a name="p10126119554"></a><a name="p10126119554"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.080808080808083%" headers="mcps1.2.4.1.2 "><p id="p1612517556"><a name="p1612517556"></a><a name="p1612517556"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="57.43434343434344%" headers="mcps1.2.4.1.3 "><p id="p22014154142838"><a name="p22014154142838"></a><a name="p22014154142838"></a>Backup policy.</p>
<p id="p160592914596"><a name="p160592914596"></a><a name="p160592914596"></a>This parameter is available for master/standby and cluster DCS instances. For details, see <a href="creating-a-dcs-instance.md#table12803218151513">Table 3</a> and <a href="creating-a-dcs-instance.md#table187492037201518">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error codes

<a name="table691509456"></a>
<table><thead align="left"><tr id="row0913014455"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p169303452"><a name="p169303452"></a><a name="p169303452"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p99140174518"><a name="p99140174518"></a><a name="p99140174518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21851341115313"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p161877413539"><a name="p161877413539"></a><a name="p161877413539"></a>dcs.00.0007</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p118718411533"><a name="p118718411533"></a><a name="p118718411533"></a>System error.</p>
</td>
</tr>
<tr id="row149709458"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p390763445011"><a name="p390763445011"></a><a name="p390763445011"></a>dcs.01.0001</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p139071834135011"><a name="p139071834135011"></a><a name="p139071834135011"></a>Internal service error.</p>
</td>
</tr>
<tr id="row164910416477"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p15907133412502"><a name="p15907133412502"></a><a name="p15907133412502"></a>dcs.01.0002</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p11908134125018"><a name="p11908134125018"></a><a name="p11908134125018"></a>Internal service error.</p>
</td>
</tr>
<tr id="row981115404719"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p17908153445010"><a name="p17908153445010"></a><a name="p17908153445010"></a>dcs.01.0003</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p79084346504"><a name="p79084346504"></a><a name="p79084346504"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1897714411473"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p990893416502"><a name="p990893416502"></a><a name="p990893416502"></a>dcs.02.0001</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1890816346503"><a name="p1890816346503"></a><a name="p1890816346503"></a>Failed to create VPC.</p>
</td>
</tr>
<tr id="row1214214515473"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1590853416508"><a name="p1590853416508"></a><a name="p1590853416508"></a>dcs.02.0002</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p590893412506"><a name="p590893412506"></a><a name="p590893412506"></a>Failed to create VPC.</p>
</td>
</tr>
<tr id="row1131318513473"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1090814349506"><a name="p1090814349506"></a><a name="p1090814349506"></a>dcs.02.0003</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p99081534115013"><a name="p99081534115013"></a><a name="p99081534115013"></a>Failed to create security group.</p>
</td>
</tr>
<tr id="row1992012455"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1490812340507"><a name="p1490812340507"></a><a name="p1490812340507"></a>dcs.02.0004</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p149089342500"><a name="p149089342500"></a><a name="p149089342500"></a>Failed to create subnet.</p>
</td>
</tr>
<tr id="row191806453"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p490813495019"><a name="p490813495019"></a><a name="p490813495019"></a>dcs.02.0005</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1790818341509"><a name="p1790818341509"></a><a name="p1790818341509"></a>Subnet status abnormal.</p>
</td>
</tr>
<tr id="row11461444174613"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1690820349503"><a name="p1690820349503"></a><a name="p1690820349503"></a>dcs.03.0001</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p4908434165019"><a name="p4908434165019"></a><a name="p4908434165019"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row76851748124616"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p790823410504"><a name="p790823410504"></a><a name="p790823410504"></a>dcs.03.0002</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p890873415012"><a name="p890873415012"></a><a name="p890873415012"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row1758749124615"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p139081334165018"><a name="p139081334165018"></a><a name="p139081334165018"></a>dcs.03.0003</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p4908534155013"><a name="p4908534155013"></a><a name="p4908534155013"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row1424814974616"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p16908103413502"><a name="p16908103413502"></a><a name="p16908103413502"></a>dcs.03.0004</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p490813346506"><a name="p490813346506"></a><a name="p490813346506"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row19419164984618"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2908173417504"><a name="p2908173417504"></a><a name="p2908173417504"></a>dcs.03.0005</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1909123416501"><a name="p1909123416501"></a><a name="p1909123416501"></a>Failed to bind NIC to the ECS.</p>
</td>
</tr>
<tr id="row559264954617"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p17909183445014"><a name="p17909183445014"></a><a name="p17909183445014"></a>dcs.03.0007</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1590973419501"><a name="p1590973419501"></a><a name="p1590973419501"></a>Failed to start ECS.</p>
</td>
</tr>
<tr id="row574814912467"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p7909334115018"><a name="p7909334115018"></a><a name="p7909334115018"></a>dcs.03.0008</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1390919345503"><a name="p1390919345503"></a><a name="p1390919345503"></a>Failed to start ECS.</p>
</td>
</tr>
<tr id="row19897249144616"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p5909234205013"><a name="p5909234205013"></a><a name="p5909234205013"></a>dcs.03.0009</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p14909434205016"><a name="p14909434205016"></a><a name="p14909434205016"></a>Failed to stop ECS.</p>
</td>
</tr>
<tr id="row7707105616595"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p76511659018"><a name="p76511659018"></a><a name="p76511659018"></a>dcs.03.0017</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p765110512013"><a name="p765110512013"></a><a name="p765110512013"></a>Some nodes of the instance are faulty.</p>
</td>
</tr>
<tr id="row1258125064618"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2909153495010"><a name="p2909153495010"></a><a name="p2909153495010"></a>dcs.04.0002</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2090917345501"><a name="p2090917345501"></a><a name="p2090917345501"></a>Failed to deploy the instance.</p>
</td>
</tr>
<tr id="row1337510501466"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2090916347503"><a name="p2090916347503"></a><a name="p2090916347503"></a>dcs.04.0003</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p13909163414502"><a name="p13909163414502"></a><a name="p13909163414502"></a>Failed to connect to the instance.</p>
</td>
</tr>
<tr id="row14539155011464"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p10909734195012"><a name="p10909734195012"></a><a name="p10909734195012"></a>dcs.04.0004</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p4909123435016"><a name="p4909123435016"></a><a name="p4909123435016"></a>Both cache nodes are in the master state. A network connection error may occur between the master and standby nodes.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "name" : "dcs-a11e",
    "engine" : "Redis",
    "capacity" : 2,
    "ip" : "192.168.3.100",
    "port" : 6379,
    "status" : "RUNNING",
    "description" : "Create a instance",
    "instance_id" : "68d5745e-6af2-40e4-945d-fe449be00148",
    "resource_spec_code" : "dcs.single_node",
    "engine_version" : "3.0",
    "internal_version" : null,
    "charging_mode" : 0,
    "vpc_id" : "27d99e17-42f2-4751-818f-5c8c6c03ff15",
    "vpc_name" : "vpc_4944a40e-ac57-4f08-9d38-9786e2759458_192",
    "created_at" : "2017-03-31T12:24:46.297Z",
    "error_code" : null,
    "product_id" : "XXXXXX",
    "security_group_id" : "60ea2db8-1a51-4ab6-9e11-65b418c24583",
    "security_group_name" : "sg_6379_4944a40e-ac57-4f08-9d38-9786e2759458",
    "subnet_id" : "ec2f34b9-20eb-4872-85bd-bea9fc943128",
    "subnet_name" : "subnet_az_7f336767-10ec-48a5-9ae8-9cacde119318",
    "available_zones" : "XXXXXX",
    "max_memory" : 460,
    "used_memory" : 56,
    "user_id": "6d0977e4c9b74ae7b5a083a8d0d8fafa",
    "user_name": "liutao02",
    "order_id": "XXXXXXXXX",
    "maintain_begin" : "22:00:00",
    "maintain_end" : "02:00:00"
}
```

## Status Code<a name="section18373103889"></a>

[Table 4](#table183731131183)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table183731131183"></a>
<table><thead align="left"><tr id="row23747312814"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p123741732818"><a name="p123741732818"></a><a name="p123741732818"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p133741337815"><a name="p133741337815"></a><a name="p133741337815"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14374732815"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p4374537817"><a name="p4374537817"></a><a name="p4374537817"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p12374834813"><a name="p12374834813"></a><a name="p12374834813"></a>Specified instance queried successfully.</p>
</td>
</tr>
</tbody>
</table>

