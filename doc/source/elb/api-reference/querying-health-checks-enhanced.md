# Querying Health Checks<a name="EN-US_TOPIC_0096561561"></a>

## Function<a name="en-us_topic_0049139663_section26745965"></a>

This API is used to query the health checks. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="en-us_topic_0049139663_section39387099"></a>

GET /v2.0/lbaas/healthmonitors

## Constraints<a name="section17493944522"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="en-us_topic_0049139663_section49635175"></a>

**Table  1**  Request parameters

<a name="table475513722510"></a>
<table><thead align="left"><tr id="row62353814250"><th class="cellrowborder" valign="top" width="23.607639236076388%" id="mcps1.2.5.1.1"><p id="p623838172512"><a name="p623838172512"></a><a name="p623838172512"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.73882611738826%" id="mcps1.2.5.1.2"><p id="p17231738172520"><a name="p17231738172520"></a><a name="p17231738172520"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.168783121687829%" id="mcps1.2.5.1.3"><p id="p7231938162519"><a name="p7231938162519"></a><a name="p7231938162519"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.4847515248475%" id="mcps1.2.5.1.4"><p id="p1723183812513"><a name="p1723183812513"></a><a name="p1723183812513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row223153816256"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1323738122511"><a name="p1323738122511"></a><a name="p1323738122511"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p423038182519"><a name="p423038182519"></a><a name="p423038182519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p323103802513"><a name="p323103802513"></a><a name="p323103802513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the health check from which pagination query starts, that is, the ID of the last health check on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b17447204517392"><a name="b17447204517392"></a><a name="b17447204517392"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row92383812516"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p12259381251"><a name="p12259381251"></a><a name="p12259381251"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p1425138152515"><a name="p1425138152515"></a><a name="p1425138152515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p825153822512"><a name="p825153822512"></a><a name="p825153822512"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of health checks on each page.</p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b1840495811395"><a name="b1840495811395"></a><a name="b1840495811395"></a>0</strong> to <strong id="b134051958143912"><a name="b134051958143912"></a><a name="b134051958143912"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row1225638172517"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1825143819256"><a name="p1825143819256"></a><a name="p1825143819256"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p192563832513"><a name="p192563832513"></a><a name="p192563832513"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p1225138162511"><a name="p1225138162511"></a><a name="p1225138162511"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b3335104216582"><a name="b3335104216582"></a><a name="b3335104216582"></a>true</strong> or <strong id="b7336142195813"><a name="b7336142195813"></a><a name="b7336142195813"></a>false</strong>, and the default value is <strong id="b1733610423581"><a name="b1733610423581"></a><a name="b1733610423581"></a>false</strong>. The last page in the list requested with <strong id="b19337174210587"><a name="b19337174210587"></a><a name="b19337174210587"></a>page_reverse</strong> set to <strong id="b1433774216586"><a name="b1433774216586"></a><a name="b1433774216586"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b20338542105814"><a name="b20338542105814"></a><a name="b20338542105814"></a>page_reverse</strong> set to <strong id="b13338184211583"><a name="b13338184211583"></a><a name="b13338184211583"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b6580105914399"><a name="b6580105914399"></a><a name="b6580105914399"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row925183882518"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1325133811258"><a name="p1325133811258"></a><a name="p1325133811258"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p142553892513"><a name="p142553892513"></a><a name="p142553892513"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p121782018181719"><a name="p121782018181719"></a><a name="p121782018181719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p825538132511"><a name="p825538132511"></a><a name="p825538132511"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="row025173810255"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1425538202516"><a name="p1425538202516"></a><a name="p1425538202516"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p162543820253"><a name="p162543820253"></a><a name="p162543820253"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p02517389256"><a name="p02517389256"></a><a name="p02517389256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p20526512"><a name="p20526512"></a><a name="p20526512"></a>Specifies the ID of the project where the health check is performed.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row112503842517"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p72593832511"><a name="p72593832511"></a><a name="p72593832511"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p3251738182518"><a name="p3251738182518"></a><a name="p3251738182518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p525338102512"><a name="p525338102512"></a><a name="p525338102512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p14251338172514"><a name="p14251338172514"></a><a name="p14251338172514"></a>Specifies the health check name.</p>
<p id="p1572924515612"><a name="p1572924515612"></a><a name="p1572924515612"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row32516389251"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1625163892519"><a name="p1625163892519"></a><a name="p1625163892519"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p1525183872520"><a name="p1525183872520"></a><a name="p1525183872520"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p1325938152515"><a name="p1325938152515"></a><a name="p1325938152515"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p62583818257"><a name="p62583818257"></a><a name="p62583818257"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="b75431021403"><a name="b75431021403"></a><a name="b75431021403"></a>1</strong> to <strong id="b254432154011"><a name="b254432154011"></a><a name="b254432154011"></a>50</strong>.</p>
</td>
</tr>
<tr id="row82583892516"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1425193811250"><a name="p1425193811250"></a><a name="p1425193811250"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p6266382258"><a name="p6266382258"></a><a name="p6266382258"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p112523813252"><a name="p112523813252"></a><a name="p112523813252"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p32643817257"><a name="p32643817257"></a><a name="p32643817257"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="b1293103215274"><a name="b1293103215274"></a><a name="b1293103215274"></a>fail</strong> to <strong id="b89473252715"><a name="b89473252715"></a><a name="b89473252715"></a>success</strong>. The value ranges from <strong id="b169519327276"><a name="b169519327276"></a><a name="b169519327276"></a>1</strong> to <strong id="b69673272715"><a name="b69673272715"></a><a name="b69673272715"></a>10</strong>.</p>
</td>
</tr>
<tr id="row10268386257"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p626123818257"><a name="p626123818257"></a><a name="p626123818257"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p726123817254"><a name="p726123817254"></a><a name="p726123817254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p182615381254"><a name="p182615381254"></a><a name="p182615381254"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p88489418492"><a name="p88489418492"></a><a name="p88489418492"></a>Specifies the administrative status of the health check.</p>
<p id="p19848040494"><a name="p19848040494"></a><a name="p19848040494"></a>The value can be <strong id="b6866118174016"><a name="b6866118174016"></a><a name="b6866118174016"></a>true</strong> or <strong id="b1686738124019"><a name="b1686738124019"></a><a name="b1686738124019"></a>false</strong>. The default value is <strong id="b486299164013"><a name="b486299164013"></a><a name="b486299164013"></a>true</strong>.</p>
<a name="ul1848244497"></a><a name="ul1848244497"></a><ul id="ul1848244497"><li><strong id="b19286191164016"><a name="b19286191164016"></a><a name="b19286191164016"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="b2067119127409"><a name="b2067119127409"></a><a name="b2067119127409"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="row126183852517"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p12268381258"><a name="p12268381258"></a><a name="p12268381258"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p10268386258"><a name="p10268386258"></a><a name="p10268386258"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p1826193817257"><a name="p1826193817257"></a><a name="p1826193817257"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p37112334494"><a name="p37112334494"></a><a name="p37112334494"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="b206981131408"><a name="b206981131408"></a><a name="b206981131408"></a>1</strong> to <strong id="b186992013144017"><a name="b186992013144017"></a><a name="b186992013144017"></a>50</strong>.</p>
<div class="note" id="note77113384910"><a name="note77113384910"></a><a name="note77113384910"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p57123374911"><a name="p57123374911"></a><a name="p57123374911"></a>You are advised to set the value less than that of parameter <strong id="b10731157401"><a name="b10731157401"></a><a name="b10731157401"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row727133820254"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1027738102511"><a name="p1027738102511"></a><a name="p1027738102511"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p102713814259"><a name="p102713814259"></a><a name="p102713814259"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p15271738142512"><a name="p15271738142512"></a><a name="p15271738142512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p87193317494"><a name="p87193317494"></a><a name="p87193317494"></a>Specifies the health check protocol.</p>
<p id="p5711533184919"><a name="p5711533184919"></a><a name="p5711533184919"></a>The value can be <strong id="b279712198409"><a name="b279712198409"></a><a name="b279712198409"></a>TCP</strong>, <strong id="b11797119184013"><a name="b11797119184013"></a><a name="b11797119184013"></a>UDP_CONNECT</strong>, or <strong id="b8798101910404"><a name="b8798101910404"></a><a name="b8798101910404"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row1527103816252"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p1327173832513"><a name="p1327173832513"></a><a name="p1327173832513"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p3271638132514"><a name="p3271638132514"></a><a name="p3271638132514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p172723818256"><a name="p172723818256"></a><a name="p172723818256"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p19915125974920"><a name="p19915125974920"></a><a name="p19915125974920"></a>Specifies the port used for the health check.</p>
<p id="p1891535916496"><a name="p1891535916496"></a><a name="p1891535916496"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="row0271038162513"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p629133810250"><a name="p629133810250"></a><a name="p629133810250"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p19291638162512"><a name="p19291638162512"></a><a name="p19291638162512"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p122919386252"><a name="p122919386252"></a><a name="p122919386252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p49464171"><a name="p49464171"></a><a name="p49464171"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="p42524361"><a name="p42524361"></a><a name="p42524361"></a>A single value, such as 200</p>
<p id="p47174935"><a name="p47174935"></a><a name="p47174935"></a>A list of values, such as 200 and 202</p>
<p id="p21921239"><a name="p21921239"></a><a name="p21921239"></a>A value range, such as 200 to 204</p>
<p id="p63073424"><a name="p63073424"></a><a name="p63073424"></a>This parameter is valid when the value of <strong id="b198618422388"><a name="b198618422388"></a><a name="b198618422388"></a>type</strong> is set to <strong id="b1615439386"><a name="b1615439386"></a><a name="b1615439386"></a>HTTP</strong>.</p>
<p id="p08925875615"><a name="p08925875615"></a><a name="p08925875615"></a>The value contains a maximum of 64 characters.</p>
<div class="note" id="note30789909"><a name="note30789909"></a><a name="note30789909"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p8673725"><a name="p8673725"></a><a name="p8673725"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
<tr id="row18291238142519"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p8291238142511"><a name="p8291238142511"></a><a name="p8291238142511"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p1829338142510"><a name="p1829338142510"></a><a name="p1829338142510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p102993802515"><a name="p102993802515"></a><a name="p102993802515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p12394754125016"><a name="p12394754125016"></a><a name="p12394754125016"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="p73941354135010"><a name="p73941354135010"></a><a name="p73941354135010"></a>This parameter is valid when the value of <strong id="b6474934154017"><a name="b6474934154017"></a><a name="b6474934154017"></a>type</strong> is set to <strong id="b17474534174013"><a name="b17474534174013"></a><a name="b17474534174013"></a>HTTP</strong>.</p>
<p id="p14394115411501"><a name="p14394115411501"></a><a name="p14394115411501"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="p15394145435010"><a name="p15394145435010"></a><a name="p15394145435010"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="b14041559174319"><a name="b14041559174319"></a><a name="b14041559174319"></a>www.test.com</strong>.</p>
<p id="p17715201310572"><a name="p17715201310572"></a><a name="p17715201310572"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="row1629183822512"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p829238162515"><a name="p829238162515"></a><a name="p829238162515"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p1129638142512"><a name="p1129638142512"></a><a name="p1129638142512"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p112993814256"><a name="p112993814256"></a><a name="p112993814256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p6417986512"><a name="p6417986512"></a><a name="p6417986512"></a>Specifies the HTTP request path for the health check. The default value is <strong id="b1424610413402"><a name="b1424610413402"></a><a name="b1424610413402"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="p64181884511"><a name="p64181884511"></a><a name="p64181884511"></a>This parameter is valid when the value of <strong id="b13342114424010"><a name="b13342114424010"></a><a name="b13342114424010"></a>type</strong> is set to <strong id="b9343184424014"><a name="b9343184424014"></a><a name="b9343184424014"></a>HTTP</strong>.</p>
<p id="p1341818185114"><a name="p1341818185114"></a><a name="p1341818185114"></a>An example value is <strong id="b489644594013"><a name="b489644594013"></a><a name="b489644594013"></a>/test</strong>.</p>
<p id="p1255119268570"><a name="p1255119268570"></a><a name="p1255119268570"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row202953802512"><td class="cellrowborder" valign="top" width="23.607639236076388%" headers="mcps1.2.5.1.1 "><p id="p829238102516"><a name="p829238102516"></a><a name="p829238102516"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="11.73882611738826%" headers="mcps1.2.5.1.2 "><p id="p20305388256"><a name="p20305388256"></a><a name="p20305388256"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.168783121687829%" headers="mcps1.2.5.1.3 "><p id="p15291338172512"><a name="p15291338172512"></a><a name="p15291338172512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.4847515248475%" headers="mcps1.2.5.1.4 "><p id="p48511267514"><a name="p48511267514"></a><a name="p48511267514"></a>Specifies the HTTP request method. The default value is <strong id="b0191547144015"><a name="b0191547144015"></a><a name="b0191547144015"></a>GET</strong>.</p>
<p id="p11851326135110"><a name="p11851326135110"></a><a name="p11851326135110"></a>The value can be <strong id="b184467487409"><a name="b184467487409"></a><a name="b184467487409"></a>GET</strong>, <strong id="b444774816404"><a name="b444774816404"></a><a name="b444774816404"></a>HEAD</strong>, <strong id="b18448124815404"><a name="b18448124815404"></a><a name="b18448124815404"></a>POST</strong>, <strong id="b3449194810402"><a name="b3449194810402"></a><a name="b3449194810402"></a>PUT</strong>, <strong id="b84496486404"><a name="b84496486404"></a><a name="b84496486404"></a>DELETE</strong>, <strong id="b11450124818402"><a name="b11450124818402"></a><a name="b11450124818402"></a>TRACE</strong>, <strong id="b1745164804010"><a name="b1745164804010"></a><a name="b1745164804010"></a>OPTIONS</strong>, <strong id="b1745294815405"><a name="b1745294815405"></a><a name="b1745294815405"></a>CONNECT</strong>, and <strong id="b184531848154018"><a name="b184531848154018"></a><a name="b184531848154018"></a>PATCH</strong>.</p>
<p id="p485142665115"><a name="p485142665115"></a><a name="p485142665115"></a>This parameter is valid when the value of <strong id="b679174914011"><a name="b679174914011"></a><a name="b679174914011"></a>type</strong> is set to <strong id="b157921949144015"><a name="b157921949144015"></a><a name="b157921949144015"></a>HTTP</strong>.</p>
<p id="p040018332572"><a name="p040018332572"></a><a name="p040018332572"></a>The value contains a maximum of 16 characters.</p>
<div class="note" id="note985119267515"><a name="note985119267515"></a><a name="note985119267515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1885112263511"><a name="p1885112263511"></a><a name="p1885112263511"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049139663_section44063391"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0049139663_table5773255"></a>
<table><thead align="left"><tr id="en-us_topic_0049139663_row19618454"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="en-us_topic_0049139663_p45590951"><a name="en-us_topic_0049139663_p45590951"></a><a name="en-us_topic_0049139663_p45590951"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.2"><p id="en-us_topic_0049139663_p1879552"><a name="en-us_topic_0049139663_p1879552"></a><a name="en-us_topic_0049139663_p1879552"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.60606060606061%" id="mcps1.2.4.1.3"><p id="en-us_topic_0049139663_p50824621"><a name="en-us_topic_0049139663_p50824621"></a><a name="en-us_topic_0049139663_p50824621"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139663_row23153616"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0049139663_p63503579"><a name="en-us_topic_0049139663_p63503579"></a><a name="en-us_topic_0049139663_p63503579"></a>healthmonitors</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0049139663_p43516279"><a name="en-us_topic_0049139663_p43516279"></a><a name="en-us_topic_0049139663_p43516279"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0049139663_p29202048"><a name="en-us_topic_0049139663_p29202048"></a><a name="en-us_topic_0049139663_p29202048"></a>Lists the health checks. For details, see <a href="#table6429512132610">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **healthmonitors**  parameter description

<a name="table6429512132610"></a>
<table><thead align="left"><tr id="row6625112172620"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p13625012132618"><a name="p13625012132618"></a><a name="p13625012132618"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p146251412102614"><a name="p146251412102614"></a><a name="p146251412102614"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.3"><p id="p3625151282618"><a name="p3625151282618"></a><a name="p3625151282618"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row206251212202620"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p76251212172616"><a name="p76251212172616"></a><a name="p76251212172616"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1391115489185"><a name="p1391115489185"></a><a name="p1391115489185"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p1262661216262"><a name="p1262661216262"></a><a name="p1262661216262"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="row1562618124262"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1743205119187"><a name="p1743205119187"></a><a name="p1743205119187"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p34401551201812"><a name="p34401551201812"></a><a name="p34401551201812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p198921122117"><a name="p198921122117"></a><a name="p198921122117"></a>Specifies the ID of the project where the health check is performed.</p>
</td>
</tr>
<tr id="row20626101212267"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p136267128260"><a name="p136267128260"></a><a name="p136267128260"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p26262127261"><a name="p26262127261"></a><a name="p26262127261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p10626612112610"><a name="p10626612112610"></a><a name="p10626612112610"></a>Specifies the health check name.</p>
<p id="p4781165175717"><a name="p4781165175717"></a><a name="p4781165175717"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row3626131262613"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p862641211265"><a name="p862641211265"></a><a name="p862641211265"></a>delay</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p162641210268"><a name="p162641210268"></a><a name="p162641210268"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p16626161282618"><a name="p16626161282618"></a><a name="p16626161282618"></a>Specifies the interval between health checks in the unit of second. The value ranges from <strong id="b161271213417"><a name="b161271213417"></a><a name="b161271213417"></a>1</strong> to <strong id="b1812820194117"><a name="b1812820194117"></a><a name="b1812820194117"></a>50</strong>.</p>
</td>
</tr>
<tr id="row162621232617"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p162616124260"><a name="p162616124260"></a><a name="p162616124260"></a>max_retries</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p662617122262"><a name="p662617122262"></a><a name="p662617122262"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p158471132332"><a name="p158471132332"></a><a name="p158471132332"></a>Specifies the number of consecutive health checks when the health check result of a backend server changes from <strong id="b1082873392718"><a name="b1082873392718"></a><a name="b1082873392718"></a>fail</strong> to <strong id="b8829113372716"><a name="b8829113372716"></a><a name="b8829113372716"></a>success</strong>.</p>
<p id="p4626312172618"><a name="p4626312172618"></a><a name="p4626312172618"></a>The value ranges from <strong id="b189231058315"><a name="b189231058315"></a><a name="b189231058315"></a>1</strong> to <strong id="b14924145811115"><a name="b14924145811115"></a><a name="b14924145811115"></a>10</strong>.</p>
</td>
</tr>
<tr id="row14626151212614"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p7626412102613"><a name="p7626412102613"></a><a name="p7626412102613"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p46264126265"><a name="p46264126265"></a><a name="p46264126265"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p893015710294"><a name="p893015710294"></a><a name="p893015710294"></a>Lists the IDs of backend server groups associated with the health check.</p>
</td>
</tr>
<tr id="row1262611122264"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p15626212202614"><a name="p15626212202614"></a><a name="p15626212202614"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p862611214269"><a name="p862611214269"></a><a name="p862611214269"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p1395749185817"><a name="p1395749185817"></a><a name="p1395749185817"></a>Specifies the administrative status of the health check.</p>
<p id="p1695104925812"><a name="p1695104925812"></a><a name="p1695104925812"></a>The value can be <strong id="b256912714412"><a name="b256912714412"></a><a name="b256912714412"></a>true</strong> or <strong id="b4570879418"><a name="b4570879418"></a><a name="b4570879418"></a>false</strong>. The default value is <strong id="b87214915417"><a name="b87214915417"></a><a name="b87214915417"></a>true</strong>.</p>
<a name="ul1195349165813"></a><a name="ul1195349165813"></a><ul id="ul1195349165813"><li><strong id="b1832310104417"><a name="b1832310104417"></a><a name="b1832310104417"></a>true</strong>: indicates that the health check function is enabled.</li><li><strong id="b4349161618418"><a name="b4349161618418"></a><a name="b4349161618418"></a>false</strong>: indicates that the health check function is disabled.</li></ul>
</td>
</tr>
<tr id="row10626201220263"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1627712112615"><a name="p1627712112615"></a><a name="p1627712112615"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1462719125261"><a name="p1462719125261"></a><a name="p1462719125261"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p39594917584"><a name="p39594917584"></a><a name="p39594917584"></a>Specifies the health check timeout duration in the unit of second. The value ranges from <strong id="b199591417144115"><a name="b199591417144115"></a><a name="b199591417144115"></a>1</strong> to <strong id="b196071744118"><a name="b196071744118"></a><a name="b196071744118"></a>50</strong>.</p>
<div class="note" id="note995104918586"><a name="note995104918586"></a><a name="note995104918586"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p195104920588"><a name="p195104920588"></a><a name="p195104920588"></a>You are advised to set the value less than that of parameter <strong id="b9590151916412"><a name="b9590151916412"></a><a name="b9590151916412"></a>delay</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row16627312172620"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p86271012162613"><a name="p86271012162613"></a><a name="p86271012162613"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p26271212122619"><a name="p26271212122619"></a><a name="p26271212122619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p1095154995817"><a name="p1095154995817"></a><a name="p1095154995817"></a>Specifies the health check protocol.</p>
<p id="p139654917587"><a name="p139654917587"></a><a name="p139654917587"></a>The value can be <strong id="b4231523104120"><a name="b4231523104120"></a><a name="b4231523104120"></a>TCP</strong>, <strong id="b152592364118"><a name="b152592364118"></a><a name="b152592364118"></a>UDP_CONNECT</strong>, or <strong id="b7263233410"><a name="b7263233410"></a><a name="b7263233410"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row462771217266"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p17627131211261"><a name="p17627131211261"></a><a name="p17627131211261"></a>monitor_port</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1862741242610"><a name="p1862741242610"></a><a name="p1862741242610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p119674915580"><a name="p119674915580"></a><a name="p119674915580"></a>Specifies the health check port. The port number ranges from 1 to 65535.</p>
<p id="p796124913588"><a name="p796124913588"></a><a name="p796124913588"></a>The value is left blank by default, indicating that the port of the backend server is used as the health check port.</p>
</td>
</tr>
<tr id="row362791219268"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p6627121282613"><a name="p6627121282613"></a><a name="p6627121282613"></a>expected_codes</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p662714129261"><a name="p662714129261"></a><a name="p662714129261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p55431899"><a name="p55431899"></a><a name="p55431899"></a>Specifies the expected HTTP status code. The following options are available:</p>
<p id="p29125048"><a name="p29125048"></a><a name="p29125048"></a>A single value, such as 200</p>
<p id="p60798848"><a name="p60798848"></a><a name="p60798848"></a>A list of values, such as 200 and 202</p>
<p id="p10318722"><a name="p10318722"></a><a name="p10318722"></a>A value range, such as 200 to 204</p>
<p id="p25759641"><a name="p25759641"></a><a name="p25759641"></a>This parameter is valid when the value of <strong id="b385414488457"><a name="b385414488457"></a><a name="b385414488457"></a>type</strong> is set to <strong id="b1285514814513"><a name="b1285514814513"></a><a name="b1285514814513"></a>HTTP</strong>.</p>
<p id="p19695101010580"><a name="p19695101010580"></a><a name="p19695101010580"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row1962761272613"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p16627161292612"><a name="p16627161292612"></a><a name="p16627161292612"></a>domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p8627151219265"><a name="p8627151219265"></a><a name="p8627151219265"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p19451641195915"><a name="p19451641195915"></a><a name="p19451641195915"></a>Specifies the domain name of the HTTP request during the health check.</p>
<p id="p945841135916"><a name="p945841135916"></a><a name="p945841135916"></a>This parameter is valid when the value of <strong id="b2064992219463"><a name="b2064992219463"></a><a name="b2064992219463"></a>type</strong> is set to <strong id="b865002294612"><a name="b865002294612"></a><a name="b865002294612"></a>HTTP</strong>.</p>
<p id="p1045104175910"><a name="p1045104175910"></a><a name="p1045104175910"></a>The parameter value is left blank by default, indicating that the private IP address of the load balancer is used as the destination address of HTTP requests.</p>
<p id="p845134113593"><a name="p845134113593"></a><a name="p845134113593"></a>The parameter value can contain only digits, letters, hyphens (-), and periods (.) and must start with a digit or letter, for example, <strong id="b113015586429"><a name="b113015586429"></a><a name="b113015586429"></a>www.test.com</strong>.</p>
<p id="p201302012585"><a name="p201302012585"></a><a name="p201302012585"></a>The value contains a maximum of 100 characters.</p>
</td>
</tr>
<tr id="row196271312192614"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p7627181292610"><a name="p7627181292610"></a><a name="p7627181292610"></a>url_path</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p10627141214267"><a name="p10627141214267"></a><a name="p10627141214267"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p1745114145914"><a name="p1745114145914"></a><a name="p1745114145914"></a>Specifies the HTTP request path for the health check. The default value is <strong id="b15642184416411"><a name="b15642184416411"></a><a name="b15642184416411"></a>/</strong>, and the value must start with a slash (/).</p>
<p id="p5451741195912"><a name="p5451741195912"></a><a name="p5451741195912"></a>This parameter is valid when the value of <strong id="b10870113994713"><a name="b10870113994713"></a><a name="b10870113994713"></a>type</strong> is set to <strong id="b168709399478"><a name="b168709399478"></a><a name="b168709399478"></a>HTTP</strong>.</p>
<p id="p16451641185910"><a name="p16451641185910"></a><a name="p16451641185910"></a>An example value is <strong id="b857214719411"><a name="b857214719411"></a><a name="b857214719411"></a>/test</strong>.</p>
<p id="p1656842965819"><a name="p1656842965819"></a><a name="p1656842965819"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row5627612182610"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p156271512122620"><a name="p156271512122620"></a><a name="p156271512122620"></a>http_method</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p8627212142610"><a name="p8627212142610"></a><a name="p8627212142610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p1147104111593"><a name="p1147104111593"></a><a name="p1147104111593"></a>Specifies the HTTP request method. The default value is <strong id="b7695248174112"><a name="b7695248174112"></a><a name="b7695248174112"></a>GET</strong>.</p>
<p id="p84774115591"><a name="p84774115591"></a><a name="p84774115591"></a>The value can be <strong id="b18677114915415"><a name="b18677114915415"></a><a name="b18677114915415"></a>GET</strong>, <strong id="b1967854911416"><a name="b1967854911416"></a><a name="b1967854911416"></a>HEAD</strong>, <strong id="b1678149134116"><a name="b1678149134116"></a><a name="b1678149134116"></a>POST</strong>, <strong id="b0679144916412"><a name="b0679144916412"></a><a name="b0679144916412"></a>PUT</strong>, <strong id="b13679849204115"><a name="b13679849204115"></a><a name="b13679849204115"></a>DELETE</strong>, <strong id="b13680124914112"><a name="b13680124914112"></a><a name="b13680124914112"></a>TRACE</strong>, <strong id="b668116498413"><a name="b668116498413"></a><a name="b668116498413"></a>OPTIONS</strong>, <strong id="b4682104916419"><a name="b4682104916419"></a><a name="b4682104916419"></a>CONNECT</strong>, and <strong id="b368213491413"><a name="b368213491413"></a><a name="b368213491413"></a>PATCH</strong>.</p>
<p id="p1747144116591"><a name="p1747144116591"></a><a name="p1747144116591"></a>This parameter is valid when the value of <strong id="b77175161489"><a name="b77175161489"></a><a name="b77175161489"></a>type</strong> is set to <strong id="b20718111644817"><a name="b20718111644817"></a><a name="b20718111644817"></a>HTTP</strong>.</p>
<p id="p10402193217586"><a name="p10402193217586"></a><a name="p10402193217586"></a>The value contains a maximum of 16 characters.</p>
<div class="note" id="note1447741175914"><a name="note1447741175914"></a><a name="note1447741175914"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5471741175911"><a name="p5471741175911"></a><a name="p5471741175911"></a>This parameter is reserved.</p>
</div></div>
</td>
</tr>
<tr id="row15181172904011"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p735612418409"><a name="p735612418409"></a><a name="p735612418409"></a>healthmonitors_links</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p93571141164018"><a name="p93571141164018"></a><a name="p93571141164018"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p5542991616"><a name="p5542991616"></a><a name="p5542991616"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p165764116119"><a name="p165764116119"></a><a name="p165764116119"></a>This parameter exists only in the response body of pagination query.</p>
<p id="p53635145114"><a name="p53635145114"></a><a name="p53635145114"></a>For details, see <a href="#table31726924112">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **healthmonitors\_links**  parameter description

<a name="table31726924112"></a>
<table><thead align="left"><tr id="en-us_topic_0141008270_en-us_topic_0096561531_row12653175213336"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0141008270_en-us_topic_0096561531_p15653195215335"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p15653195215335"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p15653195215335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0141008270_en-us_topic_0096561531_p065315253310"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p065315253310"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p065315253310"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="en-us_topic_0141008270_en-us_topic_0096561531_p765365253319"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p765365253319"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p765365253319"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0141008270_en-us_topic_0096561531_row206531152103314"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008270_en-us_topic_0096561531_p1465311528337"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1465311528337"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1465311528337"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008270_en-us_topic_0096561531_p12653952113318"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p12653952113318"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p12653952113318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008270_en-us_topic_0096561531_p1653852193312"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1653852193312"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1653852193312"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="en-us_topic_0141008270_en-us_topic_0096561531_row186535529338"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008270_en-us_topic_0096561531_p1065325215337"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1065325215337"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p1065325215337"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008270_en-us_topic_0096561531_p165305243318"><a name="en-us_topic_0141008270_en-us_topic_0096561531_p165305243318"></a><a name="en-us_topic_0141008270_en-us_topic_0096561531_p165305243318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008270_p1772113411218"><a name="en-us_topic_0141008270_p1772113411218"></a><a name="en-us_topic_0141008270_p1772113411218"></a>Specifies the prompt of the previous or next page.</p>
<p id="en-us_topic_0141008270_p422510443113"><a name="en-us_topic_0141008270_p422510443113"></a><a name="en-us_topic_0141008270_p422510443113"></a>The value can be <strong id="b1018001315421"><a name="b1018001315421"></a><a name="b1018001315421"></a>next</strong> or <strong id="b218116132423"><a name="b218116132423"></a><a name="b218116132423"></a>previous</strong>. The value <strong id="b1059011158426"><a name="b1059011158426"></a><a name="b1059011158426"></a>next</strong> indicates the href containing the URL of the next page, and <strong id="b359111554215"><a name="b359111554215"></a><a name="b359111554215"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section57677308457"></a>

-   Example request 1: Querying all health checks

    ```
    GET https://{Endpoint}/v2.0/lbaas/healthmonitors
    ```

-   Example response 1

    ```
    {
        "healthmonitors": [
            {
                "monitor_port": null,
                "name": "",
                "admin_state_up": true,
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
     
                "domain_name": null,
                "delay": 5,
                
                "max_retries": 3,
               
                "http_method": "GET",
                "timeout": 10,
                "pools": [
                    {
                        "id": "caef8316-6b65-4676-8293-cf41fb63cc2a"
                    }
                ],
                "url_path": "/",
                "type": "HTTP",
                "id": "1b587819-d619-49c1-9101-fe72d8b361ef"
            }
        ]
    }
    ```

-   Example request 2: Filtering HTTP health checks

    ```
    GET https://{Endpoint}/v2.0/lbaas/healthmonitors?type=HTTP
    ```

-   Example response 2

    ```
    {
        "healthmonitors": [
            {
                "monitor_port": null,
                "name": "",
                "admin_state_up": true,
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
                "domain_name": null,
                "delay": 5,
                "expected_codes": "200-204,300-302,401",
                "max_retries": 3,
                
                "http_method": "GET",
                "timeout": 10,
                "pools": [
                    {
                        "id": "caef8316-6b65-4676-8293-cf41fb63cc2a"
                    }
                ],
                "url_path": "/",
                "type": "HTTP",
                "id": "1b587819-d619-49c1-9101-fe72d8b361ef"
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0049139655_section64643717"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

