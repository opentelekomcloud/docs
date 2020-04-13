# Creating a Security Group Rule<a name="vpc_sg02_0008"></a>

## Function<a name="section5958580616319"></a>

This API is used to create a security group rule.

## URI<a name="section6291358016319"></a>

POST /v2.0/security-group-rules

## Request Message<a name="section3953869316319"></a>

**Table  1**  Request parameter

<a name="table981991416319"></a>
<table><thead align="left"><tr id="row191482716319"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.5.1.1"><p id="p2280026616319"><a name="p2280026616319"></a><a name="p2280026616319"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.2"><p id="p1835529716319"><a name="p1835529716319"></a><a name="p1835529716319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.7%" id="mcps1.2.5.1.3"><p id="p3464228716319"><a name="p3464228716319"></a><a name="p3464228716319"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="40.04%" id="mcps1.2.5.1.4"><p id="p3284526816319"><a name="p3284526816319"></a><a name="p3284526816319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3793835116319"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.5.1.1 "><p id="p4303593816319"><a name="p4303593816319"></a><a name="p4303593816319"></a>security_group_rule</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.2 "><p id="p3852346816319"><a name="p3852346816319"></a><a name="p3852346816319"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="16.7%" headers="mcps1.2.5.1.3 "><p id="p6530542116319"><a name="p6530542116319"></a><a name="p6530542116319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.5.1.4 "><p id="p732393116218"><a name="p732393116218"></a><a name="p732393116218"></a>Specifies the security group rule list. For details, see <a href="#table655457801607">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Security Group Rule**  objects

<a name="table655457801607"></a>
<table><thead align="left"><tr id="row54478641607"><th class="cellrowborder" valign="top" width="23.54%" id="mcps1.2.5.1.1"><p id="p389969021607"><a name="p389969021607"></a><a name="p389969021607"></a><strong id="b1588315265591"><a name="b1588315265591"></a><a name="b1588315265591"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.72%" id="mcps1.2.5.1.2"><p id="p07415175392"><a name="p07415175392"></a><a name="p07415175392"></a><strong id="b12441102716597"><a name="b12441102716597"></a><a name="b12441102716597"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.599999999999998%" id="mcps1.2.5.1.3"><p id="p36789391607"><a name="p36789391607"></a><a name="p36789391607"></a><strong id="b1934115288598"><a name="b1934115288598"></a><a name="b1934115288598"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.14%" id="mcps1.2.5.1.4"><p id="p433861031607"><a name="p433861031607"></a><a name="p433861031607"></a><strong id="b16123829125919"><a name="b16123829125919"></a><a name="b16123829125919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row250554771607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p254411021607"><a name="p254411021607"></a><a name="p254411021607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p27411717193910"><a name="p27411717193910"></a><a name="p27411717193910"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p505368621607"><a name="p505368621607"></a><a name="p505368621607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p480145951607"><a name="p480145951607"></a><a name="p480145951607"></a>Provides supplementary information about the security group rule.</p>
</td>
</tr>
<tr id="row569401671607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p115724181607"><a name="p115724181607"></a><a name="p115724181607"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p10741111717399"><a name="p10741111717399"></a><a name="p10741111717399"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p615991711607"><a name="p615991711607"></a><a name="p615991711607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p587796621607"><a name="p587796621607"></a><a name="p587796621607"></a>Specifies the ID of the belonged security group.</p>
</td>
</tr>
<tr id="row654332091607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p113008931607"><a name="p113008931607"></a><a name="p113008931607"></a>remote_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p374111793919"><a name="p374111793919"></a><a name="p374111793919"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p170542961607"><a name="p170542961607"></a><a name="p170542961607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p141218971607"><a name="p141218971607"></a><a name="p141218971607"></a>Specifies the peer ID of the belonged security group.</p>
<p id="p1511685411396"><a name="p1511685411396"></a><a name="p1511685411396"></a>Either <strong id="b123335422007"><a name="b123335422007"></a><a name="b123335422007"></a>remote_group_id</strong> or <strong id="b12350124710012"><a name="b12350124710012"></a><a name="b12350124710012"></a>remote_ip_prefix</strong> is used.</p>
</td>
</tr>
<tr id="row9932071607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p657989401607"><a name="p657989401607"></a><a name="p657989401607"></a>direction</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p19741111723910"><a name="p19741111723910"></a><a name="p19741111723910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p507988391607"><a name="p507988391607"></a><a name="p507988391607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p570991491607"><a name="p570991491607"></a><a name="p570991491607"></a>Specifies the direction of the traffic for which the security group rule takes effect.</p>
<p id="p13943922124015"><a name="p13943922124015"></a><a name="p13943922124015"></a>The value can be <strong id="b550743319110"><a name="b550743319110"></a><a name="b550743319110"></a>ingress</strong> or <strong id="b97031637212"><a name="b97031637212"></a><a name="b97031637212"></a>egress</strong>.</p>
</td>
</tr>
<tr id="row97529031607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p478834691607"><a name="p478834691607"></a><a name="p478834691607"></a>remote_ip_prefix</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p1574110175393"><a name="p1574110175393"></a><a name="p1574110175393"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p622759951607"><a name="p622759951607"></a><a name="p622759951607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p146708701607"><a name="p146708701607"></a><a name="p146708701607"></a>Specifies the peer IP address segment.</p>
<p id="p1238771033815"><a name="p1238771033815"></a><a name="p1238771033815"></a>Either <strong id="b990013518116"><a name="b990013518116"></a><a name="b990013518116"></a>remote_ip_prefix</strong> or <strong id="b108971518120"><a name="b108971518120"></a><a name="b108971518120"></a>remote_group_id</strong> is used.</p>
</td>
</tr>
<tr id="row315033981607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p163656291607"><a name="p163656291607"></a><a name="p163656291607"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p07411217183920"><a name="p07411217183920"></a><a name="p07411217183920"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p628340441607"><a name="p628340441607"></a><a name="p628340441607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p99902671607"><a name="p99902671607"></a><a name="p99902671607"></a>Specifies the protocol type or the IP protocol number.</p>
<p id="p6125143124117"><a name="p6125143124117"></a><a name="p6125143124117"></a>The value can be <strong id="b191601956161314"><a name="b191601956161314"></a><a name="b191601956161314"></a>tcp</strong>, <strong id="b3825301144"><a name="b3825301144"></a><a name="b3825301144"></a>udp</strong>, <strong id="b193416516143"><a name="b193416516143"></a><a name="b193416516143"></a>icmp</strong> or an IP protocol number</p>
</td>
</tr>
<tr id="row551583771607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p97886331607"><a name="p97886331607"></a><a name="p97886331607"></a>port_range_max</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p8741717103914"><a name="p8741717103914"></a><a name="p8741717103914"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p343603851607"><a name="p343603851607"></a><a name="p343603851607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p188144701607"><a name="p188144701607"></a><a name="p188144701607"></a>Specifies the maximum port number. When ICMP is used, the value is the ICMP code.</p>
<p id="p1354926164118"><a name="p1354926164118"></a><a name="p1354926164118"></a>The value ranges from 1 to 65535. (The value ranges from 0 to 255 when it indicates the code.)</p>
</td>
</tr>
<tr id="row456604071607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p630384091607"><a name="p630384091607"></a><a name="p630384091607"></a>port_range_min</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p137411517143913"><a name="p137411517143913"></a><a name="p137411517143913"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p337362901607"><a name="p337362901607"></a><a name="p337362901607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p258562691607"><a name="p258562691607"></a><a name="p258562691607"></a>Specifies the minimum port number. If the ICMP protocol is used, this parameter indicates the ICMP type.</p>
<p id="p5690808615417"><a name="p5690808615417"></a><a name="p5690808615417"></a>When the TCP or UDP protocol is used, both <strong id="b73511626179"><a name="b73511626179"></a><a name="b73511626179"></a>port_range_max</strong> and <strong id="b133669241718"><a name="b133669241718"></a><a name="b133669241718"></a>port_range_min</strong> must be specified, and the <strong id="b123671729178"><a name="b123671729178"></a><a name="b123671729178"></a>port_range_max</strong> value must be greater than the <strong id="b33681231715"><a name="b33681231715"></a><a name="b33681231715"></a>port_range_min</strong> value.</p>
<p id="p4241072615417"><a name="p4241072615417"></a><a name="p4241072615417"></a>When the ICMP protocol is used, if you specify the ICMP code (<strong id="b172802494244"><a name="b172802494244"></a><a name="b172802494244"></a>port_range_max</strong>), you must also specify the ICMP type (<strong id="b192811249112415"><a name="b192811249112415"></a><a name="b192811249112415"></a>port_range_min</strong>).</p>
<p id="p543313212446"><a name="p543313212446"></a><a name="p543313212446"></a>The value ranges from 1 to 65535. (The value ranges from 0 to 255 when it indicates the code.)</p>
</td>
</tr>
<tr id="row360773491607"><td class="cellrowborder" valign="top" width="23.54%" headers="mcps1.2.5.1.1 "><p id="p364292801607"><a name="p364292801607"></a><a name="p364292801607"></a>ethertype</p>
</td>
<td class="cellrowborder" valign="top" width="11.72%" headers="mcps1.2.5.1.2 "><p id="p15741131719393"><a name="p15741131719393"></a><a name="p15741131719393"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p339523071607"><a name="p339523071607"></a><a name="p339523071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.2.5.1.4 "><p id="p34728681607"><a name="p34728681607"></a><a name="p34728681607"></a>Specifies the network type.</p>
<p id="p668771714614"><a name="p668771714614"></a><a name="p668771714614"></a>The value can be <strong id="b16467068257"><a name="b16467068257"></a><a name="b16467068257"></a>IPv4</strong> or <strong id="b44695618259"><a name="b44695618259"></a><a name="b44695618259"></a>IPv6</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section2023987716319"></a>

**Table  3**  Response parameter

<a name="table676552316319"></a>
<table><thead align="left"><tr id="row5032047016319"><th class="cellrowborder" valign="top" width="31.7%" id="mcps1.2.4.1.1"><p id="p4182747116319"><a name="p4182747116319"></a><a name="p4182747116319"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.4.1.2"><p id="p4264467116319"><a name="p4264467116319"></a><a name="p4264467116319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p4267558716319"><a name="p4267558716319"></a><a name="p4267558716319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60629616319"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.2.4.1.1 "><p id="p2428304416319"><a name="p2428304416319"></a><a name="p2428304416319"></a>security_group_rule</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p2724314316319"><a name="p2724314316319"></a><a name="p2724314316319"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p5745755316319"><a name="p5745755316319"></a><a name="p5745755316319"></a>Specifies the security group rule list. For details, see <a href="#table1794215178501">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Security Group Rule**  objects

<a name="table1794215178501"></a>
<table><thead align="left"><tr id="row594401765012"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p79441917145016"><a name="p79441917145016"></a><a name="p79441917145016"></a><strong id="b723315491294"><a name="b723315491294"></a><a name="b723315491294"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p189449173501"><a name="p189449173501"></a><a name="p189449173501"></a><strong id="b8145054192919"><a name="b8145054192919"></a><a name="b8145054192919"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p14944151714502"><a name="p14944151714502"></a><a name="p14944151714502"></a><strong id="b15244658122912"><a name="b15244658122912"></a><a name="b15244658122912"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row134774871607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p269083981607"><a name="p269083981607"></a><a name="p269083981607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p630670281607"><a name="p630670281607"></a><a name="p630670281607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p334792201607"><a name="p334792201607"></a><a name="p334792201607"></a>Specifies the security group rule ID.</p>
<p id="p529374054010"><a name="p529374054010"></a><a name="p529374054010"></a>This parameter is not mandatory when you query security group rules.</p>
</td>
</tr>
<tr id="row15944617165015"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p149461217195012"><a name="p149461217195012"></a><a name="p149461217195012"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p294641745013"><a name="p294641745013"></a><a name="p294641745013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p19946917105019"><a name="p19946917105019"></a><a name="p19946917105019"></a>Provides supplementary information about the security group rule.</p>
</td>
</tr>
<tr id="row894618172509"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p149461917175015"><a name="p149461917175015"></a><a name="p149461917175015"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p179460179503"><a name="p179460179503"></a><a name="p179460179503"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p59471117115010"><a name="p59471117115010"></a><a name="p59471117115010"></a>Specifies the ID of the belonged security group.</p>
</td>
</tr>
<tr id="row494711765015"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p5947517135014"><a name="p5947517135014"></a><a name="p5947517135014"></a>remote_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p18947817175013"><a name="p18947817175013"></a><a name="p18947817175013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p194821775015"><a name="p194821775015"></a><a name="p194821775015"></a>Specifies the peer ID of the belonged security group.</p>
</td>
</tr>
<tr id="row1394891775017"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p189481171504"><a name="p189481171504"></a><a name="p189481171504"></a>direction</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p99481417185012"><a name="p99481417185012"></a><a name="p99481417185012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1694851720506"><a name="p1694851720506"></a><a name="p1694851720506"></a>Specifies the direction of the traffic for which the security group rule takes effect.</p>
</td>
</tr>
<tr id="row1994812173503"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1294831745014"><a name="p1294831745014"></a><a name="p1294831745014"></a>remote_ip_prefix</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p19948171725018"><a name="p19948171725018"></a><a name="p19948171725018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p694881717507"><a name="p694881717507"></a><a name="p694881717507"></a>Specifies the peer IP address segment.</p>
</td>
</tr>
<tr id="row3948181714504"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p59488172505"><a name="p59488172505"></a><a name="p59488172505"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p69481317155019"><a name="p69481317155019"></a><a name="p69481317155019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1094871718506"><a name="p1094871718506"></a><a name="p1094871718506"></a>Specifies the protocol type or the IP protocol number.</p>
</td>
</tr>
<tr id="row189481317185015"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p14948417155013"><a name="p14948417155013"></a><a name="p14948417155013"></a>port_range_max</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p29484172505"><a name="p29484172505"></a><a name="p29484172505"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8948417135013"><a name="p8948417135013"></a><a name="p8948417135013"></a>Specifies the maximum port number. When ICMP is used, the value is the ICMP code.</p>
</td>
</tr>
<tr id="row10948131795018"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p13948191705018"><a name="p13948191705018"></a><a name="p13948191705018"></a>port_range_min</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p89497176506"><a name="p89497176506"></a><a name="p89497176506"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4949191713509"><a name="p4949191713509"></a><a name="p4949191713509"></a>Specifies the minimum port number. If the ICMP protocol is used, this parameter indicates the ICMP type.</p>
<p id="p594916176501"><a name="p594916176501"></a><a name="p594916176501"></a>When the TCP or UDP protocol is used, both <strong id="b143321341153211"><a name="b143321341153211"></a><a name="b143321341153211"></a>port_range_max</strong> and <strong id="b2333174111326"><a name="b2333174111326"></a><a name="b2333174111326"></a>port_range_min</strong> must be specified, and the <strong id="b133474120328"><a name="b133474120328"></a><a name="b133474120328"></a>port_range_max</strong> value must be greater than the <strong id="b633510416321"><a name="b633510416321"></a><a name="b633510416321"></a>port_range_min</strong> value.</p>
<p id="p189494172509"><a name="p189494172509"></a><a name="p189494172509"></a>When the ICMP protocol is used, if you specify the ICMP code (<strong id="b77795410321"><a name="b77795410321"></a><a name="b77795410321"></a>port_range_max</strong>), you must also specify the ICMP type (<strong id="b37935416325"><a name="b37935416325"></a><a name="b37935416325"></a>port_range_min</strong>).</p>
</td>
</tr>
<tr id="row159491817195016"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p89491817165011"><a name="p89491817165011"></a><a name="p89491817165011"></a>ethertype</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p5949617125012"><a name="p5949617125012"></a><a name="p5949617125012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1894915178504"><a name="p1894915178504"></a><a name="p1894915178504"></a>Specifies the network type.</p>
<p id="p1594961712508"><a name="p1594961712508"></a><a name="p1594961712508"></a>Only IPv4 is supported.</p>
</td>
</tr>
<tr id="row532124261607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p593368391607"><a name="p593368391607"></a><a name="p593368391607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p130282191607"><a name="p130282191607"></a><a name="p130282191607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row11992111863317"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p169261732143314"><a name="p169261732143314"></a><a name="p169261732143314"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p69311132153317"><a name="p69311132153317"></a><a name="p69311132153317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p103844191312"><a name="p103844191312"></a><a name="p103844191312"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row10903153923318"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p6634195714335"><a name="p6634195714335"></a><a name="p6634195714335"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p12638157153319"><a name="p12638157153319"></a><a name="p12638157153319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1364635713332"><a name="p1364635713332"></a><a name="p1364635713332"></a>Specifies the time (UTC) when the security group rule is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i56988266348"><a name="i56988266348"></a><a name="i56988266348"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1797311427338"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1725445103416"><a name="p1725445103416"></a><a name="p1725445103416"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p192601514345"><a name="p192601514345"></a><a name="p192601514345"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1127018513343"><a name="p1127018513343"></a><a name="p1127018513343"></a>Specifies the time (UTC) when the security group rule is updated.</p>
<p id="p11481521141510"><a name="p11481521141510"></a><a name="p11481521141510"></a>Format: <em id="i1368510366348"><a name="i1368510366348"></a><a name="i1368510366348"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section5025263616319"></a>

Example request

```
POST https://{Endpoint}/v2.0/security-group-rules

{
    "security_group_rule": {
        "security_group_id": "5cb9c1ee-00e0-4d0f-9623-55463cd26ff8", 
        "direction": "egress", 
        "protocol": "tcp", 
        "remote_ip_prefix": "10.10.0.0/24"
    }
}
```

Example response

```
{
    "security_group_rule": {
        "remote_group_id": null, 
        "direction": "egress", 
        "remote_ip_prefix": "10.10.0.0/24", 
        "protocol": "tcp", 
        "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f", 
        "port_range_max": null, 
        "security_group_id": "5cb9c1ee-00e0-4d0f-9623-55463cd26ff8", 
        "port_range_min": null, 
        "ethertype": "IPv4", 
        "description": null, 
        "id": "7c336b04-1603-4911-a6f4-f2af1d9a0488",
        "project_id": "6fbe9263116a4b68818cf1edce16bc4f", 
        "created_at": "2018-09-20T02:15:34",
        "updated_at": "2018-09-20T02:15:34"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

