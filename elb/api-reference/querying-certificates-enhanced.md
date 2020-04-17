# Querying Certificates<a name="EN-US_TOPIC_0096561582"></a>

## Function<a name="en-us_topic_0085859916_section4535060517164"></a>

This API is used to query all the certificates. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="en-us_topic_0085859916_section2468576217164"></a>

GET /v2.0/lbaas/certificates

## Constraints<a name="en-us_topic_0085859916_section5080582517164"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="en-us_topic_0085859916_section3708623017164"></a>

**Table  1**  Parameter description

<a name="table662814113616"></a>
<table><thead align="left"><tr id="row166921519619"><th class="cellrowborder" valign="top" width="24.72%" id="mcps1.2.5.1.1"><p id="p7692141565"><a name="p7692141565"></a><a name="p7692141565"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.5.1.2"><p id="p96921511660"><a name="p96921511660"></a><a name="p96921511660"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.610000000000001%" id="mcps1.2.5.1.3"><p id="p56922118618"><a name="p56922118618"></a><a name="p56922118618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.2%" id="mcps1.2.5.1.4"><p id="p16951511768"><a name="p16951511768"></a><a name="p16951511768"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7695512615"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p146951511565"><a name="p146951511565"></a><a name="p146951511565"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p1869561867"><a name="p1869561867"></a><a name="p1869561867"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p1669512119611"><a name="p1669512119611"></a><a name="p1669512119611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the certificate from which pagination query starts, that is, the ID of the last certificate on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b71814591147"><a name="b71814591147"></a><a name="b71814591147"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row1869516116614"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p7695121964"><a name="p7695121964"></a><a name="p7695121964"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p46953118618"><a name="p46953118618"></a><a name="p46953118618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p06951111613"><a name="p06951111613"></a><a name="p06951111613"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of certificates on each page.</p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b1969101181515"><a name="b1969101181515"></a><a name="b1969101181515"></a>0</strong> to <strong id="b11970817152"><a name="b11970817152"></a><a name="b11970817152"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row1369581360"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p15695319612"><a name="p15695319612"></a><a name="p15695319612"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p969519114617"><a name="p969519114617"></a><a name="p969519114617"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p1269571861"><a name="p1269571861"></a><a name="p1269571861"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b1028402241818"><a name="b1028402241818"></a><a name="b1028402241818"></a>true</strong> or <strong id="b4285142216183"><a name="b4285142216183"></a><a name="b4285142216183"></a>false</strong>, and the default value is <strong id="b18286112231820"><a name="b18286112231820"></a><a name="b18286112231820"></a>false</strong>. The last page in the list requested with <strong id="b828762221813"><a name="b828762221813"></a><a name="b828762221813"></a>page_reverse</strong> set to <strong id="b22889221188"><a name="b22889221188"></a><a name="b22889221188"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b32898221184"><a name="b32898221184"></a><a name="b32898221184"></a>page_reverse</strong> set to <strong id="b102892222182"><a name="b102892222182"></a><a name="b102892222182"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b936751320155"><a name="b936751320155"></a><a name="b936751320155"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row575823444614"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p674112172473"><a name="p674112172473"></a><a name="p674112172473"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p274115173477"><a name="p274115173477"></a><a name="p274115173477"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p07411017184714"><a name="p07411017184714"></a><a name="p07411017184714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p57411617104715"><a name="p57411617104715"></a><a name="p57411617104715"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row928084434619"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p11741111711473"><a name="p11741111711473"></a><a name="p11741111711473"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p18741817154716"><a name="p18741817154716"></a><a name="p18741817154716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p15741161704719"><a name="p15741161704719"></a><a name="p15741161704719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p774131717474"><a name="p774131717474"></a><a name="p774131717474"></a>Specifies the certificate name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row3861134714612"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p197417175471"><a name="p197417175471"></a><a name="p197417175471"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p4741111784718"><a name="p4741111784718"></a><a name="p4741111784718"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p10741017134710"><a name="p10741017134710"></a><a name="p10741017134710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p1174181714718"><a name="p1174181714718"></a><a name="p1174181714718"></a>Provides supplementary information about the certificate.</p>
<p id="p11283316173720"><a name="p11283316173720"></a><a name="p11283316173720"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row19302951114618"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p3742171718479"><a name="p3742171718479"></a><a name="p3742171718479"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p17421317104712"><a name="p17421317104712"></a><a name="p17421317104712"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p7742017194718"><a name="p7742017194718"></a><a name="p7742017194718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p96491756191110"><a name="p96491756191110"></a><a name="p96491756191110"></a>Specifies the certificate type. The default value is <strong id="b15178318111519"><a name="b15178318111519"></a><a name="b15178318111519"></a>server</strong>.</p>
<div class="p" id="p1781245122"><a name="p1781245122"></a><a name="p1781245122"></a>The value can be one of the following:<a name="ul988155044417"></a><a name="ul988155044417"></a><ul id="ul988155044417"><li><strong id="b293052081510"><a name="b293052081510"></a><a name="b293052081510"></a>server</strong>: indicates the server certificate.</li><li><strong id="b14511132210152"><a name="b14511132210152"></a><a name="b14511132210152"></a>client</strong>: indicates the CA certificate.</li></ul>
</div>
</td>
</tr>
<tr id="row7225165424619"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p1174281734714"><a name="p1174281734714"></a><a name="p1174281734714"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p37424170472"><a name="p37424170472"></a><a name="p37424170472"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p17742517154717"><a name="p17742517154717"></a><a name="p17742517154717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p14884193271218"><a name="p14884193271218"></a><a name="p14884193271218"></a>Specifies the domain name associated with the server certificate. The default value is <strong id="b7821152541520"><a name="b7821152541520"></a><a name="b7821152541520"></a>null</strong>.</p>
<p id="p860921983716"><a name="p860921983716"></a><a name="p860921983716"></a>The value contains a maximum of 100 characters.</p>
<p id="p16305043131216"><a name="p16305043131216"></a><a name="p16305043131216"></a>The value can be one of the following:</p>
<a name="ul128048293014"></a><a name="ul128048293014"></a><ul id="ul128048293014"><li>A common domain name contains 0 to 100 characters and consists of several strings separated by periods (.). Each string can contain a maximum of 63 characters, including letters, digits, and hyphens (-), and must start and end with a letter or digit.</li><li>In addition to the requirements for common domain names, a wildcard domain name can start with an asterisk (*). This parameter is valid only when <strong id="b10447183181513"><a name="b10447183181513"></a><a name="b10447183181513"></a>type</strong> is set to <strong id="b7447531121517"><a name="b7447531121517"></a><a name="b7447531121517"></a>server</strong>.</li></ul>
</td>
</tr>
<tr id="row8156175712464"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p15742117194713"><a name="p15742117194713"></a><a name="p15742117194713"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p10742151734719"><a name="p10742151734719"></a><a name="p10742151734719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p8742417204714"><a name="p8742417204714"></a><a name="p8742417204714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p8742717114715"><a name="p8742717114715"></a><a name="p8742717114715"></a>Specifies the private key of the server certificate in PEM format.</p>
</td>
</tr>
<tr id="row1512881124720"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p12742217104716"><a name="p12742217104716"></a><a name="p12742217104716"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p1274231720479"><a name="p1274231720479"></a><a name="p1274231720479"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p1474231704717"><a name="p1474231704717"></a><a name="p1474231704717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p1742117104712"><a name="p1742117104712"></a><a name="p1742117104712"></a>Specifies the public key of the server certificate or CA certificate used to authenticate the client. The value of parameter <strong id="b1514151818617"><a name="b1514151818617"></a><a name="b1514151818617"></a>type</strong> determines whether a public key or CA certificate is required. Both types of certificates are in PEM format.</p>
</td>
</tr>
<tr id="row16309122951417"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p11796173111514"><a name="p11796173111514"></a><a name="p11796173111514"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p14614121381515"><a name="p14614121381515"></a><a name="p14614121381515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p117968319159"><a name="p117968319159"></a><a name="p117968319159"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p37968320158"><a name="p37968320158"></a><a name="p37968320158"></a>Specifies the time when the certificate was created.</p>
<p id="p27978316157"><a name="p27978316157"></a><a name="p27978316157"></a>The UTC time is in <em id="i6530172010820"><a name="i6530172010820"></a><a name="i6530172010820"></a>YYYY-MM-DD HH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="row164566360147"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.2.5.1.1 "><p id="p679715361511"><a name="p679715361511"></a><a name="p679715361511"></a>update_time</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.5.1.2 "><p id="p1061415135159"><a name="p1061415135159"></a><a name="p1061415135159"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.610000000000001%" headers="mcps1.2.5.1.3 "><p id="p1879711301519"><a name="p1879711301519"></a><a name="p1879711301519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.2%" headers="mcps1.2.5.1.4 "><p id="p167973361511"><a name="p167973361511"></a><a name="p167973361511"></a>Specifies the time when the certificate was updated.</p>
<p id="p8797133141519"><a name="p8797133141519"></a><a name="p8797133141519"></a>The UTC time is in <em id="i1477672917811"><a name="i1477672917811"></a><a name="i1477672917811"></a>YYYY-MM-DD HH:MM:SS</em> format.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0085859916_section5952300017164"></a>

**Table  2**  Parameter description

<a name="table11931922662"></a>
<table><thead align="left"><tr id="row696352212613"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p1296313228617"><a name="p1296313228617"></a><a name="p1296313228617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.85%" id="mcps1.2.4.1.2"><p id="p196316220614"><a name="p196316220614"></a><a name="p196316220614"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.940000000000005%" id="mcps1.2.4.1.3"><p id="p1963222766"><a name="p1963222766"></a><a name="p1963222766"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row189634221767"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p6963122211614"><a name="p6963122211614"></a><a name="p6963122211614"></a>certificates</p>
</td>
<td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.2.4.1.2 "><p id="p892419588196"><a name="p892419588196"></a><a name="p892419588196"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.940000000000005%" headers="mcps1.2.4.1.3 "><p id="p159638221265"><a name="p159638221265"></a><a name="p159638221265"></a>Lists the certificates. For details, see <a href="#table10415837566">Table 3</a>.</p>
</td>
</tr>
<tr id="row63041404465"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0032340350_p16393887111317"><a name="en-us_topic_0032340350_p16393887111317"></a><a name="en-us_topic_0032340350_p16393887111317"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="19.85%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0032340350_p52836457111317"><a name="en-us_topic_0032340350_p52836457111317"></a><a name="en-us_topic_0032340350_p52836457111317"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.940000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032340350_p51894644111317"><a name="en-us_topic_0032340350_p51894644111317"></a><a name="en-us_topic_0032340350_p51894644111317"></a>Specifies the number of certificates.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **certificates**  parameter description

<a name="table10415837566"></a>
<table><thead align="left"><tr id="en-us_topic_0085859918_row11412198173534"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0085859918_p66723761173534"><a name="en-us_topic_0085859918_p66723761173534"></a><a name="en-us_topic_0085859918_p66723761173534"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.89%" id="mcps1.2.4.1.2"><p id="en-us_topic_0085859918_p31496314173534"><a name="en-us_topic_0085859918_p31496314173534"></a><a name="en-us_topic_0085859918_p31496314173534"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="en-us_topic_0085859918_p5981838173534"><a name="en-us_topic_0085859918_p5981838173534"></a><a name="en-us_topic_0085859918_p5981838173534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085859918_row20744965173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p21724371173534"><a name="en-us_topic_0085859918_p21724371173534"></a><a name="en-us_topic_0085859918_p21724371173534"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p251555143411"><a name="p251555143411"></a><a name="p251555143411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p4585726173534"><a name="en-us_topic_0085859918_p4585726173534"></a><a name="en-us_topic_0085859918_p4585726173534"></a>Specifies the certificate ID.</p>
</td>
</tr>
<tr id="row1313561214274"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p1913501218276"><a name="p1913501218276"></a><a name="p1913501218276"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p16135161202717"><a name="p16135161202717"></a><a name="p16135161202717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1413510125272"><a name="p1413510125272"></a><a name="p1413510125272"></a>Specifies the ID of the project where the certificate is used.</p>
<p id="p59794376393"><a name="p59794376393"></a><a name="p59794376393"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row7916373278"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p19161672277"><a name="p19161672277"></a><a name="p19161672277"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p191616732710"><a name="p191616732710"></a><a name="p191616732710"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p274684451617"><a name="p274684451617"></a><a name="p274684451617"></a>Specifies the administrative status of the certificate.</p>
<p id="p1674619446167"><a name="p1674619446167"></a><a name="p1674619446167"></a>The value can be <strong id="b5437114121613"><a name="b5437114121613"></a><a name="b5437114121613"></a>true</strong> or <strong id="b19437134101615"><a name="b19437134101615"></a><a name="b19437134101615"></a>false</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row29191383173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p55607168173534"><a name="en-us_topic_0085859918_p55607168173534"></a><a name="en-us_topic_0085859918_p55607168173534"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p28026059173534"><a name="en-us_topic_0085859918_p28026059173534"></a><a name="en-us_topic_0085859918_p28026059173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p21173547173534"><a name="en-us_topic_0085859918_p21173547173534"></a><a name="en-us_topic_0085859918_p21173547173534"></a>Specifies the certificate name.</p>
<p id="p854011400395"><a name="p854011400395"></a><a name="p854011400395"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row41991314173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p63231950173534"><a name="en-us_topic_0085859918_p63231950173534"></a><a name="en-us_topic_0085859918_p63231950173534"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p35111452173534"><a name="en-us_topic_0085859918_p35111452173534"></a><a name="en-us_topic_0085859918_p35111452173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p49236727173534"><a name="en-us_topic_0085859918_p49236727173534"></a><a name="en-us_topic_0085859918_p49236727173534"></a>Provides supplementary information about the certificate.</p>
<p id="p20482043143917"><a name="p20482043143917"></a><a name="p20482043143917"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row27338318173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p43711802173534"><a name="en-us_topic_0085859918_p43711802173534"></a><a name="en-us_topic_0085859918_p43711802173534"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p16661086173534"><a name="en-us_topic_0085859918_p16661086173534"></a><a name="en-us_topic_0085859918_p16661086173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p47471091173534"><a name="en-us_topic_0085859918_p47471091173534"></a><a name="en-us_topic_0085859918_p47471091173534"></a>Specifies the certificate type.</p>
<div class="p" id="p9834519174"><a name="p9834519174"></a><a name="p9834519174"></a>The value can be one of the following:<a name="ul48343181711"></a><a name="ul48343181711"></a><ul id="ul48343181711"><li><strong id="b64938717166"><a name="b64938717166"></a><a name="b64938717166"></a>server</strong>: indicates the server certificate.</li><li><strong id="b10467789168"><a name="b10467789168"></a><a name="b10467789168"></a>client</strong>: indicates the CA certificate.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0085859918_row57368822173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p66718031173534"><a name="en-us_topic_0085859918_p66718031173534"></a><a name="en-us_topic_0085859918_p66718031173534"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p28969287173534"><a name="en-us_topic_0085859918_p28969287173534"></a><a name="en-us_topic_0085859918_p28969287173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p52667105173534"><a name="en-us_topic_0085859918_p52667105173534"></a><a name="en-us_topic_0085859918_p52667105173534"></a>Specifies the domain name associated with the server certificate.</p>
<p id="p6316174693913"><a name="p6316174693913"></a><a name="p6316174693913"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row32267386173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p2838320173534"><a name="en-us_topic_0085859918_p2838320173534"></a><a name="en-us_topic_0085859918_p2838320173534"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p43739651173534"><a name="en-us_topic_0085859918_p43739651173534"></a><a name="en-us_topic_0085859918_p43739651173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p12798312173534"><a name="en-us_topic_0085859918_p12798312173534"></a><a name="en-us_topic_0085859918_p12798312173534"></a>Specifies the private key of the server certificate in PEM format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row329105173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p10917956173534"><a name="en-us_topic_0085859918_p10917956173534"></a><a name="en-us_topic_0085859918_p10917956173534"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p50089397173534"><a name="en-us_topic_0085859918_p50089397173534"></a><a name="en-us_topic_0085859918_p50089397173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p47546713173534"><a name="en-us_topic_0085859918_p47546713173534"></a><a name="en-us_topic_0085859918_p47546713173534"></a>Specifies the public key of the server certificate or CA certificate used to authenticate the client. The value of parameter <strong id="b1839315341161"><a name="b1839315341161"></a><a name="b1839315341161"></a>type</strong> determines whether a public key or CA certificate is required. Both types of certificates are in PEM format.</p>
</td>
</tr>
<tr id="row5698184112395"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p1169816414399"><a name="p1169816414399"></a><a name="p1169816414399"></a>expire_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="p969874112392"><a name="p969874112392"></a><a name="p969874112392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p146981141133912"><a name="p146981141133912"></a><a name="p146981141133912"></a>Specifies the time when the certificate expires.</p>
<p id="en-us_topic_0141008271_p52901417154816"><a name="en-us_topic_0141008271_p52901417154816"></a><a name="en-us_topic_0141008271_p52901417154816"></a>The UTC time is in <em id="i7547113720817"><a name="i7547113720817"></a><a name="i7547113720817"></a>YYYY-MM-DD HH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row58956881173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p28854566173534"><a name="en-us_topic_0085859918_p28854566173534"></a><a name="en-us_topic_0085859918_p28854566173534"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p41288654173534"><a name="en-us_topic_0085859918_p41288654173534"></a><a name="en-us_topic_0085859918_p41288654173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p14875840173534"><a name="en-us_topic_0085859918_p14875840173534"></a><a name="en-us_topic_0085859918_p14875840173534"></a>Specifies the time when the certificate was created.</p>
<p id="p13200814155820"><a name="p13200814155820"></a><a name="p13200814155820"></a>The UTC time is in <em id="i1098911421783"><a name="i1098911421783"></a><a name="i1098911421783"></a>YYYY-MM-DD HH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0085859918_row43957201173534"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0085859918_p57772843173534"><a name="en-us_topic_0085859918_p57772843173534"></a><a name="en-us_topic_0085859918_p57772843173534"></a>update_time</p>
</td>
<td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0085859918_p43564658173534"><a name="en-us_topic_0085859918_p43564658173534"></a><a name="en-us_topic_0085859918_p43564658173534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0085859918_p4321549173534"><a name="en-us_topic_0085859918_p4321549173534"></a><a name="en-us_topic_0085859918_p4321549173534"></a>Specifies the time when the certificate was updated.</p>
<p id="p1053261545811"><a name="p1053261545811"></a><a name="p1053261545811"></a>The UTC time is in <em id="i39891749889"><a name="i39891749889"></a><a name="i39891749889"></a>YYYY-MM-DD HH:MM:SS</em> format.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section260932824817"></a>

-   Request example 1: Querying all certificates

    ```
    GET https://{Endpoint}/v2.0/lbaas/certificates
    ```

-   Example response 1

    ```
    {
        "certificates": [
            {
                "certificate": "-----BEGIN CERTIFICATE-----\nMIIC4TCCAcmgAwIBAgICEREwDQYJKoZIhvcNAQELBQAwFzEVMBMGA1UEAxMMTXlD\nb21wYW55IENBMB4XDTE4MDcwMjEzMjU0N1oXDTQ1MTExNzEzMjU0N1owFDESMBAG\nA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n0FQGzi3ucTX+DNud1p/b4XVM6I3rY7+Cfge5GMLDIUXIHXCfCgp19Z3807yNpLF5\nU0NqPQZKUrZz3rQeLN9mYiUTJZPutYlFDDbB8CtlgV+eyU9yYJslWx/Bm5kWNPh9\n7B9Yu9pbp2u6zDA99IC4ekKD93KuzxlnLmSle4Y3dbYwk0LpMDL6lfCHKt/W7jaS\nIAzlsxD+QM6l7QjhWJ+kUx+UkboOISjTe7E9XmDLJR7u8LRAQylYKy4zgnv1tn/K\ny09cxLKAFtgoZWQD2FAZJf9F7k1kYNwqITz3CPlLZUUn7yw3nkOOtLMI28IEv0Wy\nYd7CMJQkS1NPJBKNOGfR/wIDAQABozowODAhBgNVHREEGjAYggpkb21haW4uY29t\nhwQKuUvJhwR/AAABMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBCwUA\nA4IBAQA8lMQJxaTey7EjXtRLSVlEAMftAQPG6jijNQuvIBQYUDauDT4W2XUZ5wAn\njiOyQ83va672K1G9s8n6xlH+xwwdSNnozaKzC87vwSeZKIOdl9I5I98TGKI6OoDa\nezmzCwQYtHBMVQ4c7Ml8554Ft1mWSt4dMAK2rzNYjvPRLYlzp1HMnI6hkjPk4PCZ\nwKnha0dlScati9CCt3UzXSNJOSLalKdHErH08Iqd+1BchScxCfk0xNITn1HZZGmI\n+vbmunok3A2lucI14rnsrcbkGYqxGikySN6B2cRLBDK4Y3wChiW6NVYtVqcx5/mZ\niYsGDVN+9QBd0eYUHce+77s96i3I\n-----END CERTIFICATE-----",
                "create_time": "2017-02-25 09:35:27",
                "expire_time": "2045-11-17 13:25:47",
                "description": "description for certificate",
                "domain": "www.elb.com",
                "id": "23ef9aad4ecb463580476d324a6c71af",
                "admin_state_up": true,
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
                "name": "https_certificate",
                "private_key": 
    "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQVAbOLe5xNf4M\n253Wn9vhdUzojetjv4J+B7kYwsMhRcgdcJ8KCnX1nfzTvI2ksXlTQ2o9BkpStnPe\ntB4s32ZiJRMlk+61iUUMNsHwK2WBX57JT3JgmyVbH8GbmRY0+H3sH1i72luna7rM\nMD30gLh6QoP3cq7PGWcuZKV7hjd1tjCTQukwMvqV8Icq39buNpIgDOWzEP5AzqXt\nCOFYn6RTH5SRug4hKNN7sT1eYMslHu7wtEBDKVgrLjOCe/W2f8rLT1zEsoAW2Chl\nZAPYUBkl/0XuTWRg3CohPPcI+UtlRSfvLDeeQ460swjbwgS/RbJh3sIwlCRLU08k\nEo04Z9H/AgMBAAECggEAEIeaQqHCWZk/HyYN0Am/GJSGFa2tD60SXY2fUieh8/Hl\nfvCArftGgMaYWPSNCJRMXB7tPwpQu19esjz4Z/cR2Je4fTLPrffGUsHFgZjv5OQB\nZVe4a5Hj1OcgJYhwCqPs2d9i2wToYNBbcfgh8lSETq8YaXngBO6vES9LMhHkNKKr\nciu9YkInNEHu6uRJ5g/eGGX3KQynTvVIhnOVGAJvjTXcoU6fm7gYdHAD6jk9lc9M\nEGpfYI6AdHIwFZcT/RNAxhP82lg2gUJSgAu66FfDjMwQXKbafKdP3zq4Up8a7Ale\nkrguPtfV1vWklg+bUFhgGaiAEYTpAUN9t2DVIiijgQKBgQDnYMMsaF0r557CM1CT\nXUqgCZo8MKeV2jf2drlxRRwRl33SksQbzAQ/qrLdT7GP3sCGqvkxWY2FPdFYf8kx\nGcCeZPcIeZYCQAM41pjtsaM8tVbLWVR8UtGBuQoPSph7JNF3Tm/JH/fbwjpjP7dt\nJ7n8EzkRUNE6aIMHOFEeych/PQKBgQDmf1bMogx63rTcwQ0PEZ9Vt7mTgKYK4aLr\niWgTWHXPZxUQaYhpjXo6+lMI6DpExiDgBAkMzJGIvS7yQiYWU+wthAr9urbWYdGZ\nlS6VjoTkF6r7VZoILXX0fbuXh6lm8K8IQRfBpJff56p9phMwaBpDNDrfpHB5utBU\nxs40yIdp6wKBgQC69Cp/xUwTX7GdxQzEJctYiKnBHKcspAg38zJf3bGSXU/jR4eB\n1lVQhELGI9CbKSdzKM71GyEImix/T7FnJSHIWlho1qVo6AQyduNWnAQD15pr8KAd\nXGXAZZ1FQcb3KYa+2fflERmazdOTwjYZ0tGqZnXkEeMdSLkmqlCRigWhGQKBgDak\n/735uP20KKqhNehZpC2dJei7OiIgRhCS/dKASUXHSW4fptBnUxACYocdDxtY4Vha\nfI7FPMdvGl8ioYbvlHFh+X0Xs9r1S8yeWnHoXMb6eXWmYKMJrAoveLa+2cFm1Agf\n7nLhA4R4lqm9IpV6SKegDUkR4fxp9pPyodZPqBLLAoGBAJkD4wHW54Pwd4Ctfk9o\njHjWB7pQlUYpTZO9dm+4fpCMn9Okf43AE2yAOaAP94GdzdDJkxfciXKcsYr9IIuk\nfaoXgjKR7p1zERiWZuFF63SB4aiyX1H7IX0MwHDZQO38a5gZaOm/BUlGKMWXzuEd\n3fy+1rCUwzOp9LSjtJYf4ege\n-----END PRIVATE KEY-----",
                "type": "server",
                "update_time": "2017-02-25 09:35:27"
            }
        ],
        "instance_num": 1
    }
    ```


-   Example 2: Querying a certificate whose ID is ef4d341365754a959556576501791b19 or ed40e8ea9957488ea82de025e35b74c0

    ```
    GET https://{Endpoint}/v2.0/lbaas/certificates?id=ef4d341365754a959556576501791b19&id=ed40e8ea9957488ea82de025e35b74c0
    ```

-   Example response 2

    ```
    {
        "certificates": [
            {
                "description": "Push by SSL Certificate Manager", 
                "domain": null, 
                "id": "ed40e8ea9957488ea82de025e35b74c0", 
                "name": "certForSonar9", 
                "certificate": "-----BEGIN CERTIFICATE-----
    MIIFizCCBHOgAwIBAgIQBlQycV3bWsVsCttvv5rgRjANBgkqhkiG9w0BAQsFADBu
    MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
    d3cuZGlnaWNlcnQuY29tMS0wKwYDVQQDEyRFbmNyeXB0aW9uIEV2ZXJ5d2hlcmUg
    RFYgVExTIENBIC0gRzEwHhcNMTgwNzEwMDAwMDAwWhcNMTkwNzEwMTIwMDAwWjAU
    MRIwEAYDVQQDEwlpY2UxMjMudGswggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
    AoIBAQCtTDlQMoAvyInR6X1dihhNwbdGesbMW6NZX7ffpj9XrB3KCqqlxzI4VmH9
    PntvrpLJNeolgLqDZZc4zKbUkmqxY1dvGDs41coKzdtc9Ig23GVK48wfesnk5r50
    afyU52R1JlSHDOhiDhHOSyhrOzc2GreLrByWKFUaAue6rTnyMbzQaSPtrTAqsURZ
    wcmJ6R3A6JwokOgxXBSu41ufPQiFkMgxygKxEBLzIJLjRqCXQHYoxbsTyolb6jwp
    w4H6vcRIEcFAgs98ApWRoEKjy7eOP3UUm05F+OkOvXhrlxEqIPm/rlwE0PmVlmm9
    DgBafYb3xT/MtT2VRSfCJQHgIcsdAgMBAAGjggJ9MIICeTAfBgNVHSMEGDAWgBRV
    dE+yck/1YLpQ0dfmUVyaAYca1zAdBgNVHQ4EFgQUEFavzYXBNbIHBchbaKcUKad+
    qCEwIwYDVR0RBBwwGoIJaWNlMTIzLnRrgg13d3cuaWNlMTIzLnRrMA4GA1UdDwEB
    /wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwTAYDVR0gBEUw
    QzA3BglghkgBhv1sAQIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNl
    cnQuY29tL0NQUzAIBgZngQwBAgEwgYEGCCsGAQUFBwEBBHUwczAlBggrBgEFBQcw
    AYYZaHR0cDovL29jc3AyLmRpZ2ljZXJ0LmNvbTBKBggrBgEFBQcwAoY+aHR0cDov
    L2NhY2VydHMuZGlnaWNlcnQuY29tL0VuY3J5cHRpb25FdmVyeXdoZXJlRFZUTFND
    QS1HMS5jcnQwCQYDVR0TBAIwADCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AKS5
    CZC0GFgUh7sTosxncAo8NZgE+RvfuON3zQ7IDdwQAAABZIOnLCIAAAQDAEcwRQIh
    AJX6gCXNggPdfOFdDtZPzlYr64TTrR/+b9QKKhyJ2EjBAiAWgu3BG2QK9tWQXpUN
    IFadc0nvqmDovabg5nmRMan2mQB2AId1v+dZfPiMQ5lfvfNu/1aNR1Y2/0q1YMG0
    6v9eoIMPAAABZIOnLQEAAAQDAEcwRQIhAJVRe/7n88dD6KdhNrd4LdFjGARQNmta
    Y/K2dFDOXPSfAiBOLrWW8unHOL25RWHJU7Ost3XkNhQYtrLDJrnzo/9kZzANBgkq
    hkiG9w0BAQsFAAOCAQEAeqtX9cHmj4OnNAk0IGmF3nKS/u/UgGsY4EJfXwQY2bTZ
    PCkqxQOA6HEx59vJ+UilTojrNDi0WskRm/8SKBHtmRwzwX3ile8KiR6fFfQhPUtV
    XHZcTfAFo47c7axqon8vumMlEv1PxVImivQ446K7z3kGm34dhMYxS4Gz2gTl8IKt
    90OegejuhbAs5Wlvp1BK8HlYIb5+mw+cgkUC9KTALs5qVbWzogb0bS20KaYarGcu
    otcZAOMeJdBFWnpzhr1fxmjaNY4u4hrgPZSTU/iBjdHapoza3zAFfxysmGYqs9dR
    jFyxZeR4scz8GqSTFviNdH9jvtDJkdAC5hfMaB811Q==
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIEqjCCA5KgAwIBAgIQAnmsRYvBskWr+YBTzSybsTANBgkqhkiG9w0BAQsFADBh
    MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
    d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD
    QTAeFw0xNzExMjcxMjQ2MTBaFw0yNzExMjcxMjQ2MTBaMG4xCzAJBgNVBAYTAlVT
    MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j
    b20xLTArBgNVBAMTJEVuY3J5cHRpb24gRXZlcnl3aGVyZSBEViBUTFMgQ0EgLSBH
    MTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALPeP6wkab41dyQh6mKc
    oHqt3jRIxW5MDvf9QyiOR7VfFwK656es0UFiIb74N9pRntzF1UgYzDGu3ppZVMdo
    lbxhm6dWS9OK/lFehKNT0OYI9aqk6F+U7cA6jxSC+iDBPXwdF4rs3KRyp3aQn6pj
    pp1yr7IB6Y4zv72Ee/PlZ/6rK6InC6WpK0nPVOYR7n9iDuPe1E4IxUMBH/T33+3h
    yuH3dvfgiWUOUkjdpMbyxX+XNle5uEIiyBsi4IvbcTCh8ruifCIi5mDXkZrnMT8n
    wfYCV6v6kDdXkbgGRLKsR4pucbJtbKqIkUGxuZI2t7pfewKRc5nWecvDBZf3+p1M
    pA8CAwEAAaOCAU8wggFLMB0GA1UdDgQWBBRVdE+yck/1YLpQ0dfmUVyaAYca1zAf
    BgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8EBAMCAYYw
    HQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8C
    AQAwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdp
    Y2VydC5jb20wQgYDVR0fBDswOTA3oDWgM4YxaHR0cDovL2NybDMuZGlnaWNlcnQu
    Y29tL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDBMBgNVHSAERTBDMDcGCWCGSAGG
    /WwBAjAqMCgGCCsGAQUFBwIBFhxodHRwczovL3d3dy5kaWdpY2VydC5jb20vQ1BT
    MAgGBmeBDAECATANBgkqhkiG9w0BAQsFAAOCAQEAK3Gp6/aGq7aBZsxf/oQ+TD/B
    SwW3AU4ETK+GQf2kFzYZkby5SFrHdPomunx2HBzViUchGoofGgg7gHW0W3MlQAXW
    M0r5LUvStcr82QDWYNPaUy4taCQmyaJ+VB+6wxHstSigOlSNF2a6vg4rgexixeiV
    4YSB03Yqp2t3TeZHM9ESfkus74nQyW7pRGezj+TC44xCagCQQOzzNmzEAP2SnCrJ
    sNE2DpRVMnL8J6xBRdjmOsC3N6cQuKuRXbzByVBjCqAA8t1L0I+9wXJerLPyErjy
    rMKWaBFLmfK/AHNF4ZihwPGOc7w6UHczBZXH5RFzJNnww+WnKuTPI0HfnVH8lg==
    -----END CERTIFICATE-----", 
                "type": "server", 
                "create_time": "2019-03-03 16:32:30", 
                "private_key": "-----BEGIN RSA PRIVATE KEY-----
    MIIEpQIBAAKCAQEArUw5UDKAL8iJ0el9XYoYTcG3RnrGzFujWV+336Y/V6wdygqq
    pccyOFZh/T57b66SyTXqJYC6g2WXOMym1JJqsWNXbxg7ONXKCs3bXPSINtxlSuPM
    H3rJ5Oa+dGn8lOdkdSZUhwzoYg4Rzksoazs3Nhq3i6wclihVGgLnuq058jG80Gkj
    7a0wKrFEWcHJiekdwOicKJDoMVwUruNbnz0IhZDIMcoCsRAS8yCS40agl0B2KMW7
    E8qJW+o8KcOB+r3ESBHBQILPfAKVkaBCo8u3jj91FJtORfjpDr14a5cRKiD5v65c
    BND5lZZpvQ4AWn2G98U/zLU9lUUnwiUB4CHLHQIDAQABAoIBAGs5rISompP2OwA8
    virwVRVXdPUQ5oxvbuTPys+A59RxVIU8kFW+qJ4fJMYysOFrXLtOtq+5tK20YBru
    1ZLVfVqAowrELXB/J2ID+WTMkLORLsNlq1kW+nC9LL6PDY98lLW/n7FoFSkGl5HT
    AxFGNGUvpr2vIojuL6nGfmcM47uscJ9aP6IJxr4p70dhPVjZBdnMnXYwRkB3dZt/
    E0B/p8J5i3oo5Rucv4DOfB+01wXGAVyx5/zce+NZdhyrivkj3hHV55SxGhVWzWhj
    a3dAlbpKwYgfILj0inRdJYmIjBdbGb2HFix7+ncBg8B2oerJXC6/fANwRGu5/LZU
    5xuPVWkCgYEA6an8TY1unIGLYL5aBJ16Tx4usqMyTXr/T4zkQyftRPMt+ZuxVQHl
    GHsg7XvLFNd04MBZXtkZXaYVcpOm7OUYcl0i9ZAkWXXoXcBtn1Oom3gz/7RjAUnp
    k+myvxCUSQ2JSz4u3QBtyPVyYNyBFXrKqdKfcYyG85+yQVHBNMVrdvMCgYEAvd0C
    hFpm83ha+VQp+9XN1DYZNUyqhibj/E3X9jAn+gDbzlKxw/D9en2RIlQYUrl8+il8
    QKk4cfOxJYStQfxptz8QBPVeLajDN67zJ0Rk8AB50HHHcNSU8uFkaO8KxsyVjbLS
    +JltqfJAEraXLinbp1Fxcg9DsQdMd6cw2DmrWa8CgYEA1UjJOUzo80i4HYWDC4Vn
    OEK3o22do+WqmEVlsfsG9BH5HEdGVe7V3EO/6aY+1/ZXBDPvH8mRAs9v8lbeXow7
    hWCIYZfB5jre8HyOU4l8dPUCmdxhJrL913rRIuASSqBlet32ztnuXCnWzp1X4nBj
    /yF3UqFQKZ7SihcDAZVWo4sCgYEAj7al/BcNzIcynX2mldhdh583b4/Ll+YCNm2Z
    5eDHscZKmx8fLcjRpZE8dXagPqXmwtj6E1vDvQWP9m06VDNCthFHB+nO0tLmidSk
    evmbScuiaTRmmbJf2IThY0hlqNsc7PgKF2DTkIstEr0hLDFE8Z6FN6f0PiDfMcbd
    Ax6L5EMCgYEA0+qhuQftKQkGdbXX9r3H8N0TVh27ByfL3kKVYy0dUJMvsOAq6d97
    8mEhYhrYt88f1sFsPM7G09XpCcBXwiKxw8+CDt9auD4r1snBnILpqMPmanF4UDXH
    L7s+4it+nIQy24P6g1PihtzsM+HD2UCErBiYUJdRK8Q9GGHdZojFk9Y=
    -----END RSA PRIVATE KEY-----
    ", 
                "update_time": "2019-03-03 16:32:30", 
                "admin_state_up": true, 
                "tenant_id": "601240b9c5c94059b63d484c92cfe308", 
                "expire_time": "2019-07-10 12:00:00"
            }, 
            {
                "description": null, 
                "domain": "www.elb.com", 
                "id": "ef4d341365754a959556576501791b19", 
                "name": "certificate_28b824c8bbee419992fb7974b2911c72", 
                "certificate": "-----BEGIN CERTIFICATE-----
    MIIDpTCCAo2gAwIBAgIJAKdmmOBYnFvoMA0GCSqGSIb3DQEBCwUAMGkxCzAJBgNV
    BAYTAnh4MQswCQYDVQQIDAJ4eDELMAkGA1UEBwwCeHgxCzAJBgNVBAoMAnh4MQsw
    CQYDVQQLDAJ4eDELMAkGA1UEAwwCeHgxGTAXBgkqhkiG9w0BCQEWCnh4QDE2My5j
    b20wHhcNMTcxMjA0MDM0MjQ5WhcNMjAxMjAzMDM0MjQ5WjBpMQswCQYDVQQGEwJ4
    eDELMAkGA1UECAwCeHgxCzAJBgNVBAcMAnh4MQswCQYDVQQKDAJ4eDELMAkGA1UE
    CwwCeHgxCzAJBgNVBAMMAnh4MRkwFwYJKoZIhvcNAQkBFgp4eEAxNjMuY29tMIIB
    IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwZ5UJULAjWr7p6FVwGRQRjFN
    2s8tZ/6LC3X82fajpVsYqF1xqEuUDndDXVD09E4u83MS6HO6a3bIVQDp6/klnYld
    iE6Vp8HH5BSKaCWKVg8lGWg1UM9wZFnlryi14KgmpIFmcu9nA8yV/6MZAe6RSDmb
    3iyNBmiZ8aZhGw2pI1YwR+15MVqFFGB+7ExkziROi7L8CFCyCezK2/oOOvQsH1dz
    Q8z1JXWdg8/9Zx7Ktvgwu5PQM3cJtSHX6iBPOkMU8Z8TugLlTqQXKZOEgwajwvQ5
    mf2DPkVgM08XAgaLJcLigwD513koAdtJd5v+9irw+5LAuO3JclqwTvwy7u/YwwID
    AQABo1AwTjAdBgNVHQ4EFgQUo5A2tIu+bcUfvGTD7wmEkhXKFjcwHwYDVR0jBBgw
    FoAUo5A2tIu+bcUfvGTD7wmEkhXKFjcwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0B
    AQsFAAOCAQEAWJ2rS6Mvlqk3GfEpboezx2J3X7l1z8Sxoqg6ntwB+rezvK3mc9H0
    83qcVeUcoH+0A0lSHyFN4FvRQL6X1hEheHarYwJK4agb231vb5erasuGO463eYEG
    r4SfTuOm7SyiV2xxbaBKrXJtpBp4WLL/s+LF+nklKjaOxkmxUX0sM4CTA7uFJypY
    c8Tdr8lDDNqoUtMD8BrUCJi+7lmMXRcC3Qi3oZJW76ja+kZA5mKVFPd1ATih8TbA
    i34R7EQDtFeiSvBdeKRsPp8c0KT8H1B4lXNkkCQs2WX5p4lm99+ZtLD4glw8x6Ic
    i1YhgnQbn5E0hz55OLu5jvOkKQjPCW+8Kg==
    -----END CERTIFICATE-----", 
                "type": "server", 
                "create_time": "2018-09-28 03:00:47", 
                "private_key": "-----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAwZ5UJULAjWr7p6FVwGRQRjFN2s8tZ/6LC3X82fajpVsYqF1x
    qEuUDndDXVD09E4u83MS6HO6a3bIVQDp6/klnYldiE6Vp8HH5BSKaCWKVg8lGWg1
    UM9wZFnlryi14KgmpIFmcu9nA8yV/6MZAe6RSDmb3iyNBmiZ8aZhGw2pI1YwR+15
    MVqFFGB+7ExkziROi7L8CFCyCezK2/oOOvQsH1dzQ8z1JXWdg8/9Zx7Ktvgwu5PQ
    M3cJtSHX6iBPOkMU8Z8TugLlTqQXKZOEgwajwvQ5mf2DPkVgM08XAgaLJcLigwD5
    13koAdtJd5v+9irw+5LAuO3JclqwTvwy7u/YwwIDAQABAoIBACU9S5fjD9/jTMXA
    DRs08A+gGgZUxLn0xk+NAPX3LyB1tfdkCaFB8BccLzO6h3KZuwQOBPv6jkdvEDbx
    Nwyw3eA/9GJsIvKiHc0rejdvyPymaw9I8MA7NbXHaJrY7KpqDQyk6sx+aUTcy5jg
    iMXLWdwXYHhJ/1HVOo603oZyiS6HZeYU089NDUcX+1SJi3e5Ke0gPVXEqCq1O11/
    rh24bMxnwZo4PKBWdcMBN5Zf/4ij9vrZE+fFzW7vGBO48A5lvZxWU2U5t/OZQRtN
    1uLOHmMFa0FIF2aWbTVfwdUWAFsvAOkHj9VV8BXOUwKOUuEktdkfAlvrxmsFrO/H
    yDeYYPkCgYEA/S55CBbR0sMXpSZ56uRn8JHApZJhgkgvYr+FqDlJq/e92nAzf01P
    RoEBUajwrnf1ycevN/SDfbtWzq2XJGqhWdJmtpO16b7KBsC6BdRcH6dnOYh31jgA
    vABMIP3wzI4zSVTyxRE8LDuboytF1mSCeV5tHYPQTZNwrplDnLQhywcCgYEAw8Yc
    Uk/eiFr3hfH/ZohMfV5p82Qp7DNIGRzw8YtVG/3+vNXrAXW1VhugNhQY6L+zLtJC
    aKn84ooup0m3YCg0hvINqJuvzfsuzQgtjTXyaE0cEwsjUusOmiuj09vVx/3U7siK
    Hdjd2ICPCvQ6Q8tdi8jV320gMs05AtaBkZdsiWUCgYEAtLw4Kk4f+xTKDFsrLUNf
    75wcqhWVBiwBp7yQ7UX4EYsJPKZcHMRTk0EEcAbpyaJZE3I44vjp5ReXIHNLMfPs
    uvI34J4Rfot0LN3n7cFrAi2+wpNo+MOBwrNzpRmijGP2uKKrq4JiMjFbKV/6utGF
    Up7VxfwS904JYpqGaZctiIECgYA1A6nZtF0riY6ry/uAdXpZHL8ONNqRZtWoT0kD
    79otSVu5ISiRbaGcXsDExC52oKrSDAgFtbqQUiEOFg09UcXfoR6HwRkba2CiDwve
    yHQLQI5Qrdxz8Mk0gIrNrSM4FAmcW9vi9z4kCbQyoC5C+4gqeUlJRpDIkQBWP2Y4
    2ct/bQKBgHv8qCsQTZphOxc31BJPa2xVhuv18cEU3XLUrVfUZ/1f43JhLp7gynS2
    ep++LKUi9D0VGXY8bqvfJjbECoCeu85vl8NpCXwe/LoVoIn+7KaVIZMwqoGMfgNl
    nEqm7HWkNxHhf8A6En/IjleuddS1sf9e/x+TJN1Xhnt9W6pe7Fk1
    -----END RSA PRIVATE KEY-----", 
                "update_time": "2018-09-28 03:00:47", 
                "admin_state_up": true, 
                "tenant_id": "601240b9c5c94059b63d484c92cfe308", 
                "expire_time": "2020-12-03 03:42:49"
            }
        ], 
        "instance_num": 2
    }
    ```


## Status Code<a name="en-us_topic_0049139664_section36936567"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

