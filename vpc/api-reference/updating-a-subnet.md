# Updating a Subnet<a name="vpc_subnet02_0004"></a>

## Function<a name="section10267951"></a>

This API is used to update information about a subnet.

Restrictions

When updating the  **allocation\_pools**  field, neither gateway nor broadcast IP addresses can be included.

## URI<a name="section25302698"></a>

PUT /v2.0/subnets/\{subnet\_id\}

## Request Message<a name="section36252627"></a>

**Table  1**  Request parameter

<a name="table40701910"></a>
<table><thead align="left"><tr id="row5914937"><th class="cellrowborder" valign="top" width="17.67176717671767%" id="mcps1.2.5.1.1"><p id="p9347893"><a name="p9347893"></a><a name="p9347893"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.861286128612862%" id="mcps1.2.5.1.2"><p id="p18981865"><a name="p18981865"></a><a name="p18981865"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.09180918091809%" id="mcps1.2.5.1.3"><p id="p61136126"><a name="p61136126"></a><a name="p61136126"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="51.375137513751376%" id="mcps1.2.5.1.4"><p id="p53079196"><a name="p53079196"></a><a name="p53079196"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4447594"><td class="cellrowborder" valign="top" width="17.67176717671767%" headers="mcps1.2.5.1.1 "><p id="p24710800"><a name="p24710800"></a><a name="p24710800"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.2 "><p id="p55417783"><a name="p55417783"></a><a name="p55417783"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.2.5.1.3 "><p id="p59655430"><a name="p59655430"></a><a name="p59655430"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="51.375137513751376%" headers="mcps1.2.5.1.4 "><p id="p37955333"><a name="p37955333"></a><a name="p37955333"></a>Specifies the subnet list. For details, see <a href="#table12211980105515">Table 2</a>.</p>
<p id="p2265180"><a name="p2265180"></a><a name="p2265180"></a>You must specify at least one attribute when updating a subnet.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **subnet**  objects

<a name="table12211980105515"></a>
<table><thead align="left"><tr id="row32722637105515"><th class="cellrowborder" valign="top" width="24.93%" id="mcps1.2.5.1.1"><p id="p60075710105815"><a name="p60075710105815"></a><a name="p60075710105815"></a><strong id="b1960412388385"><a name="b1960412388385"></a><a name="b1960412388385"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.02%" id="mcps1.2.5.1.2"><p id="p194182022104514"><a name="p194182022104514"></a><a name="p194182022104514"></a><strong id="b1358373914383"><a name="b1358373914383"></a><a name="b1358373914383"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.93%" id="mcps1.2.5.1.3"><p id="p34294369105815"><a name="p34294369105815"></a><a name="p34294369105815"></a><strong id="b9825114083812"><a name="b9825114083812"></a><a name="b9825114083812"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.12%" id="mcps1.2.5.1.4"><p id="p25203839105815"><a name="p25203839105815"></a><a name="p25203839105815"></a><strong id="b37601241153816"><a name="b37601241153816"></a><a name="b37601241153816"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row43081158105515"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.1 "><p id="p54833166105624"><a name="p54833166105624"></a><a name="p54833166105624"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.5.1.2 "><p id="p11418162219452"><a name="p11418162219452"></a><a name="p11418162219452"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.3 "><p id="p12301465105624"><a name="p12301465105624"></a><a name="p12301465105624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38.12%" headers="mcps1.2.5.1.4 "><p id="p14797472105624"><a name="p14797472105624"></a><a name="p14797472105624"></a>Specifies the subnet name.</p>
</td>
</tr>
<tr id="row2545218105647"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.1 "><p id="p1395064410577"><a name="p1395064410577"></a><a name="p1395064410577"></a>allocation_pools</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.5.1.2 "><p id="p19418122284515"><a name="p19418122284515"></a><a name="p19418122284515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.3 "><p id="p5626034310577"><a name="p5626034310577"></a><a name="p5626034310577"></a>Array of <a href="#table24611730">allocation_pool</a> objects</p>
<p id="p3658104710577"><a name="p3658104710577"></a><a name="p3658104710577"></a></p>
</td>
<td class="cellrowborder" valign="top" width="38.12%" headers="mcps1.2.5.1.4 "><p id="p2390980910577"><a name="p2390980910577"></a><a name="p2390980910577"></a>Specifies the available IP address pool. For details about the <strong id="b842352706192134"><a name="b842352706192134"></a><a name="b842352706192134"></a>allocation_pool</strong> objects, see <a href="#table24611730">Table 3</a>.</p>
<p id="p1386169010577"><a name="p1386169010577"></a><a name="p1386169010577"></a>Example: [ { "start": "10.0.0.2", "end": "10.0.0.251"} ]</p>
<p id="p1961191927"><a name="p1961191927"></a><a name="p1961191927"></a>The last three and the first IP addresses in each subnet are the ones reserved by the system. For example, in subnet <strong id="b10846899393"><a name="b10846899393"></a><a name="b10846899393"></a>192.168.1.0/24</strong>, IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved by the system. By default, the IP addresses reserved by the system are not in the IP address pool specified by <strong id="b766815245395"><a name="b766815245395"></a><a name="b766815245395"></a>allocation_pool</strong>.</p>
<p id="p5764635410577"><a name="p5764635410577"></a><a name="p5764635410577"></a>When updating an IP address pool, the <strong id="b182341927123916"><a name="b182341927123916"></a><a name="b182341927123916"></a>allocation_pool</strong> value can contain neither gateway nor broadcast IP addresses. </p>
</td>
</tr>
<tr id="row22360302105653"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.1 "><p id="p1404384110577"><a name="p1404384110577"></a><a name="p1404384110577"></a>dns_nameservers</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.5.1.2 "><p id="p2418922154512"><a name="p2418922154512"></a><a name="p2418922154512"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.3 "><p id="p6380932110577"><a name="p6380932110577"></a><a name="p6380932110577"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="38.12%" headers="mcps1.2.5.1.4 "><p id="p324929310577"><a name="p324929310577"></a><a name="p324929310577"></a>Specifies the DNS server address.</p>
<p id="p1218711851714"><a name="p1218711851714"></a><a name="p1218711851714"></a>Instructions:</p>
<p id="p2924364410577"><a name="p2924364410577"></a><a name="p2924364410577"></a>Example: "dns_nameservers": ["8.xx.xx.8","8.xx.xx.4"]</p>
<p id="p1294111141716"><a name="p1294111141716"></a><a name="p1294111141716"></a>A maximum of five DNS server addresses are supported.</p>
</td>
</tr>
<tr id="row17847900105653"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.1 "><p id="p4510693110577"><a name="p4510693110577"></a><a name="p4510693110577"></a>host_routes</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.5.1.2 "><p id="p3418112264518"><a name="p3418112264518"></a><a name="p3418112264518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.3 "><p id="p166911588244"><a name="p166911588244"></a><a name="p166911588244"></a>Array of <a href="#table5232330">host_route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="38.12%" headers="mcps1.2.5.1.4 "><p id="p2002497710577"><a name="p2002497710577"></a><a name="p2002497710577"></a>Specifies the static VM routes. For details, see <a href="#table5232330">Table 4</a>.</p>
<p id="p4600706610577"><a name="p4600706610577"></a><a name="p4600706610577"></a>Static routes are not supported, and entered information will be ignored.</p>
</td>
</tr>
<tr id="row21625046105653"><td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.1 "><p id="p4495318510577"><a name="p4495318510577"></a><a name="p4495318510577"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="12.02%" headers="mcps1.2.5.1.2 "><p id="p1041812214516"><a name="p1041812214516"></a><a name="p1041812214516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.93%" headers="mcps1.2.5.1.3 "><p id="p1732939410577"><a name="p1732939410577"></a><a name="p1732939410577"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="38.12%" headers="mcps1.2.5.1.4 "><p id="p2100438810577"><a name="p2100438810577"></a><a name="p2100438810577"></a>Specifies whether to enable the DHCP function. Value <strong id="b19658165919430"><a name="b19658165919430"></a><a name="b19658165919430"></a>false</strong> indicates that the DHCP function is not enabled.</p>
<p id="p5482176910577"><a name="p5482176910577"></a><a name="p5482176910577"></a>The value can only be <strong id="b5528126184513"><a name="b5528126184513"></a><a name="b5528126184513"></a>true</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **allocation\_pool**  objects

<a name="table24611730"></a>
<table><thead align="left"><tr id="row15154020"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.2.5.1.1"><p id="p19516075"><a name="p19516075"></a><a name="p19516075"></a><strong id="b168601438114519"><a name="b168601438114519"></a><a name="b168601438114519"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.7%" id="mcps1.2.5.1.2"><p id="p1327122842316"><a name="p1327122842316"></a><a name="p1327122842316"></a><strong id="b1410411408459"><a name="b1410411408459"></a><a name="b1410411408459"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.5.1.3"><p id="p37298263"><a name="p37298263"></a><a name="p37298263"></a><strong id="b13407164174516"><a name="b13407164174516"></a><a name="b13407164174516"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.339999999999996%" id="mcps1.2.5.1.4"><p id="p15727687"><a name="p15727687"></a><a name="p15727687"></a><strong id="b1512154218453"><a name="b1512154218453"></a><a name="b1512154218453"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7331458"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.5.1.1 "><p id="p56977217"><a name="p56977217"></a><a name="p56977217"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="14.7%" headers="mcps1.2.5.1.2 "><p id="p227112286236"><a name="p227112286236"></a><a name="p227112286236"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.3 "><p id="p51751889"><a name="p51751889"></a><a name="p51751889"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.5.1.4 "><p id="p51610228"><a name="p51610228"></a><a name="p51610228"></a>Specifies the start IP address of a network pool.</p>
</td>
</tr>
<tr id="row61838871"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.5.1.1 "><p id="p42892680"><a name="p42892680"></a><a name="p42892680"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="14.7%" headers="mcps1.2.5.1.2 "><p id="p1727314281237"><a name="p1727314281237"></a><a name="p1727314281237"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.3 "><p id="p51755094"><a name="p51755094"></a><a name="p51755094"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.339999999999996%" headers="mcps1.2.5.1.4 "><p id="p10006650"><a name="p10006650"></a><a name="p10006650"></a>Specifies the end IP address of a network pool.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **host\_route**  objects

<a name="table5232330"></a>
<table><thead align="left"><tr id="row65973637"><th class="cellrowborder" valign="top" width="21.55%" id="mcps1.2.5.1.1"><p id="p42264412"><a name="p42264412"></a><a name="p42264412"></a><strong id="b14654153617462"><a name="b14654153617462"></a><a name="b14654153617462"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.649999999999999%" id="mcps1.2.5.1.2"><p id="p197406419246"><a name="p197406419246"></a><a name="p197406419246"></a><strong id="b9401337154614"><a name="b9401337154614"></a><a name="b9401337154614"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.63%" id="mcps1.2.5.1.3"><p id="p865310"><a name="p865310"></a><a name="p865310"></a><strong id="b14292038174615"><a name="b14292038174615"></a><a name="b14292038174615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.17%" id="mcps1.2.5.1.4"><p id="p31641985"><a name="p31641985"></a><a name="p31641985"></a><strong id="b214343904610"><a name="b214343904610"></a><a name="b214343904610"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16342414"><td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.5.1.1 "><p id="p48667192"><a name="p48667192"></a><a name="p48667192"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p181671451247"><a name="p181671451247"></a><a name="p181671451247"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63%" headers="mcps1.2.5.1.3 "><p id="p49728507"><a name="p49728507"></a><a name="p49728507"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.17%" headers="mcps1.2.5.1.4 "><p id="p28535525"><a name="p28535525"></a><a name="p28535525"></a>Specifies the destination subnet of a route.</p>
</td>
</tr>
<tr id="row55493137"><td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.5.1.1 "><p id="p65759080"><a name="p65759080"></a><a name="p65759080"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p174054102412"><a name="p174054102412"></a><a name="p174054102412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63%" headers="mcps1.2.5.1.3 "><p id="p24885284"><a name="p24885284"></a><a name="p24885284"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.17%" headers="mcps1.2.5.1.4 "><p id="p51086148"><a name="p51086148"></a><a name="p51086148"></a>Specifies the next-hop IP address of a route.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section57838187"></a>

**Table  5**  Response parameter

<a name="table49261880"></a>
<table><thead align="left"><tr id="row31386613"><th class="cellrowborder" valign="top" width="31.7%" id="mcps1.2.4.1.1"><p id="p59287744"><a name="p59287744"></a><a name="p59287744"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.4.1.2"><p id="p37577972"><a name="p37577972"></a><a name="p37577972"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p58217140"><a name="p58217140"></a><a name="p58217140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17967889"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.2.4.1.1 "><p id="p46112886"><a name="p46112886"></a><a name="p46112886"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p44156300"><a name="p44156300"></a><a name="p44156300"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p522217"><a name="p522217"></a><a name="p522217"></a>Specifies the subnet list. For details, see <a href="#table176735992713">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **subnet**  objects

<a name="table176735992713"></a>
<table><thead align="left"><tr id="row176713593276"><th class="cellrowborder" valign="top" width="28.332833283328334%" id="mcps1.2.4.1.1"><p id="p136755912715"><a name="p136755912715"></a><a name="p136755912715"></a><strong id="b15294115864614"><a name="b15294115864614"></a><a name="b15294115864614"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.332833283328334%" id="mcps1.2.4.1.2"><p id="p667105912718"><a name="p667105912718"></a><a name="p667105912718"></a><strong id="b1593719598461"><a name="b1593719598461"></a><a name="b1593719598461"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.33433343334334%" id="mcps1.2.4.1.3"><p id="p26855915275"><a name="p26855915275"></a><a name="p26855915275"></a><strong id="b1678270124720"><a name="b1678270124720"></a><a name="b1678270124720"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28303131105515"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p2014344105614"><a name="p2014344105614"></a><a name="p2014344105614"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p28944191105614"><a name="p28944191105614"></a><a name="p28944191105614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p53796361105614"><a name="p53796361105614"></a><a name="p53796361105614"></a>Specifies the subnet ID.</p>
<p id="p2677113954519"><a name="p2677113954519"></a><a name="p2677113954519"></a>This parameter is not mandatory when you query subnets.</p>
</td>
</tr>
<tr id="row1868135972719"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p37015595272"><a name="p37015595272"></a><a name="p37015595272"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p18706591271"><a name="p18706591271"></a><a name="p18706591271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p1870259172715"><a name="p1870259172715"></a><a name="p1870259172715"></a>Specifies the subnet name.</p>
</td>
</tr>
<tr id="row670165910271"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p187012596279"><a name="p187012596279"></a><a name="p187012596279"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p137095922720"><a name="p137095922720"></a><a name="p137095922720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p870155932715"><a name="p870155932715"></a><a name="p870155932715"></a>Specifies the IP address version.</p>
<p id="p10708598273"><a name="p10708598273"></a><a name="p10708598273"></a>Only IPv4 address is supported.</p>
</td>
</tr>
<tr id="row1270135915274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1770105919271"><a name="p1770105919271"></a><a name="p1770105919271"></a>ipv6_address_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p1370205912279"><a name="p1370205912279"></a><a name="p1370205912279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p5701759142713"><a name="p5701759142713"></a><a name="p5701759142713"></a>Specifies the IPv6 addressing mode.</p>
</td>
</tr>
<tr id="row57075913279"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p070195972715"><a name="p070195972715"></a><a name="p070195972715"></a>ipv6_ra_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p1970559102716"><a name="p1970559102716"></a><a name="p1970559102716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p19701959152712"><a name="p19701959152712"></a><a name="p19701959152712"></a>Specifies the IPv6 route broadcast mode.</p>
</td>
</tr>
<tr id="row970185911274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p5719599271"><a name="p5719599271"></a><a name="p5719599271"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p1671105982710"><a name="p1671105982710"></a><a name="p1671105982710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p1071259102716"><a name="p1071259102716"></a><a name="p1071259102716"></a>Specifies the ID of the network to which the subnet belongs.</p>
</td>
</tr>
<tr id="row9711659142718"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1471155922712"><a name="p1471155922712"></a><a name="p1471155922712"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p1871155912279"><a name="p1871155912279"></a><a name="p1871155912279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p471115972720"><a name="p471115972720"></a><a name="p471115972720"></a>Specifies the CIDR format.</p>
<p id="p171105952717"><a name="p171105952717"></a><a name="p171105952717"></a>Only the addresses in the 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 network segments are supported. In addition, the subnet mask cannot be greater than 28. </p>
</td>
</tr>
<tr id="row373659122718"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p173195914274"><a name="p173195914274"></a><a name="p173195914274"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p16733594272"><a name="p16733594272"></a><a name="p16733594272"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p167319597276"><a name="p167319597276"></a><a name="p167319597276"></a>The gateway IP address cannot conflict with IP addresses configured for <strong id="b517545917470"><a name="b517545917470"></a><a name="b517545917470"></a>allocation_pools</strong>.</p>
<p id="p1773175918271"><a name="p1773175918271"></a><a name="p1773175918271"></a>This attribute cannot be modified. </p>
</td>
</tr>
<tr id="row6733598278"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p37325918273"><a name="p37325918273"></a><a name="p37325918273"></a>allocation_pools</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p974125918276"><a name="p974125918276"></a><a name="p974125918276"></a>Array of <a href="#table1777145918276">allocation_pool</a> objects</p>
<p id="p107495982715"><a name="p107495982715"></a><a name="p107495982715"></a></p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p13740597271"><a name="p13740597271"></a><a name="p13740597271"></a>Specifies the available IP address pool. For details, see the <strong id="b75841341562"><a name="b75841341562"></a><a name="b75841341562"></a>allocation_pool</strong> objects.</p>
<p id="p8891441195814"><a name="p8891441195814"></a><a name="p8891441195814"></a><a href="#table1777145918276">Table 7</a></p>
<p id="p137415915279"><a name="p137415915279"></a><a name="p137415915279"></a>Example: [ { "start": "10.0.0.2", "end": "10.0.0.251"} ]</p>
<p id="p167414592279"><a name="p167414592279"></a><a name="p167414592279"></a>The last three and the first IP addresses in each subnet are the ones reserved by the system. For example, in subnet <strong id="b160218147560"><a name="b160218147560"></a><a name="b160218147560"></a>192.168.1.0/24</strong>, IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved by the system. By default, the IP addresses reserved by the system are not in the IP address pool specified by <strong id="b1632291717563"><a name="b1632291717563"></a><a name="b1632291717563"></a>allocation_pool</strong>.</p>
<p id="p074359192720"><a name="p074359192720"></a><a name="p074359192720"></a>When updating an IP address pool, the <strong id="b258412115618"><a name="b258412115618"></a><a name="b258412115618"></a>allocation_pool</strong> value can contain neither gateway nor broadcast IP addresses. </p>
</td>
</tr>
<tr id="row474205911270"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p774105972720"><a name="p774105972720"></a><a name="p774105972720"></a>dns_nameservers</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p1474155952710"><a name="p1474155952710"></a><a name="p1474155952710"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p10743593273"><a name="p10743593273"></a><a name="p10743593273"></a>Specifies the DNS server address.</p>
<p id="p97485912712"><a name="p97485912712"></a><a name="p97485912712"></a>Example: "dns_nameservers": ["8.xx.xx.8","8.xx.xx.4"]</p>
</td>
</tr>
<tr id="row6741659182714"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p574959122713"><a name="p574959122713"></a><a name="p574959122713"></a>host_routes</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p3169174310293"><a name="p3169174310293"></a><a name="p3169174310293"></a>Array of <a href="#table177865912715">host_route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p2074459132712"><a name="p2074459132712"></a><a name="p2074459132712"></a>Specifies the static VM routes. For details, see <a href="#table177865912715">Table 8</a>.</p>
<p id="p1674359172717"><a name="p1674359172717"></a><a name="p1674359172717"></a>Static routes are not supported, and entered information will be ignored.</p>
</td>
</tr>
<tr id="row42017779105653"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p5182838910577"><a name="p5182838910577"></a><a name="p5182838910577"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p3734998010577"><a name="p3734998010577"></a><a name="p3734998010577"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row97535914274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p475959202718"><a name="p475959202718"></a><a name="p475959202718"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p2755596279"><a name="p2755596279"></a><a name="p2755596279"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p47595962710"><a name="p47595962710"></a><a name="p47595962710"></a>Specifies whether to enable the DHCP function. Value <strong id="b2789114445716"><a name="b2789114445716"></a><a name="b2789114445716"></a>false</strong> indicates that the DHCP function is not enabled.</p>
<p id="p57535914276"><a name="p57535914276"></a><a name="p57535914276"></a>The value can only be <strong id="b1694831813588"><a name="b1694831813588"></a><a name="b1694831813588"></a>true</strong>.</p>
</td>
</tr>
<tr id="row63315321123"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p45641422124917"><a name="p45641422124917"></a><a name="p45641422124917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p16855104462516"><a name="p16855104462516"></a><a name="p16855104462516"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row126291040191211"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the subnet is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i510913620586"><a name="i510913620586"></a><a name="i510913620586"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1084513362123"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.33433343334334%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the subnet is updated.</p>
<p id="p173172815471"><a name="p173172815471"></a><a name="p173172815471"></a>Format: <em id="i472475555813"><a name="i472475555813"></a><a name="i472475555813"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  7** **allocation\_pool**  objects

<a name="table1777145918276"></a>
<table><thead align="left"><tr id="row11772597275"><th class="cellrowborder" valign="top" width="23.65%" id="mcps1.2.4.1.1"><p id="p1477155962713"><a name="p1477155962713"></a><a name="p1477155962713"></a><strong id="b637355845814"><a name="b637355845814"></a><a name="b637355845814"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.610000000000003%" id="mcps1.2.4.1.2"><p id="p1077859162717"><a name="p1077859162717"></a><a name="p1077859162717"></a><strong id="b35811459165818"><a name="b35811459165818"></a><a name="b35811459165818"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.739999999999995%" id="mcps1.2.4.1.3"><p id="p5771159182718"><a name="p5771159182718"></a><a name="p5771159182718"></a><strong id="b63661801594"><a name="b63661801594"></a><a name="b63661801594"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row167785982711"><td class="cellrowborder" valign="top" width="23.65%" headers="mcps1.2.4.1.1 "><p id="p1077159182720"><a name="p1077159182720"></a><a name="p1077159182720"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="24.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p2077125912718"><a name="p2077125912718"></a><a name="p2077125912718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p2078205910275"><a name="p2078205910275"></a><a name="p2078205910275"></a>Specifies the start IP address of a network pool.</p>
</td>
</tr>
<tr id="row1782594271"><td class="cellrowborder" valign="top" width="23.65%" headers="mcps1.2.4.1.1 "><p id="p9781459162717"><a name="p9781459162717"></a><a name="p9781459162717"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="24.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p1778115952719"><a name="p1778115952719"></a><a name="p1778115952719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p187825911271"><a name="p187825911271"></a><a name="p187825911271"></a>Specifies the end IP address of a network pool.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **host\_route**  objects

<a name="table177865912715"></a>
<table><thead align="left"><tr id="row1779145992719"><th class="cellrowborder" valign="top" width="23.712371237123715%" id="mcps1.2.4.1.1"><p id="p2794593271"><a name="p2794593271"></a><a name="p2794593271"></a><strong id="b1450763595914"><a name="b1450763595914"></a><a name="b1450763595914"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.4024402440244%" id="mcps1.2.4.1.2"><p id="p14791594271"><a name="p14791594271"></a><a name="p14791594271"></a><strong id="b573083611594"><a name="b573083611594"></a><a name="b573083611594"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.88518851885189%" id="mcps1.2.4.1.3"><p id="p14791459172716"><a name="p14791459172716"></a><a name="p14791459172716"></a><strong id="b1863623745913"><a name="b1863623745913"></a><a name="b1863623745913"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1379165919277"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.2.4.1.1 "><p id="p979165972710"><a name="p979165972710"></a><a name="p979165972710"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="24.4024402440244%" headers="mcps1.2.4.1.2 "><p id="p37995952710"><a name="p37995952710"></a><a name="p37995952710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88518851885189%" headers="mcps1.2.4.1.3 "><p id="p10791559172714"><a name="p10791559172714"></a><a name="p10791559172714"></a>Specifies the destination subnet of a route.</p>
</td>
</tr>
<tr id="row1779185915279"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.2.4.1.1 "><p id="p6791359102719"><a name="p6791359102719"></a><a name="p6791359102719"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="24.4024402440244%" headers="mcps1.2.4.1.2 "><p id="p107935942717"><a name="p107935942717"></a><a name="p107935942717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88518851885189%" headers="mcps1.2.4.1.3 "><p id="p87975920278"><a name="p87975920278"></a><a name="p87975920278"></a>Specifies the next-hop IP address of a route.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section5055526711495"></a>

Example request

```
PUT https://{Endpoint}/v2.0/subnets/98bac90c-0ba7-4a63-8995-097da9bead1c  

{
  "subnet": {
    "name": "subnet-test"
  }
}
```

Example response

```
{
    "subnet": {
        "name": "subnet-test",
        "cidr": "172.16.2.0/24",
        "id": "98bac90c-0ba7-4a63-8995-097da9bead1c",
        "enable_dhcp": true,
        "network_id": "0133cd73-34d4-4d4c-bf1f-e65b24603206",
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "dns_nameservers": [],
        "allocation_pools": [
            {
                "start": "172.16.2.2",
                "end": "172.16.2.251"
            }
        ],
        "host_routes": [],
        "ip_version": 4,
        "gateway_ip": "172.16.2.1",
        "created_at": "2018-09-20T02:02:16",
        "updated_at": "2018-09-20T02:03:03"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

