# Querying Backend Servers<a name="EN-US_TOPIC_0096561554"></a>

## Function<a name="en-us_topic_0049139655_section65515007"></a>

This API is used to query backend servers in a specific backend server group. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="en-us_topic_0049139655_section52764152"></a>

GET /v2.0/lbaas/pools/\{pool\_id\}/members

**Table  1**  Parameter description

<a name="table165579169133"></a>
<table><thead align="left"><tr id="row1459519165134"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p1659518164131"><a name="p1659518164131"></a><a name="p1659518164131"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p2595116171315"><a name="p2595116171315"></a><a name="p2595116171315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p3691583351"><a name="p3691583351"></a><a name="p3691583351"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p2595171616132"><a name="p2595171616132"></a><a name="p2595171616132"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13595516111319"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p3595101620131"><a name="p3595101620131"></a><a name="p3595101620131"></a>pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p125951316171311"><a name="p125951316171311"></a><a name="p125951316171311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1323891417358"><a name="p1323891417358"></a><a name="p1323891417358"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p1059561618136"><a name="p1059561618136"></a><a name="p1059561618136"></a>Specifies the backend server group ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section64011614194413"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="en-us_topic_0049139655_section46037880"></a>

**Table  2**  Request parameters

<a name="table1976114363134"></a>
<table><thead align="left"><tr id="row1293643615135"><th class="cellrowborder" valign="top" width="23.72%" id="mcps1.2.5.1.1"><p id="p18936103611135"><a name="p18936103611135"></a><a name="p18936103611135"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.110000000000001%" id="mcps1.2.5.1.2"><p id="p14936936181318"><a name="p14936936181318"></a><a name="p14936936181318"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.79%" id="mcps1.2.5.1.3"><p id="p14936103661320"><a name="p14936103661320"></a><a name="p14936103661320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.38%" id="mcps1.2.5.1.4"><p id="p1593610361132"><a name="p1593610361132"></a><a name="p1593610361132"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row109368364136"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p093617364138"><a name="p093617364138"></a><a name="p093617364138"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p6936836111310"><a name="p6936836111310"></a><a name="p6936836111310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p1993683651310"><a name="p1993683651310"></a><a name="p1993683651310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p179681426923"><a name="p179681426923"></a><a name="p179681426923"></a>Specifies the ID of the backend server from which pagination query starts, that is, the ID of the last backend server on the previous page. If this parameter is not specified, the first page will be queried.</p>
<p id="p124032918214"><a name="p124032918214"></a><a name="p124032918214"></a>This parameter must be used together with <strong id="b13766143172212"><a name="b13766143172212"></a><a name="b13766143172212"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row4937113681318"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p1393723681320"><a name="p1393723681320"></a><a name="p1393723681320"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p7937183620135"><a name="p7937183620135"></a><a name="p7937183620135"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p093793618136"><a name="p093793618136"></a><a name="p093793618136"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p814016314216"><a name="p814016314216"></a><a name="p814016314216"></a>Specifies the number of backend servers on each page.</p>
<p id="p1414613319219"><a name="p1414613319219"></a><a name="p1414613319219"></a>The value ranges from <strong id="b52691412122211"><a name="b52691412122211"></a><a name="b52691412122211"></a>0</strong> to <strong id="b326931202213"><a name="b326931202213"></a><a name="b326931202213"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row89371836121318"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p209371436171317"><a name="p209371436171317"></a><a name="p209371436171317"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p993733614135"><a name="p993733614135"></a><a name="p993733614135"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p2937536161315"><a name="p2937536161315"></a><a name="p2937536161315"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p5902734022"><a name="p5902734022"></a><a name="p5902734022"></a>Specifies the page direction. The value can be <strong id="b712099194016"><a name="b712099194016"></a><a name="b712099194016"></a>true</strong> or <strong id="b412109134013"><a name="b412109134013"></a><a name="b412109134013"></a>false</strong>, and the default value is <strong id="b101227918403"><a name="b101227918403"></a><a name="b101227918403"></a>false</strong>. The last page in the list requested with <strong id="b151221984017"><a name="b151221984017"></a><a name="b151221984017"></a>page_reverse</strong> set to <strong id="b14123129194011"><a name="b14123129194011"></a><a name="b14123129194011"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b81231910409"><a name="b81231910409"></a><a name="b81231910409"></a>page_reverse</strong> set to <strong id="b1412414911401"><a name="b1412414911401"></a><a name="b1412414911401"></a>true</strong> will not contain the "previous" link.</p>
<p id="p13879193614214"><a name="p13879193614214"></a><a name="p13879193614214"></a>This parameter must be used together with <strong id="b919511216501"><a name="b919511216501"></a><a name="b919511216501"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row18937183610133"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p1893713619131"><a name="p1893713619131"></a><a name="p1893713619131"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p793713368139"><a name="p793713368139"></a><a name="p793713368139"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p335920813460"><a name="p335920813460"></a><a name="p335920813460"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p2093714369132"><a name="p2093714369132"></a><a name="p2093714369132"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="row109461745484"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p88461695515"><a name="p88461695515"></a><a name="p88461695515"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p1084618910518"><a name="p1084618910518"></a><a name="p1084618910518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p188466919514"><a name="p188466919514"></a><a name="p188466919514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p11846891258"><a name="p11846891258"></a><a name="p11846891258"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="p77515330521"><a name="p77515330521"></a><a name="p77515330521"></a>The value contains a maximum of 255 characters.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row1893793619139"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p119371136101313"><a name="p119371136101313"></a><a name="p119371136101313"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p19937836171311"><a name="p19937836171311"></a><a name="p19937836171311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p149372368135"><a name="p149372368135"></a><a name="p149372368135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p693713366130"><a name="p693713366130"></a><a name="p693713366130"></a>Specifies the backend server name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row693713612133"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p99371736151311"><a name="p99371736151311"></a><a name="p99371736151311"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p5937136161318"><a name="p5937136161318"></a><a name="p5937136161318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p109374364138"><a name="p109374364138"></a><a name="p109374364138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p1227314024612"><a name="p1227314024612"></a><a name="p1227314024612"></a>Specifies the private IP address of the backend server.</p>
<p id="p16481141115529"><a name="p16481141115529"></a><a name="p16481141115529"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row18938436151318"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p9938123617137"><a name="p9938123617137"></a><a name="p9938123617137"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p1393833681315"><a name="p1393833681315"></a><a name="p1393833681315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p1593810369134"><a name="p1593810369134"></a><a name="p1593810369134"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p10938153691317"><a name="p10938153691317"></a><a name="p10938153691317"></a>Specifies the port used by the backend server.</p>
</td>
</tr>
<tr id="row893863691316"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p19938153618131"><a name="p19938153618131"></a><a name="p19938153618131"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p29381236191312"><a name="p29381236191312"></a><a name="p29381236191312"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p12657152824612"><a name="p12657152824612"></a><a name="p12657152824612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p11938536111320"><a name="p11938536111320"></a><a name="p11938536111320"></a>Specifies the ID of the subnet where the backend server works.</p>
</td>
</tr>
<tr id="row2938153612134"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p1893820369132"><a name="p1893820369132"></a><a name="p1893820369132"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p2093843611130"><a name="p2093843611130"></a><a name="p2093843611130"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p59381436201315"><a name="p59381436201315"></a><a name="p59381436201315"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p77019569481"><a name="p77019569481"></a><a name="p77019569481"></a>Specifies the administrative status of the backend server.</p>
<p id="p1558456113514"><a name="p1558456113514"></a><a name="p1558456113514"></a>The value can be <strong id="b172205245231"><a name="b172205245231"></a><a name="b172205245231"></a>true</strong> or <strong id="b17221162414234"><a name="b17221162414234"></a><a name="b17221162414234"></a>false</strong>.</p>
<div class="note" id="note47703154344"><a name="note47703154344"></a><a name="note47703154344"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p157701215103415"><a name="p157701215103415"></a><a name="p157701215103415"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="b84235270615599"><a name="b84235270615599"></a><a name="b84235270615599"></a>true</strong>. Otherwise, the value is <strong id="b842352706155915"><a name="b842352706155915"></a><a name="b842352706155915"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row4938113651312"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p89382036161315"><a name="p89382036161315"></a><a name="p89382036161315"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="15.110000000000001%" headers="mcps1.2.5.1.2 "><p id="p1193810367139"><a name="p1193810367139"></a><a name="p1193810367139"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.79%" headers="mcps1.2.5.1.3 "><p id="p593853614137"><a name="p593853614137"></a><a name="p593853614137"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.38%" headers="mcps1.2.5.1.4 "><p id="p98301617144916"><a name="p98301617144916"></a><a name="p98301617144916"></a>Specifies the backend server weight.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139655_section7182635"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0049139655_table14477792"></a>
<table><thead align="left"><tr id="en-us_topic_0049139655_row13265486"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139655_p762549"><a name="en-us_topic_0049139655_p762549"></a><a name="en-us_topic_0049139655_p762549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139655_p61766529"><a name="en-us_topic_0049139655_p61766529"></a><a name="en-us_topic_0049139655_p61766529"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139655_p46881895"><a name="en-us_topic_0049139655_p46881895"></a><a name="en-us_topic_0049139655_p46881895"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139655_row39337169"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139655_p32194111"><a name="en-us_topic_0049139655_p32194111"></a><a name="en-us_topic_0049139655_p32194111"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139655_p168245"><a name="en-us_topic_0049139655_p168245"></a><a name="en-us_topic_0049139655_p168245"></a>Lists backend servers in the backend server group. For details, see <a href="#table1877212199143">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **members**  parameter description

<a name="table1877212199143"></a>
<table><thead align="left"><tr id="row5943141910140"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p9498125845116"><a name="p9498125845116"></a><a name="p9498125845116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p1694331915148"><a name="p1694331915148"></a><a name="p1694331915148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p1394311911140"><a name="p1394311911140"></a><a name="p1394311911140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row594316193141"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p13943219121412"><a name="p13943219121412"></a><a name="p13943219121412"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p13816161614525"><a name="p13816161614525"></a><a name="p13816161614525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p6154231141610"><a name="p6154231141610"></a><a name="p6154231141610"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="row199441219181414"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p694411991416"><a name="p694411991416"></a><a name="p694411991416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1694481915147"><a name="p1694481915147"></a><a name="p1694481915147"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p201561631141618"><a name="p201561631141618"></a><a name="p201561631141618"></a>Specifies the ID of the project where the backend server is used.</p>
<p id="p188081726175214"><a name="p188081726175214"></a><a name="p188081726175214"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row19944141911140"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p294414191142"><a name="p294414191142"></a><a name="p294414191142"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1694481921414"><a name="p1694481921414"></a><a name="p1694481921414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p13156193151618"><a name="p13156193151618"></a><a name="p13156193151618"></a>Specifies the backend server name.</p>
<p id="p34491640125210"><a name="p34491640125210"></a><a name="p34491640125210"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1494431901416"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1694411914147"><a name="p1694411914147"></a><a name="p1694411914147"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p7944161941414"><a name="p7944161941414"></a><a name="p7944161941414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p2611194017408"><a name="p2611194017408"></a><a name="p2611194017408"></a>Specifies the private IP address of the backend server. This IP address must be in the subnet specified by <strong id="b2034823010244"><a name="b2034823010244"></a><a name="b2034823010244"></a>subnet_id</strong>.</p>
<p id="p18611164024019"><a name="p18611164024019"></a><a name="p18611164024019"></a>This parameter can be set only to the IP address of the primary NIC, for example, 192.168.3.11.</p>
<p id="p07221436521"><a name="p07221436521"></a><a name="p07221436521"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row1494421951413"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p2944121971415"><a name="p2944121971415"></a><a name="p2944121971415"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p594411917147"><a name="p594411917147"></a><a name="p594411917147"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p141561431161615"><a name="p141561431161615"></a><a name="p141561431161615"></a>Specifies the port used by the backend server. The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="row3944181911143"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1694401913146"><a name="p1694401913146"></a><a name="p1694401913146"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p99451519171419"><a name="p99451519171419"></a><a name="p99451519171419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p986015317414"><a name="p986015317414"></a><a name="p986015317414"></a>Specifies the ID of the subnet where the backend server works. The private IP address of the backend server is in this subnet.</p>
<p id="p88604374112"><a name="p88604374112"></a><a name="p88604374112"></a>IPv6 subnets are not supported.</p>
</td>
</tr>
<tr id="row12945161901410"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p109454191140"><a name="p109454191140"></a><a name="p109454191140"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p09451719141413"><a name="p09451719141413"></a><a name="p09451719141413"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p38145286413"><a name="p38145286413"></a><a name="p38145286413"></a>Specifies the administrative status of the backend server. The value can be <strong id="b126194983218"><a name="b126194983218"></a><a name="b126194983218"></a>true</strong> or <strong id="b18262194973210"><a name="b18262194973210"></a><a name="b18262194973210"></a>false</strong>.</p>
<p id="p1881412814419"><a name="p1881412814419"></a><a name="p1881412814419"></a>Currently, the value can only be <strong id="b387912444329"><a name="b387912444329"></a><a name="b387912444329"></a>true</strong>.</p>
<div class="note" id="note1873514247366"><a name="note1873514247366"></a><a name="note1873514247366"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1773662413613"><a name="p1773662413613"></a><a name="p1773662413613"></a>This parameter can be used during creation and update and its actual value depends on whether the backend server exists. If the backend server exists, the value is <strong id="b750503843"><a name="b750503843"></a><a name="b750503843"></a>true</strong>. Otherwise, the value is <strong id="b1730689346"><a name="b1730689346"></a><a name="b1730689346"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row694512191147"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p5945191941416"><a name="p5945191941416"></a><a name="p5945191941416"></a>weight</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p49452195145"><a name="p49452195145"></a><a name="p49452195145"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p8605175104117"><a name="p8605175104117"></a><a name="p8605175104117"></a>Specifies the backend server weight. The value ranges from <strong id="b760413715259"><a name="b760413715259"></a><a name="b760413715259"></a>0</strong> to <strong id="b176051273256"><a name="b176051273256"></a><a name="b176051273256"></a>100</strong>.</p>
<p id="p1460555119418"><a name="p1460555119418"></a><a name="p1460555119418"></a>If the value is <strong id="b13914917256"><a name="b13914917256"></a><a name="b13914917256"></a>0</strong>, the backend server will not accept new requests. The default value is <strong id="b184553103254"><a name="b184553103254"></a><a name="b184553103254"></a>1</strong>.</p>
</td>
</tr>
<tr id="row1945219101415"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p189451819181414"><a name="p189451819181414"></a><a name="p189451819181414"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p119453196141"><a name="p119453196141"></a><a name="p119453196141"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p187109210289"><a name="p187109210289"></a><a name="p187109210289"></a>Specifies the health check result of the backend server. The value can be one of the following:</p>
<a name="ul1229315244282"></a><a name="ul1229315244282"></a><ul id="ul1229315244282"><li><strong id="b43341325103615"><a name="b43341325103615"></a><a name="b43341325103615"></a>ONLINE</strong>: The health check is successfully conducted and the backend server is running properly.</li><li><strong id="b777962673615"><a name="b777962673615"></a><a name="b777962673615"></a>OFFLINE</strong>: The health check is abnormal and the backend server is running improperly. The load balancer stops distributing traffic to this server until it recovers.</li><li><strong id="b19298102813364"><a name="b19298102813364"></a><a name="b19298102813364"></a>NO_MONITOR</strong>: No health check is conducted. No health checks are configured, or the value of <strong id="b1524643093613"><a name="b1524643093613"></a><a name="b1524643093613"></a>admin_state_up</strong> is <strong id="b82471730103613"><a name="b82471730103613"></a><a name="b82471730103613"></a>false</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
<tr id="row223224863815"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1791419535386"><a name="p1791419535386"></a><a name="p1791419535386"></a>members_links</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p12811813111410"><a name="p12811813111410"></a><a name="p12811813111410"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p958115491633"><a name="p958115491633"></a><a name="p958115491633"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p27814512315"><a name="p27814512315"></a><a name="p27814512315"></a>This parameter exists only in the response body of pagination query. For details, see <a href="#table109691887394">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **members\_links**  parameter description

<a name="table109691887394"></a>
<table><thead align="left"><tr id="row19121913919"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p41219903910"><a name="p41219903910"></a><a name="p41219903910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p15127943917"><a name="p15127943917"></a><a name="p15127943917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p3121493399"><a name="p3121493399"></a><a name="p3121493399"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row191212983916"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p7121699392"><a name="p7121699392"></a><a name="p7121699392"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p131299153916"><a name="p131299153916"></a><a name="p131299153916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p44564735"><a name="p44564735"></a><a name="p44564735"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row31218923918"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p12125963910"><a name="p12125963910"></a><a name="p12125963910"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p2127910393"><a name="p2127910393"></a><a name="p2127910393"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p85234211272"><a name="p85234211272"></a><a name="p85234211272"></a>Specifies the prompt of the previous or next page. The value can be <strong id="b177311632192517"><a name="b177311632192517"></a><a name="b177311632192517"></a>next</strong> or <strong id="b1573223202518"><a name="b1573223202518"></a><a name="b1573223202518"></a>previous</strong>.</p>
<a name="ul577082711719"></a><a name="ul577082711719"></a><ul id="ul577082711719"><li><strong id="b510416358254"><a name="b510416358254"></a><a name="b510416358254"></a>next</strong>: indicates the URL of the next page.</li><li><strong id="b8991113692519"><a name="b8991113692519"></a><a name="b8991113692519"></a>previous</strong>: indicates the URL of the previous page.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section363719549286"></a>

-   Example request 1: Querying all backend servers

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members
    ```


-   Example response 1

    ```
    {
        "members": [
            {
                "address": "10.0.0.8", 
                "admin_state_up": true, 
                "id": "9a7aff27-fd41-4ec1-ba4c-3eb92c629313", 
                "protocol_port": 80, 
                "subnet_id": "013d3059-87a4-45a5-91e9-d721068ae0b2", 
                "tenant_id": "1a3e005cf9ce40308c900bcb08e5320c",
                "weight": 1, 
                "operating_status": "ONLINE", 
                "name": "member-name"
            }
        ]
    }
    ```


-   Example request 2: Querying the backend cloud server whose IP address is 10.0.0.8 and port number is 80

    ```
    GET https://{Endpoint}/v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members?address=10.0.0.8&protocol_port=80
    ```


-   Example response 2

    ```
    {
        "members": [
            {
                "address": "10.0.0.8", 
                "admin_state_up": true, 
                "id": "9a7aff27-fd41-4ec1-ba4c-3eb92c629313", 
                "protocol_port": 80, 
                "subnet_id": "013d3059-87a4-45a5-91e9-d721068ae0b2", 
                "tenant_id": "1a3e005cf9ce40308c900bcb08e5320c",
     
                "weight": 1, 
                "operating_status": "ONLINE", 
                "name": "member-name"
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

