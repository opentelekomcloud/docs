# Creating a Certificate<a name="EN-US_TOPIC_0096561584"></a>

## Function<a name="en-us_topic_0085859918_section45801889173534"></a>

This API is used to create a certificate. After a certificate is bound to a listener, the load balancer authenticates the client using this certificate, and backend servers can establish secure and reliable HTTP connections with the client.

## URI<a name="en-us_topic_0085859918_section43281225173534"></a>

POST /v2.0/lbaas/certificates

## Request<a name="en-us_topic_0085859918_section26755117173534"></a>

**Table  1**  Parameter description

<a name="en-us_topic_0085859918_table18680203173534"></a>
<table><thead align="left"><tr id="en-us_topic_0085859918_row26276700173534"><th class="cellrowborder" valign="top" width="21.357864213578644%" id="mcps1.2.5.1.1"><p id="en-us_topic_0085859918_p45300505173534"><a name="en-us_topic_0085859918_p45300505173534"></a><a name="en-us_topic_0085859918_p45300505173534"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.228777122287772%" id="mcps1.2.5.1.2"><p id="en-us_topic_0085859918_p35999075173534"><a name="en-us_topic_0085859918_p35999075173534"></a><a name="en-us_topic_0085859918_p35999075173534"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="8.95910408959104%" id="mcps1.2.5.1.3"><p id="en-us_topic_0085859918_p46190441173534"><a name="en-us_topic_0085859918_p46190441173534"></a><a name="en-us_topic_0085859918_p46190441173534"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.45425457454255%" id="mcps1.2.5.1.4"><p id="en-us_topic_0085859918_p37900267173534"><a name="en-us_topic_0085859918_p37900267173534"></a><a name="en-us_topic_0085859918_p37900267173534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row950718244237"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="p5507142417232"><a name="p5507142417232"></a><a name="p5507142417232"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p13507122472320"><a name="p13507122472320"></a><a name="p13507122472320"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="p85071524182312"><a name="p85071524182312"></a><a name="p85071524182312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the certificate is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
<p id="p2038118462238"><a name="p2038118462238"></a><a name="p2038118462238"></a>The value must be the same as the value of <strong id="b128491745627"><a name="b128491745627"></a><a name="b128491745627"></a>project_id</strong> in the token.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1921822811231"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="p14219122813235"><a name="p14219122813235"></a><a name="p14219122813235"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p2219328122320"><a name="p2219328122320"></a><a name="p2219328122320"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="p14219162810235"><a name="p14219162810235"></a><a name="p14219162810235"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the certificate.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b5486161310"><a name="b5486161310"></a><a name="b5486161310"></a>true</strong> or <strong id="b4487561636"><a name="b4487561636"></a><a name="b4487561636"></a>false</strong>.</p>
<p id="p1486211148117"><a name="p1486211148117"></a><a name="p1486211148117"></a>This parameter is reserved. Currently, the value can only be <strong id="b9226483317"><a name="b9226483317"></a><a name="b9226483317"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row3910969173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p47016018173534"><a name="en-us_topic_0085859918_p47016018173534"></a><a name="en-us_topic_0085859918_p47016018173534"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p5404942173534"><a name="en-us_topic_0085859918_p5404942173534"></a><a name="en-us_topic_0085859918_p5404942173534"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p64534157173534"><a name="en-us_topic_0085859918_p64534157173534"></a><a name="en-us_topic_0085859918_p64534157173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p034963734312"><a name="p034963734312"></a><a name="p034963734312"></a>Specifies the certificate name.</p>
<p id="p83621636113610"><a name="p83621636113610"></a><a name="p83621636113610"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row66757249173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p46264618173534"><a name="en-us_topic_0085859918_p46264618173534"></a><a name="en-us_topic_0085859918_p46264618173534"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p35441753173534"><a name="en-us_topic_0085859918_p35441753173534"></a><a name="en-us_topic_0085859918_p35441753173534"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p1602109173534"><a name="en-us_topic_0085859918_p1602109173534"></a><a name="en-us_topic_0085859918_p1602109173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p636474910435"><a name="p636474910435"></a><a name="p636474910435"></a>Provides supplementary information about the certificate.</p>
<p id="p2631163917369"><a name="p2631163917369"></a><a name="p2631163917369"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row7554622173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p43254076173534"><a name="en-us_topic_0085859918_p43254076173534"></a><a name="en-us_topic_0085859918_p43254076173534"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p67076645173534"><a name="en-us_topic_0085859918_p67076645173534"></a><a name="en-us_topic_0085859918_p67076645173534"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p16130402173534"><a name="en-us_topic_0085859918_p16130402173534"></a><a name="en-us_topic_0085859918_p16130402173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p96491756191110"><a name="p96491756191110"></a><a name="p96491756191110"></a>Specifies the certificate type. The default value is <strong id="b141344221744"><a name="b141344221744"></a><a name="b141344221744"></a>server</strong>.</p>
<div class="p" id="p1781245122"><a name="p1781245122"></a><a name="p1781245122"></a>The value can be one of the following:<a name="ul988155044417"></a><a name="ul988155044417"></a><ul id="ul988155044417"><li><strong id="b842352706101425"><a name="b842352706101425"></a><a name="b842352706101425"></a>server</strong>: indicates the server certificate.</li><li><strong id="b32183820417"><a name="b32183820417"></a><a name="b32183820417"></a>client</strong>: indicates the CA certificate.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0085859918_row19853468173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p31227075173534"><a name="en-us_topic_0085859918_p31227075173534"></a><a name="en-us_topic_0085859918_p31227075173534"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p56171128173534"><a name="en-us_topic_0085859918_p56171128173534"></a><a name="en-us_topic_0085859918_p56171128173534"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p13823058173534"><a name="en-us_topic_0085859918_p13823058173534"></a><a name="en-us_topic_0085859918_p13823058173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p14884193271218"><a name="p14884193271218"></a><a name="p14884193271218"></a>Specifies the domain name associated with the server certificate. The default value is <strong id="b4504870511"><a name="b4504870511"></a><a name="b4504870511"></a>null</strong>.</p>
<p id="p14591643143615"><a name="p14591643143615"></a><a name="p14591643143615"></a>The value contains a maximum of 100 characters.</p>
<p id="p16305043131216"><a name="p16305043131216"></a><a name="p16305043131216"></a>The value can be one of the following:</p>
<a name="ul128048293014"></a><a name="ul128048293014"></a><ul id="ul128048293014"><li>A common domain name contains 0 to 100 characters and consists of several strings separated by periods (.). Each string can contain a maximum of 63 characters, including letters, digits, and hyphens (-), and must start and end with a letter or digit.</li><li>In addition to the requirements for common domain names, a wildcard domain name can start with an asterisk (*).</li></ul>
<div class="note" id="en-us_topic_0085859918_note3391807017458"><a name="en-us_topic_0085859918_note3391807017458"></a><a name="en-us_topic_0085859918_note3391807017458"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0085859918_p4119083617458"><a name="en-us_topic_0085859918_p4119083617458"></a><a name="en-us_topic_0085859918_p4119083617458"></a>This parameter is valid only when <strong id="b53914942145615"><a name="b53914942145615"></a><a name="b53914942145615"></a>type</strong> is set to <strong id="b15472430145615"><a name="b15472430145615"></a><a name="b15472430145615"></a>server</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0085859918_row30303660173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p9250461173534"><a name="en-us_topic_0085859918_p9250461173534"></a><a name="en-us_topic_0085859918_p9250461173534"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p51780087173534"><a name="en-us_topic_0085859918_p51780087173534"></a><a name="en-us_topic_0085859918_p51780087173534"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p52921895173534"><a name="en-us_topic_0085859918_p52921895173534"></a><a name="en-us_topic_0085859918_p52921895173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p59621116158"><a name="p59621116158"></a><a name="p59621116158"></a>Specifies the private key of the server certificate.</p>
<p id="p6134613172515"><a name="p6134613172515"></a><a name="p6134613172515"></a>The private key is in PEM format.</p>
<div class="note" id="en-us_topic_0085859918_note58901689174653"><a name="en-us_topic_0085859918_note58901689174653"></a><a name="en-us_topic_0085859918_note58901689174653"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p63448741976"><a name="p63448741976"></a><a name="p63448741976"></a>This parameter is valid and mandatory only when <strong id="b360173449553"><a name="b360173449553"></a><a name="b360173449553"></a>type</strong> is set to <strong id="b557206449553"><a name="b557206449553"></a><a name="b557206449553"></a>server</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0085859918_row26349133173534"><td class="cellrowborder" valign="top" width="21.357864213578644%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0085859918_p10134408173534"><a name="en-us_topic_0085859918_p10134408173534"></a><a name="en-us_topic_0085859918_p10134408173534"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0085859918_p29718405173534"><a name="en-us_topic_0085859918_p29718405173534"></a><a name="en-us_topic_0085859918_p29718405173534"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="8.95910408959104%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0085859918_p40089228173534"><a name="en-us_topic_0085859918_p40089228173534"></a><a name="en-us_topic_0085859918_p40089228173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.45425457454255%" headers="mcps1.2.5.1.4 "><p id="p56851334121510"><a name="p56851334121510"></a><a name="p56851334121510"></a>Specifies the public key of the server certificate or CA certificate used to authenticate the client. The value of parameter <strong id="b8423527068473"><a name="b8423527068473"></a><a name="b8423527068473"></a>type</strong> determines whether a public key or CA certificate is required.</p>
<p id="p8982101462518"><a name="p8982101462518"></a><a name="p8982101462518"></a>The public key is in PEM format.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0085859918_section5212068173534"></a>

**Table  2**  Parameter description

<a name="en-us_topic_0085859918_table24409545173534"></a>
<table><thead align="left"><tr id="en-us_topic_0085859918_row11412198173534"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="en-us_topic_0085859918_p66723761173534"><a name="en-us_topic_0085859918_p66723761173534"></a><a name="en-us_topic_0085859918_p66723761173534"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="en-us_topic_0085859918_p31496314173534"><a name="en-us_topic_0085859918_p31496314173534"></a><a name="en-us_topic_0085859918_p31496314173534"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.4.1.3"><p id="en-us_topic_0085859918_p5981838173534"><a name="en-us_topic_0085859918_p5981838173534"></a><a name="en-us_topic_0085859918_p5981838173534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085859918_row20744965173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p21724371173534"><a name="en-us_topic_0085859918_p21724371173534"></a><a name="en-us_topic_0085859918_p21724371173534"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p11149359102718"><a name="p11149359102718"></a><a name="p11149359102718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p4585726173534"><a name="en-us_topic_0085859918_p4585726173534"></a><a name="en-us_topic_0085859918_p4585726173534"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row1313561214274"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p1913501218276"><a name="p1913501218276"></a><a name="p1913501218276"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p16135161202717"><a name="p16135161202717"></a><a name="p16135161202717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="p1413510125272"><a name="p1413510125272"></a><a name="p1413510125272"></a>Specifies the ID of the project where the certificate is used.</p>
<p id="p12961124943614"><a name="p12961124943614"></a><a name="p12961124943614"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row7916373278"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p19161672277"><a name="p19161672277"></a><a name="p19161672277"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p191616732710"><a name="p191616732710"></a><a name="p191616732710"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="p274684451617"><a name="p274684451617"></a><a name="p274684451617"></a>Specifies the administrative status of the certificate.</p>
<p id="p1674619446167"><a name="p1674619446167"></a><a name="p1674619446167"></a>The value can be <strong id="b9496204415619"><a name="b9496204415619"></a><a name="b9496204415619"></a>true</strong> or <strong id="b749711441617"><a name="b749711441617"></a><a name="b749711441617"></a>false</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row29191383173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p55607168173534"><a name="en-us_topic_0085859918_p55607168173534"></a><a name="en-us_topic_0085859918_p55607168173534"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p28026059173534"><a name="en-us_topic_0085859918_p28026059173534"></a><a name="en-us_topic_0085859918_p28026059173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p21173547173534"><a name="en-us_topic_0085859918_p21173547173534"></a><a name="en-us_topic_0085859918_p21173547173534"></a>Specifies the certificate name.</p>
<p id="p18170252113611"><a name="p18170252113611"></a><a name="p18170252113611"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row41991314173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p63231950173534"><a name="en-us_topic_0085859918_p63231950173534"></a><a name="en-us_topic_0085859918_p63231950173534"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p35111452173534"><a name="en-us_topic_0085859918_p35111452173534"></a><a name="en-us_topic_0085859918_p35111452173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p49236727173534"><a name="en-us_topic_0085859918_p49236727173534"></a><a name="en-us_topic_0085859918_p49236727173534"></a>Provides supplementary information about the certificate.</p>
<p id="p71641548361"><a name="p71641548361"></a><a name="p71641548361"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row27338318173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p43711802173534"><a name="en-us_topic_0085859918_p43711802173534"></a><a name="en-us_topic_0085859918_p43711802173534"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p16661086173534"><a name="en-us_topic_0085859918_p16661086173534"></a><a name="en-us_topic_0085859918_p16661086173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p47471091173534"><a name="en-us_topic_0085859918_p47471091173534"></a><a name="en-us_topic_0085859918_p47471091173534"></a>Specifies the certificate type. </p>
<div class="p" id="p9834519174"><a name="p9834519174"></a><a name="p9834519174"></a>The value can be one of the following:<a name="ul48343181711"></a><a name="ul48343181711"></a><ul id="ul48343181711"><li><strong id="b72031550461"><a name="b72031550461"></a><a name="b72031550461"></a>server</strong>: indicates the server certificate.</li><li><strong id="b19811145114618"><a name="b19811145114618"></a><a name="b19811145114618"></a>client</strong>: indicates the CA certificate.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0085859918_row57368822173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p66718031173534"><a name="en-us_topic_0085859918_p66718031173534"></a><a name="en-us_topic_0085859918_p66718031173534"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p28969287173534"><a name="en-us_topic_0085859918_p28969287173534"></a><a name="en-us_topic_0085859918_p28969287173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p52667105173534"><a name="en-us_topic_0085859918_p52667105173534"></a><a name="en-us_topic_0085859918_p52667105173534"></a>Specifies the domain name associated with the server certificate.</p>
<p id="p7145757123615"><a name="p7145757123615"></a><a name="p7145757123615"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row32267386173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p2838320173534"><a name="en-us_topic_0085859918_p2838320173534"></a><a name="en-us_topic_0085859918_p2838320173534"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p43739651173534"><a name="en-us_topic_0085859918_p43739651173534"></a><a name="en-us_topic_0085859918_p43739651173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p12798312173534"><a name="en-us_topic_0085859918_p12798312173534"></a><a name="en-us_topic_0085859918_p12798312173534"></a>Specifies the private key of the server certificate in PEM format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row329105173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p10917956173534"><a name="en-us_topic_0085859918_p10917956173534"></a><a name="en-us_topic_0085859918_p10917956173534"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p50089397173534"><a name="en-us_topic_0085859918_p50089397173534"></a><a name="en-us_topic_0085859918_p50089397173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p47546713173534"><a name="en-us_topic_0085859918_p47546713173534"></a><a name="en-us_topic_0085859918_p47546713173534"></a>Specifies the public key of the server certificate or CA certificate used to authenticate the client. The value of parameter <strong id="b135816391704"><a name="b135816391704"></a><a name="b135816391704"></a>type</strong> determines whether a public key or CA certificate is required. Both types of certificates are in PEM format.</p>
</td>
</tr>
<tr id="row5698184112395"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p1169816414399"><a name="p1169816414399"></a><a name="p1169816414399"></a>expire_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="p969874112392"><a name="p969874112392"></a><a name="p969874112392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="p146981141133912"><a name="p146981141133912"></a><a name="p146981141133912"></a>Specifies the time when the certificate expires.</p>
<p id="en-us_topic_0141008271_p52901417154816"><a name="en-us_topic_0141008271_p52901417154816"></a><a name="en-us_topic_0141008271_p52901417154816"></a>The UTC time is in <em id="i20651131012267"><a name="i20651131012267"></a><a name="i20651131012267"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row58956881173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p28854566173534"><a name="en-us_topic_0085859918_p28854566173534"></a><a name="en-us_topic_0085859918_p28854566173534"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p41288654173534"><a name="en-us_topic_0085859918_p41288654173534"></a><a name="en-us_topic_0085859918_p41288654173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p14875840173534"><a name="en-us_topic_0085859918_p14875840173534"></a><a name="en-us_topic_0085859918_p14875840173534"></a>Specifies the time when the certificate was created.</p>
<p id="p17245855710"><a name="p17245855710"></a><a name="p17245855710"></a>The UTC time is in <em id="i11878414172613"><a name="i11878414172613"></a><a name="i11878414172613"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row43957201173534"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p57772843173534"><a name="en-us_topic_0085859918_p57772843173534"></a><a name="en-us_topic_0085859918_p57772843173534"></a>update_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p43564658173534"><a name="en-us_topic_0085859918_p43564658173534"></a><a name="en-us_topic_0085859918_p43564658173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p4321549173534"><a name="en-us_topic_0085859918_p4321549173534"></a><a name="en-us_topic_0085859918_p4321549173534"></a>Specifies the time when the certificate was updated.</p>
<p id="p53376597572"><a name="p53376597572"></a><a name="p53376597572"></a>The UTC time is in <em id="i11337243499"><a name="i11337243499"></a><a name="i11337243499"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section183931713134716"></a>

-   Example request: Creating a certificate

    ```
    POST https://{Endpoint}/v2.0/lbaas/certificates
    
    { 
        "name": "https_certificate", 
        "description": "description for certificate", 
        "type": "server", 
        "domain": "www.elb.com", 
        "private_key":  
    "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQVAbOLe5xNf4M\n253Wn9vhdUzojetjv4J+B7kYwsMhRcgdcJ8KCnX1nfzTvI2ksXlTQ2o9BkpStnPe\ntB4s32ZiJRMlk+61iUUMNsHwK2WBX57JT3JgmyVbH8GbmRY0+H3sH1i72luna7rM\nMD30gLh6QoP3cq7PGWcuZKV7hjd1tjCTQukwMvqV8Icq39buNpIgDOWzEP5AzqXt\nCOFYn6RTH5SRug4hKNN7sT1eYMslHu7wtEBDKVgrLjOCe/W2f8rLT1zEsoAW2Chl\nZAPYUBkl/0XuTWRg3CohPPcI+UtlRSfvLDeeQ460swjbwgS/RbJh3sIwlCRLU08k\nEo04Z9H/AgMBAAECggEAEIeaQqHCWZk/HyYN0Am/GJSGFa2tD60SXY2fUieh8/Hl\nfvCArftGgMaYWPSNCJRMXB7tPwpQu19esjz4Z/cR2Je4fTLPrffGUsHFgZjv5OQB\nZVe4a5Hj1OcgJYhwCqPs2d9i2wToYNBbcfgh8lSETq8YaXngBO6vES9LMhHkNKKr\nciu9YkInNEHu6uRJ5g/eGGX3KQynTvVIhnOVGAJvjTXcoU6fm7gYdHAD6jk9lc9M\nEGpfYI6AdHIwFZcT/RNAxhP82lg2gUJSgAu66FfDjMwQXKbafKdP3zq4Up8a7Ale\nkrguPtfV1vWklg+bUFhgGaiAEYTpAUN9t2DVIiijgQKBgQDnYMMsaF0r557CM1CT\nXUqgCZo8MKeV2jf2drlxRRwRl33SksQbzAQ/qrLdT7GP3sCGqvkxWY2FPdFYf8kx\nGcCeZPcIeZYCQAM41pjtsaM8tVbLWVR8UtGBuQoPSph7JNF3Tm/JH/fbwjpjP7dt\nJ7n8EzkRUNE6aIMHOFEeych/PQKBgQDmf1bMogx63rTcwQ0PEZ9Vt7mTgKYK4aLr\niWgTWHXPZxUQaYhpjXo6+lMI6DpExiDgBAkMzJGIvS7yQiYWU+wthAr9urbWYdGZ\nlS6VjoTkF6r7VZoILXX0fbuXh6lm8K8IQRfBpJff56p9phMwaBpDNDrfpHB5utBU\nxs40yIdp6wKBgQC69Cp/xUwTX7GdxQzEJctYiKnBHKcspAg38zJf3bGSXU/jR4eB\n1lVQhELGI9CbKSdzKM71GyEImix/T7FnJSHIWlho1qVo6AQyduNWnAQD15pr8KAd\nXGXAZZ1FQcb3KYa+2fflERmazdOTwjYZ0tGqZnXkEeMdSLkmqlCRigWhGQKBgDak\n/735uP20KKqhNehZpC2dJei7OiIgRhCS/dKASUXHSW4fptBnUxACYocdDxtY4Vha\nfI7FPMdvGl8ioYbvlHFh+X0Xs9r1S8yeWnHoXMb6eXWmYKMJrAoveLa+2cFm1Agf\n7nLhA4R4lqm9IpV6SKegDUkR4fxp9pPyodZPqBLLAoGBAJkD4wHW54Pwd4Ctfk9o\njHjWB7pQlUYpTZO9dm+4fpCMn9Okf43AE2yAOaAP94GdzdDJkxfciXKcsYr9IIuk\nfaoXgjKR7p1zERiWZuFF63SB4aiyX1H7IX0MwHDZQO38a5gZaOm/BUlGKMWXzuEd\n3fy+1rCUwzOp9LSjtJYf4ege\n-----END PRIVATE KEY-----", 
        "certificate":  
    "-----BEGIN CERTIFICATE-----\nMIIC4TCCAcmgAwIBAgICEREwDQYJKoZIhvcNAQELBQAwFzEVMBMGA1UEAxMMTXlD\nb21wYW55IENBMB4XDTE4MDcwMjEzMjU0N1oXDTQ1MTExNzEzMjU0N1owFDESMBAG\nA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n0FQGzi3ucTX+DNud1p/b4XVM6I3rY7+Cfge5GMLDIUXIHXCfCgp19Z3807yNpLF5\nU0NqPQZKUrZz3rQeLN9mYiUTJZPutYlFDDbB8CtlgV+eyU9yYJslWx/Bm5kWNPh9\n7B9Yu9pbp2u6zDA99IC4ekKD93KuzxlnLmSle4Y3dbYwk0LpMDL6lfCHKt/W7jaS\nIAzlsxD+QM6l7QjhWJ+kUx+UkboOISjTe7E9XmDLJR7u8LRAQylYKy4zgnv1tn/K\ny09cxLKAFtgoZWQD2FAZJf9F7k1kYNwqITz3CPlLZUUn7yw3nkOOtLMI28IEv0Wy\nYd7CMJQkS1NPJBKNOGfR/wIDAQABozowODAhBgNVHREEGjAYggpkb21haW4uY29t\nhwQKuUvJhwR/AAABMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBCwUA\nA4IBAQA8lMQJxaTey7EjXtRLSVlEAMftAQPG6jijNQuvIBQYUDauDT4W2XUZ5wAn\njiOyQ83va672K1G9s8n6xlH+xwwdSNnozaKzC87vwSeZKIOdl9I5I98TGKI6OoDa\nezmzCwQYtHBMVQ4c7Ml8554Ft1mWSt4dMAK2rzNYjvPRLYlzp1HMnI6hkjPk4PCZ\nwKnha0dlScati9CCt3UzXSNJOSLalKdHErH08Iqd+1BchScxCfk0xNITn1HZZGmI\n+vbmunok3A2lucI14rnsrcbkGYqxGikySN6B2cRLBDK4Y3wChiW6NVYtVqcx5/mZ\niYsGDVN+9QBd0eYUHce+77s96i3I\n-----END CERTIFICATE-----" 
    }
    ```

-   Example response

    ```
    {
        "domain": "www.elb.com",
        "expire_time": "2045-11-17 13:25:47",
        "update_time": "2017-12-04 06:49:13",
        "create_time": "2017-12-04 06:49:13",
        "id": "3d8a7a02f87a40ed931b719edfe75451",
        "admin_state_up": true,
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQVAbOLe5xNf4M\n253Wn9vhdUzojetjv4J+B7kYwsMhRcgdcJ8KCnX1nfzTvI2ksXlTQ2o9BkpStnPe\ntB4s32ZiJRMlk+61iUUMNsHwK2WBX57JT3JgmyVbH8GbmRY0+H3sH1i72luna7rM\nMD30gLh6QoP3cq7PGWcuZKV7hjd1tjCTQukwMvqV8Icq39buNpIgDOWzEP5AzqXt\nCOFYn6RTH5SRug4hKNN7sT1eYMslHu7wtEBDKVgrLjOCe/W2f8rLT1zEsoAW2Chl\nZAPYUBkl/0XuTWRg3CohPPcI+UtlRSfvLDeeQ460swjbwgS/RbJh3sIwlCRLU08k\nEo04Z9H/AgMBAAECggEAEIeaQqHCWZk/HyYN0Am/GJSGFa2tD60SXY2fUieh8/Hl\nfvCArftGgMaYWPSNCJRMXB7tPwpQu19esjz4Z/cR2Je4fTLPrffGUsHFgZjv5OQB\nZVe4a5Hj1OcgJYhwCqPs2d9i2wToYNBbcfgh8lSETq8YaXngBO6vES9LMhHkNKKr\nciu9YkInNEHu6uRJ5g/eGGX3KQynTvVIhnOVGAJvjTXcoU6fm7gYdHAD6jk9lc9M\nEGpfYI6AdHIwFZcT/RNAxhP82lg2gUJSgAu66FfDjMwQXKbafKdP3zq4Up8a7Ale\nkrguPtfV1vWklg+bUFhgGaiAEYTpAUN9t2DVIiijgQKBgQDnYMMsaF0r557CM1CT\nXUqgCZo8MKeV2jf2drlxRRwRl33SksQbzAQ/qrLdT7GP3sCGqvkxWY2FPdFYf8kx\nGcCeZPcIeZYCQAM41pjtsaM8tVbLWVR8UtGBuQoPSph7JNF3Tm/JH/fbwjpjP7dt\nJ7n8EzkRUNE6aIMHOFEeych/PQKBgQDmf1bMogx63rTcwQ0PEZ9Vt7mTgKYK4aLr\niWgTWHXPZxUQaYhpjXo6+lMI6DpExiDgBAkMzJGIvS7yQiYWU+wthAr9urbWYdGZ\nlS6VjoTkF6r7VZoILXX0fbuXh6lm8K8IQRfBpJff56p9phMwaBpDNDrfpHB5utBU\nxs40yIdp6wKBgQC69Cp/xUwTX7GdxQzEJctYiKnBHKcspAg38zJf3bGSXU/jR4eB\n1lVQhELGI9CbKSdzKM71GyEImix/T7FnJSHIWlho1qVo6AQyduNWnAQD15pr8KAd\nXGXAZZ1FQcb3KYa+2fflERmazdOTwjYZ0tGqZnXkEeMdSLkmqlCRigWhGQKBgDak\n/735uP20KKqhNehZpC2dJei7OiIgRhCS/dKASUXHSW4fptBnUxACYocdDxtY4Vha\nfI7FPMdvGl8ioYbvlHFh+X0Xs9r1S8yeWnHoXMb6eXWmYKMJrAoveLa+2cFm1Agf\n7nLhA4R4lqm9IpV6SKegDUkR4fxp9pPyodZPqBLLAoGBAJkD4wHW54Pwd4Ctfk9o\njHjWB7pQlUYpTZO9dm+4fpCMn9Okf43AE2yAOaAP94GdzdDJkxfciXKcsYr9IIuk\nfaoXgjKR7p1zERiWZuFF63SB4aiyX1H7IX0MwHDZQO38a5gZaOm/BUlGKMWXzuEd\n3fy+1rCUwzOp9LSjtJYf4ege\n-----END PRIVATE KEY-----",
        "tenant_id": "930600df07ac4f66964004041bd3deaf",
        "type": "server",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIC4TCCAcmgAwIBAgICEREwDQYJKoZIhvcNAQELBQAwFzEVMBMGA1UEAxMMTXlD\nb21wYW55IENBMB4XDTE4MDcwMjEzMjU0N1oXDTQ1MTExNzEzMjU0N1owFDESMBAG\nA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n0FQGzi3ucTX+DNud1p/b4XVM6I3rY7+Cfge5GMLDIUXIHXCfCgp19Z3807yNpLF5\nU0NqPQZKUrZz3rQeLN9mYiUTJZPutYlFDDbB8CtlgV+eyU9yYJslWx/Bm5kWNPh9\n7B9Yu9pbp2u6zDA99IC4ekKD93KuzxlnLmSle4Y3dbYwk0LpMDL6lfCHKt/W7jaS\nIAzlsxD+QM6l7QjhWJ+kUx+UkboOISjTe7E9XmDLJR7u8LRAQylYKy4zgnv1tn/K\ny09cxLKAFtgoZWQD2FAZJf9F7k1kYNwqITz3CPlLZUUn7yw3nkOOtLMI28IEv0Wy\nYd7CMJQkS1NPJBKNOGfR/wIDAQABozowODAhBgNVHREEGjAYggpkb21haW4uY29t\nhwQKuUvJhwR/AAABMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBCwUA\nA4IBAQA8lMQJxaTey7EjXtRLSVlEAMftAQPG6jijNQuvIBQYUDauDT4W2XUZ5wAn\njiOyQ83va672K1G9s8n6xlH+xwwdSNnozaKzC87vwSeZKIOdl9I5I98TGKI6OoDa\nezmzCwQYtHBMVQ4c7Ml8554Ft1mWSt4dMAK2rzNYjvPRLYlzp1HMnI6hkjPk4PCZ\nwKnha0dlScati9CCt3UzXSNJOSLalKdHErH08Iqd+1BchScxCfk0xNITn1HZZGmI\n+vbmunok3A2lucI14rnsrcbkGYqxGikySN6B2cRLBDK4Y3wChiW6NVYtVqcx5/mZ\niYsGDVN+9QBd0eYUHce+77s96i3I\n-----END CERTIFICATE-----",
        "name": "https_certificate",
        "description": "description for certificate"
    }
    ```


## Status Code<a name="en-us_topic_0049139664_section36936567"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

