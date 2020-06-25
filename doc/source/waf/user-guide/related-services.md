# Related Services<a name="waf_01_0051"></a>

This section describes the relationship between WAF and other cloud services.

## CTS<a name="section19288959348"></a>

Cloud Trace Service \(CTS\) provides records of operations on WAF. With CTS, you can query, audit, and backtrack these operations. For details, see the  _Cloud Trace Service User Guide_.

**Table  1**  WAF operations that can be recorded by CTS

<a name="table1552126164019"></a>
<table><thead align="left"><tr id="row117406265409"><th class="cellrowborder" valign="top" width="42.95429542954295%" id="mcps1.2.4.1.1"><p id="p187409267407"><a name="p187409267407"></a><a name="p187409267407"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="27.062706270627064%" id="mcps1.2.4.1.2"><p id="p12740192644011"><a name="p12740192644011"></a><a name="p12740192644011"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="29.982998299829983%" id="mcps1.2.4.1.3"><p id="p974092616405"><a name="p974092616405"></a><a name="p974092616405"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row1874015262402"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p3740182617402"><a name="p3740182617402"></a><a name="p3740182617402"></a>Creating a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1874062617408"><a name="p1874062617408"></a><a name="p1874062617408"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p1374010260403"><a name="p1374010260403"></a><a name="p1374010260403"></a>createInstance</p>
</td>
</tr>
<tr id="row37401269409"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p11741526164020"><a name="p11741526164020"></a><a name="p11741526164020"></a>Deleting a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p6741122654010"><a name="p6741122654010"></a><a name="p6741122654010"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p174142664010"><a name="p174142664010"></a><a name="p174142664010"></a>deleteInstance</p>
</td>
</tr>
<tr id="row27417266401"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p13741112619409"><a name="p13741112619409"></a><a name="p13741112619409"></a>Modifying a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p2741102614011"><a name="p2741102614011"></a><a name="p2741102614011"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p0741726144019"><a name="p0741726144019"></a><a name="p0741726144019"></a>modifyInstance</p>
</td>
</tr>
<tr id="row9741102613406"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p147410262409"><a name="p147410262409"></a><a name="p147410262409"></a>Modifying the protection status of a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p6741132694011"><a name="p6741132694011"></a><a name="p6741132694011"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p8741182617407"><a name="p8741182617407"></a><a name="p8741182617407"></a>modifyProtectStatus</p>
</td>
</tr>
<tr id="row10741526194013"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1574132694014"><a name="p1574132694014"></a><a name="p1574132694014"></a>Modifying the connection status of a WAF instance</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p5741122614409"><a name="p5741122614409"></a><a name="p5741122614409"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p12741132654010"><a name="p12741132654010"></a><a name="p12741132654010"></a>modifyAccessStatus</p>
</td>
</tr>
<tr id="row87411826184011"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1874122612404"><a name="p1874122612404"></a><a name="p1874122612404"></a>Creating a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p127411326184014"><a name="p127411326184014"></a><a name="p127411326184014"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p1474118265407"><a name="p1474118265407"></a><a name="p1474118265407"></a>createPolicy</p>
</td>
</tr>
<tr id="row1174119269405"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1674112617408"><a name="p1674112617408"></a><a name="p1674112617408"></a>Applying a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p14741426154019"><a name="p14741426154019"></a><a name="p14741426154019"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p17741726194011"><a name="p17741726194011"></a><a name="p17741726194011"></a>applyToPolicy</p>
</td>
</tr>
<tr id="row15741726184011"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p774152617405"><a name="p774152617405"></a><a name="p774152617405"></a>Modifying a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1274114266408"><a name="p1274114266408"></a><a name="p1274114266408"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p17741132674015"><a name="p17741132674015"></a><a name="p17741132674015"></a>modifyPolicy</p>
</td>
</tr>
<tr id="row12741122616405"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p137421126174018"><a name="p137421126174018"></a><a name="p137421126174018"></a>Deleting a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p10742926154012"><a name="p10742926154012"></a><a name="p10742926154012"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p12742526194015"><a name="p12742526194015"></a><a name="p12742526194015"></a>deletePolicy</p>
</td>
</tr>
<tr id="row1974210266402"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p117421626184019"><a name="p117421626184019"></a><a name="p117421626184019"></a>Modifying alarm notification settings</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p2742202604020"><a name="p2742202604020"></a><a name="p2742202604020"></a>alertNoticeConfig</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p874222664018"><a name="p874222664018"></a><a name="p874222664018"></a>modifyAlertNoticeConfig</p>
</td>
</tr>
<tr id="row474212269407"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p16742152614012"><a name="p16742152614012"></a><a name="p16742152614012"></a>Uploading a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1874242612400"><a name="p1874242612400"></a><a name="p1874242612400"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p97421826144016"><a name="p97421826144016"></a><a name="p97421826144016"></a>createCertificate</p>
</td>
</tr>
<tr id="row185431219164114"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p12543141954110"><a name="p12543141954110"></a><a name="p12543141954110"></a>Changing the name of a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p105431519134114"><a name="p105431519134114"></a><a name="p105431519134114"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p1054381984111"><a name="p1054381984111"></a><a name="p1054381984111"></a>modifyCertificate</p>
</td>
</tr>
<tr id="row0742172610408"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p11742132615403"><a name="p11742132615403"></a><a name="p11742132615403"></a>Deleting a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1574232694011"><a name="p1574232694011"></a><a name="p1574232694011"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p1174212613408"><a name="p1174212613408"></a><a name="p1174212613408"></a>deleteCertificate</p>
</td>
</tr>
<tr id="row1874292613408"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p157421826104012"><a name="p157421826104012"></a><a name="p157421826104012"></a>Adding a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p07423264407"><a name="p07423264407"></a><a name="p07423264407"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p4742926174013"><a name="p4742926174013"></a><a name="p4742926174013"></a>createCc</p>
</td>
</tr>
<tr id="row974272617409"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1674212610407"><a name="p1674212610407"></a><a name="p1674212610407"></a>Modifying a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p3742026204014"><a name="p3742026204014"></a><a name="p3742026204014"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p1674272613405"><a name="p1674272613405"></a><a name="p1674272613405"></a>modifyCc</p>
</td>
</tr>
<tr id="row17742132615403"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p207421826194020"><a name="p207421826194020"></a><a name="p207421826194020"></a>Deleting a CC attack protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1374222674016"><a name="p1374222674016"></a><a name="p1374222674016"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p074362611401"><a name="p074362611401"></a><a name="p074362611401"></a>deleteCc</p>
</td>
</tr>
<tr id="row4743162610403"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p874312614406"><a name="p874312614406"></a><a name="p874312614406"></a>Adding a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p15743726184013"><a name="p15743726184013"></a><a name="p15743726184013"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p107431262407"><a name="p107431262407"></a><a name="p107431262407"></a>createCustom</p>
</td>
</tr>
<tr id="row20743726124019"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p11743102674013"><a name="p11743102674013"></a><a name="p11743102674013"></a>Modifying a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p4743182654010"><a name="p4743182654010"></a><a name="p4743182654010"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p57433267403"><a name="p57433267403"></a><a name="p57433267403"></a>modifyCustom</p>
</td>
</tr>
<tr id="row1274352611403"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p474342616406"><a name="p474342616406"></a><a name="p474342616406"></a>Deleting a precise protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p174372664013"><a name="p174372664013"></a><a name="p174372664013"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p5743102618404"><a name="p5743102618404"></a><a name="p5743102618404"></a>deleteCustom</p>
</td>
</tr>
<tr id="row19743926114013"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p16743192604017"><a name="p16743192604017"></a><a name="p16743192604017"></a>Adding a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p17743126194013"><a name="p17743126194013"></a><a name="p17743126194013"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p117431226134018"><a name="p117431226134018"></a><a name="p117431226134018"></a>createWhiteblackip</p>
</td>
</tr>
<tr id="row11743326104017"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p19743172618407"><a name="p19743172618407"></a><a name="p19743172618407"></a>Modifying a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1574382674019"><a name="p1574382674019"></a><a name="p1574382674019"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p874392694020"><a name="p874392694020"></a><a name="p874392694020"></a>modifyWhiteblackip</p>
</td>
</tr>
<tr id="row1774318262403"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1674372664017"><a name="p1674372664017"></a><a name="p1674372664017"></a>Deleting a blacklist or whitelist rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p15743202664017"><a name="p15743202664017"></a><a name="p15743202664017"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p10743426114010"><a name="p10743426114010"></a><a name="p10743426114010"></a>deleteWhiteblackip</p>
</td>
</tr>
<tr id="row1774332617403"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1874392684019"><a name="p1874392684019"></a><a name="p1874392684019"></a>Adding a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p87437261407"><a name="p87437261407"></a><a name="p87437261407"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p474414267402"><a name="p474414267402"></a><a name="p474414267402"></a>createAntitamper</p>
</td>
</tr>
<tr id="row187446269406"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p157441326124012"><a name="p157441326124012"></a><a name="p157441326124012"></a>Updating a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p7744102664013"><a name="p7744102664013"></a><a name="p7744102664013"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p15744142664011"><a name="p15744142664011"></a><a name="p15744142664011"></a>refreshAntitamper</p>
</td>
</tr>
<tr id="row1774402684016"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1974472674011"><a name="p1974472674011"></a><a name="p1974472674011"></a>Deleting a web tamper protection rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p1474422619404"><a name="p1474422619404"></a><a name="p1474422619404"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p474410263403"><a name="p474410263403"></a><a name="p474410263403"></a>deleteAntitamper</p>
</td>
</tr>
<tr id="row2744152612404"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p574442604010"><a name="p574442604010"></a><a name="p574442604010"></a>Adding a false alarm masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p47443260406"><a name="p47443260406"></a><a name="p47443260406"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p157440261404"><a name="p157440261404"></a><a name="p157440261404"></a>createIgnore</p>
</td>
</tr>
<tr id="row1874412684012"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1374417267408"><a name="p1374417267408"></a><a name="p1374417267408"></a>Deleting a false alarm masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p174472614405"><a name="p174472614405"></a><a name="p174472614405"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p18744726124019"><a name="p18744726124019"></a><a name="p18744726124019"></a>deleteIgnore</p>
</td>
</tr>
<tr id="row167441926194018"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p67442026174017"><a name="p67442026174017"></a><a name="p67442026174017"></a>Adding a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p2074462616407"><a name="p2074462616407"></a><a name="p2074462616407"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p5744826124014"><a name="p5744826124014"></a><a name="p5744826124014"></a>createPrivacy</p>
</td>
</tr>
<tr id="row074492617404"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p207441426164019"><a name="p207441426164019"></a><a name="p207441426164019"></a>Modifying a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p117441126104010"><a name="p117441126104010"></a><a name="p117441126104010"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p15744142634015"><a name="p15744142634015"></a><a name="p15744142634015"></a>modifyPrivacy</p>
</td>
</tr>
<tr id="row1974413267409"><td class="cellrowborder" valign="top" width="42.95429542954295%" headers="mcps1.2.4.1.1 "><p id="p1074452654011"><a name="p1074452654011"></a><a name="p1074452654011"></a>Deleting a data masking rule</p>
</td>
<td class="cellrowborder" valign="top" width="27.062706270627064%" headers="mcps1.2.4.1.2 "><p id="p3744726104010"><a name="p3744726104010"></a><a name="p3744726104010"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.982998299829983%" headers="mcps1.2.4.1.3 "><p id="p16744122614010"><a name="p16744122614010"></a><a name="p16744122614010"></a>deletePrivacy</p>
</td>
</tr>
</tbody>
</table>

## Cloud Eye<a name="section2948676693751"></a>

Cloud Eye monitors the metrics of WAF, so that you can understand the protection status of WAF in a timely manner, and set protection policies accordingly. For details, see the  _Cloud Eye User Guide_.

**Table  2**  WAF metrics supported by Cloud Eye

<a name="table5331155094045"></a>
<table><thead align="left"><tr id="r6d6536c2fee4445b882b399175533125"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="a017c9e13e1a147b8a9a338f5b361d780"><a name="a017c9e13e1a147b8a9a338f5b361d780"></a><a name="a017c9e13e1a147b8a9a338f5b361d780"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="aa6e36222233e4ceca1f310b2d5d69052"><a name="aa6e36222233e4ceca1f310b2d5d69052"></a><a name="aa6e36222233e4ceca1f310b2d5d69052"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="a23532e771f30464eabd4f59c5d499a69"><a name="a23532e771f30464eabd4f59c5d499a69"></a><a name="a23532e771f30464eabd4f59c5d499a69"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="ab18fef49a82249fb986811640525e62c"><a name="ab18fef49a82249fb986811640525e62c"></a><a name="ab18fef49a82249fb986811640525e62c"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row11751310105853"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p42188327105920"><a name="p42188327105920"></a><a name="p42188327105920"></a>attacks</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p66979856105927"><a name="p66979856105927"></a><a name="p66979856105927"></a>Total number of attacks on a domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p44238505105853"><a name="p44238505105853"></a><a name="p44238505105853"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p26549182105853"><a name="p26549182105853"></a><a name="p26549182105853"></a>Domain</p>
</td>
</tr>
<tr id="rbeb3eabf461745118034bbe719999f2e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0015479905_p156401051664"><a name="en-us_topic_0015479905_p156401051664"></a><a name="en-us_topic_0015479905_p156401051664"></a>requests</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0015479905_p588890221664"><a name="en-us_topic_0015479905_p588890221664"></a><a name="en-us_topic_0015479905_p588890221664"></a>Total number of requests for a domain name in a given period</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0015479905_p52815001664"><a name="en-us_topic_0015479905_p52815001664"></a><a name="en-us_topic_0015479905_p52815001664"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0015479905_p251483301664"><a name="en-us_topic_0015479905_p251483301664"></a><a name="en-us_topic_0015479905_p251483301664"></a>Domain</p>
</td>
</tr>
</tbody>
</table>

## TMS<a name="section72601459152417"></a>

Tag Management Service \(TMS\) is a visualized service for fast and unified tag management that enables you to label and manage WAF instances by tags.

**Table  3**  WAF operations supported by TMS

<a name="table126592286267"></a>
<table><thead align="left"><tr id="row566116283269"><th class="cellrowborder" valign="top" width="26.292629262926294%" id="mcps1.2.4.1.1"><p id="p166611289266"><a name="p166611289266"></a><a name="p166611289266"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="31.973197319731973%" id="mcps1.2.4.1.2"><p id="p966162817264"><a name="p966162817264"></a><a name="p966162817264"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.73417341734174%" id="mcps1.2.4.1.3"><p id="p36616282267"><a name="p36616282267"></a><a name="p36616282267"></a>Event Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row06611828162610"><td class="cellrowborder" valign="top" width="26.292629262926294%" headers="mcps1.2.4.1.1 "><p id="p1966152818262"><a name="p1966152818262"></a><a name="p1966152818262"></a>Creating a WAF instance tag</p>
</td>
<td class="cellrowborder" valign="top" width="31.973197319731973%" headers="mcps1.2.4.1.2 "><p id="p1566119285266"><a name="p1566119285266"></a><a name="p1566119285266"></a>Tag</p>
</td>
<td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.2.4.1.3 "><p id="p1480410418495"><a name="p1480410418495"></a><a name="p1480410418495"></a>createResourceTag</p>
</td>
</tr>
<tr id="row6661128202611"><td class="cellrowborder" valign="top" width="26.292629262926294%" headers="mcps1.2.4.1.1 "><p id="p766116289264"><a name="p766116289264"></a><a name="p766116289264"></a>Deleting a WAF instance tag</p>
</td>
<td class="cellrowborder" valign="top" width="31.973197319731973%" headers="mcps1.2.4.1.2 "><p id="p96611328142610"><a name="p96611328142610"></a><a name="p96611328142610"></a>Tag</p>
</td>
<td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.2.4.1.3 "><p id="p1566122832619"><a name="p1566122832619"></a><a name="p1566122832619"></a>deleteResourceTag</p>
</td>
</tr>
</tbody>
</table>

## IAM<a name="section4573770192847"></a>

Identity and Access Management \(IAM\) provides the permission management function for WAF. Only users granted with the WAF Administrator permissions can use WAF. To obtain the permissions, contact users who have the Security Administrator permissions. For details, see the  _Identity and Access Management User Guide_.

## SMN<a name="section13683170172541"></a>

The Simple Message Notification \(SMN\) service provides the notification function. After the notification function is enabled in WAF, users will receive an SMS message or email when an attack on a protected domain is detected.

For details about SMN, see the  _Simple Message Notification User Guide_.

