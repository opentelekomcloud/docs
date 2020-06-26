# Querying Firewall Rules<a name="vpc_firewall_0001"></a>

## Function<a name="section32978392122541"></a>

This API is used to query all firewall rules accessible to the tenant submitting the request. 

## URI<a name="section11642292122541"></a>

GET /v2.0/fwaas/firewall\_rules

Example:

```
GET https://{Endpoint}/v2.0/fwaas/firewall_rules?name={firewall_rule_name}&tenant_id={tenant_id}&public={is_public}&protocol={protocol}&ip_version={ip_version}&action={action}&enabled={is_enabled}
```

Example of querying rules by page

```
GET https://{Endpoint}/v2.0/fwaas/firewall_rules?limit=2&marker=2a193015-4a88-4aa1-84ad-d4955adae707&page_reverse=False
```

[Table 1](#table997509428)  describes the parameters.

**Table  1**  Parameter description

<a name="table997509428"></a>
<table><thead align="left"><tr id="row11137135094218"><th class="cellrowborder" valign="top" width="14.72147214721472%" id="mcps1.2.5.1.1"><p id="p91372500429"><a name="p91372500429"></a><a name="p91372500429"></a><strong id="b10992125015714"><a name="b10992125015714"></a><a name="b10992125015714"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.64216421642164%" id="mcps1.2.5.1.2"><p id="p20137350164218"><a name="p20137350164218"></a><a name="p20137350164218"></a><strong id="b11301526712"><a name="b11301526712"></a><a name="b11301526712"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.8017801780178%" id="mcps1.2.5.1.3"><p id="p1913719500427"><a name="p1913719500427"></a><a name="p1913719500427"></a><strong id="b459514532714"><a name="b459514532714"></a><a name="b459514532714"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.83458345834583%" id="mcps1.2.5.1.4"><p id="p2137125013423"><a name="p2137125013423"></a><a name="p2137125013423"></a><strong id="b152910552719"><a name="b152910552719"></a><a name="b152910552719"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10137165064216"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p171379507423"><a name="p171379507423"></a><a name="p171379507423"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p141378503428"><a name="p141378503428"></a><a name="p141378503428"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p5137450184219"><a name="p5137450184219"></a><a name="p5137450184219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p1013785017424"><a name="p1013785017424"></a><a name="p1013785017424"></a>Specifies that the network ACL ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row313725054217"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p8137135074211"><a name="p8137135074211"></a><a name="p8137135074211"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p14137175064212"><a name="p14137175064212"></a><a name="p14137175064212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p171372050114214"><a name="p171372050114214"></a><a name="p171372050114214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p141374506425"><a name="p141374506425"></a><a name="p141374506425"></a>Specifies that the network ACL name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1813745044211"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p9137175094217"><a name="p9137175094217"></a><a name="p9137175094217"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p18137175015420"><a name="p18137175015420"></a><a name="p18137175015420"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p213715024219"><a name="p213715024219"></a><a name="p213715024219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p1913775016422"><a name="p1913775016422"></a><a name="p1913775016422"></a>Specifies that the network ACL description is used as the filtering condition.</p>
</td>
</tr>
<tr id="row61371650194212"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p1213825054216"><a name="p1213825054216"></a><a name="p1213825054216"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p313815504428"><a name="p313815504428"></a><a name="p313815504428"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p7138165014214"><a name="p7138165014214"></a><a name="p7138165014214"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p5526124316"><a name="p5526124316"></a><a name="p5526124316"></a>Specifies that the IP address version is used as the filtering condition.</p>
<p id="p121381950174212"><a name="p121381950174212"></a><a name="p121381950174212"></a>The value can be <strong id="b57616211365"><a name="b57616211365"></a><a name="b57616211365"></a>4</strong> (IPv4) or <strong id="b5761829368"><a name="b5761829368"></a><a name="b5761829368"></a>6</strong> (IPv6).</p>
</td>
</tr>
<tr id="row12138195084219"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p161385503424"><a name="p161385503424"></a><a name="p161385503424"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p313855094219"><a name="p313855094219"></a><a name="p313855094219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p13138145015423"><a name="p13138145015423"></a><a name="p13138145015423"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p167111932438"><a name="p167111932438"></a><a name="p167111932438"></a>Specifies that the network ACL action is used as the filtering condition.</p>
<p id="p13138135016424"><a name="p13138135016424"></a><a name="p13138135016424"></a>The value can be <strong id="b13939151601215"><a name="b13939151601215"></a><a name="b13939151601215"></a>allow</strong> or <strong id="b11939111671216"><a name="b11939111671216"></a><a name="b11939111671216"></a>deny</strong>.</p>
</td>
</tr>
<tr id="row131381450164218"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p1713811507429"><a name="p1713811507429"></a><a name="p1713811507429"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p13138145094212"><a name="p13138145094212"></a><a name="p13138145094212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p17138350194215"><a name="p17138350194215"></a><a name="p17138350194215"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p1564520515432"><a name="p1564520515432"></a><a name="p1564520515432"></a>Specifies that the network ACL rule is enabled is used as the filtering condition.</p>
<p id="p513820509425"><a name="p513820509425"></a><a name="p513820509425"></a>The value can be <strong id="b156671052161214"><a name="b156671052161214"></a><a name="b156671052161214"></a>true</strong> or <strong id="b0667165216123"><a name="b0667165216123"></a><a name="b0667165216123"></a>false</strong>.</p>
</td>
</tr>
<tr id="row9138450124210"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p1138145015421"><a name="p1138145015421"></a><a name="p1138145015421"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p713855094216"><a name="p713855094216"></a><a name="p713855094216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p2138155019429"><a name="p2138155019429"></a><a name="p2138155019429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p61381650184213"><a name="p61381650184213"></a><a name="p61381650184213"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row013818506422"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p613817506423"><a name="p613817506423"></a><a name="p613817506423"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p1513817501420"><a name="p1513817501420"></a><a name="p1513817501420"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p14138450134211"><a name="p14138450134211"></a><a name="p14138450134211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p15138165064212"><a name="p15138165064212"></a><a name="p15138165064212"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row813815500428"><td class="cellrowborder" valign="top" width="14.72147214721472%" headers="mcps1.2.5.1.1 "><p id="p813825014428"><a name="p813825014428"></a><a name="p813825014428"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="21.64216421642164%" headers="mcps1.2.5.1.2 "><p id="p5138155015425"><a name="p5138155015425"></a><a name="p5138155015425"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.8017801780178%" headers="mcps1.2.5.1.3 "><p id="p41381750124216"><a name="p41381750124216"></a><a name="p41381750124216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.83458345834583%" headers="mcps1.2.5.1.4 "><p id="p491518711431"><a name="p491518711431"></a><a name="p491518711431"></a>Specifies the number of records on each page.</p>
<p id="p161381350114216"><a name="p161381350114216"></a><a name="p161381350114216"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section16626865122541"></a>

None

## Response Message<a name="section39494421122541"></a>

**Table  2**  Response parameter

<a name="table48261844122541"></a>
<table><thead align="left"><tr id="row41263599122541"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p23207162122541"><a name="p23207162122541"></a><a name="p23207162122541"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.4.1.2"><p id="p46617019122541"><a name="p46617019122541"></a><a name="p46617019122541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.540000000000006%" id="mcps1.2.4.1.3"><p id="p38363364122541"><a name="p38363364122541"></a><a name="p38363364122541"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34200971122541"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p34822248122541"><a name="p34822248122541"></a><a name="p34822248122541"></a>firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.4.1.2 "><p id="p125656569422"><a name="p125656569422"></a><a name="p125656569422"></a>Array of <a href="#table38646929121127">Firewall Rule</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="59.540000000000006%" headers="mcps1.2.4.1.3 "><p id="p24293772122541"><a name="p24293772122541"></a><a name="p24293772122541"></a>Specifies the firewall rule list. For details, see <a href="#table38646929121127">Table 3</a>. </p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Firewall Rule**  objects

<a name="table38646929121127"></a>
<table><thead align="left"><tr id="row18263398121127"><th class="cellrowborder" valign="top" width="32.76%" id="mcps1.2.4.1.1"><p id="p2027461121127"><a name="p2027461121127"></a><a name="p2027461121127"></a><strong id="b1292213354594"><a name="b1292213354594"></a><a name="b1292213354594"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.69%" id="mcps1.2.4.1.2"><p id="p51747644121127"><a name="p51747644121127"></a><a name="p51747644121127"></a><strong id="b19181113735917"><a name="b19181113735917"></a><a name="b19181113735917"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.550000000000004%" id="mcps1.2.4.1.3"><p id="p12805757121127"><a name="p12805757121127"></a><a name="p12805757121127"></a><strong id="b138496378592"><a name="b138496378592"></a><a name="b138496378592"></a>Description</strong></p>
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
<tr id="row3417421121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p16296528121127"><a name="p16296528121127"></a><a name="p16296528121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p52887833121127"><a name="p52887833121127"></a><a name="p52887833121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p29399172121127"><a name="p29399172121127"></a><a name="p29399172121127"></a>Specifies the firewall rule name.</p>
</td>
</tr>
<tr id="row33772147121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p62102623121127"><a name="p62102623121127"></a><a name="p62102623121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p30062050121127"><a name="p30062050121127"></a><a name="p30062050121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p64485971121127"><a name="p64485971121127"></a><a name="p64485971121127"></a>Provides supplementary information about the firewall rule.</p>
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
<tr id="row66347377121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p7361769121127"><a name="p7361769121127"></a><a name="p7361769121127"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p50019959121127"><a name="p50019959121127"></a><a name="p50019959121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p36897817121127"><a name="p36897817121127"></a><a name="p36897817121127"></a>Specifies the IP protocol.</p>
</td>
</tr>
<tr id="row8703753121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p5943474121127"><a name="p5943474121127"></a><a name="p5943474121127"></a>source_port</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p59206978121127"><a name="p59206978121127"></a><a name="p59206978121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p62826249121127"><a name="p62826249121127"></a><a name="p62826249121127"></a>Specifies the source port number or port number range.</p>
</td>
</tr>
<tr id="row52935496121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p12876203121127"><a name="p12876203121127"></a><a name="p12876203121127"></a>destination_port</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p66631365121127"><a name="p66631365121127"></a><a name="p66631365121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p66851026121127"><a name="p66851026121127"></a><a name="p66851026121127"></a>Specifies the destination port number or port number range.</p>
</td>
</tr>
<tr id="row37973187121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p18090983121127"><a name="p18090983121127"></a><a name="p18090983121127"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p15064211121127"><a name="p15064211121127"></a><a name="p15064211121127"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p10402054121127"><a name="p10402054121127"></a><a name="p10402054121127"></a>Specifies the IP protocol version.</p>
</td>
</tr>
<tr id="row34581454121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p61377852121127"><a name="p61377852121127"></a><a name="p61377852121127"></a>source_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p36483585121127"><a name="p36483585121127"></a><a name="p36483585121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p31475962121127"><a name="p31475962121127"></a><a name="p31475962121127"></a>Specifies the source IP address or CIDR block.</p>
</td>
</tr>
<tr id="row13949121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p43901244121127"><a name="p43901244121127"></a><a name="p43901244121127"></a>destination_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p14651426121127"><a name="p14651426121127"></a><a name="p14651426121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p53743554121127"><a name="p53743554121127"></a><a name="p53743554121127"></a>Specifies the destination IP address or CIDR block.</p>
</td>
</tr>
<tr id="row33223843121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p40131900121127"><a name="p40131900121127"></a><a name="p40131900121127"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p952780121127"><a name="p952780121127"></a><a name="p952780121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p16135729121127"><a name="p16135729121127"></a><a name="p16135729121127"></a>Specifies action performed on traffic passing through the firewall.</p>
</td>
</tr>
<tr id="row11398101121127"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p50347088121127"><a name="p50347088121127"></a><a name="p50347088121127"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p46161809121127"><a name="p46161809121127"></a><a name="p46161809121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p57324252121127"><a name="p57324252121127"></a><a name="p57324252121127"></a>Specifies whether the firewall rule is enabled.</p>
</td>
</tr>
<tr id="row1574912215580"><td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.4.1.1 "><p id="p1312116475819"><a name="p1312116475819"></a><a name="p1312116475819"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.2.4.1.2 "><p id="p5125543583"><a name="p5125543583"></a><a name="p5125543583"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.550000000000004%" headers="mcps1.2.4.1.3 "><p id="p187677200286"><a name="p187677200286"></a><a name="p187677200286"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section60841704122541"></a>

Example request

```
GET https://{Endpoint}/v2.0/fwaas/firewall_rules
```

Example response

```
{
    "firewall_rules": [
        {
            "protocol": "tcp", 
            "name": "crhfwruleupdate", 
            "mode": "normal", 
            "tenant_id": "f480f5d250824e5fafedcf05acf1419c", 
            "rule_profile": "", 
            "enabled": true, 
            "source_port": null, 
            "source_ip_address": null, 
            "destination_ip_address": null, 
            "firewall_policy_id": "b4f81251-c47a-4fe1-8579-6f9271d015d1", 
            "action": "deny", 
            "position": 1, 
            "ip_version": 4, 
            "shared": false, 
            "destination_port": null, 
            "id": "2a193015-4a88-4aa1-84ad-d4955adae707", 
            "description": "",
            "project_id": "f480f5d250824e5fafedcf05acf1419c"
        }, 
        {
            "protocol": "tcp", 
            "name": "update_firewall-role-tommy", 
            "mode": "mix", 
            "tenant_id": "a1c6f90c94334bd2953d9a61b8031a68", 
            "rule_profile": "", 
            "enabled": false, 
            "source_port": "20:50", 
            "source_ip_address": null, 
            "destination_ip_address": null, 
            "firewall_policy_id": null, 
            "action": "deny", 
            "position": null, 
            "ip_version": 4, 
            "shared": true, 
            "destination_port": "40:60", 
            "id": "db7a204c-9eb1-40a2-9bd6-ed5cfd3cff32", 
            "description": "update check parameter",
            "project_id": "a1c6f90c94334bd2953d9a61b8031a68"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

