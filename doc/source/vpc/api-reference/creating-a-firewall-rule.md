# Creating a Firewall Rule<a name="vpc_firewall_0003"></a>

## Function<a name="section3826619212329"></a>

This API is used to create a firewall rule.

## URI<a name="section2109482512329"></a>

POST /v2.0/fwaas/firewall\_rules

## Request Message<a name="section2533876012329"></a>

**Table  1**  Request parameter

<a name="table1879369612329"></a>
<table><thead align="left"><tr id="row34303012329"><th class="cellrowborder" valign="top" width="12.988701129887009%" id="mcps1.2.5.1.1"><p id="p1807949812329"><a name="p1807949812329"></a><a name="p1807949812329"></a><strong id="b51341458173310"><a name="b51341458173310"></a><a name="b51341458173310"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.98830116988301%" id="mcps1.2.5.1.2"><p id="p4218882212329"><a name="p4218882212329"></a><a name="p4218882212329"></a><strong id="b725495023311"><a name="b725495023311"></a><a name="b725495023311"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.347665233476654%" id="mcps1.2.5.1.3"><p id="p262059712329"><a name="p262059712329"></a><a name="p262059712329"></a><strong id="b1116162103414"><a name="b1116162103414"></a><a name="b1116162103414"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.675332466753325%" id="mcps1.2.5.1.4"><p id="p2622676712329"><a name="p2622676712329"></a><a name="p2622676712329"></a><strong id="b763219414341"><a name="b763219414341"></a><a name="b763219414341"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1636364712329"><td class="cellrowborder" valign="top" width="12.988701129887009%" headers="mcps1.2.5.1.1 "><p id="p3751930212329"><a name="p3751930212329"></a><a name="p3751930212329"></a>firewall_rule</p>
</td>
<td class="cellrowborder" valign="top" width="16.98830116988301%" headers="mcps1.2.5.1.2 "><p id="p1109711212329"><a name="p1109711212329"></a><a name="p1109711212329"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="23.347665233476654%" headers="mcps1.2.5.1.3 "><p id="p6089760312329"><a name="p6089760312329"></a><a name="p6089760312329"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="46.675332466753325%" headers="mcps1.2.5.1.4 "><p id="p61314665122957"><a name="p61314665122957"></a><a name="p61314665122957"></a>Specifies the firewall rule objects. For details, see <a href="#table38646929121127">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Firewall Rule**  objects

<a name="table38646929121127"></a>
<table><thead align="left"><tr id="row18263398121127"><th class="cellrowborder" valign="top" width="12.64%" id="mcps1.2.6.1.1"><p id="p2027461121127"><a name="p2027461121127"></a><a name="p2027461121127"></a><strong id="b3893165916359"><a name="b3893165916359"></a><a name="b3893165916359"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.2.6.1.2"><p id="p9927105296"><a name="p9927105296"></a><a name="p9927105296"></a><strong id="b1173719013617"><a name="b1173719013617"></a><a name="b1173719013617"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.05%" id="mcps1.2.6.1.3"><p id="p51747644121127"><a name="p51747644121127"></a><a name="p51747644121127"></a><strong id="b986514173618"><a name="b986514173618"></a><a name="b986514173618"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.58%" id="mcps1.2.6.1.4"><p id="p13528938121127"><a name="p13528938121127"></a><a name="p13528938121127"></a><strong id="b44644268114611"><a name="b44644268114611"></a><a name="b44644268114611"></a>Constraint</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.61%" id="mcps1.2.6.1.5"><p id="p12805757121127"><a name="p12805757121127"></a><a name="p12805757121127"></a><strong id="b2124186103620"><a name="b2124186103620"></a><a name="b2124186103620"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3417421121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p16296528121127"><a name="p16296528121127"></a><a name="p16296528121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p892151018292"><a name="p892151018292"></a><a name="p892151018292"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p52887833121127"><a name="p52887833121127"></a><a name="p52887833121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p12447583121127"><a name="p12447583121127"></a><a name="p12447583121127"></a>The value can contain a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p29399172121127"><a name="p29399172121127"></a><a name="p29399172121127"></a>Specifies the firewall rule name.</p>
<p id="p4331339102"><a name="p4331339102"></a><a name="p4331339102"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row33772147121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p62102623121127"><a name="p62102623121127"></a><a name="p62102623121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p718122992911"><a name="p718122992911"></a><a name="p718122992911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p30062050121127"><a name="p30062050121127"></a><a name="p30062050121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p32185140121127"><a name="p32185140121127"></a><a name="p32185140121127"></a>The value can contain a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p64485971121127"><a name="p64485971121127"></a><a name="p64485971121127"></a>Provides supplementary information about the firewall rule.</p>
<p id="p1224611561757"><a name="p1224611561757"></a><a name="p1224611561757"></a>The value can contain a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row66347377121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p7361769121127"><a name="p7361769121127"></a><a name="p7361769121127"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p42411831172914"><a name="p42411831172914"></a><a name="p42411831172914"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p50019959121127"><a name="p50019959121127"></a><a name="p50019959121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p49011438121127"><a name="p49011438121127"></a><a name="p49011438121127"></a>The value can be <strong id="b84235270620190"><a name="b84235270620190"></a><a name="b84235270620190"></a>TCP</strong>, <strong id="b84235270620198"><a name="b84235270620198"></a><a name="b84235270620198"></a>UDP</strong>, <strong id="b842352706201915"><a name="b842352706201915"></a><a name="b842352706201915"></a>ICMP</strong>, or a value ranging from 0 to 255.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p36897817121127"><a name="p36897817121127"></a><a name="p36897817121127"></a>Specifies the IP protocol.</p>
<p id="p1094663315110"><a name="p1094663315110"></a><a name="p1094663315110"></a>The value can be <strong id="b364462120396"><a name="b364462120396"></a><a name="b364462120396"></a>TCP</strong>, <strong id="b186441521133914"><a name="b186441521133914"></a><a name="b186441521133914"></a>UDP</strong>, <strong id="b1464412116398"><a name="b1464412116398"></a><a name="b1464412116398"></a>ICMP</strong>, or a value ranging from 0 to 255.</p>
</td>
</tr>
<tr id="row8703753121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p5943474121127"><a name="p5943474121127"></a><a name="p5943474121127"></a>source_port</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p268733211297"><a name="p268733211297"></a><a name="p268733211297"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p59206978121127"><a name="p59206978121127"></a><a name="p59206978121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p8739741121127"><a name="p8739741121127"></a><a name="p8739741121127"></a>The value can be an integer from 1 to 65535 or a port number range in the format of <strong id="b842352706202051"><a name="b842352706202051"></a><a name="b842352706202051"></a><em id="i842352697202059"><a name="i842352697202059"></a><a name="i842352697202059"></a>a</em>:<em id="i84235269720213"><a name="i84235269720213"></a><a name="i84235269720213"></a>b</em></strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p62826249121127"><a name="p62826249121127"></a><a name="p62826249121127"></a>Specifies the source port number or port number range.</p>
<p id="p15371666511"><a name="p15371666511"></a><a name="p15371666511"></a>The value can be an integer from 1 to 65535 or a port number range in the format of <strong id="b8882115094111"><a name="b8882115094111"></a><a name="b8882115094111"></a><em id="i88804505418"><a name="i88804505418"></a><a name="i88804505418"></a>a</em>:<em id="i28811350134119"><a name="i28811350134119"></a><a name="i28811350134119"></a>b</em></strong>.</p>
</td>
</tr>
<tr id="row52935496121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p12876203121127"><a name="p12876203121127"></a><a name="p12876203121127"></a>destination_port</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p19241934142919"><a name="p19241934142919"></a><a name="p19241934142919"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p66631365121127"><a name="p66631365121127"></a><a name="p66631365121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p34781596121127"><a name="p34781596121127"></a><a name="p34781596121127"></a>The value can be an integer from 1 to 65535 or a port number range in the format of <strong id="b18654632425"><a name="b18654632425"></a><a name="b18654632425"></a><em id="i76531031428"><a name="i76531031428"></a><a name="i76531031428"></a>a</em>:<em id="i18654173134220"><a name="i18654173134220"></a><a name="i18654173134220"></a>b</em></strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p66851026121127"><a name="p66851026121127"></a><a name="p66851026121127"></a>Specifies the destination port number or port number range.</p>
<p id="p193204108218"><a name="p193204108218"></a><a name="p193204108218"></a>The value can be an integer from 1 to 65535 or a port number range in the format of <strong id="b7419124574218"><a name="b7419124574218"></a><a name="b7419124574218"></a><em id="i7417134519427"><a name="i7417134519427"></a><a name="i7417134519427"></a>a</em>:<em id="i16418174517427"><a name="i16418174517427"></a><a name="i16418174517427"></a>b</em></strong>.</p>
</td>
</tr>
<tr id="row37973187121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p18090983121127"><a name="p18090983121127"></a><a name="p18090983121127"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p1733823692914"><a name="p1733823692914"></a><a name="p1733823692914"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p15064211121127"><a name="p15064211121127"></a><a name="p15064211121127"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p49923839121127"><a name="p49923839121127"></a><a name="p49923839121127"></a>The value can be <strong id="b21021914194316"><a name="b21021914194316"></a><a name="b21021914194316"></a>IPv4</strong> or <strong id="b510261424317"><a name="b510261424317"></a><a name="b510261424317"></a>IPv6</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p10402054121127"><a name="p10402054121127"></a><a name="p10402054121127"></a>Specifies the IP protocol version.</p>
<p id="p650618131322"><a name="p650618131322"></a><a name="p650618131322"></a>The value can be <strong id="b45255524316"><a name="b45255524316"></a><a name="b45255524316"></a>IPv4</strong> or <strong id="b85262057434"><a name="b85262057434"></a><a name="b85262057434"></a>IPv6</strong>.</p>
</td>
</tr>
<tr id="row34581454121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p61377852121127"><a name="p61377852121127"></a><a name="p61377852121127"></a>source_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p185623717291"><a name="p185623717291"></a><a name="p185623717291"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p36483585121127"><a name="p36483585121127"></a><a name="p36483585121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p16531353121127"><a name="p16531353121127"></a><a name="p16531353121127"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p31475962121127"><a name="p31475962121127"></a><a name="p31475962121127"></a>Specifies the source IP address or CIDR block.</p>
</td>
</tr>
<tr id="row13949121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p43901244121127"><a name="p43901244121127"></a><a name="p43901244121127"></a>destination_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p15707396299"><a name="p15707396299"></a><a name="p15707396299"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p14651426121127"><a name="p14651426121127"></a><a name="p14651426121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p8502527121127"><a name="p8502527121127"></a><a name="p8502527121127"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p53743554121127"><a name="p53743554121127"></a><a name="p53743554121127"></a>Specifies the destination IP address or CIDR block.</p>
</td>
</tr>
<tr id="row33223843121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p40131900121127"><a name="p40131900121127"></a><a name="p40131900121127"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p269614042916"><a name="p269614042916"></a><a name="p269614042916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p952780121127"><a name="p952780121127"></a><a name="p952780121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p13986437121127"><a name="p13986437121127"></a><a name="p13986437121127"></a>The value can be <strong id="b0147172819486"><a name="b0147172819486"></a><a name="b0147172819486"></a>DENY</strong> or <strong id="b2147122804813"><a name="b2147122804813"></a><a name="b2147122804813"></a>ALLOW</strong>. </p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p16135729121127"><a name="p16135729121127"></a><a name="p16135729121127"></a>Specifies action performed on traffic passing through the firewall.</p>
<p id="p053482914220"><a name="p053482914220"></a><a name="p053482914220"></a>The value can be <strong id="b133031547174416"><a name="b133031547174416"></a><a name="b133031547174416"></a>DENY</strong> or <strong id="b136911758164413"><a name="b136911758164413"></a><a name="b136911758164413"></a>ALLOW</strong>. </p>
</td>
</tr>
<tr id="row11398101121127"><td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.6.1.1 "><p id="p50347088121127"><a name="p50347088121127"></a><a name="p50347088121127"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.6.1.2 "><p id="p14932441202918"><a name="p14932441202918"></a><a name="p14932441202918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.2.6.1.3 "><p id="p46161809121127"><a name="p46161809121127"></a><a name="p46161809121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="24.58%" headers="mcps1.2.6.1.4 "><p id="p53180735121127"><a name="p53180735121127"></a><a name="p53180735121127"></a>The value can be <strong id="b3906124124820"><a name="b3906124124820"></a><a name="b3906124124820"></a>true</strong> or <strong id="b1190764134819"><a name="b1190764134819"></a><a name="b1190764134819"></a>false</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.6.1.5 "><p id="p57324252121127"><a name="p57324252121127"></a><a name="p57324252121127"></a>Specifies whether the firewall rule is enabled.</p>
<p id="p117941758725"><a name="p117941758725"></a><a name="p117941758725"></a>The value can be <strong id="b1652344674713"><a name="b1652344674713"></a><a name="b1652344674713"></a>true</strong> or <strong id="b46490559473"><a name="b46490559473"></a><a name="b46490559473"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section3990074312329"></a>

**Table  3**  Response parameter

<a name="table209507312329"></a>
<table><thead align="left"><tr id="row5536995412329"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p2706537512329"><a name="p2706537512329"></a><a name="p2706537512329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p5424121912329"><a name="p5424121912329"></a><a name="p5424121912329"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p1697811312329"><a name="p1697811312329"></a><a name="p1697811312329"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3190076212329"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p5714453912329"><a name="p5714453912329"></a><a name="p5714453912329"></a>firewall_rule</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p394121812329"><a name="p394121812329"></a><a name="p394121812329"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p3044429312329"><a name="p3044429312329"></a><a name="p3044429312329"></a>Specifies the firewall rule objects. For details, see <a href="#table96821221510">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Firewall Rule**  objects

<a name="table96821221510"></a>
<table><thead align="left"><tr id="row1568212181517"><th class="cellrowborder" valign="top" width="32.76%" id="mcps1.2.4.1.1"><p id="p8681812161514"><a name="p8681812161514"></a><a name="p8681812161514"></a><strong id="b4117730154919"><a name="b4117730154919"></a><a name="b4117730154919"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.4.1.2"><p id="p13681312131518"><a name="p13681312131518"></a><a name="p13681312131518"></a><strong id="b1240143111494"><a name="b1240143111494"></a><a name="b1240143111494"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.550000000000004%" id="mcps1.2.4.1.3"><p id="p116816121152"><a name="p116816121152"></a><a name="p116816121152"></a><strong id="b453523214915"><a name="b453523214915"></a><a name="b453523214915"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row39528007121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p7362024121127"><a name="p7362024121127"></a><a name="p7362024121127"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p53278848121127"><a name="p53278848121127"></a><a name="p53278848121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p13095685121127"><a name="p13095685121127"></a><a name="p13095685121127"></a>Specifies the UUID of the firewall rule.</p>
</td>
</tr>
<tr id="row1870712181518"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p2070121214156"><a name="p2070121214156"></a><a name="p2070121214156"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p570161218158"><a name="p570161218158"></a><a name="p570161218158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p2070171271514"><a name="p2070171271514"></a><a name="p2070171271514"></a>Specifies the firewall rule name.</p>
</td>
</tr>
<tr id="row47051241512"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1970141281520"><a name="p1970141281520"></a><a name="p1970141281520"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p67031271510"><a name="p67031271510"></a><a name="p67031271510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p1270412111511"><a name="p1270412111511"></a><a name="p1270412111511"></a>Provides supplementary information about the firewall rule.</p>
</td>
</tr>
<tr id="row39157453121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p40485546121127"><a name="p40485546121127"></a><a name="p40485546121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p20366062121127"><a name="p20366062121127"></a><a name="p20366062121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row13612334121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p3945861121127"><a name="p3945861121127"></a><a name="p3945861121127"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p53059091121127"><a name="p53059091121127"></a><a name="p53059091121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p46007536121127"><a name="p46007536121127"></a><a name="p46007536121127"></a>Specifies whether the firewall rule can be shared by different tenants.</p>
</td>
</tr>
<tr id="row2070312131513"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1570141241512"><a name="p1570141241512"></a><a name="p1570141241512"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p0701312161512"><a name="p0701312161512"></a><a name="p0701312161512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p17061201515"><a name="p17061201515"></a><a name="p17061201515"></a>Specifies the IP protocol.</p>
</td>
</tr>
<tr id="row1170181217153"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p12701112161517"><a name="p12701112161517"></a><a name="p12701112161517"></a>source_port</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p127021218159"><a name="p127021218159"></a><a name="p127021218159"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p137011241510"><a name="p137011241510"></a><a name="p137011241510"></a>Specifies the source port number or port number range.</p>
</td>
</tr>
<tr id="row8701112181514"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p470312191512"><a name="p470312191512"></a><a name="p470312191512"></a>destination_port</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p177081291516"><a name="p177081291516"></a><a name="p177081291516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p1770121217158"><a name="p1770121217158"></a><a name="p1770121217158"></a>Specifies the destination port number or port number range.</p>
</td>
</tr>
<tr id="row07071212159"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1370912131514"><a name="p1370912131514"></a><a name="p1370912131514"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p770212111514"><a name="p770212111514"></a><a name="p770212111514"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p13701112161518"><a name="p13701112161518"></a><a name="p13701112161518"></a>Specifies the IP protocol version.</p>
</td>
</tr>
<tr id="row1070171261513"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1970412151510"><a name="p1970412151510"></a><a name="p1970412151510"></a>source_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p14701812161510"><a name="p14701812161510"></a><a name="p14701812161510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p19701412201516"><a name="p19701412201516"></a><a name="p19701412201516"></a>Specifies the source IP address or CIDR block.</p>
</td>
</tr>
<tr id="row167031212158"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p77061219153"><a name="p77061219153"></a><a name="p77061219153"></a>destination_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p1870712131519"><a name="p1870712131519"></a><a name="p1870712131519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p1470712111516"><a name="p1470712111516"></a><a name="p1470712111516"></a>Specifies the destination IP address or CIDR block.</p>
</td>
</tr>
<tr id="row17051231516"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p13701512171516"><a name="p13701512171516"></a><a name="p13701512171516"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p871161221515"><a name="p871161221515"></a><a name="p871161221515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p87131291511"><a name="p87131291511"></a><a name="p87131291511"></a>Specifies action performed on traffic passing through the firewall.</p>
</td>
</tr>
<tr id="row571121210154"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1571712101514"><a name="p1571712101514"></a><a name="p1571712101514"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p137131218159"><a name="p137131218159"></a><a name="p137131218159"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p167121271512"><a name="p167121271512"></a><a name="p167121271512"></a>Specifies whether the firewall rule is enabled.</p>
</td>
</tr>
<tr id="row1574912215580"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1312116475819"><a name="p1312116475819"></a><a name="p1312116475819"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p5125543583"><a name="p5125543583"></a><a name="p5125543583"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p1528123115287"><a name="p1528123115287"></a><a name="p1528123115287"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section1765314912329"></a>

Example request

```
POST https://{Endpoint}/v2.0/fwaas/firewall_rules

{
    "firewall_rule": {
        "action": "allow", 
        "enabled": true, 
        "destination_port": "80", 
        "protocol": "tcp", 
        "name": "ALLOW_HTTP"
    }
}
```

Example response

```
{
    "firewall_rule": {
        "protocol": "tcp", 
        "description": "", 
        "source_ip_address": null, 
        "destination_ip_address": null, 
        "source_port": null, 
        "destination_port": "80", 
        "id": "b94acf06-efc2-485d-ba67-a61acf2a7e28", 
        "name": "ALLOW_HTTP", 
        "tenant_id": "23c8a121505047b6869edf39f3062712", 
        "enabled": true, 
        "action": "allow", 
        "ip_version": 4, 
        "public": false,
        "project_id": "23c8a121505047b6869edf39f3062712"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

