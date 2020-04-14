# Key Operations on IAM<a name="en-us_topic_0100273720"></a>

Identity and Access Management \(IAM\) enables you to centrally manage authentication information, including your authenticated email, phone number, and password. When you invoke an API to apply for an ECS, manage cloud resources, or log in to the public cloud platform in multi-tenant mode, you can query the required project ID, AK/SK, and username in real time.

With CTS, you can record operations associated with IAM for future query, audit, and backtrack operations.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>IAM is a global-level service and IAM traces are only displayed in the central region of the current site.  

**Table  1**  IAM operations that can be recorded by CTS

<a name="table56152123141211"></a>
<table><thead align="left"><tr id="r45463f2027664478912519c0654957df"><th class="cellrowborder" valign="top" width="35.35%" id="mcps1.2.4.1.1"><p id="afcfa47cfd2b34bd59b10ed0f0eae1b73"><a name="afcfa47cfd2b34bd59b10ed0f0eae1b73"></a><a name="afcfa47cfd2b34bd59b10ed0f0eae1b73"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240417_p439637141211"><a name="en-us_topic_0100240417_p439637141211"></a><a name="en-us_topic_0100240417_p439637141211"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.33%" id="mcps1.2.4.1.3"><p id="add71917243ff4bef917b13fd0f385721"><a name="add71917243ff4bef917b13fd0f385721"></a><a name="add71917243ff4bef917b13fd0f385721"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rf39ae4e38d864b10b87cfe983af70051"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p175151621635"><a name="p175151621635"></a><a name="p175151621635"></a>Creating a token</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p47965361834"><a name="p47965361834"></a><a name="p47965361834"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p143964534316"><a name="p143964534316"></a><a name="p143964534316"></a>createTokenByPwd</p>
</td>
</tr>
<tr id="rb040e93a80244e6b9be6b1c4ee3ff388"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p13515152116317"><a name="p13515152116317"></a><a name="p13515152116317"></a>Creating a token</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p117967361037"><a name="p117967361037"></a><a name="p117967361037"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1339611536311"><a name="p1339611536311"></a><a name="p1339611536311"></a>createTokenByHwAccessKey</p>
</td>
</tr>
<tr id="r729c2a01c38b41a69cf5d988ea994df4"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p95151212319"><a name="p95151212319"></a><a name="p95151212319"></a>Creating a token</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p679618361339"><a name="p679618361339"></a><a name="p679618361339"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1239615531319"><a name="p1239615531319"></a><a name="p1239615531319"></a>createTokenByToken</p>
</td>
</tr>
<tr id="r7840f8ac8161406cb292978228cad271"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p105159219319"><a name="p105159219319"></a><a name="p105159219319"></a>Creating a token</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p179623618318"><a name="p179623618318"></a><a name="p179623618318"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p173962531637"><a name="p173962531637"></a><a name="p173962531637"></a>createTokenByAssumeRole</p>
</td>
</tr>
<tr id="raf39faa465884ed0a6557c2ead831e19"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p18515821537"><a name="p18515821537"></a><a name="p18515821537"></a>Creating a token</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p5796103615318"><a name="p5796103615318"></a><a name="p5796103615318"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p0396753335"><a name="p0396753335"></a><a name="p0396753335"></a>createTokenByHwRenewToken</p>
</td>
</tr>
<tr id="rda2ddcc7c54d43ec8823b97eabf2a1eb"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p14515122113318"><a name="p14515122113318"></a><a name="p14515122113318"></a>User login</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p37961436439"><a name="p37961436439"></a><a name="p37961436439"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p439618531230"><a name="p439618531230"></a><a name="p439618531230"></a>login</p>
</td>
</tr>
<tr id="ra84512145c594039ac7a02bca37bac09"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p751520212319"><a name="p751520212319"></a><a name="p751520212319"></a>User logout</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1179633615320"><a name="p1179633615320"></a><a name="p1179633615320"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1739610531317"><a name="p1739610531317"></a><a name="p1739610531317"></a>logout</p>
</td>
</tr>
<tr id="reb713038f4ee4838888fd11e55701697"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p3515621435"><a name="p3515621435"></a><a name="p3515621435"></a>Changing a user password</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p13796536738"><a name="p13796536738"></a><a name="p13796536738"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p18396053932"><a name="p18396053932"></a><a name="p18396053932"></a>changePassword</p>
</td>
</tr>
<tr id="rf11a32b268b14d3587161ab609b4688f"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p351515214313"><a name="p351515214313"></a><a name="p351515214313"></a>Creating a user</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p279613361031"><a name="p279613361031"></a><a name="p279613361031"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13396115314310"><a name="p13396115314310"></a><a name="p13396115314310"></a>createUser</p>
</td>
</tr>
<tr id="r4c3d7bbc9a054dc1af835a0572abd532"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p5515112112319"><a name="p5515112112319"></a><a name="p5515112112319"></a>Modifying user information</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1479610361437"><a name="p1479610361437"></a><a name="p1479610361437"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p63965531833"><a name="p63965531833"></a><a name="p63965531833"></a>updateUser</p>
</td>
</tr>
<tr id="raa2f5268a30945b0aefa2a02d36543ce"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p3515102112310"><a name="p3515102112310"></a><a name="p3515102112310"></a>Deleting a user</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p147964369310"><a name="p147964369310"></a><a name="p147964369310"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p143961353337"><a name="p143961353337"></a><a name="p143961353337"></a>deleteUser</p>
</td>
</tr>
<tr id="r01f6d6289e604f58956ddf228d300a99"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1851520211839"><a name="p1851520211839"></a><a name="p1851520211839"></a>Changing a user password</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p107968361932"><a name="p107968361932"></a><a name="p107968361932"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p3396953337"><a name="p3396953337"></a><a name="p3396953337"></a>updateUserPwd</p>
</td>
</tr>
<tr id="r461cfec398d745d9b8ef53c937b716bf"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p251510211315"><a name="p251510211315"></a><a name="p251510211315"></a>Creating an AK/SK</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1479619367319"><a name="p1479619367319"></a><a name="p1479619367319"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13396125314313"><a name="p13396125314313"></a><a name="p13396125314313"></a>addCredential</p>
</td>
</tr>
<tr id="ra9bc3370cd8144578fd3b55a30aff1d4"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p135158215315"><a name="p135158215315"></a><a name="p135158215315"></a>Deleting an AK/SK</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p67965364315"><a name="p67965364315"></a><a name="p67965364315"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1939615310319"><a name="p1939615310319"></a><a name="p1939615310319"></a>deleteCredential</p>
</td>
</tr>
<tr id="r4e4a0c16b2d2462cbac7d9b86cf6f489"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p45155217316"><a name="p45155217316"></a><a name="p45155217316"></a>Changing an email address</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p137965362033"><a name="p137965362033"></a><a name="p137965362033"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1239685317317"><a name="p1239685317317"></a><a name="p1239685317317"></a>modifyUserEmail</p>
</td>
</tr>
<tr id="r3a2196c0da3e4776af684d1433b396fb"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p15515421532"><a name="p15515421532"></a><a name="p15515421532"></a>Changing a mobile phone number</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1679617361135"><a name="p1679617361135"></a><a name="p1679617361135"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p6396205314315"><a name="p6396205314315"></a><a name="p6396205314315"></a>modifyUserMobile</p>
</td>
</tr>
<tr id="r0849165c275c44a89c13074f3ba15e44"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p16515721336"><a name="p16515721336"></a><a name="p16515721336"></a>Changing a password</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p2079643612310"><a name="p2079643612310"></a><a name="p2079643612310"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p03964535317"><a name="p03964535317"></a><a name="p03964535317"></a>modifyUserPassword</p>
</td>
</tr>
<tr id="r9ecc59d49853412391c1f4893e10ad86"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p25151621136"><a name="p25151621136"></a><a name="p25151621136"></a>Enabling two-factor authentication for login</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p079633617313"><a name="p079633617313"></a><a name="p079633617313"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p193961053434"><a name="p193961053434"></a><a name="p193961053434"></a>modifySMVerify</p>
</td>
</tr>
<tr id="r08d592c0e52646869a88f5d320946612"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p115158216320"><a name="p115158216320"></a><a name="p115158216320"></a>Uploading a user picture</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p67961361136"><a name="p67961361136"></a><a name="p67961361136"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p33965530317"><a name="p33965530317"></a><a name="p33965530317"></a>modifyUserPicture</p>
</td>
</tr>
<tr id="r3ff7591a9eea4a2396d8f5b345a43617"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p115151221033"><a name="p115151221033"></a><a name="p115151221033"></a>Modifying Latch</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p87961536838"><a name="p87961536838"></a><a name="p87961536838"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p93960531732"><a name="p93960531732"></a><a name="p93960531732"></a>modifyLatchVerify</p>
</td>
</tr>
<tr id="row8145195312"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1951518211239"><a name="p1951518211239"></a><a name="p1951518211239"></a>Modifying MC</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p0796143619311"><a name="p0796143619311"></a><a name="p0796143619311"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p10396253435"><a name="p10396253435"></a><a name="p10396253435"></a>modifyMCConnectVerify</p>
</td>
</tr>
<tr id="row13144196314"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p35152211735"><a name="p35152211735"></a><a name="p35152211735"></a>Setting a user password</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p12796436430"><a name="p12796436430"></a><a name="p12796436430"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p2396453631"><a name="p2396453631"></a><a name="p2396453631"></a>setPasswordByAdmin</p>
</td>
</tr>
<tr id="row51420191834"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p18515421635"><a name="p18515421635"></a><a name="p18515421635"></a>Creating a user group</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p18796173610310"><a name="p18796173610310"></a><a name="p18796173610310"></a>userGroup</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13965539313"><a name="p13965539313"></a><a name="p13965539313"></a>createGroup</p>
</td>
</tr>
<tr id="row191481916310"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p14515221231"><a name="p14515221231"></a><a name="p14515221231"></a>Modifying a user group</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1679693617319"><a name="p1679693617319"></a><a name="p1679693617319"></a>userGroup</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p839685313314"><a name="p839685313314"></a><a name="p839685313314"></a>updateGroup</p>
</td>
</tr>
<tr id="row1014101915314"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p55157211233"><a name="p55157211233"></a><a name="p55157211233"></a>Deleting a user group</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p5796836236"><a name="p5796836236"></a><a name="p5796836236"></a>userGroup</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p183962534315"><a name="p183962534315"></a><a name="p183962534315"></a>deleteGroup</p>
</td>
</tr>
<tr id="row16141319637"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p351552119310"><a name="p351552119310"></a><a name="p351552119310"></a>Adding a user to a user group</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p67964362319"><a name="p67964362319"></a><a name="p67964362319"></a>userGroup</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p183964538316"><a name="p183964538316"></a><a name="p183964538316"></a>addUserToGroup</p>
</td>
</tr>
<tr id="row151471916310"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p15515102110314"><a name="p15515102110314"></a><a name="p15515102110314"></a>Deleting a user from a user group</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1779663619320"><a name="p1779663619320"></a><a name="p1779663619320"></a>userGroup</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1939614532314"><a name="p1939614532314"></a><a name="p1939614532314"></a>removeUserFromGroup</p>
</td>
</tr>
<tr id="row171420195318"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p45151821336"><a name="p45151821336"></a><a name="p45151821336"></a>Creating a project</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p579615361437"><a name="p579615361437"></a><a name="p579615361437"></a>project</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13396653537"><a name="p13396653537"></a><a name="p13396653537"></a>createProject</p>
</td>
</tr>
<tr id="row01417197310"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p15155211314"><a name="p15155211314"></a><a name="p15155211314"></a>Changing a project</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p12796113616316"><a name="p12796113616316"></a><a name="p12796113616316"></a>project</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1939618538316"><a name="p1939618538316"></a><a name="p1939618538316"></a>updateProject</p>
</td>
</tr>
<tr id="row51413191837"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p155152213315"><a name="p155152213315"></a><a name="p155152213315"></a>Deleting a project</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1479614361436"><a name="p1479614361436"></a><a name="p1479614361436"></a>project</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p839613531335"><a name="p839613531335"></a><a name="p839613531335"></a>deleteProject</p>
</td>
</tr>
<tr id="row151491918314"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p175151217319"><a name="p175151217319"></a><a name="p175151217319"></a>Updating the project status</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p379616366312"><a name="p379616366312"></a><a name="p379616366312"></a>project</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p9396105311319"><a name="p9396105311319"></a><a name="p9396105311319"></a>updateProjectStatus</p>
</td>
</tr>
<tr id="row1714719336"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p151592118315"><a name="p151592118315"></a><a name="p151592118315"></a>Canceling a project deletion task</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1079610361031"><a name="p1079610361031"></a><a name="p1079610361031"></a>project</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p8396145320312"><a name="p8396145320312"></a><a name="p8396145320312"></a>cancelProjectDeletion</p>
</td>
</tr>
<tr id="row161491918320"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p55159211937"><a name="p55159211937"></a><a name="p55159211937"></a>Creating an agency</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p979619361314"><a name="p979619361314"></a><a name="p979619361314"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p73964539315"><a name="p73964539315"></a><a name="p73964539315"></a>createAgency</p>
</td>
</tr>
<tr id="row514819039"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1051519212319"><a name="p1051519212319"></a><a name="p1051519212319"></a>Modifying an agency</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1879633613317"><a name="p1879633613317"></a><a name="p1879633613317"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p5396953436"><a name="p5396953436"></a><a name="p5396953436"></a>updateAgency</p>
</td>
</tr>
<tr id="row1514181914319"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p105151121136"><a name="p105151121136"></a><a name="p105151121136"></a>Deleting an agency</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p137961636734"><a name="p137961636734"></a><a name="p137961636734"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p539612531313"><a name="p539612531313"></a><a name="p539612531313"></a>deleteAgency</p>
</td>
</tr>
<tr id="row36871614330"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1151519218313"><a name="p1151519218313"></a><a name="p1151519218313"></a>Switching the role</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1796163619312"><a name="p1796163619312"></a><a name="p1796163619312"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p19396753539"><a name="p19396753539"></a><a name="p19396753539"></a>switchRole</p>
</td>
</tr>
<tr id="row16873141439"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p15150213312"><a name="p15150213312"></a><a name="p15150213312"></a>Registering an identity provider</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p779614361313"><a name="p779614361313"></a><a name="p779614361313"></a>identityProvider</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p183961532031"><a name="p183961532031"></a><a name="p183961532031"></a>createIdentityProvider</p>
</td>
</tr>
<tr id="row1468710146314"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1151514218317"><a name="p1151514218317"></a><a name="p1151514218317"></a>Modifying an identity provider</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p37963365319"><a name="p37963365319"></a><a name="p37963365319"></a>identityProvider</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p53965531135"><a name="p53965531135"></a><a name="p53965531135"></a>updateIdentityProvider</p>
</td>
</tr>
<tr id="row1968711410320"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1515152113316"><a name="p1515152113316"></a><a name="p1515152113316"></a>Deleting an identity provider</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p3796183619319"><a name="p3796183619319"></a><a name="p3796183619319"></a>identityProvider</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p639616532320"><a name="p639616532320"></a><a name="p639616532320"></a>deleteIdentityProvider</p>
</td>
</tr>
<tr id="row1468731414310"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p151532114318"><a name="p151532114318"></a><a name="p151532114318"></a>Updating IdP metadata</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p5796193613317"><a name="p5796193613317"></a><a name="p5796193613317"></a>identityProvider</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p73968531318"><a name="p73968531318"></a><a name="p73968531318"></a>updateMetaConfigure</p>
</td>
</tr>
<tr id="row568719141538"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1651514212320"><a name="p1651514212320"></a><a name="p1651514212320"></a>Updating preset IdP metadata</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p18796036932"><a name="p18796036932"></a><a name="p18796036932"></a>identityProvider</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p173961653233"><a name="p173961653233"></a><a name="p173961653233"></a>updateSystemMetaConfigure</p>
</td>
</tr>
<tr id="row12687111412315"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p15155217319"><a name="p15155217319"></a><a name="p15155217319"></a>Creating a mapping</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1479618361338"><a name="p1479618361338"></a><a name="p1479618361338"></a>mapping</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p11396115315312"><a name="p11396115315312"></a><a name="p11396115315312"></a>createMapping</p>
</td>
</tr>
<tr id="row8687014838"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p6515202117311"><a name="p6515202117311"></a><a name="p6515202117311"></a>Updating a mapping</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p197969366317"><a name="p197969366317"></a><a name="p197969366317"></a>mapping</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p163966532312"><a name="p163966532312"></a><a name="p163966532312"></a>updateMapping</p>
</td>
</tr>
<tr id="row10687201414311"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1951514211139"><a name="p1951514211139"></a><a name="p1951514211139"></a>Deleting a mapping</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p117965361133"><a name="p117965361133"></a><a name="p117965361133"></a>mapping</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p73961053334"><a name="p73961053334"></a><a name="p73961053334"></a>deleteMapping</p>
</td>
</tr>
<tr id="row126871114631"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p451517211137"><a name="p451517211137"></a><a name="p451517211137"></a>Creating a protocol</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p11796436735"><a name="p11796436735"></a><a name="p11796436735"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13962053337"><a name="p13962053337"></a><a name="p13962053337"></a>createProtocol</p>
</td>
</tr>
<tr id="row146873145315"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p2515321534"><a name="p2515321534"></a><a name="p2515321534"></a>Changing a protocol</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1779615361133"><a name="p1779615361133"></a><a name="p1779615361133"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p18396155319317"><a name="p18396155319317"></a><a name="p18396155319317"></a>updateProtocol</p>
</td>
</tr>
<tr id="row16874143312"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p551511211132"><a name="p551511211132"></a><a name="p551511211132"></a>Deleting a protocol</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p879611361835"><a name="p879611361835"></a><a name="p879611361835"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p6396253134"><a name="p6396253134"></a><a name="p6396253134"></a>deleteProtocol</p>
</td>
</tr>
<tr id="row1068716146314"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p2515172111317"><a name="p2515172111317"></a><a name="p2515172111317"></a>Granting permissions to an agency based on tenant information</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p17962363310"><a name="p17962363310"></a><a name="p17962363310"></a>roleAgencyDomain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p16396653831"><a name="p16396653831"></a><a name="p16396653831"></a>assignRoleToAgencyOnDomain</p>
</td>
</tr>
<tr id="row1468715149311"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p135155215311"><a name="p135155215311"></a><a name="p135155215311"></a>Revoking permissions from an agency based on tenant information</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p87961336433"><a name="p87961336433"></a><a name="p87961336433"></a>roleAgencyDomain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p123966531314"><a name="p123966531314"></a><a name="p123966531314"></a>unassignRoleToAgencyOnDomain</p>
</td>
</tr>
<tr id="rcfeba1661c79426db475bfb7b126a68c"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p145151921733"><a name="p145151921733"></a><a name="p145151921733"></a>Granting permissions to an agency based on project Information</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1279610361839"><a name="p1279610361839"></a><a name="p1279610361839"></a>roleAgencyProject</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p43966531316"><a name="p43966531316"></a><a name="p43966531316"></a>assignRoleToAgencyOnProject</p>
</td>
</tr>
<tr id="r428f4eb2e4684828963f0e00fd32b976"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1551520212315"><a name="p1551520212315"></a><a name="p1551520212315"></a>Deleting permissions from an agency based on project information</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1579618361531"><a name="p1579618361531"></a><a name="p1579618361531"></a>roleAgencyProject</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p93963538313"><a name="p93963538313"></a><a name="p93963538313"></a>unassignRoleToAgencyOnProject</p>
</td>
</tr>
<tr id="rab4516511b8d431184ebc3783777763e"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p3515192117320"><a name="p3515192117320"></a><a name="p3515192117320"></a>Granting permissions to a user group of a tenant</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p107961036631"><a name="p107961036631"></a><a name="p107961036631"></a>roleGroupDomain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p6396145311311"><a name="p6396145311311"></a><a name="p6396145311311"></a>assignRoleToGroupOnDomain</p>
</td>
</tr>
<tr id="r2840fa586e3b4ca7b58ed73fc248e02f"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p205151621139"><a name="p205151621139"></a><a name="p205151621139"></a>Deleting permissions of a specified user group of a tenant</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1179693611315"><a name="p1179693611315"></a><a name="p1179693611315"></a>roleGroupDomain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p143969531238"><a name="p143969531238"></a><a name="p143969531238"></a>unassignRoleToGroupOnDomain</p>
</td>
</tr>
<tr id="r2641a9dd964f4eb68cb1dfe4fff688dd"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p351512211315"><a name="p351512211315"></a><a name="p351512211315"></a>Assigning permissions to a user group corresponding to a project</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p16796153617320"><a name="p16796153617320"></a><a name="p16796153617320"></a>roleGroupProject</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p93961353238"><a name="p93961353238"></a><a name="p93961353238"></a>assignRoleToGroupOnProject</p>
</td>
</tr>
<tr id="r62216d9ab95a41cdb771b8dcf12884ad"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p951515216313"><a name="p951515216313"></a><a name="p951515216313"></a>Revoking permissions from a user group corresponding to a project</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p579616363314"><a name="p579616363314"></a><a name="p579616363314"></a>roleGroupProject</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p153964531932"><a name="p153964531932"></a><a name="p153964531932"></a>unassignRoleToGroupOnProject</p>
</td>
</tr>
<tr id="rd954e9be0a0d4d42be84f6e7442ade25"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1151514212317"><a name="p1151514212317"></a><a name="p1151514212317"></a>Modifying a security policy</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p27961536438"><a name="p27961536438"></a><a name="p27961536438"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p239615533315"><a name="p239615533315"></a><a name="p239615533315"></a>updateSecurityPolicies</p>
</td>
</tr>
<tr id="re85f1e936e9b48a78c8186ab6bb1260f"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p5515142113310"><a name="p5515142113310"></a><a name="p5515142113310"></a>Updating a password policy</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p11796173616310"><a name="p11796173616310"></a><a name="p11796173616310"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p13968531330"><a name="p13968531330"></a><a name="p13968531330"></a>updatePasswordPolicies</p>
</td>
</tr>
<tr id="re46aadcd0f3c4365919a9441a5a0371f"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p1651515213317"><a name="p1651515213317"></a><a name="p1651515213317"></a>Modifying an ACL policy</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p1579617362031"><a name="p1579617362031"></a><a name="p1579617362031"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p15396553331"><a name="p15396553331"></a><a name="p15396553331"></a>updateACLPolicies</p>
</td>
</tr>
<tr id="r430c307091fb4f95b57b49c2622b2806"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p751592111316"><a name="p751592111316"></a><a name="p751592111316"></a>Updating a security warning policy</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p57963361635"><a name="p57963361635"></a><a name="p57963361635"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p73967537317"><a name="p73967537317"></a><a name="p73967537317"></a>updateWarningPolicies</p>
</td>
</tr>
<tr id="rb4040d5eb25f4c4cbff18144226b74b4"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.2.4.1.1 "><p id="p105152213316"><a name="p105152213316"></a><a name="p105152213316"></a>Creating a domain</p>
</td>
<td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.2 "><p id="p147962361731"><a name="p147962361731"></a><a name="p147962361731"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="42.33%" headers="mcps1.2.4.1.3 "><p id="p1396153139"><a name="p1396153139"></a><a name="p1396153139"></a>createDomain</p>
</td>
</tr>
</tbody>
</table>

