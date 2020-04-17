# Querying Details of a Certificate<a name="EN-US_TOPIC_0096561583"></a>

## Function<a name="en-us_topic_0085859917_section20669223172659"></a>

This API is used to query details about a certificate.

## URI<a name="en-us_topic_0085859917_section23198423172659"></a>

GET /v2.0/lbaas/certificates/\{certificate\_id\}

**Table  1**  Parameter description

<a name="table115396581764"></a>
<table><thead align="left"><tr id="row3571205812618"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p15710589617"><a name="p15710589617"></a><a name="p15710589617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p35711958366"><a name="p35711958366"></a><a name="p35711958366"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p10571658366"><a name="p10571658366"></a><a name="p10571658366"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p957119581611"><a name="p957119581611"></a><a name="p957119581611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row657118581961"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1357111580610"><a name="p1357111580610"></a><a name="p1357111580610"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p105711858666"><a name="p105711858666"></a><a name="p105711858666"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p8571105811614"><a name="p8571105811614"></a><a name="p8571105811614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p157116580613"><a name="p157116580613"></a><a name="p157116580613"></a>Specifies the certificate ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0085859917_section32916575172659"></a>

None

## Response<a name="en-us_topic_0085859917_section31940794172659"></a>

**Table  2**  Parameter description

<a name="en-us_topic_0085859917_table45008640172659"></a>
<table><thead align="left"><tr id="en-us_topic_0096561584_en-us_topic_0085859918_row11412198173534"><th class="cellrowborder" valign="top" width="21.099999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561584_en-us_topic_0085859918_p66723761173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p66723761173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p66723761173534"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.9%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561584_en-us_topic_0085859918_p31496314173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p31496314173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p31496314173534"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561584_en-us_topic_0085859918_p5981838173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p5981838173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p5981838173534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561584_en-us_topic_0085859918_row20744965173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p21724371173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p21724371173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p21724371173534"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_p11149359102718"><a name="en-us_topic_0096561584_p11149359102718"></a><a name="en-us_topic_0096561584_p11149359102718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p4585726173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p4585726173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p4585726173534"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_row1313561214274"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_p1913501218276"><a name="en-us_topic_0096561584_p1913501218276"></a><a name="en-us_topic_0096561584_p1913501218276"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_p16135161202717"><a name="en-us_topic_0096561584_p16135161202717"></a><a name="en-us_topic_0096561584_p16135161202717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_p1413510125272"><a name="en-us_topic_0096561584_p1413510125272"></a><a name="en-us_topic_0096561584_p1413510125272"></a>Specifies the ID of the project where the certificate is used.</p>
<p id="en-us_topic_0096561584_p12961124943614"><a name="en-us_topic_0096561584_p12961124943614"></a><a name="en-us_topic_0096561584_p12961124943614"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_row7916373278"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_p19161672277"><a name="en-us_topic_0096561584_p19161672277"></a><a name="en-us_topic_0096561584_p19161672277"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_p191616732710"><a name="en-us_topic_0096561584_p191616732710"></a><a name="en-us_topic_0096561584_p191616732710"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_p274684451617"><a name="en-us_topic_0096561584_p274684451617"></a><a name="en-us_topic_0096561584_p274684451617"></a>Specifies the administrative status of the certificate.</p>
<p id="en-us_topic_0096561584_p1674619446167"><a name="en-us_topic_0096561584_p1674619446167"></a><a name="en-us_topic_0096561584_p1674619446167"></a>The value can be <strong id="en-us_topic_0096561584_b9496204415619"><a name="en-us_topic_0096561584_b9496204415619"></a><a name="en-us_topic_0096561584_b9496204415619"></a>true</strong> or <strong id="en-us_topic_0096561584_b749711441617"><a name="en-us_topic_0096561584_b749711441617"></a><a name="en-us_topic_0096561584_b749711441617"></a>false</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row29191383173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p55607168173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p55607168173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p55607168173534"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p28026059173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28026059173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28026059173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p21173547173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p21173547173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p21173547173534"></a>Specifies the certificate name.</p>
<p id="en-us_topic_0096561584_p18170252113611"><a name="en-us_topic_0096561584_p18170252113611"></a><a name="en-us_topic_0096561584_p18170252113611"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row41991314173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p63231950173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p63231950173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p63231950173534"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p35111452173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p35111452173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p35111452173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p49236727173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p49236727173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p49236727173534"></a>Provides supplementary information about the certificate.</p>
<p id="en-us_topic_0096561584_p71641548361"><a name="en-us_topic_0096561584_p71641548361"></a><a name="en-us_topic_0096561584_p71641548361"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row27338318173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p43711802173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43711802173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43711802173534"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p16661086173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p16661086173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p16661086173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p47471091173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p47471091173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p47471091173534"></a>Specifies the certificate type. </p>
<div class="p" id="en-us_topic_0096561584_p9834519174"><a name="en-us_topic_0096561584_p9834519174"></a><a name="en-us_topic_0096561584_p9834519174"></a>The value can be one of the following:<a name="en-us_topic_0096561584_ul48343181711"></a><a name="en-us_topic_0096561584_ul48343181711"></a><ul id="en-us_topic_0096561584_ul48343181711"><li><strong id="en-us_topic_0096561584_b72031550461"><a name="en-us_topic_0096561584_b72031550461"></a><a name="en-us_topic_0096561584_b72031550461"></a>server</strong>: indicates the server certificate.</li><li><strong id="en-us_topic_0096561584_b19811145114618"><a name="en-us_topic_0096561584_b19811145114618"></a><a name="en-us_topic_0096561584_b19811145114618"></a>client</strong>: indicates the CA certificate.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row57368822173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p66718031173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p66718031173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p66718031173534"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p28969287173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28969287173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28969287173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p52667105173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p52667105173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p52667105173534"></a>Specifies the domain name associated with the server certificate.</p>
<p id="en-us_topic_0096561584_p7145757123615"><a name="en-us_topic_0096561584_p7145757123615"></a><a name="en-us_topic_0096561584_p7145757123615"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row32267386173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p2838320173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p2838320173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p2838320173534"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p43739651173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43739651173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43739651173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p12798312173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p12798312173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p12798312173534"></a>Specifies the private key of the server certificate in PEM format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row329105173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p10917956173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p10917956173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p10917956173534"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p50089397173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p50089397173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p50089397173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p47546713173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p47546713173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p47546713173534"></a>Specifies the public key of the server certificate or CA certificate used to authenticate the client. The value of parameter <strong id="en-us_topic_0096561584_b135816391704"><a name="en-us_topic_0096561584_b135816391704"></a><a name="en-us_topic_0096561584_b135816391704"></a>type</strong> determines whether a public key or CA certificate is required. Both types of certificates are in PEM format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_row5698184112395"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_p1169816414399"><a name="en-us_topic_0096561584_p1169816414399"></a><a name="en-us_topic_0096561584_p1169816414399"></a>expire_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_p969874112392"><a name="en-us_topic_0096561584_p969874112392"></a><a name="en-us_topic_0096561584_p969874112392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_p146981141133912"><a name="en-us_topic_0096561584_p146981141133912"></a><a name="en-us_topic_0096561584_p146981141133912"></a>Specifies the time when the certificate expires.</p>
<p id="en-us_topic_0096561584_en-us_topic_0141008271_p52901417154816"><a name="en-us_topic_0096561584_en-us_topic_0141008271_p52901417154816"></a><a name="en-us_topic_0096561584_en-us_topic_0141008271_p52901417154816"></a>The UTC time is in <em id="en-us_topic_0096561584_i20651131012267"><a name="en-us_topic_0096561584_i20651131012267"></a><a name="en-us_topic_0096561584_i20651131012267"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row58956881173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p28854566173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28854566173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p28854566173534"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p41288654173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p41288654173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p41288654173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p14875840173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p14875840173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p14875840173534"></a>Specifies the time when the certificate was created.</p>
<p id="en-us_topic_0096561584_p17245855710"><a name="en-us_topic_0096561584_p17245855710"></a><a name="en-us_topic_0096561584_p17245855710"></a>The UTC time is in <em id="en-us_topic_0096561584_i11878414172613"><a name="en-us_topic_0096561584_i11878414172613"></a><a name="en-us_topic_0096561584_i11878414172613"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561584_en-us_topic_0085859918_row43957201173534"><td class="cellrowborder" valign="top" width="21.099999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p57772843173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p57772843173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p57772843173534"></a>update_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p43564658173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43564658173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p43564658173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561584_en-us_topic_0085859918_p4321549173534"><a name="en-us_topic_0096561584_en-us_topic_0085859918_p4321549173534"></a><a name="en-us_topic_0096561584_en-us_topic_0085859918_p4321549173534"></a>Specifies the time when the certificate was updated.</p>
<p id="en-us_topic_0096561584_p53376597572"><a name="en-us_topic_0096561584_p53376597572"></a><a name="en-us_topic_0096561584_p53376597572"></a>The UTC time is in <em id="en-us_topic_0096561584_i11337243499"><a name="en-us_topic_0096561584_i11337243499"></a><a name="en-us_topic_0096561584_i11337243499"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section18923941193218"></a>

-   Example request: Querying details of a certificate

    ```
    GET https://{Endpoint}/v2.0/lbaas/certificates/23ef9aad4ecb463580476d324a6c71af
    ```

-   Example response

    ```
    {
        "certificate": 
    "-----BEGIN CERTIFICATE-----
    \nMIIC4TCCAcmgAwIBAgICEREwDQYJKoZIhvcNAQELBQAwFzEVMBMGA1UEAxMMTXlD
    \nb21wYW55IENBMB4XDTE4MDcwMjEzMjU0N1oXDTQ1MTExNzEzMjU0N1owFDESMBAG
    \nA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA
    \n0FQGzi3ucTX+DNud1p/b4XVM6I3rY7+Cfge5GMLDIUXIHXCfCgp19Z3807yNpLF5
    \nU0NqPQZKUrZz3rQeLN9mYiUTJZPutYlFDDbB8CtlgV+eyU9yYJslWx/Bm5kWNPh9
    \n7B9Yu9pbp2u6zDA99IC4ekKD93KuzxlnLmSle4Y3dbYwk0LpMDL6lfCHKt/W7jaS
    \nIAzlsxD+QM6l7QjhWJ+kUx+UkboOISjTe7E9XmDLJR7u8LRAQylYKy4zgnv1tn/K
    \ny09cxLKAFtgoZWQD2FAZJf9F7k1kYNwqITz3CPlLZUUn7yw3nkOOtLMI28IEv0Wy
    \nYd7CMJQkS1NPJBKNOGfR/wIDAQABozowODAhBgNVHREEGjAYggpkb21haW4uY29t
    \nhwQKuUvJhwR/AAABMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBCwUA
    \nA4IBAQA8lMQJxaTey7EjXtRLSVlEAMftAQPG6jijNQuvIBQYUDauDT4W2XUZ5wAn
    \njiOyQ83va672K1G9s8n6xlH+xwwdSNnozaKzC87vwSeZKIOdl9I5I98TGKI6OoDa
    \nezmzCwQYtHBMVQ4c7Ml8554Ft1mWSt4dMAK2rzNYjvPRLYlzp1HMnI6hkjPk4PCZ
    \nwKnha0dlScati9CCt3UzXSNJOSLalKdHErH08Iqd+1BchScxCfk0xNITn1HZZGmI
    \n+vbmunok3A2lucI14rnsrcbkGYqxGikySN6B2cRLBDK4Y3wChiW6NVYtVqcx5/mZ
    \niYsGDVN+9QBd0eYUHce+77s96i3I
    \n-----END CERTIFICATE-----",
        "create_time": "2017-02-25 09:35:27",
        "expire_time": "2045-11-17 13:25:47",
        "description": "description for certificate",
        "domain": "www.elb.com",
        "id": "23ef9aad4ecb463580476d324a6c71af",
        "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
        "admin_state_up": true,
        "name": "https_certificate",
        "private_key": 
    "-----BEGIN PRIVATE KEY-----
    \nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQVAbOLe5xNf4M
    \n253Wn9vhdUzojetjv4J+B7kYwsMhRcgdcJ8KCnX1nfzTvI2ksXlTQ2o9BkpStnPe
    \ntB4s32ZiJRMlk+61iUUMNsHwK2WBX57JT3JgmyVbH8GbmRY0+H3sH1i72luna7rM
    \nMD30gLh6QoP3cq7PGWcuZKV7hjd1tjCTQukwMvqV8Icq39buNpIgDOWzEP5AzqXt
    \nCOFYn6RTH5SRug4hKNN7sT1eYMslHu7wtEBDKVgrLjOCe/W2f8rLT1zEsoAW2Chl
    \nZAPYUBkl/0XuTWRg3CohPPcI+UtlRSfvLDeeQ460swjbwgS/RbJh3sIwlCRLU08k
    \nEo04Z9H/AgMBAAECggEAEIeaQqHCWZk/HyYN0Am/GJSGFa2tD60SXY2fUieh8/Hl
    \nfvCArftGgMaYWPSNCJRMXB7tPwpQu19esjz4Z/cR2Je4fTLPrffGUsHFgZjv5OQB
    \nZVe4a5Hj1OcgJYhwCqPs2d9i2wToYNBbcfgh8lSETq8YaXngBO6vES9LMhHkNKKr
    \nciu9YkInNEHu6uRJ5g/eGGX3KQynTvVIhnOVGAJvjTXcoU6fm7gYdHAD6jk9lc9M
    \nEGpfYI6AdHIwFZcT/RNAxhP82lg2gUJSgAu66FfDjMwQXKbafKdP3zq4Up8a7Ale
    \nkrguPtfV1vWklg+bUFhgGaiAEYTpAUN9t2DVIiijgQKBgQDnYMMsaF0r557CM1CT
    \nXUqgCZo8MKeV2jf2drlxRRwRl33SksQbzAQ/qrLdT7GP3sCGqvkxWY2FPdFYf8kx
    \nGcCeZPcIeZYCQAM41pjtsaM8tVbLWVR8UtGBuQoPSph7JNF3Tm/JH/fbwjpjP7dt
    \nJ7n8EzkRUNE6aIMHOFEeych/PQKBgQDmf1bMogx63rTcwQ0PEZ9Vt7mTgKYK4aLr
    \niWgTWHXPZxUQaYhpjXo6+lMI6DpExiDgBAkMzJGIvS7yQiYWU+wthAr9urbWYdGZ
    \nlS6VjoTkF6r7VZoILXX0fbuXh6lm8K8IQRfBpJff56p9phMwaBpDNDrfpHB5utBU
    \nxs40yIdp6wKBgQC69Cp/xUwTX7GdxQzEJctYiKnBHKcspAg38zJf3bGSXU/jR4eB
    \n1lVQhELGI9CbKSdzKM71GyEImix/T7FnJSHIWlho1qVo6AQyduNWnAQD15pr8KAd
    \nXGXAZZ1FQcb3KYa+2fflERmazdOTwjYZ0tGqZnXkEeMdSLkmqlCRigWhGQKBgDak
    \n/735uP20KKqhNehZpC2dJei7OiIgRhCS/dKASUXHSW4fptBnUxACYocdDxtY4Vha
    \nfI7FPMdvGl8ioYbvlHFh+X0Xs9r1S8yeWnHoXMb6eXWmYKMJrAoveLa+2cFm1Agf
    \n7nLhA4R4lqm9IpV6SKegDUkR4fxp9pPyodZPqBLLAoGBAJkD4wHW54Pwd4Ctfk9o
    \njHjWB7pQlUYpTZO9dm+4fpCMn9Okf43AE2yAOaAP94GdzdDJkxfciXKcsYr9IIuk
    \nfaoXgjKR7p1zERiWZuFF63SB4aiyX1H7IX0MwHDZQO38a5gZaOm/BUlGKMWXzuEd
    \n3fy+1rCUwzOp9LSjtJYf4ege
    \n-----END PRIVATE KEY-----",
        "type": "server",
        "update_time": "2017-02-25 09:35:27"
    }
    ```


## Status Code<a name="en-us_topic_0049139664_section36936567"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

