# Error Codes<a name="dis_02_0021"></a>

If API calling fails, a response with HTTP status code 4_xx_  or 5_xx_  is returned. The returned message body contains the specific error code and error information. The response also includes specific error code and error information in the message body, as described in the following table.

**Sample:**

\{

"errorCode": "DIS.4301",

"message": "Stream does not exist. \[test\]\[6332998f84ac4c13a83db055da33cb66\]"

\}

<a name="table46646118152749"></a>
<table><thead align="left"><tr id="row48262329152749"><th class="cellrowborder" valign="top" width="7.39073907390739%" id="mcps1.1.6.1.1"><p id="p0590171585114"><a name="p0590171585114"></a><a name="p0590171585114"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="10.441044104410443%" id="mcps1.1.6.1.2"><p id="p2067958017348"><a name="p2067958017348"></a><a name="p2067958017348"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="27.44274427442744%" id="mcps1.1.6.1.3"><p id="p6468436815284"><a name="p6468436815284"></a><a name="p6468436815284"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="15.35153515351535%" id="mcps1.1.6.1.4"><p id="p1472441719512"><a name="p1472441719512"></a><a name="p1472441719512"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="39.373937393739375%" id="mcps1.1.6.1.5"><p id="p926103675116"><a name="p926103675116"></a><a name="p926103675116"></a><strong id="b8415102812410"><a name="b8415102812410"></a><a name="b8415102812410"></a>Measure</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row42552576152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p75901115125112"><a name="p75901115125112"></a><a name="p75901115125112"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p6479600215284"><a name="p6479600215284"></a><a name="p6479600215284"></a>DIS.4100</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p9331326172910"><a name="p9331326172910"></a><a name="p9331326172910"></a>Authorization error.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p4724191718513"><a name="p4724191718513"></a><a name="p4724191718513"></a>The signature information generated using AK and SK is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p102623615113"><a name="p102623615113"></a><a name="p102623615113"></a>Ensure that the signature information in the request header is correct.</p>
</td>
</tr>
<tr id="row64121143152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p152501582223"><a name="p152501582223"></a><a name="p152501582223"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1219628515284"><a name="p1219628515284"></a><a name="p1219628515284"></a>DIS.4101</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p4837503915284"><a name="p4837503915284"></a><a name="p4837503915284"></a>Authorization header cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p672451710513"><a name="p672451710513"></a><a name="p672451710513"></a>The signature information generated using AK and SK is blank.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p826133615518"><a name="p826133615518"></a><a name="p826133615518"></a>Ensure that the signature information is generated.</p>
</td>
</tr>
<tr id="row7301302152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p994098142214"><a name="p994098142214"></a><a name="p994098142214"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p3325040115284"><a name="p3325040115284"></a><a name="p3325040115284"></a>DIS.4102</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p580110165719"><a name="p580110165719"></a><a name="p580110165719"></a>Incorrectly parsed authorization header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1672411712513"><a name="p1672411712513"></a><a name="p1672411712513"></a>The signature cannot be parsed.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1126173655115"><a name="p1126173655115"></a><a name="p1126173655115"></a>Ensure that the signature information in the request header is correct.</p>
</td>
</tr>
<tr id="row27279250152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1765269152210"><a name="p1765269152210"></a><a name="p1765269152210"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p6605986115284"><a name="p6605986115284"></a><a name="p6605986115284"></a>DIS.4103</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p4924851815284"><a name="p4924851815284"></a><a name="p4924851815284"></a>Empty X-Sdk-Date header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p67241117145117"><a name="p67241117145117"></a><a name="p67241117145117"></a>The <strong id="b27281146183017"><a name="b27281146183017"></a><a name="b27281146183017"></a>X-Sdk-Date</strong> field in the request header is blank.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p78761437124111"><a name="p78761437124111"></a><a name="p78761437124111"></a>Ensure that the <strong id="b1862855943017"><a name="b1862855943017"></a><a name="b1862855943017"></a>X-Sdk-Date</strong> field in the request header is not blank.</p>
</td>
</tr>
<tr id="row65531305152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p19590915155113"><a name="p19590915155113"></a><a name="p19590915155113"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p6603629215284"><a name="p6603629215284"></a><a name="p6603629215284"></a>DIS.4104</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p27509787165734"><a name="p27509787165734"></a><a name="p27509787165734"></a>Error parsing X-Sdk-Date header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p57246170515"><a name="p57246170515"></a><a name="p57246170515"></a>The <strong id="b158055714310"><a name="b158055714310"></a><a name="b158055714310"></a>X-Sdk-Date</strong> field in the request header cannot be parsed.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p175811513421"><a name="p175811513421"></a><a name="p175811513421"></a>Ensure that the <strong id="b2073751910312"><a name="b2073751910312"></a><a name="b2073751910312"></a>X-Sdk-Date</strong> field in the request header is correct.</p>
</td>
</tr>
<tr id="row60942814152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p35901215135115"><a name="p35901215135115"></a><a name="p35901215135115"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1652182915284"><a name="p1652182915284"></a><a name="p1652182915284"></a>DIS.4105</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p15883185593015"><a name="p15883185593015"></a><a name="p15883185593015"></a>Invalid X-Sdk-Date header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p7711857104718"><a name="p7711857104718"></a><a name="p7711857104718"></a>The <strong id="b13638425143115"><a name="b13638425143115"></a><a name="b13638425143115"></a>X-Sdk-Date</strong> field in the request header is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1230014375486"><a name="p1230014375486"></a><a name="p1230014375486"></a>Ensure that the <strong id="b29532293316"><a name="b29532293316"></a><a name="b29532293316"></a>X-Sdk-Date</strong> field in the request header is correct.</p>
</td>
</tr>
<tr id="row33648480152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p155901815145110"><a name="p155901815145110"></a><a name="p155901815145110"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p3596536415284"><a name="p3596536415284"></a><a name="p3596536415284"></a>DIS.4106</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p2751337315284"><a name="p2751337315284"></a><a name="p2751337315284"></a>Empty AcessKey header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p18301121114916"><a name="p18301121114916"></a><a name="p18301121114916"></a>The <strong id="b1645103618314"><a name="b1645103618314"></a><a name="b1645103618314"></a>Authorization</strong> field of the request header does not contain AK.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p152613365517"><a name="p152613365517"></a><a name="p152613365517"></a>Ensure that AK is contained in the <strong id="b6751546185214"><a name="b6751546185214"></a><a name="b6751546185214"></a>Authorization</strong> field.</p>
</td>
</tr>
<tr id="row16973026152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1059041511518"><a name="p1059041511518"></a><a name="p1059041511518"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p5880811815284"><a name="p5880811815284"></a><a name="p5880811815284"></a>DIS.4107</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p8836813103217"><a name="p8836813103217"></a><a name="p8836813103217"></a>Invalid AcessKey header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p9118183335110"><a name="p9118183335110"></a><a name="p9118183335110"></a>AK in the <strong id="b13200144353113"><a name="b13200144353113"></a><a name="b13200144353113"></a>Authorization</strong> field of the request header is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p2261236135110"><a name="p2261236135110"></a><a name="p2261236135110"></a>Ensure that AK is valid and correct.</p>
</td>
</tr>
<tr id="row36492771152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p4590191595113"><a name="p4590191595113"></a><a name="p4590191595113"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1241989615284"><a name="p1241989615284"></a><a name="p1241989615284"></a>DIS.4108</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1483641313321"><a name="p1483641313321"></a><a name="p1483641313321"></a>Empty ServiceName header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p38921914195315"><a name="p38921914195315"></a><a name="p38921914195315"></a>The <strong id="b114612153213"><a name="b114612153213"></a><a name="b114612153213"></a>Authorization</strong> field of the request header does not contain the service name.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1626123610515"><a name="p1626123610515"></a><a name="p1626123610515"></a>Ensure that the <strong id="b589103412302"><a name="b589103412302"></a><a name="b589103412302"></a>Authorization</strong> field of the request header contain service name <strong id="b8896223203012"><a name="b8896223203012"></a><a name="b8896223203012"></a>dis</strong>.</p>
</td>
</tr>
<tr id="row63165927152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p959081555117"><a name="p959081555117"></a><a name="p959081555117"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1680551915284"><a name="p1680551915284"></a><a name="p1680551915284"></a>DIS.4109</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p883616134325"><a name="p883616134325"></a><a name="p883616134325"></a>The Authorization header must contain the following field: {Credential,SignedHeaders,Signature;}</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p19724161711513"><a name="p19724161711513"></a><a name="p19724161711513"></a>The <strong id="b749010820329"><a name="b749010820329"></a><a name="b749010820329"></a>Authorization</strong> field of the request header is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p626436205116"><a name="p626436205116"></a><a name="p626436205116"></a>Ensure that the <strong id="b13192445123211"><a name="b13192445123211"></a><a name="b13192445123211"></a>Authorization</strong> field of the request header contains <strong id="b1915452710336"><a name="b1915452710336"></a><a name="b1915452710336"></a>Credential</strong>, <strong id="b563152911335"><a name="b563152911335"></a><a name="b563152911335"></a>SignedHeaders</strong>, and <strong id="b18769134103318"><a name="b18769134103318"></a><a name="b18769134103318"></a>Signature</strong>.</p>
</td>
</tr>
<tr id="row41313723152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p459021513511"><a name="p459021513511"></a><a name="p459021513511"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1036386515284"><a name="p1036386515284"></a><a name="p1036386515284"></a>DIS.4110</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p9836141323214"><a name="p9836141323214"></a><a name="p9836141323214"></a>Empty Signature header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p372491765110"><a name="p372491765110"></a><a name="p372491765110"></a>The <strong id="b549203715338"><a name="b549203715338"></a><a name="b549203715338"></a>Authorization</strong> field of the request header does not contain <strong id="b037315484336"><a name="b037315484336"></a><a name="b037315484336"></a>SignedHeaders</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p172763610510"><a name="p172763610510"></a><a name="p172763610510"></a>Ensure that the signature generation mode is correct.</p>
</td>
</tr>
<tr id="row59761333152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p6590915165120"><a name="p6590915165120"></a><a name="p6590915165120"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p35794926153019"><a name="p35794926153019"></a><a name="p35794926153019"></a>DIS.4111</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p38368137323"><a name="p38368137323"></a><a name="p38368137323"></a>Invalid Region header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p8312141713018"><a name="p8312141713018"></a><a name="p8312141713018"></a>The region in the <strong id="b1845416163345"><a name="b1845416163345"></a><a name="b1845416163345"></a>Authorization</strong> field of the request header is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1127336175118"><a name="p1127336175118"></a><a name="p1127336175118"></a>Ensure that the region is valid.</p>
</td>
</tr>
<tr id="row61556720152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1590715105116"><a name="p1590715105116"></a><a name="p1590715105116"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p27506390153019"><a name="p27506390153019"></a><a name="p27506390153019"></a>DIS.4112</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p58361013123214"><a name="p58361013123214"></a><a name="p58361013123214"></a>Invalid authorization request.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1189819224216"><a name="p1189819224216"></a><a name="p1189819224216"></a>The signature information generated using AK and SK is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p10253112817217"><a name="p10253112817217"></a><a name="p10253112817217"></a>Ensure that the signature generation mode and the information about AK, SK, and region are correct.</p>
</td>
</tr>
<tr id="row45377938152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p12590151516518"><a name="p12590151516518"></a><a name="p12590151516518"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p36187622153019"><a name="p36187622153019"></a><a name="p36187622153019"></a>DIS.4113</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1983661319327"><a name="p1983661319327"></a><a name="p1983661319327"></a>Empty Token header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p2725121713516"><a name="p2725121713516"></a><a name="p2725121713516"></a>When token authentication is used, the <strong id="b958361210569"><a name="b958361210569"></a><a name="b958361210569"></a>X-Auth-Token</strong> field of the request header is blank.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p192713366519"><a name="p192713366519"></a><a name="p192713366519"></a>Ensure that the <strong id="b4599336574"><a name="b4599336574"></a><a name="b4599336574"></a>X-Auth-Token</strong> field of the request header is not blank.</p>
</td>
</tr>
<tr id="row66294281152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p3590215105115"><a name="p3590215105115"></a><a name="p3590215105115"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p4360455153019"><a name="p4360455153019"></a><a name="p4360455153019"></a>DIS.4114</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1383631363214"><a name="p1383631363214"></a><a name="p1383631363214"></a>Invalid Token header.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1172518174515"><a name="p1172518174515"></a><a name="p1172518174515"></a>When token authentication is used, the <strong id="b046117815711"><a name="b046117815711"></a><a name="b046117815711"></a>X-Auth-Token</strong> field of the request header is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1727183615518"><a name="p1727183615518"></a><a name="p1727183615518"></a>Ensure that the <strong id="b122431333570"><a name="b122431333570"></a><a name="b122431333570"></a>X-Auth-Token</strong> field of the request header is valid.</p>
</td>
</tr>
<tr id="row48811534152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p95911155516"><a name="p95911155516"></a><a name="p95911155516"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p21033370153019"><a name="p21033370153019"></a><a name="p21033370153019"></a>DIS.4116</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1983631316328"><a name="p1983631316328"></a><a name="p1983631316328"></a>Invalid RBAC.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p272581718511"><a name="p272581718511"></a><a name="p272581718511"></a>User operations are restricted.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p5274368517"><a name="p5274368517"></a><a name="p5274368517"></a>Ensure that real-name authentication have been performed, all bills have been paid, and DIS operating permissions have been obtained. </p>
</td>
</tr>
<tr id="row618662299260"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p13591915155118"><a name="p13591915155118"></a><a name="p13591915155118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p451086279260"><a name="p451086279260"></a><a name="p451086279260"></a>DIS.4117</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1383617137323"><a name="p1383617137323"></a><a name="p1383617137323"></a>Invalid Project Id.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p16725817135117"><a name="p16725817135117"></a><a name="p16725817135117"></a>The project ID input by the subscriber is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p132718362515"><a name="p132718362515"></a><a name="p132718362515"></a>Ensure that the project ID is valid and correct. </p>
</td>
</tr>
<tr id="row13723935152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p4591111515116"><a name="p4591111515116"></a><a name="p4591111515116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p66768851153045"><a name="p66768851153045"></a><a name="p66768851153045"></a>DIS.4200</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p38366134320"><a name="p38366134320"></a><a name="p38366134320"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p67250172511"><a name="p67250172511"></a><a name="p67250172511"></a>The user request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p427153675115"><a name="p427153675115"></a><a name="p427153675115"></a>Check the request by referring to the API document.</p>
</td>
</tr>
<tr id="row45154952152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p9591131515511"><a name="p9591131515511"></a><a name="p9591131515511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p45832357153138"><a name="p45832357153138"></a><a name="p45832357153138"></a>DIS.4201</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1783651318326"><a name="p1783651318326"></a><a name="p1783651318326"></a>Invalid partition_id.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p57251317135114"><a name="p57251317135114"></a><a name="p57251317135114"></a>The partition ID input by the subscriber is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1127113611517"><a name="p1127113611517"></a><a name="p1127113611517"></a>Ensure that the partition ID is valid.</p>
</td>
</tr>
<tr id="row52539615152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p5591115165117"><a name="p5591115165117"></a><a name="p5591115165117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p32185013153138"><a name="p32185013153138"></a><a name="p32185013153138"></a>DIS.4202</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p18836131353214"><a name="p18836131353214"></a><a name="p18836131353214"></a>Empty request.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p183046114218"><a name="p183046114218"></a><a name="p183046114218"></a>The user request is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1627536145118"><a name="p1627536145118"></a><a name="p1627536145118"></a>Input a valid request.</p>
</td>
</tr>
<tr id="row36059775152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p165911815135112"><a name="p165911815135112"></a><a name="p165911815135112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p3300281153138"><a name="p3300281153138"></a><a name="p3300281153138"></a>DIS.4203</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p783620136320"><a name="p783620136320"></a><a name="p783620136320"></a>Invalid monitoring period.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p472541735111"><a name="p472541735111"></a><a name="p472541735111"></a>The start time for query the monitoring information is invalid. </p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p527193645112"><a name="p527193645112"></a><a name="p527193645112"></a>Input a valid timestamp.</p>
</td>
</tr>
<tr id="row63643854152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p15591415195114"><a name="p15591415195114"></a><a name="p15591415195114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p47570265153138"><a name="p47570265153138"></a><a name="p47570265153138"></a>DIS.4204</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p883611343210"><a name="p883611343210"></a><a name="p883611343210"></a>The monitoring period cannot be longer than 7 days.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p20486418237"><a name="p20486418237"></a><a name="p20486418237"></a>Only the monitoring information generated in the recent seven days can be queried.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1427113615119"><a name="p1427113615119"></a><a name="p1427113615119"></a>Query the monitoring information generated in the recent seven days.</p>
</td>
</tr>
<tr id="row5570161132213"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p105918153514"><a name="p105918153514"></a><a name="p105918153514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p18570101192212"><a name="p18570101192212"></a><a name="p18570101192212"></a>DIS.4208</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p18836181312324"><a name="p18836181312324"></a><a name="p18836181312324"></a>Invalid MRS cluster.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1259133922313"><a name="p1259133922313"></a><a name="p1259133922313"></a>The MRS cluster input during MRS dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p12271436195111"><a name="p12271436195111"></a><a name="p12271436195111"></a>Ensure the MRS cluster name and ID are correct and the cluster is running in security mode.</p>
</td>
</tr>
<tr id="row11342114517236"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p145911915155117"><a name="p145911915155117"></a><a name="p145911915155117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p634284572319"><a name="p634284572319"></a><a name="p634284572319"></a>DIS.4209</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p283616133325"><a name="p283616133325"></a><a name="p283616133325"></a>Invalid metrics label.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p67250178515"><a name="p67250178515"></a><a name="p67250178515"></a>The monitoring metric input during monitoring information query is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p8272368511"><a name="p8272368511"></a><a name="p8272368511"></a>Check and correct the monitoring metric by referring to the API document.</p>
</td>
</tr>
<tr id="row49987471152521"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p105911157519"><a name="p105911157519"></a><a name="p105911157519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p22453337152521"><a name="p22453337152521"></a><a name="p22453337152521"></a>DIS.4215</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p10836101393214"><a name="p10836101393214"></a><a name="p10836101393214"></a>Invalid cursor type.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p6725617185116"><a name="p6725617185116"></a><a name="p6725617185116"></a>The cursor type input during the data cursor acquisition is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1238835114418"><a name="p1238835114418"></a><a name="p1238835114418"></a>Check and correct the cursor type by referring to the API document.</p>
</td>
</tr>
<tr id="row31342952164954"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p16591201575119"><a name="p16591201575119"></a><a name="p16591201575119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p55751165164954"><a name="p55751165164954"></a><a name="p55751165164954"></a>DIS.4216</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p108368133327"><a name="p108368133327"></a><a name="p108368133327"></a>Invalid sequence_number.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1423841910188"><a name="p1423841910188"></a><a name="p1423841910188"></a>The sequence number input during data cursor acquisition is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p064962619184"><a name="p064962619184"></a><a name="p064962619184"></a>Input a valid sequence number.</p>
</td>
</tr>
<tr id="row60945757162118"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1159111514514"><a name="p1159111514514"></a><a name="p1159111514514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p37659255162118"><a name="p37659255162118"></a><a name="p37659255162118"></a>DIS.4217</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p8836151313323"><a name="p8836151313323"></a><a name="p8836151313323"></a>Invalid partition cursor.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p2725217175118"><a name="p2725217175118"></a><a name="p2725217175118"></a>The partition cursor input during data download from DIS is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p4275366519"><a name="p4275366519"></a><a name="p4275366519"></a>Obtain the partition cursor again and download the data.</p>
</td>
</tr>
<tr id="row1283271819421"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p10591161519514"><a name="p10591161519514"></a><a name="p10591161519514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p10832181874212"><a name="p10832181874212"></a><a name="p10832181874212"></a>DIS.4219</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p188364131328"><a name="p188364131328"></a><a name="p188364131328"></a>The file is constantly resent.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p19725117165110"><a name="p19725117165110"></a><a name="p19725117165110"></a>The file has been received.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1427536155117"><a name="p1427536155117"></a><a name="p1427536155117"></a>Do not upload the file again.</p>
</td>
</tr>
<tr id="row101774226423"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1059116152513"><a name="p1059116152513"></a><a name="p1059116152513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1117712211423"><a name="p1117712211423"></a><a name="p1117712211423"></a>DIS.4220</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p78369137325"><a name="p78369137325"></a><a name="p78369137325"></a>The block whose sequence number is %s needs to be resent.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1672531716513"><a name="p1672531716513"></a><a name="p1672531716513"></a>The file block needs to be uploaded again.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p122713616515"><a name="p122713616515"></a><a name="p122713616515"></a>Upload the corresponding file block as instructed.</p>
</td>
</tr>
<tr id="row552173112422"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p205912156511"><a name="p205912156511"></a><a name="p205912156511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1352431144215"><a name="p1352431144215"></a><a name="p1352431144215"></a>DIS.4221</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p28362013143213"><a name="p28362013143213"></a><a name="p28362013143213"></a>Block seq %s is expected.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1572581710516"><a name="p1572581710516"></a><a name="p1572581710516"></a>Duplicate file blocks are input.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p13270363516"><a name="p13270363516"></a><a name="p13270363516"></a>Upload the file block from the one expected by the system.</p>
</td>
</tr>
<tr id="row3489137194214"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p35911315125111"><a name="p35911315125111"></a><a name="p35911315125111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p10489173764215"><a name="p10489173764215"></a><a name="p10489173764215"></a>DIS.4222</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1383615131329"><a name="p1383615131329"></a><a name="p1383615131329"></a>Block seq %s is expected.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1472516175511"><a name="p1472516175511"></a><a name="p1472516175511"></a>The input file blocks are not consecutive.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p727436175117"><a name="p727436175117"></a><a name="p727436175117"></a>Upload the file block from the one expected by the system.</p>
</td>
</tr>
<tr id="row19582534104215"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p559181525119"><a name="p559181525119"></a><a name="p559181525119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p658223494219"><a name="p658223494219"></a><a name="p658223494219"></a>DIS.4223</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p083651317329"><a name="p083651317329"></a><a name="p083651317329"></a>The file size exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1072551715114"><a name="p1072551715114"></a><a name="p1072551715114"></a>The file capacity exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p12720369514"><a name="p12720369514"></a><a name="p12720369514"></a>Split the file and upload it again.</p>
</td>
</tr>
<tr id="row50489805165522"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1959131545116"><a name="p1959131545116"></a><a name="p1959131545116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p63142376165522"><a name="p63142376165522"></a><a name="p63142376165522"></a>DIS.4224</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p19836813163210"><a name="p19836813163210"></a><a name="p19836813163210"></a>The sequence number is out of range.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1374602572418"><a name="p1374602572418"></a><a name="p1374602572418"></a>The sequence number input during data cursor acquisition is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p179021033202419"><a name="p179021033202419"></a><a name="p179021033202419"></a>Input a valid sequence number.</p>
</td>
</tr>
<tr id="row51127579165551"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p105912154519"><a name="p105912154519"></a><a name="p105912154519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p47693216165551"><a name="p47693216165551"></a><a name="p47693216165551"></a>DIS.4225</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1583661318327"><a name="p1583661318327"></a><a name="p1583661318327"></a>Expired partition cursor.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p208965514236"><a name="p208965514236"></a><a name="p208965514236"></a>The partition cursor input during data download from DIS expires.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p640612202417"><a name="p640612202417"></a><a name="p640612202417"></a>Obtain the partition cursor again and download the data.</p>
</td>
</tr>
<tr id="row39407829165613"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p12591515115120"><a name="p12591515115120"></a><a name="p12591515115120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p37917582165613"><a name="p37917582165613"></a><a name="p37917582165613"></a>DIS.4226</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p2660129173512"><a name="p2660129173512"></a><a name="p2660129173512"></a>A partition iterator error occurred or a record to which the SN corresponds has expired. Try to obtain the partition iterator again.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p07261217145110"><a name="p07261217145110"></a><a name="p07261217145110"></a>The sequence number of the partition cursor input during data acquisition expires.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1428123611517"><a name="p1428123611517"></a><a name="p1428123611517"></a>Obtain the data cursor and use the new cursor to obtain data.</p>
</td>
</tr>
<tr id="row64713143152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p8591151515515"><a name="p8591151515515"></a><a name="p8591151515515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p10812303153138"><a name="p10812303153138"></a><a name="p10812303153138"></a>DIS.4300</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p78360136325"><a name="p78360136325"></a><a name="p78360136325"></a>Request error.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p872661715514"><a name="p872661715514"></a><a name="p872661715514"></a>The request body error occurs.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p22833655119"><a name="p22833655119"></a><a name="p22833655119"></a>Correct the request body by referring to the API document.</p>
</td>
</tr>
<tr id="row567170152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p3591121510516"><a name="p3591121510516"></a><a name="p3591121510516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p5328999915326"><a name="p5328999915326"></a><a name="p5328999915326"></a>DIS.4301</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1483616131323"><a name="p1483616131323"></a><a name="p1483616131323"></a>The stream does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p6930143713356"><a name="p6930143713356"></a><a name="p6930143713356"></a>The stream does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p6281636105117"><a name="p6281636105117"></a><a name="p6281636105117"></a>Ensure that the stream exists.</p>
</td>
</tr>
<tr id="row3499231152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p14591151575114"><a name="p14591151575114"></a><a name="p14591151575114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p4800090015326"><a name="p4800090015326"></a><a name="p4800090015326"></a>DIS.4302</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p9836121323212"><a name="p9836121323212"></a><a name="p9836121323212"></a>The partition does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p572671755111"><a name="p572671755111"></a><a name="p572671755111"></a>The stream partition does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p52813635118"><a name="p52813635118"></a><a name="p52813635118"></a>Ensure that the partition ID exists.</p>
</td>
</tr>
<tr id="row65065246152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p6591415145114"><a name="p6591415145114"></a><a name="p6591415145114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p2006694715326"><a name="p2006694715326"></a><a name="p2006694715326"></a>DIS.4303</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p18836181318325"><a name="p18836181318325"></a><a name="p18836181318325"></a>The traffic control limit is exceeded.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p13726717155117"><a name="p13726717155117"></a><a name="p13726717155117"></a>The flow control limit is exceeded.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1928113614515"><a name="p1928113614515"></a><a name="p1928113614515"></a>Add partitions or reduce the upload rate.</p>
</td>
</tr>
<tr id="row23230294152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p4591131545110"><a name="p4591131545110"></a><a name="p4591131545110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1886700015326"><a name="p1886700015326"></a><a name="p1886700015326"></a>DIS.4305</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p10836913173213"><a name="p10836913173213"></a><a name="p10836913173213"></a>Too many stream requests.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p13726141713518"><a name="p13726141713518"></a><a name="p13726141713518"></a>There is an excessive number of user requests at the same time.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p5287364515"><a name="p5287364515"></a><a name="p5287364515"></a>Decrease the requesting frequency and try again.</p>
</td>
</tr>
<tr id="row20484499152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p15911715175119"><a name="p15911715175119"></a><a name="p15911715175119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p3934265615326"><a name="p3934265615326"></a><a name="p3934265615326"></a>DIS.4306</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p16836151314321"><a name="p16836151314321"></a><a name="p16836151314321"></a>The bucket does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1372617171519"><a name="p1372617171519"></a><a name="p1372617171519"></a>The OBS bucket does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p13281236175118"><a name="p13281236175118"></a><a name="p13281236175118"></a>Ensure that the OBS bucket exists.</p>
</td>
</tr>
<tr id="row19018675152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p45919159517"><a name="p45919159517"></a><a name="p45919159517"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p4777867215326"><a name="p4777867215326"></a><a name="p4777867215326"></a>DIS.4307</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1583671383211"><a name="p1583671383211"></a><a name="p1583671383211"></a>The stream already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p972611171512"><a name="p972611171512"></a><a name="p972611171512"></a>The stream already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p628103675115"><a name="p628103675115"></a><a name="p628103675115"></a>Change the name of the new stream.</p>
</td>
</tr>
<tr id="row34045997152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p859171517517"><a name="p859171517517"></a><a name="p859171517517"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p15182854153240"><a name="p15182854153240"></a><a name="p15182854153240"></a>DIS.4308</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p19836171315323"><a name="p19836171315323"></a><a name="p19836171315323"></a>Insufficient quota.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p77261917105114"><a name="p77261917105114"></a><a name="p77261917105114"></a>The quotas of the streams or partitions are insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p112820363511"><a name="p112820363511"></a><a name="p112820363511"></a>Release the quota or submit a service ticketchange the quota of the account.</p>
</td>
</tr>
<tr id="row1856573152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p2591171518511"><a name="p2591171518511"></a><a name="p2591171518511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p57062171153240"><a name="p57062171153240"></a><a name="p57062171153240"></a>DIS.4309</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1183641315324"><a name="p1183641315324"></a><a name="p1183641315324"></a>Too many request failures. Please try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p12726111745119"><a name="p12726111745119"></a><a name="p12726111745119"></a>The IP address is added to the blacklist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p72853675118"><a name="p72853675118"></a><a name="p72853675118"></a>Ensure that the authentication information and request are valid and try again later.</p>
</td>
</tr>
<tr id="row40012584152749"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1359141525110"><a name="p1359141525110"></a><a name="p1359141525110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p4816976153240"><a name="p4816976153240"></a><a name="p4816976153240"></a>DIS.4310</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p483661313323"><a name="p483661313323"></a><a name="p483661313323"></a>OBS access error.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1972601718519"><a name="p1972601718519"></a><a name="p1972601718519"></a>OBS failed to be accessed.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p92833619514"><a name="p92833619514"></a><a name="p92833619514"></a>Ensure that the user has permission to access OBS.</p>
</td>
</tr>
<tr id="row5372103212101"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p10591131515110"><a name="p10591131515110"></a><a name="p10591131515110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p13372123211015"><a name="p13372123211015"></a><a name="p13372123211015"></a>DIS.4329</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p38361813183211"><a name="p38361813183211"></a><a name="p38361813183211"></a>app quota exceeded.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1372611735113"><a name="p1372611735113"></a><a name="p1372611735113"></a>The application quota exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1828133645119"><a name="p1828133645119"></a><a name="p1828133645119"></a>Release the applications that are not used.</p>
</td>
</tr>
<tr id="row113251191015"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p859114151510"><a name="p859114151510"></a><a name="p859114151510"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p183885417126"><a name="p183885417126"></a><a name="p183885417126"></a>DIS.4330</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p15836713133219"><a name="p15836713133219"></a><a name="p15836713133219"></a>app already exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1472641795112"><a name="p1472641795112"></a><a name="p1472641795112"></a>An application with the same name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p8281036175120"><a name="p8281036175120"></a><a name="p8281036175120"></a>Change the name of the new application.</p>
</td>
</tr>
<tr id="row4169174381014"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p105911015125116"><a name="p105911015125116"></a><a name="p105911015125116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1984234317129"><a name="p1984234317129"></a><a name="p1984234317129"></a>DIS.4331</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p17836131317323"><a name="p17836131317323"></a><a name="p17836131317323"></a>app is using.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p572621714512"><a name="p572621714512"></a><a name="p572621714512"></a>The application failed to be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p182823616519"><a name="p182823616519"></a><a name="p182823616519"></a>Ensure that the application that you want to delete is not being used. </p>
</td>
</tr>
<tr id="row11108193561019"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p135911515195116"><a name="p135911515195116"></a><a name="p135911515195116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p17639165133"><a name="p17639165133"></a><a name="p17639165133"></a>DIS.4332</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p12836121323217"><a name="p12836121323217"></a><a name="p12836121323217"></a>app not found.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1572612175518"><a name="p1572612175518"></a><a name="p1572612175518"></a>The specified application does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p162823635118"><a name="p162823635118"></a><a name="p162823635118"></a>Ensure the application name is correct.</p>
</td>
</tr>
<tr id="row18821353202219"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1591315165111"><a name="p1591315165111"></a><a name="p1591315165111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p20821115372214"><a name="p20821115372214"></a><a name="p20821115372214"></a>DIS.4335</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p98366138329"><a name="p98366138329"></a><a name="p98366138329"></a>Invalid IAM agency.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1572651719510"><a name="p1572651719510"></a><a name="p1572651719510"></a>The IAM agency used during dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p628183617516"><a name="p628183617516"></a><a name="p628183617516"></a>Ensure that <strong id="b061764262313"><a name="b061764262313"></a><a name="b061764262313"></a>dis_admin_agency</strong> created by DIS or the user-defined IAM agency exists and permission is complete.</p>
</td>
</tr>
<tr id="row15369131182318"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p2591131595117"><a name="p2591131595117"></a><a name="p2591131595117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p536901115238"><a name="p536901115238"></a><a name="p536901115238"></a>DIS.4336</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p183618133322"><a name="p183618133322"></a><a name="p183618133322"></a>Invalid HDFS path.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p14726201716512"><a name="p14726201716512"></a><a name="p14726201716512"></a>The MRS HDFS path input during MRS dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p11281136135115"><a name="p11281136135115"></a><a name="p11281136135115"></a>Ensure that the MRS HDFS path exists.</p>
</td>
</tr>
<tr id="row1329133772312"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1259213155512"><a name="p1259213155512"></a><a name="p1259213155512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p19291437112311"><a name="p19291437112311"></a><a name="p19291437112311"></a>DIS.4337</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1883611313326"><a name="p1883611313326"></a><a name="p1883611313326"></a>The DLI database does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p872651711512"><a name="p872651711512"></a><a name="p872651711512"></a>The DLI database input during DLI dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p8281436195115"><a name="p8281436195115"></a><a name="p8281436195115"></a>Ensure that the DLI database exists.</p>
</td>
</tr>
<tr id="row1876015507235"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p15592161555114"><a name="p15592161555114"></a><a name="p15592161555114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1676065072310"><a name="p1676065072310"></a><a name="p1676065072310"></a>DIS.4338</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p118361513143219"><a name="p118361513143219"></a><a name="p118361513143219"></a>The DLI table does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p197261417105114"><a name="p197261417105114"></a><a name="p197261417105114"></a>The DLI table input during DLI dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p6281036145114"><a name="p6281036145114"></a><a name="p6281036145114"></a>Ensure that the DLI table exists and is an internal table.</p>
</td>
</tr>
<tr id="row102584752310"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1559212155512"><a name="p1559212155512"></a><a name="p1559212155512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1825847142316"><a name="p1825847142316"></a><a name="p1825847142316"></a>DIS.4341</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p108361113143219"><a name="p108361113143219"></a><a name="p108361113143219"></a>The CloudTable cluster does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p147262172517"><a name="p147262172517"></a><a name="p147262172517"></a>The CloudTable cluster input during CloudTable dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p18281736115119"><a name="p18281736115119"></a><a name="p18281736115119"></a>Ensure that the CloudTable cluster exists and is running properly.</p>
</td>
</tr>
<tr id="row625743122319"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p459216156519"><a name="p459216156519"></a><a name="p459216156519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1325543172316"><a name="p1325543172316"></a><a name="p1325543172316"></a>DIS.4342</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1383671393210"><a name="p1383671393210"></a><a name="p1383671393210"></a>The CloudTable table does not exist</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1272661735115"><a name="p1272661735115"></a><a name="p1272661735115"></a>The CloudTable table input during CloudTable dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p20281436185116"><a name="p20281436185116"></a><a name="p20281436185116"></a>Ensure that the CloudTable table exists.</p>
</td>
</tr>
<tr id="row1366875442418"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1959218155514"><a name="p1959218155514"></a><a name="p1959218155514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p17668554192411"><a name="p17668554192411"></a><a name="p17668554192411"></a>DIS.4343</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p4836121316322"><a name="p4836121316322"></a><a name="p4836121316322"></a>The CloudTable table family does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p220112357239"><a name="p220112357239"></a><a name="p220112357239"></a>The CloudTable column family input during CloudTable dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p91503385244"><a name="p91503385244"></a><a name="p91503385244"></a>Ensure that the CloudTable column family exists.</p>
</td>
</tr>
<tr id="row25741849152414"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p8592191514511"><a name="p8592191514511"></a><a name="p8592191514511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p557414491249"><a name="p557414491249"></a><a name="p557414491249"></a>DIS.4345</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1983611131325"><a name="p1983611131325"></a><a name="p1983611131325"></a>Invalid CloudTable schema.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p762417379238"><a name="p762417379238"></a><a name="p762417379238"></a>The schema input during CloudTable dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1129143614516"><a name="p1129143614516"></a><a name="p1129143614516"></a>Check the schema based on the returned details to ensure that the configured JSON attribute name exists and the parameters are valid.</p>
</td>
</tr>
<tr id="row202326290256"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p9592715155116"><a name="p9592715155116"></a><a name="p9592715155116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1523212298256"><a name="p1523212298256"></a><a name="p1523212298256"></a>DIS.4348</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p9836513133211"><a name="p9836513133211"></a><a name="p9836513133211"></a>Invalid CloudTable openTSDB schema.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1384539112315"><a name="p1384539112315"></a><a name="p1384539112315"></a>The schema input during CloudTable OpenTSDB dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p16291336105118"><a name="p16291336105118"></a><a name="p16291336105118"></a>Check the schema based on the returned details to ensure that the JSON attribute name exists and the parameters are valid.</p>
</td>
</tr>
<tr id="row71226334257"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p9592161511518"><a name="p9592161511518"></a><a name="p9592161511518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p1512216337258"><a name="p1512216337258"></a><a name="p1512216337258"></a>DIS.4350</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p383681373212"><a name="p383681373212"></a><a name="p383681373212"></a>Invalid DWS cluster.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p15665114152318"><a name="p15665114152318"></a><a name="p15665114152318"></a>The DWS cluster input during DWS dump task creation does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p182914366515"><a name="p182914366515"></a><a name="p182914366515"></a>Ensure that the DWS cluster exists and is running properly.</p>
</td>
</tr>
<tr id="row753018181265"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p0592101513515"><a name="p0592101513515"></a><a name="p0592101513515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p11530121816260"><a name="p11530121816260"></a><a name="p11530121816260"></a>DIS.4351</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p5836181313217"><a name="p5836181313217"></a><a name="p5836181313217"></a>Invalid KMS userKey.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p4609184272310"><a name="p4609184272310"></a><a name="p4609184272310"></a>The KMS key input during DWS dump task creation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p229236155113"><a name="p229236155113"></a><a name="p229236155113"></a>Ensure that the KMS key exists.</p>
</td>
</tr>
<tr id="row1892125932717"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p159211515514"><a name="p159211515514"></a><a name="p159211515514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p592113591275"><a name="p592113591275"></a><a name="p592113591275"></a>DIS.4354</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p15836131314322"><a name="p15836131314322"></a><a name="p15836131314322"></a>The transfer task does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p127272017105115"><a name="p127272017105115"></a><a name="p127272017105115"></a>The dump task to be deleted or updated does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p1029436145113"><a name="p1029436145113"></a><a name="p1029436145113"></a>Ensure that the dump task exists.</p>
</td>
</tr>
<tr id="row1360831513265"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p959218159510"><a name="p959218159510"></a><a name="p959218159510"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p15608915102619"><a name="p15608915102619"></a><a name="p15608915102619"></a>DIS.4355</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1083615137321"><a name="p1083615137321"></a><a name="p1083615137321"></a>The transfer task already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p172731710511"><a name="p172731710511"></a><a name="p172731710511"></a>When you create a dump task in a stream, another dump task with the same name already exists in this stream.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p6292036195115"><a name="p6292036195115"></a><a name="p6292036195115"></a>Change the name of the new dump task.</p>
</td>
</tr>
<tr id="row104671312142616"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p12592181525110"><a name="p12592181525110"></a><a name="p12592181525110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p9467312192617"><a name="p9467312192617"></a><a name="p9467312192617"></a>DIS.4357</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p78361213113215"><a name="p78361213113215"></a><a name="p78361213113215"></a>Exceeded transfer task quota.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p3727417165110"><a name="p3727417165110"></a><a name="p3727417165110"></a>A maximum of five dump tasks can be created for one stream at the same time. Creating six dump tasks will exceed the quota limit.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p52943645113"><a name="p52943645113"></a><a name="p52943645113"></a>Delete the discarded dump tasks and then add dump tasks again.</p>
</td>
</tr>
<tr id="row9841482266"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p2592171513518"><a name="p2592171513518"></a><a name="p2592171513518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p108413814262"><a name="p108413814262"></a><a name="p108413814262"></a>DIS.4358</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1836113193219"><a name="p1836113193219"></a><a name="p1836113193219"></a>The stream supports specific transfer tasks. Check the data type of the stream.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p77272179511"><a name="p77272179511"></a><a name="p77272179511"></a>Common dump tasks cannot be created in the stream for small file dump.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p129143613517"><a name="p129143613517"></a><a name="p129143613517"></a>Create a new stream and then dump tasks in the stream.</p>
</td>
</tr>
<tr id="row4343622172710"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p1059221514519"><a name="p1059221514519"></a><a name="p1059221514519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p13343132217277"><a name="p13343132217277"></a><a name="p13343132217277"></a>DIS.4360</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p883661311320"><a name="p883661311320"></a><a name="p883661311320"></a>Invalid data schema.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p47271217185110"><a name="p47271217185110"></a><a name="p47271217185110"></a>The data schema input during stream creation or update is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p92953617513"><a name="p92953617513"></a><a name="p92953617513"></a>Ensure that the data schema format is correct and try again.</p>
</td>
</tr>
<tr id="row4672131393810"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p45923154515"><a name="p45923154515"></a><a name="p45923154515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p5562153520384"><a name="p5562153520384"></a><a name="p5562153520384"></a>DIS.4601</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p25621935193815"><a name="p25621935193815"></a><a name="p25621935193815"></a>The number of resource tags has reached the maximum.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p37277172512"><a name="p37277172512"></a><a name="p37277172512"></a>A resource has a maximum of 10 tags. Adding 11 tags will exceed the quota limit.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p20291736115119"><a name="p20291736115119"></a><a name="p20291736115119"></a>Delete the discarded tags and then add tags again.</p>
</td>
</tr>
<tr id="row1185962516388"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p18592201545110"><a name="p18592201545110"></a><a name="p18592201545110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p14562183563819"><a name="p14562183563819"></a><a name="p14562183563819"></a>DIS.4602</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p13562143513383"><a name="p13562143513383"></a><a name="p13562143513383"></a>Invalid resource type.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p1133220193612"><a name="p1133220193612"></a><a name="p1133220193612"></a>The resource type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p172933625115"><a name="p172933625115"></a><a name="p172933625115"></a>Ensure that the resource type is valid.</p>
</td>
</tr>
<tr id="row8687112383818"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p135921515165112"><a name="p135921515165112"></a><a name="p135921515165112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p145621835113810"><a name="p145621835113810"></a><a name="p145621835113810"></a>DIS.4603</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p5562335183813"><a name="p5562335183813"></a><a name="p5562335183813"></a>The resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p472741714513"><a name="p472741714513"></a><a name="p472741714513"></a>The resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p029173613518"><a name="p029173613518"></a><a name="p029173613518"></a>Ensure that the resource is not deleted.</p>
</td>
</tr>
<tr id="row84841121123818"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p7592171516512"><a name="p7592171516512"></a><a name="p7592171516512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p18562143510385"><a name="p18562143510385"></a><a name="p18562143510385"></a>DIS.4604</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1756263520388"><a name="p1756263520388"></a><a name="p1756263520388"></a>The key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p187271117145112"><a name="p187271117145112"></a><a name="p187271117145112"></a>The tag key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p142983635116"><a name="p142983635116"></a><a name="p142983635116"></a>Ensure that the tag key exists.</p>
</td>
</tr>
<tr id="row10265119103810"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p0592115195113"><a name="p0592115195113"></a><a name="p0592115195113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p16562635133819"><a name="p16562635133819"></a><a name="p16562635133819"></a>DIS.4605</p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p1056218352381"><a name="p1056218352381"></a><a name="p1056218352381"></a>The action is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p19727181785113"><a name="p19727181785113"></a><a name="p19727181785113"></a>The current tag operation is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p229153616511"><a name="p229153616511"></a><a name="p229153616511"></a>Ensure that the current tag operation is valid. Currently, only the create and delete operations are supported.</p>
</td>
</tr>
<tr id="row46299316102735"><td class="cellrowborder" valign="top" width="7.39073907390739%" headers="mcps1.1.6.1.1 "><p id="p559221525115"><a name="p559221525115"></a><a name="p559221525115"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="10.441044104410443%" headers="mcps1.1.6.1.2 "><p id="p59257121102735"><a name="p59257121102735"></a><a name="p59257121102735"></a>DIS.5000 to DIS.5999</p>
<p id="p101071014171513"><a name="p101071014171513"></a><a name="p101071014171513"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.44274427442744%" headers="mcps1.1.6.1.3 "><p id="p35097515102735"><a name="p35097515102735"></a><a name="p35097515102735"></a>System error.</p>
<div class="note" id="note12841201915235"><a name="note12841201915235"></a><a name="note12841201915235"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p18842019162316"><a name="p18842019162316"></a><a name="p18842019162316"></a>Contact technical support to handle system errors.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.35153515351535%" headers="mcps1.1.6.1.4 "><p id="p572712176514"><a name="p572712176514"></a><a name="p572712176514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="39.373937393739375%" headers="mcps1.1.6.1.5 "><p id="p42933625120"><a name="p42933625120"></a><a name="p42933625120"></a>-</p>
</td>
</tr>
</tbody>
</table>

