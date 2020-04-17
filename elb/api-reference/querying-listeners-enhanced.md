# Querying Listeners<a name="EN-US_TOPIC_0096561541"></a>

## Function<a name="en-us_topic_0049139640_section63419476"></a>

This API is used to query the listeners and display them in a list. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

You can query listeners by listener ID, listener protocol, listener port number, and backend server private IP address.

## URI<a name="en-us_topic_0049139640_section33904373"></a>

GET /v2.0/lbaas/listeners

## Constraints<a name="section22561942143020"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="section953184795619"></a>

**Table  1**  Request parameters

<a name="table69867585013"></a>
<table><thead align="left"><tr id="row1317546155014"><th class="cellrowborder" valign="top" width="34.07659234076592%" id="mcps1.2.5.1.1"><p id="p12175126145015"><a name="p12175126145015"></a><a name="p12175126145015"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.228777122287772%" id="mcps1.2.5.1.2"><p id="p10175146115017"><a name="p10175146115017"></a><a name="p10175146115017"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.918808119188082%" id="mcps1.2.5.1.3"><p id="p151751266502"><a name="p151751266502"></a><a name="p151751266502"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.77582241775822%" id="mcps1.2.5.1.4"><p id="p6175196195013"><a name="p6175196195013"></a><a name="p6175196195013"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row141756675014"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p91757625010"><a name="p91757625010"></a><a name="p91757625010"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p41761362509"><a name="p41761362509"></a><a name="p41761362509"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p5175116125016"><a name="p5175116125016"></a><a name="p5175116125016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the listener from which pagination query starts, that is, the ID of the last listener on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b335210505267"><a name="b335210505267"></a><a name="b335210505267"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row11761767506"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p0176206195012"><a name="p0176206195012"></a><a name="p0176206195012"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p201769618509"><a name="p201769618509"></a><a name="p201769618509"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p2176176165018"><a name="p2176176165018"></a><a name="p2176176165018"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of listeners on each page.</p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b65971554142618"><a name="b65971554142618"></a><a name="b65971554142618"></a>0</strong> to <strong id="b3598115419262"><a name="b3598115419262"></a><a name="b3598115419262"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row101767685014"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p21761566509"><a name="p21761566509"></a><a name="p21761566509"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p131761560504"><a name="p131761560504"></a><a name="p131761560504"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p61765665014"><a name="p61765665014"></a><a name="p61765665014"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b678814564268"><a name="b678814564268"></a><a name="b678814564268"></a>true</strong> or <strong id="b16789105642618"><a name="b16789105642618"></a><a name="b16789105642618"></a>false</strong>, and the default value is <strong id="b079075614260"><a name="b079075614260"></a><a name="b079075614260"></a>false</strong>. The last page in the list requested with <strong id="b147911556192610"><a name="b147911556192610"></a><a name="b147911556192610"></a>page_reverse</strong> set to <strong id="b1379235613261"><a name="b1379235613261"></a><a name="b1379235613261"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b779310563261"><a name="b779310563261"></a><a name="b779310563261"></a>page_reverse</strong> set to <strong id="b579435612615"><a name="b579435612615"></a><a name="b579435612615"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b165161019275"><a name="b165161019275"></a><a name="b165161019275"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row71765685015"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p21769645016"><a name="p21769645016"></a><a name="p21769645016"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p917656165016"><a name="p917656165016"></a><a name="p917656165016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p1513818471452"><a name="p1513818471452"></a><a name="p1513818471452"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p1017613635014"><a name="p1017613635014"></a><a name="p1017613635014"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="row2048684517367"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p16643140135418"><a name="p16643140135418"></a><a name="p16643140135418"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p13644150165414"><a name="p13644150165414"></a><a name="p13644150165414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p3643170135418"><a name="p3643170135418"></a><a name="p3643170135418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p1564410175417"><a name="p1564410175417"></a><a name="p1564410175417"></a>Specifies the ID of the project where the listener is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row7176161506"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p71763645016"><a name="p71763645016"></a><a name="p71763645016"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p1917615617500"><a name="p1917615617500"></a><a name="p1917615617500"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p141761964500"><a name="p141761964500"></a><a name="p141761964500"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p31767695017"><a name="p31767695017"></a><a name="p31767695017"></a>Specifies the listener name.</p>
<p id="p38262421513"><a name="p38262421513"></a><a name="p38262421513"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row151766685018"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p317614617508"><a name="p317614617508"></a><a name="p317614617508"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p31767605017"><a name="p31767605017"></a><a name="p31767605017"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p161761363507"><a name="p161761363507"></a><a name="p161761363507"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p151761663508"><a name="p151761663508"></a><a name="p151761663508"></a>Provides supplementary information about the listener.</p>
<p id="p117644019215"><a name="p117644019215"></a><a name="p117644019215"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row83718327418"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p123721432049"><a name="p123721432049"></a><a name="p123721432049"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p1372193214420"><a name="p1372193214420"></a><a name="p1372193214420"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p34016591519"><a name="p34016591519"></a><a name="p34016591519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p237314321348"><a name="p237314321348"></a><a name="p237314321348"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="row1947724920153"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p3469112575415"><a name="p3469112575415"></a><a name="p3469112575415"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p8758551203215"><a name="p8758551203215"></a><a name="p8758551203215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p144691725185411"><a name="p144691725185411"></a><a name="p144691725185411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p17928111314162"><a name="p17928111314162"></a><a name="p17928111314162"></a>Specifies the maximum number of connections.</p>
</td>
</tr>
<tr id="row3684133171618"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p446922525410"><a name="p446922525410"></a><a name="p446922525410"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p09741034182018"><a name="p09741034182018"></a><a name="p09741034182018"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p3469102512549"><a name="p3469102512549"></a><a name="p3469102512549"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p257371723315"><a name="p257371723315"></a><a name="p257371723315"></a>Specifies the administrative status of the listener.</p>
</td>
</tr>
<tr id="row131761655013"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p217614615014"><a name="p217614615014"></a><a name="p217614615014"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p191763675018"><a name="p191763675018"></a><a name="p191763675018"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p17694193261"><a name="p17694193261"></a><a name="p17694193261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p37555125518"><a name="p37555125518"></a><a name="p37555125518"></a>Specifies the ID of the associated backend server group.</p>
</td>
</tr>
<tr id="row2067105212119"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p149771721230"><a name="p149771721230"></a><a name="p149771721230"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p442984120254"><a name="p442984120254"></a><a name="p442984120254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p149775217319"><a name="p149775217319"></a><a name="p149775217319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p483792111330"><a name="p483792111330"></a><a name="p483792111330"></a>Specifies whether to use HTTP/2.</p>
<p id="p2022211012365"><a name="p2022211012365"></a><a name="p2022211012365"></a>The value can be <strong id="b02211105363"><a name="b02211105363"></a><a name="b02211105363"></a>true</strong> or <strong id="b72223108365"><a name="b72223108365"></a><a name="b72223108365"></a>false</strong>.</p>
<a name="ul11538616153618"></a><a name="ul11538616153618"></a><ul id="ul11538616153618"><li><strong id="b55371516153610"><a name="b55371516153610"></a><a name="b55371516153610"></a>true</strong>: HTTP/2 is used.</li><li><strong id="b1846421143614"><a name="b1846421143614"></a><a name="b1846421143614"></a>false</strong>: HTTP/2 is not used.</li></ul>
</td>
</tr>
<tr id="row717626155019"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p21762619502"><a name="p21762619502"></a><a name="p21762619502"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p817611615507"><a name="p817611615507"></a><a name="p817611615507"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p13176166500"><a name="p13176166500"></a><a name="p13176166500"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p181344416392"><a name="p181344416392"></a><a name="p181344416392"></a>Specifies the ID of the server certificate used by the listener. </p>
<p id="p1565614491224"><a name="p1565614491224"></a><a name="p1565614491224"></a>The value contains a maximum of 128 characters.</p>
</td>
</tr>
<tr id="row111769615501"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p51769665014"><a name="p51769665014"></a><a name="p51769665014"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p13932194612393"><a name="p13932194612393"></a><a name="p13932194612393"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p19176146165017"><a name="p19176146165017"></a><a name="p19176146165017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p1867105844415"><a name="p1867105844415"></a><a name="p1867105844415"></a>Specifies the ID of the CA certificate used by the listener. </p>
<p id="p119049551328"><a name="p119049551328"></a><a name="p119049551328"></a>The value contains a maximum of 128 characters.</p>
</td>
</tr>
<tr id="row1217676165011"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p18176106205012"><a name="p18176106205012"></a><a name="p18176106205012"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p6932349113916"><a name="p6932349113916"></a><a name="p6932349113916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p171766614502"><a name="p171766614502"></a><a name="p171766614502"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p1357614505345"><a name="p1357614505345"></a><a name="p1357614505345"></a>Specifies the load balancer protocol.</p>
<p id="p174283519346"><a name="p174283519346"></a><a name="p174283519346"></a>The value can be <strong id="b14390131992714"><a name="b14390131992714"></a><a name="b14390131992714"></a>TCP</strong>, <strong id="b153911519122711"><a name="b153911519122711"></a><a name="b153911519122711"></a>HTTP</strong>, <strong id="b16392181942718"><a name="b16392181942718"></a><a name="b16392181942718"></a>UDP</strong>, or <strong id="b739311912715"><a name="b739311912715"></a><a name="b739311912715"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row20177116115018"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p1217726115010"><a name="p1217726115010"></a><a name="p1217726115010"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p8582175163919"><a name="p8582175163919"></a><a name="p8582175163919"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p017716625011"><a name="p017716625011"></a><a name="p017716625011"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p57843549342"><a name="p57843549342"></a><a name="p57843549342"></a>Specifies the port used by the load balancer.</p>
</td>
</tr>
<tr id="row188318581139"><td class="cellrowborder" valign="top" width="34.07659234076592%" headers="mcps1.2.5.1.1 "><p id="p108551029191718"><a name="p108551029191718"></a><a name="p108551029191718"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="12.228777122287772%" headers="mcps1.2.5.1.2 "><p id="p1985511298179"><a name="p1985511298179"></a><a name="p1985511298179"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.5.1.3 "><p id="p18855429181713"><a name="p18855429181713"></a><a name="p18855429181713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.77582241775822%" headers="mcps1.2.5.1.4 "><p id="p39741913115313"><a name="p39741913115313"></a><a name="p39741913115313"></a>Specifies the security policy used by the listener. This parameter is valid only when the listener protocol is set to <strong id="b120172517270"><a name="b120172517270"></a><a name="b120172517270"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p144321427103316"><a name="p144321427103316"></a><a name="p144321427103316"></a>The value can be <strong id="b109411352174411"><a name="b109411352174411"></a><a name="b109411352174411"></a>tls-1-0</strong>, <strong id="b19942452144412"><a name="b19942452144412"></a><a name="b19942452144412"></a>tls-1-1</strong>, <strong id="b15942652134411"><a name="b15942652134411"></a><a name="b15942652134411"></a>tls-1-2</strong>, or <strong id="b17943752144412"><a name="b17943752144412"></a><a name="b17943752144412"></a>tls-1-2-strict</strong>. For details of cipher suites for each security policy, see <a href="#table210773231419">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **tls\_ciphers\_policy**  parameter description

<a name="table210773231419"></a>
<table><thead align="left"><tr id="en-us_topic_0096561542_row204784101539"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561542_p147851075312"><a name="en-us_topic_0096561542_p147851075312"></a><a name="en-us_topic_0096561542_p147851075312"></a>Security Policy</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561542_p2478181015313"><a name="en-us_topic_0096561542_p2478181015313"></a><a name="en-us_topic_0096561542_p2478181015313"></a>TLS Version</p>
</th>
<th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561542_p5478131085310"><a name="en-us_topic_0096561542_p5478131085310"></a><a name="en-us_topic_0096561542_p5478131085310"></a>Cipher Suite</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561542_row125843182408"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p12584131812401"><a name="en-us_topic_0096561542_p12584131812401"></a><a name="en-us_topic_0096561542_p12584131812401"></a>tls-1-0</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1358411811405"><a name="en-us_topic_0096561542_p1358411811405"></a><a name="en-us_topic_0096561542_p1358411811405"></a>TLSv1.2 TLSv1.1 TLSv1</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p152111143203617"><a name="en-us_topic_0096561542_p152111143203617"></a><a name="en-us_topic_0096561542_p152111143203617"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1250119222406"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p050232216409"><a name="en-us_topic_0096561542_p050232216409"></a><a name="en-us_topic_0096561542_p050232216409"></a>tls-1-1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p185021822194019"><a name="en-us_topic_0096561542_p185021822194019"></a><a name="en-us_topic_0096561542_p185021822194019"></a>TLSv1.2 TLSv1.1</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row19159426144017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p31598266400"><a name="en-us_topic_0096561542_p31598266400"></a><a name="en-us_topic_0096561542_p31598266400"></a>tls-1-2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p315914265406"><a name="en-us_topic_0096561542_p315914265406"></a><a name="en-us_topic_0096561542_p315914265406"></a>TLSv1.2</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row148501331204010"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p18850153164010"><a name="en-us_topic_0096561542_p18850153164010"></a><a name="en-us_topic_0096561542_p18850153164010"></a>tls-1-2-strict</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3850531104014"><a name="en-us_topic_0096561542_p3850531104014"></a><a name="en-us_topic_0096561542_p3850531104014"></a>TLSv1.2</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p12274148203711"><a name="en-us_topic_0096561542_p12274148203711"></a><a name="en-us_topic_0096561542_p12274148203711"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section799310441575"></a>

**Table  3**  Parameter description

<a name="table16124122820184"></a>
<table><thead align="left"><tr id="row1212482810180"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p4124162816187"><a name="p4124162816187"></a><a name="p4124162816187"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="p1712420286182"><a name="p1712420286182"></a><a name="p1712420286182"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.4.1.3"><p id="p1712452812188"><a name="p1712452812188"></a><a name="p1712452812188"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61251228181815"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p4125152819181"><a name="p4125152819181"></a><a name="p4125152819181"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p31268283180"><a name="p31268283180"></a><a name="p31268283180"></a>Lists the listeners. For details, see <a href="#table7513153305114">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **listeners**  parameter description

<a name="table7513153305114"></a>
<table><thead align="left"><tr id="row771363365118"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.1"><p id="p171318335512"><a name="p171318335512"></a><a name="p171318335512"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p1571383319519"><a name="p1571383319519"></a><a name="p1571383319519"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.4.1.3"><p id="p1571316338511"><a name="p1571316338511"></a><a name="p1571316338511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row117134338510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1071363315513"><a name="p1071363315513"></a><a name="p1071363315513"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p10139391812"><a name="p10139391812"></a><a name="p10139391812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p771343365112"><a name="p771343365112"></a><a name="p771343365112"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="row97131633145111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1471311335518"><a name="p1471311335518"></a><a name="p1471311335518"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1871353355117"><a name="p1871353355117"></a><a name="p1871353355117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p2714133313514"><a name="p2714133313514"></a><a name="p2714133313514"></a>Specifies the ID of the project where the listener is used.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1871413365119"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p971463311514"><a name="p971463311514"></a><a name="p971463311514"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p9714193314518"><a name="p9714193314518"></a><a name="p9714193314518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p2714113312516"><a name="p2714113312516"></a><a name="p2714113312516"></a>Specifies the listener name.</p>
<p id="p72790202339"><a name="p72790202339"></a><a name="p72790202339"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row171418339518"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p2714143355114"><a name="p2714143355114"></a><a name="p2714143355114"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p8714143335113"><a name="p8714143335113"></a><a name="p8714143335113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p37141833105119"><a name="p37141833105119"></a><a name="p37141833105119"></a>Provides supplementary information about the listener.</p>
<p id="p1031052293310"><a name="p1031052293310"></a><a name="p1031052293310"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row127143334510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1771413311511"><a name="p1771413311511"></a><a name="p1771413311511"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p187143333515"><a name="p187143333515"></a><a name="p187143333515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p13635517112512"><a name="p13635517112512"></a><a name="p13635517112512"></a>Specifies the load balancer protocol.</p>
<p id="p12240172442512"><a name="p12240172442512"></a><a name="p12240172442512"></a>The value can be <strong id="b1339154332716"><a name="b1339154332716"></a><a name="b1339154332716"></a>TCP</strong>, <strong id="b1440643112718"><a name="b1440643112718"></a><a name="b1440643112718"></a>HTTP</strong>, <strong id="b15421143162717"><a name="b15421143162717"></a><a name="b15421143162717"></a>UDP</strong>, or <strong id="b54324319274"><a name="b54324319274"></a><a name="b54324319274"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row11714153311510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p17714113335119"><a name="p17714113335119"></a><a name="p17714113335119"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p77141733185110"><a name="p77141733185110"></a><a name="p77141733185110"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p4234102316253"><a name="p4234102316253"></a><a name="p4234102316253"></a>Specifies the port used by the load balancer.</p>
<p id="p21641625112516"><a name="p21641625112516"></a><a name="p21641625112516"></a>The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="row1871418339516"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p2714933175115"><a name="p2714933175115"></a><a name="p2714933175115"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1657317179218"><a name="p1657317179218"></a><a name="p1657317179218"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p19714163375114"><a name="p19714163375114"></a><a name="p19714163375114"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="row1571553313516"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p17151633175117"><a name="p17151633175117"></a><a name="p17151633175117"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p97151533135114"><a name="p97151533135114"></a><a name="p97151533135114"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p338014284258"><a name="p338014284258"></a><a name="p338014284258"></a>Specifies the maximum number of connections.</p>
<p id="p179192029132514"><a name="p179192029132514"></a><a name="p179192029132514"></a>The value ranges from <strong id="b1543575416273"><a name="b1543575416273"></a><a name="b1543575416273"></a>-1</strong> to <strong id="b204361654162715"><a name="b204361654162715"></a><a name="b204361654162715"></a>2147483647</strong>.</p>
<div class="note" id="note2612124522519"><a name="note2612124522519"></a><a name="note2612124522519"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1061274542518"><a name="p1061274542518"></a><a name="p1061274542518"></a>This parameter is reserved. The default value is <strong id="b531515714272"><a name="b531515714272"></a><a name="b531515714272"></a>-1</strong>, indicating that there is no restriction on maximum connections.</p>
</div></div>
</td>
</tr>
<tr id="row7715113314517"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1271543375114"><a name="p1271543375114"></a><a name="p1271543375114"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p4715833115117"><a name="p4715833115117"></a><a name="p4715833115117"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p74175152615"><a name="p74175152615"></a><a name="p74175152615"></a>Specifies the administrative status of the listener.</p>
<div class="note" id="note18146211122615"><a name="note18146211122615"></a><a name="note18146211122615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p81465112267"><a name="p81465112267"></a><a name="p81465112267"></a>This parameter is reserved. Currently, the value can only be <strong id="b29554114196"><a name="b29554114196"></a><a name="b29554114196"></a>true</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1351310491008"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p6928153808"><a name="p6928153808"></a><a name="p6928153808"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p6928253307"><a name="p6928253307"></a><a name="p6928253307"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p139947263268"><a name="p139947263268"></a><a name="p139947263268"></a>Specifies whether to use HTTP/2.</p>
<p id="p13908912161017"><a name="p13908912161017"></a><a name="p13908912161017"></a>The value can be <strong id="b1790851201018"><a name="b1790851201018"></a><a name="b1790851201018"></a>true</strong> or <strong id="b7908121218109"><a name="b7908121218109"></a><a name="b7908121218109"></a>false</strong>.</p>
<a name="ul4188182016108"></a><a name="ul4188182016108"></a><ul id="ul4188182016108"><li><strong id="b15187132021017"><a name="b15187132021017"></a><a name="b15187132021017"></a>true</strong>: HTTP/2 will be used.</li><li><strong id="b131812213102"><a name="b131812213102"></a><a name="b131812213102"></a>false</strong>: HTTP/2 will not be used.</li></ul>
<div class="note" id="note11703173412265"><a name="note11703173412265"></a><a name="note11703173412265"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1570312347262"><a name="p1570312347262"></a><a name="p1570312347262"></a>This parameter is valid only when the load balancer protocol is set to <strong id="b1221661112288"><a name="b1221661112288"></a><a name="b1221661112288"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row20716125691519"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1342713011617"><a name="p1342713011617"></a><a name="p1342713011617"></a>keepalive_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p34271904163"><a name="p34271904163"></a><a name="p34271904163"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p1442714021610"><a name="p1442714021610"></a><a name="p1442714021610"></a>Specifies the idle timeout duration in the unit of second.</p>
<p id="p1542817031611"><a name="p1542817031611"></a><a name="p1542817031611"></a>The value ranges from <strong id="b2575162384915"><a name="b2575162384915"></a><a name="b2575162384915"></a>1</strong> to <strong id="b1157516237496"><a name="b1157516237496"></a><a name="b1157516237496"></a>300</strong>. The default value is <strong id="b15481172754910"><a name="b15481172754910"></a><a name="b15481172754910"></a>15</strong>.</p>
</td>
</tr>
<tr id="row1449885814157"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p842816018164"><a name="p842816018164"></a><a name="p842816018164"></a>client_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p14428160181615"><a name="p14428160181615"></a><a name="p14428160181615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p7428140131619"><a name="p7428140131619"></a><a name="p7428140131619"></a>Specifies the request timeout duration in the unit of second.</p>
<p id="p14283041612"><a name="p14283041612"></a><a name="p14283041612"></a>The value ranges from <strong id="b3599162964913"><a name="b3599162964913"></a><a name="b3599162964913"></a>1</strong> to <strong id="b86004292499"><a name="b86004292499"></a><a name="b86004292499"></a>60</strong>. The default value is <strong id="b138541850155516"><a name="b138541850155516"></a><a name="b138541850155516"></a>60</strong>.</p>
<p id="p94289051613"><a name="p94289051613"></a><a name="p94289051613"></a>This parameter is valid only when <strong id="b03345356497"><a name="b03345356497"></a><a name="b03345356497"></a>protocol</strong> is set to <strong id="b18334203513493"><a name="b18334203513493"></a><a name="b18334203513493"></a>HTTP</strong> or <strong id="b433593514490"><a name="b433593514490"></a><a name="b433593514490"></a>HTTPS</strong>. In other cases, the request body does not contain this parameter. Otherwise, an error is reported. When <strong id="b134114372492"><a name="b134114372492"></a><a name="b134114372492"></a>protocol</strong> is set to <strong id="b934212370492"><a name="b934212370492"></a><a name="b934212370492"></a>HTTP</strong> or <strong id="b12343203794912"><a name="b12343203794912"></a><a name="b12343203794912"></a>HTTPS</strong>, if the request body does not contain this parameter or the value of this parameter is <strong id="b634319370497"><a name="b634319370497"></a><a name="b634319370497"></a>null</strong>, the default value is used.</p>
</td>
</tr>
<tr id="row123825411510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p742850131616"><a name="p742850131616"></a><a name="p742850131616"></a>member_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p242814013168"><a name="p242814013168"></a><a name="p242814013168"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p34293061614"><a name="p34293061614"></a><a name="p34293061614"></a>Specifies the response timeout duration in the unit of second.</p>
<p id="p1042918011613"><a name="p1042918011613"></a><a name="p1042918011613"></a>The value ranges from <strong id="b73912437492"><a name="b73912437492"></a><a name="b73912437492"></a>1</strong> to <strong id="b16392154311498"><a name="b16392154311498"></a><a name="b16392154311498"></a>60</strong>. The default value is <strong id="b1431105765514"><a name="b1431105765514"></a><a name="b1431105765514"></a>60</strong>.</p>
<p id="p44291507163"><a name="p44291507163"></a><a name="p44291507163"></a>This parameter is valid only when <strong id="b16290124511496"><a name="b16290124511496"></a><a name="b16290124511496"></a>protocol</strong> is set to <strong id="b729124574913"><a name="b729124574913"></a><a name="b729124574913"></a>HTTP</strong> or <strong id="b42921459495"><a name="b42921459495"></a><a name="b42921459495"></a>HTTPS</strong>. In other cases, the request body does not contain this parameter. Otherwise, an error is reported. When <strong id="b1753074718494"><a name="b1753074718494"></a><a name="b1753074718494"></a>protocol</strong> is set to <strong id="b195301347164912"><a name="b195301347164912"></a><a name="b195301347164912"></a>HTTP</strong> or <strong id="b20531447194920"><a name="b20531447194920"></a><a name="b20531447194920"></a>HTTPS</strong>, if the request body does not contain this parameter or the value of this parameter is <strong id="b253254724912"><a name="b253254724912"></a><a name="b253254724912"></a>null</strong>, the default value is used.</p>
</td>
</tr>
<tr id="row0715113345110"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p47159334519"><a name="p47159334519"></a><a name="p47159334519"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p186201828101520"><a name="p186201828101520"></a><a name="p186201828101520"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p4120520262"><a name="p4120520262"></a><a name="p4120520262"></a>Specifies the ID of the associated backend server group.</p>
<div class="note" id="note106962612710"><a name="note106962612710"></a><a name="note106962612710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p569636182713"><a name="p569636182713"></a><a name="p569636182713"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="b1929412340281"><a name="b1929412340281"></a><a name="b1929412340281"></a>null</strong>, the listener has no default backend server group.</p>
</div></div>
</td>
</tr>
<tr id="row17159330511"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p2715533105114"><a name="p2715533105114"></a><a name="p2715533105114"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1715733105114"><a name="p1715733105114"></a><a name="p1715733105114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p18611424122713"><a name="p18611424122713"></a><a name="p18611424122713"></a>Specifies the ID of the server certificate used by the listener. </p>
<p id="p040503214278"><a name="p040503214278"></a><a name="p040503214278"></a>This parameter is mandatory when <strong id="b825164519288"><a name="b825164519288"></a><a name="b825164519288"></a>protocol</strong> is set to <strong id="b162521145182819"><a name="b162521145182819"></a><a name="b162521145182819"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p10113123118354"><a name="p10113123118354"></a><a name="p10113123118354"></a>The value contains a maximum of 128 characters.</p>
</td>
</tr>
<tr id="row271518338518"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p171663310517"><a name="p171663310517"></a><a name="p171663310517"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p37161733175120"><a name="p37161733175120"></a><a name="p37161733175120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p1853317431767"><a name="p1853317431767"></a><a name="p1853317431767"></a>Specifies the ID of the CA certificate used by the listener. </p>
<p id="p7305173920352"><a name="p7305173920352"></a><a name="p7305173920352"></a>The value contains a maximum of 128 characters.</p>
</td>
</tr>
<tr id="row1716533165111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p14716113395119"><a name="p14716113395119"></a><a name="p14716113395119"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1796173211218"><a name="p1796173211218"></a><a name="p1796173211218"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p5222411996"><a name="p5222411996"></a><a name="p5222411996"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
</td>
</tr>
<tr id="row7716433125110"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p87169330512"><a name="p87169330512"></a><a name="p87169330512"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p169301235111217"><a name="p169301235111217"></a><a name="p169301235111217"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p11716533145115"><a name="p11716533145115"></a><a name="p11716533145115"></a>Tags the listener.</p>
</td>
</tr>
<tr id="row1035019216565"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p18781627124910"><a name="p18781627124910"></a><a name="p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p18781627204916"><a name="p18781627204916"></a><a name="p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p578162719490"><a name="p578162719490"></a><a name="p578162719490"></a>Specifies the time when the listener was created. The UTC time is in <em id="i1190484720259"><a name="i1190484720259"></a><a name="i1190484720259"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p45428255365"><a name="p45428255365"></a><a name="p45428255365"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="row116631226145613"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p1541843114495"><a name="p1541843114495"></a><a name="p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1810172112506"><a name="p1810172112506"></a><a name="p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p341843144919"><a name="p341843144919"></a><a name="p341843144919"></a>Specifies the time when the listener was updated. The UTC time is in <em id="i16321552112512"><a name="i16321552112512"></a><a name="i16321552112512"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p1156683019369"><a name="p1156683019369"></a><a name="p1156683019369"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="row3525155183018"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p35181611103114"><a name="p35181611103114"></a><a name="p35181611103114"></a>listeners_links</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19550113461219"><a name="p19550113461219"></a><a name="p19550113461219"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p16322173094712"><a name="p16322173094712"></a><a name="p16322173094712"></a>Provides links to the previous or next page during pagination query, respectively. This parameter exists only in the response body of pagination query. </p>
</td>
</tr>
<tr id="row7152842163513"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p15804713184311"><a name="p15804713184311"></a><a name="p15804713184311"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p78041413134319"><a name="p78041413134319"></a><a name="p78041413134319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p546123425013"><a name="p546123425013"></a><a name="p546123425013"></a>Specifies the security policy used by the listener. This parameter is valid only when the load balancer protocol is set to <strong id="b1513919143290"><a name="b1513919143290"></a><a name="b1513919143290"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p15605659143417"><a name="p15605659143417"></a><a name="p15605659143417"></a>The value can be <strong id="b7763185564411"><a name="b7763185564411"></a><a name="b7763185564411"></a>tls-1-0</strong>, <strong id="b776415574413"><a name="b776415574413"></a><a name="b776415574413"></a>tls-1-1</strong>, <strong id="b07641355114413"><a name="b07641355114413"></a><a name="b07641355114413"></a>tls-1-2</strong>, or <strong id="b187651555164415"><a name="b187651555164415"></a><a name="b187651555164415"></a>tls-1-2-strict</strong>, and the default value is <strong id="b276545554419"><a name="b276545554419"></a><a name="b276545554419"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="#table10264143363610">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **listeners\_links**  parameter description

<a name="table13018211316"></a>
<table><thead align="left"><tr id="row1210016215316"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.1"><p id="p11100162113113"><a name="p11100162113113"></a><a name="p11100162113113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p91006215318"><a name="p91006215318"></a><a name="p91006215318"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.4.1.3"><p id="p81001321123110"><a name="p81001321123110"></a><a name="p81001321123110"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1410092113119"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p14100192111317"><a name="p14100192111317"></a><a name="p14100192111317"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p16100112116310"><a name="p16100112116310"></a><a name="p16100112116310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p1510010219313"><a name="p1510010219313"></a><a name="p1510010219313"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row3100521163111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.1 "><p id="p4100102114311"><a name="p4100102114311"></a><a name="p4100102114311"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p17100112183117"><a name="p17100112183117"></a><a name="p17100112183117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.3 "><p id="p12341183715289"><a name="p12341183715289"></a><a name="p12341183715289"></a>Specifies the prompt of the previous or next page.</p>
<p id="p1770517380282"><a name="p1770517380282"></a><a name="p1770517380282"></a>The value can be <strong id="b842352706175823"><a name="b842352706175823"></a><a name="b842352706175823"></a>next</strong> or <strong id="b842352706175826"><a name="b842352706175826"></a><a name="b842352706175826"></a>previous</strong>. The value <strong id="b8423527062079"><a name="b8423527062079"></a><a name="b8423527062079"></a>next</strong> indicates the href containing the URL of the next page, and <strong id="b84235270620752"><a name="b84235270620752"></a><a name="b84235270620752"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **tls\_ciphers\_policy**  parameter description

<a name="table10264143363610"></a>
<table><thead align="left"><tr id="en-us_topic_0096561542_row204784101539_1"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561542_p147851075312_1"><a name="en-us_topic_0096561542_p147851075312_1"></a><a name="en-us_topic_0096561542_p147851075312_1"></a>Security Policy</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561542_p2478181015313_1"><a name="en-us_topic_0096561542_p2478181015313_1"></a><a name="en-us_topic_0096561542_p2478181015313_1"></a>TLS Version</p>
</th>
<th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561542_p5478131085310_1"><a name="en-us_topic_0096561542_p5478131085310_1"></a><a name="en-us_topic_0096561542_p5478131085310_1"></a>Cipher Suite</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561542_row125843182408_1"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p12584131812401_1"><a name="en-us_topic_0096561542_p12584131812401_1"></a><a name="en-us_topic_0096561542_p12584131812401_1"></a>tls-1-0</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1358411811405_1"><a name="en-us_topic_0096561542_p1358411811405_1"></a><a name="en-us_topic_0096561542_p1358411811405_1"></a>TLSv1.2 TLSv1.1 TLSv1</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p152111143203617_1"><a name="en-us_topic_0096561542_p152111143203617_1"></a><a name="en-us_topic_0096561542_p152111143203617_1"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1250119222406_1"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p050232216409_1"><a name="en-us_topic_0096561542_p050232216409_1"></a><a name="en-us_topic_0096561542_p050232216409_1"></a>tls-1-1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p185021822194019_1"><a name="en-us_topic_0096561542_p185021822194019_1"></a><a name="en-us_topic_0096561542_p185021822194019_1"></a>TLSv1.2 TLSv1.1</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row19159426144017_1"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p31598266400_1"><a name="en-us_topic_0096561542_p31598266400_1"></a><a name="en-us_topic_0096561542_p31598266400_1"></a>tls-1-2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p315914265406_1"><a name="en-us_topic_0096561542_p315914265406_1"></a><a name="en-us_topic_0096561542_p315914265406_1"></a>TLSv1.2</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row148501331204010_1"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p18850153164010_1"><a name="en-us_topic_0096561542_p18850153164010_1"></a><a name="en-us_topic_0096561542_p18850153164010_1"></a>tls-1-2-strict</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3850531104014_1"><a name="en-us_topic_0096561542_p3850531104014_1"></a><a name="en-us_topic_0096561542_p3850531104014_1"></a>TLSv1.2</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p12274148203711_1"><a name="en-us_topic_0096561542_p12274148203711_1"></a><a name="en-us_topic_0096561542_p12274148203711_1"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section9122182510112"></a>

-   Example request 1: Querying all listeners

    ```
    GET https://{Endpoint}/v2.0/lbaas/listeners
    ```


-   Example response 1

    ```
    {
        "listeners": [
            {
                "client_ca_tls_container_ref": null,
                "protocol": "TCP",
                "description": "",
                "default_tls_container_ref": null,
                "admin_state_up": true,
                "http2_enable": false,
                "loadbalancers": [
                    {
                        "id": "bc7ba445-035a-4464-a1a3-a62cf4a14116"
                    }
                ],
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
     
                "sni_container_refs": [],
                "connection_limit": -1,
                "protocol_port": 80,
                "default_pool_id": "ed75f16e-fcc6-403e-a3fb-4eae82005eab",
                "id": "75045172-70e9-480d-9443-b8b6459948f7",
                "tags": [],
                "name": "listener-cb2n",
                "tls_ciphers_policy": null,     
                "created_at": "2018-07-25T01:54:13", 
                "updated_at": "2018-07-25T01:54:14"
            },
            {
                "client_ca_tls_container_ref": null,
                "protocol": "TCP",
                "description": "",
                "default_tls_container_ref": null,
                "admin_state_up": true,
                "http2_enable": false,
                "loadbalancers": [
                    {
                        "id": "165b6a38-5278-4569-b747-b2ee65ea84a4"
                    }
                ],
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
     
                "sni_container_refs": [],
                "connection_limit": -1,
                "protocol_port": 8080,
                "default_pool_id": null,
                "id": "dada0003-7b0e-4de8-a4e1-1e937be2ba14",
                "tags": [],
                "name": "lsnr_name_mod",
                "tls_ciphers_policy": null,
                "created_at": "2018-07-25T01:54:13", 
                "updated_at": "2018-07-25T01:54:14"
      
    ,
     
            }
        ]
    }
    ```

-   Request example 2: Querying UDP listeners

    ```
    GET https://{Endpoint}/v2.0/lbaas/listeners?protocol=UDP
    ```

-   Example response 2

    ```
    {
        "listeners": [
            {
                "protocol_port": 64809,
                "protocol": "UDP",
                "description": "",
                "default_tls_container_ref": null,
                "sni_container_refs": [],
                "loadbalancers": [
                    {
                        "id": "c1127125-64a9-4394-a08a-ef3be8f7ef9c"
                    }
                ],
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
      
                "created_at": "2018-11-29T13:56:21",
                "client_ca_tls_container_ref": null,
                "connection_limit": -1,
                "updated_at": "2018-11-29T13:56:22",
                "http2_enable": false,
                "tls_ciphers_policy": null,
                "admin_state_up": true,
                "default_pool_id": "2f6895be-019b-4c82-9b53-c4a2ac009e20",
                "id": "5c63d176-444f-4c75-9cfe-bcb8a05a845c",
                "tags": [],
                "name": "listener-tvp8"
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0049139640_section48411444"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

