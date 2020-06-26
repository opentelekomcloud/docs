# Querying DNAT Rules<a name="nat_api_0012"></a>

## Function<a name="section28610428164132"></a>

This API is used to query a DNAT rule list.

## URI<a name="section19503903164158"></a>

GET /v2.0/dnat\_rules

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. All optional parameters can be filtered. For details, see the example request.  

**Table  1**  Parameter description

<a name="table93762054132613"></a>
<table><thead align="left"><tr id="row9501145413265"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p550115415265"><a name="p550115415265"></a><a name="p550115415265"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p3501754122611"><a name="p3501754122611"></a><a name="p3501754122611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.4.1.3"><p id="p250105419269"><a name="p250105419269"></a><a name="p250105419269"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14501165412613"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p75013243343"><a name="p75013243343"></a><a name="p75013243343"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1850122411341"><a name="p1850122411341"></a><a name="p1850122411341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p195072453418"><a name="p195072453418"></a><a name="p195072453418"></a>Specifies the DNAT rule ID.</p>
</td>
</tr>
<tr id="row741582519283"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1146353082810"><a name="p1146353082810"></a><a name="p1146353082810"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p44641230172812"><a name="p44641230172812"></a><a name="p44641230172812"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p1946483042811"><a name="p1946483042811"></a><a name="p1946483042811"></a>Specifies the number of records on each page.</p>
</td>
</tr>
<tr id="row105011454132610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1501024133416"><a name="p1501024133416"></a><a name="p1501024133416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p8501524153419"><a name="p8501524153419"></a><a name="p8501524153419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p150524123413"><a name="p150524123413"></a><a name="p150524123413"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row650115472619"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p650924193418"><a name="p650924193418"></a><a name="p650924193418"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p750182443418"><a name="p750182443418"></a><a name="p750182443418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p1451624163419"><a name="p1451624163419"></a><a name="p1451624163419"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row1501125413265"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p35192443411"><a name="p35192443411"></a><a name="p35192443411"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p17514241349"><a name="p17514241349"></a><a name="p17514241349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p135110246348"><a name="p135110246348"></a><a name="p135110246348"></a>Specifies the port ID of an ECS or a BMS.</p>
</td>
</tr>
<tr id="row16501354192619"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1651182413349"><a name="p1651182413349"></a><a name="p1651182413349"></a>private_ip</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p195192414349"><a name="p195192414349"></a><a name="p195192414349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p15511224133415"><a name="p15511224133415"></a><a name="p15511224133415"></a>Specifies the private IP address, for example, the IP address of a Direct Connect connection.</p>
</td>
</tr>
<tr id="row1150185452610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p5511424123420"><a name="p5511424123420"></a><a name="p5511424123420"></a>internal_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p105119243343"><a name="p105119243343"></a><a name="p105119243343"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p7513246347"><a name="p7513246347"></a><a name="p7513246347"></a>Specifies the port used by ECSs or BMSs to provide services for external systems.</p>
</td>
</tr>
<tr id="row1950195417261"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p165122412348"><a name="p165122412348"></a><a name="p165122412348"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p851132413341"><a name="p851132413341"></a><a name="p851132413341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p05119242344"><a name="p05119242344"></a><a name="p05119242344"></a>Specifies the EIP ID.</p>
</td>
</tr>
<tr id="row18501454162610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p16511224133414"><a name="p16511224133414"></a><a name="p16511224133414"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p5511224153414"><a name="p5511224153414"></a><a name="p5511224153414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p1352324123412"><a name="p1352324123412"></a><a name="p1352324123412"></a>Specifies the EIP.</p>
</td>
</tr>
<tr id="row15501115452610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p155262418349"><a name="p155262418349"></a><a name="p155262418349"></a>external_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p052152410349"><a name="p052152410349"></a><a name="p052152410349"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p05210248347"><a name="p05210248347"></a><a name="p05210248347"></a>Specifies the port for providing external services.</p>
</td>
</tr>
<tr id="row15011954142618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p552192443414"><a name="p552192443414"></a><a name="p552192443414"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1666203645612"><a name="p1666203645612"></a><a name="p1666203645612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p1152182413347"><a name="p1152182413347"></a><a name="p1152182413347"></a>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</p>
<p id="p185242483420"><a name="p185242483420"></a><a name="p185242483420"></a>The protocol number of TCP, UDP, and ANY are 6, 17, and 0, respectively.</p>
</td>
</tr>
<tr id="row18532115313334"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1252172410347"><a name="p1252172410347"></a><a name="p1252172410347"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1852142423414"><a name="p1852142423414"></a><a name="p1852142423414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul952182413342"></a><a name="ul952182413342"></a><ul id="ul952182413342"><li>Specifies the status of the DNAT rule.</li><li>For details about all its values, see <u id="u1752182473413"><a name="u1752182473413"></a><a name="u1752182473413"></a><u id="u105212413416"><a name="u105212413416"></a><a name="u105212413416"></a><a href="resource-status-description.md">Resource Status Description</a></u></u>.</li></ul>
</td>
</tr>
<tr id="row359059183310"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p752122412345"><a name="p752122412345"></a><a name="p752122412345"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the DNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b337714410313"><a name="b337714410313"></a><a name="b337714410313"></a>true</strong>: The DNAT rule is enabled.</li><li><strong id="b144324514320"><a name="b144324514320"></a><a name="b144324514320"></a>false</strong>: The DNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1768062193420"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p195292413414"><a name="p195292413414"></a><a name="p195292413414"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p17521624103417"><a name="p17521624103417"></a><a name="p17521624103417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p055611361601"><a name="p055611361601"></a><a name="p055611361601"></a>Specifies when the DNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section2749321016454"></a>

None

## Response<a name="section55770648164519"></a>

[Table 2](#table47307406164538)  lists response parameters.

**Table  2**  Response parameters

<a name="table47307406164538"></a>
<table><thead align="left"><tr id="row43170063164538"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p7114239164538"><a name="p7114239164538"></a><a name="p7114239164538"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.050000000000004%" id="mcps1.2.4.1.2"><p id="p39382504164538"><a name="p39382504164538"></a><a name="p39382504164538"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p19483074164538"><a name="p19483074164538"></a><a name="p19483074164538"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34625156164538"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p53174238164538"><a name="p53174238164538"></a><a name="p53174238164538"></a>dnat_rules</p>
</td>
<td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p12146041164538"><a name="p12146041164538"></a><a name="p12146041164538"></a>Array(Object)</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p31957648164538"><a name="p31957648164538"></a><a name="p31957648164538"></a>Specifies the DNAT rule objects. For details, see <a href="#table19520113319519">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **dnat\_rule**  field

<a name="table19520113319519"></a>
<table><thead align="left"><tr id="row185205331254"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p05291666"><a name="p05291666"></a><a name="p05291666"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p75093619"><a name="p75093619"></a><a name="p75093619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p451917619"><a name="p451917619"></a><a name="p451917619"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15520133952"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p951910610"><a name="p951910610"></a><a name="p951910610"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1656918614"><a name="p1656918614"></a><a name="p1656918614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p051291561"><a name="p051291561"></a><a name="p051291561"></a>Specifies the DNAT rule ID.</p>
</td>
</tr>
<tr id="row105201033858"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p254910616"><a name="p254910616"></a><a name="p254910616"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1251899611"><a name="p1251899611"></a><a name="p1251899611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15895619"><a name="p15895619"></a><a name="p15895619"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row145201533552"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7512916615"><a name="p7512916615"></a><a name="p7512916615"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p155999619"><a name="p155999619"></a><a name="p155999619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1251091363"><a name="p1251091363"></a><a name="p1251091363"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row65209331152"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45892062"><a name="p45892062"></a><a name="p45892062"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3517914615"><a name="p3517914615"></a><a name="p3517914615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1651197615"><a name="p1651197615"></a><a name="p1651197615"></a>Specifies the port ID of an ECS or a BMS.</p>
</td>
</tr>
<tr id="row25205331457"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1251911618"><a name="p1251911618"></a><a name="p1251911618"></a>private_ip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1351091667"><a name="p1351091667"></a><a name="p1351091667"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p95891616"><a name="p95891616"></a><a name="p95891616"></a>Specifies the private IP address, for example, the IP address of a Direct Connect connection.</p>
</td>
</tr>
<tr id="row1052018331559"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p75194611"><a name="p75194611"></a><a name="p75194611"></a>internal_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p951591063"><a name="p951591063"></a><a name="p951591063"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14520920611"><a name="p14520920611"></a><a name="p14520920611"></a>Specifies the port used by ECSs or BMSs to provide services for external systems.</p>
</td>
</tr>
<tr id="row1752020331551"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p051991961"><a name="p051991961"></a><a name="p051991961"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p05109969"><a name="p05109969"></a><a name="p05109969"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p135997619"><a name="p135997619"></a><a name="p135997619"></a>Specifies the EIP ID.</p>
</td>
</tr>
<tr id="row652015339517"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9510911613"><a name="p9510911613"></a><a name="p9510911613"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p155189360"><a name="p155189360"></a><a name="p155189360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25297618"><a name="p25297618"></a><a name="p25297618"></a>Specifies the EIP.</p>
</td>
</tr>
<tr id="row1752013312513"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p175199763"><a name="p175199763"></a><a name="p175199763"></a>external_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1951396617"><a name="p1951396617"></a><a name="p1951396617"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1557910616"><a name="p1557910616"></a><a name="p1557910616"></a>Specifies the port for providing external services.</p>
</td>
</tr>
<tr id="row752017339518"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p185591614"><a name="p185591614"></a><a name="p185591614"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1251395611"><a name="p1251395611"></a><a name="p1251395611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4517918619"><a name="p4517918619"></a><a name="p4517918619"></a>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</p>
<p id="p1551098611"><a name="p1551098611"></a><a name="p1551098611"></a>The protocol number of TCP, UDP, and ANY are 6, 17, and 0, respectively.</p>
</td>
</tr>
<tr id="row55358331458"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p353919612"><a name="p353919612"></a><a name="p353919612"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p85893612"><a name="p85893612"></a><a name="p85893612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul6519962"></a><a name="ul6519962"></a><ul id="ul6519962"><li>Specifies the status of the DNAT rule.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row1353593311511"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10529463"><a name="p10529463"></a><a name="p10529463"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12628475214"><a name="p12628475214"></a><a name="p12628475214"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul2112113885720"></a><a name="ul2112113885720"></a><ul id="ul2112113885720"><li>Specifies whether the DNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul17113838115713"></a><a name="ul17113838115713"></a><ul id="ul17113838115713"><li><strong id="b184941145142319"><a name="b184941145142319"></a><a name="b184941145142319"></a>true</strong>: The DNAT rule is enabled.</li><li><strong id="b1867424619232"><a name="b1867424619232"></a><a name="b1867424619232"></a>false</strong>: The DNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1953517336520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1050916613"><a name="p1050916613"></a><a name="p1050916613"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4529368"><a name="p4529368"></a><a name="p4529368"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p74507428015"><a name="p74507428015"></a><a name="p74507428015"></a>Specifies when the DNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section39793997164640"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/dnat_rules
    ```


-   Example response

    ```
    {
        "dnat_rules": [
            {
                "floating_ip_id": "bf99c679-9f41-4dac-8513-9c9228e713e1",
                "status": "ACTIVE",
                "nat_gateway_id": "cda3a125-2406-456c-a11f-598e10578541",
                "admin_state_up": true,
                "port_id": "9a469561-daac-4c94-88f5-39366e5ea193",
                "internal_service_port": 993,
                "protocol": "tcp",
                "tenant_id": "abc",
                "created_at": "2017-11-15 15:44:42.595173",
                "id": "79195d50-0271-41f1-bded-4c089b2502ff",
                "floating_ip_address": "5.21.11.226",
                "external_service_port": 242,
                "private_ip": ""  
            },
            {
                "floating_ip_id": "cf99c679-9f41-4dac-8513-9c9228e713e1",
                "status": "ACTIVE",
                "nat_gateway_id": "dda3a125-2406-456c-a11f-598e10578541",
                "admin_state_up": true,　
                "port_id": "",
                "private_ip": "192.168.1.100",
                "internal_service_port": 0,
                "protocol": "any",
                "tenant_id": "abc",
                "created_at": "2017-11-16 15:44:42.595173",
                "id": "89195d50-0271-41f1-bded-4c089b2502ff",
                "floating_ip_address": "5.21.11.227",
    　　　　　　"external_service_port": 0
            }
        ]
    }
    ```


## Status Code<a name="section45841191164749"></a>

See  [Status Codes](status-codes.md).

