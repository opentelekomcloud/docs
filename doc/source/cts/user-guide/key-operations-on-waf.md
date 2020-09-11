# Key Operations on WAF<a name="en-us_topic_0100291690"></a>

Web Application Firewall \(WAF\) is designed to keep web services stable and secure in combination with our many years of experience in security protection. It examines all HTTP and HTTPS requests to detect and block attacks such as Structure Query Language \(SQL\) injections, cross-site scripting \(XSS\), webshell upload, third-party vulnerability exploits, CC attacks, and malicious crawlers.

With CTS, you can record operations associated with WAF for future query, audit, and backtrack operations.

**Table  1**  WAF operations that can be recorded by CTS

<a name="table37669775174753"></a>
<table><thead align="left"><tr id="rec49ef385c1843e29db60a6a8ac2756c"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="a39aac89484e74b849b5751654f4c5e9e"><a name="a39aac89484e74b849b5751654f4c5e9e"></a><a name="a39aac89484e74b849b5751654f4c5e9e"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a4d36e4d02e2247d28422b8eb7ccfd118"><a name="a4d36e4d02e2247d28422b8eb7ccfd118"></a><a name="a4d36e4d02e2247d28422b8eb7ccfd118"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="a8812c3fc306c4922bc6b75e8eb1fe76d"><a name="a8812c3fc306c4922bc6b75e8eb1fe76d"></a><a name="a8812c3fc306c4922bc6b75e8eb1fe76d"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rf75cb220844e4402aab19fb1d1cd3d77"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p080113117207"><a name="p080113117207"></a><a name="p080113117207"></a>Creating a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7284244162015"><a name="p7284244162015"></a><a name="p7284244162015"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p119115119211"><a name="p119115119211"></a><a name="p119115119211"></a>createInstance</p>
</td>
</tr>
<tr id="r0745488409014bbca811a78647b5ea8c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p148053120201"><a name="p148053120201"></a><a name="p148053120201"></a>Deleting a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5284194419207"><a name="p5284194419207"></a><a name="p5284194419207"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13191161112115"><a name="p13191161112115"></a><a name="p13191161112115"></a>deleteInstance</p>
</td>
</tr>
<tr id="reaecb34180894dfb874e51f9d6c0c155"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1180193112012"><a name="p1180193112012"></a><a name="p1180193112012"></a>Modifying a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p162841644112018"><a name="p162841644112018"></a><a name="p162841644112018"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13191512218"><a name="p13191512218"></a><a name="p13191512218"></a>modifyInstance</p>
</td>
</tr>
<tr id="row1811811241416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1080143162014"><a name="p1080143162014"></a><a name="p1080143162014"></a>Modifying the protection status of a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p0284114462014"><a name="p0284114462014"></a><a name="p0284114462014"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1519111112214"><a name="p1519111112214"></a><a name="p1519111112214"></a>modifyProtectStatus</p>
</td>
</tr>
<tr id="row4945131281416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p0804318205"><a name="p0804318205"></a><a name="p0804318205"></a>Modifying the connection status of a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1628434482011"><a name="p1628434482011"></a><a name="p1628434482011"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p91914117217"><a name="p91914117217"></a><a name="p91914117217"></a>modifyAccessStatus</p>
</td>
</tr>
<tr id="row1087920104143"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p68011315204"><a name="p68011315204"></a><a name="p68011315204"></a>Creating a policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3284104462015"><a name="p3284104462015"></a><a name="p3284104462015"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51913132114"><a name="p51913132114"></a><a name="p51913132114"></a>createPolicy</p>
</td>
</tr>
<tr id="row124122851411"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16801631132016"><a name="p16801631132016"></a><a name="p16801631132016"></a>Deleting a policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20284154492014"><a name="p20284154492014"></a><a name="p20284154492014"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p101912011217"><a name="p101912011217"></a><a name="p101912011217"></a>deletePolicy</p>
</td>
</tr>
<tr id="row1135515651419"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p180133122012"><a name="p180133122012"></a><a name="p180133122012"></a>Modifying a policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1828415445201"><a name="p1828415445201"></a><a name="p1828415445201"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1319110120212"><a name="p1319110120212"></a><a name="p1319110120212"></a>modifyPolicy</p>
</td>
</tr>
<tr id="row113468441410"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48011318204"><a name="p48011318204"></a><a name="p48011318204"></a>Applying a policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18284124413207"><a name="p18284124413207"></a><a name="p18284124413207"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p719114122120"><a name="p719114122120"></a><a name="p719114122120"></a>applayToPolicy</p>
</td>
</tr>
<tr id="row8476923161818"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12802031152015"><a name="p12802031152015"></a><a name="p12802031152015"></a>Creating a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1628418448202"><a name="p1628418448202"></a><a name="p1628418448202"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p619131192115"><a name="p619131192115"></a><a name="p619131192115"></a>createCertificate</p>
</td>
</tr>
<tr id="row1547632341811"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p481203152018"><a name="p481203152018"></a><a name="p481203152018"></a>Deleting a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11284244132019"><a name="p11284244132019"></a><a name="p11284244132019"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61917132111"><a name="p61917132111"></a><a name="p61917132111"></a>deleteCertificate</p>
</td>
</tr>
<tr id="row11476182319183"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p128183113202"><a name="p128183113202"></a><a name="p128183113202"></a>Changing the name of a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p172841844202018"><a name="p172841844202018"></a><a name="p172841844202018"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p219119172110"><a name="p219119172110"></a><a name="p219119172110"></a>modifyCertificate</p>
</td>
</tr>
<tr id="row19476142371810"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p181231132017"><a name="p181231132017"></a><a name="p181231132017"></a>Modifying alarm notification settings</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p82861844172016"><a name="p82861844172016"></a><a name="p82861844172016"></a>alertNoticeConfig</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p101916117215"><a name="p101916117215"></a><a name="p101916117215"></a>modifyAlertNoticeConfig</p>
</td>
</tr>
<tr id="row204760235188"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1081133111206"><a name="p1081133111206"></a><a name="p1081133111206"></a>Creating a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p182862446208"><a name="p182862446208"></a><a name="p182862446208"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1919161142112"><a name="p1919161142112"></a><a name="p1919161142112"></a>createCc</p>
</td>
</tr>
<tr id="row144761323141820"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p178153110208"><a name="p178153110208"></a><a name="p178153110208"></a>Deleting a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4286174419209"><a name="p4286174419209"></a><a name="p4286174419209"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21911319219"><a name="p21911319219"></a><a name="p21911319219"></a>deleteCc</p>
</td>
</tr>
<tr id="row44131317201819"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p881183142012"><a name="p881183142012"></a><a name="p881183142012"></a>Modifying a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p112861944112012"><a name="p112861944112012"></a><a name="p112861944112012"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21914192119"><a name="p21914192119"></a><a name="p21914192119"></a>modifyCc</p>
</td>
</tr>
<tr id="row841310171180"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9816319201"><a name="p9816319201"></a><a name="p9816319201"></a>Creating a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16286204413207"><a name="p16286204413207"></a><a name="p16286204413207"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p519110115210"><a name="p519110115210"></a><a name="p519110115210"></a>createCustom</p>
</td>
</tr>
<tr id="row1999232872014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p178114313206"><a name="p178114313206"></a><a name="p178114313206"></a>Deleting a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p82860441207"><a name="p82860441207"></a><a name="p82860441207"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p719114192114"><a name="p719114192114"></a><a name="p719114192114"></a>deleteCustom</p>
</td>
</tr>
<tr id="row139921628152014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p881133110203"><a name="p881133110203"></a><a name="p881133110203"></a>Modifying a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4286114417204"><a name="p4286114417204"></a><a name="p4286114417204"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1719110113213"><a name="p1719110113213"></a><a name="p1719110113213"></a>modifyCustom</p>
</td>
</tr>
<tr id="row19992132812205"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p981531132015"><a name="p981531132015"></a><a name="p981531132015"></a>Adding a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2286184412017"><a name="p2286184412017"></a><a name="p2286184412017"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1819151182111"><a name="p1819151182111"></a><a name="p1819151182111"></a>createWhiteblackip</p>
</td>
</tr>
<tr id="row29921728102010"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1481731152018"><a name="p1481731152018"></a><a name="p1481731152018"></a>Deleting a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p228714416208"><a name="p228714416208"></a><a name="p228714416208"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9191131112119"><a name="p9191131112119"></a><a name="p9191131112119"></a>deleteWhiteblackip</p>
</td>
</tr>
<tr id="row1299232812207"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8816313203"><a name="p8816313203"></a><a name="p8816313203"></a>Modifying a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12287184432015"><a name="p12287184432015"></a><a name="p12287184432015"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p419110192117"><a name="p419110192117"></a><a name="p419110192117"></a>modifyWhiteblackip</p>
</td>
</tr>
<tr id="row899242813208"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1781531172019"><a name="p1781531172019"></a><a name="p1781531172019"></a>Adding a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p132879444201"><a name="p132879444201"></a><a name="p132879444201"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1819119117210"><a name="p1819119117210"></a><a name="p1819119117210"></a>createAntitamper</p>
</td>
</tr>
<tr id="row2041314178185"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9811231162015"><a name="p9811231162015"></a><a name="p9811231162015"></a>Deleting a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p22878448202"><a name="p22878448202"></a><a name="p22878448202"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1819117116212"><a name="p1819117116212"></a><a name="p1819117116212"></a>deleteAntitamper</p>
</td>
</tr>
<tr id="row141361791820"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p128143114203"><a name="p128143114203"></a><a name="p128143114203"></a>Updating a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4287114411207"><a name="p4287114411207"></a><a name="p4287114411207"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p131916118217"><a name="p131916118217"></a><a name="p131916118217"></a>refreshAntitamper</p>
</td>
</tr>
<tr id="row1841591714182"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p158163113203"><a name="p158163113203"></a><a name="p158163113203"></a>Adding a false alarm masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p228713445200"><a name="p228713445200"></a><a name="p228713445200"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2019114113215"><a name="p2019114113215"></a><a name="p2019114113215"></a>createIgnore</p>
</td>
</tr>
<tr id="row6415171719183"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13811631152011"><a name="p13811631152011"></a><a name="p13811631152011"></a>Deleting a false alarm masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6287544172020"><a name="p6287544172020"></a><a name="p6287544172020"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p191918111212"><a name="p191918111212"></a><a name="p191918111212"></a>deleteIgnore</p>
</td>
</tr>
<tr id="row172318610201"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2811131172016"><a name="p2811131172016"></a><a name="p2811131172016"></a>Creating a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p328704416206"><a name="p328704416206"></a><a name="p328704416206"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1819118132120"><a name="p1819118132120"></a><a name="p1819118132120"></a>createPrivacy</p>
</td>
</tr>
<tr id="row1972356102014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5811431192015"><a name="p5811431192015"></a><a name="p5811431192015"></a>Deleting a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p82871447201"><a name="p82871447201"></a><a name="p82871447201"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14191181122113"><a name="p14191181122113"></a><a name="p14191181122113"></a>deletePrivacy</p>
</td>
</tr>
<tr id="row072413616207"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p128173111202"><a name="p128173111202"></a><a name="p128173111202"></a>Modifying a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18287944182010"><a name="p18287944182010"></a><a name="p18287944182010"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p191916112215"><a name="p191916112215"></a><a name="p191916112215"></a>modifyPrivacy</p>
</td>
</tr>
</tbody>
</table>

