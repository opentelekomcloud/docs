# Querying Networks<a name="vpc_network_0001"></a>

## Function<a name="section23215317204921"></a>

This API is used to query all networks accessible to the tenant submitting the request. 

## URI<a name="section12532958204921"></a>

GET /v2.0/networks

Example:

```
GET https://{Endpoint}/v2.0/networks?id={network_id}&status={network_status}&name={network_name}&admin_state_up=${admin_state_up}&tenant_id={tenant_id}&shared={is_shared}&provider:network_type={geneve}
```

Example of querying ports by page

```
GET https://{Endpoint}/v2.0/networks?limit=2&marker=0133cd73-34d4-4d4c-bf1f-e65b24603206&page_reverse=False
```

[Table 1](#table1410155047)  describes the parameters.

**Table  1**  Parameter description

<a name="table1410155047"></a>
<table><thead align="left"><tr id="row0527145518411"><th class="cellrowborder" valign="top" width="21.23212321232123%" id="mcps1.2.5.1.1"><p id="p1652714551347"><a name="p1652714551347"></a><a name="p1652714551347"></a><strong id="b17295048507"><a name="b17295048507"></a><a name="b17295048507"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.6011601160116%" id="mcps1.2.5.1.2"><p id="p13527185520420"><a name="p13527185520420"></a><a name="p13527185520420"></a><strong id="b101721051508"><a name="b101721051508"></a><a name="b101721051508"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.53125312531253%" id="mcps1.2.5.1.3"><p id="p352795512415"><a name="p352795512415"></a><a name="p352795512415"></a><strong id="b3952617501"><a name="b3952617501"></a><a name="b3952617501"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.635463546354636%" id="mcps1.2.5.1.4"><p id="p105273551347"><a name="p105273551347"></a><a name="p105273551347"></a><strong id="b38291695014"><a name="b38291695014"></a><a name="b38291695014"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1952795512413"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p1552718559410"><a name="p1552718559410"></a><a name="p1552718559410"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p125273551643"><a name="p125273551643"></a><a name="p125273551643"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p152765519412"><a name="p152765519412"></a><a name="p152765519412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p135271855345"><a name="p135271855345"></a><a name="p135271855345"></a>Specifies that the network ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row115275551544"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p175271551841"><a name="p175271551841"></a><a name="p175271551841"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p12527145515419"><a name="p12527145515419"></a><a name="p12527145515419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p115271955446"><a name="p115271955446"></a><a name="p115271955446"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p1852775510412"><a name="p1852775510412"></a><a name="p1852775510412"></a>Specifies that the network name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row16527155514418"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p12528655847"><a name="p12528655847"></a><a name="p12528655847"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p2528195513412"><a name="p2528195513412"></a><a name="p2528195513412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p185283553418"><a name="p185283553418"></a><a name="p185283553418"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p5282556356"><a name="p5282556356"></a><a name="p5282556356"></a>Specifies that the admin state is used as the filtering condition.</p>
<p id="p25281555341"><a name="p25281555341"></a><a name="p25281555341"></a>The value can be <strong id="b318012925113"><a name="b318012925113"></a><a name="b318012925113"></a>true</strong> or <strong id="b121811993510"><a name="b121811993510"></a><a name="b121811993510"></a>false</strong>.</p>
</td>
</tr>
<tr id="row10528855948"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p15528455741"><a name="p15528455741"></a><a name="p15528455741"></a>provider:network_type</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p652825520419"><a name="p652825520419"></a><a name="p652825520419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p155283556411"><a name="p155283556411"></a><a name="p155283556411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p75281552411"><a name="p75281552411"></a><a name="p75281552411"></a>Specifies that the network type is used as the filtering condition.</p>
</td>
</tr>
<tr id="row752812551740"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p7528115518410"><a name="p7528115518410"></a><a name="p7528115518410"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p852885511418"><a name="p852885511418"></a><a name="p852885511418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p452810551843"><a name="p452810551843"></a><a name="p452810551843"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p88851621268"><a name="p88851621268"></a><a name="p88851621268"></a>Specifies that whether the network can be shared by multiple tenants is used as the filtering condition.</p>
<p id="p75288553418"><a name="p75288553418"></a><a name="p75288553418"></a>The value can be <strong id="b16750192125214"><a name="b16750192125214"></a><a name="b16750192125214"></a>true</strong> or <strong id="b675132125214"><a name="b675132125214"></a><a name="b675132125214"></a>false</strong>.</p>
</td>
</tr>
<tr id="row75282055043"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p115288559419"><a name="p115288559419"></a><a name="p115288559419"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p14528185519414"><a name="p14528185519414"></a><a name="p14528185519414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p05288553419"><a name="p05288553419"></a><a name="p05288553419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p92331363616"><a name="p92331363616"></a><a name="p92331363616"></a>Specifies that the network status is used as the filtering condition.</p>
<p id="p155281255741"><a name="p155281255741"></a><a name="p155281255741"></a>The value can be <strong id="b19116476525"><a name="b19116476525"></a><a name="b19116476525"></a>ACTIVE</strong>, <strong id="b1991116470525"><a name="b1991116470525"></a><a name="b1991116470525"></a>BUILD</strong>, or <strong id="b169114476525"><a name="b169114476525"></a><a name="b169114476525"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row7528355340"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p165289551844"><a name="p165289551844"></a><a name="p165289551844"></a>router:external</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p2528135514412"><a name="p2528135514412"></a><a name="p2528135514412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p6528195520413"><a name="p6528195520413"></a><a name="p6528195520413"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p15111118567"><a name="p15111118567"></a><a name="p15111118567"></a>Specifies whether the network is an external network  is used as the filtering condition.</p>
<p id="p1152875520410"><a name="p1152875520410"></a><a name="p1152875520410"></a>The value can be <strong id="b64711118145314"><a name="b64711118145314"></a><a name="b64711118145314"></a>true</strong> or <strong id="b2047291820537"><a name="b2047291820537"></a><a name="b2047291820537"></a>false</strong>.</p>
</td>
</tr>
<tr id="row11528165510410"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p195281055542"><a name="p195281055542"></a><a name="p195281055542"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p55282551341"><a name="p55282551341"></a><a name="p55282551341"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p2052810555417"><a name="p2052810555417"></a><a name="p2052810555417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p14528125512415"><a name="p14528125512415"></a><a name="p14528125512415"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row752819551948"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p1252817557412"><a name="p1252817557412"></a><a name="p1252817557412"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p12528185512413"><a name="p12528185512413"></a><a name="p12528185512413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p155281855944"><a name="p155281855944"></a><a name="p155281855944"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p652818556415"><a name="p652818556415"></a><a name="p652818556415"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row1552812558411"><td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.5.1.1 "><p id="p452865513417"><a name="p452865513417"></a><a name="p452865513417"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="11.6011601160116%" headers="mcps1.2.5.1.2 "><p id="p85281755943"><a name="p85281755943"></a><a name="p85281755943"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.53125312531253%" headers="mcps1.2.5.1.3 "><p id="p1952818555414"><a name="p1952818555414"></a><a name="p1952818555414"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.635463546354636%" headers="mcps1.2.5.1.4 "><p id="p25444113620"><a name="p25444113620"></a><a name="p25444113620"></a>Specifies the number of records on each page.</p>
<p id="p105281955147"><a name="p105281955147"></a><a name="p105281955147"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section24189635204921"></a>

None

## Response Message<a name="section51721924204921"></a>

**Table  2**  Response parameter

<a name="table28726301204921"></a>
<table><thead align="left"><tr id="row66095891204921"><th class="cellrowborder" valign="top" width="18.82%" id="mcps1.2.4.1.1"><p id="p52166951204921"><a name="p52166951204921"></a><a name="p52166951204921"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.709999999999997%" id="mcps1.2.4.1.2"><p id="p64773532204921"><a name="p64773532204921"></a><a name="p64773532204921"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.47%" id="mcps1.2.4.1.3"><p id="p45821640204921"><a name="p45821640204921"></a><a name="p45821640204921"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20565326204921"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p55178709204921"><a name="p55178709204921"></a><a name="p55178709204921"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.2.4.1.2 "><p id="p40290436204921"><a name="p40290436204921"></a><a name="p40290436204921"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.2.4.1.3 "><p id="p3740541204921"><a name="p3740541204921"></a><a name="p3740541204921"></a>Specifies the network list. For details, see <a href="#table49902238182444">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **network**  object

<a name="table49902238182444"></a>
<table><thead align="left"><tr id="row27727643182444"><th class="cellrowborder" valign="top" width="26.22737726227377%" id="mcps1.2.4.1.1"><p id="p31346634182444"><a name="p31346634182444"></a><a name="p31346634182444"></a><strong id="b111591487501"><a name="b111591487501"></a><a name="b111591487501"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.957704229577043%" id="mcps1.2.4.1.2"><p id="p56049421182444"><a name="p56049421182444"></a><a name="p56049421182444"></a><strong id="b8277691503"><a name="b8277691503"></a><a name="b8277691503"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.81491850814919%" id="mcps1.2.4.1.3"><p id="p32650631182444"><a name="p32650631182444"></a><a name="p32650631182444"></a><strong id="b124481095011"><a name="b124481095011"></a><a name="b124481095011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27455432182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p9297551182444"><a name="p9297551182444"></a><a name="p9297551182444"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p14904129182444"><a name="p14904129182444"></a><a name="p14904129182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p19312361182444"><a name="p19312361182444"></a><a name="p19312361182444"></a>Specifies the network status. The value can be <strong id="b84235270615384"><a name="b84235270615384"></a><a name="b84235270615384"></a>ACTIVE</strong>, <strong id="b84235270615388"><a name="b84235270615388"></a><a name="b84235270615388"></a>BUILD</strong>, <strong id="b842352706153811"><a name="b842352706153811"></a><a name="b842352706153811"></a>DOWN</strong>, or <strong id="b842352706153814"><a name="b842352706153814"></a><a name="b842352706153814"></a>ERROR</strong>.</p>
</td>
</tr>
<tr id="row39593523182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p52958822182444"><a name="p52958822182444"></a><a name="p52958822182444"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p61806169182444"><a name="p61806169182444"></a><a name="p61806169182444"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p61280841182444"><a name="p61280841182444"></a><a name="p61280841182444"></a>Specifies IDs of the subnets associated with this network. The IDs are in a list.</p>
<p id="p14656663182444"><a name="p14656663182444"></a><a name="p14656663182444"></a>Only one subnet can be associated with each network.</p>
</td>
</tr>
<tr id="row64801111182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p14398613182444"><a name="p14398613182444"></a><a name="p14398613182444"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p25436971182444"><a name="p25436971182444"></a><a name="p25436971182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p59079578182444"><a name="p59079578182444"></a><a name="p59079578182444"></a>Specifies the network name.</p>
<p id="p61954155182444"><a name="p61954155182444"></a><a name="p61954155182444"></a>The name cannot be the same as the <strong id="b759421666"><a name="b759421666"></a><a name="b759421666"></a>admin_external_net</strong> value.</p>
</td>
</tr>
<tr id="row20716483182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p313524182444"><a name="p313524182444"></a><a name="p313524182444"></a>router:external</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p25395478182444"><a name="p25395478182444"></a><a name="p25395478182444"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p17174434182444"><a name="p17174434182444"></a><a name="p17174434182444"></a>Specifies whether the network is an external network. This is an extended attribute.</p>
</td>
</tr>
<tr id="row48951951182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p5685084182444"><a name="p5685084182444"></a><a name="p5685084182444"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p57838641182444"><a name="p57838641182444"></a><a name="p57838641182444"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p52254844182444"><a name="p52254844182444"></a><a name="p52254844182444"></a>Specifies the administrative status.</p>
<p id="p531550182444"><a name="p531550182444"></a><a name="p531550182444"></a>The value can only be <strong id="b842352706151311"><a name="b842352706151311"></a><a name="b842352706151311"></a>true</strong>.</p>
</td>
</tr>
<tr id="row4783956182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p51956132182444"><a name="p51956132182444"></a><a name="p51956132182444"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p47697173182444"><a name="p47697173182444"></a><a name="p47697173182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row42537647182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p22997365182444"><a name="p22997365182444"></a><a name="p22997365182444"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p50847313182444"><a name="p50847313182444"></a><a name="p50847313182444"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p8672810182444"><a name="p8672810182444"></a><a name="p8672810182444"></a>Specifies whether the firewall rule can be shared by different tenants.</p>
</td>
</tr>
<tr id="row31409028182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p61103330182444"><a name="p61103330182444"></a><a name="p61103330182444"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p50422701182444"><a name="p50422701182444"></a><a name="p50422701182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p31263412182444"><a name="p31263412182444"></a><a name="p31263412182444"></a>Specifies the network ID.</p>
<p id="p311313148445"><a name="p311313148445"></a><a name="p311313148445"></a>This parameter is not mandatory when you query networks.</p>
</td>
</tr>
<tr id="row62882662182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p60330876182444"><a name="p60330876182444"></a><a name="p60330876182444"></a>provider:network_type</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p54962794182444"><a name="p54962794182444"></a><a name="p54962794182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p3680057182444"><a name="p3680057182444"></a><a name="p3680057182444"></a>Specifies the network type. Only the VXLAN and GENEVE networks are supported. This is an extended attribute.</p>
<p id="p33120518182444"><a name="p33120518182444"></a><a name="p33120518182444"></a>Tenants can create only networks whose type is <strong id="b5740239145318"><a name="b5740239145318"></a><a name="b5740239145318"></a>geneve</strong>.</p>
</td>
</tr>
<tr id="row8468164182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p14832653182444"><a name="p14832653182444"></a><a name="p14832653182444"></a>availability_zone_hints</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p159931721230"><a name="p159931721230"></a><a name="p159931721230"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p8008921182444"><a name="p8008921182444"></a><a name="p8008921182444"></a>Specifies the availability zones available to this network. The current version does not support cross-availability-zone network scheduling.</p>
</td>
</tr>
<tr id="row44742828182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p290489182444"><a name="p290489182444"></a><a name="p290489182444"></a>availability_zones</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p331914519318"><a name="p331914519318"></a><a name="p331914519318"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p24927678182444"><a name="p24927678182444"></a><a name="p24927678182444"></a>Specifies the availability zone of this network.</p>
</td>
</tr>
<tr id="row25641034212156"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p53737204212156"><a name="p53737204212156"></a><a name="p53737204212156"></a>port_security_enabled</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p31320715212156"><a name="p31320715212156"></a><a name="p31320715212156"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p34506445212156"><a name="p34506445212156"></a><a name="p34506445212156"></a>Specifies whether the security option is enabled for the port. If the option is not enabled, the security group and DHCP snooping settings of all VMs in the network do not take effect.</p>
</td>
</tr>
<tr id="row421706155213"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p14217767523"><a name="p14217767523"></a><a name="p14217767523"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p22172685219"><a name="p22172685219"></a><a name="p22172685219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p021812614525"><a name="p021812614525"></a><a name="p021812614525"></a>Specifies the default private network DNS domain address. The system automatically sets this parameter, and you are not allowed to configure or change the parameter value.</p>
</td>
</tr>
<tr id="row1312882941114"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1161149122412"><a name="p1161149122412"></a><a name="p1161149122412"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row9120034101119"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the network is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i169281185525"><a name="i169281185525"></a><a name="i169281185525"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1542863714112"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the network is updated.</p>
<p id="p73562512455"><a name="p73562512455"></a><a name="p73562512455"></a>Format: <em id="i36381188526"><a name="i36381188526"></a><a name="i36381188526"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section33664870204921"></a>

Example request

```
GET https://{Endpoint}/v2.0/networks?limit=1
```

Example response

```
{
    "networks": [
        {
            "id": "0133cd73-34d4-4d4c-bf1f-e65b24603206",
            "name": "3804f26c-7862-43b6-ad3c-48445f42de89",
            "status": "ACTIVE",
            "shared": false,
            "subnets": [
                "423796f5-e02f-476f-bf02-2b88c8ddac8b"
            ],
            "availability_zone_hints": [],
            "availability_zones": [
                "az2.dc2",
                "az5.dc5"
            ],
            "admin_state_up": true,
            "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "provider:network_type": "vxlan",
            "router:external": false,
            "port_security_enabled": true,
            "created_at": "2018-03-23T03:51:58",
            "updated_at": "2018-03-23T03:51:58"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

